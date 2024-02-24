import socket

def get_a_record(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        return f"Non-existent domain (NXDOMAIN) \n Error getting A record for {domain}: {str(e)}\n\n"

def check_bulk_a_records(filename):
    results = {}
    try:
        with open(filename, 'r') as file:
            domain_list = file.read().splitlines()
            for domain in domain_list:
                results[domain] = get_a_record(domain)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return results

if __name__ == "__main__":
    # Specify the path to your file containing domain names
    file_path = "domain_list.txt"

    results = check_bulk_a_records(file_path)

    for domain, a_record in results.items():
        print(f"{domain}: {a_record}\n\n")

