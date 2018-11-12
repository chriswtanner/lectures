import requests
from bs4 import BeautifulSoup

def main():

    # fetch items from online via the 'requests' library
    #url="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
    url="https://www.cnn.com"
    #url="https://www.npr.org/2018/11/05/664395755/what-if-the-polls-are-wrong-again-4-scenarios-for-what-might-happen-in-the-elect"
    response = requests.get(url)
    #print(response.content)

    # Beautiful Soup (library) time!
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    soup.prettify()
    #exit(1)
    # Q1: how do we get the title's text?
    #print(soup.title)

    # Q2: how do we get the webpage's entire content?
    #print(soup.get_text())
    links = soup.find_all('a', href=True)
    print(links)

if __name__ == '__main__':
    main()
