# Blog Project

## Overview

The Blog Project is a Django application that provides RESTful API endpoints for managing blog posts. The application allows authenticated users to create, read, update, and delete blog posts. Public users can view and search blog posts with pagination support.

## Features

- **User Authentication:** Uses JWT (JSON Web Token) authentication for secure access.
- **Blog Management:** CRUD operations (Create, Read, Update, Delete) for blog posts.
- **Search Functionality:** Allows searching blog posts by title or content.
- **Pagination:** Supports pagination for listing blog posts.

## Requirements

- Python 3.8+
- Django 4.x+
- Django REST Framework (DRF) 3.x+
- Django REST Framework SimpleJWT 5.x+

## Installation

1. **Clone the Repository:**

    ```sh
    git clone <repository-url>
    cd Blog-Project
    ```

2. **Create a Virtual Environment:**

    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a Superuser (Optional for admin access):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Authenticated Endpoints

- **GET /blogs/**
  - Retrieves a list of blog posts for the authenticated user. Supports search and pagination.

- **POST /blogs/**
  - Creates a new blog post.

- **PATCH /blogs/**
  - Updates an existing blog post identified by UUID.

- **DELETE /blogs/**
  - Deletes a blog post identified by UUID.

### Public Endpoints

- **GET /public-blogs/**
  - Retrieves a list of blog posts. Supports search and pagination. No authentication required.

## Models

### BlogModel

- `uuid`: UUID field for unique identification.
- `user`: ForeignKey linking to the User model.
- `title`: Title of the blog post.
- `blog_text`: Content of the blog post.
- `main_image`: Image associated with the blog post.

## Serializers

### BlogSerializers

- Serializes `BlogModel` instances for API responses and requests.

## Error Handling

- Returns appropriate error messages and status codes for invalid requests and server errors.

## Testing

1. **Run Tests:**

    ```sh
    python manage.py test
    ```

## Contributing

1. **Fork the Repository.**
2. **Create a Feature Branch:**

    ```sh
    git checkout -b feature/your-feature
    ```

3. **Commit Your Changes:**

    ```sh
    git commit -am 'Add new feature'
    ```

4. **Push to the Branch:**

    ```sh
    git push origin feature/your-feature
    ```

5. **Create a Pull Request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
