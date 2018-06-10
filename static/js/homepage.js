new Vue({
  el: '#homepage',
  delimiters: ['[[', ']]'],
  data: {
    hello: 'Hello World',
    slide: 0,
    sliding: null,
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
      { id: 1, title: 'Title', date:'date', author:'author',
        authorlink:'authorlink', postLink:'postlink'}
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
