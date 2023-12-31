const placeInfoSearch = async () => {
    const searchString = document.getElementById("searchPlaceId").value;
    if (searchString === "") return;

    const APIkey = "775f29948015fe62bf670848aca552ca";
    const limit = 1;
    const url = `http://api.openweathermap.org/geo/1.0/direct?q=${searchString}&limit=${limit}&appid=${APIkey}`;

    try {
        const res = await fetch(url);
        const data = await res.json();

        if (data.length > 0) {
            if (data[0].country === "BD") {
                document.getElementById("searchPlaceId").value = "";
                loadData(data[0].name, data[0].lat, data[0].lon);
            }
            else {
                console.log("Bideshi");
                document.getElementById("locationError").innerText = "Please Enter a city name of Bangladesh";
                document.getElementById("locationError").style.visibility = "visible";
            }
        }
        else {
            // invalid city name
            console.log("invalid");
            document.getElementById("locationError").innerText = "Invalid City Name";
            document.getElementById("locationError").style.visibility = "visible";
        }
    }
    catch (error) {

    }

}

const loadData = async (name, lat, lon) => {
    const APIkey = "775f29948015fe62bf670848aca552ca";
    // const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${APIkey}`;
    const url = `http://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${APIkey}`;

    sessionStorage.setItem("name", name);
    try {
        const res = await fetch(url);
        const data = await res.json();

        // const temp = (data.main.temp - 273.15).toFixed(2);
        // const feels_like = (data.main.feels_like - 273.15).toFixed(2);
        // const weatherMain = data.weather[0].main;
        // const weatherDisc = data.weather[0].description;
        // const wind = data.wind.speed;


        // sessionStorage.setItem("temp", temp);
        // sessionStorage.setItem("feels_like", feels_like);
        // sessionStorage.setItem("weatherMain", weatherMain);
        // sessionStorage.setItem("weatherDisc", weatherDisc);
        // sessionStorage.setItem("wind", wind);

        sessionStorage.setItem("weatherInfo", JSON.stringify(data));

        // window.location = "pages/weatherInfo.html";
        // window.location.href = "{% url 'home' %}";
        // window.location.replace("{% url 'home' %}");
        window.location.href = weatherInfoUrl;

    }
    catch (error) {

    }
}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// console.log("home js connected");