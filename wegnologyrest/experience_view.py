
import json

""" Module for Losant API ExperienceView wrapper class """
# pylint: disable=C0301

class ExperienceView(object):
    """ Class containing all the actions for the Experience View Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes an experience view

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceView.*, or experienceView.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceViewId - ID associated with the experience view
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If experience view was successfully deleted (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience view was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceViewId" in kwargs:
            path_params["experienceViewId"] = kwargs["experienceViewId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/views/{experienceViewId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on an experience view

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, experienceView.*, or experienceView.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceViewId - ID associated with the experience view
        *  {string} version - Version of this experience view to return
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Experience view information (https://api.app.wnology.io/#/definitions/experienceView)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience view was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceViewId" in kwargs:
            path_params["experienceViewId"] = kwargs["experienceViewId"]
        if "version" in kwargs:
            query_params["version"] = kwargs["version"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/views/{experienceViewId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def linked_resources(self, **kwargs):
        """
        Retrieves information on resources linked to an experience view

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, experienceView.*, or experienceView.linkedResources.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceViewId - ID associated with the experience view
        *  {string} version - Version of this experience view to query
        *  {string} includeCustomNodes - If the result of the request should also include the details of any custom nodes referenced by returned workflows
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Linked resource information (https://api.app.wnology.io/#/definitions/experienceLinkedResources)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience view was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceViewId" in kwargs:
            path_params["experienceViewId"] = kwargs["experienceViewId"]
        if "version" in kwargs:
            query_params["version"] = kwargs["version"]
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

        path = "/applications/{applicationId}/experience/views/{experienceViewId}/linkedResources".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about an experience view

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceView.*, or experienceView.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceViewId - ID associated with the experience view
        *  {hash} experienceView - Object containing new properties of the experience view (https://api.app.wnology.io/#/definitions/experienceViewPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated experience view information (https://api.app.wnology.io/#/definitions/experienceView)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience view was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceViewId" in kwargs:
            path_params["experienceViewId"] = kwargs["experienceViewId"]
        if "experienceView" in kwargs:
            body = kwargs["experienceView"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/views/{experienceViewId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

