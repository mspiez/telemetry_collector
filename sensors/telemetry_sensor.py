# import eventlet

# import os
# import logging
# from flask import Flask
# from slack import WebClient
# from slackeventsapi import SlackEventAdapter

import sys
import pprint
import yaml

from google.protobuf.json_format import MessageToJson
import grpc

sys.path.append("./../etc/src/genpy-ipv6-nd")
sys.path.append("./../etc/src/genpy-ipv6-nd/cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/neighbor_interfaces/neighbor_interface/

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

    def run(self, test_param):
        print(test_param)
        server_ip = "192.168.123.12"
        server_port = "57021"
        xr_user = "root"
        xr_passwd = "root"
        # print(server_ip)
        # if test_param == 'working':
        #     return (True, test_param)
        # return (False, test_param)

        print("Using GRPC Server IP(%s) Port(%s)" % (server_ip, server_port))

        # Create the channel for gRPC.
        channel = grpc.insecure_channel(str(server_ip) + ":" + str(server_port))

        # Create the gRPC stub.
        stub = mdt_grpc_dialin_pb2_grpc.gRPCConfigOperStub(channel)

        metadata = [('username', xr_user), ('password', xr_passwd)]
        Timeout = 3600 * 24 * 365  # Seconds

        sub_args = mdt_grpc_dialin_pb2.CreateSubsArgs(ReqId=99, encode=2, subidstr='IPV6')
        stream = stub.CreateSubs(sub_args, timeout=Timeout, metadata=metadata)
        for segment in stream:
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
                self.sensor_service.dispatch(trigger='telemetry_collector.event2', payload=gpb_rows)
            #     return (True, pprint.pprint(gpb_rows))
            # return (False, pprint.pprint(gpb_rows))

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def test_message_to_slack():
        app = Flask(__name__)
        slack_events_adapter = SlackEventAdapter("99f80a2400b78ffad95edfa44fab424c", "/slack/events", app)
        slack_web_client = WebClient(token="xoxb-152153693140-883922465636-Mjti2nWdnDLb3HXd37Vh90ql")
        onboarding_tutorials_sent = {}

        response = slack_web_client.chat_postMessage(**message)
        return response


# import json
# import os, sys
# import pprint
# import yaml
# import eventlet

# from google.protobuf.json_format import MessageToJson
# import grpc

# from st2reactor.sensor.base import Sensor

# sys.path.append("/home/michal/PycharmProjects/telemetry-grpc-collectors/build/python/src/genpy-ipv6-nd")
# sys.path.append(
#     "/home/michal/PycharmProjects/telemetry-grpc-collectors/build/python/src/genpy-ipv6-nd/cisco_ios_xr_ipv6_nd_oper/ipv6_node_discovery/nodes/node/neighbor_interfaces/neighbor_interface/host_addresses/host_address/")

# import telemetry_pb2
# from mdt_grpc_dialin import mdt_grpc_dialin_pb2, mdt_grpc_dialin_pb2_grpc
# from ipv6_nd_neighbor_entry_pb2 import ipv6_nd_neighbor_entry_KEYS, ipv6_nd_neighbor_entry


# class TelemetrySensor(Sensor):
#     def __init__(self, sensor_service, config):
#         super(TelemetrySensor, self).__init__(sensor_service=sensor_service, config=config)
#         self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
#         self._stop = False

#     def setup(self):
#         pass

#     def run(self):
#         while not self._stop:
#             self._logger.debug('TelemetrySensor dispatching trigger...')
#             count = self.sensor_service.get_value('hello_st2.count') or 0
#             payload = {'greeting': 'Yo, StackStorm!', 'count': int(count) + 1}
#             self.sensor_service.dispatch(trigger='hello_st2.event1', payload=payload)
#             self.sensor_service.set_value('hello_st2.count', payload['count'])
#             eventlet.sleep(60)

#     def cleanup(self):
#         self._stop = True

#     # Methods required for programmable sensors.
#     def add_trigger(self, trigger):
#         pass

#     def update_trigger(self, trigger):
#         pass

#     def remove_trigger(self, trigger):
#         pass


# class TelemetrySensor(Sensor):

#     def __init__(self, sensor_service, config):

#         super(TelemetrySensor, self).__init__(sensor_service=sensor_service, config=config)
#         # self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
#         self._stop = False

#     def setup(self):
#         pass

#     def run(self):
#         server_ip = "10.10.20.70"
#         server_port = "57021"
#         xr_user = "admin"
#         xr_passwd = "admin"
#         while not self._stop:
#             print("Using GRPC Server IP(%s) Port(%s)" % (server_ip, server_port))

#             # Create the channel for gRPC.
#             channel = grpc.insecure_channel(str(server_ip) + ":" + str(server_port))

#             # Create the gRPC stub.
#             stub = mdt_grpc_dialin_pb2_grpc.gRPCConfigOperStub(channel)

#             metadata = [('username', xr_user), ('password', xr_passwd)]
#             Timeout = 3600 * 24 * 365  # Seconds

#             sub_args = mdt_grpc_dialin_pb2.CreateSubsArgs(ReqId=99, encode=2, subidstr='IPV6')
#             stream = stub.CreateSubs(sub_args, timeout=Timeout, metadata=metadata)
#             # self.sensor_service.set_value('now.count2', server_ip)
#             for segment in stream:
#                 telemetry_pb = telemetry_pb2.Telemetry()
#                 telemetry_pb.ParseFromString(segment.data)
#                 # Return in JSON format instead of protobuf.

#                 telemetry_gpb_table = telemetry_pb2.TelemetryGPBTable()
#                 telemetry_gpb_table.CopyFrom(telemetry_pb.data_gpb)

#                 gpb_rows = []
#                 self.sensor_service.dispatch(trigger='telemetry_log.log', payload=gpb_rows)
#                 self.sensor_service.dispatch(trigger='telemetry_log.log', payload=server_ip)
#                 self.sensor_service.set_value('now.count3', server_port)
#                 while (len(telemetry_gpb_table.row)):
#                     gpb_row_dict = {}
#                     gpb_row_dict["keys"] = {}
#                     gpb_row_dict["content"] = {}

#                     telemetry_gpb_row = telemetry_pb2.TelemetryRowGPB()
#                     telemetry_gpb_row.CopyFrom(telemetry_gpb_table.row.pop())
#                     gpb_row_dict["timestamp"] = telemetry_gpb_row.timestamp

#                     ipv6_nd_neighbor_entry_keys = ipv6_nd_neighbor_entry_KEYS()
#                     ipv6_nd_neighbor_entry_keys.ParseFromString(telemetry_gpb_row.keys)

#                     ipv6_nd_neighbor_entry_content = ipv6_nd_neighbor_entry()
#                     ipv6_nd_neighbor_entry_content.ParseFromString(telemetry_gpb_row.content)

#                     print("1: {}".format(ipv6_nd_neighbor_entry_content))
#                     print("2: {}".format(ipv6_nd_neighbor_entry_keys))

#                     content_dump = MessageToJson(ipv6_nd_neighbor_entry_content)
#                     keys_dump = MessageToJson(ipv6_nd_neighbor_entry_keys)

#                     print("3: {}".format(content_dump))
#                     print("4: {}".format(keys_dump))

#                     gpb_row_dict["content"].update(yaml.safe_load(content_dump))
#                     gpb_row_dict["keys"].update(yaml.safe_load(keys_dump))

#                     gpb_rows.append(gpb_row_dict)

#                     print(pprint.pprint(gpb_rows))
#                     self.sensor_service.dispatch(trigger='telemetry_log.log', payload=gpb_rows)
#             # eventlet.sleep(15)

#     def cleanup(self):
#         self._stop = True

#     def add_trigger(self, trigger):
#         # This method is called when trigger is created
#         pass

#     def update_trigger(self, trigger):
#         # This method is called when trigger is updated
#         pass

#     def remove_trigger(self, trigger):
#         # This method is called when trigger is deleted
#         pass
