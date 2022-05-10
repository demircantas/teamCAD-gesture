import random
import time

# import pyttsx3
# engine = pyttsx3.init()

import speech_recognition as sr
from difflib import SequenceMatcher

import pyautogui
pyautogui.PAUSE = 0.001

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(sr.Microphone.list_microphone_names())

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=1.2)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
        # response["transcription"] = recognizer.recognize_google_cloud(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    # WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    # NUM_GUESSES = 3
    # PROMPT_LIMIT = 5

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(1)

    while True:
        guess = recognize_speech_from_mic(recognizer, microphone)

        try:
            gt = guess["transcription"].lower()
        except:
            gt = "not recognized"

        if guess["transcription"]:
            print(gt)

            if similar(gt, "translate") > 0.6:
                print("translate {}".format(similar(gt, "translate")))
                pyautogui.press("g")

            if similar(gt, "scale") > 0.6:
                print("scale {}".format(similar(gt, "scale")))
                pyautogui.press("s")

            if similar(gt, "rotate") > 0.6:
                print("rotate {}".format(similar(gt, "rotate")))
                pyautogui.press("r")

            if similar(gt, "enter") > 0.6:
                print("enter {}".format(similar(gt, "enter")))
                pyautogui.press("enter")

            if similar(gt, "escape") > 0.73:
                print("escape {}".format(similar(gt, "escape")))
                pyautogui.press("escape")

            if similar(gt, "delete") > 0.75:
                print("delete {}".format(similar(gt, "delete")))
                pyautogui.press("q")

            if similar(gt, "lateral") > 0.6:
                print("lateral {}".format(similar(gt, "lateral")))
                pyautogui.press("x")
                engine.say("transform restricted laterally")
                engine.runAndWait()

            if similar(gt, "vertical") > 0.6:
                print("vertical {}".format(similar(gt, "vertical")))
                pyautogui.press("z")
                engine.say("vertical constraint active")
                engine.runAndWait()

            if similar(gt, "lengthwise") > 0.6:
                print("lengthwise {}".format(similar(gt, "lengthwise")))
                pyautogui.press("y")
                engine.say("transform restricted to longtitude")
                engine.runAndWait()

            if similar(gt, "create cube") > 0.7:
                print("create cube {}".format(similar(gt, "create cube")))
                pyautogui.write('tmc', interval=0.01)

            if similar(gt, "create cylinder") > 0.7:
                print("create cylinder {}".format(similar(gt, "create cylinder")))
                pyautogui.write('tmy', interval=0.01)

            if similar(gt, "create sphere") > 0.7:
                print("create sphere {}".format(similar(gt, "create sphere")))
                pyautogui.write('tmu', interval=0.01)

            if similar(gt, "greater") > 0.77:
                print("greater {}".format(similar(gt, "greater")))
                pyautogui.write('s2', interval=0.01)
                pyautogui.press('enter')

            if similar(gt, "smaller") > 0.67:
                print("smaller {}".format(similar(gt, "smaller")))
                pyautogui.write('s0.5', interval=0.01)
                pyautogui.press('enter')

            if similar(gt, "upward") > 0.6:
                print("upward {}".format(similar(gt, "upward")))
                pyautogui.write('gz3', interval=0.01)
                pyautogui.press('enter')

            if similar(gt, "down") > 0.7:
                print("down {}".format(similar(gt, "down")))
                pyautogui.write('gz-3', interval=0.01)
                pyautogui.press('enter')

            if similar(gt, "top view") > 0.7:
                print("top view {}".format(similar(gt, "top view")))
                pyautogui.press('num7')

            if similar(gt, "front view") > 0.7:
                print("front view {}".format(similar(gt, "front view")))
                pyautogui.press('num1')

            if similar(gt, "side view") > 0.7:
                print("side view {}".format(similar(gt, "side view")))
                pyautogui.press('num3')

            if similar(gt, "orbit up") > 0.7:
                print("orbit up {}".format(similar(gt, "orbit up")))
                pyautogui.press('num8')
                pyautogui.press('num8')

            if similar(gt, "orbit down") > 0.65:
                print("orbit down {}".format(similar(gt, "down")))
                pyautogui.press('num2')
                pyautogui.press('num2')

            if similar(gt, "orbit left") > 0.7:
                print("orbit left {}".format(similar(gt, "orbit left")))
                pyautogui.press('num4')
                pyautogui.press('num4')

            if similar(gt, "orbit right") > 0.7:
                print("orbit right {}".format(similar(gt, "orbit right")))
                pyautogui.press('num6')
                pyautogui.press('num6')

            if similar(gt, "zoom in") > 0.7:
                print("zoom in {}".format(similar(gt, "zoom in")))
                pyautogui.press('-')
                pyautogui.press('-')

            if similar(gt, "zoom out") > 0.7:
                print("zoom out {}".format(similar(gt, "zoom out")))
                pyautogui.press('=')
                pyautogui.press('=')

            if similar(gt, "show all") > 0.7:
                print("show all {}".format(similar(gt, "show all")))
                pyautogui.hotkey('ctrl', 'home')

            if similar(gt, "undo") > 0.7:
                print("undo {}".format(similar(gt, "undo")))
                pyautogui.hotkey('ctrl', 'z')

            if similar(gt, "duplicate") > 0.7:
                print("duplicate {}".format(similar(gt, "duplicate")))
                pyautogui.press('d')

            if similar(gt, "select all") > 0.7:
                print("select all {}".format(similar(gt, "select all")))
                pyautogui.press('a')

            if gt.replace('.', '', 1).replace('-', '', 1).isnumeric():
                for i in range(5):
                    pyautogui.press('backspace')
                pyautogui.write('{}'.format(float(gt)))

            #
        # if guess["transcription"]:
        #         print(guess["transcription"])
        #         if guess["transcription"].lower() == "please grab object" or guess["transcription"].lower() == "please grab objects":
        #             pyautogui.keyDown('g')
        #             pyautogui.keyUp('g')
        #         elif guess["transcription"].lower() == "please scalex object" or guess["transcription"].lower() == "please scale objects":
        #             pyautogui.keyDown('s')
        #             pyautogui.keyUp('s')
        #         elif guess["transcription"].lower() == "please rotate object" or guess["transcription"].lower() == "please rotate objects":
        #             pyautogui.keyDown('r')
        #             pyautogui.keyUp('r')
        #         elif guess["transcription"].lower() == "please drop object" or guess["transcription"].lower() == "please drop objects":
        #             pyautogui.keyDown('enter')
        #             pyautogui.keyUp('enter')
        #         elif guess["transcription"].lower() == "please delete object" or guess["transcription"].lower() == "please delete objects":
        #             pyautogui.keyDown('q')
        #             pyautogui.keyUp('q')
        #         elif guess["transcription"].lower() == "constrain to x" or guess["transcription"].lower() == "limit to read" or guess["transcription"].lower() == "limit to red" or guess["transcription"].lower() == "side to side":
        #             pyautogui.keyDown('x')
        #             pyautogui.keyUp('x')
        #         elif guess["transcription"].lower() == "constrain to y" or guess["transcription"].lower() == "constrain to why" or guess["transcription"].lower() == "limit to green" or guess["transcription"].lower() == "up and down":
        #             pyautogui.keyDown('z')
        #             pyautogui.keyUp('z')
        #         elif guess["transcription"].lower() == "constrain to z" or guess["transcription"].lower() == "limit to blue" or guess["transcription"].lower() == "front and back":
        #             pyautogui.keyDown('y')
        #             pyautogui.keyUp('y')
        #         elif guess["transcription"].lower() == "please create object":
        #             pyautogui.keyDown('t')
        #             pyautogui.keyUp('t')
        #
        #         elif guess["transcription"].lower() == "please create a cube":
        #             pyautogui.write('tmc', interval=0.01)
        #         elif guess["transcription"].lower() == "please create a cylinder":
        #             pyautogui.write('tmy', interval=0.01)
        #         elif guess["transcription"].lower() == "please create a cone":
        #             pyautogui.write('tmo', interval=0.01)
        #
        #         elif guess["transcription"].lower() == "please scale up":
        #             pyautogui.write('s2', interval=0.01)
        #             pyautogui.keyDown('enter')
        #             pyautogui.keyUp('enter')
        #         elif guess["transcription"].lower() == "please scale down":
        #             pyautogui.write('s0.5', interval=0.01)
        #             pyautogui.keyDown('enter')
        #             pyautogui.keyUp('enter')
        #
        #         elif guess["transcription"].lower() == "please move up":
        #             pyautogui.write('gz3', interval=0.01)
        #             pyautogui.keyDown('enter')
        #             pyautogui.keyUp('enter')
        #
        #         elif guess["transcription"].lower() == "please move down":
        #             pyautogui.write('gz-3', interval=0.01)
        #             pyautogui.keyDown('enter')
        #             pyautogui.keyUp('enter')
        #         elif similar(guess["transcription"].lower(), "testing") > 0.1:
        #             print ("similarity: {}".format(similar(guess["transcription"].lower(), "testing")))

                    # with pyautogui.hold('shift'):
                    #     pyautogui.press('a')
                    # # pyautogui.keyUp('shift')
            elif similar(gt, "thank you") > 0.7:
                print("thank you prob: {}".format(similar(gt, "thank you")))
                engine.say("You are welcome!")
                engine.runAndWait()
                break

            # if similar(gt, "thank you") > 0.7:
            #     print("thank you {}".format(similar(gt, "thank you")))
            #     engine.say("You are welcome!")
            #     engine.runAndWait()