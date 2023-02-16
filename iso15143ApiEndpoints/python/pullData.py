from apiManagement import BodasApiManagement
import sys
import json
import pylab as plt
from datetime import datetime

class Main:
  @staticmethod
  def collectData(argv):
    
    clientID = ""
    secret = ""
    scope = ""
    projectID = ""
    fleetID = ""
    machineID = ""

    token = BodasApiManagement.getToken(clientID, secret, scope)

    print("##")
    pageNumber = 2
    result = BodasApiManagement.getFleetSnaphot(token, projectID, fleetID, pageNumber)
    print(json.dumps(result.json(), indent=2))

    print("")
    print("##")
    result = BodasApiManagement.getMachineSnaphot(token, projectID, fleetID, machineID)
    print(json.dumps(result.json(), indent=2))

    print("")
    print("##")
    dataElement = "CumulativeOperatingHours"
    valueField = "Hour"
    startDateTime = "2023-02-09T00:00:00Z"
    endDateTime = "2023-02-14T00:00:00Z"
    pageNumber = 1
    result = BodasApiManagement.getTimeSeries(token, projectID, fleetID, machineID, dataElement, startDateTime, endDateTime, pageNumber)
    timeSeriesData = result.json()
    print(json.dumps(timeSeriesData, indent=2))

    if len(timeSeriesData) > 0:
        
        timeSeriesDataElement = timeSeriesData[0]
        
        if dataElement in timeSeriesDataElement and len(timeSeriesDataElement[dataElement]) > 0:

            dateTimeArray = []
            valueArray = []
        
            for data in timeSeriesDataElement[dataElement]:
                
                dateTimeArray.append(datetime.strptime(data["datetime"], '%Y-%m-%dT%H:%M:%SZ'))
                valueArray.append(data[valueField])

            fig, ax = plt.subplots()
            ax.plot(dateTimeArray, valueArray, color = 'b')
            plt.show()

if __name__ == "__main__":
    Main.collectData(sys.argv[1:])
