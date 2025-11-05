# Prompt the user to enter a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Apply the conversion formula
fahrenheit = (celsius * 9/5) + 32

# Display the converted temperature
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")