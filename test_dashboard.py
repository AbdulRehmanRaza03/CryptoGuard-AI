"""
Test script for the new professional Dashboard page
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_dashboard_imports():
    """Test that all dashboard imports work"""
    try:
        from utils import PortfolioDatabase, convert_to_usd, format_price, calculate_percentage_change
        from utils.price_fetcher import PriceFetcher, PortfolioValueCalculator
        from utils.risk_calculator import calculate_portfolio_risk, calculate_volatility
        print("✅ All dashboard imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_portfolio_data_loading():
    """Test that portfolio data can be loaded"""
    try:
        from utils import PortfolioDatabase
        from utils.price_fetcher import PriceFetcher, PortfolioValueCalculator

        db = PortfolioDatabase()
        price_fetcher = PriceFetcher()
        calculator = PortfolioValueCalculator(price_fetcher)

        # Get holdings
        holdings_df = db.get_holdings_dataframe()
        if holdings_df.empty:
            print("⚠️ No portfolio holdings found")
            return False

        print(f"✅ Found {len(holdings_df)} holdings: {holdings_df['symbol'].tolist()}")

        # Test portfolio calculation
        holdings_dict = {}
        for _, row in holdings_df.iterrows():
            holdings_dict[row["symbol"]] = {
                "quantity": row["quantity"],
                "buy_price_usd": row["buy_price_usd"]
            }

        portfolio_data = calculator.calculate_portfolio_value(holdings_dict, 277.5)
        if portfolio_data and "summary" in portfolio_data:
            summary = portfolio_data["summary"]
            print(f"✅ Portfolio value: ₨{summary['total_current_value_pkr']:,.0f}")
            print(f"✅ Total P&L: ₨{summary['total_gain_loss_pkr']:,.0f} ({summary['total_gain_loss_pct']:+.2f}%)")
            return True
        else:
            print("❌ Failed to calculate portfolio value")
            return False

    except Exception as e:
        print(f"❌ Portfolio data loading error: {e}")
        return False

def test_portfolio_history():
    """Test portfolio history functionality"""
    try:
        from utils import PortfolioDatabase

        db = PortfolioDatabase()
        history_df = db.get_portfolio_history(days=7)

        if history_df.empty:
            print("⚠️ No portfolio history found (this is normal for new installations)")
            return True  # Not an error

        print(f"✅ Found {len(history_df)} days of portfolio history")
        return True

    except Exception as e:
        print(f"❌ Portfolio history error: {e}")
        return False

def main():
    """Run all dashboard tests"""
    print("🧪 Testing CryptoGuard AI Professional Dashboard")
    print("=" * 50)

    tests = [
        ("Dashboard Imports", test_dashboard_imports),
        ("Portfolio Data Loading", test_portfolio_data_loading),
        ("Portfolio History", test_portfolio_history),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n🔄 Running: {test_name}")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} failed")

    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All dashboard tests passed! The professional dashboard is ready.")
        print("\n🚀 To run the dashboard:")
        print("   streamlit run app.py")
        print("   Then navigate to the '📊 Dashboard' page")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()