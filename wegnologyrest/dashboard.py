
import json

""" Module for Losant API Dashboard wrapper class """
# pylint: disable=C0301

class Dashboard(object):
    """ Class containing all the actions for the Dashboard Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a dashboard

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.User, dashboard.*, or dashboard.delete.

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If dashboard was successfully deleted (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if dashboard was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a dashboard

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {string} password - Password for password-protected dashboards
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Dashboard information (https://api.app.wnology.io/#/definitions/dashboard)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if dashboard was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "password" in kwargs:
            query_params["password"] = kwargs["password"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a dashboard

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.User, dashboard.*, or dashboard.patch.

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {hash} dashboard - Object containing new dashboard properties (https://api.app.wnology.io/#/definitions/dashboardPatch)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Update dashboard information (https://api.app.wnology.io/#/definitions/dashboard)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if dashboard was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "dashboard" in kwargs:
            body = kwargs["dashboard"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

    def send_report(self, **kwargs):
        """
        Sends a snapshot of a dashboard

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.User, dashboard.*, or dashboard.sendReport.

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {hash} reportConfig - Object containing report options (https://api.app.wnology.io/#/definitions/dashboardSendReport)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Send dashboard report (https://api.app.wnology.io/#/definitions/success)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if dashboard was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "reportConfig" in kwargs:
            body = kwargs["reportConfig"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)

    def validate_context(self, **kwargs):
        """
        Validates a context object against the dashboard's context configuration

        Authentication:
        No api access token is required to call this action.

        Parameters:
        *  {string} dashboardId - ID of the associated dashboard
        *  {hash} ctx - The context object to validate (https://api.app.wnology.io/#/definitions/dashboardContextInstance)
        *  {string} password - Password for password-protected dashboards
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If context is valid (https://api.app.wnology.io/#/definitions/validateContextSuccess)

        Errors:
        *  400 - Error if context is invalid (https://api.app.wnology.io/#/definitions/validateContextError)
        *  404 - Error if dashboard or application was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "dashboardId" in kwargs:
            path_params["dashboardId"] = kwargs["dashboardId"]
        if "ctx" in kwargs:
            body = kwargs["ctx"]
        if "password" in kwargs:
            query_params["password"] = kwargs["password"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/dashboards/{dashboardId}/validateContext".format(**path_params)

        return self.client.request("POST", path, params=query_params, headers=headers, body=body)
