/**
 * Faz as requisições ajax, processa os mapas e gera os gráficos
 * 
 * Feito por rafael frade
 */
function exibir_tela_mapas() {
	 $('#area_conteudo').html("/tela_graficos.html");
}

/**
 * Realiza uma requisição ajax passando os parâmetros do form
 * e utiliza os dados do objeto json retornado do server
 * para gerar os mapas.
 */
function ajax_mapa() {
	$.getJSON('/gerarMapa', null, function (json) {gerar_mapa(json)});
}

/**
 * Gera o mapa com o json e exibe na tela
 * @param data
 */
function gerar_mapa(json) {
	$.get('/static/mapas_ibge/brasil.html', function (html) {
	    $('#page-content').html(html);
	});
}

function exibir_tela_graficos() {
	
}

function ajax_grafico() {
	$.getJSON('/gerarGrafico', null, function (json) {gerar_grafico(json)});
}

function gerar_grafico() {
	
}