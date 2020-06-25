
import json

""" Module for Losant API Device wrapper class """
# pylint: disable=C0301

class Device(object):
    """ Class containing all the actions for the Device Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, device.*, or device.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If device was successfully deleted (https://api.app.wnology.io/#/definitions/success)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def export(self, **kwargs):
        """
        Creates a device data export. Defaults to all data.

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.export.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} start - Start time of export (ms since epoch - 0 means now, negative is relative to now)
        *  {string} end - End time of export (ms since epoch - 0 means now, negative is relative to now)
        *  {string} email - Email address to send export to. Defaults to current user's email.
        *  {string} callbackUrl - Callback URL to call with export result
        *  {string} includeBlobData - If set will export any blob attributes in base64 form, otherwise they will be downloadable links which will expire.
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If generation of export was successfully started (https://api.app.wnology.io/#/definitions/success)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "email" in kwargs:
            query_params["email"] = kwargs["email"]
        if "callbackUrl" in kwargs:
            query_params["callbackUrl"] = kwargs["callbackUrl"]
        if "includeBlobData" in kwargs:
            query_params["includeBlobData"] = kwargs["includeBlobData"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/export".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} excludeConnectionInfo - If set, do not return connection info
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Device information (https://api.app.wnology.io/#/definitions/device)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "excludeConnectionInfo" in kwargs:
            query_params["excludeConnectionInfo"] = kwargs["excludeConnectionInfo"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_command(self, **kwargs):
        """
        Retrieve the last known commands(s) sent to the device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getCommand.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} limit - Max command entries to return (ordered by time descending)
        *  {string} since - Look for command entries since this time (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Recent device commands (https://api.app.wnology.io/#/definitions/deviceCommands)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "since" in kwargs:
            query_params["since"] = kwargs["since"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/command".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_composite_state(self, **kwargs):
        """
        Retrieve the composite last complete state of the device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getCompositeState.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} start - Start of time range to look at to build composite state
        *  {string} end - End of time range to look at to build composite state
        *  {string} attributes - Comma-separated list of attributes to include. When not provided, returns all attributes.
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Composite last state of the device (https://api.app.wnology.io/#/definitions/compositeDeviceState)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "attributes" in kwargs:
            query_params["attributes"] = kwargs["attributes"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/compositeState".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_log_entries(self, **kwargs):
        """
        Retrieve the recent log entries about the device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getLogEntries.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} limit - Max log entries to return (ordered by time descending)
        *  {string} since - Look for log entries since this time (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Recent log entries (https://api.app.wnology.io/#/definitions/deviceLog)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "since" in kwargs:
            query_params["since"] = kwargs["since"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/logs".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_state(self, **kwargs):
        """
        Retrieve the last known state(s) of the device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Device, all.Device.read, all.Organization, all.Organization.read, all.User, all.User.read, device.*, or device.getState.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} limit - Max state entries to return (ordered by time descending)
        *  {string} since - Look for state entries since this time (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Recent device states (https://api.app.wnology.io/#/definitions/deviceStates)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "limit" in kwargs:
            query_params["limit"] = kwargs["limit"]
        if "since" in kwargs:
            query_params["since"] = kwargs["since"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/state".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, device.*, or device.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {hash} device - Object containing new properties of the device (https://api.app.wnology.io/#/definitions/devicePatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated device information (https://api.app.wnology.io/#/definitions/device)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
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

        path = "/applications/{applicationId}/devices/{deviceId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def remove_data(self, **kwargs):
        """
        Removes all device data for the specified time range. Defaults to all data.

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, device.*, or device.removeData.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {string} start - Start time of export (ms since epoch - 0 means now, negative is relative to now)
        *  {string} end - End time of export (ms since epoch - 0 means now, negative is relative to now)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If data removal was successfully started (https://api.app.wnology.io/#/definitions/success)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/data".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def send_command(self, **kwargs):
        """
        Send a command to a device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Device, all.Organization, all.User, device.*, or device.sendCommand.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {hash} deviceCommand - Command to send to the device (https://api.app.wnology.io/#/definitions/deviceCommand)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If command was successfully sent (https://api.app.wnology.io/#/definitions/success)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "deviceCommand" in kwargs:
            body = kwargs["deviceCommand"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/command".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def send_state(self, **kwargs):
        """
        Send the current state of the device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Device, all.Organization, all.User, device.*, or device.sendState.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {hash} deviceState - A single device state object, or an array of device state objects (https://api.app.wnology.io/#/definitions/deviceStateOrStates)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If state was successfully received (https://api.app.wnology.io/#/definitions/success)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "deviceState" in kwargs:
            body = kwargs["deviceState"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/state".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def set_connection_status(self, **kwargs):
        """
        Set the current connection status of the device

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Device, all.Organization, all.User, device.*, or device.setConnectionStatus.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} deviceId - ID associated with the device
        *  {hash} connectionStatus - The current connection status of the device (https://api.app.wnology.io/#/definitions/deviceConnectionStatus)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If connection status was successfully applied (https://api.app.wnology.io/#/definitions/success)

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
        if "deviceId" in kwargs:
            path_params["deviceId"] = kwargs["deviceId"]
        if "connectionStatus" in kwargs:
            body = kwargs["connectionStatus"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/devices/{deviceId}/setConnectionStatus".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)
