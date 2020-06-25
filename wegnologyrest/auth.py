
import json

""" Module for Losant API Auth wrapper class """
# pylint: disable=C0301

class Auth(object):
    """ Class containing all the actions for the Auth Resource """

    def __init__(self, client):
        self.client = client

    def authenticate_device(self, **kwargs):
        """
        Authenticates a device using the provided credentials.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} credentials - Device authentication credentials (https://api.app.wnology.io/#/definitions/deviceCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication. The included api access token by default has the scope 'all.Device'. (https://api.app.wnology.io/#/definitions/authedDevice)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "credentials" in kwargs:
            body = kwargs["credentials"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/auth/device".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def authenticate_user(self, **kwargs):
        """
        Authenticates a user using the provided credentials.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} credentials - User authentication credentials (https://api.app.wnology.io/#/definitions/userCredentials)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication. The included api access token has the scope 'all.User'. (https://api.app.wnology.io/#/definitions/authedUser)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "credentials" in kwargs:
            body = kwargs["credentials"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/auth/user".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def authenticate_user_github(self, **kwargs):
        """
        Authenticates a user via GitHub OAuth.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} oauth - User authentication credentials (access token) (https://api.app.wnology.io/#/definitions/githubLogin)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication. The included api access token has the scope 'all.User'. (https://api.app.wnology.io/#/definitions/authedUser)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "oauth" in kwargs:
            body = kwargs["oauth"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/auth/user/github".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def authenticate_user_saml(self, **kwargs):
        """
        Authenticates a user via a SAML response.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {hash} saml - Encoded SAML response from an IDP for a user. (https://api.app.wnology.io/#/definitions/samlResponse)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful authentication. The included api access token has the scope 'all.User'. (https://api.app.wnology.io/#/definitions/authedUser)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  401 - Unauthorized error if authentication fails (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "saml" in kwargs:
            body = kwargs["saml"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/auth/user/saml".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def sso_domain(self, **kwargs):
        """
        Checks email domain for SSO configuration.

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {string} email - The email address associated with the user login
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Successful finding SSO for domain. Returns SSO request URL and type. (https://api.app.wnology.io/#/definitions/ssoRequest)
        *  204 - No domain associated with an SSO configuration

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

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

        path = "/auth/ssoDomain".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

