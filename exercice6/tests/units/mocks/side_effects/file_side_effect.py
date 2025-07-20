
from tests.units.mocks.file_content_mock import unvalide_content_with_no_database, file_content, unvalide_json_content_file
config = {
    "/1": file_content,
    "/2": unvalide_content_with_no_database,
    "/3": unvalide_json_content_file,
    }

def file_side_effect(config_path):
    result = config.get(config_path,None)
    if not result:
        raise FileNotFoundError(f"Le fichier {config_path} n'existe pas")
    
    return result
