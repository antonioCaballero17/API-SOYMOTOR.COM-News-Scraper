from bs4 import Comment




def clear_html(soup):
    [x.decompose() for x in soup.findAll(lambda tag: not tag.contents and not tag.name == 'br' )]
    html_tag=soup
    for e in html_tag.find_all(True):
        e.attrs={}
    html_tag.attrs={}   
    for comment in html_tag.findAll(text=lambda text:isinstance(text, Comment)):
        comment.extract()
    return html_tag     