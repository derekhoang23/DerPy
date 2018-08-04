import React, { Component } from 'react';
import axios from 'axios';
import { Panel, ListGroup, ListGroupItem, PageHeader, FormGroup,
	ControlLabel, FormControl, Button } from 'react-bootstrap';



export default class SubredditContent extends Component {
	constructor(props) {
		super(props);
		this.state = {
			messages: [],
			subreddit: '',
			title: '',
			comment: '',
		}
	}

	componentDidMount() {
		const { subreddit, subredditId, contentId } = this.props;
		axios.get(`/api/${subreddit}/${subredditId}/subreddit_content/${contentId}`).then(res => {
			const messages = res.data.comment;
			const subreddit = res.data.subreddit.name;
			const title = res.data.title;
			this.setState({ messages, subreddit, title });
		}).catch(err => {
			console.log('err in getting list', err)
		})
	}

	handleChangeComment(e) {
		this.setState({ comment: e.target.value });
	}

	handlePostComment() {
		const { comment, title } = this.state;
		const { subreddit, subredditId, contentId } = this.props;
		axios.post(`/api/${subreddit}/${subredditId}/subreddit_content/${contentId}/comment`, {
			user: 'derekhoang',
			user_comment: comment,
			subreddit_content: contentId,
		}).then(res => {
			console.log('success', res);
		}).catch(err => {
			console.log('posted comment error', err)
		})
	}

	render() {
		const { messages, subreddit, title, comment } = this.state;
		console.log('mesages ', messages)
		return (
			<div>
				<PageHeader>
					<small>Subreddit: {subreddit} </small>
				</PageHeader>
				<Panel>
					<Panel.Heading>{title}</Panel.Heading>
					<ListGroup>
						{messages.map(message => <ListGroupItem key={message.id}>
							{message.user_comment}
							</ListGroupItem>)}
					</ListGroup>
				</Panel>
				<form>
					<FormGroup controlId="formControlsTextarea">
						<ControlLabel>Comment</ControlLabel>
						<FormControl placeholder="comment"
						type="text"
						value={comment}
						onChange={this.handleChangeComment.bind(this)}/>
					</FormGroup>
					<Button type="submit"
						bsStyle="primary"
						onClick={this.handlePostComment.bind(this)}>
						Submit
					</Button>
				</form>
			</div>
		)
	}
}