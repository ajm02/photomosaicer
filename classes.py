# Error class from when image is too small
class ImageTooSmallError(Exception):

    def __init__(self, message):
        super().__init__(message)