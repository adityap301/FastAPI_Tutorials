from fastapi import APIRouter, HTTPException
from models.product_model import Product
from typing import List
from fastapi import status
from exceptions.ProductNotFoundException import ProductNotFoundException


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
    return products


@router.get("/{id}", summary="Product by ID", response_model=Product)
def get_product_by_id(id: str):
    for product in products:
        if product.id == id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@router.post("/", summary="Add a product", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(request: Product):
    products.append(request)
    return request


@router.put("/{id}", summary="Update a product", response_model=Product)
def update_product(id: str, request: Product):
    for idx, product in enumerate(products):
        if product.id == id:
            request.id = id
            products[idx] = request
            return request
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@router.delete("/{id}", summary="Delete a product", response_model=Product)
def delete_product(id: str):
    try:
        for idx, product in enumerate(products):
            if product.id == id:
                deleted_product = products.pop(idx)
                return deleted_product
        raise ProductNotFoundException
    except ProductNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
