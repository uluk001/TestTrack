
# Online Quiz Platform

An online quiz platform built with Django, allowing users to take quizzes and view their results. 

## Features

- User registration and authentication.
- Quiz-taking functionality with question-by-question interaction.
- Immediate feedback upon quiz completion with score and correct/incorrect answers.
- Admin interface for managing quizzes, questions, and choices.

## Installation

Make sure you have Python 3.6 or higher and `pip` installed. 

1. Clone the repository:
   ```
   git clone https://github.com/uluk001/TestTrack.git
   cd TestTrack
   ```

2. Set up a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory with the following settings (modify as necessary):
   ```
   # Basic configurations

   SECRET_KEY=secret
   DEBUG=True
   ```

5. Run migrations to create database schema:
   ```
   python manage.py migrate
   ```

6. Create an admin user:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` in your browser to start using the application.

## Usage

- **To take a quiz:**
  - Register a new user or login.
  - Select a quiz from the available list.
  - Answer each question in sequence. You cannot proceed to the next question without answering the current one.
  - Submit your answers and view your results at the end.

- **Admin users:**
  - Use the Django admin interface to manage quizzes, questions, and answer choices.
  - Access the admin at `http://127.0.0.1:8000/admin/`.


## Contributing

We welcome contributions to the Neocafe project! If you're interested in helping improve Neocafe, please follow these steps:

1. **Fork the repository**: This creates your own copy of the repository where you can make your changes.
2. **Create a new branch**: Use the command `git checkout -b feature/AmazingFeature` to create a new branch for your feature.
3. **Make your changes**: Implement your new feature or bug fix in this branch.
4. **Commit your changes**: Use the command `git commit -m 'Add some AmazingFeature'` to save your changes with a descriptive commit message.
5. **Push the branch**: Use the command `git push origin feature/AmazingFeature` to upload your changes to your forked repository.
6. **Open a Pull Request**: Go to the GitHub page of your forked repository and click on "New pull request" to submit your changes for review.

## Author & Contact

- **Ismailov** - Initial work - [uluk001](https://github.com/uluk001)

If you have questions, suggestions, or would like to report a bug, feel free to contact me at [ulukmanmuratov@gmail.com](mailto:ulukmanmuratov@gmail.com), via Telegram [@ismailovvv001](https://t.me/ismailovvv001), or connect with me on [LinkedIn](https://www.linkedin.com/in/ismailov-uluk-92784a233/).
