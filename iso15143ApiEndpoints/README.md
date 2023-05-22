# API endpoints

These endpoints allow you to pull data from your Bodas Connect Data Portal.

## ISO 15143-3 (AEMP 2.0)

The [ISO 15143-3](https://www.iso.org/standard/67556.html) standard describes how to send status data from a telematics provider's server to third-party client applications over the Internet. 

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
The OEM ISO Number (machine VIN = Vehicle Identification Number or PIN = Personal Identification Number) is used as identifier for pulling the data.

Base URL: https://bosch-iot-insights.com/r/{projectId}/bodas/

- Fleet snapshot [{fleetId}/Fleet/{pageNumber}](#get-{fleetId}Fleet{pageNumber}) <br/>
- Machine (Single-element) snapshot [{fleetId}/Fleet/Equipment/{identifier}](#get-{fleetId}FleetEquipment{identifier}) <br/>
- Timeseries data [{fleetId}/Fleet/Equipment/{identifier}/{dataElement}/{startDateUTC}/{endDateUTC}/{pageNumber}](#get-{fleetId}FleetEquipment{identifier}{dataElement}{startDateUTC}{endDateUTC}{pageNumber}) <br/>

___

### GET {fleetId}/Fleet/{pageNumber}

Get a snaphot of all machines in the fleet.

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `pageNumber` | required | int  | Page number to be returned. <br/> MUST be a positive non zero integer. <br/>This endpoint is paginated with 100 records per page. |

**Response Sample**
In this example, the fleet has 2 machines.
```
//Get the first page
[
  {
  "Equipment": [
    {
      "Location": {
        "datetime": "2023-05-08T17:17:39.666Z",
        "Latitude": 48.479507,
        "Longitude": 8.929208,
        "Altitude": 424,
        "AltitudeUnits": "meter"
      },
      "FuelUsed": {
        "datetime": "2023-05-08T17:17:38.342Z",
        "FuelConsumed": 730,
        "FuelUnits": "liter"
      },
      "CumulativeOperatingHours": {
        "datetime": "2023-05-08T17:17:38.343Z",
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
        "datetime": "2022-05-12T17:17:39.666Z",
        "Latitude": 48.479507,
        "Longitude": 8.929208,
        "Altitude": 424,
        "AltitudeUnits": "meter"
      },
      "CumulativeOperatingHours": {
        "datetime": "2022-05-12T17:17:38.343Z",
        "Hour": 162
      },
      "FuelUsed": {
        "datetime": "2022-05-12T17:17:38.342Z",
        "FuelConsumed": 730,
        "FuelUnits": "liter"
      },
      "EquipmentHeader": {
        "UnitInstallDateTime": "2023-05-12T10:00:00.000Z",
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

Get a snapshot view of a single element. This endpoint is paginated with a default of 100 records per page. 

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `identifier` | required | string  |  OEM ISO Number (PIN or VIN). The identifiers are returned as a result of pulling fleet snapshot data. |

**Response Sample**

```
[
 {
  "FuelUsed": {
    "datetime": "2023-05-12T17:17:38.342Z",
    "FuelConsumed": 730,
    "FuelUnits": "liter"
  },
  "Location": {
    "datetime": "2023-05-12T17:17:39.666Z",
    "Latitude": 48.479507,
    "Longitude": 8.929208,
    "Altitude": 424,
    "AltitudeUnits": "meter"
  },
  "CumulativeOperatingHours": {
    "datetime": "2023-05-12T17:17:38.343Z",
    "Hour": 162
  },
  "EquipmentHeader": {
    "UnitInstallDateTime": "2023-05-12T10:00:00.000Z",
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
|     `pageNumber` | required | int  | Page number to be returned. <br/> MUST be a positive non zero integer. <br/>This endpoint is paginated with 100 records per page. |

**Response Sample**

```
[
  {
  "CumulativeOperatingHours": [
    {
      "Hour": 3,
      "datetime": "2023-05-12T17:15:39"
    },
    {
      "Hour": 4,
      "datetime": "2023-05-12T18:15:40"
    },
    ...
    {
      "Hour": 8,
      "datetime": "2023-05-12T22:17:18"
    }
  ],
  "EquipmentHeader": {
    "UnitInstallDateTime": "2023-05-12T10:00:00.000Z",
    "OEMName": "Rexroth",
    "Model": "sweeperx200",
    "EquipmentID": "sn50123",
    "PIN": "SNP50123123456789"
  },
  "links": [
    {
      "rel": "self",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2023-05-12T00:00:00/2023-05-12T23:59:00/1"
    },
    {
      "rel": "next",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2023-05-12T00:00:00/2023-05-12T23:59:00/2"
    },
    {
      "rel": "prev",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2023-05-12T00:00:00/2023-05-12T23:59:00/1"
    },
    {
      "rel": "last",
      "href": "/pvz1481:fleet__bc420002fbqv8d/Fleet/Equipment/SNP50123123456789/CumulativeOperatingHours/2023-05-12T00:00:00/2023-05-12T23:59:00/2"
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
|     `404` | Not Found or you do not have access to the fleet/identifier |

