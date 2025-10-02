# FastAPI Tutorials

This project demonstrates the use of FastAPI to build RESTful APIs with database integration using SQLAlchemy. It includes examples of CRUD operations, error handling, and logging.

## Project Structure

```
FastAPI_Tutorials/
├── Course_Materials/          # Presentation decks and demo guides
├── src/                       # Source code
│   ├── database/              # Database connection and models
│   │   ├── db_connection.py   # SQLAlchemy database connection setup
│   │   ├── ecommerce.sqlite   # SQLite Database 
│   │   └── __init__.py
│   ├── exceptions/            # Custom exception classes
│   ├── models/                # Pydantic and Database models
│   ├── routers/               # API routers
│   ├── utils/                 # Utility modules (e.g., logger)
│   ├── fastapi_server.py      # Main FastAPI application
│   └── requirements.txt       # Python dependencies
```

## Features

- **FastAPI**: Framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Lightweight database for development.
- **Logging**: Custom logger for tracking application events.
- **Error Handling**: Proper error responses for API endpoints.


## Developer Setup

Refer to the doumentation [here](./DeveloperSetup.md).

## Running the Application
1. Navigate to the `src` directory:
   ```bash
   cd src
   ```

2. Start the FastAPI server:
   ```bash
   uvicorn fastapi_server:app --reload
   ```

3. Open your browser and navigate to:
   - API documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc documentation: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

### Products
- **GET** `/products/`: Retrieve all products.
- **GET** `/products/{id}`: Retrieve a product by ID.
- **POST** `/products/`: Add a new product.
- **PUT** `/products/{id}`: Update an existing product.
- **DELETE** `/products/{id}`: Delete a product by ID.

## Database
- **SQLite** database file: `src/database/ecommerce.sqlite`
- **Models**: Defined using SQLAlchemy in `src/models/db/product_model.py`.

## Logging
- Logs are managed using a custom logger defined in `src/utils/logger.py`.
- Logs include timestamps, filenames, line numbers, and log levels.

## Error Handling
- Custom exceptions are defined in `src/exceptions/`.
- API endpoints return appropriate HTTP status codes and error messages.
