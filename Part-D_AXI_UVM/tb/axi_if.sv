interface axi_if(input logic ACLK);

    logic ARESETN;

    logic [7:0] AWADDR;
    logic AWVALID;
    logic AWREADY;

    logic [31:0] WDATA;
    logic WVALID;
    logic WREADY;

    logic BVALID;
    logic BREADY;

    logic [7:0] ARADDR;
    logic ARVALID;
    logic ARREADY;

    logic [31:0] RDATA;
    logic RVALID;
    logic RREADY;

endinterface
