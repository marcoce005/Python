import random

from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp


def mac_to_bytes(mac_addr: str) -> bytes:                   # convert MAC in bytes
    return int(mac_addr.replace(":", ""), 16).to_bytes(6, "big")


client_mac = "01:02:03:04:05:06"
packet = (
    Ether(dst="ff:ff:ff:ff:ff:ff") /
    IP(src="0.0.0.0", dst="255.255.255.255") /
    UDP(sport=68, dport=67) /
    BOOTP(
        chaddr=mac_to_bytes(client_mac),
        xid=random.randint(1, 2**32-1),
    ) /
    DHCP(options=[("message-type", "discover"), "end"])
)
sendp(packet, iface="ens192", verbose=False)