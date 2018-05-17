$(document).ready(function(){

	var numberAll = 2;


    $("#testFinal").click(function(){

		var jsonObj = {
		    members: {
	            host: "hostName",
	            viewers: {
	                user1: "value1",
	                user2: "value2",
	                user3: "value3"
	            }
	        }
		}

		var i;

		for(i=4; i<=8; i++){
		    var newUser = "user" + i;
		    var newValue = "value" + i;
		    jsonObj.members.viewers[newUser] = newValue;
		}

		var ajax = {};

        $(".content").children().each(function(){
			
			var id = $(this).attr("id");
			ajax[id] = [];

			//var a = ajax[ Object.keys(ajax).pop() ];

			ajax[ Object.keys(ajax).pop() ].variants = "saasa";
			console.log(ajax);

			var quetionText = $("textarea", this).val();
			//ajax.[id][quetionText] = quetionText;
			
			var variants = [];
			$(".input-group", this).each(function(){
				//var type = $("[name^='check']", this).attr("type");
				//var check = $("[name^='check']", this).prop("checked");
				//var text = $("[type^='text']", this).val();
				var variant = {
					'type' : $("[name^='check']", this).attr("type"),
					'check': $("[name^='check']", this).prop("checked"),
					'text' : $("[type^='text']", this).val(),
				};
				variants.push(variant);
			});

			//console.log(ajax);
			/*
		var quetion = {
			'quetionText' : quetionText,
			'variants' : {}
		};


		ajax.push(myObj);
		ajax.push(myObj2);
		console.log(ajax);
*/

		});
		//console.log(ajax);
    });

    /* Меняет на тип вопросов */
    $( "body" ).on(  "click", "[class^='btn btn-info']", function(){
    	console.log("click");
    	var input = $(this).children();
		var vied = input.attr("class").substr(5);
		
		/* Заменить на RADIO */
		if($(this).children().attr("name")=="options1"){
			var arr = $("div#variant-"+vied+" input[type='checkbox']");	
			arr.each(function(){
				$(this).attr("type", "radio")
			});
		}

		/* Заменить на CHECKBOX */
		if($(this).children().attr("name")=="options2"){
			var arr = $("div#variant-"+vied+" input[type='radio']");	
			arr.each(function(){
				$(this).attr("type", "checkbox")
			});
		}
    });

    /* Создает новый вариант вопроса  */
	$( "body" ).on("click", "[id^='createAnswer']", function(){
		console.log("click");
		var number = $(this).attr("id").substr(13);
		var type = $("input[name=check-"+number+"]").attr("type");
		$("div#variant-"+number).append("<div class='col-lg-6'><div class='input-group'><span class='input-group-addon'><input type='"+type+"' name='check-"+number+"'></span> <input type='text' class='form-control' placeholder='Вариант ответа'></div></div>");
	});

    /* Создает новый вопрос  */
	$("[id='createQuetion']").on("click",function(){
		var number = numberAll.toString();
		numberAll++;
		$("div.content").append('<div class="row" id="quetion-'+number+'"> <div class="col-xs-2 col-md-2"></div> <div class="col-xs-8 col-md-8" style="padding-top: 20px; float: center;"> <div class="panel panel-default"> <div class="panel-body"> <div class="row"> <div class="col-xs-11 col-md-11" style="padding-bottom: 20px"> <div class="btn-group" data-toggle="buttons"> <label class="btn btn-info active"> <input type="radio" class="vied-'+number+'" name="options1"> <i class= "glyphicon glyphicon-record" aria-hidden= "true" > </i> </label> <label class="btn btn-info"> <input type="radio" class="vied-'+number+'" name="options2"> <i class= "glyphicon glyphicon-check" aria-hidden= "true" > </i> </label> <label class="btn btn-info"> <input type="radio" class="vied-'+number+'" name="options3"> <i class="glyphicon glyphicon-pencil" aria-hidden="true"></i> </label> </div> </div> <div class="col-xs-1 col-md-1"> <span class="glyphicon glyphicon-remove" aria-hidden="true" style="float: right; color: #efeeef; cursor:pointer;"> </span> </div> </div> <div class="row"> <div class="col-lg-11"> <textarea class = "form-control" placeholder="Вопрос"></textarea> <br> </div> </div> <div class="row" id="variant-'+number+'"> <div class="col-lg-6"> <div class="input-group"> <span class="input-group-addon"> <input type="radio" name="check-'+number+'"> </span> <input type="text" class="form-control" placeholder="Вариант ответа"> </div> </div> </div> <div class="row"> <div class="col-xs-4 col-md-4"></div> <div class="col-xs-6 col-md-6"> <br> <button type="button" class="btn btn-success" id="createAnswer-'+number+'"> <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span> Добавить вариант ответа </button> </div> </div> </div> </div> </div> <div class="col-xs-2 col-md-2"></div> </div>');
	});


	$("#saveTest").click(function(){


		var ajax = {
			'sas' : 'sas',
		};
		
        $.ajax({
                type: "GET",
                url: "/saveTest/",
                data: {
                    'colQuietions':$(".content").children().length,
                    'nameField':$("#nameField").val(),
                    'timeField': $("#timeField").val(),
                    'categoryField': $("#categoryField").val(),
                    'shortInfoField': $("#shortInfoField").val(),
                    'fullInfoField': $("#fullInfoField").val(),
                    'ajax' : ajax,
                },
                cache : false,
                success: function(rsp) {
                },
                error: function(xhr) {
                    //Do Something to handle error
                }
            });
    });
});

