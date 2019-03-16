import numpy as np
class TableExamplesGenerator(object):

    def __init__(self, data):
        self.data = data
        self.table = []
        self.column_sizes = []
        self.start_of_line = '    | '
        self.vertical_separator = ' | '
        self.end_of_line = ' |'

    def call(self):
        self.calculate_columns_sizes()
        self.prepare_meta_template()
        self.prepare_template()
        self.insert_data_to_template()
        return self.table

    def calculate_columns_sizes(self):
        sizes = self.create_matrix_of_sizes()
        transposed = self.transpose_matrix_of_sizes(sizes)
        for size in transposed:
            self.column_sizes.append(max(size))

    def create_matrix_of_sizes(self):
        sizes = []
        for row in self.data:
            size_row = []
            for item in row:
                size_row.append(len(str(item)))
            sizes.append(size_row)
        return sizes

    def transpose_matrix_of_sizes(self, sizes):
        return list(map(list, np.transpose(sizes)))

    def prepare_meta_template(self):
        number_of_elements = len(self.column_sizes)
        self.meta_template = self.vertical_separator.join(
            ['{{{{{0}:{{{0}}}}}}}'.format(i)
            for i in range(number_of_elements)
            ]
        )

    def prepare_template(self):
        self.template = '{0}{1}{2}'.format(
        self.start_of_line,
        self.meta_template.format(*self.column_sizes),
        self.end_of_line
        )

    def insert_data_to_template(self):
        for row in self.data:
            self.table.append(self.template.format(*row))
        self.table = '\n'.join(self.table)
