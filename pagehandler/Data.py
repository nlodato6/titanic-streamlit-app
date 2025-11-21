#pagehandler/Data.py
import streamlit as st
import pandas as pd

st.title("📊 Data Exploration")
st.write("Preview and describe the Titanic dataset here.")

tab1, tab2, tab3, tab4 = st.tabs(["Data Overview", "train.csv", "test.csv", "gender_submission.csv"])
#load dataframes from csv
train_df = pd.read_csv("titanic-data/train.csv" )
test_df = pd.read_csv("titanic-data/test.csv")
survived_df = pd.read_csv("titanic-data/gender_submission.csv")

with tab1:
    st.header("Data Overview")
    st.markdown(
        """
        The **Kaggle Titanic** dataset contains passenger records from the RMS Titanic's 1912 voyage and is a classic dataset for learning data cleaning, exploratory analysis, and classification.  
        This page shows each CSV included with the dataset and provides a brief description of important fields and quick checks you can run to understand data quality and signals for modeling.

        **Key fields**
        - `PassengerId` — unique id  
        - `Survived` — target (0 = died, 1 = survived) — *only in train.csv*  
        - `Pclass` — passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)  
        - `Name`, `Sex`, `Age` — demographic info  
        - `SibSp`, `Parch` — family relations aboard  
        - `Ticket`, `Fare`, `Cabin` — travel/booking info  
        - `Embarked` — port of embarkation (C/Q/S)

        **Quick EDA checks to run**
        1. Missingness: `Age`, `Cabin` often have missing values.  
        2. Distributions: age histogram, fare skew, survival rate by `Pclass` and `Sex`.  
        3. Feature checks: create `FamilySize = SibSp + Parch + 1`; extract title from `Name`.  
        4. Correlations: survival vs. `Pclass`, `Sex`, `Age`, `Fare`.
        """
        )

with tab2:
    st.header("train.csv Data")
    st.markdown(
        """
        Contains the labeled training set used for supervised modeling.
        - Rows: passenger records with `Survived` label.
        - Use for: EDA, feature engineering, model training and cross-validation.
        - Watch for: missing `Age` and `Cabin`, outliers in `Fare`.
        """
            )
    with st.expander("Training Data"):
        st.write(train_df) 
    
with tab3:
    st.header("test.csv Data")
    st.markdown(
        """
        Contains unlabeled passenger records for final predictions.
        - Rows: passenger records **without** `Survived`.
        - Use for: generating submission predictions after model training on `train.csv`.
        - Important: ensure feature engineering applied identically as for train.
        """
            )
    with st.expander("Passanger Data"):
        st.write(test_df) 
with tab4:
    st.header("gender_submission.csv Data")
    st.markdown(
        """
        A sample submission file demonstrating expected format (PassengerId, Survived).
        - Useful as a baseline: the simple gender-based baseline (`Survived = 1` if `Sex == 'female'`) often performs well.
        """
            )
    with st.expander("Passanger ID vs. Survived Data"):
        st.write(survived_df) 