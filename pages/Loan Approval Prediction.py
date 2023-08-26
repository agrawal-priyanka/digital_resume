import streamlit as st

with open("styles.css") as k:
    st.markdown(f"<style>{k.read()}</style>", unsafe_allow_html=True)

st.title("Loan Approval Prediction Model")
st.subheader("Aim")
st.write("A Machine Learning project aims to predict status of loan based on various factors like credit history, applicant's and coapplicant's income, loan term, loan amount, ownership of property, gender, number of dependents, status of self employment.")
st.subheader("Datasets")
st.write("""
- Train Dataset
- Test Dataset
""")
st.subheader("Machine Learning Models")
st.write("""
- Logistic Regression with K fold Validation
- K neighbors Classifier with Kfold Validation
- Random Forest with K fold Validation
- XG Boost with K fold validation

""")

st.subheader("Optimization Techiques")
st.write("""
- Feature Engineering 
- Cross Validation
- Hyper Parameter Tuning
""")

st.subheader("Results")
col1,col2=st.columns(2,gap="small")
with col1:
    st.write("F1 Score")
    st.image("img12.png")
with col2:
    st.write("Accuracy")
    st.image("img13.png")
st.write("Compared to other models, Random Forest Model had a somewhat higher average F1 score and accuracy of 10 folds. Therefore, the entire Train dataset was used to train the Random Forest model, and the Test dataset was used to test it.")

st.subheader("Tools and Packages")
st.write("""
- Python
- Jupyter Notebook
- scikit-learn
- XGBoost
- Pickle
- GridSearchCV

""")


with open("new_loan_pred.ipynb", "rb") as jup_file:
    jup = jup_file.read()
with open("loan_model.pkl", "rb") as pkl_file:
    pkl = pkl_file.read()

st.subheader("Source Files")
col1,col2,col3 = st.columns(3,gap="small")
with col1 :
    st.write("Download Jupyter file:")
    st.download_button(
        label="Jupyter File",
        data=jup,
        file_name="loan_pred.ipynb",
        mime="application/octet-stream")
with col2:
    st.write("Download Pickle file:")
    st.download_button(
        label="Pickle File",
        data=pkl,
        file_name="loan_model.pkl",
        mime="application/octet-stream")





