
# ............................Image Filter.............
# import cv2
# import cvzone
# bg = cv2.imread('jkr.png')
# sunglass = cv2.imread('star.png', cv2.IMREAD_UNCHANGED)
# final_image = cvzone.overlayPNG(bg, sunglass, [100,100])
# cv2.imshow('SnapChat Filtter', final_image)
# cv2.waitKey(0)

# ................Video Capture...................
# import cv2
# import cvzone
# capt = cv2.VideoCapture(0)
# while True:
#     _, frame = capt.read()
#     cv2.imshow('Snap Filtter',frame)
#     if cv2.waitKey(10) == ord('q'):
#         break

# ........................................Videoes Filtter(glases, face).......................
# import cv2
# import cvzone
# capt = cv2.VideoCapture(0)
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# overlay = cv2.imread('star.png',cv2.IMREAD_UNCHANGED)
# while True:
#     _, frame = capt.read()
#     gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces = cascade.detectMultiScale(gray_scale)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)   #2 = thickness
#         overlay_resize = cv2.resize(overlay, (w,h))
#         frame = cvzone.overlayPNG(frame,overlay_resize,[x,y])
#     cv2.imshow('Snap Filtter',frame)
#     if cv2.waitKey(10) == ord('q'):
#         break
#



# .....................................Videos Filtter  Face Mask.....................
# import cv2
# import cvzone
# capt = cv2.VideoCapture(0)
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# overlay = cv2.imread('mask.png',cv2.IMREAD_UNCHANGED)
# while True:
#     _, frame = capt.read()
#     gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces = cascade.detectMultiScale(gray_scale)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)   #2 = thickness
#         overlay_resize = cv2.resize(overlay, (int(w*1.5),int(h*1.5)))
#         frame = cvzone.overlayPNG(frame,overlay_resize,[x-45,y-75])
#     cv2.imshow('Snap Filtter',frame)
#     if cv2.waitKey(10) == ord('q'):
#         break


# ............................................For Queen..................
import cv2
import cvzone

capt = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('simple_queen.png', cv2.IMREAD_UNCHANGED)

while True:
    _, frame = capt.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (250, 250, 250), 2)   # 2 = thickness

        # Calculate the position for placing the overlay on the top of the head
        overlay_x = x + int(w * -0.09)  # Adjust these values based on your preference
        overlay_y = y - int(h * 0.8)

        overlay_resize = cv2.resize(overlay, (int(w * 1.1), int(h * 1.1)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [overlay_x, overlay_y])

    cv2.imshow('Snap Filtter', frame)

    if cv2.waitKey(10) == ord('q'):
        break



# .................................For Mask..........................
# import cv2
# import cvzone
#
# capt = cv2.VideoCapture(0)
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# overlay = cv2.imread('mask.png', cv2.IMREAD_UNCHANGED)
#
# while True:
#     _, frame = capt.read()
#     gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = cascade.detectMultiScale(gray_scale)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (250, 250, 250), 2)   # 2 = thickness
#
#         # Calculate the position for placing the overlay on the top of the head
#         overlay_x = x + int(w * -0.09)  # Adjust these values based on your preference
#         overlay_y = y - int(h * 0)
#
#         overlay_resize = cv2.resize(overlay, (int(w * 1.1), int(h * 1.1)))
#         frame = cvzone.overlayPNG(frame, overlay_resize, [overlay_x, overlay_y])
#
#     cv2.imshow('Snap Filtter', frame)
#
#     if cv2.waitKey(10) == ord('q'):
#         break
#




# ....................for flower...................
# import cv2
# import cvzone
#
# capt = cv2.VideoCapture(0)
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# overlay = cv2.imread('flower.png', cv2.IMREAD_UNCHANGED)
#
# while True:
#     _, frame = capt.read()
#     gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = cascade.detectMultiScale(gray_scale)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (250, 250, 250), 2)   # 2 = thickness
#
#         # Calculate the position for placing the overlay on the top of the head
#         overlay_x = x + int(w * -0.09)  # Adjust these values based on your preference
#         overlay_y = y - int(h * 0.49)
#
#         overlay_resize = cv2.resize(overlay, (int(w * 1.15), int(h * 1.15)))
#         frame = cvzone.overlayPNG(frame, overlay_resize, [overlay_x, overlay_y])
#
#     cv2.imshow('Snap Filtter', frame)
#
#     if cv2.waitKey(10) == ord('q'):
#         break
#


# ..................for lips.............
# import cv2
# import cvzone
#
# capt = cv2.VideoCapture(0)
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# overlay = cv2.imread('lips.png', cv2.IMREAD_UNCHANGED)
#
# while True:
#     _, frame = capt.read()
#     gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = cascade.detectMultiScale(gray_scale)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (250, 250, 250), 2)   # 2 = thickness
#
#         # Calculate the position for placing the overlay on the top of the head
#         overlay_x = x + int(w * 0.12)  # Adjust these values based on your preference
#         overlay_y = y - int(h * -0.6)
#
#         overlay_resize = cv2.resize(overlay, (int(w * 0.2), int(h * 0.15)))
#         frame = cvzone.overlayPNG(frame, overlay_resize, [overlay_x, overlay_y])
#
#     cv2.imshow('Snap Filtter', frame)
#
#     if cv2.waitKey(10) == ord('q'):
#         break






# ......................Youtube..............

# import os
# import threading
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox, filedialog, ttk
# from pytube import YouTube
#
# # Declare videoStream as a global variable
# videoStream = None
#
# def browse():
#     download_directory = filedialog.askdirectory(
#         initialdir="Your Directory path:", title='Save Video.'
#     )
#     download_path.set(download_directory)
#
# def download_callback():
#     global videoStream
#     try:
#         getVideo = YouTube(YouTube_Link)
#         videoStream = getVideo.streams.filter(res=quality).first()
#
#         # Configure the progress bar
#         progress_bar["maximum"] = int(videoStream.filesize)
#         progress_bar["value"] = 0
#
#         # Download the video
#         videoStream.download(download_folder)
#
#         messagebox.showinfo('SUCCESSFULLY', "Downloaded video in\n" + download_folder)
#     except Exception as e:
#         messagebox.showerror('ERROR', f"Error: {str(e)}")
#     finally:
#         # Reset the progress bar
#         progress_bar["value"] = 0
#
# def download():
#     global YouTube_Link, download_folder, quality
#     YouTube_Link = videolink.get()
#     download_folder = download_path.get()
#     quality = quality_combobox.get()
#
#     # Start a new thread for the download process
#     download_thread = threading.Thread(target=download_callback)
#     download_thread.start()
#
#     # Start updating the progress bar and percentage label periodically
#     root.after(100, update_progress)
#
# def update_progress():
#     global videoStream
#     if videoStream:
#         downloaded = videoStream.filepath.stat().st_size
#         total = videoStream.filesize
#         progress_percent = int((downloaded / total) * 100)
#         progress_label["text"] = f"Download Progress: {progress_percent}%"
#         progress_bar["value"] = downloaded
#         root.after(100, update_progress)
#     else:
#         progress_label["text"] = "Download Progress: 0%"
#         progress_bar["value"] = 0
#
# def widgets():
#     head_label = Label(root, text="YouTube Video Downloader by Divyansu👍",
#                        padx=15,
#                        pady=15,
#                        font='SegoeUI 14',
#                        background='palegreen2',
#                        fg='red')
#     head_label.grid(row=1,
#                     column=1,
#                     padx=5,
#                     pady=10,
#                     columnspan=3)
#     link_label = Label(root,
#                        text='Youtube Link: ',
#                        bg='salmon',
#                        pady=5,
#                        padx=5)
#     link_label.grid(row=2,
#                     column=0,
#                     pady=5,
#                     padx=5)
#     root.linkText = Entry(root,
#                           width=35,
#                           textvariable=videolink,
#                           font='Arial 14')
#     root.linkText.grid(row=2,
#                        column=1,
#                        columnspan=2,
#                        padx=5,
#                        pady=5)
#     destination_label = Label(root,
#                               text='Destination',
#                               bg='salmon',
#                               padx=5,
#                               pady=10)
#     destination_label.grid(row=3,
#                            column=0,
#                            pady=5,
#                            padx=5)
#
#     root.destinationText = Entry(root,
#                                  width=25,
#                                  textvariable=download_path,
#                                  font='Arial 14')
#     root.destinationText.grid(row=3,
#                               column=1,
#                               padx=5,
#                               pady=5)
#     browser_button = Button(root,
#                             text='Browse',
#                             command=browse,
#                             width=10,
#                             bg='red',
#                             relief=GROOVE)
#
#     browser_button.grid(row=3,
#                         column=2,
#                         pady=1,
#                         padx=1)
#
#     quality_label = Label(root,
#                           text='Select Quality:',
#                           bg='salmon',
#                           padx=5,
#                           pady=10)
#     quality_label.grid(row=4,
#                        column=0,
#                        pady=5,
#                        padx=5)
#
#     global quality_combobox
#     quality_combobox = ttk.Combobox(root, values=["1080p", "720p", "480p", "360p", "240p", "144p"])
#     quality_combobox.grid(row=4, column=1, padx=5, pady=5)
#     quality_combobox.set("144p")  # Default quality selection
#
#     global progress_label
#     progress_label = Label(root, text="Download Progress: 0%", bg='green2')
#     progress_label.grid(row=7, column=1, pady=10)
#
#     global progress_bar
#     progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
#     progress_bar.grid(row=6, column=1, pady=10)
#
#     download_button = Button(root,
#                              text='Download Video',
#                              command=download,
#                              width=20,
#                              bg='blue',
#                              padx=15,
#                              pady=10,
#                              relief=GROOVE,
#                              font='Georgia 13')
#     download_button.grid(row=5,
#                          column=1,
#                          padx=10,
#                          pady=10)
#
# root = tk.Tk()
# root.title("YouTube Videos Downloader BY--DIVYANSU VERMA❤️👍🥰😂")
# root.geometry("600x450")  # Adjusted the height to accommodate the progress bar
# root.resizable(False, False)
# root.config(background='green2')
#
# videolink = StringVar()
# download_path = StringVar()
#
# widgets()
#
# root.mainloop()
