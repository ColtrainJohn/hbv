import pathlib 
from string import Template


#toolsPath = str(pathlib.Path(__file__).parent.resolve())
#rootPath = '/'.join(toolsPath.split('/')[:-1])
blastOutCols = 'qseqid sseqid qstart qend sstart send qseq sseq evalue length mismatch positive gaps'
blastCmd = Template('$root')

argsCmd = {
        '-db' : Template('$root'),
        '-query' : Template('$file'),
        '-outfmt' : "6 " + blastOutCols,
        '-max_target_seqs' : '1'
            }

resultDict = {
            
    'result' : {
        
        'conclusion' : None,

    
        }


        }

