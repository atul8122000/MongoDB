## Install dbt on ubuntu 18.0 using pip 

#### Note : You need to use pip to install dbt Core on Linux operating systems.

#### This will install dbt-core and dbt-postgres only:
#### Step 1: Install dbd-postgres:
```bash
pip install dbt-postgres
```

#### Step 2: Check dbt version:
```bash
dbt --version
```

#### Step 3: Upgrade a specific adapter plugin:
``` bash
pip install --upgrade dbt-<adapter>
```

#### Step 4: Install dbt-core only
```bash
pip install dbt-core
```
#### You can install different dbt package by one command :
```bash
pip install \
  dbt-core \
  dbt-postgres \
  dbt-redshift \
  dbt-snowflake \
  dbt-bigquery
```
#### Initialize or  create New project
```bash
dbt init <project>
```
### dbt generic commands:
##### performs several actions necessary to create a new dbt project.
```bash
dbt init project_name
``` 
##### install the dbt dependencies from packages.yml file
```bash
dbt deps
```
##### this will remove the /dbt_modules 
```bash
dbt clean
```
##### regular run. will run all models based on hierarchy
```bash
dbt run
```
##### will run custom data tests and schema tests
```bash
dbt test
```
##### will load CSV files specified in the data-paths directory into the data warehouse.
```bash
dbt seed
```
##### compiles all models. 
```bash
dbt compile
```
##### execute all the snapshot defined in your project
```bash
dbt snapshot
```
#####  It is useful for deleting the dbt_modules and target directories.
```bash
dbt clean
```
##### make sure your connection, config file, and dbt dependencies are good.
```bash
dbt debug
```
##### run all models in 2 threads and also over-ride the threads in profiles.yml
```bash
dbt run threads 2 
```
