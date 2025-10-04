import streamlit as st
from few_shot import FewShotPosts
from generate_post import generate_post

# Page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 0.5em 1.5em;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
        }
        .stSelectbox label {
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown("## 💼 LinkedIn Post Generator")
    st.markdown("Create engaging, AI-powered LinkedIn posts with a single click ✨")
    st.markdown("---")

    # Input options
    fs = FewShotPosts()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_tag = st.selectbox("🎯 Select Title", options=sorted([tag.upper() for tag in fs.get_tags()]))

    with col2:
        selected_length = st.selectbox("📝 Select Length", options=["Short", "Medium", "Long"])
    
    with col3:
        selected_language = st.selectbox("🌐 Select Language", options=["English", "Hinglish"])

    st.markdown("")

    # Button and output
    if st.button("🚀 Generate Post"):
        with st.spinner("Generating your post... ✍️"):
            post = generate_post(selected_length, selected_language, selected_tag)
            formatted_post = post.strip().replace("\n", "  \n")  # Ensure proper markdown line breaks
            st.markdown("### ✅ Your Generated Post:")
            st.markdown(f"{formatted_post}")
    else:
        st.info("Click 'Generate Post' to get started.")

if __name__ == "__main__":
    main()
