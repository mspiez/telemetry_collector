# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/border_routers/border_router/ospf_sh_border_router.proto

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
  name='cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/border_routers/border_router/ospf_sh_border_router.proto',
  package='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router',
  syntax='proto3',
  serialized_pb=_b('\ntcisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/border_routers/border_router/ospf_sh_border_router.proto\x12Xcisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router\"^\n\x1aospf_sh_border_router_KEYS\x12\x14\n\x0cprocess_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\x12\x18\n\x10\x62order_router_id\x18\x03 \x01(\t\"\xbe\x01\n\x15ospf_sh_border_router\x12\x18\n\x10\x62order_router_id\x18\x32 \x01(\t\x12\x8a\x01\n\x17\x62order_router_path_list\x18\x33 \x03(\x0b\x32i.cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path\"\xf6\x01\n\x0fospf_sh_br_path\x12 \n\x18\x62order_router_route_type\x18\x01 \x01(\t\x12\"\n\x1a\x62order_router_route_metric\x18\x02 \x01(\r\x12\x1e\n\x16\x62order_router_next_hop\x18\x03 \x01(\t\x12-\n%border_router_next_hop_interface_name\x18\x04 \x01(\t\x12\x1a\n\x12\x62order_router_type\x18\x05 \x01(\t\x12\x1d\n\x15\x62order_router_area_id\x18\x06 \x01(\t\x12\x13\n\x0bspf_version\x18\x07 \x01(\x04\x62\x06proto3')
)




_OSPF_SH_BORDER_ROUTER_KEYS = _descriptor.Descriptor(
  name='ospf_sh_border_router_KEYS',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_KEYS.process_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_KEYS.vrf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_router_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_KEYS.border_router_id', index=2,
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
  serialized_start=210,
  serialized_end=304,
)


_OSPF_SH_BORDER_ROUTER = _descriptor.Descriptor(
  name='ospf_sh_border_router',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='border_router_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router.border_router_id', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_router_path_list', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router.border_router_path_list', index=1,
      number=51, type=11, cpp_type=10, label=3,
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
  serialized_start=307,
  serialized_end=497,
)


_OSPF_SH_BR_PATH = _descriptor.Descriptor(
  name='ospf_sh_br_path',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='border_router_route_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path.border_router_route_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_router_route_metric', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path.border_router_route_metric', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_router_next_hop', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path.border_router_next_hop', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_router_next_hop_interface_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path.border_router_next_hop_interface_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_router_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path.border_router_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_router_area_id', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path.border_router_area_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spf_version', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path.spf_version', index=6,
      number=7, type=4, cpp_type=4, label=1,
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
  serialized_start=500,
  serialized_end=746,
)

_OSPF_SH_BORDER_ROUTER.fields_by_name['border_router_path_list'].message_type = _OSPF_SH_BR_PATH
DESCRIPTOR.message_types_by_name['ospf_sh_border_router_KEYS'] = _OSPF_SH_BORDER_ROUTER_KEYS
DESCRIPTOR.message_types_by_name['ospf_sh_border_router'] = _OSPF_SH_BORDER_ROUTER
DESCRIPTOR.message_types_by_name['ospf_sh_br_path'] = _OSPF_SH_BR_PATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ospf_sh_border_router_KEYS = _reflection.GeneratedProtocolMessageType('ospf_sh_border_router_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_BORDER_ROUTER_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_KEYS)
  ))
_sym_db.RegisterMessage(ospf_sh_border_router_KEYS)

ospf_sh_border_router = _reflection.GeneratedProtocolMessageType('ospf_sh_border_router', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_BORDER_ROUTER,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router)
  ))
_sym_db.RegisterMessage(ospf_sh_border_router)

ospf_sh_br_path = _reflection.GeneratedProtocolMessageType('ospf_sh_br_path', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_BR_PATH,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_border_router_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.border_routers.border_router.ospf_sh_br_path)
  ))
_sym_db.RegisterMessage(ospf_sh_br_path)


# @@protoc_insertion_point(module_scope)
