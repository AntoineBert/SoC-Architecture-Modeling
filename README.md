# SoC & NoC Architecture Simulator

## 📌 Project Overview
This project provides a high-level modeling and simulation environment for **Systems-on-Chip (SoC)** and **Networks-on-Chip (NoC)**. Developed in **Python**, it allows users to architect custom grid-based networks of processing nodes and memory units, and simulate complex data exchange workloads using real-time routing algorithms.

## ⚙️ Key Features
* **Architectural Modeling**: Create and configure SoC layouts with dedicated compute and memory nodes.
* **Advanced Routing**: Implements a **Dijkstra-based** shortest path algorithm to optimize data packet travel through the NoC.
* **Behavioral Simulation**: Generate and execute task-based requests to analyze network congestion and latency.
* **Data Persistence**: Export and import system configurations using Python's `pickle` format.
* **Automated Reporting**: Generates detailed simulation logs for post-processing analysis.

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed.
* **Standard libraries only** (Tkinter for the GUI).

### Launching the Interface
To start the graphical user interface, run the following command:
```bash
python interface.py
```
### Loading Sample Data
The repository includes pre-configured test files to help you get started quickly:
1. **Open NoC**: Go to `File` > `Open NoC` and select `test_noc.pkl`.
2. **Import Tasks**: Go to `Tasks` > `Import Tasks` and select `test_taches.pkl`.
3. **Run**: Launch the simulation to observe node interactions.

## 📊 Output
Upon completion, the simulator generates a `simulation_report.txt` file. This report contains:
* Detailed logs of every data request and transfer.
* Success/Failure status of routing operations.
* Final system state summary.

## 📁 Repository Structure
* `src/`: Core logic (Classes: `SoC`, `NoC`, `Node`, `Request`).
* `interface.py`: Graphical user interface (GUI) implementation.
* `data/`: Sample `.pkl` configuration files.

## 👥 Authors
* **Antoine BERTRAND** - Main Developer

Samy-William AYYADA - Contributor

🏛 Academic Context

This project was developed in 2023 as part of the Computer Science curriculum at ENSTA Bretagne.
