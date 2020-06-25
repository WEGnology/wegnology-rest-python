
import json

""" Module for Losant API ExperienceUser wrapper class """
# pylint: disable=C0301

class ExperienceUser(object):
    """ Class containing all the actions for the Experience User Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes an experience user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceUser.*, or experienceUser.delete.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceUserId - ID associated with the experience user
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If experience user was successfully deleted (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience user was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceUserId" in kwargs:
            path_params["experienceUserId"] = kwargs["experienceUserId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/users/{experienceUserId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on an experience user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, experienceUser.*, or experienceUser.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceUserId - ID associated with the experience user
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Experience user information (https://api.app.wnology.io/#/definitions/experienceUser)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience user was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceUserId" in kwargs:
            path_params["experienceUserId"] = kwargs["experienceUserId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/users/{experienceUserId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about an experience user

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceUser.*, or experienceUser.patch.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} experienceUserId - ID associated with the experience user
        *  {hash} experienceUser - Object containing new properties of the experience user (https://api.app.wnology.io/#/definitions/experienceUserPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated experience user information (https://api.app.wnology.io/#/definitions/experienceUser)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if experience user was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "experienceUserId" in kwargs:
            path_params["experienceUserId"] = kwargs["experienceUserId"]
        if "experienceUser" in kwargs:
            body = kwargs["experienceUser"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/users/{experienceUserId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

