class axi_driver;

    virtual axi_if vif;

    task run();

        forever begin

            @(posedge vif.ACLK);

            if (vif.ARESETN == 0)
                continue;

            // Simple write transaction
            vif.AWVALID <= 1;
            vif.WVALID  <= 1;
            vif.AWADDR  <= 8'h10;
            vif.WDATA   <= 32'hDEAD_BEEF;

            wait(vif.AWREADY && vif.WREADY);

            vif.AWVALID <= 0;
            vif.WVALID  <= 0;

            vif.BREADY <= 1;

        end

    endtask

endclass
