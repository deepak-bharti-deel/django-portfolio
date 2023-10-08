  $('.social_links_wrong_class').hover(
  // $('.social_links').hover(
    function inFunction() {
        const classList = $(this.classList).toArray()
        if (this.classList.contains('twitter')) {
          $('body').css({
            'background': "url('/static/img/twitter_profile_bg.jpg') no-repeat center center fixed",
            'height': '100%',
            'margin': 0,
            'padding': 0,
            'width': '100%', 
            'height': '100%',
            'background-size': 'cover',
          })
          $('.box_pic').prop('src', "/static/img/deepak_jimcorbet.jpg")
        } else if (classList.includes('linkedin')) {
          $('body').css({
            'background': "url('/static/img/linkedin_profile_bg.jpg') no-repeat center center fixed",
            'height': '100%',
            'margin': 0,
            'padding': 0,
            'width': '100%', 
            'height': '100%',
            'background-size': 'cover',
          })
          $('.box_pic').prop('src', "/static/img/deepak_lucknow.jpg")
        } else if (classList.includes('github')) {
          $('body').css({
            'background': "url('/static/img/github_profile_bg.jpg') no-repeat center center fixed",
            'height': '100%',
            'margin': 0,
            'padding': 0,
            'width': '100%', 
            'height': '100%',
            'background-size': 'cover',
          })
          $('.box_pic').prop('src', "/static/img/deepak_kheerganga_rock.jpeg")
        } else if (classList.includes('quora')) {
          $('body').css({
            'background': "url('/static/img/quora_profile_bg.jpg') no-repeat center center fixed",
            'height': '100%',
            'margin': 0,
            'padding': 0,
            'width': '100%', 
            'height': '100%',
            'background-size': 'cover',
          })
          $('.box_pic').prop('src', "/static/img/deepak_lucknow_2.jpg")
        } else if (classList.includes('resume')) {
          $('body').css({
            'background': "url('/static/img/deepak_resume.jpg') no-repeat center center fixed",
            'height': '100%',
            'margin': 0,
            'padding': 0,
            'width': '100%', 
            'height': '100%',
            'background-size': 'cover',
          })
          $('.box_pic').prop('src', "/static/img/deepak.jpeg")
        }
    },
    function outFunction(){  
      // setting back to default background image
      $('body').css({
        'margin': 0,
        'padding': 0,
        'background': "url('/static/img/bg_2.jpeg') no-repeat center center fixed",
        'height': '100%',
        'background-size': 'cover',
      })
      $('.box_pic').prop('src', "/static/img/ptt_1.png")
    }
  )

  let boxPicChangeGlobal
  $('.box_pic').hover(
    function inFunction() {
      const images = [
      "/static/img/ptt_1.png",
      "/static/img/boat_1.jpeg",
      // "/static/img/bkk_1.jpeg",
      // "/static/img/dll_1.jpeg",
      // "/static/img/deepak_jimcorbet.jpg",
        ]
      let boxPicChange = setInterval(function(){
        const time = Date.now()
        $('.box_pic').prop('src', images[time % images.length])
      }, 800)
      boxPicChangeGlobal = boxPicChange
    },
    function outFunction() {
      clearInterval(boxPicChangeGlobal)
      $('.box_pic').prop('src', "/static/img/ptt_1.png")
    }
  )
  
  new TypeIt('.dbads', {
    strings: "(dbads)"
  }).go();