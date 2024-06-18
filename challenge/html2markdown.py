import re

Italics = re.compile(r'<em>(.+?)</em>')
Spaces = re.compile(r'\s+')
Paragraphs = re.compile(r'<p>(.+?)</p>')
URLs = re.compile(r'<a href="(.+?)">(.+?)</a>')

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    markdown = Italics.sub(r'*\1*', html)
    markdown = Spaces.sub(r' ', markdown)
    markdown = Paragraphs.sub(r'\1\n\n', markdown)
    markdown = URLs.sub(r'[\2](\1)', markdown) # captures url and link
    return markdown.strip()