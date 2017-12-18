<h1>F5 ASM Policy Migration:</h1>
<h2>Description&nbsp;</h2>
<p>The <em>ASM Policy Migration </em>workflow is used for migrating ASM policies between the F5 devices (that is, from a source device to a destination device). You can only migrate the policy from a lower version of F5 device to a higher version or between the same versions of F5 devices. A new policy is created on the destination device with the same configuration as in the source device and is associated with a virtual server present in the destination device. Also, you have the option to integrate the workflow with an ITSM tool called ServiceNow for approvals and tracking. The ServiceNow change request ID is associated with the request and is updated based on the implementation status.</p>
<p>&nbsp;</p>
<p><img src="hhttps://github.com/AppViewX/AVX-12.X-Visual-Workflows/blob/master/ASM%20Policy%20Migration/docs/img/F5%20ASM%20policy%20Migration.png" alt="&ldquo;F5" width="&ldquo;600&rdquo;" /> </p>
<h2>Prerequisites</h2>
<p><br />To run this automation workflow in your environment, ensure that the following pre-requisites are met:</p>
<ul>
<li>Free AppViewX or AppViewX version 12.1.0 and 12.2.0 has been downloaded and installed.</li>
<li>The ADC devices has been added in the AppViewX inventory with a Data center name.</li>
<li>The F5 ASM devices have been added under both the WAF and ADC sections in the AppViewX inventory.</li>
<li>Each ADC device is a managed entity in AppViewX.</li>
<li>You have administrator permissions to add a device to the AppViewX inventory.</li>
<li>An ITSM tool (ServiceNow) has been configured under the Change Management section of the AppViewX Settings module.</li>
</ul>
<p>&nbsp;</p>
<h2>Compatible Software Versions</h2>
<p>The workflow has been tested and validated on the following software versions:</p>
<ul>
<li>AppViewX &ndash; Free AppViewX, AVX 12.1.0, and AVX 12.2.0</li>
<li>ServiceNow &ndash; Jakartha and Geneva version</li>
<li>F5 (both LTM and GTM) &ndash; version 10.x, 11.x, or 12.x</li>
</ul>
<p>&nbsp;</p>
<h2>Download Free AppViewX</h2>
<p>Using Free AppViewX you can manage and automate your network services for 60 days. After this period, you may extend to an annual free license.</p>
<p><a href="https://login.appviewx.com/register/">https://login.appviewx.com/register/</a></p>
<p>&nbsp;</p>