'''
/*****************/
/*   server.py   */
/*  Version 1.0  */
/*   2024/10/06  */
/*****************/
'''
import sys
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    index.html route.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def app_route_emotion_detector():
    """
    emotionDetector route.
    """
    input_text = request.args.get('textToAnalyze')
    output = emotion_detector(input_text)
    # error or exception check
    if isinstance(output, str):
        return output
    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result="For the given statement, the system response is " \
        f"'anger': {output['anger']}, 'disgust': {output['disgust']}, " \
        f"'fear': {output['fear']}, 'joy': {output['joy']} and "\
        f"'sadness': {output['sadness']}. "\
        f"The dominant emotion is {output['dominant_emotion']}."
    return result


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise RuntimeError('Must be using Python 3')
app.run(host='localhost', port=5000)
