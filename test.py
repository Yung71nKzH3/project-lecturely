# import wx
# import datetime

# class NoteApp(wx.Frame):
#     def __init__(self, parent, title):
#         super(NoteApp, self).__init__(parent, title=title, size=(500, 400))

#         self.panel = wx.Panel(self)

#         # Create a text control for note input
#         self.note_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

#         # Create a button to save the note
#         self.save_button = wx.Button(self.panel, label="Save Note")
#         self.save_button.Bind(wx.EVT_BUTTON, self.save_note)

#         # Create a static text control to display the image
#         self.image_display = wx.StaticBitmap(self.panel)

#         # Create a list box to display previous notes
#         self.note_list = wx.TextCtrl(self.panel)

#         # Layout the controls
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.note_text, 1, wx.EXPAND)
#         sizer.Add(self.save_button, 0, wx.ALIGN_CENTER)
#         sizer.Add(self.image_display, 1, wx.ALIGN_CENTER)
#         sizer.Add(self.note_list, 1, wx.EXPAND)
#         self.panel.SetSizer(sizer)

#     def save_note(self, event):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         note_text = self.note_text.GetValue()
#         image_path = "image.jpg"  # Replace with your actual image path #Do it along with a screenshot button

#         # Save the note to a file
#         with open("notes.txt", "a") as f:
#             f.write(f"{timestamp}:{note_text}:{image_path}\n")

#         # Load the image
#         image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
#         image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
#         bitmap = wx.Bitmap(image)

#         # Display the image in the static bitmap control
#         self.image_display.SetBitmap(bitmap)

#         # Add the new note to the list box
#         self.note_list.Insert(f"{timestamp}: {note_text}", 0)

# if __name__ == "__main__":
#     app = wx.App()
#     frame = NoteApp(None, title="Note Taking App")
#     frame.Show()
#     app.MainLoop()

# import wx
# import datetime


# class NoteApp(wx.Frame):
#     def __init__(self, parent, title):
#         super(NoteApp, self).__init__(parent, title=title, size=(500, 400))

#         self.panel = wx.Panel(self)

#         # Create a text control for note input
#         self.note_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

#         # Create a button to save the note
#         self.save_button = wx.Button(self.panel, label="Save Note")
#         self.save_button.Bind(wx.EVT_BUTTON, self.save_note)  # Bind to self.save_note

#         # Create a static text control to display the image
#         self.image_display = wx.StaticBitmap(self.panel)

#         # Layout the controls
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.note_text, 1, wx.EXPAND)
#         sizer.Add(self.save_button, 0, wx.ALIGN_CENTER)
#         sizer.Add(self.image_display, 1, wx.ALIGN_CENTER)
#         self.panel.SetSizer(sizer)

#     def save_note(self, event):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         note_text = self.note_text.GetValue()
#         # Assuming you have the image path
#         image_path = "image.jpg"  # Replace with your actual image path

#         # Save the note to a file
#         with open("notes.txt", "a") as f:
#             f.write(f"{timestamp}:{note_text}:{image_path}\n")

#         # Display the image in the static bitmap control (Replace with your image loading logic)
#         # This part is not implemented yet, as loading images requires additional libraries
#         # image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
#         # bitmap = wx.Bitmap(image)
#         # self.image_display.SetBitmap(bitmap)


# if __name__ == "__main__":
#     app = wx.App()
#     frame = NoteApp(None, title="Note Taking App")
#     frame.Show()
#     app.MainLoop()

# import wx
# import datetime

# class NoteApp(wx.Panel):
#     def __init__(self, parent):
#         super().__init__(parent)

#         # ... (rest of your NoteApp code)

#         # Create a virtual list box
#         self.note_list = wx.ListCtrl(self, wx.LC_REPORT | wx.LC_VIRTUAL)
#         # self.note_list.InsertColumn(0, 'Note', width=400, wx.LIST_FORMAT_LEFT)

#         # Set the virtual list size based on the number of notes (replace with your data source)
#         self.notes = self.get_notes()  # Replace with function to get notes from storage
#         self.SetItemCount(len(self.notes))

#         # Bind event to handle drawing list items
#         self.note_list.Bind(wx.EVT_LIST_CACHE_HINT, self.on_cache_hint)

#     def get_notes(self):
#         # Implement logic to read notes from your storage (file, database)
#         # This is an example, replace with your actual implementation
#         notes = []
#         with open("notes.txt", "r") as f:
#             for line in f:
#                 timestamp, text, _ = line.strip().split(":")
#                 notes.append((timestamp, text))
#         return notes

#     def on_cache_hint(self, event):
#         # Get the index of the item to draw
#         index = event.GetCacheHint()

#         # Get the note text for the given index
#         timestamp, note_text = self.notes[index]

#         # Create a text control pre-filled with the note text
#         text_ctrl = wx.TextCtrl(self.note_list, style=wx.TE_MULTILINE | wx.TE_READONLY)
#         text_ctrl.SetValue(f"{timestamp}:\n{note_text}")

#         # Set the text control as the data for the list item
#         self.note_list.SetItemData(index, text_ctrl)

#     def save_note(self, event):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         note_text = self.note_text.GetValue()
#         image_path = "image.jpg"  # Replace with your actual image path

#         # Save the note to a file (replace with your storage logic)
#         with open("notes.txt", "a") as f:
#             f.write(f"{timestamp}:{note_text}:{image_path}\n")

#         self.note_text.Clear()

#         # Update the notes list and virtual list size
#         self.notes.append((timestamp, note_text))
#         self.SetItemCount(len(self.notes))

# if __name__ == "__main__":
#     app = wx.App()
#     frame = NoteApp(None, title="Note Taking App")
#     frame.Show()
#     app.MainLoop()

import wx
import cv2
import threading
import datetime


class VideoPanel(wx.Panel):

    def __init__(self, parent, video_source=0):
        super().__init__(parent)
        self.SetBackgroundColour('blue')

        self.is_active = True

        self.video_bitmap = wx.StaticBitmap(self)

        self.video_thread = threading.Thread(target=self.process_video, args=(video_source,))
        self.video_thread.start()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.video_bitmap, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_SIZE, self.OnSize)

    def process_video(self, video_source):
        try:
            cap = cv2.VideoCapture(video_source)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                wx_image = wx.Image(frame.shape[1], frame.shape[0], rgb_image)
                wx_bitmap = wx.Bitmap(wx_image)

                wx.CallAfter(self.update_bitmap, wx_bitmap)

        except Exception as e:
            print(f"Error capturing video: {e}")

    def update_bitmap(self, bitmap):
        if self.is_active:
            # Convert the bitmap to an image
            image = wx.ImageFromBitmap(bitmap)

            # Scale the image to the desired size
            image = image.Scale(self.GetSize()[0], self.GetSize()[1])

            # Create a new bitmap from the scaled image
            new_bitmap = wx.Bitmap(image)
            self.video_bitmap.SetBitmap(new_bitmap)

    def OnSize(self, event):
        self.update_bitmap(self.video_bitmap.GetBitmap())

    def Close(self, *args, **kwargs):
        if hasattr(self, 'video_panel'):
            self.video_panel.is_active = False  # Set flag here
        super().Close(*args, **kwargs)

class NoteApp(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
                
        self.panel = wx.Panel(self)

        # Create a text control for note input
        self.note_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        # Create a button to save the note
        self.save_button = wx.Button(self.panel, label="Save Note")
        self.save_button.Bind(wx.EVT_BUTTON, self.save_note)  # Bind to self.save_note

        # Create a static text control to display the image
        self.image_display = wx.StaticBitmap(self.panel)

        # Layout the controls
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.note_text, 1, wx.EXPAND)
        sizer.Add(self.save_button, 0, wx.ALIGN_CENTER)
        sizer.Add(self.image_display, 1, wx.ALIGN_CENTER)
        self.panel.SetSizer(sizer)

        # Create a virtual list box
        self.note_list = wx.ListCtrl(self, wx.LC_REPORT | wx.LC_VIRTUAL)
        # self.note_list.InsertColumn(0, 'Note', width=400, wx.LIST_FORMAT_LEFT)

        # Set the virtual list size based on the number of notes (replace with your data source)
        self.notes = self.get_notes()  # Replace with function to get notes from storage
        self.SetItemCount(len(self.notes))

        # Bind event to handle drawing list items
        self.note_list.Bind(wx.EVT_LIST_CACHE_HINT, self.on_cache_hint)

    def get_notes(self):
        # Implement logic to read notes from your storage (file, database)
        # This is an example, replace with your actual implementation
        notes = []
        with open("notes.txt", "r") as f:
            for line in f:
                timestamp, text, _ = line.strip().split(":")
                notes.append((timestamp, text))
        return notes

    def on_cache_hint(self, event):
        # Get the index of the item to draw
        index = event.GetCacheHint()

        # Get the note text for the given index
        timestamp, note_text = self.notes[index]

        # Create a text control pre-filled with the note text
        text_ctrl = wx.TextCtrl(self.note_list, style=wx.TE_MULTILINE | wx.TE_READONLY)
        text_ctrl.SetValue(f"{timestamp}:\n{note_text}")

        # Set the text control as the data for the list item
        self.note_list.SetItemData(index, text_ctrl)

    def save_note(self, event):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_text = self.note_text.GetValue()
        image_path = "image.jpg"  # Replace with your actual image path

        # Save the note to a file (replace with your storage logic)
        with open("notes.txt", "a") as f:
            f.write(f"{timestamp}:{note_text}:{image_path}\n")

        self.note_text.Clear()

        # Update the notes list and virtual list size
        self.notes.append((timestamp, note_text))
        self.SetItemCount(len(self.notes))

class RecordingWindow(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(1500, 800))

        main_panel = wx.Panel(self)
        self.SetMinSize((400, 300))

        video_panel = VideoPanel(main_panel)
        video_controls_panel = wx.Panel(main_panel)
        buttons_panel = wx.Panel(main_panel)
        notes_panel = NoteApp(main_panel)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.Add(video_panel, 4, wx.EXPAND)
        video_panel.SetMinSize((300, 200))

        left_sizer.Add(video_controls_panel, 1, wx.EXPAND)
        video_controls_panel.SetMinSize((300, 100))

        left_sizer.Add(buttons_panel, 2, wx.EXPAND)

        right_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer.Add(notes_panel, 1, wx.EXPAND)
        notes_panel.SetMinSize((100, 300))

        main_sizer.Add(left_sizer, 3, wx.EXPAND)
        main_sizer.Add(right_sizer, 1, wx.EXPAND)

        video_panel.SetBackgroundColour('black')
        video_controls_panel.SetBackgroundColour('red')
        buttons_panel.SetBackgroundColour('yellow')
        notes_panel.SetBackgroundColour('green')

        video_controls_panel = wx.StaticText(video_controls_panel, label="VIDEO VIEWER CONTROLS")
        buttons_panel = wx.StaticText(buttons_panel, label="BUTTONS")

        main_panel.SetSizer(main_sizer)
        self.Centre()


if __name__ == "__main__":
    app = wx.App()
    frame = RecordingWindow(None, title="Note Taking App")
    frame.Show()
    app.MainLoop()