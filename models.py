from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./startups.db" 

engine = create_engine(DATABASE_URL) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Startup(Base):
    __tablename__ = "startups"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String)
    state_code = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    labels = Column(Integer)
    founded_at = Column(String)
    closed_at = Column(String, nullable=True)
    funding_rounds = Column(Float)
    funding_total_usd = Column(Float)
    status = Column(String)
    category_code = Column(String)
    


Base.metadata.create_all(bind=engine)
