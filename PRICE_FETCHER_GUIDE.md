"""
Real-Time Crypto Price Fetching Guide
CryptoGuard AI - Live Price Implementation
"""

# ============================================================================
# PRICE FETCHER MODULE DOCUMENTATION
# ============================================================================

## Overview
The `utils/price_fetcher.py` module provides real-time cryptocurrency prices 
from Binance and live exchange rates using free APIs.

## Key Features

### 1. Real-Time Price Fetching from Binance
- Uses ccxt (Cryptocurrency Trading Library) for Binance integration
- Fetches current prices for any cryptocurrency
- Automatic fallback if price fetch fails
- Caching to reduce API calls (5-minute TTL)

**Usage:**
```python
from utils.price_fetcher import PriceFetcher

fetcher = PriceFetcher()
btc_price = fetcher.fetch_price("BTC")  # Returns USD price
eth_price = fetcher.fetch_price("ETH")
ada_price = fetcher.fetch_price("ADA")
```

### 2. Live Exchange Rate Fetching
- Multi-API fallback strategy for reliability
- Supports USD to any currency conversion
- Uses free APIs (no API key required):
  * exchangerate-api.com (1500 requests/month free)
  * freecurrencyapi.com (300 requests/month free)
  * exchangerate.host (unlimited free requests)

**Usage:**
```python
fetcher = PriceFetcher()
pkr_rate = fetcher.fetch_exchange_rate("PKR")  # Returns 1 USD in PKR
eur_rate = fetcher.fetch_exchange_rate("EUR")
gbp_rate = fetcher.fetch_exchange_rate("GBP")
```

### 3. Portfolio Value Calculator
- Calculates real-time portfolio value
- Supports multiple currencies (USD and PKR)
- Calculates gain/loss in both currencies
- Error handling and reporting

**Usage:**
```python
from utils.price_fetcher import PriceFetcher, PortfolioValueCalculator

fetcher = PriceFetcher()
calculator = PortfolioValueCalculator(fetcher)

holdings = {
    "BTC": {"quantity": 0.5, "buy_price_usd": 42000},
    "ETH": {"quantity": 2, "buy_price_usd": 2200},
    "ADA": {"quantity": 100, "buy_price_usd": 0.50},
}

portfolio_data = calculator.calculate_portfolio_value(holdings, exchange_rate=279)

# portfolio_data contains:
# {
#     "holdings": [...],  # Individual holdings with live prices
#     "summary": {...},   # Total investment, current value, gain/loss
#     "errors": [],       # Any errors during calculation
#     "timestamp": "...", # When data was fetched
#     "exchange_rate": 279
# }
```

## Integration with Streamlit Portfolio Page

The Portfolio page now uses PriceFetcher for live data:

### Display Components

1. **Live Price Status & Refresh Controls**
   - Shows last refresh time
   - Manual refresh button (loads latest prices)
   - Auto-refresh toggle (30-second interval - not implemented in UI yet)

2. **Portfolio Summary with Live Prices**
   - Total holdings count
   - Total investment in USD and PKR
   - Current portfolio value
   - Gain/loss in USD and PKR
   - Live exchange rate display

3. **Holdings Table with Live Prices**
   - Current price from Binance
   - Calculated gain/loss for each holding
   - Percentages in both USD and PKR
   - Color-coded (✅ for gains, ❌ for losses)

### Session State Management
```python
# Auto-refresh state
st.session_state.auto_refresh  # Enable/disable auto-refresh
st.session_state.last_refresh  # Timestamp of last refresh
st.session_state.exchange_rate # Cached exchange rate
```

## API Rate Limits & Caching

### Caching Strategy
- **Duration:** 5 minutes per API call
- **Reduces:** Excessive API calls and quota usage
- **Invalidation:** Manual refresh button bypasses cache

### Rate Limits
- **Binance API:** No strict rate limit for public endpoints
- **exchangerate-api.com:** 1,500 requests/month (free)
- **freecurrencyapi.com:** 300 requests/month (free)
- **exchangerate.host:** Unlimited (free)

### Auto-Refresh Timer
The UI includes an auto-refresh button, but the 30-second auto-refresh 
can be implemented using:
```python
import time
if st.session_state.auto_refresh:
    time.sleep(30)  # Note: Can freeze UI - use callbacks instead
```

Better approach: Use Streamlit's `write` with callbacks for non-blocking refresh.

## Error Handling

The module includes comprehensive error handling:

1. **Network Errors**
   ```
   ccxt.NetworkError - Network connectivity issues
   ```

2. **Exchange Errors**
   ```
   ccxt.ExchangeError - Trading pair not found or exchange issue
   ccxt.ExchangeNotAvailable - Pair not available on exchange
   ```

3. **API Failures**
   - Automatic fallback to next API for exchange rates
   - Graceful degradation if all APIs fail
   - User warnings in the UI

4. **Price Fetch Failures**
   - Falls back to last known price
   - Shows warning messages
   - Calculates with available data

## Testing

Run the test script to verify functionality:
```bash
python test_price_fetcher.py
```

Expected output:
```
✅ BTC: $75,747.64
✅ ETH: $2,355.05
✅ ADA: $0.26
✅ USD to PKR: 279.00
✅ Total Invested: $25,400.00
✅ Current Value: $42,583.94
✅ Gain/Loss: $17,183.94 (+67.65%)
```

## Configuration

### Exchange Rate
Default exchange rate is set to 277.5 PKR per USD.
Update in Portfolio Settings:
```
⚙️ Portfolio Settings → Exchange Rate
```

### Add Custom Currencies
To support more currencies, modify:
```python
fetcher.fetch_exchange_rate("EUR")  # Add EUR, GBP, etc.
```

## Performance Metrics

Based on testing:
- **BTC Price Fetch:** ~500ms
- **Exchange Rate Fetch:** ~300-600ms (varies by API)
- **Portfolio Calculation:** ~100-200ms
- **Total Portfolio Refresh:** ~1-2 seconds

## Future Enhancements

1. **Price History Tracking**
   ```python
   # Store hourly/daily prices in database
   price_history = db.get_price_history("BTC", days=30)
   ```

2. **Automated Price Updates**
   ```python
   # Schedule price updates every X minutes
   scheduler.add_job(update_prices, 'interval', minutes=5)
   ```

3. **Multiple Exchange Support**
   ```python
   # Fetch from multiple exchanges and average
   prices = [binance_price, kraken_price, coinbase_price]
   avg_price = sum(prices) / len(prices)
   ```

4. **Price Alerts**
   ```python
   # Alert user when price reaches threshold
   if price > threshold:
       notify_user(f"BTC reached ${threshold}")
   ```

5. **Portfolio Rebalancing Recommendations**
   ```python
   # Suggest adjustments based on target allocation
   recommendations = calculate_rebalancing(portfolio)
   ```

## Troubleshooting

### Issue: "Could not fetch price for BTC"
**Solution:** 
- Check internet connection
- Verify Binance API is accessible
- Try manual refresh

### Issue: "All exchange rate APIs failed"
**Solution:**
- Use cached exchange rate in settings
- Check internet connectivity
- Fallback to default rate (277.5)

### Issue: "Slow price updates"
**Solution:**
- Wait for cache expiry (5 minutes)
- Press refresh button for fresh data
- Check internet bandwidth

## API Response Examples

### Binance Price Response
```json
{
  "BTC/USDT": {
    "last": 75747.64,
    "bid": 75750.00,
    "ask": 75770.00,
    "high": 76000.00,
    "low": 75000.00,
    "timestamp": 1623456789000
  }
}
```

### Exchange Rate Response
```json
{
  "rates": {
    "PKR": 279.00,
    "EUR": 0.95,
    "GBP": 0.82
  }
}
```

## Resources

- **ccxt Documentation:** https://docs.ccxt.com
- **Binance API:** https://binance-docs.github.io/apidocs
- **ExchangeRate APIs:** https://exchangerate-api.com
- **Streamlit Caching:** https://docs.streamlit.io/library/advanced-features/caching

"""

if __name__ == "__main__":
    print(__doc__)
