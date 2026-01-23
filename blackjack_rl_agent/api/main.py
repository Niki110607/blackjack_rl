from fastapi import FastAPI
from predict import best_move

app = FastAPI()

@app.get("/")
def squared(h_card: int|str, p_card1: int|str, p_card2: int|str):
    return best_move(h_card, p_card1, p_card2)