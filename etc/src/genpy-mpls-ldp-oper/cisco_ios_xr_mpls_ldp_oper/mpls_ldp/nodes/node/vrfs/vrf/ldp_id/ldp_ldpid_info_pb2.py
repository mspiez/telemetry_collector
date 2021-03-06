# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/vrfs/vrf/ldp_id/ldp_ldpid_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/vrfs/vrf/ldp_id/ldp_ldpid_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id',
  syntax='proto3',
  serialized_pb=_b('\nScisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/vrfs/vrf/ldp_id/ldp_ldpid_info.proto\x12>cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id\":\n\x13ldp_ldpid_info_KEYS\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\"H\n\x0eldp_ldpid_info\x12\x0e\n\x06lsr_id\x18\x32 \x01(\t\x12\x16\n\x0elabel_space_id\x18\x33 \x01(\r\x12\x0e\n\x06ldp_id\x18\x34 \x01(\tb\x06proto3')
)




_LDP_LDPID_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_ldpid_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info_KEYS.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info_KEYS.vrf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=209,
)


_LDP_LDPID_INFO = _descriptor.Descriptor(
  name='ldp_ldpid_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lsr_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info.lsr_id', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_space_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info.label_space_id', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ldp_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info.ldp_id', index=2,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=283,
)

DESCRIPTOR.message_types_by_name['ldp_ldpid_info_KEYS'] = _LDP_LDPID_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_ldpid_info'] = _LDP_LDPID_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_ldpid_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_ldpid_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_LDPID_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_ldpid_info_KEYS)

ldp_ldpid_info = _reflection.GeneratedProtocolMessageType('ldp_ldpid_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_LDPID_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.ldp_id.ldp_ldpid_info)
  ))
_sym_db.RegisterMessage(ldp_ldpid_info)


# @@protoc_insertion_point(module_scope)
