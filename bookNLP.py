from booknlp.booknlp import BookNLP

model_params={
		"pipeline":"entity,quote,supersense,event,coref", 
		"model":"big"
	}
	
booknlp=BookNLP("en", model_params)

author = 'dick'
work = 'impostor'

# Input file to process
input_file='works' + '/' + author + '/' + work + '/' + work + '.txt'

# Output directory to store resulting files in
output_directory='works' + '/' + author + '/' + work + '/'
 
# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id=work

booknlp.process(input_file, output_directory, book_id)