
import json

""" Module for Losant API OrgInvites wrapper class """
# pylint: disable=C0301

class OrgInvites(object):
    """ Class containing all the actions for the Org Invites Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Gets information about an invite

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {string} token - The token associated with the invite
        *  {string} email - The email associated with the invite
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Information about invite (https://api.app.wnology.io/#/definitions/orgInviteInfo)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if invite not found (https://api.app.wnology.io/#/definitions/error)
        *  410 - Error if invite has expired (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "token" in kwargs:
            query_params["token"] = kwargs["token"]
        if "email" in kwargs:
            query_params["email"] = kwargs["email"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/invites".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def post(self, **kwargs):
        """
        Accepts/Rejects an invite

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} invite - Invite info and acceptance (https://api.app.wnology.io/#/definitions/orgInviteAction)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Acceptance/Rejection of invite (https://api.app.wnology.io/#/definitions/orgInviteResult)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if invite not found (https://api.app.wnology.io/#/definitions/error)
        *  410 - Error if invite has expired (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "invite" in kwargs:
            body = kwargs["invite"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/invites".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

