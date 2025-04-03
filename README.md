# Network Traffic Analyzer

## Overview
The Network Traffic Analyzer is a Python-based tool designed to capture and analyze network traffic using TShark. It leverages CCNAv7 concepts such as VLANs and routing, and uses Python libraries including PyShark, NumPy, and Pandas.

## Features
- Real-time network traffic capture.
- Analysis of protocols, source IP, destination IP, packet length, and VLAN ID.
- Save traffic analysis to a CSV file.

## Prerequisites
- Python 3.x
- TShark (installed via Wireshark)
- PyShark library: `pip install pyshark`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Snehith529/NetworkAnalyzer
   cd NetworkTrafficAnalyzer
   ```
2. Install required libraries:
   ```bash
   pip install pandas numpy pyshark
   ```

## Usage
Run the tool from the command line:
```bash
python network_analyzer.py <interface>
```
Replace `<interface>` with your network interface name (e.g., `Ethernet`, `Wi-Fi`).

## Example
```bash
python network_analyzer.py Ethernet
```

## Output
- Displays real-time captured traffic analysis.
- Saves results to `traffic_analysis.csv` in the current directory.


