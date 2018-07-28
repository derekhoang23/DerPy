import React, { Component } from 'react';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';
import { autobind } from 'core-decorators';
import axios from 'axios';

export default class NavbarComponent extends Component {
	constructor(props) {
		super(props)
	}

	testAuth() {
		// axios.get('/api/').then(res => {
		// 	console.log('res ', res)
		// }).catch(err => {
		// 	console.log('error ', err.response.status)
		// });
		axios.post('/login/', {username: 'q', password: 'arya1234' }).then(rv => {
			console.log('login ', rv);
			this.testPost();
		}).catch(err => {
			console.log('login err ', err.response);
		})
	}


	testPost() {
		axios.patch('http://localhost:8000/api/stuffs/1/', { quantity: 2 }).then(res => {
			console.log('updated res ', res);
		}).catch(err => {
			console.log('uodate err ', err)
		})
	}

	render() {
		return (
			<Navbar inverse collapseOnSelect>
			  <Navbar.Header>
			    <Navbar.Brand>
			      <a href="#brand">React-Bootstrap</a>
			    </Navbar.Brand>
			    <Navbar.Toggle />
			  </Navbar.Header>
			  <Navbar.Collapse>
			    <Nav>
			      <NavItem eventKey={1} href="#" onClick={this.testAuth.bind(this)}>
			        Test back end
			      </NavItem>
			      <NavItem eventKey={2} href="#" onClick={this.testPost.bind(this)}>
			        Test Post 
			      </NavItem>
			      <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
			        <MenuItem eventKey={3.1}>Action</MenuItem>
			        <MenuItem eventKey={3.2}>Another action</MenuItem>
			        <MenuItem eventKey={3.3}>Something else here</MenuItem>
			        <MenuItem divider />
			        <MenuItem eventKey={3.3}>Separated link</MenuItem>
			      </NavDropdown>
			    </Nav>
			    <Nav pullRight>
			      <NavItem eventKey={1} href="#">
			        Link Right
			      </NavItem>
			      <NavItem eventKey={2} href="#">
			        Link Right
			      </NavItem>
			    </Nav>
			  </Navbar.Collapse>
			</Navbar>
		)
	}
}