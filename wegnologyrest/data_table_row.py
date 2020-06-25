
import json

""" Module for Losant API DataTableRow wrapper class """
# pylint: disable=C0301

class DataTableRow(object):
    """ Class containing all the actions for the Data Table Row Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a data table row

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, dataTableRow.*, or dataTableRow.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {string} rowId - ID associated with the data table row
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If data table row was successfully deleted (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if data table row was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "rowId" in kwargs:
            path_params["rowId"] = kwargs["rowId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows/{rowId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves the data table row

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, dataTableRow.*, or dataTableRow.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {string} rowId - ID associated with the data table row
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Data table row information (https://api.app.wnology.io/#/definitions/dataTableRow)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if data table row was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "rowId" in kwargs:
            path_params["rowId"] = kwargs["rowId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows/{rowId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates the data table row

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, dataTableRow.*, or dataTableRow.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} dataTableId - ID associated with the data table
        *  {string} rowId - ID associated with the data table row
        *  {hash} dataTableRow - Object containing updated properties for the data table row (https://api.app.wnology.io/#/definitions/dataTableRowInsertUpdate)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated data table row information (https://api.app.wnology.io/#/definitions/dataTableRow)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if data table row was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "dataTableId" in kwargs:
            path_params["dataTableId"] = kwargs["dataTableId"]
        if "rowId" in kwargs:
            path_params["rowId"] = kwargs["rowId"]
        if "dataTableRow" in kwargs:
            body = kwargs["dataTableRow"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/data-tables/{dataTableId}/rows/{rowId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

