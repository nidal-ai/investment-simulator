import random
import numpy as np

# --- Data collection function ---
def collect_data():
    print("Welcome to the Investment Simulator.")
    initial_capital = float(input("Enter the amount to invest (USD): "))
    investment_duration = int(input("Enter the investment duration (in years): "))
    
    # Risk tolerance choice
    print("\nWhat is your risk tolerance?")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    risk_tolerance = int(input("Enter the number corresponding to your choice (1, 2, 3): "))
    
    # Investment advice based on data
    give_investment_advice(initial_capital, risk_tolerance)
    
    if risk_tolerance == 1:
        annual_return = 0.03  # Low return for low risk
    elif risk_tolerance == 2:
        annual_return = 0.09  # Medium return for medium risk
    else:
        annual_return = 0.12  # High return for high risk

    # Type of investment choice
    print("\nChoose your type of investment:")
    print("1. Stocks")
    print("2. Bonds")
    print("3. Cryptocurrencies")
    investment_type = input("Enter the number of your choice (1, 2, or 3): ")

    if investment_type == "1":
        annual_return += 0.02  # Stocks, slightly higher return
    elif investment_type == "2":
        annual_return += 0.01  # Bonds, slightly lower return
    else:
        annual_return += 0.05  # Cryptocurrencies, very high return but risky

    return initial_capital, investment_duration, annual_return

# --- Investment advice function ---
def give_investment_advice(initial_capital, risk_tolerance):
    print("\nInvestment Advice:")
    if initial_capital < 5000:
        print("It is advised to choose **bonds** or a more secure approach.")
    elif initial_capital >= 5000 and initial_capital < 20000:
        print("You may consider **stocks** or a mix of stocks and bonds.")
    else:
        if risk_tolerance == 1:
            print("It is advised to choose **bonds**.")
        elif risk_tolerance == 2:
            print("It is advised to choose **stocks**.")
        else:
            print("You may consider **cryptocurrencies**, depending on your risk appetite.")

# --- Investment return calculation function ---
def calculate_returns(initial_capital, annual_return, investment_duration):
    returns = []
    capital = initial_capital
    for year in range(1, investment_duration + 1):
        fluctuation = random.uniform(-0.02, 0.02)  # Moderate fluctuation
        capital = capital * (1 + annual_return + fluctuation)  # Apply return with fluctuation
        returns.append(capital)
    return returns

# --- Net profitability calculation function ---
def calculate_net_profitability(returns, inflation_rate, tax_rate):
    net_profitabilities = []
    gross_profitabilities = []  # For displaying gross capital
    for capital in returns:
        # Apply inflation
        capital_after_inflation = capital * (1 - inflation_rate)  # Inflation = 2%
        # Apply taxes
        net_capital = capital_after_inflation * (1 - tax_rate)  # Tax rate on returns (20% in this case)
        net_profitabilities.append(net_capital)
        gross_profitabilities.append(capital_after_inflation)
    
    return net_profitabilities, gross_profitabilities

# --- Result presentation and recommendations ---
def display_recommendations(initial_capital, annual_return, investment_duration, net_profitabilities, gross_profitabilities, risk):
    print(f"\nInitial investment: {initial_capital} USD")
    print(f"Estimated annual return: {annual_return * 100}%")
    print(f"Investment duration: {investment_duration} years")
    
    print("\nGross capital (before taxes and inflation) and net capital (after taxes and inflation) for each year:")
    for i in range(investment_duration):
        print(f"Year {i+1}: Gross capital = {gross_profitabilities[i]:.2f} USD, Net capital = {net_profitabilities[i]:.2f} USD")
    
    print(f"\nRisk (standard deviation) of the portfolio: {risk:.2f}")

    net_profitability_total = net_profitabilities[-1]
    print(f"\nNet profitability after {investment_duration} years: {net_profitability_total - initial_capital:.2f} USD")

    if net_profitability_total - initial_capital < 0:
        print("It seems that the investment has not generated profits. It may be useful to diversify your investments further.")
    
    # Calculating net return percentage
    net_return_percentage = ((net_profitability_total - initial_capital) / initial_capital) * 100
    print(f"\nNet return percentage after {investment_duration} years: {net_return_percentage:.2f}%")

    print("\nRecommendation:")
    if net_profitability_total > initial_capital * 1.5:
        print("Your investment seems very profitable!")
    else:
        print("It is advised to diversify your investments to maximize gains.")

# --- Main function ---
def main():
    initial_capital, investment_duration, annual_return = collect_data()
    returns = calculate_returns(initial_capital, annual_return, investment_duration)
    
    # Portfolio diversification
    net_profitabilities, gross_profitabilities = calculate_net_profitability(returns, inflation_rate=0.02, tax_rate=0.2)
    
    # Calculating risk
    risk = np.std(returns)
    
    display_recommendations(initial_capital, annual_return, investment_duration, net_profitabilities, gross_profitabilities, risk)

# Run the program
main()
