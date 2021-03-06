# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/default_vrf/backoff_parameters/ldp_backoff_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/default_vrf/backoff_parameters/ldp_backoff_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters',
  syntax='proto3',
  serialized_pb=_b('\nhcisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/default_vrf/backoff_parameters/ldp_backoff_info.proto\x12Qcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters\"\x17\n\x15ldp_backoff_info_KEYS\"D\n\x10ldp_backoff_info\x12\x17\n\x0finitial_seconds\x18\x32 \x01(\r\x12\x17\n\x0fmaximum_seconds\x18\x33 \x01(\rb\x06proto3')
)




_LDP_BACKOFF_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_backoff_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=191,
  serialized_end=214,
)


_LDP_BACKOFF_INFO = _descriptor.Descriptor(
  name='ldp_backoff_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_seconds', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info.initial_seconds', index=0,
      number=50, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_seconds', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info.maximum_seconds', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=216,
  serialized_end=284,
)

DESCRIPTOR.message_types_by_name['ldp_backoff_info_KEYS'] = _LDP_BACKOFF_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_backoff_info'] = _LDP_BACKOFF_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_backoff_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_backoff_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_BACKOFF_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_backoff_info_KEYS)

ldp_backoff_info = _reflection.GeneratedProtocolMessageType('ldp_backoff_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_BACKOFF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.backoff_parameters.ldp_backoff_info)
  ))
_sym_db.RegisterMessage(ldp_backoff_info)


# @@protoc_insertion_point(module_scope)
