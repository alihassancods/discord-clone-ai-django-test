# Messaging App

This is a full-stack messaging application built using Django, HTML, CSS, and JavaScript. The application allows users to communicate in real-time, similar to platforms like Discord.

## Features

- User authentication
- Real-time messaging
- Chat rooms
- User-friendly interface

## Technologies Used

- Django: A high-level Python web framework for rapid development.
- HTML/CSS: For structuring and styling the web pages.
- JavaScript: For client-side interactivity and real-time updates.
- SQLite: A lightweight database for storing application data.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd messaging-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

- Register a new account or log in with an existing account.
- Create or join chat rooms to start messaging.
- Enjoy real-time communication with other users.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.