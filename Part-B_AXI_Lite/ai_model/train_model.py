import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

df = pd.read_csv(
    "data/axi_transactions.csv"
)

X = df[
    [
        "awaddr",
        "awvalid",
        "wvalid",
        "arvalid",
        "rready"
    ]
]

y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print(
    "\nAccuracy:",
    accuracy_score(
        y_test,
        predictions
    )
)

print(
    "\nClassification Report:\n"
)

print(
    classification_report(
        y_test,
        predictions
    )
)

with open(
    "ai_model/protocol_detector.pkl",
    "wb"
) as f:

    pickle.dump(
        model,
        f
    )

cm = confusion_matrix(
    y_test,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.savefig(
    "results/confusion_matrix.png"
)

plt.close()

plt.figure()

plt.bar(
    X.columns,
    model.feature_importances_
)

plt.title(
    "Feature Importance"
)

plt.savefig(
    "results/feature_importance.png"
)

plt.close()

print(
    "\nModel Saved"
)
