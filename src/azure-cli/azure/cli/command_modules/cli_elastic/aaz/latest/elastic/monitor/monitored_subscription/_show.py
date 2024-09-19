# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "elastic monitor monitored-subscription show",
)
class Show(AAZCommand):
    """Get all the subscriptions currently being monitored by the Elastic monitor resource.
    """

    _aaz_info = {
        "version": "2024-06-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.elastic/monitors/{}/monitoredsubscriptions/{}", "2024-06-15-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.configuration_name = AAZStrArg(
            options=["-n", "--name", "--configuration-name"],
            help="The configuration name. Only 'default' value is supported.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^.*$",
            ),
        )
        _args_schema.monitor_name = AAZStrArg(
            options=["--monitor-name"],
            help="Monitor resource name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^.*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.MonitoredSubscriptionsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class MonitoredSubscriptionsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Elastic/monitors/{monitorName}/monitoredSubscriptions/{configurationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-15-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.monitored_subscription_list = AAZListType(
                serialized_name="monitoredSubscriptionList",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            monitored_subscription_list = cls._schema_on_200.properties.monitored_subscription_list
            monitored_subscription_list.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.monitored_subscription_list.Element
            _element.error = AAZStrType()
            _element.status = AAZStrType()
            _element.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
            )
            _element.tag_rules = AAZObjectType(
                serialized_name="tagRules",
            )

            tag_rules = cls._schema_on_200.properties.monitored_subscription_list.Element.tag_rules
            tag_rules.log_rules = AAZObjectType(
                serialized_name="logRules",
            )
            tag_rules.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            log_rules = cls._schema_on_200.properties.monitored_subscription_list.Element.tag_rules.log_rules
            log_rules.filtering_tags = AAZListType(
                serialized_name="filteringTags",
            )
            log_rules.send_aad_logs = AAZBoolType(
                serialized_name="sendAadLogs",
            )
            log_rules.send_activity_logs = AAZBoolType(
                serialized_name="sendActivityLogs",
            )
            log_rules.send_subscription_logs = AAZBoolType(
                serialized_name="sendSubscriptionLogs",
            )

            filtering_tags = cls._schema_on_200.properties.monitored_subscription_list.Element.tag_rules.log_rules.filtering_tags
            filtering_tags.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.monitored_subscription_list.Element.tag_rules.log_rules.filtering_tags.Element
            _element.action = AAZStrType()
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
