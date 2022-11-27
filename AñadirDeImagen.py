import boto3
import datetime
from itertools import chain


def minDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]


def clean_name(name):
    # XXX: Very ugly

    it = iter(name)
    first = []

    for c in it:
        if c.isalpha():
            first.append(c)
            break

    for c in it:
        if c.isalpha():
            first.append(c)
        else:
            break

    second = []

    for c in it:
        if c.isalpha():
            second.append(c)
            break

    for c in it:
        if c.isalpha():
            second.append(c)
        else:
            break

    return ''.join(chain(first, ' ', second))


def lambda_handler(event, context):
    client = boto3.client('textract')

    # TODO: Revisar que pese no más de 5MB
    # archivo_id = event['Records'][0]['s3']['object']['size']

    print(event)

    path = event['Records'][0]['s3']['object']['key']
    tenant_id = path.split('/')[0]
    bucket = event['Records'][0]['s3']['bucket']['name']

    print(f"path: {path}")
    print(f"tenant_id: {tenant_id}")
    print(f"bucket: {bucket}")

    response = client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket,
                'Name': path
            }
        }
    )

    lines = [e['Text'] for e in response['Blocks'] if e['BlockType'] == 'LINE']
    names = [clean_name(n) for n in lines[1:]]

    print(f"Names: {names}")

    dyndb = boto3.resource('dynamodb')
    table = dyndb.Table('t_alumnos')
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('tenant_id').eq(tenant_id)
    )
    names_cod = {e['nombre_estudiante']: e['codigo_alumno'] for e in response['Items']}
    known_names = list(names_cod.keys())

    print(f"known_names: {known_names}")

    def find_closest_name(name):
        d = [(minDistance(name, on), on) for on in known_names]
        return min(d, key=lambda p: p[0])

    closest_names = [(d, n) for (d, n) in (find_closest_name(n) for n in names) if d <= 5]
    print(f"closest_names: {closest_names}")

    tabla_ec = dyndb.Table('TablaEC')

    def añadir_puntaje(codigo_alumno):
        response = tabla_ec.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('codigo_curso').eq(tenant_id) &
            boto3.dynamodb.conditions.Key('codigo_alumno').eq(codigo_alumno)
        )

        item = response['Items']

        fecha = datetime.datetime.now().strftime('%Y-%m-%d')

        if item == []:
            participacion = {
                'codigo_curso': tenant_id,
                'codigo_alumno': codigo_alumno,
                'puntaje_total': 1,
                'ultimo_puntaje': 1,
                'fecha_ultimo_puntaje': fecha
            }
            tabla_ec.put_item(Item=participacion)
        else:
            old_puntaje_total = int(item[0]['puntaje_total'])
            puntaje_total = old_puntaje_total + 1

            tabla_ec.update_item(
                Key={
                    'codigo_curso': tenant_id,
                    'codigo_alumno': codigo_alumno
                },
                UpdateExpression='SET ultimo_puntaje = :val1, puntaje_total = :val2, fecha_ultimo_puntaje = :val3',
                ExpressionAttributeValues={
                    ':val1': 1,
                    ':val2': puntaje_total,
                    ':val3': fecha
                }
            )

            participacion = {
                'codigo_curso': tenant_id,
                'codigo_alumno': codigo_alumno,
                'puntaje_total': puntaje_total,
                'ultimo_puntaje': 1,
                'fecha_ultimo_puntaje': fecha
            }

    for name in closest_names:
        añadir_puntaje(names_cod[name[1]])

    return {
        'statusCode': 200
    }
