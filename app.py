import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(
    page_title="AI Social Media Creator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            padding-top: 2rem;
        }
        .stTitle {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 2rem;
        }
        .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-size: 1.1rem;
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 8px;
            width: 100%;
            font-weight: 600;
            transition: transform 0.2s;
        }
        .stButton>button:hover {
            transform: scale(1.02);
        }
        /* Improved output box for better contrast and readability */
        .output-box {
            background: linear-gradient(180deg, #eef2f7 0%, #d6e0ec 100%);
            padding: 1.5rem 2rem;
            border-radius: 12px;
            border-left: 4px solid #667eea;
            color: #0f172a !important;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
            font-size: 15px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        /* Ensure any nested tags inside the output also inherit a readable color */
        .output-box, .output-box * {
            color: #0f172a !important;
        }
    </style>
""", unsafe_allow_html=True)

# NVIDIA NIM API setup
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_NVIDIA_API_KEY"  # Replace with your actual API key
)

# Header section
st.markdown("<h1 style='text-align: center; margin-bottom: 0.5rem;'>🚀 AI Social Media Creator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle' style='text-align: center;'>✨ Generate engaging social media content in seconds powered by AI</p>", unsafe_allow_html=True)

# Divider
st.divider()

# Main content in columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Content Settings")
    topic = st.text_input(
        "🎯 What's your topic?",
        placeholder="e.g., Web Development, AI, Python Tips..."
    )
    
with col2:
    st.subheader("⚙️ Customize Output")
    tone = st.selectbox(
        "🎭 Select Tone",
        ["Professional", "Casual", "Marketing", "Funny"]
    )
    
    platform = st.selectbox(
        "📱 Select Platform",
        ["LinkedIn", "Instagram", "Twitter/X"]
    )

st.divider()

# Generate button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate_btn = st.button("✨ Generate Content", key="generate", use_container_width=True)

# Generate content
if generate_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic first!")
    else:
        with st.spinner("🤖 Creating amazing content..."):
            prompt = f"""
            Generate a {tone} style social media post about {topic}
            for {platform}.

            Also generate:
            - hashtags (relevant and trending)
            - short engagement hook (one catchy line)
            - AI image prompt suggestion
            
            Format the output clearly with sections.
            """

            response = client.chat.completions.create(
                model="meta/llama-3.1-70b-instruct",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

            output = response.choices[0].message.content

            # Display output with styling
            st.divider()
            st.markdown("<h2 style='color: #667eea;'>📊 Generated Content</h2>", unsafe_allow_html=True)
            st.markdown(f"<div class='output-box'>{output}</div>", unsafe_allow_html=True)
            
            # Copy button
            st.success("✅ Content generated successfully!")
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st.write("")
                st.info("💡 Copy the content above and customize as needed!")
