import os.path
from django.conf import settings

try:
    from PIL import Image
except ImportError:
    import Image

AUTO_GENERATE_AVATAR_SIZES = getattr(settings, 'AUTO_GENERATE_AVATAR_SIZES', (80,))
AVATAR_RESIZE_METHOD = getattr(settings, 'AVATAR_RESIZE_METHOD', Image.ANTIALIAS)
AVATAR_STORAGE_DIR = getattr(settings, 'AVATAR_STORAGE_DIR', 'avatars')
AVATAR_GRAVATAR_BACKUP = getattr(settings, 'AVATAR_GRAVATAR_BACKUP', True)
AVATAR_DEFAULT_URL = getattr(settings, 'AVATAR_DEFAULT_URL', 
    settings.MEDIA_URL + os.path.join(os.path.dirname(__file__), 'default.jpg'))



