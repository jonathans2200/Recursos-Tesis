def usuarioEntidad(data)-> dict:
    return {
        '_id':str(data['_id']),
        'codigo':str(data['codigo']),
        'usuario':data['usuario'],
         'nombre':data['nombre'],
          'apellido':data['apellido'],
        'contrasena':data['contrasena'],
        'correo':data['correo'],
        'rol':data['rol']
        
        

    }



def usuariosEntidad(entity)->list:
   return  [usuarioEntidad(data)for data in entity]
