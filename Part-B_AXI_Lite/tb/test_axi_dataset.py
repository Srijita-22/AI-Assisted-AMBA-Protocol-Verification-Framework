import csv
import random

NUM_SAMPLES = 5000

with open(
    "data/axi_transactions.csv",
    "w",
    newline=""
) as f:

    writer = csv.writer(f)

    writer.writerow(
        [
            "awaddr",
            "awvalid",
            "wvalid",
            "arvalid",
            "rready",
            "label"
        ]
    )

    # LEGAL
    for _ in range(1000):

        writer.writerow(
            [
                random.randint(0,255),
                1,
                1,
                0,
                0,
                0
            ]
        )

    # INVALID ADDRESS
    for _ in range(1000):

        writer.writerow(
            [
                random.randint(256,511),
                1,
                1,
                0,
                0,
                1
            ]
        )

    # MISSING WVALID
    for _ in range(1000):

        writer.writerow(
            [
                random.randint(0,255),
                1,
                0,
                0,
                0,
                2
            ]
        )

    # MISSING AWVALID
    for _ in range(1000):

        writer.writerow(
            [
                random.randint(0,255),
                0,
                1,
                0,
                0,
                3
            ]
        )

    # READ HANDSHAKE ERROR
    for _ in range(1000):

        writer.writerow(
            [
                random.randint(0,255),
                0,
                0,
                1,
                0,
                4
            ]
        )

print(
    "Dataset Generated Successfully"
)
