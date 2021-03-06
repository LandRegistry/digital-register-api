# digital-register-api

This is the repo for the backend of the digital register service. It is written in Python, with the Flask framework.  

### Digital Register API build status

[![Build Status](http://52.16.47.1/job/digital-register-api-unit-test%20(Master)/badge/icon)](http://52.16.47.1/job/digital-register-api-unit-test%20(Master)/)

### Digital Register Acceptance tests status

[![Build Status](http://52.16.47.1/job/digital-register-frontend-acceptance-tests/badge/icon)](http://52.16.47.1/job/digital-register-frontend-acceptance-tests/)

## Setup

To create a virtual env, run the following from a shell:

```  
    mkvirtualenv -p /usr/bin/python3 digital-register-api
    source environment.sh
    pip install -r requirements.txt
```

## Run unit tests

To run unit tests for the Digital Register, go to its folder and run `lr-run-tests`.

## Run integration tests

In order to run Digital Register API integration tests, go to its folder and run `./run_integration_tests.sh`.
This script creates the test database (test_register_data) and test elasticsearch index (test-landregistry)
and runs the tests against them.
Make sure you have postgresql and elasticsearch services running (by executing the `lr-start-services` command).

## Run the acceptance tests

To run the acceptance tests for the Digital Register, go to the `acceptance-tests` folder inside the `digital-register-frontend` repository and run:
```
   ./run-tests.sh
```

You will need to have a Postgres database running (see `db/lr-start-db` and `db/insert-fake-data` scripts in the [centos-dev-env](https://github.com/LandRegistry/centos-dev-env) project), as well as the digital-register-frontend and digital-register-api applications running on your development VM.
 
## Run the server

### Run in dev mode

To run the server in dev mode, execute the following command:

    ./run_flask_dev.sh

### Run using gunicorn

To run the server using gunicorn, activate your virtual environment
and execute the following commands:

    pip install gunicorn
    gunicorn -p /tmp/gunicorn.pid service.server:app -c gunicorn_settings.py 

## Jenkins builds 

We use three separate builds:
- [branch](http://52.16.47.1/job/digital-register-api-unit-test%20(Branch)/)
- [master](http://52.16.47.1/job/digital-register-api-unit-test%20(Master)/)
- [acceptance](http://52.16.47.1/job/digital-register-frontend-acceptance-tests/)

## Database migrations

We use Flask-Migrate (a project which integrates Flask with Alembic, a migration
tool from the author of SQLAlchemy) to handle database migrations. Every time a
model is added or modified, a migration script should be created and committed
to our version control system.

From inside a virtual environment, and after sourcing environment.sh, run the
following to add a new migration script:

    python3 manage.py db migrate -m "add foobar field"

Should you ever need to write a migration script from scratch (to migrate data
for instance) you should use the revision command instead of migrate:

    python3 manage.py db revision -m "do something complicated"

Read Alembic's documentation to learn more.

Once you have a migration script, the next step is to apply it to the database.
To do this run the upgrade command:

    python3 manage.py db upgrade

## Populate the mapping table

Once you have the new uprn_mapping table, you may want to have some data in it.
Assume you have created and working on the digital-register-api virtual environment:

    python3 import_uprn_mapping_data.py -file path/to/file.csv

Some useful operators:

    -f path/to/file.csv This will import a CSV file.
    -s <number>         This will start the file read from <number>. Handy if the import stopped half way through a million records and you need to start again around 500000.
    -o                  This will delete and replace any existing entries
    -c                  This will clear the whole table and start again
