'''
/*****************************/
/* test_emotion_detection.py */
/*        Version 1.0        */
/*          2024/10/07       */
/*****************************/
'''
import sys
import unittest

from EmotionDetection import emotion_detector

def get_emotion(text):
    return emotion_detector(text)['dominant_emotion']

class TestMain(unittest.TestCase):
    def test_1(self):
        text = "I am glad this happened"
        self.assertEqual(get_emotion(text), 'joy')

    def test_2(self):
        text = "I am really mad about this"
        self.assertEqual(get_emotion(text), 'anger')

    def test_3(self):
        text = "I feel disgusted just hearing about this"
        self.assertEqual(get_emotion(text), 'disgust')

    def test_4(self):
        text = "I am so sad about this"
        self.assertEqual(get_emotion(text), 'sadness')

    def test_5(self):
        text = "I am really afraid that this will happen"
        self.assertEqual(get_emotion(text), 'fear')

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise RuntimeError('Must be using Python 3')
    unittest.main()