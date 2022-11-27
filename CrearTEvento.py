import json
import boto3

def lambda_handler(event, context):
    # Entrada
    var_codigo_curso = event['codigo_curso']
    var_nombre_tarea = event['nombre_tarea']
    var_descripcion = event['descripcion']
    var_fecha_inicio = event['fecha_inicio']
    var_fecha_limite = event['fecha_limite']
    
    tarea = {
        'codigo_curso': var_codigo_curso,
        'nombre_tarea': var_nombre_tarea,
        'descripcion': var_descripcion,
        'fecha_inicio': var_fecha_inicio,
        'fecha_limite': var_fecha_limite
    }

    # Publicar en SNS
    sns_client = boto3.client('sns')
    response_sns = sns_client.publish(
        TopicArn = 'arn:aws:sns:us-east-1:466909036508:TemaNuevaTarea',
        Subject = 'Nueva tarea creada. REVISAR!',
        Message = json.dumps(tarea),
        MessageAttributes = {
            'codigo_curso': {'DataType': 'String', 'StringValue': var_codigo_curso },
            'nombre_tarea': {'DataType': 'String', 'StringValue': var_nombre_tarea }
        }
    )

    # TODO implement
    return {
        'statusCode': 200,
        'body': response_sns
    }