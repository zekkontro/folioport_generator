import errno
import os
import shutil
from bs4 import BeautifulSoup
import requests
from scraper import WebScraper

webScraper = WebScraper()
list = ["https://medium.com/tech-sheet/sosyal-m%C3%BChendislik-teoride-siber-g%C3%BCvenlik-89404688aef8"]


#webScraper.getGithubRepos(list)

#sendingBlogData = [
#    {
#        "cover_image_link": "https://miro.medium.com/v2/resize:fit:1200/format:webp/1*OnYuD2la9XRjveHFBt-3tg.jpeg",
#        "description" : "Hepinize merhabalar! Bence her küçüğe ya da gence “Hacker” kavramı çok çekici gelmiştir veya hepimiz illaki hayatımızın bir döneminde filmlerde, ekranda kayan o yeşil yazılara özenmişizdir. Ben de ortaokul dönemlerimde gerçekten bilişim sektörünün geneline çok meraklı bir çocuk olarak hacker olmayı isterdim. ",
#        "link" : "https://medium.com/tech-sheet/sosyal-m%C3%BChendislik-teoride-siber-g%C3%BCvenlik-89404688aef8",
#    }
#]
#ƒwebScraper.getMediumBlogs(sendingBlogData)

