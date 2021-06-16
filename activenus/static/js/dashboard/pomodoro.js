const pomo = new Vue({
  el: '#pomodoro-module',
  data: {
    totalTime: (25 * 60),
    minimum: 1,
    maximum: 90,
    timerRunning: false,
    timerPaused: false,
    timeFocused: 0,
    interval: null,
    shortBreak: 5,
    longBreak: 15,
    isFocused: true,
    isShortBreak: false,
    isLongBreak: false
  },

  mounted() {
  if (localStorage.getItem('timeFocused')) {
    try {
    this.timeFocused = localStorage.getItem('timeFocused');
    } catch(e) {
    localStorage.removeItem('timeFocused');
    }
  } 		
  },

  computed: {
     time: function() {
      return this.minutes + " : " + this.seconds;
    },
    minutes: function() {
      var min = Math.floor(this.totalTime / 60);
      return min >= 10 ? min : '0' + min;
    },
    seconds: function() {
      var sec = this.totalTime - (this.minutes * 60);
      return sec >= 10 ? sec : '0' + sec;
    }
  },
  methods: {
    timerRun() {
      this.timerRunning = true;
      this.interval = setInterval(this.countdownTimer, 1000);
      console.log(this.totalTime);
    },
    timerPause() {
      this.timerRunning = false;
      clearInterval(this.interval);
    },
    timerReset() {
      this.isFocused = true;
      this.isShortBreak = false;
      this.isLongBreak = false;
      this.timerRunning = false;
      clearInterval( () => { this.interval; });
      this.totalTime = (25 * 60);
    },

    timerShortBreak(){
      this.isFocused = false;
      this.isShortBreak = true;
      this.isLongBreak = false;
      this.timerRunning = false;
      clearInterval( () => { this.interval; });
      this.totalTime = (this.shortBreak * 60);
    },

    timerLongBreak(){
      this.isFocused = false;
      this.isShortBreak = false;
      this.isLongBreak = true;
      this.timerRunning = false;
      clearInterval( () => { this.interval; });
      this.totalTime = (this.longBreak * 60);
    },

    timeDecrease(){
      // if(this.totalTime < 60*this.minimum){
      //     this.totalTime -= 60;
      // }
      if(this.totalTime > 60*this.minimum){
          this.totalTime -= 60;
      }
      
    },

    timeIncrease(){
      // if(this.totalTime > 60*this.maximum){
      //     this.totalTime += 60;
      // }
      if(this.totalTime < 60*this.maximum) {
          this.totalTime += 60;
      }
      },
    timerCountdown() {
      console.log('Working');
      this.timerRunning = true;
      this.interval = setInterval(this.updateCurrentTime, 1000);
      // Counts down from 60 seconds times 1000.
      setInterval( () => {
        this.timerMinutes--
      }, 60 * 1000)
      
      // Check if seconds at double zero and then make it a 59 to countdown from.
      // need another method of checking the number while in the loop and then adding a zero on the number under 10
      if(this.timerSeconds === '00'){
        this.timerSeconds = 59;
        setInterval( () => {
          this.timerSeconds--
        }, 1000);
      } else {
        setInterval( () => {
          this.timerSeconds--
        }, 1000);
      }
    },
    countdownTimer() {
      if(this.totalTime <= 0){
          alert("Time's up!");
          if(this.isFocused){
              this.timerShortBreak();
          } else {
              this.timerReset();
          }
      } else {
          if (this.timerRunning == true) {
          this.totalTime--;
          if(this.isFocused){
              this.timeFocused = localStorage.getItem('timeFocused');
              this.timeFocused++;
              localStorage.setItem('timeFocused', this.timeFocused);
          }
      }
      }
      
    }
  }
})

const vm = pomo.mount('#pomodoro-module');
console.log(vm.totalTime); // => 4