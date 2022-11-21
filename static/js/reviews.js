const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const getComment = function (e) {
  const comments = document.querySelector(`#${e}`);
  const commentsList = document.querySelector(`#${e}-list`);
  commentsList.classList.toggle('display-none');

  if (commentsList.classList.contains('display-none')) {
    comments.innerText = "댓글보기"
  } else {
    comments.innerText = "댓글닫기"
  };
};

const getCreateComment = function (e) {
  const commentForm = document.querySelector(`#${e}-form`);
  commentForm.classList.toggle('display-none');
}

const submitComment = function (e) {
  event.preventDefault();
  const commentForm = document.querySelector(`#${e}`);

  const pk = event.target.dataset.reviewId;

  axios({
    method: 'post',
    url: `/reviews/${pk}/comments/`,
    headers: { 'X-CSRFToken': csrftoken },
    data: new FormData(commentForm)
  })
    .then(response => {
      const commentsList = document.querySelector(`#review-${response.data.comments_data[0].study_id}-comments-list`)
      commentsList.textContent = "";
      for (let i = 0; i < response.data.comments_data.length; i++) {
        if (response.data.comments_data[i].request_user_pk === response.data.comments_data[i].user_pk) {
          commentsList.insertAdjacentHTML('beforeend', `<span>${response.data.comments_data[i].username} | ${response.data.comments_data[i].content} | ${response.data.comments_data[i].created_at} </span>
          <button id="comment-${response.data.comments_data[i].comment_pk}-update" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" class="btn btn-outline-success" onclick="getUpdateComment(this.id)">수정</button>
          <button id="comment-${response.data.comments_data[i].comment_pk}-delete" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" class="btn btn-outline-danger" onclick="deleteComment(this.id)">삭제</button>
          <div id="comment-${response.data.comments_data[i].comment_pk}-update-form" class="display-none">
          <input id="comment-${response.data.comments_data[i].comment_pk}-update-content" type="text" value="${response.data.comments_data[i].content}">
          <button id="comment-${response.data.comments_data[i].comment_pk}-update-btn" class="btn btn-primary" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" onclick="updateComment(this.id)">확인</button>
          </div><br>`);
        } else {
          commentsList.insertAdjacentHTML('beforeend', `<span>${response.data.comments_data[i].username} | ${response.data.comments_data[i].content} | ${response.data.comments_data[i].created_at} </span><br>`);
        }

      }
      commentForm.reset();
      let counter = document.getElementById("counter_id_content");
      counter.innerText = "0/500";

      //코멘트 작성 후 코멘트리스트 보여주기
      commentsList.classList.remove('display-none');

    })

}

const getUpdateComment = function (e) {
  const updateComment = document.querySelector(`#${e}-form`);
  updateComment.classList.toggle('display-none');
}

const updateComment = function (e) {
  const commentValue = document.querySelector(`#comment-${event.target.dataset.commentId}-update-content`).value;
  const pk1 = event.target.dataset.reviewId;


  axios({
    method: 'post',
    url: `/reviews/${pk1}/${event.target.dataset.commentId}/update/`,
    headers: { 'X-CSRFToken': csrftoken },
    data: { 'content': commentValue }
  })
    .then(response => {
      const commentsList = document.querySelector(`#review-${response.data.comments_data[0].study_id}-comments-list`);
      commentsList.textContent = "";
      for (let i = 0; i < response.data.comments_data.length; i++) {
        if (response.data.comments_data[i].request_user_pk === response.data.comments_data[i].user_pk) {
          commentsList.insertAdjacentHTML('beforeend', `<span>${response.data.comments_data[i].username} | ${response.data.comments_data[i].content} | ${response.data.comments_data[i].created_at} </span>
          <button id="comment-${response.data.comments_data[i].comment_pk}-update" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" class="btn btn-outline-success" onclick="getUpdateComment(this.id)">수정</button>
          <button id="comment-${response.data.comments_data[i].comment_pk}-delete" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" class="btn btn-outline-danger" onclick="deleteComment(this.id)">삭제</button>
          <div id="comment-${response.data.comments_data[i].comment_pk}-update-form" class="display-none">
          <input id="comment-${response.data.comments_data[i].comment_pk}-update-content" type="text" value="${response.data.comments_data[i].content}">
          <button id="comment-${response.data.comments_data[i].comment_pk}-update-btn" class="btn btn-primary" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" onclick="updateComment(this.id)">확인</button>
          </div><br>`);
        } else {
          commentsList.insertAdjacentHTML('beforeend', `<span>${response.data.comments_data[i].username} | ${response.data.comments_data[i].content} | ${response.data.comments_data[i].created_at} </span><br>`);
        }

      }
    })
}

const deleteComment = function (e) {
  const reviewPk = event.target.dataset.reviewId
  if (confirm("정말 삭제하시겠습니까??") == true) {
    axios({
      method: 'post',
      url: `/reviews/${event.target.dataset.reviewId}/${event.target.dataset.commentId}/delete/`,
      headers: { 'X-CSRFToken': csrftoken },
    })
      .then(response => {
        const commentsList = document.querySelector(`#review-${reviewPk}-comments-list`)
        commentsList.textContent = "";

        for (let i = 0; i < response.data.comments_data.length; i++) {
          if (response.data.comments_data[i].request_user_pk === response.data.comments_data[i].user_pk) {
            commentsList.insertAdjacentHTML('beforeend', `<span>${response.data.comments_data[i].username} | ${response.data.comments_data[i].content} | ${response.data.comments_data[i].created_at} </span>
          <button id="comment-${response.data.comments_data[i].comment_pk}-update" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" class="btn btn-outline-success" onclick="getUpdateComment(this.id)">수정</button>
          <button id="comment-${response.data.comments_data[i].comment_pk}-delete" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" class="btn btn-outline-danger" onclick="deleteComment(this.id)">삭제</button>
          <div id="comment-${response.data.comments_data[i].comment_pk}-update-form" class="display-none">
          <input id="comment-${response.data.comments_data[i].comment_pk}-update-content" type="text" value="${response.data.comments_data[i].content}">
          <button id="comment-${response.data.comments_data[i].comment_pk}-update-btn" class="btn btn-primary" data-review-id="${response.data.comments_data[i].study_id}" data-comment-id="${response.data.comments_data[i].comment_pk}" onclick="updateComment(this.id)">확인</button>
          </div><br>`)
          } else {
            commentsList.insertAdjacentHTML('beforeend', `<span>${response.data.comments_data[i].username} | ${response.data.comments_data[i].content} | ${response.data.comments_data[i].created_at} </span><br>`)
          }

        }
      })
  } else {
    return;
  }
}