import json
import boto3
import os

def lambda_handler(event, context):
    idioma_destino = event["idioma_destino"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TablaT')
    response = table.scan()
    data = response['Items']
    
    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
    idioma_actual = os.environ['IDIOMA_ORIGEN']
    
    for item in data:
        descripcion_traducida = translate.translate_text(Text=item['descripcion'], SourceLanguageCode=idioma_actual, TargetLanguageCode=idioma_destino)
        table.update_item(
                Key={
                    'codigo_curso': item['codigo_curso'],
                    'nombre_tarea': item['nombre_tarea']
                },
                UpdateExpression = 'SET descripcion = :val1',
                ExpressionAttributeValues={
                    ':val1': descripcion_traducida.get('TranslatedText')
                }
            )
            
    os.environ['IDIOMA_ORIGEN'] = idioma_destino


    return {
        'statusCode': 200,
        'body': {'idioma_actual': idioma_destino}
    }
