# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_standby/default_vrf/message_logs/message_log/bgp_msglog_nbr_bag.proto

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
  name='cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_standby/default_vrf/message_logs/message_log/bgp_msglog_nbr_bag.proto',
  package='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log',
  syntax='proto3',
  serialized_pb=_b('\n\x80\x01\x63isco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_standby/default_vrf/message_logs/message_log/bgp_msglog_nbr_bag.proto\x12gcisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log\"]\n\x17\x62gp_msglog_nbr_bag_KEYS\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x18\n\x10neighbor_address\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\r\"\xa7\x01\n\x12\x62gp_msglog_nbr_bag\x12\x90\x01\n\x11neighbor_messages\x18\x32 \x03(\x0b\x32u.cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_\"4\n\x0c\x62gp_timespec\x12\x0f\n\x07seconds\x18\x01 \x01(\r\x12\x13\n\x0bnanoseconds\x18\x02 \x01(\r\"\x9e\x02\n\x0c\x62gp_nbr_msg_\x12\x1d\n\x15message_type_received\x18\x01 \x01(\r\x12\"\n\x1atotal_logged_message_count\x18\x02 \x01(\r\x12\x90\x01\n\x11message_timestamp\x18\x03 \x01(\x0b\x32u.cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_timespec\x12\x1b\n\x13message_data_length\x18\x04 \x01(\r\x12\x1b\n\x13logged_message_data\x18\x05 \x03(\rb\x06proto3')
)




_BGP_MSGLOG_NBR_BAG_KEYS = _descriptor.Descriptor(
  name='bgp_msglog_nbr_bag_KEYS',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_KEYS.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neighbor_address', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_KEYS.neighbor_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_KEYS.direction', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=238,
  serialized_end=331,
)


_BGP_MSGLOG_NBR_BAG = _descriptor.Descriptor(
  name='bgp_msglog_nbr_bag',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='neighbor_messages', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag.neighbor_messages', index=0,
      number=50, type=11, cpp_type=10, label=3,
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
  serialized_start=334,
  serialized_end=501,
)


_BGP_TIMESPEC = _descriptor.Descriptor(
  name='bgp_timespec',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_timespec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_timespec.seconds', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nanoseconds', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_timespec.nanoseconds', index=1,
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
  serialized_start=503,
  serialized_end=555,
)


_BGP_NBR_MSG_ = _descriptor.Descriptor(
  name='bgp_nbr_msg_',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type_received', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_.message_type_received', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_logged_message_count', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_.total_logged_message_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_timestamp', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_.message_timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_data_length', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_.message_data_length', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logged_message_data', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_.logged_message_data', index=4,
      number=5, type=13, cpp_type=3, label=3,
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
  serialized_start=558,
  serialized_end=844,
)

_BGP_MSGLOG_NBR_BAG.fields_by_name['neighbor_messages'].message_type = _BGP_NBR_MSG_
_BGP_NBR_MSG_.fields_by_name['message_timestamp'].message_type = _BGP_TIMESPEC
DESCRIPTOR.message_types_by_name['bgp_msglog_nbr_bag_KEYS'] = _BGP_MSGLOG_NBR_BAG_KEYS
DESCRIPTOR.message_types_by_name['bgp_msglog_nbr_bag'] = _BGP_MSGLOG_NBR_BAG
DESCRIPTOR.message_types_by_name['bgp_timespec'] = _BGP_TIMESPEC
DESCRIPTOR.message_types_by_name['bgp_nbr_msg_'] = _BGP_NBR_MSG_
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

bgp_msglog_nbr_bag_KEYS = _reflection.GeneratedProtocolMessageType('bgp_msglog_nbr_bag_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _BGP_MSGLOG_NBR_BAG_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_KEYS)
  ))
_sym_db.RegisterMessage(bgp_msglog_nbr_bag_KEYS)

bgp_msglog_nbr_bag = _reflection.GeneratedProtocolMessageType('bgp_msglog_nbr_bag', (_message.Message,), dict(
  DESCRIPTOR = _BGP_MSGLOG_NBR_BAG,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag)
  ))
_sym_db.RegisterMessage(bgp_msglog_nbr_bag)

bgp_timespec = _reflection.GeneratedProtocolMessageType('bgp_timespec', (_message.Message,), dict(
  DESCRIPTOR = _BGP_TIMESPEC,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_timespec)
  ))
_sym_db.RegisterMessage(bgp_timespec)

bgp_nbr_msg_ = _reflection.GeneratedProtocolMessageType('bgp_nbr_msg_', (_message.Message,), dict(
  DESCRIPTOR = _BGP_NBR_MSG_,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_msglog_nbr_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_standby.default_vrf.message_logs.message_log.bgp_nbr_msg_)
  ))
_sym_db.RegisterMessage(bgp_nbr_msg_)


# @@protoc_insertion_point(module_scope)
