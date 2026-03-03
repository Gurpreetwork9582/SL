import streamlit as st
class Game: 
    def __init__(self):
        self.Game_Name = st.text_input("What is the name of your game",label_visibility="hidden")


    def Game_name(self):

        st.title(f"{self.Game_Name}",text_alignment="center")

        st.header("Questions",text_alignment="center")

        st.subheader("What is your name", text_alignment="center")

        a, b =st.columns(2)
        c , d =st.columns(2)

        a.button("Option A",width="stretch")
        b.button("Option B",width="stretch")
        c.button("Option C",width="stretch")
        d.button("Option D",width="stretch")



g1 = Game()
g1.Game_name()