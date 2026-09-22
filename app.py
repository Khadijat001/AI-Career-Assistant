import streamlit as st

from src.pdf_reader import extract_text_from_pdf
from src.ai_analyzer import analyze_cv
from src.cv_tailor import tailor_cv
from src.cv_exporter import create_docx, create_pdf


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="💼",
    layout="wide"
)

# Custom Styling: Dark, Bold, High-Contrast Theme
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0B0F19 !important;
        color: #FFFFFF !important;
    }

    /* All Text / Paragraphs */
    p, span, div, label {
        color: #E2E8F0 !important;
        font-weight: 600 !important;
    }

    /* Main Page Title */
    h1 {
        color: #00E5FF !important;
        font-size: 3rem !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 12px rgba(0, 229, 255, 0.4);
    }

    /* Section Headings */
    h2 {
        color: #38BDF8 !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
    }

    /* Subheadings */
    h3 {
        color: #7DD3FC !important;
        font-size: 1.5rem !important;
        font-weight: 800 !important;
    }

    /* Inputs, Textareas, and File Uploaders */
    textarea, input, div[data-baseweb="select"], div[data-testid="stFileUploader"] {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 2px solid #334155 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    /* Input Focus States */
    textarea:focus, input:focus {
        border-color: #00E5FF !important;
        box-shadow: 0 0 8px rgba(0, 229, 255, 0.5) !important;
    }

    /* Bold Buttons with High Contrast */
    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(135deg, #00E5FF 0%, #0284C7 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.3s ease !important;
    }

    /* Button Hover Effect */
    .stButton > button:hover, .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #38BDF8 0%, #0369A1 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 15px rgba(0, 229, 255, 0.4) !important;
        transform: translateY(-1px);
    }

    /* Divider Line */
    hr {
        border-color: #334155 !important;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "cv_text" not in st.session_state:
    st.session_state.cv_text = None

if "saved_job_description" not in st.session_state:
    st.session_state.saved_job_description = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "tailored_cv" not in st.session_state:
    st.session_state.tailored_cv = None


# ==========================================
# HEADER
# ==========================================

st.title("AI Career Assistant")

st.write(
    "Upload your CV and paste a job description to understand "
    "your skills, gaps, and interview preparation needs."
)

st.markdown("---")


# ==========================================
# INPUT SECTION
# ==========================================

col1, col2 = st.columns(2)


# CV upload
with col1:

    st.subheader("Upload Your CV")

    uploaded_cv = st.file_uploader(
        "Choose your CV (PDF)",
        type=["pdf"]
    )


# Job description
with col2:

    st.subheader("Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=220,
        placeholder="Paste the job description here..."
    )


st.markdown("")


# ==========================================
# ANALYZE BUTTON
# ==========================================

if st.button("Analyze My CV", use_container_width=True):

    if uploaded_cv is None:

        st.warning("Please upload your CV first.")

    elif not job_description.strip():

        st.warning("Please paste the job description first.")

    else:

        with st.spinner("Analyzing your CV..."):

            # Extract CV text
            cv_text = extract_text_from_pdf(uploaded_cv)

            # Save CV text
            st.session_state.cv_text = cv_text

            # Save job description
            st.session_state.saved_job_description = job_description

            # Analyze CV
            st.session_state.analysis_result = analyze_cv(
                cv_text,
                job_description
            )

            # Clear previous tailored CV
            st.session_state.tailored_cv = None

        st.success("Analysis completed!")


# ==========================================
# DISPLAY ANALYSIS
# ==========================================

if st.session_state.analysis_result:

    st.markdown("---")

    st.header("AI Career Analysis")

    st.markdown(
        st.session_state.analysis_result
    )


    # ======================================
    # DOWNLOAD ANALYSIS
    # ======================================

    st.markdown("---")

    st.subheader("Save Your Analysis")

    st.download_button(
        label="Download Analysis",
        data=st.session_state.analysis_result,
        file_name="AI_Career_Analysis.txt",
        mime="text/plain"
    )


    # ======================================
    # TAILOR CV SECTION
    # ======================================

    st.markdown("---")

    st.header("✍️ Tailor My CV")

    st.write(
        "Create a version of your CV tailored to this specific "
        "job description. The AI will improve the wording and "
        "highlight relevant experience without inventing skills "
        "or qualifications."
    )


    # ======================================
    # GENERATE TAILORED CV
    # ======================================

    if st.button("Generate Tailored CV", use_container_width=True):

        with st.spinner("Creating your tailored CV..."):

            st.session_state.tailored_cv = tailor_cv(
                st.session_state.cv_text,
                st.session_state.saved_job_description
            )

        st.success("Your tailored CV has been created!")


    # ======================================
    # DISPLAY TAILORED CV
    # ======================================

    if st.session_state.tailored_cv:

        st.markdown("---")

        st.subheader("Your Tailored CV")

        # Display the generated CV
        st.text_area(
            "Review your tailored CV before downloading:",
            st.session_state.tailored_cv,
            height=600
        )


        # ==================================
        # CREATE DOWNLOAD FILES
        # ==================================

        docx_file = create_docx(
            st.session_state.tailored_cv
        )

        pdf_file = create_pdf(
            st.session_state.tailored_cv
        )


        # ==================================
        # DOWNLOAD OPTIONS
        # ==================================

        st.subheader("Download Your Tailored CV")

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                label="Download Word (.docx)",
                data=docx_file,
                file_name="Tailored_CV.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )

        with col2:

            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="Tailored_CV.pdf",
                mime="application/pdf",
                use_container_width=True
            )


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "AI Career Assistant • Built with Python, Streamlit and Gemini"
)