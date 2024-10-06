'''
/*************************/
/* emotion_detection.py  */
/*     Version 1.0       */
/*       2024/10/06      */
/*************************/
'''
import sys
import requests
from types import SimpleNamespace

cfg = SimpleNamespace(
    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
    HEADERS={'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'})

def emotion_detector(text_to_analyze):
    # make request
    try:
        input_json = {'raw_document': {'text': text_to_analyze}}
        response = requests.post(cfg.URL, headers=cfg.HEADERS, json=input_json)
        # check response
        if response.status_code == 200:
            # get response
            response_json = response.json()
            print(response_json)
            # get emotions
            emotions = response_json['emotionPredictions'][0]['emotion']
            emotions['dominant_emotion'] = max(emotions, key=emotions.get)
            return emotions
        else:
            return 'Error'
    except Exception as e:
        print(f"Error: {e}")
        return 'Exception'


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise 'Must be using Python 3'
    pass