import requests
import random
import time
import base64
import config as cfg
import logging

class ImageGenerator:
    def __init__(self):
        self.iam_token = cfg.YA_IAM_TOKEN
    def generate_image(self, description, style, shape="square"):
        headers = {
            "Authorization": f"Bearer {self.iam_token}",
            "Content-Type": "application/json"
        }
        data = {
            "modelUri": cfg.MODEL_URI,
            "generationOptions": {
                "seed": f"{random.randint(0, 1000000)}",
                "aspectRatio": {
                    "widthRatio": "1",
                    "heightRatio": "1"
                }
            },
            "messages": [
                {
                    "weight": "1",
                    "text": f"Нарисуй логотип в форме {shape} под описание: {description}, в стиле: {style}"
                }
            ]
        }
        logging.info("***start generation")
        response = requests.post(cfg.GEN_URL, headers=headers, json=data)
        if response.status_code == 200:
            request_id = response.json()['id']
            done = False
            while not done:
                time.sleep(5)
                url = f"{cfg.OP_STATUS_URL}/{request_id}"
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    if "response" in response.json():
                        image_base64 = response.json()['response']['image']
                        #image_data = base64.b64decode(image_base64)
                        #with open('image.jpeg', 'wb') as file:
                        #    file.write(image_data)
                        logging.info("***ready")
                        return image_base64
                    else:
                        logging.debug("******waiting")

                else:
                    logging.error(f"Ошибка ответа: {response.status_code} - {response.text}")
                    return f"Ошибка ответа: {response.status_code} - {response.text}"
        else:
            logging.error(f"Ошибка запроса: {response.status_code} - {response.text}")
            return f"Ошибка запроса: {response.status_code} - {response.text}"
