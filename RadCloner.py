import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))