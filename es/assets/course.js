/* Enhancement only: the entire course remains readable without JavaScript. */
(function(){
'use strict';
if(!window.ARCKHÉ)return;
ARCKHÉ.init();
document.querySelectorAll('[data-ARCKHÉ-check]').forEach(function(el){ARCKHÉ.registerCheck(el.dataset.ARCKHÉCheck,JSON.parse(el.dataset.checkDefinition))});
// Persist the worksheet inside the course export, using the public import API.
var form=document.getElementById('worksheet');
if(form){var state=JSON.parse(ARCKHÉ.exportJSON());Object.entries(state.worksheet||{}).forEach(function(p){if(form.elements.namedItem(p[0]))form.elements.namedItem(p[0]).value=p[1]});form.addEventListener('submit',function(ev){ev.preventDefault();var worksheet=Object.fromEntries(new FormData(form));var payload={schemaVersion:state.schemaVersion,courseId:'jev-curso-es',worksheet:worksheet};var result=ARCKHÉ.importJSON(JSON.stringify(payload));document.getElementById('saved').textContent=result.ok?"Hoja de trabajo guardada en esta sesión. Exporta Mi recorrido para conservar una copia.":"No se pudo guardar."})}
var calculate=document.getElementById('calculate');if(calculate)calculate.onclick=function(){var a=Number(document.getElementById('wr').value),b=Number(document.getElementById('wu').value);document.getElementById('composite').textContent=Number.isFinite(a)&&Number.isFinite(b)&&a>0&&b>0&&a<=100&&b<=100?((.75*a+.5*b)/(a+b)).toLocaleString('es',{minimumFractionDigits:4,maximumFractionDigits:4}):"Usa pesos positivos de hasta 100."};
document.querySelectorAll('[data-preview]').forEach(function(button){button.onclick=function(){var d=document.createElement('dialog'),close=document.createElement('button'),frame=document.createElement('iframe');close.textContent="Cerrar vista previa";frame.title="Vista previa del módulo";frame.src=button.dataset.preview;d.append(close,frame);document.body.append(d);d.showModal();close.focus();close.onclick=function(){d.close()};d.addEventListener('close',function(){d.remove();button.focus()})}});
})();
