EXCLUDED_TYPES = ["O.AAE"]
EXIF_TAGS = ["BurstUUID", "ContentIdentifier"]
SUPPORTED_ASSET_TYPES = {
    "edited_heic": {
        "file_count": 2,
        "obj_types": ["E.HEIC", "O.HEIC"],
        "to_be_loaded": ["E.HEIC"],
    },
    "original_heic": {
        "file_count": 1,
        "obj_types": ["O.HEIC"],
        "to_be_loaded": ["O.HEIC"],
    },
    "edited_jpg": {
        "file_count": 2,
        "obj_types": ["E.JPG", "O.JPG"],
        "to_be_loaded": ["E.JPG"],
    },
    "original_jpg": {
        "file_count": 1,
        "obj_types": ["O.JPG"],
        "to_be_loaded": ["O.JPG"],
    },
    "edited_mov": {
        "file_count": 2,
        "obj_types": ["E.MOV", "O.MOV"],
        "to_be_loaded": ["E.MOV"],
    },
    "original_mov": {
        "file_count": 1,
        "obj_types": ["O.MOV"],
        "to_be_loaded": ["O.MOV"],
    },
    "edited_jpg_original_heic": {
        "file_count": 2,
        "obj_types": ["E.JPG", "O.HEIC"],
        "to_be_loaded": ["E.JPG"],
    },
    "edited_screenshot": {
        "file_count": 2,
        "obj_types": ["E.JPG", "O.PNG"],
        "to_be_loaded": None,
    },
    "original_screenshot": {
        "file_count": 1,
        "obj_types": ["O.PNG"],
        "to_be_loaded": None,
    },
    "original_webp": {
        "file_count": 1,
        "obj_types": ["O.WEBP"],
        "to_be_loaded": None,
    },
    "original_gif": {"file_count": 1, "obj_types": ["O.GIF"], "to_be_loaded": None},
    "original_screen_recording": {
        "file_count": 1,
        "obj_types": ["O.MP4"],
        "to_be_loaded": None,
    },
    "live_photo": {
        "file_count": 2,
        "obj_types": ["O.MOV", "O.HEIC"],
        "to_be_loaded": ["O.MOV", "O.HEIC"],
    },
    "live_photo_jpg": {
        "file_count": 2,
        "obj_types": ["O.MOV", "O.JPG"],
        "to_be_loaded": ["O.MOV", "O.JPG"],
    },
    "live_photo_edited": {
        "file_count": 2,
        "obj_types": ["E.MOV", "E.HEIC"],
        "to_be_loaded": ["E.MOV", "E.HEIC"],
    },
    "live_photo_edited_jpg": {
        "file_count": 2,
        "obj_types": ["E.MOV", "E.JPG"],
        "to_be_loaded": ["E.MOV", "E.JPG"],
    },
}
