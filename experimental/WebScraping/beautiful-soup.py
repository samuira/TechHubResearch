from bs4 import BeautifulSoup


class BeautifulSoupModified(BeautifulSoup):
    def __init__(self, *args, **kwargs):
        self.html_doc_m = kwargs['html_doc']

    def prettify_m(self, encoding=None, formatter="minimal"):
        pass


if __name__ == '__main__':
    pass
