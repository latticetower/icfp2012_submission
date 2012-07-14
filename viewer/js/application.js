var n_size, m_size;
$(document).ready(function() {
n_size = 10;
m_size = 20;
  fieldFactory($('#game_field'), n_size, m_size);
  changemode('image-empty');
});
function sendAlert(){
n_size = $('#xsize').val();
if (n_size == 0) n_size = 10;
m_size = $('#ysize').val();
if (m_size == 0) m_size = 10;
fieldFactory($('#game_field'), n_size, m_size);
}
var startX=1, startY=1;
var isFirstClick = true;
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
	
	img = $('<div />',{class: 'image-unknown', xcoord: (n - i), ycoord:(m - j)});
	img.bind('click', function(){
	    if (click_style=="point") {
			if (input_mode == 'image-empty') 
				defaultClickHandling($(this));
			else setCellClass($(this));
    
		
		}else{
			if (isFirstClick) {
				  startX = Number($(this).attr('xcoord'));
				  startY = Number($(this).attr('ycoord'));
			} else{
				endX = Number($(this).attr('xcoord'));
				endY = Number($(this).attr('ycoord'));
				drawLine(startX, startY, endX, endY) ;
			}
			isFirstClick = !isFirstClick;
		}
					  //sendCommandToSocket("clicked on:"+$(this).parent().attr('xcoord')+','+$(this).parent().attr('ycoord')+'.');
					  });
	img.appendTo(cell);
	}
	}

}



function defaultClickHandling(el){
	var currentClass = el.attr('class');
	el.clearStyle;
	if (currentClass == 'image-unknown') {
	el.attr('class', 'image-wall');
	} else if(currentClass == "image-wall"){ 
	el.attr('class', 'image-ground');
	} else if(currentClass == "image-ground") { 
	el.attr('class', 'image-rock');
	 } else if(currentClass == "image-rock") { el.attr('class', 'image-lambda');
	 } else if(currentClass == "image-lambda") { 
	 el.attr('class', 'image-miner'); }
	else if(currentClass == "image-miner") { 
	el.attr('class', 'image-lift');
	} else if(currentClass == "image-lift") { 
	el.attr('class', 'image-opened-lift');
	 }  else if(currentClass == "image-opened-lift")  { el.attr('class', 'image-unknown');}
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
   fieldFactoryFromText($('#game_field'), text);
}

function fieldFactoryFromText(parent_div, text){
  var maxx = 0;
  var lines = text.split('\n');
  
  for (var i = 0; i < lines.length; i++) {
    if (lines[i].length > maxx) maxx = lines[i].length;
  }
 
  parent_div.empty();
  fieldFactory(parent_div,  lines.length, maxx); 
  
  for (var i =0; i < lines.length; i++) {
    for (var j = 0; j < lines[i].length; j++ ) {
      var style = '';
      if (lines[i].charAt(j) =='#') style = "image-wall";
      if (lines[i].charAt(j) =='R')  style = "image-miner";
      if (lines[i].charAt(j) =='\\') style = "image-lambda";
      if (lines[i].charAt(j) =='L') style = "image-lift";
	  if (lines[i].charAt(j) =='O') style = "image-opened-lift";
      if (lines[i].charAt(j) =='*') style = "image-rock";
      if (lines[i].charAt(j) =='.') style = "image-ground";
	  $("#cell_" + (lines.length - i) + "_" + (maxx - j) ).children().removeClass();
      $("#cell_" + (lines.length - i) + "_" + (maxx - j) ).children().addClass(style);
    }
  }
}

function saveToFile()
{
var filepath=$("#id_file_save").val();		
filepath = $.twFile.convertUriToLocalPath(filepath);
var str_all = stringGenerator();

$.twFile.save(filepath, str_all);

}
var input_mode= "image-empty";
function changemode(new_mode){
  input_mode = new_mode;
  $("#id_input_mode").html(new_mode+ ', '+click_style);
  if (new_mode == "image-empty"){}
  if (new_mode == "image-miner"){}
  if (new_mode == "image-lambda"){}
  if (new_mode == "image-opened-lift"){}
  if (new_mode == "image-lift"){ }
  if (new_mode == "image-ground"){ }
  if (new_mode == "image-wall"){}
  if (new_mode == "image-rock"){ }
}
var click_style = "point";
function changeClickStyle(){
  if (click_style == "point"){
    click_style = "line";
   } else if (click_style == "line"){
      click_style = "point";
  }
  $("#id_input_mode").html(new_mode + ', ' + click_style);
}

function setCellClass(el){

  if (input_mode != "image-empty"){
    el.clearStyle;
    el.attr('class', input_mode);
   }
   else defaultClickHandling(el);
}
function drawLine(x1, y1, x2, y2) {
    deltaX = Math.abs(x2 - x1);
    deltaY = Math.abs(y2 - y1);
    signX = (x1 < x2 ? 1 : -1);
    signY = (y1 < y2 ? 1 : -1);
	
    //
    var error = deltaX - deltaY;
    //
	
    setCellClass($('#cell_' + x2 +'_' + y2+' div:first'));
    while(x1 != x2 || y1 != y2) {
        //setPixel(x1, y1);
		
		setCellClass($('#cell_' + x1 +'_' + y1 + ' div:first'));
        var error2 = error * 2;
        //
        if(error2 > -deltaY) {
            error -= deltaY;
            x1 += signX;
        }
        if(error2 < deltaX) {
            error += deltaX;
            y1 += signY;
        }
    }
 
}


