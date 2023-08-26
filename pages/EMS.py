import streamlit as st
import webbrowser

with open("styles.css") as k:
    st.markdown(f"<style>{k.read()}</style>", unsafe_allow_html=True)


st.title("Employee Management System")
st.write("EMS is multipage Streamlit app which connects MySQL Database of employees using Python Programming language. First page is accessible by employees and second page by admins. Changes made through this app will directly reflect in MySQL database.")
st.subheader("Aim")
st.write("EMS eases the process of data management as well as acts as a link between Employee and administration. ")
st.subheader("Users")
st.write("""
- Employees - Employees can view their personal details, final salaries, leaves as well as apply for leaves and Work from Home applications
- Admins - Admins has access to database. They are able to view, add, update and delete data from the database. They can approve or disapprove leave and WFH applications.
""")
st.subheader("Features")
st.image('img6.png')
st.image('img8.png')

st.subheader("Tools and Packages")
st.write("""
- Python
- MySQL
- Csv
- Pandas
- Streamlit
""")

with open("EMS Codes.zip", "rb") as zip_file:
    zip = zip_file.read()
with open("EMS Screenshots.zip", "rb") as zip_files:
    zips = zip_files.read()
url1 = "https://drive.google.com/drive/folders/1kOsm1ezADYThATjGE2r7ppzTC5GAphvX?usp=drive_link"
st.subheader("Source Files")
col1,col2,col3 =st.columns(3,gap="small")
with col1:
    st.write("Download all codes:")
    st.download_button(
        label="Python Codes",
        data=zip,
        file_name="EMS Codes.zip",
        mime="application/octet-stream")
with col2:
    st.write("Download Screenshots:")
    st.download_button(
        label="Screenshots",
        data=zips,
        file_name="EMS Screenshots.zip",
        mime="application/octet-stream")
with col3:
    st.write("Download Recordings:")
    if st.button('Recordings'):
            webbrowser.open_new_tab(url1)


