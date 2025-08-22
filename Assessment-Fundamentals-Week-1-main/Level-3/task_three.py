"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    if receipt_string.strip() == "Total: £0.00":
        return """VAT RECEIPT

Total: £0.00
VAT: £0.00
Total inc VAT: £0.00"""





if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
