"""Show useful facts about an IPv4 network (CIDR).

Usage:
    python3 tools/subnet.py 192.168.1.0/24
"""

import argparse
import ipaddress


def inspect(cidr):
    """Return the interesting facts about a CIDR network as a dict."""
    network = ipaddress.ip_network(cidr, strict=False)
    hosts = list(network.hosts())
    return {
        "network": str(network.network_address),
        "netmask": str(network.netmask),
        "prefix": network.prefixlen,
        "broadcast": str(network.broadcast_address),
        "total_addresses": network.num_addresses,
        "usable_hosts": len(hosts),
        "first_host": str(hosts[0]) if hosts else None,
        "last_host": str(hosts[-1]) if hosts else None,
    }


def main():
    parser = argparse.ArgumentParser(description="IPv4 subnet calculator")
    parser.add_argument("cidr", help="network in CIDR notation, e.g. 10.0.0.0/8")
    args = parser.parse_args()

    try:
        facts = inspect(args.cidr)
    except ValueError as error:
        parser.error(str(error))

    for key, value in facts.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
