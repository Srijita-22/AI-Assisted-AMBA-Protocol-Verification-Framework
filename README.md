# AI-Assisted Protocol Violation Detection Framework

## 🚀 Overview

This project implements a **hybrid RTL + Verification + AI framework** for detecting protocol violations in AMBA-based systems.

It combines:
- RTL Design (APB + AXI-Lite)
- Cocotb-based verification
- SystemVerilog-style testbench concepts
- AI/ML-based classification of protocol violations
- Rule-based monitoring and checking
- UVM-inspired verification architecture (Part-D)

---

## 🏗️ Architecture
RTL (APB / AXI-Lite)
↓
Cocotb Testbench (Python)
↓
Transaction Dataset Generation
↓
AI/ML Model (Sklearn Classifier)
↓
Violation Prediction + Classification
↓
Monitor + Rule-Based Checker
↓
UVM-style Verification Environment (Part-D)



---

## 📁 Project Structure

Part-A_APB/
Part-B_AXI_Lite/
Part-C_AXI_Monitor/
Part-D_AXI_UVM/



---

## 🔹 Part-A: APB + AI Classification
- APB Slave RTL design
- Cocotb verification environment
- Dataset generation from transactions
- ML model training (classification of violations)
- Feature importance analysis

---

## 🔹 Part-B: AXI-Lite + AI Extension
- AXI-Lite slave implementation
- Extended dataset generation
- AI model reuse for AXI protocol analysis
- Confusion matrix and evaluation metrics

---

## 🔹 Part-C: AXI Protocol Monitor
- Transaction-level monitor
- Rule-based violation checker
- CSV-based logging of protocol activity
- Detection of invalid protocol behavior

---

## 🔹 Part-D: UVM-style AXI Verification Environment
- AXI interface definition
- Driver + Monitor + Scoreboard architecture
- RTL simulation using SystemVerilog (Icarus)
- UVM-inspired verification flow (lightweight implementation)

---

## 🧠 Key Features

- Hybrid **RTL + Python + AI** verification flow
- Automated dataset generation from simulations
- ML-based protocol violation classification
- Rule-based + AI-based dual checking
- Scalable verification architecture
- UVM-style verification modeling

---

## 🛠️ Tools & Technologies

- Verilog / SystemVerilog
- Cocotb (Python-based verification)
- Python (NumPy, Pandas, Scikit-learn, Matplotlib)
- Icarus Verilog
- Machine Learning (Classification models)

---

## 📊 Results

- High accuracy ML classifier for protocol violation detection
- Automated feature extraction from RTL transactions
- Successful detection of:
  - Missing handshake signals
  - Invalid address access
  - Protocol timing violations

---

## 🎯 Learning Outcomes

- RTL design and verification flow
- Python-based hardware verification (Cocotb)
- ML integration in hardware verification
- Protocol-level debugging techniques
- UVM-style architecture understanding

---

## 📌 Future Improvements

- Full UVM migration using SystemVerilog
- Real AXI4 full protocol support
- Deep Learning-based anomaly detection
- Integration with formal verification tools

---

## 👨‍💻 Author

Srijita-22

GitHub: https://github.com/Srijita-22
