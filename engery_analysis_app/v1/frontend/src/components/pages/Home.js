import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";



const Projects = () => {
  const [projects, setProject] = useState([]);

  const PROJECTS_DATA = [
    {
        "id": 16,
        "project_name": "Mettlach",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 9
    },
    {
        "id": 17,
        "project_name": "Harrienstedt",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 19
    },
    {
        "id": 11,
        "project_name": "Watzerath",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Asset",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 17
    },
    {
        "id": 12,
        "project_name": "Egeln",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "QE 4",
        "project_status_id": "1 Operating",
        "company_id": 3
    },
    {
        "id": 21,
        "project_name": "Holtum",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Asset",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 10
    },
    {
        "id": 22,
        "project_name": "Jeesewitz",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 11
    },
    {
        "id": 18,
        "project_name": "Zodel",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 16
    },
    {
        "id": 9,
        "project_name": "Zörbig",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Asset",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 14
    },
    {
        "id": 47,
        "project_name": "Ahrensbök",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "QE 4",
        "project_status_id": "1 Operating",
        "company_id": 8
    },
    {
        "id": 13,
        "project_name": "Beppener Bruch",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "QE 4",
        "project_status_id": "2 DD",
        "company_id": 12
    },
    {
        "id": 15,
        "project_name": "Schackensleben",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Asset",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 18
    },
    {
        "id": 20,
        "project_name": "Salingen",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Asset",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 18
    },
    {
        "id": 14,
        "project_name": "Sebbenhausen-Schweringen",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Share",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 13
    },
    {
        "id": 19,
        "project_name": "Ingstetten",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Asset",
        "project_group_id": "QE 4",
        "project_status_id": "2 DD",
        "company_id": 4
    },
    {
        "id": 10,
        "project_name": "Waldow",
        "project_number": 2,
        "acquisition_date": 3,
        "number_3l_code": 4,
        "project_deal_type_id": "Asset",
        "project_group_id": "RW 1",
        "project_status_id": "1 Operating",
        "company_id": 15
    }
];

  useEffect(() => {
    console.log("*** Loading Projects ***");
    loadProjects();
  }, []);

  const loadProjects = async () => {
    // const result = await axios.get("http://127.0.0.1:8000/projects");
    // console.log("*** Projects: ", result.data);

    setProject(PROJECTS_DATA);
  };

  const deleteProject = async id => {
    await axios.delete(`http://127.0.0.1:8000/projects/${id}`);
    loadProjects();
  };

  return (
    <div className="container">
      <div className="py-4">
        <h2>Projects</h2>
        <table class="table border shadow">
          <thead class="bg_color_custom">
            <tr>
            <th scope="col">#</th>
              <th scope="col">Project Name</th>
              <th scope="col">Project Deal Type Id</th>
              <th scope="col">Project Status Id</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {projects.map((project, index) => (
              <tr>
                <td>{index + 1}</td>
                <td>{project.project_name}</td>
                <td>{project.project_deal_type_id}</td>
                <td>{project.project_status_id}</td>
                <td>
                  <Link class="btn btn-primary mr-2" to={`/users/${project.id}`}>
                    View
                  </Link>
                  <Link
                    class="btn btn-outline-primary mr-2"
                    to={`/users/edit/${project.id}`}
                  >
                    Edit
                  </Link>
                  <Link
                    class="btn btn-danger"
                    onClick={() => deleteProject(project.id)}
                  >
                    Delete
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Projects;
