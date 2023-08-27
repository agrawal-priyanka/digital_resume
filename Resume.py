import streamlit as st
import webbrowser
import pyperclip
from PIL import Image
from streamlit.components.v1 import html

image = Image.open('profile_photo.png')

st.set_page_config(page_title="Resume | Priyanka Agrawal")

#url1 = 'https://github.com/agrawal-priyanka'
#url2= 'https://www.linkedin.com/in/priyanka-agrawal-46640b15a/'

with open("styles.css") as k:
    st.markdown(f"<style>{k.read()}</style>", unsafe_allow_html=True)

with open("Priyanka's Resume (4).pdf", "rb") as pdf_file:
    pdf = pdf_file.read()


def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

    def copy_gmail_address(gmail):
        gmail_copy = f"""
        <script>
            function copyToClipboard_{gmail}() {{
                var dummy = document.createElement("textarea");
                document.body.appendChild(dummy);
                dummy.value = "{gmail}";
                dummy.select();
                document.execCommand("copy");
                document.body.removeChild(dummy);
            }}
        </script>
        """
        html(gmail_copy)



    
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image,width=270)

with col2:
    st.title("Priyanka Agrawal")
    st.write("An aspiring Data Analyst with relevant knowledge in fields of Data Science and Machine Learning.")
    st.download_button(
        label="Download Resume",
        data=pdf,
        file_name="Priyanka_Resume.pdf",
        mime="application/octet-stream")
    col3,col4,col5 = col2.columns(3,gap="small")
    with col3:
        st.button('GitHub', on_click=open_page,key='widget1', args=('https://github.com/agrawal-priyanka',))

     
    with col4:
    	st.button('LinkedIn', on_click=open_page,key='widget2', args=('https://www.linkedin.com/in/priyanka-agrawal-46640b15a/',))

    with col5:
        st.button("📋" '   Gmail', on_click=copy_gmail_address,key='copy_text', args=('priyanka76.pa@gmail.com',))

    


st.subheader("Education")

st.write("""
- BBA | Amity, Indore \n
   I received a gold medal for academic excellence during graduation. I was also awarded with many medals in Table Tennis 
tournaments held at our college
Courses: Finance, Statistics
- Higher Secondary Education | Shishukunj, Indore\n
   I was able to pass 12th boards with 91%. 
Courses : Mathematics, Accounting, Economics""")

st.subheader('Certifications')

st.write("""
- MS Excel (Advanced) – Completed in August 2022
- Data Analysis with Python and Pandas (Udemy) – Completed in March 2023
- Data Science & Machine Learning Certification - A career oriented detailed certification course from ONLEI Technologies – In 
progress
""")

col5,col6= st.columns(2,gap="Medium")
with col5:
    st.subheader('Hard Skills')
    col1,col2=st.columns(2,gap="small")
    with col1:
       st.write("Programming")
    with col2:
        st.write("Python")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Data Processing")
    with col2:
        st.write("Pandas, SQL, Numpy")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Data Visualization")
    with col2:
        st.write(" PowerBI, matplotlib, seaborn, plotly")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Machine Learning")
    with col2:
        st.write("scikit-learn")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Deep Learning")
    with col2:
        st.write("TensorFlow")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Web Development")
    with col2:
        st.write("Streamlit, CSS")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Sentiment Analysis")
    with col2:
        st.write("VADER")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Database Management")
    with col2:
        st.write("MySQL, MS Excel")
    col1,col2=st.columns(2,gap="small")
    with col1:
        st.write("Web scraping")
    with col2:
        st.write("Beautiful Soup ")
with col6:
    st.subheader("Soft Skills")
    st.write("""
- Problem Solver
- Highly Organized
- Collaborative
- Initiative – Driven

""")

st.subheader("Internships")
st.write("""
- Anand Rathi Brokerage ltd. – MAY 2017 to JUNE 2017

- Data Science Intern | ONLEI Technologies |
  Feb 2023 - Aug 2023


""")



    





