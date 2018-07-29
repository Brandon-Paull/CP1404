# Constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# Inputs
print("Electricity bill estimator")
tariff = int(input("Which tariff? 11 or 31: "))
cents_per_kWh = int(input("Enter cents per kWh: "))
daily_use_kWh = int(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))

