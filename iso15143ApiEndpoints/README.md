# API endpoints

These endpoints allow you to pull data from your Bodas Connec Data Portal.

## Extended ISO 15143

The [ISO Standard 15143-3](#https://www.iso.org/standard/67556.html) specifies the communication schema designed to provide mobile machinery status data from a telematics provider's server to third-party client applications via the Internet.The data are collected from a mobile machine using telematics data-logging equipment and stored on a telematics provider's server.

Additionally to the data elements specified in the [ISO Standard 15143-3](#https://www.iso.org/standard/67556.html), bodas connects provides additional data elemtents based on the data uploaded by your machines. Contact your Bodas Connect instance owner to get the extended list of additional data elements.

## Authentication
For using the [REST API Endpoints](#endpoints), contact your Bodas Connect instance owner for getting following information:

- clientID: Oauth2 client ID of your fleet,
- secret: Oauth2 secret of your fleet,
- scope: Oauth2 scope of your fleet,
- projectID: Bodas Connect project ID,
- fleetID: Your fleet ID

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

**Response Codes**

|          Code | Description |
| -------------:|:--------:|
|     `200` | OK |
|     `400` | Bad Request |
|     `401` | Unauthorized |
|     `403` | Forbidden |
|     `404` | Not Found |

**Response Sample**

```
{
    "success": true,
    "data": {
        "subscriptions": []
    }
}

or

[]

```
___

### GET {fleetId}/Fleet/Equipment/{machineID}

Get snapshot of all data elements (inclusinve Bodas Connect specific datalements) of a machine. 

**Parameters**

|          Name | Required |  Type   | Description  |
| -------------:|:--------:|:-------:| -------- |
|     `fleetId` | required | string  | Bodas Connect ID of your fleet. |
|     `machineID` | required | string  | Bodas Connect ID of your machine. Machine IDs are returned as a result pulling fleet snapshot data. |

**Response Codes**

|          Code | Description |
| -------------:|:--------:|
|     `200` | OK |
|     `400` | Bad Request |
|     `401` | Unauthorized |
|     `403` | Forbidden |
|     `404` | Not Found |

**Response Sample**

```
{
    "success": true,
    "data": {
        "subscriptions": []
    }
}

or

[]

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

**Response Codes**

|          Code | Description |
| -------------:|:--------:|
|     `200` | OK |
|     `400` | Bad Request |
|     `401` | Unauthorized |
|     `403` | Forbidden |
|     `404` | Not Found |

**Response Sample**

```
{
    "success": true,
    "data": {
        "subscriptions": []
    }
}

or

[]

```

