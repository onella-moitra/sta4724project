# I will not be editing v3, so will add my code segments and where to put them when finished!

#imports
import tkinter as tk
from threading import Thread

#this is the popup ftn: put above the iris detecter ftn
def show_popup(message="⚠ Please look at the camera!"):
    def popup():
        root = tk.Tk()
        root.title("Gentle Reminder 💭")  #this is my default, can be changed lol
        root.geometry("300x100")
        label = tk.Label(root, text=message, font=("Helvetica", 12), fg="red")
        label.pack(expand=True)
        root.after(3000, root.destroy)  # auto-close after 3 sec so it doesn’t get annoying
        root.mainloop()
    
    Thread(target=popup).start()  # run it in the background so it doesn’t freeze the video

#inside the iris detecter ftn possibly below the input of the video line
warning_count = 0  # keeps track of how long they look away
warning_limit = 15  # how many frames before we display the popup
warning_triggered = False  # prevents spammy popups

#after contours line
if contours:
    (x, y, w, h) = cv2.boundingRect(contours[0])
    center_x = x + w // 2
    center_y = y + h // 2

    roi_center_x = cols // 2
    roi_center_y = rows // 2

    offset_x = abs(center_x - roi_center_x)
    offset_y = abs(center_y - roi_center_y)

    # if the eye wanders too far from the center...
    if offset_x > cols * 0.25 or offset_y > rows * 0.25:
        warning_count += 1
    else:
        warning_count = 0
        warning_triggered = False  # reset if they come back to center

    if warning_count >= warning_limit and not warning_triggered:
        show_popup(" Please keep your eyes on the camera!")
        warning_triggered = True  # don't repeat until they fix it

    # draw the tracking visuals
    cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.line(roi, (center_x, 0), (center_x, rows), (0, 255, 0), 2)
    cv2.line(roi, (0, center_y), (cols, center_y), (0, 255, 0), 2)

else:
    # no eye detected at all, will display dif popup
    warning_count += 1
    if warning_count >= warning_limit and not warning_triggered:
        show_popup(" Can't find your eyes! Please look this way~")
        warning_triggered = True




