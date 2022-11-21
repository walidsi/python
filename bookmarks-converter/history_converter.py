import json

output_format = 'html'

HTML_START_BOILERPLATE = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
'''

HTML_END_BOILERPLATE = '</DL><p>'

CSV_START_BOILERPLATE = 'Link, Title\n'

topics = [
    {
        'name': 'psychology',
        'keywords': ['psychologytoday.com', 'psychology', 'mental health'],
        'filename': 'psychology'
    }, {
        'name': 'coding',
        'keywords': ['coding', 'code', 'programming', 'git'],
        'filename': 'coding'
    }, {
        'name': 'python',
        'keywords': ['python'],
        'filename': 'python'
    }, {
        'name': 'data science',
        'keywords': ['data science'],
        'filename': 'data-science'
    }, {
        'name': 'machine learning',
        'keywords': ['machine learning'],
        'filename': 'machine-learning'
    }
]


def found_topic_keyword(topic: dict, url: str, title: str) -> bool:
    found = False
    for keyword in topic['keywords']:
        if title.lower().find(keyword) >= 0:
            found = True
            break

    return found


def remove_duplicates(links: list) -> list:
    links_dict = {}

    for link in links:  # O(n)
        if link['url'] not in links_dict:
            links_dict[link['url']] = link['title']

    unique_links = []

    for url, title in links_dict.items():  # O(n)
        unique_links.append({'url': url, 'title': title})

    return unique_links  # total is O(2n) which is O(n)


def main():
    # Opening JSON file
    f = open('BrowserHistory.json', encoding='utf-8')
    data = json.load(f)
    f.close()

    history = data["Browser History"]

    for topic in topics:
        links = []

        for link in history:
            if found_topic_keyword(topic, link['url'], link['title']):
                links.append({'url': link['url'], 'title': link['title']})

        links = remove_duplicates(links)

        html = HTML_START_BOILERPLATE

        csv = CSV_START_BOILERPLATE

        for link in links:
            if output_format == 'html':
                out_link = '<DT><a href=\"{}">{}</a>\n'.format(link['url'], link['title'])
                html += out_link
            elif output_format == 'csv':
                csv += '{}, {}\n'.format(link['url'], link['title'])

        if output_format == 'html':
            f = open('./outputs/' + topic['filename'] + '.html', 'w', encoding='utf-8')
            html += HTML_END_BOILERPLATE
            f.write(html)
            f.close()
        elif output_format == 'csv':
            f = open('./outputs/' + topic['filename'] + '.csv', 'w', encoding='utf-8')
            f.write(csv)
            f.close()


if __name__ == "__main__":
    main()
