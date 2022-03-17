import tkinter
import urllib.request

window = tkinter.Tk()
resolution = "300x100"  # changing this may cause the button & text positions to break
window.geometry(resolution)
window.resizable(0, 0)

input = tkinter.Entry(window)
input.pack()
input.place(relx=0.5, rely=0.5, anchor="center")

enter_text = tkinter.Label(window, text="Enter URL:")
enter_text.pack()
enter_text.place(relx=0.5, rely=0.2, anchor="center")


def execute():
    if input.get().__contains__('bigbluebutton/presentation') and input.get().endswith('svg/'):
        number = 1
        downloading = 1
        processing_text = tkinter.Label(window, text="Downloading...")
        processing_text.pack()
        processing_text.place(relx=0.5, rely=0.8, anchor="center")
        while downloading:
            try:
                processing_text = tkinter.Label(window, text="Downloading...")
                urllib.request.urlretrieve(
                    input.get() + str(number), "slide" + str(number) + ".svg")
                number += 1
            except:
                downloading = 0
                processing_text = tkinter.Label(
                    window, text="Download complete.")
                processing_text.place(relx=0.5, rely=0.8, anchor="center")
                break

    else:
        error_text = tkinter.Label(window, text="Invalid URL")
        error_text.pack()
        error_text.place(relx=0.5, rely=0.8, anchor="center")


button_execute = tkinter.Button(window, text="Start", command=execute)
button_execute.pack()
button_execute.place(relx=0.8, rely=0.5, anchor="center")

window.mainloop()  # display the gui