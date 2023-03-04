## Company Assets Tracker
A Django app to track corporate assets such as phones tablets, laptops 
and other gears handed out to employees.

## Feature
1. The application can be used by several companies
2. Each company can add all or some of its employees
3. Each company and its staff might delegate one or more devices to employees for
a certain period of time
4. Each company should be able to see when a Device was checked out and returned
5. Each device should have a log of what condition it was handed out and returned





## Exploring Endpoints Locally

Run below codes in the terminal or use any api client such as postman.

## Endpoints

The endpoints, expected payloads, and responses are described below.


## A new user sign up 

### Request

`POST api/v1/user/register/`
    
    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/user/register/
    or
    postman:  http://127.0.0.1:8000/api/v1/user/register/

### Payload

    {
        "username": <String>,
        "email":  <String>,
        "first_name": <String>,
        "last_name": <String>,
        "password": <String>,      
    }

### Server Response

    {
        "token": <String>,
    }
    
       


## Login User

### Request

`POST api/v1/user/login/`

    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/user/login/

    postman:  http://127.0.0.1:8000/api/v1/user/login/


### Payload

    {
        "email": <String>,
        "password": <String>,   
    }

### Server Response

    {
        "success": <String>,
        "token": <String>,
    }




## Create/View Companies

    Authenticated(Admin) or Read only

### Request

`POST /api/v1/companies/`
`GET /api/v1/companies/`

    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/companies/

    postman:  http://127.0.0.1:8000/api/v1/companies/


### Auth Header
    
    "token": <String>, 


### Payload
    {
        "company_name": "Amazon"
            
    }


### Server Response

    {
        "id": <Number>,
        "company name": <String>,
    }




## Update Company
    Authenticated(Admin)

### Request

`POST v1/company/update/<param:id>`


    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/company/update/1

    postman:   http://127.0.0.1:8000/api/v1/company/update/1

    
### Auth Header

        "token": <String>, 





## Create/View  All Asset Categores

    Authenticated(Admin) or Read only

### Request

`POST api/v1/category/`
`GET api/v1/category/`

    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/category/

    postman:  http://127.0.0.1:8000/api/v1/category/


### Auth Header
    
    "token": <String>, 


### Payload

    {   
        "category-name": <String>,
        "description": <String>
    }


### Server Response

    {
        "id": <Number>,
        "category-name": <String>,
        "description": <String>
    }




## Create Assets

    Authenticated(Admin)

### Request

`POST api/v1/asset/company/<param:company-name>/`


    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/asset/company/Amazon/

    postman:   http://127.0.0.1:8000/api/v1/asset/company/Amazon/


### Auth Header

        "token": <String>, 
 
### Payload

    {
        "name": <String>,
        "company-id":  <Number>,
    }

### Response

    {
    "id": <Number>,
    "category": <String>,
    "name": <String>,
    "availability": Boolean,
    "description": <String>,
    "date_created": <String>,
    "company": <Number>
    }




## Update Asset

    Authenticated(Admin)

### Request

`POST /api/v1/asset/update/<param:id>`


    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/asset/update/3

    postman:   http://127.0.0.1:8000/api/v1/asset/update/3

    
### Auth Header

        "token": <String>, 



## Delete Asset

    Authenticated(Admin)

### Request

`POST /api/v1/asset/delete/<param:id>`


    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/asset/delete/3

    postman:   http://127.0.0.1:8000/api/v1/asset/delete/3

    
### Auth Header

        "token": <String>,





## Create AssetLog/Request Assets

    Authenticated(Admin)

### Request

`POST api/v1/assetlog/<param:asset-id>/`


    curl -i -H 'Accept: application/json'  http://127.0.0.1:8000/api/v1/assetlog/1/

    postman:   http://127.0.0.1:8000/api/v1/assetlog/1/


### Auth Header

        "token": <String>, 
 
### Payload

    {
        "collected_by": <String>, 
        "condition": <String>, 
        "check_out": <String>, 
        "return_date": <String>, 
        "asset":  <Number>
    }

### Response

   {
        "id":  <Number>,
        "collected_by": <String>, 
        "condition": <String>, 
        "check_out": <String>, 
        "return_date": <String>, 
        "asset": <Number>
    }






## View All Asset Logs

### Request

`GET api/v1/assetlog/all/`

    curl -i -H 'Accept: application/json'   http://127.0.0.1:8000/api/v1/assetlog/all/

    postman:  http://127.0.0.1:8000/api/v1/assetlog/all/


### Server Response

    {
        "id":  <Number>,
        "collected_by": <String>, 
        "condition": <String>, 
        "check_out": <String>, 
        "return_date": <String>, 
        "asset": <Number>
    }




## Extra

    pytest --tb=no