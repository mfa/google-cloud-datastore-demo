# Google Cloud Datastore example

First steps in using Datastore with FastApi

related blogpost: https://madflex.de/posts/using-google-cloud-datastore-with-google-cloud-run/


### initialize datastore

- https://cloud.google.com/datastore/docs/firestore-or-datastore
- I chose "Datastore mode" and as location europe-west3

### Create IAM serviceuser

- for development you need a serviceaccount
- https://cloud.google.com/docs/authentication/production#auth-cloud-implicit-python
- save exported json as `app/credentials.json`

- for production the access is granted because the google-cloud-run instance is in the same project as the datastore


## development

```
docker-compose up web
```

url is http://localhost:8001/


## run on google cloud run

```
gcloud builds submit --tag eu.gcr.io/<PROJECT_ID>/datastore-demo
gcloud run deploy datastore-demo --image eu.gcr.io/<PROJECT_ID>/datastore-demo --allow-unauthenticated
```
