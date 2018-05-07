import os
import yaml
import itertools
from jinja2 import Template

from jinja_gen.arguments import get_args


def generate_matrix(matrix, output_dir, template_fname, defaults=None,
                    name_keys=None, output_name_key=None, output_dir_key=None):
    name_keys = name_keys or matrix.keys()
    for config in itertools.product(*matrix.values()):
        template_vars = {**(defaults or {}), **dict(zip(matrix.keys(), config))}
        name = '-'.join(map(lambda x: str(template_vars[x]), name_keys))
        output_f = os.path.join(output_dir, name, template_fname)

        if output_name_key:
            template_vars[output_name_key] = name
        if output_dir_key:
            template_vars[output_dir_key] = os.path.dirname(output_f)

        yield output_f, template_vars


def main():
    args = get_args()

    with open(args.config, 'r') as stream:
        data = yaml.load(stream)

        # Required Keys
        assert 'matrix' in data, '"matrix" key missing in "{}"'.format(args.config)

        # Optional Keys
        data['name_keys'] = data.get('name_keys', None)
        data['defaults'] = data.get('defaults', {})

        # Parse extension from the template file
        template_fname = os.path.basename(args.file)

        with open(args.file, 'r') as template_f:
            template = Template(template_f.read())

        for matrix in data['matrix']:
            for out_f, template_vars in generate_matrix(matrix, args.output_dir,
                                                        template_fname=template_fname,
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
