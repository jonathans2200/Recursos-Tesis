def bloqueEntidad(data)->dict:
    return{
        '_id':str(data['_id']),
        'codigo':data['codigo'],
        'codigo_area':data['codigo_area'],
        'nombre':data['nombre'],
   
    }


def bloqueEntidad(entity)->list:
  return   [bloqueEntidad(data)for data in entity]