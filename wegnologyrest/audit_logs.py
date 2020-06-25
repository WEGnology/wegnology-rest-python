
import json

""" Module for Losant API AuditLogs wrapper class """
# pylint: disable=C0301

class AuditLogs(object):
    """ Class containing all the actions for the Audit Logs Resource """

    def __init__(self, client):
        self.client = client

    def get(self, **kwargs):
        """
        Returns the audit logs for the organization

        Authentication:
        The client must be configured with a valid api
        access token to call this action. The token
        must include at least one of the following scopes:
        all.Organization, all.Organization.read, all.User, all.User.read, auditLogs.*, or auditLogs.get.

        Parameters:
        *  {string} orgId - ID associated with the organization
        *  {string} sortField - Field to sort the results by. Accepted values are: creationDate, responseStatus, actorName
        *  {string} sortDirection - Direction to sort the results by. Accepted values are: asc, desc
        *  {string} page - Which page of results to return
        *  {string} perPage - How many items to return per page
        *  {string} start - Start of time range for audit log query
        *  {string} end - End of time range for audit log query
        *  {hash} auditLogFilter - Filters for the audit log query (https://api.app.wnology.io/#/definitions/auditLogFilter)
        *  {string} losantdomain - Domain scope of request (rarely needed)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Collection of audit logs (https://api.app.wnology.io/#/definitions/auditLogs)

        Errors:
        *  400 - Error if malformed request (https://api.app.wnology.io/#/definitions/error)
        *  404 - Error if organization was not found (https://api.app.wnology.io/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "orgId" in kwargs:
            path_params["orgId"] = kwargs["orgId"]
        if "sortField" in kwargs:
            query_params["sortField"] = kwargs["sortField"]
        if "sortDirection" in kwargs:
            query_params["sortDirection"] = kwargs["sortDirection"]
        if "page" in kwargs:
            query_params["page"] = kwargs["page"]
        if "perPage" in kwargs:
            query_params["perPage"] = kwargs["perPage"]
        if "start" in kwargs:
            query_params["start"] = kwargs["start"]
        if "end" in kwargs:
            query_params["end"] = kwargs["end"]
        if "auditLogFilter" in kwargs:
            query_params["auditLogFilter"] = kwargs["auditLogFilter"]
        if "losantdomain" in kwargs:
            headers["losantdomain"] = kwargs["losantdomain"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/orgs/{orgId}/audit-logs".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

