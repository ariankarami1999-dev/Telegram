<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/PMYKx_PMRVBJ85fo9my9YT1Ak0wRDTGbr5C3lvsK8B4j1bJyHBBl1xosYM6RCVRim5FFWgenk8cRAiOS8lxGkG13c-Ry6bS6ByAO95Zu5kcsIaVxNzgGYG9v0JI9VRYwrfXhehPqcdLtwiqkll1_yjGdIJRMeILrn5lZ9PY3GBQjKWNFNLGb71xZojwpfFVz1mllhgeyH9nEbwiXaPhjUCtDenh_pFUfjAwAgHyT7uViIkVVCloqUPOx3n5emPwzejo_zXx_nkpIVTEtWr5SK0Uw2iLnlo4NnlMM4i0hVGnid9qOVqKzESs6RQyTvyYqqSstlZdWId7RTcYt3hq_4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">لوحة يرسمها السيد القائد عبدالملك الحوثي في الرياض والهندي يصورها.</div>
<div class="tg-footer">👁️ 633 · <a href="https://t.me/naya_foriraq/90979" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6156c7481a.mp4?token=XahQ46tRNFFBorUSFFMQq_urknabEapHlJtUWlbFbRQ5cYouTRkg7yv32ByAJ8q4MLs0vWGjwLVK9ybj0ih7RxwbY9GbRHftc3ptZDCstYcr0fF3Fvb8NKqYuuXra4ZfF2jftxbPM5Y0_N85VC3tY4h8iwJxiDnehqKsLnan41EG04DdWGuovsbZUzho-cdhaJsYAHuTbQ2pyawNEM8WVlWsnJ0s6w2RcWOCK9TH__q7ymvDh8Kv_1Dtl0BAP8flUA70f86p4Bd1rCHr3GT0tb7PNiUrXmKzI1hPNNplnlPs3atbOrc0itYPS8O4lselfAbxWiGe_XHmlknSB9we2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6156c7481a.mp4?token=XahQ46tRNFFBorUSFFMQq_urknabEapHlJtUWlbFbRQ5cYouTRkg7yv32ByAJ8q4MLs0vWGjwLVK9ybj0ih7RxwbY9GbRHftc3ptZDCstYcr0fF3Fvb8NKqYuuXra4ZfF2jftxbPM5Y0_N85VC3tY4h8iwJxiDnehqKsLnan41EG04DdWGuovsbZUzho-cdhaJsYAHuTbQ2pyawNEM8WVlWsnJ0s6w2RcWOCK9TH__q7ymvDh8Kv_1Dtl0BAP8flUA70f86p4Bd1rCHr3GT0tb7PNiUrXmKzI1hPNNplnlPs3atbOrc0itYPS8O4lselfAbxWiGe_XHmlknSB9we2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة للحرائق في العاصمة السعودية الرياض على خلفية الهجوم اليمني  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/naya_foriraq/90978" target="_blank">📅 15:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d58f031f4.mp4?token=NxqpAc-odTWdsZRvQGfmCnLA9rHeGXhCvq77TT5hY-SMi7X-iO1L94pd0gj4k9Gwc5dWrj0XnJ7xOdIhj-OiHwVBCfGUqKORh7lAuTv_W_d-FHxo6jfzdJc1D9q5bY8AqdilcOgR3EPczKLrrH27NLrD6dtLfj16fvwISNsHP3aVipvxWmFgavndesUPKt6zTc7IHoBiAUfyazLSjWkaM5Nhmzup_ShYk8Av27UJwNIjI13g3AskEx2fRRiVwxqKnADukNi5GXQUTTyQzY1TeFFIVTgunHNkqiTrbpj6cEuTpLsaY5ircubOch1mv_J5xLnlYTHv9gufw3puXYwP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d58f031f4.mp4?token=NxqpAc-odTWdsZRvQGfmCnLA9rHeGXhCvq77TT5hY-SMi7X-iO1L94pd0gj4k9Gwc5dWrj0XnJ7xOdIhj-OiHwVBCfGUqKORh7lAuTv_W_d-FHxo6jfzdJc1D9q5bY8AqdilcOgR3EPczKLrrH27NLrD6dtLfj16fvwISNsHP3aVipvxWmFgavndesUPKt6zTc7IHoBiAUfyazLSjWkaM5Nhmzup_ShYk8Av27UJwNIjI13g3AskEx2fRRiVwxqKnADukNi5GXQUTTyQzY1TeFFIVTgunHNkqiTrbpj6cEuTpLsaY5ircubOch1mv_J5xLnlYTHv9gufw3puXYwP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/naya_foriraq/90977" target="_blank">📅 15:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جيش العدو: اصابة جنديين في جنوب لبنان بعد تفجير حزب الله عبوة ناسفة بآلية إسرائيلية</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/naya_foriraq/90976" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af67e77ee.mp4?token=E0xXR1_pfVt4_ETYK42NF8bweh9JIfbYUdzHB0h0zyibuKTTz3bPyRODa9XSJsgzUaHRPDcjaMMkSMNJTBePoCV98OwbRQ77phpADO-xs8LyruAvypMx2Lo0OCn30OrJfrPjXG6UgT71RpaOhnsV1yL84A4OoywAd2Pj_clRmKRZFGr83sBTkC0U2FIlnP8njCL_hP2emBW3k53tMXkvoJXUCo8IIdmt-Y30QhA0JhMYkbCSaVeLmee_y0W-2zP-nhB1ZF_oIONIyUDY3pEFutkNzow8WFb5w3robQ7Jvwh8WQYPWxnwqSUWueG9XuhAYrDCn5OiQ6QXi7m6aJqJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af67e77ee.mp4?token=E0xXR1_pfVt4_ETYK42NF8bweh9JIfbYUdzHB0h0zyibuKTTz3bPyRODa9XSJsgzUaHRPDcjaMMkSMNJTBePoCV98OwbRQ77phpADO-xs8LyruAvypMx2Lo0OCn30OrJfrPjXG6UgT71RpaOhnsV1yL84A4OoywAd2Pj_clRmKRZFGr83sBTkC0U2FIlnP8njCL_hP2emBW3k53tMXkvoJXUCo8IIdmt-Y30QhA0JhMYkbCSaVeLmee_y0W-2zP-nhB1ZF_oIONIyUDY3pEFutkNzow8WFb5w3robQ7Jvwh8WQYPWxnwqSUWueG9XuhAYrDCn5OiQ6QXi7m6aJqJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/naya_foriraq/90975" target="_blank">📅 15:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3327b4315b.mp4?token=uJDUFKCL58NGMN_DnvuJCw7GanGVjUIjaS6L6lVm1KVpYqM2nrIJ15QVXKqLqNRv8QPRQhHYfMIBj0KCiP6Ocfea18aprQN8BMOiJirRm73xySVi36DSwTB_NkjYzA5hgI-ELAbrieYT2oo775ZCJHIrLHfwRj-UO7-mlpTBOzgCbwpL9jq5b1J9DNOFDq4KQp4qMcR8wLK7K76dA3atNxyD2mfJGpsw_Vgbn2u4wrRTqIgY-9-PZOQHH_JkwYq1pzIO5eOdlo3pyZ27jwfLze7vhg1QgzdjGDX4u4zj6JK3Te8ne-dT1IHuVdp847-jGVGzE2gyjUfgmX8qR7zcvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3327b4315b.mp4?token=uJDUFKCL58NGMN_DnvuJCw7GanGVjUIjaS6L6lVm1KVpYqM2nrIJ15QVXKqLqNRv8QPRQhHYfMIBj0KCiP6Ocfea18aprQN8BMOiJirRm73xySVi36DSwTB_NkjYzA5hgI-ELAbrieYT2oo775ZCJHIrLHfwRj-UO7-mlpTBOzgCbwpL9jq5b1J9DNOFDq4KQp4qMcR8wLK7K76dA3atNxyD2mfJGpsw_Vgbn2u4wrRTqIgY-9-PZOQHH_JkwYq1pzIO5eOdlo3pyZ27jwfLze7vhg1QgzdjGDX4u4zj6JK3Te8ne-dT1IHuVdp847-jGVGzE2gyjUfgmX8qR7zcvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/naya_foriraq/90974" target="_blank">📅 15:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0c282f20.mp4?token=Li5CDY5We3kF6NofE0RFo_Njx7kBZ9O71HGcNdDdyp9UXDJVVVK_03R6yAzcEVwh30LeEWpkB8AzToHZHN3kxTZcOCP8kyl8lLpN8OfcG0PEkv7w6G2cbHpbDO-rKfWEBumfE807WinxrgRLYsIZRH8A0_26I81AOReOkdnSTs3AaKixGYWsI-dCx2GpyXnoYHj52Gh4dm1nkEYTa7XbeHn9jLGCwv5jiSKzaal1CtUmZLwKV7UVx4Hi5JilRdmN94F978j2yQoClRrZbJrGraCkqnIiRYsLHo9t0QhGEF719lpysRXapPYIUQ527U_VEMEHQePY1k2ZqbSGkh_T6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0c282f20.mp4?token=Li5CDY5We3kF6NofE0RFo_Njx7kBZ9O71HGcNdDdyp9UXDJVVVK_03R6yAzcEVwh30LeEWpkB8AzToHZHN3kxTZcOCP8kyl8lLpN8OfcG0PEkv7w6G2cbHpbDO-rKfWEBumfE807WinxrgRLYsIZRH8A0_26I81AOReOkdnSTs3AaKixGYWsI-dCx2GpyXnoYHj52Gh4dm1nkEYTa7XbeHn9jLGCwv5jiSKzaal1CtUmZLwKV7UVx4Hi5JilRdmN94F978j2yQoClRrZbJrGraCkqnIiRYsLHo9t0QhGEF719lpysRXapPYIUQ527U_VEMEHQePY1k2ZqbSGkh_T6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/naya_foriraq/90973" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02deb34747.mp4?token=kvrbWAfMRiXDYLx-Hs573uqLA9PaxUkjdFnlV0vuqbm5ockhSPcpjdfRo8-w3o1gFI2LXMI-OilPvCvLy_ATIpkC58iInGkrNV1vgUYP1qRlJpnWotBFih1tdL4z-4gkd_q6C0gH5eUNEbY0LHPSnCUtFhf1qvvShxruvh69wKStjFU8Q14KBls0Do3CgeE6mxUOL4ymugLsOGeLEBZKZUQ-VaipiSUefgLVnzsaotYpGrmTltmzqKPTfl96SwXFsPo1DfrR-RWhCm8XH8lOfdmV3zNcdZnM9UVDkJO0qI8mBn1CIX5Sjxf4n6mKRIJR763BkkqvBUCnqqthKJMaDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02deb34747.mp4?token=kvrbWAfMRiXDYLx-Hs573uqLA9PaxUkjdFnlV0vuqbm5ockhSPcpjdfRo8-w3o1gFI2LXMI-OilPvCvLy_ATIpkC58iInGkrNV1vgUYP1qRlJpnWotBFih1tdL4z-4gkd_q6C0gH5eUNEbY0LHPSnCUtFhf1qvvShxruvh69wKStjFU8Q14KBls0Do3CgeE6mxUOL4ymugLsOGeLEBZKZUQ-VaipiSUefgLVnzsaotYpGrmTltmzqKPTfl96SwXFsPo1DfrR-RWhCm8XH8lOfdmV3zNcdZnM9UVDkJO0qI8mBn1CIX5Sjxf4n6mKRIJR763BkkqvBUCnqqthKJMaDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اثار الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/naya_foriraq/90972" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e0763727.mp4?token=b85uRXcnVnHnI3-rgtj1UMLe0B-s0uOTxF1MzPUxq9j8FW9v-FvVhJwoS5rp-D4-ymDbBfLRG5kNhideKj8WbDK4_TPdhHsHn2N7PTXYcZtPRHr8LZ0950ZyZLLyMbkoG7TYMzTBOYsnZlnen3yefIbpRWM8lrZDO7THuAE2G1paKKVBfT-1Vpuj3kzaSb7G1_4oMFtA_gJ9aYWOMYTUWGc-aFrpSOSGcmQG2_CwCfUTCFTvMO2yKraYsjFHS_bLxQKrClv5fZefheVne-A08fxPl0TK86Ebg6Gq0kJMi_QCNHQHmZ-woMCMLzhxQ5o3UPvCBCHz6yzzM1yD1x9M0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e0763727.mp4?token=b85uRXcnVnHnI3-rgtj1UMLe0B-s0uOTxF1MzPUxq9j8FW9v-FvVhJwoS5rp-D4-ymDbBfLRG5kNhideKj8WbDK4_TPdhHsHn2N7PTXYcZtPRHr8LZ0950ZyZLLyMbkoG7TYMzTBOYsnZlnen3yefIbpRWM8lrZDO7THuAE2G1paKKVBfT-1Vpuj3kzaSb7G1_4oMFtA_gJ9aYWOMYTUWGc-aFrpSOSGcmQG2_CwCfUTCFTvMO2yKraYsjFHS_bLxQKrClv5fZefheVne-A08fxPl0TK86Ebg6Gq0kJMi_QCNHQHmZ-woMCMLzhxQ5o3UPvCBCHz6yzzM1yD1x9M0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج المدرجين 15L و15R في مطار الرياض الدولي عن الخدمة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/naya_foriraq/90971" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مشاهد حصرية لنايا من الرياض   حرائق وأعمدة الدخان مستمرة من مطار الرياض الدولي …   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/naya_foriraq/90970" target="_blank">📅 15:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84e1ee9a7.mp4?token=WcLbhej9tv6Hk-zmnn5GQCKzIfEiLgXcwSCTry5Xaw8ckieZ50zJ3XxAULi7QWhUM10zdnBt9t_DamHmZc2uoyVrxame779GuM2CFmem76O0hHUTDi1ab8YnqHD3NotGr8fOSFI772iFk6QrTDBSnm7ss8T385VD5HuI1nf31aB7Mz-BGET0MZtD-UB_UbyloZmlA_9AdIZq2j9IUXWtkGSv-tHec_jRiCJn-2RH_1AlMxAcj4kyZmofmWHg6iH2ca2wq_8JLDcQOIYbC4vkL76KCC89RZog3ipU5zOL_B2oOI7-bcacovtEppFYQGnKZSTJGu3AHTdPBYimmMy1QgE_9HPpvj_S3wa7Ktp83bYBDNrL63rj9fttEDW9u25F4rs8Ix2ulY-NVXDTL4JuBz4xTy1HgagM9FQ672PIPYeVghfmxS8giiChUMIEhvP4qesNfa4XqfYQufcM9ApLFBLMjBoV_zGZt8WvWsAP67BTecZPlEAGEkNtTINWUZtzbEo41hUzBuemAUe54Awo5mtAF2M5_cevcIFxILIat9jFXa714qZVQTTYl2jyrlF2nX40YGGv5yCn4R6_F9NZNTFYcZH8F6p-Ki8hx-WWFdBZnC6K8s7cXKjBsEGUloT5_zGJoA1z5bZ1fAHCBLY1ekdlnh8RBbCU8ehNgoL4GRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84e1ee9a7.mp4?token=WcLbhej9tv6Hk-zmnn5GQCKzIfEiLgXcwSCTry5Xaw8ckieZ50zJ3XxAULi7QWhUM10zdnBt9t_DamHmZc2uoyVrxame779GuM2CFmem76O0hHUTDi1ab8YnqHD3NotGr8fOSFI772iFk6QrTDBSnm7ss8T385VD5HuI1nf31aB7Mz-BGET0MZtD-UB_UbyloZmlA_9AdIZq2j9IUXWtkGSv-tHec_jRiCJn-2RH_1AlMxAcj4kyZmofmWHg6iH2ca2wq_8JLDcQOIYbC4vkL76KCC89RZog3ipU5zOL_B2oOI7-bcacovtEppFYQGnKZSTJGu3AHTdPBYimmMy1QgE_9HPpvj_S3wa7Ktp83bYBDNrL63rj9fttEDW9u25F4rs8Ix2ulY-NVXDTL4JuBz4xTy1HgagM9FQ672PIPYeVghfmxS8giiChUMIEhvP4qesNfa4XqfYQufcM9ApLFBLMjBoV_zGZt8WvWsAP67BTecZPlEAGEkNtTINWUZtzbEo41hUzBuemAUe54Awo5mtAF2M5_cevcIFxILIat9jFXa714qZVQTTYl2jyrlF2nX40YGGv5yCn4R6_F9NZNTFYcZH8F6p-Ki8hx-WWFdBZnC6K8s7cXKjBsEGUloT5_zGJoA1z5bZ1fAHCBLY1ekdlnh8RBbCU8ehNgoL4GRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توثق فشل الدفاعات السعودية بالتصدي للهجمات اليمنية في العاصمة الرياض   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/naya_foriraq/90969" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/naya_foriraq/90968" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14d4220bd.mp4?token=RWe9Lq1CqbXaMOZ80zdhoUnVh5oqcJ1GUFuG7cFgILU6tMy20-7fGsL2L6D0wjv4YgKVOg5_3wbXe4hz2xszbQBrg9yymE9CjIBM3REO5ebO4OiFL8j4BjQSJBdosan2KFZDS1_PUxLlm6tRaEJt3B01-oK4ouzj-_8OLwV5rtQf5j9cSe_-R_w9GQwbm5ZakYlwk0TH7DZHc8fkE3GVHQBa8oMbWsPOJpKQpoPJbh-Ir-y9b36c3yBoq7D2MwlqxjZTt8rgWiuJEuZnvFJkjPT_xQuWDArYSw0m8NNNBJnYBdK-x6d4bBO4sFLdOptwj_UNnz_1ZZmqZw1KOBW7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14d4220bd.mp4?token=RWe9Lq1CqbXaMOZ80zdhoUnVh5oqcJ1GUFuG7cFgILU6tMy20-7fGsL2L6D0wjv4YgKVOg5_3wbXe4hz2xszbQBrg9yymE9CjIBM3REO5ebO4OiFL8j4BjQSJBdosan2KFZDS1_PUxLlm6tRaEJt3B01-oK4ouzj-_8OLwV5rtQf5j9cSe_-R_w9GQwbm5ZakYlwk0TH7DZHc8fkE3GVHQBa8oMbWsPOJpKQpoPJbh-Ir-y9b36c3yBoq7D2MwlqxjZTt8rgWiuJEuZnvFJkjPT_xQuWDArYSw0m8NNNBJnYBdK-x6d4bBO4sFLdOptwj_UNnz_1ZZmqZw1KOBW7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق لحظة الهجوم اليمني وفشل الدفاعات السعودية بالتصدي له  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/naya_foriraq/90967" target="_blank">📅 14:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf1563a0f.mp4?token=TamK7rDFRi5fQ88lIOJY86STqP_NamqGF2Tj1dVfHaQEeJzO1jVhzav517W3LXf-zgHYged4VBKqOB8VMEI19d5yaEVdInWoU0pj09CMHUg76xJhY-FZA5qQ9s2je4asT7bf1945oNLmqAUyqtSuaQV3IrQOjePKZ0YUHyn6v4zgv_g8kKmNQU8meoj9YMAQ-fr7aYe43a0KqCmjvxY8v1fjHQBWH_Ka3ziqmgCto42cSjyyMPRW1VryIR_Uf1JebL7mKv6ZyAmhQGDqSlWXnkZNG_thzaGQhCbRvLQ_hvwgonBToerh8ehhcOZkBoD47kjCq4NEx39ZP593PEzGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf1563a0f.mp4?token=TamK7rDFRi5fQ88lIOJY86STqP_NamqGF2Tj1dVfHaQEeJzO1jVhzav517W3LXf-zgHYged4VBKqOB8VMEI19d5yaEVdInWoU0pj09CMHUg76xJhY-FZA5qQ9s2je4asT7bf1945oNLmqAUyqtSuaQV3IrQOjePKZ0YUHyn6v4zgv_g8kKmNQU8meoj9YMAQ-fr7aYe43a0KqCmjvxY8v1fjHQBWH_Ka3ziqmgCto42cSjyyMPRW1VryIR_Uf1JebL7mKv6ZyAmhQGDqSlWXnkZNG_thzaGQhCbRvLQ_hvwgonBToerh8ehhcOZkBoD47kjCq4NEx39ZP593PEzGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق و انفجارات قرب مخزن شركة سفاري الان داخل مطار الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/naya_foriraq/90966" target="_blank">📅 14:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsmcGh38qzZ64VumrtmA71w3nXrbnHW1kFAHkeOwVFRN04ZCu9eOfhwYQXQArKId7ytiv_YCa2t_-xZVFjLIAIQmpCfWBLol7hN60Hslzo1is-vlXosOvITo3-qNIGNxiPT_8-lC48l6fmx98jjHJVzAXYtp7Jz4Z5G4gX8RZLUAQmw7h1sJelAdREgZwFSVyXi9OVS1u8MrT1KSae3FFdNby22sNjwFcBz5-FcC9YVqhxfaUxm-eXOqK1rE4PC29e150Wdt30MVWVTpC5HMevGB_NL0Ufu77hsUO_Whv0PCYKK8uEJNIk4vDFsA9eo7COqKIWPNSnmcfwEzfbNvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرياض تحترق  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/naya_foriraq/90965" target="_blank">📅 14:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90964">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef5be52b2.mp4?token=og3OxcTRmM3jm3TelwjLJmWk6OymBoGJZrCcL_wFAdP0J87Ml2g0yvE9FarzcJwlwzQO1zGHzBOZLVdc04Di-fG8_0KZiwuNXun4jryHp54tRslB4PG0sNCEy_uz4N9X-rvyji8F-byWsVwiasGK24fp9NT7Dz8LeWVztbuVCtrs-f0HSd8oBTfsqyW27QF3wS8VQVH81LR0duZnjm1TU6NQv5Zlc2R83s2ThZH0u0yWDgPR1Lj4gx0Bw8CjglZkSkGGfeBEyZ1vLtvqRa78WOzmFWJujYU3W30KJsb1x3cK64XXM2A9ZygVyiVssRN-vFETK5Qexl_-fQaOwUK9amvEKI2Z58lWFJ3OHyuArkhF8k75PKfN3B3fPiMNCjIe7W7mDPD7W0FAjupggJhnGOs8gU2GGPoU1UBmgexB18mPBiYb9fZD05Dx8gvfD_Tnd6oc8Bd1Zow-Nzls-5RTvCIvqM7a7K6_XYnLbHyLTAyCf81lw-5rdKkkB-aMHpzQ8nVrOx5wkQ3mYEay4tfLn0YdEoTGpwFHIKgX2MMRpZzPweklkrdTBLw03vwQHDTLFy8RSToZ0BqP1FsrMWImqYcbnsNrLPLgTWWVAjnh0fI79rjPmq7MAxd-q6uQyqde2pmE7vqsjFkKD4JhpFdvzVVZNAuJt5XvcQsrfIxZ4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef5be52b2.mp4?token=og3OxcTRmM3jm3TelwjLJmWk6OymBoGJZrCcL_wFAdP0J87Ml2g0yvE9FarzcJwlwzQO1zGHzBOZLVdc04Di-fG8_0KZiwuNXun4jryHp54tRslB4PG0sNCEy_uz4N9X-rvyji8F-byWsVwiasGK24fp9NT7Dz8LeWVztbuVCtrs-f0HSd8oBTfsqyW27QF3wS8VQVH81LR0duZnjm1TU6NQv5Zlc2R83s2ThZH0u0yWDgPR1Lj4gx0Bw8CjglZkSkGGfeBEyZ1vLtvqRa78WOzmFWJujYU3W30KJsb1x3cK64XXM2A9ZygVyiVssRN-vFETK5Qexl_-fQaOwUK9amvEKI2Z58lWFJ3OHyuArkhF8k75PKfN3B3fPiMNCjIe7W7mDPD7W0FAjupggJhnGOs8gU2GGPoU1UBmgexB18mPBiYb9fZD05Dx8gvfD_Tnd6oc8Bd1Zow-Nzls-5RTvCIvqM7a7K6_XYnLbHyLTAyCf81lw-5rdKkkB-aMHpzQ8nVrOx5wkQ3mYEay4tfLn0YdEoTGpwFHIKgX2MMRpZzPweklkrdTBLw03vwQHDTLFy8RSToZ0BqP1FsrMWImqYcbnsNrLPLgTWWVAjnh0fI79rjPmq7MAxd-q6uQyqde2pmE7vqsjFkKD4JhpFdvzVVZNAuJt5XvcQsrfIxZ4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من العاصمة السعودية الرياض بعد هجوم للقوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/90964" target="_blank">📅 14:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90962">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصدر محلي سعودي لنايا
بناية تابعة لشركات النقل اللوجستية قرب DHL ؛ تعرضت لدمار شامل داخل مطار الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/90962" target="_blank">📅 14:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اعمدة الدخان تتصاعد من العاصمة السعودية الرياض بعد هجوم للقوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/90961" target="_blank">📅 14:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ce0ef0c5.mp4?token=I3RI3rPl3UOzM6U9O1EzI5SclhByY4OT6uBEsBYusYceFJsfqhAVZ-lOF4P_kFo_ClSunYDFjcUswpNxdRtCjp2GK1inXSjubDt6oURd92TF7vp6TGrZNtpeTcZ_JAa6u-m2AQ7eEFRTjUl4Vqu5kYnUe2x33EKQ4C3HoTusmPhcP0GogSVIgORrvDZLDNYvuyGoBGaCGcPdaoaBeBa_mZHafC54zpyjh35PTvtt0vRlxUwq0Wfl1J5w2GD046SoY8K4Zxv2D9aO5OzYRQqCv-1-lfjgbIiykE7XxxtZtUMdlJwE7zlV5pJMj9MLa021L75pDzS_gCSDr5mD9WDNoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ce0ef0c5.mp4?token=I3RI3rPl3UOzM6U9O1EzI5SclhByY4OT6uBEsBYusYceFJsfqhAVZ-lOF4P_kFo_ClSunYDFjcUswpNxdRtCjp2GK1inXSjubDt6oURd92TF7vp6TGrZNtpeTcZ_JAa6u-m2AQ7eEFRTjUl4Vqu5kYnUe2x33EKQ4C3HoTusmPhcP0GogSVIgORrvDZLDNYvuyGoBGaCGcPdaoaBeBa_mZHafC54zpyjh35PTvtt0vRlxUwq0Wfl1J5w2GD046SoY8K4Zxv2D9aO5OzYRQqCv-1-lfjgbIiykE7XxxtZtUMdlJwE7zlV5pJMj9MLa021L75pDzS_gCSDr5mD9WDNoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرياض تشتعل   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/naya_foriraq/90960" target="_blank">📅 14:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90959">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnrX0APqH_YIoBnA2W2s3m5hfpI0Ep8yJolpA4AoIyUxULwyVC3x9ZcD5yFT-O7_Dc0NP9b_0SrCmmH3vI0gZJ0h5GhbuuqUOO0WG4vRVEqWC_gegFO9xPiemF8-HtntWH4n2u5GQ0Rtf6nfIZzkdH02mp6yqz5cysIzCEGcttQaGmhDohPAzh2xOQdZoh2vtsFsy92UE8Juh2o7kYFBKYz43s-MJK7wn_S3Mvm9KVLipE2RLxVn3QkW9rTwmt6tB17fHjk-xZFdszW9jYhVVupfPrUfE4cIYQSMZH8qrWfemnHlrc17G9I9JYwzt5q1DwnHob3EDL1DBtBRNQJ0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/naya_foriraq/90959" target="_blank">📅 14:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90958">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy_1zw2NyyLR7wiFITVfnAl-1B7HafVVFdi4SijKTC09bhBve9vCm72ih7EAF5MYF1w_jDDkYZ29BCtHSDpwYJ05t5APvgX_0IuouYW6TkQDFWMNjHhhQYG07z7EB8TfVFBpE_dpYNSi4qoMTPh3gMfQELUCkS-A_Bgjds3AI1GmAsluIrjDEpvRTB5SCvWrz8O9Re_j6e2JAR3aqmFqm-TWyNVwUjZhkvwPUtwo7bACtMC5JyDrY6PiY1Uvm8TI_wXCGBY9ofPSKJVpdY9TIEjKmr1E9AeRnIxMT_n9sKrzMPRtX01LrpGoVVqT4YlyQPztZ2R8z-oasPm1enRoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/naya_foriraq/90958" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWIWTCvEwemqCQm7ulh-mz3LzlCB-b6Ey9wEOsWwKr5G6EH_mOhedZPeupxvLIxsWWGKcEuHKOcm89H386QQLjNaw2vNbxUbZod05N60HfjYXLAqSgYWsSguSKIl0dGa1jqeSDQBvJLyYRpvgkPW8kGcFDKETwRQawijvk4t1uDUzAwTQMdgqrWiLelJ5bisTiEgqQBChsQtIIX-Khinz976dTvYDNcrpJqZM9aA62RQ0vrBMq_CgOBa3hUfanFQG-CcPrMoS6SAIUsjyjnHJdU7bSK6WaqvoG2_zadOMhocBV4A3fR-2gkjSrlMZvzBPYjModY7pIF1fxkJ2AF1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران قرب مطار الرياض الدولي قبل لحظات   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/naya_foriraq/90957" target="_blank">📅 14:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HE-UOckmuFghY_BphlgvQIn_WvnIJkHp3kv1wFWDRDlrr2ILvMBERzFSBex55RIhT3cV2KrUJT2p3JqnwzlmVE-S22QkZXZ0ABsb9D-AgFy-LdB-08Gk7LyQRKfmFVKbaj_SyH4W35GQ4qQ-krV0oEUGeAY57EOHSVnx_NfpECdz-5rE4I2szUNlrKS0KKo-fYWS9VoY3qucrigmYQVV72onndTojKdNV3J7Js_AiQub0iztI77cY8dMs57OPWzdGSz_eXY2pdR7v0o2fNB2SDhWuTJ3Vizu9tsLOIMqUKGOoPSJoAZWkt5GjAW7e5YqyyHwMOdWJfkKbprnSlOzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان تجدد الانفجارات قرب مطار الرياض</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/90956" target="_blank">📅 14:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFqdMUfjuWErc8j8CzrLoF26vXJL4UYWTvJeL1IP1IjKefAb3H965OKXHPnZY6oR0HShQKQjmA0wYINWw3vUqNhDWSHMYvs5Kl3c3sdjR2KIv_P8NlyHWO2V4-LSJ5e3n_-l0mQHaONu0x30Iz5vrmO-Qll-pdNby8xqU5rCsryxJttmNUr36dhyjaxbCNGQ84Yqm1lU4Nu21lXkR8Scr_DznHtcQreF7XH8krgRd6ekOLh9mgL5h3T6zLMeZA-WzbM4u4pTQTHszbi8DxpkpZowylXljLCdKR-bfEC9jpDE7HbQHyWL4HtP1zBoPunft-KV8InBvRjugHPOzuiSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رويترز : رصد ألسنة لهب وسحابة كبيرة من الدخان الأسود ترتفع بالقرب من مطار الملك خالد الدولي في الرياض ..</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/90955" target="_blank">📅 14:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90954">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رويترز : رصد ألسنة لهب وسحابة كبيرة من الدخان الأسود ترتفع بالقرب من مطار الملك خالد الدولي في الرياض ..</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/90954" target="_blank">📅 14:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رويترز : رصد ألسنة لهب وسحابة كبيرة من الدخان الأسود ترتفع بالقرب من مطار الملك خالد الدولي في الرياض ..</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/90953" target="_blank">📅 14:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزير الخارجية الباكستاني ييحث مع نظيره الإيراني عباس عراقجي حماية منشأت الطاقة السعودية</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/90952" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
السفير الأميركي لدى الكيان مايك هاكابي:
يوجد علاقات عسكرية واستخباراتية ممتازة بين السعودية وإسرائيل وهذا سيكون مفيدا في تقارب أكبر وصولا لدخول السعودية باتفاقات أبراهام.</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/90951" target="_blank">📅 13:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IylQJ-WLaVAZcWKjM9Yad13U36s-py55228ma5lWFNGLDPVSLOIWkePEUQggOTcAzV2gdIREfNymioYRIGYmA89SDLjzgSybh3UiYvC852twRiJfPa4Ik0Gn-uJppKJswQDWC2akfwzYM4mjB_rTCsmGwJcjzsrmwM__Rwl64X0FhXkxUIjOvGm-Ue9mcFKNp8zoAs4oAzqMXsjhtAHPVW-so1Gjx5FLH4-o1QDuJMf0DulBd2vgyCjpG6elkF-EZp6n4AdH45uIzDldDazcHumZHt1z60iDrIUPjGcSSF3rV6cnyG5Jlhg-pUqjzFADwAF971OnHtfl3R919W4Jeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcIq1xS0TD848Q482lRFiykL9eEwX6k4dTDPtoSAzI_7nKk4LVtLI_tyr7D2e2KAeIv0V3HT4OoNIvIFGupmANu5ws9bExbmtb7LTWq_SsxyJ6MNKGF3FWS8x_Xouy2onz6V8WFE8Van0yo-NNmORmxxvYPrCimiohEh3L0QD57tRdCsDqmSkcmFyGKJCqcbRoN-im-QgybyXu7ZgW00rPfKswoAFtdTRinrv_onXIUKIk7frep1wFxhp0LA2qXZuIlQHvvXuTge2sjSevsFwJM7vYOHHiRtUiMb-bBcPQ_2ehEzmjiC7WXhEhpXRSQlrPBnrModRaM8Nb6qHGMRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5jo2fffGevFdBbu6TD-qZopahxQbF4HYfgZ2HuPxrIWOFTI6lLe99uqVVcA5mwDvVZE-LiTvA986-GAo1Y-UqcK2QIt_HDFFXDVYiqc0r_5eK8h8_ypXBnxr31jXU49jvgCrjhqOwBn8mkZ9ABVdoVBjU2fiqLl0sPJrbIQ-LjiNsKBJV5mVjP5OijuuS9vyn0XnoXjtyXlnIfePEqpdnWT1tNDs948AzKeNZSgesNrhsNNjvqmYT02JBYHqddh3bFJ8oG8tLxpaU8l555tU-lTKteeS7vmFGbKXMFJvFDCmuaRfo4G_-hyPJrGgdalrqKodaZkqpxJFTACjU8KDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇷🇺
🇮🇶
موسكو تنتخب من بغداد
شاركت السفارة الروسية بالعاصمة العراقية بغداد في عملية اقتراع وانتخاب أعضاء مجلس الدوما الروسي ؛ كما وجّهت روسيا لأول مرة لجمهورية العراق المشاركة بصفة مراقب دولي من خلال تواجد المفوضية العليا للانتخابات  العراقية وعدد من الشخصيات الرسمية ..</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/90948" target="_blank">📅 13:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90947">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
🇮🇶
مسؤول أمريكي:
واشنطن لن تترك أي سلاح خلفها بالعراق بعد الانسحاب.
‏ترامب وجّه بعدم تكرار ما حدث في أفغانستان خلال الانسحاب من العراق.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90947" target="_blank">📅 12:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K77xayuQqFD-f979994q4DquWl4BoXHvMOKTkLuAmcQsaQyNnv442qDI_zy4m4lQViIs7pZtohfKJmmyOWlvFWaatfWTAPHXr2U9A2lUUy5_yDnFJdlqv9AZVjK-biQ-vWCC2gWv5VUnvtu8ajZWXPUh2sctEFcU_qURbgQHqdp_LlTHOAIArPuQg_4LZkEblByHqNw_A_IoeGr-R8B3JRTLmUZeQazEh1HibxV-uJlHc6HmdWZ3q0t2XMjGDwMGX2DR5jfdhBG5iNq1mtdTID51tVuisdGm5NClrkvKXjNQ7MQmw1Pq4eCKsENRrwPapI8widyBvSM3t3aZo8VmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/90945" target="_blank">📅 12:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
🇮🇶
وزارة الداخلية الإيرانية:
نقيم علاقات ممتازة مع جميع الدول المجاورة، بما في ذلك جارتنا الشقيقة والصديقة العراق؛ فقد توصلنا إلى تفاهمات بشأن قضايا الحدود ونشهد تفاعلاً إيجابياً مع الحكومة الجديدة، ولذا ليس لدينا أي مخاوف في هذا الصدد.
العراق دولة مستقلة. ويسعى خصومنا باستمرار لاختلاق الذرائع؛ فتارةً يزعمون أن إيران تقوم بأفعال معينة داخل العراق، وتارةً أخرى يركزون على الانتصارات الباهرة التي يحققها الشعب اليمني.
إن تعاملنا مع العراق إيجابي للغاية؛ حيث تعقد وزارة الداخلية ومحافظو المناطق الحدودية اجتماعات دورية، ولا يساورنا أي قلق بشأن تهديدات قد تنطلق من الأراضي العراقية.
كما أننا نحافظ على علاقات ودية وتعاون جيد مع إقليم كردستان، رغم أن إيران لا تتهاون أبداً عندما يتعلق الأمر بضمان أمنها أو الرد على أي تهديد يستهدفها.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90944" target="_blank">📅 11:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90943">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3fefb345.mp4?token=WRL6WvAIq_MMA3Xd9Rpl8ow6goyhP-YQyiH1FGFRroN9toygM0wpCi2HEBRwgRVpW3jB4lVRajD8jdu3mXyZ_EKDwWy4CvmVC-HrOXFjKP31zePkJ2aHnb5HKtZFZAb18v_FPqGupnHWN_nAWo1hMwEbx2cu_X2Vi_KB8XleJ4NqNt_Ek9wCS-jkMSzN0Ax0I5tGl8PmMu0VMqcGvBY8zpvErDXAOxjcic2IqslHv4MF4sTJ38tOHD_7t0w7e2F0tANMByQVt0z3N_1BCBC3qBl9loBg22LWX3utD9fppC1jS0T3OJKPKMNTkqaXUhOmPtuJ21QzqF-reFsP2wD4Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3fefb345.mp4?token=WRL6WvAIq_MMA3Xd9Rpl8ow6goyhP-YQyiH1FGFRroN9toygM0wpCi2HEBRwgRVpW3jB4lVRajD8jdu3mXyZ_EKDwWy4CvmVC-HrOXFjKP31zePkJ2aHnb5HKtZFZAb18v_FPqGupnHWN_nAWo1hMwEbx2cu_X2Vi_KB8XleJ4NqNt_Ek9wCS-jkMSzN0Ax0I5tGl8PmMu0VMqcGvBY8zpvErDXAOxjcic2IqslHv4MF4sTJ38tOHD_7t0w7e2F0tANMByQVt0z3N_1BCBC3qBl9loBg22LWX3utD9fppC1jS0T3OJKPKMNTkqaXUhOmPtuJ21QzqF-reFsP2wD4Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
أعمدة الدخان التي رصدت شمال العاصمة الإيرانية طهران ناتجة عن حريق داخل أحد المطاعم ولايوجد أي حدث أمني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90943" target="_blank">📅 10:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
🇷🇺
مسؤول بالناتو:
روسيا شنت هجمات سيبرانية وانتهاكات للمجال الجوي طالت العديد من حلفاء الحلف.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90942" target="_blank">📅 10:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90941">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇷🇺
الدب الروسي يداعب اوروبا
أوقفت مطار لوكسمبورغ الرحلات الجوية في وقت متأخر من يوم الجمعة بعد ورود تقارير عن نشاط طائرات بدون طيار غير معروفة بالقرب من المطار، مما اضطرت الطائرات القادمة إلى التوقف أو تغيير مسارها.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/90941" target="_blank">📅 01:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90940">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0kAfYB4DLIF1avv0NqXy_svRATkMRm9t_a2y_KZiC3_E8sU9-RERpFSRlzxUe2_u9R2rlux--kU1Bf2vzIweUwGmDvmKsdrVWmUrEyNOT_jOM25FibZfhJVg2JrK0ncumwWozGGY7s48cCFwxXSS8-KT5KXBONriuMQ7emKg9G4v0mWeGL1RKaPudsTRdhBEe5v8bxoTdMBFSLDNLCdMVZV5Wqpe35wwnBTyZU0HXYOOXoQcoFZheft52_TJM5reI0xrCilISHFs8GnHLz_2iINBrJnS-bjW4tlnd0vWU9TwKmvHkbCywokY1URhFoQmDgMy1ZUxlQbmbQNWjrvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محافظة فرسان تحت القصف</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/90940" target="_blank">📅 01:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90939">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90939" target="_blank">📅 01:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90938">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90938" target="_blank">📅 01:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90937">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب يوقع قانون العقوبات على روسيا.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/90937" target="_blank">📅 01:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90936">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKLC2M4nRk_OX4Du6tlskU_JaYn_s8yeXKdls0RXtDoUumaYkMunP-g2fnGqf9OERWaHYF1kWPPd7ZDJPIltwcGxt5MhPmOtuQEtEkNNV0w8XMulfLaGJTZ27N1Nue8m0bQq7qrLaPao9aplm_1Gr7AE8zUj9Onk9uxJ537pRrK8W9DJGM1mvgMVWyOpyH9XsgWvOXL10w-E-85Ri4NKvO8a1A7qHKouJyFk9bzZjvIW5zMR04e4oDo-pR5srAWn37fE00tB6Phb0yQx6roMEPrHn088cHGXhdmn2PcQZwV_AzAsDQ9LdDU44hu4ncdPyFGDrz99yWn5MRzAabwJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
يسعدني أن أعلن أن الولايات المتحدة الأمريكية قد أبرمت اتفاقية مع مملكة الدنمارك وغرينلاند، تمنح الولايات المتحدة سيطرة دائمة على الأمن وجميع الاحتياجات الأخرى في غرينلاند، مما يعالج بشكل كامل جميع مخاوفنا العديدة في الولايات المتحدة.
لن تكون هناك أي تكلفة للولايات المتحدة. بناءً على توجيهاتي، عملنا مع ممثلين عن الدنمارك وغرينلاند لضمان أن الولايات المتحدة ستحظى إلى الأبد بالقدرة الكاملة على فعل ما هو ضروري في غرينلاند من أجل تأمين وحماية أمن غرينلاند والولايات المتحدة الأمريكية.
بالإضافة إلى ذلك، اعتبارًا من الآن فصاعدًا، لا يمكن لأي خصم للولايات المتحدة أن يمتلك أبدًا قاعدة في غرينلاند، أو أن يكون له وجود عسكري في غرينلاند، أو أن يقوم باستثمارات حساسة في غرينلاند، دون موافقتنا الكتابية الصريحة.
هذه "اتفاقية مدى الحياة"، ولا يوجد لها نهاية. نحن فخورون ومسرورون بما حدث للتو، وكل ما تم الاتفاق عليه اليوم سيحظى بتقدير الشعب الأمريكي. سنبدأ على الفور عملية تطوير وجود عسكري كبير في الجزء المناسب من غرينلاند، وهناك العديد من هذه الأجزاء.
سنعمل مع شعب غرينلاند في تطويرها وبنائها. هذا الحل هو حل رائع للولايات المتحدة الأمريكية والدنمارك وغرينلاند وجميع حلفائنا. نتطلع إلى العمل مع الشعب الرائع في الدنمارك وغرينلاند نحو مستقبل عظيم فيما يتعلق بهذه المنطقة الكبيرة والاستراتيجية للغاية.
سنحرص عليها بشدة. هذا حلم يتحقق للولايات المتحدة الأمريكية، وهو حلم مهم وتاريخي وخصوصي. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90936" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90935">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام أمريكي:  ستة مسؤولين أمريكيين مطلعين على بيانات الخسائر الداخلية، فإن عدد أفراد الخدمة الأمريكية الذين لقوا حتفهم خلال الحرب الإيرانية يفوق ما كشف عنه البنتاغون علنًا.  ‏أفاد خمسة من المسؤولين بمقتل ما لا يقل عن 22 عسكريًا أمريكيًا منذ بدء النزاع…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90935" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5qGg3F3HGFSmO-EEnjZk1l0I25ubGWITRu0E-rtNRjSKKBpn3Lf6GSiBX6jDxzGMIhe_TESL58ShbswvgmSIsxKiUWopjTdCWseLkKIq-b_Nws_MtFygigLkY8_iZgGuTR60ocpRk6uOv1NLnh_llz8tm7gqni9655NgwAURxbDxLryWbJvgce0Y2P9IM8G1Be6PZA-wkWcuf1fFJjHVrCaFveGDbpLhxMAmgfevg695gn6JlGBQ19MYK2E_6MvZOaCOcvm7s12y9hfrWwhSTZxcZCdCAjg04JSfeQLpGQXr7pGvGiqyNA7QgIX5-gsw2G0RDKbCnAgnMKm5fF2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Scp9totiYqBGov_SmUwYcKIRJ1XvuFOmHWc9nv8KclM5QFs0YJdRSDcoZe4Ypi7NEyKeyUEp1xmAixNBjwNgYDxRcR2A1aGoP7i7L8l5pv1fTt6O9lNKvYaD63nVXpQfO2Ky1uhVe6uQVKJownO-qDPmExL7Kh0w2RdyDwjqlj9QK9b5te10NaOCVToFytY4B16-meJVvkaTM01OB9RMNHcxJwrKiBuH26bfcxeor8AdOYtU8OLVbmayacy0TMIKyB1u2VjB0fHG3TAnZI31d7xyjkF1mc0A5u1yDiBRixiDSN-HVOxGn-gQoS8QRygSNxpVZ2EOlYpO0lNaKN-eqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzU0fJrufKwcSNq3ZISr8HdrmXiHN_9-1sD5vmNAvbE3Lb9ODO1EiXPJ7qAn4s-lGP1G4bYQJX6MdIrj604lA_ZW0cs69akqhzxU465rlaW9Oep8COqcp2svz71n6XVaFZJDuaxZsg36j0rD6Vdq1hUtb_4t7SzVJTkSA2vgdcDIj9VN_hc1KHBoxzYAS4lw_tQsoNQCXyyJrCxazJ3qZ_SzpXoQ7o1ZO2NaoBzBiSGzZzxLJA7d7LvTBR1zDZddceqXxrWn-E6PsAtHkeOm5pxjH2T57kNW7YJHEhqtXhr0TgbRJtBej5JjB7lnaDSLwOo2oMOezaqXIDUmnN05OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jz1nSnDN6OqGOkDnPfkyJiLgJKqzL7m2uIQ9isf5OaUbmsqN1WX-57yQiRrooCe34dcSbilr3nThA9Fkd01PCynULlikwQ-sjEJRgUXimIujRqOlGTL9HQ8doGe4NuSuJ3jeee-c4GuMrfQxFzRi5LGwPgEWl7B4Oufb5JAV_xALXhymJjjojLBoLiSzJvDxJUmiDU8_qWOZElMR_OnB7YO_n52smJHmC8zQqVzqB70saURP2dJa0V8F01IH69fBiiZsqfCPK9gxRxhra_gJWJ8Pdny3a7efy2q6jOBETdKKcdpEt-VKMfgNcU6X3snxTH8GQ02neKx-Qpu7XFnAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhjo9-crzIZdsh41ZKIS-ns_BxZRyrXT_Pj6iO_OzVGE7GrbGHgDKj4gEdhrMnxRt2Kd8PYFCrlIkb4YpElo0DZHu7WCFnpy3flGuaBrB3O7T-3mP-OPDW6QjWIO9rV761EJ2b1-GXCpnXEI5AqOhFa9OLH-HVxEePTkaoz5_st3h0MfJDEdkkJExxnOudRoOuuWRn49F6dPKEbsOgqdR9PIm-aqIZzFxfeMYzopgWLm91q8UYCqOetyxqEWBlL8lBQ4jE443q_msZGCveYQVubqsW-aRAJAQk0NIL1gj2q29JN_quR1rVYKw73ivRmbOlBZmqkw4L9dINfyvFD_lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇺🇸
مشاهد جديدة تظهر الدمار الكبير في إحدى القواعد الأمريكية بالكويت جراء الهجمات الصاروخية والطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90930" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">السعودية تفعل منظومة لا تصور " تكفة ، امسح الفديو بسرعة " بعد فشل منظومات الباترويت التي تديرها اليونان و إيطاليا داخل السعودية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90929" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام أمريكي:
ستة مسؤولين أمريكيين مطلعين على بيانات الخسائر الداخلية، فإن عدد أفراد الخدمة الأمريكية الذين لقوا حتفهم خلال الحرب الإيرانية يفوق ما كشف عنه البنتاغون علنًا.
‏أفاد خمسة من المسؤولين بمقتل ما لا يقل عن 22 عسكريًا أمريكيًا منذ بدء النزاع في 28 فبراير/شباط، أي بزيادة أربعة قتلى عن العدد المسجل حاليًا في قاعدة بيانات الخسائر العامة التابعة لوزارة الدفاع الأمريكية (البنتاغون). وقال مسؤول آخر إن العدد الفعلي قد يصل إلى 23 قتيلاً. كما لقي ثلاثة متعاقدين عسكريين أمريكيين في المنطقة حتفهم.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90928" target="_blank">📅 00:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مصدر من الحكومة اليمنية لنايا
رصدنا عمليات هروب جماعي لمرتزقة العدوان السعودي في جبل حبشي بمدينة تعز .</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90927" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خميس مشيط قاعدة الملك خالد تحت رحمة أنصار الله</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90926" target="_blank">📅 23:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90925" target="_blank">📅 23:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات في العلا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90924" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">أنصار الله تضرب ب ٦ مواقع مختلفة في وقت واحد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90923" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الهجوم هو الأكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90922" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90921" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90920" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90919" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سيدفع اخوة نوره الثمن غالياً</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90918" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صنعاء بعيدة الرياض اقرب</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90917" target="_blank">📅 23:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90916" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/90916" target="_blank">📅 23:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90915" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز ينبع</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90914" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات في جدة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90913" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90912" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90911" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">العزة لأهل الإيمان والذلة لمن طغى وتجبّر وظلم.
عزت برای اهل ایمان، و ذلت برای کسی که طغیان و سرکشی کرده و ظلم ورزیده است.
Honor and dignity belong to the people of faith, and humiliation to those who transgress, oppress, and act with tyranny.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90910" target="_blank">📅 23:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
ترامب: سنرى ما إذا كان سيتم تدمير إيران.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90909" target="_blank">📅 23:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
ترامب: أنا فخور بالإعلان عن أنني، اعتبارًا من الآن، أحظر على شبكة "سي إن إن" الإخبارية (المعروفة بنشر الأخبار الكاذبة)، و"إم إس إن أو" (التي غيرت اسمها مؤخرًا من "إم إس بي سي" بسبب قلة المشاهدين والمصداقية)، و"بوليتيكو" (التي تلقت اشتراكات غير قانونية وسخيفة…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90908" target="_blank">📅 23:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
حذرت الولايات المتحدة حلفاءها من تأخير في تسليم الصواريخ قد يصل إلى خمس سنوات، وذلك في إطار جهودها لإعادة بناء مخزونها من الأسلحة الذي استنزف بسبب الاستخدام المكثف خلال الحرب في إيران.
ألمانيا والدول الأوروبية الشرقية تواجه تأخيرًا في استلام الأسلحة، في حين أن طلبات أوكرانيا للحصول على أنظمة "باتريوت" تتأثر بجهود الولايات المتحدة لإعادة بناء مخزونها الخاص.
أفاد البنتاغون أن الصراع كشف عن "نقص استراتيجي في المخزون" وعن "عقبات في الإنتاج".</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90907" target="_blank">📅 23:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
الاعلام الاوربي:
يتزايد قلق القادة الأوروبيين من احتمال قيام روسيا بشن هجمات بطائرات مسيرة أو صواريخ ضد دول حلف الناتو، في ظل تصعيد موسكو لحملتها الهجينة في أنحاء القارة. مع ذلك، يؤكد حلف الناتو أنه لا يرى أي خطر لهجوم وشيك.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90906" target="_blank">📅 23:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
استهداف برجي طاقة كهربائية على طريق بيجي_حديثة شمال غرب العراق.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90905" target="_blank">📅 23:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90904">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJ3tPyzU_uZfEfRgisiMUWwACbzCLyMTQ6enuXFOh14dx7_aJEQwtSXJCcP_s4qe5g6mthuqBp3-ScVQ2h6Ptykmd5bzkYARdFxPczXz4ib3b-Ga4CHyooPlcLJ3PhD0byorW8ODMur3N_gYFIqkm4T_2kOfh6guptpet0k73RuhIHV4sof-ax8VyZlMYzqX2C-oQApgNT-kkMA-qk7U6-OkqaOJmryGUmG5TR4KGv5Bl9lf7tG7T91ISN44a4lOGq-6mvi6yumCvggU1W9gU79bLMc5VGnLHA-QDhYNP0CJf8zcIVvXMAYoCJgXMKbUPsZ1Czl8acrCGzfIfSETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
أنا فخور بالإعلان عن أنني، اعتبارًا من الآن، أحظر على شبكة "سي إن إن" الإخبارية (المعروفة بنشر الأخبار الكاذبة)، و"إم إس إن أو" (التي غيرت اسمها مؤخرًا من "إم إس بي سي" بسبب قلة المشاهدين والمصداقية)، و"بوليتيكو" (التي تلقت اشتراكات غير قانونية وسخيفة بقيمة 8 ملايين دولار، وهو رقم قياسي، مباشرة من حكومة الولايات المتحدة، في عهد جو بايدن، وذلك للحفاظ على استمرارها. يبدو لي هذا فسادًا!).  أحظر على هذه المؤسسات العمل من البيت الأبيض نتيجة لـ "تقاريرها" المستمرة التي تتضمن أخبارًا كاذبة.
يجب ألا تتمكن وسائل الإعلام من كتابة أو نشر أكاذيب وخيال بشكل مستمر عندما تغطي أخبار الرئيس الأمريكي، أو إدارة ترامب، أو الولايات المتحدة الأمريكية.
سيتبع ذلك حظر على المزيد من وسائل الإعلام التي تنشر أخبارًا كاذبة. شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90904" target="_blank">📅 22:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
عصابات داعsh الإرهابي تتبنى استهداف قوة من الجيش العراقي في محافظة كركوك بتفجير عجلة، ما أسفر عن إصابة ضابط وعدد من الجنود.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90903" target="_blank">📅 22:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي يكذب النسب الرسمية:
تُشير قاعدة بيانات الخسائر العامة التابعة لوزارة الدفاع الأمريكية (البنتاغون) إلى مقتل 18 جنديًا أمريكيًا منذ بدء الحرب مع إيران، لكن مسؤولين صرّحوا لصحيفة واشنطن بوست بأن الحصيلة الفعلية لا تقل عن 22، وربما تصل إلى 23. كما أُصيب أكثر من 820 جنديًا أمريكيًا. وامتنع البنتاغون عن توضيح هذا التباين، فيما قدّرت (سنتكوم) أن الحرب مع إيران كلّفت نحو 43.6 مليار دولار حتى أوائل سبتمبر، بما في ذلك 28 مليار دولار على الذخائر. ولا يشمل هذا الرقم الأضرار التي لحقت بالقواعد الأمريكية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90902" target="_blank">📅 22:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
🇸🇾
الاحتلال الاسرائيلي يستهدف غرب دمشق بقذائف صاروخية.
صرنا نحكي عل مكشوف
😆</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90901" target="_blank">📅 21:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 26 غارة جوية بطائرات نوع "F15" أقلعت من قاعدة خميس مشيط الجوية واستهدفت محافظة تعز.
بلغ إجمالي الغارات التي شنها العدو السعودي خلال هذا الأسبوع 300 غارة جوية بطائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف واستهدفت محافظات تعز وحجة ومأرب والجوف والبيضاء وعمران لحج الحديدة صعدة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90900" target="_blank">📅 21:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbeW4Wq0r-ye30qulnDWul0vf4zoA2Pk1wb0ZxxLFYtxIW40h0lSagogUPyMrw0LO3ikyXdXs6Y-oxiEtAYIyE0WLXDHwGJEgOk4cv-GQ0A7_qZ7jKRGrZThL4JKfj-OdonIGWEg-tSQmaHr-DsJ7L0IFHCnDMwltJimyrD5RSX4pQ2EBAu_n4Kt3Ar0J9R0mq3_dslyHoloMM8A4YSFGdnlY5PIiDcY8DF3QVmVRDymqpbXBB-LZZSAEpqiIviXLWlz6b9KQ4Ey7QTs2uCtfveTMT7_dMAhIpUJ1mL7oQWrtvfbHeE69h-lmfdsM6KpLHzYKY75jeapU9A_ti1LDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: لقد بدأ بالفعل العصر الذي يتم فيه مطاردة طائراتك من طراز F-35 و F-15 ويتعين عليك الإبلاغ عن تعرضها لأضرار
🤏
.
ما كان في السابق كابوساً مرعباً أصبح الآن واقعاً يومياً. تعايش معه.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90899" target="_blank">📅 20:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
🇨🇳
الاعلام الاميركي:
كادت القوات الأمريكية أن تشن عملية ضد سفينة صينية بعد أن زعمت تقرير استخباراتي مدعوم بالذكاء الاصطناعي بشكل خاطئ أنها كانت تحمل مكونات أسلحة نووية.
اكتشف المسؤولون، قبل وقت قصير من الإجراء المخطط له، أن التقرير تم إنشاؤه باستخدام الذكاء الاصطناعي وأنه تضمن معلومات غير دقيقة.
أثار هذا الحادث مخاوف بشأن مخاطر الاعتماد على الذكاء الاصطناعي في مجال الاستخبارات العسكرية وقرارات تحديد الأهداف.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90898" target="_blank">📅 20:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7e415de1.mp4?token=cWgQVyEw13kngJRPB43uDo-wIgJW1it1HKx-ZSkEpybYpntA_S0o9wzJ1ToSl8MClSD4xjSy5yo0U2deshuv5Gg2hFIFV6wh0QkJXtCZXW4KwsnlULHSW7Bgh4gN5p3v0rjnwRVNzVLV2wAu-i5s2sNt7EluLcPcklxFB5Qx5fGTeaBXf4UdRkX_Dhhp62AEnHNasALdN85MVzUatx2fTh-lFNMBo5ZT2WTaSs_J8ZwFawJed1ibWWJ7tfZD5LMzmLuIwrCfnOkUKEZUl7NmeOPNFj7U_EqJJY3M8d4gkP4AO547q_hBtv_2AuRGMf1gZFLAQlme9mSikXoHO79s3XIdyCM8wkeGqRZix6j8U_DSZzH97VlDq247D_fqCKpaNINidm3gVuxHmrc8sCmrxy0q7R-KUxhxmc8kCo4A1E-VQlL97oMV6lrj-LyioaiZDvzdLaIS1N2ZVKCwjZlYcRzEcjhMiyqkNI8W6jlhwK2nKbJj4MU9H_kfrENtdXn2nmieVQCFRYEg7B2iHF3JfD1ZAbUEF-vzu1t_uoIpfSMISh0cd09rCvVQdeDM3RBXFMusxsZk381wdnl1sKfWVWnS6VeOZyWDTaOUBDgT9eUOjNljOxm6uBmZmSbbYLO0P0M6vmZnvHNp8sj-E8hAQqrDUK_7LRnt5myjwe1t4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7e415de1.mp4?token=cWgQVyEw13kngJRPB43uDo-wIgJW1it1HKx-ZSkEpybYpntA_S0o9wzJ1ToSl8MClSD4xjSy5yo0U2deshuv5Gg2hFIFV6wh0QkJXtCZXW4KwsnlULHSW7Bgh4gN5p3v0rjnwRVNzVLV2wAu-i5s2sNt7EluLcPcklxFB5Qx5fGTeaBXf4UdRkX_Dhhp62AEnHNasALdN85MVzUatx2fTh-lFNMBo5ZT2WTaSs_J8ZwFawJed1ibWWJ7tfZD5LMzmLuIwrCfnOkUKEZUl7NmeOPNFj7U_EqJJY3M8d4gkP4AO547q_hBtv_2AuRGMf1gZFLAQlme9mSikXoHO79s3XIdyCM8wkeGqRZix6j8U_DSZzH97VlDq247D_fqCKpaNINidm3gVuxHmrc8sCmrxy0q7R-KUxhxmc8kCo4A1E-VQlL97oMV6lrj-LyioaiZDvzdLaIS1N2ZVKCwjZlYcRzEcjhMiyqkNI8W6jlhwK2nKbJj4MU9H_kfrENtdXn2nmieVQCFRYEg7B2iHF3JfD1ZAbUEF-vzu1t_uoIpfSMISh0cd09rCvVQdeDM3RBXFMusxsZk381wdnl1sKfWVWnS6VeOZyWDTaOUBDgT9eUOjNljOxm6uBmZmSbbYLO0P0M6vmZnvHNp8sj-E8hAQqrDUK_7LRnt5myjwe1t4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان تقدم ميداني كبير لانصار الله في اليمن على جبهة راس العارة بعد تقهقر مرتزقة العدوان في جبهة الأغبرة</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90897" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
ترامب: سنرى ما إذا كان سيتم تدمير إيران.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90896" target="_blank">📅 20:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامب: الولايات المتحدة تتحدث مع الحوثيين، الحوثيون أيضًا يرغبون في إبرام صفقة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90895" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
ترامب
: الولايات المتحدة تتحدث مع الحوثيين، الحوثيون أيضًا يرغبون في إبرام صفقة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90894" target="_blank">📅 19:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇷🇺
روسيا تستدعي المبعوث البريطاني على خلفية تزايد شحنات الأسلحة إلى أوكرانيا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90893" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/90892" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90892" target="_blank">📅 19:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90891" target="_blank">📅 19:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90890">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
إفشال محاولات إجرامية في العاصمة صنعاء قام بها العدو السعودي مصبوغةً بالصبغة الداعشية ولن تمر دون رد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90890" target="_blank">📅 19:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
احتجاجات وقطع احد الطرق امام مولدة اهلية بسبب امتناع صاحبها من التشغيل في محافظة كركوك.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90889" target="_blank">📅 18:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يستمر في استهدافه لمواقع المدنيين في تعز.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90888" target="_blank">📅 18:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
اعلام العبري:
قضية تجسس خطيرة تتعلق بالتجسس لصالح إيران من داخل الجيش الإسرائيلي قيد التحقيق حاليًا.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90887" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇷🇺
‏
الوكالة الدولية للطاقة الذرية:
برج التبريد التابع لوحدة مفاعل في محطة كورسك للطاقة النووية في روسيا تعرض لهجوم بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90886" target="_blank">📅 18:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
🔻
رئيس وزراء سلفوكيا:
أشعر بقلق بالغ من أن كل ما يتم السعي إليه الآن هو ذريعة لنشوب صراع كبير بين الناتو وروسيا.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90885" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇱
رغم انبطاح الدولة اللبنانية..
جيش العدو: إقامة الجيش اللبناني لحواجز بالمنطقة الأمنية بالجنوب "يخالف التفاهمات".</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90884" target="_blank">📅 17:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90883" target="_blank">📅 17:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90882" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90881" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f17d0c4a.mp4?token=PDSQX3mB_evyG-asBu3lEqVqVuJGgxhTC-hxjID1x1go0ovLsOG9BG895Svowm3AQB1OMt4FWZ6eE1TCZMwkEuxOgf82vmXEBMSqf7peCA35NeIwWreZzmxOGCP7VmYErgUzRmoo-jWcmAk-hLF62-uQGLwqn26EeyAg0GRjo21jtjbrjoMMEV-h8BjzAnjrpTvD1sPWw5q55F4hJ0Kj0Kodios9WPLyeACOojfWec2hz-2Ep6nQ-iUMCYDZFLIpe3RaUrpdGlQgm240OcXv7IlzqZLU6ljDPeLjtwQEs5VnHRvu4JFbzOHSlOPnOrGbGNaYDrSDp2g5qYKv4co1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f17d0c4a.mp4?token=PDSQX3mB_evyG-asBu3lEqVqVuJGgxhTC-hxjID1x1go0ovLsOG9BG895Svowm3AQB1OMt4FWZ6eE1TCZMwkEuxOgf82vmXEBMSqf7peCA35NeIwWreZzmxOGCP7VmYErgUzRmoo-jWcmAk-hLF62-uQGLwqn26EeyAg0GRjo21jtjbrjoMMEV-h8BjzAnjrpTvD1sPWw5q55F4hJ0Kj0Kodios9WPLyeACOojfWec2hz-2Ep6nQ-iUMCYDZFLIpe3RaUrpdGlQgm240OcXv7IlzqZLU6ljDPeLjtwQEs5VnHRvu4JFbzOHSlOPnOrGbGNaYDrSDp2g5qYKv4co1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ونقولها من عراق زيد ابن علي بوضوح
نحن جمهور فصائل المقاومة العراقية بندقية بيد السيد قائد المسيرة في اليمن سيدنا ابو جبريل …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90880" target="_blank">📅 16:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab46f5034b.mp4?token=qO_WaerHNoY7j7ZABOXUmWW4dZsL5Y2Z1ZvIKZSpA0RnWR1BVbu1hqNRIm6Gh7gaHm6ksREbn1v90F32OwpZUqfyHvlf61BuTR8q1kJ5tMSh0Ek1GYwKT86QI6iclURzhCihDU5Shy7uxJ4kgEtf2_EdtMqutFiTw8uaSjlGaACz5514Uh4YW_5WONb6eTg_39gdfUm5kqlD_09BcbR2AzfDiEEnsNdT8tkKpbX8KOUs9YYlj2IQI7onUOj5uJPmwLJPs-KsxFEyAtVZPHHOY3OCgCPSFzyLyp_OfdGdJxRtmVUl8tD8lYvENZEMo-MzvgU4STL8tglSz4uVC3rRGaCoZgVTyqHwPx3lrDn_W2fE9HcDBQSxN4MXMcg-gAwx-m4IU05x2SXYc7BK0l2QPjxzdOX0zy68jaAtY0M8iGkvI6BXX7xem8vQcO7q9OSAK1VNl_d7flULjpyXuA9foeRX5X4fc9iwM-leqToxKqTjW99c0aW_DmfiguBuq9as0eEJpKhXH2ruJpcQdhBTGlQDvELn9JwGeCCNWU634lVWNTBY37nSWotYxoygk2Q8knitBJlWIR_LTqAmd7ZI6vm0A-YMG4I3RZp3TkwNr64hGGDfMRLuoEqDliJ5kQIrsQoju-Jx7vhuk7Pl-fBjD5bKqyfG6fGO31ptBq418SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab46f5034b.mp4?token=qO_WaerHNoY7j7ZABOXUmWW4dZsL5Y2Z1ZvIKZSpA0RnWR1BVbu1hqNRIm6Gh7gaHm6ksREbn1v90F32OwpZUqfyHvlf61BuTR8q1kJ5tMSh0Ek1GYwKT86QI6iclURzhCihDU5Shy7uxJ4kgEtf2_EdtMqutFiTw8uaSjlGaACz5514Uh4YW_5WONb6eTg_39gdfUm5kqlD_09BcbR2AzfDiEEnsNdT8tkKpbX8KOUs9YYlj2IQI7onUOj5uJPmwLJPs-KsxFEyAtVZPHHOY3OCgCPSFzyLyp_OfdGdJxRtmVUl8tD8lYvENZEMo-MzvgU4STL8tglSz4uVC3rRGaCoZgVTyqHwPx3lrDn_W2fE9HcDBQSxN4MXMcg-gAwx-m4IU05x2SXYc7BK0l2QPjxzdOX0zy68jaAtY0M8iGkvI6BXX7xem8vQcO7q9OSAK1VNl_d7flULjpyXuA9foeRX5X4fc9iwM-leqToxKqTjW99c0aW_DmfiguBuq9as0eEJpKhXH2ruJpcQdhBTGlQDvELn9JwGeCCNWU634lVWNTBY37nSWotYxoygk2Q8knitBJlWIR_LTqAmd7ZI6vm0A-YMG4I3RZp3TkwNr64hGGDfMRLuoEqDliJ5kQIrsQoju-Jx7vhuk7Pl-fBjD5bKqyfG6fGO31ptBq418SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظام ال سعود يستخدم منابر المقدسات الاسلامية في مكة المكرمة والمدينة المنورة لمهاجمة انصار الله والتحريض عليهم دينيا وبث الاكاذيب لتعويض خسائره الميدانية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90879" target="_blank">📅 16:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من العاصمة اليمنية صنعاء لخروج اليمنيين استجابة لنداء السيد عبدالملك الحوثي لادانة البهتان السعودي باستهداف مكة المكرمة واسناد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90878" target="_blank">📅 16:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbODQkIAUCL0ruBKjw7JMrKtquJYvA3BuuFpfVm0YVCAZW5KqElazamOXNQdZKi3CCI4EsgTiuO8h9CR0ZQAlF7pIEu0mpkTh51XZyiL5U0x16L91N48HeyWYK2Y1h4hCPkOOIJBok0v59epeZ-pWxYJQD83KTYeWMWvxW4qWqVchhN_22hhP9NyO9d7ZMVlVOSTg9eh4N5FICNWeIXTVYwIXfi-Jfx5paoCIg_OxPn1-ex2gYGTtsKrLxPuE0ssWSo92bKOKN1_O7TCxRqMCcU9Az-lCSEpUHJn7HcDjlEiw7Z6RWptsTg2unNMnERPOInuL1rH3fmZMmJGPh_EcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من العاصمة اليمنية صنعاء لخروج اليمنيين استجابة لنداء السيد عبدالملك الحوثي لادانة البهتان السعودي باستهداف مكة المكرمة واسناد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90877" target="_blank">📅 16:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me8mHQMZc8RmvHLMwcpoB-TZO2tQMkYo8GS94HXgJOhgNySd_SqDYILrh0dV_tcF34TIejeQb98M7aEaROMZtoWCEj4HISHG5LY3lFeASM7pd1CHwij3Z83lk70zzzsT3aGPCzaBy7_tBUxkaVhxNOXFjf0elJVJvXjuUCmtMKCYAxIhJ08jmR2oVeb2Dw_nw9jFG8eMCA2qixbJdUg59tiGbC3hDn7rvxIJLsJsK2lJ5QoiVYCjupTNa-c2ij1SZPSddi4kZQBZhL0P_jz7W5fyzE1lw26OEnlWzTr9RRx73apZZjRugbSsFpaV7m-3p1UcSQ5yyKaaK31Pl8bhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEw3RKMjecDdLmcsGYDxFVkGk44BvNgwlXmpYj2-U8sK-ia6MUVe7zQ2iNehecfIunTyUWT7MFD99SzBqzJdq64QWQ976L-HHa31DdtzYhN-PGU9Eoakyd7GuDFASXRZ-bmY5UN6siY-2_J0moGIvQ8dNIBqyMb1I1qlY6Sgbjm8yKTwA8b6LufWgIyuTJ1L6vpNFXyHqZHUdtxb4h8p_kI7F7nPqMOFXaX4T44uYlv49lWSRUyPbPpy4W01tPYEDgxHB7zg1OqtmZ6RV_wYuXxAwgREPEpTqvnmbstfhUN2nGyci5PANP4cX4perKiLRMURbMLzgtkidyANrPusiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULmyM8P-2QYxvjANxzg0Se2nacnP0H2qGj_kqSk-mvM6dBqEboCFFhOiF4NxMWs1OIXvYh1AoaqRRQcTE5oAXQj7LUoHkHRrxatJlsgsS0I1K5jcCdvsLrqZVnMQ0QS4VEKe197avVmBWqXKezySujynQ7tF0ItQDTLLt7get2-9mCFcn5BkRJRz2L4dX7T9hxpIlrCjL7zsWiXyPKKwBaeXj_J6sste8ObBUZvc3x68ouSR7i97--QkOHWSmTSpW_YKbo90q2cmYgTuQxlB9KSzaxtcALd1bTAJchB0uPVdqdo0Wy_MwZqg7vavuhb340Ub2rIArOTHEip0AJUzXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇷🇺
من محافظة واسط العراقية
منتسبي الشركات الروسية يشاركون بانتخابات مجلس الدوما الروسي ؛ الانتخابات تجري تحت إشراف السفارة الروسية في بغداد ولأول مرة يشارك العراق عبر المفوضية العليا للانتخابات بصفة مشرف دولي على الانتخابات داخل روسيا ..</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90874" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90873">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏الاتحاد الاوروبي: هجمات انصار الله على السعودية غير مقبولة وتعرقل الاقتصاد العالمي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90873" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90872">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
الـ100 دولار امريكي في الاسواق العراقية الان تسجل 159،250 الف دينار.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90872" target="_blank">📅 16:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الرئيس الفرنسي:
نعمل لإنشاء خط أنابيب لنقل الغاز والنفط من العراق إلى السوق الأوروبي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90871" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في محافظة دير الزور السورية بانفجار هز بلدة عياش</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90870" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
