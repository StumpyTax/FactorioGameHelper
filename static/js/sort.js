const table=document.querySelectorAll('table');

let colIndex=-1;

const sortTable=function(index,type,isSorted)
{
	const tbody=table[0].querySelector('tbody');

	const compare=function(rowA,rowB){
		const rowAData=rowA.cells[index>0?index+1:index].innerHTML;
		const rowBData=rowB.cells[index>0?index+1:index].innerHTML;

		switch(type){
			case "int":
					return rowAData-rowBData;
			case "string":
					if(rowAData>rowBData)
						return 1;
					else if(rowAData==rowBData)
						return 0;
					return -1;
		}
	}
	let rows=[].slice.call(tbody.rows);

	rows.sort(compare);

	if(isSorted) rows.reverse();

	console.log(rows[0]);
	console.log(rows[rows.length-1]);
	table[0].removeChild(tbody);

	for(let i=0;i<rows.length;i++){
		tbody.appendChild(rows[i]);
	}

	table[0].appendChild(tbody);
}

table[0].addEventListener('click',e=>{
	
	const el=e.target;
	if(el.nodeName!="TH") return;

	const index=el.cellIndex;
	const type=el.getAttribute('data-type')

	sortTable(index,type,colIndex==index);
	
	if(colIndex==index) colIndex=-1;
	else colIndex=index;
});