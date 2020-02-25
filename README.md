# ONLINE SHOP API WITH DJANGO REST FRAMEWORK
Built with [Django REST framework](http://www.django-rest-framework.org/)

## Requirements
- Python 3.6
- Django (2.2)
- Django REST Framework
- Django Rest Auth

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
```
### Clone this repo and run commands:
 - *python manage.py migrate* to create the database
 - *python manage.py createsuperuser* to create a superuser
 - *python manage.py runserver* to start django's python lightweight development server 
 - visit ``http://127.0.0.1:8000/smartadmin`` and login to the admin site with credentials used when creating a super user
 - add Products to the database
 
 ``username: admin``
 
 ``password: superadmin``
 
 
## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `api`

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/products` | GET | READ | Get all products
`ai/products/:id` | GET | READ |  Get a single product
`ai/products/:id` | PATCH | UPDATE | Updates a single product
`api/products/create`| POST | CREATE| Create new product  

## Use
We can test the API using Postman

First, we have to start up Django's development server.
```
	python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
	http  http://127.0.0.1:8000/api/products/
```
we get:
```
 {  "detail":  "You must be authenticated"  }
```
Instead, if we try to access with credentials:
```
	http http://127.0.0.1:8000/api/products/ "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```
we get all the available products
```
[
    {
        "id": 1,
        "image": "http://localhost:8000/api/products/products/image/product07.png",
        "name": "samsung j7",
        "price": 12000.0,
        "discounted_price": 10000.0,
        "description": "smart phone",
        "stock_level": 56,
        "created_date": "2019-11-22T15:36:17.731069Z",
        "updated_date": "2019-11-22T15:36:17.731069Z",
        "category": 1
    },
    {
        "id": 2,
        "image": "http://localhost:8000/api/products/products/image/product04.png",
        "name": "smart tv",
        "price": 20000.0,
        "discounted_price": 18000.0,
        "description": "smart tv",
        "stock_level": 200,
        "created_date": "2019-11-22T16:09:26.257681Z",
        "updated_date": "2019-11-22T16:09:26.258179Z",
        "category": 2
    },
]
```

## Login and Tokens

To get a token first we have to login
```
	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="root1234"
```
after that, we get the token
```
{
    "key": "2d500db1e51153318e300860064e52c061e72016"
}
```
**ALL request must be authenticated with a valid token, otherwise they will be invalid**

We can create new users. (password1 and password2 must be equal)
```
http POST http://127.0.0.1:8000/auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
And we can logout, the token must be your actual token
```
http POST http://127.0.0.1:8000/auth/logout/ "Authorization: Token <YOUR_TOKEN>" 
```

The API has some restrictions:
-   Only authenticated users may create and see products.
-   Unauthenticated requests shouldn't have access.

For api documentation go to:<br/>
``http://127.0.0.1:8000/docs``

For the homepage go to:<br/>
``http://127.0.0.1:8000``