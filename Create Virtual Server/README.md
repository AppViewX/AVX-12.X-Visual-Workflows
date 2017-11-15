<h4>Create Virtual Server</h4>
<div>
<p>The <strong>Create Virtual Server</strong> workflow creates a virtual server and associates it with profiles, monitors, pool, and pool members in F5 LTM using Infoblox and ServiceNow integration. </p>
<p>It uses a simple, self-service based approach to gather application-provisioning requirements and generate vendor-specific configurations or REST APIs. This self-service workflow filters F5 ADC devices based on the user’s access permissions, defined by Role Based Access Control (RBAC). The platform integrates with IPAM systems like Infoblox, which allows users to reserve a free IP address from the available address pools and create DNS binding for the new virtual server in Infoblox.</p>
<p>The workflow also includes an option to create or bind existing profiles and monitors to the virtual server and allows users to create change request tickets in ITSM systems ¬like ServiceNow for approvals and tracking. The service request change ID is associated with the work order and is updated based on the implementation status.</p>
<img src=“images/abc.png” alt=“Relevant alt”>


