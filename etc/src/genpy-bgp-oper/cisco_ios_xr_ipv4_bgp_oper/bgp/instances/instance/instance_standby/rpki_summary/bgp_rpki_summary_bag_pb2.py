# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_standby/rpki_summary/bgp_rpki_summary_bag.proto

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
  name='cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_standby/rpki_summary/bgp_rpki_summary_bag.proto',
  package='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary',
  syntax='proto3',
  serialized_pb=_b('\njcisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_standby/rpki_summary/bgp_rpki_summary_bag.proto\x12Ocisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary\"2\n\x19\x62gp_rpki_summary_bag_KEYS\x12\x15\n\rinstance_name\x18\x01 \x01(\t\"\xed\x01\n\x14\x62gp_rpki_summary_bag\x12\x0f\n\x07servers\x18\x32 \x01(\r\x12\x15\n\ripv4_roa_nets\x18\x33 \x01(\r\x12\x16\n\x0eipv4_roa_paths\x18\x34 \x01(\r\x12\x15\n\ripv6_roa_nets\x18\x35 \x01(\r\x12\x16\n\x0eipv6_roa_paths\x18\x36 \x01(\r\x12\x15\n\rrpki_disabled\x18\x37 \x01(\x08\x12\x19\n\x11rpki_use_validity\x18\x38 \x01(\x08\x12\x1a\n\x12rpki_allow_invalid\x18\x39 \x01(\x08\x12\x18\n\x10rpki_signal_ibgp\x18: \x01(\x08\x62\x06proto3')
)




_BGP_RPKI_SUMMARY_BAG_KEYS = _descriptor.Descriptor(
  name='bgp_rpki_summary_bag_KEYS',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag_KEYS.instance_name', index=0,
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
  serialized_start=191,
  serialized_end=241,
)


_BGP_RPKI_SUMMARY_BAG = _descriptor.Descriptor(
  name='bgp_rpki_summary_bag',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servers', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.servers', index=0,
      number=50, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv4_roa_nets', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.ipv4_roa_nets', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv4_roa_paths', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.ipv4_roa_paths', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv6_roa_nets', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.ipv6_roa_nets', index=3,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv6_roa_paths', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.ipv6_roa_paths', index=4,
      number=54, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpki_disabled', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.rpki_disabled', index=5,
      number=55, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpki_use_validity', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.rpki_use_validity', index=6,
      number=56, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpki_allow_invalid', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.rpki_allow_invalid', index=7,
      number=57, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpki_signal_ibgp', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag.rpki_signal_ibgp', index=8,
      number=58, type=8, cpp_type=7, label=1,
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
  serialized_start=244,
  serialized_end=481,
)

DESCRIPTOR.message_types_by_name['bgp_rpki_summary_bag_KEYS'] = _BGP_RPKI_SUMMARY_BAG_KEYS
DESCRIPTOR.message_types_by_name['bgp_rpki_summary_bag'] = _BGP_RPKI_SUMMARY_BAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

bgp_rpki_summary_bag_KEYS = _reflection.GeneratedProtocolMessageType('bgp_rpki_summary_bag_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _BGP_RPKI_SUMMARY_BAG_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag_KEYS)
  ))
_sym_db.RegisterMessage(bgp_rpki_summary_bag_KEYS)

bgp_rpki_summary_bag = _reflection.GeneratedProtocolMessageType('bgp_rpki_summary_bag', (_message.Message,), dict(
  DESCRIPTOR = _BGP_RPKI_SUMMARY_BAG,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.rpki_summary.bgp_rpki_summary_bag)
  ))
_sym_db.RegisterMessage(bgp_rpki_summary_bag)


# @@protoc_insertion_point(module_scope)
