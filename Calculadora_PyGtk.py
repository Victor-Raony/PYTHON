import gi
from Calculadora import Calculadora

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

builder = Gtk.Builder()
builder.add_from_file('user_interface.glade')


class Handler(object):
    def __init__(self):
        self.usar_estilo()

        self.display = builder.get_object('display')
        self.display.set_text("0")

        self.primeiro_numero = None
        self.operacao = None
        self.calc = Calculadora()
        self.limpar_display = None

    def usar_estilo(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static/estilo_calculadora.css')
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_butao_clicked(self, botao):
        if self.limpar_display:
            self.display.set_text("0")
            self.limpar_display = False

        if self.display.get_text() == "0":
            self.display.set_text(str(botao.get_label()))
        else:
            self.display.set_text(str(self.display.get_text() + botao.get_label()))

    def on_butao_ponto_clicked(self, botao):
        self.display.set_text(str(self.display.get_text() + botao.get_label()))

    def on_butao_reset_clicked(self, botao):
        self.display.set_text("0")

    def on_butao_soma_clicked(self, botao):
        self.operacao = "soma"
        self.primeiro_numero = self.ler_display()
        self.limpar_display = True

    def on_butao_subtracao_clicked(self, botao):
        self.operacao = "subtracao"
        self.primeiro_numero = self.ler_display()
        self.limpar_display = True

    def on_butao_multiplicacao_clicked(self, botao):
        self.operacao = "multiplicacao"
        self.primeiro_numero = self.ler_display()
        self.limpar_display = True

    def on_butao_divisao_clicked(self, botao):
        self.operacao = "divisao"
        self.primeiro_numero = self.ler_display()
        self.limpar_display = True

    def on_butao_raiz_quadrada_clicked(self, botao):
        numero_atual = self.ler_display()
        resultado = self.calc.funcoes["raiz_quadrada"](numero_atual)
        self.display.set_text(str(resultado))

    def on_butao_porcentagem_clicked(self, botao):
        self.operacao = "porcentagem"
        self.primeiro_numero = self.ler_display()
        self.limpar_display = True

    def ler_display(self):
        string = self.display.get_text()

        try:
            numero = int(string)
        except:
            numero = float(string)
        return numero

    def on_butao_igual_clicked(self, botao):
        numero_atual = self.ler_display()

        resultado = self.calc.funcoes[self.operacao](self.primeiro_numero, numero_atual)
        self.display.set_text(str(resultado))
        self.limpar_display = True

builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
