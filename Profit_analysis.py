import requests
import matplotlib.pyplot as plt


api_key = "98d765ca4fd6a09e0355f015bd5f1cdb"


company= "AAPL"
years= 5

income_statement =requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")

income_statement= income_statement.json()
print(income_statement)

revenue = list(reversed([income_statement[i]['revenue'] for i in range(years)]))
profit = list(reversed([income_statement[i]['grossProfit'] for i in range(years)]))

plt.plot(revenue, label="Revenue")
plt.plot(profit, label="Gross Profit")
plt.legend(loc="upper left")
plt.show()