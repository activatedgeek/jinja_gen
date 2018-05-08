import os
import yaml
from jinja2 import Template
from datetime import datetime

from jinja_gen.arguments import get_args
from jinja_gen.utils import resolve_random_matrix, generate_matrix


def main():
    args = get_args()

    matrix_modified = False

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

        for i in range(len(data['matrix'])):
            data['matrix'][i], mod = resolve_random_matrix(data['matrix'][i])
            matrix_modified = matrix_modified or mod

            for out_f, template_vars in generate_matrix(data['matrix'][i], args.output_dir,
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

                if args.debug:
                    print('Generated {}'.format(out_f))

    # Dump an extra file with the deterministic values (if it had distributional values)
    if args.no_dump and matrix_modified:
        f_name, ext = os.path.splitext(os.path.basename(args.config))
        deterministic_dump_file = os.path.join(os.path.dirname(args.config),
                                               f_name + '-' + str(datetime.now().strftime('%b-%d-%H-%M-%S')) + ext)
        with open(deterministic_dump_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
