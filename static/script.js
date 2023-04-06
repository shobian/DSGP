
function addData(){
  var randdspend = document.getElementById("randdspend").value;
  var administration = document.getElementById("administration").value;
  var marketingspend = document.getElementById("marketingspend").value;
  var totalfunding = document.getElementById("totalfunding").value;
  var fundingrounds = document.getElementById("fundingrounds").value;
  var fundingduration = document.getElementById("fundingduration").value;
  var category = document.getElementById("category").value;
  var countrycode = document.getElementById("countrycode").value;

  var table = document.getElementById("data-table").getElementsByTagName("tbody")[0];

  var row = table.insertRow(table.length);


  var cell1 = row.insertCell(0);
  var cell2 =  row.insertCell(1);
  var cell3 =  row.insertCell(2);
  var cell4 =  row.insertCell(3);
  var cell5 =  row.insertCell(4);
  var cell6 =  row.insertCell(5);
  var cell7 =  row.insertCell(6);
  var cell8 =  row.insertCell(7);

  cell1.innerHTML = randdspend;
  cell2.innerHTML = administration;
  cell3.innerHTML = marketingspend;
  cell4.innerHTML = totalfunding;
  cell5.innerHTML = fundingrounds;
  cell6.innerHTML = fundingduration;
  cell7.innerHTML = category;
  cell8.innerHTML = countrycode;


    // Clear form inputs
  document.getElementById("randdspend").value = "";
  document.getElementById("administration").value = "";
  document.getElementById("marketingspend").value = "";
  document.getElementById("totalfunding").value = "";
  document.getElementById("fundingrounds").value = "";
  document.getElementById("fundingduration").value = "";
  document.getElementById("category").value = "";
  document.getElementById("countrycode").value = "";


  // Prevent form from submitting and refreshing the page





  return false;




}

