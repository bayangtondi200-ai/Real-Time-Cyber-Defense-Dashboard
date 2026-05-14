from collections import defaultdict

def analyze_logs(logs):
    brute_force = defaultdict(int)
    port_scan = defaultdict(set)

    alerts = []

    for line in logs:
        if "FAILED_LOGIN" in line:
            ip = line.split()[1]
            brute_force[ip] += 1

        if "PORT_ACCESS" in line:
            parts = line.split()
            ip = parts[1]
            port = parts[2]
            port_scan[ip].add(port)

    for ip, count in brute_force.items():
        if count > 5:
            alerts.append(f"🚨 Brute Force détecté depuis {ip} ({count} tentatives)")

    for ip, ports in port_scan.items():
        if len(ports) > 10:
            alerts.append(f"🚨 Scan de ports depuis {ip} ({len(ports)} ports)")

    return alerts
