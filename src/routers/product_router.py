from fastapi import APIRouter


router = APIRouter(
    prefix="/products", 
    tags=["products"]
)

products = ["P1", "P2"]

@router.get("/", summary="Get all products", description="Get all products")
def get_all_products():
    return products


@router.get("/{id}", summary="Product by ID", description="Get product by ID")
def get_product_by_id(id: int):
    return products[id-1]