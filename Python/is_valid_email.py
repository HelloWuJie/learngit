import re

def is_valid_email(mail):
    if re.match(r'\w+\.?\w*@\w+\.com', mail):
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')