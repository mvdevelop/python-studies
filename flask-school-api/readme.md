
# School API - Flask MVC

REST API developed with **Python and Flask** following the **MVC (Model-View-Controller)** architecture pattern.
This project simulates a **school management API** with support for **student registration and image upload**.

## 🚀 Features

* Student registration
* List students
* Upload student profile images
* MVC architecture
* RESTful API design

## 🏗️ Project Structure

```
school_api
│
├── app
│   ├── __init__.py
│   ├── config.py
│
│   ├── models
│   │   └── student_model.py
│
│   ├── controllers
│   │   └── student_controller.py
│
│   ├── routes
│   │   └── student_routes.py
│
│   └── services
│       └── upload_service.py
│
├── uploads
│
├── run.py
├── requirements.txt
├── .env
└── README.md
```

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/school-api.git
```

Enter the project folder:

```
cd school-api
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## ▶️ Running the API

Start the server:

```
python run.py
```

Default server:

```
http://localhost:5000
```

## 📌 API Endpoints

### Create Student

POST `/students`

Form-data:

```
name: Student name
age: Student age
image: image file
```

Response:

```
{
 "id": 1,
 "name": "Marcos",
 "age": "20",
 "image": "photo.jpg"
}
```

### List Students

GET `/students`

Response:

```
[
 {
  "id": 1,
  "name": "Marcos",
  "age": "20",
  "image": "photo.jpg"
 }
]
```

## 📂 Image Upload

Uploaded images are stored in the **uploads/** directory.

## 🧰 Technologies Used

* Python
* Flask
* REST API
* MVC Architecture
* File Upload Handling

## 📈 Future Improvements

* Database integration (PostgreSQL / MongoDB)
* Authentication (JWT)
* Pagination
* Validation with Marshmallow
* Docker containerization
* Automated tests

## 👨‍💻 Author

Developed by mvdevelop
