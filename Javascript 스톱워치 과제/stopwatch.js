let seconds = 0;
let millisec = 0;
const $appendMillisec = document.querySelector("#milliseconds")
const $appendSeconds = document.querySelector("#seconds")
const $buttonStart = document.querySelector("#start--btn")
const $buttonStop = document.querySelector("#stop--btn")
const $buttonReset = document.querySelector("#reset--btn")
const $recordList = document.querySelector('#record--list')
let timeId;


// start버튼 클릭시
$buttonStart.addEventListener("click", function() {
  clearInterval(timeId)
  timeId = setInterval(operateTimer, 10)
})

// stop버튼 클릭시 
$buttonStop.addEventListener("click", function(){
  clearInterval(timeId)

  //record 기능
  console.log(seconds, millisec)
  let li = document.createElement('span')
  li.setAttribute("class", "record--text")
  let checkbox = document.createElement("input")
  checkbox.setAttribute("type", "checkbox")
  checkbox.setAttribute("class", "licheckbox")
  checkbox.setAttribute("name", "rowcheck")
  li.innerHTML = $appendSeconds.innerHTML + ':' + $appendMillisec.innerHTML
  
  let listitem = document.createElement('li')
  listitem.setAttribute("class", "li-item")
  listitem.append(checkbox, li)  
  $recordList.append(listitem)
})

// reset버튼 클릭시
$buttonReset.addEventListener("click", function() {
  clearInterval(timeId)
  millisec = 0; seconds = 0;
  $appendMillisec.textContent = "00"
  $appendSeconds.textContent = "00"
})


// 10ms 마다 1초 증가 계산 
function operateTimer(){
  millisec++;
  $appendMillisec.textContent = millisec > 9 ? millisec : '0' + millisec
  if(millisec > 99){
    seconds++;
    $appendSeconds.textContent = seconds > 9 ? seconds : '0' + seconds
    millisec = 0
    $appendMillisec.textContent = "00"
  }
}

//전체 선택 기능
function selectAll(selectAll){
  const $checkAll = document.querySelectorAll('input[type="checkbox"]');
  $checkAll.forEach((checkbox) => {
    checkbox.checked = selectAll.checked
  })
}

//부분, 전체 삭제 기능
var del = document.querySelector(".trash--btn");
del.onclick = () => {
  const resetbox = document.querySelector(".checkbox");
  var checkitem = document.querySelectorAll(".licheckbox");

  for(var i = 0; i < checkitem.length; i++){
    if(checkitem[i].checked){
      checkitem[i].parentElement.remove();
    }
    }
  resetbox.checked = false;
}

