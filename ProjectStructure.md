# Project Structure

## Project Components
The project runs on Django 3.1.7 .

The project makes use of 5 additional components which are called Apps. They are as follows:

1. acounts
2. department
3. product
4. riskassessment
5. vendor

Each App has the following the files in it:

1. admin.py - Registers the App in Django Administration.
2. models.py - Contains attributes to represent the Database structure.
4. views.py - Contains the the Business Logic and maps Views to Templates.
5. urls.py - Contains the mapping of URLs and Views.
---

## Templates

Templates are located in `templates` in the following folders:

1. `accounts` - Includes all Dashboard-related templates.
2. `riskassessment` - Includes all Risk Assessment Questionnaire and Report Templates.
3. Project Root - Includes password reset templates.
--- 
