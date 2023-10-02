# adypu_erp
A Functional and Superb ERP for ADYPU

Steps to set up Backend:

1 -> Start a POWERSHELL (preferably in VS CODE) in the Root Dir (Directory containing this readme file).<br>
2 -> Type ./activate_env<br>
3 -> Navigate to backend using 'cd backend'.<br>
4 -> Ensure Python is installed. Do 'pip install pipenv'<br>
5 -> Do 'pipenv install'<br>
6 -> The above file will install or repair any necessary files included within the Pipfile.<br>
7 -> Navigate to adypu_erp<br>
8 -> Do 'python manage.py makemigrations' . Followed by 'python manage.py migrate'<br>

To run server:

python manage.py runserver [PORT NUMBER (default = 8000)]

Log Book
====================================================
## [1][2] - Setting Up

Includes the initial ERP Database Structure in MYSQL, Initial Setup of The Django Server. Update to the README file. Inclusion of Log Book. Inclusion of activate_env.ps1.

## [3][4][5][6][7][8] - Student App

Initialised Student App. Updated student_data table structure. Updated Models. Completed SQL Migration to MySQL DB. Registered Model in Django Admin.