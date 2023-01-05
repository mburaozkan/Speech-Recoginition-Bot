import speech_recognition as sr
import webbrowser as wb
import time


def speech_cutter(main_str, cut_str):
    return_str = ""
    index_list = []
    for index, _ in enumerate(main_str):
        if _ == cut_str[0]:
            for i in range(len(cut_str)):
                try:
                    if main_str[index + i] == cut_str[i] and not cut_str[i].isspace():
                        if main_str[index + i + 1] == cut_str[i + 1]:
                            index_list.append(index + i)
                except IndexError:
                    print("problem!!")
    for index, _ in enumerate(main_str):
        if index not in index_list and not _.isspace():
            return_str += _
    return return_str


r = sr.Recognizer()

audio = "start"
speech = ""

try:
    while "close" not in speech:
        with sr.Microphone() as source:
            print("Speak Now: ")
            audio = r.listen(source, 1)
        speech = r.recognize(audio)
        print(speech)
        time.sleep(0.5)
        if "open" in speech.lower():
            wb.open_new("www.{}.com".format(speech_cutter(speech, "open ")))
        elif "search" in speech.lower():
            if "youtube" in speech.lower():
                wb.open_new("https://www.youtube.com/results?search_query={}"
                            .format(speech_cutter(speech.lower(), "youtube search ")))
            if "twitter" in speech.lower():
                wb.open_new("https://twitter.com/search?q={}&src=typed_query"
                            .format(speech_cutter(speech.lower(), "twitter search ")))
            if "google" in speech.lower():
                wb.open_new("https://www.google.com/search?client=firefox-b-d&q={}"
                            .format(speech_cutter(speech.lower(), "google search ")))
        elif "university site" in speech.lower():
            manuel_link = input("<<<<İTÜ SITES ENTERS>>>>")
            wb.open_new("www.{}.itu.edu.tr".format(manuel_link))
        elif "quit" in speech.lower():
            break

        input("To say more thing press Enter: ")

except TimeoutError:
    print("You hadn't said anything!!!")
except LookupError:
    print("Did not understand what you said!!!")
