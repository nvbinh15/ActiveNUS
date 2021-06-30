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
  
  var todolist = new Vue({
    el: '#todolist',
    delimiters : ['[[',']]'],
    data: {
      newitem:'',
      sortByStatus:false,
      todo: [
        // { id:1, label: "Learn VueJs", done: true },
        // { id:2, label: "Code a todo list", done: false },
        // { id:3, label: "Learn something else", done: false }
      ]
    },
    mounted() {
      if (localStorage.getItem('todo')) {
        try {
          this.todo = JSON.parse(localStorage.getItem('todo'));
        } catch(e) {
          localStorage.removeItem('todo');
        }
      }

      if (localStorage.getItem('sortByStatus')) {
        try {
          this.sortByStatus = JSON.parse(localStorage.getItem('sortByStatus'));
        } catch(e) {
          localStorage.removeItem('sortByStatus');
        }
      }
    },

    methods: {
      addItem: function() {
        this.todo.push({id: Math.floor(Math.random() * 9999) + 10, label: this.newitem, done: false});
        this.newitem = '';
        this.saveTodo();
      },
      markAsDoneOrUndone: function(item) {
        item.done = !item.done;
      },
      deleteItemFromList: function(item) {
        let index = this.todo.indexOf(item)
        this.todo.splice(index, 1);
        this.saveTodo();
      },
      clickontoogle: function(active) {
        this.sortByStatus = active;
        this.saveTodo();
      },

      saveTodo: function() {
        const parsed = JSON.stringify(this.todo);
        localStorage.setItem('todo', parsed);
        localStorage.setItem('sortByStatus', this.sortByStatus);
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