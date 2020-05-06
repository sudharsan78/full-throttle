# full-throttle API listing test project

### To run this project
#### Clone the repository
```
git clone https://github.com/sudharsan78/full-throttle.git
```
#### Create and activate virtualenv
```
cd full-throttle
python -m venv test_venv

# activate in windows
test_venv/Script/activate
# activate in linux
source test_venv\bin\activate
```

#### Install the required packages
```
pip install -r requirments.txt
```
#### Run application
```
cd full_throttle
python manage.py migrate

# Load sample datas (optional)
python manage.py load_user_activity_data "file_path"

python manage.py runserver
```

#### Endpoint to get the list of user activity 
```
http://vssudharsan.pythonanywhere.com/user-activity/list/
```


