import logging
import os
from threading import Thread
from PIL import Image
from pystray import MenuItem as item, Icon

from src.DisplayManager import DisplayManager
from src.utils import fetch_content_path


def exit_app(icon):
    icon.stop()
    os._exit(0)


def toggle_clock(icon):
    icon.manager.display_clock = not icon.manager.display_clock
    update_menu(icon)


def toggle_player(icon):
    icon.manager.display_player = not icon.manager.display_player
    update_menu(icon)


def update_menu(icon):
    menu = (
        item("Exit", exit_app),
        item("Display Clock", toggle_clock, checked=lambda item:icon.manager.display_clock),
        item("Display Player", toggle_player, checked= lambda item:icon.manager.display_player)
    )
    icon.menu = menu


def run_systray_async(display_manager: DisplayManager):
    menu = (
        item("Exit", exit_app),
        item("Display Clock", toggle_clock, checked=lambda item: display_manager.display_clock),
        item("Display Player", toggle_player, checked=lambda item: icon.manager.display_player)
    )

    icon = Icon("name", Image.open(fetch_content_path("./assets/icon.png")), "Spotify Linker", menu)
    icon.manager = display_manager

    logging.info("[SYSTRAY] Enabled")
    systray_thread = Thread(target=icon.run, daemon=True)
    systray_thread.start()
