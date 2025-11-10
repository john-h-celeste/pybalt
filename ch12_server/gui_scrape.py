from tkinter import *
from tkinter import ttk,filedialog,messagebox
import base64
import json
from pathlib import Path

from bs4 import BeautifulSoup
import requests


config = {}


def fetch_url(fetch_cb):
    def fetch_url():
        url = _url.get()
        config['images'] = []
        _images.set(())  # initialised as an empty tuple
        try:
            page = requests.get(url)
        except requests.RequestException as err:
            sb(str(err))
        else:
            soup = BeautifulSoup(page.content, 'html.parser')
            images = fetch_cb(soup, url)
    return fetch_url


def fetch_images(soup, base_url):
    images = []
    for img in soup.findAll('img'):
        src = img.get('src')
        img_url = f'{base_url}/{src}'
        name = img_url.split('/')[-1]
        images.append(dict(name=name, url=img_url))
    if _save_method not in ['json', 'img']:
        save_method = ['img']
    _img_only_radio.configure(state = ACTIVE)
    _json_radio.configure(state = ACTIVE)
    _scrape_btn.configure(state = ACTIVE)
    if images:
        _images.set(tuple(img['name'] for img in images))
        sb('Images found: {}'.format(len(images)))
    else:
        sb('No images found')
    config['images'] = images
    config['type'] = 'images'


def fetch_title(soup, base_url):
    _save_method.set('')
    _img_only_radio.configure(state = DISABLED)
    _json_radio.configure(state = DISABLED)
    _scrape_btn.configure(state = DISABLED)
    sb('Title found: {}'.format(soup.find('title').string))


def fetch_links(soup, base_url):
    links = []
    for link in soup.findAll('a'):
        href = link.get('href')
        if not (href.startswith('http://') or href.startswith('https://')):
            continue
        if base_url in href:
            continue
        name = href.rstrip('/').split('/')[-1]
        links.append(dict(name=href, visiblename=name, url=href))
    if links:
        _images.set(tuple(link['visiblename'] for link in links))
        sb('Links found: {}'.format(len(links)))
    else:
        sb('No links found')
    _save_method.set('json')
    _img_only_radio.configure(state = DISABLED)
    _json_radio.configure(state = ACTIVE)
    _scrape_btn.configure(state = ACTIVE)
    config['images'] = links
    config['type'] = 'links'


def save():
    if not config.get('images'):
        alert('No {} to save'.format(config['type']))
        return

    if _save_method.get() == 'img':
        dirname = filedialog.askdirectory(mustexist=True)
        save_images(dirname)
    else:
        filename = filedialog.asksaveasfilename(
            initialfile='{}.json'.format(config['type']),
            filetypes=[('JSON', '.json')])
        save_json(filename)


def save_images(dirname):
    if dirname and config.get('images'):
        for img in config['images']:
            img_data = requests.get(img['url']).content
            filename = Path(dirname).joinpath(img['name'])
            with open(filename, 'wb') as f:
                f.write(img_data)
        alert('Done')


def save_json(filename):
    if filename and config.get('images'):
        data = {}
        for img in config['images']:
            img_data = requests.get(img['url']).content
            b64_img_data = base64.b64encode(img_data)
            str_img_data = b64_img_data.decode('utf-8')
            data[img['name']] = str_img_data

        with open(filename, 'w') as ijson:
            ijson.write(json.dumps(data))
        alert('Done')


def sb(msg):
    _status_msg.set(msg)


def alert(msg):
    messagebox.showinfo(message=msg)


if __name__ == "__main__": # execute logic if run directly
    _root = Tk() # instantiate instance of Tk class
    _root.title('bobby\'s cool web scraper 2000')
    _mainframe = ttk.Frame(_root, padding='5 5 5 5 ') # root is parent of frame
    _mainframe.grid(row=0, column=0, sticky=("E", "W", "N", "S")) # placed on first row,col of parent
    # frame can extend itself in all cardinal directions
    _url_frame = ttk.LabelFrame(
        _mainframe, text='URL', padding='5 5 5 5') # label frame
    _url_frame.grid(row=0, column=0, sticky=("E","W")) # only expands E W
    _url_frame.columnconfigure(0, weight=1)
    _url_frame.rowconfigure(0, weight=1) # behaves when resizing

    _url = StringVar()
    _url.set('http://localhost:8000') # sets initial value of _url
    _url_entry = ttk.Entry(
        _url_frame, width=40, textvariable=_url) # text box
    _url_entry.grid(row=1, column=0, sticky=(E, W, S, N), padx=5)
    _fetch_btn_1 = ttk.Button(
        _url_frame, text='Fetch info', command=fetch_url(fetch_images))
    _fetch_btn_1.grid(row=0, column=1, sticky=W, padx=5)
    _fetch_btn_2 = ttk.Button(
        _url_frame, text='Fetch title', command=fetch_url(fetch_title))
    _fetch_btn_2.grid(row=1, column=1, sticky=W, padx=5)
    _fetch_btn_3 = ttk.Button(
        _url_frame, text='Fetch links', command=fetch_url(fetch_links))
    _fetch_btn_3.grid(row=2, column=1, sticky=W, padx=5)

    # img_frame contains Listbox and Radio Frame
    _img_frame = ttk.LabelFrame(
        _mainframe, text='Content', padding='9 0 0 0')
    _img_frame.grid(row=1, column=0, sticky=(N, S, E, W))

    # Set _img_frame as parent of Listbox and _images is variable tied to
    _images = StringVar()
    _img_listbox = Listbox(
        _img_frame, listvariable=_images, height=6, width=25)
    _img_listbox.grid(row=0, column=0, sticky=(E, W), pady=5)
    #Scrollbar can move vertical
    _scrollbar = ttk.Scrollbar(
        _img_frame, orient=VERTICAL, command=_img_listbox.yview)
    _scrollbar.grid(row=0, column=1, sticky=(S, N), pady=6)
    _img_listbox.configure(yscrollcommand=_scrollbar.set)

    #Listbox occupies (0,0) on _img_frame.
    # Scrollbar occupies (0,1) so _radio_frame goes to (0,2)
    _radio_frame = ttk.Frame(_img_frame)
    _radio_frame.grid(row=0, column=2, sticky=(N, S, W, E))

    # place label and padding
    # radio buttons are children of _radio_frame
    _choice_lbl = ttk.Label(
        _radio_frame, text="Choose how to save")
    _choice_lbl.grid(row=0, column=0, padx=5, pady=5)
    _save_method = StringVar()
    _save_method.set('img')
    # Radiobutton connected to _save_method variable
    # Know which button is selected by checking value
    _img_only_radio = ttk.Radiobutton(
        _radio_frame, text='As Images', variable=_save_method,
        value='img')
    _img_only_radio.grid(row=1, column=0,padx=5, pady=2, sticky="W")
    _img_only_radio.configure(state='normal')
    _json_radio = ttk.Radiobutton(
        _radio_frame, text='As JSON', variable=_save_method,
        value='json')
    _json_radio.grid(row=2, column=0, padx=5, pady=2, sticky="W")

    # save command saves images to be listed in Listbox after parsing
    _scrape_btn = ttk.Button(
        _mainframe, text='Scrape!', command=save)
    _scrape_btn.grid(row=2, column=0, sticky=E, pady=5)

    _status_frame = ttk.Frame(
        _root, relief='sunken', padding='2 2 2 2')
    _status_frame.grid(row=1, column=0, sticky=("E", "W", "S"))
    _status_msg = StringVar() # need modified when update status text
    _status_msg.set('Tye a URL to start scraping...')
    _status= ttk.Label(
        _status_frame, textvariable=_status_msg, anchor=W)
    _status.grid(row=0, column=0, sticky=(E, W))

    _root.mainloop() # listens for events, blocks any code that comes after it

