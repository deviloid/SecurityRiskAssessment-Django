# Sentinel Security Risk Assessment Application

## About
A software security risk assessment tool developed as part of ASU Information Technology IFT 593 Applied Project for ASU University Technology Office under the guidance of and direct collaboration with Dr. Tatiana Walsh.

---
## Technology Stack
![Python v3.8](https://img.shields.io/badge/Python-v3.8-blue?style=flat-square&logo=python&logoColor=white)
![Django v3.1.7](https://img.shields.io/badge/Django-v3.1.7-blue?style=flat-square&logo=django)
![HTML 5](https://img.shields.io/badge/HTML-5-blue?style=flat-square)
![Bootstrap 5.0](https://img.shields.io/badge/Bootstrap-v5.0-blue?style=flat-square&logo=bootstrap&logoColor=white)

---
## Features
- Role-based views and functions.
- Django custom decorators, custom User Model Class including custom reateUser and Superuser functions.
- Adding following entities:
  - Users
  - Vendors
  - Products
  - Departments
  - Risk Assessments
- Detail pages for all entites. 
- Password Reset Functionality.
- Risk Assessment features:
  - Binds Users, Vendor, Product and Department to Risk Assessment.
  - Tracking completed steps.
  - Generating Risk Assessment scores automatically.
  - Adding comments to Risk Assessment sections.
  - Risk Assessment re-evaluations.
  - Risk Assessment approval (manager role required).
  - Generating Risk Assessment report.
- Developed using Python, Django Framework, HTML5, Bootstrap 5, JavaScript.

---
## Stats
![Lines of code](https://img.shields.io/tokei/lines/github/deviloid/SecurityRiskAssessment-Django?label=Total%20Lines%20of%20Code&style=flat-square)
![GitHub commits since tagged version](https://img.shields.io/github/commits-since/deviloid/SecurityRiskAssessment-Django/6ddbd29?label=%23%20of%20Commits%20made%20since%20initial&style=flat-square)

---
## Running the Project

1. Install Python 3.8
   
2. Make project directory
    ```
    mkdir Sentinel
    ```
3. Go to repository folder.
    ```
    cd Sentinel
    ```
4. Create virtual environment
    ```
    virtualenv -p python .
    ```
5. Activating virtualenv

    - For Windows:
        ```cmd
        .\Scripts\activate
        ```
    - For linux/Mac:
        ```bash
        $ source /bin/activate
        ```
6. Make source-file directory
    ```
    mkdir src
    cd src
    ```
7. Download Source code:
    ```
    git clone GITHUB-REPO-URL
    ```
8. Install required Python packages
    ```pip
    pip install -r requirements.txt
    ```
9.  Make necessary database migrations.
    
    *Note: This project uses SQLite database for development.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
10. Run the application
    ```
    python manage.py runserver
    ```
