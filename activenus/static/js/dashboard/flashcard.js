var deck1 = [{
	"val": "Goddess of love, beauty, desire, sex and pleasure",
	"key": "Aphrodite",
	"startcard": false,
	"number": 0
}, {
	"val": "God of music, arts, knowledge, healing, plague, prophecy, poetry, manly beauty, archery, and the sun",
	"key": "Apollo",
	"startcard": false,
	"number": 0
}, {
	"val": "King of the underworld and the dead, and god of regret.",
	"key": "Hades",
	"startcard": false,
	"number": 0
}, {
	"val": "Crippled god of fire, metalworking, and crafts",
	"key": "Hephaestus",
	"startcard": false,
	"number": 0
}, {
	"val": "Queen of the gods and goddess of marriage, women, childbirth, heirs, kings, and empires",
	"key": "Hera",
	"startcard": false,
	"number": 0
}, {
	"val": "King and father of the gods, the ruler of Mount Olympus and the god of the sky, weather, thunder, lightning, law, order, and justice",
	"key": "Zeus",
	"startcard": false,
	"number": 0
}];


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

	mounted() {
		if (localStorage.getItem('deck')) {
		  try {
			this.deck = JSON.parse(localStorage.getItem('deck'));
		  } catch(e) {
			localStorage.removeItem('deck');
		  }
		} else {
			let parsed = JSON.stringify(deck1);
			localStorage.setItem('deck', parsed);
			this.deck = JSON.parse(localStorage.getItem('deck'));
		}
		
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
			let parsed = JSON.stringify(this.deck);
			localStorage.setItem('deck', parsed);
			console.log('It landed to addcard func!');
		  },

		previous: function(){
			this.flipped = false;
			this.card.number++;
			this.card = this.deck[Math.floor(Math.random() * this.deck.length)];
			let parsed = JSON.stringify(this.deck);
			localStorage.setItem('deck', parsed);
			// this.current = this.getPrev;
		},

		forward: function(){
			if(!this.card.startcard){
				this.flipped = false;
				this.card.number++;
				this.card = this.deck[Math.floor(Math.random() * this.deck.length)];
				let parsed = JSON.stringify(this.deck);
				localStorage.setItem('deck', parsed);
				// this.current = this.getNext;
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