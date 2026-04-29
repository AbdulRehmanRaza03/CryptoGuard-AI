#!/usr/bin/env python
"""
Quick test of Portfolio Optimizer functionality
"""

import pandas as pd
from utils.portfolio_optimizer import PortfolioOptimizer, get_action_explanation

# Sample portfolio data
holdings_data = {
    "symbol": ["BTC", "ETH", "ADA", "SOL"],
    "quantity": [0.5, 5.0, 1000.0, 50.0],
    "buy_price_usd": [42000, 2500, 0.60, 180],
    "current_price_usd": [75706, 2351, 0.26, 210],
}

df = pd.DataFrame(holdings_data)
df["total_investment_usd"] = df["quantity"] * df["buy_price_usd"]
df["current_value_usd"] = df["quantity"] * df["current_price_usd"]

print("=" * 80)
print("PORTFOLIO OPTIMIZER TEST")
print("=" * 80)

# Create optimizer
optimizer = PortfolioOptimizer(max_single_exposure=30.0)

# Get current allocation
current = optimizer.calculate_current_allocation(df)
print("\n📊 CURRENT ALLOCATION:")
for symbol, pct in sorted(current.items(), key=lambda x: x[1], reverse=True):
    print(f"  {symbol:5s}: {pct:6.2f}%")

# Get ideal allocation
ideal = optimizer.calculate_ideal_allocation(df)
print("\n🎯 IDEAL ALLOCATION:")
for symbol, pct in sorted(ideal.items(), key=lambda x: x[1], reverse=True):
    print(f"  {symbol:5s}: {pct:6.2f}%")

# Get rebalancing actions
total_value = df["current_value_usd"].sum()
actions = optimizer.calculate_rebalancing_actions(df, current, ideal, total_value)

print(f"\n💰 TOTAL PORTFOLIO VALUE: ${total_value:,.2f}")
print("\n📋 REBALANCING ACTIONS:")
for action in actions:
    symbol = action["symbol"]
    action_type = action["action"]
    amount = action["amount_usd"]
    diff_pct = action["difference_pct"]
    
    if action_type == "Hold":
        status = "✓"
    else:
        status = "↑" if action_type == "Buy" else "↓"
    
    print(f"  {status} {symbol:5s} {action_type:4s}: ${amount:10,.2f} ({diff_pct:+6.2f}%)")

# Get diversification analysis
diversification = optimizer.get_diversification_analysis(current)
print(f"\n📈 DIVERSIFICATION ANALYSIS:")
print(f"  Number of coins:        {diversification['num_coins']}")
print(f"  Largest holding:        {diversification['max_exposure']:.2f}%")
print(f"  Smallest holding:       {diversification['min_exposure']:.2f}%")
print(f"  Diversification score:  {diversification['herfindahl_score']:.1f}/100")
print(f"  Rating:                 {diversification['diversification_rating']}")

# Test action explanations
print("\n💡 SAMPLE ACTION EXPLANATIONS:")
for action in actions[:2]:
    if action["action"] != "Hold":
        explanation = get_action_explanation(
            action["action"],
            action["symbol"],
            action["amount_usd"],
            action["difference_pct"]
        )
        print(f"\n  {action['symbol']} ({action['action']}):")
        print(f"  {explanation}")

print("\n" + "=" * 80)
print("✅ PORTFOLIO OPTIMIZER TEST COMPLETE")
print("=" * 80)
