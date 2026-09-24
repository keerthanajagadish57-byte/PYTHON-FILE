print("===== WEATHER DASHBOARD =====")

city = input("Enter city name: ")
temperature = float(input("Enter temperature in °C: "))
humidity = float(input("Enter humidity percentage: "))

print("\n===== WEATHER REPORT =====")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")

if temperature >= 35:
    print("Weather: Very Hot ☀️")
elif temperature >= 25:
    print("Weather: Warm")
elif temperature >= 15:
    print("Weather: Pleasant")
else:
    print("Weather: Cold ❄️")

if humidity >= 70:
    print("Humidity: High")
elif humidity >= 40:
    print("Humidity: Moderate")
else:
    print("Humidity: Low")
