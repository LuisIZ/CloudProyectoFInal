import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # Entrada (json)
    body = json.loads(event['Records'][0]['body'])
    Message = json.loads(body['Message'])
    
    # Entrada
    var_codigo_curso = Message['codigo_curso']
    var_codigo_alumno = Message['codigo_alumno']
    var_puntaje_total = Message['puntaje_total']
    var_ultimo_puntaje = int(Message['ultimo_puntaje'])
    var_fecha_ultimo_puntaje = Message['fecha_ultimo_puntaje']

    # TablaEC
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TablaEC')
    
    response = table.query(
            KeyConditionExpression = Key('codigo_curso').eq(var_codigo_curso) &
            Key('codigo_alumno').eq(var_codigo_alumno)
        )
    item = response['Items']
    
    if item == []:
        participacion = {
            'codigo_curso': var_codigo_curso,
            'codigo_alumno': var_codigo_alumno,
            'puntaje_total': var_puntaje_total,
            'ultimo_puntaje': var_ultimo_puntaje,
            'fecha_ultimo_puntaje': var_fecha_ultimo_puntaje
        }
        table.put_item(Item=participacion)
    else:
        table.update_item(
                Key={
                    'codigo_curso': var_codigo_curso,
                    'codigo_alumno': var_codigo_alumno
                },
                UpdateExpression = 'SET ultimo_puntaje = :val1, puntaje_total = :val2, fecha_ultimo_puntaje = :val3',
                ExpressionAttributeValues={
                    ':val1': var_ultimo_puntaje,
                    ':val2': str(int(item[0]['puntaje_total']) + int(var_ultimo_puntaje)),
                    ':val3': var_fecha_ultimo_puntaje
                }
            )
            
        participacion = {
            'codigo_curso': var_codigo_curso,
            'codigo_alumno': var_codigo_alumno,
            'puntaje_total': item[0]['puntaje_total'],
            'ultimo_puntaje': var_ultimo_puntaje,
            'fecha_ultimo_puntaje': item[0]['fecha_ultimo_puntaje']
        }

    # Salida
    return {
        'statusCode': 200,
        'participacionInsertada': participacion
    }