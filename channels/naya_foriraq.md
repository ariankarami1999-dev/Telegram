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
<img src="https://cdn4.telesco.pe/file/vFJQ9jo6At1ZzyS0zrx35sX-8blejeIcyDNn3wkcUMbh_1lUo-D3GDCXLV0qKea1dX8Sd3W7Bpo2vAvAUa8X3rzjf4NHx9WUv6siJqpA3SuZlhUsOHC_jJSWylgRxztuC6qMNtuzQzec6OCw-ADZ6sio_NV_xlG7i8jZ4UclXnPX7QFG-e74k--QLr_vTmjX4BkL_1vFeYUpBYJGj8q_sli4DNS7FmXfOoJHqZOgg48CNudOMoGvTClmIW7ETq90wy79_s8Y8mvcNM86wQ2PuoiQWTlXJgBHoYfn94WTsEAPU83bqEyVtldk1KngFbrUPLtVad_hk6fjcx48leD7tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 07:45:33</div>
<hr>

<div class="tg-post" id="msg-80446">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
الطائرة المسيرة استهدفت منطقة الخضراء ومن الممكن كانت تستطلع سفارة الاحتلال الاميركي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80446" target="_blank">📅 03:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80444">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59de911ab6.mp4?token=DK1i0X4rHdf9tnFVwUbO89f6ln7kj77MRqkxFRkeS-OSbxfOkUPtAmTiiEP2D3Lo2_OdqTFD7c9ifrwNYMIFPQVXwjJj9Loj1WYu8qdyo5Y6IKPZAFLlrCy5Rh3YxFl58ZhtK9JIFi372aC1YopI6QXiO9M8g6N4cjsGu0YP6FEPQMH7hnMnZZs2Ol7mcWRnx8qQx1MhieVB_vlStrIPbimhFCgpA5wZkm37LZkHHsr8gykBLww8teO-daQobkHVMqUWi-wfqGEnEsNhgRZKnryoQWEg2yeTsHEDK8I1GFEC0nESoUHBlUW5le4WDkhzAwqEs7MNRgA3FdHfSR8bDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59de911ab6.mp4?token=DK1i0X4rHdf9tnFVwUbO89f6ln7kj77MRqkxFRkeS-OSbxfOkUPtAmTiiEP2D3Lo2_OdqTFD7c9ifrwNYMIFPQVXwjJj9Loj1WYu8qdyo5Y6IKPZAFLlrCy5Rh3YxFl58ZhtK9JIFi372aC1YopI6QXiO9M8g6N4cjsGu0YP6FEPQMH7hnMnZZs2Ol7mcWRnx8qQx1MhieVB_vlStrIPbimhFCgpA5wZkm37LZkHHsr8gykBLww8teO-daQobkHVMqUWi-wfqGEnEsNhgRZKnryoQWEg2yeTsHEDK8I1GFEC0nESoUHBlUW5le4WDkhzAwqEs7MNRgA3FdHfSR8bDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الطائرة المسيرة استهدفت منطقة الخضراء ومن الممكن كانت تستطلع سفارة الاحتلال الاميركي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80444" target="_blank">📅 03:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80443">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هجوم بطائرة مسيرة على منطقة الخضراء</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80443" target="_blank">📅 03:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80442">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c7bc3f30.mp4?token=lwxrUSsEr7-uJflralDFtveApoTKPK7z6dwgtzVR3dXuFsqkdkEtqXu_0Lh4ES8uxaW09JHSW1BRkulGNSG1Fg9Vm6HJkQ_wvZXsYmIdUhEb6u8frMbB7cCXQMStIbxT87_x2MY8ByT3tVWhxHVvJjCxKg3DPi9avrJPa0NiJE0Kx_bu6YdvHMU7NpDqbOzn_vWgHmeknuActfTDsEwj4r9wnXsZ7qna3gKw5yYFl7cF50z-j8QJ-hT1VJo0a4IWra55gb7GXHH9NmFK3d3aCBxwuhKLQkO21RgRdSAUfe0R6D7AsKCEEvjlJyuPknyZhbGDl_L9ZoCu5o1L6VlOaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c7bc3f30.mp4?token=lwxrUSsEr7-uJflralDFtveApoTKPK7z6dwgtzVR3dXuFsqkdkEtqXu_0Lh4ES8uxaW09JHSW1BRkulGNSG1Fg9Vm6HJkQ_wvZXsYmIdUhEb6u8frMbB7cCXQMStIbxT87_x2MY8ByT3tVWhxHVvJjCxKg3DPi9avrJPa0NiJE0Kx_bu6YdvHMU7NpDqbOzn_vWgHmeknuActfTDsEwj4r9wnXsZ7qna3gKw5yYFl7cF50z-j8QJ-hT1VJo0a4IWra55gb7GXHH9NmFK3d3aCBxwuhKLQkO21RgRdSAUfe0R6D7AsKCEEvjlJyuPknyZhbGDl_L9ZoCu5o1L6VlOaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بطائرة مسيرة على منطقة الخضراء</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80442" target="_blank">📅 03:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80441">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80441" target="_blank">📅 03:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80440">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اصوات قوية تسمع في بغداد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80440" target="_blank">📅 03:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80439">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اصوات قوية تسمع في بغداد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80439" target="_blank">📅 02:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80438">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4747a2157b.mp4?token=osIvQ5Xg2PixHduTW2ko3AnXnfw3ylyQou4b6B0l_LvQ5m4lGjdelpS6MXakxdvvLKN-fjzM6K9Z97WW6VlddY13yqU6wQks77gnZ1vPUYRXzIJBgYglxcCSE9T1fuJLUb9A_aFL0WNtH5Yu5vk_ORHf3cwUKPYvbDRlK9QG_zv4LbM9F7NMJHjJ-6cDF_XlXcBV0FpTbQPoN5VGzbvXZQeKaPOzef8PAG72bQlExHTyDsoscZpeAsZ4KUsQngGEVADUnflKCpZan_bPqQVcE80eW1an2QBtBczRLhl_mluRUL-LUEaBCaxb7UXw1bhXkHTBlnp9oenOeq4FZFgIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4747a2157b.mp4?token=osIvQ5Xg2PixHduTW2ko3AnXnfw3ylyQou4b6B0l_LvQ5m4lGjdelpS6MXakxdvvLKN-fjzM6K9Z97WW6VlddY13yqU6wQks77gnZ1vPUYRXzIJBgYglxcCSE9T1fuJLUb9A_aFL0WNtH5Yu5vk_ORHf3cwUKPYvbDRlK9QG_zv4LbM9F7NMJHjJ-6cDF_XlXcBV0FpTbQPoN5VGzbvXZQeKaPOzef8PAG72bQlExHTyDsoscZpeAsZ4KUsQngGEVADUnflKCpZan_bPqQVcE80eW1an2QBtBczRLhl_mluRUL-LUEaBCaxb7UXw1bhXkHTBlnp9oenOeq4FZFgIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تعزيزات امنية كبيرة تتجه صوب قضاء قره تبة في محافظة ديالى.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80438" target="_blank">📅 02:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80436">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prcO7wSCA2EtK--aNuIb6eSRngd9ettmjf86SNAPJfIscwsgBWpVPdZxMCbCMuoi0A0sDAYli42oxiNBvDpgu1TZILovsbzCBztKD97ntpTeHsBufX1L-LiqjjxpYZ1Rl6Q_c9RAwcHAZkcj3bOvsVnUEKQENWGrS5AYvEoB25e_lBU1cnM6umbrFbSxEs9sgN1iQT_YRWnaBDfr2MsxVO3KXJUNei54kGp0l0ezQ3c80Rs1wRlLAarGe3nPHYN7FpNcxCg3m4mQ2RRmd5LiPglJ-gMctG7SY_cRaDFdXwe6MAW5Z5Pqt1VYxVIf3bih8N1G6KOSlYKirxrf5Gkocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mU9lGa5NhMyRiFONoiWc-B1ZAp1HOHeSFAYNOMZokJJI6IYZNNUrhbNYNlQORuMfWG3qrtZ6cL4vtxj_8zaIyJb7O9kWqkK4OSul6YADVbauXzDyGIunYchhNcL6H_ASgFjBPQEkWXmWtevvfSUDlvQRSLAwUBkNy30DmTIZl-DcwVZ-V-vpAqZQc86iG2a5IohPrkfFqUuxiCbWiF1zWyQwsFxvFO1KzCEj-CCEPlimgvH_kuJdf5qPPKaSqwsTwmhJc52ujJryV21aF8uWP1mSn2W8-VHdOdXFptMxKPB2pGp2KZGovBkxhUgN-EZrh3S4HE1RXTnjlt8NszbEhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
متداول
: اشتباكات وإطلاق نار عند سيطرة امنية في قضاء قره تبة في محافظة ديالى بعد رفض شقيق النائب عن حزب تقدم أحمد مظهر الجبوري الامتثال لأوامر التوقف ما أدى إلى إصابة طفلة كانت داخل المركبة وفراره من المكان بدراجة نارية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80436" target="_blank">📅 02:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80435">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
رئيس البرلمان الإيراني قالبياف: لن ندخل بمفاوضات جديدة مع واشنطن حتى تنفيذ شروط مذكرة التفاهم، وهناك التزام أمريكي وفق مذكرة التفاهم بوقف الحرب على لبنان وضمان سيادته و صدرنا أكثر من 40 مليون برميل نفط منذ توقيع مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80435" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80434">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH9qJ_HcB9e-mJA4UhngVO-LSQIAoJTQrSeqyJUVCs3gWmc-sJ-j-Blg7r73ci9rTeBKhc_5hd_3iQJ-woyjckGcXbm1L4GpefG70pT9J-rKss7lb0UJNpS-M8xE4zmWreqO7sLFtpQ2fTZ9fCDMWhzTDJEYCv54qeXnUziLQS9VWHZ4leTgAnVdrgwF81qZhkb-GANvrRniM1Pn7BTLmd0x2BRo_yVC9XHpjrWeVNlIAiIXgslNz0Pv0dd1hdWykx8ADjYBNPAtOpIac7iUlBYjx6yzChDLTW39IttCeMHQQi2cd9oxg3LcCiKH2EdyD_DnXDYP-WJschT75mKOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اعتقال الطفل عباس إبراهيم نصر القلاف في البحرين على خلفية حضوره في المجالس الحسينية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80434" target="_blank">📅 00:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/577a8900f6.mp4?token=XqqEpoDFqlwOY4O1wSopvevoEttpC6RGKYW7AeJ3gn3udempuhUw-oDsyweOXLNVlYhVAUyVbH-dvPGfnXGQrT_soYegpl2FiBOb3A9MJrvGmWj0SqazWt3P67oP0tv47_uU9NaHUgoMcQ926KmuULAOEnCyehmB67mByA05DzKhRqfgGAadv11l3uPfx6mGkAKDTTTR-Ad73ZCfQiPxHd2LliLJ707OhbwrjAb1M6x5Lld258bdRI-m27UJuJXHKZmt8kG_a_Q7f3WkFoW3A6JrVktrCZKK8lbd-QtG9r0iuUOzTrD105LcIrzNJ5YXgyEly9UgZbhpIXIibpfCWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/577a8900f6.mp4?token=XqqEpoDFqlwOY4O1wSopvevoEttpC6RGKYW7AeJ3gn3udempuhUw-oDsyweOXLNVlYhVAUyVbH-dvPGfnXGQrT_soYegpl2FiBOb3A9MJrvGmWj0SqazWt3P67oP0tv47_uU9NaHUgoMcQ926KmuULAOEnCyehmB67mByA05DzKhRqfgGAadv11l3uPfx6mGkAKDTTTR-Ad73ZCfQiPxHd2LliLJ707OhbwrjAb1M6x5Lld258bdRI-m27UJuJXHKZmt8kG_a_Q7f3WkFoW3A6JrVktrCZKK8lbd-QtG9r0iuUOzTrD105LcIrzNJ5YXgyEly9UgZbhpIXIibpfCWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انسحاب جميع الحفارات، مع بدء انسحاب أغلب القوات الأمنية المتواجدة في الموقع بمحافظة بابل.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80432" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80430">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plZD1ZOIvFs3MjUGpyLpbM53ZK8s7sHNl-EyAtRHSnWN0zpO30c4Jqw8TwdMr24Mbx61LV5JOAWRP2flHLZ9-BiKVTCZh5jokT0N719hbRcBZ2wNsLSYWaKHXKnDsRcP4o5oAH2H3x-3DW8x2LmxUVTId0K6vXugfp-UG0tMf1VLwWW0XXxQ4ACQzAY7WymXh5uCspp_3t74Gvw36HGvkMHMLYFitgj6TFckysxojvARTPGEPYFT0gtDhLjYUviehdvIMfn4jLJ7zNd7jPf0ssmHMFIZAKnyBbAkF0AqNRz47-wa76MUUZehvja25hNsZdyiNyKpkzpXeoxRdj_DSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KI2UIGnQosIEmMiCGCoRXD5bRGgqINtGLBWaH2p0zc_pdRPXW0LHgdw6Cw9Ds7LI7ruyxXUlj0Gb_m88TWRnjv9-qkqCEVCsObuck7AGj5-ulyI63ZzM6e7DL52eHA1gQmRwpCFZBuaARq6NHVCHq0H7aNnOjAB93HJwNLDddl_ZzuAFQI1726VYHXZtBQoKuLO-NwQPihVdSt-mSTpUbenXvK4Stydo15q75UJ3RM5vf-xSHcO2xV4YWboB_FAOv3BsqXp9-2cLRYudpmP_BKhHllwnZ9bUJK_8sp79nCkIk8Dh3CTCfdNwCC7_hYGIsCdk3X0F96SRy1T9McTd0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
بحسب تصريح عضو مجلس محافظة بابل حسين عليوي، تُجرى أعمال بحث وحفر في ناحية الشوملي بمحافظة بابل بحثًا عن مبلغ يُقدّر بـ32 مليار دينار عراقي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80430" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80428">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0addd9e39.mp4?token=MVZ3mk7sGwI9xY8cTiRI9HlTSKbRCHkGRvUhxoEBoU4fx0sPtvFJtY6vB8C6E_BbJz1-oprLzvSN-uU6Xn48XjyQrwo5hNMYFUNERmENlSET2Tc4O3TcdQXcoxokTCBLYliWd4Jiax0vwUoQBBS7D1QJZNgGj86bZdYHxZunb23MLBPiIRFLXWAEAnCMdGF_pwSbSfZmPCH-ZHLcS2XGRoKZlZLcfFDtmXviUSkpsig5Gv7KqG_X3SbIhGKCybnItJifEbthlz4nFHOhd51zpdlaIKBMo94LFu8U8wFBCXLc8CsvWoBw2c3x2kdKBjM-arMFxNLFLdvgXLdOzIs21A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0addd9e39.mp4?token=MVZ3mk7sGwI9xY8cTiRI9HlTSKbRCHkGRvUhxoEBoU4fx0sPtvFJtY6vB8C6E_BbJz1-oprLzvSN-uU6Xn48XjyQrwo5hNMYFUNERmENlSET2Tc4O3TcdQXcoxokTCBLYliWd4Jiax0vwUoQBBS7D1QJZNgGj86bZdYHxZunb23MLBPiIRFLXWAEAnCMdGF_pwSbSfZmPCH-ZHLcS2XGRoKZlZLcfFDtmXviUSkpsig5Gv7KqG_X3SbIhGKCybnItJifEbthlz4nFHOhd51zpdlaIKBMo94LFu8U8wFBCXLc8CsvWoBw2c3x2kdKBjM-arMFxNLFLdvgXLdOzIs21A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وزارة الداخلية العراقية:
تكرّم منتسبين أحبطوا محاولة تهريب أربعة ملايين دولار في إحدى السيطرات، بعد رفضهم الرشوة تثمينًا لجهودهم في إنجاح العملية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80428" target="_blank">📅 23:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80427">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
وزارة التربية العراقية تقر شمول طلبة الثالث المتوسط والسادس الإعدادي غير المؤهلين بأداء امتحانات الدور الثاني</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80427" target="_blank">📅 22:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80426">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
رئيس البرلمان الإيراني قالبياف:
لن ندخل بمفاوضات جديدة مع واشنطن حتى تنفيذ شروط مذكرة التفاهم، وهناك التزام أمريكي وفق مذكرة التفاهم بوقف الحرب على لبنان وضمان سيادته و صدرنا أكثر من 40 مليون برميل نفط منذ توقيع مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80426" target="_blank">📅 22:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80425">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">لنستقبل أكبر تشييع في التأريخ
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/80425" target="_blank">📅 22:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80424">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCIKS_floG13kuUQ-6AOsSKUJvzA5Ge2cxjykGI4VHaBUGgTtPOXJi-C7O_rzHpyLKc1iFLdTdYRm5Ynldzd0WJtPqxsdcY8ven4kjWFDK5UlUbg9g2FcFuh4ieMhMNIGKOfSqliSAAdDac6aKOPeeiMAPyRLEbmM4LXB_eAfjOeFsCVoR4_1BPblwlrJwBeBLyWZJ7TfXEVt7lDvLyDuYdTZPF8OJTeNJCYat07aHJ6_bHKwiuQtt7q2N8qSA1IX-RroLyMBNZiwl6xXAGuw-GfVnnCCWydknzzXgghcleXlKEyKgmjft4SXOYJ4Rj6Mhk536yj3ZVTambFcG-3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي:
خلال زيارتي لبغداد، التقيت بالرئيس ورئيس الوزراء ورئيس مجلس النواب ووزير الخارجية وغيرهم من الشخصيات البارزة في العراق. ‏على غرار إيران، يستعد العراق لمراسيم جنازة جماعية للشهيد القائد السيد علي الخامنئي، وهو حدث سيخلده التاريخ بلا شك وسيعزز الروابط بين بلدينا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80424" target="_blank">📅 21:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
عملية دهس في إحدى المستوطنات.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80423" target="_blank">📅 21:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80422">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
خبر دفن جثمان القائد الشهيد "وديعة" في مرقد السيدة معصومة (عليها السلام) عاري تماماً عن الصحة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80422" target="_blank">📅 21:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80421">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVSmH5n56rFBb5erZ0ZL9ahyy9X7XlYtr1W-g-XHLNYC1iiYhI_7EP4Qw60-CYW_vV2WW-IgcjdmBexwk6AvjDCwytxV918t5ZesCIJYSQDNGwtF0yVn7TfhsDw37oUNiS1QVNVPSBD9jhHgrmOsO87J_i-QfiMS5Kdd3Xpvoo2R93RDBzXtSX02eDl2EFCUNXRf1IdiY4xkg1dAqazsvx3AEKSZimopEUw45dtcPXPPEeAlUYbgjwoPx4tqHwBrVsr4xD2FWeJ3wtHkl_I2ktNkW5ggUptTugMJOb1x2GqE7B9H3mG8459Gor9tlIZerfGIKVBtr2mgpqIYjQXOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني عباس عراقجي:
تم إنجاز المهمة"، السيد مولين.
‏لقد أنجزتَ شيئًا آخر أيضًا: إثباتك للعالم أنك لا تملك أي حق في استضافة بطولة دولية. لقد كان سلوكك مثالًا صارخًا على كيفية إهدار الكرامة التي تأتي مع كونك مضيفًا.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80421" target="_blank">📅 21:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80420">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
بسم الله الرحمن الرحيم
﴿وَمَن يُعَظِّمْ شَعَائِرَ اللَّهِ فَإِنَّهَا مِن تَقْوَى الْقُلُوبِ﴾
وتحت شعار: (قوموا لله)
تدعو المديرية العامة للإعلام في هيئة الحشد الشعبي جميع وسائل الإعلام المحلية والأجنبية، والقنوات الفضائية، والوكالات الإخبارية، والإذاعات، والصحف، والمواقع الإلكترونية، والمصورين الصحفيين، وصنّاع المحتوى، والراغبين في تغطية مراسم تشييع قائد الثورة الإسلامية السيد الشهيد علي الخامنئي (قدست روحه الزكية) في محافظات بغداد والنجف الأشرف وكربلاء المقدسة، إلى ملء الاستمارة الخاصة بالتسجيل، لغرض إصدار الهوية التعريفية الإعلامية التي تخوّل حاملها الدخول إلى مواقع التغطية الإعلامية وممارسة مهامه خلال المراسم.
الاستمارة الإعلامية
للاستفسار والتنسيق:
القنوات الفضائية والوكالات المحلية وصنّاع المحتوى:
* 07713513822
* 07737599025
* 07713282065
الوكالات ووسائل الإعلام الأجنبية:
* 07710066020
المصورون الصحفيون:
07807172059
ملاحظة:
لن يُسمح بممارسة أي نشاط إعلامي داخل مواقع التغطية إلا بعد إكمال إجراءات التسجيل واستحصال الهوية التعريفية الخاصة بالمراسم.
اللجنة الإعلامية الخاصة بمراسم تشييع قائد الثورة الإسلامية، آية الله العظمى السيد علي الخامنئي (قدست روحة الزكية)
٣٠ حزيران ٢٠٢٦</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80420" target="_blank">📅 21:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVMjM_NnZIMoeycMjy0j63jh2kfrfzjy03_7FA7O7cEYwpxVMYRKWHoEFgthMXXfAd13EUi3-kEjqcgXq6O6BWFB5hQssdROLRdLuFedUyvIAuwDGQ_aWN4cR8M7ybxYRp7C7TIrQ2w6fXDJbcbBjfSvEnwHnlsy0-74fC---AGIoEtgoC6ToSX-rXiL_Mbq0OG-4cgOpy0qv-JVqnW4UN8lkjf8XtZ2A2i4vjHcpyZn0FJ5dnJnnLqI8ZGIqaErHS0ybuPm8Ws-m55LyIXNkPiJrxUz8etuoE7Eteth8p9yxh4H0zVJiK_c9s3qvunaUqqHUJRQZ8RBjEfREP9Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعش الشهيد القائد الإمام الخامنئي رضوان الله عليه وعائلته الذين نالوا الشهادة على يد العدو الغادر الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80419" target="_blank">📅 21:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80418">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭐️
تانكر تراكرز:
صدرت إيران 50 مليون برميل من النفط الخام منذ رفع الحصار الأمريكي المفروض عليها قبل أسبوعين. وهذا يعادل 1.66 مليون برميل يومياً حتى يونيو 2026. أما معظم دول المنطقة الأخرى فلا تزال بعيدة كل البعد عن مستويات ما قبل الحرب.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80418" target="_blank">📅 21:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80417">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXU1IuSrzGe9UNfxXiChypbvKMGC29Mk2-20GAT_vkz9gzF6Z3cIxCOuL0pda7TOU8hoIoKGVrl5BKVvyUGoMRxQJo8WJK-5rmAxevkfWWeHFL8CK5lTmsqwHyMLnqjz19PGWiNYHf6pZuGxXK9HeudTsSm3ZFLLpe3y0t4QEKxPEOHHIJfzGax_OG5dmJUEl2aqk18rISuBjgZQkpRl8xF11a7Cy5Bk_Mt8v2wJuoX4w66v-iW_593lhKHVchYliPapJ0OdL9NeW3a6b_0ceN_MQ8IoYqBt525Pzx_VyuJdp0hIs7yHnbNtj7Cu7L4jKsLeQkLQJumiEr7yOu2vuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب ساخراً:
أود أن أهنئ الرئيس شي، والدولة العظيمة للصين، على فوزهم الضخم في مسألة "المواطنة بالولادة".</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80417" target="_blank">📅 21:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80416">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA0jxAXYUq256kMYJhujUaJG-QqB23uEzlfHE25eGr4MI_zDsDG7oadftAjH1jykf1myp_gig46gTPDbs7iLSdbh_do9TICrwObJrZrjkZGM71ce4crZWPnt-khkKb2cO8-l5UwUwXZktao1CaI_GLKsJgZg0ph1ARkxVaLXxxb1hMelCSrLfu6_Asn42g1iEhDACF3LaGP6Ir9en6M6bT0ZnK9bAaJRLrD0mu__G8qUmKiTsYTKHiIfyRby5NDLO2JHaZz1CwnMvUDf4yO3vZQYWJK6qfWvQqlmA_hZJgN_LQOgFkgNV9SdljzQa1iUGVUNnKt4CjkAIe2BzQQxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو ينشر صورة يزعم أنها لفلسطيني تم إعتقاله وتعذيبه على يد جنود جيش الإحتلال الإسرائيلي.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80416" target="_blank">📅 20:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80415">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭐️
المنظمة البحرية الدولية:
تم إبلاغنا أن الممرات التي قدمناها ليست آمنة.
علقنا إخراج السفن العالقة في مضيق هرمز بعد الهجوم على ناقلة نفط.
ننتظر موقفا إيرانيا بعد الهجوم للسماح لنا بإخراج السفن من هرمز.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80415" target="_blank">📅 20:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80414">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
اجتماع الغد الذي سنشارك فيه في الدوحة سيركز على موضوع الإفراج عن أموالنا المجمدة وإيقاف الحرب في لبنان.
البند 13 واضح بأن بدء مفاوضات الاتفاق النهائي رهن بتنفيذ بنود أهمها وقف الحرب على لبنان.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80414" target="_blank">📅 20:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80413">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
🇮🇷
اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي في العراق:
تؤكد اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي، رضوان الله تعالى عليه، أن جميع المواقع والمنصات والوكالات التي تدّعي تمثيل اللجنة المكلفة بالمراسم هي جهات غير رسمية، وما يصدر عنها لا يتعدى كونه توقعات أو اجتهادات أو معلومات مسرّبة غير معتمدة.
وتوضح أن الجهة الوحيدة المكلفة بهذا الملف هي هذه اللجنة، وأن الناطق الرسمي المخوّل بالتصريح بشأن هذه المناسبة هو الفريق سعد معن حصرا.
وسيصدر بيان تفصيلي عن توقيتات ومراسيم واماكن التشيع (في النجف الأشرف وكربلاء المقدسة) من اللجنة الإعلامية المشكلة رسميا برئاسته.
اللجنة العليا لمراسم تشيع جثمان الشهيد القائد السيد الخامئني رضوان الله عليه
٣٠ حزيران ٢٠٢٦</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80413" target="_blank">📅 19:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80410">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a935b97b50.mp4?token=KBCiFy3MPli4ciWD7cUxmbUhbzAMIZRQNMeRlyALVYn-O8cgXSxpsQY8jqTBBLbgEQlaAqv83aCALbaMPY8d8c_lhsVmIyzMVyHF-SiMRPNtLae7vmwZOQ5sbpbcQXk46KeyRZVGf1JfVtcOdKWnbrcAUaXK64igT7nsu-o2ngWy4qQ549JIRI7iaFN_hQLi9Oaoi0MUw0uNCnFelVy8pUazOoQjYrrc1qo9UrTDAykmJt_k-CzqXm-U7bzyXGAygR0KR7YppH-S7bwzuGGsqbuxvZo9FODRQZpCSmGXjVSSe2MeYTRi_U8H1ayur-osveqvchmH-_FoMNcAHHsqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a935b97b50.mp4?token=KBCiFy3MPli4ciWD7cUxmbUhbzAMIZRQNMeRlyALVYn-O8cgXSxpsQY8jqTBBLbgEQlaAqv83aCALbaMPY8d8c_lhsVmIyzMVyHF-SiMRPNtLae7vmwZOQ5sbpbcQXk46KeyRZVGf1JfVtcOdKWnbrcAUaXK64igT7nsu-o2ngWy4qQ549JIRI7iaFN_hQLi9Oaoi0MUw0uNCnFelVy8pUazOoQjYrrc1qo9UrTDAykmJt_k-CzqXm-U7bzyXGAygR0KR7YppH-S7bwzuGGsqbuxvZo9FODRQZpCSmGXjVSSe2MeYTRi_U8H1ayur-osveqvchmH-_FoMNcAHHsqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
استمرار عملية تجهيز مصلى طهران لإستقبال الجثمان الطاهر لقائد الثورة الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80410" target="_blank">📅 19:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80409">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قوة امنية تطوق منزل معاون مدير عام مصافي الجنوب في منطقة الجمعيات بمحافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80409" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80408">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭐️
‏رئيس البرلمان العراقي "هيبت الحلبوسي": لن ندخل في توترات مع محيطنا العربي من أجل إيران.  ‏أكدنا في السعودية أن العراق جزء لا يتجزأ من العمق العربي.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80408" target="_blank">📅 18:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80407">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKi-2TsS-hI-H1C0Qb3FblflH-kPKLDDjVZSdnIIKaBNIFX8w9Gn2ooGbihMqGywqrtsKInJrWtjO3xrIb4Aci1QIq7WXl5sJVuC4yjU_20pGCHXIVO_xEBhGVypl7eQmrlGqM2QegskOdZj8xpI-Dd-adFad997OCET0fe4ApexX5rxPVxYUei9mY9DeTT9lp2AIwI8ADhSHeJS1BzYRdXrxv_SW5ZKiaTW67kPD4pMW3fCU0N7QFgJ2G2MFAuqcLi6p_-K5wGV4_cYGFQFoEVEK-1jD4tltB2IwGTfFxqVIwaHBSjlmjh8k39PFCVAwjuUC3JolgOP-eXCRf4VmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
«انتصار كبير: المحكمة العليا الأمريكية أصدرت حكمًا ضد مشاركة الرجال في الرياضات النسائية. يا للعجب! هذا ينهي هذا الوضع السخيف تمامًا!»</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80407" target="_blank">📅 18:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80406">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭐️
‏
رئيس البرلمان العراقي "هيبت الحلبوسي":
لن ندخل في توترات مع محيطنا العربي من أجل إيران.
‏أكدنا في السعودية أن العراق جزء لا يتجزأ من العمق العربي.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80406" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80405">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
إعلام العدو:
"ألقت الشرطة وجهاز الأمن العام الإسرائيلي (الشاباك) القبض على مواطن أمريكي للاشتباه في تجسسه لصالح إيران".</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80405" target="_blank">📅 17:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من عملية تجهيز مكان وضع الجثمان الطاهر لقائد الثورة الشهيد السيد علي الحسيني الخامنئي في مصلى طهران.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80404" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80403">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⭐️
نيويورك تايمز:
بعد الحرب الأمريكية الإيرانية، اقترحت عُمان نظامًا جديدًا تدفع بموجبه السفن التي تستخدم مضيق هرمز رسوم خدمة، حيث تدير إيران وعُمان هذا الترتيب.
تقول عُمان إن الدفعات ستكون طوعية وستساعد في تمويل خدمات الملاحة والأمن والبيئة، بينما أشارت إيران إلى أن الرسوم يجب أن تكون إلزامية.
تعارض الولايات المتحدة أي رسوم على المرور، مشيرة إلى أن المضيق يجب أن يظل حرًا كما كان قبل النزاع.
أصبح الاقتراح قضية رئيسية في محادثات السلام الجارية بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80403" target="_blank">📅 17:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80402">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho0Tmjl1euPVn3PMWWtww5-DRzStetcfx1s0iYpUzhuVRO_C2Kee8Dosg2hjt5auLhYxVA2JupiDAbycyEXocwXTS8WYnz3sePEIARV7x9IzrZQuK-fjOK41BM91bn3-O0UqXYAI4LS90YPGJQ2FyTlF7rX9uTMCqRuvMl1eS5ptmIrn39ODrlf1MJkqTlhICldFvY4vVW_ASW_kEgyrwW6e20rQwXl4GyCL3k83zVbzH7qbnF4DhKLbt6xuIgzKU0tXhwImcAwkKVfNRA5ZtL2v4Q97H81TzRR2qfvcLaY45dXrGu0Eoa1J7T0u0tORMCFlYAaAfCn5j4ifLnJjeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
نتنياهو ووزير الحرب كاتس زارا اليوم "الحزام الأمني" في جنوب لبنان بعد توقيع اتفاقية التفاهمات.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80402" target="_blank">📅 17:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80401">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2JX93LpGC-fMiw_JC5rXxNVusevxvpIxf5Nji94ZGRzTgd1y9X3VHFazwxvRd9Yn0BmtAhxv93uuz27npAFU5rYRNw83zNxMLZeah6vZ-nfApYY6smP5vuEkojwcT8hSIgBFhhDXSL34JDQZj7sbILtZsNPNPtZE6RVmrveG0HI-NtfWsUTQVUSrt7hEqaGb8sCgy2vRXned0DAYXg_WL052udllJyk7uCQeG69wBKhuT5_z11iisjGonYIIAuCy5k114d8QPeH09ij7P1no1ezqvzYlxVaRpIciwoNg6cjoWMgzLh_RCN76oqTo3L_2AI4E2SXPnO2OrhCl_YJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة امنية تطوق منزل معاون مدير عام مصافي الجنوب في منطقة الجمعيات بمحافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80401" target="_blank">📅 17:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjHFSxJJhZ9fgDXzUUg50VIHmPBfWjCkeA2WHtsGKeQRM63w7e3ta4DKOxW7f_bGakltECGe_dXLlrWn4ucCGvaFc30EO24AkK5CcGEW52B-0J7IsVedN2yfvEXpXpim9I0WTYt-3dqyEMZgLcinVGNlBTzmFSiqh_Z24aNcgMu0OEMyMt7PBl63aSS5r01n4pzBSMmT4X6LkNIvskFUTJDGd9lu6DvKkhpZJQS_m78niCsrYK2yuJ-2at3xmjuI9dHXudOFCo3TmFisqEW0dw0qdQgD4gUkvPi4_XOSR310coYOrdAPI2Um5mex_A2sp8ud-7j3Z1RyCp24ShJ7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة من بغداد تداهم مديرية بلدية محافظة الديوانية وتعتقل مسؤولين بارزين فيها</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80400" target="_blank">📅 17:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارة التعليم العالي العراقية توافق على منح خمس درجات لمعالجة حالات طلبة المراحل الدراسية المنتهية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80399" target="_blank">📅 17:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc24e9d2ba.mp4?token=rvHDcWZrOmrr3ARMKhevKG5_C74xCumYA-uT95Q4gptawPUd7MKYtkvywSVwmOt8_dcN6K2KbSH-NUT2Xc4wThavvMiy0AMSQaOfQSvdY8_kYjnEF6ij7K9SLzaQzSPJCA9tJgJHkkyTkdF6OL5PMmsnmns0uEdmYHqlPxrkj8mCbRrz2p0gAYtjkZqmePNko1Fz0tVuV-wAd1oV8wN2UPQeUF_sxbEQMvL3lkbFr5aK7TrIgyKT5Og8jtFSnddLiFkNpU7Gf6dKzxQTWdoY6LmDueCuYi32634fk8r_Bl09LgvCF3xFa7sgwo4LWnN7DYhFnPScX2Oc8rbkH0hmkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc24e9d2ba.mp4?token=rvHDcWZrOmrr3ARMKhevKG5_C74xCumYA-uT95Q4gptawPUd7MKYtkvywSVwmOt8_dcN6K2KbSH-NUT2Xc4wThavvMiy0AMSQaOfQSvdY8_kYjnEF6ij7K9SLzaQzSPJCA9tJgJHkkyTkdF6OL5PMmsnmns0uEdmYHqlPxrkj8mCbRrz2p0gAYtjkZqmePNko1Fz0tVuV-wAd1oV8wN2UPQeUF_sxbEQMvL3lkbFr5aK7TrIgyKT5Og8jtFSnddLiFkNpU7Gf6dKzxQTWdoY6LmDueCuYi32634fk8r_Bl09LgvCF3xFa7sgwo4LWnN7DYhFnPScX2Oc8rbkH0hmkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية في محافظة البصرة جنوبي العراق تلقي القبض على (مرتضى زوير) برفقة أربعة من أبنائه على خلفية تهم تتعلق بالتزوير وتم ضبط بحوزته على 30 ختم يُستخدم في عمليات التزوير إضافة إلى كميات من الاموال</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80398" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جيش العدو الصهيوني: تم إرسال طائرتين مقاتلتين تابعتين لسلاح الجو قبل قليل باتجاه طائرة مدنية في البحر الأبيض المتوسط ​​بعد ورود بلاغ عن فقدان الاتصال بها.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80397" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80396">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اعلام العدو: عقب الحادث، لم يُسمح لطاقم الطائرة بالهبوط في إسرائيل، ومن المحتمل أن يعودوا أدراجهم ويهبطوا في بلغاريا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80396" target="_blank">📅 16:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اعلام العدو: طائرة كانت في طريقها إلى إسرائيل في الجو ضغط الطيار على زر الاختطاف ثم ألغاه، الطائرة غيرت مسارها من وارسو إلى قبرص وتم ارسال طائرات مقاتلة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80395" target="_blank">📅 16:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اعلام العدو: انباء عن اختطاف طائرة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80394" target="_blank">📅 16:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80393">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اعلام العدو:
انباء عن اختطاف طائرة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80393" target="_blank">📅 16:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80392">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73908e4ec3.mp4?token=QidtqWHiAbb7nomb3GIGnU-NpDvr2lynmK1Au1Nr4tP9BSkwn_xBkcUeg3KIrljGB8dFIU45nb73GYMAk5FhAB8HTlcM9r-SIR3sTG-bZu0LsaOZ7FYEQ2Bv-NkJaKxBnCLYZlWNzOTzgW-6kLSbCijUPZj8BbHvltihuWj4Pc4W35xNrvK6g1PeVnwcWws7s8zTUFkFpKpt2n8_And5bWt0ZpFV2Fn7tpznmDhr7BkgHiMtYDkYituvrLhYTy3RxXAHCE1Z2YXpuIzqIF2hrXvC87Y0GHr4-tOUoTwBgEH0KkVufDw5O_xHjImyUc-w84lnORnGl06bwMib2Y5V_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73908e4ec3.mp4?token=QidtqWHiAbb7nomb3GIGnU-NpDvr2lynmK1Au1Nr4tP9BSkwn_xBkcUeg3KIrljGB8dFIU45nb73GYMAk5FhAB8HTlcM9r-SIR3sTG-bZu0LsaOZ7FYEQ2Bv-NkJaKxBnCLYZlWNzOTzgW-6kLSbCijUPZj8BbHvltihuWj4Pc4W35xNrvK6g1PeVnwcWws7s8zTUFkFpKpt2n8_And5bWt0ZpFV2Fn7tpznmDhr7BkgHiMtYDkYituvrLhYTy3RxXAHCE1Z2YXpuIzqIF2hrXvC87Y0GHr4-tOUoTwBgEH0KkVufDw5O_xHjImyUc-w84lnORnGl06bwMib2Y5V_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من عمليات هدم بيوت الشيعة وتهجيرهم التي قامت بها عصابات الجولاني في قرية المزرعة بريف حمص السورية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80392" target="_blank">📅 16:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80391">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
عرّاب تهريب المخدرات يقع في قبضة مفارز مديرية شؤون المخدرات، وبحوزته 32 كغم من مادة الكبتاغون قرب منفذ عرعر الحدودي ضمن محافظة الأنبار، كان يحاول تهريبها إلى إحدى دول الجوار.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80391" target="_blank">📅 16:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80390">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">متداول  الافراج عن النائب السابق محمد الصيهود السوداني لأسباب صحية بعد ان تم اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80390" target="_blank">📅 16:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
هيئة المنافذ الحدودية العراقية:
إلزام الشركة العامة لموانئ العراق بعدم السماح بمرور أي شخص غير مخول، ومحاسبة المتواجدين في البوابات في حال حدوث أي خرق أمني أو حالات سرقة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80389" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
وزارة التعليم العالي العراقية توجه بالإيقاف الفوري لتسلم جميع الطلبات المتعلقة باستحداث الجامعات والكليات الأهلية فضلا عن إيقاف طلبات فتح الأقسام العلمية الجديدة فيها اعتباراً من اليوم الثلاثاء.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80388" target="_blank">📅 16:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80387">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
مديرية المرور العامة العراقية:
منع سير المركبات الكبيرة على الطريق السريع (محمد القاسم) ابتداءً من مطلع وزارة المالية ولغاية منحدر قرطبة/ الباب الشرقي ذهابا وإيابا، وذلك بسبب الأضرار التي لحقت بالطريق نتيجة الحريق الذي اندلع صباح هذا اليوم في منطقة النهضة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80387" target="_blank">📅 15:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80386">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CujHDQ5en5AJsZ1eFTnpGN_4zpm-K4UIpI-VnaV_DiXxcH629CR8bEmy1GVTXFrh9MDiOI4YFkJcBKPxGUtPUIoeziFuuE9SJLgN3RoSOggLuG3rqhZyLyE17E1LoWE4iT-0Gpdii964eRQQp6bxwjRnjhOuwRtkSWSAgcLmrkIDBNPYSMa8r_Tu4fNbAPhXk98Lf-ctBXrrveOTVWDS-xXhC8PQOb6lJlUaKSIQoes30I_hDm7tU8P1ZUCvY4ECHiUoHjH83nwFtc-L6XmTXsB_v2ZOyPJw4dr9YAeGza08mLeid5YYjdUHBBY9qLWVNqPP4zY3J4HkYInjAMde0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متداول
الافراج عن النائب السابق محمد الصيهود السوداني لأسباب صحية بعد ان تم اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80386" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80385">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
قوة أمنية عراقية تلقي القبض على زوج أحد أعضاء مجلس محافظة الديوانية بتهمة التلاعب والتزوير بوثائق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80385" target="_blank">📅 15:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
الخارجية الايرانية لغروسي: توقف عن إصدار البيانات السياسية وركز على أداء واجباتك المهنية كرئيس لهيئة الرقابة النووية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80384" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80383">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfa-gUtOFczu7XI_2VFxnH54qRFHl35RrMA4UPX9PhQClxwmSxPmtDGyfPgR9Hfy4_q1n6Dhv50KCNwagA1LIZofXJCEe7LIylY1itT4K7jKNEf6Vlj20_UtM-Z5bKRvoFbLo233rL-jwN1wlxY77Xj7H8z4ut5Ogy111cB2J0oYppciRs-r_GOutXO3ixw54mUQWJF9xViC56dref7cN5FhJHiIc9eFvM41GNIJK1EpicwXfRUiG33BkoBQJcvAfoA6iE2YsXQ1tnxPcWp4GHfY74MXoy3oWIGc2v1XQKrR5u2E9KuJlD1aUHzWaTteU2Yyd4DHbEIqhbywrdFj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الاستخبارات العسكرية العراقية تعتقل تاجر  للمخدرات بحوزته 4 كيلو من حبة الكبتاجون في محافظة الأنبار ما يعادل 23 الف حبة</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80383" target="_blank">📅 15:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80382">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
الخارجية الايرانية لغروسي:
توقف عن إصدار البيانات السياسية وركز على أداء واجباتك المهنية كرئيس لهيئة الرقابة النووية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80382" target="_blank">📅 15:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصدر:
رفع الحصانة عن ثلاثة نواب عراقيين جدد تمهيدا لاعتقالهم.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80381" target="_blank">📅 14:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80379">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1wLEBgnkSBqtV8rCW6NtR1ZsEs5N8vc7xQXR1SkBfLFNeaeioS74xzTA9CQ5ejUsT_t_SFogOBAfXpAmRWaEjHfazsElqwPEnzEx_4Z_c8gcMQce8GGb_5HuTz3lJ69Do7D1Ntk4kGsG4NLoRLrimd7xO9oPf1OkbxhJ2WENwqsYC-rGM0QG7O4JsmMh2qLtvhuVRG6VtaAPcQ-ZYke8zPCUX2w3c0xwYWw84dNBb0zCpbVnH8qxE4VcaFhf5SJNkHC2S2aURdqU_FCPxiyrlwnZD2hYp9Wdfcu9YgZYnP5G9fZrAhOXSiikkrP2rFSeGL3KHzQHATBJWbra-5CHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6om5deynzRSpZhEBGyZS7H4ha_oR68Wd7_YmeLQ3ekC0dJSDdtixwBOng9X35klcf9-ue9c7d9tSZaKly41C-oTbCrgQ9_v0WdeTq3c-4O1_U5QyqMRWDYeEJoou-vtbM-nKamDK-D2Avzxn_qJSebD3l5F5f5rz_x7lYd9uiw5jbpOob2Dc2Jp4ivMxdGzOdDVHjy9oX1oLqyu8maZMLxsPEgvJsIR4z8vPiHMM-pgICFyfM9fUIRg5cylarOdo5WSqOHvvKgdoid5Jb3BIcLnW8TjGvEHMKRbe7irz14aaROpZ5L5bMk3gr27Y7koI13Vp0Yip9O324S8X1pQgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
متداول: القوات الأمنية تضبط 11 قارورة مملوءة بالأموال كانت مخبأة داخل منزل يعود لوكيل وزارة النفط الموقوف (عدنان الجميلي) في حي القضاة بمدينة تكريت مركز محافظة صلاح الدين شمالي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80379" target="_blank">📅 14:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80378">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
دخول قوة أمنية كبيرة لمدينة النرجس السكنية في محافظة البصرة جنوبي العراق وإغلاق البوابة الرئيسية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80378" target="_blank">📅 14:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80377">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">محكمة الكرخ تُصدر حكمًا بحق النائبة عالية نصيف جاسم
أصدرت محكمة الكرخ المختصة حكمًا مدنيًا بإلزام النائبة عالية نصيف جاسم بدفع تعويض مالي إلى المشاور القانوني في وزارة الداخلية حسين يوسف التميمي على خلفية ما انتهت إليه المحكمة من ثبوت المسؤولية المدنية عن الأضرار الناجمة عن العبارات التي صدرت بحق المدعي عبر وسائل الإعلام والتي رأت المحكمة أنها ألحقت ضررًا بسمعته ومكانته الوظيفية ومركزه الاجتماعي بسبب تنفيذه واجب اصولي وفقاً لقرار قضائي بإلقاء القبض على ابن شقيقها بالجرم المشهود .
ويأتي هذا الحكم عقب صدور حكم جزائي في ذات الوقائع والذي منح المدعي الحق في المطالبة بالتعويض المدني عن الأضرار المادية والمعنوية التي لحقت به نتيجة تلك الأفعال .
ويؤكد هذا القرار أن القضاء العراقي يمثل الضمانة الدستورية لتوفير الحماية القانونية للمكلفين بخدمة عامة أثناء تأدية واجباتهم الرسمية وترسيخ مبدأ عدم الإفلات من المسؤولية عن أي إساءة أو تجاوز يقع بسبب تنفيذ القانون أو تطبيق القرارات القضائية .</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80377" target="_blank">📅 14:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80376">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏الخارجية القطرية: لا لقاء مجدولا بين ويتكوف وكوشنر والإيرانيين في الدوحة اليوم</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80376" target="_blank">📅 14:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzzTm2rop7OmgZDhaDtxaAAcR0HF2bE-09N7aDRh0yCRTbOumYtIKBfT178CSPq5rsb41J8pRsO1Vf17eFh_YVZeYmIxv1I1xpDE3_yHa6-aYoHEtwNESsaAp28ERDttu9sn2jSYNLhlc_QzGVDnrR8aeqw1TDkwygzgnoXx-rgsV1jTR_sOQlkHGj76iPnANmovtpP_AJpoU_D2KXRHJRVzAXROeluy1WW5RS78NGvxow19-foaqeZRsjSqY9JKpU5EJLoJEKtiQ4m8fPhtcrmS51OVCRDsoOKOjqnLn5X8LwV2HvuGjBlUxauk_nCxIg_mllqvUGpQvouljxLTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1_SDxHxXaJe1NqQBT6sEx4H4R549gTyxEzrVHIMsga-c0kuj4PAqCANdLfFWi49GOcE2N8cyTWJml9Yr1rTKGBLd6LWpyIWsNVMLUiDfmrzTxg4NthsXyuATbxsR7VBFuO5DgFUaFX9KIVIATnWVsgCQO4LFU8aeMwNbytoqiOj1dkRwf3JOMlM9vKy0F4WO1ch07tZtM36Z8da9kUrr8y2IDhLJXut4yZAqCO_3lt6_SFkYDmITcruGuruEjqiDYr0dmoRtsD0PX_a0tS904jXB4zU-Lz73JTjZROJN2t3nuaxrq5YnCN8HXlA_Qj-hV1iRTB0yN9EBj24Z_J6kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
دخول قوة أمنية كبيرة لمدينة النرجس السكنية في محافظة البصرة جنوبي العراق وإغلاق البوابة الرئيسية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80374" target="_blank">📅 13:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
متداول:
القوات الأمنية تضبط 11 قارورة مملوءة بالأموال كانت مخبأة داخل منزل يعود لوكيل وزارة النفط الموقوف (عدنان الجميلي) في حي القضاة بمدينة تكريت مركز محافظة صلاح الدين شمالي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80373" target="_blank">📅 13:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80372">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5XBu-Bcp2aCY_Gn2Q3xVa2Xgoqkk52fXwSam8_7D__LUpsVBS_vK2780hybOA1_50YYdbUxyZ7e22g4rc2zS9Ih8PYudUm0UL3lNxUo3Lwn71jXcCYI7y9lp9S5AwtJMQaGLPPuJR-a20gsm13iu1BcyD7JdH1torGFem7QduEIBvWtaE8MkzQp7b0N8JRNpKX0cxkjwpyrEnY_2r5HgHg7PA8Tp8N4uKH9X0RDLOnZplZq1bdxRgVK-FKcF3d5B3qF3FFCLw170PoYjvKtPsUYoJ-21XJaUpqa8yAyM1POlbQ-HEtq_76Xw3Rcd1-e3Acr7XL5ifs3-U3LuCE4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوات من جهاز مكافحة الارهاب العراقي تقتحم منزل في مجمع زيتون بمحافظة اربيل وتعتقل صاحب المنزل الذي يعتقد انه مسؤول حكومي</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80372" target="_blank">📅 13:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
القضاء العراقي يصدر
احكاماً بالسجن لمدة عشر سنوات بحق ثلاثة مدانين يعملون في ديوان محافظة ديالى اقدموا على اختلاس
مبالغ مالية مخصصة لتعويضات الشهداء والجرحى من خلال تنظيم 301 صك وهمي وتحويل الأموال من حساب التعويضات إلى حساب السلف التشغيلية الخاص بديوان المحافظة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80371" target="_blank">📅 12:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24675f9dc6.mp4?token=L_KqvVQBLLnNX9sIEz9ArmMmfzGTM_5hLZQc89uLms67gh1RRYzltI7WOSoi7wcBNLJFP1G5p9970lce6Bt9hpw8hKRQtA_JfTOl4ExPu57na3pGFIBlfJoD_HYH4EERL6nwrXrbIEEY6KuEncpaCx443Ww7kPl_fvQbQ_438N4xGTAEiH1LHaEPYsNo_G3pgZZz9EiqraN6WQP5BsrAdjks7yKDmzwgOOwupIW8woE5PTPR1YBF7P7-2p4zvLYmG2rHCCw8DXuwelPdGMDbk9sc77fRXWBnRu2UZyBIwIwSg2eU9AX5vg5TscCg0heZ-q-n94YKn5o1dP7bC_0x-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24675f9dc6.mp4?token=L_KqvVQBLLnNX9sIEz9ArmMmfzGTM_5hLZQc89uLms67gh1RRYzltI7WOSoi7wcBNLJFP1G5p9970lce6Bt9hpw8hKRQtA_JfTOl4ExPu57na3pGFIBlfJoD_HYH4EERL6nwrXrbIEEY6KuEncpaCx443Ww7kPl_fvQbQ_438N4xGTAEiH1LHaEPYsNo_G3pgZZz9EiqraN6WQP5BsrAdjks7yKDmzwgOOwupIW8woE5PTPR1YBF7P7-2p4zvLYmG2rHCCw8DXuwelPdGMDbk9sc77fRXWBnRu2UZyBIwIwSg2eU9AX5vg5TscCg0heZ-q-n94YKn5o1dP7bC_0x-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عصابات الجولاني تعتقل عدد كبير من النساء الشيعيات في قرية المزرعة بريف حمص بسبب قيامهن بتصوير عمليات الهدم التي طالت القرية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80370" target="_blank">📅 12:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في بافيه مقاطعة كرمانشاه الايرانية،شهيدين كحصيلة اولية من الحرس الثوري.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80369" target="_blank">📅 12:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80368">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
مراسم تشييع جثمان الشهيد السيد علي الخامنئي في العراق:
▫️
يصل الجثمان الطاهر للسيد الخامنئي وعائلته عصر يوم الثلاثاء المقبل الموافق 7 تموز، قادمةً من مدينة قم المقدسة إلى مطار بغداد الدولي
▫️
في مساء اليوم ذاته {الثلاثاء} يتجه الجثمان إلى مدينة الكاظمية…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80368" target="_blank">📅 11:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f940aab8e8.mp4?token=fyB1x6jhgiC8tNDZ02-kuWCNCyw786UqT_jRzXrjffnzfNPIoBgy-qJSTd-Nqi3xHKp1IV4Z3caP8czvf68N8kdtYfyL6B3FJBLFPNO7ysRe_uEcu3AKU6l74pRSnoxHnQODhOxjgZNpY8jNcn7BErCrHittn0T1RirvPmmWZvPZ9HtG6BwEOH936rpL5VIfK_KQzAlnqeS1V76DFfB-U-sykULOzPOol3tccTzGfz445pBD2vvYjA-NtDsx3dqLIAjrMoVKh4g13Dt8gnxgbZ5ZjcRzHRfIypgJBYNT-BFemVxl5pQaSCMkuwNLQXkfVlp_HNuEtRwuUiMJBod_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f940aab8e8.mp4?token=fyB1x6jhgiC8tNDZ02-kuWCNCyw786UqT_jRzXrjffnzfNPIoBgy-qJSTd-Nqi3xHKp1IV4Z3caP8czvf68N8kdtYfyL6B3FJBLFPNO7ysRe_uEcu3AKU6l74pRSnoxHnQODhOxjgZNpY8jNcn7BErCrHittn0T1RirvPmmWZvPZ9HtG6BwEOH936rpL5VIfK_KQzAlnqeS1V76DFfB-U-sykULOzPOol3tccTzGfz445pBD2vvYjA-NtDsx3dqLIAjrMoVKh4g13Dt8gnxgbZ5ZjcRzHRfIypgJBYNT-BFemVxl5pQaSCMkuwNLQXkfVlp_HNuEtRwuUiMJBod_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مراسم تشييع جثمان الشهيد السيد علي الخامنئي في العراق:
▫️
يصل الجثمان الطاهر للسيد الخامنئي وعائلته عصر يوم الثلاثاء المقبل الموافق 7 تموز، قادمةً من مدينة قم المقدسة إلى مطار بغداد الدولي
▫️
في مساء اليوم ذاته {الثلاثاء} يتجه الجثمان إلى مدينة الكاظمية المقدسة حيث تُقام مراسم التشييع الشعبي
▫️
في صباح يوم الأربعاء الموافق 8 تموز تبدأ مراسم التشييع الشعبي في كربلاء المقدسة
▫️
بعد عصر الأربعاء يتجه إلى النجف الأشرف حيث تُقام أولًا مراسم التشييع العلمائي في صحن السيدة فاطمة الزهراء (عليها السلام) تليها مراسم التشييع الشعبي انطلاقًا من الصحن المطهر وصولًا إلى ساحة الشهيدين الصدرين
▫️
بعد إنتهاء مراسم التشييع في النجف ينتقل الجثمان من مطار النجف إلى مشهد المقدّسة حيث يقام التشييع الأخير والدفن قرب ضريح الإمام الرضا {ع} يوم الخميس 9 تموز.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80367" target="_blank">📅 11:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d338d557b.mp4?token=GPXuC2QkJQu8_vwz1HgbGOLJFSqB4kH0wRI9VGtfrrmBTXJG1oEggSoL82dj7xdAZF1u2V072h883nmVtsad6QQh2PongSU6-ZffkKc5oof--n3P_4l7BVqM4TEqJnQD3G5O3g84qf3cKToYOkuPdxYH2EU8-tMr6CKUJDSx8RUfw4godWzuTySn2js68KP7lN8t92zWaKI-u65DYYOIwmYIkSkE7VbMoUrNwwXAycJqSofwZvgzKMHSei_WHb7LwP1JdnDJKicbEkwDlwipO-5yRpuaCqw4TknH-fFyHHKWuruGkflBsLVboEK1vBPNh1dKXLuYqfyp_8DxDaI7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d338d557b.mp4?token=GPXuC2QkJQu8_vwz1HgbGOLJFSqB4kH0wRI9VGtfrrmBTXJG1oEggSoL82dj7xdAZF1u2V072h883nmVtsad6QQh2PongSU6-ZffkKc5oof--n3P_4l7BVqM4TEqJnQD3G5O3g84qf3cKToYOkuPdxYH2EU8-tMr6CKUJDSx8RUfw4godWzuTySn2js68KP7lN8t92zWaKI-u65DYYOIwmYIkSkE7VbMoUrNwwXAycJqSofwZvgzKMHSei_WHb7LwP1JdnDJKicbEkwDlwipO-5yRpuaCqw4TknH-fFyHHKWuruGkflBsLVboEK1vBPNh1dKXLuYqfyp_8DxDaI7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اسرائيل تدبك في الجنوب السوري وعصابات الجولاني تهدم بيوت الشيعة وسط سوريا.. لليوم الثاني على التوالي تشهد قرية المزرعة الشيعية في مدينة حمص عمليات هدم واسعة لمنازل الطائفة الشيعية بهدف التهجير القسري وإخراجهم من بلدهم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80366" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80365">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a6b70b88.mp4?token=j82Z2VB5smTbYCSbez7WIpzKsspn8V9kREaWFCpbqYbKzlIifOgmQeOBwh46WotXnEtkVBREUw2cKeITdGi93rVKxC5ELeQcIiPHYHHEUZZH3wnhDbhOZXFYFx2-Fa9ht6RbwCYYcpC50Ao9CrNecBdd1irqJUviJA3Yb_nb5DUg7lXrGCjvM0IqkOvO5Grtainyob5bLDV2RHNmHxcfWrxj6z0bkqBJ0c0Kx_qC4EvRZVwWsI1iYlIzFS-zTxnS-ddyVomaEpSORIZCSSe_bJj3KFlo6QbhFtR1CuL7aqXpfP3G5oRt7Tyvq5TGIDnilE3mZwg2smWxkMDo3hnYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a6b70b88.mp4?token=j82Z2VB5smTbYCSbez7WIpzKsspn8V9kREaWFCpbqYbKzlIifOgmQeOBwh46WotXnEtkVBREUw2cKeITdGi93rVKxC5ELeQcIiPHYHHEUZZH3wnhDbhOZXFYFx2-Fa9ht6RbwCYYcpC50Ao9CrNecBdd1irqJUviJA3Yb_nb5DUg7lXrGCjvM0IqkOvO5Grtainyob5bLDV2RHNmHxcfWrxj6z0bkqBJ0c0Kx_qC4EvRZVwWsI1iYlIzFS-zTxnS-ddyVomaEpSORIZCSSe_bJj3KFlo6QbhFtR1CuL7aqXpfP3G5oRt7Tyvq5TGIDnilE3mZwg2smWxkMDo3hnYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تقوم بهدم جميع منازل قرية المزرعة الشيعية بريف حمص بالدبابات والجرافات وتوجه سكان القرية بالذهاب إلى إيران أو الضاحية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80365" target="_blank">📅 11:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
ميناء أم قصر العراقي: استقبلنا 80 سفينة في حزيران بينها بواخر عملاقة</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80364" target="_blank">📅 11:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpOZ8LIs9k6zo_5Fvo80TQpzxNQouKsUYbg6Obvhrg1n0onY0iB5tza0M3T0wlFFFRSyrLuE6U1oViYOfM5w-KO-mChLu_G8dFRsrWSLXevA3e_uRH9si3grWCzw2SmmvROF_a0mBjeF2AGJ0G9EyWu0iGd257T8QAY9oCo1BYwRDdf1YEfEu4cjMm2agbe2ifszOIGOXNUk0dc6fffbDB4SbERDw7kda7hX_g5jOSM3lGQdlvH9DP7WuAm77RMxEOaZkHsOYIE99gLViw-b8uwNF-5FwtgogB27TVQdFrZl1afw1AafnyTm-meY0Tzkk2Ek7nmsOaCRMiat-NXmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إعلام كردي: توحيد قوات البيشمركة شمال العراق ولم يعد هناك شيء باسم القوات السبعين والثمانين، وسيطلق عليها قيادة المنطقة الأولى والمنطقة الثانية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/80363" target="_blank">📅 10:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
رئيس لجنة الأمن القومي بمجلس الشورى الإيراني: مضيق هرمز الاستراتيجي جزء لا يتجزأ من السيادة الوطنية الإيرانية وإدارته هي مسؤولية طهران وحدها.
لا تُضمن السيادة اللبنانية بنزع سلاح المقاومة بل بإنهاء الاحتلال والعدوان.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80362" target="_blank">📅 09:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrHep2yrx9u5Yr0Qjfe9AeHykG9I7g3uRKl6URTLkHcmFrH0KfGVyD9TiZOAnDAz_LAlLg1v1KzBCKXip4jiJ-cqLNvcSdsuYE_nYXUgIwvhPJ53awh7deSul8wm9p4sh-fMoQLBBLlUxHoBgF7NonsG5wclmUVefbUV43dal2RYpwLZKjDslLMsREzsxlR7PQaDAWkXIFSlvR5McPM_68rDjE7rmGupnb7Acu6qcvf38T5H2EmRZH0UsXdcoKfTzab3jPTmXgwklEFpIV959nUcU-V4FcevjcmV_76tV_warInFDw1Qrke_RHitZLgHyEH8j0y4HArTscG_zJzLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Despaseto</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/80361" target="_blank">📅 02:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في بافيه مقاطعة كرمانشاه الايرانية،شهيدين كحصيلة اولية من الحرس الثوري.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/80360" target="_blank">📅 01:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a452ae09.mp4?token=LEqCMUr5_Lq4mIIdbad2IbCZARVBPEqvsuKzA8i9uaafRoRXwkQiMhuj_ZGAXVbxp_sWdlTtxi_X8n5DMzwgueYjO8yItlBbMltVcDQbDZfr5yo3xaE2-LVWAIK1wzSBcIAIOCqSU-6YtL_8-zR5VBNR_KKbB8Vo-p0f9FOHpIforSYz4TAeE4jsho-hq8oZomvm7nZ4TKIDv0fLhrWSrXWfPpcaCnrpZs1dZuAg6PjMNVeJ79p7o2xkQaKUxoRdXYU5Ksj62J1yatHAl3oGZ_9Yk3ylq_r5wSJlkx9p8eajCG1c1ylemZhXhPpYr_FRHh0QNUsIX6dK3-9TNrO-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a452ae09.mp4?token=LEqCMUr5_Lq4mIIdbad2IbCZARVBPEqvsuKzA8i9uaafRoRXwkQiMhuj_ZGAXVbxp_sWdlTtxi_X8n5DMzwgueYjO8yItlBbMltVcDQbDZfr5yo3xaE2-LVWAIK1wzSBcIAIOCqSU-6YtL_8-zR5VBNR_KKbB8Vo-p0f9FOHpIforSYz4TAeE4jsho-hq8oZomvm7nZ4TKIDv0fLhrWSrXWfPpcaCnrpZs1dZuAg6PjMNVeJ79p7o2xkQaKUxoRdXYU5Ksj62J1yatHAl3oGZ_9Yk3ylq_r5wSJlkx9p8eajCG1c1ylemZhXhPpYr_FRHh0QNUsIX6dK3-9TNrO-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
توثيق من تجهيز موقع المصلى لاستقبال الجسد الطاهر للسيد علي الخامنئي، استعدادا لإقامة المراسيم جماهيرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/80359" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vji4YOQty-5xQHssAANkXVuw0ZJwcU4zXPozXqQ0GodfHFsSQXLzDeG9LjhEjXNIRs2HzGQ3QdEV-O82QyM7NrNTUARW7UwLqKWlKD7QPI_TVk5K9ccxllZ5_ZloxixigS804G7UUkq2o11b8nuP8Er4iwHQsaIRBQs5munVQ95W7T4PSSUAIxpKXfGrTYZ-TNYh2trxgqCIwph8b4QCiyPwtNkSK9Z1zex-8JUjwOKoNUOpOPkkLat_kUOpTJN6924re69qUVcu8LMQngyzRoGaxHqICd-HGPkp_x8fHL1l5azqJ11W-GrcG52nDhwNPZwpJAQ5rH7DIRmz4ETw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وزارة الاتصالات العراقية:
الاتفاق مع شركة فايبر إكس على توفير الإنترنت المجاني على طريق بغداد - كربلاء خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/80358" target="_blank">📅 01:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
انفجار في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/80357" target="_blank">📅 00:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
انفجار في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/80356" target="_blank">📅 00:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80355">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مداهمات في منطقة زيونة شرق العاصمة بغداد للمرة الثانية تطال منزل وكيل وزير النفط</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/80355" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80354">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
اندلاع اشتباكات مسلحة في قرية يارمجة بمحافظة كركوك، شمالي العراق، بين قوة مسلحة والجيش العراقي.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80354" target="_blank">📅 00:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80353">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XU80i2_o7B4UVL_BUaRPbttqLDKratxW75vo0rJzBYDfAVQhOLqBLDUV1uB-_1rbo8laNiS1mCaN7Y8xvuljB8p78EY3TrxEemwmT5Z85iyOv7tJuqRrbzr2T46RHTJdXY-JbwCYxbKnUU9v4BDOSXs0U5IX-3gS_OvMQ0lcOQPmtfs8aFGvp3F8hg8ssoU48OaUP9qvqIiDdbpQTj6FBvYk40CtXeb54GRbvVmNM6OyhAnC6KQZbReVQkxnggMnKR20NBySnM1_n0ZGd3KFshwqVmmyMcHEVjhnicfjn77YQPT-0rqVxW8A8azfflQOskVLKLAySI4tvIg8Sm7RAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
توثيق من تجهيز موقع المصلى لاستقبال الجسد الطاهر للسيد علي الخامنئي، استعدادا لإقامة المراسيم جماهيرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/80353" target="_blank">📅 00:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80351">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT-xJarDbd8aUZ3pTKME4yOCSewZoCGgQLV5dzT8Jd_7um_du-gbjS1MfBm9slJcdnOZgUDIgJW5Gljd4MSwKVdpZ7pg7ti6boqMTeLQirlH70u-_EaW4oQ143RILtTjP4WTgXhe2AEHa2vN-GPnN6fhD7dJSfyyrnSY3n7gGepijCy9sgQk7PHcRrXxV2FiSF__pRuGqH4Gu2-k-j0IfKwVa1kFK4FKjPcragAwLgFKaXF4rgTyXD6AzSUVCitlUE8yFaWdC_yMgp7E7P1uqCzyc1WS3MsVGB7nm9GOIJiFnFxHJmmAW1ghFVTNNxFSMc3XtIX0_CG4NJpv8lL-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7da4bff7.mp4?token=SatvQe3x9QYIXGrtpwPTSW7YuRFcaaclq-00c439tkjNcaAyk0KBjNkvqQpfT3eO8Rv4iVuCWmbRG8rdkEHNE8T3FrR2jfYwsHUYG96UG-HXQ1Oz71r43tFFGZQ2iyGSip5Nz5z9JMWALAOhv4fnVE5AgzDnBfCX49yKnbtnIKfY8YxJyIzOOxtEILFa74ODsXj7dpgD0ruKlOvGBtg4G8A7Ttdkxj5SzO8eWdyIOqnTuOM6nL3bS58PQwQlG_zTwFD5Rw-ATJw87P7Y13wlRj0GmO7CF5317fCWzrkN1zg8d5YJQatRF-syjAfA_9Apgx05QeMgcpFFLARoKO2A1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7da4bff7.mp4?token=SatvQe3x9QYIXGrtpwPTSW7YuRFcaaclq-00c439tkjNcaAyk0KBjNkvqQpfT3eO8Rv4iVuCWmbRG8rdkEHNE8T3FrR2jfYwsHUYG96UG-HXQ1Oz71r43tFFGZQ2iyGSip5Nz5z9JMWALAOhv4fnVE5AgzDnBfCX49yKnbtnIKfY8YxJyIzOOxtEILFa74ODsXj7dpgD0ruKlOvGBtg4G8A7Ttdkxj5SzO8eWdyIOqnTuOM6nL3bS58PQwQlG_zTwFD5Rw-ATJw87P7Y13wlRj0GmO7CF5317fCWzrkN1zg8d5YJQatRF-syjAfA_9Apgx05QeMgcpFFLARoKO2A1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏شرطة موناكو: انفجار كبير إثر عبوة ناسفة ثلاث ضحايا كحصيلة اولية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/80351" target="_blank">📅 00:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80350">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a4a7c7ec.mp4?token=FLsV61mYniWm6wFJzloF6E6Xhaq5CsaRXxHzaDmOzuO_CzdGNcWC_rfQe-l9-ofGfg_iPgFiSTOYT3F-MFwyu6tNWAzom2EwEUmUQloBhmlqZxWyiH5K8fSx64_UvPMKbZUldwB4VFT9WuVAk56ruEgoLt857GeQaxA53L3MBoqGKdVB6MkAP4SMfCtL4dm8rFl3cifDGcOTksDgIhYcnzQ3NbTVMzVzAq7olZzw2aboUusU_xavKIzgwwjwLIGflQpeVgo4xRAJMiQ4C2B01fKvjV75Ljb8U9NUxGEC8-rN5Y946vE16BeK-o5ElJbs3p4dvmW_czL0S8fAcXrzkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a4a7c7ec.mp4?token=FLsV61mYniWm6wFJzloF6E6Xhaq5CsaRXxHzaDmOzuO_CzdGNcWC_rfQe-l9-ofGfg_iPgFiSTOYT3F-MFwyu6tNWAzom2EwEUmUQloBhmlqZxWyiH5K8fSx64_UvPMKbZUldwB4VFT9WuVAk56ruEgoLt857GeQaxA53L3MBoqGKdVB6MkAP4SMfCtL4dm8rFl3cifDGcOTksDgIhYcnzQ3NbTVMzVzAq7olZzw2aboUusU_xavKIzgwwjwLIGflQpeVgo4xRAJMiQ4C2B01fKvjV75Ljb8U9NUxGEC8-rN5Y946vE16BeK-o5ElJbs3p4dvmW_czL0S8fAcXrzkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في الوقت الذي تلاحق به عصابات الجولاني الشيعة في حمص وتهدم بيوتهم وتهجرهم إلى الضاحية وطهران على قولهم.. جيش الاحتلال الإسرائيلي يبث مشاهد للرقص والدبكة من وسط المدن التي تدعي حكومة الجولاني أنها واقعة تحت سيطرتها.
نشوف اليوم ينزل بيان إدانة ولا تبع مبارح بيكفي
🙈</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/80350" target="_blank">📅 00:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
‏
الرئيس الإيراني:
سنلتزم بمذكرة التفاهم إذا التزمت بها أميركا.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80349" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80348">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
‏
شرطة موناكو:
انفجار كبير إثر عبوة ناسفة ثلاث ضحايا كحصيلة اولية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80348" target="_blank">📅 23:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80347">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba122719bb.mp4?token=umHpBVoSgxNlG_lTYvca7Tnt9QwIywvzGo3HOG6G2d-c-nt55pVzK5YGbtTNbpQWMKRIErH3W4iI2o-n8JyjDUD3Xo6SCP8QSCESe-oDlgBLHwZpZJc-qSZbC6rsCQsh14YKeFqkDzVaT3Ebl9AuYyd5CVz7P70eDoEn_lBKy8_0bYrNoW-Ewy5Dii1FqdaDVoM4irUaRRXcac0bRbobk9lUnDfjg-eMm9Mhn8UHFuwD9LL3a18vdOW51Bn-inZCA5dKJS8YkgzAJndb5SqFmGrWwnco8SFnxEUz2am7pWi7Kjt5is_dHCovA82w5sBI3rhrvJWj9tEfkUJA0D3p2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba122719bb.mp4?token=umHpBVoSgxNlG_lTYvca7Tnt9QwIywvzGo3HOG6G2d-c-nt55pVzK5YGbtTNbpQWMKRIErH3W4iI2o-n8JyjDUD3Xo6SCP8QSCESe-oDlgBLHwZpZJc-qSZbC6rsCQsh14YKeFqkDzVaT3Ebl9AuYyd5CVz7P70eDoEn_lBKy8_0bYrNoW-Ewy5Dii1FqdaDVoM4irUaRRXcac0bRbobk9lUnDfjg-eMm9Mhn8UHFuwD9LL3a18vdOW51Bn-inZCA5dKJS8YkgzAJndb5SqFmGrWwnco8SFnxEUz2am7pWi7Kjt5is_dHCovA82w5sBI3rhrvJWj9tEfkUJA0D3p2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تحليق مكثف للطائرات المسيّرة في سماء العاصمة بغداد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/80347" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80346">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ec5551c0.mp4?token=fjlbq2bz8QwKvXiHiVkA3YvAL67uC9XVAoCjl0TMjgfD6PHMk6-5T7d2OZmUSpbhDbsWHci6ZAQDXUdANnDS9gE_4sSlTOYFGjzzcbHSXtxSIikis0t8_KeTV0HObqSeGMKQJ1DnJLwxsq_ID4r4HKaFNmfsj3a6YyRZoEC8x-fmHZSAdxjstecSxKZM0BK2HCmw9isVuzl1TjmhtK4f8VgHOOBecpN5AUSr8djQ1fqOOHjutFec4yoMlHMtlelUazPPDbssH53ZC298axTzwxtdrP2P7UoLsnLMd9kdIwju5AdL6KgXAEvUR0t1LGnl6_OeC4VYQ5tHsk67PwI8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ec5551c0.mp4?token=fjlbq2bz8QwKvXiHiVkA3YvAL67uC9XVAoCjl0TMjgfD6PHMk6-5T7d2OZmUSpbhDbsWHci6ZAQDXUdANnDS9gE_4sSlTOYFGjzzcbHSXtxSIikis0t8_KeTV0HObqSeGMKQJ1DnJLwxsq_ID4r4HKaFNmfsj3a6YyRZoEC8x-fmHZSAdxjstecSxKZM0BK2HCmw9isVuzl1TjmhtK4f8VgHOOBecpN5AUSr8djQ1fqOOHjutFec4yoMlHMtlelUazPPDbssH53ZC298axTzwxtdrP2P7UoLsnLMd9kdIwju5AdL6KgXAEvUR0t1LGnl6_OeC4VYQ5tHsk67PwI8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد توثق دخول قوات الأمم المتحدة (UN) إلى قرية عابدين في ريف درعا.
جولاني وينك بدنا البانجان مجقجق باللبن
😂</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80346" target="_blank">📅 23:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80345">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
المحكمة الجنائية الدولية تفتح تحقيقًا مع مسؤولين كبار من الإمارات العربية المتحدة ودول مجاورة، بتهمة المساعدة والتحريض على ارتكاب جرائم وحشية في إقليم دارفور السوداني.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/80345" target="_blank">📅 22:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80343">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
الإطار التنسيقي يدعو جماهيره إلى المشاركة الواسعة في تشييع الشهيد علي الخامنئي في الأراضي العراقية</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/80343" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80342">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
مسؤول أمريكي:
دورنا يشمل استخدام قوات أمريكية على الأرض في لبنان وإسرائيل
عون وينك السيادة عم تبكي
😫</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/80342" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpin0kLncfiZ-D9DTg0PXwWX_vTJUjxJ5elV-tzfmYwHE6hBcaitUGH-xf-lFE-7T5JlpNrJQfDhtLEgTzyyYlMZmIehwb05_EFPjJK7DBUXPKbPZ9omi3FbfJC3xLeVc9RFh8lysBWSzuTL5BtFOSvHBfllx2tHNMQHYaOffEcLjTf-1c2M9hbd728D83r2II5WhJEhHrpEahEUMjn_kBb88KnvH-LvbcHlGXjQUO-NSLgk0olPawQCHmm3AE06vHjPnHIxzvJUDdgs6WhimoHE_tFcitcQJPFdfd1v0IBS175B3Ou6HE3fmLzQrSk6E6iwOGmOHzL2Ttviem3SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwuguNfK15CmquGg7Qj5UVva4JirjiUGe1ss1t4oTtaQf-MVhMSH7OYnFKjpiYOr1bEandFwL8weJ0PJlzF3P1-EwwjembCRsHInYy2ITRcLSvmYQUfFAChlWs0IGCSqhU-Za9rC3flT8VivT0iG2bQYMsaf4_dqFRRCE2FPSovaC4wLvcVIuUw92d7ZUNsvQNCVYgYhIG2z-OXKWzzuAIkOjGPt2091CFuSwVnUp8-j-_a3YJbjPvRD07nXjqKgILLdePTJZksmGR1OAA-9E7SNs-2-83gcIpg_NoSgQDUPBp2n-6ClC_wuvKvZbf68rvG-y9HqNmrVOrDVT43MaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhXd7GRmfPnwbTq_GDocPTyT7zR13g8LkTvGvZ-Xy1Idu1wCt8Sc7BHNq318Sw9JTWLLzqeacv4Z-AyydmWU-t0MT2Vwe47lPcuMUEXUYZljIjcMFnGM-o3nTiNXTCN5PLdExR9hx_9mMB7JAwSZHcNs7LtA_09GVa-Fw1Ha70xreW8FPN56bR8rww1-Lb1hLfZOz0WljBam0VFsyHMKPVPdlHDlneMx30n9D5FmU9xKwSLVKYKOz-cOI72Wy7rmzj67qTogELhdYTiu2xkv2hwzvmyUEXwJ9xMa7F6CXwoVwyt6dnxRAlWmk_lTILIlIZrLuSSlWZgue-UMb68LmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSkuJGYbTkd4xS4HBTgRm-hEhsolPWYglwx-tVQsBTfN7FO2M54R53b_b8djL8IZrHOF9dFHwpCpYjVclTIAOAvFMtfBhX1pATztaYbD1XKDwjjMLhetH69lmivRr5rl4bjYhED4wHGa9UIPTVnV5OsMDEzZchF5PJ0g16VLVKoIdpdpKDcpAQCam5MX4M_7c3JfxpiMfe0JQD1yvhG7uqFkJu8Jk83FH9Q20R60pDsOf6NqPUJ1yjGzGA-XqUTiSjWGcc3r5gD5lLAf9UwFxEx7essjCzJSSB1YnKYgiv7RqSzHMrA9QxhSoBLIPQkXD9DJspRbpvHKW1p0QuU7jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى: التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/80338" target="_blank">📅 22:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى:
التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80337" target="_blank">📅 22:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80336">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي:  وفد خبراء إيراني يتوجه إلى الدوحة لمتابعة تنفيذ التفاهمات.  زيارة الممثلين الأمريكيين إلى قطر لا علاقة لها بزيارة الوفد الإيراني.  لن نعقد أي اجتماعات تفاوضية على أي مستوى مع الجانب الأمريكي في الأيام المقبلة.…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80336" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80335">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=nehWEG1GIekn6BH6Qu7G_3GteLJ9-t3NClNge5jNYT11xH2TZDpoflYHQRElLcynDiFiOeME9lDghuQWqKdwwX98vXKmIYUlvGjZYjA_gsK4nqIg1XLpzh2yxP0GnBjcmY1hITUV3MuMxltFBvmQ1XU2180w20pV9ujJTCppElKg7VtEPVdhqFxbgJCTQHrof3HFbxMh9QvAOYY9KB82DNy_H3AQmEF7QKMOblLSDWBEMSYJeIYJX0scuq1c7q_EUWkSKIsfo4vnex5K9BzrpNp5zgdzIy17h6RipjVrm7yz1NOf1lwjIX2WWozyyk4kjC4dl0WuJ8PlkdQvpkSYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=nehWEG1GIekn6BH6Qu7G_3GteLJ9-t3NClNge5jNYT11xH2TZDpoflYHQRElLcynDiFiOeME9lDghuQWqKdwwX98vXKmIYUlvGjZYjA_gsK4nqIg1XLpzh2yxP0GnBjcmY1hITUV3MuMxltFBvmQ1XU2180w20pV9ujJTCppElKg7VtEPVdhqFxbgJCTQHrof3HFbxMh9QvAOYY9KB82DNy_H3AQmEF7QKMOblLSDWBEMSYJeIYJX0scuq1c7q_EUWkSKIsfo4vnex5K9BzrpNp5zgdzIy17h6RipjVrm7yz1NOf1lwjIX2WWozyyk4kjC4dl0WuJ8PlkdQvpkSYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي يجوب سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80335" target="_blank">📅 21:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80334">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭐️
هجوم إرهابي يستهدف عجلة في مدينة سراوان بمحافظة بلوشستان الإيرانية ؛ إستشهاد شخص وإصابة أخر كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80334" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80333">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">البيت الأبيض: ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80333" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
