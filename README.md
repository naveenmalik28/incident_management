# incident_management
This project is an Incident Management System built using Django Rest Framework (DRF) with MySQL/MariaDB as the database. The system allows users to create, view, update, and delete incidents, with features such as role-based access control, auto-generated incident IDs, and user authentication.

**Features**

-Incident Management: Users can log, view, and manage incidents within the system.

-Role-Based Access Control: Users have different levels of access based on their roles (e.g., Admin, User).

-Auto-Generated Incident IDs: Unique IDs are generated for each incident.

-User Authentication: Secure login and management of user accounts.

-Database: Integrated with MySQL for robust data storage.

**Installation**

1. Set Up the Virtual Environment:

   python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

2. Install Dependencies:

   pip install -r requirements.txt

3. Set Up the Database:

   python manage.py makemigrations

python manage.py migrate

4. Run the Development Server:
   python manage.py runserver

**Usage**

Access the API at http://127.0.0.1:8000/api/.

Use your preferred API client (e.g., Postman) to interact with the API endpoints.   
