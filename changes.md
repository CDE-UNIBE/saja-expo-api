# Changes

Only changes relevant to the functionality / architecutre are documented.

## 2016-05-24
* Additional validation to ensure the whole message was scanned in properly at the station.
* New migrations from scratch: db reset is required (as discussed).

## 2016-05-14: Decision by pm: urls can be stored to a nfc chip
* Removed endpoint for 'register'
* Stations can deliver URLs instead of ids
* Parse 'rucksack_id' from URL and pass only the id to the myswissalps API

