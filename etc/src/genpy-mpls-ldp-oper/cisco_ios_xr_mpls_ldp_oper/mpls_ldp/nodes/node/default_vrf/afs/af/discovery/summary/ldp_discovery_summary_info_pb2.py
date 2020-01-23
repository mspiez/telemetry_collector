# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/default_vrf/afs/af/discovery/summary/ldp_discovery_summary_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/default_vrf/afs/af/discovery/summary/ldp_discovery_summary_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary',
  syntax='proto3',
  serialized_pb=_b('\ntcisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/default_vrf/afs/af/discovery/summary/ldp_discovery_summary_info.proto\x12Scisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary\"E\n\x1fldp_discovery_summary_info_KEYS\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x66_name\x18\x02 \x01(\t\"\xab\x04\n\x1aldp_discovery_summary_info\x12n\n\x03vrf\x18\x32 \x01(\x0b\x32\x61.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_vrf_info\x12\x14\n\x0clocal_ldp_id\x18\x33 \x01(\t\x12\x1d\n\x15num_of_ldp_interfaces\x18\x34 \x01(\r\x12$\n\x1cnum_of_active_ldp_interfaces\x18\x35 \x01(\r\x12\x1c\n\x14num_of_lnk_disc_xmit\x18\x36 \x01(\r\x12\x1c\n\x14num_of_tgt_disc_xmit\x18\x37 \x01(\r\x12\x1c\n\x14num_of_lnk_disc_recv\x18\x38 \x01(\r\x12\x1c\n\x14num_of_tgt_disc_recv\x18\x39 \x01(\r\x12&\n\x1enum_of_disc_with_bad_addr_recv\x18: \x01(\r\x12&\n\x1enum_of_disc_with_bad_hello_pdu\x18; \x01(\r\x12\'\n\x1fnum_of_disc_with_bad_xport_addr\x18< \x01(\r\x12\'\n\x1fnum_of_disc_with_same_router_id\x18= \x01(\r\x12(\n num_of_disc_with_wrong_router_id\x18> \x01(\r\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\rb\x06proto3')
)




_LDP_DISCOVERY_SUMMARY_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_discovery_summary_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info_KEYS.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info_KEYS.af_name', index=1,
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
  serialized_start=205,
  serialized_end=274,
)


_LDP_DISCOVERY_SUMMARY_INFO = _descriptor.Descriptor(
  name='ldp_discovery_summary_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.vrf', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_ldp_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.local_ldp_id', index=1,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_ldp_interfaces', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_ldp_interfaces', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_active_ldp_interfaces', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_active_ldp_interfaces', index=3,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_lnk_disc_xmit', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_lnk_disc_xmit', index=4,
      number=54, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_tgt_disc_xmit', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_tgt_disc_xmit', index=5,
      number=55, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_lnk_disc_recv', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_lnk_disc_recv', index=6,
      number=56, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_tgt_disc_recv', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_tgt_disc_recv', index=7,
      number=57, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_disc_with_bad_addr_recv', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_disc_with_bad_addr_recv', index=8,
      number=58, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_disc_with_bad_hello_pdu', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_disc_with_bad_hello_pdu', index=9,
      number=59, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_disc_with_bad_xport_addr', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_disc_with_bad_xport_addr', index=10,
      number=60, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_disc_with_same_router_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_disc_with_same_router_id', index=11,
      number=61, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_of_disc_with_wrong_router_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info.num_of_disc_with_wrong_router_id', index=12,
      number=62, type=13, cpp_type=3, label=1,
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
  serialized_start=277,
  serialized_end=832,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_vrf_info.id', index=1,
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
  serialized_start=834,
  serialized_end=874,
)

_LDP_DISCOVERY_SUMMARY_INFO.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_discovery_summary_info_KEYS'] = _LDP_DISCOVERY_SUMMARY_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_discovery_summary_info'] = _LDP_DISCOVERY_SUMMARY_INFO
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_discovery_summary_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_discovery_summary_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_DISCOVERY_SUMMARY_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_discovery_summary_info_KEYS)

ldp_discovery_summary_info = _reflection.GeneratedProtocolMessageType('ldp_discovery_summary_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_DISCOVERY_SUMMARY_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info)
  ))
_sym_db.RegisterMessage(ldp_discovery_summary_info)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_discovery_summary_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.discovery.summary.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)


# @@protoc_insertion_point(module_scope)
