from dotenv import load_dotenv
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

documents_path = Path.home() / ".env"

load_dotenv(os.path.join(documents_path, 'gv.env'))
YA_IAM_TOKEN = os.environ.get('YA_IAM_TOKEN')
YA_ART_CAT_ID = os.environ.get('YA_ART_CAT_ID')


BASE_URL = "https://llm.api.cloud.yandex.net"
GEN_URL = f"{BASE_URL}/foundationModels/v1/imageGenerationAsync"
OP_STATUS_URL = f"{BASE_URL}/operations"
MODEL_URI = f"art://{YA_ART_CAT_ID}/yandex-art/latest"