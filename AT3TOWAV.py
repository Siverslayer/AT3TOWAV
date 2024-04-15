import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import subprocess

def convert_at3_to_wav(input_file, output_file):
    ffmpeg_path = "F:/AT9&AT3_Converter_V2.3/ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/AT3/ffmpeg.exe"
    
    if os.path.exists(output_file):
        os.remove(output_file)
    
    subprocess.run([ffmpeg_path, "-i", input_file, output_file])

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("AT3 Files", "*.at3")])
    root.destroy()
    return file_path

def main():
    input_file = select_file()
    if not input_file:
        print("لم يتم تحديد ملف.")
        return

    output_file = input_file[:-4] + ".wav"

    convert_at3_to_wav(input_file, output_file)
    print("تم التحويل بنجاح!")
    
if __name__ == "__main__":
    main()
