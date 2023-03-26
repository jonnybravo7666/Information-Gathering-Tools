import whois
import dns.resolver


target_domain = input("Enter a domain name: ")

# Use python-whois to get WHOIS information
whois_info = whois.whois(target_domain)

# Set the target domain and record type
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
# Create a DNS resolver
resolver = dns.resolver.Resolver()
for record_type in record_types:
    # Perform DNS lookup for the specified domain and record type
    try:
        answers = resolver.resolve(target_domain, record_type)
    except dns.resolver.NoAnswer:
        continue

    print (f"Domain: {target_domain}\n\n") 
    print (str(whois_info)) 

    print ("-------------------------------------------------\n\n") 
    # Print the answers
    print (f"{record_type} records for {target_domain}:")
    for rdata in answers:
        print(f" {rdata}")