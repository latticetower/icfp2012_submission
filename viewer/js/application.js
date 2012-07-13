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
  var str_all = stringGenerator();
  $('#id_output').html(str_all);
}

function stringGenerator(){
  var str = "";
  var str_all = "";
  for (var i = 0; i < n_size; i++){
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
	return str_all;
}


function loadField(){
   var filepath = $('#id_file_open').val(); // Get the current file
   filepath = $.twFile.convertUriToLocalPath(filepath); // Convert the path to a readable format
   var text = $.twFile.load(filepath); // Load the file
alert(text);
}
function saveToFile()
{
  /* var str_all = stringGenerator();
   var filepath = document.location.href; // Get the current file
   filepath = $.twFile.convertUriToLocalPath(filepath); // Convert the path to a readable format
   var text = $.twFile.load(filepath); // Load the file
   // If the file loads succesfully create an editing element
   if(text){
					// Create a textarea
					var textarea = $("<textarea></textarea>").css({
						margin: "8px auto 0",
						display: "block",
						width: "90%",
						height: "90%"
					}).text(text);
					// Create a save button
					var dButton = $('<input type="button" value="Save">').click(function(){
						// On click, write the value of the textarea to file
						$.twFile.save(filepath, textarea.val());
						// Reload the file
						box.animate({ opacity: 0 }, function() {
							window.location.reload();
						});
					});
					// Create a div to contain the text area
					var box = $("<div></div>").css({
						position: "fixed",
						textAlign: "center",
						top:"0",
						left: "0",
						width: "100%",
						height: "100%",
						opacity: "0",
						background: "black"
					}).append(textarea).append(dButton);
					$("body").append(box);
					// Fade in
					box.animate({ opacity: 1 });
				} else {
					// Show an error message on fail
					$("#error").fadeIn();
				}
		})*/
}



