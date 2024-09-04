from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Startup, SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def base():
    return {"Bem vindo à API"}

@app.get("/startups/{page_num}")
def retornar_startups(page_num: int, limit: int = 20, db: Session = Depends(get_db)):
    offset = (page_num - 1) * limit
    startups = db.query(Startup).offset(offset).limit(limit).all()
    return startups

@app.get("/startups/name/{startup_name}")
def buscar_startup_nome(startup_name: str, db: Session = Depends(get_db)):
    startup = db.query(Startup).filter(Startup.name == startup_name).first()
    if startup is None:
        raise HTTPException(status_code=404, detail="Startup não encontrada no banco de dados.")
    return startup

@app.get("/startups/id/{startup_id}")
def buscar_startup(startup_id: str, db: Session = Depends(get_db)):
    startup = db.query(Startup).filter(Startup.id == startup_id).first()
    if startup is None:
        raise HTTPException(status_code=404, detail="Startup não encontrada no banco de dados.")
    return startup

@app.get("/startups/city/{city}")
def buscar_cidade(city: str, db: Session = Depends(get_db)):
    startups = db.query(Startup).filter(func.lower(Startup.city) == func.lower(city)).all()
    if not startups:
        raise HTTPException(status_code=404, detail="Nenhuma startup encontrada nessa cidade.")
    return startups

@app.get("/startups/state/{state_code}")
def buscar_estado(state_code: str, db: Session = Depends(get_db)):
    startups = db.query(Startup).filter(func.lower(Startup.state_code) == func.lower(state_code)).all()
    if not startups:
        raise HTTPException(status_code=404, detail="Nenhuma startup encontrada nesse Estado.")
    return startups
