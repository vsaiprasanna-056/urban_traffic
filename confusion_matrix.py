import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_test = [0] * 293 + [1] * 293

y_pred = (
    [0] * 203 + [1] * 90 +
    [0] * 76 + [1] * 217
)

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Normal Congestion", "High Congestion"]
)

disp.plot(values_format="d")

plt.title("Logistic Regression - Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()

plt.savefig("logistic_regression_confusion_matrix.png", dpi=300, bbox_inches="tight")
plt.show()