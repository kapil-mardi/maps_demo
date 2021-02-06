# Sample application for the dependant dropdowns

## Setup
    - clone this repository to your local machine
    - create virtual environment in the root directory of the application
    - make sure that the name of the environment forlder is venv
     ```
        python3 -m -venv venv
     ```
    - Before any library installation make sure to activate the environment 
        - For windows 
            - Go to /venv/Scripts/
            - execute activate bash file
        - For linux
            - Go to /venv/bin
            - execute ./activate shell file
    - Install the 3rd party dependacies 
    ```
        pip install -r requirement.txt
    ```

## Run
    - Application already has the database file with it
    - It has been populated with sample data for Maharashtra -> Urban -> Kolhapur
    - After activating the environment execute
    ```
        python manage.py runserver
    ```
    - Visit http://localhost:8080/maps/
