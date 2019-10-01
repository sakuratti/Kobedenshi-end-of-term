$(function(){
	$('input:submit[id="submit"]').click(function(){
		if(!input_check()){
			return false;
		}
	});
});

function input_check(){
    var result = true;

    $('#fm1').removeClass("inp_error");
	$('#fm2').removeClass("inp_error");
    $('#fm3').removeClass("inp_error");
    
    $("#fm1_error").empty();
	$("#fm2_error").empty();
    $("#fm3_error").empty();
    
    var time   = $("#fm1").val();
	var total  = $("#fm2").val();
    var amount = $("#fm3").val();

    // 残り時間
    if(time <= 0){
    $("#fm1_error").html("※ 残り時間を入力してください");
		$("#fm1").addClass("inp_error");
		result = false;
    }
    // 一日の販売数
    if(total <= 0){
		$("#fm2_error").html("※ 一日の平均販売数を入力してください");
		$("#fm2").addClass("inp_error");
		result = false;
    }
    // 在庫数
    if(amount <= 0){
		$("#fm3_error").html("※ 在庫を入力してください");
		$("#fm3").addClass("inp_error");
		result = false;
    }

    return result
}