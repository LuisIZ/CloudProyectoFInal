import json
import boto3

def lambda_handler(event, context):
    # Entrada
    var_codigo_curso = event['codigo_curso']
    var_codigo_alumno = event['codigo_alumno']
    var_puntaje_total = event['puntaje_total']
    var_ultimo_puntaje = int(event['ultimo_puntaje'])
    var_fecha_ultimo_puntaje = event['fecha_ultimo_puntaje']
    
    participacion = {
        'codigo_curso': var_codigo_curso,
        'codigo_alumno': var_codigo_alumno,
        'puntaje_total': var_puntaje_total,
        'ultimo_puntaje': var_ultimo_puntaje,
        'fecha_ultimo_puntaje': var_fecha_ultimo_puntaje
    }

    # Publicar en SNS
    sns_client = boto3.client('sns')
    response_sns = sns_client.publish(
        TopicArn = 'arn:aws:sns:us-east-1:466909036508:TemaNuevaParticipacion',
        Subject = 'Nueva participacion',
        Message = json.dumps(participacion),
        MessageAttributes = {
            'codigo_curso': {'DataType': 'String', 'StringValue': var_codigo_curso },
            'codigo_alumno': {'DataType': 'String', 'StringValue': var_codigo_alumno }
        }
    )

    # TODO implement
    return {
        'statusCode': 200,
        'body': response_sns
    }