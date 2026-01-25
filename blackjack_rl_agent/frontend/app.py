import streamlit as st
import requests
import time
import random

Base_URL = "https://blackjack-rl.onrender.com"

if "selectboxes" not in st.session_state:
    st.session_state.selectboxes = 2

def add_card():
    st.session_state.selectboxes += 1

def remove_card():
    st.session_state.selectboxes -= 1

st.set_page_config(page_title="Blackjack AI", page_icon="♠️")
st.title("♠️♥️ Blackjack RL Agent ♣️♦️", text_alignment="center")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Player's Hand")
    p_cards = []
    for i in range(st.session_state.selectboxes):
        p_card = st.selectbox(
            label="Select a card",
            options=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
            key=i
        )
        p_cards.append(p_card)

    but_col1, but_col2 = st.columns(2)
    with but_col1:
        st.button("Add card", on_click=add_card)
    with but_col2:
        if st.session_state.selectboxes > 2:
            st.button("Remove card", on_click=remove_card)

with col2:
    st.subheader("Dealer's Hand")
    h_card = st.selectbox(label="Select a card", options=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])



if st.button("Get best move!"):
    with st.spinner("Calculating the best move..."):
        time.sleep(random.uniform(0.5, 3))
        response = requests.get(
            f"{Base_URL}/cards/",
            params={"h_card": h_card, "p_cards": p_cards}
        )
        if response.status_code == 200:
            output = response.json()
            action = output.get("action")
            if action == "o21":
                st.error("Error: Hand value is over 21!")
            else:
                st.subheader(f"Recommended action: {action}", text_alignment="center")

        else:
            try:
                st.error(f"Server Error ({response.status_code}): {response.json().get("detail", "Unknown error")}")
            except:
                st.error(f"Server Error ({response.status_code}): The server returned an invalid response.")