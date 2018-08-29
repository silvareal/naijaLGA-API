# naijaLGA-API
API for getting all states and Local Government Areas in Nigeria-🇳🇬
<hr>

# About
A simple API that shows the states and Local Government Areas in Nigera, and displays them in json format, nice right 👉, For developer who need a dropdown of States or Local government Areas in Nigeria(Not constrained to that use case only).

built with ❤️‍, Django, Django Rest Framework. More details on technology used below👇.

# Versioning
We hope to improve this API on every release version, and these changes won't always be backward compatible. V1 will be live at [{domain}/api/v1/](#) and is structured as described below👇.
<hr>

# States
To get the list of all states in Nigeria, Endpoint. [{domain}/api/v1/state/](#)
```json
{
  {
      "state": "Abia",
      "capital": "Umuahia",
      "lat": 22.92,
      "population": 2338487,
      "coord": {
        "lon": -1.9,
        "lat": 22.92,
      }
  },
  {
    "state": "Adamawa",
    "capital": "Yola",
    "population": 2102053,
    "coord": {
      "lon": 9.92,
      "lat": -12.9233,
    }
  },
  ...
}
```
States are identified using their names, which are unique and case sensitive(state begins with an uppercase `/Abia/`). For example, a state: [{domain}/api/v1/states/Abia/](#)
```json
{
    "state": "Abia",
    "capital": "Umuahia",
    "lon": 22.92,
    "lat": -1.9,
}
```

# States And Their LGA's
To get the list of all states and their LGA's in Nigeria, Endpoint. [{domain}/api/v1/stateslga/](#)
```json
{
  {
      "state": "Abia",
      "capital": "Umuahia",
      "lat": 22.92,
      "population": 2338487,
      "coord": {
        "lon": -1.9,
        "lat": 22.92,
      },
      "lga": [
        {
          "name": "Aba North",
          "population": 991011,
          "coord": {
            "lon": 9.000001,
            "lat": 1e-06
          }
        },
        {
          "name": "Aba South",
          "population": 991011,
          "coord": {
            "lon": 9.000001,
            "lat": 1e-06
          }
        },
        {
          "name": "Arochukwu",
          "population": 991011,
          "coord": {
            "lon": 9.000001,
            "lat": 1e-06
          }
        },
        {
          "name": "Bende",
          "population": 991011,
          "coord": {
            "lon": 9.000001,
            "lat": 1e-06
          }
        },
        ...
      ]
    }
  },
  {
    "state": "Adamawa",
    "capital": "Yola",
    "population": 2102053,
    "coord": {
      "lon": 9.92,
      "lat": -12.9233,
    }
  },
  ...
}
```
States are identified using their names, which are unique and case sensitive(state begins with an uppercase `/Abia/`). For example, a state: [{domain}/api/v1/stateslga/Abia/](#)
```json
{
    "state": "Abia",
    "capital": "Umuahia",
    "lon": 22.92,
    "lat": -1.9,
}
```


# List of endpoints
This is just a summary of all four endpoints you can call.

* `GET /states/` returns a list of all states in `Nigeria`.
* `GET /states/<state_name>/` returns a state. pass in the state name i.e `Abuja`.
* `GET /stateslga/` returns a list of all states and their LGA's in `Nigeria`.
* `GET /stateslga/<state_name>/` returns a state and it's LGA's. pass in the state name i.e `Abuja`.

# Using Django Rest Freamework(DRF)
Django REST framework is a powerful and flexible toolkit for building Web APIs 👉 [more details](http://www.django-rest-framework.org/).
<hr>

# Contributions
Contributions are always welcome! Please read the [Contribution guidelines for this project](docs/CONTRIBUTING.md).
