$(function(){
    $(".login").click(function(){
        var data = new Array();
        data['username'] = $('.username').val();
        data['password'] = $('.password').val();
        data['type'] = "login";
        $.ajax({
            type:'post',
            url:"/check",
            data:{'username':data['username'],'password':data['password'],'type':data['type']},
            dataType:'json',
            success:function(data){
                if (data == '1'){
                    alert("username is not exist.");
                }
                if(data == '2'){
                    alert("password is wrong.");
                }
              
            },
            error:function(){
                alert("error");
            }
        });
    });

    $(".register").click(function(){
        var datas = new Array();
        datas['username'] = $('.username').val();
        datas['email'] = $('.email').val();
        datas['password'] = $('.password').val();
        datas['type'] = "register";
        $.ajax({
            type:'post',
            url:"/check",
            data:{'username':datas['username'],'password':datas['password'],'email':datas['email'],'type':datas['type']},
            dataType:'json',
            success:function(msg){
                if(msg == '1'){
                    alert("email is exist.");
                }
                if(msg == '2'){
                    alert("username is exist.");
                }
                if(msg == '3'){
                    var content = '<div><h3>yes,you are goodman,'+datas['username']+' ,login success!!,</h3><h3>your Email is '+datas['email']+'</h3></div>';
                    $('.container').html(content);
                }
            },
            error:function(){
                alert("error");
            }

        });


    });


});