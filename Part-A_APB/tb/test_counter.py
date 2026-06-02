import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def counter_test(dut):

    cocotb.start_soon(
        Clock(dut.clk, 10, unit="ns").start()
    )

    dut.rst_n.value = 0

    for _ in range(2):
        await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    for _ in range(10):
        await RisingEdge(dut.clk)

    dut._log.info(
        f"Counter Value = {int(dut.count.value)}"
    )
