# Evexia

You need to have pip installed

## Install pip

```bat
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

```bat
python get-pip.py
```
## Use requirements.txt

```bat
pip3 install -r requirements.txt
```

if that doesn't work then:

```bat
python3 -m pip install -r requirements.txt
```
## Running the project

```bat
set FLASK_APP=app.py
```

```bat
python3 -m flask run
```