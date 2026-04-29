"""
Quick test of price fetcher without Streamlit
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

# Mock streamlit for testing
class MockStreamlit:
    @staticmethod
    def cache_data(ttl=None):
        def decorator(func):
            return func
        return decorator

sys.modules['streamlit'] = MockStreamlit()

from utils.price_fetcher import PriceFetcher, PortfolioValueCalculator

print("🔄 Testing Price Fetcher (without Streamlit caching)...")
print("="*60)

fetcher = PriceFetcher()

# Test single price
print("\n📊 Testing Binance Price Fetch:")
symbols = ["BTC", "ETH", "ADA"]

for symbol in symbols:
    try:
        price = fetcher._fetch_price_internal(symbol)
        if price:
            print(f"  ✅ {symbol}: ${price:,.2f}")
        else:
            print(f"  ⚠️  {symbol}: Could not fetch")
    except Exception as e:
        print(f"  ❌ {symbol}: Error - {str(e)}")

# Test exchange rate
print("\n💱 Testing Exchange Rate Fetch:")
try:
    rate = fetcher._fetch_exchange_rate_internal("PKR")
    if rate:
        print(f"  ✅ USD to PKR: {rate:.2f}")
    else:
        print(f"  ⚠️  Could not fetch exchange rate")
except Exception as e:
    print(f"  ❌ Error: {str(e)}")

# Test portfolio calculation
print("\n💰 Testing Portfolio Value Calculator:")
try:
    calculator = PortfolioValueCalculator(fetcher)
    
    sample_holdings = {
        "BTC": {"quantity": 0.5, "buy_price_usd": 42000},
        "ETH": {"quantity": 2, "buy_price_usd": 2200},
    }
    
    portfolio_data = calculator.calculate_portfolio_value(sample_holdings, 277.5)
    
    if portfolio_data:
        summary = portfolio_data["summary"]
        print(f"  ✅ Total Invested: ${summary['total_invested_usd']:,.2f}")
        print(f"  ✅ Current Value: ${summary['total_current_value_usd']:,.2f}")
        print(f"  ✅ Gain/Loss: ${summary['total_gain_loss_usd']:,.2f} ({summary['total_gain_loss_pct']:+.2f}%)")
        
        if portfolio_data["errors"]:
            print(f"\n  ⚠️  Warnings:")
            for error in portfolio_data["errors"]:
                print(f"    - {error}")
    else:
        print("  ❌ Failed to calculate portfolio value")
except Exception as e:
    print(f"  ❌ Error: {str(e)}")

print("\n" + "="*60)
print("✅ Test complete!")
