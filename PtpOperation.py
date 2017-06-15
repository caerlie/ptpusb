from construct import *

class PtpOperation(object):

    GenericContainerStructure = Struct (
            "length" / Int32ul,
            "type" / Enum(Int16ul, com=1, data=2, resp=3, event=4),
            "code" / Int16ul,
            "transactionid" / Int32ul,
            "parametas" / Array((this.length - 12) / 4, Int32ul)
    )

    # OpenSession
    OpenSession = GenericContainerStructure.build(dict(
            length=16,
            type="com",
            code=0x1002,
            transactionid=0,
            parametas=[1]
    ))
               



