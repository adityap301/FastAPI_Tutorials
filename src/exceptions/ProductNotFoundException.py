class ProductNotFoundException(Exception):
    """Raised when a requested product is not found"""
    def __init__(self, message: str = "Product not found"):
        self.message = message
        super().__init__(message)
