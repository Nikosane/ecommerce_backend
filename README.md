# Simple E-commerce Backend

## Overview
This is a simple e-commerce backend built using Python and an ORM . It provides basic functionality for managing users, products, and orders.

---

## Features
- **User Management**: Registration, login, and profile management.
- **Product Management**: CRUD operations for products.
- **Order Management**: Placing orders, managing order statuses, and retrieving order history.
- **Database Integration**: Fully integrated with an ORM for database operations.

---

## Getting Started

### Prerequisites
- Python 3.8+
- Virtual Environment Tool (e.g., `venv` or `virtualenv`)
- Database (e.g., PostgreSQL, SQLite)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Nikosane/ecommerce-backend.git
   cd ecommerce-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` file with your environment variables:
   ```
   DATABASE_URL=your_database_url
   SECRET_KEY=your_secret_key
   ```

5. Initialize the database:
   ```bash
   python app/database.py
   ```

6. Run the application:
   ```bash
   python app/main.py
   ```

---

## API Endpoints

### User Endpoints
- `POST /users/` - Register a new user.
- `POST /login/` - Authenticate a user.
- `GET /users/{user_id}` - Retrieve user profile.

### Product Endpoints
- `GET /products/` - Retrieve all products.
- `POST /products/` - Create a new product.
- `GET /products/{product_id}` - Retrieve a specific product.
- `PUT /products/{product_id}` - Update a product.
- `DELETE /products/{product_id}` - Delete a product.

### Order Endpoints
- `POST /orders/` - Place a new order.
- `GET /orders/{order_id}` - Retrieve order details.
- `GET /orders/` - Retrieve all orders for a user.

---

## Technologies Used
- **Python**
- **ORM**: SQLAlchemy or Django ORM
- **FastAPI** (for RESTful API development)
- **Pydantic** (for data validation)
- **SQLite/PostgreSQL** (database)

---

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For any inquiries or issues, please email [your-email@example.com].

