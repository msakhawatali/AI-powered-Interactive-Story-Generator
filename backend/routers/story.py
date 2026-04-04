import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks

from db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.story import (
    ComplateStoryResponce, CompleteStoryNodeResponse, CreateStoryRequest
)
from schemas.job import StoryJobResponce

router = APIRouter(
    prefix="/stories",
    tage = ["stories"]
)

def get_session_id()