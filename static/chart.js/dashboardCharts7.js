if ($("#traffic-chart").length) {
      var gradientStrokeBlue = ctx.createLinearGradient(0, 0, 0, 181);
      gradientStrokeBlue.addColorStop(0, 'rgba(54, 215, 232, 1)');
      gradientStrokeBlue.addColorStop(1, 'rgba(177, 148, 250, 1)');
      var gradientLegendBlue = 'linear-gradient(to right, rgba(54, 215, 232, 1), rgba(177, 148, 250, 1))';

      var gradientStrokeRed = ctx.createLinearGradient(0, 0, 0, 50);
      gradientStrokeRed.addColorStop(0, 'rgba(238, 8, 70, 1)');
      gradientStrokeRed.addColorStop(1, 'rgba(238, 8, 70, 1)');
      var gradientLegendRed = 'linear-gradient(to right, rgba(238, 8, 70, 1), rgba(238, 8, 70, 1))';

      var gradientStrokeGreen = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStrokeGreen.addColorStop(0, 'rgba(6, 185, 157, 1)');
      gradientStrokeGreen.addColorStop(1, 'rgba(132, 217, 210, 1)');
      var gradientLegendGreen = 'linear-gradient(to right, rgba(6, 185, 157, 1), rgba(132, 217, 210, 1))';   

      var gradientStrokeYellow = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStrokeYellow.addColorStop(0, 'rgba(255, 234, 97, 1)');
      gradientStrokeYellow.addColorStop(1, 'rgba(255, 241, 146, 1)');
      var gradientLegendYellow = 'linear-gradient(to right, rgba(255, 234, 97, 1), rgba(255, 241, 146, 1))';   

      var trafficChartData = {
        datasets: [{
          data: [24, 37, 11, 19],
          backgroundColor: [
            gradientStrokeBlue,
            gradientStrokeGreen,
            gradientStrokeRed,
            gradientStrokeYellow
          ],
          hoverBackgroundColor: [
            gradientStrokeBlue,
            gradientStrokeGreen,
            gradientStrokeRed,
            gradientStrokeYellow
          ],
          borderColor: [
            gradientStrokeBlue,
            gradientStrokeGreen,
            gradientStrokeRed,
            gradientStrokeYellow
          ],
          legendColor: [
            gradientLegendBlue,
            gradientLegendGreen,
            gradientLegendRed,
            gradientLegendYellow
          ]
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: [
          'All Works Completed Sites',
          'Work in Progress Sites',
          'Not Yet Started',
          'NOC and Clearance Issues'
        ]
      };
      var trafficChartOptions = {
        responsive: true,
        animation: {
          animateScale: true,
          animateRotate: true
        },
        legend: false,
        legendCallback: function(chart) {
          var text = []; 
          text.push('<ul>'); 
          for (var i = 0; i < trafficChartData.datasets[0].data.length; i++) { 
              text.push('<li><span class="legend-dots" style="background:' + 
              trafficChartData.datasets[0].legendColor[i] + 
                          '"></span>'); 
              if (trafficChartData.labels[i]) { 
                  text.push(trafficChartData.labels[i]); 
              }
              //text.push('<span class="float-right">'+trafficChartData.datasets[0].data[i]+"%"+'</span>')
              text.push('<span class="float-right">'+trafficChartData.datasets[0].data[i]+" Nos"+'</span>')
              text.push('</li>'); 
          } 
          text.push('</ul>'); 
          return text.join('');
        }
      };
      var trafficChartCanvas = $("#traffic-chart").get(0).getContext("2d");
      var trafficChart = new Chart(trafficChartCanvas, {
        type: 'doughnut',
        data: trafficChartData,
        options: trafficChartOptions
      });
      $("#traffic-chart-legend").html(trafficChart.generateLegend());      
    }