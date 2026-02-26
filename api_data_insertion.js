async function get_dt(){
    const res=await fetch("https://classmonitor.aucseapp.in/get_date_time.php")
    if(!res.ok){
        console.log("Error fetching date and time")
    }
    const data=await res.json()
    return data
}