from apiManagement import BodasApiManagement
import sys, getopt
import json

class Main:
  @staticmethod
  def collectData(argv):  
    # Get the mode and credential passed as parameter
    try:
        opts, args = getopt.getopt(argv, "c:")
    except getopt.GetoptError:
        print('-c <credentials>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-c']:
            credentialFile = open(arg, "r")
            credentials = json.load(credentialFile)

    clientID = credentials["clientID"]
    secret = credentials["secret"]
    scope = credentials["scope"]

    projectID = credentials["projectID"]
    fleetID = credentials["fleetID"]
    machineID = credentials["machineID"]

    token = BodasApiManagement.getToken(clientID, secret, scope)

    result = BodasApiManagement.getMachineSnaphot(token, projectID, fleetID, machineID)

    print(result)

    print(json.dumps(result.json(), indent=2))

if __name__ == "__main__":
    Main.collectData(sys.argv[1:])