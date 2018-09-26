new Vue({
  el: '#login',
  delimiters: ['[[', ']]'],
  data: {
    username: '',
    password: '',
    block:true,
    message: ''
    // users:[
    //   {username: 'Vincent', password: '12345678'},
    //   {username: 'Jose', password: 'sample123'},
    //   {username: 'Dilaw', password: 'dilawan123'}
    // ]
  },
  methods:{
    login: function(){
      if(this.username.length<4){
        this.message='Username must have atleast 4 characters';
      }
      else if(this.password.length<8){
        this.message='Password must have atleast 8 characters';
      }
      else{
        var formdata=new FormData();
        var csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value;
        formdata.append('csrfmiddlewaretoken',csrf);
        formdata.append('username',this.username);
        formdata.append('password',this.password);
        axios.defaults.xsrfHeaderName='X-CSRFToken';
        axios.defaults.xsrfCookieName='XCSRF-TOKEN';
        axios({
          method:'POST',
          url: '/login/',
          data:formdata,
          headers:{
            'X-CSRFToken': csrf
          }
        })
        .then(function( res){
          if(res.data.error==''){
            window.location='/profile'
          }
        })
        .catch(function( error){
        });
        this.message="Invalid username or password";
        this.password='';
      }
    },
    check: function(){
      return this.users.filter( (user)=> {
        return user.username==this.username && user.password==this.password;
      }).length>0;
    }
  },
  computed: {
    state () {
      return (this.message == '' ? true : false)
    },
    // state2 () {
    //   return this.password.length >= 8 ? true : false
    // },
    // invalidUserFeedback () {
    //   if (this.username.length > 4) {
    //     return ''
    //   } else if (this.username.length > 0) {
    //     return 'Enter at least 4 characters'
    //   } else {
    //     return 'Please enter something'
    //   }
    // },
    // validUserFeedback () {
    //   return this.state === true ? 'Valid Username' : ''
    // },
    invalidPassFeedback () {
      return this.message;
    },
    // validPassFeedback () {
    //   return this.state === true ? 'Your good tog go' : ''
    // }
  }
})