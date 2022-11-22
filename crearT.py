import boto3

def lambda_handler(event, context):
    print(event)
    # Entrada
    var_codigo_curso = event['codigo_curso']
    var_nombre_tarea = event['nombre_tarea']
    var_descripcion = event['descripcion']
    var_fecha_inicio = event['fecha_inicio']
    var_fecha_limite = event['fecha_limite']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TablaT')
    tarea = {
        'codigo_curso': var_codigo_curso,
        'nombre_tarea': var_nombre_tarea,
        'descripcion': var_descripcion,
        'fecha_inicio': var_fecha_inicio,
        'fecha_limite': var_fecha_limite
    }
    table.put_item(Item=tarea)
    # Salida
    return {
        'statusCode': 200,
        'participacionInsertada': tarea
    }