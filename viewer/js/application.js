var n_size, m_size;
$(document).ready(function() {
n_size = 10;
m_size = 20;
  fieldFactory($('#game_field'), n_size, m_size);
});
function sendAlert(){
n_size = $('#xsize').val();
if (n_size == 0) n_size = 10;
m_size = $('#ysize').val();
if (m_size == 0) m_size = 10;
fieldFactory($('#game_field'), n_size, m_size);
}

function fieldFactory(parent_div, n, m){
  parent_div.empty();
  for (var i = 0; i < n; i++){
    row = $('<div />', {id: 'row_' + (n - i).toString(), class: 'row'});
	row.appendTo(parent_div);
	for (var j = 0; j < m; j++) {
      cell = $('<div />', { id: 'cell_' + (n - i).toString() + '_' + (m - j).toString(), 
	  class: 'cell column_' + (m - j).toString(), xcoord: (n - i), ycoord:(m - j)
	  });
    cell.appendTo(row);
	
	img = $('<div />',{class: 'image-unknown'});
	img.bind('click', function(){
	                  var currentClass = $(this).attr('class');
					  $(this).clearStyle;
					  if (currentClass == 'image-unknown') {
					      $(this).attr('class', 'image-wall');
					  } 
					  else if(currentClass == "image-wall")
					  { 
					     $(this).attr('class', 'image-ground');
					  }
					  else if(currentClass == "image-ground")
					  { 
					     $(this).attr('class', 'image-rock');
					  }
					  else if(currentClass == "image-rock")
					  { 
					     $(this).attr('class', 'image-lambda');
					  }
					  else if(currentClass == "image-lambda")
					  { 
					     $(this).attr('class', 'image-miner');
					  }
					  else if(currentClass == "image-miner")
					  { 
					     $(this).attr('class', 'image-lift');
					  }
					  else if(currentClass == "image-lift")
					  { 
					     $(this).attr('class', 'image-opened-lift');
					  }
					  else if(currentClass == "image-opened-lift")
					  { 
					     $(this).attr('class', 'image-unknown');
					  }
					  //sendCommandToSocket("clicked on:"+$(this).parent().attr('xcoord')+','+$(this).parent().attr('ycoord')+'.');
					  });
	img.appendTo(cell);
	}
	}

}

function generateText(){
  var str = "";
  var str_all = "";
  field = $('#game_field');
  for (var i = 0; i < n_size; i++){
	row = $('#row_' + (n_size - i).toString());
	str = "";
		for (var j = 0; j < m_size; j++) {	
		  
		  cell = $('#cell_' + (n_size - i).toString() + '_' + (m_size - j).toString());
		  img = $('#cell_' + (n_size - i).toString() + '_' + (m_size - j).toString() + ' div:first');
		  //img = cell.child();
		  var currentClass = img.attr('class');
		  if (currentClass == "image-unknown") {
		    str = str + ' ';
		  }
		 if (currentClass == "image-rock") {
		    str = str + "*";
		  }
		 if (currentClass == "image-miner") {
		    str = str + "R";
		  }
		  if (currentClass == "image-lambda") {
		    str = str + "L";
		  }
		  if (currentClass == "image-ground") {
		    str = str + ".";
		 }
		 if (currentClass == "image-wall") {
		    str = str + "#";
		 }
		 if (currentClass == "image-opened-lift") {
		    str = str + "O";
		 }
		}
		if (str_all != '')
		   str_all = str_all  + '\r\n'+ str;
		   else str_all=str;
	}
	
$('#id_output').html(str_all);
}



