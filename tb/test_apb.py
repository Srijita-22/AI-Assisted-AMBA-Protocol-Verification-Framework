import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def apb_write_read(dut):

    # Start clock
    cocotb.start_soon(
        Clock(dut.PCLK, 10, unit="ns").start()
    )

    # ---------------- Reset ----------------
    dut.PRESETn.value = 0

    dut.PSEL.value = 0
    dut.PENABLE.value = 0
    dut.PWRITE.value = 0
    dut.PADDR.value = 0
    dut.PWDATA.value = 0

    for _ in range(2):
        await RisingEdge(dut.PCLK)

    dut.PRESETn.value = 1

    await RisingEdge(dut.PCLK)

    dut._log.info("RESET COMPLETE")

    # ==================================================
    # WRITE TRANSACTION
    # ==================================================

    dut._log.info("STARTING WRITE TRANSACTION")

    # Setup Phase
    dut.PADDR.value = 10
    dut.PWDATA.value = 1234
    dut.PWRITE.value = 1
    dut.PSEL.value = 1
    dut.PENABLE.value = 0

    await RisingEdge(dut.PCLK)

    dut._log.info(
        f"WRITE SETUP: ADDR={int(dut.PADDR.value)} DATA={int(dut.PWDATA.value)}"
    )

    # Access Phase
    dut.PENABLE.value = 1

    await RisingEdge(dut.PCLK)

    dut._log.info(
        f"WRITE ACCESS: PREADY={int(dut.PREADY.value)}"
    )

    # End Transfer
    dut.PSEL.value = 0
    dut.PENABLE.value = 0

    await RisingEdge(dut.PCLK)

    dut._log.info("WRITE COMPLETE")

    # Give memory one extra cycle
    await RisingEdge(dut.PCLK)

    # ==================================================
    # READ TRANSACTION
    # ==================================================

    dut._log.info("STARTING READ TRANSACTION")

    # Setup Phase
    dut.PADDR.value = 10
    dut.PWRITE.value = 0
    dut.PSEL.value = 1
    dut.PENABLE.value = 0

    await RisingEdge(dut.PCLK)

    dut._log.info(
        f"READ SETUP: ADDR={int(dut.PADDR.value)}"
    )

    # Access Phase
    dut.PENABLE.value = 1

    await RisingEdge(dut.PCLK)

    dut._log.info(
        f"READ ACCESS: PREADY={int(dut.PREADY.value)}"
    )

    # Extra cycle before sampling
    await RisingEdge(dut.PCLK)

    read_data = int(dut.PRDATA.value)

    dut._log.info(
        f"READ DATA = {read_data}"
    )

    # End Transfer
    dut.PSEL.value = 0
    dut.PENABLE.value = 0

    await RisingEdge(dut.PCLK)

    # ==================================================
    # CHECK RESULT
    # ==================================================

    assert read_data == 1234, (
        f"Expected 1234, Got {read_data}"
    )

    dut._log.info("TEST PASSED")
