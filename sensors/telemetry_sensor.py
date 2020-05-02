import sys
import pprint
import yaml

from google.protobuf.json_format import MessageToJson
import grpc

import telemetry_pb2
from mdt_grpc_dialin import mdt_grpc_dialin_pb2, mdt_grpc_dialin_pb2_grpc
from ipv6_nd_neighbor_entry_pb2 import ipv6_nd_neighbor_entry_KEYS, ipv6_nd_neighbor_entry

from st2reactor.sensor.base import Sensor


class TelemetrySensor(Sensor):
    def __init__(self, sensor_service, config):
        super(TelemetrySensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass

    def run(self):
        server_ip = "192.168.123.12"
        server_port = "57777"
        xr_user = "root"
        xr_passwd = "root"
        print("Using GRPC Server IP(%s) Port(%s)" % (server_ip, server_port) )

        channel = grpc.insecure_channel(str(server_ip) + ":" + str(server_port))

        stub = mdt_grpc_dialin_pb2_grpc.gRPCConfigOperStub(channel)

        metadata = [('username', xr_user), ('password', xr_passwd)]
        Timeout = 3600 * 24 * 365

        sub_args = mdt_grpc_dialin_pb2.CreateSubsArgs(ReqId=99, encode=2, subidstr='IPV6')
        stream = stub.CreateSubs(sub_args, timeout=Timeout, metadata=metadata)
        print("##########1")
        for segment in stream:
            telemetry_pb = telemetry_pb2.Telemetry()
            telemetry_pb.ParseFromString(segment.data)

            telemetry_gpb_table = telemetry_pb2.TelemetryGPBTable()
            telemetry_gpb_table.CopyFrom(telemetry_pb.data_gpb)

            gpb_rows = []
            print("##########2")
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
                self.sensor_service.dispatch(trigger='telemetry_collector.event2', payload=gpb_rows)

    def cleanup(self):
        pass

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
