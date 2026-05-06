"""
Streamlit app for fetching live cryptocurrency prices from CoinGecko.
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import streamlit as st
from dotenv import load_dotenv

from utils.api_handler import fetch_live_price


load_dotenv()


st.set_page_config(
    page_title="Crypto Price Tracker",
    page_icon="🪙",
    layout="centered",
)


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #08111f 0%, #12233a 45%, #1a3554 100%);
        color: #eef4ff;
    }
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2.5rem;
    }
    .price-card {
        background: rgba(10, 22, 40, 0.72);
        border: 1px solid rgba(90, 189, 255, 0.25);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.28);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("Live Crypto Price Tracker")
st.caption("Search a coin by name or symbol and fetch its live USD price from CoinGecko.")


@st.cache_data(ttl=60)
def get_live_price_cached(coin_name: str, api_key: Optional[str]) -> Dict[str, Any]:
    """Cache CoinGecko lookups for 60 seconds."""
    _ = api_key
    return fetch_live_price(coin_name)

with st.container():
    st.markdown('<div class="price-card">', unsafe_allow_html=True)
    coin_name = st.text_input("Coin name", placeholder="Bitcoin, Ethereum, solana, btc")
    api_key_present = bool(os.getenv("COINGECKO_API_KEY"))
    st.caption("CoinGecko API key loaded from .env" if api_key_present else "No CoinGecko API key found in .env; public access will be used where allowed.")

    if st.button("Fetch live price", type="primary"):
        if not coin_name.strip():
            st.error("Enter a coin name or symbol first.")
        else:
            with st.spinner("Fetching live price from CoinGecko..."):
                result = get_live_price_cached(coin_name.strip(), os.getenv("COINGECKO_API_KEY"))

            if result.get("success"):
                coin = result["coin"]
                st.success(f"Matched {coin['name']} ({coin['symbol']})")
                st.metric("Live USD Price", f"${result['price_usd']:,.6f}")

                col1, col2 = st.columns(2)
                with col1:
                    market_cap = result.get("market_cap")
                    st.metric("Market Cap", f"${market_cap:,.0f}" if market_cap is not None else "N/A")
                with col2:
                    volume_24h = result.get("volume_24h")
                    st.metric("24h Volume", f"${volume_24h:,.0f}" if volume_24h is not None else "N/A")

                change_24h = result.get("change_24h")
                if change_24h is not None:
                    delta_label = f"{change_24h:+.2f}%"
                    if change_24h >= 0:
                        st.success(f"24h Change: {delta_label}")
                    else:
                        st.error(f"24h Change: {delta_label}")
            else:
                st.error(result.get("error", "Unable to fetch the live price."))

    st.markdown("</div>", unsafe_allow_html=True)
