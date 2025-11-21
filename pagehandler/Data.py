#pagehandler/Data.py
import streamlit as st
import pandas as pd

st.title("📊 Data Exploration")
st.write("Preview and describe the Titanic dataset here.")

tab1, tab2, tab3 = st.tabs(["Data Overview", "Training data", "Passanger Data"])

with tab1:
    st.header("Data Overview")
    st.write("View all the data in dataframes")
    
    csv_file_path = "titanic-data/train.csv" 
    train_df = pd.read_csv(csv_file_path)

    csv_file_path = "titanic-data/test.csv" 
    test_df = pd.read_csv(csv_file_path)

    csv_file_path = "titanic-data/gender_submission.csv" 
    survived_df = pd.read_csv(csv_file_path)

    with st.expander("Training Data"):
        st.write(train_df) 

    with st.expander("Passanger Data"):
        st.write(test_df) 

    with st.expander("Passanger ID vs. Survived Data"):
        st.write(survived_df) 

with tab2:
    st.header("Training Data")
    st.write("Explore the Training Data")
    
with tab3:
    st.header("Passanger Data")
    st.write("Explore the Passanger Data")
    
#display each csv as a dataframe
