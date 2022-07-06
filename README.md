# auto_factory_project
## DESCRIPTION
API service for creating detail's cards and calculating full price of car

## ENDPOINTS


### DETAILS
 - #### GETTING LIST OF DETAILS

 `api/v1/posts/` `GET`

*Responses*

200, 404
- #### CREATING NEW CARD OF DETAIL

 `api/v1/details/` `POST`

*Request sample*
```json
{
    "id": 1,
    "type_name": "Hood",
    "price": 1000.0,
    "amount": 1
}
```
*Responses*

200, 400, 401

- #### GETTING, PATCHING, PUTTING, DELETING CARD OF DETAIL

 `api/v1/details/{detail_id}/` `GET` `PUT` `PATCH` `DELETE` (patching, putting, deleting)

*Responses*

200, 404 - for GET
200, 400, 401, 403, 404 - for PUT
200, 400, 401, 403, 404 - for PATCH
204, 401, 403, 404 - for DELETE
### COSTS

- #### GETTING COSTS

 `api/v1/costs/` `GET`

*Responses*

200
- #### CREATING NEW COST (CALCULATE PRICE)

 `api/v1/costs/` `POST`

*Request sample*
```json
{
    "margin": 30,
}
```
*Responses*

200, 400, 401

- #### GETTING CERTAIN COST

 `api/v1/costs/{cost_id}/` `GET`

*Responses*

200, 404


## TECHNOLOGY

- Python 3.8
- Django 2.2
- Django Rest Framework 3.12

## HOW TO START PROJECT
Clone repository and going:
```
git clone ...
cd auto_factory_project/
```
Create and activate virtual environment:
```
python -m venv venv
source venv/Script/activate
python -m pip install --upgrade pip
```
Install dependencies from file requirements.txt:
```
pip install -r requirements.txt
```
Make migrations:
```
python manage.py migrate
```
Run project:
```
python manage.py runserver
```
# AUTHORS
*Kozhevnikov Aleksei*
