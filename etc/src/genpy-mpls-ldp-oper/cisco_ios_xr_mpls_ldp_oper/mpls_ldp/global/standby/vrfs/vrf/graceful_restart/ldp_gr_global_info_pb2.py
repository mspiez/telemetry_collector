# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/graceful_restart/ldp_gr_global_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/graceful_restart/ldp_gr_global_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart',
  syntax='proto3',
  serialized_pb=_b('\necisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/standby/vrfs/vrf/graceful_restart/ldp_gr_global_info.proto\x12Lcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart\"+\n\x17ldp_gr_global_info_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\"\xec\x02\n\x12ldp_gr_global_info\x12g\n\x03vrf\x18\x32 \x01(\x0b\x32Z.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_vrf_info\x12.\n&is_forwarding_state_hold_timer_running\x18\x33 \x01(\x08\x12\x35\n-forwarding_state_hold_timer_remaining_seconds\x18\x34 \x01(\r\x12\x85\x01\n\x1egraceful_restartable_neighbors\x18\x35 \x03(\x0b\x32].cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info\"\x1f\n\x0eldp_in6_addr_t\x12\r\n\x05value\x18\x01 \x01(\t\"\xab\x01\n\x13ldp_ip_addr_t_union\x12\x0b\n\x03\x61\x66i\x18\x01 \x01(\t\x12\r\n\x05\x64ummy\x18\x02 \x01(\r\x12\x0c\n\x04ipv4\x18\x03 \x01(\t\x12j\n\x04ipv6\x18\x04 \x01(\x0b\x32\\.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_in6_addr_t\"H\n\x0eldp_ldpid_info\x12\x0e\n\x06lsr_id\x18\x01 \x01(\t\x12\x16\n\x0elabel_space_id\x18\x02 \x01(\r\x12\x0e\n\x06ldp_id\x18\x03 \x01(\t\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"I\n\x15ldp_gr_dnbr_intf_info\x12\x16\n\x0e\x61\x64\x64ress_family\x18\x01 \x01(\t\x12\x18\n\x10interface_handle\x18\x02 \x01(\t\"\x9e\x05\n\x0fldp_gr_nbr_info\x12m\n\x07gr_peer\x18\x01 \x01(\x0b\x32\\.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ldpid_info\x12\x15\n\rconnect_count\x18\x02 \x01(\r\x12\x16\n\x0eis_neighbor_up\x18\x03 \x01(\x08\x12!\n\x19is_liveness_timer_running\x18\x04 \x01(\x08\x12(\n liveness_timer_remaining_seconds\x18\x05 \x01(\r\x12!\n\x19is_recovery_timer_running\x18\x06 \x01(\x08\x12(\n recovery_timer_remaining_seconds\x18\x07 \x01(\r\x12\x80\x01\n\x13\x64own_nbr_interfaces\x18\x08 \x03(\x0b\x32\x63.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_dnbr_intf_info\x12}\n\x12\x64own_nbr_addresses\x18\t \x03(\x0b\x32\x61.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ip_addr_t_union\x12\x1b\n\x13\x64own_nbr_flap_count\x18\n \x01(\r\x12\x16\n\x0e\x64own_nbr_flags\x18\x0b \x01(\r\x12\x1c\n\x14\x64own_nbr_down_reason\x18\x0c \x01(\rb\x06proto3')
)




_LDP_GR_GLOBAL_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_gr_global_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_KEYS.vrf_name', index=0,
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
  serialized_start=183,
  serialized_end=226,
)


_LDP_GR_GLOBAL_INFO = _descriptor.Descriptor(
  name='ldp_gr_global_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info.vrf', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_forwarding_state_hold_timer_running', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info.is_forwarding_state_hold_timer_running', index=1,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forwarding_state_hold_timer_remaining_seconds', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info.forwarding_state_hold_timer_remaining_seconds', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graceful_restartable_neighbors', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info.graceful_restartable_neighbors', index=3,
      number=53, type=11, cpp_type=10, label=3,
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
  serialized_start=229,
  serialized_end=593,
)


_LDP_IN6_ADDR_T = _descriptor.Descriptor(
  name='ldp_in6_addr_t',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_in6_addr_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_in6_addr_t.value', index=0,
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
  serialized_start=595,
  serialized_end=626,
)


_LDP_IP_ADDR_T_UNION = _descriptor.Descriptor(
  name='ldp_ip_addr_t_union',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ip_addr_t_union',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='afi', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ip_addr_t_union.afi', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dummy', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ip_addr_t_union.dummy', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv4', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ip_addr_t_union.ipv4', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv6', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ip_addr_t_union.ipv6', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=629,
  serialized_end=800,
)


_LDP_LDPID_INFO = _descriptor.Descriptor(
  name='ldp_ldpid_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ldpid_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lsr_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ldpid_info.lsr_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_space_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ldpid_info.label_space_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ldp_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ldpid_info.ldp_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=802,
  serialized_end=874,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_vrf_info.id', index=1,
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
  serialized_start=876,
  serialized_end=916,
)


_LDP_GR_DNBR_INTF_INFO = _descriptor.Descriptor(
  name='ldp_gr_dnbr_intf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_dnbr_intf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_family', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_dnbr_intf_info.address_family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_handle', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_dnbr_intf_info.interface_handle', index=1,
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
  serialized_start=918,
  serialized_end=991,
)


_LDP_GR_NBR_INFO = _descriptor.Descriptor(
  name='ldp_gr_nbr_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gr_peer', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.gr_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connect_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.connect_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_neighbor_up', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.is_neighbor_up', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_liveness_timer_running', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.is_liveness_timer_running', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='liveness_timer_remaining_seconds', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.liveness_timer_remaining_seconds', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_recovery_timer_running', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.is_recovery_timer_running', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recovery_timer_remaining_seconds', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.recovery_timer_remaining_seconds', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='down_nbr_interfaces', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.down_nbr_interfaces', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='down_nbr_addresses', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.down_nbr_addresses', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='down_nbr_flap_count', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.down_nbr_flap_count', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='down_nbr_flags', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.down_nbr_flags', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='down_nbr_down_reason', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info.down_nbr_down_reason', index=11,
      number=12, type=13, cpp_type=3, label=1,
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
  serialized_start=994,
  serialized_end=1664,
)

_LDP_GR_GLOBAL_INFO.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
_LDP_GR_GLOBAL_INFO.fields_by_name['graceful_restartable_neighbors'].message_type = _LDP_GR_NBR_INFO
_LDP_IP_ADDR_T_UNION.fields_by_name['ipv6'].message_type = _LDP_IN6_ADDR_T
_LDP_GR_NBR_INFO.fields_by_name['gr_peer'].message_type = _LDP_LDPID_INFO
_LDP_GR_NBR_INFO.fields_by_name['down_nbr_interfaces'].message_type = _LDP_GR_DNBR_INTF_INFO
_LDP_GR_NBR_INFO.fields_by_name['down_nbr_addresses'].message_type = _LDP_IP_ADDR_T_UNION
DESCRIPTOR.message_types_by_name['ldp_gr_global_info_KEYS'] = _LDP_GR_GLOBAL_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_gr_global_info'] = _LDP_GR_GLOBAL_INFO
DESCRIPTOR.message_types_by_name['ldp_in6_addr_t'] = _LDP_IN6_ADDR_T
DESCRIPTOR.message_types_by_name['ldp_ip_addr_t_union'] = _LDP_IP_ADDR_T_UNION
DESCRIPTOR.message_types_by_name['ldp_ldpid_info'] = _LDP_LDPID_INFO
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_gr_dnbr_intf_info'] = _LDP_GR_DNBR_INTF_INFO
DESCRIPTOR.message_types_by_name['ldp_gr_nbr_info'] = _LDP_GR_NBR_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_gr_global_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_gr_global_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_GR_GLOBAL_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_gr_global_info_KEYS)

ldp_gr_global_info = _reflection.GeneratedProtocolMessageType('ldp_gr_global_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_GR_GLOBAL_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info)
  ))
_sym_db.RegisterMessage(ldp_gr_global_info)

ldp_in6_addr_t = _reflection.GeneratedProtocolMessageType('ldp_in6_addr_t', (_message.Message,), dict(
  DESCRIPTOR = _LDP_IN6_ADDR_T,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_in6_addr_t)
  ))
_sym_db.RegisterMessage(ldp_in6_addr_t)

ldp_ip_addr_t_union = _reflection.GeneratedProtocolMessageType('ldp_ip_addr_t_union', (_message.Message,), dict(
  DESCRIPTOR = _LDP_IP_ADDR_T_UNION,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ip_addr_t_union)
  ))
_sym_db.RegisterMessage(ldp_ip_addr_t_union)

ldp_ldpid_info = _reflection.GeneratedProtocolMessageType('ldp_ldpid_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_LDPID_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_ldpid_info)
  ))
_sym_db.RegisterMessage(ldp_ldpid_info)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)

ldp_gr_dnbr_intf_info = _reflection.GeneratedProtocolMessageType('ldp_gr_dnbr_intf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_GR_DNBR_INTF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_dnbr_intf_info)
  ))
_sym_db.RegisterMessage(ldp_gr_dnbr_intf_info)

ldp_gr_nbr_info = _reflection.GeneratedProtocolMessageType('ldp_gr_nbr_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_GR_NBR_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_global_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.standby.vrfs.vrf.graceful_restart.ldp_gr_nbr_info)
  ))
_sym_db.RegisterMessage(ldp_gr_nbr_info)


# @@protoc_insertion_point(module_scope)
