#-*- coding:utf-8 -*-
import requests
from lxml import etree
import pafy
import os
# need install youtube-dl

DOMAIN = 'https://www.youtube.com'

playlist = raw_input('Enter playlist link and press enter: ')
request = requests.get(playlist).content
main_tree = etree.HTML(request)
playlist_name = main_tree.xpath(
    './/h1[@class="pl-header-title"]/text()')[0].replace('\n', '').strip()
links = main_tree.xpath(
    './/table[@id="pl-video-table"]/tbody[@id="pl-load-more-destination"]/tr/td[@class="pl-video-title"]/a/@href')
folder = 'downloaded/%s' % (playlist_name)
try:
    os.makedirs(folder)
except:
    print 'Folder already exist.'
counter = 0
for link in links:
    counter += 1
    print counter, '\n'
    prepare_link = DOMAIN + link
    video = pafy.new(prepare_link)
    title = video.title
    filename = '%s/%s.mp4' % (folder, title)
    print title
    if os.path.isfile(filename):
        print 'File already exist!'
        continue
    else:
        best = video.getbest(preftype='mp4')
        best.download(filepath=folder)
print '\nDownload complete!'
