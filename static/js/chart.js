var module = angular.module('myApp',[]);

function Main($scope,$http, $compile){

  $http.get("/chart/").then( function(response) {
       $scope.data = response.data;

var options5 = {
  series: [{
    name: 'Total Orders Value',
    type: 'column',
    data: $scope.data.y1
  }, {
    name: 'Received Payments',
    type: 'column',
    data: $scope.data.y2
  }, {
    name: 'Panding Payments',
    type: 'column',
    data: $scope.data.y3 
  }, {
    name: 'Panding Work Payments',
    type: 'column',
    data: $scope.data.y4 
  }],
  chart: {
    height: 350,
    //type: 'line',
    stacked: false,
    toolbar: {
      show: true,
    }
  },
  grid: {
    show: false,
    padding: {
      left: 30,
      right: 30
    }
  },
  stroke: {
    width: [0, 2, 3, 3],
    curve: 'smooth'
  },
  plotOptions: {
    bar: {
      columnWidth: '70%',
      endingShape: 'rounded',

    }
  },

  fill: {
    opacity: [1, 1, 1, 1],
    gradient: {
      inverseColors: false,
      shade: 'light',
      type: "vertical",
      opacityFrom: 0.85,
      opacityTo: 0.55,
      stops: [0, 100, 100, 100, 100]
    }
  },
  labels: $scope.data.xaxis,
  markers: {
    size: 0
  },
  xaxis: {
    
    // title: {
    //   text: 'Customer Name',
    //   offsetY: 10,
    // },
    // labels: {
    //   rotate: -90,
    //   rotateAlways: true,},

    // min: 1,
    // max: 74
  },
  yaxis: {
    // title: {
    //   text: 'Points',
    // },
    min: 0,
    //max: 20000
  },
  legend: {
    position: 'top',
    horizontalAlign: 'left',
    fontFamily: 'ubuntu-medium',
    fontSize: '13px',
  },
  tooltip: {
    shared: true,
    intersect: false,
    y: {
      formatter: function (y) {
        if (typeof y !== "undefined") {
          return  y.toFixed(0);
        }
        return y;

      }
    }
  }
};
var chart = new ApexCharts(document.querySelector("#chart5"), options5);
chart.render();

  })
}

module.controller("MainCtrl",Main); 
