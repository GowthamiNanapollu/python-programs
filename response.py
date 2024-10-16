from validator_collection import validators, checkers, errors

def main():
    email = input("What's your email address?")
    print(validate(email))

def validate(s):
    try:
        # This will check if the email is overall valid
        validated_email = validators.email(s)

        # Additional check for 'harvard.edu' domain
        if 'harvard.edu' in validated_email.split('@')[1]:
            return "Valid"
        else:
            return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()
