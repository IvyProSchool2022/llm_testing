import os
from InquirerPy import inquirer
from scripts.youtube import youtube
from scripts.link import link, links, crawler
from scripts.substack import substack
from scripts.medium import medium
from scripts.gitbook import gitbook
from scripts.sitemap import sitemap
from scripts.twitter import twitter


def main():
    if os.name == "nt":  # Windows
        methods = {
            "1": "YouTube Channel",
            "2": "Article or Blog Link",
            "3": "Substack",
            "4": "Medium",
            "5": "Gitbook",
            "6": "Twitter",
            "7": "Sitemap",
        }
        print(
            "There are options for data collection to make this easier for you.\n"
            "Type the number of the method you wish to execute."
        )
        print(
            "1. YouTube Channel\n2. Article or Blog Link (Single)\n3. Substack\n"
            "4. Medium\n\n[In development]:\nTwitter\n\n"
        )
        selection = input("Your selection: ")
        method = methods.get(str(selection))
    else:  # Posix
        method = inquirer.select(
            message="What kind of data would you like to add to convert into long-term memory?",
            choices=[
                {"name": "YouTube Channel", "value": "YouTube Channel"},
                {"name": "Substack", "value": "Substack"},
                {"name": "Medium", "value": "Medium"},
                {"name": "Article or Blog Link(s)", "value": "Article or Blog Link(s)"},
                {"name": "Gitbook", "value": "Gitbook"},
                {"name": "Twitter", "value": "Twitter"},
                {"name": "Sitemap", "value": "Sitemap"},
                {"name": "Abort", "value": "Abort"},
            ],
        ).execute()

    if "Article or Blog Link" in method:
        method = inquirer.select(
            message="Do you want to scrape a single article/blog/url or many at once?",
            choices=[
                {"name": "Single URL", "value": "Single URL"},
                {"name": "Multiple URLs", "value": "Multiple URLs"},
                {"name": "URL Crawler", "value": "URL Crawler"},
                {"name": "Abort", "value": "Abort"},
            ],
        ).execute()
        if method == "Single URL":
            link()
            exit(0)
        if method == "Multiple URLs":
            links()
            exit(0)
        if method == "URL Crawler":
            crawler()
            exit(0)

    if method == "Abort":
        exit(0)
    if method == "YouTube Channel":
        youtube()
        exit(0)
    if method == "Substack":
        substack()
        exit(0)
    if method == "Medium":
        medium()
        exit(0)
    if method == "Gitbook":
        gitbook()
        exit(0)
    if method == "Sitemap":
        sitemap()
        exit(0)
    if method == "Twitter":
        twitter()
        exit(0)
    print("Selection was not valid.")
    exit(1)


if __name__ == "__main__":
    main()
