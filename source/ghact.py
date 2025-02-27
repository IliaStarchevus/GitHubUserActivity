# python


if __name__ == "__main__":
    import logging as lg
    import os
    
    from scripts import parser
    
    # set path to the logs file
    logsPath = f"{os.path.realpath(__file__)}/../../logs/ghact.log"
    logsDir, _ = os.path.split(logsPath)
    
    # check if logs folders and files exist
    if not os.path.exists(logsDir):
        os.makedirs(logsDir)
    if not os.path.exists(logsPath):
        with open(logsPath, "w", encoding="utf-8"): pass

    # config logger
    lg.basicConfig(filename=logsPath, filemode="w",
                   datefmt="%Y-%m-%d %H:%M:%S",
                   format="%(name)s %(levelname)s %(asctime)s %(message)s",
                   level=lg.DEBUG)

    # start the scripts
    parser.main()
