# 🐶 Dog Gallery Backend API (FastAPI + SQLAlchemy)

This project is a **backend API** built with **FastAPI** that fetches dog breed data from the public **Dog CEO API** and provides features like **liking/unliking images** and **tracking recently viewed breeds** using a local **SQLite database**.

---

## 🚀 Features

- **Dog Breed Data:** Fetch all available dog breeds and their images.
- **Like/Unlike Feature:** Save or remove your favorite dog images.
- **Recently Viewed Breeds:** Track the last 5 breeds you viewed.
- **RESTful API:** Clean, modern, and scalable design.
- **Auto Documentation:** Swagger UI available at `/docs`.
- **Database Integration:** Local SQLite database with SQLAlchemy ORM.

---

## 🧰 Tech Stack

- **Backend Framework:** FastAPI
- **Database:** SQLite + SQLAlchemy ORM
- **External API:** [Dog CEO API](https://dog.ceo/dog-api/)
- **Data Validation:** Pydantic
- **Server:** Uvicorn
- **CORS Support:** For frontend integration

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd dog_gallery_backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

### 6. Access API Documentation

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

---

## 📖 API Documentation

### **Base URL:**

```
http://127.0.0.1:8000
```

### **Endpoints**

#### 1. `GET /breeds`

Fetch all available dog breeds.  
**Response:**

```json
{
  "bulldog": ["boston", "english", "french"],
  "poodle": []
}
```

#### 2. `GET /breed/{breed_name}/images`

Fetch images of a specific breed.  
**Response:**

```json
[
  "https://images.dog.ceo/breeds/labrador/image1.jpg",
  "https://images.dog.ceo/breeds/labrador/image2.jpg"
]
```

#### 3. `POST /like`

Like a dog image.  
**Request:**

```json
{ "image_url": "https://images.dog.ceo/breeds/labrador/image1.jpg" }
```

**Response:**

```json
{ "message": "Liked" }
```

#### 4. `DELETE /like`

Unlike a dog image.  
**Request:**

```json
{ "image_url": "https://images.dog.ceo/breeds/labrador/image1.jpg" }
```

**Response:**

```json
{ "message": "Unliked" }
```

#### 5. `GET /likes`

Fetch all liked images.  
**Response:**

```json
[
  "https://images.dog.ceo/breeds/labrador/image1.jpg",
  "https://images.dog.ceo/breeds/hound/image2.jpg"
]
```

#### 6. `POST /viewed`

Store a recently viewed breed.  
**Request:**

```json
{ "breed": "bulldog" }
```

**Response:**

```json
{ "message": "Viewed saved" }
```

#### 7. `GET /viewed`

Fetch the last 5 recently viewed breeds.  
**Response:**

```json
["bulldog", "labrador", "poodle"]
```

---

## 📂 Folder Structure

```
dog_gallery_backend/
│
├── main.py          # FastAPI app with routes
├── database.py      # SQLAlchemy models and DB setup
├── dog_gallery.db   # SQLite database
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

Author
Samiksha Deshmukh
