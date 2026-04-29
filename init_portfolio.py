"""
CryptoGuard AI - Portfolio Initialization Script
Initialize portfolio with sample data for testing
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.database import PortfolioDatabase
from datetime import datetime, timedelta

def init_sample_portfolio():
    """Initialize portfolio with sample cryptocurrency holdings"""
    
    db = PortfolioDatabase()
    
    # Sample holdings
    sample_holdings = [
        {
            "symbol": "BTC",
            "quantity": 0.85,
            "buy_price_usd": 42500,
            "buy_date": "2024-01-15",
            "current_price_usd": 45200
        },
        {
            "symbol": "ETH",
            "quantity": 5.2,
            "buy_price_usd": 2280,
            "buy_date": "2024-01-10",
            "current_price_usd": 2580
        },
        {
            "symbol": "ADA",
            "quantity": 1200,
            "buy_price_usd": 0.61,
            "buy_date": "2024-01-05",
            "current_price_usd": 0.72
        },
        {
            "symbol": "SOL",
            "quantity": 45.5,
            "buy_price_usd": 165.30,
            "buy_date": "2023-12-28",
            "current_price_usd": 195.50
        }
    ]
    
    print("🚀 Initializing portfolio with sample data...")
    
    for holding in sample_holdings:
        success = db.add_holding(
            symbol=holding["symbol"],
            quantity=holding["quantity"],
            buy_price_usd=holding["buy_price_usd"],
            buy_date=holding["buy_date"],
            current_price_usd=holding["current_price_usd"]
        )
        
        if success:
            print(f"✅ Added {holding['quantity']} {holding['symbol']}")
        else:
            print(f"⚠️  {holding['symbol']} already exists or error occurred")
    
    # Display summary
    summary = db.get_portfolio_summary()
    
    print("\n" + "="*50)
    print("📊 Portfolio Summary")
    print("="*50)
    print(f"Total Holdings: {summary['total_holdings']}")
    print(f"Total Investment: ${summary['total_investment_usd']:,.2f}")
    print(f"Current Value: ${summary['current_value_usd']:,.2f}")
    print(f"Total Gain/Loss: ${summary['total_gain_loss_usd']:,.2f}")
    print(f"Percentage Change: {summary['total_gain_loss_pct']:.2f}%")
    print("="*50)
    
    print("\n✨ Portfolio initialized successfully!")
    print("📁 Database file: portfolio.db")

def clear_portfolio():
    """Clear all portfolio data"""
    
    db = PortfolioDatabase()
    
    confirm = input("🗑️  This will delete all portfolio data. Continue? (yes/no): ")
    
    if confirm.lower() == "yes":
        if db.clear_all_data():
            print("✅ Portfolio cleared successfully!")
        else:
            print("❌ Error clearing portfolio")
    else:
        print("❌ Operation cancelled")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="CryptoGuard AI Portfolio Manager")
    parser.add_argument("--init", action="store_true", help="Initialize with sample data")
    parser.add_argument("--clear", action="store_true", help="Clear all data")
    
    args = parser.parse_args()
    
    if args.init:
        init_sample_portfolio()
    elif args.clear:
        clear_portfolio()
    else:
        print("Portfolio Manager - Initialization Script")
        print("\nUsage:")
        print("  python init_portfolio.py --init     Initialize with sample data")
        print("  python init_portfolio.py --clear    Clear all portfolio data")
