TOPLEVEL_LANG = verilog

VERILOG_SOURCES = $(PWD)/rtl/apb_slave.v

TOPLEVEL = apb_slave

COCOTB_TEST_MODULES = test_apb_dataset

SIM = icarus

include $(shell cocotb-config --makefiles)/Makefile.sim
