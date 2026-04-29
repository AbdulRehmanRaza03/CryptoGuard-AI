"""
Test script for Alert System functionality
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.alert_manager import AlertManager

def test_alert_system():
    """Test the alert system functionality"""
    print("🔔 Testing Alert System...")

    # Initialize alert manager
    alert_manager = AlertManager()

    # Test creating alerts
    print("\n1. Testing alert creation...")

    # Price drop alert
    success1 = alert_manager.create_price_drop_alert("BTC", 5.0)
    print(f"Price drop alert creation: {'✅ Success' if success1 else '❌ Failed'}")

    # High risk alert
    success2 = alert_manager.create_high_risk_alert("SCAM_TOKEN")
    print(f"High risk alert creation: {'✅ Success' if success2 else '❌ Failed'}")

    # Portfolio value alert
    success3 = alert_manager.create_portfolio_value_alert(10.0, "decrease")
    print(f"Portfolio alert creation: {'✅ Success' if success3 else '❌ Failed'}")

    # Test getting active alerts
    print("\n2. Testing alert retrieval...")
    active_alerts = alert_manager.get_active_alerts()
    print(f"Active alerts count: {len(active_alerts)}")

    if not active_alerts.empty:
        print("Active alerts:")
        for _, alert in active_alerts.iterrows():
            print(f"  - {alert['alert_type']}: {alert['symbol'] or 'Portfolio'} ({alert['threshold']}%)")

    # Test alert history
    print("\n3. Testing alert history...")
    history = alert_manager.get_alert_history(limit=10)
    print(f"Alert history count: {len(history)}")

    # Test Telegram settings
    print("\n4. Testing Telegram settings...")
    bot_token, chat_id = alert_manager.get_telegram_settings()
    print(f"Telegram configured: {'✅ Yes' if bot_token and chat_id else '❌ No'}")

    print("\n🎉 Alert system test completed!")

if __name__ == "__main__":
    test_alert_system()