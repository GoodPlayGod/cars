from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

URL = 'postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/query'

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CarDB(Base):
    __tablename__ = 'cars_litvinovich'

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price_per_day = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)
