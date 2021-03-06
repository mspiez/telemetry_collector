# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/process_information/protocol_summary/ospf_sh_protocol.proto

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
  name='cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/process_information/protocol_summary/ospf_sh_protocol.proto',
  package='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary',
  syntax='proto3',
  serialized_pb=_b('\nwcisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/process_information/protocol_summary/ospf_sh_protocol.proto\x12`cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary\"?\n\x15ospf_sh_protocol_KEYS\x12\x14\n\x0cprocess_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\"\xcb\x01\n\x10ospf_sh_protocol\x12\x1a\n\x12protocol_router_id\x18\x32 \x01(\t\x12\x19\n\x11protocol_distance\x18\x33 \x01(\r\x12*\n\"administrative_distance_inter_area\x18\x34 \x01(\r\x12(\n administrative_distance_external\x18\x35 \x01(\r\x12\x14\n\x0cprotocol_nsf\x18\x36 \x01(\x08\x12\x14\n\x0c\x64ist_list_in\x18\x37 \x01(\tb\x06proto3')
)




_OSPF_SH_PROTOCOL_KEYS = _descriptor.Descriptor(
  name='ospf_sh_protocol_KEYS',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol_KEYS.process_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol_KEYS.vrf_name', index=1,
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
  serialized_start=221,
  serialized_end=284,
)


_OSPF_SH_PROTOCOL = _descriptor.Descriptor(
  name='ospf_sh_protocol',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_router_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol.protocol_router_id', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_distance', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol.protocol_distance', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='administrative_distance_inter_area', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol.administrative_distance_inter_area', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='administrative_distance_external', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol.administrative_distance_external', index=3,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol_nsf', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol.protocol_nsf', index=4,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dist_list_in', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol.dist_list_in', index=5,
      number=55, type=9, cpp_type=9, label=1,
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
  serialized_start=287,
  serialized_end=490,
)

DESCRIPTOR.message_types_by_name['ospf_sh_protocol_KEYS'] = _OSPF_SH_PROTOCOL_KEYS
DESCRIPTOR.message_types_by_name['ospf_sh_protocol'] = _OSPF_SH_PROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ospf_sh_protocol_KEYS = _reflection.GeneratedProtocolMessageType('ospf_sh_protocol_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_PROTOCOL_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol_KEYS)
  ))
_sym_db.RegisterMessage(ospf_sh_protocol_KEYS)

ospf_sh_protocol = _reflection.GeneratedProtocolMessageType('ospf_sh_protocol', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_PROTOCOL,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.process_information.protocol_summary.ospf_sh_protocol)
  ))
_sym_db.RegisterMessage(ospf_sh_protocol)


# @@protoc_insertion_point(module_scope)
