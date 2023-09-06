def areaEntidad(data)->dict:
    return{
        '_id':str(data['_id']),
        'nombre':data['nombre'],
        'codigo':data['codigo'],
        'imagen':data['imagen'],
   
    }


def areasEntidad(entity)->list:
  return   [areaEntidad(data)for data in entity]