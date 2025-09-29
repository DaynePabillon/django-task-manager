# Django Task Manager

A simple Django web application for managing tasks and tracking productivity.

## Features

- Task creation and management
- Priority levels (High, Medium, Low)
- Status tracking (Pending, In Progress, Completed)
- Due date management
- User assignment
- Admin interface for task management
- Responsive design

## Setup Instructions

1. Create a virtual environment:
   ```
   python -m venv env
   ```

2. Install dependencies:
   ```
   .\env\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   .\env\Scripts\python.exe manage.py makemigrations
   .\env\Scripts\python.exe manage.py migrate
   ```

4. Create a superuser:
   ```
   .\env\Scripts\python.exe manage.py createsuperuser
   ```

5. Run the development server:
   ```
   .\env\Scripts\python.exe manage.py runserver
   ```

## Project Structure

- `task_app/` - Main application containing models, views, and templates
- `task_project/` - Django project settings and configuration
- `static/` - Static files (CSS, JavaScript)
- `templates/` - HTML templates
- `requirements.txt` - Python dependencies

## Usage

- Visit the home page to see the welcome message
- Navigate to the tasks page to view all tasks
- Click on individual tasks to view details and update status
- Access the admin panel at `/admin/` to manage tasks and users