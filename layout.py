from components.body import ContentBody
from components.header import AppHeader
from components.sidebar import Sidebar
from flet import (
    CrossAxisAlignment,
    MainAxisAlignment,
    Row,
    Page,
    View,
)

class MyLayout(View):
    def __init__(self, page: Page, route='/'):
        super().__init__()
        self.page = page
        self.route = route
        if self.route=='/':
            self.page_title = 'Home'
        elif self.route=='/Setting':
            self.page_title = 'Setting'
        elif self.route=='/Tool_1':
            self.page_title = 'Tool#1'
        elif self.route=='/Tool_2':
            self.page_title = 'Tool#2'
        self.controls = [
            AppHeader(self.page, self.page_title.upper()),
            Row(
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.START,
                controls=[Sidebar(self.page),ContentBody(self.page, self.page_title.upper()+' Page')],
            ),
        ]