# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/vrfs/vrf/update_inbound_error_vrf/bgp_upderr_vrf_bag.proto

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
  name='cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/vrfs/vrf/update_inbound_error_vrf/bgp_upderr_vrf_bag.proto',
  package='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf',
  syntax='proto3',
  serialized_pb=_b('\n|cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/vrfs/vrf/update_inbound_error_vrf/bgp_upderr_vrf_bag.proto\x12\x63\x63isco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf\"B\n\x17\x62gp_upderr_vrf_bag_KEYS\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\"\xbe\x02\n\x12\x62gp_upderr_vrf_bag\x12\x17\n\x0fupdate_vrf_name\x18\x32 \x01(\t\x12&\n\x1eupdate_malformed_message_count\x18\x33 \x01(\r\x12\'\n\x1fupdate_malformed_neighbor_count\x18\x34 \x01(\r\x12\x9a\x01\n\x1flast_update_malformed_timestamp\x18\x35 \x01(\x0b\x32q.cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_timespec\x12!\n\x19last_update_malformed_age\x18\x36 \x01(\r\"4\n\x0c\x62gp_timespec\x12\x0f\n\x07seconds\x18\x01 \x01(\r\x12\x13\n\x0bnanoseconds\x18\x02 \x01(\rb\x06proto3')
)




_BGP_UPDERR_VRF_BAG_KEYS = _descriptor.Descriptor(
  name='bgp_upderr_vrf_bag_KEYS',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag_KEYS.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag_KEYS.vrf_name', index=1,
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
  serialized_start=229,
  serialized_end=295,
)


_BGP_UPDERR_VRF_BAG = _descriptor.Descriptor(
  name='bgp_upderr_vrf_bag',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_vrf_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag.update_vrf_name', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_malformed_message_count', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag.update_malformed_message_count', index=1,
      number=51, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_malformed_neighbor_count', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag.update_malformed_neighbor_count', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_update_malformed_timestamp', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag.last_update_malformed_timestamp', index=3,
      number=53, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_update_malformed_age', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag.last_update_malformed_age', index=4,
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
  serialized_start=298,
  serialized_end=616,
)


_BGP_TIMESPEC = _descriptor.Descriptor(
  name='bgp_timespec',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_timespec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_timespec.seconds', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nanoseconds', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_timespec.nanoseconds', index=1,
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
  serialized_start=618,
  serialized_end=670,
)

_BGP_UPDERR_VRF_BAG.fields_by_name['last_update_malformed_timestamp'].message_type = _BGP_TIMESPEC
DESCRIPTOR.message_types_by_name['bgp_upderr_vrf_bag_KEYS'] = _BGP_UPDERR_VRF_BAG_KEYS
DESCRIPTOR.message_types_by_name['bgp_upderr_vrf_bag'] = _BGP_UPDERR_VRF_BAG
DESCRIPTOR.message_types_by_name['bgp_timespec'] = _BGP_TIMESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

bgp_upderr_vrf_bag_KEYS = _reflection.GeneratedProtocolMessageType('bgp_upderr_vrf_bag_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _BGP_UPDERR_VRF_BAG_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag_KEYS)
  ))
_sym_db.RegisterMessage(bgp_upderr_vrf_bag_KEYS)

bgp_upderr_vrf_bag = _reflection.GeneratedProtocolMessageType('bgp_upderr_vrf_bag', (_message.Message,), dict(
  DESCRIPTOR = _BGP_UPDERR_VRF_BAG,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag)
  ))
_sym_db.RegisterMessage(bgp_upderr_vrf_bag)

bgp_timespec = _reflection.GeneratedProtocolMessageType('bgp_timespec', (_message.Message,), dict(
  DESCRIPTOR = _BGP_TIMESPEC,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_upderr_vrf_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.update_inbound_error_vrf.bgp_timespec)
  ))
_sym_db.RegisterMessage(bgp_timespec)


# @@protoc_insertion_point(module_scope)
