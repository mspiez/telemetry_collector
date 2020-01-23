# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/route_information/backup_routes/backup_route/ospf_sh_topology_backup.proto

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
  name='cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/route_information/backup_routes/backup_route/ospf_sh_topology_backup.proto',
  package='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route',
  syntax='proto3',
  serialized_pb=_b('\n\x89\x01\x63isco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/route_information/backup_routes/backup_route/ospf_sh_topology_backup.proto\x12kcisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route\"[\n\x1cospf_sh_topology_backup_KEYS\x12\x14\n\x0cprocess_name\x18\x01 \x01(\t\x12\x0e\n\x06prefix\x18\x02 \x01(\t\x12\x15\n\rprefix_length\x18\x03 \x01(\r\"\xc6\x03\n\x17ospf_sh_topology_backup\x12\x14\n\x0croute_prefix\x18\x32 \x01(\t\x12\x1b\n\x13route_prefix_length\x18\x33 \x01(\r\x12\x14\n\x0croute_metric\x18\x34 \x01(\r\x12\x12\n\nroute_type\x18\x35 \x01(\t\x12\x17\n\x0froute_connected\x18\x36 \x01(\x08\x12\x93\x01\n\nroute_info\x18\x37 \x01(\x0b\x32\x7f.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common\x12\x9e\x01\n\x0froute_path_list\x18\x38 \x03(\x0b\x32\x84\x01.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup\"2\n\x0cospf_sh_time\x12\x0e\n\x06second\x18\x01 \x01(\r\x12\x12\n\nnanosecond\x18\x02 \x01(\r\"^\n\x0eospf_sh_rep_el\x12\x19\n\x11repair_element_id\x18\x01 \x01(\t\x12\x14\n\x0crepair_label\x18\x02 \x01(\r\x12\x1b\n\x13repair_element_type\x18\x03 \x01(\r\"\x85\x04\n\x13ospf_sh_backup_path\x12#\n\x1b\x62\x61\x63kup_route_interface_name\x18\x01 \x01(\t\x12%\n\x1d\x62\x61\x63kup_route_next_hop_address\x18\x02 \x01(\t\x12\x1b\n\x13\x62\x61\x63kup_route_source\x18\x03 \x01(\t\x12\x15\n\rbackup_metric\x18\x04 \x01(\r\x12\x14\n\x0cprimary_path\x18\x05 \x01(\x08\x12\x1a\n\x12line_card_disjoint\x18\x06 \x01(\x08\x12\x12\n\ndownstream\x18\x07 \x01(\x08\x12\x14\n\x0cnode_protect\x18\x08 \x01(\x08\x12\x15\n\rsrlg_disjoint\x18\t \x01(\x08\x12\x19\n\x11\x62\x61\x63kup_remote_lfa\x18\n \x01(\t\x12\x97\x01\n\x12\x62\x61\x63kup_repair_list\x18\x0b \x03(\x0b\x32{.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_rep_el\x12 \n\x18\x62\x61\x63kup_repair_list_sizei\x18\x0c \x01(\r\x12$\n\x1c\x62\x61\x63kup_tunnel_interface_name\x18\r \x01(\t\"\xa5\x03\n\x17ospf_sh_top_path_backup\x12\x1c\n\x14route_interface_name\x18\x01 \x01(\t\x12\x1e\n\x16route_next_hop_address\x18\x02 \x01(\t\x12\x14\n\x0croute_source\x18\x03 \x01(\t\x12\x13\n\x0broute_lsaid\x18\x04 \x01(\t\x12\"\n\x1aroute_path_is_mcast_intact\x18\x05 \x01(\x08\x12\x1f\n\x17route_path_is_ucmp_path\x18\x06 \x01(\x08\x12\x14\n\x0croute_metric\x18\x07 \x01(\r\x12\x15\n\rroute_path_id\x18\x08 \x01(\r\x12\x10\n\x08lsa_type\x18\t \x01(\r\x12\x9c\x01\n\x11route_backup_path\x18\n \x01(\x0b\x32\x80\x01.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path\"\xde\x04\n\x12ospf_sh_top_common\x12\x15\n\rroute_area_id\x18\x01 \x01(\r\x12\x17\n\x0froute_te_metric\x18\x02 \x01(\r\x12\x19\n\x11route_rib_version\x18\x03 \x01(\r\x12\x19\n\x11route_spf_version\x18\x04 \x01(\x04\x12\x1e\n\x16route_forward_distance\x18\x05 \x01(\r\x12\x14\n\x0croute_source\x18\x06 \x01(\r\x12\x94\x01\n\x11route_update_time\x18\x07 \x01(\x0b\x32y.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_time\x12\x92\x01\n\x0froute_fail_time\x18\x08 \x01(\x0b\x32y.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_time\x12\x1a\n\x12route_spf_priority\x18\t \x01(\r\x12\x1b\n\x13route_auto_excluded\x18\n \x01(\x08\x12$\n\x1croute_srte_prefix_registered\x18\x0b \x01(\x08\x12!\n\x19route_srte_nbr_registered\x18\x0c \x01(\rb\x06proto3')
)




_OSPF_SH_TOPOLOGY_BACKUP_KEYS = _descriptor.Descriptor(
  name='ospf_sh_topology_backup_KEYS',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_KEYS.process_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_KEYS.prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefix_length', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_KEYS.prefix_length', index=2,
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
  serialized_start=251,
  serialized_end=342,
)


_OSPF_SH_TOPOLOGY_BACKUP = _descriptor.Descriptor(
  name='ospf_sh_topology_backup',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_prefix', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup.route_prefix', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_prefix_length', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup.route_prefix_length', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_metric', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup.route_metric', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup.route_type', index=3,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_connected', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup.route_connected', index=4,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_info', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup.route_info', index=5,
      number=55, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_path_list', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup.route_path_list', index=6,
      number=56, type=11, cpp_type=10, label=3,
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
  serialized_start=345,
  serialized_end=799,
)


_OSPF_SH_TIME = _descriptor.Descriptor(
  name='ospf_sh_time',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='second', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_time.second', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nanosecond', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_time.nanosecond', index=1,
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
  serialized_start=801,
  serialized_end=851,
)


_OSPF_SH_REP_EL = _descriptor.Descriptor(
  name='ospf_sh_rep_el',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_rep_el',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repair_element_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_rep_el.repair_element_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repair_label', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_rep_el.repair_label', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repair_element_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_rep_el.repair_element_type', index=2,
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
  serialized_start=853,
  serialized_end=947,
)


_OSPF_SH_BACKUP_PATH = _descriptor.Descriptor(
  name='ospf_sh_backup_path',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backup_route_interface_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_route_interface_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_route_next_hop_address', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_route_next_hop_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_route_source', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_route_source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_metric', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_metric', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary_path', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.primary_path', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_card_disjoint', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.line_card_disjoint', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downstream', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.downstream', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_protect', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.node_protect', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='srlg_disjoint', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.srlg_disjoint', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_remote_lfa', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_remote_lfa', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_repair_list', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_repair_list', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_repair_list_sizei', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_repair_list_sizei', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_tunnel_interface_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path.backup_tunnel_interface_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=950,
  serialized_end=1467,
)


_OSPF_SH_TOP_PATH_BACKUP = _descriptor.Descriptor(
  name='ospf_sh_top_path_backup',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_interface_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_interface_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_next_hop_address', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_next_hop_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_source', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_lsaid', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_lsaid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_path_is_mcast_intact', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_path_is_mcast_intact', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_path_is_ucmp_path', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_path_is_ucmp_path', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_metric', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_metric', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_path_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_path_id', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsa_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.lsa_type', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_backup_path', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup.route_backup_path', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=1470,
  serialized_end=1891,
)


_OSPF_SH_TOP_COMMON = _descriptor.Descriptor(
  name='ospf_sh_top_common',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_area_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_area_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_te_metric', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_te_metric', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_rib_version', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_rib_version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_spf_version', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_spf_version', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_forward_distance', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_forward_distance', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_source', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_source', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_update_time', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_update_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_fail_time', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_fail_time', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_spf_priority', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_spf_priority', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_auto_excluded', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_auto_excluded', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_srte_prefix_registered', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_srte_prefix_registered', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_srte_nbr_registered', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common.route_srte_nbr_registered', index=11,
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
  serialized_start=1894,
  serialized_end=2500,
)

_OSPF_SH_TOPOLOGY_BACKUP.fields_by_name['route_info'].message_type = _OSPF_SH_TOP_COMMON
_OSPF_SH_TOPOLOGY_BACKUP.fields_by_name['route_path_list'].message_type = _OSPF_SH_TOP_PATH_BACKUP
_OSPF_SH_BACKUP_PATH.fields_by_name['backup_repair_list'].message_type = _OSPF_SH_REP_EL
_OSPF_SH_TOP_PATH_BACKUP.fields_by_name['route_backup_path'].message_type = _OSPF_SH_BACKUP_PATH
_OSPF_SH_TOP_COMMON.fields_by_name['route_update_time'].message_type = _OSPF_SH_TIME
_OSPF_SH_TOP_COMMON.fields_by_name['route_fail_time'].message_type = _OSPF_SH_TIME
DESCRIPTOR.message_types_by_name['ospf_sh_topology_backup_KEYS'] = _OSPF_SH_TOPOLOGY_BACKUP_KEYS
DESCRIPTOR.message_types_by_name['ospf_sh_topology_backup'] = _OSPF_SH_TOPOLOGY_BACKUP
DESCRIPTOR.message_types_by_name['ospf_sh_time'] = _OSPF_SH_TIME
DESCRIPTOR.message_types_by_name['ospf_sh_rep_el'] = _OSPF_SH_REP_EL
DESCRIPTOR.message_types_by_name['ospf_sh_backup_path'] = _OSPF_SH_BACKUP_PATH
DESCRIPTOR.message_types_by_name['ospf_sh_top_path_backup'] = _OSPF_SH_TOP_PATH_BACKUP
DESCRIPTOR.message_types_by_name['ospf_sh_top_common'] = _OSPF_SH_TOP_COMMON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ospf_sh_topology_backup_KEYS = _reflection.GeneratedProtocolMessageType('ospf_sh_topology_backup_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_TOPOLOGY_BACKUP_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_KEYS)
  ))
_sym_db.RegisterMessage(ospf_sh_topology_backup_KEYS)

ospf_sh_topology_backup = _reflection.GeneratedProtocolMessageType('ospf_sh_topology_backup', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_TOPOLOGY_BACKUP,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup)
  ))
_sym_db.RegisterMessage(ospf_sh_topology_backup)

ospf_sh_time = _reflection.GeneratedProtocolMessageType('ospf_sh_time', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_TIME,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_time)
  ))
_sym_db.RegisterMessage(ospf_sh_time)

ospf_sh_rep_el = _reflection.GeneratedProtocolMessageType('ospf_sh_rep_el', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_REP_EL,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_rep_el)
  ))
_sym_db.RegisterMessage(ospf_sh_rep_el)

ospf_sh_backup_path = _reflection.GeneratedProtocolMessageType('ospf_sh_backup_path', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_BACKUP_PATH,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_backup_path)
  ))
_sym_db.RegisterMessage(ospf_sh_backup_path)

ospf_sh_top_path_backup = _reflection.GeneratedProtocolMessageType('ospf_sh_top_path_backup', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_TOP_PATH_BACKUP,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_path_backup)
  ))
_sym_db.RegisterMessage(ospf_sh_top_path_backup)

ospf_sh_top_common = _reflection.GeneratedProtocolMessageType('ospf_sh_top_common', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_TOP_COMMON,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_topology_backup_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.route_information.backup_routes.backup_route.ospf_sh_top_common)
  ))
_sym_db.RegisterMessage(ospf_sh_top_common)


# @@protoc_insertion_point(module_scope)
