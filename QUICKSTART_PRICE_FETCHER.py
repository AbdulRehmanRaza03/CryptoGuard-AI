#!/usr/bin/env python3
"""
CryptoGuard AI - Quick Start Guide for Real-Time Price Fetching
"""

import sys
from pathlib import Path

print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                  CryptoGuard AI - Price Fetcher Guide                     ║
║              Real-Time Crypto Prices + Live Exchange Rates                 ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 WHAT'S NEW:
═════════════

1. Live Binance Prices
   ├─ Fetches real-time cryptocurrency prices
   ├─ Supports any coin traded on Binance
   └─ Cached for 5 minutes to optimize API calls

2. Live Exchange Rates
   ├─ USD to PKR conversion (and other currencies)
   ├─ Multiple free APIs with automatic fallback
   └─ No API key required

3. Portfolio Value Calculator
   ├─ Real-time gain/loss in USD
   ├─ Real-time gain/loss in PKR
   ├─ Automatic error handling
   └─ Detailed error reporting

4. Refresh Controls
   ├─ Manual refresh button for latest prices
   ├─ Auto-refresh capability (30-second interval)
   └─ Last refresh timestamp display


🚀 QUICK START:
═══════════════

1. Install Dependencies
   ───────────────────────
   pip install -r requirements.txt

2. Test Price Fetcher
   ─────────────────────
   python test_price_fetcher.py
   
   Expected output:
   ✅ BTC: $75,747.64
   ✅ ETH: $2,355.05
   ✅ ADA: $0.26
   ✅ USD to PKR: 279.00

3. Run CryptoGuard AI
   ────────────────────
   streamlit run app.py
   
   Then navigate to: Portfolio → Live Prices

4. Use Live Price Features
   ────────────────────────
   - Add your crypto holdings
   - Press "Refresh Prices" button
   - See live prices from Binance
   - View gain/loss in USD and PKR


📋 FEATURES BREAKDOWN:
════════════════════════

Portfolio Summary (Live)
┌─────────────────────────────────────────────────────────────┐
│ Holdings: 4              Total Invested: $25,400.00         │
│ Current Value: $42,583.94 (+67.65%)                         │
│ Gain/Loss: $17,183.94 (≈ ₨4,793,620.86)                     │
│ Exchange Rate: 1 USD = 279.00 PKR                           │
└─────────────────────────────────────────────────────────────┘

Holdings Table (Live Prices)
┌──────┬─────────┬────────────┬───────────────┬────────────────┐
│ Code │ Current │ Invested   │ Current Value │ Gain/Loss      │
├──────┼─────────┼────────────┼───────────────┼────────────────┤
│ BTC  │ $75,747 │ $21,000    │ $37,873.50    │ ✅ +80.35%    │
│ ETH  │ $2,355  │ $4,400     │ $4,710.00     │ ✅ +7.05%     │
│ ADA  │ $0.26   │ $50        │ $26.00        │ ❌ -48.00%    │
└──────┴─────────┴────────────┴───────────────┴────────────────┘


🔧 API SOURCES:
═════════════════

Crypto Prices:
  • Binance (via ccxt)
  • Unlimited requests
  • Updates: Real-time with 5-min cache

Exchange Rates (Fallback Order):
  1. exchangerate-api.com (1,500/month)
  2. freecurrencyapi.com (300/month)
  3. exchangerate.host (Unlimited)


⚙️ HOW TO USE:
═══════════════

In Streamlit App
─────────────────
1. Go to Portfolio page
2. See live prices in:
   - Portfolio Summary (top)
   - Holdings Table (filtered by live data)
   - Allocation section
3. Click "🔄 Refresh Prices" for latest data
4. Toggle "🔄 Auto Refresh" for periodic updates

In Python Code
────────────────
from utils.price_fetcher import PriceFetcher, PortfolioValueCalculator

# Fetch single price
fetcher = PriceFetcher()
btc_price = fetcher.fetch_price("BTC")
print(f"BTC: ${btc_price:,.2f}")

# Fetch exchange rate
rate = fetcher.fetch_exchange_rate("PKR")
print(f"1 USD = {rate:.2f} PKR")

# Calculate portfolio
holdings = {
    "BTC": {"quantity": 0.5, "buy_price_usd": 42000},
    "ETH": {"quantity": 2, "buy_price_usd": 2200},
}

calculator = PortfolioValueCalculator(fetcher)
portfolio = calculator.calculate_portfolio_value(holdings, rate)

print(f"Current Value: ${portfolio['summary']['total_current_value_usd']:,.2f}")
print(f"Gain/Loss: ${portfolio['summary']['total_gain_loss_usd']:,.2f}")


📊 SUPPORTED CRYPTOCURRENCIES:
═══════════════════════════════

Any coin with USDT pair on Binance:
  ✓ BTC, ETH, ADA, SOL, XRP, etc.
  ✓ Thousands of coins supported
  ✓ Custom symbols supported


💡 TIPS & TRICKS:
═════════════════

1. Update Exchange Rate
   ⚙️ Settings → Exchange Rate → Update Rate
   (Saves to database for persistent use)

2. Export Portfolio
   ⚙️ Settings → Export Portfolio Data
   (Downloads CSV with current prices)

3. Use Manual Refresh
   Click "🔄 Refresh" button to bypass cache
   and get latest prices immediately

4. Monitor Price Changes
   Refresh periodically to track live updates
   Color codes show ✅ gains / ❌ losses


🐛 TROUBLESHOOTING:
══════════════════

Issue: "Could not fetch price"
───────────────────────────────
✓ Check internet connection
✓ Verify coin symbol (must trade on Binance)
✓ Try manual refresh
✓ Restart app

Issue: "Exchange rate fetch failed"
────────────────────────────────────
✓ Check internet connection
✓ All 3 APIs may be down (unlikely)
✓ Fallback to cached rate (277.5)
✓ Update manually in settings

Issue: "Prices seem outdated"
─────────────────────────────
✓ Click refresh button (bypasses 5-min cache)
✓ Cache duration is 5 minutes
✓ Wait 5 min for auto-update


📈 PERFORMANCE:
═══════════════

Price Fetch Time:  ~500ms
Exchange Rate:     ~300-600ms
Portfolio Calc:    ~100-200ms
───────────────────────────
Total Refresh:     ~1-2 seconds


📚 DOCUMENTATION:
═════════════════

For detailed information, see:
  📄 PRICE_FETCHER_GUIDE.md
  📄 utils/price_fetcher.py (source code)
  📄 test_price_fetcher.py (examples)


✨ FEATURES PIPELINE:
════════════════════

Planned Enhancements:
  □ Price history charts (30-day trends)
  □ Automated price alerts
  □ Multiple exchange support
  □ Portfolio rebalancing suggestions
  □ Webhook notifications
  □ Trading bot integration


💬 FEEDBACK & SUPPORT:
══════════════════════

Found a bug or issue?
  → GitHub: https://github.com/AbdulRehmanRaza03/CryptoGuard-AI
  → Issues: Report at GitHub Issues

Need help?
  → Check PRICE_FETCHER_GUIDE.md
  → Look at test_price_fetcher.py examples
  → Read utils/price_fetcher.py comments


═════════════════════════════════════════════════════════════════════════════

Happy Trading! 🚀💰

═════════════════════════════════════════════════════════════════════════════
""")


def show_code_examples():
    """Show code examples"""
    print("""

📝 CODE EXAMPLES:
═════════════════

Example 1: Fetch Single Price
──────────────────────────────
from utils.price_fetcher import PriceFetcher

fetcher = PriceFetcher()
price = fetcher.fetch_price("BTC")
print(f"Bitcoin: ${price:,.2f}")
# Output: Bitcoin: $75,747.64


Example 2: Fetch Multiple Prices
─────────────────────────────────
symbols = ["BTC", "ETH", "ADA", "SOL"]
prices = fetcher.fetch_multiple_prices(symbols)

for symbol, price in prices.items():
    if price:
        print(f"{symbol}: ${price:,.2f}")
    else:
        print(f"{symbol}: Failed to fetch")


Example 3: Get Exchange Rate
─────────────────────────────
rate = fetcher.fetch_exchange_rate("PKR")
print(f"1 USD = {rate:.2f} PKR")

usd = 1000
pkr = usd * rate
print(f"${usd:,} = ₨{pkr:,.0f}")


Example 4: Calculate Portfolio Value
─────────────────────────────────────
from utils.price_fetcher import PortfolioValueCalculator

calculator = PortfolioValueCalculator(fetcher)

holdings = {
    "BTC": {"quantity": 0.5, "buy_price_usd": 42000},
    "ETH": {"quantity": 2.5, "buy_price_usd": 1800},
    "ADA": {"quantity": 1000, "buy_price_usd": 0.50},
}

portfolio = calculator.calculate_portfolio_value(holdings, exchange_rate=279)

# Access calculations
for holding in portfolio["holdings"]:
    print(f"{holding['symbol']}:")
    print(f"  Current Price: ${holding['current_price_usd']:,.2f}")
    print(f"  Current Value: ${holding['current_value_usd']:,.2f}")
    print(f"  Gain/Loss: ${holding['gain_loss_usd']:+,.2f} ({holding['gain_loss_pct']:+.2f}%)")

summary = portfolio["summary"]
print(f"\\nTotal Invested: ${summary['total_invested_usd']:,.2f}")
print(f"Current Value: ${summary['total_current_value_usd']:,.2f}")
print(f"Total Gain/Loss: ${summary['total_gain_loss_usd']:+,.2f} ({summary['total_gain_loss_pct']:+.2f}%)")
print(f"In PKR: ₨{summary['total_gain_loss_pkr']:+,.2f}")


═════════════════════════════════════════════════════════════════════════════
""")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--examples":
        show_code_examples()
    else:
        print("\nUse --examples flag to see code examples:")
        print("  python QUICKSTART_PRICE_FETCHER.py --examples\n")
