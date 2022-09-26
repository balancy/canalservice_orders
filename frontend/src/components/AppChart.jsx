import React, { useEffect, useState } from "react";
import Chart from "react-apexcharts";

const AppChart = (props) => {
    const [options, setOptions] = useState({});
    const [series, setSeries] = useState([]);

    useEffect(() => {
        setOptions({
            chart: {
                id: "basic-bar"
            },
            xaxis: {
                categories: props.getColumnData(props.data, 'delivery_date')
            }
        })
        setSeries([
            {
                name: "price",
                data: props.getColumnData(props.data, 'rub_price')
            }
        ])
    }, [props])

    return (
        <div className="app">
            <div className="row">
                <div className="mixed-chart">
                    <Chart
                        options={options}
                        series={series}
                        type="line"
                        width="100%"
                    />
                </div>
            </div>
        </div>
    );
}

// class AppChart extends Component {
//     constructor(props) {
//         super(props);


//         this.state = {
//             options: {
//                 chart: {
//                     id: "basic-bar"
//                 },
//                 xaxis: {
//                     categories: props.getColumnData(props.data, 'delivery_date')
//                 }
//             },
//             series: [
//                 {
//                     name: "price",
//                     data: props.getColumnData(props.data, 'rub_price')
//                 }
//             ]
//         };
//     }

//     componentDidUpdate(prevProps) {
//         if (this.props.data !== prevProps.data) {
//             console.log('changed');
//         }
//     };

//     render() {
//         return (
//             <div className="app">
//                 <div className="row">
//                     <div className="mixed-chart">
//                         <Chart
//                             options={this.state.options}
//                             series={this.state.series}
//                             type="line"
//                             width="100%"
//                         />
//                     </div>
//                 </div>
//             </div>
//         );
//     }
// }

export default AppChart;