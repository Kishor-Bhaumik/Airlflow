## A basic DAG script to connect a gcloud instance

** PURPOSE **

> start a remote instance named shobdokutir-gpu-2
> run tactron2 till 5 epochs 
> create an output print file as a text file
> move output file to local
> stop instance

** how to run **

`install airflow if not installed from [here](https://youtu.be/46YEL47ieQE)`
`download remote_run.sh in local`
`download run.sh in the instance`
`go to your airflow folder`
`download gcloud_run.py  and copy it to *dags* folder`
`open a terminal in airflow directory and run ***airflow initdb*** `
`then run ***airflow webserver --port 8080*** `
`open another terminal in airflow directory and run ***airflow scheduler*** `
`then in a browser *localhost:8080* `
