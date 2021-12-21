import shutil
from pathlib import Path


def make_dir(dir_path):
    dir_path.mkdir(exist_ok=True)


def clean_any_content(folder: Path) -> None:
    for file_path in folder.iterdir():
        if file_path.is_file():
            file_path.unlink()
        elif file_path.is_dir():
            shutil.rmtree(file_path)


def define_build_dir():
    global build_dir
    build_dir = Path('build')


def prepare_build_dir():
    define_build_dir()
    make_dir(build_dir)
    clean_any_content(build_dir)

    return build_dir


def layout_from_file(lines):
    modifiers = [
        'shift',
        'ctrl',
        'alt'
    ]

    layout = {}
    for line in lines:
        line = line.strip().lower()
        if not line or line.startswith(';'):
            continue

        def gen_key(_key: str):
            _key = _key.strip()

            if _key in modifiers:
                _key = 'left' + _key

            if not (_key.startswith('rel') or _key.startswith('btn')):
                _key = 'key:' + _key

            return _key

        orig_key, command = line.split()
        orig_key = gen_key(orig_key)
        command_keys = [gen_key(key) for key in command.split('+')]
        layout[orig_key] = command_keys

    return layout


def read_layout(layout_name):
    with open(layout_name + '.csv') as file:
        lines = file.readlines()
    return layout_from_file(lines)


def convert_to_args(layout):
    output_args = []
    for orig_key, command_keys in layout.items():
        output_arg = '--map ' + f'{orig_key}@dev_layout ' + ' '.join(command_keys) + ' \\'
        output_args.append(output_arg)
    return output_args


keyboard_id = ''


def write_file(filename, content):
    with open(filename, mode='w+', encoding='utf8') as file:
        file.write(content)


def write_layout(layout_name, lines):
    write_file(build_dir / (layout_name + '.sh'), '\n'.join(lines))


toggle_key = 'delete'
exec_path = '/home/user/CLionProjects/evsieve/target/release/'
device_id = 'usb-Logitech_USB_Receiver-if02-event-mouse'

common_headers = [
    '#!/bin/sh',
    '',
    f'cd {exec_path} || {{ echo "Error changing directory"; exit 1; }}',
    f'sudo ./evsieve --input /dev/input/by-id/{device_id} ',
]


def gen_print_events():
    print_headers = common_headers.copy()
    print_headers[-1] = print_headers[-1] + '--print'
    write_layout('print_events', print_headers)


def convert_layout(raw_layout):
    convert_headers = common_headers.copy()
    convert_headers[-1] = convert_headers[-1] + 'grab \\'

    headers = [
        f'--hook key:{toggle_key} toggle \\',  # exec-shell=
        f'--block key:{toggle_key} \\',
        '--toggle "" @norm_layout @dev_layout \\',
    ]

    ending = ['--output']
    output_args = convert_to_args(raw_layout)

    output_args = headers + output_args + ending

    output_args = [' ' * len('evsieve ') + line for line in output_args]
    output_args = convert_headers + output_args
    return output_args


def gen_layout(layout_name):
    raw_layout = read_layout(layout_name)
    out_args = convert_layout(raw_layout)
    write_layout(layout_name, out_args)


def gen_layouts():
    prepare_build_dir()
    gen_layout('dev')


if __name__ == '__main__':
    gen_layouts()
    gen_print_events()
