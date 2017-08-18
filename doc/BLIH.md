# Blueprint BLIH

Route : `https://api.epiteks.xyz/blih/`

## General

### GET /

Check if API is avaiable

Response :
````json
{
    "status":true/false
}
````

### GET /test

Check if credentials are rights

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
{
    "status":true/false
}
````

## Repository

### GET /repositories

Get repositories list

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
[
    "project",
    ...
]
````

### POST /repositories

Create new repository

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Body :
````json
{
    "name": "Project",
    "description": "OPTIONAL"
}
````

Response :
````json
{
    "message": "Repository Project created"
}
````

### GET /repositories/___repo___

Get repository informations

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
{
    "uuid": "...",
    "url": "https://blih.epitech.eu/repositories/Project",
    "creation_time": "123456789",
    "name": "Project",
    "public": "False",
    "description": "None"
}
````

### DELETE /repositories/___repo___

Delete repository

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
{
    "message": "Repository deleted"
}
````

### GET /repositories/___repo___/acls

Get repository ACLs

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
[
    {
        "login": "login_y",
        "read": true,
        "write": true,
        "admin": false
    },
    ...
]
````

### GET /repositories/____repo___/acls/___user___

Get repository ACLs for user

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
{
    "login": "login_y",
    "read": true,
    "write": true,
    "admin": false
}
````

### POST /repositories/___repo___/acls/___user___

Set repository ACLs for user

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Body :
````json
{
    "read": true/false,
    "write": true/false,
    "admin": true/false
}
````

Response :
````json
{
    "message": "ACL correctly applied"
}
````

## SSHKeys

### GET /sshkeys

Get sshkeys list

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
[
    {
        "name": "login_x",
        "key": "..."
    },
    ...
]
````

### POST /sshkeys

Add sshkey

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Body :
````json
{
    "key": "..."
}
````

Response :
````json
{
    "message": "sshkey uploaded"
}
````

### DELETE /sshkeys/___key___

Delete sshkey

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
{
    "message": "sshkey deleted"
}
````
