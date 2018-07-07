new Vue({
  el: '#register',
  delimiters: ['[[', ']]'],
  data: {
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
    block:true,
    message: '',
    users:[
      {username: 'Vincent', password: '12345678'},
      {username: 'Jose', password: 'sample123'},
      {username: 'Dilaw', password: 'dilawan123'}
    ]
  },
  methods:{
    register: function(){
      if(this.username<4){
        this.message='Username must have atleast 4 characters';
      }
      else if(this.password<8){
        this.message='Password must have atleast 8 characters';
      }
      else if(this.password!=this.confirmPassword){
        this.message='Password Mismatch';
      }
      else if(!this.check()){
        this.message='';
        alert('successfully login');
      }
      else{
        this.message="Invalid username or password";
        this.password='';
        this.confirmPassword='';
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
    }
    // validPassFeedback () {
    //   return this.state === true ? 'Your good tog go' : ''
    // }
  }
})