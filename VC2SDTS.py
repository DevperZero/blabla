'''
Devper Zero - DZ
'''

import sys,os
import csv

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Lack arguments...')
    else:
        inTestCase = False
        inFilePath = sys.argv[1]

        unitName = ''
        subProgram = ''
        testName = ''
        inputParam = ''
        expectedParam = ''
        outFileName = 'output.csv'

        fields = ['Unit  Name', 'Function Test Name', 'Test Case Name', 'Input', 'Expected']

        with open(inFilePath) as inFile:
            with open(outFileName,'w', newline='') as csvOut:
                csvOutWriter = csv.writer(csvOut)
                csvOutWriter.writerow(fields)

                while True:
                    line = inFile.readline()

                    """Break if end of file"""
                    if not line:
                        break
                    elif line.startswith('TEST.UNIT:'):
                        unitName = line.removeprefix('TEST.UNIT:')
                    elif line.startswith('TEST.SUBPROGRAM:'):
                        subProgram = line.removeprefix('TEST.SUBPROGRAM:')
                    elif line.startswith('TEST.NAME:'):
                        testName = line.removeprefix('TEST.NAME:')
                        print('Start with test case: ' + testName)
                    elif line.startswith('TEST.VALUE:'):
                        inputParam += line.removeprefix('TEST.')
                    elif line.startswith('TEST.STUB:'):
                        inputParam += line.removeprefix('TEST.')
                    elif line.startswith('TEST.EXPECTED:'):
                        expectedParam += line.removeprefix('TEST.EXPECTED:')
                    elif line.startswith('TEST.FLOW'):
                        expectedParam += 'FLOW\n'
                        line = inFile.readline()
                        while not line.startswith('TEST.END_FLOW'):
                            expectedParam += line
                            line = inFile.readline()
                    elif line.startswith('TEST.END'):
                        unitName.replace('\n','')
                        subProgram.replace('\n','')
                        testName.replace('\n','')
                        inputParam.replace('\n','')
                        expectedParam.replace('\n','')
                        csvOutWriter.writerow([unitName, subProgram, testName, inputParam, expectedParam])
                        unitName = ''
                        subProgram = ''
                        testName = ''
                        inputParam = ''
                        expectedParam = ''
                
