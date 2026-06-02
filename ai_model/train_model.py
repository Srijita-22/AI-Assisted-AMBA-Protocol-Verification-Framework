import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# -----------------------------------------
# LOAD DATASET
# -----------------------------------------

df = pd.read_csv("data/transactions.csv")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# -----------------------------------------
# FEATURES
# -----------------------------------------

X = df[
    [
        "addr",
        "pwrite",
        "data",
        "psel",
        "penable",
        "pready"
    ]
]

# -----------------------------------------
# LABELS
# -----------------------------------------

y = df["label"]

# -----------------------------------------
# TRAIN TEST SPLIT
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------------
# MODEL
# -----------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# -----------------------------------------
# TRAIN
# -----------------------------------------

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Training Complete!")

# -----------------------------------------
# PREDICTION
# -----------------------------------------

y_pred = model.predict(X_test)

# -----------------------------------------
# ACCURACY
# -----------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(accuracy)

# -----------------------------------------
# CONFUSION MATRIX
# -----------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)

# -----------------------------------------
# CLASSIFICATION REPORT
# -----------------------------------------

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)

# -----------------------------------------
# FEATURE IMPORTANCE
# -----------------------------------------

print("\nFeature Importance")

for feature, score in zip(
    X.columns,
    model.feature_importances_
):
    print(
        f"{feature}: {score:.4f}"
    )

# -----------------------------------------
# SAVE MODEL
# -----------------------------------------

with open(
    "ai_model/protocol_detector.pkl",
    "wb"
) as model_file:

    pickle.dump(
        model,
        model_file
    )

print(
    "\nModel saved successfully!"
)

# -----------------------------------------
# FEATURE IMPORTANCE PLOT
# -----------------------------------------

plt.figure(
    figsize=(8,5)
)

plt.bar(
    X.columns,
    model.feature_importances_
)

plt.title(
    "Feature Importance"
)

plt.xlabel(
    "Features"
)

plt.ylabel(
    "Importance"
)

plt.tight_layout()

plt.savefig(
    "results/feature_importance.png"
)

print(
    "\nFeature Importance Plot Saved"
)

print(
    "results/feature_importance.png"
)
