new Vue({
  el: '#login',
  delimiters: ['[[', ']]'],
  data: function(){
    return {
    username: '',
    password: '',
    block:true,
    user_msg: null,
    pass_msg: null,
    user_state: null,
    pass_state: null
    }
  },
  watch:{
  },
  methods:{
    login: function(){
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
      .then(( res)=>{
        var pass=res.data.p_error;
        var user=res.data.u_error;
        var error=res.data.error;
        if(!pass&&!user){
          if(error){
            this.pass_msg=error;
            this.user_msg='';
          }
          else{
            window.location='/profile';
          }
        }
        else{
          this.user_msg=user;
          this.pass_msg=pass;
        }
        console.log(data);
      })
      .catch(function( error){
      });
    }
  }
})
