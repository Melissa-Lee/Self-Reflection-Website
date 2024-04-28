# SELF-REFLECTION APP
#### Video Demo: https://youtu.be/NpQvF4keLrY
#### Description:

# Self-Reflection Form Application

This is a Flask web application that allows users to submit self-reflections and store them in a SQLite database. Users can input the date, select a category, and provide their reflection content. Additionally, users can view their past reflections and remove them if needed.

## Features

- **Add Reflections**: Users can submit their reflections using a form with fields for date, category, and reflection content.
- **View Reflections**: Users can view their past reflections, including the date, category, and content.
- **Remove Reflections**: Users have the option to remove any reflection from their records.

## Technologies Used

- **Flask**: Flask is a micro web framework for Python used to develop web applications.
- **SQLite**: SQLite is a lightweight relational database management system used for storing the reflections.
- **Jinja2**: Jinja2 is a template engine for Python used to generate HTML templates.
- **CS50 Library**: The CS50 library is used to interact with the SQLite database.
- **HTML/CSS**: HTML and CSS are used for the structure and styling of the web pages.

## Installation and Usage

1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

- Upon accessing the application, users will see a form where they can input their self-reflections.
- After submitting a reflection, users will be redirected to a page displaying their past reflections.
- Users can also remove any reflection by clicking the "Remove" button next to it.
