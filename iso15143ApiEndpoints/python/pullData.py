from apiManagement import BodasApiManagement
import sys
import json
from datetime import datetime
#used for displaying the timeseries data 
#import pylab as plt

class Main:
  @staticmethod
  def collectData(argv):
    # client OAuth2 credentials 
    clientID = ""
    secret = ""
    scope = ""
    projectID = ""
    fleetID = ""
    identifier = ""

    token = BodasApiManagement.getToken(clientID, secret, scope)

    print("##")
    pageNumber = 1
    result = BodasApiManagement.getFleetSnaphot(token, projectID, fleetID, pageNumber)
    print(json.dumps(result.json(), indent=2))

    print("")
    print("##")
    result = BodasApiManagement.getMachineSnaphot(token, projectID, fleetID, identifier)
    print(json.dumps(result.json(), indent=2))

    print("")
    print("##")
    dataElement = "CumulativeOperatingHours"
    valueField = "Hour"
    #include here the
    startDateUTC = "2022-09-23T00:00:00"
    endDateUTC = "2022-09-23T23:00:00"
    pageNumber = 1
    result = BodasApiManagement.getTimeSeries(token, projectID, fleetID, identifier, dataElement, startDateUTC, endDateUTC, pageNumber)
    timeSeriesData = result.json()
    print(json.dumps(timeSeriesData, indent=2))

    if len(timeSeriesData) > 0:
        
        timeSeriesDataElement = timeSeriesData[0]
        
        if dataElement in timeSeriesDataElement and len(timeSeriesDataElement[dataElement]) > 0:

            dateTimeArray = []
            valueArray = []
        
            for data in timeSeriesDataElement[dataElement]:
                
                dateTimeArray.append(datetime.strptime(data["datetime"], '%Y-%m-%dT%H:%M:%S'))
                valueArray.append(data[valueField])

            # use to display data
            """ fig, ax = plt.subplots()
            ax.plot(dateTimeArray, valueArray, color = 'b')
            plt.show() """

if __name__ == "__main__":
    Main.collectData(sys.argv[1:])
