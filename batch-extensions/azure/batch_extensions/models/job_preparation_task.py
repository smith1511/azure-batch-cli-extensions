# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=redefined-builtin

from msrest.serialization import Model


class JobPreparationTask(Model):
    """A Job Preparation task to run before any tasks of the job on any given
    compute node.

    :param id: A string that uniquely identifies the Job Preparation task
     within the job. The ID can contain any combination of alphanumeric
     characters including hyphens and underscores and cannot contain more than
     64 characters. If you do not specify this property, the Batch service
     assigns a default value of 'jobpreparation'. No other task in the job can
     have the same id as the Job Preparation task. If you try to submit a task
     with the same id, the Batch service rejects the request with error code
     TaskIdSameAsJobPreparationTask; if you are calling the REST API directly,
     the HTTP status code is 409 (Conflict).
    :type id: str
    :param command_line: The command line of the Job Preparation task. The
     command line does not run under a shell, and therefore cannot take
     advantage of shell features such as environment variable expansion. If you
     want to take advantage of such features, you should invoke the shell in
     the command line, for example using "cmd /c MyCommand" in Windows or
     "/bin/sh -c MyCommand" in Linux.
    :type command_line: str
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. Files listed
     under this element are located in the task's working directory.
    :type resource_files: list of :class:`ExtendedResourceFile
     <azure.batch_extensions.models.ExtendedResourceFile>`
    :param environment_settings: A list of environment variable settings for
     the Job Preparation task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param constraints: Constraints that apply to the Job Preparation task.
    :type constraints: :class:`TaskConstraints
     <azure.batch.models.TaskConstraints>`
    :param wait_for_success: Whether the Batch service should wait for the Job
     Preparation task to complete successfully before scheduling any other
     tasks of the job on the compute node. If true and the Job Preparation task
     fails on a compute node, the Batch service retries the Job Preparation
     task up to its maximum retry count (as specified in the constraints
     element). If the task has still not completed successfully after all
     retries, then the Batch service will not schedule tasks of the job to the
     compute node. The compute node remains active and eligible to run tasks of
     other jobs. If false, the Batch service will not wait for the Job
     Preparation task to complete. In this case, other tasks of the job can
     start executing on the compute node while the Job Preparation task is
     still running; and even if the Job Preparation task fails, new tasks will
     continue to be scheduled on the node. The default value is true.
    :type wait_for_success: bool
    :param user_identity: The user identity under which the Job Preparation
     task runs. If omitted, the task runs as a non-administrative user unique
     to the task.
    :type user_identity: :class:`UserIdentity
     <azure.batch.models.UserIdentity>`
    :param rerun_on_node_reboot_after_success: Whether the Batch service
     should rerun the Job Preparation task after a compute node reboots. The
     Job Preparation task is always rerun if a compute node is reimaged, or if
     the Job Preparation task did not complete (e.g. because the reboot
     occurred while the task was running). Therefore, you should always write a
     Job Preparation task to be idempotent and to behave correctly if run
     multiple times. The default value is true.
    :type rerun_on_node_reboot_after_success: bool
    """

    _validation = {
        'command_line': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ExtendedResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'wait_for_success': {'key': 'waitForSuccess', 'type': 'bool'},
        'user_identity': {'key': 'userIdentity', 'type': 'UserIdentity'},
        'rerun_on_node_reboot_after_success': {'key': 'rerunOnNodeRebootAfterSuccess', 'type': 'bool'},
    }

    def __init__(self, command_line, id=None, resource_files=None, environment_settings=None,
                 constraints=None, wait_for_success=None, user_identity=None,
                 rerun_on_node_reboot_after_success=None):
        self.id = id
        self.command_line = command_line
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.constraints = constraints
        self.wait_for_success = wait_for_success
        self.user_identity = user_identity
        self.rerun_on_node_reboot_after_success = rerun_on_node_reboot_after_success
