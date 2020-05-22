cd matplotlib

python -m pip install --upgrade pip --user

python -m pip install -r requirements.txt


export FLASK_APP=microservice.py

python -m flask run