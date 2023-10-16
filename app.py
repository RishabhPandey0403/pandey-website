from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "rishabh-pandey-resume.pdf"
profile_pic = current_dir / "assets" / "headshot.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Rishabh Pandey"
PAGE_ICON = "🅿️"
NAME = "Rishabh Pandey"
DESCRIPTION = """
Student @ Purdue University
"""
EMAIL = "email.rishabhp@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pandey-rishabh",
    "GitHub": "https://github.com/RishabhPandey0403",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Create the sidebar menu
st.sidebar.title("Navigation")

# Define the menu options and corresponding page titles
menu = {
    "Home": "Home",
    "Experience & Qualifications": "Experience & Qualifications",
    "Technical Skills": "Technical Skills",
    "Work History": "Work History",
    "Projects & Accomplishments": "Projects & Accomplishments",
}

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
def home():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    # --- SOCIAL LINKS ---
    st.write('\n')
    for platform, link in SOCIAL_MEDIA.items():
        st.write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
def experience():
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write(
        """
    - ✔️ Software Development Intern at Agrofocal Technologies
    - ✔️ Software Engineer Intern at Texas Instruments
    - ✔️ IT & Analytics Head at Alpha Kappa Psi (Pi Omega Chapter)
    """
    )

# --- SKILLS ---
def skills():
    st.write('\n')
    st.subheader("Technical Skills")
    st.write(
        """
    - Languages: Python, Java, C, SQL, PL/SQL, Javascript, Swift
    - Developer Tools: Git, AWS, Postman, Insomnia, MySQL, Oracle ERP
    - Libraries/Frameworks: Pandas, NumPy, Tensorflow, Pytorch, Keras, Sklearn, FastAPI, Django, Flask
    """
    )

# --- WORK HISTORY ---
def work_history():
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # Software Development Intern
    st.write("🚧", "**Software Development Intern | Agrofocal Technologies**")
    st.write("Aug 2023 - Present")
    st.write(
        """
    - Conducting systematic error analysis while preparing 1000s of images for TensorRT models.
    - Improving the accuracy of crop yield prediction models by fine-tuning scripts to extract relevant features from video data.
    - Creating scripts that utilize multiprocessing for a 'Compute Box' with the goal of decreasing the computational time required by machine learning algorithms to perform analysis on different crops.
    """
    )

    # Software Engineer Intern
    st.write('\n')
    st.write("🚧", "**Software Engineer Intern | Texas Instruments**")
    st.write("May 2023 - Aug 2023")
    st.write(
        """
    - Developed an Oracle APEX application that manages software licenses for over 100+ products sold by the company.
    - Integrated with 10Duke’s REST API to retrieve and display customer personal details based on the activation code in real-time.
    - Enhanced customer support efficiency and satisfaction by reducing information retrieval time from an average of 4-6 hours to roughly 5-10 seconds.
    - Wrote shell scripts to archive invalid packages within the system, playing a pivotal role in preparing the team for an Oracle upgrade.
    """
    )

    # IT & Analytics Head
    st.write('\n')
    st.write("🚧", "**IT & Analytics Head | Alpha Kappa Psi (Pi Omega Chapter)**")
    st.write("Dec 2022 - May 2023")
    st.write(
        """
    - Spearheaded the development of a web application for Alpha Kappa Psi, which will allow brothers to query alumni based on specific criteria, resulting in increased engagement and connection within the fraternity.
    - Designed and implemented an interactive map using Power BI, which will plot the current locations of alumni, providing valuable insights into the distribution of alumni across different regions.
    """
    )

# --- PROJECTS & ACCOMPLISHMENTS ---
def projects():
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")

    # Real-time Stock Market Analyzer
    st.write("🏆", "**Real-time Stock Market Analyzer**")
    st.write("Sept 2023 - Present")
    st.write(
        """
    Implemented a Kafka streaming pipeline that collects and processes real-time stock data from the Nasdaq Data Link.
    Built a Python script that uses the Twilio API to send text alerts whenever a particular stock crosses the Bollinger Bands.
    """
    )

    # Daily News
    st.write('\n')
    st.write("🏆", "**Daily News**")
    st.write("July 2023 - Aug 2023")
    st.write(
        """
    Developed a Python script that leverages NewsAPI to generate and store catchy news headlines from various sources and categories.
    Incorporated AWS EC2 cluster to automate daily text messages with curated news titles to friends and family.
    """
    )

# Create separate sections for each page
if st.experimental_get_query_params().get("page") == "home":
    st.title("Home")
    # Add content for the Home page here
    home()
elif st.experimental_get_query_params().get("page") == "experience":
    st.title("Experience & Qualifications")
    # Add content for the Experience & Qualifications page here
    experience()
elif st.experimental_get_query_params().get("page") == "skills":
    st.title("Technical Skills")
    # Add content for the Technical Skills page here
    skills()
elif st.experimental_get_query_params().get("page") == "work_history":
    st.title("Work History")
    # Add content for the Work History page here
    work_history()
elif st.experimental_get_query_params().get("page") == "projects":
    st.title("Projects & Accomplishments")
    # Add content for the Projects & Accomplishments page here
    projects()

# Create a selectbox in the sidebar for navigation
selected_page = st.sidebar.selectbox("Go to", list(menu.keys()))
if selected_page == "Home":
    st.title("Home")
    home()
elif selected_page == "Experience & Qualifications":
    st.title("Experience & Qualifications")
    experience()
elif selected_page == "Technical Skills":
    st.title("Technical Skills")
    skills()
elif selected_page == "Work History":
    st.title("Work History")
    work_history()
elif selected_page == "Projects & Accomplishments":
    st.title("Projects & Accomplishments")
    projects()