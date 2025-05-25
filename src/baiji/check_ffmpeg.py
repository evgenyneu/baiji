import shutil
import sys
import platform


def check_ffmpeg() -> bool:
    """
    Check if ffmpeg is installed and available in PATH.
    Returns True if ffmpeg is found, False otherwise.
    """
    return shutil.which('ffmpeg') is not None


def get_install_instructions() -> str:
    """
    Get platform-specific instructions for installing ffmpeg.
    """
    system = platform.system().lower()

    if system == 'linux':
        return "Please install ffmpeg using your package manager:\n" \
               "  Ubuntu/Debian: sudo apt-get install ffmpeg\n" \
               "  Fedora: sudo dnf install ffmpeg\n" \
               "  Arch Linux: sudo pacman -S ffmpeg"

    if system == 'darwin':
        return "Please install ffmpeg using Homebrew:\n" \
               "  brew install ffmpeg"

    if system == 'windows':
        return "Please install ffmpeg:\n" \
               "  1. Download from https://ffmpeg.org/download.html\n" \
               "  2. Add ffmpeg to your system PATH"

    return "Please install ffmpeg for your operating system from https://ffmpeg.org/download.html"


def verify_ffmpeg() -> None:
    """
    Verify that ffmpeg is installed. If not, print instructions and exit.
    """
    if not check_ffmpeg():
        print("\nError: ffmpeg is not installed or not found.")
        print("\nInstallation instructions:")
        print(get_install_instructions())
        sys.exit(1)
