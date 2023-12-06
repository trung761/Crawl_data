import re
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
def relative_uri(href):
    return re.compile('^https://').search(href) is None
url = 'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
news_section = soup.find('section', class_='section wrap-main-nav')
new_feed = news_section.find_all('a', class_='', href=relative_uri)
categories1 = ['Thời sự', 'Sức khỏe', 'Đời sống', 'Ý kiến']
categories2 = ['Thế giới', 'Kinh doanh', 'Khoa học', 'Giải trí', 'Thể thao', 'Pháp luật', 'Giáo dục', 'Xe']
cate4 = ['Bất động sản']
cate5 = ['Số hóa']
data = []
visited_links = {}
for feed in new_feed:
    type = feed.get('title')
    link = 'https://vnexpress.net' + feed.get('href')
    if type == 'Mới nhất' and link == 'https://vnexpress.net/tin-tuc-24h':
        if type not in visited_links and not link.startswith('https://vnexpress.netjavascript:'):
            Page_Child = urllib.request.urlopen(link)
            soup_Child = BeautifulSoup(Page_Child, 'html.parser')
            Secsion_Child = soup_Child.find('section',
                                    class_='section section_container mt20')
            new_feed_Child = Secsion_Child.find_all('a', class_='')
            data = []
            visited_links = {}
            for News_feed_Child in new_feed_Child:
                Title_Child = News_feed_Child.get('title')
                Link_Title = News_feed_Child.get('href')
                Content_Child = News_feed_Child.text.strip()
                if Title_Child not in visited_links and Content_Child not in visited_links and not link.startswith(
                        'javascript:') and Title_Child != Content_Child:
                    visited_links[Title_Child] = Content_Child
                    data.append([type, link, Title_Child, Link_Title, Content_Child])
    if type not in visited_links and not link.startswith('https://vnexpress.netjavascript:'):
        page = urllib.request.urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')
        section = soup.find('section', class_='section section_container mt15')
        for cate in cate4:
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
        section = soup.find('section', class_='section section_container')
        for categ in cate5:
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
        section = soup.find('section', class_='section section_container section_topstory section_topstory_folder')
        for category in categories1:
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
        section = soup.find('section', class_='section section_topstory section_topstory_folder')
        for catego in categories2:
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
