def add_html(title):
    with open(f"test.html", "at") as f:
        f.write(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>{title}</title>\n</head>\n<body>\n<h1>This is {title}</h1>\n</body>\n</html>')

def rewrite_html(title):
    with open(f"test.html", "wt") as f:
        f.write(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>{title}</title>\n</head>\n<body>\n<h1>This is {title}</h1>\n</body>\n</html>')

def read_from_html(title):
    red_html= ""
    with open(f"{title}.html", "rt") as f:
        for line in f:
            if line.startswith("</body>"):
                pass
            elif line.startswith("</html>"):
                pass
            else:
                red_html += f'{line}'
    return red_html

def add_paragraph_with_header_to_html(title):   #needs test if html exists
    red_html = read_from_html(title)
    with open(f"test.html", "wt") as prepfile:
        prepfile.write(f"{red_html}")
    headline = input("please enter a headline for the paragraph")
    paragraph = input("please enter the paragraph")
    with open(f"test.html", "at") as f:
        f.write(f'\n<h2>{headline}</h2>\n<p>{paragraph}</p>\n</body>\n</html>')