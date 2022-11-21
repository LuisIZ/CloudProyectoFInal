import boto3
def lambda_handler(event, context):
    # Entrada (json)
    nombre = event['nombre']
    codigo = event['codigo']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.delete_item(
        Key={
            'nombre': nombre,
            'codigo': codigo
        }
    )
# Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }