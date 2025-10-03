from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_models.product_model import Base
from database.db_models.product_model import ProductDB
from models.product_model import Product
import uuid
from utils.logger import Logger


LOGGER = Logger(__name__).get_logger()


db_file_name = "database/ecommerce.sqlite"
db_url = f"sqlite:///{db_file_name}"
db_engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


def get_db_conn():
    db_conn = session()
    try:
        yield db_conn
    finally:
        db_conn.close()


def create_db_and_tables():
    db_conn = session()
    # Create all tables
    Base.metadata.create_all(bind=db_engine)
    products = [
        Product(id=str(uuid.uuid4()), name="iPhone 17", description="Phone by Apple", price=799.0, quantity=100),
        Product(id=str(uuid.uuid4()), name="Samsung Galaxy S25", description="Phone by Samsung", price=829.0, quantity=200),
        Product(id=str(uuid.uuid4()), name="Asus TUF", description="Laptop by Asus", price=649.0, quantity=300),
    ]
    products_cnt = db_conn.query(ProductDB).count()
    if products_cnt == 0:
        LOGGER.info("Populating the table with data")
        for product in products:
            # Convert model to dict
            # Unpack this dict to key-value pairs, to populate the ProductDB model
            product_db = ProductDB(**product.model_dump())
            db_conn.add(product_db)  
        db_conn.commit()
        LOGGER.info("Data populated successfully")
    else:
        LOGGER.info("Data already present in the table")

