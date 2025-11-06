from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select
from time import time
from .db import init_db, get_session
from .models import Link

app = FastAPI(title="URL Shortener")
RATE = {}

@app.on_event("startup")
def startup(): init_db()

@app.post("/shorten")
def shorten(code: str, url: str, session: Session = Depends(get_session)):
    if session.exec(select(Link).where(Link.code==code)).first():
        raise HTTPException(400, "Code exists")
    l = Link(code=code, url=url)
    session.add(l); session.commit(); session.refresh(l)
    return {"code": code, "url": url}

@app.get("/{code}")
def go(code: str, request: Request, session: Session = Depends(get_session)):
    # basic rate limit: 5 req per 10s per ip
    ip = request.client.host if request.client else "anon"
    now = time()
    wins = RATE.get(ip, [])
    wins = [t for t in wins if now - t < 10]
    if len(wins) >= 5: raise HTTPException(429, "Too Many")
    wins.append(now); RATE[ip] = wins
    l = session.exec(select(Link).where(Link.code==code)).first()
    if not l: raise HTTPException(404, "Not found")
    return RedirectResponse(l.url)
