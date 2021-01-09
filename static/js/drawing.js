var canvas = document.getElementById("draw");
var ctx = canvas.getContext("2d");
var xPrev=0, yPrev=0, xCurr=0, yCurr = 0;
var flag = false, dot_flat = false;
var stroke = 20;
var inputClassName =  document.getElementById("formClassName")
var inputProbability = document.getElementById("classProbability")

// Create Listener
canvas.addEventListener("mousemove", function(event){
    draw("move", event)
}, false);
canvas.addEventListener("mousedown", function(event){
    draw("down", event)
}, false);
canvas.addEventListener("mouseup", function(event){
    draw("up", event)
}, false);
canvas.addEventListener("mouseout", function(event){
    draw("out", event)
}, false);

function setCoordinates(event){
    xPrev = xCurr;
    yPrev = yCurr;
    // Current x, y 
    xCurr = event.clientX - canvas.getBoundingClientRect().left;
    yCurr = event.clientY - canvas.getBoundingClientRect().top;
}

function requestPrediction(){
    var urlParam = {
        param_data: canvas.toDataURL("image/jpeg")
    }

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({"image_data":urlParam.param_data});

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    fetch("http://localhost:5000/predict", requestOptions)
            .then(response => response.json())
            .then(result => {
                inputClassName.setAttribute("placeholder", result.class_name)
                inputProbability.setAttribute("placeholder", result.prob)
            })
            .catch(error => console.log('error', error));
}

var sw = true;
if (sw){
    setInterval(requestPrediction, 1000)
    sw = false;
}

function draw(movementType, event){
    switch (movementType){
        case "down":
            setCoordinates(event)
            flag = true, dot_flag = true;
            if (dot_flag){
                ctx.beginPath();
                ctx.fillStyle = "white";
                ctx.arc(xCurr, yCurr, stroke*0.5, 0, 2*Math.PI)
                ctx.fill()
                ctx.closePath()
                dot_flag = false;
            }
            break;
        case "up":
            flag = false;
            break;

        case "out":
            flag = false;
            break;

        case "move":
            if (flag){
                setCoordinates(event)
                ctx.beginPath();
                ctx.moveTo(xPrev, yPrev)
                ctx.lineTo(xCurr, yCurr)
                ctx.lineCap = "round";
                ctx.lineJoin = "round";
                ctx.strokeStyle = "white";
                ctx.lineWidth = stroke;
                ctx.stroke()
                ctx.fill()
                ctx.closePath()
            }
            break;
    }
}

function clearCanvas(){
    console.log("cleaning canvas")
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}