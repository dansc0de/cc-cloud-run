from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google.cloud import firestore
from typing import Annotated
import datetime

app = FastAPI()

# mount static files
app.mount("/static", StaticFiles(directory="/app/static"), name="static")
templates = Jinja2Templates(directory="/app/template")

# init firestore client
db = firestore.Client()
votes_collection = db.collection("votes")


@app.get("/")
async def read_root(request: Request):
    votes = votes_collection.stream()

    # collect vote data
    vote_data = []
    for v in votes:
        vote_data.append(v.to_dict())

    tabs_count = sum(1 for v in vote_data if v.get("team") == "TABS")
    spaces_count = sum(1 for v in vote_data if v.get("team") == "SPACES")

    return templates.TemplateResponse("index.html", {
        "request": request,
        "tabs_count": tabs_count,
        "spaces_count": spaces_count,
        "recent_votes": vote_data
    })


@app.post("/")
async def create_vote(team: Annotated[str, Form()]):
    if team not in ["TABS", "SPACES"]:
        raise HTTPException(status_code=400, detail="Invalid vote")

    try:
        votes_collection.add({
            "team": team,
            "time_cast": datetime.datetime.utcnow().isoformat()
        })
        return {"detail": "Vote recorded successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
