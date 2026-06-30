# 🛡️ SentinelNet — Hybrid Intrusion Detection using Machine Learning, CTGAN & Ensemble Learning

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=for-the-badge&logo=numpy)

</p>

---

# 📌 Project Overview

SentinelNet is an **end-to-end Machine Learning Intrusion Detection System (IDS)** designed to identify malicious network activities using both **supervised** and **unsupervised** learning techniques.

Unlike conventional IDS solutions that rely on a single machine learning model, SentinelNet adopts a **hybrid approach**, combining **classification**, **anomaly detection**, **synthetic data generation**, and **ensemble learning** to improve the detection of both known and previously unseen cyber threats.

The project was developed as part of an **Infosys Virtual Internship** and demonstrates the complete machine learning lifecycle—from raw network traffic preprocessing to deployment as a real-time web application.

---

# 🎯 Problem Statement

Traditional Intrusion Detection Systems are effective at recognizing **known attack signatures**, but often fail when confronted with **zero-day attacks** or previously unseen network behaviors.

The objective of SentinelNet is to bridge this gap by integrating:

- Supervised Learning for known attack classification
- Unsupervised Learning for anomaly detection
- CTGAN-based synthetic data generation to improve learning from imbalanced data
- Ensemble Learning to improve anomaly detection robustness
- A deployable API-driven prediction system for real-time inference

---

# ✨ Key Features

## 🤖 Machine Learning

- Supervised Intrusion Detection using Random Forest
- Unsupervised Anomaly Detection using Isolation Forest
- One-Class SVM for anomaly learning
- Weighted Ensemble Learning
- Hyperparameter Optimization
- Threshold Tuning
- Model Persistence using Joblib

---

## 📊 Data Engineering

- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Feature Scaling
- Feature Engineering
- Feature Selection
- Large-scale preprocessing pipeline

---

## 🧠 Synthetic Data Generation

SentinelNet incorporates **CTGAN (Conditional Tabular GAN)** to generate synthetic attack samples for improving model learning on imbalanced cybersecurity datasets.

Instead of relying solely on original training samples, CTGAN learns the distribution of minority attack classes and generates realistic synthetic network traffic, enabling better anomaly detection performance.

---

## 🌐 Deployment

- FastAPI REST Backend
- Streamlit Interactive Frontend
- Real-Time Prediction Pipeline
- Joblib Model Loading
- API-based Architecture

---

# 🚀 Technologies Used

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Data Augmentation | CTGAN |
| Deployment | FastAPI, Streamlit |
| Model Storage | Joblib |
| Datasets | CICIDS2017, NSL-KDD |

---

# 🏗️ System Architecture

```
                    +----------------------+
                    |     User Input       |
                    +----------+-----------+
                               |
                               |
                      Streamlit Frontend
                               |
                               |
                               ▼
                     FastAPI REST Backend
                               |
               +---------------+---------------+
               |                               |
               |                               |
               ▼                               ▼
     Supervised Pipeline              Unsupervised Pipeline
       (CICIDS2017)                     (NSL-KDD)

   Random Forest Model          Isolation Forest
                                        +
                               One-Class SVM
                                        +
                             Weighted Ensemble
               |                               |
               +---------------+---------------+
                               |
                               ▼
                      Intrusion Prediction
                               |
                               ▼
                      Results Dashboard
```


# 📂 Project Structure

```text
SentinelNet
│
├── 📁 backend
│   ├── 📁 config
│   │   └── ensemble_config.json
│   │
│   ├── 📁 models
│   │   ├── isolation_forest_final.joblib
│   │   ├── oneclass_svm_final.joblib
│   │   └── preprocessing_pipeline_final.joblib
│   │
│   ├── main.py
│   └── model_service.py
│
├── 📁 frontend
│   ├── 📁 components
│   ├── 📁 styles
│   ├── app.py
│   └── data_loader.py
│
├── 📁 data
│   └── Dataset files used for training and testing
│
├── SentinelNet_CICDS.ipynb
├── SentinelNet_NSL_KDD.ipynb
├── requirements.txt
└── README.md
```

---

## 📁 Directory Description

| Directory/File | Purpose |
|----------------|---------|
| **backend/** | FastAPI backend responsible for serving machine learning predictions. |
| **backend/config/** | Configuration files used by the ensemble prediction pipeline. |
| **backend/models/** | Stores trained machine learning models and preprocessing pipeline serialized using Joblib. |
| **main.py** | Entry point of the FastAPI application exposing prediction APIs. |
| **model_service.py** | Handles model loading, preprocessing, inference, and ensemble prediction logic. |
| **frontend/** | Streamlit web application providing an interactive interface for users. |
| **frontend/components/** | Reusable UI components used throughout the application. |
| **frontend/styles/** | Custom styling and visual enhancements for the frontend. |
| **app.py** | Main Streamlit application. |
| **data_loader.py** | Loads datasets and prepares inputs for prediction. |
| **data/** | Contains the datasets used during model training and evaluation. |
| **SentinelNet_CICDS.ipynb** | Notebook containing the complete supervised learning pipeline using the CICIDS2017 dataset. |
| **SentinelNet_NSL_KDD.ipynb** | Notebook containing the complete unsupervised learning pipeline using the NSL-KDD dataset, including CTGAN and weighted ensemble learning. |
| **requirements.txt** | Lists all Python dependencies required to run the project. |

#  Project Objectives

- Detect both known and unknown cyber attacks using a hybrid ML approach.
- Improve anomaly detection using CTGAN-generated synthetic data.
- Enhance prediction robustness through weighted ensemble learning.
- Deploy the complete solution as a real-time web application using FastAPI and Streamlit.

# 📊 Datasets

SentinelNet leverages two benchmark intrusion detection datasets to evaluate both **supervised** and **unsupervised** machine learning techniques. Each dataset was selected to address a different aspect of intrusion detection, enabling the system to identify both **known** and **previously unseen** cyber threats.

| Dataset | Learning Type | Purpose |
|----------|---------------|---------|
| **CICIDS2017** | Supervised Learning | Multi-class network attack classification |
| **NSL-KDD** | Unsupervised Learning | Anomaly detection for unknown attacks |

---

## 📌 CICIDS2017

The CICIDS2017 dataset contains modern network traffic captured under realistic conditions, including both benign traffic and multiple categories of cyber attacks. It provides rich flow-based features that make it suitable for supervised classification tasks.

**Used for:**

- Supervised Machine Learning
- Multi-class attack classification
- Model training and evaluation
- Performance benchmarking

---

## 📌 NSL-KDD

NSL-KDD is an improved version of the KDD'99 dataset with redundant records removed, making it more suitable for machine learning research.

Instead of learning attack labels directly, SentinelNet utilizes this dataset to detect **anomalous network behavior**, allowing the system to identify attacks that differ significantly from normal traffic.

**Used for:**

- Unsupervised Learning
- Anomaly Detection
- Ensemble Learning
- Synthetic Data Generation

---

# ⚙️ End-to-End Machine Learning Pipeline

The complete workflow followed by SentinelNet is illustrated below.

```text
          Raw Network Traffic
                    │
                    ▼
          Data Cleaning & Validation
                    │
                    ▼
        Missing Value Handling
                    │
                    ▼
     Encoding & Feature Scaling
                    │
                    ▼
        Feature Engineering
                    │
                    ▼
         Dataset Preparation
             │           │
             │           │
             ▼           ▼
      CICIDS2017      NSL-KDD
             │           │
             ▼           ▼
      Random Forest   Isolation Forest
                          │
                          ▼
                   One-Class SVM
                          │
                          ▼
             CTGAN Data Augmentation
                          │
                          ▼
             Weighted Ensemble Model
                          │
                          ▼
             Intrusion Prediction
```

---

# ⚙️ Data Preprocessing

Before model training, both datasets underwent a comprehensive preprocessing pipeline to ensure data quality and consistency.

The preprocessing steps included:

- Handling missing and invalid values
- Encoding categorical features
- Feature scaling using **StandardScaler**
- Removal of inconsistent records
- Train-test splitting
- Data validation before model training

These steps improved model stability while ensuring that both datasets were transformed into a machine-learning-ready format.

---

# 🧠 Feature Engineering

Feature engineering was performed to maximize the predictive capability of the machine learning models.

The pipeline included:

- Categorical feature encoding
- Numerical feature normalization
- Feature importance analysis
- Removal of redundant features
- Consistent preprocessing pipeline for deployment

Rather than relying solely on raw network traffic attributes, engineered features enabled the models to better distinguish between normal and malicious traffic patterns.

---

# 🤖 Machine Learning Methodology

Instead of relying on a single machine learning algorithm, SentinelNet adopts a hybrid methodology by combining supervised classification, anomaly detection, synthetic data generation, and ensemble learning.

This layered approach improves both detection accuracy and robustness against unseen cyber threats.

---

## 🌳 Random Forest (Supervised Learning)

The Random Forest classifier was trained on the **CICIDS2017** dataset to classify network traffic into attack categories.

It was selected because it:

- Handles high-dimensional data effectively
- Is resistant to overfitting
- Provides feature importance scores
- Delivers excellent classification accuracy

The optimized model achieved an accuracy of **99.98%**.

---

## 🌲 Isolation Forest (Unsupervised Learning)

Isolation Forest was used to identify anomalous network traffic by isolating observations that differ significantly from normal behavior.

Unlike supervised models, it does not require labeled attack data, making it suitable for detecting previously unseen attacks.

---

## 🎯 One-Class SVM

One-Class SVM complements Isolation Forest by learning the boundary of normal network traffic.

Any observation falling outside this learned boundary is considered anomalous.

Combining both algorithms provides stronger anomaly detection than using either model independently.

---

# 🧬 CTGAN-Based Synthetic Data Generation

Real-world intrusion detection datasets are often highly imbalanced, with significantly fewer attack samples than normal traffic.

To address this challenge, SentinelNet integrates **Conditional Tabular GAN (CTGAN)** to generate realistic synthetic network traffic for minority attack classes.

Benefits of using CTGAN include:

- Improved representation of minority attack classes
- Reduced class imbalance
- Better generalization
- Enhanced anomaly detection performance

Instead of simply duplicating existing records, CTGAN learns the underlying distribution of the data and generates entirely new synthetic samples that closely resemble real network traffic.

---

# ⚖️ Weighted Ensemble Learning

Rather than relying on a single anomaly detection algorithm, SentinelNet combines multiple unsupervised models using a **Weighted Ensemble Learning** approach.

The final anomaly score is computed by assigning different weights to individual model predictions, allowing stronger models to contribute more significantly to the final decision.

### Ensemble Components

- Isolation Forest
- One-Class SVM

This strategy improves:

- Prediction robustness
- Generalization capability
- Stability across unseen network traffic
- Overall anomaly detection accuracy

The final weighted ensemble achieved **86.67% accuracy** on the CTGAN-augmented dataset, outperforming the individual anomaly detection models.

# 📈 Model Performance & Results

SentinelNet was evaluated using both **supervised** and **unsupervised** machine learning techniques to assess its effectiveness in detecting malicious network traffic. Standard evaluation metrics such as **Accuracy, Precision, Recall, F1-Score**, and **Confusion Matrix** were used to measure model performance.

---

## 🏆 Supervised Learning Results (CICIDS2017)

The Random Forest classifier demonstrated excellent performance in classifying network traffic into benign and attack categories.

| Metric | Value |
|---------|-------|
| Accuracy | **99.98%** |
| Precision | **≈99%** |
| Recall | **≈99%** |
| F1-Score | **≈99%** |

### Key Takeaways

- Excellent classification performance
- High precision with minimal false positives
- Strong generalization on unseen network traffic
- Suitable for real-time intrusion detection

---

## 🛡️ Unsupervised Learning Results (NSL-KDD)

For anomaly detection, SentinelNet combined **Isolation Forest** and **One-Class SVM** using a **Weighted Ensemble Learning** approach.

To improve learning from minority attack classes, **CTGAN** was used to generate realistic synthetic network traffic before model training.

### Final Pipeline

```text
NSL-KDD Dataset
        │
        ▼
 Data Preprocessing
        │
        ▼
 Feature Engineering
        │
        ▼
 CTGAN Synthetic Data Generation
        │
        ▼
 Isolation Forest
        │
        ├─────────────┐
        ▼             │
   One-Class SVM      │
        │             │
        └──────┬──────┘
               ▼
     Weighted Ensemble
               ▼
    Final Intrusion Prediction
```

### Weighted Ensemble Performance

| Metric | Value |
|---------|-------|
| Accuracy | **86.67%** |
| Precision | **91%** |
| Recall | **72%** |
| F1-Score | **81%** |

### Why Ensemble Learning?

Instead of relying on a single anomaly detection model, the weighted ensemble combines predictions from multiple algorithms, making the system more robust against unknown attack patterns while reducing model-specific bias.

---

# 🌐 Deployment Architecture

SentinelNet was designed as a production-style machine learning application by separating the frontend, backend, and inference layers.

```text
                 User
                  │
                  ▼
        Streamlit Frontend
                  │
                  ▼
          FastAPI Backend
                  │
                  ▼
      Preprocessing Pipeline
                  │
          ┌───────┴────────┐
          ▼                ▼
 Random Forest      Weighted Ensemble
    (CICIDS)          (NSL-KDD)
          │                │
          └───────┬────────┘
                  ▼
         Intrusion Prediction
                  │
                  ▼
      Interactive Results Dashboard
```

---

# 🚀 Getting Started

## Prerequisites

- Python 3.10+
- Git
- pip

---

## Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/SentinelNet.git
```

Navigate to the project directory.

```bash
cd SentinelNet
```

Install all dependencies.

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Backend

Start the FastAPI server.

```bash
cd backend

uvicorn main:app --reload
```

The backend will be available at:

```
http://127.0.0.1:8000
```

Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🎨 Running the Frontend

Open a new terminal.

```bash
cd frontend

streamlit run app.py
```

The Streamlit application will launch in your browser.


# 💡 Future Improvements

Although SentinelNet demonstrates strong performance, several enhancements can further improve the system.

- Real-time packet capture using Wireshark or Scapy
- Online learning for continuous model updates
- Explainable AI using SHAP/LIME
- Docker containerization
- Kubernetes deployment
- Cloud deployment on AWS/Azure/GCP
- CI/CD integration using GitHub Actions
- Monitoring using Prometheus and Grafana
- Deep Learning-based intrusion detection
- Automated threat alerting

---

# 📊 Project Summary

| Component | Implementation |
|------------|----------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Supervised Learning | Random Forest |
| Unsupervised Learning | Isolation Forest, One-Class SVM |
| Synthetic Data | CTGAN |
| Ensemble Learning | Weighted Ensemble |
| Backend | FastAPI |
| Frontend | Streamlit |
| Deployment | API + Web Interface |
| Best Supervised Accuracy | **99.98%** |
| Best Ensemble Accuracy | **86.67%** |

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Programming Language** | Python |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Data Augmentation** | CTGAN |
| **Supervised Learning** | Random Forest |
| **Unsupervised Learning** | Isolation Forest, One-Class SVM |
| **Ensemble Learning** | Weighted Ensemble |
| **Model Serialization** | Joblib |
| **Backend Framework** | FastAPI |
| **Frontend Framework** | Streamlit |
| **Version Control** | Git & GitHub |

---

# 💼 Skills Demonstrated

This project showcases practical experience across the complete Machine Learning lifecycle, including:

### 📊 Data Science
- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Handling Imbalanced Datasets
- Synthetic Data Generation using CTGAN
- Statistical Model Evaluation

### 🤖 Machine Learning
- Supervised Learning
- Unsupervised Learning
- Ensemble Learning
- Hyperparameter Tuning
- Model Optimization
- Model Serialization & Inference

### 🛡️ Cybersecurity
- Intrusion Detection Systems (IDS)
- Network Traffic Analysis
- Anomaly Detection
- Cyber Attack Classification
- Threat Detection

### 🚀 MLOps & Deployment
- FastAPI Model Serving
- Streamlit Web Application
- API Development
- End-to-End ML Pipeline
- Real-Time Prediction
- Production-Oriented Project Structure

---

# 🎯 Key Achievements

- ✅ Developed a hybrid Intrusion Detection System combining supervised and unsupervised learning.
- ✅ Achieved **99.98% accuracy** on the CICIDS2017 dataset using an optimized Random Forest model.
- ✅ Improved anomaly detection performance using **CTGAN-generated synthetic data** and a **Weighted Ensemble Learning** approach, achieving **86.67% accuracy**.
- ✅ Designed and deployed a production-style machine learning application using **FastAPI** and **Streamlit**.
- ✅ Built a modular architecture that separates data processing, model inference, API services, and frontend components.

---

# 🔮 Future Enhancements

The current implementation provides a strong foundation for intrusion detection. Future improvements may include:

- Integration with live network traffic using packet capture tools such as Scapy.
- Explainable AI (XAI) using SHAP or LIME for model interpretability.
- Deep learning architectures such as Autoencoders and LSTMs for advanced anomaly detection.
- Containerization using Docker and orchestration with Kubernetes.
- Cloud deployment on AWS, Azure, or Google Cloud Platform.
- CI/CD pipeline for automated testing and deployment.
- Real-time monitoring and alerting using Prometheus and Grafana.

---

# 🙏 Acknowledgements

This project was developed as part of the **Infosys Virtual Internship**, with the objective of applying Machine Learning techniques to solve real-world cybersecurity problems.

Special thanks to:

- The University of New Brunswick for providing the **CICIDS2017** and **NSL-KDD** datasets.
- The open-source communities behind **Scikit-learn**, **FastAPI**, **Streamlit**, and **CTGAN** for providing the tools and libraries used throughout this project.

---

# 📜 License

This project is licensed under the **MIT License**.

You are welcome to use, modify, and distribute this project for educational and research purposes while providing appropriate attribution.

---

# 👨‍💻 Author

**Daniel Wesley**

Computer Science & Engineering Student

Interested in:
- Machine Learning
- Data Science
- Artificial Intelligence
- Cybersecurity
- MLOps

---

# 🤝 Connect With Me

If you found this project interesting or would like to collaborate, feel free to connect.

- 💼 Gmail: danielwesleybtech2023@gmail.com
- 💻 GitHub: https://github.com/Daniel-wesley-06

---

<p align="center">

###  If you found this project useful, consider giving it a star!

**SentinelNet — Hybrid Intrusion Detection using Machine Learning, CTGAN & Ensemble Learning**

Built with ❤️ using Python, Machine Learning, and Cybersecurity.

</p>
