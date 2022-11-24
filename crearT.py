import json
import boto3

def lambda_handler(event, context):
    # Entrada (json)
    body = json.loads(event['Records'][0]['body'])
    Message = json.loads(body['Message'])
    
    # Entrada
    var_codigo_curso = Message['codigo_curso']
    var_nombre_tarea = Message['nombre_tarea']
    var_descripcion = Message['descripcion']
    var_fecha_inicio = Message['fecha_inicio']
    var_fecha_limite = Message['fecha_limite']
    
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