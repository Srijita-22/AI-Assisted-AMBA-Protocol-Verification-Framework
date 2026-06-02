class axi_monitor;

    virtual axi_if vif;

    task run();

        forever begin

            @(posedge vif.ACLK);

            if (vif.AWVALID && vif.WVALID)
                $display("[MONITOR] WRITE Addr=%0h Data=%0h",
                         vif.AWADDR, vif.WDATA);

            if (vif.ARVALID)
                $display("[MONITOR] READ Addr=%0h Data=%0h",
                         vif.ARADDR, vif.RDATA);

        end

    endtask

endclass
