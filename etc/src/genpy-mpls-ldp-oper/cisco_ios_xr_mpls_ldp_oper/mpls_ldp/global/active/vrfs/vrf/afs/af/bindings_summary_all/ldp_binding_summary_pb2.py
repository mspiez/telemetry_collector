# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/bindings_summary_all/ldp_binding_summary.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/bindings_summary_all/ldp_binding_summary.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all',
  syntax='proto3',
  serialized_pb=_b('\npcisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/bindings_summary_all/ldp_binding_summary.proto\x12Vcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all\"=\n\x18ldp_binding_summary_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x66_name\x18\x02 \x01(\t\"\xbd\x04\n\x13ldp_binding_summary\x12q\n\x03vrf\x18\x32 \x01(\x0b\x32\x64.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_vrf_info\x12\x16\n\x0e\x61\x64\x64ress_family\x18\x33 \x01(\t\x12\x7f\n\x07\x62ind_af\x18\x34 \x03(\x0b\x32n.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af\x12\x18\n\x10\x62inding_no_route\x18\x35 \x01(\r\x12\x1e\n\x16\x62inding_local_no_route\x18\x36 \x01(\r\x12\x1a\n\x12\x62inding_local_null\x18\x37 \x01(\r\x12#\n\x1b\x62inding_local_implicit_null\x18\x38 \x01(\r\x12#\n\x1b\x62inding_local_explicit_null\x18\x39 \x01(\r\x12\x1e\n\x16\x62inding_local_non_null\x18: \x01(\r\x12\x19\n\x11\x62inding_local_oor\x18; \x01(\r\x12\x1e\n\x16lowest_allocated_label\x18< \x01(\r\x12\x1f\n\x17highest_allocated_label\x18= \x01(\r\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"\xb6\x01\n\x16ldp_binding_summary_af\x12\x16\n\x0e\x61\x64\x64ress_family\x18\x01 \x01(\t\x12\x17\n\x0flast_lib_update\x18\x02 \x01(\r\x12%\n\x1dlib_minimum_revision_sent_all\x18\x03 \x01(\r\x12\x15\n\rbinding_total\x18\x04 \x01(\r\x12\x15\n\rbinding_local\x18\x05 \x01(\r\x12\x16\n\x0e\x62inding_remote\x18\x06 \x01(\rb\x06proto3')
)




_LDP_BINDING_SUMMARY_KEYS = _descriptor.Descriptor(
  name='ldp_binding_summary_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_KEYS.vrf_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_KEYS.af_name', index=1,
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
  serialized_start=204,
  serialized_end=265,
)


_LDP_BINDING_SUMMARY = _descriptor.Descriptor(
  name='ldp_binding_summary',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.vrf', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_family', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.address_family', index=1,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bind_af', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.bind_af', index=2,
      number=52, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_no_route', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.binding_no_route', index=3,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_local_no_route', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.binding_local_no_route', index=4,
      number=54, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_local_null', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.binding_local_null', index=5,
      number=55, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_local_implicit_null', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.binding_local_implicit_null', index=6,
      number=56, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_local_explicit_null', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.binding_local_explicit_null', index=7,
      number=57, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_local_non_null', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.binding_local_non_null', index=8,
      number=58, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_local_oor', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.binding_local_oor', index=9,
      number=59, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lowest_allocated_label', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.lowest_allocated_label', index=10,
      number=60, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='highest_allocated_label', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary.highest_allocated_label', index=11,
      number=61, type=13, cpp_type=3, label=1,
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
  serialized_start=268,
  serialized_end=841,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_vrf_info.id', index=1,
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
  serialized_start=843,
  serialized_end=883,
)


_LDP_BINDING_SUMMARY_AF = _descriptor.Descriptor(
  name='ldp_binding_summary_af',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_family', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af.address_family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_lib_update', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af.last_lib_update', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lib_minimum_revision_sent_all', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af.lib_minimum_revision_sent_all', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_total', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af.binding_total', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_local', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af.binding_local', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding_remote', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af.binding_remote', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=886,
  serialized_end=1068,
)

_LDP_BINDING_SUMMARY.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
_LDP_BINDING_SUMMARY.fields_by_name['bind_af'].message_type = _LDP_BINDING_SUMMARY_AF
DESCRIPTOR.message_types_by_name['ldp_binding_summary_KEYS'] = _LDP_BINDING_SUMMARY_KEYS
DESCRIPTOR.message_types_by_name['ldp_binding_summary'] = _LDP_BINDING_SUMMARY
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_binding_summary_af'] = _LDP_BINDING_SUMMARY_AF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_binding_summary_KEYS = _reflection.GeneratedProtocolMessageType('ldp_binding_summary_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_BINDING_SUMMARY_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_KEYS)
  ))
_sym_db.RegisterMessage(ldp_binding_summary_KEYS)

ldp_binding_summary = _reflection.GeneratedProtocolMessageType('ldp_binding_summary', (_message.Message,), dict(
  DESCRIPTOR = _LDP_BINDING_SUMMARY,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary)
  ))
_sym_db.RegisterMessage(ldp_binding_summary)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)

ldp_binding_summary_af = _reflection.GeneratedProtocolMessageType('ldp_binding_summary_af', (_message.Message,), dict(
  DESCRIPTOR = _LDP_BINDING_SUMMARY_AF,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.bindings_summary_all.ldp_binding_summary_af)
  ))
_sym_db.RegisterMessage(ldp_binding_summary_af)


# @@protoc_insertion_point(module_scope)
