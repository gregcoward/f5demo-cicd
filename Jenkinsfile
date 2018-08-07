pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                powershell 'az login --service-principal -u "http://azure-cli-2018-07-09-16-31-25" -p "8f7d17c4-e6db-41dc-8797-9fa1b9d537a1" --tenant "3254cd50-e46e-4a72-9d0c-504f2740f425"'
                powershell 'az group create -l eastus -n $($env:rgName)'
                powershell 'az group deployment create --resource-group $($env:rgName) --mode Incremental --template-uri "https://raw.githubusercontent.com/gregcoward/f5demo-cicd/master/azuresqldeploy.json" --parameters adminPassword="$($env:adminPassword)"'
                powershell 'az group deployment create  --resource-group $($env:rgName) --mode Incremental --template-uri "https://raw.githubusercontent.com/gregcoward/f5demo-cicd/master/azurewebdeploy.json" --parameters adminPassword="$($env:adminPassword)"'
                powershell 'az group deployment create  --resource-group $($env:rgName) --mode Incremental --template-uri "https://raw.githubusercontent.com/gregcoward/f5-azure-arm-templates/master/supported/standalone/1nic/existing-stack/bigiq/azuredeploy.json" --parameters adminPasswordOrKey="$($env:adminPasswordOrKey)" bigIqPassword="$($env:bigIqPassword)" mgmtAddress="$($env:mgmtAddress)"'
      }
        }
    }
}
