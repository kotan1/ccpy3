str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
print str[start:end:stride]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message