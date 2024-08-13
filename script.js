const supabaseUrl = ""
const supabaseKey = ""
const supabase = window.supabase.createClient(supabaseUrl, supabaseKey)

const stage1container = document.getElementById("stage1")
const stage2container = document.getElementById("stage2")
const stage3container = document.getElementById("stage3")
const stage4container = document.getElementById("stage4")

let newElement = document.createElement('p')
newElement.textContent = "text for element"
stage1container.appendChild(newElement)

let {data: warehouse, error} = await supabase
    .from('warehouse')
    .select("*")
    .eq("stage",1)