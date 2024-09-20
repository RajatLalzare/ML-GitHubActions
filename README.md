# Python Project with CI/CD Integration 🚀

This repository demonstrates a simple Python project integrated with a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions. The project includes basic mathematical operations and unit testing to verify the correctness of functions. It highlights automation of testing through a CI/CD pipeline.

## Project Overview 📚

This project covers:
1. **Mathematical Operations**: Basic operations like addition and subtraction.
2. **Unit Testing**: Ensuring code correctness using `pytest`.
3. **CI/CD Integration**: Automating the testing process using GitHub Actions.
4. **Version Control**: Managing code changes with GitHub.

## Features 🛠️

- **Python Functions**: Implement basic math operations.
- **CI/CD Pipeline**: Automatically builds and tests the code upon every push or pull request.
- **Unit Tests**: Comprehensive unit testing using `pytest`.
- **Automation**: Efficient CI/CD workflows ensure smooth code integration.

## Project Structure 📁

- ├── src/ # Core Python functions │ └── math_operations.py # Basic math operations (addition, subtraction) ├── test/ # Unit test  
- folder │ └── test_operation.py # Unit tests for math operations ├── .github/ │ └── workflows/ │ └── python-app.yml # GitHub Actions - 
- workflow file for CI/CD ├── requirements.txt # Dependencies └── README.md # Project documentation


## Getting Started 🏁

### Prerequisites

- Python 3.11 or higher
- [Git](https://git-scm.com/) for version control
- [pytest](https://pytest.org/) for running the tests

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/RajatLalzare/ML-GitHubActions.git
    cd ML-GitHubActions
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the tests to ensure everything is set up correctly:
    ```bash
    pytest
    ```

## CI/CD Pipeline with GitHub Actions ⚙️

The CI/CD pipeline uses GitHub Actions to automatically build and test the code whenever changes are pushed or pull requests are opened against the `main` branch.

### Workflow Breakdown:
1. **Checkout Repository**: GitHub Actions pulls the repository to access the code.
2. **Set up Python Environment**: Python 3.11 is installed to run the project.
3. **Install Dependencies**: Dependencies from `requirements.txt` are installed using pip.
4. **Run Tests**: All unit tests are executed using `pytest`.

For more details, refer to the `.github/workflows/python-app.yml` file, which outlines the full CI/CD process.

### GitHub Actions Workflow Configuration

```yaml
name: Python CI

# Trigger the workflow on push to main branch or pull request
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest  # Use Ubuntu as the runner environment
    
    steps:
    # Check out the repository code
    - name: Checkout repository
      uses: actions/checkout@v2
    
    # Set up Python environment
    - name: Set up Python environment
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'

    # Install dependencies
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    # Run unit tests
    - name: Run tests
      run: pytest
