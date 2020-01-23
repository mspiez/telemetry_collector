# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/issu/ha_statistics/ha_neighbors/ha_neighbor/ldp_nsr_stats_nbr_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/issu/ha_statistics/ha_neighbors/ha_neighbor/ldp_nsr_stats_nbr_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor',
  syntax='proto3',
  serialized_pb=_b('\n\x84\x01\x63isco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/issu/ha_statistics/ha_neighbors/ha_neighbor/ldp_nsr_stats_nbr_info.proto\x12gcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor\"W\n\x1bldp_nsr_stats_nbr_info_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\x12\x0e\n\x06lsr_id\x18\x02 \x01(\t\x12\x16\n\x0elabel_space_id\x18\x03 \x01(\r\"\xa1\x03\n\x16ldp_nsr_stats_nbr_info\x12\x0e\n\x06lsr_id\x18\x32 \x01(\r\x12\x12\n\nlbl_spc_id\x18\x33 \x01(\r\x12\x16\n\x0ensr_sync_state\x18\x34 \x01(\x11\x12\x0f\n\x07num_msg\x18\x35 \x01(\r\x12\x97\x01\n\x0einit_sync_info\x18\x36 \x01(\x0b\x32\x7f.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info\x12\x9f\x01\n\x16steady_state_sync_info\x18\x37 \x01(\x0b\x32\x7f.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info\"\xe0\x01\n\x16ldp_nsr_nbr_synci_info\x12\x17\n\x0finit_sync_start\x18\x01 \x01(\r\x12\x15\n\rinit_sync_end\x18\x02 \x01(\r\x12\x10\n\x08num_addr\x18\x03 \x01(\r\x12\x1a\n\x12num_duplicate_addr\x18\x04 \x01(\r\x12\x14\n\x0cnum_rx_bytes\x18\x05 \x01(\r\x12\x14\n\x0cnum_cap_sent\x18\x06 \x01(\r\x12\x14\n\x0cnum_cap_rcvd\x18\x07 \x01(\r\x12\x0f\n\x07num_lbl\x18\x08 \x01(\r\x12\x15\n\rnum_app_bytes\x18\t \x01(\r\"\xa5\x01\n\x16ldp_nsr_nbr_syncs_info\x12\x14\n\x0cnum_cap_sent\x18\x01 \x01(\r\x12\x14\n\x0cnum_cap_rcvd\x18\x02 \x01(\r\x12\x12\n\nrem_lbl_wd\x18\x03 \x01(\r\x12\x12\n\nrem_lbl_rq\x18\x04 \x01(\r\x12\x1a\n\x12num_stdby_adj_join\x18\x05 \x01(\r\x12\x1b\n\x13num_stdby_adj_leave\x18\x06 \x01(\rb\x06proto3')
)




_LDP_NSR_STATS_NBR_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_nsr_stats_nbr_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_KEYS.vrf_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsr_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_KEYS.lsr_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_space_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_KEYS.label_space_id', index=2,
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
  serialized_start=242,
  serialized_end=329,
)


_LDP_NSR_STATS_NBR_INFO = _descriptor.Descriptor(
  name='ldp_nsr_stats_nbr_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lsr_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info.lsr_id', index=0,
      number=50, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lbl_spc_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info.lbl_spc_id', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsr_sync_state', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info.nsr_sync_state', index=2,
      number=52, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_msg', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info.num_msg', index=3,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_sync_info', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info.init_sync_info', index=4,
      number=54, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steady_state_sync_info', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info.steady_state_sync_info', index=5,
      number=55, type=11, cpp_type=10, label=1,
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
  serialized_start=332,
  serialized_end=749,
)


_LDP_NSR_NBR_SYNCI_INFO = _descriptor.Descriptor(
  name='ldp_nsr_nbr_synci_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='init_sync_start', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.init_sync_start', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_sync_end', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.init_sync_end', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_addr', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.num_addr', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_duplicate_addr', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.num_duplicate_addr', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_rx_bytes', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.num_rx_bytes', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_cap_sent', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.num_cap_sent', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_cap_rcvd', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.num_cap_rcvd', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_lbl', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.num_lbl', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_app_bytes', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info.num_app_bytes', index=8,
      number=9, type=13, cpp_type=3, label=1,
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
  serialized_start=752,
  serialized_end=976,
)


_LDP_NSR_NBR_SYNCS_INFO = _descriptor.Descriptor(
  name='ldp_nsr_nbr_syncs_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_cap_sent', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info.num_cap_sent', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_cap_rcvd', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info.num_cap_rcvd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rem_lbl_wd', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info.rem_lbl_wd', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rem_lbl_rq', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info.rem_lbl_rq', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_stdby_adj_join', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info.num_stdby_adj_join', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_stdby_adj_leave', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info.num_stdby_adj_leave', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=979,
  serialized_end=1144,
)

_LDP_NSR_STATS_NBR_INFO.fields_by_name['init_sync_info'].message_type = _LDP_NSR_NBR_SYNCI_INFO
_LDP_NSR_STATS_NBR_INFO.fields_by_name['steady_state_sync_info'].message_type = _LDP_NSR_NBR_SYNCS_INFO
DESCRIPTOR.message_types_by_name['ldp_nsr_stats_nbr_info_KEYS'] = _LDP_NSR_STATS_NBR_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_nsr_stats_nbr_info'] = _LDP_NSR_STATS_NBR_INFO
DESCRIPTOR.message_types_by_name['ldp_nsr_nbr_synci_info'] = _LDP_NSR_NBR_SYNCI_INFO
DESCRIPTOR.message_types_by_name['ldp_nsr_nbr_syncs_info'] = _LDP_NSR_NBR_SYNCS_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_nsr_stats_nbr_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_nsr_stats_nbr_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_STATS_NBR_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_nsr_stats_nbr_info_KEYS)

ldp_nsr_stats_nbr_info = _reflection.GeneratedProtocolMessageType('ldp_nsr_stats_nbr_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_STATS_NBR_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info)
  ))
_sym_db.RegisterMessage(ldp_nsr_stats_nbr_info)

ldp_nsr_nbr_synci_info = _reflection.GeneratedProtocolMessageType('ldp_nsr_nbr_synci_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_NBR_SYNCI_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_synci_info)
  ))
_sym_db.RegisterMessage(ldp_nsr_nbr_synci_info)

ldp_nsr_nbr_syncs_info = _reflection.GeneratedProtocolMessageType('ldp_nsr_nbr_syncs_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_NSR_NBR_SYNCS_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_stats_nbr_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.issu.ha_statistics.ha_neighbors.ha_neighbor.ldp_nsr_nbr_syncs_info)
  ))
_sym_db.RegisterMessage(ldp_nsr_nbr_syncs_info)


# @@protoc_insertion_point(module_scope)
