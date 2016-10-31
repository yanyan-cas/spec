from reservoircomputing import rc_interface as rcif
import random


class RandomMappingEncoder(rcif.RCEncoder):
    def __init__(self):
        super().__init__()
        self.R = 1
        self.encoding_scheme = "separate"

    def encode_input(self, _input):
        """
        Encodes the input with randomization of the input R times

        The encoding scheme tells the encoder if the input and permutations is to be

        :param _input:
        :return:
        """
        #new_input = _input[:]
        input_vectors = []
        new_input = []

        for i in range(self.R):
            r_list = _input[:]
            random.shuffle(r_list)
            if self.encoding_scheme == "separate":
                input_vectors.append(r_list)
            elif self.encoding_scheme =="concat":
                new_input.extend(r_list)  # Flatten

        if self.encoding_scheme =="concat":
            input_vectors = [[new_input]]



        return input_vectors

    def encode_input_with_translator(self, _input, translator):
        # new_input = _input[:]
        input_vectors = []
        new_input = []

        # NB_ only separate reservoirs now possible!

        for i in range(self.R):
            _input =
            r_list = _input[:]
            random.shuffle(r_list)
            if self.encoding_scheme == "separate":
                input_vectors.append(r_list)
            elif self.encoding_scheme == "concat":
                new_input.extend(r_list)  # Flatten

        if self.encoding_scheme == "concat":
            input_vectors = [[new_input]]

        return input_vectors


    def encode_output(self, _output):
        # Flatten
        _output = [ca_val for sublist in _output for ca_val in sublist]
        return _output
