import os

# variable d'environnement afin d'utiliser wayland et non x11 sur Ubuntu
os.environ['QT_QPA_PLATFORM'] = 'wayland'
