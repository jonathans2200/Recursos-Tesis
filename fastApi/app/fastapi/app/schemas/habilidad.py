def habilidadEntidad(data)->dict:
    return{
        '_id':str(data['_id']),
        'codigo':str(data['codigo']),
        'cod_competencia':data['cod_competencia'],
        'identificador':str(data['identificador']),
        'nombre':data['nombre'],
        
        
   
    }


def habilidadesEntidad(entity)->list:
  return   [habilidadEntidad(data) for data in entity]