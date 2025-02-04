import streamlit as st

# Inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Page Configuration
st.set_page_config(
    page_title="Sri Sreenivasa Vidhyanikethan High School",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navigation
st.markdown("""
<nav class="header">
    <div class="logo">
        <a href="#">
            <h1>Sri Sreenivasa Vidhyanikethan</h1>
            <p>Beluguppa</p>
        </a>
    </div>
</nav>
""", unsafe_allow_html=True)

# Main content
menu = ['Home', 'About', 'Academics', 'Gallery', 'Contact']
choice = st.selectbox("Navigate to:", menu, label_visibility="collapsed")

# Sections
if choice == 'Home':
    st.markdown("""
    <div class="hero">
        <div class="slide-bg">
            <div class="hero-text-container">
                <h1>Welcome to SSVNH School</h1>
                <p class="nepali-font">शिक्षा सबैका लागि</p>
                <a href="#contact" class="btn">Admission Open</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif choice == 'About':
    st.markdown("""
    <div class="about-section">
        <h1>About Our School</h1>
        <div class="flex-container">
            <div class="about-info">
                <h2>Established in 2006</h2>
                <p>SREENIVASA VIDYA NIKETAN was established in 2006 and is managed by Pvt. Unaided...</p>
            </div>
            <div class="members">
                <div class="img-container">
                    <img src="https://via.placeholder.com/200" alt="Principal">
                </div>
                <div class="principal-info">
                    <h2>V.Sreenivasulu Ph.D</h2>
                    <p>Experienced educator with 20+ years in academic leadership...</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif choice == 'Academics':
    st.markdown("""
    <div class="academic-section">
        <h2>Our Academic Programs</h2>
        <div class="education-levels">
            <div class="education-level">
                <h3>Pre-primary</h3>
                <p>Age 3-5 years (Nursery, LKG, UKG)</p>
            </div>
            <div class="education-level">
                <h3>Primary</h3>
                <p>Class 1 to Class 5</p>
            </div>
            <div class="education-level">
                <h3>Secondary</h3>
                <p>Class 6 to Class 10</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif choice == 'Gallery':
    st.markdown("""
    <div class="gallery">
        <h2>School Gallery</h2>
        <ul class="grid">
            <li>
                <figure class="grid__figure">
                    <img src="https://via.placeholder.com/400x300" alt="School Building">
                    <figcaption>Our School Campus</figcaption>
                </figure>
            </li>
            <!-- Add more gallery items -->
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif choice == 'Contact':
    st.markdown("""
    <div class="contact-section">
        <h2>Contact Us</h2>
        <div class="contact-info">
            <div class="contact-item">
                <i class="fas fa-phone"></i>
                <a href="tel:+919440081463">+91 9440081463</a>
            </div>
            <div class="contact-item">
                <i class="fas fa-envelope"></i>
                <a href="mailto:info@ssvnhs.com">info@ssvnhs.com</a>
            </div>
        </div>
        <div class="google-map">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3804.536061229059!2d77.32654631534795!3d15.635943988772957!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bb6a2b7c5739345%3A0x3e4a4a3c3d3d3b3a!2sSri%20Sreenivasa%20Vidyanikethan%20High%20School!5e0!3m2!1sen!2sin!4v162987654321!5m2!1sen!2sin" 
            width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<footer class="footer">
    <div class="footer-container">
        <div class="row">
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="#">Admissions</a></li>
                    <li><a href="#">Calendar</a></li>
                    <li><a href="#">Careers</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Follow Us</h4>
                <div class="social-links">
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
        <div class="creator">
            <p>© 2024 Sri Sreenivasa Vidhyanikethan High School</p>
            <p>Created by K.Manjunatha Reddy</p>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)

# Add Font Awesome
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)
