import streamlit as st
import pandas as pd
import numpy as np

def show():
    st.title("📊 Analysis")
    st.markdown("This is Analysis based on when I chose 3 clusters as a k value")
    st.markdown("As the ideak K value came out to be 3 using elbow method")
    data = {
    "Strategy": ["Channel Priority", "Product Focus", "Promotion Type", "Loyalty Incentives"],
    "Premium Loyalists": ["Digital", "Premium", "Early Access", "VIP Rewards"],
    "Value-Focused Families": ["Email", "Wine", "Family Deals", "Points System"],
    "Budget-Conscious Traditionalists": ["In-Store", "Essentials", "Clearance Sales", "Cashback"]}

    
    df = pd.DataFrame(data)
    st.markdown(" 📈 Actionable Marketing Recommendations ")

    st.markdown("---")
    st.dataframe(df, use_container_width=True,hide_index=True)
    st.markdown("---")
    col1 , col2 , col3 = st.columns(3)
    st.markdown("---")

    with col1:
        st.markdown("<span style='color:gold; font-weight:bold;'>Cluster 1: Premium Loyalists</span>", unsafe_allow_html=True)
        st.markdown("""
        ✅ **Young Demographic**  
        ✅ **Active Online Shoppers and Highest Income**  
        ✅ **Most responsive to marketing Campaigns**
        """)

    with col2:
        st.markdown("<span style='color:gold; font-weight:bold;'>Cluster 0: Value-Focused Families</span>", unsafe_allow_html=True)
        st.markdown("""
        ✅ **Majority are married and family orientated**  
        ✅ **Moderate Income and Wine Products are preferred**  
        ✅ **Responsive to basic campaigns**
        """)

    with col3:
        st.markdown("<span style='color:gold; font-weight:bold;'>Cluster 2: Budget-Conscious Traditionalists</span>", unsafe_allow_html=True)
        st.markdown("""
        ✅ **Older Demographic**  
        ✅ **Prefer offline purchases**  
        ✅ **Unresponsive to campaigns**
        """)

    st.markdown("### 🔑 Key Differentiators")

    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<span style='color:gold; font-weight:bold;'>Cluster 1</span>", unsafe_allow_html=True)
        st.markdown("""
        📈 <span style='font-size:20px; font-weight:bold;'>27.5%</span> higher campaign responsiveness than average.
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<span style='color:gold; font-weight:bold;'>Cluster 2</span>", unsafe_allow_html=True)
        st.markdown("""
        💍 <span style='font-size:20px; font-weight:bold;'></span> More spending on gold products — potential jewelry partnership opportunity.
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("<span style='color:gold; font-weight:bold;'>Cluster 0</span>", unsafe_allow_html=True)
        st.markdown("""
        🍷 <span style='font-size:20px; font-weight:bold;'></span> Wine spending — opportunity for curated wine subscriptions.
        """, unsafe_allow_html=True)