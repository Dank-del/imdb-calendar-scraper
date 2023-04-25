# IMDB Upcoming Scraper

> Scrapes upcoming movies based on their regions and exposes a flask REST API

## Made using

- BeautifulSoup
- Requests
- Flask

## Sample Response

- `/upcoming-movies?region=IN`

```json

  {
    "cast": [
      "Golshifteh Farahani",
      "Irrfan Khan",
      "Waheeda Rehman",
      "Shashank Arora"
    ],
    "genres": [
      "Drama",
      "Golshifteh Farahani",
      "Irrfan Khan",
      "Waheeda Rehman",
      "Shashank Arora"
    ],
    "title": "The Song of Scorpions (2017)"
  },
  {
    "cast": [
      "Vikram",
      "Karthi",
      "Jayam Ravi",
      "Aishwarya Rai Bachchan"
    ],
    "genres": [
      "Action",
      "Adventure",
      "Drama",
      "Vikram",
      "Karthi",
      "Jayam Ravi",
      "Aishwarya Rai Bachchan"
    ],
    "title": "Ponniyin Selvan: Part Two (2023)"
  }
  ...
]
```

- `/regions`

```json
[
  "AF",
  "AL",
  "AS",
  "AI",
  "AR",
  "AM",
  "AU",
  "AT",
  "BD",
  "BB",
  "BY",
  "BE",
  "BJ",
  "BM",
  "BR",
  "KH",
  "CM",
  "CA",
  "CF",
  "CL",
  "CN",
  "CC",
  "CO",
  "CR",
  "HR",
  "CU",
  "CW",
  ...
]
```

> Built by Sayan Biswas [<me@sayanbiswas.in>](mailto:me@sayanbiswas.in)
