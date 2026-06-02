`timescale 1ns/1ps

module testbench;

    reg ACLK = 0;
    reg ARESETN;

    reg [7:0] AWADDR;
    reg AWVALID;
    wire AWREADY;

    reg [31:0] WDATA;
    reg WVALID;
    wire WREADY;

    wire BVALID;
    reg BREADY;

    // Clock
    always #5 ACLK = ~ACLK;

    // DUT (replace with your RTL if needed)
    axi_lite_slave dut (
        .ACLK(ACLK),
        .ARESETN(ARESETN),
        .AWADDR(AWADDR),
        .AWVALID(AWVALID),
        .AWREADY(AWREADY),
        .WDATA(WDATA),
        .WVALID(WVALID),
        .WREADY(WREADY),
        .BVALID(BVALID),
        .BREADY(BREADY)
    );

    // -------------------------
    // Simple Driver
    // -------------------------
    initial begin

        ARESETN = 0;
        AWADDR = 0;
        AWVALID = 0;
        WDATA = 0;
        WVALID = 0;
        BREADY = 0;

        #20;
        ARESETN = 1;

        // WRITE TRANSACTION
        #10;
        AWADDR  = 8'h10;
        WDATA   = 32'hDEAD_BEEF;
        AWVALID = 1;
        WVALID  = 1;

        wait(AWREADY && WREADY);

        #10;
        AWVALID = 0;
        WVALID  = 0;
        BREADY  = 1;

        #50;

        $finish;

    end

    // -------------------------
    // Monitor
    // -------------------------
    always @(posedge ACLK) begin
        if (AWVALID && WVALID) begin
            $display("[MONITOR] WRITE Addr=%0h Data=%0h", AWADDR, WDATA);
        end
    end

endmodule
