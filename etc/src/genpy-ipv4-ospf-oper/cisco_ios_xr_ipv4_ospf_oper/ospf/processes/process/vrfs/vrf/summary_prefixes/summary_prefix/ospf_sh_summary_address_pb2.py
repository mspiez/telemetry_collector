# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/summary_prefixes/summary_prefix/ospf_sh_summary_address.proto

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
  name='cisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/summary_prefixes/summary_prefix/ospf_sh_summary_address.proto',
  package='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix',
  syntax='proto3',
  serialized_pb=_b('\nycisco_ios_xr_ipv4_ospf_oper/ospf/processes/process/vrfs/vrf/summary_prefixes/summary_prefix/ospf_sh_summary_address.proto\x12[cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix\"g\n\x1cospf_sh_summary_address_KEYS\x12\x14\n\x0cprocess_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x0f\n\x07netmask\x18\x04 \x01(\t\"\x91\x01\n\x17ospf_sh_summary_address\x12\x16\n\x0esummary_prefix\x18\x32 \x01(\t\x12\x14\n\x0csummary_mask\x18\x33 \x01(\t\x12\x16\n\x0esummary_metric\x18\x34 \x01(\r\x12\x1b\n\x13summary_metric_type\x18\x35 \x01(\t\x12\x13\n\x0bsummary_tag\x18\x36 \x01(\rb\x06proto3')
)




_OSPF_SH_SUMMARY_ADDRESS_KEYS = _descriptor.Descriptor(
  name='ospf_sh_summary_address_KEYS',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_KEYS.process_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_KEYS.vrf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_KEYS.prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='netmask', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_KEYS.netmask', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=218,
  serialized_end=321,
)


_OSPF_SH_SUMMARY_ADDRESS = _descriptor.Descriptor(
  name='ospf_sh_summary_address',
  full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary_prefix', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address.summary_prefix', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary_mask', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address.summary_mask', index=1,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary_metric', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address.summary_metric', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary_metric_type', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address.summary_metric_type', index=3,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary_tag', full_name='cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address.summary_tag', index=4,
      number=54, type=13, cpp_type=3, label=1,
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
  serialized_start=324,
  serialized_end=469,
)

DESCRIPTOR.message_types_by_name['ospf_sh_summary_address_KEYS'] = _OSPF_SH_SUMMARY_ADDRESS_KEYS
DESCRIPTOR.message_types_by_name['ospf_sh_summary_address'] = _OSPF_SH_SUMMARY_ADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ospf_sh_summary_address_KEYS = _reflection.GeneratedProtocolMessageType('ospf_sh_summary_address_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_SUMMARY_ADDRESS_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_KEYS)
  ))
_sym_db.RegisterMessage(ospf_sh_summary_address_KEYS)

ospf_sh_summary_address = _reflection.GeneratedProtocolMessageType('ospf_sh_summary_address', (_message.Message,), dict(
  DESCRIPTOR = _OSPF_SH_SUMMARY_ADDRESS,
  __module__ = 'cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_ospf_oper.ospf.processes.process.vrfs.vrf.summary_prefixes.summary_prefix.ospf_sh_summary_address)
  ))
_sym_db.RegisterMessage(ospf_sh_summary_address)


# @@protoc_insertion_point(module_scope)
