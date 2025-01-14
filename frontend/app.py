import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import io
import os

# Get backend URL from environment variable, default to localhost if not set
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000')

st.set_page_config(page_title="Data Science Dashboard", layout="wide")

st.title("Data Science Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx', 'xls'])

if uploaded_file is not None:
    # Send file to backend for processing
    try:
        files = {'file': uploaded_file}
        response = requests.post(f"{BACKEND_URL}/upload", files=files)
        if response.status_code != 200:
            st.error("Error processing file")
            return
        
        # Read the file for local processing
        uploaded_file.seek(0)
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Display basic information
        st.subheader("Data Overview")
        st.write(f"Shape: {df.shape}")
        st.write(f"Columns: {', '.join(df.columns)}")
        
        # Data preview
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        # Column selection for analysis
        st.subheader("Data Analysis")
        selected_column = st.selectbox("Select column for analysis", df.columns)
        
        if selected_column:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Distribution Plot")
                if df[selected_column].dtype in ['int64', 'float64']:
                    fig = px.histogram(df, x=selected_column)
                    st.plotly_chart(fig)
                else:
                    fig = px.bar(df[selected_column].value_counts())
                    st.plotly_chart(fig)
            
            with col2:
                st.subheader("Summary Statistics")
                if df[selected_column].dtype in ['int64', 'float64']:
                    st.write(df[selected_column].describe())
                else:
                    st.write(df[selected_column].value_counts())
        
        # Correlation analysis for numerical columns
        numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
        if len(numerical_cols) > 1:
            st.subheader("Correlation Analysis")
            correlation = df[numerical_cols].corr()
            fig = px.imshow(correlation, 
                          labels=dict(color="Correlation"),
                          color_continuous_scale="RdBu")
            st.plotly_chart(fig)
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
