def generate_account_number(phone_number):
    """Generate an account number based on the phone number."""
    if len(phone_number) == 11 and phone_number.isdigit():
        # Derive the account number by shuffling or transforming the phone number
        # Example: Reverse the phone number and add a fixed prefix
        account_number = phone_number[::-1]
        print(f"Phone number is valid.\nGenerated Account Number: {account_number}")
    else:
        print("Invalid phone number. Please ensure it is exactly 11 digits long and contains only numbers.")

# Main program
if __name__ == "__main__":
    phone_number = input("Enter your 11-digit phone number: ").strip()
    generate_account_number(phone_number)
