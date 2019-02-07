from bs4 import BeautifulSoup


class SoupTest:
    def __init__(self, html_doc):
        self.html_doc = html_doc
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def soup_test(self):
        print('\n# prettify()')
        print('soup.prettify()\n', self.soup.prettify())
        print('soup.title\n', self.soup.title)
        print('soup.title.name\n', self.soup.title.name)
        print('soup.title.string\n', self.soup.title.string)
        print('soup.title.parent.name\n', self.soup.title.parent.name)
        # print('soup.p\n', self.soup.p)
        # print('soup.p["class"]\n', self.soup.p['class'])
        # print('soup.a\n', self.soup.a)
        # print('soup.find_all("a")\n', self.soup.find_all('a'))
        # print('soup.find(id="link3")\n', self.soup.find(id='link3'))
        # for link in self.soup.find_all('a'):
        #     print(link.get('href'))
        # print('\nsoup.get_text()\n', self.soup.get_text())


if __name__ == '__main__':
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    # st = SoupTest(html_doc)
    # st.soup_test()
    with open("index.html") as fp:
        st = SoupTest(fp)
        st.soup_test()



