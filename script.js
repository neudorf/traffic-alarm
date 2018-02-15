function update(){
    var now = new Date();
    var bedHour = parseInt($('#bedTimeInput').val().slice(0,2));
    var wakeHour = parseInt($('#wakeTimeInput').val().slice(0,2));
    var bedMin = parseInt($('#bedTimeInput').val().slice(3,5));
    var wakeMin = parseInt($('#wakeTimeInput').val().slice(3,5));
    console.log("bedHour: " + bedHour + "wakeHour: "+wakeHour+"bedMin: "+ bedMin + "wakeMin: "+wakeMin + '\n' + "now Hour: " + now.getHours() + "now Minute: "+now.getMinutes())
    if (bedHour > wakeHour){ //night time, sleeping overnight
            bed = !(((now.getHours() < bedHour) && (now.getHours() > wakeHour)) || (now.getHours()==bedHour && now.getMinutes() < bedMin) || (now.getHours()==wakeHour && now.getMinutes() >= wakeMin));
    }
    else if (bedHour < wakeHour){ //nap time, sleeping during the day
            bed = ((now.getHours() < wakeHour) && (now.getHours() > bedHour)) || (now.getHours()==bedHour && now.getMinutes() >= bedMin) || (now.getHours()==wakeHour && now.getMinutes() < wakeMin);
    }
    else if (bedHour == wakeHour){ //nap time, sleeping during the day
            bed = (now.getMinutes() >= bedMin && now.getMinutes() < wakeMin);
    }
    //console.log("now="+now+"bedTime="+bedTime+"wakeTime="+wakeTime)
    if(bed){
        document.getElementById("stoplight").src="javascript-web-app/stoplightRed.png";
        //console.log("Bedtime? True");
    }
    else{
        document.getElementById("stoplight").src="javascript-web-app/stoplightGreen.png";
        //console.log("Bedtime? False");
    }
};

$(document).ready(function(){
    jQuery('#bedTimeInput').datetimepicker({
      datepicker:false,
      format:'H:i',
      step:15
    });
    jQuery('#wakeTimeInput').datetimepicker({
      datepicker:false,
      format:'H:i',
      step:15
    });
    update();
    setInterval('update()',5000);
});
