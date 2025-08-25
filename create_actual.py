import json

# Load accounts
with open('accounts.json', 'r') as f:
    accounts = json.load(f)

# Template for IMAP/SMTP
def make_entry(account):
    username = account.get("username")
    return {
        "display_name": account.get("display_name"),
        "real_name": account.get("real_name_name"),  # Note: field is 'real_name_name' in accounts.json
        "email": account.get("email"),
        "imap": {
            "host": "imap.example.com",
            "port": 993,
            "security": "ssl-on-alternate-port",
            "auth_method": "none",
            "username": username
        },
        "smtp": {
            "host": "smtp.example.com",
            "port": 465,
            "security": "ssl-on-alternate-port",
            "auth_method": "PLAIN",
            "username": username
        },
        "check_interval_minutes": 10
    }

# Build new entries
entries = [make_entry(acc) for acc in accounts]

# Write to new file
with open('actual.json', 'w') as f:
    json.dump(entries, f, indent=2)

print("Generated entries written to generated_examples.json")