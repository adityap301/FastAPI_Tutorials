from fastapi import APIRouter, HTTPException
from models.product_model import Product
from typing import List
from fastapi import status
from exceptions.ProductNotFoundException import ProductNotFoundException
from utils.logger import Logger
import traceback


LOGGER = Logger(__name__).get_logger()

router = APIRouter(
    prefix="/products_im", 
    tags=["products_im"]
)

products = [
    Product(id="1", name="Product 1", description="Description 1", price=10.0, quantity=100),
    Product(id="2", name="Product 2", description="Description 2", price=20.0, quantity=200),
    Product(id="3", name="Product 3", description="Description 3", price=30.0, quantity=300),
]


@router.get("/", summary="Get all products", response_model=List[Product])
def get_all_products():
    LOGGER.info("Retrieving all products")
    return products


@router.get("/{id}", summary="Product by ID", response_model=Product)
def get_product_by_id(id: str):
    for product in products:
        if product.id == id:
            LOGGER.info(f"Product retrieved with id: {id}")
            return product
    LOGGER.error(f"Product with id: {id} not found")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@router.post("/", summary="Add a product", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(request: Product):
    products.append(request)
    LOGGER.info(f"Added product with id: {request.id} to list")
    return request


@router.put("/{id}", summary="Update a product", response_model=Product)
def update_product(id: str, request: Product):
    for idx, product in enumerate(products):
        if product.id == id:
            LOGGER.info(f"Unpdating product details having id: {id}")
            request.id = id
            products[idx] = request
            return request
    LOGGER.error(f"Product with id: {id} not found")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@router.delete("/{id}", summary="Delete a product", response_model=Product)
def delete_product(id: str):
    try:
        for idx, product in enumerate(products):
            if product.id == id:
                deleted_product = products.pop(idx)
                LOGGER.info(f"Product deleted with id: {id}")
                return deleted_product
        raise ProductNotFoundException
    except ProductNotFoundException as e:
        LOGGER.error("Product with id: {id} not found")
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    except Exception as e:
        LOGGER.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
