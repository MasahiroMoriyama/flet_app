from flet import (
    ElevatedButton,
    icons,
    FilePicker,
    FilePickerResultEvent,
    Page,
    TextField
)

class FileSelecter(ElevatedButton):

    def __init__(self, page: Page, file_path_value: TextField):
        super().__init__()
        self.page = page
        self.text = "ファイル選択"
        self.icon = icons.FILE_OPEN
        self.file_path_value = file_path_value
        self.file_picker = FilePicker(
            on_result=self.pick_files_result
        )
        self.on_click = self.file_picker.pick_files
        self.page.overlay.append(self.file_picker)

    def pick_files_result(self, e: FilePickerResultEvent):
        if e.files:  # ファイルが選択された場合
            # ファイルパスを表示
            self.file_path_value.value = e.files[0].path
            print("file_path_value in pick_files_result=",self.file_path_value.value)
            self.page.update()
        else:  # ファイルを選択せず「キャンセル」でダイアログを閉じた場合
            pass  # 何もしない

        

