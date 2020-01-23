import json
import os, sys
import pprint
import yaml

from google.protobuf.json_format import MessageToJson
import grpc

from st2reactor.sensor.base import Sensor


sys.path.append("etc/src/genpy-ipv6-nd")
sys.path.append("etc/src/genpy-ipv6-nd/cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/neighbor_interfaces/neighbor_interface/host_addresses/host_address/")

import telemetry_pb2
from mdt_grpc_dialin import mdt_grpc_dialin_pb2, mdt_grpc_dialin_pb2_grpc
from ipv6_nd_neighbor_entry_pb2 import ipv6_nd_neighbor_entry_KEYS, ipv6_nd_neighbor_entry


class TelemetrySensor(Sensor):

    def __init__(self, sensor_service, config):

        super(TelemetrySensor, self).__init__(sensor_service, config)

        self.server_ip = "10.10.20.70"
        self.server_port = "2221"
        self.xr_user = "admin"
        self.xr_passwd  = "admin"

    def setup(self):
        channel = grpc.insecure_channel(str(server_ip) + ":" + str(server_port))
        stub = mdt_grpc_dialin_pb2_grpc.gRPCConfigOperStub(channel)
        metadata = [('username', xr_user), ('password', xr_passwd)]
        timeout = 3600 * 24 * 365  # Seconds
        sub_args = mdt_grpc_dialin_pb2.CreateSubsArgs(ReqId=99, encode=2, subidstr='IPV6')
        self.stream = stub.CreateSubs(sub_args, timeout=timeout, metadata=metadata)

    def run(self):
        for segment in self.stream:
            telemetry_pb = telemetry_pb2.Telemetry()
            telemetry_pb.ParseFromString(segment.data)
            # Return in JSON format instead of protobuf.

            telemetry_gpb_table = telemetry_pb2.TelemetryGPBTable()
            telemetry_gpb_table.CopyFrom(telemetry_pb.data_gpb)

            gpb_rows = []
            while (len(telemetry_gpb_table.row)):
                gpb_row_dict = {}
                gpb_row_dict["keys"] = {}
                gpb_row_dict["content"] = {}

                telemetry_gpb_row = telemetry_pb2.TelemetryRowGPB()
                telemetry_gpb_row.CopyFrom(telemetry_gpb_table.row.pop())
                gpb_row_dict["timestamp"] = telemetry_gpb_row.timestamp

                ipv6_nd_neighbor_entry_keys = ipv6_nd_neighbor_entry_KEYS()
                ipv6_nd_neighbor_entry_keys.ParseFromString(telemetry_gpb_row.keys)

                ipv6_nd_neighbor_entry_content = ipv6_nd_neighbor_entry()
                ipv6_nd_neighbor_entry_content.ParseFromString(telemetry_gpb_row.content)

                print("1: {}".format(ipv6_nd_neighbor_entry_content))
                print("2: {}".format(ipv6_nd_neighbor_entry_keys))

                content_dump = MessageToJson(ipv6_nd_neighbor_entry_content)
                keys_dump = MessageToJson(ipv6_nd_neighbor_entry_keys)

                print("3: {}".format(content_dump))
                print("4: {}".format(keys_dump))

                gpb_row_dict["content"].update(yaml.safe_load(content_dump))
                gpb_row_dict["keys"].update(yaml.safe_load(keys_dump))

                gpb_rows.append(gpb_row_dict)

                print(pprint.pprint(gpb_rows))

                self._sensor_service.dispatch(trigger='telemetry_log.log', payload=gpb_rows)

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass
