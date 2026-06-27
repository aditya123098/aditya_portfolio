import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ADITYA THAKUR | AI & ML Portfolio",
    page_icon="🤖",
    layout="wide",
)

#--- DATA ---
PROJECTS = [
    {
        "title": "Indian Cybercrime Legal RAG Assistant",
        "short_description": "RAG application for Indian cyber law research providing AI-generated legal analysis.",
        "long_description": """
• Built a Retrieval-Augmented Generation (RAG) application for Indian cyber law research, enabling users to describe situations in plain English and receive AI-generated legal analysis grounded in the IT Act 2000, IPC, and BNS 2023.
• Designed and curated a structured dataset of 153 real-world cybercrime scenarios across 12 categories with mapped legal sections, explanations, and punishments.
• Engineered a semantic search pipeline using FAISS vector indexing and Sentence-Transformers (all-MiniLM-L6-v2) embeddings to retrieve the most relevant legal provisions for any user query with sub-second latency.
• Implemented a LangChain-based RAG chain that retrieves context from the FAISS vector store, formats multi-field legal metadata, and generates grounded responses via Groq-hosted LLaMA-3.3-70B with temperature-controlled inference.
• Developed a conversational Streamlit interface with chat history, configurable retrieval depth (top-k), example query shortcuts, source transparency, and sidebar API key management.
• Ensured privacy-first architecture by running all embedding generation locally on-device, with no user data leaving the machine during indexing.
""",
        "technologies": ["Python", "LangChain", "RAG", "FAISS", "Sentence-Transformers", "Groq", "LLaMA-3.3-70B", "Streamlit"]
    },
    {
        "title": "PDF Q&A RAG Application",
        "short_description": "Intelligent PDF Question-Answering system using LangChain, PyPDF, Hugging Face Transformers, and FAISS.",
        "long_description": """
• Built an intelligent PDF Question-Answering system using LangChain, PyPDF, Hugging Face Transformers, and FAISS for document querying.
• Developed complete pipeline: PDF text extraction, chunking, embedding creation using sentence-transformers, and similarity-based semantic retrieval.
• Integrated open-source LLaMA models for accurate response generation; optimized retrieval via chunk-size tuning and metadata filtering.
• Achieved 85-90% relevance accuracy on user test cases; deployed with a clean Streamlit-based UI on Hugging Face Spaces.
""",
        "technologies": ["Python", "LangChain", "RAG", "Generative AI", "FAISS", "Streamlit", "Hugging Face"]
    },
    {
        "title": "YouTube Q&A RAG Application",
        "short_description": "YouTube-based RAG application for transcript-based question answering.",
        "long_description": """
• Developed a YouTube-based Retrieval-Augmented Generation (RAG) application for transcript-based question answering using LangChain, Streamlit, and Hugging Face Transformers.
• Implemented end-to-end pipeline: YouTube transcript extraction, text chunking, embedding generation via sentence transformers, and semantic retrieval using FAISS vector database.
• Integrated open-source LLMs for contextual answer generation; achieved 90%+ answer relevancy on evaluation queries.
• Designed interactive Streamlit interface and deployed on Hugging Face Spaces for public access.
""",
        "technologies": ["Python", "LangChain", "RAG", "FAISS", "Sentence Transformers", "Streamlit", "Hugging Face"]
    }
]

EXPERIENCE = [
  {
    "title": "Deep Learning & NLP Trainee",
    "company": "Coder Roots",
    "date": "June 2025 – July 2025",
    "description": """
• Developed a production-ready PDF Q&A RAG application enabling users to upload documents and generate contextual question-answer pairs using LangChain, Streamlit, and Generative AI.
• Implemented complete RAG pipeline covering PDF text extraction, text chunking, embedding generation, and semantic retrieval with FAISS vector database.
• Utilized technologies: Python, LangChain, RAG, Generative AI, Streamlit, HTML, CSS.
• Deployed application publicly on Hugging Face Spaces, demonstrating end-to-end MLOps skills.
"""
  },
  {
    "title": "Data Science & Machine Learning Trainee",
    "company": "O7 Services",
    "date": "June 2024 – September 2024",
    "description": """
• Built and deployed predictive CNN models and interactive data applications using Streamlit.
• Processed large datasets using Pandas and NumPy; conducted EDA and implemented regression, classification, and clustering models.
• Delivered an end-to-end ML cloth prediction application, demonstrating full project lifecycle execution.
"""
  }
]

EDUCATION = [
  {
      "degree": "B.Tech in Computer Science & Engineering",
      "institution": "DAV University",
      "year": "2022 – 2026"
  },
  {
      "degree": "Senior Secondary (12th Grade)",
      "institution": "S.D.S.V.M Talwara",
      "year": "2021 – 2022 | 74.6%"
  },
  {
      "degree": "Secondary (10th Grade)",
      "institution": "S.D.S.V.M Talwara",
      "year": "2018 – 2019 | 79.8%"
  }
]

SKILLS = {
    "All Skills": [
        "LangChain",
        "Hugging Face Transformers",
        "OpenAI API",
        "Prompt Engineering",
        "Agentic Workflows",
        "TensorFlow",
        "PyTorch",
        "Scikit-Learn",
        "RAG",
        "Sentence Transformers",
        "FAISS",
        "Pinecone",
        "FastAPI",
        "Python",
        "SQL",
        "HTML / CSS",
        "Streamlit",
        "Docker",
        "Git & GitHub",
        "CI/CD",
        "Pandas",
        "NumPy",
        "EDA"
    ]
}


# --- SIDEBAR ---
with st.sidebar:
    try:
        profile_pic = Image.open("assets/profile_picture.jpg")
        st.image(profile_pic, width=200)
    except FileNotFoundError:
        pass # Silently fail if not found, standard Streamlit practice

    st.title("ADITYA THAKUR")
    st.write("AI Engineer | LLM Applications | RAG Pipelines | NLP")
    
    try:
        with open("assets/resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="Aditya_Thakur_Resume.pdf",
            mime='application/octet-stream',
            use_container_width=True
        )
    except FileNotFoundError:
        st.warning("Resume file not found.")
    st.write("---")
    
    selected = option_menu(
        menu_title=None,
        options=["About", "Experience & Education", "Projects", "Skills", "Contact"],
        icons=["person", "briefcase", "code-slash", "batch-chart", "envelope"],
        default_index=0,
    )


# --- PAGE CONTENT ---

# ABOUT PAGE
if selected == "About":
    st.title("About Me")
    st.write("---")
    
    st.header("AI Engineer | LLM Applications | RAG Pipelines | NLP")
    st.write("""
👋 Hi, I'm **Aditya Thakur**.

AI Engineer with hands-on experience building and deploying LLM-based applications, Retrieval-Augmented Generation (RAG) pipelines, and NLP solutions. Proficient in LangChain, Hugging Face Transformers, Python, and vector databases (FAISS, Pinecone). 

I have a demonstrated ability to architect end-to-end AI systems from data ingestion through model deployment, achieving 85-90%+ answer relevancy benchmarks. Adept at prompt engineering, agentic workflows, and optimizing system accuracy and scalability using Docker and CI/CD practices.
    """)
    st.subheader("Connect with me:")
    st.markdown(
        """
        <div style="display: flex; gap: 20px; margin-top: 10px;">
            <a href="https://www.linkedin.com/in/aditya-thakur-735110258/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
            </a>
            <a href="https://github.com/aditya123098" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40">
            </a>
            <a href="mailto:adityathakur0123321@gmail.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="40">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# EXPERIENCE & EDUCATION PAGE
elif selected == "Experience & Education":
    st.title("Professional Experience")
    st.write("---")
    
    for exp in EXPERIENCE:
        st.subheader(exp['title'])
        st.write(f"**{exp['company']}** | {exp['date']}")
        st.markdown(exp['description'])
        st.write("---")
        
    st.title("Education")
    st.write("---")
    for edu in EDUCATION:
        st.subheader(edu['degree'])
        st.write(f"**{edu['institution']}** | {edu['year']}")
        st.write("---")

# PROJECTS PAGE
elif selected == "Projects":
    st.title("Project Showcase")
    st.write("---")
    
    for project in PROJECTS:
        st.subheader(project['title'])
        st.write(project['short_description'])
        st.markdown(project['long_description'])
        st.markdown(f"**Technologies:** `{'`, `'.join(project['technologies'])}`")
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
            "link": "https://www.linkedin.com/in/aditya-thakur-735110258/"
        },
        {
            "platform": "GitHub",
            "icon": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
            "link": "https://github.com/aditya123098"
        },
        {
            "platform": "Email",
            "icon": "https://cdn-icons-png.flaticon.com/512/732/732200.png",
            "link": "mailto:adityathakur0123321@gmail.com"
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
