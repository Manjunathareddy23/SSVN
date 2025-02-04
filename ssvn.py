import streamlit as st

# Page Configuration
st.set_page_config(page_title="Sri Sreenivasa Vidhyanikethan High School", layout="wide")

# Header
st.markdown("""
    <style>
    .header {text-align: center;}
    .header h1 {font-size: 40px;}
    .header p {font-size: 20px;}
    </style>
    <div class="header">
        <h1>Sri Sreenivasa Vidhyanikethan High School</h1>
        <p>Education for all</p>
    </div>
""", unsafe_allow_html=True)

# Navigation Menu
menu = ['Home', 'About', 'Academics', 'Gallery', 'Contact']
choice = st.sidebar.radio("Menu", menu)

# Hero Section (Marquee)
if choice == 'Home':
    st.markdown("""
        <div class="hero">
            <marquee><h1>Sri Sreenivasa Vidhyanikethan High School</h1></marquee>
        </div>
    """, unsafe_allow_html=True)

# About Section
if choice == 'About':
    st.subheader("About Our School")
    st.markdown("""
        **Established Date:**  
        Sri Sreenivasa Vidhyanikethan High School, Beluguppa was established in 2006.
        
        **Our Mission:**  
        Our mission is to provide high-quality education to students of all ages and backgrounds.
        
        **More Info:**  
        SREENIVASA VIDYA NIKETAN was established in 2006 and it is managed by the Pvt. Unaided...
    """)
    
    # Principal Info
    st.subheader("Principal")
    st.image("https://picsum.photos/200", caption="V.Sreenivasulu Ph.D")
    st.markdown("""
        **V.Sreenivasulu Ph.D**  
        V.Sreenivasulu has been the principal of Sri Sreenivasa Vidhyanikethan High School...
    """)

# Academics Section
if choice == 'Academics':
    st.subheader("Academics")
    st.markdown("""
        **Pre-primary:**  
        Age: 3-5 years, Nursery, LKG, UKG

        **Primary:**  
        Class 1 to Class 5

        **Higher Secondary:**  
        Class 6 to Class 10
    """)

# Gallery Section
if choice == 'Gallery':
    st.subheader("Gallery")
    st.image("https://picsum.photos/300/200", caption="Image description title here...")

# Contact Section
if choice == 'Contact':
    st.subheader("Contact Us")
    st.markdown("""
        **Email:** [example@example.com](mailto:example@example.com)  
        **Phone:** [+91 9440081463](tel:+919440081463)
    """)
    
    # Social Media Links
    st.markdown("""
        **Follow us:**  
        [Facebook](https://www.facebook.com/p/Sri-Sreenivasa-Vidya-Niketan-High-School/) | [Twitter](#) | [Instagram](#)
    """)

    # Location (Google Maps)
    st.markdown("""
        **Location:**  
        <iframe src="https://www.google.com/maps/search/Sri+Sreenivasa+Vidyanikethan+High+School+location/" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
    """, unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <footer>
        <div style="text-align: center;">
            <p>Sri Sreenivasa Vidyanikethan High School, Beluguppa | Created by K.Manjunatha Reddy | &copy; 2024</p>
        </div>
    </footer>
""", unsafe_allow_html=True)
