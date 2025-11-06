# URL Shortener (FastAPI + SQLite + Rate Limit)

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-pytest-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


Create short codes, redirect, and list. Simple in-memory rate limit per IP.

## Run
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
