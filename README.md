# ❤️ Heart Disease Prediction using Machine Learning

An end-to-end Machine Learning project that predicts the possibility of heart disease based on patient health parameters. The project combines a trained Scikit-learn model with an interactive Streamlit web application, allowing users to enter patient details and obtain an instant prediction.

## 🚀 Live Demo

**Try the application:** [Heart Disease Prediction App](https://heart-disease-prediction-model-3p3na49xb9vkwhab7fvd7l.streamlit.app/)

**Source Code:** [GitHub Repository](https://github.com/arushparikh16-netizen/Heart-Disease-Prediction-Model)

---

## 📌 Project Overview

This project uses a supervised Machine Learning classification model to predict whether heart disease may be present based on selected clinical parameters.

The project covers the complete workflow, from data analysis and model development to saving the trained pipeline and deploying an interactive web application.

**Note:** This is an educational project and is not intended to diagnose medical conditions.

## ✨ Features

- 🩺 **Heart Disease Prediction:** Predicts whether heart disease may be present based on user-provided inputs.
- 🖥️ **Interactive Web Interface:** Built using Streamlit for a simple, user-friendly experience.
- 📋 **Patient Input Form:** Collects clinical parameters through dropdowns, number inputs, and sliders.
- 🤖 **Trained ML Pipeline:** Uses a saved Scikit-learn pipeline for predictions.
- ⚡ **Instant Results:** Displays the prediction when the user clicks the Predict button.
- 📊 **Input Summary:** Allows users to review the entered patient details.
- 🌐 **Live Deployment:** Accessible through a public Streamlit Community Cloud URL.

## 🧠 Machine Learning Approach

The project uses **Logistic Regression**, a supervised Machine Learning algorithm suitable for binary classification.

The trained model is saved as a serialized pipeline and loaded by the Streamlit application. This allows the app to make predictions without retraining the model every time it runs.

### Workflow

1. Load the heart disease dataset.
2. Explore and analyze the data.
3. Prepare the input features for Machine Learning.
4. Build and evaluate the classification model.
5. Save the trained pipeline using Joblib.
6. Load the saved pipeline in the Streamlit application.
7. Collect patient inputs and generate predictions.
8. Deploy the application using Streamlit Community Cloud.

## 📋 Input Parameters

The application collects the following 11 features:

| Feature | Description |
|---|---|
| Age | Patient's age in years |
| Sex | Patient's sex |
| ChestPainType | Type of chest pain |
| RestingBP | Resting blood pressure |
| Cholesterol | Serum cholesterol level |
| FastingBS | Whether fasting blood sugar exceeds the specified threshold |
| RestingECG | Resting electrocardiogram results |
| MaxHR | Maximum heart rate achieved |
| ExerciseAngina | Exercise-induced angina indicator |
| Oldpeak | ST depression associated with exercise |
| ST_Slope | Slope of the peak exercise ST segment |

The inputs are passed to the trained pipeline in a Pandas DataFrame using the feature names expected by the model.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Pandas** — Data manipulation and tabular data handling
- **NumPy** — Numerical computing
- **Scikit-learn** — Machine Learning model and preprocessing pipeline
- **Logistic Regression** — Classification algorithm
- **Joblib** — Saving and loading the trained model
- **Streamlit** — Interactive web application
- **Jupyter Notebook** — Data analysis and model development
- **Git and GitHub** — Version control and source code hosting
- **Streamlit Community Cloud** — Application deployment

## 📊 Model Evaluation

The model was evaluated using standard classification metrics.

| Metric | Score |
|---|---:|
| Accuracy | 88.76% |
| Precision | 89.10% |
| Recall | 90.84% |
| F1-score | 89.96% |

These scores represent the reported model evaluation results for this project. They reflect performance on the evaluation data and do not guarantee equivalent performance on new patients or real-world clinical data.

## 📂 Project Structure

```text
Heart-Disease-Prediction-Model/
│
├── app.py                       # Streamlit web application
├── HeartDetection.ipynb          # Model development and analysis
├── heart.csv                    # Dataset
├── heart_disease_pipeline.pkl    # Saved ML pipeline
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .vscode/
    └── settings.json             # VS Code settings
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/arushparikh16-netizen/Heart-Disease-Prediction-Model.git
```

### 2. Navigate to the project directory

```bash
cd Heart-Disease-Prediction-Model
```

### 3. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, visit:

```text
http://localhost:8501
```

## 📦 Dependencies

The project uses the following Python libraries:

```text
streamlit
pandas
scikit-learn
joblib
numpy
```

Install them together using the provided `requirements.txt` file.

## 💻 How to Use the Application

1. Open the [live application](https://heart-disease-prediction-model-3p3na49xb9vkwhab7fvd7l.streamlit.app/).
2. Enter the patient's clinical details using the available input controls.
3. Click the **Predict** button.
4. View the prediction displayed by the Machine Learning model.
5. Expand the patient input details section to review the submitted values.

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud** and connected to the GitHub repository.

The deployment uses `app.py` as the main application file and installs the required Python dependencies from `requirements.txt`.

- **Live application:** [Open the app](https://heart-disease-prediction-model-3p3na49xb9vkwhab7fvd7l.streamlit.app/)
- **GitHub repository:** [View the source code](https://github.com/arushparikh16-netizen/Heart-Disease-Prediction-Model)

## ⚠️ Limitations and Disclaimer

- This project is developed for educational and portfolio purposes.
- Model predictions are based on patterns learned from the training dataset.
- Performance may vary on data from different populations or healthcare settings.
- The model has not been established as a clinically validated diagnostic system.
- A positive or negative prediction must not be treated as a medical diagnosis.
- Always consult a qualified healthcare professional for medical advice, diagnosis, or treatment.

## 🔮 Future Improvements

Potential improvements include:

- Compare Logistic Regression with Random Forest, Support Vector Machine, and other classifiers.
- Perform cross-validation and systematic hyperparameter tuning.
- Add visualizations for model performance and feature relationships.
- Improve model interpretability using appropriate explainability techniques.
- Add automated input validation and more informative error handling.
- Evaluate generalization on independent datasets.
- Improve the application's accessibility and user experience.

## 🎯 Learning Outcomes

Through this project, I explored:

- Data analysis and preparation for Machine Learning.
- Supervised learning and binary classification.
- Logistic Regression and classification evaluation metrics.
- Saving and loading trained pipelines using Joblib.
- Connecting a trained model to a Streamlit interface.
- Deploying a Machine Learning application publicly.
- Managing and documenting a project using Git and GitHub.

## 👨‍💻 Author

**Arush Parikh**

GitHub: [@arushparikh16-netizen](https://github.com/arushparikh16-netizen)

---

⭐ If you find this project useful, consider giving the repository a star!

