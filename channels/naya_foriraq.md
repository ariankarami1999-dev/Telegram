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
<img src="https://cdn4.telesco.pe/file/KTx0vRtDfJYJQ8lWqQgGnbxTV8hiRSFMfJrmFo4cCw4vIGiUz8apGxcnKZgPlOVDkg1wzGr_ko8yBInuLOczDdiwgM3nmz5G9dqkutoapGaYGl5qSXBcWjCPZJM07UX8b826KKm4mB56xN2zpNkcv3oEo-qnOkc0xQLBDtOvCA4v7mDoqksNRzkI39_JoM1Ot0laT_iYONi1Z8cuW9eSmUU_00jQBcDN8p1sZ1KSccTNOFaNKz0RCle8IV5rvXTacxUzZuWv3alQknT_NjVgY-q5QeGo5aE3meSj3fQBdFDV1SZdh8unAtPHAZqrvr_3cv5hwixVqCSe6gy9AMPOaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 03:25:38</div>
<hr>

<div class="tg-post" id="msg-86973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48497ffdf.mp4?token=eLc6SjpLiYbm3U1_kiCjSs2Udfbw8lPHlK8UpWpZ-LcHd5WlBBwyY2RhmxexZUUqEtsCq9Jndl83JnHCOGGicLbtMj004S9qBSmDBYK2nhkHH2I70HgUUO5VxzO4_LcALd3e-abujuY-2MbACeP8iE3brTrfDS9Rx_ugU4a8JEoVrW3pTmVAOJxOG_n_FwrhVcRmUG_eRC1O8bHfP9OlBXE0TImiuhTkyjsgnSw3RhrUfP_klxEDUpmxWgK8N7JNgbP4Q_QCWXdssB4_sRBfgsZttjiK7sKlYZQavn3JcqJ5mRSSp-LltgLCfJPPqNed4E9NBYmpVboqWEGHjK-T5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48497ffdf.mp4?token=eLc6SjpLiYbm3U1_kiCjSs2Udfbw8lPHlK8UpWpZ-LcHd5WlBBwyY2RhmxexZUUqEtsCq9Jndl83JnHCOGGicLbtMj004S9qBSmDBYK2nhkHH2I70HgUUO5VxzO4_LcALd3e-abujuY-2MbACeP8iE3brTrfDS9Rx_ugU4a8JEoVrW3pTmVAOJxOG_n_FwrhVcRmUG_eRC1O8bHfP9OlBXE0TImiuhTkyjsgnSw3RhrUfP_klxEDUpmxWgK8N7JNgbP4Q_QCWXdssB4_sRBfgsZttjiK7sKlYZQavn3JcqJ5mRSSp-LltgLCfJPPqNed4E9NBYmpVboqWEGHjK-T5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شكرا بابا انت نفر هندي زين</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/86973" target="_blank">📅 03:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86972">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyTaF6AQdpMpkpfyO8LQf-4iKFMmsyY9ToMhGhiJwFNUgJHvw2Im3pLtMq3xBqwxzgQXkDPDPO0oAf_-vY6t0Ug068sEH06RhOQAQhMWusGPj7LpSMrfPY_ha5H_GZ4OmZJBpbrhwxHXaC7j4UFWp5NWXo8UXshmCj4Zd90OWGNW-gTWSveOabrs4kXeY1smxM7xC12ytVYf6BCwmpAW98nep4U3MHsPrQ22KXZs0d0N6_4hf6EfUf4RWcH47o6Oe7a-vuVjVYF12-htWbwUX2YddQNPqLFCV5bP_fjSlY4sqnYGX92EYHIINdBSVR7xSg3e7rVh3uJphlXrWed4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمار شامل في المدينة الصناعية بجبل علي</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/naya_foriraq/86972" target="_blank">📅 03:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86971">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/naya_foriraq/86971" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86970">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4T6BdaSXeTZZ2U7reMlDeGZ3UJzfjeT6qB5HQmN-unJRWcaIbxDJRsme8FsbgypBHC6ZaAkWd_8kjkV4mMNxpSgEglhaPou3YB0lkRXhcEjGu8s4s7lmf1EjTkfk9j1U6LTXxYwyOv3jEmXWt06bCaRSqWXHZIfIcw-o3tfmKG8RhAdf1JIdnAvG6Ha8xhZfCJ7r2jhpwwcExEUJFj1EPQQkFk6ch4cAM4ivy3Pg2btj33958Wvt7R0wNseuXX5H1H5Rx2xx9GtY6nSYBD-BJn5a3uFbj_L-k2jqVYVVAodsIcPSOpMomejzBtrTUcGAOLLzwX5WzfYIypkZkn5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة في الخليج الفارسي بالقرب من مضيق هرمز والنيران تشتعل فيها</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/naya_foriraq/86970" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86969">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/naya_foriraq/86969" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86968">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc5IMG0AW8FHc7s6BU1dbrGic1APcfIL8ZItjtSI8iT5Hvncbuyu2sq6tQeikyWpAF5zMuLa6KD5XYxUHrPTihUCJLKOWsUnnxoCHR4itKMaDNhaIqZ_BFUMh71lu5GWrvBSne05IRxok4maD2VKK5djozDdCN0Ypx7e7FbaQHxLtotEQLqB9ddG66YA8zdk-tdxWdXSbEhbkgnsGAslCVW1H8o8vg2k1cQh7N6uoBczZdnZrvlnBBMYoNr4sUOFxb_kpWcKB1oVVLeHBFRaRE0iviYGQL2YeVVgLDShvEIA8m9uKpy3hEdj53OptSWpSY6WXNSz75aj7yiRF0iYFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمار شامل في منطقة المارينا بالمدينة الصناعية في دبي نتيجة هجوم مجهول</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/naya_foriraq/86968" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86967">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/86967" target="_blank">📅 03:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86966">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ef471bfb.mp4?token=bSyFmX7TOImTSc5RlfOpMCjoVvMbLkFqCXXbmIH8wLqqWFa2AXpjr3ebZloVoef9Y76ctvmLV8EUY1F06HcXkRO4lj9kZWbY4YygK2jqQ9oaCEYszp98K3OrX6ZPGK84N3Je_JcJ8yZE7bBor9b1YbzBmn1akjoHTQ2JjBRHUdokPq1y22sAcADT4dvrHh-w7Cqsr_ONlKeLej3nRBUCcTbs4L-jhuB5pqOpyGqtuCaiuoy_ecoxvSMyP1V0ba1x1AEHuLrzLXk7u8MjFI7FnVaoiQDp0Snw2vBz6riVsWjmLjmviw2Pm5DCS61MyzenvcHThGPP7-GSIELkEu4-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ef471bfb.mp4?token=bSyFmX7TOImTSc5RlfOpMCjoVvMbLkFqCXXbmIH8wLqqWFa2AXpjr3ebZloVoef9Y76ctvmLV8EUY1F06HcXkRO4lj9kZWbY4YygK2jqQ9oaCEYszp98K3OrX6ZPGK84N3Je_JcJ8yZE7bBor9b1YbzBmn1akjoHTQ2JjBRHUdokPq1y22sAcADT4dvrHh-w7Cqsr_ONlKeLej3nRBUCcTbs4L-jhuB5pqOpyGqtuCaiuoy_ecoxvSMyP1V0ba1x1AEHuLrzLXk7u8MjFI7FnVaoiQDp0Snw2vBz6riVsWjmLjmviw2Pm5DCS61MyzenvcHThGPP7-GSIELkEu4-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/naya_foriraq/86966" target="_blank">📅 03:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86965">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBzyf0XGHYQoesL0QK0Q-Ln92reEkE67DX-7htCfNNq5pDZxTypPc_PQz9BL8pj6_WM_PFK1SXoHh0ZMFBtSmq4DoZYQ4JnEg46zxYgZvvU-tBSXyy1IiqXpRhRNqobNHPkpT10afZsKm4JLK5VpV_NlaDZQfML-vUG1vq2vkUAEQqk4pT64i5nIoEAOFvnrh0a-IJVXo9Svr6mD79kxNddikBQTMRqfsOUWLAJh6gVlJm5kx5oUIctsOkJKJj8OfeZRVve0zLtIOW31jeT_i5zRH7841b1PSH9uueZiadhSwE50Jyq8g-LtCh1iVnN_lM6rEwAOyDEx80fohsQMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي اصوات انفجارات مجددا في دبي المنطقة الصناعية</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/naya_foriraq/86965" target="_blank">📅 03:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86964">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/naya_foriraq/86964" target="_blank">📅 03:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86963">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hconG9D_c-3jtcM9VgjF-t1NZPe9GcJrKyh6OuHJiCSLd_2XeJUArCkv59tvNTKZfhi3S5iTl8Z5c42UGFkpq2yheBb16Rt_Vr_FrUJdJ9pLMo2Eg9ZQ_p-pCNrj3tpV4wDhmf02kIXRO71z6WiMzi58RDrGtGYBbaSfRbrhMebUid63FwNkHNeezYtGFs2OP2J_zEuURYxu20O1eQvDeR0yCKh6xSMTQLr77aLuTVY43FSGOIQkHCnyHQvnMZRSWKGb7wQj4FJmZst_iE1BS_mBtUPWmGj4mEHxXi26CUc99thl1vcn3iCU8l7jS-cWqi0dF7PYHE_LvrjzmBFCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/naya_foriraq/86963" target="_blank">📅 03:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86962">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/naya_foriraq/86962" target="_blank">📅 03:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86961">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/86961" target="_blank">📅 03:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86960">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474c99c5b5.mp4?token=JYUTVjvZmctgYrR8lIEV-uvRx-B4LmSFdlhcEn9-Y66bIw_TRsFRAJvxvA56LRl9S5GcbRcu7vP4-MuaQINZpY-o8Ncpo4-EQVbbGXFerVS92llvCHdJiDoqP-60VfLsDhV3O6dudgIede0rEnjleB644yzsiKVsY-xn-y3E9Oqau5BQI-2v-Tf1ZRncTvHGBk5_PVEi2gi3vP7iI1_ctFVUBJ0Yh5oTAlNHa5o521l6UqjKCRMzSD2AHfPePUvXCz41MEGahuuO1BkSAf72G1iykzPxYRFdW7W2x9FoQ2LJcwDDJfPt6N6de7TYt7fTFowkP70clXWWh6RJyifElw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474c99c5b5.mp4?token=JYUTVjvZmctgYrR8lIEV-uvRx-B4LmSFdlhcEn9-Y66bIw_TRsFRAJvxvA56LRl9S5GcbRcu7vP4-MuaQINZpY-o8Ncpo4-EQVbbGXFerVS92llvCHdJiDoqP-60VfLsDhV3O6dudgIede0rEnjleB644yzsiKVsY-xn-y3E9Oqau5BQI-2v-Tf1ZRncTvHGBk5_PVEi2gi3vP7iI1_ctFVUBJ0Yh5oTAlNHa5o521l6UqjKCRMzSD2AHfPePUvXCz41MEGahuuO1BkSAf72G1iykzPxYRFdW7W2x9FoQ2LJcwDDJfPt6N6de7TYt7fTFowkP70clXWWh6RJyifElw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/naya_foriraq/86960" target="_blank">📅 02:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86959">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWCg56KZExW3efdmtc64Df5tpuNVdGtJQ-b-yDEZBXuvl8u-Ecl19m4rAH53EdFrmiwOfGdRFEfMEO6Dic9mqp_UbnYkzg_9RXbLQLaTMllBrmBaLThjn0BUYlRduhH86js1H98eS_QtzMcq-z6mwrXNJt5zCo0_s6-9nLsE76Ga37N8jFg0hKv3tF3iFdhN4oS9ZGrRYgnU5NJcnIBICM51yHfnXMJ-S6B1PHeV0vlcZ86rnpaEbbOFWPWW3VFIv6J7AhFvhxzUPpzW0KIC2Iv-h7RCwUeK4yLh_7-1BVMkQSRfEzDefBkO52L4L7yQYykHAuizQ2Vth4zTP4pyMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
لفترة طويلة جدًا، حاول نشطاء المناخ المتطرفون احتجاز بلدنا العظيم رهينة من خلال توسيع نطاق قانون الأنواع المهددة بالانقراض بشكل كبير وغير معقول. لقد كان هذا تجاوزًا تنظيميًا كاملًا وشاملًا من قبل بيروقراطيين غير منتخبين! لقد عاملوا الأمريكيين بظلم شديد من خلال خنق إنتاج موارد مهمة مثل النفط والغاز الطبيعي والأخشاب، ومنع بناء منازل العائلات والبنية التحتية الحيوية. حتى جيشنا لم يتمكن من التدريب على أرض اعتبرت "محظورة" لحماية قارض صغير! الآن أعادت إدارتي قانون الأنواع المهددة بالانقراض إلى ما كان مقصودًا له، تمامًا كما أوضح القاضي العظيم أنتونين سكاليا في قضايا سابقة. بينما تحمي الولايات المتحدة الأمريكية بلدنا الجميل بمسؤولية، فإنها ستبني مرة أخرى. شكرًا لكم على اهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/86959" target="_blank">📅 02:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86958">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">احباط محاولة اغتيال ترامب</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/86958" target="_blank">📅 02:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86957">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxTR4lsW9kd-6gdPWjWuzxNqdcQnDMGKmMimfbKTveTL9C8jtVIFsz-5XRkOz85NzGr6Hwngz4l4bk3hFizsONAK_3I2cHrXh1rUyyIemRXcEOaG7BEylHwSTl3f6KL0LdVy2AIIKqpeaIhGnflOhIuc8oF7wGSymzqXdlatZw5gHSjXxcv7jeL0ybBUTPQ7Ju-h0f2TPFFK9nI1nc9_Pc2MWADzZb4wD_vj7eM00Sm9SJ0p7tkRKrK9KztKEQajPnxQmShloc0goh1r5w5IG-Y4dHj0rZ4Mxj9RuM5SIckCnjQaUGCaaVaGLhE9pc3fXLUBVEAKC2AMNxJdvcHCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احباط محاولة اغتيال ترامب</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/86957" target="_blank">📅 02:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86956" target="_blank">📅 02:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عدوان على صنعاء</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/86955" target="_blank">📅 02:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عدوان على صنعاء</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/86954" target="_blank">📅 02:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86953">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الغاء رحلة اسطنبول - بغداد لاسباب غير معروفة بعد ان شهدت تأخير دام 6 ساعات</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/86953" target="_blank">📅 02:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86952">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
‏
اعلام العدو عن مسؤول صهيوني كبير:
ترامب يريد التوصل إلى اتفاق بأي ثمن، مشيراً إلى أن "المسافة بين السلام والحرب مع ترامب هي المسافة بين الأحرف على لوحة المفاتيح</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86952" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86951">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-bJUs1tqkdzH17ftdTTeGseSuco1HN3Pe-GEIiXGeaut4JnVMFOxgFQF2TZOJzGR7rcoPo-TCYta9NYhPDWwjFdYurktUpw3kCPCqF__p8jqLdcAlbYZ_074r78hn8-cwl9OJP87P7lPaiRxSSVlu2ItV55GlJgHgrQB9D57xiz5IAJpvEQHt9JyJvyjVff9foOF6zNi_SUclTSqCxmA4bajD3cE_41ZGc-Hs4_OyUcl8LDi6Wq6ajV4KsUlWQDDHgUUv47xOcgSmaFewy77bQV_70mTQ-4Q0nkth810ZVmDclCYa16KY12MmLxadMHpgTNBNbgyF7QIT-rjzfa9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط لعبة "ديلاب هوا" بعدد من العوائل في مدينة ألعاب جلولاء بمحافظة ديالى شرقي العراق وانباء عن عدة أصابات بشرية بالغة</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/86951" target="_blank">📅 01:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCI_mqneC_w8GUBm_a1_rN3oDdyR8npzNDdrgnl1XyNg_7a9_c0t5zw_P1cjiBELS2RChZQNw389Qjp2Ab9w5BSlnVBre2bvkmrNwgH7QmrU027NmlQuBI19sQVtJBxR4vsCOv3lLaJWrfYftUOqVGssr2HLlyRfZYFls_Tct_ayUsDncVRz7NooSW5RWb74OBql4JLnmTKBh_hXy2e907jbtHHf6AJek8fgt9fxL7sWjIE4vC4Wwsu-KtgMiA68UM4J18XRmv1_46VKOE1gBIHJVHqSLP_FQjvQ7BM9OzEtoUXZ85niqjX9nl4t-v_VJbPgqb14gykhNsA7KnNClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsnyvxHQvpLiH9XDEGGn3NYAP-ftmMwNV42q8TL8bi-bg0iU5Ms7D5W4qW3IpMwfaOg194aVa-HgU2CfIRmHCZEG-NOttzyuSOIT1ki6ng8T_lX7IJ1JpiGV5r1Ybff80YQ0iD2d8RqDnRa25_AQQqjobXnXh6oFtZypCL77LIVnT68zx_jDhQk5ra27j9giOYuuebLfL7XGyj3Ftff8yNWiSPBi0nhmaUIiU65oYRgZlNwJUwB-6SQM6DMOxXgLWEnkE43IVKbJPBpHJwGN3bRNBC7OEUV9gNiYRwagYZzscuwssUEjm08cNyjfW4QGQre9p1Sak-kiQ_hT_TgNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqJmJcwXjFyV4XqYgyJ3m2qQlxlTqfqZgZZ1cH2SV29GVb_KiQyDYAJYpIVPr8MgBLwK0OCRj_uGI1gHFKFpn4C26Vl40XDVO1UJg2ssSaNwp8SHNQTozeBvwOkiN2dAnzaNKRLzZfhRCC4PsOjbe6eHY_jWV41yejxM8ReMl1EXYPMeyfX7Htr3BNZyuQcRayXn_iZihl_3jvo9IKvhArnj5mMh5BEl8A9PTAjHtjIh0we8b7vzVGLRtlRjyOCAK9ZL91r_sMRzf3tsVFlrCmLxBe0NuIW5ncSFUfEW7DQrnZoPTC3kOVs2eSrdfxHj8xJdjqJi53qG9h_ugsXljA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدة انفجارات في كييف بعد هجوم باليستي روسي</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86948" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d88d2557f.mp4?token=OgjiNhG3UneaSMnh5LNcqIIgUbMmomKJyKI4aG3mMG09DQpr42edsoBY3lGIicVlIo_atzopgvQ6oM8xBcU4r2oPRLxgD7HaDCT4GzL81Z5QWibwnVtMT-5bUhl3HNG4mk7XfYwlrbGLESDbT9i2-1Uqxq6vhZoYmpDlJDZtEVzhABeyzFfm11qNato4_Dw1nSxR_Lh95rvVwinHm6iRqP_WU49-R4gPib61PzGpgukM6sNv1sP2XwXolp_j-o9wAaJiccnDALaiO4zmN8pkUPF3HmrrdxVU2YE8buwRGb5p-JYX7L3Dng83MgU1cjbuVsWKteQJ0nZ2YFHs7z5PZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d88d2557f.mp4?token=OgjiNhG3UneaSMnh5LNcqIIgUbMmomKJyKI4aG3mMG09DQpr42edsoBY3lGIicVlIo_atzopgvQ6oM8xBcU4r2oPRLxgD7HaDCT4GzL81Z5QWibwnVtMT-5bUhl3HNG4mk7XfYwlrbGLESDbT9i2-1Uqxq6vhZoYmpDlJDZtEVzhABeyzFfm11qNato4_Dw1nSxR_Lh95rvVwinHm6iRqP_WU49-R4gPib61PzGpgukM6sNv1sP2XwXolp_j-o9wAaJiccnDALaiO4zmN8pkUPF3HmrrdxVU2YE8buwRGb5p-JYX7L3Dng83MgU1cjbuVsWKteQJ0nZ2YFHs7z5PZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لصافرات الانذار تدوي في كييف</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86947" target="_blank">📅 01:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a7482ddd.mp4?token=j0Nf_NANNs57A3LDQ3nwF6eiCsZDqWYFxtfWlx0VC5cy9arr8ywsTjHozNG8Ta-eHo3EeO-L3IILeeD_NdsBtGS391Oxm9nh1tgetBu6Atd6LtKlUM65MprVD-zGX_R2n6TL6mVxibbkMARP31a-rq3lIHytmAHbwwVa8-82EfQAjOtbce7kCrjHUKucvJM8QOU9cNzfIBwyOWqm1zX97PQeErQHhRnJ3DRkbmAmbBFGxSGlNeHAV4UgPNA5Bnglw9iewcappPFpm0uFRfqxVokbgH4TunBy9VKhgEv5ehyE3tFCWDNO9pnXk--ci8EnZFXJ0Kwh5DmeqvaecC6qRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a7482ddd.mp4?token=j0Nf_NANNs57A3LDQ3nwF6eiCsZDqWYFxtfWlx0VC5cy9arr8ywsTjHozNG8Ta-eHo3EeO-L3IILeeD_NdsBtGS391Oxm9nh1tgetBu6Atd6LtKlUM65MprVD-zGX_R2n6TL6mVxibbkMARP31a-rq3lIHytmAHbwwVa8-82EfQAjOtbce7kCrjHUKucvJM8QOU9cNzfIBwyOWqm1zX97PQeErQHhRnJ3DRkbmAmbBFGxSGlNeHAV4UgPNA5Bnglw9iewcappPFpm0uFRfqxVokbgH4TunBy9VKhgEv5ehyE3tFCWDNO9pnXk--ci8EnZFXJ0Kwh5DmeqvaecC6qRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86946" target="_blank">📅 01:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">في خبر غير مهم
🇰🇼
‏مجلس الوزراء الكويتي: الغزو العراقي جريمة غدر ارتكبت فجر الثاني من أغسطس.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/86945" target="_blank">📅 00:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86943">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات ضخمة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86943" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86942">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
- على الرغم من التحذيرات التي أطلقتها الجمهورية الإسلامية الإيرانية بشأن أي محاولة أمريكية لفتح ممر جديد في مضيق هرمز، فقد أقدمت القيادة المركزية الأمريكية، وهي منظمة إرهابية، على إطلاق ادعاءات استفزازية بشأن مسار في الجزء الجنوبي من هذا الممر المائي.
- زعمت القيادة المركزية الأمريكية أن المسار الجنوبي لمضيق هرمز مفتوح ومتاح لجميع السفن التجارية التي تسعى إلى العبور من خلال هذا الممر المائي الدولي.
- كما زعمت هذه المنظمة الإرهابية أن القوات الأمريكية قد ساعدت أكثر من ألف سفينة خلال الأشهر الثلاثة الماضية على اجتياز هذا المضيق بنجاح، على الرغم من الهجمات الإيرانية.
- في حين أن طهران قد حذرت مرارًا وتكرارًا السفن التجارية في المياه الجنوبية لإيران، مشددة على أن المسار الوحيد المعتمد لعبور مضيق هرمز هو الممر الذي حددته إيران، وأن العبور من أي مسار آخر سيؤدي إلى إلحاق أضرار جسيمة بهذه السفن.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/86942" target="_blank">📅 00:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86941">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51226c57d7.mp4?token=Zw2T2sbvUETKkSvkPdVvEooiLuwMPmvnKgHyozhZZ30c7_ekklLYLM3VW4eU7OmrxVPV3o70RmM8QUzEzb3qRx3IXrOcUpDNpMOTgt-wiW9DR1do0DwZ_Acd-CidlCRq1pha6f1yGbKuoRYKAixv1WrfLL7qmqX89OycMC_o-mfwilkQHFKINNAiIw-_tyPJYGmiyGtDJ5MWndXbzANnUAYimurfOZbddXRfjsckbL6BZAj9uMfmJiiC4uR6_Tsh48rxexQQ5HySbJOsRkCmuzOJ_FOLexyN6hJhFpfvfn5-aw02op4AIsEYOR9SsXg5VPV8ROe6ckKabhFZZfV1Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51226c57d7.mp4?token=Zw2T2sbvUETKkSvkPdVvEooiLuwMPmvnKgHyozhZZ30c7_ekklLYLM3VW4eU7OmrxVPV3o70RmM8QUzEzb3qRx3IXrOcUpDNpMOTgt-wiW9DR1do0DwZ_Acd-CidlCRq1pha6f1yGbKuoRYKAixv1WrfLL7qmqX89OycMC_o-mfwilkQHFKINNAiIw-_tyPJYGmiyGtDJ5MWndXbzANnUAYimurfOZbddXRfjsckbL6BZAj9uMfmJiiC4uR6_Tsh48rxexQQ5HySbJOsRkCmuzOJ_FOLexyN6hJhFpfvfn5-aw02op4AIsEYOR9SsXg5VPV8ROe6ckKabhFZZfV1Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر لنايا   تحرك لواء سبعين بقيادة مختار التركي نحو حماة لإخضاع فرقة ابو عمشة حتى لو لزم الأمر استخدام القوة ..</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86941" target="_blank">📅 00:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86940">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npbnX5vIV8g1YXKJpABXI1C94atd0vQWcjSaO0Lk9XmCQB21PH4tuzC_Bny6M519SzSYWLjpBZ6qXW7elS2GvGl8n6Ij3I7mvbcCLbrKYRzWs5xS4lE3haM8qp1JVNerxcrm6IwoNQeVwUmNHdn2tNRaYQQbVyCBH0pHgYSRhrTUyl-ktV7XdzrXd7_8K7PgxfhTBJj8Ygk-ZF8RbPWYO9VlHEPXUHoip2KzRPhl_i4TGxYqbOi9pIRPANGcafB238ojptnQU32c6cU42hzm-iefD5VNKbOhLGiUgcy4v1xzARFNdWsPWcgoj9DObClQjtChJ3AC4QNKJQmMFTuMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
القيادة الوسطى الأمريكية ساعدنا بخروج ١٠٠٠ سفينة من هرمز
The shape of ships that CENTCOM helpe after went out Hormuz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/86940" target="_blank">📅 00:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86938">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية:
بيونغ يانغ ستتخذ إجراءات عسكرية جديدة ردًا على تهديد اليابان باجرائها اختبارات إطلاق صواريخ "تومهاوك" الأخيرة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/86938" target="_blank">📅 00:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86937">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الاعلام الغربي:
استنزفت الولايات المتحدة الأمريكية ما يقرب من 80٪ من صواريخها الاعتراضية من طراز "THAAD"، وحوالي نصف صواريخها من طراز "باتريوت"، وكميات كبيرة من الذخائر الدقيقة الأخرى خلال الصراع مع إيران.
وقد دفع ذلك كبار القادة العسكريين إلى التحذير من أن المخزونات الرئيسية منخفضة بشكل خطير. ووفقًا لمصادر، ساهمت هذه النقصات - بالإضافة إلى المخاوف بشأن الرد الإيراني وإصابات المدنيين - في إقناع الرئيس ترامب بإلغاء الضربات المخطط لها على إيران في نهاية الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86937" target="_blank">📅 00:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86936">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏الأسهم تصل إلى أعلى مستوياتها القياسية مع آمال اتفاق صفقة مضيق هرمز التي تضغط على النفط.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86936" target="_blank">📅 00:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86935">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXqBq-S-gjr4D2Z4lFtRpTyv5VIl05kyqHOH_NVeq65mWbmgzyea3O6zIa8nc5hkaugxAAl969LSQuqk3feb-ED2B4ps9FsNhUUd5qFt-jjvt6vQnCcsHrIGGe9YN3h-dSI7ql4jL972h6wGuOEfXFyNUZzvsbn2K9LXVhbUdEZa2Zq6zxaKz0m_9LXFPFSKbOtpHc_8ZnXoVi8z4-MNDGwbDu3ZmaP8R1PoDNPiIUBiqe-kMf8-bwu6K2ylkVjHYmTBSZBCbIiDqJylbKiuVarUgiAGvrhVfseCvs1ew1VdtUhsyMK4NZUD-FivIddf_uBTo-xBysedoXtbDrHqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ما تو «نایا» میگیم ترامپ چاخان‌بافه؟! اون میگه (( داریم تو عمان با ایران مذاکره می‌کنیم))
بعد همزمان ما خودمون عراقچی رو دیدیم که عمود ۳۱۰ نجف چای ابو علی می‌زد به بدن، از ما هم یه ساندویچ فلافل با ترشی بندری خواست!
@Naya_Press</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86935" target="_blank">📅 23:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86934">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجار سمع بوضوح من الجانب الإيراني في الشلامجة قرب الحدود مع عبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86934" target="_blank">📅 23:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86933">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
مصدر خاص لنايا... سبب الاستنفار الذي تشهده عصابات الجولاني يعود إلى انشقاقات داخلية مرتبطة بمحاولة لإعادة ترتيب القيادات وأفادت مصادرنا ان خلاف نشب بين العميد جميل الصالح و أبو عمشة قائد فرقة السلطان التابعة لما يُعرف بالجيش السوري أدت لاعتقال ابو عمشة المقرب…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86933" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86932">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouBixjp_uqk3_xovtlgwnl4lRKPE7v9L9s_7ddz_jyNa4eNcg6uRWNo8PC4dxz1KJzgHeZC8d1mu2n9wjfvLQ0ucvmhpPDdrYNoJv1_UbZ5_yskZ5VzXqsQpUyLp06EW1yzqxkqrP4_hf35UvRp2Gq-nnAaQP6V7WINNNKlhF3qn4HxduMB4TnxKUu1sDaJxQFYDm2a5c9_-M1gtW4I0VODDtGGFoTlZ2hVpX7q0MiY6nRxynbay5HodmPOnyg4-eS-_JauROxt8RDJQISdR8IS0jhYw9jcPYsChV7wDzzix0NNLWIqw9EXM4SW8gvhftdqeHy_y1BJbgcrCV52vnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مصدر خاص لنايا... سبب الاستنفار الذي تشهده عصابات الجولاني يعود إلى انشقاقات داخلية مرتبطة بمحاولة لإعادة ترتيب القيادات وأفادت مصادرنا ان خلاف نشب بين العميد جميل الصالح و أبو عمشة قائد فرقة السلطان التابعة لما يُعرف بالجيش السوري أدت لاعتقال ابو عمشة المقرب…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86932" target="_blank">📅 22:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الاعلام الغربي:
‏أوروبا تتحمل تكاليف إعادة فتح مضيق هرمز في خطة جديدة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86931" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86930">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8713a50d.mp4?token=E4SbBoUKxUpARM3ZAzUMS5SYupNzb4zuMsNknBbcmf93d2zvEgvY4goa8Gh-CBjCgIfs7f-uB4YsnON-gcFvFymz4OFHhgzD0DqduML4Ug4AftrqE4Y9JXtkfXorSsjCbExhT7wDUNuCmySRDJbjXcqf84p5knR_PaNGKdaE6SEml4OSdLDR_U94GHyMQPP1Nlk1gRr8Md5APaF6tickSmyVNWUP_lkRNoFMUIhPGGMZ-APXSCR10tjpZMBmgnUcONs_QLwDcRxtvRHXxm-1B7E-W3xsJlaL8CgB1f30OfwG5t53eh1Mulco8mKTkl958WOh25HmIaiiGhjHunjg2VPLhlnV0t5-_Z0g0s4kq4ONTGcmdJ5DBuItOlez1lx7TVMoQgicsKy8GuDekot_j12-BmjwoCYQv3DHox0mLgotm5ronhKyKn-uEZDSpi1GkB7GDLdIxlAzgSo8l-ZP2V0hRDICzWKsUh3pi9M_OvouNw-ci_Jnsl5V5KVLUc_VmjeAYMdRozsQxcIe965fP_7dJRk_334D3Gxgsia27BfbI-Zu10KI6jmVuhsCaQPuDCPyRh_qRDJgXX19c8abmTBvUQYuXZsEAYdTrfrE8sjPziMfeMjb4Y1huM5TgCrkZ7Wq5D1DpYN4qXWl5safw5EFAqqRjHNX9OoITxu6SrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8713a50d.mp4?token=E4SbBoUKxUpARM3ZAzUMS5SYupNzb4zuMsNknBbcmf93d2zvEgvY4goa8Gh-CBjCgIfs7f-uB4YsnON-gcFvFymz4OFHhgzD0DqduML4Ug4AftrqE4Y9JXtkfXorSsjCbExhT7wDUNuCmySRDJbjXcqf84p5knR_PaNGKdaE6SEml4OSdLDR_U94GHyMQPP1Nlk1gRr8Md5APaF6tickSmyVNWUP_lkRNoFMUIhPGGMZ-APXSCR10tjpZMBmgnUcONs_QLwDcRxtvRHXxm-1B7E-W3xsJlaL8CgB1f30OfwG5t53eh1Mulco8mKTkl958WOh25HmIaiiGhjHunjg2VPLhlnV0t5-_Z0g0s4kq4ONTGcmdJ5DBuItOlez1lx7TVMoQgicsKy8GuDekot_j12-BmjwoCYQv3DHox0mLgotm5ronhKyKn-uEZDSpi1GkB7GDLdIxlAzgSo8l-ZP2V0hRDICzWKsUh3pi9M_OvouNw-ci_Jnsl5V5KVLUc_VmjeAYMdRozsQxcIe965fP_7dJRk_334D3Gxgsia27BfbI-Zu10KI6jmVuhsCaQPuDCPyRh_qRDJgXX19c8abmTBvUQYuXZsEAYdTrfrE8sjPziMfeMjb4Y1huM5TgCrkZ7Wq5D1DpYN4qXWl5safw5EFAqqRjHNX9OoITxu6SrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض سفينة مخالفة لقوانين عبور الحرس الثوري لصاروخ مما ادى الى استهدافها بشكل مباشر عند سواحل عمان.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86930" target="_blank">📅 22:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86929">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86929" target="_blank">📅 22:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86928">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jojGHxRXqfmhUs82_QcgOqBxRUNs2uuJAwTPiYoNkz3OmBk70RxcEEqL3Hp4SbW1_ZIDm3wVpLPQYApf6DCNFnGB8dul3-CGHTwDNnDgafmTu7GwMnJFx7ChTfP5CmR5G8oc_sl1c6CYe1UeVW9H0N8_lr7SjFFO3_RGDM3JXROx8hG-YaUl9evMiy55bn3KsTuTxEIEOgZuFtHjWfvNTrbVlXHudxyeEfVsH8JVZVCSJGgHUAz-4JfAZsOvDnH5n2GsUqVcWFjSNTthw7sFD0fl7tLISFrSt3L7TpZXqEDo2wKpAP1X2diRm4Jzz7rrt2qGKweC5FP_0s8DCa_pSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
الصورة حينما السعودية تحدت النجباء في حلب
بدنا كبة لبنية خال بخناصر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86928" target="_blank">📅 22:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86927">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ppSDKGZ8cQMPX2jAAoY6JW2CRR4vSN538d8DGM7L4sr4wHpWtpKjGcWnr-YMY8FrjknjgUmnbYuhr9PUzT_w6ibU3NOQcrkS6MuE_Gqe83oyUlNmc2vRDojxdah5YW-raIV0CUkrwqRjtvYvNLnz_eS8XM_1PWlC9nvPcGccQp-11kwq82gaGT7lp_sPDbTUWcnPgXAz0nrSWxQSrDxmcbixVrHbDcjm-2KLAcqlFx-u8P9o7_07ks2azxr-ItcJyxgj641Mfztc5g1TsL8H7ZOdKNUIXGpbAHWFAsJM9No6wiEjrGu9uNnTaebBY6hriH6LCahOkTr-Hd1ZLy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86927" target="_blank">📅 21:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
🇸🇾
وزارة خارجية السورية ستفتتح أول قنصلية سورية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86926" target="_blank">📅 21:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha-23KkFVscnmbfi7rUkWBKHmjy_DrqS29sVxkXhZOZS4STF8WI1BcHzyzPXJ--JsJu2r55jydOIXaZ5ta7YhioP3BGSuqThagjiSXNI7NZx8_5dmi6w2-Rj_Zhjo6_aDMMpANm44fOkj9xkwOTsYlFDeghwYZ2wW_E_C0gy_40l7BzOLcRWqUUMztMv9IWbqEXWmSgMgydX-QWyr0qREG_aj5B6Jxy5n7CFgLpDm-KfFQWYHgNBlx6Johm27qbApO8x6zj-dIiZe1tzbj2hc3bHV6aGMfyrd6fCbzHAzfcSjwjNEYgakHOzagkmvn6k8sPEgqtFBT7j9gZ5pATxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استخبارات الحرس الثوري تنفذ عملية أمنية في محافظة أربيل أسفرت عن اصابة خطرة  للقيادي موكري حسين يزدان بنا نجل زعيم حزب حرية كوردستان المعارض لإيران.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86925" target="_blank">📅 21:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw8SljGgc5jCkpVOgZWXCQur442F4U6R3u5B6COi9CqnoZu5lezeH8C60l7NkllRRw1TIHTWFWATd2xT8qD0IKYas9eH1bHE_6OPROak5aTLKHhP5IPavQHpr6buhaEnR1iqQefH5Sd2E2HoOBzidHQQC0Gjc8VehDobIOpE_geActL9xSfV3ng6zcsQ6x3i85G0SU4If7eF7GnYuGmNtJWPFByp_fq27_dFSXU6Oyi24lfKGbJ5LN0eU8BjVjK5zrY9rfTD7FSNmO-lUwvGC_ADRwvxwQF10ZIIzKE72hien_-pLlA5eEQy4CqxKk-Uos84yen7THrFXoLZCLm-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
ارتفاع جنوني في أسعار البنزين في إقليم كوردستان العراق وسط شكاوى متزايدة من المواطنين بشأن رداءة جودة الوقود المتداول وما يسببه من أضرار للمركبات رغم ارتفاع أسعاره.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86924" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVRetEM1j_gwTKgixDySZeD0l8YbmwXg5BAHu-475WjBqVQliAp5sU3LD1ETJIptzJ94KgSXvRQHNWtVgqL2Bv8AlS_LUBOzY7OgBdtqLCQgQZEvd85ASnxeYCmwZX-p6A0XXs0apDZwAqlG5Kr_yCzIDaxtM6Eavs2qvkK14bB_qG4y0fAJbHmUZaZtrcl44vNG8C2e3d62HFXtaIy6PS5I3Hk882JloH9c2d4xYY0cv4BUZ0UhDSYXMlThyLxrksb6hxKiahZ8Q2AjBWQNmT2fm6-t9eRl9Hr72-ogMV9Z4FdXL4Ms4Ds3FrkXMkg1fU8uFr2wvHK19j2HnqlD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSbVTheuBjZyjDbt5qPvjCAelFPLNeSWROunfH4Z9WMGIVu_DKkOCEE00psvzCF9x_jhP623SxXIajW-aqvQFss_sxPFovqQD4rfu0ZT1GiMZcmgwEloR6HkaaIfM-WbXUkk_r7J6LHM7HxsX-Mf8Qqm0HiZF6l0cQ9F-qf_8R-pjuJV2ZiH35SH-dEn-ojV8-ZQmc7HdWChsbXFZosUjfnLhUeCEtzExePlFEj_Ytaa5VegIVw0Dcoo5IxST3pGKQ_IcxNoeinhIsSKF_TlXE6Xbr8tGI59_3pFUgYTmJmyxtLFOxBHgWihDtIk4BY2ormdV_pJ93impPjx4tZNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQrzpbrGpUd6H0eEtUrezqna1F9G_uwzRmvdHnOrhveo4dcvj_1CUE0nKPvg0n5gy9Bp-szYqo2lxMH0X77jfdiaM0WGTGpO3nTX5hPUGmZ9Dr1AWA2imc3TuJP5uSK0jcDR6k47cYCM2uzVTi1AtWR5P2acfbtnf2mRlpcmLqi0dgNXhAh2iJvaZLnsLjcEBg0JIrfDtDzkkJsMgS3kQZADsJpYRM7p6RMZSr-bFubnC1Zr6w7mqZJ_YBJnfqtNM0hKyW86RDbkjA3CSkKIS9RqA4PSREbR7eTWeZLHiDlnJmo7mbnyeGHgyri-2zVsuJyB_QdIA0_3w8zJJbv9pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
قائمة بالأهداف غير العسكرية التي ضربتها الجمهورية الاسلامية الإيرانية خلال الأشهر الخمسة الماضية:
السفارة الإسرائيلية في البحرين
الأحياء الدبلوماسية الأمريكية في الرياض
السفارة الأمريكية في الكويت
القنصلية الأمريكية في دبي
4 مراكز بيانات مختلفة</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86921" target="_blank">📅 21:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHHaqrUbcHu-exZq8hYZTDKnrSOrhCF9t0dJG8KYvkpmM6lnpMD0NJrWRMpt2vzSLNQUKdSe2qgZPc2uJ1IKJPVffw1g4GJg0eXK5ubhDBAoI6Im8aOZTezztsouqkNkZE_0J4tbjDzZYiPcEHuFxDL_rxUkYa6ThADK-243lCQPyzdQUdL298Kh73CO0fDFHG9fjV2y14W2INqh89mnlFldgBOqRxXmVRBf1Im8Z4UCHeQrVH7mez3tKZ-fdWeTHsg8mYh1R_V_e1Kv35OSTrUPgbHGiCT5Jk-3iJpEFjxJ0bXOTHr3Z66JEpHNPikXx9qHGPd1WBBiJAXB9tp1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رصد   حملات إعلامية ممنهجة من جهات مدفوعة الثمن بدأت حرب على مواقع التواصل الاجتماعي على الشخصيات العراقية المقاومة ؛ حتى اللحظة تم رصد ٥٠٠ صفحة على الفيس بوك تقوم بنشر منشورات كاذبة ومزورة ..</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86920" target="_blank">📅 20:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86919">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kabu7B6G5FXUPBv7NpLb1XPxdfHD-SBSF1O57OKEIa9ztvoyKchoqmghk4L7S28q-ZdxxWNMG--WP4y_fblTgbm8_L5pefjo8fQvo7EL-w6zFSccH8HJBNln5MP9H5pOkMWLpoF9l51Fps5UxPFtmMqC99_4y9ilmpD0kFcF4dzlJkwjXwhs4QJCPeDkV5kUtZPCehWVb-AKff29zlQPqXFO7m2YB1AFsm9286lneP9Pv3C1GDT35MD6gKvTRg4vU0ZExq9OyrkNUjqhbhVPvIzvEL5wQRJs0N6WsMr8G7zMjlbEibxRLmdX8jsGnvGc0wBS60_Fp82fP8LlKpp-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رصد
حملات إعلامية ممنهجة من جهات مدفوعة الثمن بدأت حرب على مواقع التواصل الاجتماعي على الشخصيات العراقية المقاومة ؛ حتى اللحظة تم رصد ٥٠٠ صفحة على الفيس بوك تقوم بنشر منشورات كاذبة ومزورة ..</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86919" target="_blank">📅 20:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86918">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86918" target="_blank">📅 20:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86917">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">غرق سفينة هندية على بعد 13 ميل قبالة سواحل الحديدة بعد إستهدافها بزورق إنتحاري مسير.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86917" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86915">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exD5qDvnfIGB-uNj2O_0-pLujoFcKWhRLl5ZKENMWgB-r4USKrBP918ekUfV4X2OHs3ndhfKJCHco5EYlXUeQYFA9MiSvd3PhoFoHy2IJHJ9LwZ9TynO-3alc_31mhFIkVvqabzyvtlzc-ssOyQtSOMIMPIM5qGBxZhLG1NsSCItJtRz5rE6tlLiOZuP_eLeYIxUjDRcYU7z2onxAhFeRqz4RyC8gF9rab9p9lglR4Q9c2bOMPE09r2V7ZhX3_x6NH0BEZI9p2Kobz5cyFc3NkmkvnvqOZ8etBxFKT1aufIhkZ99QrGFq2cGr7g_oTN8hBm8ORM-GYduONIpv5hq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86915" target="_blank">📅 20:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86914">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86914" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86913">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مصدر امني لنايا : نشر دفاعات جوية عراقية بين الشريط الحدودي العراقي الايراني امتداداً من ديالى إلى واسط .</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86913" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86912">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-text">"
⭐️
If you have a
verified
Telegram
account with a blue checkmark, we kindly ask you, our esteemed subscriber, to support our channel by promoting the link and sharing updates on the channel."
في حالة تمتلك
حساب تلغرام موثق بالعلامة الزرقاء
نطلب منكم عزيزنا المشترك دعم رابط قناتنا بعمل تعزيز لغرض نشر حالات على القناة
⭐️
https://t.me/boost/naya_foriraq</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86912" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86911">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نايا - NAYA
pinned «
يقرأ القران سيدّ من بني هاشم فوق القبر الشريف بالفديو والصوت والصورة …  أنا نايا عندي كل الخفايا
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86911" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86910">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">يقرأ القران سيدّ من بني هاشم فوق القبر الشريف بالفديو والصوت والصورة …
أنا نايا عندي كل الخفايا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86910" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86909">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
محافظ كربلاء المقدسة:
22 مليون زائر أحيوا زيارة أربعينية الإمام الحسين (ع) من بينهم أكثر من 5 ملايين زائر أجنبي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86909" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86908">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تقرير: تسعى السعودية إلى استخدام الدبلوماسية لوقف تصاعد هجمات الحوثيين</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86908" target="_blank">📅 17:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86907">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/86907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86907" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86906">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">غرق سفينة هندية على بعد 13 ميل قبالة سواحل الحديدة بعد إستهدافها بزورق إنتحاري مسير.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86906" target="_blank">📅 17:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86905">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86905" target="_blank">📅 17:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86904">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
عدد من المحافظات العراقية تعطل الدوام الرسمي يوم غد بسبب ارتفاع درجات الحرارة |
تعرف عليها</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86904" target="_blank">📅 17:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86903">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
‏
وزير الخارجية الأمريكي روبيو:
تم إحراز تقدم في المحادثات مع إيران لإعادة فتح معبر هرمز</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86903" target="_blank">📅 17:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86902">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تقرير:
تسعى السعودية إلى استخدام الدبلوماسية لوقف تصاعد هجمات الحوثيين</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86902" target="_blank">📅 17:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86901">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
شركة دانا للغاز وشركة كريسنت للنفط:
سنقوم بتوريد 100 مليون قدم مكعب من الغاز يوميًا من حقل كورمور الى السلطات العراقية لمدة عام..</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86901" target="_blank">📅 17:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86900">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اعلام خليجي يزعم: اعلان مرتقب عن اعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86900" target="_blank">📅 17:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86899">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fh22eXKJTCf3ongacDG_Ze8dLimmxAXLHZ6NDnQctZtT49sfcs5VMwWI1jPZ3XqkxAP1qbvau9uVKY6Rz97Ahhzm8wu16CZhL7KeBhh4ViMT4Q8bB_HKQ92F9FCTMbXE4l2UKtRzoS5FI0IDbZy1Dhq2WQMCz1MRpWXJdpbiF-7MDjiBcBDR2Nqlxix8ShhBftp6PuvOkMwkw6FCA5qT_5ziVHPMaUxEFSh550UyA-BiAJQkypLmHw8B3COZKtxIt1Nsz_Jv5UAUw7gJpDmb3hwYfmgfj9i_Iu6C_1vrz_UbJ0GbsvKVtmOPR41_lgBfZWLGITN1CH2qs1Nv8Fs_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇺🇸
فَكِد كَيدَكَ وَاسعَ سَعيَكَ وناصِب جَهدَكَ، فَوَاللَّهِ لا تَمحُوَنَّ ذِكرَنا، ولا تُميتُ وَحيَنا، ولا تُدرِكَ أمَدَنا، ولا تَرحَضُ‌ عَنكَ عارَها، وهَل رَأيُكَ إلّا فَنَدٌ، وأيّامُكَ إلّا عَدَدٌ ، وجَمعُكَ إلّا بَدَدٌ، يَومَ يُنادِي المُنادِ: ألا لَعنَةُ اللَّهِ عَلَى الظّالِمينَ.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86899" target="_blank">📅 17:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86898">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصدر لنايا في المفاوضات بعمان   ايران تريد نسبة 7% من اصل كل سفينة تجارية تمر في هرمز فيما تتوسل امريكا لجعل النسبة 5 % ؛ المصدر لنايا اكد ان سفن روسيا الصين سوف تكون معفى من الضريبة .</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86898" target="_blank">📅 16:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86897">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعلام خليجي يزعم:
اعلان مرتقب عن اعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86897" target="_blank">📅 16:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86896">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مصدر لنايا في المفاوضات بعمان
ايران تريد نسبة 7% من اصل كل سفينة تجارية تمر في هرمز فيما تتوسل امريكا لجعل النسبة 5 % ؛ المصدر لنايا اكد ان سفن روسيا الصين سوف تكون معفى من الضريبة .</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86896" target="_blank">📅 16:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86895">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0550b2f93f.mp4?token=p1vuOqAFBU7Srwo12SKtIcMmsXn_FIXwO2EtoGXKEjSzhskPtoeMpiZhzt0_pw5ZJsiSa_10nmY-atSsn9YgOP_9m8yx0X_Vj9RYiCrQMEKCM5qZ-U7999hNoU259vB6zABDMm3zMIEnkT5PpcR73GVzpvfJRhQlZ4N-vxWo1RwUl9hm4J_Klb_m7RkKEFjY8wvedMSZDIa53Y0vNR5x-XBLvvNy1fMc17SpU619p13U18FHh9QHYhzm7IH_LVnCTLwZ-odcK7uyAwCv8cT-C8WNmbwI3txNloTleOPOU6HeCtEVb1bWyQDC_V_8cCpnBc-YxpOCe4s4tRh3QsqAcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0550b2f93f.mp4?token=p1vuOqAFBU7Srwo12SKtIcMmsXn_FIXwO2EtoGXKEjSzhskPtoeMpiZhzt0_pw5ZJsiSa_10nmY-atSsn9YgOP_9m8yx0X_Vj9RYiCrQMEKCM5qZ-U7999hNoU259vB6zABDMm3zMIEnkT5PpcR73GVzpvfJRhQlZ4N-vxWo1RwUl9hm4J_Klb_m7RkKEFjY8wvedMSZDIa53Y0vNR5x-XBLvvNy1fMc17SpU619p13U18FHh9QHYhzm7IH_LVnCTLwZ-odcK7uyAwCv8cT-C8WNmbwI3txNloTleOPOU6HeCtEVb1bWyQDC_V_8cCpnBc-YxpOCe4s4tRh3QsqAcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ناقلات النفط العملاقة السعودية تغير مسارها حول أفريقيا. ‏ست ناقلات نفط عملاقة ترفع العلم السعودي، تبحر وهي فارغة، انحرفت عن مسار باب المندب وتتجه الآن جنوبًا عبر المحيط الهندي</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86895" target="_blank">📅 16:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86894">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزير الخزانة الأميركي سكوت بيسنت يزعم: قد نتوصل إلى اتفاق مع إيران بشأن مضيق هرمز اليوم أو غداً</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86894" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86893">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk5lrK7rjKxdzve6Oc3KKyQ4BaDyt3qn7E_Wz_fkk-D4UnCKSvKa8_fnAOe29p7oJAV3olabOlmo0i3g8BS3YeaSmri8ES5hfk6sGI1cah3g3oz4IiKSFw7Uf4fO3LzI4lnK-ir20gMDjRVLAN-vf3MyamuCb5G1nf_nx5e48epL6l9IDK7QrSEi2tAc_UtuyQj8ZRmrX41jpLnURcXbPV7pdVLJJjbQxeKMi2iiVtyBT_8OYBomy1EG0Guv0VI-8uUS2e9bF4fFmTjGYjxKm_tx30BiEFJZMuQgfoyKZmfpdF9RWqMGx9xL_zVpHk-v8eGmVstYHSzPFVqkScGAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صگار البعث الصدامي وشيخ المجاهدين ابو الحسن العامري يلتقي وزير الخارجية الايراني عباس عراقجي
العامري يوم الاثنين الماضي تجدوني اول بندقية بوجه من يقترب من سلاح المقاومة العراقية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86893" target="_blank">📅 15:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86892">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇶🇦
قطر تقول ان هناك مشروع اتفاق محتمل يجري تداوله بين الأطراف وان التركيز حاليًا ينصب على إيجاد حلول قصيرة الأجل.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86892" target="_blank">📅 14:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86891">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e077c0ea7c.mp4?token=SUtdZjHPoZCx3cV5zaJinECFkAmQmEzRXECVqRU4wjRsMht1r_hUfp9ViXgTCoCIez4TPjhB25YboWiBV70E1DlEqZgQ6j9f4UFRuOcU8LIimIxd1uZQiHst_7b1B3f2os2pbfHTWCjLfmCPSu16O2Nag4JqXJVhZsmB0mJAlvZZJiB11Z5hHpnu1h0ot2lGf7pZneb_ZXTTSA8ZIq5i9TSxKzyO0DSnu8jBMyN78rAxrpe79mW2x1KDk2IYaeHwvMCXXs9NGUH8DRVNXAAXgx4V9CvH3m6TtF7AmP8p1fvXBD1ddZGEos3HqPjI4cpC2RS0nhdoQphJ1xYiHVi5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e077c0ea7c.mp4?token=SUtdZjHPoZCx3cV5zaJinECFkAmQmEzRXECVqRU4wjRsMht1r_hUfp9ViXgTCoCIez4TPjhB25YboWiBV70E1DlEqZgQ6j9f4UFRuOcU8LIimIxd1uZQiHst_7b1B3f2os2pbfHTWCjLfmCPSu16O2Nag4JqXJVhZsmB0mJAlvZZJiB11Z5hHpnu1h0ot2lGf7pZneb_ZXTTSA8ZIq5i9TSxKzyO0DSnu8jBMyN78rAxrpe79mW2x1KDk2IYaeHwvMCXXs9NGUH8DRVNXAAXgx4V9CvH3m6TtF7AmP8p1fvXBD1ddZGEos3HqPjI4cpC2RS0nhdoQphJ1xYiHVi5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجمهورية الاسلامية الايرانية تواصل نقل قوات ومعدات عسكرية على الحدود الايرانية العراقية الكويتية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86891" target="_blank">📅 14:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86890">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇸🇾
سوريا الجولاني توافق على خفض واردات النفط الروسية خلال مفاوضات رفع العقوبات الأمريكية عنها.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86890" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86889">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الدخان يتصاعد من معمل الالمنیوم في مدينة شمس آباد الصناعية والاسباب غير معروفة</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86889" target="_blank">📅 13:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86888">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thn_c6yCN8xHdrw_OPi_ZQ5Fmj3BX91xlFbR8NN2aCE6VWjISXzkn5xCCmBUSahtTvho5A3jCZlm9mU7qPkgojS2ast9mZsm1ncZYswjLiQ5aJAXu3VOQS9PxsQKobW3iKWbd_WjbkuzuZ2eko1IG9elnjF5z014LqOkwSAymLiV754qIGv9AmLy4Ydfgpgn9G-hygZUVd8fJY60vkXUx_X7IgK3W7uDiplRvQwdDevJPlkaPRdFRBPhEFuJa99qVzs127Y8Qe3p-MdbCHl4ty6W3BNP78HRenWUweAGVoeTijuOQs__n77-5t7DEkdfupgv-UZnyBEEO0wJ_pac0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86888" target="_blank">📅 13:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86887">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86887" target="_blank">📅 13:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86886">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي: أكثر من 70 فوجاً انتشرت على حدود المحافظات خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86886" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86885">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي:
أكثر من 70 فوجاً انتشرت على حدود المحافظات خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86885" target="_blank">📅 13:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86884">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6l-2gtBspR_5uv0quNBiSZc3yU-cSOIWZNI7iaeGxqO6DcqXal90UdvNySZoJpKgd1kMnBAlaXE_cIslqlALd78CfM2EJpNfuE-iD-bRrqBnAA_PMjT2Ekh6EZzkrmClaiRDGcmv6GxpRuDDlD4CRP5yBghduNK01Qw4MxD73yeDN-s0O6lTF-k_hI3SGYJnhsoIl9Psu80xMyXHa6O1lOsXoYxkSZYb5dwBKr3Q0iQ2i67v1M5fppTChtQ4VmapvcSpBoY36lAjuVMqD1TiH7t_rclHt30wnXUsIyXdUEReWmuVdi_O-dIdMCJQhML5YHTcTHVS21_mKQ92Zjoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد لاعمدة الدخان من جنوب طهران لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86884" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86883">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_tlfjCTl5a9Ra2mmOXDnmpv60UQitWNKHYREDPZWGbhh2QOEz8rPxADc_epdMjGl6nQk_mlQcnTYEpghGe0hISQQ8EsiGH4Vt1SGEYKrIXYyzQfIIIRGJmvdz8C2aHcwoRdLlQ3GWBvaJcmKC5PFpRCHlPzJX6Vg9dC2H2SbDFszNOBTFEoZUn_z7YRitp6JlFc5rcOGQhJak5qXnpTia22if2WfOroMFP-veGgi0oSK43k8nNzXzYiWyC1CC-2jXmTIfM4v77JcS3sZ4FkCn3i_rh95YNpX1_EUbsjgOO3mA94SEfJDqNdMn53cATrU-2fnn4LFSTrbJB-WRdtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد لاعمدة الدخان من جنوب طهران لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86883" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86882">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مصدر ايراني رفيع المستوى: بالنسبة لمسار الملاحة الخارجة عبر مضيق هرمز، ستسمح سلطنة عُمان للسفن بالمغادرة بعد إبلاغ إيران بذلك</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86882" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86881">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مصدر ايراني رفيع المستوى: ستتبع مساحة الملاحة البحرية الخارجة من هرمز مسارًا يربط بين إيران وعُمان.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86881" target="_blank">📅 13:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86880">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📰
مصدر ايراني رفيع المستوى لرويترز: خطة مؤقتة بشأن مضيق هرمز قيد المناقشة مع سلطنة عمان تمنح طهران السيطرة الكاملة على حركة السفن القادمة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86880" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86879">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📰
مصدر ايراني رفيع المستوى لرويترز:
خطة مؤقتة بشأن مضيق هرمز قيد المناقشة مع سلطنة عمان تمنح طهران السيطرة الكاملة على حركة السفن القادمة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86879" target="_blank">📅 13:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86878">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e85d3110.mp4?token=tkMkWRh5bEKF96vzC5XRSK5f_CEvsEk0aAbaIZeyXcvdbUUB51tdoTaX4BGdXwYs4Dcm-r3-5a3iwjuA1MSRHL9KulqXWQqEGSViYpF_R1o3sWLKJ8yWROAb6mZMHakmG568HTqh9prlxcNveGGYT58NF-RIr09G9JIEeWaHswWGBJkwZeelqwvziVUWOTYgsPc5T2Kaz0EsU-hnahfEXokcQ7RRdYW0l5nv9EIe5bOdsnY26F7Qs6v0xRXUEl1ufswMV20et5BOCCT1jdvGFMgR58ycaqo5Vs33QJPWgWPwp9YLuE14SnfvFGVsXn1XjqiSvCB5TxwKriNO7Pp7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e85d3110.mp4?token=tkMkWRh5bEKF96vzC5XRSK5f_CEvsEk0aAbaIZeyXcvdbUUB51tdoTaX4BGdXwYs4Dcm-r3-5a3iwjuA1MSRHL9KulqXWQqEGSViYpF_R1o3sWLKJ8yWROAb6mZMHakmG568HTqh9prlxcNveGGYT58NF-RIr09G9JIEeWaHswWGBJkwZeelqwvziVUWOTYgsPc5T2Kaz0EsU-hnahfEXokcQ7RRdYW0l5nv9EIe5bOdsnY26F7Qs6v0xRXUEl1ufswMV20et5BOCCT1jdvGFMgR58ycaqo5Vs33QJPWgWPwp9YLuE14SnfvFGVsXn1XjqiSvCB5TxwKriNO7Pp7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق نفسه وهو يحرض على الطائفية ويسيء إلى زائري الإمام الحسين (ع) من قلب العاصمة العراقية بغداد  إلى وزارة الداخلية ومديرية الإقامة والجوازات: كيف منح هذا الشخص تأشيرة دخول إلى العراق دون تدقيق في نشاطه ومحتواه رغم ما ينشره من خطاب تحريضي يثير…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86878" target="_blank">📅 13:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: عبور ناقلات محملة بالخام العراقي عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86877" target="_blank">📅 12:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">السفينة خالفت توجيهات حرس الثورة الاسلامية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86876" target="_blank">📅 12:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏استهداف سفينة بضائع بمقذوف حربي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86875" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حدث امني قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86874" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حدث امني قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86873" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XW38rQN1H5ufrCQqdokh0uV9mITZ5r-KF61zqYfh9836BiwhSfnbYccDh6hh4Is2gGP_gig5oCRtcIULdXNNTJRiYdBQGmjMoaBtKgoptu6FkEK6Lc1TqIhZWOy86s1JtLkaWUPa7dQdGO01qs0RV2AeMOQVSISHd5kiZkFZoxkhg6ysH9T1B7koeryrXeGbHlyP7dKddTrHc4DzFPmGMnfnV_pJgxWy5rPMDwo0QiuBnWW9z97J9G2aaArZ2IRVNaMB16ds2PDtnOBZF-Dtr05LBcBeRr7mwWKAmp1u-MTgLi5TPwtxSj65THHCa8UnP3WyVS9hDtkw-6A3M2hnyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3NXc_GR6pqiiURN-M-ZbkQCHtl-rxi6wYM23XVWm0pZZxnnkdetpYuqe89PeGvO-GdnUVG5SevHYKgiQBU6SFj6dxd5TasG13EpVKlea_AxRno2vlmmCXRDxL25WPNkczAXu8gJSC8ro2i3_M0rzEbbTh0r_ir8Dnxunlw2ooyMzBMGbguAVHPbMHTc-w1y0R2NufMZU_BJlSaddZRyypFcLp9L2Ije9jHsQhChVQx8AaCGOhVDrzuYVikJWhG1Xb90Ol2d7o0CRWI7uP_8apJZJuYgMItgqyh50ACiwRaMFMN-thL4qq9r5ifvlSmVub8ZrGHGJjt44O7DKHP7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EO8-HRTmGfphlnMqGmGjFmZRUY_nNgw-uIasiuD28cEwCj2za1_yWnC2OWskwjqCxQz4QAvtIBn81o5rBaIVGfod7g3wBKiVcvcZ7uH-3D1PXxmwgUZuc6G6z7cZzOtqGAZ3Tw5PEzhJLscAFwWU_USFpsd56WagE22jHDRjKuhhWNTmrAt-2n7J4HCliT78xojGL076vGGIsFl75VZCpr32LeCdyvVOsdmN6ZvLSY5YWO-ihkM5hoGEhy9WhirIx8jbRf-5T1_iFsdPogAlFLUgdHsSXnQrv-7I5nhNUCn6_pme4BS6HFpfLhLMMQuthuHJKa2dRCaOgI1N7XDexA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇱🇧
الجيش اللبناني يدعي إحباط محاولة تهريب صواريخ غراد بقطر 122 ملم من الأراضي السورية إلى الأراضي اللبنانية كانت بطريقها إلى حزب الله.
تنويه للجيش اللبناني: الجنوب اللبناني بحاجة كمان لإحباط التوغل الإسرائيلي
🤷‍♀️</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86870" target="_blank">📅 12:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb1b6f848.mp4?token=j9xkO4M91OQgG7rb1MTP3duzgd6UgiMW71DrLCrptsza50-NvEUvaMLDz7A5qqesXGSbjae0xmiczOnLkSb-vLn7lncT6QVoou6A0mV__Ar6Ojpe8rT7NrvSftPYi9IkeCy9fWqjOyUx-jEd9KLVKwYnDU-ZPbLTQdXWU_uNC9Dh3BiUJYa4G1G4SSgJm85_gIKU2JSMHTNwyNrZNZKJlCV_ZrBuN0HLDB9zMxLwN8ZQLiyWi_z9mMNLpyYTAMGrABTgp4MI24l28Yg6-Flv3VWjxWIGUcbVwzP7F0hxNqtXdwEEKNK9ZhLTjgN5jgX2z3g0Jj6FqxiJ7ztaiYdbrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb1b6f848.mp4?token=j9xkO4M91OQgG7rb1MTP3duzgd6UgiMW71DrLCrptsza50-NvEUvaMLDz7A5qqesXGSbjae0xmiczOnLkSb-vLn7lncT6QVoou6A0mV__Ar6Ojpe8rT7NrvSftPYi9IkeCy9fWqjOyUx-jEd9KLVKwYnDU-ZPbLTQdXWU_uNC9Dh3BiUJYa4G1G4SSgJm85_gIKU2JSMHTNwyNrZNZKJlCV_ZrBuN0HLDB9zMxLwN8ZQLiyWi_z9mMNLpyYTAMGrABTgp4MI24l28Yg6-Flv3VWjxWIGUcbVwzP7F0hxNqtXdwEEKNK9ZhLTjgN5jgX2z3g0Jj6FqxiJ7ztaiYdbrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اندلاع حريق مفاجئ مجهول على متن سفينة أثناء إبحارها قبالة سواحل منطقة "الفاتح" في مدينة إسطنبول التركية وسط حالة استنفار كبيرة للسلطات البحرية وفرق الإنقاذ.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86869" target="_blank">📅 12:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d4da1cb4.mp4?token=uI3PqNkug24nbLbIhpK9Jn0O1BiHUmfQLp2Fjlcz_caG34CZd5ABzRdA6GYh25jfrqw4D3j8DPeVDsvk3HGq3PL_tOjcRpa0-YNN9NYUomeuTTPB80DKVbw8WxdrLiGTysnIHOxmj8UwbYRpuyw5DQCZ6PWAOu7Ho-mFV-XBll0UfSHkMA1yV2B81iHdB1lfhh_H2XHhTh8ovwhYq9lsNPUbQMaG380vSMc6cf2H7h_aNWbrZ0806DiQks2bVZqkoOeIumrhB-lJIdLdyszephXOJl0Rf3muI7eCzvyj2ilYWAWhR4HmYXHi7oG3lZcVMebfsele1BxrnSVCQq5RujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d4da1cb4.mp4?token=uI3PqNkug24nbLbIhpK9Jn0O1BiHUmfQLp2Fjlcz_caG34CZd5ABzRdA6GYh25jfrqw4D3j8DPeVDsvk3HGq3PL_tOjcRpa0-YNN9NYUomeuTTPB80DKVbw8WxdrLiGTysnIHOxmj8UwbYRpuyw5DQCZ6PWAOu7Ho-mFV-XBll0UfSHkMA1yV2B81iHdB1lfhh_H2XHhTh8ovwhYq9lsNPUbQMaG380vSMc6cf2H7h_aNWbrZ0806DiQks2bVZqkoOeIumrhB-lJIdLdyszephXOJl0Rf3muI7eCzvyj2ilYWAWhR4HmYXHi7oG3lZcVMebfsele1BxrnSVCQq5RujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق نفسه وهو يحرض على الطائفية ويسيء إلى زائري الإمام الحسين (ع) من قلب العاصمة العراقية بغداد
إلى وزارة الداخلية ومديرية الإقامة والجوازات: كيف منح هذا الشخص تأشيرة دخول إلى العراق دون تدقيق في نشاطه ومحتواه رغم ما ينشره من خطاب تحريضي يثير الفتنة ويسيء إلى شريحة واسعة من العراقيين؟!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86867" target="_blank">📅 12:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86864">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ec2bebd6.mp4?token=l8t5UIRV9Im9nvNOV2PMhnESubnAq6PB34HXLBt0VPb0mnJb8HDdFSYW2rfo7TKQr876pMee7QFGt9LN4NDwj3cGcco6wWk4vmQW7XUKQZL01sMtPav1X5uJPWtzdBMniB1YEGvYJHefLQFwfKcOix6XUrw8vMhq4k6a6Za0Qi-6MpEHihJe6g1K2L_Ot8rI-7wcmOZEFoqxgjRwfZFwb-khG0SVUD2Aau9wmIQVYulVFr6YiTca3cNgZxwym8kGWjF9JYeIC-Tz-Nds5tIqAfAt0sEE8iBrbJUsUxJ370szPV9zqsfO3kmOrKWJz-_EnXwcjnZZc44s5KoUhLG_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ec2bebd6.mp4?token=l8t5UIRV9Im9nvNOV2PMhnESubnAq6PB34HXLBt0VPb0mnJb8HDdFSYW2rfo7TKQr876pMee7QFGt9LN4NDwj3cGcco6wWk4vmQW7XUKQZL01sMtPav1X5uJPWtzdBMniB1YEGvYJHefLQFwfKcOix6XUrw8vMhq4k6a6Za0Qi-6MpEHihJe6g1K2L_Ot8rI-7wcmOZEFoqxgjRwfZFwb-khG0SVUD2Aau9wmIQVYulVFr6YiTca3cNgZxwym8kGWjF9JYeIC-Tz-Nds5tIqAfAt0sEE8iBrbJUsUxJ370szPV9zqsfO3kmOrKWJz-_EnXwcjnZZc44s5KoUhLG_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇺🇸
تأهب عسكري غير مسبوق في مطار رامون العسكري بالكيان الصهيوني.. حيث أظهرت مشاهد انتشار أسطول طائرات وقود أمريكية في قاعدة رامون لجوية وسط تصاعد التوترات الإقليمية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86864" target="_blank">📅 11:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86863">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم:
الجمهورية الإسلامية الإيرانية انتصرت ولم يعد هناك مجال للحديث عن من انتصر في المواجهة
إيران عملت على أن يكون لبنان في البند الأول من المذكرة واشترطت إيقاف العدوان والانسحاب الإسرائيلي
المفاوضات المباشرة لم تجلب للبنان إلا العار والذل والخيبة والتنازلات المتتالية
﻿
تحية إلى العراق واليمن على نصرة قضايانا في مواجهة العدو الواحد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86863" target="_blank">📅 10:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86862">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/86862" target="_blank">📅 08:42 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
