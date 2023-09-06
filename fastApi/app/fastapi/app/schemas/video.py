def videoEntidad(data)->dict:
    return{
       '_id':str(data['_id']),
       'codigo':str(data['codigo']),
        'link':data['link'],
        'descripcion':data['descripcion'],
        'identificador':str(data['identificador']),
        
    
        
        
   
    }


def videosEntidad(entity)->list:
  return   [videoEntidad(data) for data in entity]