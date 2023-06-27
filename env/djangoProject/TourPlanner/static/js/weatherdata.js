const showData = () => {
    let data = sessionStorage.getItem('weatherInfo');
    data = JSON.parse(data);
    // console.log(data);
    const city = sessionStorage.getItem('name');
    // let infos = {};
    // let temp2 = '';
    // let temparature = [];
    // let date = [];
    // let lastKey = '';
    // let index = 0;

    // var size = Object.keys(data.list).length;
    // var keys = Object.keys(data.list);
    // console.log(data.list);

    const temperature = [];
    const dateTime = [];


    document.getElementById("location").innerText = `${city} (${data.city['name']})`;

    let htmlData = "";

    data.list.forEach(element => {
        const imageLink = `https://openweathermap.org/img/wn/${element.weather[0].icon}@2x.png`;
        const temp = parseFloat(element.main.temp) - 273.15;
        const feels = parseFloat(element.main.feels_like) - 273.15;

        // const parts = element.dt_txt.split(" ");
        // temp2 = parts[0];

        // if (index != 0) {
        //     let lastIndex = index-1;
        //     if (data.list[lastIndex+''].dt_txt == element.dt_txt) {
        //         temparature.push(temp.toFixed(2));
        //         date.push(temp2);
        //         lastKey = temp2;
        //     }
        //     else {
        //         if (infos[lastKey] == undefined) {
        //             const dateKey = 'date-' + lastKey;
        //             const temparatureKey = 'temp-' + lastKey;
        //             let demoObject = { dateKey: date, temparatureKey: temparature };
        //             infos[lastKey] = demoObject;

        //             delete demoObject[dateKey];
        //             delete demoObject[temparatureKey];
        //             temparature = [];
        //             date = [];
        //         }
        //     }
        // }

        temperature.push(temp.toFixed(2));
        dateTime.push(element.dt_txt);
        htmlData += `
        <div class="weatherCard">
            <p class="DateTime">${element.dt_txt}</p>
            <img src="${imageLink}" alt="">
            <p class="fellMargin">${temp.toFixed(2)}°C, Feels Like ${feels.toFixed(2)}°C</p>
            <h6 class="miniMarginTop">${element.weather[0].main}</h6>
            <p class="miniMarginTop">${element.weather[0].description}</p> 
            <p class="humidityMagin">Wind ${element.wind.speed}KM/h, Humidity ${element.main.humidity}%</p> 
        </div>
        `;
    });

    document.getElementById("fullDiv").innerHTML = '';
    document.getElementById("fullDiv").innerHTML = htmlData;

    console.log(temperature);
    console.log(dateTime);

    // drawChart(temperature, dateTime);
}

showData();

const drawChart = (data2, label) => {
    console.log(data2);
    console.log(label);
    const ctx = document.getElementById('myChart');
            const xx = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'];
            const yy = [12, 19, 3, 5, 2, 3];

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: xx,
                    datasets: [{
                        label: '# of Votes',
                        data: yy,
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
}

document.getElementById("HomeBtn").addEventListener("click", function () {
    window.location = "../index.php";
});