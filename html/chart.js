google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Rok');
    data.addColumn('number', 'Bilance');
    data.addColumn('number', 'Příjmy');
    data.addColumn('number', 'Výdaje');
    data.addRows({{ rozpocty.count }});
{% for rozpocet in rozpocty %}
    data.setValue({{ rozpocet.rok }} - 1993, 0, '{{ rozpocet.rok }}');
    data.setValue({{ rozpocet.rok }} - 1993, 1, {{ rozpocet.bilance }});
    data.setValue({{ rozpocet.rok }} - 1993, 2, {{ rozpocet.prijmy }});
    data.setValue({{ rozpocet.rok }} - 1993, 3, {{ rozpocet.vydaje }});
{% endfor %}

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, {width: 800, height: 400, colors: ['FF9900', '3300cc', 'cc0000']});
}
