# -* - coding: UTF-8 -* -

import google.protobuf
from google.protobuf import descriptor as _descriptor

if __name__ == '__main__':
    DESCRIPTOR = _descriptor.FileDescriptor(
        name='test.proto',
        package='',
        syntax='proto3',
        # serialized_options=None,
        # serialized_pb=b'',
        # dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR, ]
    )
    print(DESCRIPTOR.GetOptions())
