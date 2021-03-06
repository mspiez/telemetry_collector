# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/nd_virtual_routers/nd_virtual_router/ipv6_nd_vr_entry.proto

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
  name='cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/nd_virtual_routers/nd_virtual_router/ipv6_nd_vr_entry.proto',
  package='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router',
  syntax='proto3',
  serialized_pb=_b('\ntcisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/nd_virtual_routers/nd_virtual_router/ipv6_nd_vr_entry.proto\x12]cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router\"B\n\x15ipv6_nd_vr_entry_KEYS\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x16\n\x0einterface_name\x18\x02 \x01(\t\"\x87\x03\n\x10ipv6_nd_vr_entry\x12\x1a\n\x12link_layer_address\x18\x32 \x01(\t\x12\x82\x01\n\rlocal_address\x18\x33 \x01(\x0b\x32k.cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_addr\x12\x0f\n\x07\x63ontext\x18\x34 \x01(\r\x12\r\n\x05state\x18\x35 \x01(\t\x12\r\n\x05\x66lags\x18\x36 \x01(\t\x12\x15\n\rvr_gl_addr_ct\x18\x37 \x01(\r\x12\x8b\x01\n\x16vr_global_address_list\x18\x38 \x03(\x0b\x32k.cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_addr\"$\n\x0cipv6_nd_addr\x12\x14\n\x0cipv6_address\x18\x01 \x01(\tb\x06proto3')
)




_IPV6_ND_VR_ENTRY_KEYS = _descriptor.Descriptor(
  name='ipv6_nd_vr_entry_KEYS',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry_KEYS.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry_KEYS.interface_name', index=1,
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
  serialized_start=215,
  serialized_end=281,
)


_IPV6_ND_VR_ENTRY = _descriptor.Descriptor(
  name='ipv6_nd_vr_entry',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_layer_address', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry.link_layer_address', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_address', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry.local_address', index=1,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry.context', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry.state', index=3,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry.flags', index=4,
      number=54, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vr_gl_addr_ct', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry.vr_gl_addr_ct', index=5,
      number=55, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vr_global_address_list', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry.vr_global_address_list', index=6,
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
  serialized_start=284,
  serialized_end=675,
)


_IPV6_ND_ADDR = _descriptor.Descriptor(
  name='ipv6_nd_addr',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_addr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipv6_address', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_addr.ipv6_address', index=0,
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
  serialized_start=677,
  serialized_end=713,
)

_IPV6_ND_VR_ENTRY.fields_by_name['local_address'].message_type = _IPV6_ND_ADDR
_IPV6_ND_VR_ENTRY.fields_by_name['vr_global_address_list'].message_type = _IPV6_ND_ADDR
DESCRIPTOR.message_types_by_name['ipv6_nd_vr_entry_KEYS'] = _IPV6_ND_VR_ENTRY_KEYS
DESCRIPTOR.message_types_by_name['ipv6_nd_vr_entry'] = _IPV6_ND_VR_ENTRY
DESCRIPTOR.message_types_by_name['ipv6_nd_addr'] = _IPV6_ND_ADDR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ipv6_nd_vr_entry_KEYS = _reflection.GeneratedProtocolMessageType('ipv6_nd_vr_entry_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _IPV6_ND_VR_ENTRY_KEYS,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry_KEYS)
  ))
_sym_db.RegisterMessage(ipv6_nd_vr_entry_KEYS)

ipv6_nd_vr_entry = _reflection.GeneratedProtocolMessageType('ipv6_nd_vr_entry', (_message.Message,), dict(
  DESCRIPTOR = _IPV6_ND_VR_ENTRY,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry)
  ))
_sym_db.RegisterMessage(ipv6_nd_vr_entry)

ipv6_nd_addr = _reflection.GeneratedProtocolMessageType('ipv6_nd_addr', (_message.Message,), dict(
  DESCRIPTOR = _IPV6_ND_ADDR,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_vr_entry_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.nd_virtual_routers.nd_virtual_router.ipv6_nd_addr)
  ))
_sym_db.RegisterMessage(ipv6_nd_addr)


# @@protoc_insertion_point(module_scope)
