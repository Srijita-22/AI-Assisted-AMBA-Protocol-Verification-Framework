module axi_lite_slave(

    input wire ACLK,
    input wire ARESETN,

    input wire [7:0] AWADDR,
    input wire AWVALID,
    output reg AWREADY,

    input wire [31:0] WDATA,
    input wire WVALID,
    output reg WREADY,

    output reg BVALID,
    input wire BREADY,

    input wire [7:0] ARADDR,
    input wire ARVALID,
    output reg ARREADY,

    output reg [31:0] RDATA,
    output reg RVALID,
    input wire RREADY

);

reg [31:0] mem [0:255];

integer i;

always @(posedge ACLK or negedge ARESETN)
begin

    if(!ARESETN)
    begin

        AWREADY <= 0;
        WREADY <= 0;
        BVALID <= 0;

        ARREADY <= 0;
        RVALID <= 0;
        RDATA <= 0;

        for(i=0;i<256;i=i+1)
            mem[i] <= 0;

    end

    else
    begin

        AWREADY <= 1;
        WREADY <= 1;
        ARREADY <= 1;

        //----------------------------------
        // WRITE
        //----------------------------------

        if(AWVALID && WVALID)
        begin

            mem[AWADDR] <= WDATA;

            BVALID <= 1;

        end

        if(BVALID && BREADY)
            BVALID <= 0;

        //----------------------------------
        // READ
        //----------------------------------

        if(ARVALID)
        begin

            RDATA <= mem[ARADDR];

            RVALID <= 1;

        end

        if(RVALID && RREADY)
            RVALID <= 0;

    end

end

endmodule
