# Certificate Management System API

This is the backend API for a certificate management system, developed in Django. The system generates certificates for courses attended by users.

## Features

- **User Authentication:** Secure login and authentication for users.
- **Course Management:** CRUD operations for managing courses.
- **Certificate Generation:** Automatically generate certificates for completed courses.
- **Admin Dashboard:** Admin interface for managing users and certificates.

## Technologies Used

- **Django:** High-level Python web framework for rapid development.
- **Django REST Framework:** Toolkit for building Web APIs.
- **PostgreSQL:** Relational database system.
- **Docker:** Containerization for development and deployment.

## Prerequisites

Before starting, ensure you have the following installed:

- Python (version 3.8 or higher)
- PostgreSQL
- Docker (optional, for containerization)

## Installation

Follow these steps to set up and run the project locally:

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables:

    Create a `.env` file in the root of the project and add the following variables:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/certificate_db
    ```

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser for the admin dashboard:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Open your browser and navigate to `http://localhost:8000/admin` to access the admin dashboard.

## Usage

Once the API is running, you can perform the following actions:

- **User Authentication:** Register and log in users.
- **Manage Courses:** Use API endpoints to create, read, update, and delete courses.
- **Generate Certificates:** Automatically generate and retrieve certificates for completed courses.
- **Admin Dashboard:** Manage users and certificates via the admin interface.

## API Endpoints

Here are some of the main API endpoints:

- **User Registration:** `POST /api/register/`
- **User Login:** `POST /api/login/`
- **Course List:** `GET /api/courses/`
- **Course Detail:** `GET /api/courses/<id>/`
- **Create Course:** `POST /api/courses/`
- **Update Course:** `PUT /api/courses/<id>/`
- **Delete Course:** `DELETE /api/courses/<id>/`
- **Generate Certificate:** `POST /api/certificates/`

## Contributing

If you wish to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push your changes to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## Contact

For more information or inquiries, you can contact me via email: [jojeda5171@uta.edu.ec](mailto:jojeda5171@uta.edu.ec).

---

Thank you for using the Certificate Management System API!
