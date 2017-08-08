An addon will generate some JSON.


{
  "request": {
    "requesting-member": "person-who-requested-the-check",
    "group": {
      "members": [
        {"name": "Peppiwyn", "realm": "Grizzly Hills"},
        {"name": "Fuzzy", "realm": "Grizzly Hills"},
        {"name": "Shyne", "realm": "Grizzly Hills"}
      ]
    }
  }
}

JSON gets pasted into the window.

The group request is entered into the database for metrics. A request id is generated.

The request id then goes through the api_functions and looks for character information based on the members attribute.
