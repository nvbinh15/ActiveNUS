//JS code for progress
Vue.component('progres', {
  props: ['title', 'count', 'backgroundcolor', 'id'],
  template: `<div class='progress-card' :style="filterStyleCard">
      <div class="progress_title">{{ title }}</div>
      <div style='margin-top: 2rem' class="ui small indicating progress">
          <div :style="filterStyleProgress" class="bar"></div>
          <div class="label">Progress</div>
      </div>
      <span>{{ count }} %</span>
      <div class="ui icon buttons">
          <div class="decrement ui basic button icon"  @click="decrease"><i class="minus icon"></i></div>
          <div class="increment ui basic button icon"  @click="increase"><i class="plus icon"></i></div>
          <div class="ui basic button icon ui right dropdown simple item"><i class="edit outline icon"></i>
            <div class="menu">
              <div class="item" @click="removeProgress"><i class="trash icon"></i></div>
              <div class="item" @click="editTitle"><i class="pencil alternate icon"></i></div>
            </div>
          </div>

          <div class="ui basic button icon ui right dropdown simple item"><i class="tint icon"></i>
            <div class="menu">
              <div class="item" @click="backgroundRed">
              <i class="circle icon" style="color: #ff714f"></i></div>
              <div class="item" @click="backgroundBlue">
              <i class="circle icon" style="color: #91b3cf"></i></div>
              <div class="item" @click="backgroundYellow">
              <i class="circle icon" style="color: #fdba2e"></i></div>
              <div class="item" @click="backgroundCream">
              <i class="circle icon" style="color: #fef4d9"></i></div>
            </div>
        </div>
  </div></div>`,

  computed: {
    filterStyleProgress() {
      return {
        width: this.count.toString() + '%'
        // width: this.count + ""
      };
    },

    filterStyleCard() {
      return {
        float: 'left',
        width: '230px',
        height: '147px',
        margin: '20px',
        // margin: '2rem 0 2rem 2rem',
        padding: '1rem',
        background: this.backgroundcolor,
        boxShadow: 'rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px',
        borderRadius: '20px'
    }
  }


  },

  methods: {
    decrease: function () {
      if(this.count > 0){
      this.count -= 5;
      $.ajax({
        type: "GET",
        url: '/decreaseprogress',
        data: {'id': this.id},
        dataType: "json",
      });
      }
    },
    increase: function () {
      if(this.count < 100){
      this.count += 5;
      $.ajax({
        type: "GET",
        url: '/increaseprogress',
        data: {'id': this.id},
        dataType: "json",
      });
    }
    },

    backgroundRed: function() {
      this.backgroundcolor = "#ff714f";
      $.ajax({
        type: "GET",
        url: '/setred',
        data: {'id': this.id},
        dataType: "json",
      });
    },

    backgroundBlue: function() {
      this.backgroundcolor = "#91b3cf";
      $.ajax({
        type: "GET",
        url: '/setblue',
        data: {'id': this.id},
        dataType: "json",
      });
    },

    backgroundCream: function() {
      this.backgroundcolor = "#fef4d9";
      $.ajax({
        type: "GET",
        url: '/setcream',
        data: {'id': this.id},
        dataType: "json",
      });
    },

    backgroundYellow: function() {
      this.backgroundcolor = "#fdba2e";
      $.ajax({
        type: "GET",
        url: '/setyellow',
        data: {'id': this.id},
        dataType: "json",
      });
    },

    editTitle: function() {
      var title = prompt("Change progress title: ");
      if(title) {
        this.title = title;
        var id = this.id;
        $.ajax({
          type: "GET",
          url: '/renameprogress',
          data: {'id': id, 'title': title},
          dataType: "json",
        });
      }
    },

    removeProgress: function() {
      if (confirm("Are you sure you want to remove the progress?")) {
        var id = this.id;
        console.log(id);
        $.ajax({
          type: "GET",
          url: '/deleteprogress',
          data: {'id': id},
          dataType: "json",
        });
        window.location.reload();
      }
    }
  }
});


var app = new Vue({
  el: '#progress',
  delimiters : ['[[',']]'],
  data: {
    cards: progressBackend
  },
});
  