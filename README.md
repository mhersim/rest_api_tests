# rest_api_tests


# Install and Create virtual environment:
pip install virtualenv
virtualenv venv

# Activate virtual environment:
Windows: ".\venv\Scripts\activate.bat"
Linux: "source venv/bin/activate"

# To install all required libraries from requirements.txt:
pip install -r requirements.txt

# (Optional) For Deactivate virtual environment run following command:
deactivate

# Run tests:
    To run all test:
        pytest tests -v

    To run only smoke tests
        pytest tests -v -m smoke

    To run only negative tests
        pytest tests -v -m negatives
