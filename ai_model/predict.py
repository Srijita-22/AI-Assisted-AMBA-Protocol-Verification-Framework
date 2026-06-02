import pickle
import pandas as pd

with open("ai_model/protocol_detector.pkl", "rb") as f:
    model = pickle.load(f)

addr = int(input("Address: "))
pwrite = int(input("PWRITE: "))
data = int(input("Data: "))

sample = pd.DataFrame(
    [[addr, pwrite, data]],
    columns=["addr", "pwrite", "data"]
)

prediction = model.predict(sample)[0]

if prediction == 0:
    print("LEGAL TRANSACTION")
else:
    print("PROTOCOL VIOLATION")
