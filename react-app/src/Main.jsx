/* global Plotly:true */

import 'rc-calendar/assets/index.css'
import './style.css'
import moment from 'moment'
import React from 'react'
import Calendar from 'rc-calendar'
import createPlotlyComponent from 'react-plotly.js/factory'

const Plot = createPlotlyComponent(Plotly);

export default class Main extends React.Component {

  constructor(props) {
    super(props);

    const results = require('./readings.json')

    const dateUniq = results.map(el => {
        let myDate = new Date(el.createdAt.$date)
        return(new Date(myDate.getFullYear(), myDate.getMonth(), myDate.getDate(), 0, 0, 0, 0).valueOf())
      }).filter(function(item, i, ar){ return ar.indexOf(item) === i; })

    const lastValue = moment(dateUniq.sort()[dateUniq.length - 1].valueOf());

    this.state = {
      disabled: false,
      value: lastValue,
      results: results,
      data: results.map((el) => {
        return {
          date: new Date(el.createdAt.$date),
          temp: el.temperature,
          humd: el.humidity
        }
      }),
      dateUnique: dateUniq
    };
  }

  disabledDate(current) {
    if (!current) {
      // allow empty select
      return false;
    }
    let date = current;
    date.hour(0);
    date.minute(0);
    date.second(0);
    date.millisecond(0)
    return this.state.dateUnique.indexOf(date.valueOf()) === -1;  // can not select days before today
  }

  plotData() {
    const startDate = moment(this.state.value.valueOf())
    let endDate = moment(this.state.value.valueOf())
    endDate = endDate.add(1, 'days')

    return this.state.data.filter(el => el.date >= startDate.valueOf() && el.date <= endDate.valueOf())
  }

  onSelect(value) {
    this.setState({
      value: value
    })
  }

  render() {
    let data = this.plotData()
    let x = data.map(el => el.date)
    let yT = data.map(el => el.temp)
    let yH = data.map(el => el.humd)

    const minT = Math.floor(Math.min.apply(null, yT)) - 2
    const minH = Math.floor(Math.min.apply(null, yH)) - 2

    const maxT = Math.ceil(Math.max.apply(null, yT)) + 2
    const maxH = Math.ceil(Math.max.apply(null, yH)) + 2


    const dataP = [{
      type: 'scatter',
      mode: 'markers',
      x: x,
      y: yT,
      name: 'Temperature',
      marker: {size: 2},
    },
    {
      type: 'scatter',
      mode: 'markers',
      x: x,
      y: yH,
      name: 'Humidity',
      yaxis: 'y2',
      marker: {size: 2},
    }
  ]

    const layoutP = {
      // width: 'auto',
      // height: 500,
      title: 'Temperature & Humidity',
      yaxis: {
        title: 'Temperature',
        range: [minT, maxT],
      },
      yaxis2: {
        title: 'Humidity',
        titlefont: {color: 'rgb(148, 103, 189)'},
        tickfont: {color: 'rgb(148, 103, 189)'},
        overlaying: 'y',
        side: 'right',
        range: [minH, maxH],
      }
    }

    return (
      <main>
        <div className='container'>
          <div className='header'>
            <h1>Plot for sensor data</h1>
          </div>
          <div className='calendar'>
            <h3>Please select a date to see plot</h3>
            <Calendar
              dateInputPlaceholder="please input"
              formatter={'YYYY-MM-DD'}
              showDateInput={true}
              disabledDate={this.disabledDate.bind(this)}
              onSelect={this.onSelect.bind(this)}
              defaultValue={this.state.value}
            />
          </div>
          <div className='plot'>
            <Plot
              data={dataP}
              layout={layoutP}
            />
          </div>
          {/* <div className='plot-humd'>
            <Plot
              data={[]}

              layout={{
                width: 'auto',
                height: 500,
                title: 'Humidity'
              }}
            />
          </div> */}
        </div>
      </main>
    )
  }
}
