import wx
import cv2
import threading

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


class RecordingWindow(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(1500, 800))

        main_panel = wx.Panel(self)
        self.SetMinSize((400, 300))

        video_panel = VideoPanel(main_panel)
        video_controls_panel = wx.Panel(main_panel)
        buttons_panel = wx.Panel(main_panel)
        notes_panel = wx.Panel(main_panel)

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

        video_panel.SetBackgroundColour('blue')
        video_controls_panel.SetBackgroundColour('red')
        buttons_panel.SetBackgroundColour('yellow')
        notes_panel.SetBackgroundColour('green')

        video_panel = wx.StaticText(video_panel, label="VIDEO VIEWER")
        video_controls_panel = wx.StaticText(video_controls_panel, label="VIDEO VIEWER CONTROLS")
        buttons_panel = wx.StaticText(buttons_panel, label="BUTTONS")
        notes_panel = wx.StaticText(notes_panel, label="NOTES")

        main_panel.SetSizer(main_sizer)
        self.Centre()

app = wx.App()
frame = RecordingWindow(None, "Recording Window")
frame.Show()
app.MainLoop()