new Vue({
  el: '#register',
  delimiters: ['[[', ']]'],
  data: function(){
    return {
    email: '',
    username: '',
    fname: '',
    lname: '',
    password: '',
    confirmPassword: '',
    block:true,
    user_msg: null,
    email_msg: null,
    l_msg: null,
    f_msg: null,
    cp_msg: null,
    p_msg: null,
    user_state: null,
    email_state: null,
    l_state: null,
    f_state: null,
    cp_state: null,
    p_state: null
    }
  },
  methods:{
    register: function(){
      var formdata=new FormData();
      var csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value;
      formdata.append('csrfmiddlewaretoken',csrf);
      formdata.append('username',this.username);
      // formdata.append('password',this.password);
      formdata.append('password1',this.password);
      formdata.append('password2',this.confirmPassword);
      formdata.append('email',this.email);
      formdata.append('first_name',this.fname);
      formdata.append('last_name',this.lname);
      axios.defaults.xsrfHeaderName='X-CSRFToken';
      axios.defaults.xsrfCookieName='XCSRF-TOKEN';
      axios({
        method:'POST',
        url: '/register/',
        data:formdata,
        headers:{
          'X-CSRFToken': csrf
        }
      })
      .then((res)=>{
        var error=res.data.error;
        var user=res.data.u_error;
        var email=res.data.e_error;
        var lname=res.data.l_error;
        var fname=res.data.f_error;
        var pass=res.data.p_error;
        var cpass=res.data.cp_error;
        this.user_state=user==''?true:false;
        this.email_state=email==''?true:false;
        this.l_state=lname==''?true:false;
        this.f_state=fname==''?true:false;
        this.cp_state=cpass==''?true:false;
        this.p_state=pass==''?true:false;
        if(!pass&&!user&&!fname&&!lname&&!email&&!cpass){
            window.location='/profile/';
        }
        else{
          this.cp_msg=cpass;
          this.user_msg=user;
          this.email_msg=email;
          this.l_msg=lname;
          this.f_msg=fname;
          this.p_msg=pass;
        }
      })
      .catch(function( error){
      });
    },
    check: function(){
      return this.users.filter( (user)=> {
        return user.username==this.username && user.password==this.password;
      }).length>0;
    }
  },
  computed: {
    // state () {
    //   return (this.message == '' ? true : false)
    // },
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
    // invalidPassFeedback () {
    //   return this.message;
    // }
    // validPassFeedback () {
    //   return this.state === true ? 'Your good tog go' : ''
    // }
  }
})
