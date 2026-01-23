from fastapi import FastAPI, Query
from blackjack_rl_agent.api.predict import best_move
app = FastAPI()

@app.get("/cards/")
def get_cards(
        h_card: int | str,
        p_cards: list[int | str] = Query(..., min_items=2)
) -> dict[str, str]:

    action = best_move(h_card, p_cards)
    return {"action": action}