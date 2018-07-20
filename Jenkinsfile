pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                powershell 'az group deployment create  --resource-group $($env:rgName) --mode Incremental --template-uri "https://raw.githubusercontent.com/gregcoward/f5demo-cicd/master/azurewafdeploy.json" --parameters location="$($env:location)" namePrefix="$($env:namePrefix)" adminUsername="$($env:adminUserName)" adminPassword="$($env:adminPassword)" licenseToken1="$($env:licenseToken1)" licenseToken2="$($env:licenseToken2)" appAddress1="$($env:appAddress1)" appAddress2="$($env:appAddress2)" applicationType="$($env:applicationType)" securityBlockingLevel="$($env:securityBlockingLevel)" applicationCertificate="$($env:applicationCertificate)" applicationKey="$($env:applicationKey)" applicationChain="$($env:applicationChain)"'
      }
        }
    }
}
