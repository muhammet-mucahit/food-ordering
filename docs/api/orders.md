# Orders

Supports creating, listing and processing orders.

## Create a new order

**Request**:

`POST` `/api/v1/orders/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
restaurant      | int    | Yes      | The restaurant id which ordered from.
orderfood_set   | list   | Yes      | The foods which ordered from the restaurant.

orderfood_set:

Name       | Type | Required | Description
-----------|------|----------|------------
food      | int  | Yes      | The food id.
quantity   | int  | Yes      | The quantity of the food.

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
    "restaurant": 3,
    "orderfood_set": [
        {
            "food": 9,
            "quantity": 3
        }
    ]
}
```

## List orders

**Request**:

`GET` `/api/v1/orders/list` | `/api/v1/orders/list?status=ACCEPTED`

*Note:*

- This is a filterable endpoint through status
- Statuses: **_CREATED_**, **_WAITING_**, **_ACCEPTED_**, **_REJECTED_**, **_COMPLETED_**
- **[Authorization Protected](authentication.md)**
- **Requires Admin Privileges**

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 10,
            "created_date": "2021-12-06T15:51:12+0300",
            "modified_date": "2021-12-06T15:51:13+0300",
            "uuid": "ef6c38f0-b0e5-4be7-bf38-57104475b81d",
            "status": "ACCEPTED",
            "restaurant": 3,
            "user": "dcb8c90c-58f8-4d79-833a-8d60b9ff919f"
        }
    ]
}
```

## Process Orders

**Request**:

`POST` `/api/v1/orders/process`

*Note:*

- Processes the orders which is published through Pub/Sub Channel
- **[Authorization Protected](authentication.md)**
- **Requires Admin Privileges**

**Response**:

```json
Content-Type application/json
200 OK

{
    "message": "Orders processed successfully"
}
```