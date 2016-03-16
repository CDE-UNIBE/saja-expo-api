Logging
=======

* Use Opbeat, as port for mail should not be open on the machine at the expo.
* File logs as fallback (50 MB max).


Infrastructure
==============

* Accept only requests from internal network.
* Allow only port 80 for outgoing traffic.
  * Required to call external API.
  * And maybe: opbeat.
* Block all incoming traffic, except for local network.


Endpoint documentation
======================


Register
--------
Register the connection between a nfc id, backpack id and language. Backpack ids
are unique.


* Example request:
* URL:

  http://saja-expo-api.local/api/v1/register/

* Request header:

  Content-Type: application/json
  Authentication: Token <token>

* Request body:

  {
      "nfc_id": "<foo>",
      "backpack_id": "<bar>",
      "language_id": "1",
  }


Log
---

Register an interest from a nfc id on an exhibition stand. Only registered nfc
ids are allowed.

* Example request:
* URL:

  http://saja-expo-api.local/api/v1/log/

* Request header:

  Content-Type: application/json
  Authentication: Token <token>

* Request body:

  {
      "nfc_id": "<foo>",
      "content_type": "<bar>",
      "perma_id": "1"
  }
