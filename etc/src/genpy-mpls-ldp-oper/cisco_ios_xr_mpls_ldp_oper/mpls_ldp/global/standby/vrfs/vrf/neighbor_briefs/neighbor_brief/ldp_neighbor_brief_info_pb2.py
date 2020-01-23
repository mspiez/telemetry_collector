# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/neighbor_briefs/neighbor_brief/ldp_neighbor_brief_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/neighbor_briefs/neighbor_brief/ldp_neighbor_brief_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief',
  syntax='proto3',
  serialized_pb=_b('\nxcisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/neighbor_briefs/neighbor_brief/ldp_neighbor_brief_info.proto\x12Zcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief\"X\n\x1cldp_neighbor_brief_info_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\x12\x0e\n\x06lsr_id\x18\x02 \x01(\t\x12\x16\n\x0elabel_space_id\x18\x03 \x01(\r\"\xee\x02\n\x17ldp_neighbor_brief_info\x12u\n\x03vrf\x18\x32 \x01(\x0b\x32h.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_vrf_info\x12\x1f\n\x17is_graceful_restartable\x18\x33 \x01(\x08\x12\x11\n\tnsr_state\x18\x34 \x01(\t\x12\x17\n\x0fup_time_seconds\x18\x35 \x01(\r\x12\x8e\x01\n\x0enbr_br_af_info\x18\x36 \x03(\x0b\x32v.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_af_info\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"\x88\x01\n\x1aldp_neighbor_brief_af_info\x12\x16\n\x0e\x61\x64\x64ress_family\x18\x01 \x01(\t\x12\x1c\n\x14num_of_nbr_discovery\x18\x02 \x01(\r\x12\x1c\n\x14num_of_nbr_addresses\x18\x03 \x01(\r\x12\x16\n\x0enum_of_nbr_lbl\x18\x04 \x01(\rb\x06proto3')
)




_LDP_NEIGHBOR_BRIEF_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_neighbor_brief_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_KEYS.vrf_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsr_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_KEYS.lsr_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_space_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_KEYS.label_space_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_end=304,
)


_LDP_NEIGHBOR_BRIEF_INFO = _descriptor.Descriptor(
  name='ldp_neighbor_brief_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info.vrf', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_graceful_restartable', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info.is_graceful_restartable', index=1,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info.nsr_state', index=2,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='up_time_seconds', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info.up_time_seconds', index=3,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nbr_br_af_info', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info.nbr_br_af_info', index=4,
      number=54, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=307,
  serialized_end=673,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_vrf_info.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=675,
  serialized_end=715,
)


_LDP_NEIGHBOR_BRIEF_AF_INFO = _descriptor.Descriptor(
  name='ldp_neighbor_brief_af_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_af_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_family', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_af_info.address_family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_nbr_discovery', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_af_info.num_of_nbr_discovery', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_nbr_addresses', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_af_info.num_of_nbr_addresses', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_nbr_lbl', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_af_info.num_of_nbr_lbl', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=718,
  serialized_end=854,
)

_LDP_NEIGHBOR_BRIEF_INFO.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
_LDP_NEIGHBOR_BRIEF_INFO.fields_by_name['nbr_br_af_info'].message_type = _LDP_NEIGHBOR_BRIEF_AF_INFO
DESCRIPTOR.message_types_by_name['ldp_neighbor_brief_info_KEYS'] = _LDP_NEIGHBOR_BRIEF_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_neighbor_brief_info'] = _LDP_NEIGHBOR_BRIEF_INFO
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_neighbor_brief_af_info'] = _LDP_NEIGHBOR_BRIEF_AF_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_neighbor_brief_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_neighbor_brief_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NEIGHBOR_BRIEF_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_neighbor_brief_info_KEYS)

ldp_neighbor_brief_info = _reflection.GeneratedProtocolMessageType('ldp_neighbor_brief_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NEIGHBOR_BRIEF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info)
  ))
_sym_db.RegisterMessage(ldp_neighbor_brief_info)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)

ldp_neighbor_brief_af_info = _reflection.GeneratedProtocolMessageType('ldp_neighbor_brief_af_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NEIGHBOR_BRIEF_AF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.neighbor_briefs.neighbor_brief.ldp_neighbor_brief_af_info)
  ))
_sym_db.RegisterMessage(ldp_neighbor_brief_af_info)


# @@protoc_insertion_point(module_scope)
