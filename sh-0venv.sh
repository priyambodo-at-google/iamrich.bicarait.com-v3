export GCP_PROJECT='work-mylab-machinelearning'     # Change this
export GCP_REGION='us-central1'                     # If you change this, make sure the region is supported.

pip install --upgrade pip
python3 -m venv .venv-iamrich
source .venv-iamrich/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
#streamlit run app.py --browser.serverAddress=localhost --server.enableCORS=false --server.enableXsrfProtection=false