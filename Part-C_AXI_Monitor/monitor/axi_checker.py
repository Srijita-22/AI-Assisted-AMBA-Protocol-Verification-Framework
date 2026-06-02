import pandas as pd

class AXIChecker:

    def check(
        self,
        input_file,
        output_file
    ):

        df = pd.read_csv(
            input_file
        )

        violations = []

        for _, row in df.iterrows():

            if row["awvalid"] == 1 and row["wvalid"] == 0:

                violations.append(
                    [
                        row["awaddr"],
                        "MISSING_WVALID"
                    ]
                )

            elif row["awaddr"] > 255:

                violations.append(
                    [
                        row["awaddr"],
                        "INVALID_ADDRESS"
                    ]
                )

        report = pd.DataFrame(
            violations,
            columns=[
                "address",
                "violation"
            ]
        )

        report.to_csv(
            output_file,
            index=False
        )

        print(
            f"Detected {len(violations)} violations"
        )
