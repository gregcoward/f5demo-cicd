##get token
$TENANTID=$env:tenantId
$APPID=$env:appId
$PASSWORD=$env:pswd
$result=Invoke-RestMethod -Uri https://login.microsoftonline.com/$TENANTID/oauth2/token?api-version=1.0 -Method Post -Body @{"grant_type" = "client_credentials"; "resource" = "https://management.core.windows.net/"; "client_id" = "$APPID"; "client_secret" = "$PASSWORD" }
$token=$result.access_token
$containerGroupName = $env:ctrGrpName

##set subscriptionId and resource group name
$subscriptionId=$env:subId
$resourcegroupname=$env:rgName

$Headers=@{
    'authorization'="Bearer $token"
    'host'="management.azure.com"
    'contentype'='application/json'
}

Invoke-RestMethod -Uri "https://management.azure.com/subscriptions/${subscriptionId}/resourceGroups/${resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/${containerGroupName}?api-version=2018-06-01" -Headers $Headers -Method DELETE
