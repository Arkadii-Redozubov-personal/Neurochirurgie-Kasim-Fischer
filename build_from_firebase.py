import os
import json
import subprocess
import firebase_admin
from firebase_admin import credentials, firestore

def should_heal_collection(col_name, docs, clean_seed):
    if col_name not in clean_seed:
        return False
    target_count = len(clean_seed[col_name])
    if len(docs) == 0:
        return True
    if len(docs) != target_count:
        return True
        
    if col_name == 'team':
        for d in docs:
            name_str = str(d.get('name', '') or d.get('de', {}).get('name', ''))
            if 'Nese' in name_str or 'David Liu' in name_str:
                return True
    elif col_name == 'branches':
        docs_sorted = sorted(docs, key=lambda x: x.get('order', 0))
        city0 = str(docs_sorted[0].get('city', '') or docs_sorted[0].get('de', {}).get('city', ''))
        if 'Viersen' in city0:
            return True
    elif col_name == 'schwerpunkte':
        for d in docs:
            t = str(d.get('title', '') or d.get('de', {}).get('title', ''))
            if 'Phantomschmerzen' in t or '-test' in t:
                return True
    return False

def download_data():
    service_account_json = os.environ.get('FIREBASE_SERVICE_ACCOUNT')
    if not service_account_json:
        print('❌ FIREBASE_SERVICE_ACCOUNT not set')
        return False
        
    try:
        cred_dict = json.loads(service_account_json)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        
        clean_seed = {}
        if os.path.exists('clean_seed.json'):
            with open('clean_seed.json', 'r', encoding='utf-8') as f:
                clean_seed = json.load(f)

        collections = [
            'pages', 'schwerpunkte', 'treatments', 'team',
            'press', 'branches', 'diagnostik', 'faq', 'reviews'
        ]
        
        # Check and heal collections if needed
        for col_name in collections:
            if col_name not in clean_seed:
                continue
            cur_docs = []
            for doc in db.collection(col_name).get():
                d = doc.to_dict()
                d['id'] = doc.id
                cur_docs.append(d)
                
            if should_heal_collection(col_name, cur_docs, clean_seed):
                print(f'🔧 Auto-healing Firestore collection {col_name} ({len(cur_docs)} -> {len(clean_seed[col_name])} items)...')
                # Delete existing
                for doc in db.collection(col_name).get():
                    doc.reference.delete()
                # Insert clean items
                for idx, item in enumerate(clean_seed[col_name]):
                    doc_id = item.get('id') or f'{col_name}_{idx + 1}'
                    db.collection(col_name).document(doc_id).set(item)
                print(f'✅ Collection {col_name} healed successfully!')

        # Download all data into cms_data.json
        data = {}
        for col_name in collections:
            data[col_name] = []
            for doc in db.collection(col_name).get():
                doc_data = doc.to_dict()
                doc_data['id'] = doc.id
                data[col_name].append(doc_data)
                
        with open('cms_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print('✅ Downloaded data from Firebase to cms_data.json')
        return True
    except Exception as e:
        print(f'❌ Error downloading data: {e}')
        return False

if __name__ == '__main__':
    if download_data():
        print('Running sync_cms.py...')
        subprocess.run(['python3', 'sync_cms.py'], check=True)
        if os.path.exists('build_sprechzeiten.py'):
            print('Running build_sprechzeiten.py...')
            subprocess.run(['python3', 'build_sprechzeiten.py'], check=True)
