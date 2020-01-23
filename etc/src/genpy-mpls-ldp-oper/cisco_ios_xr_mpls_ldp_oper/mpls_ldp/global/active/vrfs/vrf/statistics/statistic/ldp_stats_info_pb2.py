# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/statistics/statistic/ldp_stats_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/statistics/statistic/ldp_stats_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic',
  syntax='proto3',
  serialized_pb=_b('\ndcisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/statistics/statistic/ldp_stats_info.proto\x12Ocisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic\"O\n\x13ldp_stats_info_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\x12\x0e\n\x06lsr_id\x18\x02 \x01(\t\x12\x16\n\x0elabel_space_id\x18\x03 \x01(\r\"\x95\x02\n\x0eldp_stats_info\x12\x14\n\x0ciccp_enabled\x18\x32 \x01(\x08\x12v\n\x0bmessage_out\x18\x33 \x01(\x0b\x32\x61.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters\x12u\n\nmessage_in\x18\x34 \x01(\x0b\x32\x61.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters\"\xb4\x03\n\x10ldp_msg_counters\x12\x13\n\x0btotal_count\x18\x01 \x01(\r\x12\x12\n\ninit_count\x18\x02 \x01(\r\x12\x15\n\raddress_count\x18\x03 \x01(\r\x12\x1e\n\x16\x61\x64\x64ress_withdraw_count\x18\x04 \x01(\r\x12\x17\n\x0flabel_map_count\x18\x05 \x01(\r\x12\x1c\n\x14label_withdraw_count\x18\x06 \x01(\r\x12\x1b\n\x13label_release_count\x18\x07 \x01(\r\x12\x1b\n\x13label_request_count\x18\x08 \x01(\r\x12!\n\x19label_abort_request_count\x18\t \x01(\r\x12\x1a\n\x12notification_count\x18\n \x01(\r\x12\x18\n\x10keep_alive_count\x18\x0b \x01(\r\x12\x1a\n\x12iccp_rg_conn_count\x18\x0c \x01(\r\x12\x1d\n\x15iccp_rg_disconn_count\x18\r \x01(\r\x12\x1b\n\x13iccp_rg_notif_count\x18\x0e \x01(\r\x12\x1e\n\x16iccp_rg_app_data_count\x18\x0f \x01(\rb\x06proto3')
)




_LDP_STATS_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_stats_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_KEYS.vrf_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsr_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_KEYS.lsr_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_space_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_KEYS.label_space_id', index=2,
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
  serialized_start=185,
  serialized_end=264,
)


_LDP_STATS_INFO = _descriptor.Descriptor(
  name='ldp_stats_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iccp_enabled', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info.iccp_enabled', index=0,
      number=50, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_out', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info.message_out', index=1,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_in', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info.message_in', index=2,
      number=52, type=11, cpp_type=10, label=1,
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
  serialized_start=267,
  serialized_end=544,
)


_LDP_MSG_COUNTERS = _descriptor.Descriptor(
  name='ldp_msg_counters',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.total_count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.init_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.address_count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_withdraw_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.address_withdraw_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_map_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.label_map_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_withdraw_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.label_withdraw_count', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_release_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.label_release_count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_request_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.label_request_count', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_abort_request_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.label_abort_request_count', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notification_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.notification_count', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keep_alive_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.keep_alive_count', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iccp_rg_conn_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.iccp_rg_conn_count', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iccp_rg_disconn_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.iccp_rg_disconn_count', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iccp_rg_notif_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.iccp_rg_notif_count', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iccp_rg_app_data_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters.iccp_rg_app_data_count', index=14,
      number=15, type=13, cpp_type=3, label=1,
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
  serialized_start=547,
  serialized_end=983,
)

_LDP_STATS_INFO.fields_by_name['message_out'].message_type = _LDP_MSG_COUNTERS
_LDP_STATS_INFO.fields_by_name['message_in'].message_type = _LDP_MSG_COUNTERS
DESCRIPTOR.message_types_by_name['ldp_stats_info_KEYS'] = _LDP_STATS_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_stats_info'] = _LDP_STATS_INFO
DESCRIPTOR.message_types_by_name['ldp_msg_counters'] = _LDP_MSG_COUNTERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_stats_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_stats_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_STATS_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_stats_info_KEYS)

ldp_stats_info = _reflection.GeneratedProtocolMessageType('ldp_stats_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_STATS_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info)
  ))
_sym_db.RegisterMessage(ldp_stats_info)

ldp_msg_counters = _reflection.GeneratedProtocolMessageType('ldp_msg_counters', (_message.Message,), dict(
  DESCRIPTOR = _LDP_MSG_COUNTERS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_stats_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.statistics.statistic.ldp_msg_counters)
  ))
_sym_db.RegisterMessage(ldp_msg_counters)


# @@protoc_insertion_point(module_scope)