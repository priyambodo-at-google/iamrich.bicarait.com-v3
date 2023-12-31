export GCP_REGION='us-central1'
export GCP_PROJECT='work-mylab-machinelearning'
export AR_REPO='iamrichv3-artifactregistry-bydoddi'  
export SERVICE_NAME='iamrich-bicarait-com-v3' 

#gcloud artifacts repositories create "$AR_REPO" --location="$GCP_REGION" --repository-format=Docker
gcloud auth configure-docker "$GCP_REGION-docker.pkg.dev"
gcloud builds submit --tag "$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME"

gcloud run deploy "$SERVICE_NAME" \
   --port=80 \
   --image="$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME" \
   --allow-unauthenticated \
   --region=$GCP_REGION \
   --platform=managed  \
   --project=$GCP_PROJECT \
   --set-env-vars=GCP_PROJECT=$GCP_PROJECT,GCP_REGION=$GCP_REGION