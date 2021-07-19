var deck1 = "{{all_cards | safe}}";
console.log(deck1);


const fc = new Vue({
    delimiters: ["[[", "]]"],
	el: '#fc',
	data: {
		deck: [],
		title: "Olympian Gods",
		current: 0,
		card: {
			"val": "Deck: Olympians God. Click next to start",
			"key": "Click me!",
			"startcard": true,
			"number": 0},
		flipped:true,
		newCard:{
			"val": '',
			"key": '',
			"number": 0},
	},



	methods: {
		flip: function(card){
			this.flipped = !this.flipped;
		},

		addCard() {
			// ensure they actually typed something
			if(!(this.newCard.val && this.newCard.key)) return;
			this.deck.push(this.newCard);
			this.newCard = {
				"val": '',
				"key": '',
				"startcard": false,
				"number": 0};
		  },

		previous: function(){
			this.flipped = false;
			this.card.number++;
			this.card = this.deck[Math.floor(Math.random() * this.deck.length)];
			
		},

		forward: function(){
			if(!this.card.startcard){
				this.flipped = false;
				this.card.number++;
				this.card = this.deck[Math.floor(Math.random() * this.deck.length)];

			}

			else {
				if (JSON.parse(localStorage.getItem('deck')) != null && JSON.parse(localStorage.getItem('deck')).length != 0) {
					try {
					  this.deck = JSON.parse(localStorage.getItem('deck'));
					} catch(e) {
					  localStorage.removeItem('deck');
					}
				  } else {
					  let parsed = JSON.stringify(deck1);
					  localStorage.setItem('deck', JSON.stringify(deck1));
					  this.deck = JSON.parse(localStorage.getItem('deck'));
				  }
				this.flipped = false;
				this.card = this.deck[Math.floor(Math.random() * this.deck.length)];
			}
			
		},

	}	
})