def programaEntidad(data)->dict:
    return{
        '_id':str(data['_id']),
        'codigo':str(data['codigo']),
        'identificador':str(data['identificador']),
         'link':str(data['link']),
        'descripcion':data['descripcion'],
        'nombre':data['nombre'],
        
        
    
    
    }


def programasEntidad(entity)->list:
  return   [programaEntidad(data) for data in entity]