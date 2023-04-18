# TodoApp

This is the Simple Todo App project built on Python Django framework with the necessary features including Login/Signup and Managing Tasks.

-*Python Version: 3.11*<br>
-*Django Version: 4.2*<br>
-*Database: 10.3.38-MariaDB-log-cll-lve*<br>

**Link: <a href='http://todoapp.ammadbaig.com/' target="_blank">Live Demo</a>**

App can be tested using the provided credentials below, or users can create their own accounts to try it out.

**Test Credentials:**<br>
username: test@todoapp.com<br>
password: Testing


### Installation Guide:
- Use following command to get project repository in local machine: <br>
```git clone https://github.com/ammadmaddydev/todoapp.git ```

- Install Python and Django Framework in your project in order to run this app.<br>
**Python: https://www.python.org/downloads/** <br>
**Django: https://www.djangoproject.com/download/** <br>

- After setting up the above then create a new database and change credentials in ***settings.py*** file in ***todolist*** folder.<br>

- Run the following command after the above step: <br>
```python manage.py makemigrations ``` <br>
```python manage.py migrate ``` <br> 

- Create Super User for accessing the admin site: <br>
```python manage.py createsuperuser ``` <br>

- **All Done**, Just run the following command to get your app run: <br>
```python manage.py runserver ``` <br>

***Let's make some awesome code  <3 ;)***
