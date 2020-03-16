setInterval(()=>
	(
		$(".form-control")[0].value=new Array(25).fill(1).map((v)=>(String.fromCharCode(Math.random(1)*150))).join(""),
		$(".form-control")[1].value=new Array(25).fill(1).map((v)=>(String.fromCharCode(Math.random(1)*150))).join(""),
		document.querySelector("#app > div > div > form > div:nth-child(3) > button:nth-child(1)").click()
	), 
	0
)
