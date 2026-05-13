# HPE Work Experience Project 2026

## Project Overview

This is a web application that serves as an educational platform for HPE's STEM Work Experience program, which is run twice a year for local year 10-12 students in April and July. The project demonstrates full-stack development concepts through a fact management system where users can:

- **View random facts** from a pre-populated database of facts
- **Create and submit** their own facts to the database
- **Vote** on facts using a like/dislike system
- **Explore** different categories of interesting information

## Educational Purpose

The application is designed to teach work experience students:
- **Web development fundamentals** (HTML, CSS, JavaScript)
- **Backend development** with Python Flask
- **Database operations** using SQLite
- **REST API concepts** and CRUD operations
- **Testing methodologies** using the Arrange-Act-Assert pattern
- **Project structure** demonstrating best practices

The codebase includes comprehensive worksheets and guides covering database concepts, REST APIs, and unit testing to provide hands-on learning experiences in modern software development practices.

# Development Instructions

## To setup the database

1. Create the SQLite database (facts.db), create a facts table, and insert sample data:

```make setup-db```

## To inspect the database

1. Open the SQLite shell (useful for debugging purposes):

```make db-shell```

2. Exit the SQLite shell:

```.quit```

## To run the app

1. Create a virtual environment:

```python3 -m venv venv```

2. Activate the virtual environment:

```source venv/bin/activate```

3. Install dependencies:

```pip install -r requirements.txt```

4. Run the app:

```python app.py```
