 # Software Quality Tools Project

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Fork and Clone the Repository](#fork-and-clone-the-repository)
3. [Installation](#installation)
4. [Run the Flask App](#run-the-flask-app)
5. [Testing](#testing)

---

## Prerequisites

Before you begin, ensure you have the following software installed:

- **Python**: Version 3.7 or higher
- **pip**: Python package installer
- **Git**: To clone the repository

You can check the installed versions by running the following commands:

```bash
python --version
pip --version
git --version
```

## Fork and Clone the Repository

1. Go to the [repository URL](https://github.com/ericBlack1/Software-Quality-Tools-Project).
2. Click on the **Fork** button (top-right corner) to fork the repository to your own GitHub account.
3. Clone your forked repository to your local machine:

   ```bash
   https://github.com/<Your-github-name>/Software-Quality-Tools-Project.git
   ```

4. Navigate into the project directory:

   ```bash
   cd Software-Quality-Tools-Project
   ```

## Installation

1. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:

   - On **Windows**:
   
     ```bash
     venv\Scripts\activate
     ```

   - On **Mac/Linux**:
   
     ```bash
     source venv/bin/activate
     ```

3. **Install the required dependencies**:

   ```bash
   pip install -r flask flask-sqlalchemy flask-login pytest
   ```

   This will install all the necessary libraries for the Flask app to run.

## Run the Flask App

1. **Run the Flask application**:

   ```bash
   python app.py
   ```

2. Open your browser and go to `http://127.0.0.1:5000/` to see the app in action.

---

## Testing
Go to [Github-issues](https://github.com/ericBlack1/Software-Quality-Tools-Project/issues), select the unit test issue you'll implement.
To run the tests, make sure the dependencies are installed (as mentioned in the **Installation** section). Then, you can use `pytest` or any other testing framework that you have set up:

```bash
pytest
```

This will run all the tests in your project.

---

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Create a new pull request.

---

## License

This project is licensed under the MIT License.
