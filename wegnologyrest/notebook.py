
import json

""" Module for Losant API Notebook wrapper class """
# pylint: disable=C0301

class Notebook(object):
    """ Class containing all the actions for the Notebook Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a notebook

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, notebook.*, or notebook.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} notebookId - ID associated with the notebook
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If notebook was successfully deleted (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if notebook was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "notebookId" in kwargs:
            path_params["notebookId"] = kwargs["notebookId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/notebooks/{notebookId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def execute(self, **kwargs):
        """
        Triggers the execution of a notebook

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, notebook.*, or notebook.execute.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} notebookId - ID associated with the notebook
        *  {hash} executionOptions - The options for the execution (https://api.app.wnology.io/#/definitions/notebookExecutionOptions)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If execution request was accepted and successfully queued (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if notebook was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "notebookId" in kwargs:
            path_params["notebookId"] = kwargs["notebookId"]
        if "executionOptions" in kwargs:
            body = kwargs["executionOptions"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/notebooks/{notebookId}/execute".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a notebook

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, notebook.*, or notebook.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} notebookId - ID associated with the notebook
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - notebook information (https://api.app.wnology.io/#/definitions/notebook)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if notebook was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "notebookId" in kwargs:
            path_params["notebookId"] = kwargs["notebookId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/notebooks/{notebookId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def logs(self, **kwargs):
        """
        Retrieves information on notebook executions

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, notebook.*, or notebook.logs.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} notebookId - ID associated with the notebook
        *  {string} limit - Max log entries to return (ordered by time descending)
        *  {string} since - Look for log entries since this time (ms since epoch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - notebook execution information (https://api.app.wnology.io/#/definitions/notebookExecutionLogs)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if notebook was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "notebookId" in kwargs:
            path_params["notebookId"] = kwargs["notebookId"]
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

        path = "/applications/{applicationId}/notebooks/{notebookId}/logs".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a notebook

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, notebook.*, or notebook.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} notebookId - ID associated with the notebook
        *  {hash} notebook - Object containing new properties of the notebook (https://api.app.wnology.io/#/definitions/notebookPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated notebook information (https://api.app.wnology.io/#/definitions/notebook)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if notebook was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "notebookId" in kwargs:
            path_params["notebookId"] = kwargs["notebookId"]
        if "notebook" in kwargs:
            body = kwargs["notebook"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/notebooks/{notebookId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def request_input_data_export(self, **kwargs):
        """
        Requests a combined zip file of the potential input data for a notebook execution

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, notebook.*, or notebook.requestInputDataExport.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} notebookId - ID associated with the notebook
        *  {hash} exportOptions - The options for the export (https://api.app.wnology.io/#/definitions/notebookDataExportOptions)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If export request was accepted and successfully queued (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if notebook was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "notebookId" in kwargs:
            path_params["notebookId"] = kwargs["notebookId"]
        if "exportOptions" in kwargs:
            body = kwargs["exportOptions"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/notebooks/{notebookId}/requestInputDataExport".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

