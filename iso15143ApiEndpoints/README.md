# API endpoints

These endpoints allow you to pull data from your Bodas Connec Data Portal.

## Extended ISO 15143

The [ISO Standard 15143-3](#https://www.iso.org/standard/67556.html) 
The standard describes how to send status data from a telematics provider's server to third-party client applications over the Internet. 

The OEM ISO Number (machine VIN = Vehicle Identification Number or PIN = Personal Identification Number) is used as identifier for pulling data.

## Authentication
For information (see the list below) about using the [REST API Endpoints](#endpoints), please contact your instance owner.
Following information are needed:

- Client ID: OAuth2 client ID of your fleet,
- Client secret: OAuth2 secret of your fleet,
- Scope: OAuth2 scope of your fleet,
- projectID: Bodas Connect project ID,
- fleetId: Your fleet ID 

## Endpoints
There are two classifications of endpoints: snapshot (fleet or single piece of equipment) and timeseries.

Base URL: https://bosch-iot-insights.com/r/{projectId}/bodas/

- Fleet snapshot [{fleetId}/Fleet/{pageNumber}](#get-{fleetId}Fleet{pageNumber}) <br/>
- Machine (Single-element) snapshot [{fleetId}/Fleet/Equipment/{machineID}](#get-{fleetId}FleetEquipment{identifier}) <br/>
- Timeseries data [{fleetId}/Fleet/Equipment/{machineID}/{dataElement}/{startDateUTC}/{endDateUTC}/{pageNumber}](#get-{fleetId}FleetEquipment{identifier}{dataElement}{startDateUTC}{endDateUTC}{pageNumber}) <br/>

___

### GET {fleetId}/Fleet/{pageNumber}

Get a snaphots of all machines in the fleet.

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `pageNumber` | required | int  | Page number to be returned. <br/> MUSS be a positive non zero integer. <br/>This endpoint is paginated with 100 records per page. |

**Response Sample**
In this example, the fleet has 2 machines.
```
//Get the first page
[
  {
  "Equipment": [
    {
      "Location": {
        "datetime": "2022-09-23T17:17:39.666Z",
        "Latitude": 48.479507,
        "Longitude": 8.929208,
        "Altitude": 424,
        "AltitudeUnits": "meter"
      },
      "FuelUsed": {
        "datetime": "2022-09-23T17:17:38.342Z",
        "FuelConsumed": 730,
        "FuelUnits": "liter"
      },
      "CumulativeOperatingHours": {
        "datetime": "2022-09-23T17:17:38.343Z",
        "Hour": 162
      },
      "EquipmentHeader": {
        "UnitInstallDateTime": "2023-05-08T10:00:00.000Z",
        "OEMName": "Rexroth",
        "Model": "sweeperx200",
        "EquipmentID": "sn50123",
        "PIN": "SNP50123123456789"
      }
    },
    {
      "Location": {
        "datetime": "2022-09-23T17:17:39.666Z",
        "Latitude": 48.479507,
        "Longitude": 8.929208,
        "Altitude": 424,
        "AltitudeUnits": "meter"
      },
      "CumulativeOperatingHours": {
        "datetime": "2022-09-23T17:17:38.343Z",
        "Hour": 162
      },
      "FuelUsed": {
        "datetime": "2022-09-23T17:17:38.342Z",
        "FuelConsumed": 730,
        "FuelUnits": "liter"
      },
      "EquipmentHeader": {
        "UnitInstallDateTime": "2023-05-08T10:00:00.000Z",
        "OEMName": "Rexroth",
        "Model": "sweeperx200",
        "EquipmentID": "sn50456",
        "PIN": "SNV50456123456789"
      }
    }
  ],
  "links": [
    {
      "rel": "self",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/1"
    },
    {
      "rel": "next",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/1"
    },
    {
      "rel": "prev",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/1"
    },
    {
      "rel": "last",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/1"
    }
  ]
}
]

or

// Trying to get the second page (which is empty)
[
  {
  "Equipment": [],
  "links": [
    {
      "rel": "self",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/2"
    },
    {
      "rel": "next",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/1"
    },
    {
      "rel": "prev",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/1"
    },
    {
      "rel": "last",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/1"
    }
  ]
}
]

```
___

### GET {fleetId}/Fleet/Equipment/{identifier}

Get snapshot of all data elements of a machine. This endpoint provides a snapshot view of a single element. This endpoint is paginated with a default of 100 records per page. 

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `identifier` | required | string  |  OEM ISO Number (PIN or VIN). The identifiers are returned as a result pulling fleet snapshot data. |

**Response Sample**

```
[
 {
  "FuelUsed": {
    "datetime": "2022-09-23T17:17:38.342Z",
    "FuelConsumed": 730,
    "FuelUnits": "liter"
  },
  "Location": {
    "datetime": "2022-09-23T17:17:39.666Z",
    "Latitude": 48.479507,
    "Longitude": 8.929208,
    "Altitude": 424,
    "AltitudeUnits": "meter"
  },
  "CumulativeOperatingHours": {
    "datetime": "2022-09-23T17:17:38.343Z",
    "Hour": 162
  },
  "EquipmentHeader": {
    "UnitInstallDateTime": "2023-05-08T10:00:00.000Z",
    "OEMName": "Rexroth",
    "Model": "sweeperx200",
    "EquipmentID": "sn50123",
    "PIN": "SNP50123123456789"
  }
}   
]

```

___

### GET {fleetId}/Fleet/Equipment/{identifier}/{dataElement}/{startDateUTC}/{endDateUTC}/{pageNumber}

Get a view into telematics data for a single construction machine over the specified time.

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `identifier` | required | string  | OEM ISO Number (PIN or VIN). The identifiers are returned as a result pulling fleet snapshot data. |
|     `dataElement` | required | string  | Data element to be returned (Locations, CumulativeOperatingHours, etc.). |
|     `startDateUTC` | required | string  | Start date and time of the timeseries. <br/>All date and time stamps in an XML document shall be formatted as ISO 8601 (all parts) “date and time” that includes the year, month, day, hour, minutes, and seconds. It does not include fractional seconds.<br/>Date and Time are expressed as: YYYY-MM-DDThh:mm:ssZ. |
|     `endDateUTC` | required | string  | End date and time of the timeseries. <br/>All date and time stamps in an XML document shall be formatted as ISO 8601 (all parts) “date and time” that includes the year, month, day, hour, minutes, and seconds. It does not include fractional seconds.<br/>Date and Time are expressed as: YYYY-MM-DDThh:mm:ssZ. |
|     `pageNumber` | required | int  | Page number to be returned. <br/> MUSS be a positive non zero integer. <br/>This endpoint is paginated with 100 records per page. |

**Response Sample**

```
[
  {
  "CumulativeOperatingHours": [
    {
      "Hour": 3,
      "datetime": "2022-09-23T17:15:39"
    },
    {
      "Hour": 13,
      "datetime": "2022-09-23T17:15:40"
    },
    {
      "Hour": 23,
      "datetime": "2022-09-23T17:15:41"
    },
    {
      "Hour": 33,
      "datetime": "2022-09-23T17:15:42"
    },
    {
      "Hour": 43,
      "datetime": "2022-09-23T17:15:43"
    },
    {
      "Hour": 53,
      "datetime": "2022-09-23T17:15:44"
    },
    {
      "Hour": 63,
      "datetime": "2022-09-23T17:15:45"
    },
    {
      "Hour": 73,
      "datetime": "2022-09-23T17:15:46"
    },
    {
      "Hour": 83,
      "datetime": "2022-09-23T17:15:47"
    },
    {
      "Hour": 93,
      "datetime": "2022-09-23T17:15:48"
    },
    {
      "Hour": 103,
      "datetime": "2022-09-23T17:15:49"
    },
    {
      "Hour": 113,
      "datetime": "2022-09-23T17:15:50"
    },
    {
      "Hour": 123,
      "datetime": "2022-09-23T17:15:51"
    },
    {
      "Hour": 133,
      "datetime": "2022-09-23T17:15:52"
    },
    {
      "Hour": 143,
      "datetime": "2022-09-23T17:15:53"
    },
    {
      "Hour": 153,
      "datetime": "2022-09-23T17:15:54"
    },
    {
      "Hour": 163,
      "datetime": "2022-09-23T17:15:55"
    },
    {
      "Hour": 173,
      "datetime": "2022-09-23T17:15:56"
    },
    {
      "Hour": 183,
      "datetime": "2022-09-23T17:15:57"
    },
    {
      "Hour": 193,
      "datetime": "2022-09-23T17:15:58"
    },
    {
      "Hour": 203,
      "datetime": "2022-09-23T17:15:59"
    },
    {
      "Hour": 213,
      "datetime": "2022-09-23T17:16:00"
    },
    {
      "Hour": 223,
      "datetime": "2022-09-23T17:16:01"
    },
    {
      "Hour": 233,
      "datetime": "2022-09-23T17:16:02"
    },
    {
      "Hour": 243,
      "datetime": "2022-09-23T17:16:03"
    },
    {
      "Hour": 253,
      "datetime": "2022-09-23T17:16:04"
    },
    {
      "Hour": 263,
      "datetime": "2022-09-23T17:16:05"
    },
    {
      "Hour": 273,
      "datetime": "2022-09-23T17:16:06"
    },
    {
      "Hour": 283,
      "datetime": "2022-09-23T17:16:07"
    },
    {
      "Hour": 293,
      "datetime": "2022-09-23T17:16:08"
    },
    {
      "Hour": 303,
      "datetime": "2022-09-23T17:16:09"
    },
    {
      "Hour": 313,
      "datetime": "2022-09-23T17:16:10"
    },
    {
      "Hour": 323,
      "datetime": "2022-09-23T17:16:11"
    },
    {
      "Hour": 333,
      "datetime": "2022-09-23T17:16:12"
    },
    {
      "Hour": 343,
      "datetime": "2022-09-23T17:16:13"
    },
    {
      "Hour": 353,
      "datetime": "2022-09-23T17:16:14"
    },
    {
      "Hour": 363,
      "datetime": "2022-09-23T17:16:15"
    },
    {
      "Hour": 373,
      "datetime": "2022-09-23T17:16:16"
    },
    {
      "Hour": 383,
      "datetime": "2022-09-23T17:16:17"
    },
    {
      "Hour": 393,
      "datetime": "2022-09-23T17:16:18"
    },
    {
      "Hour": 403,
      "datetime": "2022-09-23T17:16:19"
    },
    {
      "Hour": 413,
      "datetime": "2022-09-23T17:16:20"
    },
    {
      "Hour": 423,
      "datetime": "2022-09-23T17:16:21"
    },
    {
      "Hour": 433,
      "datetime": "2022-09-23T17:16:22"
    },
    {
      "Hour": 443,
      "datetime": "2022-09-23T17:16:23"
    },
    {
      "Hour": 453,
      "datetime": "2022-09-23T17:16:24"
    },
    {
      "Hour": 463,
      "datetime": "2022-09-23T17:16:25"
    },
    {
      "Hour": 473,
      "datetime": "2022-09-23T17:16:26"
    },
    {
      "Hour": 483,
      "datetime": "2022-09-23T17:16:27"
    },
    {
      "Hour": 493,
      "datetime": "2022-09-23T17:16:28"
    },
    {
      "Hour": 503,
      "datetime": "2022-09-23T17:16:29"
    },
    {
      "Hour": 513,
      "datetime": "2022-09-23T17:16:30"
    },
    {
      "Hour": 523,
      "datetime": "2022-09-23T17:16:31"
    },
    {
      "Hour": 533,
      "datetime": "2022-09-23T17:16:32"
    },
    {
      "Hour": 543,
      "datetime": "2022-09-23T17:16:33"
    },
    {
      "Hour": 553,
      "datetime": "2022-09-23T17:16:34"
    },
    {
      "Hour": 563,
      "datetime": "2022-09-23T17:16:35"
    },
    {
      "Hour": 573,
      "datetime": "2022-09-23T17:16:36"
    },
    {
      "Hour": 583,
      "datetime": "2022-09-23T17:16:37"
    },
    {
      "Hour": 593,
      "datetime": "2022-09-23T17:16:38"
    },
    {
      "Hour": 603,
      "datetime": "2022-09-23T17:16:39"
    },
    {
      "Hour": 613,
      "datetime": "2022-09-23T17:16:40"
    },
    {
      "Hour": 623,
      "datetime": "2022-09-23T17:16:41"
    },
    {
      "Hour": 633,
      "datetime": "2022-09-23T17:16:42"
    },
    {
      "Hour": 643,
      "datetime": "2022-09-23T17:16:43"
    },
    {
      "Hour": 653,
      "datetime": "2022-09-23T17:16:44"
    },
    {
      "Hour": 663,
      "datetime": "2022-09-23T17:16:45"
    },
    {
      "Hour": 673,
      "datetime": "2022-09-23T17:16:46"
    },
    {
      "Hour": 683,
      "datetime": "2022-09-23T17:16:47"
    },
    {
      "Hour": 693,
      "datetime": "2022-09-23T17:16:48"
    },
    {
      "Hour": 703,
      "datetime": "2022-09-23T17:16:49"
    },
    {
      "Hour": 713,
      "datetime": "2022-09-23T17:16:50"
    },
    {
      "Hour": 723,
      "datetime": "2022-09-23T17:16:51"
    },
    {
      "Hour": 733,
      "datetime": "2022-09-23T17:16:52"
    },
    {
      "Hour": 743,
      "datetime": "2022-09-23T17:16:53"
    },
    {
      "Hour": 753,
      "datetime": "2022-09-23T17:16:54"
    },
    {
      "Hour": 763,
      "datetime": "2022-09-23T17:16:55"
    },
    {
      "Hour": 773,
      "datetime": "2022-09-23T17:16:56"
    },
    {
      "Hour": 783,
      "datetime": "2022-09-23T17:16:57"
    },
    {
      "Hour": 793,
      "datetime": "2022-09-23T17:16:58"
    },
    {
      "Hour": 803,
      "datetime": "2022-09-23T17:16:59"
    },
    {
      "Hour": 813,
      "datetime": "2022-09-23T17:17:00"
    },
    {
      "Hour": 823,
      "datetime": "2022-09-23T17:17:01"
    },
    {
      "Hour": 833,
      "datetime": "2022-09-23T17:17:02"
    },
    {
      "Hour": 843,
      "datetime": "2022-09-23T17:17:03"
    },
    {
      "Hour": 853,
      "datetime": "2022-09-23T17:17:04"
    },
    {
      "Hour": 863,
      "datetime": "2022-09-23T17:17:05"
    },
    {
      "Hour": 873,
      "datetime": "2022-09-23T17:17:06"
    },
    {
      "Hour": 883,
      "datetime": "2022-09-23T17:17:07"
    },
    {
      "Hour": 893,
      "datetime": "2022-09-23T17:17:08"
    },
    {
      "Hour": 903,
      "datetime": "2022-09-23T17:17:09"
    },
    {
      "Hour": 913,
      "datetime": "2022-09-23T17:17:10"
    },
    {
      "Hour": 923,
      "datetime": "2022-09-23T17:17:11"
    },
    {
      "Hour": 933,
      "datetime": "2022-09-23T17:17:12"
    },
    {
      "Hour": 943,
      "datetime": "2022-09-23T17:17:13"
    },
    {
      "Hour": 953,
      "datetime": "2022-09-23T17:17:14"
    },
    {
      "Hour": 963,
      "datetime": "2022-09-23T17:17:15"
    },
    {
      "Hour": 973,
      "datetime": "2022-09-23T17:17:16"
    },
    {
      "Hour": 983,
      "datetime": "2022-09-23T17:17:17"
    },
    {
      "Hour": 993,
      "datetime": "2022-09-23T17:17:18"
    }
  ],
  "EquipmentHeader": {
    "UnitInstallDateTime": "2023-05-08T10:00:00.000Z",
    "OEMName": "Rexroth",
    "Model": "sweeperx200",
    "EquipmentID": "sn50123",
    "PIN": "SNP50123123456789"
  },
  "links": [
    {
      "rel": "self",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2022-09-23T00:00:00/2022-09-23T23:00:00/1"
    },
    {
      "rel": "next",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2022-09-23T00:00:00/2022-09-23T23:00:00/2"
    },
    {
      "rel": "prev",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2022-09-23T00:00:00/2022-09-23T23:00:00/1"
    },
    {
      "rel": "last",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2022-09-23T00:00:00/2022-09-23T23:00:00/2"
    }
  ]
}
]

or
// If the page number is greater than the maximum page number
[]

```

### Response Codes

|          Code | Description |
| -------------:|:--------:|
|     `200` | OK |
|     `400` | Bad Request |
|     `401` | Unauthorized |
|     `403` | Forbidden |
|     `404` | Not Found or you do not have access to the fleet/machine |

