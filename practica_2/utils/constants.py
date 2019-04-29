"""Constant definitions, text used in warning and error messages"""

text_description = 'Cifrar información utilizando el algoritmo de clave simétrica AES, y ' \
                   'su correspondiente descifrado.\n' \
                   'Calcular su función resumen SHA256 y verificarlo\n' \
                   'Firmar esta información mediante RSA y verificar la firma'

text_help_mode = 'Modo: ' \
                 '[cs/ds] cifrado/descifrado simétrico. La contraseña se establecerá con -p, el fichero cifrado -o' \
                 '[h/vh] función resumen y su verificación. El hash se pasara con -ad ' \
                 '[ca/da] cifrado/descifrado asimétrico. El par de claves publica-privada se ' \
                 'guardara en ./files/, bajo la mascara *_rsa y *_rsa.pub ' \
                 '[cert] Creación de un certificado X.509, cuyo nombre se especificará con -o ' \
                 '[ts/tsv] Sellado de tiempo y su verificación. La autoridad de sellado de tiempo podrá ' \
                 'establecerse directamente en el código fuente.'

text_help_password = 'Contraseña para cifrado simetrico'

text_help_input = 'Path al fichero sobre el que se va a interactuar'

text_help_add = 'Path al fichero adicional requerido'

text_help_output = 'Path al fichero de salida que se va a generar'

text_error_incorrect_arguments = 'Argumentos erroneos, comprueba qué se necesita con -h'

text_error_unsupported_operation = 'Operación no implementada'

text_error_file_missing = 'Fichero no encontrado'

text_signature_OK = 'Firma verificada'

text_signature_KO = 'Firma incorrecta'

text_hash_OK = 'Resumen verificado'

text_hash_KO = 'Resumen incorrecto'

text_metavar_password = "contraseña"

text_metavar_path = "path"
