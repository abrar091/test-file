import os
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.identity import ClientSecretCredential

# https://github.com/search?l=Python&q=ResourceManagementClient+web_apps&type=Code

subscription_id = ""

credentials = ClientSecretCredential(
    client_id="",
    client_secret= "{PUT SECRET HERE}",
    tenant_id=""
)
client = ResourceManagementClient(credentials, subscription_id)
web_client = WebSiteManagementClient(credentials, subscription_id)

# Microsoft.Web/sites
# Retrieve the list of resource groups
group_list = client.resource_groups.list()

# Show the groups in formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Azure App Service")
print("-" * (column_width * 2))


for group in list(group_list):
    resource_list = web_client.web_apps.list_by_resource_group(group.name)
    for resource in list(resource_list):
        print(f"{resource.name:<{column_width}}{group.name}")

# client.web_apps.restart("iotIcpDevWu2RgProductconfig","icpdevgetrfsplan")
