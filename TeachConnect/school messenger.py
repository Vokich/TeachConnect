from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem, ThreeLineIconListItem, IconLeftWidget

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"



Screen:

    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            Screen:
                name: 'login_screen'

                MDLabel:
                    text: "Вход"
                    color: (0.5, 0.5, 0.5, 1)
                    font_size: 45
                    pos_hint: {'center_x': 0.95, 'center_y':.7}
                    font_name: 'font_text1.ttf'

                MDTextField:
                    id: name
                    hint_text: "Name"
                    mode: "round"
                    max_text_length: 15
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: None
                    width: '250dp'

                MDTextField:
                    id: password
                    hint_text: "Password"
                    mode: "round"
                    max_text_length: 15
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    size_hint_x: None
                    width: '250dp'

                MDRaisedButton:
                    text: 'Войти'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_release: 
                        app.save_data()
                        app.back_to_home()   

            Screen:
                name: 'home_screen'

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Приложение"
                        md_bg_color: 87/255, 176/255, 255/255, 1
                        specific_text_color: 1, 1, 1, 1
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    MDBottomNavigation:

                        MDBottomNavigationItem:
                            name: 'contact'
                            text: 'Контакты'
                            icon: 'images/contact.png'

                            ScrollView:
                                MDList:
                                    id: container1                                 

                        MDBottomNavigationItem:
                            name: 'profile'
                            text: 'Профиль'
                            icon: 'images/profile.png'

                            MDIconButton:
                                icon: 'images/profile100.png'
                                icon_size: '100sp'
                                pos_hint: {'x':0.42, 'y':.65}

                            MDFillRoundFlatButton:
                                text: 'настройки'
                                pos_hint: {'x':.25, 'y':.45}
                                size_hint: 0.5, 0
                                on_release: app.show_settings()

                            MDFillRoundFlatButton:
                                text: 'о проекте'
                                pos_hint: {'x':.25, 'y':.3}
                                size_hint: 0.5, 0
                                on_release: app.show_project()

                            MDLabel:
                                text: name.text
                                pos_hint: {'x':.4, 'y':.1}
                                color: (0.5, 0.5, 0.5, 1)
                                font_size: 45
                                font_name: 'font_text1.ttf'

                        MDBottomNavigationItem:
                            name: 'calls'
                            text: 'Звонки'
                            icon: 'images/phone.png'

                            ScrollView:
                                MDList:
                                    id: container

                        MDBottomNavigationItem:
                            name: 'classes'
                            text: 'Классы'
                            icon: 'images/scholl.png'

                            MDLabel:
                                text: 'Ваш класс: 6Б'
                                color: (0.5, 0.5, 0.5, 1)
                                font_size: 45
                                pos_hint: {'x':.35, 'y':.4}
                                font_name: 'font_text1.ttf'

                            MDLabel:
                                text: 'Кол-во учеников: 30'
                                color: (0.5, 0.5, 0.5, 1)
                                pos_hint: {'x':.25, 'y':.2}
                                font_name: 'font_text1.ttf'

                            MDLabel:
                                text: 'Классный руководитель: Татьяна Вячеславовна'
                                color: (0.5, 0.5, 0.5, 1)
                                pos_hint: {'x':.25, 'y':.1}
                                font_name: 'font_text1.ttf'

                            MDLabel:
                                text: 'Кабинет классного руководителя: 204'
                                color: (0.5, 0.5, 0.5, 1)
                                pos_hint: {'x':.25, 'y':0}
                                font_name: 'font_text1.ttf'

                            MDLabel:
                                text: 'Предмет классного руководителя: Физика/Математика'
                                color: (0.5, 0.5, 0.5, 1)
                                pos_hint: {'x':.25, 'y':-.1}
                                font_name: 'font_text1.ttf'


            Screen:
                name: 'lessons_screen'

                MDLabel:
                    text: 'Расписание уроков'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {"x": .3, "y": .3}
                    font_size: 35
                    font_name: 'font_text1.ttf'

                MDLabel:
                    text: 'Понедельник:\\n Биология.\\n Русский язык.\\n Математика.\\n Родной язык.\\n Технология.'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {"x": .01, "y": 0}
                    font_name: 'font_text1.ttf'

                MDLabel:
                    text: 'Вторник:\\n Английский.\\n Математика.\\n Русский язык.\\n Русский язык.\\n Литература.'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {"x": .2, "y": 0}
                    font_name: 'font_text1.ttf'

                MDLabel:
                    text: 'Среда:\\n Математика.\\n Русский язык.\\n История.\\n Физкультура.\\n Родной язык.'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {"x": .4, "y": 0}
                    font_name: 'font_text1.ttf'

                MDLabel:
                    text: 'Четверг:\\n Обществознан.\\n Биология.\\n Математика.\\n Родной язык.\\n Музыка.'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {"x": .6, "y": 0}
                    font_name: 'font_text1.ttf'

                MDLabel:
                    text: 'Пятница:\\n География.\\n Русский язык.\\n ИЗО.\\n Родной язык.\\n Математика.'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {"x": .8, "y": 0}
                    font_name: 'font_text1.ttf'

                MDRaisedButton:
                    text: 'выйти'
                    md_bg_color: "red"
                    on_release: app.back_to_home()
                    pos_hint: {'x': 0.9, 'y': 0.9}
                    font_name: 'font_text1.ttf'

            Screen:
                name: 'teacher_screen'

                ScrollView:
                    MDList:
                        id: teacher

                MDRaisedButton:
                    text: 'Выйти'
                    md_bg_color: "red"
                    on_release: app.back_to_home()
                    pos_hint: {'x': 0.9, 'y': 0.9}
                    font_name: 'font_text1.ttf'

            Screen:
                name:'settings_screen'

                MDLabel:
                    text: 'Темный режим:'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {'x': .09, 'y': .01}
                    font_name: 'font_text1.ttf'

                MDSwitch:
                    pos_hint: {'x': .27, 'y': .466}
                    widget_style: "ios"
                    active: False
                    on_active: app.on_switch_active(self)

                MDLabel:
                    text: 'Размер шрифта:'
                    color: (0.5, 0.5, 0.5, 1)
                    pos_hint: {'x':.5, 'y':.01}
                    font_name: 'font_text1.ttf'

                MDSlider:
                    id: slider
                    hint: True
                    size_hint_x: None
                    width: '150dp'
                    value: 6
                    max: 10
                    hint_text_color: 'white'
                    hint_bg_color: (.2, .2, 2, 1)
                    pos_hint: {'x':.7, 'y':.01}
                    on_value: app.change_font_size(args[-1])

                MDRaisedButton:
                    text: 'Выйти'
                    md_bg_color: "red"
                    on_release: app.back_to_home()
                    pos_hint: {'x': 0.9, 'y': 0.9}
                    font_name: 'font_text1.ttf'

            Screen:
                name: 'school_screen'

                GridLayout:
                    cols: 3

                    MDSmartTile:
                        radius: 24
                        box_radius: [0, 0, 24, 24]
                        box_color: 1, 1, 1, .2
                        source: 'images/school1.jpg'
                        size_hint: None, None
                        size: "220dp", "220dp"
                        MDLabel:
                            text: "День в память жертв Холокоста"
                            bold: True
                            color: 1, 1, 1, 1

                    MDSmartTile:
                        radius: 24
                        box_radius: [0, 0, 24, 24]
                        box_color: 1, 1, 1, .2
                        source: 'images/school2.jpg'
                        size_hint: None, None
                        size: "220dp", "220dp"
                        MDLabel:
                            text: "Загадки"
                            bold: True
                            color: 1, 1, 1, 1

                    MDSmartTile:
                        radius: 24
                        box_radius: [0, 0, 24, 24]
                        box_color: 1, 1, 1, .2
                        source: 'images/school3.jpg'
                        size_hint: None, None
                        size: "220dp", "220dp"
                        MDLabel:
                            text: "#СпасибоУчителям"
                            bold: True
                            color: 1, 1, 1, 1

                    MDSmartTile:
                        radius: 24
                        box_radius: [0, 0, 24, 24]
                        box_color: 1, 1, 1, .2
                        source: 'images/school4.jpg'
                        size_hint: None, None
                        size: "220dp", "220dp"
                        MDLabel:
                            text: "1 сентября!"
                            bold: True
                            color: 1, 1, 1, 1

                    MDSmartTile:
                        radius: 24
                        box_radius: [0, 0, 24, 24]
                        box_color: 1, 1, 1, .2
                        source: 'images/school5.jpg'
                        size_hint: None, None
                        size: "220dp", "220dp"
                        MDLabel:
                            text: "9 мая!"
                            bold: True
                            color: 1, 1, 1, 1

                MDRaisedButton:
                    text: 'Выйти'
                    md_bg_color: "red"
                    on_release: app.back_to_home()
                    pos_hint: {'x': 0.9, 'y': 0.9}
                    font_name: 'font_text1.ttf'

            Screen:
                name: 'project_screen'
                MDLabel:
                    text: 'Контакты разработчика: 7-999-999-99-99, nothing@gmail.com'
                    halign: 'center'
                    color: (0.5, 0.5, 0.5, 1)
                    font_name: 'font_text1.ttf'

                MDRaisedButton:
                    text: 'Выйти'
                    md_bg_color: "red"
                    on_release: app.back_to_home()
                    pos_hint: {'x': 0.9, 'y': 0.9}
                    font_name: 'font_text1.ttf'


        MDNavigationDrawer:
            id: nav_drawer

            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title: "TeachConnect"
                    title_color: 87/255, 176/255, 255/255, 1
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp" 

                MDFillRoundFlatButton:
                    text: "Домашнее задание"
                    md_bg_color: 87/255, 176/255, 255/255, 1
                    pos_hint: {'x': 1, 'y':-1.5}
                    on_release: app.homework(self)

                MDFillRoundFlatButton:
                    text: "Звонки"
                    md_bg_color: 87/255, 176/255, 255/255, 1
                    pos_hint: {'x': -1, 'y':-4}
                    on_release: app.subjects(self)

                MDFillRoundFlatButton:
                    text: "Уроки"
                    md_bg_color: 87/255, 176/255, 255/255, 1
                    pos_hint: {'x': -1, 'y':-4}
                    on_release: app.open_lessons_screen()
                MDFillRoundFlatButton:
                    text: "Учителя"
                    md_bg_color: 87/255, 176/255, 255/255, 1
                    pos_hint: {'x': -1, 'y':-4}
                    on_release:
                        app.descrip_teaсh()
                        app.auto_teacher()
                MDFillRoundFlatButton:
                    text: "Галерея"
                    md_bg_color: 87/255, 176/255, 255/255, 1
                    pos_hint: {'x': -1, 'y':-4}
                    on_release: app.show_school()




'''


class MyOneLineListItem(OneLineListItem):
    default_text = StringProperty()
    font_size = NumericProperty()
    font_name = StringProperty()

    def _create_text(self):
        font = f"[font={self.font_name}]"
        size = f"[size={15 + self.font_size}]"

        self.text = f"{font}{size}{self.default_text}[/size][/font]"

    def on_default_text(self, *_args):
        self._create_text()

    def on_font_size(self, *_args):
        self._create_text()

    def on_font_name(self, *_args):
        self._create_text()


class MyThreeLineIconListItem(ThreeLineIconListItem):
    default_text_one = StringProperty()
    default_text_two = StringProperty()
    default_text_three = StringProperty()
    font_size = NumericProperty()
    font_name = StringProperty("Roboto")

    def _create_text(self):
        font = f"[font={self.font_name}]"
        size = f"[size={15 + self.font_size}]"

        self.text = f"{font}{size}{self.default_text_one}[/size][/font]"
        self.secondary_text = f"{font}{size}{self.default_text_two}[/size][/font]"
        self.tertiary_text = f"{font}{size}{self.default_text_three}[/size][/font]"

    def on_default_text_one(self, *_args):
        self._create_text()

    def on_default_text_two(self, *_args):
        self._create_text()

    def on_default_text_three(self, *_args):
        self._create_text()

    def on_font_size(self, *_args):
        self._create_text()

    def on_font_name(self, *_args):
        self._create_text()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class SchoolMessenger(MDApp):  # класс приложения
    def build(self):  # функция для создания приложения и его запуска
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"
        # layout = BoxLayout()
        # bg_image = Image(source='bg.png', allow_stretch=True, keep_ratio=False)
        # layout.add_widget(bg_image)
        return Builder.load_string(KV)

    def on_start(self):  # цикл для создания пользователей
        font_size = int(self.root.ids.slider.value)
        w = 0
        for i in range(10):
            w += 1
            item = MyOneLineListItem(default_text=f"Контакт {w}", on_release=self.show_dialog,
                                     theme_text_color="Custom", text_color=(0.5, 0.5, 0.5, 1),
                                     font_name='Roboto',
                                     font_size=font_size)  # Использование значения слайдера для размера шрифта
            self.root.ids.container.add_widget(item)

            item2 = MyOneLineListItem(default_text=f"Пользователь {w}", on_release=self.show_dialog,
                                      theme_text_color="Custom", text_color=(0.5, 0.5, 0.5, 1),
                                      font_name='Roboto',
                                      font_size=font_size)  # Использование значения слайдера для размера шрифта
            self.root.ids.container1.add_widget(item2)

    def on_switch_active(self, checkbox):  # функция для переключения темы приложения на dark или light
        if checkbox.active:
            self.theme_cls.theme_style = "Dark"
            font_size = int(self.root.ids.slider.value)  # Получение значения слайдера
            for child in self.root.ids.container.children:
                child.font_size = font_size  # Изменение размера шрифта текста
            for child in self.root.ids.container1.children:
                child.font_size = font_size  # Изменение размера шрифта текста
        else:
            self.theme_cls.theme_style = "Light"
            font_size = int(self.root.ids.slider.value)  # Получение значения слайдера
            for child in self.root.ids.container.children:
                child.font_size = font_size  # Изменение размера шрифта текста
            for child in self.root.ids.container1.children:
                child.font_size = font_size  # Изменение размера шрифта текста

    def show_dialog(self, instance):  # функция для отображения диалогового окна
        dialog = MDDialog(
            title="Звонок!",
            text="Вы собираетесь звонить этому человеку?",
            buttons=[
                MDFlatButton(
                    text="НET", text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: dialog.dismiss()
                ),
                MDFlatButton(
                    text="ДA", text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    def homework(self, instance):  # функция для отображения диалогового окна для домашней работы
        dialog1 = MDDialog(
            title="Домашная работа",
            text="ДЗ на завтра: нету",
            buttons=[
                MDFlatButton(
                    text='OK', text_color=self.theme_cls.primary_color,
                    on_release=lambda *args: dialog1.dismiss()
                ),
            ],
        )
        dialog1.open()

    def subjects(self, instance):  # функция для отображения диалогового окна для уроков
        dialog2 = MDDialog(
            title="Расписание звонков",
            text="1 урок: 8.00 - 8.40\n2 урок: 8.55 - 09.35\n3 урок: 09.55 - 10-35\n4 урок: 10.55 - 11.35"
                 "\n5 урок: 11.50 - 12.30\n6 урок: 12.45 - 13.25\n7 урок: 13.35 - 14.15\n8 урок: 14.25 - 15.05",
            buttons=[
                MDFlatButton(text='OK', text_color=self.theme_cls.primary_color,
                             on_release=lambda *args: dialog2.dismiss()),
            ],
        )
        dialog2.open()

    def open_lessons_screen(self):
        self.root.ids.screen_manager.current = 'lessons_screen'

    def back_to_home(self):
        self.root.ids.screen_manager.current = 'home_screen'

    def descrip_teaсh(self):
        self.root.ids.screen_manager.current = 'teacher_screen'

    def show_settings(self):
        self.root.ids.screen_manager.current = 'settings_screen'

    def show_school(self):
        self.root.ids.screen_manager.current = 'school_screen'

    def show_project(self):
        self.root.ids.screen_manager.current = 'project_screen'

    def auto_teacher(self):
        font_size = int(self.root.ids.slider.value)
        q = 0
        for i in range(10):
            q += 1
            item1 = MyThreeLineIconListItem(IconLeftWidget(icon="images/profile1.png"),
                                            default_text_one=f"Учитель {q}",
                                            default_text_two="Фамилия",
                                            default_text_three="Имя",
                                            font_size=font_size,
                                            text_color=(0.5, 0.5, 0.5, 1))
            self.root.ids.teacher.add_widget(item1)

    def save_data(self):  # функция для сохранения данных пользователя
        nickname = self.root.ids.name
        pass_word = self.root.ids.password
        nick_saved = nickname.text
        password_saved = pass_word.text
        print(nick_saved, password_saved)

    def change_font_size(self, value):  # функция для изменения размера шрифта
        for item in self.root.ids.container.children:
            item.font_size = int(value)

        for item in self.root.ids.container1.children:
            item.font_size = int(value)


if __name__ == '__main__':  # запуск приложения
    SchoolMessenger().run()
