# Import the Flask libraries
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''for getting the analysis result of the text'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response = "Invalid text! Please try again!."

    return response

@app.route("/")
def render_index_page():
    '''for rendering the index.html'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
