from fastapi import APIRouter, HTTPException, Depends
from models.product_model import Product
from database.db_models.product_model import ProductDB
from typing import List
from fastapi import status
from database.db_connection import get_db_conn
from sqlalchemy.orm import Session
from exceptions.ProductNotFoundException import ProductNotFoundException 
from utils.logger import Logger
import traceback


LOGGER = Logger(__name__).get_logger()


router = APIRouter(
    prefix="/api/db/products", 
    tags=["products"]
)


@router.get("/", summary="Get all products", response_model=List[Product])
def get_all_products(db_conn: Session = Depends(get_db_conn)):
    try:
        products = db_conn.query(ProductDB).all()
        LOGGER.info(f"Fetched {len(products)} products from db")
        return products
    except Exception as e:
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=f"Something went wrong")
    

@router.get("/{id}", summary="Product by ID", response_model=Product)
def get_product_by_id(id: str, db_conn: Session = Depends(get_db_conn)):
    try:
        product = db_conn.query(ProductDB).filter(ProductDB.id == id).first()
        if product:
            LOGGER.info(f"Product found in db with id: {id}")
            return product
        else:
            LOGGER.info(f"Product does not exist in db with id: {id}")
            raise ProductNotFoundException
    except Exception as e:
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Product not found")


@router.post("/", summary="Add a product", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(request: Product, db_conn: Session = Depends(get_db_conn)):
    try:
        product_dict = request.model_dump()
        db_conn.add(ProductDB(**product_dict))
        db_conn.commit()
        LOGGER.info("Product added to db")
        return request
    except Exception as e:
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=f"Something went wrong")


@router.put("/{id}", summary="Update a product", response_model=Product)
def update_product(id: str, request: Product, db_conn: Session = Depends(get_db_conn)):
    try:
        db_product = db_conn.query(ProductDB).filter(ProductDB.id == id).first()
        if db_product:
            db_product.name = request.name
            db_product.description = request.description
            db_product.price = request.price
            db_product.quantity = request.quantity
            db_conn.commit()
            return db_product
        else:
            LOGGER.info(f"No product found for the id: {request.id}")
            raise ProductNotFoundException
    except ProductNotFoundException as e:
        LOGGER.error("Product with id: {id} not found")
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    except Exception as e:
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@router.delete("/{id}", summary="Delete a product", response_model=Product)
def delete_product(id: str, db_conn: Session = Depends(get_db_conn)):
    try:
        db_product = db_conn.query(ProductDB).filter(ProductDB.id == id).first()
        if db_product:
            db_conn.delete(db_product)
            db_conn.commit()
            LOGGER.info(f"Product deleted with id: {id}")
            return db_product
        else:
            raise ProductNotFoundException
    except ProductNotFoundException as e:
        LOGGER.error("Product with id: {id} not found")
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    except Exception as e:
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
