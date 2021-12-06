# Users

Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `/api/v1/users/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
email      | string | Yes      | The user's email address.
password   | string | Yes      | The password for the new user account.
first_name | string | No       | The user's given name.
last_name  | string | No       | The user's family name.

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "email": "mucahit@aktepe.com",
  "first_name": "Mucahit",
  "last_name": "Aktepe",
  "auth_token": "cd278601c9d60bb9b871722bbd669b408381911f"
}
```

The `auth_token` returned with this response should be stored by the client for authenticating future requests to the
API. See [Authentication](authentication.md).

## Get authenticated user's profile information

**Request**:

`GET` `/api/v1/users/me`

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "email": "mucahit@aktepe.com",
  "first_name": "Mucahit",
  "last_name": "Aktepe",
  "auth_token": "cd278601c9d60bb9b871722bbd669b408381911f"
}
```

## Update your profile information

**Request**:

`PUT/PATCH` `/api/v1/users/me`

Parameters:

Name       | Type   | Description
-----------|--------|---
first_name | string | The first_name of the user object.
last_name  | string | The last_name of the user object.

*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "email": "mucahit@aktepe.com",
  "first_name": "Mucahit",
  "last_name": "Aktepe",
  "auth_token": "cd278601c9d60bb9b871722bbd669b408381911f"
}
```


## List all users

**Request**:

`GET` `/api/v1/users/list`

*Note:*

- **[Authorization Protected](authentication.md)**
- **Requires Admin Privileges**

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "3944ecd0-b525-47ef-b050-5a7bcc04fe9d",
            "email": "asd@gmail.com",
            "first_name": "asd",
            "last_name": "asd",
            "auth_token": "a4d86d8c664766be93869bd88dff9c61a4abe361"
        },
        {
            "id": "63cff70b-5679-4969-80b7-6bee1666f7fd",
            "email": "uozy@ypst.com",
            "first_name": "Uğur",
            "last_name": "Özi",
            "auth_token": "12b19b9e4228d29505cb70d0a367334c8afcf838"
        },
        {
            "id": "dcb8c90c-58f8-4d79-833a-8d60b9ff919f",
            "email": "mucahitaktepe@gmail.com",
            "first_name": "",
            "last_name": "",
            "auth_token": "9206625ae77921cfb34e3815bedfa295cf8680ec"
        }
    ]
}
```


## Retrieve one user

**Request**:

`GET` `/api/v1/users/:id`

*Note:*

- The path param **"id"** is a UUID
- **[Authorization Protected](authentication.md)**
- **Requires Admin Privileges**

**Response**:

```json
Content-Type application/json
200 OK

{
    "id": "3944ecd0-b525-47ef-b050-5a7bcc04fe9d",
    "email": "asd@gmail.com",
    "first_name": "asd",
    "last_name": "asd",
    "auth_token": "a4d86d8c664766be93869bd88dff9c61a4abe361"
}
```