import re
from collections import defaultdict

def parse_log_file(file_path):
    ip_count = defaultdict(int)
    response_code_count = defaultdict(int)
    url_count = defaultdict(int)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                print(f"Processing line: {line.strip()}")  # Debugging line
                # Extract IP address
                ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
                if ip_match:
                    ip_count[ip_match.group()] += 1
                
                # Extract response code
                response_code_match = re.search(r'\s(\d{3})\s', line)
                if response_code_match:
                    response_code_count[response_code_match.group(1)] += 1
                
                # Extract URL
                url_match = re.search(r'\"(GET|POST)\s(.*?)\sHTTP', line)
                if url_match:
                    url_count[url_match.group(2)] += 1
    
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return ip_count, response_code_count, url_count

def display_summary(ip_count, response_code_count, url_count):
    print("Most Frequent IP Addresses:")
    for ip, count in sorted(ip_count.items(), key=lambda item: item[1], reverse=True):
        print(f"{ip}: {count} times")
    
    print("\nResponse Codes:")
    for code, count in sorted(response_code_count.items(), key=lambda item: item[1], reverse=True):
        print(f"{code}: {count} times")
    
    print("\nMost Accessed URLs:")
    for url, count in sorted(url_count.items(), key=lambda item: item[1], reverse=True):
        print(f"{url}: {count} times")

# Example usage
file_path = 'C:/Users/HP/Videos/Captures/Main Flow/task 4 codes/access.log'
ip_count, response_code_count, url_count = parse_log_file(file_path)
display_summary(ip_count, response_code_count, url_count)
