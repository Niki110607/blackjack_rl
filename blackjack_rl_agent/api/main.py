from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from predict import best_move
app = FastAPI()

origins = [
    "http://localhost:8501",
    "https://blackjack-rl-agent.streamlit.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cards/")
def get_cards(
        h_card: int | str,
        p_cards: list[int | str] = Query(..., min_items=2)
) -> dict[str, str]:

    action = best_move(h_card, p_cards)
    return {"action": action}