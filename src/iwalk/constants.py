from typing import TypedDict, NotRequired

EXCLUDED_TYPES: list[str] = ["O.AAE"]
EXIF_TAGS: list[str] = ["BurstUUID", "ContentIdentifier"]
INDEX_COLS: list[str] = ["dir", "obj_name", "is_patterned"]


class AssetType(TypedDict):
    name: str
    file_count: int
    obj_types: list[str]
    to_be_loaded: NotRequired[list[str]]


SUPPORTED_ASSET_TYPES: list[AssetType] = [
    {
        "name": "edited_heic",
        "file_count": 2,
        "obj_types": ["E.HEIC", "O.HEIC"],
        "to_be_loaded": ["E.HEIC"],
    },
    {
        "name": "original_heic",
        "file_count": 1,
        "obj_types": ["O.HEIC"],
        "to_be_loaded": ["O.HEIC"],
    },
    {
        "name": "edited_jpg",
        "file_count": 2,
        "obj_types": ["E.JPG", "O.JPG"],
        "to_be_loaded": ["E.JPG"],
    },
    {
        "name": "original_jpg",
        "file_count": 1,
        "obj_types": ["O.JPG"],
        "to_be_loaded": ["O.JPG"],
    },
    {
        "name": "edited_mov",
        "file_count": 2,
        "obj_types": ["E.MOV", "O.MOV"],
        "to_be_loaded": ["E.MOV"],
    },
    {
        "name": "original_mov",
        "file_count": 1,
        "obj_types": ["O.MOV"],
        "to_be_loaded": ["O.MOV"],
    },
    {
        "name": "edited_jpg_original_heic",
        "file_count": 2,
        "obj_types": ["E.JPG", "O.HEIC"],
        "to_be_loaded": ["E.JPG"],
    },
    {
        "name": "edited_screenshot",
        "file_count": 2,
        "obj_types": ["E.JPG", "O.PNG"],
    },
    {
        "name": "original_screenshot",
        "file_count": 1,
        "obj_types": ["O.PNG"],
    },
    {
        "name": "original_webp",
        "file_count": 1,
        "obj_types": ["O.WEBP"],
    },
    {
        "name": "original_gif",
        "file_count": 1,
        "obj_types": ["O.GIF"],
    },
    {
        "name": "original_screen_recording",
        "file_count": 1,
        "obj_types": ["O.MP4"],
    },
    {
        "name": "live_photo",
        "file_count": 2,
        "obj_types": ["O.MOV", "O.HEIC"],
        "to_be_loaded": ["O.MOV", "O.HEIC"],
    },
    {
        "name": "live_photo_jpg",
        "file_count": 2,
        "obj_types": ["O.MOV", "O.JPG"],
        "to_be_loaded": ["O.MOV", "O.JPG"],
    },
    {
        "name": "live_photo_edited",
        "file_count": 2,
        "obj_types": ["E.MOV", "E.HEIC"],
        "to_be_loaded": ["E.MOV", "E.HEIC"],
    },
    {
        "name": "live_photo_edited_jpg",
        "file_count": 2,
        "obj_types": ["E.MOV", "E.JPG"],
        "to_be_loaded": ["E.MOV", "E.JPG"],
    },
]
