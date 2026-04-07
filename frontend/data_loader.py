import pandas as pd
import requests

# Backend API URL
BACKEND_URL = "http://localhost:8000"


def call_backend_api(sample_size: int = 2000) -> tuple[pd.DataFrame, dict]:
    """
    Call the FastAPI backend to get real ensemble predictions.

    Returns:
        (results_df, metrics_dict)
    """
    response = requests.post(
        f"{BACKEND_URL}/predict",
        json={"sample_size": sample_size},
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()

    # Convert sample_data list-of-dicts back to DataFrame
    results_df = pd.DataFrame(data["sample_data"])
    metrics = data["metrics"]

    return results_df, metrics


def check_backend_health() -> bool:
    """Check if the backend API is running."""
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=3)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
