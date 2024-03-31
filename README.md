# FastAPI gets information and images of books API

This FastAPI application provides endpoints to retrieve images of books stored in a PostgreSQL database and get information about all books.

![fastapi](https://img.shields.io/badge/fastapi-0.110.0-blue)
![pillow](https://img.shields.io/badge/pillow-10.2.0-blue)
![psycopg2](https://img.shields.io/badge/psycopg2-2.9.9-blue)
![pydantic](https://img.shields.io/badge/pydantic-2.6.4-blue)
![python-dotenv](https://img.shields.io/badge/dotenv-1.0.1-blue)
![uvicorn](https://img.shields.io/badge/uvicorn-0.29.0-blue)

## Endpoints

### Get Image by ID

- **URL**: `/image/{image_id}`
- **Method**: `GET`
- **Description**: Retrieves an image of a book by its ID from the database.

### Get All Books

- **URL**: `/all_books`
- **Method**: `GET`
- **Description**: Retrieves information about all books stored in the database.

## Technologies Used

- FastAPI: For building the web API.
- PostgreSQL: For storing book data and images.
- PIL (Python Imaging Library): For handling image data.
- psycopg2: For interacting with the PostgreSQL database.
- dotenv: For loading environment variables from a .env file.

## Setup

1. Clone the repository.
2. Install the required dependencies:

    pip install -r requirements.txt


1. Set up a PostgreSQL database and provide the connection details in a `.env` file.
2. Run the FastAPI application:

    uvicorn app.main:app --reload

