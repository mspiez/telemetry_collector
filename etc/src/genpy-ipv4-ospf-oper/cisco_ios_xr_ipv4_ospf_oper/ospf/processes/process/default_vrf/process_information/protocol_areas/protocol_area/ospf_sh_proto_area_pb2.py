# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/process_information/protocol_areas/protocol_area/ospf_sh_proto_area.proto

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
  name='cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/process_information/protocol_areas/protocol_area/ospf_sh_proto_area.proto',
  package='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area',
  syntax='proto3',
  serialized_pb=_b('\n\x88\x01\x63isco_ios_xr_ipv4_ospf_oper/ospf/processes/process/default_vrf/process_information/protocol_areas/protocol_area/ospf_sh_proto_area.proto\x12ocisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area\"Q\n\x17ospf_sh_proto_area_KEYS\x12\x14\n\x0cprocess_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61rea_id\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"\x89\x02\n\x12ospf_sh_proto_area\x12\x14\n\x0cprotcol_area\x18\x32 \x01(\t\x12\x15\n\rprotocol_mpls\x18\x33 \x01(\x08\x12\"\n\x1aprotocol_area_dist_list_in\x18\x34 \x01(\t\x12\xa1\x01\n\x13protocol_interfaces\x18\x35 \x03(\x0b\x32\x83\x01.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_intf\"\x84\x01\n\x12ospf_sh_proto_intf\x12\x1f\n\x17protocol_interface_name\x18\x01 \x01(\t\x12$\n\x1cprotocol_authentication_type\x18\x02 \x01(\t\x12\'\n\x1fprotocol_interface_dist_list_in\x18\x03 \x01(\tb\x06proto3')
)




_OSPF_SH_PROTO_AREA_KEYS = _descriptor.Descriptor(
  name='ospf_sh_proto_area_KEYS',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_KEYS.process_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_KEYS.area_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_KEYS.address', index=2,
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
  serialized_start=254,
  serialized_end=335,
)


_OSPF_SH_PROTO_AREA = _descriptor.Descriptor(
  name='ospf_sh_proto_area',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protcol_area', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area.protcol_area', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_mpls', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area.protocol_mpls', index=1,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_area_dist_list_in', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area.protocol_area_dist_list_in', index=2,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_interfaces', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area.protocol_interfaces', index=3,
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
  serialized_start=338,
  serialized_end=603,
)


_OSPF_SH_PROTO_INTF = _descriptor.Descriptor(
  name='ospf_sh_proto_intf',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_intf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_interface_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_intf.protocol_interface_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_authentication_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_intf.protocol_authentication_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_interface_dist_list_in', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_intf.protocol_interface_dist_list_in', index=2,
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
  serialized_start=606,
  serialized_end=738,
)

_OSPF_SH_PROTO_AREA.fields_by_name['protocol_interfaces'].message_type = _OSPF_SH_PROTO_INTF
DESCRIPTOR.message_types_by_name['ospf_sh_proto_area_KEYS'] = _OSPF_SH_PROTO_AREA_KEYS
DESCRIPTOR.message_types_by_name['ospf_sh_proto_area'] = _OSPF_SH_PROTO_AREA
DESCRIPTOR.message_types_by_name['ospf_sh_proto_intf'] = _OSPF_SH_PROTO_INTF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ospf_sh_proto_area_KEYS = _reflection.GeneratedProtocolMessageType('ospf_sh_proto_area_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_PROTO_AREA_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_KEYS)
  ))
_sym_db.RegisterMessage(ospf_sh_proto_area_KEYS)

ospf_sh_proto_area = _reflection.GeneratedProtocolMessageType('ospf_sh_proto_area', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_PROTO_AREA,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area)
  ))
_sym_db.RegisterMessage(ospf_sh_proto_area)

ospf_sh_proto_intf = _reflection.GeneratedProtocolMessageType('ospf_sh_proto_intf', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_PROTO_INTF,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_area_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.default_vrf.process_information.protocol_areas.protocol_area.ospf_sh_proto_intf)
  ))
_sym_db.RegisterMessage(ospf_sh_proto_intf)


# @@protoc_insertion_point(module_scope)
