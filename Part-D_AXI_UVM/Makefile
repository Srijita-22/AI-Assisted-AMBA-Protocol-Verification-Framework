SIM = iverilog

all:
	iverilog -g2012 -g2012 -o sim.vvp rtl/axi_lite_slave.v tb/testbench.sv
	vvp sim.vvp
