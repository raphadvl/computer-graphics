
function setup(){
    createCanvas(600,600);
}  

function ponto(A){
    circle(A.x,A.y,5);
}

function BezierCubicaP0(t,p){
	var k = 1-t;
	return (k**3)*p;
}

function BezierCubicaP1(t,p){
	var k = 1-t;
	return 3*(k**2)*t*p;
}

function BezierCubicaP2(t,p){
    var k = 1-t;
	return 3*(k)*(t**2)*p;
}

function BezierCubicaP3(t,p){
	return (t**3)*p;
}

function BezierCubica(t,p0,p1,p2,p3){
	return {
        x: BezierCubicaP0(t,p0.x) + 
        BezierCubicaP1(t,p1.x) + 
        BezierCubicaP2(t,p2.x) + 
        BezierCubicaP3(t,p3.x),

        y: BezierCubicaP0(t,p0.y) + 
        BezierCubicaP1(t,p1.y) + 
        BezierCubicaP2(t,p2.y) + 
        BezierCubicaP3(t,p3.y)
    }
}

function draw(){
    let p0, p1, p2, p3;

    background(200);

    p0 = {x:10,y:3*height/5};
    p1 = {x:width-10,y:height/2};
    p2 = {x:mouseX,y:mouseY};
    p3 = {x:width-10,y:height*0.2};

    ponto(p0);
    ponto(p1);
    ponto(p2);
    ponto(p3);
 
    noFill();
    beginShape();

    for(let t=0; t<=1; t+=0.01)
    {
        A = BezierCubica(t,p0,p1,p2,p3);        
        vertex(A.x, A.y);
    }

    endShape();
}
