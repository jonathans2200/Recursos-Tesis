def encuestaEntidad(data)->dict:
    return{
        '_id':str(data['_id']),
        'pregunta1':data['pregunta1'],
        'pregunta2':data['pregunta2'],
        'pregunta3':data['pregunta3'],
        'pregunta4':data['pregunta4'],
       
        'codigo_usuario':data['codigo_usuario'],
        'codigo_habilidad':data['codigo_habilidad']
       
        
        
        
    
    
    }


def encuestasEntidad(entity)->list:
  return   [encuestaEntidad(data) for data in entity]