new Vue({
  el: '#homepage',
  delimiters: ['[[', ']]'],
  data: {
    hello: 'Hello World',
    slide: 0,
    sliding: null,
    tags:[
      {id: 1,link:'wewe.com', name:'bkit ganun?'},
      {id: 2,link:'wewe.com', name: 'hays'},
      {id: 3,link:'wewe.com', name: 'bkit ako nag tatype?'},
      {id: 4,link:'wewe.com', name: 'anu to?'},
      {id: 5,link:'wewe.com', name: 'angas'},
      {id: 6,link:'wewe.com', name: 'medyo malupet'},
      {id: 7,link:'wewe.com', name: 'nice nice'},
      {id: 8,link:'wewe.com', name: 'lupet'},
      {id: 9,link:'wewe.com', name: 'bukake'},
      {id: 10,link:'wewe.com', name: 'my step sister'},
      {id: 11,link:'wewe.com', name: 'I just came'},
      {id: 12,link:'wewe.com', name: 'team bahay'},
      {id: 13,link:'wewe.com', name: 'dilawan'},
      {id: 14,link:'wewe.com', name: 'malacanang'},
      {id: 15,link:'wewe.com', name: 'php'},
      {id: 16,link:'wewe.com', name: 'programming'},
      {id: 17,link:'wewe.com', name: 'incredibles'},
      {id: 18,link:'wewe.com', name: 'avengers'},
      {id: 19,link:'wewe.com', name: 'your mom'},
      {id: 20,link:'wewe.com', name: 'hentai is life'}
    ],
    subscriptions: [
      { id: 1, text: 'Subsciptions 1', link:'subscription1'},
      { id: 2, text: 'Subsciptions 2', link:'subscription2'},
      { id: 3, text: 'Subsciptions 3', link:'subscription3'},
      { id: 4, text: 'Subsciptions 4', link:'subscription4'},
      { id: 5, text: 'Subsciptions 5', link:'subscription5'},
      { id: 6, text: 'Subsciptions 6', link:'subscription6'}
    ],
    topWriters: [
      { id: 1, text: 'Writer 1', link:'Writer'},
      { id: 2, text: 'Writer 2', link:'Writer'},
      { id: 3, text: 'Writer 3', link:'Writer'},
      { id: 4, text: 'Writer 4', link:'Writer'},
      { id: 5, text: 'Writer 5', link:'Writer'}
    ],
    topPublications: [
      { id: 1, text: 'Publication 1', link:'Publication'},
      { id: 2, text: 'Publication 2', link:'Publication'},
      { id: 3, text: 'Publication 3', link:'Publication'},
      { id: 4, text: 'Publication 4', link:'Publication'},
      { id: 5, text: 'Publication 5', link:'Publication'}
    ],
    posts:[
      { id: 1, title: 'Title', date:'June 1, 2016', author:'Vincent TIbbs',
        authorlink:'vince', postLink:'postLink',details: 'We can use the v-for directive to render a list of items based on an array. The v-for directive requires a special syntax in the form of item in items, where items is the source data array and item is an alias for the array element being iterated on',points:33},
        { id: 2, title: 'Title2', date:'June 2, 2016', author:'Kyle Aquino',
          authorlink:'kyle', postLink:'postLink',details: 'We can use the v-for directive to render a list of items based on an array. The v-for directive requires a special syntax in the form of item in items, where items is the source data array and item is an alias for the array element being iterated on',points:34},
    ]
  },
  methods: {
    onSlideStart (slide) {
     this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    }
  }
})
