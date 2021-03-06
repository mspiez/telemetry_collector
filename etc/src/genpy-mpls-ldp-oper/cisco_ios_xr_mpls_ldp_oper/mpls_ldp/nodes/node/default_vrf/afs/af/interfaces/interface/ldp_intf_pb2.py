# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/default_vrf/afs/af/interfaces/interface/ldp_intf.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/default_vrf/afs/af/interfaces/interface/ldp_intf.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface',
  syntax='proto3',
  serialized_pb=_b('\necisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/default_vrf/afs/af/interfaces/interface/ldp_intf.proto\x12Vcisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface\"K\n\rldp_intf_KEYS\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x66_name\x18\x02 \x01(\t\x12\x16\n\x0einterface_name\x18\x03 \x01(\t\"\x8e\x04\n\x08ldp_intf\x12\x11\n\tinterface\x18\x32 \x01(\t\x12\x16\n\x0einterface_name\x18\x33 \x01(\t\x12q\n\x03vrf\x18\x34 \x01(\x0b\x32\x64.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_vrf_info\x12\x13\n\x0bldp_enabled\x18\x35 \x01(\x08\x12\x13\n\x0bis_im_stale\x18\x36 \x01(\x08\x12\x17\n\x0fldp_config_mode\x18\x37 \x01(\x08\x12\x1e\n\x16ldp_autoconfig_disable\x18\x38 \x01(\x08\x12\x81\x01\n\x0bte_mesh_grp\x18\x39 \x03(\x0b\x32l.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_te_mesh_grp\x12}\n\x0b\x61uto_config\x18: \x03(\x0b\x32h.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_autocfg\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"!\n\x10ldp_intf_autocfg\x12\r\n\x05tuple\x18\x01 \x01(\t\"t\n\x14ldp_intf_te_mesh_grp\x12\"\n\x1aldp_te_mesh_group_all_cfgd\x18\x01 \x01(\x08\x12\x1e\n\x16ldp_mesh_group_enabled\x18\x02 \x01(\x08\x12\x18\n\x10te_mesh_group_id\x18\x03 \x01(\rb\x06proto3')
)




_LDP_INTF_KEYS = _descriptor.Descriptor(
  name='ldp_intf_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_KEYS.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_KEYS.af_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_KEYS.interface_name', index=2,
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
  serialized_start=193,
  serialized_end=268,
)


_LDP_INTF = _descriptor.Descriptor(
  name='ldp_intf',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.interface', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.interface_name', index=1,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.vrf', index=2,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ldp_enabled', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.ldp_enabled', index=3,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_im_stale', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.is_im_stale', index=4,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ldp_config_mode', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.ldp_config_mode', index=5,
      number=55, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ldp_autoconfig_disable', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.ldp_autoconfig_disable', index=6,
      number=56, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='te_mesh_grp', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.te_mesh_grp', index=7,
      number=57, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_config', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf.auto_config', index=8,
      number=58, type=11, cpp_type=10, label=3,
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
  serialized_start=271,
  serialized_end=797,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_vrf_info.id', index=1,
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
  serialized_start=799,
  serialized_end=839,
)


_LDP_INTF_AUTOCFG = _descriptor.Descriptor(
  name='ldp_intf_autocfg',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_autocfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuple', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_autocfg.tuple', index=0,
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
  serialized_start=841,
  serialized_end=874,
)


_LDP_INTF_TE_MESH_GRP = _descriptor.Descriptor(
  name='ldp_intf_te_mesh_grp',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_te_mesh_grp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ldp_te_mesh_group_all_cfgd', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_te_mesh_grp.ldp_te_mesh_group_all_cfgd', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ldp_mesh_group_enabled', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_te_mesh_grp.ldp_mesh_group_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='te_mesh_group_id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_te_mesh_grp.te_mesh_group_id', index=2,
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
  serialized_start=876,
  serialized_end=992,
)

_LDP_INTF.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
_LDP_INTF.fields_by_name['te_mesh_grp'].message_type = _LDP_INTF_TE_MESH_GRP
_LDP_INTF.fields_by_name['auto_config'].message_type = _LDP_INTF_AUTOCFG
DESCRIPTOR.message_types_by_name['ldp_intf_KEYS'] = _LDP_INTF_KEYS
DESCRIPTOR.message_types_by_name['ldp_intf'] = _LDP_INTF
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_intf_autocfg'] = _LDP_INTF_AUTOCFG
DESCRIPTOR.message_types_by_name['ldp_intf_te_mesh_grp'] = _LDP_INTF_TE_MESH_GRP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_intf_KEYS = _reflection.GeneratedProtocolMessageType('ldp_intf_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_INTF_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_KEYS)
  ))
_sym_db.RegisterMessage(ldp_intf_KEYS)

ldp_intf = _reflection.GeneratedProtocolMessageType('ldp_intf', (_message.Message,), dict(
  DESCRIPTOR = _LDP_INTF,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf)
  ))
_sym_db.RegisterMessage(ldp_intf)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)

ldp_intf_autocfg = _reflection.GeneratedProtocolMessageType('ldp_intf_autocfg', (_message.Message,), dict(
  DESCRIPTOR = _LDP_INTF_AUTOCFG,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_autocfg)
  ))
_sym_db.RegisterMessage(ldp_intf_autocfg)

ldp_intf_te_mesh_grp = _reflection.GeneratedProtocolMessageType('ldp_intf_te_mesh_grp', (_message.Message,), dict(
  DESCRIPTOR = _LDP_INTF_TE_MESH_GRP,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.default_vrf.afs.af.interfaces.interface.ldp_intf_te_mesh_grp)
  ))
_sym_db.RegisterMessage(ldp_intf_te_mesh_grp)


# @@protoc_insertion_point(module_scope)
