from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from database import init_db, Like, Viewed, SessionLocal
import requests

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update with your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DOG_API_BASE = "https://dog.ceo/api"

class LikeRequest(BaseModel):
    image_url: str

class ViewedRequest(BaseModel):
    breed: str

@app.get("/breeds")
def get_all_breeds():
    res = requests.get(f"{DOG_API_BASE}/breeds/list/all")
    if res.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch breeds")
    return res.json()["message"]

@app.get("/breed/{breed_name}/images")
def get_breed_images(breed_name: str):
    res = requests.get(f"{DOG_API_BASE}/breed/{breed_name}/images")
    if res.status_code != 200:
        raise HTTPException(status_code=404, detail="Breed not found")
    return res.json()["message"]

@app.post("/like")
def like_image(payload: LikeRequest):
    db = SessionLocal()
    if db.query(Like).filter(Like.image_url == payload.image_url).first():
        raise HTTPException(status_code=400, detail="Already liked")
    db.add(Like(image_url=payload.image_url))
    db.commit()
    return {"message": "Liked"}

@app.delete("/like")
def unlike_image(payload: LikeRequest):
    db = SessionLocal()
    image = db.query(Like).filter(Like.image_url == payload.image_url).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    db.delete(image)
    db.commit()
    return {"message": "Unliked"}

@app.get("/likes")
def get_liked_images():
    db = SessionLocal()
    return [like.image_url for like in db.query(Like).all()]

@app.post("/viewed")
def add_viewed(payload: ViewedRequest):
    db = SessionLocal()
    db.add(Viewed(breed=payload.breed))
    db.commit()
    return {"message": "Viewed saved"}

@app.get("/viewed")
def get_recent_views():
    db = SessionLocal()
    views = db.query(Viewed).order_by(Viewed.timestamp.desc()).limit(5).all()
    return [v.breed for v in views]
