var canvas;
var graphics;
var pixelSize;
window.onload = init;

function draw(){
    //makes the canvas go from -10 to 10 left to right and down to up
    graphics.save();
    applyWindowToViewportTransformation(-20, 20, -10, 10, true);

    graphics.beginPath();
    graphics.lineWidth = 1.5 * pixelSize;
    var leftx = 12;
    var rightx = 20;
    var pully = 6;
    var y = 0;
    for (let j = 0; j < 3; j++){
        if(j == 1){
            leftx = 4;
            rightx = 12
            pully = 3
            y = -3;
        }else if (j == 2){
            leftx = -4;
            rightx = 4;
            pully = 0;
            y = -6;
        }
        for (let i = 0; i < 6; i++){
            graphics.moveTo(leftx, -20);
            graphics.lineTo(leftx, y);
            graphics.bezierCurveTo(leftx, pully, rightx, pully, rightx, y);
            graphics.lineTo(rightx, -20);
            leftx = leftx + 0.5;
            rightx = rightx - 0.5;
            pully = pully - 0.75;
        }
    }
    graphics.stroke();
    graphics.restore();
    

}

function applyWindowToViewportTransformation(left,right,bottom,top,preserveAspect) {
    let displayAspect, windowAspect;
    let excess;
    let pixelwidth, pixelheight;
    if (preserveAspect) {
        // Adjust the limits to match the aspect ratio of the drawing area.
        displayAspect = Math.abs(canvas.height / canvas.width);
        windowAspect = Math.abs(( top-bottom ) / ( right-left ));
        if (displayAspect > windowAspect) {
            // Expand the viewport vertically.
            excess = (top-bottom) * (displayAspect/windowAspect - 1);
            top = top + excess/2;
            bottom = bottom - excess/2;
        }
        else if (displayAspect < windowAspect) {
            // Expand the viewport vertically.
            excess = (right-left) * (windowAspect/displayAspect - 1);
            right = right + excess/2;
            left = left - excess/2;
        }
    }
    graphics.scale( canvas.width / (right-left), canvas.height / (bottom-top) );
    graphics.translate( -left, -top );
    pixelwidth =  Math.abs(( right - left ) / canvas.width);
    pixelheight = Math.abs(( bottom - top ) / canvas.height);
    pixelSize = Math.max(pixelwidth,pixelheight);
}  // end of applyWindowToViewportTransformation()

function init(){
    try{
        canvas = document.getElementById("canvas1");
        graphics = canvas.getContext("2d");
    }catch(e) {
        //put something here to display when something goes wrong
    }
    draw();
}