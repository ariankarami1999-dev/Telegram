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
<img src="https://cdn4.telesco.pe/file/CU7MtUBqA8WfQ4-3LvicnP4ROL2aiIcNcLJiUis2zGk2sa7tV4cKjLUjn-EIoTwfg2C79OVibiQ0sWC5m2Xj2e-zOnPauh-oRuMIQgnPsSnkqlXAa4RXNJ5CPlmAKK2MVyzNJeMVTNvSm3HMsScj5HqO_s_zWQdkW4475BPD0MnOCKq3_Zbulju3LYiP9gkrXpc95TFhMpkT9S0Q-7ZZele_r0osN4Xi80fOcExaTS8rMjG1oqEDSPnJ7V2dgGwxpGtsxyqb2FYcqkkpSUWSBZ0tt76SWCfPqqpVQnCzShrTpPbDbRpgA6bY5_0WFUqHyAUxweYTJv9ubbOvWdoWBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-444520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAztAQMnrG3-ldLFrmjU5Pbln3M8VuAwwE3nDgVs0_5BeSXTntHrpRoROlDO0kdHAeTCZghqfwQiFOTY4mtW3WzjzGUK6gGzFiBl0LYyQLbzXtThz7C_gHexvdzV_zn7QT1iI-oQnHA9f3oyiAe2Qhx7Fco3uCz_bz0drWP1T48gmMKl-zcpHBugHc3F32dCoFKMCd2ccgED5PaXPW0MDbt0_U9DHMCzZ1_xz2N8ucUVdNtV0CnS5qg3lqSViyh7iqtSwNEVDMVi3X3dX0ndeIKDV8cdgMnLhw3sHHCZTry-5WSLxHtk8wNDt4ZbEy3fPl_9bk9ZKc5Yd-yMdL--qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/444520" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/farsna/444519" target="_blank">📅 18:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a3ee11eb.mp4?token=QeTPlKoCI0XarUbx4nhz1kGI4rkLZJOZKuMa3khSoW8AvQNWmqx28g4iMrY1ewWcphTTUQMZbbjIoPiL1fHrKPUBrqT3nDowHAI465GRx06wuW8BIb4nDqEgXYK0actoAu4Uuqg-_E4zRAin4MfXlKUx0a_GI2sOCs88XfE-MaZNunayUqyfcX0wzb2jvp8DM_YXfh-q3kDVNuzYyA-glFdUTnxGrhGz04fUwYRCFJs5Yph33NKfjidIUgpvrnfWEHy1lV-r8X2C_U36yxz0zKnO7O5FGhycaESKb9TIz4myvS6hou1gaX4lNY8Hx5Ut1UdIKMlr0dkgacVfOxzRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a3ee11eb.mp4?token=QeTPlKoCI0XarUbx4nhz1kGI4rkLZJOZKuMa3khSoW8AvQNWmqx28g4iMrY1ewWcphTTUQMZbbjIoPiL1fHrKPUBrqT3nDowHAI465GRx06wuW8BIb4nDqEgXYK0actoAu4Uuqg-_E4zRAin4MfXlKUx0a_GI2sOCs88XfE-MaZNunayUqyfcX0wzb2jvp8DM_YXfh-q3kDVNuzYyA-glFdUTnxGrhGz04fUwYRCFJs5Yph33NKfjidIUgpvrnfWEHy1lV-r8X2C_U36yxz0zKnO7O5FGhycaESKb9TIz4myvS6hou1gaX4lNY8Hx5Ut1UdIKMlr0dkgacVfOxzRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه
‌زیر بیرق حضرت عباسیم(ع)
منتخب تصاویر از حضور عزاداران و آیین «علم سلام» در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/farsna/444518" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3981d896a.mp4?token=ngZffI9CH8HmC-7iitFYt0DQsY1VgBjTcq5r4SBl5-y_AhyWINvMrFyB_ds11ZvFMR_RZYPamQEEPL5aDNdgNbULn21nvIj4atdzDuB06GGTXvByUIEShItF7n8lGg72rZIQXYD0wzP4Zqvv3-sEbsTqVyJwYdHxb-zzAMhll7yG-oYPNLaum6rbs_nqLF23WkUyABINazQdZRPmG9VCDjP9xDOKA9EG0XcjQr8V8_iDDdsBKYDjDBu1OKhqgYGcg2P8WGiI1eAYOQWVNhAP0bBEuYbL0arLQdIGlpl9_zlkAXPAJlBnsGQimKGtti4_W257rWs4aNV-KBGyOuUURnrxN7ZMVxk-8nFSkwimFCNSWXJ_OkyaCPk9j0AT-63hWTAFmEdqZcKpl6blzAfJrU_w_gA5UHpnGfqwyPz9MZZGTsOE05l6IULQ1oNJ7tVyKihLeHvZAYbQr4ldGIz0sa5uNSvqN-uxtuElnYmEISf5o2hoy1TAs2ZmZdBsL7Yrk6E9volXmt29qhOkAmVx3PZRtS9yDSc9nnBwyb6T06fm4py2G5YFeu35N_0kxLGlh5pbiedIrBjOW4c4ZRS2wi9FEnuwstrIZI2kgVtC9brJryAKPdhZUrA_sGLqAddiZC0vVmYEFW2uG_d4M0Xg46_3qOhohqgT5K1t-5Tyx0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3981d896a.mp4?token=ngZffI9CH8HmC-7iitFYt0DQsY1VgBjTcq5r4SBl5-y_AhyWINvMrFyB_ds11ZvFMR_RZYPamQEEPL5aDNdgNbULn21nvIj4atdzDuB06GGTXvByUIEShItF7n8lGg72rZIQXYD0wzP4Zqvv3-sEbsTqVyJwYdHxb-zzAMhll7yG-oYPNLaum6rbs_nqLF23WkUyABINazQdZRPmG9VCDjP9xDOKA9EG0XcjQr8V8_iDDdsBKYDjDBu1OKhqgYGcg2P8WGiI1eAYOQWVNhAP0bBEuYbL0arLQdIGlpl9_zlkAXPAJlBnsGQimKGtti4_W257rWs4aNV-KBGyOuUURnrxN7ZMVxk-8nFSkwimFCNSWXJ_OkyaCPk9j0AT-63hWTAFmEdqZcKpl6blzAfJrU_w_gA5UHpnGfqwyPz9MZZGTsOE05l6IULQ1oNJ7tVyKihLeHvZAYbQr4ldGIz0sa5uNSvqN-uxtuElnYmEISf5o2hoy1TAs2ZmZdBsL7Yrk6E9volXmt29qhOkAmVx3PZRtS9yDSc9nnBwyb6T06fm4py2G5YFeu35N_0kxLGlh5pbiedIrBjOW4c4ZRS2wi9FEnuwstrIZI2kgVtC9brJryAKPdhZUrA_sGLqAddiZC0vVmYEFW2uG_d4M0Xg46_3qOhohqgT5K1t-5Tyx0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فقط حسین سردر عالم زده پرچم
@Farsna</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/444517" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYArg8XWuekqvNg4tme1LymEE7OSyQcWpB7xwLMigOxYJSUkEIqMJdYBNIS7bGpe7hSXK8l9HTuAcM-B3Cugxojxb11VJEwL9Fw7UrXNbNJ3PEmYGdCjuonov2Ei4bzPLuiwD_L52VvF6Nw2qe2Rrh340mmtQZZ2j8QSv57ZdFFyudUp8_7w8R2URqMH-1dJ3R5bfM9jENOjDUKgU0WXwmVEypHqKhNIDypy8DgGh8rzPioeVXIP-qCTgTbR4jZXjEcYUNjhuoH5uRtz6S2qbxjIHdm8y72il0cBWhCREh2KF1MnqY3AVQIDGV-vUzhXCSN9-287LebBbjapsaUoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
خبرنگار الجزیره از حمله پهپادی رژیم صهیونیستی به خودرویی در نزدیکی شهرک کفر رومان در جنوب لبنان خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/444516" target="_blank">📅 18:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۵.pdf</div>
  <div class="tg-doc-extra">2 MB</div>
</div>
<a href="https://t.me/farsna/444515" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بستۀ خط ۷۵.pdf</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/444515" target="_blank">📅 18:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7ODxf0wi80G2XaFYo323RmzCD1ThdJBIIcOOjcM6TIyFcwHDbuK5HS84Dw0ejiSJuQAZJaVt4WzHG-p4-ClpGZ0dlsaJPjK3Ccjbwur8o6LXj1WmFM6TpcxrDa7PIlNqwCuh4P0hZ0zTd63ouhnGyIfK8L4dDUZSIaJqTtTH83F1Q2TBXtvW0IbSd51KO_y-TIr06bTN6oC-JHaxA_rcekxJM0Es5siN-RGwIN0Ex_WcfTyWgAk7hV-mJ6vvFlrZ1xtTSFT93ulTklPRLfN6yx3xnPCt-odMC09ySOowFkHBGzWqJ9xdWbNk1XNAFkaVv4qXW4IQeqZ442-AXEpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXyGzgigFuJH4HM7biyIeya04ZZBnTgGMCYvuQ3punodOjrxU8SuR_gdDND1kQ-WzkeW6iu0rk2qbCjKQBKN0jczGrYM4-CkCdgJ4csqsOs6djkyX5Jv6GgjnVlIGs1vo6Ml9BRaPp9EW7EYSX_A9AHmaoG9N752f6nBY-MK46x5gDrSs6yoaN98Ddw0izlu-nOJ3uCqlOAjuzxLCX9Y_Ni5KB5Tbpkj90bC_yjbbLqlZ9W_XyKxTZt6SbGbv6Rrk-J_e3l3uwfAdNLF6dEnMRUtY75YFuyHxm4O5Fw4HqJAjVXR_MTqvFahE69DkLxOhwe2N3rp1cgwaIKDsli_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDElCV_SFwhcFKWuuH7JozVDCEXJgN3hg626B8Sh540i_dJBpZ-BuvJC6Kje1nf7JUbkSl7xjt9BiQCEdmR2mxbFmA8zlIwTd1t5gnVuEZFkbXcTDmDobx-TwaEBrIF5HK_aytcuNy2oSFTp7FpuBeazppIm3NQF0LRDkB4fHEMRSwEh26dLstREdp606u8j-Tk2ujomf_d_MYS8eyGFmjYM5I4XcoTMRpAWLxMm4TuL5UVi_vGttmDvIFFVkDxT3xZPieXSPeosNBqGKArxYSBhomSP3jSFrkTwPMQllARtyQNIyjMo_547fryVbKS1YrXoi35f1cmN87ccFgNR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnH-066kPPqOYesWGKzXHeIPf7xwYk-GasiwkLvo-3wiuQDM8A4qshn6wkhsQzMpNtSOB3I2mJ51hNSPHZXpaArll9eCiiVkSOO2NKCyHQnr79J1Yz9idLMuhmM1WQvUkPAdj2VxVUUNdC06D56uolMDiHbxTqxRY7Pubi6uabJp-ZxK1ZTO5Z0vAvym4GVTigJSZMOcCfD5UnfVr1mgsooz58E6tNEcBD185BN-T_qWdrjTRH7NHzi7yZgAbcJfJOqmboFIbNFbKlYRA4MsCn-S8z-eCrcoKDfoS_-JR4bAtgjNUiJXeA5NnkZ8OAQgPSXXlfxvdkx0QIVCUZmcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ayQFFKtAoCp8lvcNmpBmbKpG1xTk_3Put-KUcKsexnq0bWDgC_XSnN4MwpWQGmDqOzF5ZWlekgchZ2T7YZuj3Luw7oivu7bpbmJ-fSJBd7KRK2IBrD0dLVnTR_nH8c-I3LdLz7hhiD_T2DFIpGk-zjugI5a9zAWL_fMuLuvllKpyhVBw58rQ_AZQNIWQKmMnEUP57j5tdonLCiQOJlqAFpfRPxAa09qk2UnXRp7dWbiRlHr3eFBCJ3dbvMhBhCkIZLt4RHCkeqM3nDsfySxNmUrqzyhUUAldlNT2MySz9YnU_H7Fm-8nzqcGr8sewrh6v6Q8SKMzLywkcXbkz0_iLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZXtul-XGiBqpuIClAZ8j-RZ_cIwYu8zWXgAgif01_GhS4CT_4yV8TNBABbQ7H8R10M_S6y_xHAlI5ulu3MwswrKmZ7YR6TIEZIJDMdy0GuazAIa-faW6BfEZAz9gXIRC-oSA6HfCH6Bxo31kR3fpwg7HExncR6aOVYqnUmrjm2AjSjZYOcZTaVKoMnvh90JnQoxaP0H6ygmxGW0SW882wnRsFxfpSMBT0m8M-pZNtkrzKskAVihzixOo02xjXJsfe-49AOqD4i5pNEr8vHXNgpF14Ok8tyw2bf4Ed_F6UICobDphnCPSIejZkDP3HVw1xuPey9MKptJQMRkRnPOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkvV70TxHzzUfPFfSKNT_aoTGzWkfoKkoAhTJbmD-o5pPiqEv7aBEm_7icKmJLU18H0ZGsIEnfs9GFLJBBJGSit_2ffMCoGsuQQD36KMVU1xmESDAJ5sSKVeGiF5D15K2sf1uwf1I49vYFwXPk5R45Cht8V3SecAE8Un67gwhKliNG2BQHyPL9eXCAvRD3mt1nEcm7hjTDt0HF_PTOChr_qakQHvJGOhc26sGy5GK0LwqH06xlqF30yqe4tvNdIxOfOlZKCES3mD9-hSmpQzTZdsKCXiSw2tWFYNa8K8h7PwY2LYcY5q5iiUgfazgWKLysX5aReK1ZGdGX36uD69Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری تاسوعا در قلب بازار تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/444508" target="_blank">📅 17:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pdz2JjDF7kQWKiPv4WqTiYGjBtME1gefdBUfc4vWjvLTDyu8ddxTF7RBMMGUHpfEEx3hkyVk0Xcp8mfzfmsTGN4YdOa4cTqLg-n6x_79kQWHV8jYSIR6x_Yxrvq8xO3ZhSGlaqMbYI9OTfnMbXRBmsu3KdGpfCnj2TTKdmzGotOETRWBWnM7NJtvDCAI54HThumgfWouWVM4D0rjH3DeK7RFcbwBMZFbPFqD60d62Re8r9SIS5XkEDON1AnZAcP35V3EmsG1Vfef58D_PtWD40ENTooJb4Np8snGs-4NwfiFv-yfzfkgWJIKZ56o6IQ67UthSMgo-4bN1UoJicv3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک نظامی اسرائیلی به هنگام تخریب خانه فلسطینی‌ها در غزه
🔹
منابع اسرائیلی از کشته شدن یک راننده بولدزر در غزه در پی فروریختن آوار ساختمان بر سرش خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/444507" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6437736592.mp4?token=bpvyU_L9zug0KDzwCJESy2-3sltX6uQedQw4Iq8QDevB6JUj9vzTfIn-hXIt1MqJo9UwnvzWPBlNCwB_XY5p317Xnwj43v3ZvzOtG8-yS2AMYC3vh-UX6WJj8RvrL6ct-uvjPl0xFjgqavr6I1cGOA7a-o8klM9U8_TNXLXF7X0tnEAJ_pkCR4n_tdegS0VYxi7aCVoBjMG9vkVeucxSBWZuIHw-R5nfkM-e98AY89xtdepp_Dqa78sfJ2MoRevwsHCFkDcY-7ZRWJR1Q67QgjnzcZ0K4NQLvlqmx_TSNs5IxIIb9BMrTHyNiR7hWdmCL3t_qWBvPMgPv2N_gcKVXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6437736592.mp4?token=bpvyU_L9zug0KDzwCJESy2-3sltX6uQedQw4Iq8QDevB6JUj9vzTfIn-hXIt1MqJo9UwnvzWPBlNCwB_XY5p317Xnwj43v3ZvzOtG8-yS2AMYC3vh-UX6WJj8RvrL6ct-uvjPl0xFjgqavr6I1cGOA7a-o8klM9U8_TNXLXF7X0tnEAJ_pkCR4n_tdegS0VYxi7aCVoBjMG9vkVeucxSBWZuIHw-R5nfkM-e98AY89xtdepp_Dqa78sfJ2MoRevwsHCFkDcY-7ZRWJR1Q67QgjnzcZ0K4NQLvlqmx_TSNs5IxIIb9BMrTHyNiR7hWdmCL3t_qWBvPMgPv2N_gcKVXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من زیر بیرق اباالفضل‌العبّاسم
...
@Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/444506" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d63faca1.mp4?token=cI5dZVqgR5tBozEWjjWSEvzEfssae5WJSZFDwxm3xxgbT3OhirsBNc7v0YQWL0J3pDPWjY2p51Ua4Vx2HJk9BIDYhUI3V05NA7W4KJ1ADs63R7eVyVQvr7J5OdCE5mMwBLKylHKzulBPaIAQbMMgRdFWlZEllezE80gpzhPp1aaGmsj0HOj6IBpWi8YNTgyoN0RKDO4o6CZ7kz49xaJ-E3SeJ4_MotZUX60jtTLJwgpt3QaMPkvFtoUidQAwbzNzSjvHk_6-XbO66eP_3cef25YS_ldoRfak2yUOCZHfRjxa2Nljrifzg9ER7gvFpcI4t4ykt4i5Rc3OZk3p2egWtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d63faca1.mp4?token=cI5dZVqgR5tBozEWjjWSEvzEfssae5WJSZFDwxm3xxgbT3OhirsBNc7v0YQWL0J3pDPWjY2p51Ua4Vx2HJk9BIDYhUI3V05NA7W4KJ1ADs63R7eVyVQvr7J5OdCE5mMwBLKylHKzulBPaIAQbMMgRdFWlZEllezE80gpzhPp1aaGmsj0HOj6IBpWi8YNTgyoN0RKDO4o6CZ7kz49xaJ-E3SeJ4_MotZUX60jtTLJwgpt3QaMPkvFtoUidQAwbzNzSjvHk_6-XbO66eP_3cef25YS_ldoRfak2yUOCZHfRjxa2Nljrifzg9ER7gvFpcI4t4ykt4i5Rc3OZk3p2egWtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مستان همه افتاده و ساقی نمانده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/444505" target="_blank">📅 17:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b59c54660.mp4?token=YVEo6rs0nEFg32_irtxbdRm6DFnDVsmfKFufcpgQrMULsX9qw_n9GUTaR_DWG3ndQonpdF3Xq7GNt0hD7xxK730RnkJCbD4UyOXb5lug0pHO_g7R4JpMRdfVRZPFAMoxzK0hP4jxSKJcv5etH4zWRc3etcJTWXJx92gucKIqt-Y_nSc_SQ-08N3cGc_tzPa-VE7vQBq5IPUpALnt2wKBPmavgMEyTR_1vFSaVnUmbswa9G7BfYyQIZDBIFm6Djj4eRIYgnKl0k8IpBRWs9qF1fAMhxdk4xitkR91U3Jhs-EwxGaiAJArawrB4tdq35ozga6NK6R4F9oa3Tclp_oa3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b59c54660.mp4?token=YVEo6rs0nEFg32_irtxbdRm6DFnDVsmfKFufcpgQrMULsX9qw_n9GUTaR_DWG3ndQonpdF3Xq7GNt0hD7xxK730RnkJCbD4UyOXb5lug0pHO_g7R4JpMRdfVRZPFAMoxzK0hP4jxSKJcv5etH4zWRc3etcJTWXJx92gucKIqt-Y_nSc_SQ-08N3cGc_tzPa-VE7vQBq5IPUpALnt2wKBPmavgMEyTR_1vFSaVnUmbswa9G7BfYyQIZDBIFm6Djj4eRIYgnKl0k8IpBRWs9qF1fAMhxdk4xitkR91U3Jhs-EwxGaiAJArawrB4tdq35ozga6NK6R4F9oa3Tclp_oa3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عالی‌قاپوی اردبیل غرق عزاداران تاسوعا  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/444504" target="_blank">📅 17:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b199c517.mp4?token=Bql5gPM0M2NNZYHCaSyiugx47oDVo5n963zr7shmBFZYl3jrm48YUthJsXLHQZdzP49UJcEQPOw5YMHgEIrKARsD9evvJNkNG1lbbmal0vZcVPZkiEtx5i6-OcCv8Df-0ljWuWl9sy3tLbJ9ou_oLS8qoYkL6NXF_0FEgNZ6YSdfXj9HLSxPKMNmaXrvahXipV8rJlXC1OqxlpXNIu1RRjeeYfluaCmBhcSqFu3Lw1a-k5AxVOJ7gT1_2iAYWTIxszYmfCDc4p1UOFTTPuZ8Vr8Y4Tmfwks0KkoIkw16mHOZMI-eANyarDWgPHExvtcAKVfdtCI7bg99ARM-w9crsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b199c517.mp4?token=Bql5gPM0M2NNZYHCaSyiugx47oDVo5n963zr7shmBFZYl3jrm48YUthJsXLHQZdzP49UJcEQPOw5YMHgEIrKARsD9evvJNkNG1lbbmal0vZcVPZkiEtx5i6-OcCv8Df-0ljWuWl9sy3tLbJ9ou_oLS8qoYkL6NXF_0FEgNZ6YSdfXj9HLSxPKMNmaXrvahXipV8rJlXC1OqxlpXNIu1RRjeeYfluaCmBhcSqFu3Lw1a-k5AxVOJ7gT1_2iAYWTIxszYmfCDc4p1UOFTTPuZ8Vr8Y4Tmfwks0KkoIkw16mHOZMI-eANyarDWgPHExvtcAKVfdtCI7bg99ARM-w9crsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامه سمت خدا: ماموریت ما یک ماموریت الهی است و باید فرعون زمانه را سرنگون کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/444503" target="_blank">📅 17:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9ace070e.mp4?token=t0U_9RYobrRHjwbv2GZKd5VlUa-bwwv_CVH0ODYQpYr3GIkAk-Kq0gxRgkUrLwPNcVfHx01Vjf0atyIosYvvlfUQZgxwNDOJGOwedcxagBDrhiLw77UeBreIcv-bvxPxdYM9WXwJFLaWcxPbhdYg9XSzwdOVOiJgNoYo6t7GHvrKkpCUD6KP4HC6xRPZFKlVYnZF3JEHF2HSdXCK95tAuW6S3M2sAW0i_FzsyZg8zoirF0KCJtbMNirhGB9tiAQ86kQ5vOzWT4LkpRkuBuib8OuXkoP-AgxNRPJ_MEALOAnpSJtGFW8ZbZ8Hz7kR_nD_gKA0PLMw21tms2754SLYZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9ace070e.mp4?token=t0U_9RYobrRHjwbv2GZKd5VlUa-bwwv_CVH0ODYQpYr3GIkAk-Kq0gxRgkUrLwPNcVfHx01Vjf0atyIosYvvlfUQZgxwNDOJGOwedcxagBDrhiLw77UeBreIcv-bvxPxdYM9WXwJFLaWcxPbhdYg9XSzwdOVOiJgNoYo6t7GHvrKkpCUD6KP4HC6xRPZFKlVYnZF3JEHF2HSdXCK95tAuW6S3M2sAW0i_FzsyZg8zoirF0KCJtbMNirhGB9tiAQ86kQ5vOzWT4LkpRkuBuib8OuXkoP-AgxNRPJ_MEALOAnpSJtGFW8ZbZ8Hz7kR_nD_gKA0PLMw21tms2754SLYZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری عشایر ایل قره‌داغ طایفه آتمیانلو آذربایجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/444502" target="_blank">📅 16:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
اسرائیل از حملۀ هوایی به لبنان خبر داد
🔹
درحالی که آمریکا طبق بند اول تفاهم‌نامه با ایران متعهد به «پایان فوری جنگ در لبنان» است، رژیم صهیونیستی از حمله به بلندی‌های «علی الطاهر» خبر داد.
🔹
سخنگوی ارتش اسرائیل: نیروی هوایی به دو تروریست مسلح حزب‌الله در…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/444501" target="_blank">📅 16:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJFERMUJOipZshUz1_JqQ9IUtOgPpZQAcnh60C8dfAUueJGYgSdnOhecS2GSmPmsKjX71H5zTGedqjTDbHLtPWDudDpiAnIWdwbOst3UPbbXd4KflpygSdJGw5LIeTeMANSx4Pv3LMsktUidWxngrAAILN8b1caah2LsrD4zPVLtQGcaJydKcm3INUQFwye5M8lhuIgdHdLnD3UTzrAGhvNaiQAHv32e6HQ6O9Rw8sj5c10IyRom8zS47oJwdztWWZdpuiUGziynhGK6yNhwLZGIAiF-TB4IZAUBsED3MsxnmBFq3KoHj4xp9M4GdqU0NBqowc7W-f9udlemY4OZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پول ایران را برای کشاورزان و دامداران آمریکا آزاد می‌کنیم
🔹
ایران به ایالات متحده اطلاع داده که برخلاف گزارش‌های دروغین و فتنه‌انگیز رسانه‌های جعلی، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ‌گونه هزینه دیگری از سوی ایران از کشتی‌های عبوری از تنگه هرمز درخواست…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/444500" target="_blank">📅 16:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8d15794d.mp4?token=RNiLdCwZ9rmPCrWnYdPJBE7FpjpJBGGXz_kJ7HrablAC2ex3k5L6H4u8FUUaMHAc5GR4mNdxAnYryp1rFI2afqEzO_pOsJnM6XoQWpPfVh5EDko31Ed3phLlu5cGJMBE_y5WR96yr2K0y5EQBzAZrsQT74EutkWkCt1WCEzobPapkn28q9OWL1C9bGls3Lwdj2sVmXDprOnu2u1Gytx-_rgB2NiEPEq0BkHHN6E7FoELz4Qh0tdDRf4n_fgvr6WYbMqR1_MeM_iY9vqyI93Jl0iyh3wAhECj9eFUMm86Z6c620XkmdwEgYTtqxHnfbMQ4Yx1IM0ak9o7aLoWSPti0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8d15794d.mp4?token=RNiLdCwZ9rmPCrWnYdPJBE7FpjpJBGGXz_kJ7HrablAC2ex3k5L6H4u8FUUaMHAc5GR4mNdxAnYryp1rFI2afqEzO_pOsJnM6XoQWpPfVh5EDko31Ed3phLlu5cGJMBE_y5WR96yr2K0y5EQBzAZrsQT74EutkWkCt1WCEzobPapkn28q9OWL1C9bGls3Lwdj2sVmXDprOnu2u1Gytx-_rgB2NiEPEq0BkHHN6E7FoELz4Qh0tdDRf4n_fgvr6WYbMqR1_MeM_iY9vqyI93Jl0iyh3wAhECj9eFUMm86Z6c620XkmdwEgYTtqxHnfbMQ4Yx1IM0ak9o7aLoWSPti0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عالی‌قاپوی اردبیل غرق عزاداران تاسوعا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/444499" target="_blank">📅 16:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d29db6d55.mp4?token=e9gKiAPIQGSMVJRF-iuiKK1wRZzjJvlhGEnbK-jzopfhAoqSs_zNAsXphziLPJI8gdYfb97gNzcJMbXCqpit-fhWRqx0n-OvZx3WDEBCw3boWXtykKtMItHFoRoV4-5h15wh05EtIAbpMWCbyhN-ndYFiUS2Ad4OHRU4MxxoIc2v40-NT6wInWBxNez3W4MgSPO5vCTfbUtr6FEXUBFzqHVmdiFysR-_VTvsOLROai843BkYKxbpsQEZnT9TpJEbGu7y16jXYmeJmFo5njeCh2SSLzEPtriV2NCUyuddjVV2if9hQjRitMHq9NlEwaqPkJeHtMwtYY5c9noKxnC8YSoRPjQo6auT7zA-9hNLXfffweNvEWN92SrKy4xjMIdPEQLUag7bfK-kcaQuVqzsJFGuHfmAso4PZFTuXfGYib-UX1eMmEAjtTw-3Oc1Puv1hZZxJOuThjAcpwJc6nn_wXtDzkJStRUtdwxGtCsS_pFrwZu4G8ioKqnASGd16ZFsCLlSBJIzFoMcekfwDIIiiD3Nx9WqfwaXn9XnMMeVtdkMJqWqhfu3oWOo0PmO2m1M4_TGk3h7gflm-Mw9sX_GmodvNO8gJnAPQjBv14kKFwjT0Mltd7KAZpPXckX8XBTQg4hZB3h5jwTS0iSxRg_j-1GjRcapQVPvYkBsr4w55TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d29db6d55.mp4?token=e9gKiAPIQGSMVJRF-iuiKK1wRZzjJvlhGEnbK-jzopfhAoqSs_zNAsXphziLPJI8gdYfb97gNzcJMbXCqpit-fhWRqx0n-OvZx3WDEBCw3boWXtykKtMItHFoRoV4-5h15wh05EtIAbpMWCbyhN-ndYFiUS2Ad4OHRU4MxxoIc2v40-NT6wInWBxNez3W4MgSPO5vCTfbUtr6FEXUBFzqHVmdiFysR-_VTvsOLROai843BkYKxbpsQEZnT9TpJEbGu7y16jXYmeJmFo5njeCh2SSLzEPtriV2NCUyuddjVV2if9hQjRitMHq9NlEwaqPkJeHtMwtYY5c9noKxnC8YSoRPjQo6auT7zA-9hNLXfffweNvEWN92SrKy4xjMIdPEQLUag7bfK-kcaQuVqzsJFGuHfmAso4PZFTuXfGYib-UX1eMmEAjtTw-3Oc1Puv1hZZxJOuThjAcpwJc6nn_wXtDzkJStRUtdwxGtCsS_pFrwZu4G8ioKqnASGd16ZFsCLlSBJIzFoMcekfwDIIiiD3Nx9WqfwaXn9XnMMeVtdkMJqWqhfu3oWOo0PmO2m1M4_TGk3h7gflm-Mw9sX_GmodvNO8gJnAPQjBv14kKFwjT0Mltd7KAZpPXckX8XBTQg4hZB3h5jwTS0iSxRg_j-1GjRcapQVPvYkBsr4w55TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز مردم سنندج عزادارِ علمدار کربلا بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/444498" target="_blank">📅 16:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
رویترز: ریاض میزبان مذاکرات ایران و کشورهای عربی می‌شود
🔹
خبرگزاری رویترز به‌نقل از یک دیپلمات آگاه گزارش کرد که مذاکرات منطقه‌ای برای آشتی و نزدیکی میان ایران و کشورهای عربی حاشیۀ خلیج فارس در عربستان سعودی در دست برنامه‌ریزی است.
🔹
براساس این گزارش، این مذاکرات که با حضور اعضای شورای همکاری خلیج فارس و عراق برگزار خواهد شد، بر موضوع «مدیریت و بهره‌برداری آینده از تنگه هرمز» متمرکز خواهد بود.
🔹
این نشست منطقه‌ای، کاملاً جدا از مذاکرات صلح جاری میان ایران و آمریکا و همچنین ترتیبات مربوط به مین‌روبی و پاکسازی تنگه هرمز برگزار می‌شود و صرفاً به چارچوب همکاری‌های منطقه‌ای میان کشورهای ساحلی و ذی‌نفع این آبراه راهبردی می‌پردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/444497" target="_blank">📅 16:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444492">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خراسان رضوی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-GPF7ipsJ9S3qN8DV9DlQ-NA6Z7x3660YAQHl9dQHruq_oHx24bTY2qoIP5mFqLD6Qk-QG_G4bfYe1LHEnhhFYMMAhOmpHIU0SLVOBP536Qx1YEHcBuDZw0Zx5Onjp7Dp1N4rMBRyb-6GaIW1pGv8AsONmgEATYkxzQjf-PuvHdTOoNMgq0bA7ENCRH334PjEXHfZdrof-_M0fd8ZOieMPGtccgELFwgcZrvY0rVaVmaUp7z22ymnWJiUidrkcOhSBvgNhn1hdp3xNu4LthJ19CKq2PZPO2MyiThOwuiybAwVCie96QiAM2vXaPnwYEHkgSp5h2hADufjU3fiPjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRsJt0oiPNUzA3XHyFnw_3n4Um2PRzPIrNunZBk6VkGR4GeL4GdkMI-L622Fp_6V1SaHkLGWjPqOJQnxGru-_iKPxvQAik9AgVGEJbOAF6OFQ9zFqDT_LqNeVoHfYtMFSGr64fEE3RFP5Pisno4u2WHIX6EoGEnSVpbIFFCBoKGEyQ7njZYKzVog3S_FkISooN3-wBrKILluedXObQprB8TQ3l09vjbTZxblTbzrc_hswOxmhsWqKEXzoyVQ3zhky2DtJBz5eWUGqjfwpgdPsKzNCe4TWAj_s0UZk_c8LrPPGC_10_dj19ehgCMGZ2aF6jIzqNeojCpO8kNDjfIg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9Irj3BIdeR7Aae20cqWW4kDhm7DubK8jq3hFGPFscPlmL_1e6KFqJ5ZhTz2O9BTpVxkx6NIezObb2NgVviXQ2lHQ0TkPyZ5tRyL0MgFKt7DWLUeUIZkYEMCkPrQyEETZxNC-wHA8kDDD9g62fFiximlcaoqCzJRS-l76CG3h74LmWe7gtcsjjUIeDQnQxcAg6U67kvDJWkellWq1DeVEWMCkipOMqesqsVY-yoZLc_pWkPbhx8wCEbW0zOKg-4blzm48mCtyQY7y_rNVSsUOta6vMlJkiBsmwkmvQkZrdgBXW-Zamjdqp-XmaAPcGxBckeUV4QkbIIkXhcsm56CMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eefGNg7NUdSkqvPM9zNeD79SNHiuaZzYH1JnLvyUfwi9vio6wOzfQQUHFVj_HCKHROCoO9q3PHkLv2gtNYBiXUmUm2WzOsnuALOeuwFUAs5VJQVim1UMmJXM0Y_LRfUbJbDYo19uEmulhOmMkHEtckf58vuCoUNpa5XTUDQkTKWOjtDzzn0aIBx2pljpLFBf8qn_LfjpEWzfq7Ro1aV2YMcZhLJweS7xGvlT7V4otcM4nsdaw2ZyI0HS4_KmieGzGbOb2YbhHD9bna_htxQsZxYVIsruT6IqjoBpiTf_dkv4Od3aFQ459MSOVhMLd3OyOoFqscsoLJtE3zYfMDaUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9bImsejKQPr1fluizss_8GjTgCJwaOiRIjRUJf-cnK35POOUVbbfnsN0n8nAJKW5nP-1Wm1DOIhr0Be7wBYZyZJxMNEgvSykCee5hv2jwMvyA3EXhu2KXllprl3jlOp2bsbEtH9YmGid0QfQwNZx5qPIoO7I8Y23BpUqkl05JisMHopKWt5vQqaeK0Bx9bH4P69eGqo9XbptvdHkLun8K8oDGFF9P8nuxIxDezA7RZcclVguPC5ipbs4oaxP38r3yF2_d5k5SKoYFpsCC_JKB4l3ayjRtxgj2QViPl1uSu1SDgQLdsnR8f0ET1fi4to40dmOr_cLaTeKzkDa9FcoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تاسوعای حسینی در حرم امام رضا(ع)
عکس:
حدیث فقیری
@FarsRazavi
‌</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/444492" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444491">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d71a829b.mp4?token=mp-mHGIurn01byOWj-SQKaK3RJ8olsiwc1heqcBzJL-bfKToRrAZrPg1ymTQqekqEi60ooOm73hnoy-5hskyMKdPec5AV79u-2i8ciqwpiR2nIXZVucWzGWoUUSD6ItIvtD9vCHc7YilVFCH1UDwN6pInIvVRkzQ5eaU2WxxeubvgxZ-JUVPAnqSqsfXc2ArKhSR7kxjzRge4QQc7a2yFoLDBOWKK3pNYFTX8eYH2yHS3zb_m1S_MCj4cCKpd6ed2lPUGw8tbeXgBY6zdUoEL2Y8no1NqzCqjw8Q20krbmAQz75vTsvkQdnmhvD2ROimkG7O7wD1bysl9gCTxrqmHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d71a829b.mp4?token=mp-mHGIurn01byOWj-SQKaK3RJ8olsiwc1heqcBzJL-bfKToRrAZrPg1ymTQqekqEi60ooOm73hnoy-5hskyMKdPec5AV79u-2i8ciqwpiR2nIXZVucWzGWoUUSD6ItIvtD9vCHc7YilVFCH1UDwN6pInIvVRkzQ5eaU2WxxeubvgxZ-JUVPAnqSqsfXc2ArKhSR7kxjzRge4QQc7a2yFoLDBOWKK3pNYFTX8eYH2yHS3zb_m1S_MCj4cCKpd6ed2lPUGw8tbeXgBY6zdUoEL2Y8no1NqzCqjw8Q20krbmAQz75vTsvkQdnmhvD2ROimkG7O7wD1bysl9gCTxrqmHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پروژۀ‌ محرمانۀ اسپیس‌ایکس سرانجام به فضا رفت
🔹
شرکت اسپیس‌ایکس دیروز برای نخستین‌بار یک کپسول بازگشت جدید به‌نام «استارفال» را به فضا پرتاب کرد؛ پروژه‌ای که تا پیش از این تقریباً به‌صورت محرمانه توسعه یافته بود و اطلاعات کمی درباره آن منتشر شده بود.
🔹
این کپسول با استفاده از موشک فالکون ۹ به فضا رفت تا توانایی خود را در کنترل پرواز و تحمل گرمای شدید هنگام بازگشت به جو زمین آزمایش کند.
🔹
هدف اصلی از توسعۀ استارفال، انتقال سریع محموله‌های زیادی از فضا به زمین و پشتیبانی از تولیدات صنعتی در شرایط بی‌وزنی عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/444491" target="_blank">📅 15:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444490">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
اسرائیل از حملۀ هوایی به لبنان خبر داد
🔹
درحالی که آمریکا طبق بند اول تفاهم‌نامه با ایران متعهد به «پایان فوری جنگ در لبنان» است، رژیم صهیونیستی از حمله به بلندی‌های «علی الطاهر» خبر داد.
🔹
سخنگوی ارتش اسرائیل: نیروی هوایی به دو تروریست مسلح حزب‌الله در منطقه کوه علیطاهر در جنوب لبنان که تهدیدی برای نیروها بودند، حمله کرد.
🔹
پس از شناسایی تروریست‌ها، نیروی هوایی و نیروهای میدانی بلافاصله آنها را هدف قرار دادند تا تهدید را خنثی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/444490" target="_blank">📅 15:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444489">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6jBSYnDSnoIdMqdAiCyKG_1PsGmxKhra5VarCoP4RzHW8p6yM9GTj_UXPTITvPIt2sZZeKVcY30tGvETEwnHbDzM09SbHQGRG9YQOd0TN_mbpIpQuQ6nmLWKjjlH5qGSXKEsjnxwVnl1ozcJuWhAQkgJ04hxxUQH2-om5JzPVZeN43A9yoVxPqUc0zrzuDoregfLvqpAz8NAsw5qBPYzZe02qgpCm0LydPDN7UF_bl3HQmiT8OdROlhRyryGftphlkxgEL6emmaE7FfE1Et-j4-XU-5__ULz07lawGV9Vf7DO14QHljRxgPyPHk06Dd2LJzZjRT5u7k7_B3jeDiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود هندبال ساحلی ایران با شکست آمریکا
🔹
ملی‌پوشان هندبال ساحلی ایران در مرحلۀ گروهی قهرمانی جهان ۲۰۲۶ کرواسی ۲ بر صفر آمریکا را شکست دادند و به دور بعد صعود کردند.
🔹
در مرحلّۀ دوم که از فردا آغاز می‌شود، تیم‌ها در دو گروه شش تیمی قرار می‌گیرند و برای رسیدن به دور پایانی با یکدیگر رقابت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/444489" target="_blank">📅 15:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444488">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lny74CI45o7UU83YfxM3fTfsLexVxIUGAylwLIYDbPDhtgC-1u_75x-aDwzQ-DFPWLDKsCyD78REGcC3eVYlXy7D23nDs3mHdvgEPGBTWeheqw0MUNN2x_gko57BMuAxBkF8erk1NQTGkdqgTZUyBzm4p6QEJuzW8InEVKDwztmnkXOScILFDytYWQVpCxCa8sO3g17ctywLzM68Tq_wqQ2iXBGuMOv1Hnvt7vvJdHU1wp9Rkza5nm5O1kKrNSG64DJdM81cWn7sXFGdjl11jxZXAaZuXRCtB9kOIw_TbRBxE9eiAi-txsGL96sd2COgoOvLqK8psUsaZQJhyP-raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قالیباف: پایگاه‌های نیروهای فرامنطقه‌ای در غرب آسیا منشاء بی‌ثباتی است
🔹
ایران آمادگی دارد با همۀ کشورهای اسلامی، براساس اصول احترام متقابل، عدم مداخله در امور داخلی، حسن همجواری و منافع مشترک، همکاری‌های خود را گسترش دهد.
🔹
ایران از هر ابتکار عملی برای…</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/444488" target="_blank">📅 15:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444487">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d529e9614a.mp4?token=qLcyVbi7jbrse9jDMERL8LfKBqcXEgdCGUazCl43WXGRJ7L_meQM73RywgIffP5qqari2WNhC1jisGnMAL33oD1RGKqGH-sbw0XiVEbxNRiwNC9jdRdZo9JeilJr4SLOOAZx-9DDrXAXDs8gVGxHeD7vnIxJXuCILLL6iqk0gbRT_9slkYUVrTlCZTDWsyRCQN_zECV2bc1mQPgUc7-TbCBJDMFS99CN4Px3A3muOeK0oTHKXod6o0MwFc5TDiluSBMOp64tTiJMYHj-OtysVm4u2mDwuKyRbaxTLMlRrw8_Z9Qytcpl_kT1LLX0fYdCp66ej2wwOBga6eMXeYpIATOym9KKdsNO6RSSF43_aXr_nJiRnrBXx3kKmPlUrjD3UnBRhDc9Hdre6806YmCfQm4-WN2w_PVZqnrViXZ3ryxq6twHkRWqaRZhzohBBfbXAwnU7tJvl6g80-G8rR8n0Qp4mR82BPNieM96XYLTN4HADIicRQlYBq1z-iMzVxk0Xm1PNgr0IE3dsNti2TxMA1RQ1kOJa2Tz1dHLTOLxjnC51kKkGvz9EMR9iaLKIgXqC3rr9U7HV0V3AZknJuygZhXxxfp660GGQUEBMhqXgDh6hquagFFlHdt0cgO3TI6R2N1eTrN0aH--2EFlRyKIFoF87tcqg8wBQIPGZLlwCw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d529e9614a.mp4?token=qLcyVbi7jbrse9jDMERL8LfKBqcXEgdCGUazCl43WXGRJ7L_meQM73RywgIffP5qqari2WNhC1jisGnMAL33oD1RGKqGH-sbw0XiVEbxNRiwNC9jdRdZo9JeilJr4SLOOAZx-9DDrXAXDs8gVGxHeD7vnIxJXuCILLL6iqk0gbRT_9slkYUVrTlCZTDWsyRCQN_zECV2bc1mQPgUc7-TbCBJDMFS99CN4Px3A3muOeK0oTHKXod6o0MwFc5TDiluSBMOp64tTiJMYHj-OtysVm4u2mDwuKyRbaxTLMlRrw8_Z9Qytcpl_kT1LLX0fYdCp66ej2wwOBga6eMXeYpIATOym9KKdsNO6RSSF43_aXr_nJiRnrBXx3kKmPlUrjD3UnBRhDc9Hdre6806YmCfQm4-WN2w_PVZqnrViXZ3ryxq6twHkRWqaRZhzohBBfbXAwnU7tJvl6g80-G8rR8n0Qp4mR82BPNieM96XYLTN4HADIicRQlYBq1z-iMzVxk0Xm1PNgr0IE3dsNti2TxMA1RQ1kOJa2Tz1dHLTOLxjnC51kKkGvz9EMR9iaLKIgXqC3rr9U7HV0V3AZknJuygZhXxxfp660GGQUEBMhqXgDh6hquagFFlHdt0cgO3TI6R2N1eTrN0aH--2EFlRyKIFoF87tcqg8wBQIPGZLlwCw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری روز تاسوعا در روستای محروم خویه
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/444487" target="_blank">📅 15:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444486">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed756b6b2.mp4?token=pUQwRzvYxgCPGLmMRbzj-E9Xj093fwZ4A8qOIDGHwMG1dOS6rT1wtCgbr2jmN0cFxv_dLcWM_DkWG5TsSq4Sr6NOPHPmop53lr51nKwsbJCAD7QbJl5hjnL7loBnjJ4l2kKsQAHLlCX-R3U_kIqrbhYNOEFvGsf_JKpelqUaP_OYf5bbiXa3ItAv6xKm2LUtERxmtDMK5KnZakk4uiJ-c8RfUsvqigd-Onvcg7GoJi1HAOmYTXzeRMn88TECQAusb4rVPxg3nj5xWxCOpQbCMrozsjxY3lq39afmL05630fRfEhw_IeYbj6rkS2ovIFdwmj--wE9wHiUhizWEpU1zx8X5xBN4kRLRblvdHjZcHGhN8JDTeVRSsHw1xPZxkGl3l2b-LtfHh4cvu6bCGI3gfKiIuy-YgXylSIdwh__hBRR-EVEJ61vWUiktQoHJmx_rU8gzdsywPvfv64jZWQB0ZtJI2yyKkkbYJQ0rCTO9rqOFibXoCFh3oClscJBZtn88RBXqCjCIBuPEumjyqaMKapfpZbs3HqLr-9NBjim6NVFWC0MExtaFkxDWogYQE24qv5SctDgWRuxhlUDuA3h-snKnz1hcGphlA8XJ8DipVG0LGNTN5Ep5X1GhE5hu8Vj-e-v9FKZMsTqk6cRFc3MyHSApfPl1wDpruzC49ScLJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed756b6b2.mp4?token=pUQwRzvYxgCPGLmMRbzj-E9Xj093fwZ4A8qOIDGHwMG1dOS6rT1wtCgbr2jmN0cFxv_dLcWM_DkWG5TsSq4Sr6NOPHPmop53lr51nKwsbJCAD7QbJl5hjnL7loBnjJ4l2kKsQAHLlCX-R3U_kIqrbhYNOEFvGsf_JKpelqUaP_OYf5bbiXa3ItAv6xKm2LUtERxmtDMK5KnZakk4uiJ-c8RfUsvqigd-Onvcg7GoJi1HAOmYTXzeRMn88TECQAusb4rVPxg3nj5xWxCOpQbCMrozsjxY3lq39afmL05630fRfEhw_IeYbj6rkS2ovIFdwmj--wE9wHiUhizWEpU1zx8X5xBN4kRLRblvdHjZcHGhN8JDTeVRSsHw1xPZxkGl3l2b-LtfHh4cvu6bCGI3gfKiIuy-YgXylSIdwh__hBRR-EVEJ61vWUiktQoHJmx_rU8gzdsywPvfv64jZWQB0ZtJI2yyKkkbYJQ0rCTO9rqOFibXoCFh3oClscJBZtn88RBXqCjCIBuPEumjyqaMKapfpZbs3HqLr-9NBjim6NVFWC0MExtaFkxDWogYQE24qv5SctDgWRuxhlUDuA3h-snKnz1hcGphlA8XJ8DipVG0LGNTN5Ep5X1GhE5hu8Vj-e-v9FKZMsTqk6cRFc3MyHSApfPl1wDpruzC49ScLJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
آه ای حسینیه بگو آقا کجا رفت
◾️
آن رهبری که قتلگاهش خانه‌اش شد
🎥
سومین شب عزاداری در زینیبۀ تهران و در نزدیک‌ترین محل به حسینیۀ امام خمینی (ره) و بیت رهبری اقامه شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/444486" target="_blank">📅 15:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444485">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaPwRw-MV9gLeIVzMLDSm1LdRjb0GUq7PWHTHPkMftDlPZJhT_Nn2YWgPtEiQOnF0__KnCI9ywuOaRu4w5EZX-ey8yTxGQ0ktf_ARXaVtYaXany8zus_FNX_0gY6ILWmyKzGlxQDbtcH-0hnHqvkztmIg6JNdmNR4ur8f9XTUHHUpi2qXi9Qm_Fd2Ms2eb9wW1VQGMACETISB2miPM3xPeU6QDpuA1iXeA2j4xsuJHQECTSveGSyDDFIjuIvI1Oc-LDV3jGBCJHxabebh0cCW5Im81xtR0_AoLVXrAV4updgCLMV0BsQM-jutHJSx_m00kBXojEob74g1PcG5ipZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: دربارهٔ اموال آزادشدهٔ ایران هر طور صلاح بدانیم تصمیم می‌گیریم و هیچ محدودیتی دراین‌باره وجود ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/444485" target="_blank">📅 15:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444484">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تراستی‌ها موقتا از تجارت نفت ایران کنار می‌روند
🔹
طبق تفاهم‌نامۀ ایران و آمریکا فروش نفت و نقل‌وانتقالات مربوط به آن در مدت ۶۰ روز معافیت خواهد داشت. این یعنی پول نفت می‌تواند مستقیما از طریق سیستم بانکی بین‌الملل به ایران برسد.
🔹
رئیس بانک‌مرکزی می‌گوید در…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/444484" target="_blank">📅 15:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444483">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO_M_JIm4YDq1o9CVE2-UOACeHfDRm5P72UY9K94-Syv4Xj-4livRo-B0odbc3L_ssXWFZDM7yT-dr-1AQgwbLY2zsVGtKWv2r7GYj7mrN4z8nfrkcjPFsGSzLxFDG_po5vVtjhJLZ1yCHB-ourHK12yG4LP3pSJv_GKK2Oiind94CmzPhV5_A7fDbgxVCJ_syfWeT1D_a3pMdIpJVu0gqKXOXJMvPJaBqja41LVNHGxFC-Te9fuTUFnnlxRTDdkFuPX-LWs-umOvC9eMpGj_K-DHWoIN2X8oOJlXu0U9mMrE79FNIXZ-wYZ9GVsSD9QUSBM4NAS53Te2F5DO2FFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانۀ رسمی «بدرقۀ آقای شهید ایران» آغاز به‌کار کرد
🔹
آ
خرین اخبار و اطلاعات دربارۀ مراسم وداع، تشییع و تدفین امام مجاهد شهید انقلاب را از نشانی‌های زیر دنبال کنید.
🔹
تلگرام
t.me/Badraghe_agha
🔹
ایتا
eitaa.com/Badraghe_agha
🔹
بله
ble.ir/Badraghe_agha
🔹
روبیکا
rubika.ir/Badraghe_agha
🔹
سروش
splus.ir/Badraghe_agha
🔹
توییتر
x.com/Badraghe_agha
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/444483" target="_blank">📅 15:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خراسان شمالی - خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5r3JwF-Hbg91Aiy7gNozu0UUlH7UL33PPPaspOyMdJgQWH5sawL6oHxux7mk9Jpn6oxu6saEPPrYL4zalcXALYpn0iCnx649c0_njsOJvL-Mo9tIYU2JeEgFME7ILWPxKXVaB5MRoYDS7sEGRSDmvogawqkkXtnsh5jYCt_ncH065LAOoqNi-4B5mzTklQWwB7bFtE5b3CQvLwWRM2Q5mt_tgdgqF_xPMbXhp1azVkOw-t0MwDKTzomQT_uEUNme_fWrCD0RItLT992skE9WIdfTAXcGi6Q1ZiTIekKpLFAym_aBun4fS119BKgQbLdt0zSgbIyqi_BUsnRe6h6zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W26PpXv43Z7-IeAHTwX2PEOHsgWasZZUbeKAcoLpzqb8mJG9qO0O0s2H4A1STVJumCIxeKRwkMJPojnBD25LRuG2jWioj8TVm9N4cprX9DqCqYaR6rzP8Z1EMzkeU10z4gn4HnD8D7bnRbbtAeeswlt97mcEKY7WzNFpwUWrmZYyb2PB0OIX-thNydSGXLYF8FLFuS_yN2egYFVSQVG2vU5bYIANB_u3Jnj3pPtHfnKgIzj4S2I1iE8bxtZe98H7zJ5mxqtu3Lw8jKxJPOFsZzjWsUehod9Vvz1Po4E6gSg-UVJ20lhHzl-kUQrEyHa1-2PkzRyR8odGY7QDJA23kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iolnrUQdMTJV-HqZhnXn40PGDzXzAIl0sqdM_L_uw4UX7mjVBvvuq4jLBFGEBQPhkpuNvlyJFyX1ElalmmjXkVUlNLY-Yw2ZM44TnPik1mUwCeATNNz_EukKDQY48cRNplMolTAR1KQ-fjOKn4Kd71mSuu_FMCbFE7JHwNHYFU2j8w7Xq8iv17DiERh4UXSK6ZXbeu7TFYHjEG8GNY0DCtUqFfQrE2KdeDwJ5tRrgXXvGXlPpU544wGerN48J14qxDOcDBCb_oEhATBeFjOXdXM3nrHIBW9-t4Zp_ne5lQgL8gQeZg6irwYEB8ztvNqokQoXDSUTIAKqGgmFryxO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqzzBWttvcRmGD914vY71ZkN_jmyGl9Zp21NrcPIw9hYoLX1gAF-YahZM8fJTQmPjndQ5dXL-7vPLLL6dodiOesaiTmB7n0phFVCcg8YomQ44QvleYg_2WC9Xv2m3Ibz6eGMVqzp1vtj9ypLVwGjC9bwaVEoCdnpjRfhcUc6QNhrgKPaHeRdMd3QvMK95C3r_UTPgaHcr4Tc3nTJmPwzzi_Dcc70yfJ7ar7wYSqOeGRCGDKtn21-WMaCewZdm_cQ8YySFbdQio5XFXG0mCMu8ie4vSc7V361BvtuAIHqJhlgtR_7dAnsqTmioT4ezNrr_C23enjRaDEHvC0vYKBuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWJ3dm-rw4zJg_jt2Sj4AX9wvnOUE_GojHkGpLlAwpmS-1A0raTBEguw7yhdfzHHECYGDZB6nsLoaTFZ9bpogJT2REA4bXMtuhTx5yH-vbAwuka9CL78Bs7NXKeoKQMxIjTZsFLzWMvdwGhjvxgtQeFiYFrwLurl1iNQ68JA2ssw0beqFnz7_DD6f_x0rTczB7CfJjvVYf2QgJqUcmEHf-df2x0CWeLKNVhyGNA0g2hgi64BQbg8zPESMJB38110uQzLCP3Sv8kJiwxWwLFAklZ5ba5jEIgoWGcXKxlEVuU2Gme8KakHf7FcMO9qHuFxZSuueHkmFd5rUolwIlsZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/evyLSDox03X60cknjM9EjGU0jBVHkNJqYDOpS1Z8NNMeTjR7wYrUvFFHnkSadOC0RSOe8wIcRq2EtXRCmnqkffGXPVrdYxYuOZbn-Oee9BZ7dfLQzV9KyzFkubGn_65THvi7ukutpyq4O5vtqxStt1KoD6mADN_BVJfPLoLH25a0m-YEd7GJQ1uEiHbR7KHmJFUT5kfpbl41O9CI_UWPeJfbMmlqVynmYRNQt3e-nxmltgUO5J4GYd_FT4R1mvrxhS0YVOgX9rgoXskkVai_8WwpG15La8hsLWgC_2u9gJjWnnI7Jzl32e-y7pKCYLbSjVvXiff4mI6DIUss7yVZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VN9rjpLgBFpr_XkquSsKoy5qAFpiUH0LDrosz96nH-pn472YDMlC1PmhgSN37sfHYZawBtvJSdhhvwOMactiaysUcatvPOCx1gRu3--SyapnD1c_hVQNUyKD45-7esxH_VPv1mUp4JFQF75X610QgNTcH44BXPpNSPYyANRV09Eh3VtNUNRy8frBo40w11TGL0y9GJvXXdXZ9V70Ia4GYdRSOHFjJbuXInzo4uEUl8IT3uxkVqRCkCV7M7g8lOsuKUo59oGwI-Kh-mdRJaAWU3I3wSTSs7SYsQBl-5X5aJpkue0Dmgqfa8Vwuz6OEjNu_HsSm2dvzE95n21vOrcyHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری تاسوعا در «روستای دَرصوفیان» بجنورد
@Farsna_nkh
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/444476" target="_blank">📅 15:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOTEDwlyRADtuMQ4fj3vW07i4AQMUmMsxgq5HOPkkAsSmSIeYJ4C7145g0pRlsuRnTI0R-CIO6s0lZehQeXrMZ6H-9wPYJS-OfO5mNfkMatcYyqdpvCWEwF6eUUOivXijCY6gOkQSDwt1xU_TQXzr4PKLYxn9_rqtN53af1b9QobxSCIdbWORoxKUREYgqzgV7Gev4tqJy_8Laib4sJf6Pj5dbmERneYzcAwNia00wZnNsiiAIuF838hIgYVEqPs9_BYz7KgXgZkBk4is8gVCgM_OKQ8lXvVsBxZeadD2KxKqFgPU36s4iClvYh36B6FyLDfPzI8BqyOGhDvXa5zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
شرکت خدمات انفورماتیک: دیشب خدمات بانک تجارت به حالت عادی برگشت
🔹
از امروز صبح نیز خدمات سایر بانک‌ها به حالت عادی بازگشته. @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/444475" target="_blank">📅 14:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b289055d7.mp4?token=eTlMsfOkaiKUm1kHy6UjvMGEXMWie2h2kps0P-ZMx08EgDLeRV0obU5OmId3z089z-IhVZGuuPUnx-GHkwXg1SvUNwt5io70RBHfwn90KMVHilbYhVAPDnM_eWoYzsbG0OboV6NqyGc8cIstJcoF65rGGn_J2qUSz5ZcK7El7GPa3DtlY87Hcl1hU8eUaPUbwKNXBBO16lwPRfVQxG5rGTShS0Zd-1OxtBAQfvP8JYh0tEGkNuBTJGXdmZ0UUJy97do_QcSP3cc7WH2A2tLFTCDhrD7K9M-qLXDj7G_JCx9QF9nmflvdbrkEwQVUmhReh2ou6VN_PNlPQ9lhhFMFtHi7WlEleDrlhxNDnstskrePpF97UbwPyWJAkzRjpDi0QRBXOKgaI2qeMZa3uMEsWB2QjeS2y55yXGs5IzOjmPWjymqF9W9y48Z0tRrIAotyz_DK1Bm1yHbZ3z_LA9BNvWvD9akzCDHsP-dbOmt8dAJ18YRAgHDmIFRL02d0hrD5ZOzbCEhyGe1b-j_m7GBsqDNRvxsY3yUHaDtDcjiIlzHMzWPa0NYehAhYoWpv7GzfjrN5QGLGSwUkX6RnC6iOGJ-2MPoMeeMdFMxAcyQH5WVlnSkbceQXhaw3rMFytI9XGjRcoj8v_RFKO80-pOB34LDyMFheV1TDpBCUiDstt-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b289055d7.mp4?token=eTlMsfOkaiKUm1kHy6UjvMGEXMWie2h2kps0P-ZMx08EgDLeRV0obU5OmId3z089z-IhVZGuuPUnx-GHkwXg1SvUNwt5io70RBHfwn90KMVHilbYhVAPDnM_eWoYzsbG0OboV6NqyGc8cIstJcoF65rGGn_J2qUSz5ZcK7El7GPa3DtlY87Hcl1hU8eUaPUbwKNXBBO16lwPRfVQxG5rGTShS0Zd-1OxtBAQfvP8JYh0tEGkNuBTJGXdmZ0UUJy97do_QcSP3cc7WH2A2tLFTCDhrD7K9M-qLXDj7G_JCx9QF9nmflvdbrkEwQVUmhReh2ou6VN_PNlPQ9lhhFMFtHi7WlEleDrlhxNDnstskrePpF97UbwPyWJAkzRjpDi0QRBXOKgaI2qeMZa3uMEsWB2QjeS2y55yXGs5IzOjmPWjymqF9W9y48Z0tRrIAotyz_DK1Bm1yHbZ3z_LA9BNvWvD9akzCDHsP-dbOmt8dAJ18YRAgHDmIFRL02d0hrD5ZOzbCEhyGe1b-j_m7GBsqDNRvxsY3yUHaDtDcjiIlzHMzWPa0NYehAhYoWpv7GzfjrN5QGLGSwUkX6RnC6iOGJ-2MPoMeeMdFMxAcyQH5WVlnSkbceQXhaw3rMFytI9XGjRcoj8v_RFKO80-pOB34LDyMFheV1TDpBCUiDstt-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران دیشب و امروز به‌یاد سقای دشت کربلا عزاداری کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/444474" target="_blank">📅 14:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444473">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1818a75a.mp4?token=oTv-IUhYnRvW1ckO3PvQs80VcUF6KM-0yK02JUxQdlmZTMmZMfFBuF_LilPm8eNe5UiLOqLn2gteyghtQ86BQzS1--aD-iuyNtOuMITKwqwNgBdTdZ0ym5JMY4NMJuDxxOt7HmeN-AllHnkV8xN2qv2NBpywODAEaXbi6UF8Nn23FN5OH3ju2U-xJfgWY4qj-oE-RbZmhFPOajHuo2iBE55yTISk54MsKJOnaVdo8MRq5sWo09SOWgoVPfPB3dggQkrgC1IN12ngalmFEhdi3KbLlkXAJTeZ-w5AiqGRIDnEV6kj3k3WeGjwBDj-g4x8QZ3cAR_OFt12MMjkEUxWlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1818a75a.mp4?token=oTv-IUhYnRvW1ckO3PvQs80VcUF6KM-0yK02JUxQdlmZTMmZMfFBuF_LilPm8eNe5UiLOqLn2gteyghtQ86BQzS1--aD-iuyNtOuMITKwqwNgBdTdZ0ym5JMY4NMJuDxxOt7HmeN-AllHnkV8xN2qv2NBpywODAEaXbi6UF8Nn23FN5OH3ju2U-xJfgWY4qj-oE-RbZmhFPOajHuo2iBE55yTISk54MsKJOnaVdo8MRq5sWo09SOWgoVPfPB3dggQkrgC1IN12ngalmFEhdi3KbLlkXAJTeZ-w5AiqGRIDnEV6kj3k3WeGjwBDj-g4x8QZ3cAR_OFt12MMjkEUxWlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای امروز بین‌الحرمین  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/444473" target="_blank">📅 14:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b546118abc.mp4?token=R7j1w6A44zLLa7Ue-4IOSZMyTQy8uwRGxDbclpH-CPSP7dUD4GvQ18x_0-YcU4bETj7jCAbU7RlReA_za9SQLr1J8KPMqEbbkNx2H31ansT0TCqD3HNle1LT1EJX3GlSeV4QzbgwBH-FPNLTF1z9a52UUPa-LdPZLi00xmsm8Qxvh983V3PVJKC-3DTm3g4NdF-qecnL7j4pY4I2PbK7lPEoMmam2Ho_ekOv_6pLwfW_hQ-UNdvxvnB_01jUoatt-D_7OI6Z48SeCnVZfVuqxrw_7JusS4aeRVwu8xWs3X8WLtzAts5Kt30K7oFFS1hplGORGyPTppPHFO9gVWJxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b546118abc.mp4?token=R7j1w6A44zLLa7Ue-4IOSZMyTQy8uwRGxDbclpH-CPSP7dUD4GvQ18x_0-YcU4bETj7jCAbU7RlReA_za9SQLr1J8KPMqEbbkNx2H31ansT0TCqD3HNle1LT1EJX3GlSeV4QzbgwBH-FPNLTF1z9a52UUPa-LdPZLi00xmsm8Qxvh983V3PVJKC-3DTm3g4NdF-qecnL7j4pY4I2PbK7lPEoMmam2Ho_ekOv_6pLwfW_hQ-UNdvxvnB_01jUoatt-D_7OI6Z48SeCnVZfVuqxrw_7JusS4aeRVwu8xWs3X8WLtzAts5Kt30K7oFFS1hplGORGyPTppPHFO9gVWJxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار مستقر در لبنان: دولت‌هایی مثل عربستان درحال افزایش فشار بر لبنان جهت محدودکردن حزب‌الله هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/444472" target="_blank">📅 14:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444471">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a01c17eb.mp4?token=SjhTLvAGoXcutFna1oO8tkdrzQSk8avdP2Xk2oRmLTDtVdyJ6ry65sw-ETGf3ZvPGUphu7sXxR1Eb7fGkBEhS-3FxCTh059wjAsrYcWZyzhOi77xubdjwHay0uj2BAD9TjRKKKwDaNEBvIFmbQGk2Wjj_zo0Yzys4kKxyHlBmQiLNs7vJ8eiMja0ueMTDx5U3z92drDfgZDlzZJiQSc9_o50ZjYvcuCedHmdHjNILSk3VylXPvYmX4U6Nn1Q3KlKNiMAg7uSK3rDhXXNaUetJbjLpPkJJ9HNwN26VFQCmliCPNQ-ttdfmlcQS571ZnoZ5ZlQdmg5ueTB2ZRAQKvMCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a01c17eb.mp4?token=SjhTLvAGoXcutFna1oO8tkdrzQSk8avdP2Xk2oRmLTDtVdyJ6ry65sw-ETGf3ZvPGUphu7sXxR1Eb7fGkBEhS-3FxCTh059wjAsrYcWZyzhOi77xubdjwHay0uj2BAD9TjRKKKwDaNEBvIFmbQGk2Wjj_zo0Yzys4kKxyHlBmQiLNs7vJ8eiMja0ueMTDx5U3z92drDfgZDlzZJiQSc9_o50ZjYvcuCedHmdHjNILSk3VylXPvYmX4U6Nn1Q3KlKNiMAg7uSK3rDhXXNaUetJbjLpPkJJ9HNwN26VFQCmliCPNQ-ttdfmlcQS571ZnoZ5ZlQdmg5ueTB2ZRAQKvMCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار مستقر در لبنان: در تاریخ ایران متحدی نداشته است که در یک جنگ بیشتر از خودمان شهید داده باشد
🔹
ما اگر نتوانیم شرط عقب‌نشینی و پایان جنگ را در لبنان محقق کنیم، شرایط جبهه مقاومت در آینده به تجربه‌ای تلخ تبدیل خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/444471" target="_blank">📅 14:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444470">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
معاون بین‌الملل وزارت خارجه: هیچ برنامه‌ای برای دسترسی آژانس به تاسیسات موردحمله‌واقع‌شده و مواد هسته‌ای وجود ندارد
🔹
این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمهٔ تمامی تحریم‌ها و... بررسی و تعیین‌تکلیف خواهند شد. @Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/444470" target="_blank">📅 13:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444469">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ادعای گروسی: آژانس از سایت‌های ایران بازرسی خواهد کرد
🔹
مدیرکل آژانس بین‌المللی انرژی اتمی: یک یادداشت تفاهم بین رئیس‌جمهور آمریکا و ایران  وجود داشته که توسط هر دو امضا شده.
🔹
این تفاهم‌نامه «به صراحت می‌گوید که فعالیت‌های هسته‌ای که قرار است در رابطه با…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/444469" target="_blank">📅 13:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444468">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f4582f6.mp4?token=TLZHv0ihdJQf5wfQGfMclJ43DRZEoTQyGh64tZgPYxEmDbIaXomjXhhV6s_pNjHTdG_Mq8osFXy8Uth_AS5JNQS5fy1OYtg9WLU3R1BTfKCTIk-4QYtmUdcFR6oVllcGFFzBtpJdVjkRPtOa4460Ov2SFNg2VaqhtmOzX1rQXKH-x24emTftGDh12tIH8CAKGTpCP5Y2fKeCHcLOMePrgeeRRtj2cYYNrFz-9vZ6WYeQrOu9k-Hp42LkbVp659jIXrTXdeweXKJ5-FmVRnFH2LWOrivWXx6yFq2GZCuu0EPrspMheRJhDWvr_V4xO_dugVCMcT9NFDqwW6wAypatfGJ1NpjI-3i64js0U8NKt0LMV40PxntaNRuTNi2WHMtWhIphjr5qtcCsop2G2Vp8C079YVM4oFuxx3-Ihez7KDDro4TcV78p7_s5qcQzBwqUkIcS5NxZnTZID6UtMfhGAXN0gl0U4-KQhsgRlEuuGsS12POt2anzZlt8v3cnfBZqCsgG0H3kJIruwm_m1Mv9GMxFyyQ3dNJkWZ02-IeM2dMGZY1qSrqAvZqX5xx1fPZOZKIj-n0FfxUpBX6KurY1tZlQSj97hV9WaCnaMQPk0gdOXtPjtIyxnuutW5ZPk7VthE3ZunnBQsljth9mvZcvAbuPnUzbgBYM8b7UIDdLERo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f4582f6.mp4?token=TLZHv0ihdJQf5wfQGfMclJ43DRZEoTQyGh64tZgPYxEmDbIaXomjXhhV6s_pNjHTdG_Mq8osFXy8Uth_AS5JNQS5fy1OYtg9WLU3R1BTfKCTIk-4QYtmUdcFR6oVllcGFFzBtpJdVjkRPtOa4460Ov2SFNg2VaqhtmOzX1rQXKH-x24emTftGDh12tIH8CAKGTpCP5Y2fKeCHcLOMePrgeeRRtj2cYYNrFz-9vZ6WYeQrOu9k-Hp42LkbVp659jIXrTXdeweXKJ5-FmVRnFH2LWOrivWXx6yFq2GZCuu0EPrspMheRJhDWvr_V4xO_dugVCMcT9NFDqwW6wAypatfGJ1NpjI-3i64js0U8NKt0LMV40PxntaNRuTNi2WHMtWhIphjr5qtcCsop2G2Vp8C079YVM4oFuxx3-Ihez7KDDro4TcV78p7_s5qcQzBwqUkIcS5NxZnTZID6UtMfhGAXN0gl0U4-KQhsgRlEuuGsS12POt2anzZlt8v3cnfBZqCsgG0H3kJIruwm_m1Mv9GMxFyyQ3dNJkWZ02-IeM2dMGZY1qSrqAvZqX5xx1fPZOZKIj-n0FfxUpBX6KurY1tZlQSj97hV9WaCnaMQPk0gdOXtPjtIyxnuutW5ZPk7VthE3ZunnBQsljth9mvZcvAbuPnUzbgBYM8b7UIDdLERo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار مستقر در لبنان:  عملیات دشمن صهیونیستی در جنوب لبنان کاهش جدی داشته اما صهیونیست‌ها پایبندی کامل به آتش‌بس ندارند و هروقت بخواهند حمله می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/444468" target="_blank">📅 13:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444467">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e3f389b7.mp4?token=DtB09IKcTONawAS56XcDUliTzRdTaEcxZe_OPnWw23QLa0u4pSQe_b6PUgm9sP5UP0V6G8pSeHKUV23ag4uU15hLOUBDbIDppSZOeemrqLRjqaMLcSL1tYCdzDCuMUX-PBfTQuqxowKP6EgJxj47R8VhukJmkMXeX__rOLFO3wQ15AWhRLLAxNeWfzcRIjiM-xo1Z7ucfdqVRR5BAu34cmaXiOBjUQoZjls8ETUUYaPSBGhnNkMUYZM7XwHDxrarm7iuIE83jwBXvUhXPxVSCZo9rVf347MI1uQ269sAh-HYz-v3FLKkgltQyrcZsJpb1cXH3As3GGhg3qTNYwDrlrr1kUgX5-ojClNdvf0TAkqQntqSatmz5dy8PK9OyfAEBDfEM-81Xo-sdyNT-O3yUwDgWHys2FXB1lFd5DiRbIrOgUeln6yRCfHqMz-3gXPhP54YRPchDpqpuVbXlgyAYKrjhXwp_7-p1qt2VmdjldjRZnpvURKu2TD9u8CCnLOtV7dJTlkz5SZdt5-sYy4_bHoUaEsiQDB_Jh_XTs0UDckVp3n1xsXQo5rNyO7UVgLXiYNn8EE_RUtenmwvSefmwVDupqq7XyqWGWYtUySxUsZJX4YRKE84N2G65cJyXeqo8bykagUY4DLva0V6BTr8VRYfxMxHCDaMZo0qAtdy9Qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e3f389b7.mp4?token=DtB09IKcTONawAS56XcDUliTzRdTaEcxZe_OPnWw23QLa0u4pSQe_b6PUgm9sP5UP0V6G8pSeHKUV23ag4uU15hLOUBDbIDppSZOeemrqLRjqaMLcSL1tYCdzDCuMUX-PBfTQuqxowKP6EgJxj47R8VhukJmkMXeX__rOLFO3wQ15AWhRLLAxNeWfzcRIjiM-xo1Z7ucfdqVRR5BAu34cmaXiOBjUQoZjls8ETUUYaPSBGhnNkMUYZM7XwHDxrarm7iuIE83jwBXvUhXPxVSCZo9rVf347MI1uQ269sAh-HYz-v3FLKkgltQyrcZsJpb1cXH3As3GGhg3qTNYwDrlrr1kUgX5-ojClNdvf0TAkqQntqSatmz5dy8PK9OyfAEBDfEM-81Xo-sdyNT-O3yUwDgWHys2FXB1lFd5DiRbIrOgUeln6yRCfHqMz-3gXPhP54YRPchDpqpuVbXlgyAYKrjhXwp_7-p1qt2VmdjldjRZnpvURKu2TD9u8CCnLOtV7dJTlkz5SZdt5-sYy4_bHoUaEsiQDB_Jh_XTs0UDckVp3n1xsXQo5rNyO7UVgLXiYNn8EE_RUtenmwvSefmwVDupqq7XyqWGWYtUySxUsZJX4YRKE84N2G65cJyXeqo8bykagUY4DLva0V6BTr8VRYfxMxHCDaMZo0qAtdy9Qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار مستقر در لبنان: در نقض آتش‌بس دیروز رژیم صهیونسیتی در لبنان، ۳ شهید داشته‌ایم
🔹
دشمن درحال برنامه‌ریزی بلندمت جهت اشغال منطقه طیبه است.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/444467" target="_blank">📅 13:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444466">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mUfq8r0ufpbq4gB_XVQkGbqZcU6Tgs1uaP-XJ6FLXU8dYjoJGZS35TChHU0du4-kEDxnCRqvym7Gga_oXv0CK3XmQQTB2KM6eUO3vpNVOTmNI1AEIkTecBepHIdTWTAbdmC2W-pMGckiTTkxQFXbf3JoypkUdP8ug3D0bx6GympFD7kMiwf5SR7513CugIUwadNokT4de9LtzqbO0HSqKC5_7AN7d6wZRAzAihEZr0I0cd-l9Du046Fjs0yEQLOc_3M-q8nUZKFGEJ0xrNYjmlSiz7_5zW93GIP1vjLewjCrzu1JSAEdwNZMS-hMUJASZWu50JP2xfaz2gWEs-fE_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mUfq8r0ufpbq4gB_XVQkGbqZcU6Tgs1uaP-XJ6FLXU8dYjoJGZS35TChHU0du4-kEDxnCRqvym7Gga_oXv0CK3XmQQTB2KM6eUO3vpNVOTmNI1AEIkTecBepHIdTWTAbdmC2W-pMGckiTTkxQFXbf3JoypkUdP8ug3D0bx6GympFD7kMiwf5SR7513CugIUwadNokT4de9LtzqbO0HSqKC5_7AN7d6wZRAzAihEZr0I0cd-l9Du046Fjs0yEQLOc_3M-q8nUZKFGEJ0xrNYjmlSiz7_5zW93GIP1vjLewjCrzu1JSAEdwNZMS-hMUJASZWu50JP2xfaz2gWEs-fE_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاع خلیل‌زاده: ایرانی‌ها در خارج از کشور خیلی به ما لطف داشتند و جوری ما را تشویق کردند که شاید بشود گفت جو استادیوم لس‌آنجلس از ورزشگاه آزادی هم بهتر بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/444466" target="_blank">📅 13:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444465">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خراسان رضوی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14e03072d.mp4?token=ChSlD20C_3NzEv4GhdEzgziFoMg02Kj343CmR1wt2X6-CrE-0SKsBc05W8FZAzrB-9gBiIgqkR7V9rG9vZwrbkE2FhOM9b3ERoIp1i2MaPoK1Pc8D5ZKCuJCu5_TrOdA5frEXzKCnuYXNwVSl8xUN70u78Y0wN_Vz5RVkNkn_WwNm2Ah7DoVYoSE5JvsXx5zoDxYkOTJP2ehZFf9c2XkbKxj3vcH7myTNghJ_LTlUg8GHDylciMR1PrXslu7YLYbU3DvzMbhLLmxNVLBO7_-4SrZD2YQ8g8iZ0k3lGDgDVnOLEbCCKLJjPGQ96Z7yzdtIDWSxWQVLw8k16hITep5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14e03072d.mp4?token=ChSlD20C_3NzEv4GhdEzgziFoMg02Kj343CmR1wt2X6-CrE-0SKsBc05W8FZAzrB-9gBiIgqkR7V9rG9vZwrbkE2FhOM9b3ERoIp1i2MaPoK1Pc8D5ZKCuJCu5_TrOdA5frEXzKCnuYXNwVSl8xUN70u78Y0wN_Vz5RVkNkn_WwNm2Ah7DoVYoSE5JvsXx5zoDxYkOTJP2ehZFf9c2XkbKxj3vcH7myTNghJ_LTlUg8GHDylciMR1PrXslu7YLYbU3DvzMbhLLmxNVLBO7_-4SrZD2YQ8g8iZ0k3lGDgDVnOLEbCCKLJjPGQ96Z7yzdtIDWSxWQVLw8k16hITep5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهدالرضا در سوگ علمدار کربلا
@FarsRazavi
‌-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/444465" target="_blank">📅 13:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f69b645e1.mp4?token=l59DrgZ2vN64_A51eGKA4wjJ-1QayzZa1jVrWblDXVkeJNhmNkiZ8iJStp7pClkFpT4s3wfjXdeVPwtASIyozJo6h8chGfTBsODN1Gg760p1_vE8GW5CX-j3bJVerPycha5xx0KojKc-lOOPBDOnVH03eqwqoYiMoC_j-5HY25a50ANvi4Ih-j5GYfHUrr7rNzaGwFqdPPTbFWpSS7FGUDS9wvOsrhQWYt6yg4djVJ4HmUuvUi1IzxgoRz0CAUPIkBP4QAyvfpFJbPwLwLko37PZi3IO3IibOpYPvfoUSBkeDbcf7T9Yvcb3D3hK4HT0GqvVXVPvbZ-yy1O3W24Mzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f69b645e1.mp4?token=l59DrgZ2vN64_A51eGKA4wjJ-1QayzZa1jVrWblDXVkeJNhmNkiZ8iJStp7pClkFpT4s3wfjXdeVPwtASIyozJo6h8chGfTBsODN1Gg760p1_vE8GW5CX-j3bJVerPycha5xx0KojKc-lOOPBDOnVH03eqwqoYiMoC_j-5HY25a50ANvi4Ih-j5GYfHUrr7rNzaGwFqdPPTbFWpSS7FGUDS9wvOsrhQWYt6yg4djVJ4HmUuvUi1IzxgoRz0CAUPIkBP4QAyvfpFJbPwLwLko37PZi3IO3IibOpYPvfoUSBkeDbcf7T9Yvcb3D3hK4HT0GqvVXVPvbZ-yy1O3W24Mzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاچاق برق برای استخراج رمزارز
❌
روایتی تکان‌دهنده از واقعیتی که کمتر دیده شده؛
تاراج سرمایه‌ای که متعلق به مردم است
⁉️
چگونه «پول کثیف» از دل برق یارانه‌ای مردم تولید می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/444464" target="_blank">📅 13:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444463">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨ ⁨
⚽️
در کآپ‌شهر فقط تماشاگر نباش؛ بازی کن و برنده شو!
🎉
💰
بیش از ۵۵ میلیارد تومان جایزه نقدی
🏠
کمک‌هزینه خرید آپارتمان برای ۸ نفر
🚗
کمک‌هزینه خرید خودرو برای ۱۱ نفر
🎁
۲۰۲۶ جایزه ۱۰ میلیون تومانی
کافیه اپلیکیشن آپ رو به‌روزرسانی کنی و با کارت بانک شهر یا آپ‌کارت، شانس خودت رو برای بردن چند برابر کنی!
✨</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/444463" target="_blank">📅 13:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/444462" target="_blank">📅 13:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444460">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌ محدودیت‌های پروازی در ایام تشییع رهبر شهید انقلاب
🔹
فرودگاه مهرآباد تهران: ۱۲ و ۱۵ تیرماه توقف کامل پروازها، ۱۳. ۱۴. ۱۶ و ۱۷ تیر فعالیت با ظرفیت محدود در پذیرش مسافران.
🔹
فرودگاه مشهد: ۱۷ تیرماه اعمال محدودیت‌های عملیاتی در پذیرش مسافر و ۱۸ تیر توقف کامل…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/444460" target="_blank">📅 12:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444459">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
اعلام تعطیلی چند استان در روزهای برگزاری مراسم وداع و تشییع رهبر شهید انقلاب
🔹
براساس اعلام معاون اول رئیس‌جمهور، استان تهران در روزهای ۱۳ و ۱۴ تیر و کل کشور در روز ۱۵ تیر تعطیل خواهد بود.
🔹
همچنین استان قم در ۱۶ تیر و استان خراسان رضوی در ۱۸ تیر تعطیل اعلام…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/444459" target="_blank">📅 12:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444458">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4fGYhBW7cUahUKCIGEVQdMDnIuKcEhkrc8fpUzTJwr4G6yIl7OtbUbP14WZwOcsLZ2ZsNZjf4niV3OUi0LNCCkiE3GCDQTn3WVZXJfhTVllbNXLwMJv2beI3WH4WdYkJHfk54-Rqn3bDqN3oggvHcBCMN72EsdnLQ-O73kOBE17HT8uaEuchq7GoVbnwcCM1L-9l4qUIV42adPxUeK4xjWMRPrSly8LC-le1x0B8wyC1zk00iBBosNbM6DV0wI83qRTBqyjaEaoNISTDexUl_BX3iWx47Gw-0an2ul13g5v8tgAvltZPluRpP7k-s9P4vU7RBh5PjmJRSLHTZzAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌
🔸
غریب‌آبادی، رئیس هیئت مذاکرات فنی ایران: مجوز‌ عام برای فروش نفت، محصولات پتروشیمی، فرآورده‌های نفتی و خدمات مربوطه از سوی طرف آمریکایی صادر و در سایت اوفک نیز منتشر شد.   @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444458" target="_blank">📅 12:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2j9-bqejTWK_dipkdFXSBwdjT1naiogsrAoRS--BHWn366Ccw7gs-sUflX4VwoKc7HeLdTEf2FFhj10Wvt1vVdMxRoLwE_PNqr3ZMFoPKqyM4ThrvAzQOaxfQFL5hdBlyzXV2DlwtsO1-bX-A7rzuTXv4aJEQLl4lOt1-i5-qwMhXP2GSynhR1_unyRj2yDGLwE4S83buI_7r3vRVEiRnfVjmibRSnidJnRgtUbWm5IMy89HCtG7QzxtUW15doSmz5SnAsJqy0yXvuTWJM0Di-wO1pmdteyxoB7gbZV8NhsSrmocGTvyZ_RNqSTBZ7DMkHyffqtDtSutmJqPbO1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خبرنگار: بازرس‌های آژانس دقیقاً چه زمانی در ایران مستقر می‌شوند؟
🔸
ترامپ: در زمان مناسب. هیچ عجله‌ای نیست.
🔹
این ادعا درحالی است که به‌تازگی یک منبع نزدیک به تیم مذاکره‌کننده ادعای بازگشت بازرسان آژانس را تکذیب کرده است. @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/444457" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444456">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjShiNES35OqdhyQP7ro0FLAU5UUP9pJPSLFzD_IXDHY-Dl-z1MwahhpLNcp7yaPY3pwcQ6sivLATEmax73CC-yKcr7SWJM3rOr2UJH_TRXsZRJ4LZuadDjd8YOqyme4tjHhlc5rB7LJPYyF9Uk1CZLOE5FKnMLcOehbhdyDVsZFj80xdHw0rrVa2h-TpcyjDd_pvdqo00b5k_Wt2CSjYj-MRTQh6u8N4_olE25oRI8hy2rY_7Z9qfc-iIBSGSML5myKAHMqezxkWfNpcC_CIheaqoBUtu1Oihe5SbtXl1XvF6ti4i-_nwUHP4T8m_9kqmpajNAam9QrjzsfJVUrKPcHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjShiNES35OqdhyQP7ro0FLAU5UUP9pJPSLFzD_IXDHY-Dl-z1MwahhpLNcp7yaPY3pwcQ6sivLATEmax73CC-yKcr7SWJM3rOr2UJH_TRXsZRJ4LZuadDjd8YOqyme4tjHhlc5rB7LJPYyF9Uk1CZLOE5FKnMLcOehbhdyDVsZFj80xdHw0rrVa2h-TpcyjDd_pvdqo00b5k_Wt2CSjYj-MRTQh6u8N4_olE25oRI8hy2rY_7Z9qfc-iIBSGSML5myKAHMqezxkWfNpcC_CIheaqoBUtu1Oihe5SbtXl1XvF6ti4i-_nwUHP4T8m_9kqmpajNAam9QrjzsfJVUrKPcHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاع خلیل‌زاده: علیرضا بیرانوند وسیله بود و دست خدا بود که اجازه نداد شوت بازیکن بلژیک گل شود
🔹
در حق بیرانوند خیلی نامهربانی کردند و حالا کل دنیا در خصوص بیرانوند صحبت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/444456" target="_blank">📅 12:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444455">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار قم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1512b4c0f1.mp4?token=m4q-AU68v71xVet1ppaGzvxgFKsMimTy1ghUS_djcZec89UaINWHLiYmpH69a20P9-qc1ezn0817lGFKGAT7cvvqQL4xfk4_avJscOh7ue4ZV2iuTYG3tKf6cXI5qhoqofbxUpZr-Fqmq7a1j9G-pASMk34vAXn9OpMPi0nmVJecmeqDBeTohS0JXmDLXPOaVUDNMACeZh9EGZm0LoAbjyarpS8eg3SByV-hVzHyn0w10NHJTfpS64DmU0KVDBj7W-CX2FY7iyOnjZCyXw1UdUeWmb5DUUS4f_eKxK6aHQpl8NdmKF-FBSlANL_qXbvD7o4CdJ5_1sggXWqF6u5Ulxu_hlpRUQB26DGEOxBlRHBQ9FR-DZFSOVOtlumIBL9BpITJN0RgKDueBBgmKcGYd4Kx90qbZDnRQpW2U9H8Q2sqrZjr6WBMllRWbRJWBa83-AW5uJxHTTkMex0jdo_TU4m7ZN-CfsmNLZ1yVIECRcyPAd0duRM1PGd5dekFQVnQ4HzQuswZm0DVmk-R1-1aPvm0wfDN88rKgDOydI2PEkxG0xSmAskQSWH3OUyaK_lHG8j5iV1YstC3xUcEyhpwfyws49CJrLkrvI_nTxy9dDCzVPXbL8IZRH60BedXhnZhcZ11B4l8zIHDyuyywl_ABeQCY_-fm5H1WrogbtBUxLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1512b4c0f1.mp4?token=m4q-AU68v71xVet1ppaGzvxgFKsMimTy1ghUS_djcZec89UaINWHLiYmpH69a20P9-qc1ezn0817lGFKGAT7cvvqQL4xfk4_avJscOh7ue4ZV2iuTYG3tKf6cXI5qhoqofbxUpZr-Fqmq7a1j9G-pASMk34vAXn9OpMPi0nmVJecmeqDBeTohS0JXmDLXPOaVUDNMACeZh9EGZm0LoAbjyarpS8eg3SByV-hVzHyn0w10NHJTfpS64DmU0KVDBj7W-CX2FY7iyOnjZCyXw1UdUeWmb5DUUS4f_eKxK6aHQpl8NdmKF-FBSlANL_qXbvD7o4CdJ5_1sggXWqF6u5Ulxu_hlpRUQB26DGEOxBlRHBQ9FR-DZFSOVOtlumIBL9BpITJN0RgKDueBBgmKcGYd4Kx90qbZDnRQpW2U9H8Q2sqrZjr6WBMllRWbRJWBa83-AW5uJxHTTkMex0jdo_TU4m7ZN-CfsmNLZ1yVIECRcyPAd0duRM1PGd5dekFQVnQ4HzQuswZm0DVmk-R1-1aPvm0wfDN88rKgDOydI2PEkxG0xSmAskQSWH3OUyaK_lHG8j5iV1YstC3xUcEyhpwfyws49CJrLkrvI_nTxy9dDCzVPXbL8IZRH60BedXhnZhcZ11B4l8zIHDyuyywl_ABeQCY_-fm5H1WrogbtBUxLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم حضرت معصومه(س) در تاسوعای حسینی
@FarsQom
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/444455" target="_blank">📅 12:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3JoNdJEVtXSvSeE3A8YCBJks6s4n7YQT1d7Nv4AdUD-J6y_H4UtOv_3SmZ2QL95v_T7d-J0lFI46tq0d9LjITxRS9XgS_KLfnZ7TRqBhJl7BUy2B89ae3GCr_wiLSYJyHY4PpK74D5Vw5xRRZu3n6K9ULjVkUE6I-stAAbSg_aKiFQeo36D6jBh-TQ_HGMs4D4S9cHp9ae-jssbtX9ONJYiY7vyb3K0QgSBkLCRvYXoQ0ZiNWXTTP6xsrGSKe_NtfDl6oIpPhkFxZtjZzxXtnHxBRw-LiTJkCCFnRiz0xEZAgJprdVbQimQ47XhEdQksKYbx8Ivsto04Mb9HC-Pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آخرین تمرین تیم ملی در تیخوانا پیش از سفر به سیاتل
🔹
در حاشیه آخرین تمرین تیم ملی پیش از بازی مقابل مصر، یکی از مدیران باشگاه تیخوانا تابلویی نقاشی با نمادهایی از ایران و مکزیک را به فدراسیون فوتبال اهدا کرد.
🔹
در مقابل نیز پیراهن تیم ملی ایران به نشانه…</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/444454" target="_blank">📅 12:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccb5f05bb4.mp4?token=gqoCiVxB5apMDPBbfb3xeSa1ib67OqHWkdIKEZkGS-G2WyVSdp-2b5AcTLVfq7iJa1b0kC1-4SFH_u8seSE4q5U7kcUPtIBbKuZNwIb6kapy4eigxsCLAj0jMLk-fSY2OWs4Q_79eB_8v7Gw2lUGZvzkF3sXZdn-11Nrj6ks2lkc0Uf074SQq28SxpkgXkS6UQSjwgOEZWoOCAOOR1ynTz4_EaDmnYv0Eir3-KxvuAwdyh-TuKSy7ypCZVjCDd-_Piu384STPOUBXpOFx90hmLvJDqmMJPmFkgRSuc4DpaN6afAQ6K6fzaPfItA614T7h2wQ2VQDTigqGqpLt27GKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccb5f05bb4.mp4?token=gqoCiVxB5apMDPBbfb3xeSa1ib67OqHWkdIKEZkGS-G2WyVSdp-2b5AcTLVfq7iJa1b0kC1-4SFH_u8seSE4q5U7kcUPtIBbKuZNwIb6kapy4eigxsCLAj0jMLk-fSY2OWs4Q_79eB_8v7Gw2lUGZvzkF3sXZdn-11Nrj6ks2lkc0Uf074SQq28SxpkgXkS6UQSjwgOEZWoOCAOOR1ynTz4_EaDmnYv0Eir3-KxvuAwdyh-TuKSy7ypCZVjCDd-_Piu384STPOUBXpOFx90hmLvJDqmMJPmFkgRSuc4DpaN6afAQ6K6fzaPfItA614T7h2wQ2VQDTigqGqpLt27GKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای امروز بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/444453" target="_blank">📅 12:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ادعاهای جدید ترامپ در مورد مذاکرات
🔹
ترامپ ادعا کرد که علی‌رغم تکذیبیه‌ها و بیانیه‌های رسمی، ایران به‌طور کامل با بالاترین سطح از بازرسی‌های هسته‌ای برای آینده‌ای نامحدود موافقت کرده است.
🔹
او مدعی شد که این تعهد، ضامن «صداقت هسته‌ای» ایران خواهد بود و درصورت…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/444452" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894b023e8.mp4?token=fzDKLjANVo7QHGxXpF37pBruSr6x5UX7dkfF894Nq9MQD8rgiLjkv5xwmpQgeunRXumEpAumzqpwkzodZLkE2MOio7i4rPRe3hRu2tdgFyx2zznq4LjNp7s9O5iJc4WMVdkBTr15TfOEt8o5gPCb4HPvnwk1dsOx-DmWfWR8WijerIh8oj6Kb6qzwg859Re6mGvC-m8wKOetaT4LowMwOgoJrmNaB_lw_m6f7Ux_t6vUlIcBmoLFdFqhUZ0wMU8-zCk4AYxtbAJINmUBCXzinRVgI9nIPRYvGMUNX40dP7TNFiozCDF3J2w9R3K8ojMPE-52C3h-O3rl1RGTZhg0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894b023e8.mp4?token=fzDKLjANVo7QHGxXpF37pBruSr6x5UX7dkfF894Nq9MQD8rgiLjkv5xwmpQgeunRXumEpAumzqpwkzodZLkE2MOio7i4rPRe3hRu2tdgFyx2zznq4LjNp7s9O5iJc4WMVdkBTr15TfOEt8o5gPCb4HPvnwk1dsOx-DmWfWR8WijerIh8oj6Kb6qzwg859Re6mGvC-m8wKOetaT4LowMwOgoJrmNaB_lw_m6f7Ux_t6vUlIcBmoLFdFqhUZ0wMU8-zCk4AYxtbAJINmUBCXzinRVgI9nIPRYvGMUNX40dP7TNFiozCDF3J2w9R3K8ojMPE-52C3h-O3rl1RGTZhg0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: فلسطین صرفا یک موضوع سیاسی یا یک پروندۀ دیپلماتیک نیست
🔹
ملت فلسطین همانند همۀ ملت‌های جهان حق تعیین سرنوشت از طریق همه‌پرسی دارند.  @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/444451" target="_blank">📅 11:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2bc4f1c3.mp4?token=ZxlFXJkEnlPZK55x6XvI-bCYheIKgUxGO-2R7iuxw2Fi0oxVUFoxBPji6nmLNmukOWImnx6f7Z6ixp8FFWdB5yAmneqTUg0J_sASFNuCk5fRHTApq5zflwydp5D-iSWbglm1Fxgq-0WNum26sft6C57yfER836ac1qaBkYWGgnNycITxTFk-Hu_cX1YEldruP_JSHTG1Kj-95ES__mu27M2ZTFHsgMykT6NLe4WjvmZhfedeamzG4c8h5-OZcnHPi55cn_gcEwzP0vZCRBKjcJaBuT6dJywhKPDnDTcSbgD5Y5tyLYtcBc8US9hi-8ajnM_ihusJ7R7d_RCQP4u6lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2bc4f1c3.mp4?token=ZxlFXJkEnlPZK55x6XvI-bCYheIKgUxGO-2R7iuxw2Fi0oxVUFoxBPji6nmLNmukOWImnx6f7Z6ixp8FFWdB5yAmneqTUg0J_sASFNuCk5fRHTApq5zflwydp5D-iSWbglm1Fxgq-0WNum26sft6C57yfER836ac1qaBkYWGgnNycITxTFk-Hu_cX1YEldruP_JSHTG1Kj-95ES__mu27M2ZTFHsgMykT6NLe4WjvmZhfedeamzG4c8h5-OZcnHPi55cn_gcEwzP0vZCRBKjcJaBuT6dJywhKPDnDTcSbgD5Y5tyLYtcBc8US9hi-8ajnM_ihusJ7R7d_RCQP4u6lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: توقف آتش‌بس و پایان دادن به جنگ در لبنان برای ما به همان اندازه مهم است که توقف آتش‌بس و پایان دادن به جنگ بر ایران اهمیت دارد.  @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/444450" target="_blank">📅 11:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444ebf05e2.mp4?token=HuYzQkoweAB9UVAh2rnvfG0KcnjqQL38L0ebiTYaoBHqndApuXNPVlUkc_O_E5U0ztXucB8iax37vCQJlEEkM3WfaqgmzZDxG0PjrFdxW_emEDS-Pol50fdsY6Ph2HYbwhuGA1JN-Da9EbP3RpM7lSa7RLTN32mJV3vowKs7TqkUN-JLE3b86b_nLzAP1MMvnPcaKtURSALwAP-CSjdfGzfjMNKa9UaFjTcVAh8ZMtVyujIzwT0nPGKnM0hgR1TL2PYeL5gbedp0SK2QAC2k2sOABMdWPj8k-gAjGXJzdoDx0zX5b_okpNAB43mpnYo00jVWBIbB_ISVlq6M1cRiGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444ebf05e2.mp4?token=HuYzQkoweAB9UVAh2rnvfG0KcnjqQL38L0ebiTYaoBHqndApuXNPVlUkc_O_E5U0ztXucB8iax37vCQJlEEkM3WfaqgmzZDxG0PjrFdxW_emEDS-Pol50fdsY6Ph2HYbwhuGA1JN-Da9EbP3RpM7lSa7RLTN32mJV3vowKs7TqkUN-JLE3b86b_nLzAP1MMvnPcaKtURSALwAP-CSjdfGzfjMNKa9UaFjTcVAh8ZMtVyujIzwT0nPGKnM0hgR1TL2PYeL5gbedp0SK2QAC2k2sOABMdWPj8k-gAjGXJzdoDx0zX5b_okpNAB43mpnYo00jVWBIbB_ISVlq6M1cRiGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: امنیت منطقه باید توسط خود کشورهای منطقه تامین شود
🔹
آمادۀ همکاری با کشورهای منطقه براساس عدم دخالت در امور داخلی و احترام به حاکمیت هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/444449" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
قالیباف: جنگ تحمیلی ۴۰ روزۀ آمریکا و رژیم صهیونیستی علیه ایران اقدامی جنایتکارانه بود
🔹
در این جنایت آشکار رهبر معظم انقلاب و تعدادی از مقامات عالی‌رتبۀ نظامی و سیاسی و بیش از ۳۰۰۰ شهروند ایرانی که اکثر آنان زنان و کودکان بودند به شهادت رسیدند.
🔹
مقاومت…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/444448" target="_blank">📅 11:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ae4a24f1.mp4?token=tq9nO05Ng7_8He7dmV1GtWUNyPz5GTxg9_LkLQvTFXSiQDyvZ42fHYFRfO41Pb49dPUG13Ji1qHouLXkDxIfRTNko9XOa57oM6IFiYch_0lXfi9OUo9Gr3M7YT1tj8i_3_U-Bm3WTd0pMPsDJaLbRLSMLm8yqnZEbroCKZjLrEuwKcVuVycR3RMvU2GTkTjProjB-EvyAVx5BiWBOOz2dtc6nkqAvC5gBr4UZAXZZqw0hMiCVOAbrVXUw_B33yaaAMhEsEvMHODF5zcfyOcNXXezWm1nfpsmBwmxYYPwJAQ8aOOutxuJmT6fjGeCLGEAlQGOjWesxMXOi1OrOtHvpjQAylk-0Dgh4mneBRJ59j8aBRwXoUtQaoW8D9tB76lhrKE0ryRP9BRT3ocjicI3zAY3JL3t0j5RmM63gLQQs0EfqW42B9Q7EBLaN8vBomw38uZ05V8yrvQ3Gwcq4h0z5XumekoreRIW1tzr4CrXnRPsvV4Tf_AvPY99QRrNKn2tKGmR7vxQjU9HmFaShizD14-uezwq1Bi4ypNwmsJNImqh4nmd372PHAVdpMm3ocTzGo6t78PYobYCVW_eLOhzC0Xq-EQ_oZTRvemk9lwnkv8ai-mVK0EFMscdIVb2ysDkbSd52Rzl6c2yIDT2jsbXjH8x_jXKjWCPueJVE3ALxI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ae4a24f1.mp4?token=tq9nO05Ng7_8He7dmV1GtWUNyPz5GTxg9_LkLQvTFXSiQDyvZ42fHYFRfO41Pb49dPUG13Ji1qHouLXkDxIfRTNko9XOa57oM6IFiYch_0lXfi9OUo9Gr3M7YT1tj8i_3_U-Bm3WTd0pMPsDJaLbRLSMLm8yqnZEbroCKZjLrEuwKcVuVycR3RMvU2GTkTjProjB-EvyAVx5BiWBOOz2dtc6nkqAvC5gBr4UZAXZZqw0hMiCVOAbrVXUw_B33yaaAMhEsEvMHODF5zcfyOcNXXezWm1nfpsmBwmxYYPwJAQ8aOOutxuJmT6fjGeCLGEAlQGOjWesxMXOi1OrOtHvpjQAylk-0Dgh4mneBRJ59j8aBRwXoUtQaoW8D9tB76lhrKE0ryRP9BRT3ocjicI3zAY3JL3t0j5RmM63gLQQs0EfqW42B9Q7EBLaN8vBomw38uZ05V8yrvQ3Gwcq4h0z5XumekoreRIW1tzr4CrXnRPsvV4Tf_AvPY99QRrNKn2tKGmR7vxQjU9HmFaShizD14-uezwq1Bi4ypNwmsJNImqh4nmd372PHAVdpMm3ocTzGo6t78PYobYCVW_eLOhzC0Xq-EQ_oZTRvemk9lwnkv8ai-mVK0EFMscdIVb2ysDkbSd52Rzl6c2yIDT2jsbXjH8x_jXKjWCPueJVE3ALxI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیۀ شهید سلامی به تیم مذاکره‌کننده: اگر آمریکا تهدید کرد، مذاکره را ترک و کار را به نیروهای مسلح بسپارید
🔹
تیم مذاکره‌کننده ایران حامل یک امانت الهی هستند؛ یعنی بار عزّت، کرامت، حیثیّت و استقلال ملّت را به دوش می‌کشند. و نمایندگان واقعی این ملّت هستند در عرصه نبرد دیپلماتیک.
🔹
به آن‌ها توصیه می‌کنیم با آرامش، با وقار، با اعتماد به نفس و
با تکیه بر قدرت عظیم و بی‌پایانی که ملّت ایران و نیروهای مسلّح جمهوری اسلامی ایران
اندوخته‌اند، در مذاکرات حاضر بشوند.
🔹
و هیچ‌گونه مصالحه‌ای و یا توافقی که ذره‌ای خدشه به عزّت ملّت ایران و به باور‌های اصیل ملّت ایران می‌زند، نداشته باشند.
🔹
ملّت ایران، ملّت کارآزموده‌ای‌ست، جنگ‌دیده است. ملّت آزموده را آزمودن مجدّد خطاست.
🔹
من توصیه‌ام به تیم مذاکره‌کننده این است که
اگر آمریکایی‌ها مجدّداً با ادبیات ارعاب یا تهدید یا تحقیر در مذاکرات به دنبال برتری‌طلبی سیاسی هستند، میدان مذاکرات را ترک کنند و این قضیّه را به نیروهای مسلح بسپارند تا در فضای تهدید با آن‌ها تعیین تکلیف شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/444447" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f715f2c470.mp4?token=n8b_o7i8qfKUUP6I5OnWgUL71DRP-LumK2zA8MeYllotFsFtPxezIqK650AmXOoFwNhj2Q7VOS-aKFTTYHXpBy3k0TNzVtBGbEKfqSPKLefwJZNWouLL7LeJmMZJ42Uxk1Y9RtZUx26_vBbvB2P8TDF7g-P1gnvF2DquNdYl1VRdIytinZw5-O5iG0QC12BmMTKu_b4lhkMSX0s2N2ZSLjW1E2rmRyNngyQqlKX3Z6Q-SywV4xd5HBhP1Nf8cQo_OeAZYTzsBL0Vo687I81XdbQ3Oulooe2hUwFhq9YErqil8Fut0OoDF8vmW7UX-3rxxeCK6aHED28iB62M5-9ajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f715f2c470.mp4?token=n8b_o7i8qfKUUP6I5OnWgUL71DRP-LumK2zA8MeYllotFsFtPxezIqK650AmXOoFwNhj2Q7VOS-aKFTTYHXpBy3k0TNzVtBGbEKfqSPKLefwJZNWouLL7LeJmMZJ42Uxk1Y9RtZUx26_vBbvB2P8TDF7g-P1gnvF2DquNdYl1VRdIytinZw5-O5iG0QC12BmMTKu_b4lhkMSX0s2N2ZSLjW1E2rmRyNngyQqlKX3Z6Q-SywV4xd5HBhP1Nf8cQo_OeAZYTzsBL0Vo687I81XdbQ3Oulooe2hUwFhq9YErqil8Fut0OoDF8vmW7UX-3rxxeCK6aHED28iB62M5-9ajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: اجلاس باکو فرصتی برای تبیین تحولات پس از جنگ است
🔹
بعد از جنگ رمضان، شرایط منطقه متفاوت شده و باید با نگاه دیگری به آن نگاه کرد.   @Farsna - Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/444446" target="_blank">📅 10:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYKf5_8YeZ5RFEP1hft3DiU4XeeF4C6O9NHjT3U1_Q2uK5A23eZ1DWQEDeb4CjVFHDHmHM4yzqCU68MFCpbM3Xhszwkr4kBFAiP_J7MX3fdARoqcRQIXSJzW8UGj-jvs0h5zeRT9woubpJRkscK8SSdUDZfom2Vf74vl6arCcn0tpnLgItFoARPaNnRXCdDGE8Ng_YxfZeR1j0IAYzWms8b8n95a2230gxWUHiXTb9xLJfikNRWqppnfJul4BqQSn04LkmVbz1jPm1yOktaOO4bUE-V4ORgL8bmcsX-K-P0fVkUaonS39feppn65_3438dKXztc4rxW6rva9AKBmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مردم آمریکا در پمپ‌بنزین‌ها سرکیسه می‌شوند
🔹
شرکت‌های بزرگ نفتی قیمت بنزین در جایگاه‌ها را متناسب با کاهش شدید قیمتی که خودشان برای نفت می‌پردازند، پایین نمی‌آورند.
🔹
به وزارت دادگستری دستور داده‌ام که فوراً بررسی این موضوع را شروع کند. قیمت بنزین بهتر است خیلی سریع‌تر از چیزی که الان می‌بینم پایین بیاید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/444445" target="_blank">📅 10:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYqac9YhC8z977-_yTzFBBIq6rfjsPfhKUWilZ2NPcvdZBVodbq4EXd71tqhpSmb044MbasC_2EzSF3aBTDp-s9aW5Lsgjpf1WOgBxGAL_VI9GcuZl7_h6Z57g0y8n2gXdgwyZjBfe8sRikttv3NGIRbWHyY-spGM8qwJUo0iOt6VZYoG-DVOLvOtF9U7bAD9yyWuIPpn7NFMc3c3jEdtPKggW4tlNhbykLXeNsBoGhlIi2VU9VucZM39yg87ltETXNVgus8G3jyC1i_T5QZ-2QNP78b2gb-c6XKksGl2kElPCjNVIqEeS53ufkW9U037oHTeAQZbaA5k_UCGtcf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام سردار مجید موسوی به خانوادۀ ماکان نصیری رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444444" target="_blank">📅 10:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFoB7IiyYNycDCPcuPNsSK54sXCwQ5I53qv7Lo-uQGIjg7t_8m7guTPdYwdMY9YYh-_cvWPjXFoitJkDr4fkeEFNjzsgeuBFbKf0xx34FXhuE8wu96BEGvWsnR4PAeTrK0wtygWQuOiBQBPjZRS8R-auC2iwDNGl9kwrq3dZ_b4sNfcupc08khbR2NyJx5ZroKYb-GMUcXvIiao8qdZUjbxFhTk2Z3oSLOoLtO6iKstI5G34Hc3e0YrQkv4XijcHfXaBZL_S3PTXSxtXh999ncC4LH-irXU6_ewUul6kYEyw3XHJn-Y3ppzx5k8js_8U3VgXCy8sWyBlKUnTTg2p6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijftfwH2wgd7w3yl8f8Ibaq9y0DrwuVSPnSv8xUMwUZJ-1h07RNS1HBKVh9zYwt4i1qD-Poo77tjcFSdI07MFMnPJBfMPkzK5HuODCKr4tGGs-wmaQ8OzFdvKmCMrGH9crk_ujk0Q7MUlsfkXdLXxb_rBldCsbo-KtH5e7A57QGaEkCVRbFlHbzKSQYVjoB-FdLY8Bv1D_eXNAbZAVCWv6-R_4T12Du2IbGWu8fFhLrZC1CZ7wyLacLvyY3UlWQ9S9ZywHMNCmk2TeZ3tvirn-om4F2iQlVmQmdqGROWXrMxpdB451XylYK6P3ddgzY2YQDEGLbxLxOh5TXcH_vhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIbS6X7VGYuKlbk46QpMDwAdqrZF63QUaDonOfcvjhlpY7cW98KEGDxKOs-vTDdBS0NOr96K7nOGvCy66fZLShgFQi0tVesed7q2RJWjr67Df_MwBBB-H3iWM7wQGmoQxPW9iIO7X99mj2O99rvFpAPC5lMqKbLo8qFDJ6CItd3rFZ9vaqQ4Nl_inV1JECx5DHR2vg4JqoTyIvPmEvJGtpDiDqzi_UU--qGeS_RYOTY7_pnUxU0zmKAM2cvyxAb2ZKXmdW4ohj6tsEte8Cci5UPioUit3d2CohDAktY2RMoR46kQ2RJomphtD9RO_EvEKznZ0CiU4dIopW0BS5aFLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نصب یکی از بزرگ‌ترین سکوهای نفتی خلیج فارس در شرایط جنگی
🔹
سکوی رشادت به وزن ۶۲۰۰ تن توسط مهندسان ایرانی طراحی ساخت اجرا و حمل‌ونقل و در میدان نفتی رشادت در خلیج فارس در روز اول تیر نصب شد.
🔹
این سکو به گفته مسئولان اجرای آن، قرار است ظرف ۶ ماه آینده با تکمیل سایر بخش‌ها و تجهیزات آن تولید نفتی این میدان را از حدود ۱۴ الی ۱۵ هزار بشکه در روز کنونی به ۵۰ هزار بشکه در روز افزایش دهد.
🔹
به عبارت دیگر با نصب این سکو ۳۵ هزار بشکه به ظرفیت تولید میدان رشادت افزوده خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444441" target="_blank">📅 10:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444440">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISQnIChJ1DHI8W67V_Nx28nSk4O7ZUTjBCj6QSWR_NHfaEKcl2oP8362C_X1u-atCQf5IE_uCj2KI-Omaq3fG_zL2l9vDjjuELz1vQNpFVVZ5CXznJrKtZwSgGEwUGN1mR8-COlDA3dSgXFkfczaq5G8tvubY7-hBboRMYTXZec6RqyX4l6IakjzFasFrJxsL8Lk9YYiFbK-uZwNm9zrjDJbL793w-xWm01s2JLiAFDtvkiU9pEyS5Wjb7ocFnceUfKOHgkMkrRjPbHcBWClw5Qk48Cvy9FPlUb3zgdLXD7_1Ptxqtu26iM6DMmeOSGR6i52X4FgEDZ-PWvCqoen0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باج‌گیری بزرگ حریدی‌ها از نتانیاهو؛ انحلال کنست عقب افتاد
🔹
در حالی که انتظار می‌رفت کنست در هفته جاری روند انحلال خود را نهایی کند، معامله غیرمنتظره نتانیاهو با رهبران احزاب حریدی، به تعویق انتخابات و تصویب قوانین مورد درخواست حریدی‌ها انجامید.
🔹
به اعلام رسانه‌های عبری، «آریه درعی»، رئیس حزب «شاس» و «موشه گافنی» رئیس حزب «دگل هاتوراه»، در بیانیه‌ای مشترک اعلام کردند که به نتانیاهو «مطالبه‌ای قاطع» از جانب مراجع دینی «حریدی» اعطا کرده‌اند؛ مبنی بر اینکه فوراً در مسیر «قانون‌گذاریِ قوانین مورد نیاز» حرکت شود.
🔹
این بیانیه هشدار داد که اگر در روزهای آینده اقدام عملی صورت نگیرد، آنان از انحلال «کنست» در هفته آینده حمایت خواهند کرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/444440" target="_blank">📅 09:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3oxB7iNH3LO86_F1HI7S1L1OHxZfX5SyppQ5CmruQFEL1jKg7cU1d3dmaKQhLIeH9IW5ovfPNq85yix54qpbvZwXC6FLdUrptx_qVLHmtk3Ym82FYE0d0tVKWzmH2l1e5QbLEKCgZ0ymXjasDjekToQ53X-oxgow7j_OdICX1wDKdz6dQfYfj0Y_0KSd3EZ_9qUiba1u7HWSJBbix1J2hTFMQ9ITkrtmJ-bF1SPIHA8dcRZthv7d-UPtV23Xnukbi-0pIaeJZARxkHV1swT81gKF_ZpLG7ejBdiZwb9vl-j-RkqkZS2LGfK0bNLlHQJ-5MQzsSzCFiqaewshQKNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم‌های صعود کرده به مرحلۀ حذفی جام‌جهانی پس از پایان دور دوم بازی‌های گروهی  @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/444439" target="_blank">📅 09:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444438">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6471f3a8.mp4?token=G7Sx-LVtVIarVmD1bPq_oZvfmstBg12GO-915v8SR1OMNWSnqIFmTzZXRspdBl_6Nq53OdS4_HgxB0LJvraWRs4wG2iwLjnD6O_aeYJccyX2P5GPFN6ldchM6Q1hXxNSXMLojOpqK5sxqK-wN7539swTvIKjbtK6Fc_TBAyTEGX9DQXqAfYfctiCg2gVujyXVz4r7sb9RMcZA9OgH-gKtMasoK81bWzwmNvvHsZqtg707-wxIxYk1rhh5wRgpcj8L09ubDYPg-fu0QQ5UPI6CMFw18Vv-hBUKQnCrnwof5nBBr5VjbwHb-Tk3DnwXEFOV7kE7RS4WphRQFRqGvsu8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6471f3a8.mp4?token=G7Sx-LVtVIarVmD1bPq_oZvfmstBg12GO-915v8SR1OMNWSnqIFmTzZXRspdBl_6Nq53OdS4_HgxB0LJvraWRs4wG2iwLjnD6O_aeYJccyX2P5GPFN6ldchM6Q1hXxNSXMLojOpqK5sxqK-wN7539swTvIKjbtK6Fc_TBAyTEGX9DQXqAfYfctiCg2gVujyXVz4r7sb9RMcZA9OgH-gKtMasoK81bWzwmNvvHsZqtg707-wxIxYk1rhh5wRgpcj8L09ubDYPg-fu0QQ5UPI6CMFw18Vv-hBUKQnCrnwof5nBBr5VjbwHb-Tk3DnwXEFOV7kE7RS4WphRQFRqGvsu8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختلال خدمات بانکی تا پایان امشب برطرف می‌شود
🔹
رسانۀ بانک مرکزی: اختلال خدمات کارت‌محور همه بانک‌ها به‌جز بانک‌های ملی، صادرات و تجارت برطرف شده و خدمات آن‌ها به حالت عادی بازگشته است.
🔹
تیم‌های فنی و متخصصان امنیت سایبری همچنان درحال رفع اختلال سامانه‌های…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/444438" target="_blank">📅 09:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRrKbhcexnRpRULupBhQe0nRa5UNSqRm9XYC6zmoO9JcuR9CP8ua-8Z0VtbgjDvt6awiW2FXfGBFIoa7sVHIr0A7F6M9LnjTKeimilJ-l36q-A0_W0st1P_yWcUqOH3BpJjv21PgnG8MdwqKfVLGCtTVvxOT_6M_lrfuI2LNBK1A2_Uj71MNxwniUd8n9s2Rop0yICNQt3MnWf3KpcwbE2BzMwI4ErT5wtnTgxrUM4JzasLDnjL-vd6Iul1tCEDC5Bj4arQHEsmG_wT-28ej_HzxSfJ3p1BZWYcVwaKrz4rilLdElMoHPEunkPYk04udy4mEhTKgMY45c-L7dAGwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم باکو شد
🔹
رئیس مجلس، دقایقی قبل به منظور شرکت و سخنرانی در بیستمین اجلاس کنفرانس اتحادیۀ مجالس کشورهای عضو سازمان همکاری اسلامی، راهی باکو پایتخت جمهوری آذربایجان شد. @Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/444437" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444431">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0KVa7Dq36yotWSaSEdtkz2WuWUq8aG2g84kAjgfat8tdz0rX902lbb_uWDxgNZxTyw_N9LC6gl-AYL49y2OqFywk8AbsUeLjDeQrY70YIpuFQ-gUXaRIBowezbFyqG9hlZEWWlLHQCF2TK9CiIQAUs0pPYXVLUfGWiDQbmM6OQdzYfMIW96kJQWKJnHIYkVPMyt4-R6g3Q9UhJzcNa9aeCBH6OcWU7WV0cmSn582ZMJ5rCitYd1IyPksvz-K2yVJE6vhy82E_zrI3W7gnuExokWoZEJLyE2jQa7pX6BUw4lOw8mrHXq3dx3z76uBBXME51tqsAnN_lwJURaflOD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnTrhf1lJBpSE2JJayk6rYotwNT5NB5uyHBAsExwGv7m8JLXdp6oGl3b-SmlEHxMc3P7Bl1QZ3X2Lk1PdjHR9CQ9dM_J_Zx5RVF3DIpjG_aDxsHgRNRm8QhSbP8d2M-DhGCFN9u-tyK3kXerTbAguNHEu1SGZTtVQ4wxwuiH4mtak8C4tVwvsnfDNy1xSe4ZnHjxIu_RBtI8aPNpjJNSFsFBQDPJwztiCQ1QdXlxG3rBaBb0GSnQqlpsbhTJMpOf_Hl2d1V1OTfW5B4tjJMRh8kSpPjcLw657lLETTafL5kJUnm1VBfbCzpxF2qabVcn5n99gdMmxirOnEhFshKwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYMpPyyh42Ojsx8gRa6Z5i0bqJmfPslHQF7u220QgqLUZINEHQ1CinBm4kyUtOm-wEjWmKPVQ6Mc5naumi07gUH707Es6XCJ1wG8n3irEP7qA3ViJLFIfGfsQefUV70P4kOZVEVt5HFKg5F2DCu6WkqarjOEyf70d-9tCNmpqsxlBfRntAGDQKCQaBxUlsF8ZNZyb-VXnWIgD6WDTRJmekgqYRXpDVpKEYeia1hD2Pu9PMq2VJwzwIHoK34M0x6fj7oy9mabMmuhFT9M2N_OxBKrx5WeIFr9uEs9cnD12PDepxhA4T7yH8Y95HCR2MCwZbhNnNWJYg0RIPNpBUheag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRXBy7gwPFd3bp7REb7h3QwiR4smKYtAYAWYE7M5CiSkS9FXt8nmEUSx3_96OAZu34QnG8UhE3gUlnWQRG33rVtfxsA41G_PzkrapN1LbLcvyhGCS73zP1o-Emtr2ALciNjs2Hq1bgDC-qp5bWpbXkbNAd_-acfZllBwA5s4Nk8ojMDfp88w9DujW6l3qnG9IYYNSutUeXpNjcufWs_2GgUZIZBBJskDxsGf1EIC5LOp0ZMZ2kS33PIWquWc820j1vFO_bqldLBCH1SA2FQSgQ74gR8TfcEH7-Rf01LIorIASAOtdNMscN2nXUM5L5o-WC1NrMeV0hp4blXexDeuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTbbZdq4iq9Y9KRsXVrRmekZ40IqXfjjE0oUfvbt5cXUXx6KQcfEXDKKccn4yAMj4Rhcr0K9W7fQaGW9KkVrdJbATEeg1Hk28A9PO95Fd8FCBj83fp2BuLXUA_P97K5NJMgcCyz-dzmiP-myWLyKre5XNuc_arFH0qOYC0mhEpJjqZIC8mFjX5NGE-XoYhhIasZ4bDGjH6TQnRH7wTlAZuvuKopAn7CQVyZxqcJwzwGNOokamTiV1KiEmq-ApLkzu_LWLVvrX5GttZRI35_eOtAsw9pui50XmHAizMgoIMC9ao-eofCxA4zzs3zI4w51QFtBwTVRtTA3X4VklpFP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnTrhf1lJBpSE2JJayk6rYotwNT5NB5uyHBAsExwGv7m8JLXdp6oGl3b-SmlEHxMc3P7Bl1QZ3X2Lk1PdjHR9CQ9dM_J_Zx5RVF3DIpjG_aDxsHgRNRm8QhSbP8d2M-DhGCFN9u-tyK3kXerTbAguNHEu1SGZTtVQ4wxwuiH4mtak8C4tVwvsnfDNy1xSe4ZnHjxIu_RBtI8aPNpjJNSFsFBQDPJwztiCQ1QdXlxG3rBaBb0GSnQqlpsbhTJMpOf_Hl2d1V1OTfW5B4tjJMRh8kSpPjcLw657lLETTafL5kJUnm1VBfbCzpxF2qabVcn5n99gdMmxirOnEhFshKwrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین تمرین تیم ملی در تیخوانا
پیش از سفر به سیاتل
🔹
در حاشیه آخرین تمرین تیم ملی پیش از بازی مقابل مصر، یکی از مدیران باشگاه تیخوانا تابلویی نقاشی با نمادهایی از ایران و مکزیک را به فدراسیون فوتبال اهدا کرد.
🔹
در مقابل نیز پیراهن تیم ملی ایران به نشانه قدردانی از میزبانی و همکاری باشگاه تیخوانا از سوی تاج به مسئولان این باشگاه اهدا شد.
🔹
همچنین کادر فنی و بازیکنان تیم ملی با برگزاری مراسمی از علیرضا جهانبخش به مناسبت انجام صدمین بازی ملی‌اش تقدیر کردند.
🔹
در بخش دیگری از برنامه امروز، از پرچم‌های کرنر ویژه‌ای که به یاد شهدای مظلوم میناب و با نشان #۱۶۸ طراحی شده بود، رونمایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444431" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9pA8xivsp6JJxH8n2Z46C1pL8Ao1kcB3iKnjwsOSKOLjhHhnzXSyD3E6MZ_q02jR7X_0inyC1eDZwZk8GAiNBOREaTbsS2iwsZbCDMwcFIaIOGZr-i9av8UiONTMI8qpiuYv2PJVhz9cnZtBUKKVM46IdVkJcwVG1PanvxroLlliyhWoYUhSiLK31I2Zhs7oOjno4v_ISbaxtJG2yyUMw5gNTGmYXGRdniUOmksFISKufD2sP2nf847ANpOF2r4YNCB2cHpF2JocfbM-Asd2p3SBBqJV7wTToS2p2mOrOEXinSZuNdYAzPb43qYudc8OWO1DB_Kwb-Wvmr7faXP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد سخت کلمبیا؛ صعود قطعی شد
⚽️
کلمبیا ۱ - ۰ کنگو @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/444430" target="_blank">📅 08:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444429">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دریای مازندران تا جمعه شدیداً مواج و تعطیل است
🔹
هواشناسی استان مازندران با صدور هشدار سطح نارنجی و پیش‌بینی وزش‌بادهای تند و مواج شدن شدید دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را تا جمعه پنجم تیرماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/444429" target="_blank">📅 07:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444428">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9cQbtYkuGxKxhJQdo63F52RY5IOkslNlqv-sJkMmrnnqN7aVRUkGincjKuuxZUWQeIOa3ShetMWNEUcQ4EmDTLSCGtI_1v-xgLs6GdXhRpDg15JqSi62TRUBtSnml6T6i5JfA_n5ZscTk58LakFWvGkNkc2GnDJ3IN8sNfpNFjFKVTPJFp3Von9U-fEZ50CBDxql9JIzgcgzivbrsdoyCl3pxKSErsxU95KKJWzFjpxdAzdcXLQ29s_rqgE_LQPVJ_3OR6KLTBH1vbp2yyJXU8t0GSah92yc0J-3hSXgBttLbQV5mYfbsIIQd9TnvRMOdFaslSk7eItb1v31bRUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444428" target="_blank">📅 07:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444427">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc-ubvwD1h5MnbmigfIpOOj9r_Z7gvk_JD-0Ik2gxbXZ-aC88pe7WXdFWh5tFS_1y6yW_MvxdeRAXBEUGdOIOSw_6asLlP0GoSPjqFLv9O1u_i0HCuYvNCzz9GF7NeVt3rZACzg8AJFGXng1nc8U78eDxikfMPME_pci9aue7GKxS5e9ANQkpBVUlzqmorHsA-IcBLmpUHbL6obqP-zPMfdfj_I7j9-qkXKrecMJ-vLnGCUql1F_jfZKBjwkT5_2okXwTlM4OLeexPGKTfjPJ_P9e19YcwCVoIICsBySvXyLc3nZR0_GXXpzaIBDYyCHmQzLuIRD-ZVqB-PwHbt1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد سخت کلمبیا؛ صعود قطعی شد
⚽️
کلمبیا ۱ - ۰ کنگو
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/444427" target="_blank">📅 07:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444422">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mF_nsX54X3sgBZOiQZI6G6DptDWuwyRNH2DTGglZEERKJYbtUfYC3OXBVT1xV0KzrkCV-jEwl4PRKxPa1TGn-dIMTTYyNVUMaFPPmM4Uv-Rou5woSecgEPbx2DX6NqOh21BnBdYzZgJ7Pz3HpYFJjUWiAumLFeD_vRdD7BFp5220ikyf35KMcAiv94H8Of-2nInJ-xg91R_XKyIjSHudJIHliIF9s3nj7uyn5MkLYgnTPqcn094e6evFE6Fu0Eq8h2aJa2O0hgmmahXlIHubKyit44xYoYCkhj6xiL8yWWbLy-ydNZnck13CfrUerAd71KBryqvS-D3EYq2TsPvt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mf9WSu2QtzD_m1q7Vyi4cMOovHYnu_nLgm2DdgFr50SC-CNVwZuTgNc1g44wrHVZTJEyJcPeb8Thn0u26lBp7xsDHFfMFrCcGiIdQ4UNUDAe3LFgiYx8QlwcvLGaKTQ203r9rvAKQclzrfBi8Np03J5_c7GIdSO3uZyzCjsifzV7Ornudv3odr8fIStCj9DzvpFXj-PPbiLOig4zNLcQDjXpcx7hX9iyKSjxuYKGzz-6HJyYehEx2u2VViMcxhWE3uPPlS7Z-xHw-BFVc6P1knHbEkNOiCdxBToFpQr9GHl5Zxkv6S5E1yN0Ca0-Q12SRRaNRD5-aVDNGckLsbd57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSD8pqHRzfaxBaBMpCKUYihbYn16lbUk61_80TtIANh2_JkQx858zs9Cj-BVvcokrF-kKDAZhcvRDBbRSWdZ7PRznIVr0poyj8qAdAZdLN2wXWHD18VwXURVxbxOePeY6p9YuRZPUoXt8xwxcwmvezE2qvT1iqxluH_UiW0tSSGBCAwdP5M3ktDabBSemjZYcGcWWYvY7vUu9ktGQbGgEXBGsbrQzIcRS4bTzBD_hpAHKZrLM3H54Jis9qz-0wdCoACndVv3-sJ1b2MBHUoNFPIpNtOMSFD5wbAjRhEJrrlXn4Pqzw4ha5aKi7g10u4msNz3GPMQ0qO2ciMua4zvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uK8eL5lAybduYpmhjiWvrI9CZomDbZpd0OJAfITZFCKNC7ty2CN1WY6551kXiUST5rP3TFmOGsU_e9M4tsfYNqwQum_pIXEVnwhvFKAgYe0nfwpcVK4LjxBgJ5d5ZBwY7tK6dRYgxroe9QYbP1npxBA4MyZSfhZpXm5K5O67DvDlTfxm1Fls3UYY24ZOBK0o21ivCrobQMdc0iVHEbzKBxPiyoLQte-mvklIvWINH2WcD3aqiOZCoXVsE-3jnLgEZpqfpJxFUf4AGQnyBuFtu67qPphoHZztY7TGDNOcFAvAAWrXV9cneRdQoR7y4qxF767zmeDKX1c7a0iMglvHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxNwZsuka6UPskL--QK9eaGO7Wblc2EiK3NER_19HI0huJTL68-eBB341eeNmOIUmbzdwFeZfDRbC-ELxJbEqbxdmn5IPPLl34nZoNdCZXKKjETGBj2BMAJEWx7QEJliVJwOP0YdYXwvt65uRuBWaC7tnj2Fsa3Mx7FaG87fNyPZd27LPX2otASe5mabB8XFUrV63WKICxFXfnlcNly9dyt9uAKBxhhu88ADp8ZnZICD07tWf1PzGv9ArPrBm8fLSOYQYdCgVefFL8ws01JmkqPitDIqZjxH_OC_nJDDUk2FeEQOjIAkcDJqKHcsbY_mgZzX1X60kMTTxReuOFwprw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسینیه‌ای که در آتش اغتشاشات سوخت اما چراغ روضه‌اش خاموش نشد
🔹
اینجا حسینیه‌ای است در بلوار وکیل‌آباد مشهد؛ همان‌جایی که در فتنۀ دی‌ماه، طعمۀ آتش شد.
🔹
روزی شعله‌ها به جان دیوارهایش افتادند و حالا در محرم، مردم دوباره به همان‌جا برگشته‌اند؛ نه به حسینیه‌ای کاملاً بازسازی‌شده و بی‌نقص، بلکه به فضایی که هنوز زخم‌هایش پیداست.
🔹
میان دیوارهای آسیب‌دیده، فرش پهن کرده‌اند و جایی برای نشستن عزاداران فراهم شده؛ پرچم های مشکی بر درودیوار آویخته شده و یک صندلی ساده تبدیل شده به منبر سخنران و ده‌ها نفر که صبح شان را با اشک بر امام شهید آغاز کرده‌اند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/444422" target="_blank">📅 07:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444421">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کربلا به آخرین روزها نزدیک می‌شود
🔹
روز هشتم محرم فرا رسید. اکنون چند روز از استقرار کاروان امام حسین بن علی در کربلا می‌گذشت و شرایط اردوگاه به‌مراتب دشوارتر از روزهای نخست شده بود.
🔹
محاصره فرات که از روز هفتم آغاز شده بود، آثار خود را نشان می‌داد. آب در…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/444421" target="_blank">📅 07:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444420">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSZDv_7WHprpl19BKLmEvj12Nqx6VleJo74axFVthyM3kKydc1JN7grR5PtXAQlNwtFc_0Rh7g1kRHfkIR85WA0TQvJIO_AVqz8LmGU8f1UKvN4es3JAin6JNOdesc_bvKau9mSkpjry6MPmrluwvu7L_iIAt3cgo2lO3qRUPxCldzuWXpNONTFgUOddIQHpUz3niDPt_ZTt5nrwvWgyeavWsWA6-22BHlOLTYAF86tWv6gvntdjJMCpi67jU_tymbAX5r248UNg2-PI9wOLhvv_YiC8w-jGxT9DGHFp0jp2gSoKxoS8hvEdfMHHSM6ibElo-tdy-e4IJ2M2mhhUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم باکو شد
🔹
رئیس مجلس، دقایقی قبل به منظور شرکت و سخنرانی در بیستمین اجلاس کنفرانس اتحادیۀ مجالس کشورهای عضو سازمان همکاری اسلامی، راهی باکو پایتخت جمهوری آذربایجان شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/444420" target="_blank">📅 06:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444419">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-rLDw5wYMXGka7PL0y5xg6XullSbHJqAsHYu0tKCsFPJdM6g2fzkbEiBb-JvOouy4cGI2dXFE3rkOhcZNJa39Fs7ljUc2oXFWK8uQhx7HZbJHIHtZ1xfw3gQ9bxMS6_aJoIat0RVrUN8Li8nuWF4-OnTzsYb48Xhts6mNLpwAgXlSE_kV7QwZqkP2FVBNvBoweQ-uK_-TtpAO2dkvHHOfRJBGOopaF4ngkvN4WGSkg6mbDXraVNgqi2SIeVp9VEDXqTfVApavSHqjRfpipFGXNkTH0zKbbT4tx9O0rhiuvTdodYdDVTfJH2X4UG-_0S6y8Fgsk5ojAxOx6F610YEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجهیز نیروی دریایی کرۀشمالی به سلاح اتمی
🔹
رهبر کرۀ شمالی اعلام کرد که نیروی دریایی این کشور به تسلیحات هسته‌ای مجهز خواهد شد، و برنامۀ تجهیز درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/444419" target="_blank">📅 06:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444418">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY3VO3CXy56y5yO-Ob0PYRA0lKAXh_BVERvY2RQWwgvoLXxgCjTpwsK_JvIcGFO0eLVqc4-9l1UdEQb6k46JU_ilts-vrS4HEutPVBb7dY4KKqDPrciS4Hg9kh7qM26bbyVO2jxvpCMo8DXX2xNGUjGRgMgSMCTd8pv5GQWgF3kY3_fr67AbfsZL9qSWgWgiAH3eJ1kC2SLMZoxSBGVDXD65DAKsJykJaTRobtzl48qTPSakjb2mWEf-gnW8r1Iy9xTJEbutn7pnxmN3wR0Vb5hjbVdG8wqjN-vBQsX5cOIU4P67xt1846Xq-3YKqOV4TFemFl1DgJYPWDyNAgNNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای پرکردن انبار خالی موشک‌ها سراغ خودروسازان رفت!
🔹
در حالی که ایالات متحده بخش مهمی از تسلیحات خود را در جنگ علیه ایران مصرف کرده، هم‌اکنون دو غول خودروسازی این کشور به فرمان ترامپ خط تولیدشان را از خودرو به موشک تغییر می‌دهند.
🔹
او گفت که دو غول خودروسازی آمریکا جنرال موتورز و فورد، در حال آماده‌سازی برای تغییر کاربری خطوط تولید بلااستفاده خود هستند و تاکنون توافق‌هایی برای تولید محصولات مرتبط با موشک منعقد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/444418" target="_blank">📅 05:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444417">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
تست موتور سوخت جامد ماهوار‌ه‌بر
🔹
برای نخستین‌بار، در مستند «مرد ابدی» تصاویری از تست موتور سوخت جامد منتشر شده که گفته می‌شود مربوط به توسعۀ پیشران مرحلۀ سوم ماهواره‌بر «قائم» در جریان پروژه‌های تحقیقاتی شهید حسن طهرانی‌مقدم است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/444417" target="_blank">📅 05:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444416">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO2E2qDNQ_gjWZAIt8uS0bvsq2X2oQlaQE06BwGGmpApXPu-GOkqfAWw9XcmqVeVnCT4h7yJx99lEuMoPqY-9K2AOCM5E2uU01pFDeAd8l4nP-Cq8K-1l8gwSU-i7T17eekUz-MytJS8v86VE4YWJDVd0SLtxpZKDa6S8RCIuXBSVvU5hHLtf7Dh6V631ZVD4HYjsSmMvKeY-3tGiu1tAU3kUh1Eqo0PUBdhTxVzXJvwDtcpCRemgB_9gD6pU_XszM29-QG42Eg58YzzDICer5snBaLA8cEmSC0G_GxQnEqmtl6LpfuZ12gR4-v_iKkE1n3TZWdHTLO1yQqnmUcZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد سخت کرواسی؛ پاناما از دور رقابت‌ها کنار رفت
⚽️
پاناما ۰ - ۱ کر‌واسی
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444416" target="_blank">📅 04:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444415">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiDSIpQBuWaQbF_MwRwWnKofOA0CGHVhPC3Y3-ZSt3wAA9QozR2fyDdXtXEf4lLs6Ezb3TU_BV_v4bMP4bbTJEblU33JwXs442Gt9J5JeQJ73gLu2LsUdKSkOx-hdXTa_DQvMFoVhEG2wGhSJoleZ2-AZMV0U24InTkSr0r1gpKm2Sy0aFTpcnY1iu3Q0_azqBjcB3taulN5DyZhYBqORXa2ZlT2J0NEtf3e2SuPjm7QSnLzQVvuKRcpQSTw8hMdYBwQ9PzY4TUEKNW7tOKzhMhHjUVguCY_4yPho5GiA6azvM9Nqnad2nS-jEJDfnFkw-4mKx2-G4fOY17zmhN3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جریمۀ ۱۲۲ هزار راننده موبایل‌به‌دست پایتخت از ابتدای امسال
🔹
رئیس پلیس راهور تهران از اعمال قانون بیش از ۱۲۲ هزار و ۶۰۰ فقره تخلف حادثه‌ساز استفاده از تلفن همراه حین رانندگی، در سه‌ماه ابتدایی سال خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444415" target="_blank">📅 04:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444414">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN-jnPnowAcPWiUZnfHp_I0LqyfWUuOQipkbgfyGuzpRtPeYykTvbp2_p_KoizwUtaqm4Dw8nzrV5LS_Qv5QMDNYqLji-loCCyuUhUBB-2fXwL3yrohYDWWKKm2jpvJko9yDu1SNkRWSOJfzScKJlrwhIcW1MrGxB_gH_4bVmg1Ru7T81QPlHB-jV_pcO-MrZbnYhaBgNkKatAF0Hlb7dVsZOEyaNcqJGpbN1cCkymkG73j311SuDIlO1oYNZMp3gsSq3PrXL9ncj684if9a_b52Bu-_aZraHa0bQe2WixYJSs2x2ba-F5X-BjiYZSZVDnghYLfO3G1-wyOA61BzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۰ درصد نوار غزه در اشغال ارتش رژیم صهیونیستی
🔹
شبکۀ آرتی گزارش داد که ارتش رژیم صهیونیستی اشغالگری خود را به حدود ۷۰ درصد از نوار غزه گسترش داده است و پیش‌بینی می‌شود این مساحت در ماه‌های آینده باز هم افزایش یابد.
🔹
همچنین ارتش اشغالگر در حال گسترش مناطق امنیتی در نزدیکی شهرک‌های صهیونیست‌نشین است؛ اقدامی که از طریق ساخت جاده‌ها، توسعۀ پایگاه‌های نظامی و تقویت نیروها انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444414" target="_blank">📅 03:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSQOL1AMh1c8lQokkw1oYbHGPC_ia32sPSjZRJfeL_5QgZn5SA32yDWMLfD-qk_BIl_zaZqiFqtJjdJkeLkW7_FpaUreoZ772CJ7Y5BANUc58S3iVE9ci4QWbS16F0KU3sMVg730L3tnDS0O4fa5xvDqXcmDVwql4z8MGDQ18YQcdZYSmvRBA817WiekoY82kzlQZW5gOn6bEtL5Wwz3DrhXCL0OL45KUg2YlR3z5D2DspOxqau15EkXjs69ZaTeephASa8YSLbUH45VCl-PRCNOhOGTm3aRpc6yvSfc5MoRnqMlWb0N7AWUNVNlS8Mhr_1f1VnRl7GbTHLYWheTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6I7dYpNxJlQxNwxYRco4zmmaj7fC5XPmZNyPkW-kNO0rf322uFPJzzA_8xaZTWRsNyK3sE6DSl2sXCWEhJQK7OypFZATonitnGdrZBeEFSrD-hLJ5-imPReJn5BQV7YL0gTjOHBk9EwZqND0wfycWz4w6W0YopLNQa9kWVp0wd76gG204MdYVtdSE_vqJuqcpW9IxAVkvV2pt3L0iR2oCxI6MzQVSrhiP7_xliZfgUgwbYXElh9fKg3zN-2Rvhh-i-yFa48KaCYn5Sp0MUpABkL7TZurTm0PiprNRwOjBapqIXZtD1Q8fGmTMRoBX2gmAG6ggUefYayGuFGuWlwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQMd03DzV4ngYVOFCvxUo-A0CEoy4HRJ5c1TEfmBlNg-VBnWhT3rTrROHnqzy6iw2Im8oAi0wDux8PGEddr46MJJ7HQ-dl7x_Lm26VkcZ8zcKBK73g7AQhWanWzBrfRzJ4zfCCWjJOkUrYF5nX7H_BOXVjlbmUy-0M7QekWW3pxADLLLvf_7ZRaMtbI6tENTjTJVb1GOc7lCAbaw4jIz6pTPuGLY4hbSYfIHVg3kwHkO06otGQYyVSfRnLyBTKA4nOy4BAqSXt7q-OxSmq9ARo3XwhgqNQfKxfvOZ9txVrUrU8MjNF8gdlAKPKFYu0q14P-iDXCfYqg-WTPT3rbt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ0O_iCqLIJcPs2ttnd4a13RUcuXODcEPI2LIZnYQLFwtyImR_a7oNvNUkUYWtC6FyVrYraujklRjkevxGgrl3aLu4OUwlUysN0kn_89CSE7qghs3H-grFRdbVobZ2fokzT-tZjhoPJq2sbPmyIlgd6z9v8tJk3eKWEJH9tN6F_KW_V0P9F_bk3_udXPAgtN6OW3VrchfSYiwAN0S_pnTh6NOFbjkdroyQh_66OlFNNhFsru3KrHcbtkhpPYppN9hQofadapdcUOZABty9AxKqi22IuPo53G1ogewZOApXAnMwk74jwa7QXripD_7_t5EYqhKZbXA7gWT9qQkURU-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fbz-bHwSeDxWbZlWkcUK4V7rWOyZGkYxQiczfFjETxvAy_Vl4t1gb18PucmPyWLpD_M4Mjl3nQT7rCh9C5NReRtuUREht_TfUmI-q3Z89DyFf8Dt67_IkP8JjCZ2kPVUm0EKXgasd0xju9PVJu1vNouz_540T3pjj_LXx4TmcLIlYm3OED_1AZ2KKMTzH7qoqFVQmSNlU_RHrXKZX1EUZbSFd5sefhMpR8sUKvXA2VU_AE2DCPPiicgtaQ-SPWdl-rJ36IK01QZH2c1_FqQd9nbRPWNVaFc8oH76Fh0T9fQZincPiFN-Qi3CsYqpLkC9HDlHm_Kor-AoJyycEWq3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owFG3NzZzfWsKGBrmnNECrl8kqTFo2S1VAm1lZKwsvntFoz5zlKfniWeCx9fXLCOOogP5kF0SuBhZOnFGKb8A_M48LvRcmVZ_21VJRc9FBprIvyWhbXYhJwO6nEnJnYHOszYi7RBRfOj75f8h6NWtGOLRtYy_XsBvh1JtrsY0HOBlAeOlbdmskxJhk8lhOH8DxNPH6czjbbMbVDzkYueK8zOW1sw1L3OFbyW8LKrm7Tsaed7LqHwDgiouFBY8feHTwWV2r71aJ1YLy69x4trGbuw3DIAyXp13NAXcqZ2FwMaK7KysBme7YSsMqyrcLbJOxrrfX5n4vZXevH_1yDdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hA4m9lVxuoDEr9-0GZ-zba6YxzscnJuakP-j2E9iezZGbFOYdX60GbYnOdfgfNHgFemSNnxNSiFd30sOv-HlilEqhQ52daybrBUG7PgXwGfJ7UHLbd8OJNp3fy6tX94E3NA1JDMvgV885o6iWm_mTio16QryppbMC4YuPlttKOYMhFCR38NrnWFUbFLpaY8xOKMZgkq2ZnL0-7QWKHmykVNxLqJfGlUMIOTfBtn256vMFNIlxGbTQv98hmDFgiFzyuZQ3_qVYuauu6Bj71QUkc4YAzJNKtw-ip0vekXvFSCpIdTFfHqf-ko6dfqN6dAWepRa_-keeKzNP8yg1phxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqERGz1JAZAlGA8GH1Hq7VTWZ45tLw41J3HgkIvRG-jx4YRyiZAjuKhrD6CigXfFqNOLaZOi-D7SeBYew3rD8mNLd7djC3BbeMejhcfUK45rqaSbMwO0psVYXrlhOaY9KLPd77QLj5bunjzyK6estOPfCMRw4JoOZNo3ckiLs7k-6Z9tKVvS2CFn6PK14kEuOQ--RpRx-uUkwwzZDUp9AfmswxpXrRP5ZomDv2O7FbMuP8r_wA6DcWbOfRQNKZmLrbqSHoKENDFZ3kaj7DNjwjXHK2f2JOC48PgUYUgp1aVs0-PFqbbeX-QePubLmEkd3FL-ZtFcabLNhgGZhtqDvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع عزاداران حسینی در رواق کشوردوست در شب تاسوعا
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444406" target="_blank">📅 02:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd86c81b16.mp4?token=AKhwfk84-AkP-SDP9U9bWp8ssL61iGnM9FSOMPFe6rTKrVqW_--saeKK7MVhkrDwM2PZ1pQZ3PhXGRIAcwGLsWn4XAupQ5bgXYvlYSgQYWwBKFtdYVuL9wXTtYEgQQJF4o63DD2JFoy8u3Zy_pUPF6pU64U26Nh5x2GL6ztNqbIAbrvVYkvZFvmnApvnjDRVs8HGmaU1Y0Qft-bJHSYv-fmsozz6g73NJH6t64wlaa6ghOdnYFZ3WUfNEeDtdqFC23U4V5KrCmUdufQVV6rtoprgUR0_SDI8a0WPVPEr39qccX6QLuJCF5OAza-3T4xP3sFxWvBdQTWLYdADhYfOEVYji_4-gdCFQHXPvNUE5Xb1h0Ae1a4SiU_bDfK4YcW-jhIWOopwIMKIJ4k1B34cOqiw8vxjLoGbwKe7Tf4zieibDS-zgYbpbK2gNsBpfYeyy805V7-Q5E_SgbF3YyjxtmeYhafElTG4QCcs17bMmEJaRU-Co2VPiFwBc31TzH27OcnL8DgtDeuFXrzKtvPa3KywBuGcfJNbRu4xEnrdC-u0d4uHoKMcprOWfDsoIQ7dZF-Sf6yr7qzhc-0NQXZQZ8HNyix8OoKPnMLlyXMvqKS6fwMGpDetgvropfPLiHaerITFRg7MW6F4ikv7joMy61A-OTDy_1o8u1BkNKUfBlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd86c81b16.mp4?token=AKhwfk84-AkP-SDP9U9bWp8ssL61iGnM9FSOMPFe6rTKrVqW_--saeKK7MVhkrDwM2PZ1pQZ3PhXGRIAcwGLsWn4XAupQ5bgXYvlYSgQYWwBKFtdYVuL9wXTtYEgQQJF4o63DD2JFoy8u3Zy_pUPF6pU64U26Nh5x2GL6ztNqbIAbrvVYkvZFvmnApvnjDRVs8HGmaU1Y0Qft-bJHSYv-fmsozz6g73NJH6t64wlaa6ghOdnYFZ3WUfNEeDtdqFC23U4V5KrCmUdufQVV6rtoprgUR0_SDI8a0WPVPEr39qccX6QLuJCF5OAza-3T4xP3sFxWvBdQTWLYdADhYfOEVYji_4-gdCFQHXPvNUE5Xb1h0Ae1a4SiU_bDfK4YcW-jhIWOopwIMKIJ4k1B34cOqiw8vxjLoGbwKe7Tf4zieibDS-zgYbpbK2gNsBpfYeyy805V7-Q5E_SgbF3YyjxtmeYhafElTG4QCcs17bMmEJaRU-Co2VPiFwBc31TzH27OcnL8DgtDeuFXrzKtvPa3KywBuGcfJNbRu4xEnrdC-u0d4uHoKMcprOWfDsoIQ7dZF-Sf6yr7qzhc-0NQXZQZ8HNyix8OoKPnMLlyXMvqKS6fwMGpDetgvropfPLiHaerITFRg7MW6F4ikv7joMy61A-OTDy_1o8u1BkNKUfBlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله میرباقری: اگر می‌خواهیم با امام زمان(عج) همراه شویم باید از وسط دنیای بنی‌امیه عبور کنیم و با آن متارکه کنیم
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444405" target="_blank">📅 02:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axZRLPHey6xtEtFfGq9Ks3WP5D_HIa--CoWVHARg03EAIMDffDuY_-ssoM8Bzy8fFFEtZ-Ixw4LfSRajV6EWnvt3J23iVmEeKvwULH5jfmTGQUMfZuuZJlQBN0dXsinVPEHmAJho5AxxgzanUN2zvJt3-Ike_3JrxiNPEcizW34zjWbfqnsWCs0_W0yvKnmVTF3z-YBkC5scQq_higf9vCrKMereHQl0GqxWdxUVZl475kaj-rAY7Yd8DwJz9qs36UvGh1fkk7MS0GJvlNpM44u4QnZXXZgD3yLucY-8v-0ImQdyYgDJ4W-Cj0ib05huGsMgL5dE-H37-nkZR-RfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkyhPP-YbdVoW8GeHfiy5MRZD9BoR5rJc8kgIGB07p3KYl4UXjKaCgclaCbD_xV4bHRtnSSNED9DfSDZrA2FUu5fs-IrfZrzuNsCbDFJ--1h9v06h6Qa-k6VR5MFz1WV9xeGd8A_ufNYj0w4YiTyK2oahqn26BD1L4A9J5uuQ7SaPJy9MftVArhL8Ivfbqpe9bgW3TSYZhPTlNGYfLcxsuKvpsmYm5Bkr_eKgZyiuGo6buE5U8wpgKzIKpHCbH-nPeDGv0pbDQt3qPVtYMKWYfJkM3wW5by4-yCGuE-Xj4UEMHe6gjg7rFbpxYMbCapmx9tsT9-weGnMH5z_Bkn3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVmYhcJfSggAzfaJyG4Ssx1sjfjXscvbucW4MgUHPNAKu0jsTdPCwoqb46wFiR9ehJ_1vna-Jc3fUir8gPZlKNlgjeuH3NlCaKDWDZyjPuS2tGbOhucHrSt8Qjtc6HJv8ogu2M_slXP1WF8-DNZcQB54O11y6pb3BHZCrZmec8aYWXhTM5HR_kSSlr8zIYIqQXUVpGlCFv3ehCVXnfFfBRTGXULih3G-ADjLxyjiPMv02Hch-lG6Big-nieq6-sqYWgMwaMiC8vN9nxNlP-v7Z5kG01kXtG2QK80dnaXrB1y4qT3DV2kZbSShxiS-jZLYZjyga4SaPwEmXfsoJo3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gw30-IRy1qcMToraxh2LNYblXboaGDWa_7xDegkFoDh_oEr_ktzhx8k8RSv81jCE5huuPoyo-GkE3ppR0AYLO3HaHo8_HaqfpbovR9QRRaT4J8OAPko2Ab3UuJEu1k-jzWlTchBEsX2X-NUifhDIJCb3QZc-2elTUmUQ1VyZYTWAB9NbCosLkKeE_SyeFdSNpVKtN1vcL5Gy4W-FEH2nMQWstevbqLmL14HntF12g1Zc1WyBLtE2xLlz0mxycGXLLzDCjjhNqWKe1hIust_CAxu8AJaqIzLU43-BioFP4x_GixRfCTAVwb6mGdLq_Vvow-RCRijSjhhqJENG0IEQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/td3c3CREYBuMRy7K-12DblCY1KF3xgLfK0oUO6VZyaCouafarQWRyCSQZ7s6OJF1lo_EjSdhxwVovRKgLtYB-d_wKCX44E4TQG5yoAh5Mg_Pw-25FzoV_396KKLFcp452ttOR9bYkz7ow6zvbiLkNFut3kyCl_A4ihGIUyyNCXN56UOivBPw94LfGnef5J1rVLJ3ELKdghDeVa1Cr13X5O-Gj9BLOfVVVBYHRtFqetb3QzAVxpHfuedUqVSzVPTtnbt0zjtVb8AI8BrXq4a7kiGU3_U23t35KSeGGCBXYgmxAUddIiZxZNOp-9F4yxcxBxRFmv-KX0oIc4jNqCkzmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزاداری ملی‌پوشان در مکزیک برای تاسوعای حسینی
◾️
همزمان با فرارسیدن شب تاسوعای حسینی و در آستانه ایام سوگواری حضرت اباعبدالله الحسین (ع) مراسم عزاداری با حضور اعضای کاروان تیم ملی فوتبال ایران در محل اقامت این تیم در تیخوانا مکزیک برگزار شد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444400" target="_blank">📅 02:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444399">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSeAKU4yqLoP6KTLk2lrOgLX1s1nuUSeRqXp6-dKvPog_OUpLEAzReGXs2gExMoCISwIt0xKPjEriTQJxGAqsUYZNUs3vUvDE3Sg_5jOX0U-UPU_Bqq0f0m-sbXZsTL_lK_3sOl3XFC9axiFea2IBFxvjTJHU3LDFWXzhV4_U6vfr8nqyvradCHkHx9d8pSwn3_xaHWH3VZMBT4GHXmO0_uDjbE6U7z0xJ7aBwk_CFL6Zqjm5uT7KI-HIaacGoppFWurFB2lRMn_0Wi-LhBvKTCn2mvyXpF4kNCyqtA5uyoL4OanD8i7UZ1xS-VFXIy-m3GrH5oSQ5cRqc-DqB87zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان تیم ملی فوتبال: با روحیه و اتحاد بازی قبلی به مصاف مصر می‌رویم
🔹
علیرضا جهانبخش در گفت‌وگو با تلویزیون فیفا: این بخشی از فرهنگ ماست که همیشه در شرایط سخت عملکرد خوبی داشته‌ایم و نشان داده‌ایم چقدر یک‌دل و یکپارچه هستیم؛ این ویژگی وجه مشترک همۀ ایرانی‌ها در سراسر دنیاست.
🔹
ما سعی کردیم در این دو بازی هم همین موضوع را نشان بدهیم. امیدوارم همین ذهنیت را برای بازی آخر حفظ کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444399" target="_blank">📅 02:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نگرانی اسرائیل از اسارت نظامیانش در جنوب لبنان
🔹
نشریۀ واللا به‌نقل از یک منبع امنیتی رژیم صهیونیستی گزارش داد که اسرائیل نگران احتمال اسارت نظامیان در کفر تبنیت و مجبور شدن به تبادل آنها با جنگجویان حزب‌الله است که در تونل‌ها گرفتار شده‌اند.
🔹
به همین دلیل، به سربازان اسرائیلی دستور داده شده است که برای محافظت از خود، به صورت دو نفره و سه نفره حرکت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444398" target="_blank">📅 01:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌ قطعنامه سنای آمریکا علیه جنگ با ایران غیرالزام‌آور است
🔹
قطعنامه‌ای که ساعتی پیش در سنای آمریکا با هدف محدودکردن اختیارات جنگی ترامپ و جلوگیری از ورود به جنگ مجدد با ایران تصویب شد، جنبه غیرالزام‌آور دارد و معادل یک قانون محسوب نمی‌شود.
🔹
پیش‌تر مجلس نمایندگان…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444397" target="_blank">📅 01:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9oSFotrmupLxBq4W-yTQGdTVGyoCbPzcK7IQyP1RgV9QQsmSsV9NnmYzUQtdKxhAdOR8CQs6W3MY_ICi-7ybQ-aHrtN-XNO22ynH8Hg-lP_9SusqpIksCYdaFW9v6BRilXegl2rAYt_rzJrOp5wB0_r7cWTCLjbFukN0C3j_SQEceGZrgxCyk1gleKQ2a_yg3ZF5bGbR0ejg2Mt-EZY9bxZu8nnIqdUbPQ6zmGFH3JVgBRbtcPilbvoB7XHhXeyR7RnKA8GQrxexqSqAAjuhWEUtyeg837fUxMsLU4nrsTsBm5SuNjtFT3RGQcpnN1Ng9C8ywDgczNW8uqlFJIUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1XxcdeOQRH9qIDPNT6_ku2uPOkCAnvjRznJ1CQJxwgXp5snoC54klexYL6V3vy27914g9OWxF9w40x6-EvajN2hO59wOTHZIEpopHOh5B97Hjm8DRDFCHapwUUSMK7LdhUsQjSrf0-ID0dgPdvCiEnsxCy1MTGgFaWP7SXw1BZWWWn9kNXtRe8DOgHVMTlk1MLRIZim7mtbSv6ZyMmbqORZnk9IqPxGIkTaEDd7SOJTGDCJf0RdYNUXhNjcLR6xjm4VfP_0H5Qt2qV0-vaGEIjRYhagjxCnBPUDQXO8xbp8GqQb7MW-pjiDkSXKOdM8AdsEx_as7-9s2a0NMpSpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYMg6VR9vbWph8hsK9SR5JxjF1TOtdf-c6u3J8nTrMnF40WY0q6JdYI9DvkHNjeNopIAwg00XNllfsVXCaelGkCakPvj-hbvNSe3boXBfj7DMel0YXV-LaZkJ4U_ArgxlcWt1OkC7V335cI_FC3ZZToKpogQYR1THwjHZRAaCh0JyxZpCniMrNNwDI1ig-V6tvXPEGQBxxev9rl6mg3cBAz-OhoZm7QCBfomPQOkjz78QE0gs6Qp7jRFk575HRGkjVna6gXNG7y4gKPmiXwn_CrndMKBX2I-UvR530Vw8Mw0NQjqVoh8cIsuvnlG5bcmBbobj3qgMqDPiJWso2gjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h96BJ_lAceVFipT6ZZHNT9JCViycfdxqg27bEb4nTYemyTQxHYcv9cjSuStNmW2O0D52uVLD2Z32W7e2wYUOund6bdvslehjptbubcoK7U2yhpFQY5ggb9Qn8riApNSFX-pGnnjZZTdPLRv_wM-nbh3rPBrTOk3d_8P8u5Ld0D3229Be0fqnxXZ6npyIiGSMHqKOJGYRIo1fldE3pOLbHe8ytJ_IO9AESCtOs0BqWpBtfsMnCAyic0PANSDAjD3GDFbGFt38YpuOfu-ZZq0BfQ5nLnZlo3FFPoC0ccFkJlrHj3TvNjCy3GGx0HL-EjvRYpF6jTJh0ZeyJnC9DS3mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTLER3esMPxI1zGdVnawc8u__-w4gvu__ocwieDUVHuqDxWicK8QqryG5EdfFSm525I4PxKDG7VteC4iHqOlyVaHh5-ZZLPzlXCEsdg00ollPSnjSdrvsQBwuPB_kTscx3xo87V909fETS1f5flnhRf7ho9Zmim4NqKtq0zNj4A8qceaFjHvDqd43ntRasYYMcYA5cY-eCwRH7r-76pm6E4eByfAujw_pozrW2Tp2ryGCxtpcygBm9zmSnYnOoqmsD1YkoP92Lk8QgLEA6emc90jSDjm2J9TaO2kJwewzo6HJjuRFox0iDuBcEhxX8h5EAS9bksvFFzaAEtvZaiXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZzJK3dHi5gGLq434qSr4bWNpr9ICj0-KVqYGMhApKwkjepQ1DbZ43DfPqybQLayqMyI7s8ADLaoqES_BUV1_OqKjlcPnr7rWOU-Qvj8fLHihgNVg6kBn_9YFdBJG8vfHQVHNKmydSIInUPuy44-rIs91RiSiTnU81qvjdMpctmb3yWoaPII5B5b2PSXmur4Rx5Op4Vmi3qxtcQwnMU1GWP8KTfAv0hDLyCm7z1SFyGCdQ5PJlfPkvyh976R4mowaGpUm17VfZ3z3z2PaeITe8T2B6w9UPHNBmQtRTd431gUVAdlnb-SuNuPYWTjMDwf9KaOzuIR5LdDHOCvIs8lqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/so3Ij_uI1HCnHqrhwqVx3jvJkOBwyLtuwQkgXZNlboc-EI4dJOrgZpiuYfflfXFyMRJcrnVsnXPc4mFmLkIY-oQUam00M-GwbePeyf-MrcMSs0D21qHmHxo0znptlR1xSP6PCBDk8BtBfligzYAxp_LzG9NQxwGIdQ8piVWoJOTaKFq6NqaH70z1bNIYlHMPCeSQKGqoxYBu7GsHOpu00W-q2-quc69d1z9mSI5M8ziuXnbzIuXjIJo_pf8VYgiR-BH4BGwR9DfIIUoYyhhdkWrOe1qU2s3dep4s3ZT4aIN4Q22-lfkOsuLaTXiPyaQH-YRIn_bHXBtKGGUJZscAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUr8tI9o1AAJzPy6kJefYZ9OD9GcA6poXXht7VK4u_unZuucmv6u3jh0Dxrk4CQALKwVZikbPBEzHVZWyIM0AwchHnZLnnKmJTvP_C-NcZw-kOdiFtfouU-EaWdmMf1oeuChb8hv9pEL-W9JP_D7IGVbd7idPuC0CdFkJ3IhjixVYqcsas73szwTBVfQvGeA-h9xn0gl-dGInTnja86rBPZPTi4ZKefe3s73nbI2HeHC5aKTghdY2vy91LjGes2RGGc6APkoEKTV58N3f7H6UldRVxzqvtqOv5CvJvmV-R9m9waNzUTmzkUacDx_pxmKPOG4QcRpCDWp9mr-_Ei9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stzPJy7sz-thA67ylDYZgCEkWhCmd8BpxSrm-MO6Ze9Kuy4AEc21cgoVdzdQUjsGdYLTc4GLbtYX8CYb4Cl3v8HEcm6a0DildxJ-Ia3P_w0gqNAzIWWmqse5HasyUGYhCtkv4jafEfPipWNDAE7ljJQnbdfEBiMiR9KJlDFPW--MW4SUiODwTUn7mP4lbTzV7YfCo9GTHeDHTP00xi4tdoeAKUBClHIBM5_FQZiVWKA_r--G8FdRKMpq68GB_WpWcH55DCSLPFvVZMvFxMzsfFLm8AOpOf8XaPGDFShONU5jKoV-6EhGYXhXxLpzNFL0vlxjbbLMMlw_BPGhL5nQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjvCsJiQlc6RbD1J0iLOPIvS2_fnGx1iw5RWRb4SSLZoFwuIADvUAVDZtiBxZrg9CT48DcbR0D5iQdC6mcsT1P4SobJ6mqMttz2RQzOuBXgCg9JDLGgvw4l6R6PMKRym9u7qciWwQ0eIguzEP0Z5z8fRf666piDa4hUwZQtkAMLfoVe-VUGfQ-50JyFiMB1fkZlkFUM_Iu3vRHMAC7QfD9R-wHxh1ycocePpcW6bxUB1IHpvNK-eIDCB2zZNQsi6AWtJsAvrZ2UijZA14T-2ChH37r9LQHBK2qApDJXmSM6fhA_nAq9vYPWuFj9Ab4Da7XzKro1EWNVJatzyyVk-cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزاداری هیئات مذهبی رشت در میدان شهرداری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/444387" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooTb1AZ_8zzdB2POyXXh3S54dC85b_UJT4YkxCWnsj2BJMfme6yd5WM54DOOU_F4pp0-cLEFHNmHrr7gfIALDF8f6Wl53Zs24DJ4grMbKpPVpUEPh4Dx5STqVQXS0-BLTozgH-Hx9FyhYXYCMtiipx87O5b5jhaH89hB3uSAaAkUcmGIaoymuU8m6aq9cch7BEDXpoB0OSrPk0gAHWnoi9us7vH0umqoW9uJKbTomYXssHz3AU8ZWD5nex4B7U7wC449_PhfbT8eM7yNq_luxk-SgQFLI6gO24gB5myi4wEKZFpgVBvBS_xqadokcEfu-3ERXyCVK8j2RsV6XkuhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم ملی فوتبال غنا با ثبت یک تساوی مقابل انگلیس به مرحلۀ بعدی جام‌جهانی صعود کرد‌.
انگلیس ۰ - ۰ غنا
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444386" target="_blank">📅 01:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
منابع خبری از حملۀ ساعاتی پیش رژیم صهیونیستی به اردوگاه آوارگان در جنوب، و نزدیکی یک مدرسه در شمال‌شرق غزه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/444385" target="_blank">📅 01:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4588151e87.mp4?token=ePMc3ZtKkF-fxF1ql9oFVYeNhkgEaxaNVnGeKevhkyMuUH5FYVWrtyf8Fn2b3hPabGzSMpWubK1sitPMK6t8gTaYSZpDvnX_m9vct92gQyjjgz3GrvEU0bf2NT4WwhbSW_Kx-0dQQQdcII8v3QcgNgp6HhOFRwGJfULrZmsdPcdsXjKg3wqY5WroE7rcAQIX2eIiSr07MUIsZ-gqhHWkJqEkjuLw-TfGXaO2xzXp5Vrw7h90z0gExViUHjfdqJ6qXbwoJ-jzeFFumo1H7s50OXeKuaE68OIVtR2-hNNgmuUPVc3hZgbuJgGuN0C5j5I6kLiwq3IfokFtwGrNtAsJQoZud9N4siZFDMUSqv2sPq2q8jEAwuNugVt8xBbbTgk0Hgy5MI3ypuo3q9LXvo68DkYnMHcFK-RMv7gselVUAjwmC9eVO9JiqP9bmASPjLYQ_yksHMRXDwBTEhqmMi1rgvOeznyHSVsBf2HwKQ0pAGA5gp9e8yfQ0toXqz0O2w0XtVq05NKLEeYpD4zC4k_7VzyKtKKuWJ0km2CV8For8vAZYv-srIMmtXWLYrR4Lv8SKTTYYR7kt1Axx57tckk2TJ4SwqSngevPCjvOmD_EdLU95u5nItMmCPA7_kruk1KsAK6ErQ4FKRDBdK4841o0e0HmaFMDxg1n34Z8-OojOX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4588151e87.mp4?token=ePMc3ZtKkF-fxF1ql9oFVYeNhkgEaxaNVnGeKevhkyMuUH5FYVWrtyf8Fn2b3hPabGzSMpWubK1sitPMK6t8gTaYSZpDvnX_m9vct92gQyjjgz3GrvEU0bf2NT4WwhbSW_Kx-0dQQQdcII8v3QcgNgp6HhOFRwGJfULrZmsdPcdsXjKg3wqY5WroE7rcAQIX2eIiSr07MUIsZ-gqhHWkJqEkjuLw-TfGXaO2xzXp5Vrw7h90z0gExViUHjfdqJ6qXbwoJ-jzeFFumo1H7s50OXeKuaE68OIVtR2-hNNgmuUPVc3hZgbuJgGuN0C5j5I6kLiwq3IfokFtwGrNtAsJQoZud9N4siZFDMUSqv2sPq2q8jEAwuNugVt8xBbbTgk0Hgy5MI3ypuo3q9LXvo68DkYnMHcFK-RMv7gselVUAjwmC9eVO9JiqP9bmASPjLYQ_yksHMRXDwBTEhqmMi1rgvOeznyHSVsBf2HwKQ0pAGA5gp9e8yfQ0toXqz0O2w0XtVq05NKLEeYpD4zC4k_7VzyKtKKuWJ0km2CV8For8vAZYv-srIMmtXWLYrR4Lv8SKTTYYR7kt1Axx57tckk2TJ4SwqSngevPCjvOmD_EdLU95u5nItMmCPA7_kruk1KsAK6ErQ4FKRDBdK4841o0e0HmaFMDxg1n34Z8-OojOX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زخمی که التیام نمی‌یابد
◾️
روضه‌خوانی میثم مطیعی در مراسم عزاداری شب تاسوعا در جوار محل شهادت رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/444384" target="_blank">📅 01:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de08a11e6.mp4?token=QrbbA88c8WfebfP6l96qfSgOo6uFr1IGUGPJVJg9wWolNldvBqKDKYE25__E83JqP3sDIIe9KpjYADdlDy6sSn48TXfqlLO_13sTwEsIL39IBm8CzKTkjppOweEaXNla_xfSX8RuFqVoDbDO0vtgBt-xbTVvS44hp_pNOhsCbi6y2waoCxog-DOPxbdP18xFpe76q14xxsrCQXy4zpI3eVg2i6ytJGLOrnv_j-4KbvKY3JELbBfTi_2EQnt6n7-P_7k0ejhNyMrpaA1rgMJOcVQgk8Aeua_sSwxNT2dk_zA2TAHZc-VZKAW-icI8w6Fn8_PdYEYkNNEMCelKlIoaNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de08a11e6.mp4?token=QrbbA88c8WfebfP6l96qfSgOo6uFr1IGUGPJVJg9wWolNldvBqKDKYE25__E83JqP3sDIIe9KpjYADdlDy6sSn48TXfqlLO_13sTwEsIL39IBm8CzKTkjppOweEaXNla_xfSX8RuFqVoDbDO0vtgBt-xbTVvS44hp_pNOhsCbi6y2waoCxog-DOPxbdP18xFpe76q14xxsrCQXy4zpI3eVg2i6ytJGLOrnv_j-4KbvKY3JELbBfTi_2EQnt6n7-P_7k0ejhNyMrpaA1rgMJOcVQgk8Aeua_sSwxNT2dk_zA2TAHZc-VZKAW-icI8w6Fn8_PdYEYkNNEMCelKlIoaNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاع خلیل‌زاده: اگر مقابل مصر نتیجه نگیریم فایده‌ای ندارد و مثل جام‌های جهانی قبلی باید برگردیم.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/444383" target="_blank">📅 00:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f59f08ba.mp4?token=mx9JbwLH7hSP6WBcxF4nBA9vutfjMonE0_G7aTXklcriIWf1EkbMWBg83336yhYD1G4vKjWyURlR1ENVguCbjalieSh44Re_E550QSeowWW6kkmVgSxdmY14bSAvzi9ZhDR3oGOphphejM6dRChCpr6JJbiq--Ypmf86VDdtp1QvSceEvUMsvCIjEWhkIli6Kn7-3iwV-y4ukJ5EqfFCahXznssYmapW-IpiaHN6FygtA3ULM13zJpg99bQo2hntBRV60y9zMrMRJLwD9YzyN25QR8vhr32eSP7T86Zrdn2Pr_0szsdjYu-u7pvmTctO2rkzh4TYIZmNDLxo_vaYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f59f08ba.mp4?token=mx9JbwLH7hSP6WBcxF4nBA9vutfjMonE0_G7aTXklcriIWf1EkbMWBg83336yhYD1G4vKjWyURlR1ENVguCbjalieSh44Re_E550QSeowWW6kkmVgSxdmY14bSAvzi9ZhDR3oGOphphejM6dRChCpr6JJbiq--Ypmf86VDdtp1QvSceEvUMsvCIjEWhkIli6Kn7-3iwV-y4ukJ5EqfFCahXznssYmapW-IpiaHN6FygtA3ULM13zJpg99bQo2hntBRV60y9zMrMRJLwD9YzyN25QR8vhr32eSP7T86Zrdn2Pr_0szsdjYu-u7pvmTctO2rkzh4TYIZmNDLxo_vaYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاع خلیل‌زاده: اگر مقابل مصر نتیجه نگیریم فایده‌ای ندارد و مثل جام‌های جهانی قبلی باید برگردیم.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/444382" target="_blank">📅 00:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI7tCHliy1aAg5qigi0w3qML34aUBOR2eYzBHPfjk8z8YT1m_ZDUxkOIgrJTZQYZk1h61i4eUFLPH48aSuPt_tUJEE1uf3QVfAozSRtDsnF8TVU9FAtaV0WFenaWrOu94_Sv_SwWA-Xkl9Intpdr7k2USeenbOSGL_6FEsBMXV5PQfVf8Y9ESoPurCPt3qeutZ6-O_GFSs_b3cKFjfQNpS7GujG2VKf54AAUITQGKEvHSeYM_UjWBHEIYNNBSRhZ4yRZTZsLF2DXDx1_DldZmM63Qw_7cf78OG-uSJlZ8SuU3nzhX5IYYHepIk5WZ4aaLdfAbiNcrKv2M4RvR6XT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد مشهد شد
🔹
رئیس‌جمهور دقایقی پیش همزمان با شب تاسوعای حسینی و پس از بازگشت از سفر رسمی به کشور پاکستان، وارد مشهد مقدس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/444381" target="_blank">📅 00:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAlzHYxOEWDXcMkLmpJVV4eBWqGmlFrrxZqXBBTd9cPCJGAkZzNtYmSls5xem-QrUICJp_cXwRso5DkvmmzBez_BPXgQ4AIUGKNS0M4tEFi7Ds9kOLCp5VbnZiiDx7iHaatNgXowMVUARq6K_n1YSwnkjUMqOnqngsrUaM2Zg_FcyuOAm7DHHMic8BNurPxGoc3CcFzsGHFzhQB7JlK6QQrkHa7XL053UnwhcvONmVDW7O8z9AQ9NETesyixqCm7OoI6Pi8SDgEuKs7BAtJbmIinqC6DjwCzdr61-sxQizGq5AsNEiQ2me2mDbCU0xxChjPnsVGMT6LZFxIChgUrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام مراکز اهدای خون تهران در تاسوعا و عاشورای حسینی فعال هستند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/444380" target="_blank">📅 00:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۹</div>
</div>
<a href="https://t.me/farsna/444379" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۸ – کتاب آه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444379" target="_blank">📅 00:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJYd0FmywUxDjy1kKj8zr51SW1hfQRFXQDfaqyJVjY8prdgJE1OUPQiR1g_BcXsDOxMNCduTTKlrYfboOdmriqiyNEyW_ihqKdfVoF5-BX7QVAoVpoCQHuXlg9Sq2psnCuiwCK8569nIc552pfZ6FfKlsuaMPODjwpU3WT5zfw_lhhqauPAWVXqVBI1xI2Y12GM1Di6BTxgePD5zV59or34z7flMjoHcqLKIzLL3bYcZS6wOx8vNXcepX6R7rreMFf5NqXrZ1oipGw3rlqUx8PGtIKErO5pjsilVqN7tsNuuY7XUqDqlADC1yyTdjgblivWk-a9pr65Kg1ZCYnBaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرق کار
🔹
روزی علی بن ابی‌حمزه در روزی بسیار گرم و سوزان، امام موسی کاظم(ع) را در مزرعه و زمین کشاورزی‌شان دید. امام در حال کار و تلاش سخت بودند؛ به‌طوری‌که از شدت گرما و فعالیت، تمام بدنشان خیس عرق شده بود و عرق از سر و رویشان می‌ریخت.
🔹
علی بن ابی‌حمزه با دیدن این صحنه جلو رفت و عرض کرد: «فدایت شوم، چرا خودتان را این‌طور به زحمت انداخته‌اید؟ پس مردان و کارگران شما کجا هستند که خودتان آستین بالا زده‌اید؟»
🔹
امام موسی کاظم(ع) در پاسخ به او فرمودند: «ای علی! کسانی که از من و پدرم بالاتر و بهتر بودند، با دست خودشان روی زمین کار می‌کردند و عرق می‌ریختند.»
🔹
علی بن ابی‌حمزه پرسید: «منظورتان چه کسانی است؟» امام فرمودند: «رسول خدا(ص)، امیرالمؤمنین علی(ع) و همه پدران و اجدادم. کار کردن با دست و کسب روزی حلال، سیره و روش پیامبران، فرستادگان الهی و بندگان صالح خداست.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/444378" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9803e13ea.mp4?token=dTfyrqAgosSPC38kB053v38xgJdtboIkpO_PRPj3LQCJVefVE8aNBm77pWUX4cX2Hg2-Pppxo0gx5BOqPFv46GgvD8_VDJLVxUYwPc5brz3N-Mjoi3n6VCJP6MWNFhCztHWpUmFdQdxM7rhH0-AFZ574XK3rV9-hmf1rg_am63uFF-I-8WdZiSV9GtfzygSHby0UYhPvtPmz7TTmC9p-6_rkCzuBdUMvC1LFIWz5ptwOu6JsiHyXkynJN8Nl9AEOC8JA6DNRgubJldMdhYdmhhKObbPEsTGNkr4zeMpNm1s8VoVU9Kl_ymLMKLIvR_b4ZIgnAjC808EHKQ0bT-leeiD1jkEWD7WBqJtlOXh07uGw2bUerOXLB9gNpcnmzqck3AMgOxIKiO9FWRbwCV-bvZPruzR-tDyFpt3a6glmMRSLrEcMEblWaglbhpc3Pd_0LLtGFm56t7TCp3PjDCqQU_j8MUTwyjp5ZUWqiy5ViID8iZwluvscPTGXRDgFnNdx0U2wPHp0R1Y9xXi4YKRAiIl29GdC3Mu0Zo53ks2IOKrnN1KNc6o6Sm7XQxiI8y0BLeJcdFW3KLNkHO_BBZxJ8AKFQzLOI0lJ3Wiquaki4db_Cqh37rwwVN3GQlWU51bhfRtO6L-l0AVxwmCOTSrtOp-q-ZeN0EAdd0CiGvVqG0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9803e13ea.mp4?token=dTfyrqAgosSPC38kB053v38xgJdtboIkpO_PRPj3LQCJVefVE8aNBm77pWUX4cX2Hg2-Pppxo0gx5BOqPFv46GgvD8_VDJLVxUYwPc5brz3N-Mjoi3n6VCJP6MWNFhCztHWpUmFdQdxM7rhH0-AFZ574XK3rV9-hmf1rg_am63uFF-I-8WdZiSV9GtfzygSHby0UYhPvtPmz7TTmC9p-6_rkCzuBdUMvC1LFIWz5ptwOu6JsiHyXkynJN8Nl9AEOC8JA6DNRgubJldMdhYdmhhKObbPEsTGNkr4zeMpNm1s8VoVU9Kl_ymLMKLIvR_b4ZIgnAjC808EHKQ0bT-leeiD1jkEWD7WBqJtlOXh07uGw2bUerOXLB9gNpcnmzqck3AMgOxIKiO9FWRbwCV-bvZPruzR-tDyFpt3a6glmMRSLrEcMEblWaglbhpc3Pd_0LLtGFm56t7TCp3PjDCqQU_j8MUTwyjp5ZUWqiy5ViID8iZwluvscPTGXRDgFnNdx0U2wPHp0R1Y9xXi4YKRAiIl29GdC3Mu0Zo53ks2IOKrnN1KNc6o6Sm7XQxiI8y0BLeJcdFW3KLNkHO_BBZxJ8AKFQzLOI0lJ3Wiquaki4db_Cqh37rwwVN3GQlWU51bhfRtO6L-l0AVxwmCOTSrtOp-q-ZeN0EAdd0CiGvVqG0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام سردار موسوی به خانواده شهیدان جعفری
🔹
این خانواده پیش‌تر با تأکید بر گذشت از حق خود، اعلام کرده بودند تنها خواستار گرفتن انتقام خون «رهبر شهید» هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444377" target="_blank">📅 23:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌ سنای آمریکا قطعنامه‌ای علیه جنگ با ایران تصویب کرد
🔹
سنای آمریکا قطعنامه‌ای را تصویب کرد که از ترامپ می‌خواهد عملیات علیه ایران را متوقف کند، مگر اینکه مجوز کنگره را دریافت کنند. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444376" target="_blank">📅 23:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444375">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e70b355a8.mp4?token=p-Yggdq3UIxaeprmTiSko43un4oAZMYvV16kMYA4FSQYsyJUUEWu0mgI4NbXpa6hu0YnyZCcwGX-kpinzJO2DfDwY_zeTNUNlutfZrE92zkBA9nrz2oJQazyj5bPUj8vk6AkB3rQib1BVxEKfrJ_hCEJYdJRHO3xwo48hiW8YGugPrVPpO2BayFBrqtDolY9cQnp5OlG2ONQp3DqBR2BnCumxomePqaIK2Bu5iwQtdcrD7rIeiAqEUjAvkIuWjlEzTj1XWdK4fQ4zk9bUf46D6OkO-94Wa5Lh6OVOoTxSPi2AtZtNSeFsINlxxAHgGlCZRKdiaoQzz8jDoo6BRkMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e70b355a8.mp4?token=p-Yggdq3UIxaeprmTiSko43un4oAZMYvV16kMYA4FSQYsyJUUEWu0mgI4NbXpa6hu0YnyZCcwGX-kpinzJO2DfDwY_zeTNUNlutfZrE92zkBA9nrz2oJQazyj5bPUj8vk6AkB3rQib1BVxEKfrJ_hCEJYdJRHO3xwo48hiW8YGugPrVPpO2BayFBrqtDolY9cQnp5OlG2ONQp3DqBR2BnCumxomePqaIK2Bu5iwQtdcrD7rIeiAqEUjAvkIuWjlEzTj1XWdK4fQ4zk9bUf46D6OkO-94Wa5Lh6OVOoTxSPi2AtZtNSeFsINlxxAHgGlCZRKdiaoQzz8jDoo6BRkMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان جمهوری یاسوج غرق در سوگ علمدار کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444375" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444374">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJwaaMSeMmrj0hTayKb5ODREcJEGhsxgBkAHq1Jb7ZaZPCgbVn9CZ98cJkAwgYDeSaqO1O3NGlVvt1Hc_s6Wm2IL7wMLgb3nhitgN4gATskFdndUQvpURJlYw1JlyoZwkx6tmEyc5GyJh07b4HA_iULtkL0BlgMT47tt1Z5_ZRKu-opOAUvN6qvpYfth4uefqeLPVhL7PWsFrbNkbkOXiHemNHqWEC19N2tvjtQs79eT4sCaIavvdbCS7-f2lVOWiMlrHdNo51lGb8gLZPJEMBwusJrPeoHr_-RSvk14lEwGIbQq6RB3uaHLEjnTnfKVDFpGA2o4BPoT6jG9JeNxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری اسکن ۶۰ ثانیه‌ای بدن جای ام‌آرآی را می‌گیرد؟
🔹
شرکت میدجرنی از یک فناوری اسکن تمام‌بدن اولتراسونیک رونمایی کرده که می‌تواند در حدود ۶۰ ثانیه تصویری سه‌بعدی از داخل بدن تولید کند.
🔹
این سیستم با عبور بدن از حلقه‌ای از حسگرها، تصویری سه‌بعدی از اندام‌ها، عضلات و استخوان‌ها تولید و سپس پردازش می‌کند تا نقشه‌ای از وضعیت داخلی بدن ساخته شود.
🔹
با این حال، متخصصان هشدار داده‌اند که این فناوری هنوز جایگزین روش‌هایی مانند ام‌آر‌آی یا سی‌تی‌اسکن نیست و ممکن است در مرحله تشخیص، خطا یا تفسیر اشتباه ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444374" target="_blank">📅 23:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd0156436.mp4?token=Tg3qsrm--Tx8xjUjBgJL7DSySvM-XSuFhYL65TuyUVFdO1CDVmbgrT7YMcO9PSC3MDJo575i7bdLn5FCC2-f5N5nH-COaCgMW1PtzKlCNFxMUc68sFS4viRzqyTAsWVnqG9Hgs2yLzmdOu-LFpLlnjBJE0yCtqxFO3txtGZ_MBsVIaN4LKB9FlBwYQk1lKRxBCYhoxvOiX724izniVklbJ9Gs3fEH4oKYFd_vNHlvHui9heg1ZmgLVA07SPoDZxMRH3l5SQGdVzxRGtR8JiQ54HodVxgTmxNkTKq_0wvqvQjWSVoRGA84-7N4FBm9Ehv_LNPas7eiCRqdo5phB9-Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd0156436.mp4?token=Tg3qsrm--Tx8xjUjBgJL7DSySvM-XSuFhYL65TuyUVFdO1CDVmbgrT7YMcO9PSC3MDJo575i7bdLn5FCC2-f5N5nH-COaCgMW1PtzKlCNFxMUc68sFS4viRzqyTAsWVnqG9Hgs2yLzmdOu-LFpLlnjBJE0yCtqxFO3txtGZ_MBsVIaN4LKB9FlBwYQk1lKRxBCYhoxvOiX724izniVklbJ9Gs3fEH4oKYFd_vNHlvHui9heg1ZmgLVA07SPoDZxMRH3l5SQGdVzxRGtR8JiQ54HodVxgTmxNkTKq_0wvqvQjWSVoRGA84-7N4FBm9Ehv_LNPas7eiCRqdo5phB9-Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی شب تاسوعا در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444373" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
