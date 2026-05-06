"""
CryptoGuard AI - Premium cryptocurrency portfolio dashboard.
"""

from __future__ import annotations

import streamlit as st

from utils.ui import inject_global_styles


st.set_page_config(
    page_title="CryptoGuard AI | FinTech Portfolio Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/AbdulRehmanRaza03/CryptoGuard-AI",
        "Report a bug": "https://github.com/AbdulRehmanRaza03/CryptoGuard-AI/issues",
        "About": "CryptoGuard AI - Premium crypto portfolio and risk dashboard",
    },
)

inject_global_styles()

with st.sidebar:
    st.markdown(
        """
        <div style="padding:0.4rem 0 0.8rem 0;">
            <div style="font-size:1.55rem;font-weight:800;letter-spacing:-0.04em;">🛡️ CryptoGuard AI</div>
            <div style="color:rgba(237,242,255,0.72);margin-top:0.35rem;line-height:1.5;">
                Professional portfolio monitoring, live pricing, and wallet risk intelligence.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Pages are available from the sidebar navigation.")
    st.divider()
    st.markdown("### What’s inside")
    st.write("• Live Portfolio"); st.write("• Market Dashboard"); st.write("• Scam Detector"); st.write("• Portfolio Optimizer")
    st.divider()
    st.markdown("[GitHub](https://github.com/AbdulRehmanRaza03/CryptoGuard-AI)")
    st.markdown("[Issues](https://github.com/AbdulRehmanRaza03/CryptoGuard-AI/issues)")


def main() -> None:
    # Hero section with value proposition
    st.markdown(
        """
        <div style="text-align:center;padding:2rem 0;">
            <h1 style="font-size:3.2rem;margin:0;letter-spacing:-0.05em;">🛡️ Take Control of Your Crypto</h1>
            <p style="font-size:1.25rem;color:rgba(237,242,255,0.75);margin-top:1rem;margin-bottom:0;">
                Monitor. Analyze. Protect. Your complete cryptocurrency portfolio intelligence platform.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.divider()
    
    # Feature cards with icons and benefits
    st.markdown("### ⚡ Core Features")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            """
            <div style="background:rgba(56,189,248,0.1);border:1px solid rgba(56,189,248,0.3);border-radius:1rem;padding:1.5rem;text-align:center;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem;">💼</div>
                <h3 style="margin:0.5rem 0;font-size:1.1rem;">Live Portfolio</h3>
                <p style="color:rgba(237,242,255,0.7);font-size:0.9rem;margin:0;">Real-time price updates & gains/losses</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            """
            <div style="background:rgba(52,211,153,0.1);border:1px solid rgba(52,211,153,0.3);border-radius:1rem;padding:1.5rem;text-align:center;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem;">📊</div>
                <h3 style="margin:0.5rem 0;font-size:1.1rem;">Market Dashboard</h3>
                <p style="color:rgba(237,242,255,0.7);font-size:0.9rem;margin:0;">Analytics & performance tracking</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col3:
        st.markdown(
            """
            <div style="background:rgba(251,113,133,0.1);border:1px solid rgba(251,113,133,0.3);border-radius:1rem;padding:1.5rem;text-align:center;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem;">🔍</div>
                <h3 style="margin:0.5rem 0;font-size:1.1rem;">Risk Analysis</h3>
                <p style="color:rgba(237,242,255,0.7);font-size:0.9rem;margin:0;">Volatility & concentration scoring</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col4:
        st.markdown(
            """
            <div style="background:rgba(94,234,212,0.1);border:1px solid rgba(94,234,212,0.3);border-radius:1rem;padding:1.5rem;text-align:center;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem;">🚨</div>
                <h3 style="margin:0.5rem 0;font-size:1.1rem;">Scam Detection</h3>
                <p style="color:rgba(237,242,255,0.7);font-size:0.9rem;margin:0;">Wallet security & risk alerts</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    st.divider()
    
    # Why CryptoGuard section
    st.markdown("### 🎯 Why CryptoGuard AI?")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            ✅ **Real-time Market Data**  
            Live prices from CoinGecko with intelligent caching
            
            ✅ **Advanced Risk Scoring**  
            Volatility analysis, concentration metrics, and diversification insights
            
            ✅ **Security First**  
            Etherscan-powered wallet analysis to detect scam patterns
            
            ✅ **Smart Optimization**  
            AI-driven rebalancing recommendations for portfolio growth
            """
        )
    
    with col2:
        st.markdown(
            """
            ✅ **One-Click Analytics**  
            Comprehensive dashboards with minimal setup
            
            ✅ **PKR Conversion**  
            Automatic USD ↔ PKR exchange rates for local insights
            
            ✅ **Portfolio History**  
            Track snapshots over time to see growth trends
            
            ✅ **Open Source**  
            Community-driven, transparent, and always improving
            """
        )
    
    st.divider()
    
    # Call-to-action section
    st.markdown("### 🚀 Get Started in 30 Seconds")
    
    action_col1, action_col2, action_col3 = st.columns(3)
    
    with action_col1:
        if st.button("📈 View Live Portfolio", use_container_width=True, key="cta_portfolio"):
            st.switch_page("pages/2_Portfolio.py")
    
    with action_col2:
        if st.button("📊 Market Dashboard", use_container_width=True, key="cta_dashboard"):
            st.switch_page("pages/5_Dashboard.py")
    
    with action_col3:
        if st.button("🔐 Scan Wallet Risk", use_container_width=True, key="cta_scam"):
            st.switch_page("pages/4_Scam_Detector.py")
    
    st.divider()
    
    # Stats and social proof
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Features", "7+", "Core Tools")
    with col2:
        st.metric("Data Refresh", "<1s", "Real-time")
    with col3:
        st.metric("Support", "Active", "Community")
    
    st.divider()
    
    # Footer with additional info
    st.markdown(
        """
        <div style="text-align:center;color:rgba(237,242,255,0.6);padding:2rem 0;font-size:0.9rem;">
            <p>🛡️ CryptoGuard AI | Premium Portfolio Intelligence Platform</p>
            <p>Built with ❤️ for the crypto community | <a href="https://github.com/AbdulRehmanRaza03/CryptoGuard-AI" style="color:#5eead4;">Open Source on GitHub</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
