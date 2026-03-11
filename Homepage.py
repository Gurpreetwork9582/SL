import streamlit as st


Main_Page= st.Page("pages/Main.py",title="Quiz Play",icon=	"📓")
#Upload_Page= st.Page("pages/Upload_Questions.py",title="Upload File")
Manual_Page = st.Page("pages/Manual_Que.py",title="Build a Quiz",icon="📘")

pg =st.navigation([Main_Page,Manual_Page])

pg.run()