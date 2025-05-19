import streamlit as st
def show():
    st.markdown("<h1 style='text-align: center;'> 🏡 HOME</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: White;'> Uncover Hidden Customer Patterns </h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 What does this app do?"):
            st.markdown("---")
            st.markdown("""
            ### 💡 What This App Does
            - 📊 Performs **K-Means clustering** to group customers based on key features like spending habits and product preferences.
            - 🔍 Helps businesses **identify patterns** in customer behavior.
            - 🎯 Enables **targeted marketing** and improved customer engagement.
            - 📈 Visualizes insights with interactive **scatter plots** and **summary cards**.

            Ready to explore your customers? Click below to begin!
            """)
            
    st.markdown("<h3 style='text-align: center; color: White;'> Use sidebar to navigate to Analytics Section </h2>", unsafe_allow_html=True)
    
