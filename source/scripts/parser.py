def main() -> None:
    """Start fetching user input and process data."""
    # set custom formatter class for parser
    class CapitalizedUsageHelpFormatter(ap.HelpFormatter):
        def add_usage(self, usage, actions, groups, prefix=None):
            if prefix is None:
                prefix = "Usage: "
            return super(CapitalizedUsageHelpFormatter, self).add_usage(usage, actions, groups, prefix)
        
    # set parser
    parser = ap.ArgumentParser(
        prog="ghact",
        add_help=False,
        formatter_class=CapitalizedUsageHelpFormatter,
        description="Script to get user activity on GitHub.",
        epilog="This project is inspired by https://roadmap.sh/.",
    )
    
    # set custopm titles for arguments in help message
    parser._positionals.title = "Positional arguments"
    parser._optionals.title = "Optional arguments"
    
    # add arguments to the parser
    parser.add_argument("user_name", type=str, metavar="<user_name>", default="IliaStarchevus",
                        help="Set real user name on GitHub.")
    parser.add_argument("-h", "--help", action="help",
                        help="Show this help message and exit.")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.1.0",
                        help="Show program's version number and exit.")
    parser.add_argument("--page", type=int, metavar="<number>", default=1,
                        help="Set a number of page with results.")
    parser.add_argument("--per_page", type=int, metavar="<number>", default=100,
                        help="Set amount of results on page.")
    parser.set_defaults(func=pr.process_data)
    
    # parse arguments
    args = parser.parse_args()
    logger.debug(f"{args=}")
    args.func(args.user_name, args.per_page, args.page)


if __name__ != "__main__":
    import argparse as ap
    import logging as lg
    
    from . import processor as pr
    
    # get logger
    logger = lg.getLogger(name=__name__)