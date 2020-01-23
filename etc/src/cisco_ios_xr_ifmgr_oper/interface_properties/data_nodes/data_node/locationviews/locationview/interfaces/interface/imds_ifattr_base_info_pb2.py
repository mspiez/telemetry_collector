# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_ifmgr_oper/interface_properties/data_nodes/data_node/locationviews/locationview/interfaces/interface/imds_ifattr_base_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cisco_ios_xr_ifmgr_oper/interface_properties/data_nodes/data_node/locationviews/locationview/interfaces/interface/imds_ifattr_base_info.proto',
  package='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x8d\x01\x63isco_ios_xr_ifmgr_oper/interface_properties/data_nodes/data_node/locationviews/locationview/interfaces/interface/imds_ifattr_base_info.proto\x12qcisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface\"h\n\x1aimds_ifattr_base_info_KEYS\x12\x16\n\x0e\x64\x61ta_node_name\x18\x01 \x01(\t\x12\x1a\n\x12location_view_name\x18\x02 \x01(\t\x12\x16\n\x0einterface_name\x18\x03 \x01(\t\"\xba\x02\n\x15imds_ifattr_base_info\x12\x11\n\tinterface\x18\x32 \x01(\t\x12\x18\n\x10parent_interface\x18\x33 \x01(\t\x12\x0c\n\x04type\x18\x34 \x01(\t\x12\r\n\x05state\x18\x35 \x01(\t\x12\x14\n\x0c\x61\x63tual_state\x18\x36 \x01(\t\x12\x12\n\nline_state\x18\x37 \x01(\t\x12\x19\n\x11\x61\x63tual_line_state\x18\x38 \x01(\t\x12\x15\n\rencapsulation\x18\x39 \x01(\t\x12!\n\x19\x65ncapsulation_type_string\x18: \x01(\t\x12\x0b\n\x03mtu\x18; \x01(\r\x12\"\n\x1asub_interface_mtu_overhead\x18< \x01(\r\x12\x14\n\x0cl2_transport\x18= \x01(\x08\x12\x11\n\tbandwidth\x18> \x01(\rb\x06proto3')
)




_IMDS_IFATTR_BASE_INFO_KEYS = _descriptor.Descriptor(
  name='imds_ifattr_base_info_KEYS',
  full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_node_name', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info_KEYS.data_node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_view_name', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info_KEYS.location_view_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info_KEYS.interface_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=365,
)


_IMDS_IFATTR_BASE_INFO = _descriptor.Descriptor(
  name='imds_ifattr_base_info',
  full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.interface', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_interface', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.parent_interface', index=1,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.type', index=2,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.state', index=3,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_state', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.actual_state', index=4,
      number=54, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line_state', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.line_state', index=5,
      number=55, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_line_state', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.actual_line_state', index=6,
      number=56, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encapsulation', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.encapsulation', index=7,
      number=57, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encapsulation_type_string', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.encapsulation_type_string', index=8,
      number=58, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtu', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.mtu', index=9,
      number=59, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_interface_mtu_overhead', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.sub_interface_mtu_overhead', index=10,
      number=60, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_transport', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.l2_transport', index=11,
      number=61, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bandwidth', full_name='cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info.bandwidth', index=12,
      number=62, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=682,
)

DESCRIPTOR.message_types_by_name['imds_ifattr_base_info_KEYS'] = _IMDS_IFATTR_BASE_INFO_KEYS
DESCRIPTOR.message_types_by_name['imds_ifattr_base_info'] = _IMDS_IFATTR_BASE_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

imds_ifattr_base_info_KEYS = _reflection.GeneratedProtocolMessageType('imds_ifattr_base_info_KEYS', (_message.Message,), {
  'DESCRIPTOR' : _IMDS_IFATTR_BASE_INFO_KEYS,
  '__module__' : 'cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info_KEYS)
  })
_sym_db.RegisterMessage(imds_ifattr_base_info_KEYS)

imds_ifattr_base_info = _reflection.GeneratedProtocolMessageType('imds_ifattr_base_info', (_message.Message,), {
  'DESCRIPTOR' : _IMDS_IFATTR_BASE_INFO,
  '__module__' : 'cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_ifmgr_oper.interface_properties.data_nodes.data_node.locationviews.locationview.interfaces.interface.imds_ifattr_base_info)
  })
_sym_db.RegisterMessage(imds_ifattr_base_info)


# @@protoc_insertion_point(module_scope)
