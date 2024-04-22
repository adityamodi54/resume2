import streamlit as st
from streamlit_lottie import st_lottie
import json  # To load and parse the JSON file

def load_lottiefile(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

def render_skills():
    st.markdown("""
        <div class="skills-title">🛠 Skills</div>
        <div class="skills-container">
            <div class="skill-item">Python</div>
            <div class="skill-item">Pandas</div>
            <div class="skill-item">Numpy</div>
            <div class="skill-item">React</div>
            <div class="skill-item">Angular</div>
            <div class="skill-item">Git</div>
            <div class="skill-item">Docker</div>
            <div class="skill-item">Jenkins</div>
            <div class="skill-item">Agile Methodologies</div>
            <div class="skill-item">UX Design</div>
        </div>
    """, unsafe_allow_html=True)

def render_education_and_experience():
    st.markdown("""
        <div>
            <div class="section-title">🎓 Education</div>
            <div class="info-box">
                <div class="info-title">Bachelor of Science in Computer Science</div>
                <div class="info-subtitle">University of California, Berkeley</div>
                <div class="info-footer">2005 - 2009</div>
            </div>
            <!-- Add more education entries if needed -->
        </div>
        <div>
            <div class="section-title">💼 Work Experience</div>
            <div class="info-box">
                <div class="info-title">Senior Software Developer</div>
                <div class="info-subtitle">Tech Solutions Inc., San Francisco, CA</div>
                <div class="info-footer">June 2015 - Present</div>
                <ul class="info-details">
                    <li>Lead a team of 10 developers in creating information systems for clients in the finance industry.</li>
                    <li>Focus on improving application responsiveness and streamline functionalities.</li>
                    <li>Conduct code reviews, mentor junior developers, and manage project timelines.</li>
                </ul>
            </div>
            <!-- Add more work experience entries if needed -->
        </div>
    """, unsafe_allow_html=True)

def main():
    # Load local Lottie animation file
    lottie_animation = load_lottiefile("Animation17.json")  # Ensure the file name matches
    

    # Advanced CSS and HTML for enhanced appearance and icons
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;  /* Light grey background for a softer look */
            color: #333333;
        }
        h1 {
            color: #0068c9; /* Blue for main titles */
        }
        h2, h3 {
            color: #ff6347; /* Tomato red for subheadings */
            margin-top: 40px; /* Space above headers for clarity */
        }
        p, li {
            color: #4a4a4a; /* Dark grey for text for better readability */
            font-size: 18px; /* Larger font size */
        }
        .icon {
            font-size: 25px; /* Size of the icons */
            color: #ff6347; /* Matching the headers */
            padding-right: 10px; /* Space between icon and text */
        }
        .section-title {
            font-weight: bold;
            color: #007bff; /* Blue color for the section titles */
            margin-bottom: 5px;
        }
        .info-box {
            margin-bottom: 20px;
            padding-left: 15px;
            border-left: 3px solid #007bff; /* Blue color for the vertical line */
        }
        .info-title {
            font-weight: bold;
        }
        .info-subtitle {
            color: #555; /* Darker grey for subtitle */
        }
        .info-details {
            margin-top: 5px;
            margin-bottom: 5px;
        }
        .info-footer {
            color: #777; /* Lighter grey for footer (dates, location) */
        }
        .skills-title {
            color: #007bff; /* Blue color for the skills title */
            font-weight: bold;
            margin-bottom: 10px;
        }
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .skill-item {
            background-color: #e1e1e1;
            color: #007bff; /* Blue color for skill text */
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Title with animation
    col1, col2 = st.columns([1, 6])
    with col1:
        # This will display the Lottie animation next to the title
        st_lottie(lottie_animation, height=100, key="resume")
    with col2:
        st.title("Adi's Resume")

    st.markdown("""
        ## 📞 Contact Information
        - **Email:** `jane.doe@example.com`
        - **Phone:** `+1234567890`
        - **Location:** `San Francisco, CA`
    """)
    st.markdown("""
        ## 📝 Professional Summary
        *Experienced software developer with over 10 years of experience specializing in front-end development.
        Strong background in project management and customer relations. Committed to high standards of user experience,
        optimizing performance, and collaborating effectively with team members.*
    """)

    # Render the education and work experience sections
    render_education_and_experience()
    
    # Render the skills section
    render_skills()

if __name__ == "__main__":
    main()
