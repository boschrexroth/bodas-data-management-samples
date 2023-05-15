# API endpoints

These endpoints allow you to pull data from your Bodas Connec Data Portal.

## Extended ISO 15143

The [ISO Standard 15143-3](#https://www.iso.org/standard/67556.html) The standard describes how to send status data from a telematics provider's server to third-party client applications over the Internet. Furthermore, Bodas Connect provides additional data elements based on the data uploaded by your machines. 
The OEM ISO NUmber (machine VIN (Vehicle Identification Number) or PIN (Personal Identification Number)) is used as identifier for pulling data.

## Authentication
For information (see the list below) about using the [REST API Endpoints](#endpoints), please contact your instance owner.
Following information are needed:

- Client ID: OAuth2 client ID of your fleet,
- Client secret: OAuth2 secret of your fleet,
- scope: OAuth2 scope of your fleet,
- projectID: Bodas Connect project ID,
- fleetId: Your fleet ID 

## Endpoints
Base URL: https://bosch-iot-insights.com/r/{projectId}/bodas/

- Fleet snapshot [{fleetId}/Fleet/{pageNumber}](#get-{fleetId}Fleet{pageNumber}) <br/>
- Machine (Single-element) snapshot [{fleetId}/Fleet/Equipment/{machineID}](#get-{fleetId}FleetEquipment{machineID}) <br/>
- Timeseries data [{fleetId}/Fleet/Equipment/{machineID}/{dataElement}/{startDateUTC}/{endDateUTC}/{pageNumber}](#get-{fleetId}FleetEquipment{machineID}{dataElement}{startDateUTC}{endDateUTC}{pageNumber}) <br/>

___

### GET {fleetId}/Fleet/{pageNumber}

Get asnaphots of all machines in the fleet.

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
        "CumulativeOperatingHours": {
          "Hour": 2053.8,
          "datetime": "2023-02-08T12:38:02Z"
        },
        //EEC1__EngSpeed is not an ISO 15143 data element, but it is included in the results.
        "EEC1__EngSpeed": {
          "EEC1__EngSpeed": 1265.3,
          "EEC1__EngSpeedUnits": "rpm",
          "datetime": "2023-02-08T12:39:49Z"
        },
        "Locations": {
          "Latitude": 48.424358,
          "Longitude": 9.935278,
          "Altitude": 603.6,
          "AltitudeUnits": "meter",
          "datetime": "2023-02-08T12:37:29Z"
        },
        //EquipmentHeader is extended with Bodas Connect specific identifiers.
        "EquipmentHeader": {
          "BodasMachineId": "Machine1",
          "BodasTelematicsId": "RCU1",
          "BodasThingId": "project1:model1__RCU1",
          "Model": "model1",
          "UnitInstallDateTime": "2021-10-14T17:56:28Z"
        }
      },
      {
        "CumulativeOperatingHours": {
          "Hour": 736.1,
          "datetime": "2023-02-13T10:20:09Z"
        },
        "Locations": {
          "Latitude": 48.424002,
          "Longitude": 9.935772,
          "Altitude": 607.1,
          "AltitudeUnits": "meter",
          "datetime": "2023-02-13T10:24:10Z"
        },
        //EEC1__EngSpeed is not an ISO 15143 data element, but it is included in the results.
        "EEC1__EngSpeed": {
          "EEC1__EngSpeed": 943.2,
          "EEC1__EngSpeedUnits": "rpm",
          "datetime": "2023-02-13T13:07:28Z"
        },
        //EquipmentHeader is extended with Bodas Connect specific identifiers.
        "EquipmentHeader": {
          "BodasMachineId": "Machine2",
          "BodasTelematicsId": "RCU2",
          "BodasThingId": "project1:model1__RCU2",
          "Model": "model1",
          "UnitInstallDateTime": "2021-11-29T14:26:12Z"
        }
      }      
    ],
    "links": [
      {
        "rel": "self",
        "href": "/Fleet/1"
      },
      {
        "rel": "next",
        "href": "/Fleet/1"
      },
      {
        "rel": "prev",
        "href": "/Fleet/1"
      },
      {
        "rel": "last",
        "href": "/Fleet/1"
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
        "href": "/Fleet/2"
      },
      {
        "rel": "next",
        "href": "/Fleet/1"
      },
      {
        "rel": "prev",
        "href": "/Fleet/1"
      },
      {
        "rel": "last",
        "href": "/Fleet/1"
      }
    ]
  }
]

```
___

### GET {fleetId}/Fleet/Equipment/{machineID}

Get snapshot of all data elements (inclusinve Bodas Connect specific datalements) of a machine. 

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `machineID` | required | string  | Bodas Connect ID of your machine. Machine IDs are returned as a result pulling fleet snapshot data. |

**Response Sample**

```
[
    "CumulativeOperatingHours": {
      "Hour": 736.1,
      "datetime": "2023-02-13T10:20:09Z"
    },
    "Locations": {
        "Latitude": 48.424002,
        "Longitude": 9.935772,
        "Altitude": 607.1,
        "AltitudeUnits": "meter",
        "datetime": "2023-02-13T10:24:10Z"
    },
    //EEC1__EngSpeed is not an ISO 15143 data element, but it is included in the results.
    "EEC1__EngSpeed": {
      "EEC1__EngSpeed": 1244.4,
      "EEC1__EngSpeedUnits": "rpm",
      "datetime": "2023-02-13T13:07:28Z"
    },
    //EquipmentHeader is extended with Bodas Connect specific identifiers.
    "EquipmentHeader": {
        "BodasMachineId": "Machine2",
        "BodasTelematicsId": "RCU2",
        "BodasThingId": "project1:model1__RCU2",
        "Model": "model1",
        "UnitInstallDateTime": "2021-11-29T14:26:12Z"
    },
    "SnapshotTime": "2023-02-13T23:26:12Z",
    "Version": "0.0.1"
  }
]

```

___

### GET {fleetId}/Fleet/Equipment/{machineID}/{dataElement}/{startDateUTC}/{endDateUTC}/{pageNumber}

Get timeseries data of a data element of a machine.

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `machineID` | required | string  | Bodas Connect ID of your machine. Machine IDs are returned as a result pulling fleet snapshot data. |
|     `dataElement` | required | string  | Data element to be returned. |
|     `startDateUTC` | required | string  | Start date and time of the timeseries. <br/>All date and time stamps in an XML document shall be formatted as ISO 8601 (all parts) “date and time” that includes the year, month, day, hour, minutes, and seconds. It does not include fractional seconds.<br/>Date and Time are expressed as: YYYY-MM-DDThh:mm:ssZ. |
|     `endDateUTC` | required | string  | End date and time of the timeseries. <br/>All date and time stamps in an XML document shall be formatted as ISO 8601 (all parts) “date and time” that includes the year, month, day, hour, minutes, and seconds. It does not include fractional seconds.<br/>Date and Time are expressed as: YYYY-MM-DDThh:mm:ssZ. |
|     `pageNumber` | required | int  | Page number to be returned. <br/> MUSS be a positive non zero integer. <br/>This endpoint is paginated with 100 records per page. |

**Response Sample**

```
[
  {
    "CumulativeOperatingHours": [
      {
        "Hour": 1848.65,
        "datetime": "2023-02-09T06:30:00Z"
      },
      {
        "Hour": 1848.7,
        "datetime": "2023-02-09T06:35:00Z"
      },
      {
        "Hour": 1848.8,
        "datetime": "2023-02-09T06:40:00Z"
      },
      {
        "Hour": 1848.9,
        "datetime": "2023-02-09T06:45:00Z"
      },
      {
        "Hour": 1848.95,
        "datetime": "2023-02-09T06:50:00Z"
      },
      
      ...

      {
        "Hour": 1856.55,
        "datetime": "2023-02-09T15:10:00Z"
      },
      {
        "Hour": 1856.65,
        "datetime": "2023-02-09T15:15:00Z"
      },
      {
        "Hour": 1856.8,
        "datetime": "2023-02-09T15:20:00Z"
      },
      {
        "Hour": 1856.9,
        "datetime": "2023-02-09T15:25:00Z"
      },
      {
        "Hour": 1857.0,
        "datetime": "2023-02-09T15:30:00Z"
      }
    ],
    "links": [
      {
        "rel": "self",
        "href": "/Fleet/Equipment/510TS_15075/CumulativeOperatingHours/2023-02-09T00:00:00Z/2023-02-14T00:00:00Z/1"
      },
      {
        "rel": "next",
        "href": "/Fleet/Equipment/510TS_15075/CumulativeOperatingHours/2023-02-09T00:00:00Z/2023-02-14T00:00:00Z/2"
      },
      {
        "rel": "prev",
        "href": "/Fleet/Equipment/510TS_15075/CumulativeOperatingHours/2023-02-09T00:00:00Z/2023-02-14T00:00:00Z/1"
      },
      {
        "rel": "last",
        "href": "/Fleet/Equipment/510TS_15075/CumulativeOperatingHours/2023-02-09T00:00:00Z/2023-02-14T00:00:00Z/3"
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

