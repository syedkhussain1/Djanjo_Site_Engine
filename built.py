print('Building a site - Execution begins')

pages = [
    {
        "input": "content/index.html",
        "output": "docs/index.html",
        "title": "About Me",
    },
    {
        "input": "content/project.html",
        "output": "docs/project.html",
        "title": "My Projects",
    },
    {
        "input": "content/blog.html",
        "output": "docs/blog.html",
        "title": "Travel Blog",
    }


]

def read_files():
    return open("templates/base.html").read()

def read_input(page):
    return open(page["input"]).read()

def final_merge(page, finished_index_page):
    return open(page["output"] , "w+").write(finished_index_page)


def main():

    #Loop around the page list
    for page in pages:
        #reading the template
        template = read_files()
         #reading the html pages
        final_content = read_input(page)
         #combining the base with content
        finished_index_page = template.replace("{{content}}", final_content)
        final_merge(page, finished_index_page)

print('Building a site - Execution ends')


if __name__ == "__main__":
    main()
