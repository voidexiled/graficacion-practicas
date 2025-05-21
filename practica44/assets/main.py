from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(text='Animación por Computadora', font_size=24, size_hint_y=None, height=50)
        layout.add_widget(title)
        
        layout.add_widget(Button(text='Historia', size_hint_y=None, height=50, on_release=self.show_historia))
        layout.add_widget(Button(text='Evolucion', size_hint_y=None, height=50, on_release=self.show_evolucion))
        layout.add_widget(Button(text='Aplicaciones', size_hint_y=None, height=50, on_release=self.show_aplicaciones))
        
        return layout
    
    def show_historia(self, instance):
        contenido = (
            "* Década de 1960: Ivan Sutherland y Sketchpad.\n",
            "* 1982: Dinsey Lanza Tron.\n",
            "* 1995: Pixar Lanza Toy Story, la primera pelicula animada digitalmente."
        )
        self.show_popup("Historia", contenido)
        
    def show_evolucion(self, instance):
        contenido = (
            "* 1980-90: Nace el CGI.\n",
            "* 2000-10: Captura de movimiento y realismo.\n",
            "* 2010+: IA, RV, y motores como Unreal y Unity."
        )
        self.show_popup("Evolución", contenido)
        
    def show_aplicaciones(self, instance):
        contenido = (
            "* Cine y TV: efectos, personajes digitales.\n",
            "* Videojuegos: interacción 3D.\n",
            "* Medicina: simulaciones.\n",
            "* Educación: videos didácticos.<\n",
            "* Arquitectura: recorridos virtuales."
        )
        self.show_popup("Aplicaciones", contenido)
        
    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text="".join(message)),
                      size_hint=(0.8, 0.5))
        popup.open()
        
if __name__ == '__main__':
    MainApp().run()
        