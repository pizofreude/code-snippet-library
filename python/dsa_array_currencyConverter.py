# Import necessary libraries
import requests
from config import OER_APP_ID

# This function gets the exchange rate for a given currency pair.
def get_exchange_rate(base_currency, target_currency):
    # API URL
    url = "https://openexchangerates.org/api/latest.json"

    # API parameters
    params = {
        "app_id": OER_APP_ID,
        "base": base_currency,
        "symbols": target_currency,
    }

    # Get the response from the API
    response = requests.get(url, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        # Get the exchange rate from the response
        exchange_rate = response.json()["rates"][target_currency]
    else:
        raise Exception("Failed to get exchange rate.")

    return exchange_rate


# This function converts an amount from one currency to another.
def convert_currency(amount, base_currency, target_currency):
    # Get the exchange rate
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    # Convert the amount
    converted_amount = amount * exchange_rate

    return converted_amount


# This function checks if the currency is valid.
def is_valid_currency(currency):
    # Get the list of valid currencies.
    valid_currencies = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLF","CLP","CNH","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","SSP","STD","STN","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VES","VND","VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPD","XPF","XPT","YER","ZAR","ZMW","ZWL",]
    # Check if the currency is in the list of valid currencies.
    return currency in valid_currencies


# This function gets the closest currency to the target currency.
def get_closest_currency(target_currency):
    # Get the list of valid currencies.
    valid_currencies = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLF","CLP","CNH","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","SSP","STD","STN","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VES","VND","VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPD","XPF","XPT","YER","ZAR","ZMW","ZWL",]
    
    # Find the closest currency to the target currency.
    closest_currency = valid_currencies[0]
    closest_distance = abs(target_currency - closest_currency)

    for currency in valid_currencies:
        distance = abs(target_currency - currency)
        if distance < closest_distance:
            closest_currency = currency
            closest_distance = distance

    return closest_currency

# Main function
def main():
    # Get the base currency and target currency from the user.
    base_currency = "USD"
    print("Base currency is default to USD. Subscribe to our premium plan to change the API base")
    target_currency = input("Enter the target currency: ")

    # Check if the base currency is valid.
    if not is_valid_currency(base_currency):
        print(f"Invalid base currency: {base_currency}")

        # Ask user if they want to try again or exit.
        try_again = input("Do you want to try again? Y or N: ")
        if try_again == "Y":
            main()
        else:
            return

    # Check if the target currency is valid.
    if not is_valid_currency(target_currency):
        print(f"Invalid target currency: {target_currency}")
        print("Do you want me to suggest the closest currency available?")
        closest_currency = input("Enter Y or N: ")
        if closest_currency == "Y":
            closest_currency = get_closest_currency(target_currency)
            print(f"The closest currency available is {closest_currency}")
            target_currency = closest_currency
        else:
            return

    # Get the amount to be converted.
    amount = float(input("Enter the amount to be converted: "))

    # Convert the amount
    converted_amount = convert_currency(amount, base_currency, target_currency)

    # Print the converted amount
    print(f"{amount} {base_currency} = {converted_amount} {target_currency}")


if __name__ == "__main__":
    main()

