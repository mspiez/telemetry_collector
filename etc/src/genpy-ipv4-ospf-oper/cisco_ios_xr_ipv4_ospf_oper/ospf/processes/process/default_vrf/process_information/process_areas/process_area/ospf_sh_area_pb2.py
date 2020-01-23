# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/process_information/process_areas/process_area/ospf_sh_area.proto

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
  name='cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/process_information/process_areas/process_area/ospf_sh_area.proto',
  package='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area',
  syntax='proto3',
  serialized_pb=_b('\n\x80\x01\x63isco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/process_information/process_areas/process_area/ospf_sh_area.proto\x12mcisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area\"K\n\x11ospf_sh_area_KEYS\x12\x14\n\x0cprocess_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61rea_id\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"\x8c\t\n\x0cospf_sh_area\x12\x16\n\x0e\x61rea_id_string\x18\x32 \x01(\t\x12\x1c\n\x14\x62\x61\x63kbone_area_active\x18\x33 \x01(\x08\x12\x1c\n\x14\x61rea_interface_count\x18\x34 \x01(\r\x12\x11\n\tarea_stub\x18\x35 \x01(\x08\x12\x17\n\x0f\x61rea_total_stub\x18\x36 \x01(\x08\x12\x19\n\x11stub_default_cost\x18\x37 \x01(\r\x12\x11\n\tarea_nssa\x18\x38 \x01(\x08\x12\x1e\n\x16nssa_no_redistribution\x18\x39 \x01(\x08\x12\x16\n\x0enssa_translate\x18: \x01(\x08\x12\x14\n\x0cnssa_default\x18; \x01(\x08\x12\x12\n\nte_enabled\x18< \x01(\x08\x12\x1b\n\x13te_topology_version\x18= \x01(\r\x12\x14\n\x0c\x65xternal_out\x18> \x01(\x08\x12\x12\n\nsummary_in\x18? \x01(\x08\x12\x17\n\x0fsegment_routing\x18@ \x01(\r\x12\x19\n\x11sr_strict_spf_cap\x18\x41 \x01(\x08\x12$\n\x1csr_strict_spfsi_ds_available\x18\x42 \x01(\x08\x12\x1b\n\x13\x61uthentication_type\x18\x43 \x01(\t\x12\x11\n\tspf_count\x18\x44 \x01(\r\x12\x16\n\x0e\x61rea_policy_in\x18\x45 \x01(\x08\x12\x1b\n\x13\x61rea_policy_in_name\x18\x46 \x01(\t\x12\x17\n\x0f\x61rea_policy_out\x18G \x01(\x08\x12\x1c\n\x14\x61rea_policy_out_name\x18H \x01(\t\x12\x9b\x01\n\x0f\x61rea_range_list\x18I \x03(\x0b\x32\x81\x01.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_range\x12\x16\n\x0e\x61rea_lsa_count\x18J \x01(\r\x12\x19\n\x11\x61rea_lsa_checksum\x18K \x01(\r\x12\x1d\n\x15\x61rea_opaque_lsa_count\x18L \x01(\r\x12 \n\x18\x61rea_opaque_lsa_checksum\x18M \x01(\r\x12!\n\x19\x61rea_dc_bitless_lsa_count\x18N \x01(\r\x12\x1c\n\x14indication_lsa_count\x18O \x01(\r\x12\x15\n\rdna_lsa_count\x18P \x01(\r\x12\x19\n\x11\x66lood_list_length\x18Q \x01(\r\x12 \n\x18\x61rea_lfa_interface_count\x18R \x01(\r\x12+\n#area_per_prefix_lfa_interface_count\x18S \x01(\r\x12\x19\n\x11\x61rea_lfa_revision\x18T \x01(\r\x12%\n\x1d\x61rea_adj_stag_num_nbr_forming\x18U \x01(\r\x12\x19\n\x11\x61rea_num_nbr_full\x18V \x01(\r\"d\n\x12ospf_sh_area_range\x12\x14\n\x0crange_prefix\x18\x01 \x01(\t\x12\x12\n\nrange_mask\x18\x02 \x01(\t\x12\x0c\n\x04\x63ost\x18\x03 \x01(\r\x12\x16\n\x0e\x61\x64vertise_flag\x18\x04 \x01(\x08\x62\x06proto3')
)




_OSPF_SH_AREA_KEYS = _descriptor.Descriptor(
  name='ospf_sh_area_KEYS',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_KEYS.process_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_KEYS.area_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_KEYS.address', index=2,
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
  serialized_start=244,
  serialized_end=319,
)


_OSPF_SH_AREA = _descriptor.Descriptor(
  name='ospf_sh_area',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='area_id_string', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_id_string', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backbone_area_active', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.backbone_area_active', index=1,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_interface_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_interface_count', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_stub', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_stub', index=3,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_total_stub', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_total_stub', index=4,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stub_default_cost', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.stub_default_cost', index=5,
      number=55, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_nssa', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_nssa', index=6,
      number=56, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nssa_no_redistribution', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.nssa_no_redistribution', index=7,
      number=57, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nssa_translate', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.nssa_translate', index=8,
      number=58, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nssa_default', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.nssa_default', index=9,
      number=59, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='te_enabled', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.te_enabled', index=10,
      number=60, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='te_topology_version', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.te_topology_version', index=11,
      number=61, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_out', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.external_out', index=12,
      number=62, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary_in', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.summary_in', index=13,
      number=63, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segment_routing', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.segment_routing', index=14,
      number=64, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sr_strict_spf_cap', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.sr_strict_spf_cap', index=15,
      number=65, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sr_strict_spfsi_ds_available', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.sr_strict_spfsi_ds_available', index=16,
      number=66, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authentication_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.authentication_type', index=17,
      number=67, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spf_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.spf_count', index=18,
      number=68, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_policy_in', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_policy_in', index=19,
      number=69, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_policy_in_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_policy_in_name', index=20,
      number=70, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_policy_out', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_policy_out', index=21,
      number=71, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_policy_out_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_policy_out_name', index=22,
      number=72, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_range_list', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_range_list', index=23,
      number=73, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_lsa_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_lsa_count', index=24,
      number=74, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_lsa_checksum', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_lsa_checksum', index=25,
      number=75, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_opaque_lsa_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_opaque_lsa_count', index=26,
      number=76, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_opaque_lsa_checksum', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_opaque_lsa_checksum', index=27,
      number=77, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_dc_bitless_lsa_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_dc_bitless_lsa_count', index=28,
      number=78, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indication_lsa_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.indication_lsa_count', index=29,
      number=79, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dna_lsa_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.dna_lsa_count', index=30,
      number=80, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flood_list_length', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.flood_list_length', index=31,
      number=81, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_lfa_interface_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_lfa_interface_count', index=32,
      number=82, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_per_prefix_lfa_interface_count', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_per_prefix_lfa_interface_count', index=33,
      number=83, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_lfa_revision', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_lfa_revision', index=34,
      number=84, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_adj_stag_num_nbr_forming', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_adj_stag_num_nbr_forming', index=35,
      number=85, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_num_nbr_full', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area.area_num_nbr_full', index=36,
      number=86, type=13, cpp_type=3, label=1,
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
  serialized_start=322,
  serialized_end=1486,
)


_OSPF_SH_AREA_RANGE = _descriptor.Descriptor(
  name='ospf_sh_area_range',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='range_prefix', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_range.range_prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_mask', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_range.range_mask', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_range.cost', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='advertise_flag', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_range.advertise_flag', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1488,
  serialized_end=1588,
)

_OSPF_SH_AREA.fields_by_name['area_range_list'].message_type = _OSPF_SH_AREA_RANGE
DESCRIPTOR.message_types_by_name['ospf_sh_area_KEYS'] = _OSPF_SH_AREA_KEYS
DESCRIPTOR.message_types_by_name['ospf_sh_area'] = _OSPF_SH_AREA
DESCRIPTOR.message_types_by_name['ospf_sh_area_range'] = _OSPF_SH_AREA_RANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ospf_sh_area_KEYS = _reflection.GeneratedProtocolMessageType('ospf_sh_area_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_AREA_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_KEYS)
  ))
_sym_db.RegisterMessage(ospf_sh_area_KEYS)

ospf_sh_area = _reflection.GeneratedProtocolMessageType('ospf_sh_area', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_AREA,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area)
  ))
_sym_db.RegisterMessage(ospf_sh_area)

ospf_sh_area_range = _reflection.GeneratedProtocolMessageType('ospf_sh_area_range', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_AREA_RANGE,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.process_areas.process_area.ospf_sh_area_range)
  ))
_sym_db.RegisterMessage(ospf_sh_area_range)


# @@protoc_insertion_point(module_scope)
