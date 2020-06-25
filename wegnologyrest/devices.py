
import json

""" Module for Losant API Devices wrapper class """
# pylint: disable=C0301

class Devices(object):
    """ Class containing all the actions for the Devices Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Delete devices

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, devices.*, or devices.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} options - Object containing device query and email (https://api.app.wnology.io/#/definitions/devicesDeletePost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Object indicating number of devices deleted or failed (https://api.app.wnology.io/#/definitions/devicesDeleted)
        *  202 - If a job was enqueued for the devices to be deleted (https://api.app.wnology.io/#/definitions/jobEnqueuedResult)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if application was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "options" in kwargs:
            body = kwargs["options"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/delete".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def export(self, **kwargs):
        """
        Creates an export of all device metadata

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, devices.*, or devices.export.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} email - Email address to send export to. Defaults to current user's email.
        *  {string} callbackUrl - Callback URL to call with export result
        *  {hash} options - Object containing device query and optionally email or callback (https://api.app.wnology.io/#/definitions/devicesExportPost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If generation of export was successfully started (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if application was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "email" in kwargs:
            query_params["email"] = kwargs["email"]
        if "callbackUrl" in kwargs:
            query_params["callbackUrl"] = kwargs["callbackUrl"]
        if "options" in kwargs:
            body = kwargs["options"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/export".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Returns the devices for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, devices.*, or devices.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} sortField - Field to sort the results by. Accepted values are: name, id, creationDate, lastUpdated
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {hash} deviceClass - Filter the devices by the given device class or classes (https://api.app.wnology.io/#/definitions/deviceClassFilter)
        *  {hash} tagFilter - Array of tag pairs to filter by (https://api.app.wnology.io/#/definitions/deviceTagFilter)
        *  {string} excludeConnectionInfo - If set, do not return connection info
        *  {string} parentId - Filter devices as children of a given system id
        *  {hash} query - Device filter JSON object which overrides the filterField, filter, deviceClass, tagFilter, and parentId parameters. (https://api.app.wnology.io/#/definitions/advancedDeviceQuery)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of devices (https://api.app.wnology.io/#/definitions/devices)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if application was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "sortField" in kwargs:
            query_params["sortField"] = kwargs["sortField"]
        if "sortDirection" in kwargs:
            query_params["sortDirection"] = kwargs["sortDirection"]
        if "page" in kwargs:
            query_params["page"] = kwargs["page"]
        if "perPage" in kwargs:
            query_params["perPage"] = kwargs["perPage"]
        if "filterField" in kwargs:
            query_params["filterField"] = kwargs["filterField"]
        if "filter" in kwargs:
            query_params["filter"] = kwargs["filter"]
        if "deviceClass" in kwargs:
            query_params["deviceClass"] = kwargs["deviceClass"]
        if "tagFilter" in kwargs:
            query_params["tagFilter"] = kwargs["tagFilter"]
        if "excludeConnectionInfo" in kwargs:
            query_params["excludeConnectionInfo"] = kwargs["excludeConnectionInfo"]
        if "parentId" in kwargs:
            query_params["parentId"] = kwargs["parentId"]
        if "query" in kwargs:
            query_params["query"] = json.dumps(kwargs["query"])
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Update the fields of one or more devices

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, devices.*, or devices.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} patchInfo - Object containing device query or IDs and update operations (https://api.app.wnology.io/#/definitions/devicesPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Object including an update log link and the number of devices updated, failed, and skipped (https://api.app.wnology.io/#/definitions/devicesUpdated)
        *  202 - Successfully queued bulk update job (https://api.app.wnology.io/#/definitions/jobEnqueuedResult)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if application was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "patchInfo" in kwargs:
            body = kwargs["patchInfo"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new device for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, devices.*, or devices.post.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} device - New device information (https://api.app.wnology.io/#/definitions/devicePost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created device (https://api.app.wnology.io/#/definitions/device)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if application was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "device" in kwargs:
            body = kwargs["device"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def remove_data(self, **kwargs):
        """
        Removes all device data for the specified time range. Defaults to all data.

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, devices.*, or devices.removeData.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} options - Object defining the device data to delete and devices to delete from (https://api.app.wnology.io/#/definitions/devicesRemoveDataPost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Object indicating number of devices completed or skipped (https://api.app.wnology.io/#/definitions/devicesDataRemoved)
        *  202 - If a job was enqueued for device data to be removed (https://api.app.wnology.io/#/definitions/jobEnqueuedResult)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if device was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "options" in kwargs:
            body = kwargs["options"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/removeData".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def send_command(self, **kwargs):
        """
        Send a command to multiple devices

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Device, all.Organization, all.User, devices.*, or devices.sendCommand.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} multiDeviceCommand - Command to send to the device (https://api.app.wnology.io/#/definitions/multiDeviceCommand)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If command was successfully sent (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if application was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "multiDeviceCommand" in kwargs:
            body = kwargs["multiDeviceCommand"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/command".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

