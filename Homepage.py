import streamlit as st

Upload_Page= st.Page("pages\Main.py",title="Upload Questions")
Upload_Page= st.Page("pages\Page1.py",title="Upload Questions")

pg =st.navigation([st.Page("pages\Main.py"),st.Page("pages\Page1.py")])

pg.run()