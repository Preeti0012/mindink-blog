<<<<<<< HEAD
![testing-ezgif com-speed](https://github.com/user-attachments/assets/aa29732b-c4a6-42f6-8342-5bae54b39a46)


=======
![testing-ezgif com-speed](https://github.com/user-attachments/assets/df3d7439-dc7d-463b-bc32-112ce7b1df69)


---
>>>>>>> b2f03a1 (Update README.md)

````markdown
# 📝 Django Blog Creation API

This is a Django-based **Blog Creation API** that allows users to create, edit, delete, and view blog posts. Additionally, it features grammar correction and search functionality. The API is built using **Django REST Framework**.

---

## 🚀 Features

- ✅ User-created blog posts  
- ✏️ Blog post creation, editing, and deletion  
- 🧠 Grammar checking for blog content  
- 🔍 Search functionality to filter blog posts  
- 🌐 API endpoints for interaction  

---

## ⚙️ Installation

### 📋 Prerequisites

Ensure you have the following installed:

- Python 3.11.9  
- Django 4.2  
- Django REST Framework  

---

### 🛠️ Steps to Set Up the Project

1. **Clone the repository from GitHub:**

   ```bash
   git clone <your_github_repository_url>
````

2. **Navigate to the project folder:**

   ```bash
   cd <cloned_repository_folder_name>
   ```

3. **Create and activate a virtual environment:**

   On **macOS/Linux**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On **Windows**:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the server:**

   ```bash
   python manage.py runserver
   ```

---

## 📡 API Endpoints

### 📚 Blog Management

#### 🔸 Create Blog

`POST /blog/`

**Request Body:**

```json
{
  "title": "My First Blog",
  "content": "This is my first blog post content."
}
```

**Response:**

```json
{
  "id": 1,
  "title": "My First Blog",
  "content": "This is my first blog post content.",
  "created_at": "2025-05-19T10:00:00Z",
  "updated_at": null
}
```

#### ✏️ Edit Blog

`PUT /blog/<blog_id>/`

#### ❌ Delete Blog

`DELETE /blog/<blog_id>/`

#### 📥 Get All Blogs

`GET /blog/`

#### 🔍 Search Blogs

`GET /blog/?search=keyword`

---

### ✨ Grammar Fixing

#### 🧠 Fix Grammar in Blog Content

`POST /blog/fix-grammar/`

**Request Body:**

```json
{
  "content": "This is my frst blog."
}
```

**Response:**

```json
{
  "corrected_content": "This is my first blog."
}
```

---

## ⚠️ Error Handling

* `400 Bad Request`: Missing or invalid data.
* `404 Not Found`: Blog post not found.
* `500 Internal Server Error`: Unexpected server issues.

---

## 📊 Evaluation Parameters

* ✅ **Overall Implementation**: Proper structure, use of Django best practices, and adherence to requirements.
* 🐞 **Bug-Free**: The API should work seamlessly without any issues or errors.
* 🧹 **Code Quality**: Clean, maintainable, and readable code, including proper documentation and comments.

---

## 📄 License

This project is licensed under the **MIT License**.

```

---
<<<<<<< HEAD
<<<<<<< HEAD
```
=======

Let me know if you want this in a downloadable `.md` file or want to add badges (e.g., for license, Python version, or GitHub actions).
=======
>>>>>>> 006f910 (Update README.md)
```

>>>>>>> b2f03a1 (Update README.md)
