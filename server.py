from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion_Detector")


@app.route("/emotionDetector")
def emotionDetector():
    # Retrieve the text to analyze 
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the function and store the response
    response = emotion_detector(text_to_analyze)
    
    dominant_emotion = response['dominant_emotion']

    # Generate the formatted string
    emotion_str = ', '.join([f"'{emotion}': {score}" for emotion, score in response.items()]) 
    
    response_message = (
        f"For the given statement, the system response is {emotion_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_message


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)