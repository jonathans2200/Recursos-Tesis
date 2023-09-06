def competenciaEntidad(data)->dict:
    return{
        '_id':str(data['_id']),
        'codigo':data['codigo'],
        'codigo_bloque':data['codigo_bloque'],
        'nombre':data['nombre'],
   
    }


def CompetenciaEntidad(entity)->list:
  return   [competenciaEntidad(data)for data in entity]