import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session

from db.database import get_db
from models.job import StoryJob
from schemas.job import StoryJobRepsonse