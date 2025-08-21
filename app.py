# app.py

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Rohan Verma | AI & ML Portfolio",
    page_icon="🤖",
    layout="wide",
)

#--- DATA ---
PROJECTS = [
    {
        "title": "MovieVerse",
        "image": "assets/project_movieverse.png",
        "short_description": "A movie recommendation platform built using Streamlit & ML.",
        "long_description": "Placeholder for MovieVerse detailed description.",
        "technologies": ["Python", "Streamlit", "Machine Learning"],
        "github_url": "#",
        "live_demo_url": "#"
    },
    {
        "title": "Fashion MNIST Classifier",
        "image": "assets/project_fashionmnist.png",
        "short_description": "CNN-based image classifier deployed with Streamlit.",
        "long_description": "Placeholder for Fashion MNIST Classifier detailed description.",
        "technologies": ["Python", "TensorFlow", "CNN", "Streamlit"],
        "github_url": "#",
        "live_demo_url": "#"
    },
    {
        "title": "Text Transformer App",
        "image": "assets/project_texttransformer.png",
        "short_description": "Summarization & paraphrasing app with NLP models.",
        "long_description": "Placeholder for Text Transformer App detailed description.",
        "technologies": ["Python", "NLP", "Transformers", "Streamlit"],
        "github_url": "#",
        "live_demo_url": "#"
    },
    {
        "title": "Project Placeholder 1",
        "image": "assets/project_placeholder1.png",
        "short_description": "Short description here.",
        "long_description": "Long description placeholder. Replace with your project details.",
        "technologies": ["Tech1", "Tech2", "Tech3"],
        "github_url": "#",
        "live_demo_url": "#"
    },
    {
        "title": "Project Placeholder 2",
        "image": "assets/project_placeholder2.png",
        "short_description": "Short description here.",
        "long_description": "Long description placeholder. Replace with your project details.",
        "technologies": ["Tech1", "Tech2", "Tech3"],
        "github_url": "#",
        "live_demo_url": "#"
    }
]
CERTIFICATIONS = [
  {
    "title": "Machine Learning Specialization",
    "issuer": "DeepLearning.AI | Coursera",
    "date": "july 2025",
    "credential_url": "https://coursera.org/share/ef42cab780762c685b25c605cbe5de5d"
  },
  {
    "title": "Applied Data Science",
    "issuer": "IBM",
    "date": "June 2025",
    "credential_url": "https://www.credly.com/badges/cebd4bea-6956-4143-aadd-6f9061ad0a60/public_url"
  },
  {
    "title": "Data Analytics",
    "issuer": "ICT Academy",
    "date": "Feb 2025",
    "credential_url": "https://drive.google.com/file/d/1vY0c07UQjRXnzyEi7cWhF1yccaMpaN8h/view?usp=drive_link"
  },
  {
    "title": "Data Science and Machine Learning",
    "issuer": "O7 Services",
    "date": "July 2024",
    "credential_url": "https://drive.google.com/file/d/1xMJzkpGRlJ1elvX3ouG-DMjNHyMrzaY_/view?usp=drive_link"
  },
  {
    "title": "Python Fundamentals",
    "issuer": "O7 Services",
    "date": "July 2023",
    "credential_url": "https://drive.google.com/file/d/1X_7mPh6-u9xLJxM3PLHNT4zlbfRA_D6c/view?usp=drive_link"
  },
]

# Updated SKILLS data structure to include logos
SKILLS = {
    "All Skills": [
        "LangChain",
        "LangGraph",
        "FastAPI",
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "N8N",
        "Hugging Face",
        "Docker",
        "Git",
        "GitHub",
        'PowerBI'
        
    ]
}



# --- SIDEBAR ---
with st.sidebar:
    try:
        profile_pic = Image.open("assets/profile_picture.png")
        st.image(profile_pic, width=200)
    except FileNotFoundError:
        st.error("Profile picture not found.")

    st.title("Rohan Verma")
    st.write("Aspiring AI Engineer | Data Scientist")
    
    try:
        with open("assets/resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="Rohan_resume.pdf",
            mime='application/octet-stream',
            use_container_width=True
        )
    except FileNotFoundError:
        st.warning("Resume file not found.")
    st.write("---")
    
    selected = option_menu(
        menu_title=None,
        options=["About", "Projects", "Skills", "Certifications", "Contact"],
        icons=["person", "code-slash", "bar-chart", "patch-check", "envelope"],
        default_index=0,
    )

    # Resume Download

# --- PAGE CONTENT ---

# ABOUT PAGE
if selected == "About":
    st.title("About Me")
    st.write("---")
    
    st.header("Crafting Intelligent Solutions with Data and AI")
    st.write("""
👋 👋 Hi, I'm Rohan Verma, a recent graduate from DAV University with a GPA of 8.4+. I'm passionate about AI and Data Science and currently looking forward to any opportunities. I enjoy transforming complex datasets into intelligent, automated systems that solve real-world challenges. This portfolio showcases my projects, skills, and certifications. Explore and feel free to connect with me!
    """)
    st.subheader("Connect with me:")
    st.markdown(
        """
        <div style="display: flex; gap: 20px; margin-top: 10px;">
            <a href="https://www.linkedin.com/in/rohan-verma-3b95a026a/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
            </a>
            <a href="https://github.com/rverma345" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40">
            </a>
            <a href="mailto:vermaron9@gmail.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="40">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# PROJECTS PAGE

elif selected == "Projects":
    st.title("Project Showcase")
    st.write("---")
    
    PROJECTS = [
        {
            "title": "Movie Recommender System",
            "short_description": "A personalized movie recommendation app using TMDB dataset and API.",
            "technologies": [
                "Python", "Streamlit", "TMDB API", "Cosine Similarity", "Pandas"
            ],
            "long_description": """
• Developed movie recommendation application leveraging the TMDB dataset and TMDB API.
• Implemented a robust similarity search mechanism using cosine similarity to provide personalized movie suggestions.
• Designed a multi-page interactive interface using Streamlit, featuring a Movie Details page, Trending Movies page,
and comprehensive search functionality for an intuitive user experience.
"""
        },
        {
            "title": "Text Transformer App",
            "short_description": "Real-time text summarization and paraphrasing application using NLP models.",
            "technologies": [
                "Python", "Streamlit", "T5", "BART", "spaCy", "SpeechRecognition", "gTTS"
            ],
            "long_description": """
• Developed an NLP application for real-time text summarization and paraphrasing using fine-tuned T5 and BART models.
• Integrated spaCy and custom spell-checking logic for NER and grammar correction; added speech-to-text and text-to-speech features.
• Designed an interactive Streamlit interface enabling users to perform advanced NLP tasks with minimal technical input.
"""
        }
    ]
    
    for project in PROJECTS:
        st.subheader(project['title'])
        st.write(project['short_description'])
        st.markdown(project['long_description'])
        st.markdown(f"**Technologies:** `{'`, `'.join(project['technologies'])}`")
        st.write("---")

# SKILLS PAGE
elif selected == "Certifications":
    st.title("Professional Certifications")
    st.write("---")
    
    for cert in CERTIFICATIONS:
        st.subheader(cert['title'])
        st.write(f"**Issued by:** {cert['issuer']} ({cert['date']})")
        
        if cert.get('credential_url') and cert['credential_url'] != "#":
            st.markdown(f"[View Certificate]({cert['credential_url']})", unsafe_allow_html=True)
        else:
            st.info("Certificate link not available.")
        
        st.write("---")

# SKILLS PAGE
elif selected == "Skills":
    st.title("Technical Skills")
    st.write("---")
    
    all_skills = SKILLS["All Skills"]
    NUM_COLS = 4
    cols = st.columns(NUM_COLS)
    
    for i, skill_name in enumerate(all_skills):
        with cols[i % NUM_COLS]:
            st.markdown(f"- {skill_name}")
# CONTACT PAGE
elif selected == "Contact":
    st.title("Get In Touch")
    st.write("---")
    st.write("I'm open to new opportunities and collaborations. Feel free to reach out via any of the platforms below:")

    # Contact Info with Icons
    contact_info = [
        {
            "platform": "LinkedIn",
            "icon": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
            "link": "https://www.linkedin.com/in/rohan-verma-3b95a026a/"
        },
        {
            "platform": "GitHub",
            "icon": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
            "link": "https://github.com/rverma345/"
        },
        {
            "platform": "Email",
            "icon": "https://cdn-icons-png.flaticon.com/512/732/732200.png",
            "link": "mailto:vermaron9@gmail.com"
        }
    ]

    # Display in a row
    cols = st.columns(len(contact_info))
    for col, info in zip(cols, contact_info):
        with col:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <a href="{info['link']}" target="_blank">
                        <img src="{info['icon']}" width="50">
                    </a>
                    <p style="margin-top:5px;">{info['platform']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
