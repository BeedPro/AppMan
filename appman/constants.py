import os

HOME = os.path.expanduser("~")
PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
APPIMAGE_DOWNLOAD_PATH = f"{HOME}/Downloads/AppImages"
SOURCES_DIR = f"{PROJECT_DIR}/packages"
