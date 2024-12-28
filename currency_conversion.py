def currency_converter(amount, from_currency, to_currency):
    # Static conversion rates
    rates = {
        "USD": {"EUR": 0.92, "GBP": 0.75, "INR": 82.5},
        "EUR": {"USD": 1.09, "GBP": 0.81, "INR": 89.5},
        "GBP": {"USD": 1.33, "EUR": 1.24, "INR": 110.5},
        "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.009},
    }

    # Check if the conversion is valid
    if from_currency not in rates or to_currency not in rates[from_currency]:
        return "Conversion rate not available for the selected currencies."

    # Convert the amount
    converted_amount = amount * rates[from_currency][to_currency]
    return f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"

# WRITE VALUE HERE

amount = float(input("Enter amount: "))
from_currency = input("Enter from currency (USD, EUR, GBP, INR): ").upper()
to_currency = input("Enter to currency (USD, EUR, GBP, INR): ").upper()

result = currency_converter(amount, from_currency, to_currency)
print(result)
