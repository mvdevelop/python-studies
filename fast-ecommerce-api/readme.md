
# FastAPI Ecommerce API

Simple ecommerce API built with **FastAPI** using the **MVC architecture pattern** and **MongoDB** as the database.

## Technologies

- Python
- FastAPI
- MongoDB
- Pydantic
- Uvicorn
- MVC Architecture

## Project Structure


ecommerce_api
│
├── app
│ ├── main.py
│
├── controllers
│ ├── product_controller.py
│ └── order_controller.py
│
├── models
│ ├── product_model.py
│ └── order_model.py
│
├── views
│ ├── product_view.py
│ └── order_view.py
│
├── .env
├── .gitignore
└── README.md


## Installation

Clone the repository:


git clone https://github.com/yourusername/ecommerce-fastapi.git

cd ecommerce-fastapi


Create a virtual environment:


python -m venv venv


Activate the environment:

Linux / Mac


source venv/bin/activate


Windows


venv\Scripts\activate


Install dependencies:


pip install fastapi uvicorn pymongo python-dotenv


## Environment Variables

Create a `.env` file in the root directory:


MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=ecommerce_db


## Run the Application


uvicorn app.main:app --reload


The API will be available at:


http://localhost:8000


API documentation (Swagger):


http://localhost:8000/docs


## Features

- Create products
- List products
- Create orders
- List orders

## Future Improvements

- User authentication (JWT)
- Shopping cart
- Payment integration
- Product categories
- Docker support

## Author

mvdevelop  
