<h1>Create Virtual Server:</h1>
<h2>Description&nbsp;</h2>
<p>The <em>Create Virtual Server </em>workflow creates a virtual server and associates it with profiles, monitors, pool, and pool members in F5 LTM using Infoblox and ServiceNow integration.</p>
<p><img src="https://github.com/AppViewX/AVX-12.X-Visual-Workflows/blob/master/Create%20Virtual%20Server/docs/img/Automating%20Virtual%20Server%20creation%20with%20AppViewX_1.0-01-04.png" alt="Create virtual server flow diagram" width="70" /></p>
<p>It uses a simple, self-service based approach to gather application-provisioning requirements and generate vendor-specific configurations or REST APIs. This self-service workflow filters F5 ADC devices based on the user&rsquo;s access permissions, defined by Role Based Access Control (RBAC). The platform integrates with IPAM systems like Infoblox, which allows users to reserve a free IP address from the available address pools and create DNS binding for the new virtual server in Infoblox.</p>
<p>The workflow also includes an option to create or bind existing profiles and monitors to the virtual server and allows users to create change request tickets in ITSM systems &not;like ServiceNow for approvals and tracking. The service request change ID is associated with the work order and is updated based on the implementation status.</p>
<h2><strong>Prerequisites </strong></h2>
<p>To run this workflow in your environment, the following prerequisites must be met:</p>
<ul>
<li>Free AppViewX, AVX 12.1.0, or AVX 12.2.0 is downloaded and installed.</li>
<li>An F5 LTM device is added to AppViewX as a managed device.</li>
<li>An Infoblox device is added to AppViewX (optional).</li>
<li>ServiceNow is registered to AppViewX (optional).</li>
<li>Multiple server nodes are running the application.</li>
</ul>
<h2><strong>Compatible Software Versions </strong></h2>
<p>The application provisioning automation temples have been validated for the following software versions:</p>
<ul>
<li>AppViewX &ndash; Free AppViewX version, AVX 12.1.0, and AVX 12.2.0</li>
<li>ServiceNow &ndash; Geneva version and Eureka version</li>
<li>Infoblox &ndash; version 7.2.X</li>
<li>F5 LTM &ndash; version 10.X, 11.X, or 12.X</li>
</ul>