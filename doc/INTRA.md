# Blueprint Intra

## Routes

### POST /login

Connection to the API

Parameters : None

Body :
````json
{
    "login": "login_x",
    "password": "UNIXPWD"
}
````

Response :
````json
{
    "token": "xxx"
}
````
or if there's an error :
````json
{
    "error": "xxx"
}
````

### GET /infos

Get informations from your intranet homepage

Parameters :
* __token : 42__

Response :
````json
{...}
````

### GET /planning

Get your planning

Parameters :
* __token : 42__
* start : YYYY-MM-DD (Default: Today)
* end : YYYY-MM-DD (Default: Today + 6 days)

Response :
````json
{...}
````

### GET /projects

Get all your projects

Parameters :
* __token : 42__
* start: YYYY-MM-DD (Default: Today)
* end: YYYY-MM-DD (Default: Today + 6 days)

Response :
````json
[
    {...}
]
````

### GET /project

Get project info

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__

Response :
````json
{...}
````

### POST /project

Suscribe to project

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__

Response :
````json
{...}
````

### DELETE /project

Unuscribe to project

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__

Response :
````json
{...}
````

### GET /project/files

Get project files

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__

Response :
````json
{...}
````


### GET /project/marks

Get project marks

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__

Response :
````json
{...}
````

### GET /allmodules

Get all modules

Parameters :
* __token : 42__
* __year : 2014__
* __location : [FR/PAR, FR/BDX, FR/LIL, FR/LYN, FR/MAR, FR/MPL, FR/NCY, FR/NAN, FR/NCE, FR/PAR, FR/REN, FR/STG, FR/TLS]__
* __course : [bachelor/classic, bachelor/tek1ed, bachelor/tek2ed]__

Response :
````json
{...}
````

### GET /modules

Get user modules

Parameters :
* __token : 42__
* login : login_x

Response :
````json
{...}
````

### GET /module

Get module infos

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__

Response :
````json
{...}
````

### POST /module

Subscribe to module

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__

Response :
````json
{...}
````

### DELETE /module

Unsubscribe to module

Parameters :
* __token : 42__
* __year : YYYY__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__

Response :
````json
{...}
````

### GET /event

Get event infos

Parameters :
* __token : 42__
* __year : 2014__
* __module : X-XXX-XXX__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__
* __event : event-XXXXXX__

Response :
````json
{...}
````

### POST /event

Subscribe to event

Parameters :
* __token : 42__
* __year : 2014__
* __module : X-XXX-XXX__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__
* __event : event-XXXXXX__

Response :
````json
{...}
````
* * *

### DELETE /event

Unsubscribe to event

Parameters :
* __token : 42__
* __year : 2014__
* __module : X-XXX-XXX__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__
* __event : event-XXXXXX__

Response :
````json
{...}
````

### GET /marks

Get marks

Parameters :
* __token : 42__

Response :
````json
{...}
````

### GET /messages

Get messages

Parameters :
* __token : 42__

Response :
````json
{...}
````

### GET /alerts

Get alerts

Parameters :
* __token : 42__

Response :
````json
{...}
````

### GET /photo

Get photo url

Parameters :
* __token : 42__
* __login : login_x__

Response :
````json
{...}
````

### POST /token

Validate token

* __token : 42__
* __year : 2014__
* __module : X-XXX-XXX-X__
* __instance : XXX-X-X__
* __acti : acti-XXXXXX__
* __event : event-XXXXXX__
* __tokenvalidationcode : XXXXXXXX__

Response :
````json
{...}
````

### GET /trombi

Get a list of students

Parameters :
* __token : 42__
* __year : 2014__
* __location : [FR/PAR, FR/BDX, FR/LIL, FR/LYN, FR/MAR, FR/MPL, FR/NCY, FR/NAN, FR/NCE, FR/PAR, FR/REN, FR/STG, FR/TLS]__
* course : [bachelor/classic, bachelor/tek1ed, bachelor/tek2ed]
* promo : tekX
* offset : 43

Response :
````json
{...}
````

## GET /user

Get a student's information

Parameters :
* __token : 42__
* __user : login_x__

Response :
````json
{...}
````

## GET /user/files

Get your documents

Parameters :
* __token : 42__
* __user : login_x__
* folder : folderName
* raw : [true, false]

Response
````json
{...}
````
