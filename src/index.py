import ffmpeg
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk
start_point =0
video_duration =0

def file_changed(filechooserbutton):
    video_file = filechooserbutton.get_filename()


def on_duration_entered(entry):
        video_duration = entry.get_text()
    

def on_start_of_video_entered(entry):
        start_point = entry.get_text()
        # return start_point

def on_btn_clicked(btn):
    on_duration_entered(gif_duration)
    print(video_duration)
   

window = Gtk.Window()
window.set_title("GIF-Maker")
window.set_default_size(250, 200)
window.connect("destroy", Gtk.main_quit)

btn=Gtk.Button(label="convert")
btn.connect("clicked", on_btn_clicked)
filechooserbutton = Gtk.FileChooserButton(title="FileChooserButton")
filechooserbutton.connect("file-set", file_changed)

filefilter = Gtk.FileFilter()
filefilter.set_name("Videos")
filefilter.add_pattern("*.mp4")
filefilter.add_pattern("*.avi")
# filefilter.add_pattern("*.bmp")
filechooserbutton.add_filter(filefilter)

gif_duration = Gtk.Entry()
gif_duration.set_placeholder_text("Enter GIF duration")
gif_duration.connect("activate", on_duration_entered)
     
start_of_gif = Gtk.Entry()
start_of_gif.set_placeholder_text("Enter the starting timestamp ")
start_of_gif.connect("activate", on_start_of_video_entered)

entry_box = Gtk.HBox(spacing=5)
entry_box.add(gif_duration)
entry_box.add(start_of_gif)


label = Gtk.Label()
label.set_text("Select a video file to convert to gif")
label.set_justify(Gtk.Justification.LEFT)
label.set_name('custom_label')

box = Gtk.VBox(spacing=6)
box.set_margin_left(80)
box.set_margin_right(80)
box.set_margin_top(50)
box.set_margin_bottom(30)
box.add(filechooserbutton)
box.add(entry_box)
box.add(btn)
box.add(label)

grid = Gtk.Grid()
grid.set_row_spacing(15)

window.add(box)
window.show_all()

Gtk.main()



# stream = ffmpeg.input("/home/abhishekmaurya/Projects/py-ffmpeg/src/test.mp4")
# stream = ffmpeg.trim(stream,start=77,end=79,duration=2)
# stream = ffmpeg.output(stream,'output.gif',video_bitrate=4500,f="gif")
# ffmpeg.run(stream)