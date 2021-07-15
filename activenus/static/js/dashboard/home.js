Vue.component('togglebutton', {
  props: ['label', 'name'],
  template: `<div class="togglebutton-wrapper" v-bind:class="isactive ? 'togglebutton-checked' : ''">
      <label v-bind:for="name">
        <span class="togglebutton-label">{{ label }}</span>
        <span class="tooglebutton-box"></span>
      </label>
      <input v-bind:id="name" type="checkbox" v-bind:name="name" v-model="isactive" v-on:change="onToogle">
  </div>`,
  model: {
    prop: 'checked',
    event: 'change'
  },
  data: function() {
    return {
      isactive:false
    }
  },
  methods: {
    onToogle: function() {
       this.$emit('clicked', this.isactive)
    }
  }
});

var todoBackend = JSON.parse("{{todolist|escapejs}}");
// var todoBackend = '{{ todolist|safe }}';
console.log(todoBackend);

var todolist = new Vue({
  el: '#todolist',
  delimiters : ['[[',']]'],
  data: {
    newitem:'',
    sortByStatus:false,
    // todo: [
    //   // { id:1, label: "Learn VueJs", done: true },
    //   // { id:2, label: "Code a todo list", done: false },
    //   // { id:3, label: "Learn something else", done: false }
    // ]
    todo: [],
  },
  methods: {
    addItem: function() {
      this.todo.push({id: Math.floor(Math.random() * 9999) + 10, label: this.newitem, done: false});
      this.newitem = '';
    },
    markAsDoneOrUndone: function(item) {
      item.done = !item.done;
    },
    deleteItemFromList: function(item) {
      let index = this.todo.indexOf(item)
      this.todo.splice(index, 1);
    },
    clickontoogle: function(active) {
      this.sortByStatus = active;
    }
  },
  computed: {
    todoByStatus: function() {

      if(!this.sortByStatus) {
        return this.todo;
      }

      var sortedArray = []
      var doneArray = this.todo.filter(function(item) { return item.done; });
      var notDoneArray = this.todo.filter(function(item) { return !item.done; });
      
      sortedArray = [...notDoneArray, ...doneArray];
      return sortedArray;
    }
  }
});


//JS code for progress

// Vue.component('progres', {
//   props: ['title', 'count', 'backgroundColor'],
//   template: `<div class='progress-card' :style="filterStyleCard">
//       <div class="progress_title">{{ title }}</div>
//       <div style='margin-top: 2rem' class="ui small indicating progress">
//           <div :style="filterStyleProgress" class="bar"></div>
//           <div class="label">Progress</div>
//       </div>
//       <span>{{ count }} %</span>
//       <div class="ui icon buttons">
//           <div class="decrement ui basic button icon"  @click="decrease"><i class="minus icon"></i></div>
//           <div class="increment ui basic button icon"  @click="increase"><i class="plus icon"></i></div>
//           <div class="ui basic button icon" @click="editTitle"><i class="edit outline icon"></i></div>
//           <div class="ui basic button icon ui right dropdown simple item"><i class="tint icon"></i>
//             <div class="menu">
//               <div class="item" @click="backgroundRed">
//               <i class="circle icon" style="color: #ff714f"></i></div>
//               <div class="item" @click="backgroundBlue">
//               <i class="circle icon" style="color: #91b3cf"></i></div>
//               <div class="item" @click="backgroundYellow">
//               <i class="circle icon" style="color: #fdba2e"></i></div>
//               <div class="item" @click="backgroundCream">
//               <i class="circle icon" style="color: #fef4d9"></i></div>
//             </div>
//         </div>
//   </div>`,

//   computed: {
//     filterStyleProgress() {
//       return {
//         width: this.count.toString() + '%'
//       };
//     },

//     filterStyleCard() {
//       return {
//         float: 'left',
//         width: '230px',
//         height: '147px',
//         margin: '30px',
//         padding: '1rem',
//         background: this.backgroundColor,
//         boxShadow: 'rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px',
//         borderRadius: '20px'
//     }
//   }


//   },

//   methods: {
//     decrease: function () {
//       if(this.count > 0){
//       this.count -= 5
//       }
//     },
//     increase: function () {
//       if(this.count < 100){
//       this.count += 5
//     }
//     },

//     backgroundRed: function() {
//       this.backgroundColor = "#ff714f";
//     },

//     backgroundBlue: function() {
//       this.backgroundColor = "#91b3cf";
//     },

//     backgroundCream: function() {
//       this.backgroundColor = "#fef4d9";
//     },

//     backgroundYellow: function() {
//       this.backgroundColor = "#fdba2e";
//     },

//     editTitle: function() {
//       var title = prompt("Change progress title: ");
//       if(title) {
//         this.title = title;
//       }
//     }
//   }


// });

// var app = new Vue({
//   el: '#progress',
//   delimiters : ['[[',']]'],
//   data: {
//     cards: [
//       { id:1, title: "Discrete Math", count: 50, backgroundColor: "#91b3cf"},
//       { id:2, title: "Machine Learning", count: 60, backgroundColor: "#91b3cf"},
//       { id:3, title: "Orbital", count: 90, backgroundColor: "#91b3cf"}
//     ]
//   },
// });
  