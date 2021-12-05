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

Parameters:

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
}
```

## Update your profile information

**Request**:

`PUT/PATCH` `/users/:id`

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
}
```
