__author__ = 'Benjamin Millot'
__date__ = '13/11/2015'


def fasta_input():
    """
    Get the location of the input file
    """
    return raw_input('Please enter the path of your fasta file:\n')
    
def parse_fasta(fasta):
    """
    Parse the fasta file
    Input :
        fasta : fasta file
    Output :
        parse : concatenated list of sequence name, sequence and sequence length
    """

    flag_name = -1
    flag_seq = -1
    seq = ''
    parse =[[],[],[]]
    
    with open(fasta,'r') as filin:
        for line in filin:
            # ignore comments
            if line.startswith(';'):
                pass
            # start a new sequence and store the name
            if line.startswith('>'):
                parse[0].append(line[:-1])
                flag_name += 1
            else :
                # if the sequence continue over the lines, concatenates them
                if flag_seq == flag_name - 2:
                    parse[1].append(seq)
                    seq = ''
                    flag_seq += 1
                # if a new sequence name appear, store the sequence in parse
                # but it will never store last sequence since there is nothing
                # after
                if flag_seq == flag_name - 1:
                    seq = seq + line[:-1]
        # update last sequence we did not add before
        parse[1].append(seq)
    

    # update sequence length
    for i in parse[1]:
        parse[2].append(len(i))

    return parse


def output_making(parse):
    """
    Create the output file at the end of the analysis
    Input:
        parse : concatenated list of sequence name, sequence and sequence length
    """
    
    size = len(parse[0])

    with open('fasta.log', 'w') as filout:
        filout.write("\n{0} sequence(s) has been found in this file\n".format(size))
        filout.write("name\tlength\n")
        for i in range(size):
            filout.write("{0}\t{1}\n".format(parse[0][i], parse[2][i]))

if __name__ == '__main__':
    fasta = fasta_input()
    infos = parse_fasta(fasta)
    output_making(infos)
