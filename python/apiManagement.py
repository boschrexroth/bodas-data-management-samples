from datetime import datetime
import os
import requests
import json
import pytz
from http import HTTPStatus
from requests import HTTPError

class BodasApiManagement:

    @staticmethod
    def getToken(clientID, secret, scope):

        print("Request acces token for your data portal!")

        url = "https://access.bosch-iot-suite.com/token"

        payload='grant_type=client_credentials&client_id=' + clientID + '&client_secret=' + secret + '&scope=' + scope
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        tokenJson = response.json()
        
        access_token = tokenJson['access_token']

        return access_token

    @staticmethod
    def getMachineSnaphot(token, projectID, fleetID, machineID):

        #url = "https://bosch-iot-insights.com/r/ppz0761/ppz0761:group_qmatec1114ts/Fleet/Equipment/510TS_15079/VEP1__BattVolt/2022-12-20T00:00:00/2022-12-21T15:00:00/1"

        print("Pull data!")

        url = "https://bosch-iot-insights.com/r/" + projectID + "/bodas/" + fleetID + "/Fleet/Equipment/" + machineID

        print(url)

        payload={}
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + token,
            'Accept-Encoding': 'gzip, deflate, br'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response
