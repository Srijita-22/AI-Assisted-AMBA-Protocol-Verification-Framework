import cocotb

from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def axi_lite_write_read(dut):

    cocotb.start_soon(
        Clock(dut.ACLK, 10, unit="ns").start()
    )

    dut.ARESETN.value = 0

    await RisingEdge(dut.ACLK)
    await RisingEdge(dut.ACLK)

    dut.ARESETN.value = 1

    # WRITE

    dut.AWADDR.value = 25
    dut.WDATA.value = 123456

    dut.AWVALID.value = 1
    dut.WVALID.value = 1

    await RisingEdge(dut.ACLK)

    dut.AWVALID.value = 0
    dut.WVALID.value = 0

    dut.BREADY.value = 1

    await RisingEdge(dut.ACLK)

    # READ

    dut.ARADDR.value = 25
    dut.ARVALID.value = 1

    await RisingEdge(dut.ACLK)

    dut.ARVALID.value = 0

    dut.RREADY.value = 1

    await RisingEdge(dut.ACLK)

    read_data = int(dut.RDATA.value)

    dut._log.info(
        f"READ DATA = {read_data}"
    )

    assert read_data == 123456
