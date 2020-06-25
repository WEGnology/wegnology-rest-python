
import json

""" Module for Losant API ExperienceVersion wrapper class """
# pylint: disable=C0301

class ExperienceVersion(object):
    """ Class containing all the actions for the Experience Version Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes an experience version

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceVersion.*, or experienceVersion.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceVersionIdOrName - Version ID or version name associated with the experience version
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If experience version was successfully deleted (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience version was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceVersionIdOrName" in kwargs:
            path_params["experienceVersionIdOrName"] = kwargs["experienceVersionIdOrName"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/versions/{experienceVersionIdOrName}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on an experience version

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, experienceVersion.*, or experienceVersion.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceVersionIdOrName - Version ID or version name associated with the experience version
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Experience version information (https://api.app.wnology.io/#/definitions/experienceVersion)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience version was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceVersionIdOrName" in kwargs:
            path_params["experienceVersionIdOrName"] = kwargs["experienceVersionIdOrName"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/versions/{experienceVersionIdOrName}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about an experience version

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceVersion.*, or experienceVersion.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceVersionIdOrName - Version ID or version name associated with the experience version
        *  {hash} experienceVersion - Object containing new properties of the experience version (https://api.app.wnology.io/#/definitions/experienceVersionPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated experience version information (https://api.app.wnology.io/#/definitions/experienceVersion)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience version was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceVersionIdOrName" in kwargs:
            path_params["experienceVersionIdOrName"] = kwargs["experienceVersionIdOrName"]
        if "experienceVersion" in kwargs:
            body = kwargs["experienceVersion"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/versions/{experienceVersionIdOrName}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

