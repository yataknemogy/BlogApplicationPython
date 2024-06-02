# Blog Application

A Django-based blog application allowing users to create, view, edit, and delete blog posts. This application includes features such as commenting on posts and uploading images.

## Features

- Create, view, edit, and delete blog posts
- Optional commenting on blog posts
- Optional image uploads to blog posts
- Admin interface for managing posts

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 3.x
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yataknemogy/blog.git
    cd blog
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    - Go to `http://127.0.0.1:8000` to view the blog.
    - Go to `http://127.0.0.1:8000/admin` to access the admin interface.

## Usage

### Creating a Post

1. Log in to the admin interface at `http://127.0.0.1:8000/admin`.
2. Click on "Posts" and then "Add Post".
3. Fill in the title and content, then click "Save".

### Viewing Posts

- Visit `http://127.0.0.1:8000` to see a list of all blog posts.
- Click on the post title to view the detailed post.

### Editing or Deleting a Post

1. Log in to the admin interface at `http://127.0.0.1:8000/admin`.
2. Click on "Posts" and then on the post you want to edit or delete.
3. Make changes and click "Save" or click "Delete" to remove the post.

### Additional Features

#### Comments

1. Uncomment and configure the code related to comments in the `blog` app.
2. Apply migrations and update admin settings to manage comments.

#### Image Uploads

1. Uncomment and configure the code related to image uploads in the `blog` app.
2. Install necessary dependencies (e.g., Pillow) and update settings for media files.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
