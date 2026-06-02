import pickle
import pandas as pd

with open(
    "ai_model/protocol_detector.pkl",
    "rb"
) as f:

    model = pickle.load(f)

df = pd.read_csv(
    "data/transactions.csv"
)

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

predictions = model.predict(X)

label_map = {
    0: "LEGAL",
    1: "INVALID_ADDRESS",
    2: "MISSING_PENABLE",
    3: "PENABLE_BEFORE_PSEL",
    4: "WAIT_STATE_ERROR"
}

df["prediction"] = [
    label_map[p]
    for p in predictions
]

df.to_csv(
    "results/violations_report.csv",
    index=False
)

print(
    "Report generated successfully"
)
