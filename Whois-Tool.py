import whois

# Prompt the user for input
domain = input("Enter a domain name: ")

# Use python-whois to get WHOIS information
whois_info = whois.whois(domain)

# Write the information to a file
with open("whois_info.txt", "w") as f:
    f.write(f"Domain: {domain}\n\n")
    f.write("WHOIS Information:\n")
    f.write