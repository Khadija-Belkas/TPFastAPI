from tests.unit.mocks.file_content_mock import user_not_found,error_user,user_inactive,user_valid 
config ={
    "/1":user_not_found,
    "/2": error_user,
    "/3":user_inactive,
    "/4": user_valid ,
    
}
def file_side_effects(config_path):

    result = config.get(config_path,None)
    
