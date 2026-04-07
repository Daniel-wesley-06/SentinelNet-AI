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
startup_error: str = None


@app.on_event("startup")
def load_models():
    global model_service, startup_error
    try:
        print("🔄 Starting up... Loading models...")
        model_service = ModelService()
        print("🚀 SentinelNet AI Backend ready!")
    except Exception as e:
        startup_error = str(e)
        print(f"❌ ERROR loading models: {e}")
        import traceback
        traceback.print_exc()
        # Don't re-raise - let app continue so we can debug via /health endpoint
        print("⚠️  App is running but models failed to load. Check /health endpoint.")


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
    if model_service is None:
        return {
            "status": "degraded",
            "models_loaded": False,
            "error": startup_error or "Models not loaded yet"
        }
    return {"status": "healthy", "models_loaded": True, "error": None}


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
    if model_service is None:
        raise RuntimeError(f"Models not loaded: {startup_error}")
    results = model_service.predict(sample_size=request.sample_size)
    return results
