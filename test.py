from PtpOperation import *
from PtpResponse import *

def sendRepuset(data):
    print(type(data))

def recvResponse():
    return PtpResponse.OK

sendRepuset(PtpOperation.OpenSession)

result = recvResponse()
print(hex(PtpResponse.GenericContainerStructure.parse(result).code))

ptpapi = PtpApi()
