# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/igp/sync_delay_restart/ldp_igp_sync_delay_restart_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/igp/sync_delay_restart/ldp_igp_sync_delay_restart_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart',
  syntax='proto3',
  serialized_pb=_b('\n~cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/igp/sync_delay_restart/ldp_igp_sync_delay_restart_info.proto\x12Xcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart\"I\n$ldp_igp_sync_delay_restart_info_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x66_name\x18\x02 \x01(\t\"x\n\x1fldp_igp_sync_delay_restart_info\x12\x12\n\nconfigured\x18\x32 \x01(\x08\x12\x12\n\ndelay_secs\x18\x33 \x01(\r\x12\x15\n\rtimer_running\x18\x34 \x01(\x08\x12\x16\n\x0eremaining_secs\x18\x35 \x01(\rb\x06proto3')
)




_LDP_IGP_SYNC_DELAY_RESTART_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_igp_sync_delay_restart_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info_KEYS.vrf_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info_KEYS.af_name', index=1,
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
  serialized_start=220,
  serialized_end=293,
)


_LDP_IGP_SYNC_DELAY_RESTART_INFO = _descriptor.Descriptor(
  name='ldp_igp_sync_delay_restart_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configured', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info.configured', index=0,
      number=50, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delay_secs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info.delay_secs', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timer_running', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info.timer_running', index=2,
      number=52, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remaining_secs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info.remaining_secs', index=3,
      number=53, type=13, cpp_type=3, label=1,
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
  serialized_start=295,
  serialized_end=415,
)

DESCRIPTOR.message_types_by_name['ldp_igp_sync_delay_restart_info_KEYS'] = _LDP_IGP_SYNC_DELAY_RESTART_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_igp_sync_delay_restart_info'] = _LDP_IGP_SYNC_DELAY_RESTART_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_igp_sync_delay_restart_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_igp_sync_delay_restart_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_IGP_SYNC_DELAY_RESTART_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_igp_sync_delay_restart_info_KEYS)

ldp_igp_sync_delay_restart_info = _reflection.GeneratedProtocolMessageType('ldp_igp_sync_delay_restart_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_IGP_SYNC_DELAY_RESTART_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.igp.sync_delay_restart.ldp_igp_sync_delay_restart_info)
  ))
_sym_db.RegisterMessage(ldp_igp_sync_delay_restart_info)


# @@protoc_insertion_point(module_scope)
