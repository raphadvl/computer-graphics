const r1 = 150;
const r2 = 50;
let n = 4;

function setup() {
    createCanvas(800, 600);
}

function draw() {
    background(300);
    translate(width / 2, height / 2);

    let c = color(255, 204, 0);
    let [mx, my] = relativeMouse();
    let v = createVector(1, 0)
    let u = createVector(mx, my);

    fill(c);

    rotate(v.angleBetween(u))

    n = floor(map(u.mag(), 0, width/2, 4, 20));

    beginShape();

    for (let i = 0; i < (2 * n); i++) {
        let angle = map(i, 0,2*n, 0, TWO_PI);

        if (i % 2 === 0){
            vertex(r1*cos(angle), r1*sin(angle));
        } 
        else { 
            vertex(r2*cos(angle), r2*sin(angle));
        }
    }

    endShape(CLOSE);
}

function relativeMouse() {
    let mx = mouseX;
    let my = mouseY;

    let matrix = drawingContext.getTransform()

    let pd = pixelDensity()
    let rp = matrix.inverse().transformPoint(new DOMPoint(mx * pd, my * pd));

    return [rp.x, rp.y];
}