import yfinance as yf

class Portfolio:
    def __init__(self):
        self.holdings = {}  # Store stock holdings: {symbol: {"quantity": quantity, "purchase_price": price}}

    def add_stock(self, symbol, quantity, purchase_price):
        """Adds a stock to the portfolio."""
        if symbol in self.holdings:
            print(f"Stock {symbol} already exists in portfolio. Use 'update' to modify.")
        else:
            self.holdings[symbol] = {"quantity": quantity, "purchase_price": purchase_price}
            print(f"Stock {symbol} added to portfolio.")

    def remove_stock(self, symbol):
        """Removes a stock from the portfolio."""
        if symbol in self.holdings:
            del self.holdings[symbol]
            print(f"Stock {symbol} removed from portfolio.")
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def update_stock(self, symbol, quantity, purchase_price):
        """Updates an existing stock in the portfolio."""
        if symbol in self.holdings:
            self.holdings[symbol]["quantity"] = quantity
            self.holdings[symbol]["purchase_price"] = purchase_price
            print(f"Stock {symbol} updated in portfolio.")
        else:
            print(f"Stock {symbol} not found in portfolio. Use 'add' to add it.")

    def get_portfolio_value(self):
        """Calculates and returns the current total value of the portfolio."""
        total_value = 0
        for symbol, details in self.holdings.items():
            try:
                ticker = yf.Ticker(symbol)
                current_price = ticker.info.get("currentPrice", ticker.info.get("regularMarketPrice"))  
                if current_price:
                    total_value += details["quantity"] * current_price
                else:
                    print(f"Could not retrieve price for {symbol}. Check the ticker symbol.")
            except Exception as e:
                print(f"Error retrieving data for {symbol}: {e}")
        return total_value

    def print_portfolio(self):
        """Prints the portfolio holdings and their current values."""
        print("\n--- Portfolio Holdings ---")
        for symbol, details in self.holdings.items():
            try:
                ticker = yf.Ticker(symbol)
                current_price = ticker.info.get("currentPrice", ticker.info.get("regularMarketPrice"))  
                if current_price:
                    total_value = details["quantity"] * current_price
                    gain_loss = total_value - details["purchase_price"] * details["quantity"]
                    print(f"Stock: {symbol}, Quantity: {details['quantity']}, "
                          f"Purchase Price: {details['purchase_price']:.2f}, "
                          f"Current Price: {current_price:.2f}, "
                          f"Total Value: {total_value:.2f}, "
                          f"Gain/Loss: {gain_loss:.2f}")
                else:
                    print(f"Could not retrieve price for {symbol}. Check the ticker symbol.")
            except Exception as e:
                print(f"Error retrieving data for {symbol}: {e}")

        print(f"\nTotal Portfolio Value: {self.get_portfolio_value():.2f}")


# Example usage:
portfolio = Portfolio()
portfolio.add_stock("AAPL", 10, 150.0)
portfolio.add_stock("GOOG", 5, 2000.0)
portfolio.print_portfolio()
portfolio.remove_stock("AAPL")
portfolio.update_stock("GOOG", 7, 2100.0)
portfolio.print_portfolio()