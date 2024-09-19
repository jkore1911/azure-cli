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
    "elastic monitor update-vm-collection",
)
class UpdateVmCollection(AAZCommand):
    """Update the vm details that will be monitored by the Elastic monitor                                resource.

    :example: Update vm collection
        az elastic monitor update-vm-collection --monitor-name monitor1 -g rg --operation-name Add --vi-resource-id id
    """

    _aaz_info = {
        "version": "2024-06-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.elastic/monitors/{}/vmcollectionupdate", "2024-06-15-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return None

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
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

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.operation_name = AAZStrArg(
            options=["--operation-name"],
            arg_group="Body",
            help="Operation to be performed for given VM.",
            enum={"Add": "Add", "Delete": "Delete"},
        )
        _args_schema.vm_resource_id = AAZStrArg(
            options=["--vm-resource-id"],
            arg_group="Body",
            help="ARM id of the VM resource.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VMCollectionUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class VMCollectionUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Elastic/monitors/{monitorName}/vmCollectionUpdate",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
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
                    "Content-Type", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("operationName", AAZStrType, ".operation_name")
            _builder.set_prop("vmResourceId", AAZStrType, ".vm_resource_id")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            pass


class _UpdateVmCollectionHelper:
    """Helper class for UpdateVmCollection"""


__all__ = ["UpdateVmCollection"]
