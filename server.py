"""Module providing a function printing python version."""
# Import Flask, render_template, request from the flask pramework package
# Import the emotion_detection function from the package created
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion_Detector")

@app.route("/emotionDetector")
def emotional_detector():
    """Function to analyze emotions from a given input."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    emotion_str = ', '.join([f"'{emotion}': {score}" for emotion, score in response.items()])
    response_message = (
        f"For the given statement, the system response is {emotion_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response_message

@app.route("/")
def render_index_page():
    """Function rendering the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
