class Config:
    DEFAULT_CONFIG = {
        "primary": 1,
        "secondary": 0,
        "pause_steps": 10,
        "scrollbar_padding": 2,
        "text_padding_left": 25,
        "scroll_text_padding_left": 35,
        "width": 128,
        "height": 40
    }

    def __init__(self, config=None):
        if config is None:
            config = {}

        for key, value in self.DEFAULT_CONFIG.items():
            setattr(self, key, config.get(key, value))