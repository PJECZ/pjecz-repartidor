import click
import configparser


class Config(object):

    def __init__(self):
        self.rama = ''
        self.distrito = ''  # Filtro
        self.autoridad = ''  # Filtro
        self.fecha = ''  # Filtro
        self.fecha_por_defecto = ''
        self.deposito_ruta = ''
        self.google_storage_url = ''
        self.metadatos_partes = ''
        self.servidor_json_ruta = ''
        self.servidor_json_url = ''

    def cargar_configuraciones(self):
        if self.rama == '':
            raise Exception('ERROR: Faltó definir la rama.')
        settings = configparser.ConfigParser()
        settings.read('settings.ini')
        try:
            self.fecha_por_defecto = settings['global']['fecha_por_defecto']
            self.deposito_ruta = settings[self.rama]['deposito_ruta']
            self.google_storage_url = settings[self.rama]['google_storage_url']
            self.metadatos_partes = settings[self.rama]['metadatos_partes']
            self.servidor_json_ruta = settings[self.rama]['servidor_json_ruta']
            self.servidor_json_url = settings[self.rama]['servidor_json_url']
        except KeyError:
            raise Exception(f'ERROR: Falta configuración en settings.ini para la rama {self.rama}')


pass_config = click.make_pass_decorator(Config, ensure=True)
