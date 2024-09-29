from lib.exetool import ExeTool
from flet import (
    ElevatedButton,
    icons,
    Page,
    TextField
)

class EventExe(ElevatedButton):

    def __init__(self, page: Page, file_path_1st: TextField, file_path_2nd: TextField):
        super().__init__()
        self.page = page
        self.text = "実行"
        self.icon = icons.PLAY_CIRCLE
        self.file_path_1st = file_path_1st
        self.file_path_2nd = file_path_2nd
        self.on_click = self.exe_btn_clicked

    def exe_btn_clicked(self, e):
        if self.file_path_1st.value and self.file_path_2nd.value:
            ExeTool()
            self.page.update()
        else:
            pass  # 何もしない
