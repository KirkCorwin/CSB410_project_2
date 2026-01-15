# Sign Language Recognition with Deep Learning

## Overview

This project investigates **deep learning approaches for classifying American Sign Language (ASL) hand signs** across 25 classes. The primary objective is to evaluate how different optimizers and regularization strategies affect model accuracy, stability, and training behavior. A secondary experiment on the MNIST dataset provides a baseline comparison against a more uniform and well-studied classification task.

All training, evaluation, and visualization logic is implemented in a single Jupyter notebook (`.ipynb`), with shared utilities and environment configuration handled at the project level.

---

## Dataset

- When running in **Google Colab**, the ASL dataset is manually uploaded via the notebook.
- When running **locally**, dataset paths should be updated to point to the local `data/` directory.

The project does not automatically download datasets in order to keep data handling explicit and transparent.

---

## Project Structure

```
project_root/
├── notebooks/
│   └── project_2.ipynb
├── src/
│   └── (helper modules and model utilities)
├── setup.sh
└── README.md
```

- `project_2.ipynb` — Contains all model definitions, training runs, evaluations, and visualizations  
- `src/` — Reusable helper functions used by the notebook  
- `setup.sh` — Shell script for creating and configuring the Conda environment  

---

## Environment Setup

This project uses a **Conda-based environment configured via `setup.sh`**.

### Setup Instructions

From the project root:

```
chmod +x setup.sh
./setup.sh
```

This script will:
- Create a Conda environment with Python 3.12
- Install all required scientific and ML dependencies
- Register the environment as a Jupyter kernel
- Configure `PYTHONPATH` so modules in `src/` are importable from notebooks

After setup, activate the environment with:

```
conda activate asl_project
```

Then launch Jupyter and select the **Python (asl_project)** kernel.

---

## Models and Optimizations

### 1. Baseline Model
- Optimizer: **Adam**
- No regularization
- Dense architecture: **512 → 256 → 25**
- Serves as a reference point for comparison

### 2. Model A — Adam + Dropout
- Dropout rate: **0.3**
- Reduces overfitting by randomly deactivating neurons
- Produced smoother and more stable validation performance than the baseline

### 3. Model B — SGD + Batch Normalization
- Batch normalization applied after each dense layer
- Stabilizes gradients and accelerates convergence
- Demonstrated the **lowest instability** across training runs

### 4. Model C — RMSProp + L2 Regularization
- L2 regularization applied to dense layers
- Penalizes overly large weights
- Exhibited noisy validation behavior, suggesting excessive regularization hindered learning

---

## Key Analyses

- **Validation Curves:** Accuracy and loss compared across all model variants  
- **Instability Metric:** Standard deviation of validation accuracy used to measure training consistency  
- **Classification Reports:** Precision, recall, and F1-score per class  
- **Misclassification Visualizations:** Side-by-side image comparisons of commonly confused signs  
- **MNIST Experiment:** Identical optimization strategies applied to MNIST for cross-dataset comparison  

---

## Findings

- Most optimization techniques improved either stability or accuracy, but no single approach resolved all classification challenges.
- **SGD + Batch Normalization** produced the most stable training behavior.
- **RMSProp + L2 regularization** was the least stable configuration, likely due to over-penalization.
- Visually similar hand shapes consistently caused misclassification across models.
- MNIST proved significantly easier to model due to lower intra-class variability.

---

## Usage

- After environment setup, all experiments can be run directly from the notebook.
- When running locally, update dataset paths to match your local directory structure.
- Helper functions in `src/` are automatically available to notebooks via the configured `PYTHONPATH`.

---

## Extra Credit

- MNIST dataset trained using the same optimization configurations
- Results compared directly against ASL model performance
- Supporting visualizations included for clarity

---

## Ethical Considerations

- Automated sign recognition systems risk flattening the expressive and contextual richness of human signing.
- Treating sign language purely as a classification task may reduce a culturally and identity-rich practice to a technical artifact.
- Any real-world deployment of such systems should be developed with careful consideration of the Deaf and Hard-of-Hearing communities they affect.

---

## Dependencies

- Python 3.12  
- TensorFlow / Keras  
- NumPy, Pandas  
- Matplotlib, Seaborn  
- Scikit-learn  

All dependencies are installed via `setup.sh`.

---

## Author

**Kirk Corwin**  
Seattle, WA  
Data Science & Computer Science Student  
