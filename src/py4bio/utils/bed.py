import pandas as pd


class Bed:
    '''A bed like class. This class can import and export bed file.'''

    def __init__(self) -> None:
        pass

    def as_bed(self, bed: list) -> None:
        '''Import bed like content from a list.
        bed: bed like list'''
        self.bed = pd.DataFrame(bed)

    def read_bed(self, bed_path: str) -> None:
        '''Import bed from a bed file.
        bed_path: bed file path'''
        with open(bed_path) as bed_file:
            self.bed: pd.DataFrame = pd.read_table(bed_file, header=None)

    def read_csv(self, csv_path: str) -> None:
        '''Import bed from a csv file with a header.
        csv_path: csv file path'''
        with open(csv_path) as csv_file:
            self.bed: pd.DataFrame = pd.read_csv(csv_file)

    def read_tsv(self, tsv_path: str) -> None:
        '''Import bed from a tsv file with a header.
        tsv_path: tsv file path'''
        with open(tsv_path) as tsv_file:
            self.bed: pd.DataFrame = pd.read_table(tsv_file)

    def load(self,
             bed_content: str,
             sep: str = '\t',
             header: bool = False) -> None:
        '''Load a bed like string
        bed_content: string contain bed like content
        sep: delimiter to use
        header: first row is column name or not'''
        bed_content: list = bed_content.split('\n')
        while '' in bed_content:
            bed_content.remove('')
        if header:
            column_name = bed_content[0].split(sep)
            bed_content = bed_content[1:]
        bed_content = [line.split(sep) for line in bed_content]
        self.bed = pd.DataFrame(bed_content)
        if header:
            self.bed.columns = column_name

    def to_bed(self, bed_path: str) -> None:
        '''Export bed to a bed file.
        bed_path: bed file path'''
        self.bed.to_csv(bed_path, sep='\t', header=False, index=False)

    def to_csv(self, csv_path: str) -> None:
        '''Export bed to a csv file with a header.
        csv_path: csv file path'''
        self.bed.to_csv(csv_path, index=False)

    def to_tsv(self, tsv_path: str) -> None:
        '''Export bed to a tsv file with a header.
        tsv_path: tsv file path'''
        self.bed.to_csv(tsv_path, sep='\t', index=False)
