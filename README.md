# PROJECT TIME TRACKING

## SETUP
*** 
### Prerequisites
It is assumed that you have access to the repository
* Linux [debian distro]
* Docker
* Docker-compose
* python 3


1. clone the repository
```bash
  $ git clone git@github.com:fuzumoe/backend_pletnific.git
```
***

2. Create a virtual environment for development

* Create a virtual environment to isolate our package dependencies locally  

```bash
     $ pip install -r dev-requirements.txt 
     $ python3 -m venv venv
     $ source venv/bin/activate  # On Windows use `env\Scripts\activate`
```  

* Install all dependencies  

```bash
  $ pip install -r requirements.txt
```
***  

3. Configure python virtual environment with IDE

* Pycharm  

    see from the following [link](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env)  


* VSCode  
    create `settings.json` file under directory `.vscode` if directory does not exist create one  


```bash
{
    "python.defaultInterpreterPath": "venv/bin/python",  
    "python.linting.enabled": true, 
    "editor. formatOnSave": true
}

```  
***
4. Extract dependecies
```bash
     $ sudo chmod +x
     $ ./scripts/prepare.sh
```
***
5. Run application
```bash
    # spin up teest containers / will take some time when it is run the first time 
    # since it includes database + records creation
    $ docker-compose up
 
```
* API Documentation 

Visit [https://plentific-app-sw5ke.ondigitalocean.app/docs](https://plentific-app-sw5ke.ondigitalocean.app/docs) or in your development environment visit [http://localhost:8000/docs](http://localhost:8000/docs)
***
6. Run tests  
```bash
    # run test
    $ docker-compose run backend ./manage.py test
    # stop all test containers
    $ docker-compose -f docker-compose.test.yml  down
```
7. Populate data <optional>  
this will take around some time to complete
```bash
    # for single file by file manual population of records
     $ docker-compose run backend  ./manage.py  populate --path project_time_tracking/data/pp-data/pp-2022.csv
    # for directory based multi file population of records
     $ docker-compose run backend  ./manage.py  populate --path backend_plentific/data/pp-data

```  


