import re

def extract_unique_ips(log_file_path):
    # Regular expression pattern to match IP addresses
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    
    unique_ips = set()  # Using a set to store unique IPs

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Search for IP addresses in the line
            matches = ip_pattern.findall(line)
            unique_ips.update(matches)  # Add found IPs to the set

    return unique_ips

if __name__ == "__main__":
    log_file_path = 'path/to/your/logfile.log'  # Replace with your log file path
    unique_ips = extract_unique_ips(log_file_path)
    
    print("Unique IP Addresses:")
    for ip in unique_ips:
        print(ip)