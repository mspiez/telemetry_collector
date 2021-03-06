# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/default_vrf/afs/af/discovery/stats/stat/ldp_discovery_adj_grp_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/default_vrf/afs/af/discovery/stats/stat/ldp_discovery_adj_grp_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat',
  syntax='proto3',
  serialized_pb=_b('\n{cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/default_vrf/afs/af/discovery/stats/stat/ldp_discovery_adj_grp_info.proto\x12Zcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat\"Z\n\x1fldp_discovery_adj_grp_info_KEYS\x12\x0f\n\x07\x61\x66_name\x18\x01 \x01(\t\x12\x0e\n\x06lsr_id\x18\x02 \x01(\t\x12\x16\n\x0elabel_space_id\x18\x03 \x01(\r\"\x82\x01\n\x1aldp_discovery_adj_grp_info\x12\x1f\n\x17\x61\x64jacency_group_up_time\x18\x32 \x01(\r\x12\x16\n\x0etcp_open_count\x18\x33 \x01(\r\x12\x19\n\x11tcp_arb_chg_count\x18\x34 \x01(\r\x12\x10\n\x08tcp_role\x18\x35 \x01(\rb\x06proto3')
)




_LDP_DISCOVERY_ADJ_GRP_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_discovery_adj_grp_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info_KEYS.af_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsr_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info_KEYS.lsr_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_space_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info_KEYS.label_space_id', index=2,
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
  serialized_start=219,
  serialized_end=309,
)


_LDP_DISCOVERY_ADJ_GRP_INFO = _descriptor.Descriptor(
  name='ldp_discovery_adj_grp_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adjacency_group_up_time', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info.adjacency_group_up_time', index=0,
      number=50, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tcp_open_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info.tcp_open_count', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tcp_arb_chg_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info.tcp_arb_chg_count', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tcp_role', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info.tcp_role', index=3,
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
  serialized_start=312,
  serialized_end=442,
)

DESCRIPTOR.message_types_by_name['ldp_discovery_adj_grp_info_KEYS'] = _LDP_DISCOVERY_ADJ_GRP_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_discovery_adj_grp_info'] = _LDP_DISCOVERY_ADJ_GRP_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_discovery_adj_grp_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_discovery_adj_grp_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_DISCOVERY_ADJ_GRP_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_discovery_adj_grp_info_KEYS)

ldp_discovery_adj_grp_info = _reflection.GeneratedProtocolMessageType('ldp_discovery_adj_grp_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_DISCOVERY_ADJ_GRP_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.default_vrf.afs.af.discovery.stats.stat.ldp_discovery_adj_grp_info)
  ))
_sym_db.RegisterMessage(ldp_discovery_adj_grp_info)


# @@protoc_insertion_point(module_scope)
