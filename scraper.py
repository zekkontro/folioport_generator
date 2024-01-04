import requests
from bs4 import BeautifulSoup


class WebScraper:
    def getGithubRepos(self, linkList ) -> dict:
        repoList = []
        for link in linkList:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            bordergrid_html_element = soup.select_one('.BorderGrid')
            # Star count
            star_icon_html_element = bordergrid_html_element.select_one('.octicon-star')
            stars_html_element = star_icon_html_element.find_next_sibling('strong')
            stars = stars_html_element.get_text().strip().replace(',', '')
            # Fork count
            fork_icon_html_element = bordergrid_html_element.select_one('.octicon-repo-forked')
            forks_html_element = fork_icon_html_element.find_next_sibling('strong')
            forks = forks_html_element.get_text().strip().replace(',', '')
            # Description
            about_html_element = bordergrid_html_element.select_one('h2')
            description_html_element = about_html_element.find_next_sibling('p')
            description = None if description_html_element == None else description_html_element.get_text().strip()
            # Primary language
            lang = soup.find("span", {"class": "color-fg-default text-bold mr-1"}).text
            # Title
            title_html_element = soup.select_one('[itemprop="name"]')
            title = title_html_element.text.strip()
            
            repoList.append( {
                "title" : title,
                "stars" : int(stars),
                "description" : description,
                "language" : lang,
                "url" : link,
                "forks" : int(forks)
            })

        return repoList

    def getMediumBlogs(self, blogData) -> dict:
        blogs = []
        for data in blogData:
            link = data['link']
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find("h1", {"data-testid" : "storyTitle"}).text
            readTime = soup.find("span", {"data-testid" : "storyReadTime"}).text
            publishDate = soup.find("span", {"data-testid" : "storyPublishDate"}).text

            blogs.append(
                {
                    "title" : title,
                    "readTime" : readTime,
                    "publishDate" : publishDate,
                    "link": link,
                    "cover_image_link" : data['cover_image_link'],
                    "description": data['description']
                }
            )

        return blogs            
                    
            






