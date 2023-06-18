### Contacts

- Create a contact

    ```py
  DATA={
    "name":"Gaurav Kumar",
    "email":"gaurav.kumar@example.com",
    "contact":"9123456789",
    "type":"employee",
    "reference_id":"Acme Contact ID 12345",
    "notes":{
            "notes_key_1":"Tea, Earl Grey, Hot",
            "notes_key_2":"Tea, Earl Grey… decaf."
        }
    }
  client.contact.create(data=DATA)
    ```

- Fetch a particular contact by id

    ```py
    client.contact.fetch(contact_id = "<CONTACT_ID>")
    ```

- Fetch all contacts

    ```py
    client.contact.fetch_all()
    ```

- Update contact details

    ```py
  DATA={
    "name": "Gaurav Kumar",
    "email": "gaurav.kumar@example.com",
    "contact": "9123456789",
    "type": "self",
    "reference_id": "Acme Contact ID 12345",
    "notes": {
            "notes_key_1":"Tea, Earl Grey, Hot",
            "notes_key_2":"Tea, Earl Grey… decaf."
        }
    }
  client.contact.update(contact_id = "<CONTACT_ID>", data=DATA)
    ```

- Activate or Deactivate a contact

    ```py
  DATA={
    "active": false
  }
    client.contact.status(contact_id = "<CONTACT_ID>", data=DATA)
    ```
