## Sportsranking Website from csv Upload


### To install requirements and setup: 
```
virtualenv myvenv
```
```
myvenv\Scripts\activate.bat
```
- clone the repository
- cd into the root directory (sportsranking)
```
 pip install -r requirements.txt
```
```
 python manage.py makemigrations
```
```
 python manage.py migrate
```

### useage:

 - cd into sportsranking directory:

```
 python .\manage.py runserver
```

 - open the browser on port 8000
 - add csv or modify displayed content using the ui buttons

