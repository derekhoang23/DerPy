import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link, Switch, matchPath} from 'react-router-dom';
import { ModalContainer } from 'react-router-modal';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import Example from './Components/Match';
import SubredditList from './Components/SubredditList';
import NavbarContainer from './Containers/NavbarContainer';
import SubredditContentContainer from './Containers/SubredditContentContainer';
import Test from './Components/Test';
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true;

class RouteRender extends Component {
	render() {
		const url = '/'
		return (
			<BrowserRouter>
				<div>
					<NavbarContainer/>
					<Switch>
						<Route path='/r/:subreddit/:subredditId/subreddit_content/:contentId' component={SubredditContentContainer}/>
						<Route exact path={url} component={App}/>
					</Switch>
				</div>
			</BrowserRouter>
		)
	}
}
ReactDOM.render(<RouteRender/>, document.getElementById('root'));
registerServiceWorker();
