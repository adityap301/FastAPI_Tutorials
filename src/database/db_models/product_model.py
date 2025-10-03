from sqlalchemy import Column, Integer, String, Float
from database.db_models.base import Base

class ProductDB(Base):
    __tablename__ = "Products"
    
    id = Column(String(36), primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)
