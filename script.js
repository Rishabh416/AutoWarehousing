const supabaseUrl = 
const supabaseKey = 
const supabase = window.supabase.createClient(supabaseUrl, supabaseKey)

const stage1container = document.getElementById("stage1")
const stage2container = document.getElementById("stage2")
const stage3container = document.getElementById("stage3")
const stage4container = document.getElementById("stage4")

async function getData1() {
    let { data: warehouse, error } = await supabase
        .from('warehouse')
        .select("*")
        .eq("stage", 1);

    if (error) {
        console.error("Error fetching data:", error);
        return null;
    }

    return warehouse;
}

getData1().then(data => {
    console.log(data)
    for (let i in data) {
        console.log(data[i].product)

        let newElement = document.createElement('p')
        newElement.textContent = data[i].product
        stage1container.appendChild(newElement)
    }
}).catch(error => {
    console.error("Error occurred:", error);
});

async function getData2() {
    let { data: warehouse, error } = await supabase
        .from('warehouse')
        .select("*")
        .eq("stage", 2);

    if (error) {
        console.error("Error fetching data:", error);
        return null;
    }

    return warehouse;
}

getData2().then(data => {
    console.log(data)
    for (let i in data) {
        console.log(data[i].product)

        let newElement = document.createElement('p')
        newElement.textContent = data[i].product
        stage2container.appendChild(newElement)
    }
}).catch(error => {
    console.error("Error occurred:", error);
});

async function getData3() {
    let { data: warehouse, error } = await supabase
        .from('warehouse')
        .select("*")
        .eq("stage", 3);

    if (error) {
        console.error("Error fetching data:", error);
        return null;
    }

    return warehouse;
}

getData3().then(data => {
    console.log(data)
    for (let i in data) {
        console.log(data[i].product)

        let newElement = document.createElement('p')
        newElement.textContent = data[i].product
        stage3container.appendChild(newElement)
    }
}).catch(error => {
    console.error("Error occurred:", error);
});


async function getData4() {
    let { data: warehouse, error } = await supabase
        .from('warehouse')
        .select("*")
        .eq("stage", 4);

    if (error) {
        console.error("Error fetching data:", error);
        return null;
    }

    return warehouse;
}

getData4().then(data => {
    console.log(data)
    for (let i in data) {
        console.log(data[i].product)

        let newElement = document.createElement('p')
        newElement.textContent = data[i].product
        stage4container.appendChild(newElement)
    }
}).catch(error => {
    console.error("Error occurred:", error);
});

