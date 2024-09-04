from sqlalchemy.orm import Session
from models import Startup, SessionLocal, engine
import pandas as pd

df = pd.read_csv('startup data.csv')

session = Session(bind=engine)


for index, row in df.iterrows():
    if session.query(Startup).filter_by(id=row['id']).first():
        continue  

    startup = Startup(
        id=row['id'],
        name=row['name'],
        city=row['city'],
        state_code=row['state_code'],
        latitude=row['latitude'],
        longitude=row['longitude'],
        labels=row['labels'],
        founded_at=row['founded_at'],
        closed_at=row['closed_at'],
        funding_rounds=row['funding_rounds'],
        funding_total_usd=row['funding_total_usd'],
        status=row['status'],
        category_code =row['category_code']
    )
    session.add(startup)

session.commit()

session.close()
        