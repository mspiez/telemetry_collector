# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/label_entries/label_entry/bgp_label_bag.proto

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
  name='cisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/label_entries/label_entry/bgp_label_bag.proto',
  package='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry',
  syntax='proto3',
  serialized_pb=_b('\nocisco_ios_xr_ipv4_bgp_oper/bgp/instances/instance/instance_active/label_entries/label_entry/bgp_label_bag.proto\x12[cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry\":\n\x12\x62gp_label_bag_KEYS\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\r\"\x92\x01\n\rbgp_label_bag\x12\x80\x01\n\x05\x65ntry\x18\x32 \x01(\x0b\x32q.cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_\"\xd0\x01\n\x14\x62gp_edm_label_entry_\x12\r\n\x05label\x18\x01 \x01(\r\x12\x0b\n\x03rds\x18\x02 \x01(\t\x12\x0b\n\x03vrf\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0b\n\x03ip6\x18\x05 \x01(\t\x12\x12\n\nrpc_set_id\x18\x06 \x01(\r\x12\x0f\n\x07masklen\x18\x07 \x01(\r\x12\x0e\n\x06ts_sec\x18\x08 \x01(\r\x12\x0f\n\x07ts_ssec\x18\t \x01(\r\x12\x0c\n\x04info\x18\n \x01(\r\x12\x10\n\x08refcount\x18\x0b \x01(\r\x12\x10\n\x08inactive\x18\x0c \x01(\x08\x62\x06proto3')
)




_BGP_LABEL_BAG_KEYS = _descriptor.Descriptor(
  name='bgp_label_bag_KEYS',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag_KEYS.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag_KEYS.label', index=1,
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
  serialized_start=208,
  serialized_end=266,
)


_BGP_LABEL_BAG = _descriptor.Descriptor(
  name='bgp_label_bag',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag.entry', index=0,
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
  serialized_start=269,
  serialized_end=415,
)


_BGP_EDM_LABEL_ENTRY_ = _descriptor.Descriptor(
  name='bgp_edm_label_entry_',
  full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.label', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rds', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.rds', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.vrf', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip6', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.ip6', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpc_set_id', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.rpc_set_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='masklen', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.masklen', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts_sec', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.ts_sec', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts_ssec', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.ts_ssec', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.info', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refcount', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.refcount', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inactive', full_name='cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_.inactive', index=11,
      number=12, type=8, cpp_type=7, label=1,
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
  serialized_start=418,
  serialized_end=626,
)

_BGP_LABEL_BAG.fields_by_name['entry'].message_type = _BGP_EDM_LABEL_ENTRY_
DESCRIPTOR.message_types_by_name['bgp_label_bag_KEYS'] = _BGP_LABEL_BAG_KEYS
DESCRIPTOR.message_types_by_name['bgp_label_bag'] = _BGP_LABEL_BAG
DESCRIPTOR.message_types_by_name['bgp_edm_label_entry_'] = _BGP_EDM_LABEL_ENTRY_
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

bgp_label_bag_KEYS = _reflection.GeneratedProtocolMessageType('bgp_label_bag_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _BGP_LABEL_BAG_KEYS,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag_KEYS)
  ))
_sym_db.RegisterMessage(bgp_label_bag_KEYS)

bgp_label_bag = _reflection.GeneratedProtocolMessageType('bgp_label_bag', (_message.Message,), dict(
  DESCRIPTOR = _BGP_LABEL_BAG,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag)
  ))
_sym_db.RegisterMessage(bgp_label_bag)

bgp_edm_label_entry_ = _reflection.GeneratedProtocolMessageType('bgp_edm_label_entry_', (_message.Message,), dict(
  DESCRIPTOR = _BGP_EDM_LABEL_ENTRY_,
  __module__ = 'cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_label_bag_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ipv4_bgp_oper.bgp.instances.instance.instance_active.label_entries.label_entry.bgp_edm_label_entry_)
  ))
_sym_db.RegisterMessage(bgp_edm_label_entry_)


# @@protoc_insertion_point(module_scope)
