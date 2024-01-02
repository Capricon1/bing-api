import ctypes
import os
import requests
from tkinter import messagebox

class DesktopBG:

    def get_url(self):
        base_url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
        response = requests.get(base_url)
        if response.status_code == 200:
            full_url = 'https://cn.bing.com' + response.json()['images'][0]['url']
        else: full_url = ''
        return full_url

    def process_download(self, image_url):
        if image_url != '':
            response = requests.get(image_url)
            if response.status_code == 200:
                with open('th.jpg', 'wb') as image_file:
                    image_file.write(response.content)
                return True
        return False

    def set_wallpaper(self):
        base_path = os.getcwd()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{base_path}\\th.jpg", 0)

    def run(self):
        url = self.get_url()
        ret = self.process_download(url)
        if ret == True:
            self.set_wallpaper()
            messagebox.showinfo('Done', ':)')
        else:
            messagebox.showerror('Error', 'An error occurred')

DesktopBG().run()
