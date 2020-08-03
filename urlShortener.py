import pyshorteners

def eShortener(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

def eExpander(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.expand(url)

# url = input()
# print(f"\n{eShortener(url)}")

1
print("""Welcome to URL Shortener
Press 1 to shorten the URL
Press 2 to expand the URL.""")
n = int(input())
if n==1:
    url = input()
    print(f"\n{eShortener(url)}")
elif n==2:
    url = input()
    print(f"\n{eExpander(url)}")
else:
    print("Choose the correct option.")