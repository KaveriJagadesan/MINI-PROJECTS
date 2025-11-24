import random
import time
 
def generate_otp():
    otp = random.randint(100000, 999999)  
    expiry_time = time.time() + 10      
    return otp, expiry_time
 
def verify_otp(user_input, otp, expiry_time):
    if time.time() > expiry_time:
        return "OTP expired!"
    elif user_input == otp:
        return "OTP verified successfully!"
    else:
        return "Invalid OTP!"
 
otp, expiry = generate_otp()
print("Your OTP is:", otp)
 
time.sleep(5)  
 
user_otp = int(input("Enter OTP: "))
result = verify_otp(user_otp, otp, expiry)
print(result)