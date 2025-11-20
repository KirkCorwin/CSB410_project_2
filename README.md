# Sign Language Recognition with Deep Learning

## Overview

This project explores **deep learning approaches for classifying American Sign Language (ASL) hand signs** using a custom dataset of 25 labels. The main goal was to compare **baseline and optimized models** with different optimizers and regularization techniques, analyze model stability, and visualize misclassifications. An **extra credit experiment** compares performance on the MNIST dataset for reference.

All code, plots, and results are contained within the provided Jupyter notebook (`.ipynb` file).

---

## Dataset

- The ASL dataset is **added manually in Google Colab**.
- If running locally, update the file path to point to your `data/` folder.

---

## Project Structure

- `notebooks/` – Jupyter notebook with all model training, evaluation, and visualization code
- `plots/` – Generated figures including accuracy/loss curves, instability charts, and example misclassified images
- `requirements.yaml` – Conda environment with all necessary dependencies

---

## Models and Optimizations

1. **Baseline Model**
   - Optimizer: Adam
   - No regularization
   - Dense layers: 512 → 256 → 25
   - Purpose: Reference for comparison

2. **Model A: Adam + Dropout**
   - Dropout: 30% after each dense layer
   - Helps reduce overfitting and improves generalization
   - Achieved higher validation stability than baseline

3. **Model B: SGD + Batch Normalization**
   - Batch normalization added after each dense layer
   - Stabilizes learning by normalizing activations
   - Resulted in very low instability (std of val_accuracy)

4. **Model C: RMSProp + L2 Regularization**
   - L2 penalty on weights for both dense layers
   - Aimed to reduce overfitting
   - Showed high fluctuation across epochs, demonstrating that regularization can backfire if overapplied

---

## Key Analyses

- **Validation Accuracy and Loss:** Overlay plots compare all models across epochs
- **Instability:** Calculated as standard deviation of validation accuracy to assess model consistency
- **Classification Reports:** Evaluated per-class performance to identify difficult classes (e.g., 23, 12)
- **Misclassified Examples:** Visualized similarities between misclassified and true classes
- **Extra Credit:** MNIST dataset was used to compare optimizer performance across datasets

---

## Findings

- Optimized models generally outperformed the baseline, but not all optimizations improved results.  
- SGD + BatchNorm was the most stable, while RMSProp + L2 fluctuated significantly.  
- Classes with high visual similarity were hardest to classify, regardless of optimizer.  
- Dropout and batch normalization consistently improved generalization, but L2 needs careful tuning.  
- MNIST is less variable than ASL, making models easier to train and more stable.

---

## Usage

1. **Setup Environment**

```bash
conda env create -f requirements.yaml
conda activate asl_dl
```

## Run Notebook

- All models, evaluations, and plots are self-contained in the notebook  
- Update dataset paths if running locally  

## Extra Credit

- Load MNIST dataset  
- Train models with the same optimizations  
- Compare performance and visualizations  

## Ethical Considerations

- Models for sign language recognition may strip emotion and individuality from live signing  
- Treating sign language purely as a classification task risks reducing an identity feature to a data point  
- Responsible deployment should complement, not replace, human interaction in Deaf and Hard-of-Hearing communities  

## Dependencies

- Python 3.12+  
- TensorFlow/Keras  
- NumPy, Pandas  
- Matplotlib, Seaborn  
- Scikit-learn  

*(See `requirements.yaml` for exact versions)*  

## Author

**Kirk Corwin**  
Seattle, WA  
Data Science & Computer Science Student






