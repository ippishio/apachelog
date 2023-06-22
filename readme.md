# Apache log viewer
This script allows you to access your **Apache webserver** logs using **POST/GET** requests, saving it to **PostgreSQl** database. Repository includes [index.html](index.html) with simple control panel, that uses this API, and also [cron.py](cron.py) script, which allows user to run this code with **cron**
## Creating table in database

```console
foo@bar:~& sudo -i -u postgres
postgres@bar:~& psql -U username -d myDataBase -a -f path/to/table.sql
postgres@bar:~& exit
```

## Installing dependecies and running server

```console
foo@bar:~$ pip install pipenv
foo@bar:~$ pipenv install
foo@bar:~$ pipenv run python3 main.py
```

## Request format

- `updateLogs` - **POST** method. Returns `{"status" : "ok"}`. Used to update database with log files. 
- `getEntries`- **GET** method. Takes two arguments: `from` and `to`, which corresponds to start and end of timeframe. Returns array of **JSON**, each of them have `{"address" : "192.168.0.1", "date" : "2023-06-22-13-00-00}` structure. Date must be in `*YYYY-MM-DD-HH-mm-dd` format.
## Request example

```http
> POST http://127.0.0.1:5000/updateLogs
> {"status" : "ok"}

> GET http://127.0.0.1:5000/getEntries?from=2023-06-22-12-45-10&to=2023-06-24-15-34-00
> [{"address" : "192.168.0.1", "date" : "2023-06-22-13-00-00}, ...]

> GET http://127.0.0.1:5000/getEntries?from=all
> [{"address" : "192.168.0.1", "date" : "2023-06-22-13-00-00}, ...]
```

