import os
import yaml
import itertools
from jinja2 import Template

from jinja_gen.arguments import get_args


def generate_matrix(matrix, output_dir, prefix='', ext='', defaults={},
                    name_keys=None, output_name_key=None, output_dir_key=None):
    name_keys = name_keys or matrix.keys()
    for config in itertools.product(*matrix.values()):
        template_vars = {**defaults, **dict(zip(matrix.keys(), config))}
        name = prefix + '-'.join(map(lambda x: str(template_vars[x]), name_keys))
        output_f = os.path.join(output_dir, name, 'run' + ext)

        if output_name_key:
            template_vars[output_name_key] = name
        if output_dir_key:
            template_vars[output_dir_key] = os.path.dirname(output_f)

        yield output_f, template_vars


def main():
    args = get_args()

    with open(args.file, 'r') as stream:
        data = yaml.load(stream)

        # Required Keys
        for key in ['template', 'matrix']:
            assert key in data, '"{}" key missing in "{}"'.format(key, args.file)

        # If template path is not absolute, consider relative to config file
        if not os.path.isabs(data['template']):
            data['template'] = os.path.join(os.path.dirname(args.file), data['template'])

        # Optional Keys
        data['name_keys'] = data.get('name_keys', None)
        data['ext'] = data.get('ext', '')
        data['prefix'] = data.get('prefix', '')
        data['defaults'] = data.get('defaults', {})

        with open(data['template'], 'r') as template_f:
            template = Template(template_f.read())

        for matrix in data['matrix']:
            for out_f, template_vars in generate_matrix(matrix, args.output_dir,
                                                        prefix=data['prefix'], ext=data['ext'],
                                                        defaults=data['defaults'], name_keys=data['name_keys'],
                                                        output_name_key=args.output_name_key,
                                                        output_dir_key=args.output_dir_key):
                if not args.dry:
                    rendered_string = template.render(template_vars)
                    if not os.path.isdir(os.path.dirname(out_f)):
                        os.makedirs(os.path.dirname(out_f))
                    with open(out_f, 'w') as f:
                        f.write(rendered_string)
                print('Generated {}'.format(out_f))
