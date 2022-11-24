import json
import boto3

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    try:
        response_sns = sns_client.publish(
                TopicArn = 'arn:aws:sns:us-east-1:466909036508:TemaNotificacionNuevaTarea',
                Subject = 'Nueva tarea creada',
                Message = json.dumps(event['Records'][0]['dynamodb']['NewImage'])
            )
    except:
        # Asumo que la tarea solo se puede eliminar
        # debido a que en la pagina web no se pueden modificar tareas
        response_sns = sns_client.publish(
                TopicArn = 'arn:aws:sns:us-east-1:466909036508:TemaNotificacionNuevaTarea',
                Subject = 'Tarea eliminada',
                Message = json.dumps(event['Records'][0]['dynamodb']['Keys'])
            )
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': response_sns
    }