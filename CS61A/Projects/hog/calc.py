import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

