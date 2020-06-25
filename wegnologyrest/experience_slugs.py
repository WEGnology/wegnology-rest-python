
import json

""" Module for Losant API ExperienceSlugs wrapper class """
# pylint: disable=C0301

class ExperienceSlugs(object):
    """ Class containing all the actions for the Experience Slugs Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the experience slugs for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Application.read, all.Organization, all.Organization.read, all.User, all.User.read, experienceSlugs.*, or experienceSlugs.get.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of experience slugs (https://api.app.wnology.io/#/definitions/experienceSlugs)

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
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/slugs".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Create a new experience slug for an application

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Application, all.Organization, all.User, experienceSlugs.*, or experienceSlugs.post.

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {hash} experienceSlug - New experience slug information (https://api.app.wnology.io/#/definitions/experienceSlugPost)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  201 - Successfully created experience slug (https://api.app.wnology.io/#/definitions/experienceSlug)

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
        if "experienceSlug" in kwargs:
            body = kwargs["experienceSlug"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/experience/slugs".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

