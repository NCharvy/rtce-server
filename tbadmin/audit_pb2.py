# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbadmin/audit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbrpc import tbrpc_pb2 as tbrpc_dot_tbrpc__pb2
from tbmatch import account_pb2 as tbmatch_dot_account__pb2
from tbmatch import shop_pb2 as tbmatch_dot_shop__pb2
from tbmatch import query_pb2 as tbmatch_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbadmin/audit.proto',
  package='tbadmin',
  syntax='proto2',
  serialized_pb=_b('\n\x13tbadmin/audit.proto\x12\x07tbadmin\x1a\x11tbrpc/tbrpc.proto\x1a\x15tbmatch/account.proto\x1a\x12tbmatch/shop.proto\x1a\x13tbmatch/query.proto\"C\n\x0e\x41\x63\x63ountSummary\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0e\n\x06handle\x18\x03 \x01(\t\"a\n\x0c\x41uditAccount\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.tbadmin.AccountSummary\x12*\n\x0clogin_status\x18\x02 \x01(\x0e\x32\x14.tbmatch.LoginStatus\"H\n\nAuditOrder\x12\x14\n\x0corder_number\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.tbmatch.OrderStatus\"\x8b\x02\n\nAuditEvent\x12&\n\x05\x61\x63tor\x18\x02 \x01(\x0b\x32\x17.tbadmin.AccountSummary\x12\x12\n\nevent_time\x18\x03 \x01(\t\x12+\n\nevent_type\x18\x04 \x01(\x0e\x32\x17.tbadmin.AuditEventType\x12\x11\n\tremote_ip\x18\x05 \x01(\t\x12\x13\n\x0bserver_host\x18\x06 \x01(\t\x12\x11\n\toperation\x18\t \x01(\t\x12\r\n\x05query\x18\n \x01(\t\x12&\n\x07\x61\x63\x63ount\x18\x0b \x01(\x0b\x32\x15.tbadmin.AuditAccount\x12\"\n\x05order\x18\x0c \x01(\x0b\x32\x13.tbadmin.AuditOrder\"\xb9\x02\n\x12\x41uditEventCriteria\x12\x18\n\x10\x61\x63tor_account_id\x18\x01 \x01(\x03\x12&\n\nevent_time\x18\x02 \x01(\x0b\x32\x12.tbmatch.TimeRange\x12+\n\nevent_type\x18\x03 \x01(\x0e\x32\x17.tbadmin.AuditEventType\x12\x15\n\rremote_ip_net\x18\x04 \x01(\t\x12)\n\x0bserver_host\x18\x05 \x01(\x0b\x32\x14.tbmatch.StringMatch\x12\'\n\toperation\x18\x06 \x01(\x0b\x32\x14.tbmatch.StringMatch\x12#\n\x05query\x18\x07 \x01(\x0b\x32\x14.tbmatch.StringMatch\x12\x12\n\naccount_id\x18\x0b \x01(\x03\x12\x10\n\x08order_id\x18\x0c \x01(\x03\"\x84\x02\n\x0e\x41uditEventSort\x12\x39\n\x05\x66irst\x18\x01 \x01(\x0e\x32\x1e.tbadmin.AuditEventSort.SortBy:\nEVENT_TIME\x12.\n\x06second\x18\x02 \x01(\x0e\x32\x1e.tbadmin.AuditEventSort.SortBy\x12\x12\n\ndescending\x18\x03 \x01(\x08\"s\n\x06SortBy\x12\x0c\n\x08\x41\x43TOR_ID\x10\x01\x12\x0e\n\nEVENT_TIME\x10\x02\x12\r\n\tREMOTE_IP\x10\x03\x12\x0f\n\x0bSERVER_HOST\x10\x04\x12\r\n\tOPERATION\x10\x05\x12\x0e\n\nACCOUNT_ID\x10\x06\x12\x0c\n\x08ORDER_ID\x10\x07\"\x94\x01\n\x19SearchAuditHistoryRequest\x12-\n\x08\x63riteria\x18\x01 \x01(\x0b\x32\x1b.tbadmin.AuditEventCriteria\x12%\n\x04sort\x18\x02 \x01(\x0b\x32\x17.tbadmin.AuditEventSort\x12\x0e\n\x06offset\x18\x05 \x01(\x05\x12\x11\n\x05limit\x18\x06 \x01(\x05:\x02\x32\x35\"T\n\x18SearchAuditHistoryResult\x12#\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x13.tbadmin.AuditEvent\x12\x13\n\x0b\x65nd_of_data\x18\x02 \x01(\x08*=\n\x0e\x41uditEventType\x12\x08\n\x04USER\x10\x01\x12\x0b\n\x07\x41\x43\x43OUNT\x10\x02\x12\t\n\x05ORDER\x10\x03\x12\t\n\x05QUERY\x10\x04\x32q\n\x0c\x41uditService\x12\x61\n\x12SearchAuditHistory\x12\".tbadmin.SearchAuditHistoryRequest\x1a!.tbadmin.SearchAuditHistoryResult\"\x04\xc8\xf3\x18\x18')
  ,
  dependencies=[tbrpc_dot_tbrpc__pb2.DESCRIPTOR,tbmatch_dot_account__pb2.DESCRIPTOR,tbmatch_dot_shop__pb2.DESCRIPTOR,tbmatch_dot_query__pb2.DESCRIPTOR,])

_AUDITEVENTTYPE = _descriptor.EnumDescriptor(
  name='AuditEventType',
  full_name='tbadmin.AuditEventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1443,
  serialized_end=1504,
)
_sym_db.RegisterEnumDescriptor(_AUDITEVENTTYPE)

AuditEventType = enum_type_wrapper.EnumTypeWrapper(_AUDITEVENTTYPE)
USER = 1
ACCOUNT = 2
ORDER = 3
QUERY = 4


_AUDITEVENTSORT_SORTBY = _descriptor.EnumDescriptor(
  name='SortBy',
  full_name='tbadmin.AuditEventSort.SortBy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTOR_ID', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENT_TIME', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_IP', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_HOST', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_ID', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_ID', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1089,
  serialized_end=1204,
)
_sym_db.RegisterEnumDescriptor(_AUDITEVENTSORT_SORTBY)


_ACCOUNTSUMMARY = _descriptor.Descriptor(
  name='AccountSummary',
  full_name='tbadmin.AccountSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='tbadmin.AccountSummary.account_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='tbadmin.AccountSummary.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='handle', full_name='tbadmin.AccountSummary.handle', index=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=182,
)


_AUDITACCOUNT = _descriptor.Descriptor(
  name='AuditAccount',
  full_name='tbadmin.AuditAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='tbadmin.AuditAccount.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_status', full_name='tbadmin.AuditAccount.login_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=281,
)


_AUDITORDER = _descriptor.Descriptor(
  name='AuditOrder',
  full_name='tbadmin.AuditOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_number', full_name='tbadmin.AuditOrder.order_number', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='tbadmin.AuditOrder.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=355,
)


_AUDITEVENT = _descriptor.Descriptor(
  name='AuditEvent',
  full_name='tbadmin.AuditEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actor', full_name='tbadmin.AuditEvent.actor', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='tbadmin.AuditEvent.event_time', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='tbadmin.AuditEvent.event_type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_ip', full_name='tbadmin.AuditEvent.remote_ip', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_host', full_name='tbadmin.AuditEvent.server_host', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='tbadmin.AuditEvent.operation', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query', full_name='tbadmin.AuditEvent.query', index=6,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account', full_name='tbadmin.AuditEvent.account', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order', full_name='tbadmin.AuditEvent.order', index=8,
      number=12, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=625,
)


_AUDITEVENTCRITERIA = _descriptor.Descriptor(
  name='AuditEventCriteria',
  full_name='tbadmin.AuditEventCriteria',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actor_account_id', full_name='tbadmin.AuditEventCriteria.actor_account_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='tbadmin.AuditEventCriteria.event_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='tbadmin.AuditEventCriteria.event_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_ip_net', full_name='tbadmin.AuditEventCriteria.remote_ip_net', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_host', full_name='tbadmin.AuditEventCriteria.server_host', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='tbadmin.AuditEventCriteria.operation', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query', full_name='tbadmin.AuditEventCriteria.query', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='tbadmin.AuditEventCriteria.account_id', index=7,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='tbadmin.AuditEventCriteria.order_id', index=8,
      number=12, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=941,
)


_AUDITEVENTSORT = _descriptor.Descriptor(
  name='AuditEventSort',
  full_name='tbadmin.AuditEventSort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='tbadmin.AuditEventSort.first', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='second', full_name='tbadmin.AuditEventSort.second', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='descending', full_name='tbadmin.AuditEventSort.descending', index=2,
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
    _AUDITEVENTSORT_SORTBY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=944,
  serialized_end=1204,
)


_SEARCHAUDITHISTORYREQUEST = _descriptor.Descriptor(
  name='SearchAuditHistoryRequest',
  full_name='tbadmin.SearchAuditHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='criteria', full_name='tbadmin.SearchAuditHistoryRequest.criteria', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort', full_name='tbadmin.SearchAuditHistoryRequest.sort', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='tbadmin.SearchAuditHistoryRequest.offset', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='tbadmin.SearchAuditHistoryRequest.limit', index=3,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=25,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1207,
  serialized_end=1355,
)


_SEARCHAUDITHISTORYRESULT = _descriptor.Descriptor(
  name='SearchAuditHistoryResult',
  full_name='tbadmin.SearchAuditHistoryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='tbadmin.SearchAuditHistoryResult.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_of_data', full_name='tbadmin.SearchAuditHistoryResult.end_of_data', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1357,
  serialized_end=1441,
)

_AUDITACCOUNT.fields_by_name['user'].message_type = _ACCOUNTSUMMARY
_AUDITACCOUNT.fields_by_name['login_status'].enum_type = tbmatch_dot_account__pb2._LOGINSTATUS
_AUDITORDER.fields_by_name['status'].enum_type = tbmatch_dot_shop__pb2._ORDERSTATUS
_AUDITEVENT.fields_by_name['actor'].message_type = _ACCOUNTSUMMARY
_AUDITEVENT.fields_by_name['event_type'].enum_type = _AUDITEVENTTYPE
_AUDITEVENT.fields_by_name['account'].message_type = _AUDITACCOUNT
_AUDITEVENT.fields_by_name['order'].message_type = _AUDITORDER
_AUDITEVENTCRITERIA.fields_by_name['event_time'].message_type = tbmatch_dot_query__pb2._TIMERANGE
_AUDITEVENTCRITERIA.fields_by_name['event_type'].enum_type = _AUDITEVENTTYPE
_AUDITEVENTCRITERIA.fields_by_name['server_host'].message_type = tbmatch_dot_query__pb2._STRINGMATCH
_AUDITEVENTCRITERIA.fields_by_name['operation'].message_type = tbmatch_dot_query__pb2._STRINGMATCH
_AUDITEVENTCRITERIA.fields_by_name['query'].message_type = tbmatch_dot_query__pb2._STRINGMATCH
_AUDITEVENTSORT.fields_by_name['first'].enum_type = _AUDITEVENTSORT_SORTBY
_AUDITEVENTSORT.fields_by_name['second'].enum_type = _AUDITEVENTSORT_SORTBY
_AUDITEVENTSORT_SORTBY.containing_type = _AUDITEVENTSORT
_SEARCHAUDITHISTORYREQUEST.fields_by_name['criteria'].message_type = _AUDITEVENTCRITERIA
_SEARCHAUDITHISTORYREQUEST.fields_by_name['sort'].message_type = _AUDITEVENTSORT
_SEARCHAUDITHISTORYRESULT.fields_by_name['events'].message_type = _AUDITEVENT
DESCRIPTOR.message_types_by_name['AccountSummary'] = _ACCOUNTSUMMARY
DESCRIPTOR.message_types_by_name['AuditAccount'] = _AUDITACCOUNT
DESCRIPTOR.message_types_by_name['AuditOrder'] = _AUDITORDER
DESCRIPTOR.message_types_by_name['AuditEvent'] = _AUDITEVENT
DESCRIPTOR.message_types_by_name['AuditEventCriteria'] = _AUDITEVENTCRITERIA
DESCRIPTOR.message_types_by_name['AuditEventSort'] = _AUDITEVENTSORT
DESCRIPTOR.message_types_by_name['SearchAuditHistoryRequest'] = _SEARCHAUDITHISTORYREQUEST
DESCRIPTOR.message_types_by_name['SearchAuditHistoryResult'] = _SEARCHAUDITHISTORYRESULT
DESCRIPTOR.enum_types_by_name['AuditEventType'] = _AUDITEVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountSummary = _reflection.GeneratedProtocolMessageType('AccountSummary', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTSUMMARY,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.AccountSummary)
  ))
_sym_db.RegisterMessage(AccountSummary)

AuditAccount = _reflection.GeneratedProtocolMessageType('AuditAccount', (_message.Message,), dict(
  DESCRIPTOR = _AUDITACCOUNT,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.AuditAccount)
  ))
_sym_db.RegisterMessage(AuditAccount)

AuditOrder = _reflection.GeneratedProtocolMessageType('AuditOrder', (_message.Message,), dict(
  DESCRIPTOR = _AUDITORDER,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.AuditOrder)
  ))
_sym_db.RegisterMessage(AuditOrder)

AuditEvent = _reflection.GeneratedProtocolMessageType('AuditEvent', (_message.Message,), dict(
  DESCRIPTOR = _AUDITEVENT,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.AuditEvent)
  ))
_sym_db.RegisterMessage(AuditEvent)

AuditEventCriteria = _reflection.GeneratedProtocolMessageType('AuditEventCriteria', (_message.Message,), dict(
  DESCRIPTOR = _AUDITEVENTCRITERIA,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.AuditEventCriteria)
  ))
_sym_db.RegisterMessage(AuditEventCriteria)

AuditEventSort = _reflection.GeneratedProtocolMessageType('AuditEventSort', (_message.Message,), dict(
  DESCRIPTOR = _AUDITEVENTSORT,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.AuditEventSort)
  ))
_sym_db.RegisterMessage(AuditEventSort)

SearchAuditHistoryRequest = _reflection.GeneratedProtocolMessageType('SearchAuditHistoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAUDITHISTORYREQUEST,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.SearchAuditHistoryRequest)
  ))
_sym_db.RegisterMessage(SearchAuditHistoryRequest)

SearchAuditHistoryResult = _reflection.GeneratedProtocolMessageType('SearchAuditHistoryResult', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAUDITHISTORYRESULT,
  __module__ = 'tbadmin.audit_pb2'
  # @@protoc_insertion_point(class_scope:tbadmin.SearchAuditHistoryResult)
  ))
_sym_db.RegisterMessage(SearchAuditHistoryResult)



_AUDITSERVICE = _descriptor.ServiceDescriptor(
  name='AuditService',
  full_name='tbadmin.AuditService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1506,
  serialized_end=1619,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchAuditHistory',
    full_name='tbadmin.AuditService.SearchAuditHistory',
    index=0,
    containing_service=None,
    input_type=_SEARCHAUDITHISTORYREQUEST,
    output_type=_SEARCHAUDITHISTORYRESULT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\310\363\030\030')),
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDITSERVICE)

DESCRIPTOR.services_by_name['AuditService'] = _AUDITSERVICE

# @@protoc_insertion_point(module_scope)