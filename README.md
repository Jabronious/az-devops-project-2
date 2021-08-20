# az-devops-project-2
[![Python application test with Github Actions](https://github.com/Jabronious/az-devops-project-2/actions/workflows/pythonapp.yml/badge.svg?branch=main)](https://github.com/Jabronious/az-devops-project-2/actions/workflows/pythonapp.yml)

# Initial Run of Github Actions Passing:
![image](https://user-images.githubusercontent.com/14021591/129647964-a3d62bbd-0d7b-4930-89ba-8b165c3f961a.png)

# Overview

This project is a complete CI/CD pipeline of a Flask app that makes a sklearn prediction. It is a complete pipeline that starts all the way from the source control that is being hosted on the GitHub GUI that we are using all the way through to the deployment on Azure. In between those two points in the pipeline we have Github Actions that ensures code quality using `pylint` and code coverage using `pytest` (coupled with `pytest-cov`). After that it also includes a working Azure pipeline that takes care of the deployment of the code. All of this is handled off the `main` branch and is triggered any time a merge or push occurs on the said branch thus ensuring that the code we write is of the upmost quality.

## Project Plan

- [Trello Board](https://trello.com/b/J1n6heTV/azure-devops-project-2)  
- [Project Plan](https://docs.google.com/spreadsheets/d/1XA8g_UfMBQ9fupKeEjWAxjeBuQ17x5MeRusmG4qLieU/edit?usp=sharing)

## Instructions

* Architectural Diagram:  
![image](https://user-images.githubusercontent.com/14021591/129821847-1c9d4549-aa44-4046-843c-915ea03ed05c.png)

* Project running on Azure App Service
    - Once the repo has been cloned into the Cloud Shell run `cd az devops-project-2`
    - run `az webapp up -n az-devops-project-2`
    - The app should now be acceissble at `https://az-devops-project-2.azurewebsites.net/`
    ![image](https://user-images.githubusercontent.com/14021591/129961207-d97cbf99-0c3b-421c-80b5-7d1c177000d2.png)

* Project cloned into Azure Cloud Shell
    - On the cloud shell on Azure, open and run `ssh-keygen -t rsa`.
    - Run `cat ~/.ssh/id_rsa.pub` and then copy the outputed key
    - Go the `SSH and GPG Keys` and then Create new SSH Key with the copid text from the previous step
    - Finally, on the Cloud Shell run `git clone git@github.com:Jabronious/az-devops-project-2.git`
    - Recreate screen shot below using `ls`
    ![image](https://user-images.githubusercontent.com/14021591/129959169-cdfc890f-af2b-4b24-8297-b7fbf5efbfdc.png)


* Passing tests that are displayed after running the `make all` command from the `Makefile`
    ![image](https://user-images.githubusercontent.com/14021591/129960105-7f55d27d-b270-44b0-9a4a-47746c0ae0fe.png)

* Output of a test run  
    ![image](https://user-images.githubusercontent.com/14021591/129960673-76d184bf-c170-42f3-90f0-64b8e3873a2b.png)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
    - On [Azure Devops](https://dev.azure.com/) select `+ New Project`  
        ![image](https://user-images.githubusercontent.com/14021591/129962492-d9861d7b-a417-4fe5-aa00-99ace113dae6.png)
    - Input a unique/identfying name for the project and then "Create"
    - Navigate to pipelines and then create new pipeline. When prompted select `Github Yaml`.
    - Find the repo you need (`az-devops-project-2` if you are cloning from this repo)
    - Then select `Run`

* Running Azure App Service from Azure Pipelines automatic deployment
    - After a push occurs to the `main` branch the Azure Pipeline Begins:  
      ![image](https://user-images.githubusercontent.com/14021591/129995033-92c120c9-b4af-45a2-aef5-cdd454da727e.png)
    - Once the Build step completes you will see the Deploy step begin and once everything is successful you will see this:  
      ![image](https://user-images.githubusercontent.com/14021591/129995125-f71334dd-54bb-46af-974f-c3016ae2f52d.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.
    - This can be achieve by running `./make_predict_azure_app.sh` from the root o
    ![image](https://user-images.githubusercontent.com/14021591/129961455-edc6e6a9-f589-4893-b1ff-b58946bb1525.png)

* Output of streamed log files from deployed application
    ![image](https://user-images.githubusercontent.com/14021591/129962109-490fc329-ea71-460f-aca1-5c913d118142.png)

## Enhancements

- Add more test cases to ensure more coverage.
- Create GUI that will allow for easier prediction execution outside of command line tools

## Demo 

[Youtube Link](https://youtu.be/tClwOaNFQsU)

