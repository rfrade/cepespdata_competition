/**
 * Realiza uma requisição ajax passando os parâmetros do form e utiliza os dados
 * do objeto json retornado do server para gerar os mapas.
 */
function ajax_mapa() {
	$.getJSON('/gerarMapa', null, function(json) {
		gerar_mapa(json)
	});
}

/**
 * Gera o mapa com o json e exibe na tela
 * 
 * @param data
 */
function gerar_mapa(json) {
	$.get('/static/mapas_ibge/brasil.html', function(html) {
		$('#area_mapa').html(html);
	});
}

function ajax_grafico() {
	var grafico = $('#select__tipo_grafico').val();
	var cargo = $('#job-input').val();
	var agregacaoRegional = $('#regionalAggregation-input').val();
	var agregacaoPolitica = $('#politicalAggregation-input').val();

	var requestJSON = {
		"grafico" : grafico,
		"cargo" : cargo,
		"ar" : agregacaoRegional,
		"ap" : agregacaoPolitica
	};

	var retorno = null;
	$.getJSON('/gerarGrafico', requestJSON, function(json) {
		gerar_grafico(json)
		retorno = json;
	});
	return retorno;
}

function gerar_grafico(json) {

	var lista = [];
	for (var i = 0; i < json.length; i++) {
		var linha = {
			x : json[i].eleicoes,
			y : json[i].votos_por_eleicao,
			mode : 'lines',
			name : json[i].partido
		};
		lista.push(linha);
	}

	var layout = {
		margin : {
			t: 20,
			l: 20,
			pad : 10
		},
		width : 600,
		height : 350,
		xaxis: {
			type : 'category'
		}
	};

	Plotly.newPlot(document.getElementById("area_grafico"), lista, layout);
}
