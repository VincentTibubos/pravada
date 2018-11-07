new Vue({
  el: '#account',
  delimiters: ['[[', ']]'],
  data: {
    slide: 0,
    sliding: null,
    tags:[
      {link:'wewe.com',name: 'tag'},
      {link:'wewe.com',name: 'tag'},
      {link:'wewe.com',name: 'tag'},
      {link:'wewe.com',name: 'tag'},
      {link:'wewe.com',name: 'tag'},
      {link:'wewe.com',name: 'tag'},
      {link:'wewe.com',name: 'tag'},
    ],
    subscriptions: [
      { id: 1, text: 'Subsciptions 1', link:'subscription1'},
      { id: 2, text: 'Subsciptions 2', link:'subscription2'},
      { id: 3, text: 'Subsciptions 3', link:'subscription3'},
      { id: 4, text: 'Subsciptions 4', link:'subscription4'},
      { id: 5, text: 'Subsciptions 5', link:'subscription5'}
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
