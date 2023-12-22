import re
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
def relative_uri(href):
    return re.compile('^https://').search(href) is None
url = 'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
news_section = soup.find('section', class_='section wrap-main-nav')
new_feed = news_section.find_all('a', class_='', href=relative_uri)
categories1 = ['Thời sự', 'Sức khỏe', 'Đời sống', 'Ý kiến']
categories2 = ['Thế giới', 'Kinh doanh', 'Khoa học', 'Giải trí', 'Thể thao', 'Pháp luật', 'Giáo dục', 'Xe', 'Thư giản']
cate4 = ['Bất động sản']
cate5 = ['Số hóa']
cate6 = ['Mới nhất']
data = []
visited_links = {}
for feed in new_feed:
    type = feed.get('title')
    # print(type)
    link = 'https://vnexpress.net' + feed.get('href')
    if type not in visited_links and not link.startswith('https://vnexpress.netjavascript:'):
        page = urllib.request.urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')
        for catego in cate6:
            section = soup.find('section', class_='section section_container mt20')
            if section is not None:
                new_feed_child = section.find_all('a', class_='')
                for news_feed_child in new_feed_child:
                    title_child = news_feed_child.get('title')
                    link_title = news_feed_child.get('href')
                    content_child = news_feed_child.text.strip()
                    if title_child not in visited_links and content_child not in visited_links and not link.startswith(
                            'javascript:') and title_child != content_child:
                        visited_links[title_child] = content_child
                        data.append([type, link, title_child, link_title, content_child])
    if type not in visited_links and not link.startswith('https://vnexpress.netjavascript:'):
        page = urllib.request.urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')

        for cate in cate4:
            section = soup.find('section', class_='section section_container mt15')
            if section is not None:
                new_feed_child = section.find_all('a', class_='')
                for news_feed_child in new_feed_child:
                    title_child = news_feed_child.get('title')
                    link_title = news_feed_child.get('href')
                    content_child = news_feed_child.text.strip()
                    if title_child not in visited_links and content_child not in visited_links and not link.startswith(
                            'javascript:') and title_child != content_child:
                        visited_links[title_child] = content_child
                        data.append([type, link, title_child, link_title, content_child])
    if type not in visited_links and not link.startswith('https://vnexpress.netjavascript:'):
        page = urllib.request.urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')

        for categ in cate5:
            section = soup.find('section', class_='section section_container')
            if section is not None:
                new_feed_child = section.find_all('a', class_='')
                for news_feed_child in new_feed_child:
                    title_child = news_feed_child.get('title')
                    link_title = news_feed_child.get('href')
                    content_child = news_feed_child.text.strip()
                    if title_child not in visited_links and content_child not in visited_links and not link.startswith(
                            'javascript:') and title_child != content_child:
                        visited_links[title_child] = content_child
                        data.append([type, link, title_child, link_title, content_child])
    if type not in visited_links and not link.startswith('https://vnexpress.netjavascript:'):
        page = urllib.request.urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')
        for category in categories1:
            section = soup.find('section', class_='section section_container section_topstory section_topstory_folder')
            if section is not None:
                new_feed_child = section.find_all('a', class_='')
                for news_feed_child in new_feed_child:
                    title_child = news_feed_child.get('title')
                    link_title = news_feed_child.get('href')
                    content_child = news_feed_child.text.strip()
                    if title_child not in visited_links and content_child not in visited_links and not link.startswith(
                            'javascript:') and title_child != content_child:
                        visited_links[title_child] = content_child
                        data.append([type, link, title_child, link_title, content_child])
    if type not in visited_links and not link.startswith('https://vnexpress.netjavascript:'):
        page = urllib.request.urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')
        for catego in categories2:
            section = soup.find('section', class_='section section_topstory section_topstory_folder')
            if section is not None:
                new_feed_child = section.find_all('a', class_='')
                for news_feed_child in new_feed_child:
                    title_child = news_feed_child.get('title')
                    link_title = news_feed_child.get('href')
                    content_child = news_feed_child.text.strip()
                    if title_child not in visited_links and content_child not in visited_links and not link.startswith(
                            'javascript:') and title_child != content_child:
                        visited_links[title_child] = content_child
                        data.append([type, link, title_child, link_title, content_child])
df = pd.DataFrame(data, columns=['Category', 'URL', 'Title', 'Link_Child', 'Content'])

link_child_by_category = {}
categories = df['Category'].unique()
for category in categories:
    filtered_links = df.loc[df['Category'] == category, 'Link_Child'].tolist()
    link_child_by_category[category] = filtered_links
data_child = []
for category, links_child in link_child_by_category.items():
    Type = (category)
    for link_child in links_child:
        if link_child.startswith('https://vnexpress.net'):
            page_p_tags = urllib.request.urlopen(link_child)
            soup_p_tags = BeautifulSoup(page_p_tags, 'html.parser')
            news_section_p_tags = soup_p_tags.find('section', class_='section page-detail top-detail')
            if news_section_p_tags is not None:
                new_feed_p_tags = news_section_p_tags.find_all('p', class_='Normal')
                content_p_tags = [para.text for para in new_feed_p_tags]
                for item_p_tags in content_p_tags:
                    Content_p_tags = item_p_tags
                    data_child.append([Type, link_child, Content_p_tags])
df = pd.DataFrame(data_child)
df.to_csv('final.csv', index=False)
