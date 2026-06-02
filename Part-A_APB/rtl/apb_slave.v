module apb_slave (
    input  wire        PCLK,
    input  wire        PRESETn,

    input  wire [7:0]  PADDR,
    input  wire        PSEL,
    input  wire        PENABLE,
    input  wire        PWRITE,
    input  wire [31:0] PWDATA,

    output wire [31:0] PRDATA,
    output wire        PREADY
);

    reg [31:0] mem [0:255];

    integer i;

    assign PREADY = 1'b1;

    assign PRDATA = mem[PADDR];

    always @(posedge PCLK or negedge PRESETn) begin
        if (!PRESETn) begin

            for (i = 0; i < 256; i = i + 1)
                mem[i] <= 32'd0;

        end
        else begin

            if (PSEL && PENABLE && PWRITE)
                mem[PADDR] <= PWDATA;

        end
    end

endmodule
