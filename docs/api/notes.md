Logging
-------

* Use Opbeat, as port for mail should not be open on the machine at the expo.
* File logs as fallback (50 MB max).


Infrastructure
--------------

* Accept only requests from internal network.
* Allow only port 80 for outgoing traffic.
  * Required to call external API.
  * And maybe: opbeat.
* Block all incoming traffic, except for local network.


Documentation
-------------

* Example request:
* URL:

  http://saja-expo-api.local/api/v1/logs/

* Request header:

  Content-Type: application/json
  Authentication: Token <token>

* Request body:

  {
      "nfc_id": "<foo>",
      "tag_id": "<bar>",
  }
