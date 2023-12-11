from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = '314108b9-1353-4288-8261-202a7e3f2d1c '

credentials = DefaultAzureCredential()


resource_client = ResourceManagementClient(credentials, subscription_id)



