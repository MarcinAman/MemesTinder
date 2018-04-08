import urllib.request

base_subdomain = "https://kwejk.pl/strona/"
base_domain = "https://kwejk.pl/"

current_page = "1"


class Image:
    def __init__(self, img_src, img_alt):
        self.src = img_src
        self.alt = img_alt


def get_page_html(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    return response.read()


def is_picture(element):
    return ".jpg" in element and "src" in element


def get_picture_from_html(html):
    splitted_html = html.split(" ")
    src = list(filter(is_picture, splitted_html))[0]

    alt_index_beg = html.index("\"",html.index("alt"))
    alt_index_end = html.index("\"",alt_index_beg+1)

    return Image(src[5:-1],html[alt_index_beg+1:alt_index_end])


def filter_images(server_html):
    server_array = server_html.decode().replace(">", "<").split("<")
    return [get_picture_from_html(i) for i in server_array if is_picture(i)]


def get_latest_page():
    request = get_page_html(base_domain).decode().split(" ")
    element_with_number = list(filter(lambda a: "https://kwejk.pl\">" in a, request))[-1]
    return list(filter(lambda a: a.isdigit(), element_with_number.replace("<", ">").split(">")))


def update_current_page():
    global current_page
    current_page = str(int(current_page) - 1)


def get_next_memes():
    current_url = base_subdomain + current_page
    update_current_page()
    current_html = get_page_html(current_url)
    return filter_images(current_html)


if __name__ == '__main__':
    current_page = get_latest_page()[0]
    for a in get_next_memes():
        print(a.src + " " +a.alt)
