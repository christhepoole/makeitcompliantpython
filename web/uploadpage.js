let state = {
    fileArray: [],
    comparePercentage: [],
};

eel.expose(doUpload)
function doUpload(event) {
    //get file from input
    let file = document.getElementById("file").files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (event) {
        //read text file into JS object
            let textFile = {
                name: file.name,
                data: event.target.result,
            };

            state.fileArray = [...state.fileArray, textFile]

            document.getElementById("uploadedFile").innerHTML = state.fileArray.map((file) => {
                return `${file.name}`
            });
        };

        reader.readAsText(file);
    }
}

eel.expose(classifyJS)
async function classifyJS() {
    let res = await eel.classify(state.fileArray[0])();

    document.getElementById("comparisonResults").innerHTML = res.map((value) => {
        return `${value.name} <br> ${value.value}`
    });    
}

async function compareJS() {
    let res = await eel.compare(state.fileArray)();
        document.getElementById("comparisonResults").innerHTML
            = res.map((value) => {return `${value.name} <br> ${value.value}`});
}

