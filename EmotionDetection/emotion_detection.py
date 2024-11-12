import requests
import json

def emotion_detector(text_to_analyze):
    # URL ของบริการการวิเคราะห์อารมณ์
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # สร้าง payload ของคำร้องในรูปแบบที่คาดหวัง
    myobj = { "raw_document": { "text": text_to_analyze } }

    # หัวข้อที่กำหนดโมเดล ID สำหรับบริการการวิเคราะห์อารมณ์
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # ส่งคำร้อง POST ไปยัง API การวิเคราะห์อารมณ์
    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        first_prediction = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = first_prediction['anger']
        disgust_score = first_prediction['disgust']
        fear_score = first_prediction['fear']
        joy_score = first_prediction['joy']
        sadness_score = first_prediction['sadness']
        # Find the emotion with the highest score
        dominant_emotion = max(first_prediction, key=first_prediction.get)
        
    elif response.status_code == 400 or response.status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

        print(dominant_emotion)


    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }
