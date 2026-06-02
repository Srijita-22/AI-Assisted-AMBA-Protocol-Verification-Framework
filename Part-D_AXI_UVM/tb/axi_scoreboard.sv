class axi_scoreboard;

    logic [31:0] mem [0:255];

    task write(input [7:0] addr, input [31:0] data);
        mem[addr] = data;
    endtask

    task check(input [7:0] addr, input [31:0] expected);

        if (mem[addr] !== expected)
            $display("[SCOREBOARD] MISMATCH addr=%0h exp=%0h got=%0h",
                     addr, expected, mem[addr]);
        else
            $display("[SCOREBOARD] MATCH addr=%0h", addr);

    endtask

endclass
