
import json

""" Module for Losant API Flows wrapper class """
# pylint: disable=C0301

class Flows(object):
    """ Class containing all the actions for the Flows Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the flows for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, flows.*, or flows.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} sortField - Field to sort the results by. Accepted values are: name, id, creationDate, lastUpdated
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {string} flowClass - Filter the workflows by the given flow class. Accepted values are: edge, cloud, customNode, experience
        *  {hash} triggerFilter - Array of triggers to filter by - always filters against default flow version. (https://api.app.wnology.io/#/definitions/flowTriggerFilter)
        *  {string} includeCustomNodes - If the result of the request should also include the details of any custom nodes referenced by the returned workflows
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of flows (https://api.app.wnology.io/#/definitions/flows)

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
        if "flowClass" in kwargs:
            query_params["flowClass"] = kwargs["flowClass"]
        if "triggerFilter" in kwargs:
            query_params["triggerFilter"] = kwargs["triggerFilter"]
        if "includeCustomNodes" in kwargs:
            query_params["includeCustomNodes"] = kwargs["includeCustomNodes"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def get_by_version(self, **kwargs):
        """
        Returns the flows by version for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, flows.*, or flows.getByVersion.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} sortField - Field to sort the results by. Accepted values are: name, id, creationDate, lastUpdated
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} filterField - Field to filter the results by. Blank or not provided means no filtering. Accepted values are: name
        *  {string} filter - Filter to apply against the filtered field. Supports globbing. Blank or not provided means no filtering.
        *  {string} flowClass - Filter the workflows by the given flow class. Accepted values are: edge, cloud, customNode, experience
        *  {string} version - Return the workflow versions for the given version.
        *  {hash} triggerFilter - Array of triggers to filter by - always filters against default flow version. (https://api.app.wnology.io/#/definitions/flowTriggerFilter)
        *  {string} includeCustomNodes - If the result of the request should also include the details of any custom nodes referenced by the returned workflows
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of flow versions (https://api.app.wnology.io/#/definitions/flowVersions)

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
        if "flowClass" in kwargs:
            query_params["flowClass"] = kwargs["flowClass"]
        if "version" in kwargs:
            query_params["version"] = kwargs["version"]
        if "triggerFilter" in kwargs:
            query_params["triggerFilter"] = kwargs["triggerFilter"]
        if "includeCustomNodes" in kwargs:
            query_params["includeCustomNodes"] = kwargs["includeCustomNodes"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/version".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def api_import(self, **kwargs):
        """
        Import a set of flows and flow versions

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, flows.*, or flows.import.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} importData - New flow and flow version information (https://api.app.wnology.io/#/definitions/flowsImportPost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully imported workflows (https://api.app.wnology.io/#/definitions/flowsImportResult)

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
        if "importData" in kwargs:
            body = kwargs["importData"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows/import".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new flow for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, flows.*, or flows.post.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} flow - New flow information (https://api.app.wnology.io/#/definitions/flowPost)
        *  {string} includeCustomNodes - If the result of the request should also include the details of any custom nodes referenced by the returned workflows
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created flow (https://api.app.wnology.io/#/definitions/flow)

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
        if "flow" in kwargs:
            body = kwargs["flow"]
        if "includeCustomNodes" in kwargs:
            query_params["includeCustomNodes"] = kwargs["includeCustomNodes"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/flows".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)
