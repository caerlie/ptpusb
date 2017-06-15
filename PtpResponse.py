from construct import *

class PtpResponse(object):

    GenericContainerStructure = Struct (
            "length" / Int32ul,
            "type" / Enum(Int16ul, com=1, data=2, resp=3, event=4),
            "code" / Int16ul,
            "transactionid" / Int32ul,
            "parametas" / Array((this.length - 12) / 4, Int32ul)
    )

    # OK
    OK = GenericContainerStructure.build(dict(
            length=12,
            type="resp",
            code=0x2001,
            transactionid=0,
            parametas=[]
    ))
