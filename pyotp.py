import pyotp
import time

# Generate a random base32 secret key (compatible with Google Authenticator)
secret = pyotp.random_base32()
print(f"Generated Secret: {secret}")

# Create a TOTP object with the secret key
totp = pyotp.TOTP(secret)

# Generate the current OTP
current_otp = totp.now()
print(f"Current OTP: {current_otp}")

# Verify an OTP (e.g., from user input)
# Simulate user input after a short delay
time.sleep(5) 
user_entered_otp = input("Enter the OTP from your authenticator app: ")

if totp.verify(user_entered_otp):
    print("OTP Verified Successfully!")
else:
    print("Invalid OTP.")

# Generate a provisioning URI for Google Authenticator (optional)
provisioning_uri = totp.provisioning_uri(
    name="user@example.com",
    issuer_name="MySecureApp"
)
print(f"Provisioning URI for Google Authenticator: {provisioning_uri}")