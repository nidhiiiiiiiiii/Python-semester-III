import re

# 1. The sample text we want to search through
text = """
Hello, you can contact support at support@example.com for general inquiries.
For sales, email us at sales.team@company.org or reach out to john.doe123@gmail.co.in.
Please do not email invalid addresses like @domain.com or hello@com.
"""

# 2. The regular expression (regex) pattern for a basic email
email_pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}"

# 3. Use re.findall() to extract all matching emails from the text
found_emails = re.findall(email_pattern, text)

# 4. Print the results
print("Found Emails:")
for email in found_emails:
    print("-", email)
