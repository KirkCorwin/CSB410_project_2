from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

def eval_model(y_true, y_pred, model_name):
    test_acc = accuracy_score(y_true, y_pred)
    print(f'{model_name} test accuracy: {test_acc:.4f}\n')

    # confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10,8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{model_name} confusion matrix')
    plt.xlabel('predicted')
    plt.ylabel('true')
    plt.show()

    # classification report
    print(f'{model_name} classification report:\n')
    print(classification_report(y_true, y_pred))

    return test_acc