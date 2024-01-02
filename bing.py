import ctypes, os, requests
from tkinter import messagebox

class BingAPI:

    def __init__(self):
        self.image_url = self.get_url()

    def get_url(self):
        base_url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
        response = requests.get(base_url)
        if response.status_code == 200:
            full_url = 'https://cn.bing.com' + response.json()['images'][0]['url']
        else: full_url = ''
        return full_url

    def process_download(self):
        if self.image_url != '':
            response = requests.get(self.image_url)
            if response.status_code == 200:
                with open('out.jpg', 'wb') as image_file:
                    image_file.write(response.content)
                return True
        return False

def set_wallpaper():
    ret = BingAPI().process_download()
    if ret:
        base_path = os.getcwd()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{base_path}\\out.jpg", 0)
        messagebox.showinfo('Done', ':)')
    else:
        messagebox.showerror('Error', 'An error occurred, try agin.')

set_wallpaper()