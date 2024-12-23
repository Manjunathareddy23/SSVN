import streamlit as st
import streamlit.components.v1 as components

# Custom CSS and HTML for styling and layout, including JS for mobile menu toggle
css_code = """
    <style>
        /* Importing Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Arya:wght@700&family=Montserrat:wght@500&display=swap');

        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
          font-family: 'Montserrat', sans-serif;
        }

        html{
          scroll-behavior: smooth;
        }

        body {
          font-weight: 500;
          color: rgb(0, 0, 0);
          background: #fcfcfc89;
        }

        /* Header Styles */
        header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 1% 3%;
          background-color: #fff;
          box-shadow: 0px .125rem 10px rgba(0, 0, 0, 0.1);
          position: fixed;
          top: 0;
          z-index: 3;
          width: 100%;
        }

        .logo a {
          text-decoration: none;
          color: #24262b;
        }

        .logo a:hover{
          color: #24262b91;
          transition: 1s;
        }

        .logo a h1 {
          font-size: 1.5rem;
          text-transform: uppercase;
        }

        nav {
          height: 3.75rem;
          background: #ffffff;
          display: flex;
          align-items: center;
        }

        nav ul {
          list-style: none;
          display: flex;
          justify-content: space-between;
        }

        nav ul li a {
          color: #24262b;
          text-decoration: none;
          font-size: 1rem;
          font-weight: 600;
          margin: .125rem .5rem;
          padding: .25rem .5rem;
          letter-spacing: .0625rem;
          text-transform: uppercase;
        }

        nav ul li a:hover {
          transition: width 1s;
          color: #24262bb1; 
          border-bottom: .25rem solid #24262bb1;
        }

        /* Hero Section */
        .hero {
          display: flex;
          width: 100%;
          height: 100vh;
          flex-direction: column;
          justify-content: center;
          padding: 1.3rem;
        }

        .hero-text-container {
          text-align: center;
          position: absolute;
          left: 0;
          display: flex;
          flex-direction: column;
          width: 100%;
          align-items: center;
          justify-content: center;
          color: rgb(255, 255, 255);
          padding: 2% 2%;
        }

        .hero-text-container h1 {
          font-size: 1.8rem;
          text-transform: uppercase;
          letter-spacing: 0.1em;
        }

        .hero-text-container p {
          font-size: 1rem;
          margin: .5rem .5rem;
          font-weight: bold;
          letter-spacing: 0.08em;
          text-transform: uppercase;
        }

        .hero-text-container .btn {
          border: none;
          outline: 0;
          display: inline-block;
          padding: .625rem 1.25rem;
          color: #24262b;
          background-color: #ffffff;
          text-align: center;
          cursor: pointer;
          margin: .625rem .25rem;
          text-decoration: none;
          border-radius: 1rem;
          font-size: 0.7rem;
          text-transform: uppercase;
          letter-spacing: 0.08em;
          font-weight: 900;
        }

        .hero-text-container .btn:hover {
          background-color: #24262b;
          color: rgb(255, 255, 255);
          transition: 1.5s;
        }

        /* About Section */
        .about-section {
          padding-left: 0.5%;
          padding-right: 4%;
        }

        .about-section h1 {
          font-size: 2.1875rem;
          font-weight: bold;
          margin-top: 1rem;
          margin-bottom: .9rem;
          text-align: center;
          text-transform: uppercase;
        }

        .about-info {
          width: 50%;
          margin: 1.25rem;
        }

        .about-info h2 {
          font-size: 1.4rem;
          margin: .625rem;
        }

        .about-info p {
          font-size: 1rem;
          line-height: 1.5;
          margin-bottom: 1.25rem;
          text-align: justify;
        }

        /* Academic Section */
        .academic-section {
          margin: 0.625rem;
          padding: 1.25rem;
        }

        .academic-section h2 {
          text-align: center;
          margin: 1.25rem;
          padding: 0.9375rem;
          text-transform: uppercase;
        }

        .education-levels {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-around;
          align-items: center;
          margin: 1.25rem;
        }

        .education-level {
          width: 100%;
          background-color: #f5f5f5;
          padding: 1.25rem;
          margin-bottom: 1.25rem;
          box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
          border-radius: 16px;
          transition: all 0.3s ease;
        }

        .education-level:hover {
          background-color: #e0e0e0;
          box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
        }

        .education-level h3 {
          margin-top: 0;
          text-transform: uppercase;
        }

        /* Gallery Section */
        .gallery {
          margin: 1.25rem;
        }

        .gallery h2 {
          text-align: center;
          margin: 1.25rem;
          padding: .9375rem;
          text-transform: uppercase;
        }

        .grid {
          display: grid;
          grid-auto-flow: column;
          grid-auto-columns: 100%;
          grid-gap: 1em;
          overflow-x: scroll;
          -webkit-overflow-scrolling: touch;
          padding: 2em 1em;
          background: white;
          list-style: none;
        }

        @media all and (min-width: 740px) {
          .grid {
            grid-auto-flow: initial;
            grid-template-columns: repeat(auto-fit, minmax(auto, 20em));
            justify-content: center;
          }
        }

        /* Contact Section */
        .contact-section {
          padding: 50px;
          margin: 20px;
        }

        .contact-section h2 {
          font-size: 32px;
          margin-bottom: 40px;
          text-align: center;
        }

        .google-map iframe {
          height: 100%;
          width: 100%;
          left: 0;
          top: 0;
          position: absolute;
        }

        /* Mobile menu toggle button */
        .toggle-button {
          display: none;
        }

        @media (max-width: 876px) {
            .toggle-button {
                display: block;
                background-color: #24262b;
                padding: 0.5rem;
                border-radius: 0.25rem;
                color: white;
                cursor: pointer;
            }

            nav ul {
                display: none;
                width: 100%;
                background-color: #fff;
                position: absolute;
                top: 60px;
                left: 0;
                padding: 1rem;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                flex-direction: column;
                align-items: flex-start;
            }

            nav ul li {
                width: 100%;
                padding: 0.5rem 0;
            }

            nav ul li a {
                color: #24262b;
                text-decoration: none;
                font-size: 1.25rem;
            }

            .close-button {
                display: block;
                color: #24262b;
                font-size: 1.5rem;
                cursor: pointer;
                margin-top: 1rem;
            }

            .close-button:hover {
                color: #ff5f5f;
            }
        }
    </style>
"""

# HTML Content with JavaScript
html_code = """
    <header>
        <div class="logo">
            <a href="#">
                <h1>Sri Sreenivasa Vidhyanikethan High School</h1>
                <p>Education for all</p>
            </a>
        </div>
        <div class="toggle-button">☰</div>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#About">About</a></li>
                <li><a href="#Academic">Academics</a></li>
                <li><a href="#Gallery">Gallery</a></li>
                <li><a href="#Contact">Contact</a></li>
            </ul>
            <div class="close-button">X</div>
        </nav>
    </header>

    <section id="About" class="about-section">
        <h1>About Our School</h1>
        <div class="about-info">
            <h2>Established Date</h2>
            <p>Sri Sreenivasa Vidhyanikethan High School, Beluguppa was established in 2006...</p>
            <h2>Our Mission</h2>
            <p>Our mission is to provide high-quality education to students...</p>
        </div>
    </section>

    <section id="Academic" class="academic-section">
        <h2>Academics</h2>
        <div class="education-levels">
            <div class="education-level">
                <h3>Pre-primary</h3>
                <p>Age: 3-5 years, Nursery, LKG, UKG</p>
            </div>
            <div class="education-level">
                <h3>Primary</h3>
                <p>Class 1 to Class 5</p>
            </div>
            <div class="education-level">
                <h3>Higher Secondary</h3>
                <p>Class 6 to Class 10</p>
            </div>
        </div>
    </section>

    <section id="Gallery" class="gallery">
        <h2>Our Gallery</h2>
        <ul class="grid">
            <!-- Example of gallery images -->
            <li><img src="https://via.placeholder.com/400" alt="image1"></li>
            <li><img src="https://via.placeholder.com/400" alt="image2"></li>
            <li><img src="https://via.placeholder.com/400" alt="image3"></li>
        </ul>
    </section>

    <section id="Contact" class="contact-section">
        <h2>Contact Us</h2>
        <div class="google-map">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18..."></iframe>
        </div>
    </section>

    <script>
        const toggleButton = document.querySelector('.toggle-button');
        const closeButton = document.querySelector('.close-button');
        const mobileNav = document.querySelector('nav ul');
        const navItem = document.querySelectorAll('li a');

        const Display = () => {
            mobileNav.style.display = 'block';
            closeButton.style.display = 'block';
        };

        const Close = () => {
            mobileNav.style.display = 'none';
            closeButton.style.display = 'none';
        }

        // When pressed toggle button then mobile navmenu should appear
        toggleButton.addEventListener('click', () => {
            Display();
        });

        // When pressed clicked on close button, the mobile navmenu should disappear
        closeButton.addEventListener('click', () => {
            Close();
        });

        // When clicked on navitems the mobile navmenu should close;
        navItem.forEach(navItem => {
            navItem.addEventListener('click', () => {
                if (window.innerWidth < 876) // Adjust the breakpoint as needed
                    Close();
            });
        });
    </script>
"""

# Injecting the HTML and CSS into Streamlit app
components.html(html_code, height=800)
st.markdown(css_code, unsafe_allow_html=True)
