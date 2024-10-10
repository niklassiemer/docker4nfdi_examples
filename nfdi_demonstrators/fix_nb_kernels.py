import json
import glob

kernels={
        'experimental_workflow_demo': {
               "display_name": "Python [conda env:exp_wf_demo]",
               "language": "python",
               "name": "conda-env-exp_wf_demo-py"
               },
        'iuc04-demonstrator': {
               "display_name": "Python [conda env:iuc04]",
               "language": "python",
               "name": "conda-env-iuc04-py"
               },
        'iuc17_demonstrator': {
               "display_name": "Python [conda env:iuc17]",
               "language": "python",
               "name": "conda-env-iuc17-py"
               },
        'iuc09-demonstrator': {
               "display_name": "Python [conda env:iuc09]",
               "language": "python",
               "name": "conda-env-iuc09-py"
               }
        }

for path in kernels:
    for nb_file in glob.glob(f"{path}/**/*.ipynb", recursive=True):
        with open(nb_file) as f:
            nb = json.load(f)
        nb["metadata"]["kernelspec"] = kernels[path]
        with open(nb_file, "w") as f:
            json.dump(nb, f)

