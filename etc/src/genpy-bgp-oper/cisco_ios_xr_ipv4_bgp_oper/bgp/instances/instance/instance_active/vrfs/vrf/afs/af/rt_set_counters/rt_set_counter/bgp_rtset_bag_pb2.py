# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/vrfs/vrf/afs/af/rt_set_counters/rt_set_counter/bgp_rtset_bag.proto

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
  name='cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/vrfs/vrf/afs/af/rt_set_counters/rt_set_counter/bgp_rtset_bag.proto',
  package='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter',
  syntax='proto3',
  serialized_pb=_b('\n\x84\x01\x63isco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/vrfs/vrf/afs/af/rt_set_counters/rt_set_counter/bgp_rtset_bag.proto\x12pcisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter\"a\n\x12\x62gp_rtset_bag_KEYS\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x66_name\x18\x03 \x01(\t\x12\x11\n\trt_set_id\x18\x04 \x01(\r\"\xa8\x01\n\rbgp_rtset_bag\x12\x96\x01\n\x10route_target_set\x18\x32 \x01(\x0b\x32|.cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_\"]\n\nbgp_rtset_\x12\x0e\n\x06rt_set\x18\x01 \x03(\r\x12\x12\n\nrt_set_len\x18\x02 \x01(\r\x12\x11\n\trt_set_id\x18\x03 \x01(\r\x12\x18\n\x10rt_set_net_count\x18\x04 \x01(\rb\x06proto3')
)




_BGP_RTSET_BAG_KEYS = _descriptor.Descriptor(
  name='bgp_rtset_bag_KEYS',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_KEYS.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_KEYS.vrf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_KEYS.af_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rt_set_id', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_KEYS.rt_set_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=251,
  serialized_end=348,
)


_BGP_RTSET_BAG = _descriptor.Descriptor(
  name='bgp_rtset_bag',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_target_set', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag.route_target_set', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=351,
  serialized_end=519,
)


_BGP_RTSET_ = _descriptor.Descriptor(
  name='bgp_rtset_',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rt_set', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_.rt_set', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rt_set_len', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_.rt_set_len', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rt_set_id', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_.rt_set_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rt_set_net_count', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_.rt_set_net_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=521,
  serialized_end=614,
)

_BGP_RTSET_BAG.fields_by_name['route_target_set'].message_type = _BGP_RTSET_
DESCRIPTOR.message_types_by_name['bgp_rtset_bag_KEYS'] = _BGP_RTSET_BAG_KEYS
DESCRIPTOR.message_types_by_name['bgp_rtset_bag'] = _BGP_RTSET_BAG
DESCRIPTOR.message_types_by_name['bgp_rtset_'] = _BGP_RTSET_
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

bgp_rtset_bag_KEYS = _reflection.GeneratedProtocolMessageType('bgp_rtset_bag_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _BGP_RTSET_BAG_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_KEYS)
  ))
_sym_db.RegisterMessage(bgp_rtset_bag_KEYS)

bgp_rtset_bag = _reflection.GeneratedProtocolMessageType('bgp_rtset_bag', (_message.Message,), dict(
  DESCRIPTOR = _BGP_RTSET_BAG,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag)
  ))
_sym_db.RegisterMessage(bgp_rtset_bag)

bgp_rtset_ = _reflection.GeneratedProtocolMessageType('bgp_rtset_', (_message.Message,), dict(
  DESCRIPTOR = _BGP_RTSET_,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.vrfs.vrf.afs.af.rt_set_counters.rt_set_counter.bgp_rtset_)
  ))
_sym_db.RegisterMessage(bgp_rtset_)


# @@protoc_insertion_point(module_scope)
