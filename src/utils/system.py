

def clean_args(args):
    return [arg.lower().replace("--", "") for arg in args if "--" in arg]
