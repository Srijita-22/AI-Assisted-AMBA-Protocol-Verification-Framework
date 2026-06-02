import cocotb
import random
import csv

from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def generate_dataset(dut):

    cocotb.start_soon(
        Clock(dut.PCLK, 10, unit="ns").start()
    )

    dut.PRESETn.value = 0

    for _ in range(2):
        await RisingEdge(dut.PCLK)

    dut.PRESETn.value = 1

    await RisingEdge(dut.PCLK)

    with open(
        "data/transactions.csv",
        "w",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "addr",
            "pwrite",
            "data",
            "psel",
            "penable",
            "pready",
            "label"
        ])

        # ------------------
        # LEGAL
        # ------------------

        for _ in range(1000):

            writer.writerow([
                random.randint(0,255),
                random.randint(0,1),
                random.randint(0,65535),
                1,
                1,
                1,
                0
            ])

        # ------------------
        # INVALID ADDRESS
        # ------------------

        for _ in range(250):

            writer.writerow([
                random.randint(256,500),
                random.randint(0,1),
                random.randint(0,65535),
                1,
                1,
                1,
                1
            ])

        # ------------------
        # MISSING PENABLE
        # ------------------

        for _ in range(250):

            writer.writerow([
                random.randint(0,255),
                random.randint(0,1),
                random.randint(0,65535),
                1,
                0,
                1,
                2
            ])

        # ------------------
        # PENABLE BEFORE PSEL
        # ------------------

        for _ in range(250):

            writer.writerow([
                random.randint(0,255),
                random.randint(0,1),
                random.randint(0,65535),
                0,
                1,
                1,
                3
            ])

        # ------------------
        # WAIT STATE ERROR
        # ------------------

        for _ in range(250):

            writer.writerow([
                random.randint(0,255),
                random.randint(0,1),
                random.randint(0,65535),
                1,
                1,
                0,
                4
            ])

    dut._log.info(
        "Generated Multiclass Dataset"
    )
