# Blueprint BLIH

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

### GET /repository

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

### POST /repository

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

### GET /repository/___repo___

Get repository informations

Parameters :
* __"login":"login_x"__
* __"password":"password"__

Response :
````json
{
    "uuid": "...",
    "url": "https://blih.epitech.eu/repository/Project",
    "creation_time": "123456789",
    "name": "Project",
    "public": "False",
    "description": "None"
}
````

### DELETE /repository/___repo___

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

### GET /repository/___repo___/acls

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

### GET /repository/____repo___/acls/___user___

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

### POST /repository/___repo___/acls/___user___

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

### GET /sshkey

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

### POST /sshkey

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

### DELETE /sshkey/___key___

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
