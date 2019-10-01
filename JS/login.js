$(function(){
	$('input:submit[id="submit"]').click(function(){
		if(!input_check()){
			return false;
		}
	});
});

function input_check(){
    var result = true;

	$('#fm2').removeClass("inp_error");
    
	$("#fm2_error").empty();
    
    var loginid   = $("#fm1").val();
    var pass  = $("#fm2").val();
    

    // ログインできるかどうか 今は5がログインIDかつパスワードに設定されている。
    if(loginid != 12345 && pass != 12345678){
		$("#fm2_error").html("ログインIDとパスワードが間違っています。");
		$("#fm2").addClass("inp_error");
		result = false;
    }else if(pass != 12345678){
        $("#fm2_error").html("パスワードが間違っています。");
		$("#fm2").addClass("inp_error");
		result = false;
    }else if(loginid != 12345){
        $("#fm2_error").html("ログインIDが間違っています。");
		$("#fm2").addClass("inp_error");
		result = false;
    }

    if(result == true){
        window.location.href = '../ShopSpecial/HTML/menu.html';
    }
}
