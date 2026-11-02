const items = [
 {name:'Field camera',available:4,description:'Weather-resistant camera kit'},
 {name:'Studio microphone',available:2,description:'USB microphone with stand'},
 {name:'Conference projector with extended installation kit',available:1,description:'HDMI projector and mounting kit'}
];
function render(list){document.querySelector('#rows').innerHTML=list.map((item,index)=>`<tr><td>${item.name}</td><td>${item.available}</td><td><button data-index="${index}">Details</button></td></tr>`).join('');}
document.querySelector('#filter').addEventListener('input',()=>render(items));
document.querySelector('#rows').addEventListener('click',event=>{if(event.target.matches('button')){const item=items[Number(event.target.dataset.index)];document.querySelector('#details').textContent=item.name+': '+item.description;}});
document.querySelector('#refresh').addEventListener('click',async()=>{document.querySelector('#status').textContent='Loading…';const response=await fetch('/api/items');render(await response.json());document.querySelector('#status').textContent='Updated';});
render(items);
