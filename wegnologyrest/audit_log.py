
import json

""" Module for Losant API AuditLog wrapper class """
# pylint: disable=C0301

class AuditLog(object):
    """ Class containing all the actions for the Audit Log Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Retrieves information on an audit log

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.Organization.read, all.User, all.User.read, auditLog.*, or auditLog.get.

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} auditLogId - ID associated with the audit log
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Audit log information (https://api.app.wnology.io/#/definitions/auditLog)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if audit log was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "auditLogId" in kwargs:
            path_params["auditLogId"] = kwargs["auditLogId"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/audit-logs/{auditLogId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

