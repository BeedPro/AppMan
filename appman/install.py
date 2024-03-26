from appman.constants import APPIMAGE_DOWNLOAD_PATH
import os


def get_filename_from_url(url: str) -> str:
    return url.split("/")[-1]


def download(
    url: str,
    filename: str = "",
    download_dir: str = APPIMAGE_DOWNLOAD_PATH,
) -> bool:
    """
    Download an AppImage file from a given URL to the APPIMAGE_DOWNLOAD_PATH path.
        Parameters:
            url (str): The URL to download the AppImage from.
            filename (str): The name of the downloaded file.
            filepath (str): The path to save the downloaded file to.

        Returns:
            download_status (bool): True if the download was successful, False otherwise.
    """
    if not download_dir:
        os.makedirs(APPIMAGE_DOWNLOAD_PATH)
    if not filename:
        pass
    download_success = False
    return download_success


def main():
    pass


if __name__ == "__main__":
    main()
