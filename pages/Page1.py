import streamlit as st
import pandas as pd

# let the user upload either a CSV or an Excel workbook
file_types = ["csv", "xlsx", "xls"]
uploaded = st.file_uploader("Upload questionnaire file", type=file_types)

if uploaded is not None:
    try:
        name = uploaded.name.lower()
        if name.endswith(".csv"):
            # try to infer delimiter and encoding
            try:
                df = pd.read_csv(uploaded, sep=None, engine="python")
            except Exception:
                # fallback to common options
                df = pd.read_csv(uploaded, encoding="ISO-8859-1", sep=";")
        else:
            # treat as Excel workbook
            df = pd.read_excel(uploaded)
    except Exception as e:
        st.error(f"Could not read the file: {e}")
    else:
        st.write(df)
