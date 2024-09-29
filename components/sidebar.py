from flet import (
    alignment,
    border_radius,
    colors,
    Container,
    CrossAxisAlignment,
    FloatingActionButton,
    Icon,
    IconButton,
    icons,
    NavigationRail,
    NavigationRailDestination,
    NavigationRailLabelType,
    Row,
    Text,
    Page,
)

class Sidebar(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.page = page
        self.nav_rail_visible = True
        self.nav_rail_items = [
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
            NavigationRailDestination(
                icon=icons.RUN_CIRCLE_OUTLINED,
                selected_icon=icons.RUN_CIRCLE_OUTLINED,
                label="Tool#1"
            ),
            NavigationRailDestination(
                icon=icons.DIFFERENCE_OUTLINED,
                selected_icon=icons.DIFFERENCE_OUTLINED,
                label="Tool#2"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.HOME_OUTLINED),
                selected_icon_content=Icon(icons.HOME_OUTLINED),
                label="home"
            ),

        ]
        self.nav_rail = NavigationRail(
            height= 300,
            selected_index=None,
            # label_type=NavigationRailLabelType.ALL,
            # min_width=100,
            # min_extended_width=400,
            # leading=FloatingActionButton(icon=icons.CREATE, text="ADD"),
            # group_alignment=-0.9,
            destinations=self.nav_rail_items,
            on_change=self.tap_nav_icon,
        )
        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT,
            icon_color=colors.BLUE_GREY_400,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail,
            tooltip="Collapse Nav Bar",
        )
        self.visible = self.nav_rail_visible
        self.content = Row(
            controls=[
                self.nav_rail,
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=480,
                    alignment=alignment.center_right,
                    width=2
                ),
                self.toggle_nav_rail_button,
            ],
            vertical_alignment=CrossAxisAlignment.START,
        )

    def toggle_nav_rail(self, e):
        self.nav_rail.visible = not self.nav_rail.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.toggle_nav_rail_button.tooltip = "Open Side Bar" if self.toggle_nav_rail_button.selected else "Collapse Side Bar"
        self.update()

    def tap_nav_icon(self, e):
        if e.control.selected_index == 0:
            self.page.go('/Setting')
        elif e.control.selected_index == 1:
            self.page.go('/Tool_1')
        elif e.control.selected_index == 2:
            self.page.go('/Tool_2')
        else:
            self.page.go('/')