from pathlib import Path

from monitor.axi_monitor import AXIMonitor
from monitor.axi_checker import AXIChecker

# Base directory
BASE_DIR = Path(__file__).parent

# Paths
LOG_FILE = BASE_DIR / "logs" / "transactions.csv"
REPORT_FILE = BASE_DIR / "results" / "violations.csv"

# Create objects
monitor = AXIMonitor()
checker = AXIChecker()

# -------------------------
# Generate sample transactions
# -------------------------

monitor.capture_write(100, 1, 1)   # legal
monitor.capture_write(50, 1, 0)    # missing WVALID
monitor.capture_write(300, 1, 1)   # invalid address

# -------------------------
# Save + Analyze
# -------------------------

monitor.save(LOG_FILE)

checker.check(
    LOG_FILE,
    REPORT_FILE
)
