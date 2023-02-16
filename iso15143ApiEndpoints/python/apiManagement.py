import requests

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
    def getFleetSnaphot(token, projectID, fleetID, pageNumber):

        print("Pull fleet snapshot (page: " + str(pageNumber) + ") data for " + fleetID + " !")

        url = "https://bosch-iot-insights.com/r/" + projectID + "/bodas/" + fleetID + "/Fleet/" + str(pageNumber)

        print(url)

        payload={}
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + token,
            'Accept-Encoding': 'identity'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response)

        return response

    @staticmethod
    def getMachineSnaphot(token, projectID, fleetID, machineID):

        print("Pull data machine snapshot of " + machineID + " !")

        url = "https://bosch-iot-insights.com/r/" + projectID + "/bodas/" + fleetID + "/Fleet/Equipment/" + machineID

        print(url)

        payload={}
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + token,
            'Accept-Encoding': 'identity'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response)

        return response

    @staticmethod
    def getTimeSeries(token, projectID, fleetID, machineID, dataElement, startDateTime, endDateTime, pageNumber):

        print("Pull data!")
        
        url = "https://bosch-iot-insights.com/r/" + projectID + "/bodas/" + fleetID + "/Fleet/Equipment/" + machineID + "/" + dataElement + "/" + startDateTime + "/" + endDateTime + "/" + str(pageNumber)

        print(url)

        payload={}
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + token,
            'Accept-Encoding': 'identity'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response
