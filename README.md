# API QA Automation with Python

Hey there! 👋

This project is an automated API testing using Python and `pytest`. 

---

## What’s this project about?

I'm testing a public API ([Reqres](https://reqres.in)), which provides fake user data and typical API endpoints like:

- Getting lists of users (with pagination)
- Creating users
- Handling errors (like user not found)

The tests include:

- Validating response status codes
- Checking JSON response structures
- Ensuring the API key authorization works correctly

This project shows how to:

- Organize tests using `pytest`
- Write clean, reusable code with a helper function for API requests
- Use Python’s `requests` library to interact with APIs

---

## Getting started — setup instructions

### 1. Clone this repo

```bash
git clone https://github.com/uncleejay/api-automation-python.git
cd api-automation-python
```

### 2. Set up a Python virtual environment (venv)

Create a virtual environment to keep dependencies isolated:

```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# OR
venv\Scripts\activate      # Windows
```

### 3. Install dependecies

```
pip install -r requirements.txt
```

### 4. Running the test

Once everything is setup, run all tests with

```
pytest
```

