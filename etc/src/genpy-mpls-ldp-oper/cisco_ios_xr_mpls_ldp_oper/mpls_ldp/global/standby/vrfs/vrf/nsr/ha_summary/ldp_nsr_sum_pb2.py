# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/nsr/ha_summary/ldp_nsr_sum.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/nsr/ha_summary/ldp_nsr_sum.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary',
  syntax='proto3',
  serialized_pb=_b('\n\\cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/nsr/ha_summary/ldp_nsr_sum.proto\x12Jcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary\"$\n\x10ldp_nsr_sum_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\"\xe4\x01\n\x0bldp_nsr_sum\x12\x65\n\x03vrf\x18\x32 \x01(\x0b\x32X.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_vrf_info\x12n\n\x08sessions\x18\x33 \x01(\x0b\x32\\.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"\x92\x02\n\x10ldp_nsr_sum_sess\x12\r\n\x05total\x18\x01 \x01(\r\x12\x14\n\x0cnsr_eligible\x18\x02 \x01(\r\x12\x16\n\x0ensr_state_none\x18\x03 \x01(\r\x12\x16\n\x0ensr_state_wait\x18\x04 \x01(\r\x12\x17\n\x0fnsr_state_ready\x18\x05 \x01(\r\x12\x19\n\x11nsr_state_prepare\x18\x06 \x01(\r\x12\x1a\n\x12nsr_state_app_wait\x18\x07 \x01(\r\x12\x1d\n\x15nsr_state_operational\x18\x08 \x01(\r\x12\x1c\n\x14nsr_state_tcp_phase1\x18\t \x01(\r\x12\x1c\n\x14nsr_state_tcp_phase2\x18\n \x01(\rb\x06proto3')
)




_LDP_NSR_SUM_KEYS = _descriptor.Descriptor(
  name='ldp_nsr_sum_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_KEYS.vrf_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=172,
  serialized_end=208,
)


_LDP_NSR_SUM = _descriptor.Descriptor(
  name='ldp_nsr_sum',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum.vrf', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sessions', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum.sessions', index=1,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=439,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_vrf_info.id', index=1,
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
  serialized_start=441,
  serialized_end=481,
)


_LDP_NSR_SUM_SESS = _descriptor.Descriptor(
  name='ldp_nsr_sum_sess',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.total', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_eligible', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_eligible', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_none', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_none', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_wait', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_wait', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_ready', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_ready', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_prepare', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_prepare', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_app_wait', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_app_wait', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_operational', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_operational', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_tcp_phase1', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_tcp_phase1', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_state_tcp_phase2', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess.nsr_state_tcp_phase2', index=9,
      number=10, type=13, cpp_type=3, label=1,
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
  serialized_start=484,
  serialized_end=758,
)

_LDP_NSR_SUM.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
_LDP_NSR_SUM.fields_by_name['sessions'].message_type = _LDP_NSR_SUM_SESS
DESCRIPTOR.message_types_by_name['ldp_nsr_sum_KEYS'] = _LDP_NSR_SUM_KEYS
DESCRIPTOR.message_types_by_name['ldp_nsr_sum'] = _LDP_NSR_SUM
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_nsr_sum_sess'] = _LDP_NSR_SUM_SESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_nsr_sum_KEYS = _reflection.GeneratedProtocolMessageType('ldp_nsr_sum_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_SUM_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_KEYS)
  ))
_sym_db.RegisterMessage(ldp_nsr_sum_KEYS)

ldp_nsr_sum = _reflection.GeneratedProtocolMessageType('ldp_nsr_sum', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_SUM,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum)
  ))
_sym_db.RegisterMessage(ldp_nsr_sum)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)

ldp_nsr_sum_sess = _reflection.GeneratedProtocolMessageType('ldp_nsr_sum_sess', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_SUM_SESS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.nsr.ha_summary.ldp_nsr_sum_sess)
  ))
_sym_db.RegisterMessage(ldp_nsr_sum_sess)


# @@protoc_insertion_point(module_scope)
