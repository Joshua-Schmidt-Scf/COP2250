import re


# Function for phone numbers
def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None


# Function for Social Security numbers
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.match(pattern, ssn) is not None


# Function for ZIP codes
def validate_zip(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    return re.match(pattern, zip_code) is not None


# Main function
def main():
    phone = input("Enter a phone number (XXX-XXX-XXXX): ")
    ssn = input("Enter a Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code (12345 or 12345-6789): ")

    # Validate phone number
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    # Validate SSN
    if validate_ssn(ssn):
        print("Social Security Number is valid.")
    else:
        print("Social Security Number is invalid.")

    # Validate ZIP code
    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


# Run the program
main()
