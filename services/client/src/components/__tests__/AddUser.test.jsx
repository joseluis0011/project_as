import React from 'react';
import { shallow } from 'enzyme';
import render from 'react-test-render';

import AddUser from './AddUser'

test('AddUser renders properly',()=>{
    const wrapper = shallow (<AddUser/>);
    const element = wrapper.find('form');
    expect(element.find('input').length).toBe(3);
    expect(element = wrapper.find('input').get(0).props.name).toBe('username');
    expect(element = wrapper.find('input').get(1).props.name).toBe('email');
    expect(element = wrapper.find('input').get(2).props.type).toBe('submit');
})