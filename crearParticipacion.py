import boto3

def lambda_handler(event, context):
    # Entrada
    var_codigo = event['codigo']
    var_nombre = event['nombre']
    var_puntos = event['puntos']
    var_fecha = event['fecha']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EvaCon')
    participacion = {
        'codigo': var_codigo,
        'nombre': var_nombre,
        'puntos': var_puntos,
        'fecha': var_fecha
    }
    table.put_item(Item=participacion)
    # Salida
    return {
        'statusCode': 200,
        'participacionInsertada': participacion
    }