# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/neighbor_summary/ipv6_nd_neighbor_entry_summary.proto

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
  name='cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/neighbor_summary/ipv6_nd_neighbor_entry_summary.proto',
  package='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary',
  syntax='proto3',
  serialized_pb=_b('\nncisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/neighbor_summary/ipv6_nd_neighbor_entry_summary.proto\x12Icisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary\"8\n#ipv6_nd_neighbor_entry_summary_KEYS\x12\x11\n\tnode_name\x18\x01 \x01(\t\"\x8e\x03\n\x1eipv6_nd_neighbor_entry_summary\x12o\n\tmulticast\x18\x32 \x01(\x0b\x32\\.cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum\x12l\n\x06static\x18\x33 \x01(\x0b\x32\\.cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum\x12m\n\x07\x64ynamic\x18\x34 \x01(\x0b\x32\\.cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum\x12\x1e\n\x16total_neighbor_entries\x18\x35 \x01(\r\"\xcd\x01\n\x11\x62\x61g_nbr_entry_sum\x12\x1a\n\x12incomplete_entries\x18\x01 \x01(\r\x12\x19\n\x11reachable_entries\x18\x02 \x01(\r\x12\x15\n\rstale_entries\x18\x03 \x01(\r\x12\x17\n\x0f\x64\x65layed_entries\x18\x04 \x01(\r\x12\x15\n\rprobe_entries\x18\x05 \x01(\r\x12\x17\n\x0f\x64\x65leted_entries\x18\x06 \x01(\r\x12!\n\x19subtotal_neighbor_entries\x18\x07 \x01(\rb\x06proto3')
)




_IPV6_ND_NEIGHBOR_ENTRY_SUMMARY_KEYS = _descriptor.Descriptor(
  name='ipv6_nd_neighbor_entry_summary_KEYS',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary_KEYS.node_name', index=0,
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
  serialized_start=189,
  serialized_end=245,
)


_IPV6_ND_NEIGHBOR_ENTRY_SUMMARY = _descriptor.Descriptor(
  name='ipv6_nd_neighbor_entry_summary',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='multicast', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary.multicast', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='static', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary.static', index=1,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dynamic', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary.dynamic', index=2,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_neighbor_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary.total_neighbor_entries', index=3,
      number=53, type=13, cpp_type=3, label=1,
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
  serialized_start=248,
  serialized_end=646,
)


_BAG_NBR_ENTRY_SUM = _descriptor.Descriptor(
  name='bag_nbr_entry_sum',
  full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incomplete_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum.incomplete_entries', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reachable_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum.reachable_entries', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stale_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum.stale_entries', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delayed_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum.delayed_entries', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probe_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum.probe_entries', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum.deleted_entries', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subtotal_neighbor_entries', full_name='cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum.subtotal_neighbor_entries', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=649,
  serialized_end=854,
)

_IPV6_ND_NEIGHBOR_ENTRY_SUMMARY.fields_by_name['multicast'].message_type = _BAG_NBR_ENTRY_SUM
_IPV6_ND_NEIGHBOR_ENTRY_SUMMARY.fields_by_name['static'].message_type = _BAG_NBR_ENTRY_SUM
_IPV6_ND_NEIGHBOR_ENTRY_SUMMARY.fields_by_name['dynamic'].message_type = _BAG_NBR_ENTRY_SUM
DESCRIPTOR.message_types_by_name['ipv6_nd_neighbor_entry_summary_KEYS'] = _IPV6_ND_NEIGHBOR_ENTRY_SUMMARY_KEYS
DESCRIPTOR.message_types_by_name['ipv6_nd_neighbor_entry_summary'] = _IPV6_ND_NEIGHBOR_ENTRY_SUMMARY
DESCRIPTOR.message_types_by_name['bag_nbr_entry_sum'] = _BAG_NBR_ENTRY_SUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ipv6_nd_neighbor_entry_summary_KEYS = _reflection.GeneratedProtocolMessageType('ipv6_nd_neighbor_entry_summary_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _IPV6_ND_NEIGHBOR_ENTRY_SUMMARY_KEYS,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary_KEYS)
  ))
_sym_db.RegisterMessage(ipv6_nd_neighbor_entry_summary_KEYS)

ipv6_nd_neighbor_entry_summary = _reflection.GeneratedProtocolMessageType('ipv6_nd_neighbor_entry_summary', (_message.Message,), dict(
  DESCRIPTOR = _IPV6_ND_NEIGHBOR_ENTRY_SUMMARY,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary)
  ))
_sym_db.RegisterMessage(ipv6_nd_neighbor_entry_summary)

bag_nbr_entry_sum = _reflection.GeneratedProtocolMessageType('bag_nbr_entry_sum', (_message.Message,), dict(
  DESCRIPTOR = _BAG_NBR_ENTRY_SUM,
  __module__ = 'cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.ipv6_nd_neighbor_entry_summary_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv6_nd_oper.ipv6_node_discovery.nodes.node.neighbor_summary.bag_nbr_entry_sum)
  ))
_sym_db.RegisterMessage(bag_nbr_entry_sum)


# @@protoc_insertion_point(module_scope)