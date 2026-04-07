import json
import numpy as np
import pandas as pd
import joblib
from pathlib import Path
import os


class ModelService:
    """
    Loads pre-trained models and serves ensemble predictions.

    Pipeline:
        1. Load CSV → sample N rows
        2. Apply preprocessing pipeline (OneHotEncoder + StandardScaler)
        3. Predict with Isolation Forest → binary labels
        4. Predict with One-Class SVM → binary labels
        5. Weighted voting ensemble → final predictions
        6. Compute metrics vs true labels
    """

    def __init__(self):
        print(f"🔍 Current working directory: {os.getcwd()}")
        print(f"🔍 Model service file location: {Path(__file__).resolve()}")
        
        base_dir = Path(__file__).resolve().parent
        models_dir = base_dir / "models"
        config_dir = base_dir / "config"
        data_dir = base_dir.parent / "data"

        print(f"🔍 Resolved paths:")
        print(f"   base_dir: {base_dir}")
        print(f"   models_dir: {models_dir}")
        print(f"   config_dir: {config_dir}")
        print(f"   data_dir: {data_dir}")
        print(f"🔍 Directory existence:")
        print(f"   {models_dir}: {models_dir.exists()}")
        print(f"   {config_dir}: {config_dir.exists()}")
        print(f"   {data_dir}: {data_dir.exists()}")
        
        if models_dir.exists():
            print(f"   Contents of {models_dir}: {list(models_dir.iterdir())}")
        if data_dir.exists():
            print(f"   Contents of {data_dir}: {list(data_dir.iterdir())}")

        # Load models with error handling
        try:
            self.pipeline = joblib.load(models_dir / "preprocessing_pipeline_final.joblib")
            print(f"✅ Loaded preprocessing pipeline")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Preprocessing pipeline not found: {e}")

        try:
            self.iforest = joblib.load(models_dir / "isolation_forest_final.joblib")
            print(f"✅ Loaded isolation forest model")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Isolation forest model not found: {e}")

        try:
            self.svm = joblib.load(models_dir / "oneclass_svm_final.joblib")
            print(f"✅ Loaded SVM model")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"SVM model not found: {e}")

        # Load ensemble config
        config_file = config_dir / "ensemble_config.json"
        if not config_file.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")

        with open(config_file, "r") as f:
            self.config = json.load(f)

        self.weights = self.config["weights"]
        self.threshold = self.config["threshold"]

        # Load dataset
        data_file = data_dir / "synthetic_ctgan_data.csv"
        if not data_file.exists():
            raise FileNotFoundError(f"Data file not found: {data_file}")

        self.full_df = pd.read_csv(data_file)

        print(f"✅ Models loaded successfully.")
        print(f"   Dataset: {len(self.full_df)} rows")
        print(f"   Ensemble: IF={self.weights['isolation_forest']}, SVM={self.weights['oneclass_svm']}, threshold={self.threshold}")

    def _convert_sklearn_to_binary(self, predictions: np.ndarray) -> np.ndarray:
        """
        Convert sklearn anomaly detection output to binary labels.
        sklearn: 1 = normal (inlier), -1 = anomaly (attack)
        Our convention: 1 = attack, 0 = normal
        """
        return (predictions == -1).astype(int)

    def predict(self, sample_size: int = 2000) -> dict:
        """
        Run the full ensemble prediction pipeline.

        Returns dict with:
            - metrics: accuracy, recalls, confusion matrix, counts
            - sample_data: list of dicts with features + predictions
            - individual_predictions: IF and SVM individual results
        """
        # 1. Sample data
        n = min(sample_size, len(self.full_df))
        sampled_df = self.full_df.sample(n=n).reset_index(drop=True)

        true_labels = sampled_df["label"].values
        features = sampled_df.drop("label", axis=1)

        # 2. Preprocess
        X_transformed = self.pipeline.transform(features)

        # 3. Individual model predictions (sklearn: 1=normal, -1=anomaly)
        if_raw = self.iforest.predict(X_transformed)
        svm_raw = self.svm.predict(X_transformed)

        # 4. Convert to our binary convention (1=attack, 0=normal)
        if_binary = self._convert_sklearn_to_binary(if_raw)
        svm_binary = self._convert_sklearn_to_binary(svm_raw)

        # 5. Weighted voting ensemble
        w_if = self.weights["isolation_forest"]
        w_svm = self.weights["oneclass_svm"]
        ensemble_score = w_if * if_binary + w_svm * svm_binary
        ensemble_pred = (ensemble_score >= self.threshold).astype(int)

        # 6. Compute metrics
        tp = int(np.sum((true_labels == 1) & (ensemble_pred == 1)))
        fp = int(np.sum((true_labels == 0) & (ensemble_pred == 1)))
        fn = int(np.sum((true_labels == 1) & (ensemble_pred == 0)))
        tn = int(np.sum((true_labels == 0) & (ensemble_pred == 0)))

        total = tp + fp + fn + tn
        accuracy = round((tp + tn) / total * 100, 1) if total > 0 else 0
        attack_recall = round(tp / (tp + fn) * 100, 1) if (tp + fn) > 0 else 0
        normal_recall = round(tn / (tn + fp) * 100, 1) if (tn + fp) > 0 else 0

        metrics = {
            "accuracy": accuracy,
            "attack_recall": attack_recall,
            "normal_recall": normal_recall,
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "tn": tn,
            "total_samples": n,
            "attack_count": int(np.sum(ensemble_pred == 1)),
            "normal_count": int(np.sum(ensemble_pred == 0)),
        }

        # 7. Build sample data for frontend
        result_df = sampled_df.copy()
        result_df["prediction"] = ensemble_pred
        result_df["prediction_label"] = result_df["prediction"].map({0: "Normal", 1: "Attack"})
        result_df["true_label"] = result_df["label"].map({0: "Normal", 1: "Attack"})
        result_df["if_prediction"] = if_binary
        result_df["svm_prediction"] = svm_binary
        result_df["ensemble_score"] = np.round(ensemble_score, 2)

        # Convert to list of dicts for JSON serialization
        sample_data = result_df.to_dict(orient="records")

        return {
            "metrics": metrics,
            "sample_data": sample_data,
        }
