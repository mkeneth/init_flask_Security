# Implementing Flask Security for Log in And Registration.

## Application requirements
To install the neccesarry requirements, refer to requirements.txt

```pip install -r requirements.txt ```

## Settings and configuration
There are two config files which are used to store private information necessary for the application. 

### .env
The file is used to store parameters that the app. From the ```example.env``` file there are example on the parameter to be set that are required base on the environment of the application. 

### instance/settings.py
With in root directory of the application create a folder ```instance``` containing the file ```settings.py```. 
Then copy the contents of ```example.settings.py``` and make the necessary changes in to suit the needs of your application. 

## Recommendation on Database.
Note that the database method used here is to create the database is for test purposes only kindly refer to the [``Flask-Migrate``](https://flask-migrate.readthedocs.io/en/latest/index.html ) module for a better implementation on the database Models. 

