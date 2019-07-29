# we expect to get only one parameter in float format
def rpc_handler(method_name, param):
    if method_name == "rpcHandlerFunction":
        return {"deviceName": "Temp Sensor", "tag": "WriteInteger", "value": int(200 * float(param)), "functionCode": 16,
                "address": 0, "unitId": 1, "byteOrder": "BIG", "registerCount": 1}
    elif method_name == "rpcHandlerFunction2":
        return {"deviceName": "Temp Sensor", "tag": "WriteInteger", "value": int(200 * float(param)), "functionCode": 16,
                "address": 0, "unitId": 1, "byteOrder": "BIG", "registerCount": 1}