$(function() {
	var num=0;
	var i=0;
	var flag=true;
	var timer;
	if (location.search != '') {
		var string = location.search.substr(1);
		var arr = string.split('=');
		$(".box2 .a1").text(decodeURI(arr[1]));
		// 页面提交的时候，将它用%XX方式编码转换了，这样的字符串，如果在页面中，可以用JavaScript的decodeURI方法将其转换为中文出来。
		$(".box2 .a1").prop("href", "javascript:;");
		$(".box2 div").css("display","block");
		$(".box2 li:last").mouseenter(function(){
			$(".box2 p").removeClass("yinchan");
		})
		$(".box2 li:last").mouseleave(function(){
			$(".box2 p").addClass("yinchan");
		})
	}
	if($(".a1").text()!="登录"){
		$(".box1 li").eq(9).click(function(){
			window.open(".html?username=" +$(".a1").text() , "_blank");
		})
		$(".box1 li").eq(7).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".box1 li").eq(4).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".b1").click(function(){
			// window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".box13 li").eq(4).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".box13 li").eq(2).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".box1 li").eq(0).click(function(){
			window.open("index.html?username=" + $(".a1").text() , "_self");
		})
		$(".box3>a").click(function(){
			window.open("index.html?username=" + $(".a1").text() , "_self");
		})
		$(".box3 #fw").click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".a6 li").eq(1).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".a6 li").eq(2).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".a6 li").eq(3).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".a6 li").eq(4).click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
		$(".dj a").click(function(){
			window.open(".html?username=" + $(".a1").text() , "_blank");
		})
	}else{
		$(".box1 li").eq(4).click(function(){
			window.open(".html" , "_blank");
		})
		$(".box1 li").eq(9).click(function(){
			window.open(".html", "_blank");
		})
		$(".box1 li").eq(7).click(function(){
			window.open(".html", "_blank");
		})
		$(".b1").click(function(){
			// alert("Please enter");
			window.open(".html" , "_blank");
		})
		$(".box13 li").eq(4).click(function(){
			window.open(".html" , "_blank");
		})
		$(".box13 li").eq(2).click(function(){
			window.open(".html" , "_blank");
		})
		$(".box1 li").eq(0).click(function(){
			window.open("index.html" , "_self");
		})
		$(".box3>a").click(function(){
			window.open("index.html" , "_self");
		})
		$(".box3 #fw").click(function(){
			window.open(".html"  , "_blank");
		})
		$(".a6 li").eq(1).click(function(){
			window.open(".html", "_blank");
		})
		$(".a6 li").eq(2).click(function(){
			window.open(".html", "_blank");
		})
		$(".a6 li").eq(3).click(function(){
			window.open(".html" , "_blank");
		})
		$(".a6 li").eq(4).click(function(){
			window.open(".html" , "_blank");
		})
		$(".dj a").click(function(){
			window.open(".html" , "_blank");
		})
	}
	$(".box2 li:last a:last").click(function(){
		window.open("index.html" , "_self");
	})
	$(".box3>ul>li").mouseenter(function(){
		var i=$(this).index();
		$(".childen").eq(i).css("display","block");
	})
	$(".box3>ul>li").mouseleave(function(){
		var i=$(this).index();
		$(".childen").eq(i).css("display","none");;

	})
	$(".box4 input").focus(function(){
		$(".box4").css("borderColor","#ff6767")
		$(".box4 span").css("borderLeftColor","#ff6767")
		$(".box4 .a7").css("display","block")
	})
	$(".box4 input").blur(function(){
		$(".box4").css("borderColor","#e0e0e0")
		$(".box4 span").css("borderLeftColor","#e0e0e0")
		$(".box4 .a7").css("display","none")
	})
	var arr=["","","","",""];
	setInterval(function(){
		$(".box4 input").prop("placeholder",arr[i])
		i++;
		if(i==arr.length){
			i=0;
		}
	},2000)

	// 轮播图开始
	$.each($(".a4 li"),function(i,ele){
		var li=$('<li></li>');
		$(".a5").append(li);
	})
	$(".a5 li:first").addClass("bj");
	$(".a5 li:last").remove();
	$(".a5 li").click(function(){
		var i=$(this).index()*1225;
		$(this).addClass("bj").siblings().removeClass("bj");
		$(".a4").animate({
			marginLeft: -i+'px',
		})
		num=$(this).index();
	})
	$(".box7").click(function(){
		if(flag){
			flag=false;
			if(num==($(".a4 li").length-1)){
				$(".a4").css("marginLeft",0);
				num=0;
			}
			num++;
			$(".a4").animate({
				marginLeft: -(num*1225)+'px',
			},function(){
				flag=true;
			})
			if(num==($(".a4 li").length-1)){
				$(".a5 li").eq(0).addClass("bj").siblings().removeClass("bj");
			}else{
				$(".a5 li").eq(num).addClass("bj").siblings().removeClass("bj");
			}
		}
	})

	$(".box6").click(function(){
		if(flag){
			flag=false;
			if(num==0){
				$(".a4").css("marginLeft",-6125+'px')
				num=$(".a4 li").length-1;
			}
			num--;
			$(".a4").animate({
				marginLeft: -(num*1225)+'px',
			},function(){
				flag=true;
			})
			$(".a5 li").eq(num).addClass("bj").siblings().removeClass("bj");
		}
	})
	$(".box5 .a4").mouseenter(function(){
		clearInterval(timer);
	})
	$(".box5 .a4").mouseleave(function(){
		timer=setInterval(function(){
			$(".box7").click();
		},3000)
	})
	timer=setInterval(function(){
		$(".box7").click();
	},3000)
	// 轮播图结束

	if($(document).scrollTop()>=100){
		$(".box13 li:last").stop().fadeIn()
	}
	$(document).scroll(function(){
		console.log($("body").scrollTop())
		if($(document).scrollTop()>=100){
			$(".box13 li:last").stop().fadeIn()
		}else{
			$(".box13 li:last").stop().fadeOut()
		}
	})
	$(".box13 li:last").click(function(){
		$("html,body").animate({
			scrollTop:0
		},1000)
	})
	$(".box13 li:first").mouseenter(function(){
		$(".box13 li:first .box14").stop().fadeIn()
	})
	$(".box13 li:first").mouseleave(function(){
		$(".box13 li:first .box14").stop().fadeOut()
	})
	$(".box13 li:eq(4)").click(function(){
		window.open("购物车.html")
	})
	function countDown(){
		var nowTime=+new Date();
		var inputTime=+new Date('2022-2-25');
		var times=(inputTime-nowTime)/1000;
		var d=parseInt(times/60/60/24);
		d=d<10? '0'+d : d;
		var h=parseInt(times/60/60%24);
		h=h<10? '0'+h : h;
		var m=parseInt(times/60%60);
		m=m<10? '0'+m : m;
		var s=parseInt(times%60);
		s=s<10? '0'+s : s;
		$("#ms span").eq(0).text(d)
		$("#ms span").eq(1).text(h)
		$("#ms span").eq(2).text(m)
		$("#ms span").eq(3).text(s)
	}
	countDown()
	setInterval(function(){
		countDown();
	},1000)
	$(".box1 li:eq(10)").mouseenter(function(){
		$(".box1 li:eq(10) .div1").stop().slideDown();
	})
	$(".box1 li:eq(10)").mouseleave(function(){
		$(".box1 li:eq(10) .div1").stop().slideUp();
	})
})
