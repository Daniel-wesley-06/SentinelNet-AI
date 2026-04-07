import sys
from pathlib import Path

# Ensure backend directory is on the path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from model_service import ModelService


# ─── App Setup ───
app = FastAPI(
    title="SentinelNet AI — Backend",
    description="Network Intrusion Detection API using Ensemble (IF + SVM)",
    version="1.0.0",
)

# Allow Streamlit frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Load models at startup ───
model_service: ModelService = None


@app.on_event("startup")
def load_models():
    global model_service
    try:
        model_service = ModelService()
        print("🚀 SentinelNet AI Backend ready!")
    except Exception as e:
        print(f"❌ ERROR loading models: {e}")
        import traceback
        traceback.print_exc()
        raise  # Re-raise so we know there's an issue


# ─── Request/Response Models ───
class PredictRequest(BaseModel):
    sample_size: int = Field(default=2000, ge=100, le=5000, description="Number of samples to analyze")


class MetricsResponse(BaseModel):
    accuracy: float
    attack_recall: float
    normal_recall: float
    tp: int
    fp: int
    fn: int
    tn: int
    total_samples: int
    attack_count: int
    normal_count: int


class PredictResponse(BaseModel):
    metrics: MetricsResponse
    sample_data: list[dict]


# ─── Endpoints ───
@app.get("/")
def root():
    return {
        "service": "SentinelNet AI Backend",
        "status": "running",
        "models": ["isolation_forest", "oneclass_svm"],
        "ensemble": "weighted_voting",
    }


@app.get("/health")
def health():
    return {"status": "healthy", "models_loaded": model_service is not None}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    """
    Run ensemble intrusion detection on sampled data.

    1. Randomly samples `sample_size` rows from the 20k dataset
    2. Applies preprocessing pipeline
    3. Runs Isolation Forest + One-Class SVM
    4. Combines via weighted voting
    5. Returns predictions + metrics
    """
    results = model_service.predict(sample_size=request.sample_size)
    return results
