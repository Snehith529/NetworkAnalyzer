import pandas as pd
import pyshark
import sys

class NetworkTrafficAnalyzer:
    def __init__(self, interface):
        self.interface = interface
        self.capture = None

    def start_capture(self):
        print(f"Starting capture on interface: {self.interface}")
        self.capture = pyshark.LiveCapture(interface=self.interface)

    def analyze_packet(self, packet):
        try:
            protocol = packet.transport_layer
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            length = int(packet.length)
            vlan_id = packet.vlan.id if hasattr(packet, 'vlan') else 'N/A'
            return {'Protocol': protocol, 'Source IP': src_ip, 'Destination IP': dst_ip, 'Length': length, 'VLAN ID': vlan_id}
        except AttributeError:
            return None

    def analyze_traffic(self, packet_count=50):
        print("Analyzing traffic...")
        data = []
        for packet in self.capture.sniff_continuously(packet_count=packet_count):
            analysis = self.analyze_packet(packet)
            if analysis:
                data.append(analysis)
        df = pd.DataFrame(data)
        print("Traffic Analysis:")
        print(df.head())
        return df

    def save_analysis(self, dataframe,filename="traffic_analysis.csv"):
        print(f"Saving analysis to {filename}")
        dataframe.to_csv(filename, index=False)
        print("File saved.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python network_analyzer.py <interface>")
        sys.exit(1)

    interface = sys.argv[1]
    analyzer = NetworkTrafficAnalyzer(interface)
    analyzer.start_capture()
    df  = analyzer.analyze_traffic()
    analyzer.save_analysis(df)
