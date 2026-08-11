import os
import json
import subprocess
import firebase_admin
from firebase_admin import credentials, firestore

def download_data():
    service_account_json = os.environ.get('FIREBASE_SERVICE_ACCOUNT')
    if not service_account_json:
        print("❌ FIREBASE_SERVICE_ACCOUNT not set")
        return False
        
    try:
        cred_dict = json.loads(service_account_json)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        
        data = {
            'pages': [],
            'schwerpunkte': [],
            'treatments': [],
            'team': [],
            'press': []
        }
        
        for collection_name in data.keys():
            docs = db.collection(collection_name).get()
            for doc in docs:
                doc_data = doc.to_dict()
                doc_data['id'] = doc.id
                data[collection_name].append(doc_data)
                
        with open('cms_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print("✅ Downloaded data from Firebase to cms_data.json")
        return True
    except Exception as e:
        print(f"❌ Error downloading data: {e}")
        return False

if __name__ == "__main__":
    if download_data():
        print("Running sync_cms.py...")
        subprocess.run(['python', 'sync_cms.py'], check=True)
