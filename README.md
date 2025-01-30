# Pantry Pirates


**Pantry Pirates** is a creative and interactive web application designed to help users navigate the treasures of their pantry and create delicious meals tailored to their preferences. This project is a submission for the **8th Grade Technology Student Association (TSA)** and showcases web development, teamwork, and innovative use of technology.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Components](#components)
- [Why Flask?](#why-flask)
- [Why GitHub?](#why-github)
- [Using AI in the Project](#using-ai-in-the-project)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Instructions to Use](#instructions-to-use)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

---

## Overview

**Pantry Pirates** was developed as part of an **8th Grade TSA project** to demonstrate the potential of technology in solving everyday problems. The idea originated from the question:

> *"How can we make better use of what's already in our pantry while learning web development?"*

This application allows users to:
- **Search Recipes:** Find recipes based on available ingredients.
- **Take a Survey:** Share preferences like favorite cuisine, dietary restrictions, and more.
- **Receive Personalized Recommendations:** Tailored recipes that match user preferences and pantry contents.
- **View Recipe Details:** Step-by-step instructions and ingredient lists for each recipe.

---

## Features

1. **Interactive Home Page:**
   - Welcome message with quick access to seasonal recipes and surveys.

2. **Dynamic Recipe Search:**
   - Users can search recipes by title, description, or ingredients.

3. **Survey Results Display:**
   - View all saved survey responses in an organized table.

4. **Custom Recipe Recommendations:**
   - Recipes filtered based on user survey responses.

5. **Responsive Design:**
   - Built with Bootstrap, ensuring compatibility on all devices.

6. **Modern UI:**
   - A clean, pirate-themed design with intuitive navigation.

---

## Components

1. **Flask Framework:**
   - Python-based framework used to build the backend and handle dynamic content.

2. **SQLite Database:**
   - Stores survey responses and ensures data persistence.

3. **Jinja2 Templating:**
   - Dynamically renders HTML pages based on user input and database content.

4. **Bootstrap:**
   - Provides a responsive and visually appealing design.

5. **GitHub:**
   - Used for version control, team collaboration, and code hosting.

---

## Why Flask?

Flask was chosen because it’s:
- **Lightweight and Flexible:** Perfect for small projects like Pantry Pirates.
- **Beginner-Friendly:** Easy to learn and use for 8th graders starting with web development.
- **Dynamic Content:** Allows integration of Python logic with HTML templates.

---

## Why GitHub?

GitHub was essential for:
- **Version Control:** Ensures the project remains organized even as features are added or updated.
- **Collaboration:** Multiple team members can work on the project simultaneously.
- **Showcasing the Project:** GitHub serves as a portfolio to share this project with others, including judges and potential collaborators.

---

## Using AI in the Project

Artificial Intelligence (AI) played a key role in:
- **Design Assistance:** AI tools helped suggest page layouts, color schemes, and functional components.
- **Code Generation:** AI provided initial drafts for Flask routes, HTML templates, and CSS styles, which were customized by the team.
- **Debugging:** AI identified and resolved coding errors during development.
- **Documentation:** This README was drafted with AI assistance to ensure clarity and professionalism.

---

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- **Python** (3.6 or higher)
- **pip** (Python package manager)
- **Git** (optional, for cloning the repository)

---

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/pantry-pirates.git
   cd pantry-pirates
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the Database**
   ```bash
   python init_db.py
   ```

---

## Running the Application

To start the application:
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## Instructions to Use

### 1. Home Page
- View seasonal recipes and access the survey.
- Navigate to other sections via the navbar.

### 2. Survey Page
- Share your name, favorite cuisine, dietary restrictions, and available ingredients.
- Submit the survey to see personalized recipe recommendations.

### 3. Recipes Page
- Browse all recipes or search using the search bar.
- Click "View Recipe" to see step-by-step instructions.

### 4. Survey Results Page
- Admins can view all submitted survey responses in a table format.

---

## Project Structure

```
pantry-pirates/
├── app.py                 # Main Flask application
├── init_db.py             # Initializes the SQLite database
├── requirements.txt       # Lists dependencies
├── templates/             # HTML templates
│   ├── base.html          # Shared base layout
│   ├── home.html          # Home page
│   ├── survey.html        # Survey page
│   ├── recipes.html       # Recipe listing page
│   ├── recipe_detail.html # Detailed recipe page
│   ├── survey_results.html # Displays survey responses
│   └── 404.html           # Custom 404 error page
└── static/
    └── css/
        └── styles.css     # Custom styles
```

---

## Acknowledgments

- **Mentorship:** Thanks to our teacher and mentors for guiding us through the process.
- **OpenAI:** For AI assistance in designing and debugging the site.
- **Flask and Python Communities:** For extensive documentation and tutorials.
- **GitHub:** For providing a platform to host and share the project.

---

## Why This Project Deserves First Place

This project stands out because it:
1. **Solves a Real Problem:** Helps users make the best use of pantry ingredients.
2. **Showcases Technical Skills:** Demonstrates Python, Flask, database integration, and responsive design.
3. **Uses Modern Tools:** Incorporates AI and GitHub for enhanced productivity.
4. **Encourages Learning:** Reflects the creativity and teamwork of 8th-grade students passionate about technology.

---

**Let the treasure hunt for recipes begin!** 🏴‍☠️🍲
