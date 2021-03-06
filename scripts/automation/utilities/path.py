# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os.path

from automation.utilities.const import COMMAND_MODULE_PREFIX


def get_repo_root():
    """Returns the path to the source code root directory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(current_dir, 'CONTRIBUTING.rst')):
        current_dir = os.path.dirname(current_dir)

    return current_dir


def get_all_module_paths():
    """List all core and command modules"""
    return get_command_modules_paths(include_prefix=True)


def get_command_modules_paths(include_prefix=False):
    """List all the command modules"""
    root = get_repo_root()
    modules = []
    name = 'batch-extensions'
    sdk_name = 'azure-' + name if include_prefix else name
    modules.append((sdk_name, os.path.join(root, name)))
    
    cli_name = COMMAND_MODULE_PREFIX + name if include_prefix else name
    modules.append((cli_name, os.path.join(root, 'batch-cli-extensions')))
    return modules


def get_command_modules_paths_with_tests():
    """List all the command modules and returns those have tests folder"""
    for name, module_path in get_command_modules_paths():
        test_path = os.path.join(module_path, 'tests')
        if os.path.exists(test_path):
            yield name, module_path, test_path


def make_dirs(path):
    """Create a directories recursively"""
    import errno
    try:
        os.makedirs(path)
    except OSError as exc:  # Python <= 2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def get_test_results_dir(with_timestamp=None, prefix=None):
    """Returns the folder where test results should be saved to. If the folder doesn't exist,
    it will be created."""
    result = os.path.join(get_repo_root(), 'test_results')

    if isinstance(with_timestamp, bool):
        from datetime import datetime
        with_timestamp = datetime.now()

    if with_timestamp:
        if prefix:
            result = os.path.join(result, with_timestamp.strftime(prefix + '_%Y%m%d_%H%M%S'))
        else:
            result = os.path.join(result, with_timestamp.strftime('%Y%m%d_%H%M%S'))

    if not os.path.exists(result):
        make_dirs(result)

    if not os.path.exists(result) or not os.path.isdir(result):
        raise Exception('Failed to create test result dir {}'.format(result))

    return result


def filter_user_selected_modules(user_input_modules):
    import itertools

    existing_modules = list(itertools.chain(get_command_modules_paths()))

    if user_input_modules:
        selected_modules = set(user_input_modules)
        extra = selected_modules - set([name for name, _ in existing_modules])
        if any(extra):
            print('ERROR: These modules do not exist: {}.'.format(', '.join(extra)))
            return None

        return list((name, module) for name, module in existing_modules
                    if name in selected_modules)
    else:
        return list((name, module) for name, module in existing_modules)


def filter_user_selected_modules_with_tests(user_input_modules):
    import itertools

    existing_modules = list(itertools.chain(get_command_modules_paths_with_tests()))

    if user_input_modules:
        selected_modules = set(user_input_modules)
        extra = selected_modules - set([name for name, _, _ in existing_modules])
        if any(extra):
            print('ERROR: These modules do not exist: {}.'.format(', '.join(extra)))
            return None

        return list((name, module, test) for name, module, test in existing_modules
                    if name in selected_modules)
    else:
        return list((name, module, test) for name, module, test in existing_modules)
