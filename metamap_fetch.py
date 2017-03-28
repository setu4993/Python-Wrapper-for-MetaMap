import subprocess
import tempfile

def metamap_fetch(sentences, mm_location):

    if sentences is not None:
        in_file = tempfile.NamedTemporaryFile(mode="wb", delete=False)
        for sentence in sentences:
            in_file.write(b'%r\n' % sentence)
    else:
        print("No input defined.")

    in_file.flush()

    out_file = tempfile.NamedTemporaryFile(mode="r", delete=False)

    command = [mm_location]

    command.append("-f") #number the mappings
    command.append("-s") #short semantic types
    command.append("--negex") #negex
    command.append("--silent") #hide header information
    command.append("-G") #show sources
    command.append("-c") #show candidates
    
    '''
    add other options here in the format as below
    command.append("")
    '''
    
    command.append(in_file.name)
    command.append(out_file.name)

    run_metamap = subprocess.Popen(command, stdout=subprocess.PIPE)

    while run_metamap.poll() is None:
        stdout = str(run_metamap.stdout.readline())
        if 'ERROR' in stdout:
            run_metamap.terminate()
            error = stdout.rstrip()
    output = str(out_file.read())
    return output
