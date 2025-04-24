import streamlit as st
import urllib.parse

# --- PAGE CONFIG ---
st.set_page_config(page_title="TeslaTech", page_icon="💻", layout="wide")

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #1c1c1c;            
        }
        .stApp {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(-45deg, #ffffff, #e0e0f8, #f0f8ff, #ffffff);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: #1c1c1c;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .home-section {         
            background-image: url('https://i.postimg.cc/Gm5ycnJf/8469936.jpg');
            background-size: cover;
            background-position: center;
            padding: 100px 10vw;
            color: white;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
            border-radius: 12px;
            margin-bottom: 40px;
        }
        .home-title {
            font-size: 48px;
            font-weight: 800;
            margin-bottom: 20px;
        }
        .home-subtitle {
            font-size: 20px;
            color: #f0f0f0;
        }
        .section {
            padding: 60px 10vw;
        }
        .headline {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .tagline {
            font-size: 20px;
            color: #555;
            margin-bottom: 40px;
        }
        .pricing-card {
            border: 2px solid #e6e6e6;
            border-radius: 12px;
            padding: 30px;
            background: #fefefe;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            transition: all 0.2s ease;
            text-align: center;
        }
        .pricing-card:hover {
            border-color: #0072ff;
            background: linear-gradient(to bottom right, #f9fbff, #e7efff);
        }
        .service-card {
            border: 2px solid #e6e6e6;
            border-radius: 12px;
            padding: 20px;
            background: #f9f9f9;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            text-align: center;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #999;
            margin-top: 60px;
            padding-bottom: 20px;
        }
        .review-card {
            border: 2px solid #e6e6e6;
            border-radius: 12px;
            padding: 20px;
            background: #f9f9f9;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 20px;
        }
    </style>
    <div class="home-section">
        <div class="home-title"></div>
        <div class="home-subtitle"></div>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.image("https://i.postimg.cc/qq17j21F/3918929.jpg", width=60) 
st.title("TeslaTech")
st.title("Let’s Build Your Website — Fast, Affordable & Professional.")
st.write("Modern, secure, and fast websites built to turn visitors into customers.")


# --- SERVICES SECTION ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Why Choose TeslaTech")

# Cards for services
service1, service2, service3 = st.columns(3)

with service1:
    st.markdown('<div class="service-card"><b>Custom Web Design</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/5tgqbCG4/3405339.jpg" alt="service 1" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.write("We create tailor-made websites that reflect your brand and vision.")
    st.markdown("</div>", unsafe_allow_html=True)

with service2:
    st.markdown('<div class="service-card"><b>Conversion-First Approach</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/SsKLsKFW/3999989.jpg" alt="service 2" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.write("Our designs focus on driving engagement and achieving business goals.")
    st.markdown("</div>", unsafe_allow_html=True)

with service3:
    st.markdown('<div class="service-card"><b>SEO & Mobile Optimized</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/L5Yzt0s5/5252484.jpg" alt="service 3" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.write("Our websites are optimized for mobile and search engine visibility.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- PRICING SECTION ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Our Pricing")

# Pricing Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="pricing-card"><b>Starter Package</b>', unsafe_allow_html=True)
    st.markdown("****")
    st.markdown('<img src="https://i.postimg.cc/qqyLKMQg/71z-2202-w012-n001-39b-p12-39.jpg" alt="col1" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.markdown("**৳500**")
    st.write("""
    - 1 Page Website  
    - Basic Design  
    - Delivery in 2 Days  
    - Basic SEO
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="pricing-card"><b>Professional Package</b>', unsafe_allow_html=True)
    st.markdown("****")
    st.markdown('<img src="https://i.postimg.cc/dQynp4vv/9578083.jpg" alt="col2" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.markdown("**৳1000**")
    st.write("""
    - Up to 5 Pages  
    - Responsive Layout  
    - Contact Form + SEO  
    - Delivery in 5 Days  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="pricing-card"><b>Business Plus Package</b>', unsafe_allow_html=True)
    st.markdown("****")
    st.markdown('<img src="https://i.postimg.cc/nLpYyk3S/19199410.jpg" alt="col3" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.markdown("**৳2000+**")
    st.write("""
    - Unlimited Pages  
    - Admin Panel / Database  
    - Custom Features & Support  
    - Dedicated Project Manager
    """)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- SERVICES SECTION ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("What our clients says")

# Cards for services
review1, review2, review3 = st.columns(3)

with review1:
    st.markdown('<div class="service-card"><b>John Doe(JD Enterprises)</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/HxKZ5Ngv/JEMA-VIVI-018-02.jpg" alt="review1" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.write("TeslaTech created an amazing e-commerce website for us. Our sales doubled in 3 months!")
    st.markdown("</div>", unsafe_allow_html=True)

with review2:
    st.markdown('<div class="service-card"><b>Sarah Smith(Sarahs Crafts)</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/ZYBDZJ8G/7737534.jpg" alt="review 2" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.write("We love our portfolio site. The team understood our needs and delivered a perfect design.")
    st.markdown("</div>", unsafe_allow_html=True)

with review3:
    st.markdown('<div class="service-card"><b>Michael Lee(TechSphere)</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/SRMZGGQS/d9db9cb9-e91c-48cc-9fa2-b9cb17ff1b0e.jpg" alt="review 3" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("****")
    st.write("Highly recommend TeslaTech for startups. Their team supported us through the entire process.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Our Projects")

# Cards for projects with images
project1, project2, project3 = st.columns(3)

with project1:
    st.markdown('<div class="service-card"><b>Project 1: E-Commerce Website</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/xCyr0tQk/6505894.jpg" alt="Project 1" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("***", unsafe_allow_html=True)
    st.write("An innovative e-commerce platform that increased client sales by 200%.")
    st.markdown("</div>", unsafe_allow_html=True)

with project2:
    st.markdown('<div class="service-card"><b>Project 2: Portfolio Website</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/3NKsWmrt/4942432.jpg" alt="Project 2" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("***", unsafe_allow_html=True)
    st.write("A clean and responsive portfolio site for creative professionals showcasing their work.")
    st.markdown("</div>", unsafe_allow_html=True)

with project3:
    st.markdown('<div class="service-card"><b>Project 3: Corporate Website</b>', unsafe_allow_html=True)
    st.markdown('<img src="https://i.postimg.cc/c1hq29T2/2762498.jpg" alt="Project 3" style="width:100%; height:auto;">', unsafe_allow_html=True)
    st.markdown("***", unsafe_allow_html=True)
    st.write("A corporate site with advanced features, including a client portal and integrated systems.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# --- CONTACT FORM SECTION ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Start Your Project")

with st.form("contact_form"):
    name = st.text_input("Full Name *")
    email = st.text_input("Email *")
    phone = st.text_input("Phone Number *")
    project_type = st.selectbox("Website Type", ["Portfolio", "Business", "E-commerce", "Educational", "Other"])
    budget = st.selectbox("Your Budget", ["৳500", "৳1000", "৳2000+", "Custom"])
    message = st.text_area("Briefly describe your project *")

    submitted = st.form_submit_button("Send to WhatsApp")

    if submitted:
        whatsapp_msg = f"""New Website Project Request

Name: {name}
Email: {email}
Phone: {phone}
Website Type: {project_type}
Budget: {budget}

Project Summary:
{message}
"""
        encoded_msg = urllib.parse.quote(whatsapp_msg)
        wa_link = f"https://wa.me/8801400461284?text={encoded_msg}"
        st.warning("Click below to continue conversation on WhatsApp:")
        st.markdown(f"[Open WhatsApp →]({wa_link})", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<div class="footer">© 2025 TeslaTech. Crafted with care for serious brands.</div>', unsafe_allow_html=True)
