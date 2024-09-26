import re

def extract_unique_ips(log_file_path):
    # Regular expression pattern for matching IP addresses
    ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    
    unique_ips = set()  # Using a set to store unique IP addresses

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Search for all IP addresses in the line
                matches = re.findall(ip_pattern, line)
                unique_ips.update(matches)  # Add found IPs to the set

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' was not found.")
        return set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()

    return unique_ips

# Example usage
if __name__ == "__main__":
    log_file = 'server.log'  # Replace with your log file path
    unique_ips = extract_unique_ips(log_file)
    
    print("Unique IP addresses:")
    for ip in unique_ips:
        print(ip)
