# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/interfaces/interface/ipv6_nd_if_params.proto

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
  name='cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/interfaces/interface/ipv6_nd_if_params.proto',
  package='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface',
  syntax='proto3',
  serialized_pb=_b('\necisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/interfaces/interface/ipv6_nd_if_params.proto\x12Mcisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface\"C\n\x16ipv6_nd_if_params_KEYS\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x16\n\x0einterface_name\x18\x02 \x01(\t\"\xb1\x04\n\x11ipv6_nd_if_params\x12\x16\n\x0eis_dad_enabled\x18\x32 \x01(\x08\x12\x14\n\x0c\x64\x61\x64_attempts\x18\x33 \x01(\r\x12\x1b\n\x13is_icm_pv6_redirect\x18\x34 \x01(\x08\x12\x17\n\x0fis_dhcp_managed\x18\x35 \x01(\x08\x12 \n\x18is_route_address_managed\x18\x36 \x01(\x08\x12\x15\n\ris_suppressed\x18\x37 \x01(\x08\x12\x1e\n\x16nd_retransmit_interval\x18\x38 \x01(\r\x12 \n\x18nd_min_transmit_interval\x18\x39 \x01(\r\x12 \n\x18nd_max_transmit_interval\x18: \x01(\r\x12!\n\x19nd_advertisement_lifetime\x18; \x01(\r\x12\x19\n\x11nd_reachable_time\x18< \x01(\r\x12\x16\n\x0end_cache_limit\x18= \x01(\r\x12\x1f\n\x17\x63omplete_protocol_count\x18> \x01(\r\x12\x1c\n\x14\x63omplete_glean_count\x18? \x01(\r\x12!\n\x19incomplete_protocol_count\x18@ \x01(\r\x12\x1e\n\x16incomplete_glean_count\x18\x41 \x01(\r\x12\"\n\x1a\x64ropped_protocol_req_count\x18\x42 \x01(\r\x12\x1f\n\x17\x64ropped_glean_req_count\x18\x43 \x01(\rb\x06proto3')
)




_IPV6_ND_IF_PARAMS_KEYS = _descriptor.Descriptor(
  name='ipv6_nd_if_params_KEYS',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params_KEYS.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params_KEYS.interface_name', index=1,
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
  serialized_start=184,
  serialized_end=251,
)


_IPV6_ND_IF_PARAMS = _descriptor.Descriptor(
  name='ipv6_nd_if_params',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_dad_enabled', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.is_dad_enabled', index=0,
      number=50, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dad_attempts', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.dad_attempts', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_icm_pv6_redirect', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.is_icm_pv6_redirect', index=2,
      number=52, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_dhcp_managed', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.is_dhcp_managed', index=3,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_route_address_managed', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.is_route_address_managed', index=4,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_suppressed', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.is_suppressed', index=5,
      number=55, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nd_retransmit_interval', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.nd_retransmit_interval', index=6,
      number=56, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nd_min_transmit_interval', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.nd_min_transmit_interval', index=7,
      number=57, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nd_max_transmit_interval', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.nd_max_transmit_interval', index=8,
      number=58, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nd_advertisement_lifetime', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.nd_advertisement_lifetime', index=9,
      number=59, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nd_reachable_time', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.nd_reachable_time', index=10,
      number=60, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nd_cache_limit', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.nd_cache_limit', index=11,
      number=61, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complete_protocol_count', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.complete_protocol_count', index=12,
      number=62, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complete_glean_count', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.complete_glean_count', index=13,
      number=63, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incomplete_protocol_count', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.incomplete_protocol_count', index=14,
      number=64, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incomplete_glean_count', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.incomplete_glean_count', index=15,
      number=65, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropped_protocol_req_count', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.dropped_protocol_req_count', index=16,
      number=66, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropped_glean_req_count', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params.dropped_glean_req_count', index=17,
      number=67, type=13, cpp_type=3, label=1,
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
  serialized_start=254,
  serialized_end=815,
)

DESCRIPTOR.message_types_by_name['ipv6_nd_if_params_KEYS'] = _IPV6_ND_IF_PARAMS_KEYS
DESCRIPTOR.message_types_by_name['ipv6_nd_if_params'] = _IPV6_ND_IF_PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ipv6_nd_if_params_KEYS = _reflection.GeneratedProtocolMessageType('ipv6_nd_if_params_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _IPV6_ND_IF_PARAMS_KEYS,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params_KEYS)
  ))
_sym_db.RegisterMessage(ipv6_nd_if_params_KEYS)

ipv6_nd_if_params = _reflection.GeneratedProtocolMessageType('ipv6_nd_if_params', (_message.Message,), dict(
  DESCRIPTOR = _IPV6_ND_IF_PARAMS,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.interfaces.interface.ipv6_nd_if_params)
  ))
_sym_db.RegisterMessage(ipv6_nd_if_params)


# @@protoc_insertion_point(module_scope)
