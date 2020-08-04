from src.utils.logger import logger


def process_input_file(input_filename: str = None) -> dict:
    # Validate input
    if input_filename is None:
        raise ValueError("input_filename cannot be None!")

    logger.debug("input_filename = {}".format(input_filename))

    # Open input file and read in the contents to generate the nodes and edges
    f = open(input_filename, 'r')
    lines = f.readlines()

    return_object: dict = dict(
        {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }
    )

    for line in lines:
        logger.debug("line = {}".format(line))
        edge = line.strip('(\n').split('=')
        edge[0] = edge[0][:-1]  # <- strip the closing bracket.
        edge[1] = float(edge[1])  # <- string to float.
        node_info = edge[0].split(',')
        edge = (node_info[0], node_info[1], edge[1])
        timestep: int = int(node_info[2])

        # Create an object that has an array of vertices and edge values as a tuple for each timestep
        # e.g.
        # {
        #   0: [('A0', 'A9', 0.686), ('B0', 'B9', 0.731)],
        #   1: [('A0', 'A9', 0.789), ('B0', 'B9', 0.632)]
        # }
        # This will help with the management of the input data.
        return_object[timestep].append(edge)

    f.close()
    return return_object

