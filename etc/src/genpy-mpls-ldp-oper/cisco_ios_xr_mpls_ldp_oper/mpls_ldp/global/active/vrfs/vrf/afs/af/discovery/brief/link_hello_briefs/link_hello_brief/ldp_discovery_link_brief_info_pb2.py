# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/discovery/brief/link_hello_briefs/link_hello_brief/ldp_discovery_link_brief_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/discovery/brief/link_hello_briefs/link_hello_brief/ldp_discovery_link_brief_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief',
  syntax='proto3',
  serialized_pb=_b('\n\x98\x01\x63isco_ios_xr_mpls_ldp_oper/mpls_ldp/global/active/vrfs/vrf/afs/af/discovery/brief/link_hello_briefs/link_hello_brief/ldp_discovery_link_brief_info.proto\x12tcisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief\"_\n\"ldp_discovery_link_brief_info_KEYS\x12\x10\n\x08vrf_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x66_name\x18\x02 \x01(\t\x12\x16\n\x0einterface_name\x18\x03 \x01(\t\"\xba\x03\n\x1dldp_discovery_link_brief_info\x12\x90\x01\n\x03vrf\x18\x32 \x01(\x0b\x32\x82\x01.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_vrf_info\x12\x16\n\x0e\x61\x64\x64ress_family\x18\x33 \x01(\t\x12\x1a\n\x12\x61\x64\x64ress_family_set\x18\x34 \x01(\t\x12\x11\n\tinterface\x18\x35 \x01(\t\x12\x16\n\x0einterface_name\x18\x36 \x01(\t\x12\xa6\x01\n\x11hello_information\x18\x37 \x03(\x0b\x32\x8a\x01.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_hello_brief_info\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"^\n\x14ldp_hello_brief_info\x12\x1f\n\x17neighbor_ldp_identifier\x18\x01 \x01(\t\x12\x11\n\thold_time\x18\x02 \x01(\r\x12\x12\n\nsession_up\x18\x03 \x01(\x08\x62\x06proto3')
)




_LDP_DISCOVERY_LINK_BRIEF_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_discovery_link_brief_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_KEYS.vrf_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_KEYS.af_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_KEYS.interface_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=275,
  serialized_end=370,
)


_LDP_DISCOVERY_LINK_BRIEF_INFO = _descriptor.Descriptor(
  name='ldp_discovery_link_brief_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info.vrf', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_family', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info.address_family', index=1,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_family_set', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info.address_family_set', index=2,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info.interface', index=3,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info.interface_name', index=4,
      number=54, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hello_information', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info.hello_information', index=5,
      number=55, type=11, cpp_type=10, label=3,
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
  serialized_start=373,
  serialized_end=815,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_vrf_info.id', index=1,
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
  serialized_start=817,
  serialized_end=857,
)


_LDP_HELLO_BRIEF_INFO = _descriptor.Descriptor(
  name='ldp_hello_brief_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_hello_brief_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='neighbor_ldp_identifier', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_hello_brief_info.neighbor_ldp_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hold_time', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_hello_brief_info.hold_time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_up', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_hello_brief_info.session_up', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=859,
  serialized_end=953,
)

_LDP_DISCOVERY_LINK_BRIEF_INFO.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
_LDP_DISCOVERY_LINK_BRIEF_INFO.fields_by_name['hello_information'].message_type = _LDP_HELLO_BRIEF_INFO
DESCRIPTOR.message_types_by_name['ldp_discovery_link_brief_info_KEYS'] = _LDP_DISCOVERY_LINK_BRIEF_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_discovery_link_brief_info'] = _LDP_DISCOVERY_LINK_BRIEF_INFO
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_hello_brief_info'] = _LDP_HELLO_BRIEF_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_discovery_link_brief_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_discovery_link_brief_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_DISCOVERY_LINK_BRIEF_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_discovery_link_brief_info_KEYS)

ldp_discovery_link_brief_info = _reflection.GeneratedProtocolMessageType('ldp_discovery_link_brief_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_DISCOVERY_LINK_BRIEF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info)
  ))
_sym_db.RegisterMessage(ldp_discovery_link_brief_info)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)

ldp_hello_brief_info = _reflection.GeneratedProtocolMessageType('ldp_hello_brief_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_HELLO_BRIEF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_discovery_link_brief_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.global.active.vrfs.vrf.afs.af.discovery.brief.link_hello_briefs.link_hello_brief.ldp_hello_brief_info)
  ))
_sym_db.RegisterMessage(ldp_hello_brief_info)


# @@protoc_insertion_point(module_scope)
