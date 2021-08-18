# az-devops-project-2
[![Python application test with Github Actions](https://github.com/Jabronious/az-devops-project-2/actions/workflows/pythonapp.yml/badge.svg?branch=main)](https://github.com/Jabronious/az-devops-project-2/actions/workflows/pythonapp.yml)

# Initial Run of Github Actions Passing:
![image](https://user-images.githubusercontent.com/14021591/129647964-a3d62bbd-0d7b-4930-89ba-8b165c3f961a.png)

# Overview

This project is a complete CI/CD pipeline of a Flask app that makes a sklearn prediction. It is a complete pipeline that starts all the way from the source control that is being hosted on the GitHub GUI that we are using all the way through to the deployment on Azure. In between those two points in the pipeline we have Github Actions that ensures code quality using `pylint` and code coverage using `pytest` (coupled with `pytest-cov`). After that it also includes a working Azure pipeline that takes care of the deployment of the code. All of this is handled off the `main` branch and is triggered any time a merge or push occurs on the said branch thus ensuring that the code we write is of the upmost quality.

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

* Architectural Diagram:  
![image](https://user-images.githubusercontent.com/14021591/129821847-1c9d4549-aa44-4046-843c-915ea03ed05c.png)

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell
    - On the cloud shell on Azure, open and run `ssh-keygen -t rsa`.
    - Run `cat ~/.ssh/id_rsa.pub` and then copy the outputed key
    - Go the `SSH and GPG Keys` and then Create new SSH Key with the copid text from the previous step
    - Finally, on the Cloud Shell run `git clone git@github.com:Jabronious/az-devops-project-2.git`
    - Recreate screen shot below using `ls`
    ![image](https://user-images.githubusercontent.com/14021591/129959169-cdfc890f-af2b-4b24-8297-b7fbf5efbfdc.png)


* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>

