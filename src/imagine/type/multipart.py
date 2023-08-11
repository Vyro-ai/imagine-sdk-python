from typing import Dict, Tuple, Union


MultipartForm = Dict[str, Tuple[None, str]]
MultipartFile = Dict[str, Tuple[str, bytes, str]]
Multipart = Dict[str, Union[Tuple[None, str], Tuple[str, bytes, str]]]
