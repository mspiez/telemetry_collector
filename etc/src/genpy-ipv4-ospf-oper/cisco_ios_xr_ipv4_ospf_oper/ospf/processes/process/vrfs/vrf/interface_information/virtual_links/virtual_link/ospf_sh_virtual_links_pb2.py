# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/interface_information/virtual_links/virtual_link/ospf_sh_virtual_links.proto

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
  name='cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/interface_information/virtual_links/virtual_link/ospf_sh_virtual_links.proto',
  package='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link',
  syntax='proto3',
  serialized_pb=_b('\n\x88\x01\x63isco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/interface_information/virtual_links/virtual_link/ospf_sh_virtual_links.proto\x12lcisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link\"_\n\x1aospf_sh_virtual_links_KEYS\x12\x14\n\x0cprocess_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\x12\x19\n\x11virtual_link_name\x18\x03 \x01(\t\"\xc4\x08\n\x15ospf_sh_virtual_links\x12\x19\n\x11virtual_link_name\x18\x32 \x01(\t\x12 \n\x18virtual_link_neighbor_id\x18\x33 \x01(\t\x12\x1a\n\x12virtual_link_state\x18\x34 \x01(\t\x12#\n\x1bvirtual_link_demand_circuit\x18\x35 \x01(\x08\x12#\n\x1bvirtual_link_dc_bitless_lsa\x18\x36 \x01(\r\x12\x14\n\x0ctransit_area\x18\x37 \x01(\t\x12#\n\x1bvirtual_link_interface_name\x18\x38 \x01(\t\x12\x19\n\x11virtual_link_cost\x18\x39 \x01(\r\x12&\n\x1evirual_link_transmission_delay\x18: \x01(\r\x12#\n\x1bvirtual_link_hello_interval\x18; \x01(\r\x12&\n\x1evirtual_link_hello_interval_ms\x18< \x01(\r\x12\"\n\x1avirtual_link_dead_interval\x18= \x01(\r\x12\"\n\x1avirtual_link_wait_interval\x18> \x01(\r\x12,\n$virtaul_link_retransmission_interval\x18? \x01(\r\x12\x1f\n\x17virtual_link_next_hello\x18@ \x01(\r\x12\"\n\x1avirtual_link_next_hello_ms\x18\x41 \x01(\r\x12\x1c\n\x14virtual_link_passive\x18\x42 \x01(\x08\x12(\n virtual_link_authentication_type\x18\x43 \x01(\t\x12$\n\x1cvirtual_link_youngest_md_key\x18\x44 \x01(\x08\x12\'\n\x1fvirtual_link_youngest_md_key_id\x18\x45 \x01(\r\x12%\n\x1dvirtual_link_old_md_key_count\x18\x46 \x01(\r\x12 \n\x18virtual_link_md_key_list\x18G \x03(\r\x12 \n\x18virtual_link_keychain_id\x18H \x01(\x04\x12 \n\x18virtual_link_nsf_enabled\x18I \x01(\x08\x12\x18\n\x10virtual_link_nsf\x18J \x01(\x08\x12\x1d\n\x15virtual_link_last_nsf\x18K \x01(\r\x12\xa4\x01\n\x15virtual_link_neighbor\x18L \x01(\x0b\x32\x84\x01.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_vlink_neighbor\"\xd3\x05\n\x18ospf_sh_neighbor_retrans\x12 \n\x18\x64\x62\x64_retransmission_count\x18\x01 \x01(\r\x12&\n\x1e\x64\x62\x64_retransmission_total_count\x18\x02 \x01(\r\x12\x1b\n\x13\x61rea_flooding_index\x18\x03 \x01(\r\x12\x16\n\x0e\x61s_flood_index\x18\x04 \x01(\r\x12%\n\x1dneighbor_retransmission_count\x18\x05 \x01(\r\x12!\n\x19number_of_retransmissions\x18\x06 \x01(\r\x12$\n\x1c\x61rea_first_flood_information\x18\x07 \x01(\r\x12*\n\"area_first_flood_information_index\x18\x08 \x01(\r\x12\"\n\x1a\x61s_first_flood_information\x18\t \x01(\r\x12(\n as_first_flood_information_index\x18\n \x01(\r\x12#\n\x1b\x61rea_next_flood_information\x18\x0b \x01(\r\x12)\n!area_next_flood_information_index\x18\x0c \x01(\r\x12!\n\x19\x61s_next_flood_information\x18\r \x01(\r\x12\'\n\x1f\x61s_next_flood_information_index\x18\x0e \x01(\r\x12\"\n\x1alast_retransmission_length\x18\x0f \x01(\r\x12%\n\x1dmaximum_retransmission_length\x18\x10 \x01(\r\x12 \n\x18last_retransmission_time\x18\x11 \x01(\r\x12#\n\x1bmaximum_retransmission_time\x18\x12 \x01(\r\x12 \n\x18lsa_retransmission_timer\x18\x13 \x01(\r\"\x88\x02\n\x16ospf_sh_vlink_neighbor\x12#\n\x1bvirtual_link_suppress_hello\x18\x01 \x01(\x08\x12\x1a\n\x12virtual_link_state\x18\x02 \x01(\t\x12\xac\x01\n\x1bvirtual_link_retransmissoin\x18\x03 \x01(\x0b\x32\x86\x01.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retransb\x06proto3')
)




_OSPF_SH_VIRTUAL_LINKS_KEYS = _descriptor.Descriptor(
  name='ospf_sh_virtual_links_KEYS',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_KEYS.process_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_KEYS.vrf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_KEYS.virtual_link_name', index=2,
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
  serialized_start=251,
  serialized_end=346,
)


_OSPF_SH_VIRTUAL_LINKS = _descriptor.Descriptor(
  name='ospf_sh_virtual_links',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='virtual_link_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_name', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_neighbor_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_neighbor_id', index=1,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_state', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_state', index=2,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_demand_circuit', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_demand_circuit', index=3,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_dc_bitless_lsa', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_dc_bitless_lsa', index=4,
      number=54, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transit_area', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.transit_area', index=5,
      number=55, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_interface_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_interface_name', index=6,
      number=56, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_cost', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_cost', index=7,
      number=57, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virual_link_transmission_delay', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virual_link_transmission_delay', index=8,
      number=58, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_hello_interval', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_hello_interval', index=9,
      number=59, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_hello_interval_ms', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_hello_interval_ms', index=10,
      number=60, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_dead_interval', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_dead_interval', index=11,
      number=61, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_wait_interval', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_wait_interval', index=12,
      number=62, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtaul_link_retransmission_interval', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtaul_link_retransmission_interval', index=13,
      number=63, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_next_hello', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_next_hello', index=14,
      number=64, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_next_hello_ms', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_next_hello_ms', index=15,
      number=65, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_passive', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_passive', index=16,
      number=66, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_authentication_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_authentication_type', index=17,
      number=67, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_youngest_md_key', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_youngest_md_key', index=18,
      number=68, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_youngest_md_key_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_youngest_md_key_id', index=19,
      number=69, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_old_md_key_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_old_md_key_count', index=20,
      number=70, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_md_key_list', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_md_key_list', index=21,
      number=71, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_keychain_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_keychain_id', index=22,
      number=72, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_nsf_enabled', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_nsf_enabled', index=23,
      number=73, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_nsf', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_nsf', index=24,
      number=74, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_last_nsf', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_last_nsf', index=25,
      number=75, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_neighbor', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links.virtual_link_neighbor', index=26,
      number=76, type=11, cpp_type=10, label=1,
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
  serialized_start=349,
  serialized_end=1441,
)


_OSPF_SH_NEIGHBOR_RETRANS = _descriptor.Descriptor(
  name='ospf_sh_neighbor_retrans',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbd_retransmission_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.dbd_retransmission_count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbd_retransmission_total_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.dbd_retransmission_total_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_flooding_index', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.area_flooding_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='as_flood_index', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.as_flood_index', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neighbor_retransmission_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.neighbor_retransmission_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_retransmissions', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.number_of_retransmissions', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_first_flood_information', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.area_first_flood_information', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_first_flood_information_index', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.area_first_flood_information_index', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='as_first_flood_information', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.as_first_flood_information', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='as_first_flood_information_index', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.as_first_flood_information_index', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_next_flood_information', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.area_next_flood_information', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_next_flood_information_index', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.area_next_flood_information_index', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='as_next_flood_information', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.as_next_flood_information', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='as_next_flood_information_index', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.as_next_flood_information_index', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_retransmission_length', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.last_retransmission_length', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_retransmission_length', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.maximum_retransmission_length', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_retransmission_time', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.last_retransmission_time', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_retransmission_time', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.maximum_retransmission_time', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsa_retransmission_timer', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans.lsa_retransmission_timer', index=18,
      number=19, type=13, cpp_type=3, label=1,
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
  serialized_start=1444,
  serialized_end=2167,
)


_OSPF_SH_VLINK_NEIGHBOR = _descriptor.Descriptor(
  name='ospf_sh_vlink_neighbor',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_vlink_neighbor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='virtual_link_suppress_hello', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_vlink_neighbor.virtual_link_suppress_hello', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_state', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_vlink_neighbor.virtual_link_state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_link_retransmissoin', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_vlink_neighbor.virtual_link_retransmissoin', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=2170,
  serialized_end=2434,
)

_OSPF_SH_VIRTUAL_LINKS.fields_by_name['virtual_link_neighbor'].message_type = _OSPF_SH_VLINK_NEIGHBOR
_OSPF_SH_VLINK_NEIGHBOR.fields_by_name['virtual_link_retransmissoin'].message_type = _OSPF_SH_NEIGHBOR_RETRANS
DESCRIPTOR.message_types_by_name['ospf_sh_virtual_links_KEYS'] = _OSPF_SH_VIRTUAL_LINKS_KEYS
DESCRIPTOR.message_types_by_name['ospf_sh_virtual_links'] = _OSPF_SH_VIRTUAL_LINKS
DESCRIPTOR.message_types_by_name['ospf_sh_neighbor_retrans'] = _OSPF_SH_NEIGHBOR_RETRANS
DESCRIPTOR.message_types_by_name['ospf_sh_vlink_neighbor'] = _OSPF_SH_VLINK_NEIGHBOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ospf_sh_virtual_links_KEYS = _reflection.GeneratedProtocolMessageType('ospf_sh_virtual_links_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_VIRTUAL_LINKS_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_KEYS)
  ))
_sym_db.RegisterMessage(ospf_sh_virtual_links_KEYS)

ospf_sh_virtual_links = _reflection.GeneratedProtocolMessageType('ospf_sh_virtual_links', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_VIRTUAL_LINKS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links)
  ))
_sym_db.RegisterMessage(ospf_sh_virtual_links)

ospf_sh_neighbor_retrans = _reflection.GeneratedProtocolMessageType('ospf_sh_neighbor_retrans', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_NEIGHBOR_RETRANS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_neighbor_retrans)
  ))
_sym_db.RegisterMessage(ospf_sh_neighbor_retrans)

ospf_sh_vlink_neighbor = _reflection.GeneratedProtocolMessageType('ospf_sh_vlink_neighbor', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_VLINK_NEIGHBOR,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_virtual_links_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.interface_information.virtual_links.virtual_link.ospf_sh_vlink_neighbor)
  ))
_sym_db.RegisterMessage(ospf_sh_vlink_neighbor)


# @@protoc_insertion_point(module_scope)
