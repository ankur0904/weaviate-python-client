# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weaviate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import batch_pb2 as batch__pb2
from . import search_get_pb2 as search__get__pb2
from . import search_get_v1_pb2 as search__get__v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eweaviate.proto\x12\x0cweaviategrpc\x1a\x0b\x62\x61tch.proto\x1a\x10search_get.proto\x1a\x13search_get_v1.proto2\xee\x01\n\x08Weaviate\x12\x42\n\x06Search\x12\x1b.weaviategrpc.SearchRequest\x1a\x19.weaviategrpc.SearchReply\"\x00\x12H\n\x08SearchV1\x12\x1d.weaviategrpc.SearchRequestV1\x1a\x1b.weaviategrpc.SearchReplyV1\"\x00\x12T\n\x0c\x42\x61tchObjects\x12!.weaviategrpc.BatchObjectsRequest\x1a\x1f.weaviategrpc.BatchObjectsReply\"\x00\x42`\n\x19io.weaviate.grpc.protocolB\rWeaviateProtoZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'weaviate_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031io.weaviate.grpc.protocolB\rWeaviateProtoZ4github.com/weaviate/weaviate/grpc/generated;protocol'
  _globals['_WEAVIATE']._serialized_start=85
  _globals['_WEAVIATE']._serialized_end=323
# @@protoc_insertion_point(module_scope)
