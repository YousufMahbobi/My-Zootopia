class Color:
    @staticmethod
    def red(text): return f'\033[91m{text}\033[0m'
    @staticmethod
    def green(text): return f'\033[92m{text}\033[0m'
    @staticmethod
    def cyan(text): return f'\033[96m{text}\033[0m'
    @staticmethod
    def blue(text): return f'\033[94m{text}\033[0m'
