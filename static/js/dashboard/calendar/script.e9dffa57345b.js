document.addEventListener('DOMContentLoaded', function() {

  var ev;
    if(localStorage.getItem('ev')){
      ev = JSON.parse(localStorage.getItem('ev'));
    } else {
      ev = [
        {
          title: 'All Day Event',
          start: '2021-06-01'
        },
        {
          title: 'Long Event',
          start: '2021-06-07',
          end: '2021-06-10'
        },
        {
          groupId: 999,
          title: 'Repeating Event',
          start: '2021-06-09T16:00:00'
        },
        {
          groupId: 999,
          title: 'Repeating Event',
          start: '2021-06-16T16:00:00'
        },
        {
          title: 'Conference',
          start: '2021-06-11',
          end: '2021-06-13'
        },
        {
          title: 'Meeting',
          start: '2021-06-12T10:30:00',
          end: '2021-06-12T12:30:00'
        },
        {
          title: 'Lunch',
          start: '2021-06-12T12:00:00'
        },
        {
          title: 'Meeting',
          start: '2021-06-12T14:30:00'
        },
        {
          title: 'Happy Hour',
          start: '2021-06-12T17:30:00'
        },
        {
          title: 'Dinner',
          start: '2021-06-12T20:00:00'
        },
        {
          title: 'Birthday Party',
          start: '2021-06-13T07:00:00'
        },
        {
          title: 'Click for Google',
          url: 'http://google.com/',
          start: '2021-06-28'
        }
      ];
    }
    var calendarEl = document.getElementById('calendar');
    var calendarEl = document.getElementById('calendar');

    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

	today = yyyy + '-' + mm + '-' + dd;

    var calendar = new FullCalendar.Calendar(calendarEl, {
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
      },
      initialDate: today,
      navLinks: true, // can click day/week names to navigate views
      nowIndicator: true,

      weekNumbers: true,
      weekNumberCalculation: 'ISO',

      editable: true,
      selectable: true,
      dayMaxEvents: true, // allow "more" link when too many events
      events: ev
    });

    document.querySelector('#choose').addEventListener('submit', function(){
      event.preventDefault();
      ename = document.getElementById("name").value;
      estart = document.getElementById("start").value;
      eend = document.getElementById("end").value;
      calendar.addEvent({ // this object will be "parsed" into an Event Object
      title: ename, // a property!
      start: estart, // a property!
      end: eend // a property! ** see important note below about 'end' **
      });
      console.log(ev);
      localStorage.setItem('ev', JSON.stringify([{ // this object will be "parsed" into an Event Object
      title: ename, // a property!
      start: estart, // a property!
      end: eend // a property! ** see important note below about 'end' **
      },...ev]));
      document.getElementById("name").value = "";
      document.getElementById("start").value = "";
      document.getElementById("end").value = "";
  });

  calendar.render();
});