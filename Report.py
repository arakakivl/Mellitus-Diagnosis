'''
Grupo iamAware:
João Busar,
Larissa xyz,
Luiza Hubert,
Rafael Nunes,
Vitor Arakaki
'''

class Report:
    # Constructor
    def __init__(self, inFasting, oralTolerance, casual):
        self.inFasting = inFasting
        self.oralTolerance = oralTolerance
        self.casual = casual

        # Setting the diagnosis.
        if casual < 200:
            if oralTolerance < 140:
                self.result = 0 # Normal
            else:
                self.result = 1 # Prediabetes
        else:
            self.result = 2 # Diabetes mellitus

    '''
    This function returns the obj as a "readable data" for
    our AI model.
    '''
    def raw(self):
        return [self.inFasting, self.oralTolerance, self.casual]