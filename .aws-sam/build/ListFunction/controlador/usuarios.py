from src.modelo import Usuario
import json


def listar(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(list(Usuario.scan())),
    }

