from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import os

class main(App):

    def save_doc(a):
        save_popup.dismiss()
        pass

    def close_doc(a):
        close_popup.dismiss()
        main().stop()
        pass

    def save_popup(self):
        s = BoxLayout(orientation='vertical')
        global save_popup
        save_popup = Popup(title=title+'.txt', size_hint=(None, None), size=(400, 200), auto_dismiss=False)
        saved = Label(text='To the path:')
        loc = TextInput(text=title + '.txt', multiline=False)
        sve_btn = Button(text='Save')
        sve_btn.bind(on_release=main.save_doc)
        cls_btn = Button(text='Cancel')
        cls_btn.bind(on_release=save_popup.dismiss)
        sve = BoxLayout(orientation='horizontal')
        sve.add_widget(sve_btn)
        sve.add_widget(cls_btn)
        s.add_widget(saved)
        s.add_widget(loc)
        s.add_widget(sve)
        save_popup.add_widget(s)
        save_popup.open()

    def close_popup(self):
        c = BoxLayout(orientation='vertical')
        d = BoxLayout(orientation='horizontal')
        global close_popup
        close_popup = Popup(title='Close', size_hint=(None, None), size=(400, 200), auto_dismiss=False)
        closed = Label(text='Are you sure?')
        loc = Label(text='')
        cl_btn = Button(text='Cancel')
        cl_btn.bind(on_release=close_popup.dismiss)
        cls_btn = Button(text='Yes')
        cls_btn.bind(on_release=main.close_doc)
        d.add_widget(cls_btn)
        d.add_widget(cl_btn)
        c.add_widget(closed)
        c.add_widget(loc)
        c.add_widget(d)
        close_popup.add_widget(c)
        close_popup.open()

    def build(self):
        global title
        title = 'untitled'
        head = BoxLayout (orientation='horizontal', size_hint=(1, .05))
        save_btn = Button(text='S', size_hint=(.1, 1))
        save_btn.bind(on_release=main.save_popup)
        close_btn = Button(text='C', size_hint=(.1, 1))
        close_btn.bind(on_release=main.close_popup)
        doc_title = Label(text=title+'.txt', size_hint=(.8, 1))
        head.add_widget(doc_title)
        head.add_widget(save_btn)
        head.add_widget(close_btn)
        txt_input = TextInput(scroll_x=1, size_hint=(1, .8))
        content = GridLayout(cols=1, padding=20)
        content.add_widget(head)
        content.add_widget(txt_input)
        return content

if __name__ == '__main__':
    main().run()
