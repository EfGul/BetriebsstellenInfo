# BetriebsstellenInfo
## Description
The BetriebsstellenInfo application provides an endpoint that delivers information about operating stations. The user has to enter the RL-100 code when calling up the endpoint and then receives information about the operating station as output.
## How to run project
To run the project correctly, a web server like uvicorn is also required. First you have to start with installing the necessary packages. This can be done via
```
pip install -r requirements.txt
```
If all necessary packages are installed correctly the API can be started with the following command
```
uvicorn main:app --host 127.0.0.1 --port 8000
```

The app will then run on port 80 at host 127.0.0.1 and can be called from there.
## How to use
In order to use the application correctly, it is necessary to enter the RL-100 Code of the operating station into the betriebsstelle endpoint. The endpoint must be called in the following format to function properly
```
GET betriebsstelle/RL-100_CODE
```
As a result, you will then receive information about the operating station. This information includes the name, the short name and the type of the operating station. The output has the following form
``` json
{
   "Name": "Hamburg Anckelmannsplatz",
   "Kurzname": "Anckelmannsplatz",
   "Typ": "Üst",
}
