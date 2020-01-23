# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/issu/ha_statistics/ha_global/ldp_nsr_gbl_stats_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/issu/ha_statistics/ha_global/ldp_nsr_gbl_stats_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global',
  syntax='proto3',
  serialized_pb=_b('\ntcisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/issu/ha_statistics/ha_global/ldp_nsr_gbl_stats_info.proto\x12Wcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global\"/\n\x1bldp_nsr_gbl_stats_info_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\"\x9d\x01\n\x16ldp_nsr_gbl_stats_info\x12\x82\x01\n\tinit_sync\x18\x32 \x01(\x0b\x32o.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info\"\xae\x04\n\x16ldp_nsr_gbl_synci_info\x12\x11\n\tnsr_cfged\x18\x01 \x01(\x08\x12\x12\n\nnsr_synced\x18\x02 \x01(\x08\x12\x17\n\x0finit_sync_start\x18\x03 \x01(\r\x12\x15\n\rinit_sync_end\x18\x04 \x01(\r\x12\x11\n\tnum_peers\x18\x05 \x01(\r\x12\x14\n\x0cnum_cap_sent\x18\x06 \x01(\r\x12\x14\n\x0cnum_cap_rcvd\x18\x07 \x01(\r\x12\x0f\n\x07num_pfx\x18\x08 \x01(\r\x12\x0f\n\x07num_lbl\x18\t \x01(\r\x12\x17\n\x0fnum_lcl_addr_wd\x18\n \x01(\r\x12\x13\n\x0bnum_lbl_adv\x18\x0b \x01(\r\x12\x16\n\x0eipc_msg_tx_cnt\x18\x0c \x01(\r\x12\x18\n\x10ipc_msg_tx_bytes\x18\r \x01(\r\x12\x16\n\x0eipc_msg_rx_cnt\x18\x0e \x01(\r\x12\x18\n\x10ipc_msg_rx_bytes\x18\x0f \x01(\r\x12\x1e\n\x16ipc_max_tx_batch_bytes\x18\x10 \x01(\r\x12\x1e\n\x16ipc_max_rx_batch_bytes\x18\x11 \x01(\r\x12\x17\n\x0fipc_tx_fail_cnt\x18\x12 \x01(\r\x12\x1d\n\x15total_ipc_tx_fail_cnt\x18\x13 \x01(\r\x12\x17\n\x0fipc_restart_cnt\x18\x14 \x01(\r\x12\x17\n\x0fipc_default_mtu\x18\x15 \x01(\r\x12 \n\x18ipc_exceeded_mtu_msg_cnt\x18\x16 \x01(\rb\x06proto3')
)




_LDP_NSR_GBL_STATS_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_nsr_gbl_stats_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info_KEYS.vrf_name', index=0,
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
  serialized_start=209,
  serialized_end=256,
)


_LDP_NSR_GBL_STATS_INFO = _descriptor.Descriptor(
  name='ldp_nsr_gbl_stats_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='init_sync', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info.init_sync', index=0,
      number=50, type=11, cpp_type=10, label=1,
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
  serialized_start=259,
  serialized_end=416,
)


_LDP_NSR_GBL_SYNCI_INFO = _descriptor.Descriptor(
  name='ldp_nsr_gbl_synci_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nsr_cfged', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.nsr_cfged', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_synced', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.nsr_synced', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_sync_start', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.init_sync_start', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_sync_end', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.init_sync_end', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_peers', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.num_peers', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_cap_sent', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.num_cap_sent', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_cap_rcvd', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.num_cap_rcvd', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_pfx', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.num_pfx', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_lbl', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.num_lbl', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_lcl_addr_wd', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.num_lcl_addr_wd', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_lbl_adv', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.num_lbl_adv', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_msg_tx_cnt', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_msg_tx_cnt', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_msg_tx_bytes', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_msg_tx_bytes', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_msg_rx_cnt', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_msg_rx_cnt', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_msg_rx_bytes', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_msg_rx_bytes', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_max_tx_batch_bytes', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_max_tx_batch_bytes', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_max_rx_batch_bytes', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_max_rx_batch_bytes', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_tx_fail_cnt', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_tx_fail_cnt', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_ipc_tx_fail_cnt', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.total_ipc_tx_fail_cnt', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_restart_cnt', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_restart_cnt', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_default_mtu', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_default_mtu', index=20,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipc_exceeded_mtu_msg_cnt', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info.ipc_exceeded_mtu_msg_cnt', index=21,
      number=22, type=13, cpp_type=3, label=1,
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
  serialized_start=419,
  serialized_end=977,
)

_LDP_NSR_GBL_STATS_INFO.fields_by_name['init_sync'].message_type = _LDP_NSR_GBL_SYNCI_INFO
DESCRIPTOR.message_types_by_name['ldp_nsr_gbl_stats_info_KEYS'] = _LDP_NSR_GBL_STATS_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_nsr_gbl_stats_info'] = _LDP_NSR_GBL_STATS_INFO
DESCRIPTOR.message_types_by_name['ldp_nsr_gbl_synci_info'] = _LDP_NSR_GBL_SYNCI_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_nsr_gbl_stats_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_nsr_gbl_stats_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_GBL_STATS_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_nsr_gbl_stats_info_KEYS)

ldp_nsr_gbl_stats_info = _reflection.GeneratedProtocolMessageType('ldp_nsr_gbl_stats_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_GBL_STATS_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info)
  ))
_sym_db.RegisterMessage(ldp_nsr_gbl_stats_info)

ldp_nsr_gbl_synci_info = _reflection.GeneratedProtocolMessageType('ldp_nsr_gbl_synci_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_GBL_SYNCI_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_stats_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.issu.ha_statistics.ha_global.ldp_nsr_gbl_synci_info)
  ))
_sym_db.RegisterMessage(ldp_nsr_gbl_synci_info)


# @@protoc_insertion_point(module_scope)
