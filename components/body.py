from components.fileselecter import FileSelecter
from components.eventexe import EventExe
from flet import (
    Column,
    Text,
    Row,
    MainAxisAlignment,
    CrossAxisAlignment,
    Page,
    TextField,
)

class ContentBody(Column):
    
    def __init__(self, page: Page, text:str='Body Text'):
        super().__init__()
        self.page = page
        self.text = text
        self.spacing = 10
        self.file_path_display_1st = TextField(
            label = "File#1",
            hint_text = "ファイルを選択して下さい",
            value = "",
            read_only = True,
        )
        self.file_path_display_2nd = TextField(
            label = "File#2",
            hint_text = "ファイルを選択して下さい",
            value = "",
            read_only = True,
        )
        self.controls = [
            Text(self.text),
            Row(
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.START,
                controls=[self.file_path_display_1st, FileSelecter(self.page, self.file_path_display_1st)],
            ),
            Row(
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.START,
                controls=[self.file_path_display_2nd, FileSelecter(self.page, self.file_path_display_2nd)],
            ),
            Row(
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.START,
                controls=[EventExe(
                    self.page, 
                    self.file_path_display_1st, 
                    self.file_path_display_2nd,
                )]
            ),
        ]

