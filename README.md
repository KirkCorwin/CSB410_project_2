# Sign Language Recognition with Deep Learning

## Overview

This project investigates **deep learning methods for classifying American Sign Language (ASL) hand signs** across 25 classes. The primary goal was to compare how different optimizers and regularization techniques affect accuracy, stability, and overall model behavior. A secondary experiment on MNIST provides a baseline reference against a more uniform dataset.

All code, training runs, and visualizations are contained in the Jupyter notebook (`.ipynb`).

---

## Dataset

- The ASL dataset is **manually uploaded** when running in Google Colab.  
- When running locally, update the dataset path to your `data/` directory.

---

## Project Structure

- `project_2.ipynb` — notebook containing all training code, evaluation steps, and visualizations  
- `requirements.yaml` — Environment specification for consistent reproduction  

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
- Produced smoother and more stable validation performance compared to the baseline

### 3. Model B — SGD + Batch Normalization
- Batch normalization added after each dense layer  
- Normalizes activations to stabilize and speed up training  
- Showed the **lowest instability** (most consistent learning)

### 4. Model C — RMSProp + L2 Regularization
- L2 regularization applied to dense layers  
- Intended to penalize overly large weights  
- Displayed noisy validation behavior, showing that overly strong regularization can hinder learning instead of helping

---

## Key Analyses

- **Validation Curves:** Accuracy and loss compared across all models  
- **Instability Metric:** Standard deviation of validation accuracy used to evaluate consistency  
- **Classification Reports:** Identified which classes remained difficult  
- **Misclassification Visuals:** Side-by-side images highlight similarities between confusing labels  
- **MNIST Experiment:** Same optimization strategies tested on MNIST for cross-dataset comparison  

---

## Findings

- Most optimizations improved stability or accuracy, but none solved all classification issues.  
- **SGD + BatchNorm** was the most stable configuration overall.  
- **RMSProp + L2** was the most unstable, likely from excessive regularization.  
- Overlapping sign shapes caused consistent misclassification across models.  
- MNIST proved substantially easier to model due to its lower variability.

---

## Usage

- Everything needed to run the project is contained within the notebook.  
- If running locally, update dataset file paths from the Colab upload workflow.  

---

## Extra Credit

- MNIST dataset loaded and trained with the same optimization settings  
- Results compared side-by-side with ASL model performance  
- Visualizations included for direct comparison  

---

## Ethical Considerations

- Automated sign recognition can unintentionally flatten the nuance and emotional expression present in human signing.  
- Viewing sign language solely as a classification task risks reducing an identity-rich practice to a technical artifact.  
- Systems should be designed with careful ethical consideration of the impact on Deaf and Hard-of-Hearing communities.

---

## Dependencies

- Python 3.12+  
- TensorFlow / Keras  
- NumPy, Pandas  
- Matplotlib, Seaborn  
- Scikit-learn  

See `requirements.yaml` for full version details.

---

## Author

**Kirk Corwin**  
Seattle, WA  
Data Science & Computer Science Student
