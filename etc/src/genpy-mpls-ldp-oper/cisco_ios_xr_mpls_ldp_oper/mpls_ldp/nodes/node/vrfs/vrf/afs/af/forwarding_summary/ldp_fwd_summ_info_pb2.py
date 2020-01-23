# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/vrfs/vrf/afs/af/forwarding_summary/ldp_fwd_summ_info.proto

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
  name='cisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/vrfs/vrf/afs/af/forwarding_summary/ldp_fwd_summ_info.proto',
  package='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary',
  syntax='proto3',
  serialized_pb=_b('\nicisco_ios_xr_mpls_ldp_oper/mpls_ldp/nodes/node/vrfs/vrf/afs/af/forwarding_summary/ldp_fwd_summ_info.proto\x12Qcisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary\"N\n\x16ldp_fwd_summ_info_KEYS\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x10\n\x08vrf_name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x66_name\x18\x03 \x01(\t\"\xb4\x02\n\x11ldp_fwd_summ_info\x12l\n\x03vrf\x18\x32 \x01(\x0b\x32_.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_vrf_info\x12\x14\n\x0cis_lsd_bound\x18\x33 \x01(\x08\x12\x0c\n\x04\x66sht\x18\x34 \x01(\r\x12\r\n\x05intfs\x18\x35 \x01(\r\x12\x0c\n\x04lbls\x18\x36 \x01(\r\x12p\n\x04r_ws\x18\x37 \x01(\x0b\x32\x62.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_summ\"(\n\x0cldp_vrf_info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"\xac\x01\n\x14ldp_fwd_rw_path_summ\x12\x13\n\x0btotal_paths\x18\x01 \x01(\r\x12\x17\n\x0fprotected_paths\x18\x02 \x01(\r\x12\x14\n\x0c\x62\x61\x63kup_paths\x18\x03 \x01(\r\x12\x1b\n\x13remote_backup_paths\x18\x04 \x01(\r\x12\x15\n\rlabeled_paths\x18\x05 \x01(\r\x12\x1c\n\x14labeled_backup_paths\x18\x06 \x01(\r\"e\n\x17ldp_fwd_rw_pfx_lbl_summ\x12\x14\n\x0clabeled_pfxs\x18\x01 \x01(\r\x12\x1c\n\x14labeled_pfxs_partial\x18\x02 \x01(\r\x12\x16\n\x0eunlabeled_pfxs\x18\x03 \x01(\r\"\xf1\x03\n\x13ldp_fwd_rw_pfx_summ\x12\x12\n\ntotal_pfxs\x18\x01 \x01(\r\x12\x11\n\tecmp_pfxs\x18\x02 \x01(\r\x12\x16\n\x0eprotected_pfxs\x18\x03 \x01(\r\x12\x85\x01\n\x11labeled_pfxs_aggr\x18\x04 \x01(\x0b\x32j.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ\x12\x88\x01\n\x14labeled_pfxs_primary\x18\x05 \x01(\x0b\x32j.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ\x12\x87\x01\n\x13labeled_pfxs_backup\x18\x06 \x01(\x0b\x32j.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ\"\xfe\x01\n\x0fldp_fwd_rw_summ\x12t\n\x04pfxs\x18\x01 \x01(\x0b\x32\x66.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ\x12u\n\x04n_hs\x18\x02 \x01(\x0b\x32g.cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summb\x06proto3')
)




_LDP_FWD_SUMM_INFO_KEYS = _descriptor.Descriptor(
  name='ldp_fwd_summ_info_KEYS',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_KEYS.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vrf_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_KEYS.vrf_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='af_name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_KEYS.af_name', index=2,
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
  serialized_start=192,
  serialized_end=270,
)


_LDP_FWD_SUMM_INFO = _descriptor.Descriptor(
  name='ldp_fwd_summ_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vrf', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info.vrf', index=0,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_lsd_bound', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info.is_lsd_bound', index=1,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fsht', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info.fsht', index=2,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intfs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info.intfs', index=3,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lbls', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info.lbls', index=4,
      number=54, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r_ws', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info.r_ws', index=5,
      number=55, type=11, cpp_type=10, label=1,
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
  serialized_start=273,
  serialized_end=581,
)


_LDP_VRF_INFO = _descriptor.Descriptor(
  name='ldp_vrf_info',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_vrf_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_vrf_info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_vrf_info.id', index=1,
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
  serialized_start=583,
  serialized_end=623,
)


_LDP_FWD_RW_PATH_SUMM = _descriptor.Descriptor(
  name='ldp_fwd_rw_path_summ',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_paths', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ.total_paths', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protected_paths', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ.protected_paths', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backup_paths', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ.backup_paths', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_backup_paths', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ.remote_backup_paths', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeled_paths', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ.labeled_paths', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeled_backup_paths', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ.labeled_backup_paths', index=5,
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
  serialized_start=626,
  serialized_end=798,
)


_LDP_FWD_RW_PFX_LBL_SUMM = _descriptor.Descriptor(
  name='ldp_fwd_rw_pfx_lbl_summ',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labeled_pfxs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ.labeled_pfxs', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeled_pfxs_partial', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ.labeled_pfxs_partial', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlabeled_pfxs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ.unlabeled_pfxs', index=2,
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
  serialized_start=800,
  serialized_end=901,
)


_LDP_FWD_RW_PFX_SUMM = _descriptor.Descriptor(
  name='ldp_fwd_rw_pfx_summ',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_pfxs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ.total_pfxs', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ecmp_pfxs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ.ecmp_pfxs', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protected_pfxs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ.protected_pfxs', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeled_pfxs_aggr', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ.labeled_pfxs_aggr', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeled_pfxs_primary', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ.labeled_pfxs_primary', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeled_pfxs_backup', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ.labeled_pfxs_backup', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=904,
  serialized_end=1401,
)


_LDP_FWD_RW_SUMM = _descriptor.Descriptor(
  name='ldp_fwd_rw_summ',
  full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_summ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pfxs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_summ.pfxs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_hs', full_name='cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_summ.n_hs', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1404,
  serialized_end=1658,
)

_LDP_FWD_SUMM_INFO.fields_by_name['vrf'].message_type = _LDP_VRF_INFO
_LDP_FWD_SUMM_INFO.fields_by_name['r_ws'].message_type = _LDP_FWD_RW_SUMM
_LDP_FWD_RW_PFX_SUMM.fields_by_name['labeled_pfxs_aggr'].message_type = _LDP_FWD_RW_PFX_LBL_SUMM
_LDP_FWD_RW_PFX_SUMM.fields_by_name['labeled_pfxs_primary'].message_type = _LDP_FWD_RW_PFX_LBL_SUMM
_LDP_FWD_RW_PFX_SUMM.fields_by_name['labeled_pfxs_backup'].message_type = _LDP_FWD_RW_PFX_LBL_SUMM
_LDP_FWD_RW_SUMM.fields_by_name['pfxs'].message_type = _LDP_FWD_RW_PFX_SUMM
_LDP_FWD_RW_SUMM.fields_by_name['n_hs'].message_type = _LDP_FWD_RW_PATH_SUMM
DESCRIPTOR.message_types_by_name['ldp_fwd_summ_info_KEYS'] = _LDP_FWD_SUMM_INFO_KEYS
DESCRIPTOR.message_types_by_name['ldp_fwd_summ_info'] = _LDP_FWD_SUMM_INFO
DESCRIPTOR.message_types_by_name['ldp_vrf_info'] = _LDP_VRF_INFO
DESCRIPTOR.message_types_by_name['ldp_fwd_rw_path_summ'] = _LDP_FWD_RW_PATH_SUMM
DESCRIPTOR.message_types_by_name['ldp_fwd_rw_pfx_lbl_summ'] = _LDP_FWD_RW_PFX_LBL_SUMM
DESCRIPTOR.message_types_by_name['ldp_fwd_rw_pfx_summ'] = _LDP_FWD_RW_PFX_SUMM
DESCRIPTOR.message_types_by_name['ldp_fwd_rw_summ'] = _LDP_FWD_RW_SUMM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ldp_fwd_summ_info_KEYS = _reflection.GeneratedProtocolMessageType('ldp_fwd_summ_info_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _LDP_FWD_SUMM_INFO_KEYS,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_KEYS)
  ))
_sym_db.RegisterMessage(ldp_fwd_summ_info_KEYS)

ldp_fwd_summ_info = _reflection.GeneratedProtocolMessageType('ldp_fwd_summ_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_FWD_SUMM_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info)
  ))
_sym_db.RegisterMessage(ldp_fwd_summ_info)

ldp_vrf_info = _reflection.GeneratedProtocolMessageType('ldp_vrf_info', (_message.Message,), dict(
  DESCRIPTOR = _LDP_VRF_INFO,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_vrf_info)
  ))
_sym_db.RegisterMessage(ldp_vrf_info)

ldp_fwd_rw_path_summ = _reflection.GeneratedProtocolMessageType('ldp_fwd_rw_path_summ', (_message.Message,), dict(
  DESCRIPTOR = _LDP_FWD_RW_PATH_SUMM,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_path_summ)
  ))
_sym_db.RegisterMessage(ldp_fwd_rw_path_summ)

ldp_fwd_rw_pfx_lbl_summ = _reflection.GeneratedProtocolMessageType('ldp_fwd_rw_pfx_lbl_summ', (_message.Message,), dict(
  DESCRIPTOR = _LDP_FWD_RW_PFX_LBL_SUMM,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_lbl_summ)
  ))
_sym_db.RegisterMessage(ldp_fwd_rw_pfx_lbl_summ)

ldp_fwd_rw_pfx_summ = _reflection.GeneratedProtocolMessageType('ldp_fwd_rw_pfx_summ', (_message.Message,), dict(
  DESCRIPTOR = _LDP_FWD_RW_PFX_SUMM,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_pfx_summ)
  ))
_sym_db.RegisterMessage(ldp_fwd_rw_pfx_summ)

ldp_fwd_rw_summ = _reflection.GeneratedProtocolMessageType('ldp_fwd_rw_summ', (_message.Message,), dict(
  DESCRIPTOR = _LDP_FWD_RW_SUMM,
  __module__ = 'cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_summ_info_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_mpls_ldp_oper.mpls_ldp.nodes.node.vrfs.vrf.afs.af.forwarding_summary.ldp_fwd_rw_summ)
  ))
_sym_db.RegisterMessage(ldp_fwd_rw_summ)


# @@protoc_insertion_point(module_scope)
