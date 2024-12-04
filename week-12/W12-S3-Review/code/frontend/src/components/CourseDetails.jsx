import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api';

const CourseList = () => {
  const [course, setCourse] = useState({});

  const [showDelegates, setShowDelegates] = useState(false);

  const { id } = useParams();

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await api.get(`/api/courses/${id}`);

        setCourse(response.data);
      } catch (error) {
        console.error(`Failed to fetch course with id ${id}`, error);
      }
    };

    fetchCourses();
  }, []);

  const toggleDelegates = () => {
    setShowDelegates(!showDelegates);
  }

  return (
    <div>
      <h2>Course Details</h2>
      {course.id && (
        <>
        <div className="card">
          <div>Course Number: {course.id}</div>
          <div>Course Title: {course.title}</div>
          <div>Course Description: {course.description}</div>
          <div>Number of Delegates: {course.users.length}</div>

          <div className="card-options">
            <button className="button" onClick={() => toggleDelegates()}>View Delegates</button>
          </div>
        </div>

        {showDelegates && (

          <div className="card mt-5">
            <h3>Delegates</h3>
            <div className="delegate-list">
              {course.users.map((user) => (
                <div key={user.id} className="delegate">
                  <div>{user.username}</div>
                  <div>{user.email}</div>
                </div>
              ))}
            </div>
          </div> )
        }
      </>   
      )}
    </div>
  );
};

export default CourseList;
