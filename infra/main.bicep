@description('Azure region')
param location string = 'switzerlandnorth'

@description('IoT Hub name')
param iotHubName string

@description('IoT Hub SKU')
@allowed([
  'S1'
  'S2'
  'S3'
])
param iotHubSku string = 'S1'

@description('Storage account name (must be globally unique, only lowercase letters and numbers)')
param storageAccountName string

@description('Web App (App Service) name')
param webAppName string

@description('App Service plan name')
param appServicePlanName string = '${webAppName}-plan'

@description('App Service plan SKU')
@allowed([
  'F1'   // Free
  'B1'   // Basic small
])
param appServiceSku string = 'F1'


// Storage Account (Blob Storage)

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
}


// IoT Hub

resource iotHub 'Microsoft.Devices/IotHubs@2021-07-02' = {
  name: iotHubName
  location: location
  sku: {
    name: iotHubSku
    capacity: 1
  }
  properties: {
    publicNetworkAccess: 'Enabled'
    features: 'None'
  }
}


// App Service Plan (Linux)

resource appServicePlan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: appServiceSku
    tier: appServiceSku == 'F1' ? 'Free' : 'Basic'
    size: appServiceSku
    capacity: 1
  }
  kind: 'linux'
  properties: {
    reserved: true // Linux
  }
}


// Web App (backend API)

resource webApp 'Microsoft.Web/sites@2022-09-01' = {
  name: webAppName
  location: location
  kind: 'app,linux'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.10'
      alwaysOn: false
    }
    httpsOnly: true
  }
}

// Outputs
output iotHubHostname string = iotHub.properties.hostName
output storageAccountId string = storageAccount.id
output webAppUrl string = 'https://${webApp.properties.defaultHostName}'
