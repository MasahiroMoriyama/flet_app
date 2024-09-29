from views import MyView
from flet import (
    app,
    Page,
)

def main(page: Page):
    page.title = "Example Route"
    page.padding = 10

    MyView(page)

if __name__ == '__main__':
    app(target=main)