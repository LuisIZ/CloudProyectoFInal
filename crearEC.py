import boto3

def lambda_handler(event, context):
    print(event)
    # Entrada
    var_codigo_curso = event['codigo_curso']
    var_codigo_alumno = int(event['codigo_alumno'])
    var_puntaje_total = int(event['puntaje_total'])
    var_ultimo_puntaje = int(event['ultimo_puntaje'])
    var_fecha_ultimo_puntaje = event['fecha_ultimo_puntaje']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TablaEC')
    participacion = {
        'codigo_curso': var_codigo_curso,
        'codigo_alumno': var_codigo_alumno,
        'puntaje_total': var_puntaje_total,
        'ultimo_puntaje': var_ultimo_puntaje,
        'fecha_ultimo_puntaje': var_fecha_ultimo_puntaje
    }
    table.put_item(Item=participacion)
    # Salida
    return {
        'statusCode': 200,
        'participacionInsertada': participacion
    }