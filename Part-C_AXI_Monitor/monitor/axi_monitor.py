import csv

class AXIMonitor:

    def __init__(self):

        self.transactions = []

    def capture_write(
        self,
        awaddr,
        awvalid,
        wvalid
    ):

        self.transactions.append(
            [
                awaddr,
                awvalid,
                wvalid
            ]
        )

    def save(
        self,
        filename
    ):

        with open(
            filename,
            "w",
            newline=""
        ) as f:

            writer = csv.writer(f)

            writer.writerow(
                [
                    "awaddr",
                    "awvalid",
                    "wvalid"
                ]
            )

            writer.writerows(
                self.transactions
            )
