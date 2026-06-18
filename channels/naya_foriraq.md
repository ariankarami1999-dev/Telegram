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
<img src="https://cdn4.telesco.pe/file/NR1vxTSY2mIJ4gsEyvk5cFoUPwdBiSGR-bDJNfzw7BNengGlMhyp5mZJKB404PgwImPHiefJf3mJVT5pHMaka9m4y2t8k6BdjAo_BZAdd_b5aMJEuE6SfZFRiUbzjKB8T0OZGs-QuT5UFO4Wdxlr3j6ZFkSLRDQr2GBYZwQktMYRmH4cRX9dG8pKcHB-gO8FaK5MV-PFrmOymgYXY9gAdaFlEpqU147eiWSFlahWoa2mp8PIwzguZAV8FpWWy1_MOKmycPO4SkqhdsQZ_eMlyQiA06144vyYvC8E82NEwUvMDMROen6B6umhC9-Pfbyz7StVb2RLfhrkpvqtHa59Bw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 01:58:36</div>
<hr>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
وزارة النفط العراقية:
- الحقول النفطية جاهزة لاستئناف عمليات الاستخراج
- العودة إلى الوضع الطبيعي ستتم بشكل متزايد حتى بلوغ معدلات الإنتاج السابقة
(سومو) تواصلت مع جميع الزبائن لترشيح الناقلات المؤجرة والمملوكة من قبلهم لتحميل الكميات التعاقدية  من النفط الخام العراقي عبر الموانىء الجنوبية
- ستكون عودة الصادرات بشكل تدريجي استناداً إلى انسيابية مرورها عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/naya_foriraq/79242" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0819644274.mp4?token=IVkUZMfJUJP6am4UvnZ8fep5ksMwI9A2tGIIPQfu82XN2XgqMVgnphEfpN2u8APFbd_60JGxcJ7AoRyx-pCCBiEKLn40FV0sY0_3sZA1QIOs3PIU1nB3kXBoUJ-R8FLmy50Zh_1aS8-ukTFFGuSCdQc94-ZHoVOVcqmh6j35jZBuHLFmBeJyaTq_EPEyWnoszNJAb6O-vu1rBzPgQY3MxqUMPu6Wh4j_VRJvvcNb6tGuazEaD2oPzNbX5KpiJm8NBASTh0Fl-xYiHS3gDIti2T3jjVB9SaF_mcD_1OCnholyUJcQVu_SDC0uSOIK50Ap32dKJDOvEUKRQ-jYcHgewA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0819644274.mp4?token=IVkUZMfJUJP6am4UvnZ8fep5ksMwI9A2tGIIPQfu82XN2XgqMVgnphEfpN2u8APFbd_60JGxcJ7AoRyx-pCCBiEKLn40FV0sY0_3sZA1QIOs3PIU1nB3kXBoUJ-R8FLmy50Zh_1aS8-ukTFFGuSCdQc94-ZHoVOVcqmh6j35jZBuHLFmBeJyaTq_EPEyWnoszNJAb6O-vu1rBzPgQY3MxqUMPu6Wh4j_VRJvvcNb6tGuazEaD2oPzNbX5KpiJm8NBASTh0Fl-xYiHS3gDIti2T3jjVB9SaF_mcD_1OCnholyUJcQVu_SDC0uSOIK50Ap32dKJDOvEUKRQ-jYcHgewA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب
:كنت أرغب في منح نفسي وسام الشرف من الكونغرس، لكن قيل لي إن ذلك غير ممكن
😫</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/79241" target="_blank">📅 00:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154f345198.mp4?token=RsD0oHAQmCAnqVCqkvaO1-oawEZ7Cxmx02WOWLgViuiQmcplOSD76G2tYV7n2MVss_xaFOD7q56t_8da1eLnmr92mDrgyxQhNpRoPCFL7UDEnvZgIXEg87xsJ5gfFeobe2k6C7Z_tGF8w05xGc0PlIVRuMSJgDyvbO22MfA73HRjYq2J1qeJKdKv26lDuKZsuPMZ2ivS-xxVN9bh9iorCEaszd_WUoS_CTaK6d-jKOgUhi1q59T3MafGxKHcfLedAz24Xfh3Lqvk79HqTQfE3plSWYtd8plhFY761yGs4dhbKLZUDFBvYESUBEZK5oZKdsKuX9kVk0_shQsl8eeLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154f345198.mp4?token=RsD0oHAQmCAnqVCqkvaO1-oawEZ7Cxmx02WOWLgViuiQmcplOSD76G2tYV7n2MVss_xaFOD7q56t_8da1eLnmr92mDrgyxQhNpRoPCFL7UDEnvZgIXEg87xsJ5gfFeobe2k6C7Z_tGF8w05xGc0PlIVRuMSJgDyvbO22MfA73HRjYq2J1qeJKdKv26lDuKZsuPMZ2ivS-xxVN9bh9iorCEaszd_WUoS_CTaK6d-jKOgUhi1q59T3MafGxKHcfLedAz24Xfh3Lqvk79HqTQfE3plSWYtd8plhFY761yGs4dhbKLZUDFBvYESUBEZK5oZKdsKuX9kVk0_shQsl8eeLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
استنفار أمني واسع في نيويورك لاحتواء الموقف وطمأنة السياح القادمين من مختلف دول العالم.</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/79240" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79239">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGPIa6FJFpaflg5Yg-zo7H-04Zi6fAQG0itVwxnnoC9SuER-fkTK7u4OttP_kLC2Zp1Nkyi0z4w3BQNe2AEaPKHOSxSXlektmWqBehmLJEqQW8eiYAOcRVU-XUZTodvfPGYQQSatiTAUuFBGRUELgGYe9eE5JdEeHdrNGzGS_eG79WkspUP-XhLhDAWWl4OdWSLZFeN_zh04ylSad3bUTfvPG7Kk-tT_G9sJcd0_QPEVdJpYyfpDtLoHMS3znN94VA_y0q0emYZ0Qad2N0PE5O3C2pNJLK4oVhH2WW-VUJHjkphD9d32uZY_QgL_AkhO21f728DecQj1CMm3n7Scow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مشاهد أخرى لفرّ وهروب المدنيين في الشوارع إثر اشتباكات مسلحة عنيفة أثارت حالة من الهلع والخوف بين السكان والزوار</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/79239" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79238">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=TP3W7UqsmmU3xhS46CqAlUBiU67Oo6AyBQULxdWoUbg4VnNSE9jWu84O6IhQVV3_NHs5WROyfK2ykAjrua2NDjqgIijhIY57IIGJ_ChlPdi6W3BgNzMf20C9PSBJzGWpqDhXoKWq2lisdVzStl1qiTuy8d7eOmSD4v_AYUD8G_TNE4CNmtF53upR5g0Ux4yQsFqWFdnoex_eT6ciLeAwNljeTaXVl7I5PIE0MXbYwCMuT9itluneAX7GZ2-06jVQSDMnN5lEfGu1aoNrfWcU_VgLgQt8UMa1eu-YbU1o4rQun0zDvrIkWMM7A-tALdsmKRSJJ9c9Pt2BQZtrHKEiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=TP3W7UqsmmU3xhS46CqAlUBiU67Oo6AyBQULxdWoUbg4VnNSE9jWu84O6IhQVV3_NHs5WROyfK2ykAjrua2NDjqgIijhIY57IIGJ_ChlPdi6W3BgNzMf20C9PSBJzGWpqDhXoKWq2lisdVzStl1qiTuy8d7eOmSD4v_AYUD8G_TNE4CNmtF53upR5g0Ux4yQsFqWFdnoex_eT6ciLeAwNljeTaXVl7I5PIE0MXbYwCMuT9itluneAX7GZ2-06jVQSDMnN5lEfGu1aoNrfWcU_VgLgQt8UMa1eu-YbU1o4rQun0zDvrIkWMM7A-tALdsmKRSJJ9c9Pt2BQZtrHKEiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الذعر بين السياح القادمين إلى الولايات المتحدة لمتابعة مباريات كأس العالم، عقب اندلاع اشتباكات عنيفة أسفرت عن وقوع عدد من الإصابات والوفيات.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/79238" target="_blank">📅 00:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79237">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=kc6ub-iq27FwuyvuEJNt_DZkwqFgvNUKBPsc6O6NcXN7he7Af6UupaZ6OWEVQI7BRt3_C6k-556sdv1IIR8y0csoP7XGWSVBo0X0TqjL4p8G8iTJlhrPL_keeNNyGklKVxJdk8eVryzXy_Mrd4iIJ3eEMnXoXBOpLJc7Vx7F6MSl3KwRCR-drUBDwWIoJ3_aiSaagJZjiyIRSYxZvvc-5fNOwb79-ocwDbvX6_X64KxTBlK1gMMG2CzDLi_fxETDCVQw8ulI_Fw0ISGieCy3EgIpAEdcjlyf6fz3HZ0jvBTOGgpKyx7zM4ijCZrGCO6NmJyvwpWrMuuUtGxiQOo9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=kc6ub-iq27FwuyvuEJNt_DZkwqFgvNUKBPsc6O6NcXN7he7Af6UupaZ6OWEVQI7BRt3_C6k-556sdv1IIR8y0csoP7XGWSVBo0X0TqjL4p8G8iTJlhrPL_keeNNyGklKVxJdk8eVryzXy_Mrd4iIJ3eEMnXoXBOpLJc7Vx7F6MSl3KwRCR-drUBDwWIoJ3_aiSaagJZjiyIRSYxZvvc-5fNOwb79-ocwDbvX6_X64KxTBlK1gMMG2CzDLi_fxETDCVQw8ulI_Fw0ISGieCy3EgIpAEdcjlyf6fz3HZ0jvBTOGgpKyx7zM4ijCZrGCO6NmJyvwpWrMuuUtGxiQOo9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/79237" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79236">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/79236" target="_blank">📅 00:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081d58322.mp4?token=QWM8I55DZ1O3WkYYVuQUMO0pOzZ2AVGRuQiAedzW-p-mO4OKkqtYCt2e1qaIvGij98CcthjXlGDXWuopt9VtLH9bNjYeD3EYZbNvSFS0_obvnQWqHVXGcRbF0_Up4xe69c4QITAUVuclTeCDk4zxq0hVqD7pFhp21PSG2KE2W1DrSk9O0E8eb97-Eo4HU1Bjp_I-Ws-j9AgZELVKV843VMJ5d8rvdxq8ojya9vp6aVFAwQunqsRGJoNll4LCex3TQkIhhFz252G3rOneZnUgS9BLiARj1bllOhlWTzMvO3J_v9jt8ZsEuBisDuxeZ3vCMizEqjMdDhwV7gxmW37pig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081d58322.mp4?token=QWM8I55DZ1O3WkYYVuQUMO0pOzZ2AVGRuQiAedzW-p-mO4OKkqtYCt2e1qaIvGij98CcthjXlGDXWuopt9VtLH9bNjYeD3EYZbNvSFS0_obvnQWqHVXGcRbF0_Up4xe69c4QITAUVuclTeCDk4zxq0hVqD7pFhp21PSG2KE2W1DrSk9O0E8eb97-Eo4HU1Bjp_I-Ws-j9AgZELVKV843VMJ5d8rvdxq8ojya9vp6aVFAwQunqsRGJoNll4LCex3TQkIhhFz252G3rOneZnUgS9BLiARj1bllOhlWTzMvO3J_v9jt8ZsEuBisDuxeZ3vCMizEqjMdDhwV7gxmW37pig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
قصف صاروخي مجهول يستهدف مواقع لعصابات الجولاني في بلدة الهول بمحافظة الحسكة السورية الملاصقة للعراق</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/79234" target="_blank">📅 23:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇫🇷
إعلام الفرنسي:
تشكيلة منتخب فرنسا أمام العراق {فجر الثلاثاء} ستشهد بحد أقصى تغييرين أو ثلاثة في اللاعبين من أجل حسم التأهل للدور المقبل.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79233" target="_blank">📅 22:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سوالف الگهوة
لقاء بعد قليل بين العامري والمالكي لحسم منصب وزير الداخلية … وباقي المقاعد …</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79232" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇫🇷
‏
ماكرون
: الكثير من علامات الاستفهام بشأن الاتفاق..  ولا أعتقد أن الحرب انتهت</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79231" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6ZVRUkaUWklN4sxsk00fYRK5hIFW6JuRFq1-bI4xJpAS4MkwvOrRxcpQM1k5PtcVByRLofZwaIiw6sA-JxzVbIXqeZWJViZJh2BqlEwQHFgqQbinyIi77nHUAYt7dUadWv1k6rwz0SRHUnULLdtYDK9wy005KeUrD9jx_NecZKkRGiSGkQq2sLnKR8TOwmEo6wX8kMDFDLfExOHDTs4wvv5Fqi4x7o1nknxBIniAnX0mdNc8uTUulBD2B6wmMxfu34iKSkfNtNqu0vKzd-dG-AHksjBBnHwN42oRSvarsZfZujLoPs0ZuDmWW8w-oXH_-YfZ6j6b3-VF70YIT-A9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تلتزم الولايات المتحدة بالسلام، ونشجع الجميع في منطقة الشرق الأوسط على الحفاظ على التزامهم بالسماح لمفاوضاتنا بالتطور بشكل جيد. الأسواق سعيدة بما يحدث مع انخفاض أسعار النفط بشكل كبير، وارتفاع الأسهم بشكل كبير. نتوقع وقفًا كاملاً لإطلاق النار على جميع الجبهات، بما في ذلك لبنان وحزب الله وإسرائيل. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79230" target="_blank">📅 21:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=rBKtPsEA6H06110ydGrL4gzWdrsDWTS2QhyiCANCkUd5eA5TuXxAkc07NQD4vjJfIzRrThZDPsMMupom6Rp1kcp9BeTvafSyu8JN6KTLBk_da_4hSLQakAyL3GWff8R03M_kNRMwuHX4O7bBquzHY0bbpzSagLrK9TkZKiJ4gyIn34OB_ygVQC22slfwAb8CO15TVgFf0xnkHCHDKGheg903iv1WyJisp998C6iLBf0ZBaq1Ug9B69iDGrb6pVo8Ujqe0XxjuzIu5XvusvBCi2sxTYqDhLp5Vg2R-iKzocq98yE4x0ZSVOsiRv34fsUY5C-UyHnJqwv0sR5TZSYmC3M9LfFKjwvQlPjElY3oLjDTBR-1EaG3kYIP__OXrNj95MopzR3CzvIaiLsojGBsAP_sqKqKpPGR_jsN_LI6Ut6zGKdpK9kIYePX7-fxBR5GbzMbjWFZLEP2d9kQcvo_shLb7Oc8Ix6ATxVBgFvcksLv9bmS9AMhSG9rrY-NHrls3rANhrX-_xaVf-xOPVBCbdgABtjv457B6cnINClySU95RhrPBHA5ConTlOyUJS9wFUtPBu4V7Nosujn1OW938QGeN7Jj6AVAr7iuJLY21hi4OWCyR8gGVMskFPLIW6_oDvDZPjDklapPN8W_s6Eefs2b1J_tAS4h7CtR97dqb1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=rBKtPsEA6H06110ydGrL4gzWdrsDWTS2QhyiCANCkUd5eA5TuXxAkc07NQD4vjJfIzRrThZDPsMMupom6Rp1kcp9BeTvafSyu8JN6KTLBk_da_4hSLQakAyL3GWff8R03M_kNRMwuHX4O7bBquzHY0bbpzSagLrK9TkZKiJ4gyIn34OB_ygVQC22slfwAb8CO15TVgFf0xnkHCHDKGheg903iv1WyJisp998C6iLBf0ZBaq1Ug9B69iDGrb6pVo8Ujqe0XxjuzIu5XvusvBCi2sxTYqDhLp5Vg2R-iKzocq98yE4x0ZSVOsiRv34fsUY5C-UyHnJqwv0sR5TZSYmC3M9LfFKjwvQlPjElY3oLjDTBR-1EaG3kYIP__OXrNj95MopzR3CzvIaiLsojGBsAP_sqKqKpPGR_jsN_LI6Ut6zGKdpK9kIYePX7-fxBR5GbzMbjWFZLEP2d9kQcvo_shLb7Oc8Ix6ATxVBgFvcksLv9bmS9AMhSG9rrY-NHrls3rANhrX-_xaVf-xOPVBCbdgABtjv457B6cnINClySU95RhrPBHA5ConTlOyUJS9wFUtPBu4V7Nosujn1OW938QGeN7Jj6AVAr7iuJLY21hi4OWCyR8gGVMskFPLIW6_oDvDZPjDklapPN8W_s6Eefs2b1J_tAS4h7CtR97dqb1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79229" target="_blank">📅 21:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">رسالة_قائد_الثورة_الإسلاميّة_الموجّهة_إلى_الشعب_الإيراني_بشأن_مذكّرة.pdf</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/naya_foriraq/79228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رسالة قائد الثورة الإسلاميّة الموجّهة إلى الشعب الإيراني بشأن مذكّرة التفاهم بين رئيسي جمهورية إيران الإسلامية وأمريكا
بسم الله الرحمن الرحيم
أيّها الشعب الإيراني الغيور والوفي،
💬
كما علمتم، فقد جرى توقيع مذكّرة تفاهم بين رئيسي إيران وأمريكا. وفي مسار الوصول إلى هذه المرحلة، بذل المسؤولون المعنيون جهوداً حثيثة دافعُها الحرص وحسن النية، وإن كان الرئيس الأمريكي هو من لجأ إلى شتى أنواع أوراق الضغط، انطلاقاً من حالة العجز لإنجاز هذا الأمر.
💬
كان لي رأيٌ آخرُ بطبيعة الحال، غير أنني أصدرتُ الإذن بذلك من منطلق الالتزام الذي قطعه رئيس الجمهورية الموقّر بوصفه رئيساً للمجلس الأعلى للأمن القومي، نيابةً عن نفسه وسائر الأعضاء، بصون حقوق الشعب الإيراني وجبهة المقاومة، وإعلانه الصريح تحمُّل المسؤولية، حسبما صرّح جنابه، بأنهم لن يرضخوا للطرف الأمريكي إذا ما أراد فرض إملاءات توسُّعية أو المطالبة بالمزيد. ومن هذه اللحظة، سنكون نحن - أي أنتم، أيها الشعب الشامخ، وهذا الخادم الصغير - بانتظار تحقق الشروط المذكورة، بيد أنه من البديهي أن المفاوضات المباشرة التي ستنعقد في المستقبل، لن تعني بحالٍ من الأحوال الإذعان لرأي العدوّ. كلّنا أمل في أن تحفّ دعوات مولانا (عجّل الله تعالى فرجه الشريف) شعب إيران الأبيّ بشتى صنوف النصر والفتوحات.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79228" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
المركزية الأمريكية: رفعت القوات الأمريكية اليوم الحصار المفروض على جميع الملاحة البحرية الداخلة إلى الموانئ والمناطق الساحلية الإيرانية والخارجة منه
🇺🇸
الخزانة الأمريكية: ‏عقوبات أميركية على 3 أفراد و5 كيانات مرتبطة بحزب الله من عدة جنسيات "سوريا عمان العراق لبنان" وأحد الشخصيات سليمان فرنجية ومحمود قماطي.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79227" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
‏الخارجية الإيرانية: تخفيف المواد المخصبة مطروح الآن كخيار لكي نغلق الطريق أمام الخيارات الأخرى نقل المواد النووية المخصبة إلى خارج البلاد خيار غير مقبول لنا</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79226" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📰
رويترز: البيت الأبيض قدم نص مذكرة التفاهم بين الولايات المتحدة وإيران للكونغرس</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79225" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مصادر إعلامية: معلومات عن وصول أعضاء من الوفد الاميركي الى مقر المفاوضات في منتجع بورغنشتوك بسويسرا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79224" target="_blank">📅 19:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888b5dbc65.mp4?token=hJG4yH3mQV8mU4LSlltVQmGc2CnH9MR_7g80QkWJ6zEwo2uq_DUCFbZej7cC-O-Wm2ZM7ANzy1ISh1v0eWkkT4e6plAiSCh3a3Gyi7BK57sspHQNUBJcDcwyrc_6E-B46LtC81Le7Wa1EhUfIyyizBHBdmOHpDyMiCl2ezZ88PAO_sQ43WAAIz8hTK-gDFYuSBzbp1luQXDRAKyvvEZiJpKZUCXOmSiR-bnf8JC_Ot4Y04CYHuDrfYENdAVyn_VRXqAUSt3LCqedWgBcY4kV3G8CXRmeRxrhqHOxX3ud3GVlOmFXbqKtIlwqpksa8fNWhgLliAiVtXbjUvi9YDs5Kp-e3GI8kHTRl6Zqvt02UZgMzmFLL2_3PGq6IRZDmM2oZ4BjRzlifNYYnuAG6jMcsN5JAbj79bSxuUUmmcZ8ZI0nYNHCoIKCUoYogpc6wrWamgCtby7z3q4zjYmrfMZL_POig7zQjYr0uD3yUElyEAZwHXE4XfIBUtOZKbiJd4UGhO2RxeXQldd2SwnCx0D8trN8-lE8hwTiL87rYhwYRvbEC6K-Zx2KeJWsRSAPpNMn0N094MvIZ5wmSubi7e8g1u8jNenhgiZhZc5xz0Kh4QzcVlLi01-QUo2oDTsN47gW5n__ezGLYzjtW4j2LFV15VLUonkqGhuwe4Cp9garAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888b5dbc65.mp4?token=hJG4yH3mQV8mU4LSlltVQmGc2CnH9MR_7g80QkWJ6zEwo2uq_DUCFbZej7cC-O-Wm2ZM7ANzy1ISh1v0eWkkT4e6plAiSCh3a3Gyi7BK57sspHQNUBJcDcwyrc_6E-B46LtC81Le7Wa1EhUfIyyizBHBdmOHpDyMiCl2ezZ88PAO_sQ43WAAIz8hTK-gDFYuSBzbp1luQXDRAKyvvEZiJpKZUCXOmSiR-bnf8JC_Ot4Y04CYHuDrfYENdAVyn_VRXqAUSt3LCqedWgBcY4kV3G8CXRmeRxrhqHOxX3ud3GVlOmFXbqKtIlwqpksa8fNWhgLliAiVtXbjUvi9YDs5Kp-e3GI8kHTRl6Zqvt02UZgMzmFLL2_3PGq6IRZDmM2oZ4BjRzlifNYYnuAG6jMcsN5JAbj79bSxuUUmmcZ8ZI0nYNHCoIKCUoYogpc6wrWamgCtby7z3q4zjYmrfMZL_POig7zQjYr0uD3yUElyEAZwHXE4XfIBUtOZKbiJd4UGhO2RxeXQldd2SwnCx0D8trN8-lE8hwTiL87rYhwYRvbEC6K-Zx2KeJWsRSAPpNMn0N094MvIZ5wmSubi7e8g1u8jNenhgiZhZc5xz0Kh4QzcVlLi01-QUo2oDTsN47gW5n__ezGLYzjtW4j2LFV15VLUonkqGhuwe4Cp9garAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جي دي ‏فانس:  سمحت اتفاقية أوباما النووية بالتخصيب، أما اتفاقيتنا فلن تسمح بذلك. منحتهم اتفاقية أوباما مليار دولار من المال الأمريكي، بينما لا تمنحهم هذه الاتفاقية أي دولار من المال الأمريكي.  ‏لنفترض جدلاً - لنفترض بعد عامين أنهم فعلوا ما نحتاج إلى رؤيته…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79223" target="_blank">📅 19:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
محكمة جنايات الكرخ تصدر حكماً بالحبس لمدة سنة بحق مشعان الجبوري بناءً على شكوى تقدم بها محمد الحلبوسي بتهمة التهديد بالقتل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79222" target="_blank">📅 19:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
جي دي فانس: نشعر بثقة تامة بأننا نستطيع رفع تلك العقوبات مؤقتاً دون اللجوء إلى الكونغرس وطلب موافقته.  لم تكن العقوبات هي العائق الرئيسي أمام النفط الإيراني. لم نعتبر ذلك تنازلاً كبيراً للإيرانيين.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79221" target="_blank">📅 19:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b349c3eaa.mp4?token=Szq3QtRwLA8kKTecE6HF0C-whdtM8LKzfiuZloaeKcpDWV7BTcuvf3FrHM4xv0sniVTZ76J9IqGohqnlONt4hZWIbCNaYvvUy_Q2r98GQrMMQaMO5yXQ7SvaXLj0jKTrJF5q8RfqmWeHmSnOC0MhX4s7yUqwK_KYvfeUOBxPwrBKySaPPwS2Wi6ffTWwi_hcdYHKQ-wu6deWLQan-8EjaUczJ5UMVz-zlXavRRfbVRxrY9uMItb_Q-So-sLVAnsftlfMob65-JHHkW70CxQwVVDHg3Blazu_auu9KgE6MMhCOp6QQutCxa7F4w2-KE-231Dl7nZ-uarz7FQIyv44yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b349c3eaa.mp4?token=Szq3QtRwLA8kKTecE6HF0C-whdtM8LKzfiuZloaeKcpDWV7BTcuvf3FrHM4xv0sniVTZ76J9IqGohqnlONt4hZWIbCNaYvvUy_Q2r98GQrMMQaMO5yXQ7SvaXLj0jKTrJF5q8RfqmWeHmSnOC0MhX4s7yUqwK_KYvfeUOBxPwrBKySaPPwS2Wi6ffTWwi_hcdYHKQ-wu6deWLQan-8EjaUczJ5UMVz-zlXavRRfbVRxrY9uMItb_Q-So-sLVAnsftlfMob65-JHHkW70CxQwVVDHg3Blazu_auu9KgE6MMhCOp6QQutCxa7F4w2-KE-231Dl7nZ-uarz7FQIyv44yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تفعيل الدفاعات الجوية في سماء المطلة شمال الكيان المحتل جراء رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79220" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79219">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7e219b34.mp4?token=duN-k0pwxWA0zHs5uyj5W2eoa6DjLTZGE7RxPxHMkT_7lH2wXI4OePBplcnt9VFHyZR1RPyjGdfdPoCw0sSZLrtjfsexV9Xkso-OUv4fh_jaeAlLA1i4YWKh_Derg_p7XCNJraP3hg0akOJiOv49IdbHGMdZC558drtW75TEklTl2gc0-e6oSY7VApXXb7GY5J45k_x5s-IgZBgU7DRp0OCKTuNW5pRMYgVLZ9GFPUsEEVxsl1fol2Mq--3RlsJwhMDgvjjjArdD92vUPyHrleGed6ClzEwNrD91tG_0Qn6W-RnNxG1XINfo8h2u4MMbvSjH8VnJY0tVXu9PdChqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7e219b34.mp4?token=duN-k0pwxWA0zHs5uyj5W2eoa6DjLTZGE7RxPxHMkT_7lH2wXI4OePBplcnt9VFHyZR1RPyjGdfdPoCw0sSZLrtjfsexV9Xkso-OUv4fh_jaeAlLA1i4YWKh_Derg_p7XCNJraP3hg0akOJiOv49IdbHGMdZC558drtW75TEklTl2gc0-e6oSY7VApXXb7GY5J45k_x5s-IgZBgU7DRp0OCKTuNW5pRMYgVLZ9GFPUsEEVxsl1fol2Mq--3RlsJwhMDgvjjjArdD92vUPyHrleGed6ClzEwNrD91tG_0Qn6W-RnNxG1XINfo8h2u4MMbvSjH8VnJY0tVXu9PdChqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جي دي فانس ملوحاً عن برنامج إيران الصاروخي: لإيران حق في الدفاع عن النفس وحقها في امتلاك صواريخ باليستية، قائلاً: "إسرائيل لا تتخلى عن حقها في الدفاع عن النفس إذا أطلق حزب الله صواريخ أو طائرات مسيرة على إسرائيل. والإيرانيون لا يتخلون عن حقهم في الدفاع عن…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/79219" target="_blank">📅 19:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79214">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeDfitnWp9GuEryhlA7d3oTfciHQl6rxjeAdIITNuTn6AEF5aB5LVJ4qBJP6-ueMeEwKc-UHo2LOTagHhUCUexysANqNUQ44ffNSjdOnJ1j_qEB5S4sH4mONLcRAvv8Ad1kTQ1KrVoAyskQcvoV40_iflATfnZN3Wml5p2cDPyvTjTJXNTCi-M7Wwtrv3WNgWXbF305kaTlHs0K_srGfSUMKQZhubQpvkBxNJtMupYll-qVLR5l-Y0h0xgheyXRXbli252Ho-mUxWu-AqJxc4zR9medCy-BZiIRepWc9UQXy6k-KHBzG9bOVciPsYtJelRFS_TwrinFVLN8fIJhAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBL4QfPdS_maKZ8P1mgHfacnRezzoYVKdolI3nMpWnNSLt_ImRdSi3lnwHZ1-uTKrxt5LnLwPWZHV7O0sbDaf0tS9kXfLp4p2CgG-1fYzJZwl-ignAocnV5vKchIlLlEe2Be6KCyRyJV4cwUF7OpQ35qs_blufo1HhK0k7WZadE1SeBngLBZU0PDEGeS2Er3ETREKnETogS2uYdyi4gPm96R0AQlQ0kgPXAvHpTIT6bou9nirBfoj7dGG0Au419_NZ-tyP-IRHqF1X0aqDLUktVzvmEDfmpVR3I_i-puhd5k1-_TTJShMAx8b5RGhF01YOwmcRZrPc2V5A5Oo0jl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGHc84lPTDvFAZ9gagavuuIJJz9pNm6-A7ox_WbdoVXJiPBOHiZ57Bzd2kDLiibiMIVuDUZyMTGH0VzsRmbPU4fmQQZr20gGERCO7lssjUbxnjD494Lsg1cEGOML4jFZfEL3Phoz8tQKHHvqRhk5-3_ShlOFRTGa3V4Fyz-JneOqG5i3nUWxsUoTRtBmlbm5fOoCHhi5I1uGW9GGv4sqv37n1assUNDQbndEc6xpA0JS5RfJuSbMqqE7_C_M4HjL0rqYYJaXoXDVLGo_cECZCarDhW_q8nNl7fdwDNKcDECAdSWXSx7s3kGFn1szQAG2CzvvF1EDPHzR0f28-nVuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3i5MKEcQC28ZtTBlXkBntCk2DP8iGRQBvrDFjR4kDn3JpR3ILLQqH7yCP2-ObGTJ8a8EZGpLH-CKARpzIIZRsPelrnue6Jsjrxz27y3tMuAIEqAkPiF1ytsdBem6G8dQQsRIsIrjLF-ShXk2VAwMRAJDBAdswil140RoaTS-lc1LedBkpZYq1CI1vzfCdfSvcvy5PbAbfMmlle5rLMKhEHnekZpZpjBf4fZesUijptT1s9SBZ_ccxq4rBrtpVqriEYhbDweSX-35GwFdncEdeIFHe7bo07KpmU82BX9ql83gQTCkp6P4rdqZ3vMES4YsEI7padcxPX3igObvZpkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFrnigkQFDV4V7RePI_qFvzgHkwQ_KpQ3byXuYsswfxPpvL2SStTVlUtGz8jOvE0RLD2qOn_q-Ll2qo4yUZW3Dqvu28mvHarPKP-K0i5sr4J8jCCzfl2j8SJIr72JsHDmX1Ars2LVMVyAyHZVtGdjA-rgEzZ5qfXwIXdSOtffIZgwdsPkAXqwxSIZdnyK55LRYQT8Fvo4yo1Bw3vscoCcd5ojH3-mQva8ERWj2w5g1P27vXohCdks_OcvCWfi4Yauqk0rGQ2Pt1tPNk7ktmlBrHxWv6V1ukiXjWfwMI1P4r8r76oCLbtlE4rfZlXbPqvoabMv7tzwwL5zVifMIIozg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
صيادله العراق يعلنون الاضراب و اغلاق جميع الصيدليات في العراق احتجاجا على قرارات وزاره الصحة العراقية و الظلم و التهميش الذي يتعرض له صيادله العراق و الطلبه الخريجين حسب تعبيرهم</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79214" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79213">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
جي دي ‏فانس: بدأت فترة الستين يوماً اليوم، بتوقيت إيران ؛ ‏بدأ الاتفاق أمس، وسنبدأ اليوم احتساب فترة الستين يومًا  ‏نتوقع كجزء من الاتفاق النهائي ألا تمتلك إيران صواريخ تهدد العالم بأسره ؛ ‏تم تدمير برنامج الأسلحة النووية الإيراني، لقد انتهى أمره</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/79213" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79212">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43227bc2ef.mp4?token=DYLyu0G7uwLAOB2KW_nDgKpBgn1P_tSgkbWenDW3PQpdxLWP5wKbL6-agHa3V3KRFWoeNrKjvIzGLKMBR_y_FTSWryrh7n_Jb7znf8OB9WtY61c_5ItBAWHRD877Rs79KJ3rCAdtq-WF2PKAO0dMde8YYW5Ypah4LAOA69VznO8kWDUBTFsbU8wrKYo6bLMoLDd-e6AuAiosjKDFp9pMLDNgBk_3grvqXog8uQ9r-kqmKnO4pukUxfLtvTi4B_jxix4QVHEuHJ96XBSwAWF4fvHntGCIgKOgzeo47Q__B8Kh0yOMsXpqeynKXgvc6BJnJpAPzdID5wIzpj9BFRPT4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43227bc2ef.mp4?token=DYLyu0G7uwLAOB2KW_nDgKpBgn1P_tSgkbWenDW3PQpdxLWP5wKbL6-agHa3V3KRFWoeNrKjvIzGLKMBR_y_FTSWryrh7n_Jb7znf8OB9WtY61c_5ItBAWHRD877Rs79KJ3rCAdtq-WF2PKAO0dMde8YYW5Ypah4LAOA69VznO8kWDUBTFsbU8wrKYo6bLMoLDd-e6AuAiosjKDFp9pMLDNgBk_3grvqXog8uQ9r-kqmKnO4pukUxfLtvTi4B_jxix4QVHEuHJ96XBSwAWF4fvHntGCIgKOgzeo47Q__B8Kh0yOMsXpqeynKXgvc6BJnJpAPzdID5wIzpj9BFRPT4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جي دي فانس: الليلة الماضية، مرت 12.5 مليون برميل من النفط عبر مضيق هرمز.   وهذا رقم مرتفع منذ بداية الصراع.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/79212" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79211">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
جي دي فانس: الليلة الماضية، مرت 12.5 مليون برميل من النفط عبر مضيق هرمز.
وهذا رقم مرتفع منذ بداية الصراع.</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/79211" target="_blank">📅 18:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79210">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇧🇭
الدفاع المدني في البحرين: حريق كبير في منطقة الصالحية ، والجهات المختصة تباشر بالتحقيقات.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79210" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79209">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🦠
الكونغو الديمقراطية: 202 حالة وفاة مؤكدة بفيروس إيبولا</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79209" target="_blank">📅 18:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79208">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4IJ4aG_r8ql2Evb-m9HSiNu1lCnw_uK9LBFU43fkumZjhfEuPOGyBiY_d_CftKnlUXSFTFcWnt2H8TjrsNhYIK_BslQ7pd5HqyrGYAp85XX4gJAetblI4Ypv_jES1_rGwf3waDFhrwCbzApYUKC0sc_Z8U54pI6dPvTstY7QE4omv6w-MmYkYeFCe_IhCzhqI1QlHpCtRl9sz-TkMfyuQ10B5JFPe2Z2r7S4vVcwEwsHM3_MuJPpWY7zQZa680_Hg-eOWg3OdQy7dU1On4dALfmv-jnPK4wtEpveUkoAzpdMAMGLJEwCC8YpFmwEeAjH_3-QZLU3292bb8tECjFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
احتراق دبابة صهيونية وعدد من آليات جيش الاحتلال إثر استهدافهم برشقة صاروخية من قبل حزب الله في الجنوب اللبناني وإعلام العدو يتحدث عن إصابات عدة في المكان.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79208" target="_blank">📅 18:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79207">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇱🇧
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة حول التصدّي لمحاولات العدوّ الوصول إلى مرتفع علي الطاهر:‏
يحاول جيش العدوّ الإسرائيليّ، منذ 4 أيّام، التقدّم باتّجاه بلدة كفرتبنيت ومنطقة علي الطاهر عبر أكثر من مسار مدعومًا بقصف مدفعيّ عنيف يستهدف المنطقة وإطباق جوّيّ استخباريّ تنفّذه طائرات العدوّ الاستطلاعيّة. وقد تصدّى مجاهدو المقاومة الإسلاميّة لجميع هذه المحاولات عبر استهداف تحرّكات وتحشّدات العدوّ بالصواريخ والمسيّرات والمحلّقات الانقضاضيّة، ممّا كبّد العدوّ خسائر كبيرة بين ضبّاطه وجنوده وفي آليّاته، اضطرّ خلالها إلى التراجع وزجّ الطائرات المروحيّة تحت غطاء دخانيّ ومدفعيّ في الليل لسحب خسائره.
يوم أمس الأربعاء 17-06-2026، الساعة 8:00، وبعد رصد قوّة مشاة من جيش العدوّ الإسرائيليّ تتسلّل للتموضع في الأطراف الشماليّة الشرقيّة لبلدة كفرتبنيت، وبنداء يا أبا عبد الله، استهدفها مجاهدو المقاومة الإسلاميّة بسرب من المسيّرات ومحلّقات أبابيل الانقضاضيّة وأوقعوا أفرادها بين قتيل وجريح، ثمّ استكمل المجاهدون هجومهم بصليات صاروخية وقذائف مدفعية باتّجاه منطقة الهدف.
وعند الساعة 1:50 من فجر اليوم الخميس 18 - 06 – 2026، وأثناء محاولة العدوّ التحشيد مجدّدًا عند منطقة المعبر، استهدف المجاهدون دبّابة ميركافا بالأسلحة المناسبة وحقّقوا إصابة مؤكّدة ما أجبر القوّة المتحشّدة على الانسحاب من المنطقة.
تؤكّد المقاومة الإسلاميّة أنّ قوّات العدوّ لا تزال تتواجد عند الأطراف الجنوبيّة لبلدة كفرتبنيت لجهة أرنون، وأن منطقة كفرتبنيت - علي الطاهر ستبقى عصيّة على توغّل العدوّ، وسيسطّر المجاهدون فيها ملاحم كربلائيّة دفاعًا عن بلدهم وشعبهم.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79207" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79206">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇱
🇮🇱
إعلام صهيوني نقلاً عن ‏ترامب: من المحتمل جدًا أن أدعم نتنياهو في الانتخابات المقبلة لدينا علاقة جيدة لكن على نتنياهو أن يكون أكثر عقلانية.. وأنا مستعد للالتقاء معه</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79206" target="_blank">📅 17:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79205">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79205" target="_blank">📅 17:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79204">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvKqj7K2ATDCUOaJ5MCYK6tfB-BbR-7D9Ocw5cRyluZUHYjKe3b4zK6IYBIPVASmnWCc4SG_07CSAz9K7lIiifdZbjNDOp4Toe7Uer4QlWhkHdqOGdZYStDdBLg-BxXUlmSPrvWY1-6lPx61ofabeV2vTFzTK_p1KEvTq4J23pshAyY9p9UWZDiKgGPs3NBYSnglhJjaRKc0IO2qOqe12HX_C3yKcaUVmM5VyZz4cFL9fdVgdqcZj5y69sKfm93hSK1CXicz4AbOj1ZG0UAmAlWdot_VrTvjP-QKVXew0Wte3eJcEaBgi0ZkvP6IalhpHYYZlCY_tHVsupvveJgiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب من غمرة أحلامه يغرد: "النفط يتدفق، وإيران لن تمتلك سلاحًا نوويًا أبدًا (سيكون العالم آمنًا!)، وأسواق الأسهم مزدهرة، والوظائف في مستويات قياسية، والأسعار في انخفاض (القدرة على الشراء!). بلدنا قوي وآمن ويحظى بالاحترام أكثر من أي وقت مضى. على الرحب والسعة!"</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79203">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدير عام وزارة الأمن الصهيونية: الحوثيون والميليشيات العراقية يملكون القدرة على التسلل بريا إلى إسرائيل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79203" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79202">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية: الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79202" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79201">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية:
الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79201" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79200">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzZDPrA6rwY1JxJqzeNam24UliwyGtW45mjqHzkrLKn-m0el6C1EPlgb_LgIaIwh6zzcuTzNEWz4rMKRPSyIvldBpGkswbVG0EPEzXFvTcQwjgiKNsYTX2M28lwaxJGenh0Knu8-CXq9wIY0-xDuLZ5O_py8UKvAUDs7yF7SkvRFc1Aw1cOlezjl6z5B92f6qrAOXW7dnHrTnfHEGtWoofVIwrRMhhCYw5nU4fYfMtDkgYBHtEAlLLPVQQ1SV1YVWiE_fGu6JfgIkmwnU8uR3oCva-rIdbu5Vqz8g8GC02DUu_Wh8knJS8_eIM681em4e3zND-Ud8lTo3ObmxAMhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة
يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.
التاريخ: يوم الجمعة 2026/6/19
الوقت: الساعة الخامسة مساءً
المكان: بغداد الصالحية - أمام السفارة الايرانية</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79199">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اعلام العدو:
يعتقد مسؤولون إسرائيليون أن الرئيس ترامب قد يؤجل شحنات الأسلحة أو يفرض حظراً على توريد الأسلحة إلى إسرائيل في المستقبل إذا لم يسحب نتنياهو قواته من لبنان.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/79199" target="_blank">📅 17:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
التلفزيون الباكستاني يعلن الغاء زيارة رئيس الوزراء شهباز شريف المقررة إلى سويسرا دون تحديد الاسباب ويقول ان المفاوضات التقنية الأمريكية الإيرانية ستبدأ بشكل منفصل ووكيل وزارة الخارجية سيمثل باكستان في اجتماع سويسرا.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79198" target="_blank">📅 17:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الخلاف الامريكي الاسرائيلي يتصاعد.. نتن ياهو: أمامنا تحديات إضافية تتطلب التمسك بالمصالح الأمنية والحفاظ على العلاقة مع أصدقائنا الأمريكيين.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79197" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حدث امني في جنوب لبنان وإخلاء عدد من الجرحى في صفوف الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79196" target="_blank">📅 17:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي لافروف:
زيلينسكي إرهابي وروسيا ستشن ضربات منتظمة على أهداف في أوكرانيا حيوية وفعالة لقواتها العسكرية رداً على هجمات كييف.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79195" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث امني في جنوب لبنان وإخلاء عدد من الجرحى في صفوف
الجيش الإسرائيلي
.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79194" target="_blank">📅 17:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">متداول:
تكليف (نزار ناصر) بمنصب محافظ البنك المركزي العراقي.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79193" target="_blank">📅 17:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2da43f07.mp4?token=gs3efZeUnuRZF-59uL4rRzizqbSq19_zng0vQFeEXX7_1RdIgc-GVkH88Jbm9u9x8QEi6gZ0pwfRquTqmDsEX3CbgjahmqP7ML1X3VU1GaR3rnTDLJ_GSggMPN3eg-NBV5oK9uK85OBn77LMzXNwo0zYZYQFH0MVDPx7tIJkkUpMDUUWWORQ_-P8dY74rWV63xsz07rXpHH3uGMi5uxT3-fi5yP20LDnd_OgnI27DB7yo06O0WORgiH4Ctx04rYpBSlxIm4lp0m4s3N8q3JP8F1Pg0bo-tE-xqp6HbKYOzdkK_WQwlIv6ioTTPyWwPO09ubaU6q_V04LbY6k4rpAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2da43f07.mp4?token=gs3efZeUnuRZF-59uL4rRzizqbSq19_zng0vQFeEXX7_1RdIgc-GVkH88Jbm9u9x8QEi6gZ0pwfRquTqmDsEX3CbgjahmqP7ML1X3VU1GaR3rnTDLJ_GSggMPN3eg-NBV5oK9uK85OBn77LMzXNwo0zYZYQFH0MVDPx7tIJkkUpMDUUWWORQ_-P8dY74rWV63xsz07rXpHH3uGMi5uxT3-fi5yP20LDnd_OgnI27DB7yo06O0WORgiH4Ctx04rYpBSlxIm4lp0m4s3N8q3JP8F1Pg0bo-tE-xqp6HbKYOzdkK_WQwlIv6ioTTPyWwPO09ubaU6q_V04LbY6k4rpAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ظهور كائن نهري نادر غير معروف في محافظة ديالى ومواطن يتسائل هل هو حلال او حرام اكله تمهيدا لتحويله الى منسف.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79192" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXMw66rrx3k6KgwTuH-ryPdHzAZQbGqOOubMHmit06uluWeFMNcnwT3OJuvKG8VMt7hKADoSLfvMU9mg8x33-Ot_YNBs0bACMEzm4MhLKPn1hVUTsDGHZjDgUh2L1Nv6APHqwOGRMbQFxd-yr3inVomso2t1S3Dets84mdzLgO2dufC_XMyRBGzLUGBeisZXtm6DOa3jx0a73vjfytFnlSkLEB1VjOfODffCSGLG76PLC0Dey64SE6NU-NV3qbGu9mp6BQiGd2_pTWtEcSs86VE0_T5jyufKSbWWWC4oSGZEEAepVXJuylbZSPeBby-687ILrwb9qkWlDoqOurNlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يعيد نشر تقرير بعنوان "البابا ليو يشيد باتفاق السلام بين الولايات المتحدة وإيران".</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79191" target="_blank">📅 16:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الخلاف الامريكي الاسرائيلي يتصاعد..
نتن ياهو: أمامنا تحديات إضافية تتطلب التمسك بالمصالح الأمنية والحفاظ على العلاقة مع أصدقائنا الأمريكيين.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79190" target="_blank">📅 16:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇬🇧
‏بريطانيا تقرر تزويد أوكرانيا بـ150 ألف طائرة مسيرة بحلول نهاية العام ضمن حزمة تمويل بقيمة 752 مليون جنيه إسترليني.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79189" target="_blank">📅 16:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
القائد العام للقوات المسلحة يكلف باسم البدري برئاسة جهاز الأمن الوطني العراقي.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79188" target="_blank">📅 16:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174a7917f4.mp4?token=JYyaKjHfAIJRXinNbHmPDjk4cHPvM93FlE0Q2_C0RdlkWDO0IANHQRFuelO4gpbOoTkthXWkjCpAju77ODotft117mjirsPwu8dZ_asAsxHz5bPj0GUjSLJH0-dhkBFO8ud6_YHLtOdzeQeROMXQAvf9jE7DrCRyiD-s9JKq8IQwmAvwGWvQKGrqumd9ka_7vOATdJPMxEp8GtyDTJNK8f_Y3zREani1I_eq44mFNzN5TO6Xa1dAnfdj-qQvm6_5OcQKy-UiAdUD2sKqkaeROP3L-tMO2rL4o-hlRcuVrK7tcmfCQOm1ZOllIm0NKWejRJIHBMmqTOZi0xjYBjYJ7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174a7917f4.mp4?token=JYyaKjHfAIJRXinNbHmPDjk4cHPvM93FlE0Q2_C0RdlkWDO0IANHQRFuelO4gpbOoTkthXWkjCpAju77ODotft117mjirsPwu8dZ_asAsxHz5bPj0GUjSLJH0-dhkBFO8ud6_YHLtOdzeQeROMXQAvf9jE7DrCRyiD-s9JKq8IQwmAvwGWvQKGrqumd9ka_7vOATdJPMxEp8GtyDTJNK8f_Y3zREani1I_eq44mFNzN5TO6Xa1dAnfdj-qQvm6_5OcQKy-UiAdUD2sKqkaeROP3L-tMO2rL4o-hlRcuVrK7tcmfCQOm1ZOllIm0NKWejRJIHBMmqTOZi0xjYBjYJ7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جندي في جيش الاحتلال التركي ينشر مشاهد يُظهر الطريق العسكري الجديد الذي تم تشييده بعمق 9 كيلومترات في قرية باساغا بمحافظة دهوك ضمن اقليم كردستان العراق
يمتلك جيش الاحتلال التركي 139 قاعدة عسكرية في إقليم كردستان رُبطت جميع هذه القواعد والمقرات بشبكة من الطرق العسكرية وقد قُطعت عشرات الآلاف من الأشجار ونُسفت جبال وتلال الاقليم لبناء هذه الطرق.
اين مسعود وميليشياته التي تضيق على شباب وجمهور الحشد الشعبي والسائحين ممن يرفع العلم العراقي من هذا الاحتلال؟</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79187" target="_blank">📅 16:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
المتحدثة باسم الحكومة فاطمة مهاجراني:
هذا الانتصار اليوم هو ثمرة جهود القوات المسلحة وكافة أركان المجتمع والحكومة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79186" target="_blank">📅 15:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
الأنواء الجوية العراقية تبشر الشعب العراقي:
موجة حرّ خمسينية تضرب البلاد بداية الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79185" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79183">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcqSYB3Pa_f5qePSftBJwfOikirhhOEX2Lu4XaRpHdRFpAH1buUOCJdeC7-Opge-UkvL1T1eheGz1sdb5mFmnx6HD_SbVNFO15Huj4ny4Ga6J8Yrg3gPKRW8_P8fS0eGUddiT4R1ZligzCxpktdaNaBn_i7lAbM_TIG2RixLI3UFo5BOBTBnc7CLatpmx7J8eIo9o75LCNhfszGxre1ORZkegXM_-m0TYBmDLjEh7z_i6lUkqGPX3BoENT6HqD_9iyO7TKOFHCxJRSFVujGtIP_j0KV3rFklWFYVarQOKjh2T29z4M4j8HMqgs1diPzWdQxVH586Y7R_Zvq4L9vvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
توثيق أخر يظهر كثافة استخدام القنابل المسيلة للدموع وإطلاق الرصاص الحي من قبل عصابات آل خليفة نحو المعزين بذكرى أيام إستشهاد الإمام الحسين (عليه السلام) في منطقة أبوصيبع البحرينية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79183" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79182">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اعلام العدو:
اتفاق جيد لإيران وسيء "لإسرائيل"، سيبقى اليورانيوم المخصب في إيران، وينهي الحرب في لبنان، ويضمن إعادة إعمار إيران.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79182" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79181">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
سي إن إن عن مصدر إسرائيلي:
نتنياهو يرى أن الاتفاق النهائي لن يحدث وأن طهران لن توافق على تقييد برنامجها النووي، نتنياهو يسعى للتأثير على الاتفاق مع إيران عبر إعلاميين يمينيين وأعضاء بالكونغرس.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79181" target="_blank">📅 15:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjL2V44BVtBoMcPuaNRJnq951AI1HMTd-mdHcfGQ961yycg6xZmcDHCVb7ZxbZaCE49QUdqd3zWlKXUYd3lHucI7goBxclC53TF2f6Dz828mjZ0TsU337gXVRhRDH6eU8VnWvVVsaugRFaB4mam99TcgbbIc48O-lyNS1FF1Gt-n3tJ9a2KJ8vYA_XC7j12CZbICa_pxEPHQp22lPHwRsT6-ZFbzBV3dDK86bknuYUlrFNEwcsTRMZtjaYyNf1ePVKMHFi5sBtrhWxm_KOZf4lCgJ-Oih9w2oT-7jmPjhWXguo_mnaLCaj7oPlTpYGacIz0xCAx1RITg45wXq2n91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPUTiCX0mu6qN-qAGEF-pr52P5kVR3_TpBtdM2FUzJ81vY_ejozrr_n7i0fPTyWHFHW4ceSfUaumgm9Bbtlm_w1PKXtEW3lw69-MXvwYPTA9PCXhh0UQRVGmWnKlqUOtMSkau-cNd7nyBWCLlHDmWFFGV4XzFABcugLRGS3R8sDJmeIeuZ4Y06bbD3E34ej0O5J6X7jDbBcY5gp4wwvcxHB0GsH7SQs2cdOwzu14SQLGFQueDNRuF6hYDHVlGSlapG8PUPMRmvk4CKycLnufl454THrx3U2q2aQkmcSL5T0omszhW5ZIeDDKfdeBPbPtBpZqmbu8K4JtgRkCYGPK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8YJeI0cFiizC3qaBJcdJSRa9WN5BjNZbequKWbq-Uq23TKBbSoWnUQlKsAtkBTh7Nprdf8kf9DaBhdLIGTYZSi5YTvLzIe3dyfJIvmwi0iYGKumGeUyOm4h5lqYNa3-kfUgZHfLvduyYxEp9ORd1h76G6VS9_Yy_jqeYpSyFEZCwp4GDP0MG1s4S7XH04TYp51E2M_B5MWwu7oQkabINJQoBI-6B4xSEFwlVvqNmwPI9r0ovgrMfGf4Il35YCP_Ot3xz1MgxogV6QsNLkpyGV9eH2GxL8GGR25EAQ0MXtjBTLf5LCMgtR7nNKj2Uf4rHeQy_kuTYLuN8dqeP_BDqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان ينشر بنود الاتفاقية مع الولايات المتحدة رسميا.
- تُعلن الجمهورية الإسلامية والولايات المتحدة وحلفاؤهما في الحرب الحالية الإنهاء الفوري والدائم للعمليات العسكرية على جميع الجبهات، بما في ذلك في لبنان، ويتعهدون من الآن فصاعدًا بعدم بدء أي حرب أو أي عملية عسكرية ضد بعضهم البعض
- تتعهد الجمهورية الإسلامية والولايات المتحدة باحترام سيادة كل منهما والسلامة الإقليمية والامتناع عن التدخل في الشؤون الداخلية لكل منهما
- تلتزم الجمهورية الإسلامية والولايات المتحدة بالتفاوض والتوصل إلى الاتفاق النهائي، في مدة أقصاها 60 يومًا قابلة للتمديد بالتراضي.
- فور توقيع مذكرة التفاهم هذه، ستبدأ الولايات المتحدة في إزالة حصارها البحري ضد الجمهورية الإسلامية كما تتعهد الولايات المتحدة الأمريكية بسحب قواتها من محيط جمهورية إيران الإسلامية في غضون 30 يومًا بعد الاتفاق النهائي
- عند توقيع مذكرة التفاهم هذه ستبذل الجمهورية الإسلامية قصارى جهدها لاتخاذ الترتيبات اللازمة لضمان المرور الآمن للسفن التجارية مجانًا لمدة 60 يومًا فقط
- تتعهد الولايات المتحدة مع الشركاء الإقليميين، بوضع خطة نهائية متفق عليها بشكل متبادل بقيمة لا تقل عن 300 مليار دولار أمريكي، لإعادة إعمار وتنمية اقتصاد الجمهورية الإسلامية
- تتعهد الولايات المتحدة بإنهاء جميع أنواع العقوبات المفروضة على الجمهورية الإسلامية، بما في ذلك قرارات مجلس الأمن وقرارات الوكالة الدولية للطاقة الذرية وجميع العقوبات الأحادية الجانب، الأولية والثانوية، وفقًا لجدول زمني متفق عليه كجزء من الاتفاق النهائي
- تؤكد جمهورية إيران الإسلامية مجددًا أنها لن تحصل على أسلحة نووية أو تطورها. وقد اتفقت الجمهورية الإسلامية والولايات المتحدة على حل مسألة التخلص من المواد المخصبة المخزنة وفقًا لآلية يتم الاتفاق عليها بين الطرفين كما اتفق الطرفان على مناقشة مسألة التخصيب، وغيرها من المسائل المتفق عليها والمتعلقة باحتياجات الجمهورية الإسلامية النووية، وذلك في إطار عمل مُرضٍ يتم الاتفاق عليه في الاتفاق النهائي.
- في انتظار الاتفاق النهائي، تتفق الجمهورية الإسلامية والولايات المتحدة على الحفاظ على الوضع الراهن الحالي لبرنامجها النووي، ولن تفرض الولايات المتحدة أي عقوبات جديدة، ولن تنشر قوات إضافية في المنطقة.
- تتعهد الولايات المتحدة بأنه فور توقيع مذكرة التفاهم هذه، وحتى انتهاء العقوبات، ستقوم وزارة الخزانة بإصدار تصاريح لتصدير النفط الخام الإيراني، والمنتجات البترولية ومشتقاتها، وجميع الخدمات المرتبطة بها، بما في ذلك المعاملات المصرفية والتأمين والنقل والشحن
- تتعهد الولايات المتحدة بإتاحة الأموال والأصول المجمدة أو المقيدة للجمهورية الإسلامية للاستخدام بالكامل عند تنفيذ مذكرة التفاهم هذه وتتعهد الولايات المتحدة الأمريكية بإصدار جميع التراخيص والتصاريح اللازمة وفقًا لذلك
- تتفق جمهورية إيران الإسلامية والولايات المتحدة الأمريكية على إنشاء آلية تنفيذية لمراقبة التنفيذ الناجح لهذه المذكرة والامتثال المستقبلي للاتفاقية النهائية لعام 2001
- بعد توقيع مذكرة التفاهم هذه، ورهناً ببدء تنفيذ الفقرات ١ و٤ و٥ و١٠ و١١ من مذكرة التفاهم هذه واستمرار تنفيذ هذه التدابير، ستبدأ جمهورية إيران الإسلامية والولايات المتحدة الأمريكية مفاوضات بشأن الاتفاق النهائي حصراً بشأن الفقرات الأخرى.
14- سيتم اعتماد الاتفاق النهائي بقرار ملزم من مجلس الأمن التابع للأمم المتحدة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79178" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79177">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
بيانات ملاحية:
ناقلة فرنسية للغاز الطبيعي المسال تعبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79177" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79176">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في أطراف بلدة مجدل زون جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79176" target="_blank">📅 14:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79175">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
بناء على الحاجة العملياتية تنتشر قواتنا في المنطقة الأمنية بعمق 10 كلم داخل الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79175" target="_blank">📅 13:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79174" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79173" target="_blank">📅 13:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=ibPdrIkh4lglgYyn3DnDrxl-yQvbHh-R2y_D9xFpLAZKJZxb-FYf4oemoM9iLARqAP1Hz2ONTZwn-or07ZsoQl2Sf23uxj_S-UBTshLDyxq4sS7gR0Ce7enVpzf7kB5MVylpssA8MRrFjGx3zs8y8PTiuZY_evMK1Rz7l7l9GgMI-5JmLqlUlKi1IZY9FvFHJjDJWTRQJp2ygzf8SWoBhbmFiwqez0OCeRLcNyZqTzB1N66tZEaft6ppcT0q6XMGVXo4f-lvfPZ3UJJLc52xqwVBejY6XU0Wr5BS_E_JfVhCx1y4vzcWqfkIO89JKemr-orTTWtfBwTweYI-VmGASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=ibPdrIkh4lglgYyn3DnDrxl-yQvbHh-R2y_D9xFpLAZKJZxb-FYf4oemoM9iLARqAP1Hz2ONTZwn-or07ZsoQl2Sf23uxj_S-UBTshLDyxq4sS7gR0Ce7enVpzf7kB5MVylpssA8MRrFjGx3zs8y8PTiuZY_evMK1Rz7l7l9GgMI-5JmLqlUlKi1IZY9FvFHJjDJWTRQJp2ygzf8SWoBhbmFiwqez0OCeRLcNyZqTzB1N66tZEaft6ppcT0q6XMGVXo4f-lvfPZ3UJJLc52xqwVBejY6XU0Wr5BS_E_JfVhCx1y4vzcWqfkIO89JKemr-orTTWtfBwTweYI-VmGASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79172" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtRY8wZYH8U7sX2f2qWk-y1teMWEJ6fqriaSMyMiAgO54wRpe30HNNKaRYAtKFTJ-MwxMs16fLEyW5WsExg_XO6lG1iHBpmJVb9-gKEDwymtsMi2gZMDITqgrqKxQxBupnIE8acao6qeKl7i-4WyN9-2PI69IIOtN9E7AT4Hi7qM5Xd-Hz2DJr65NKJGp-fb69eBJEB7bWxgaQg52NJLiPIQ6t2QiKFVY-I24-oLKa1p-N9TBBQvNLFZfzusWljunZVNaHysmdW5a6jPV8RXbw2NAYHwQERVoUvr5zPz-h2wwKuuwulbW18XtzNJFnelJORxV0jdRZQ56AjUFLsLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
"هؤلاء الحمقى الذين يظنون أنني لم أكن حازماً بما فيه الكفاية مع إيران، في حين أن سوق الأسهم قد سجل للتو مستوى قياسياً، وأسعار النفط "تنهار"، إما أنهم حسودون، أو أناس سيئون، أو أغبياء. لنجعل أمريكا عظيمة مرة أخرى!!!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79171" target="_blank">📅 12:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=BDcnJo9AZ17ln4-Xh_VxgT0lfDhNdCFPcRbRqv6cCiIdmhEoSMfE7BKDRxgSi9xzDeFZ9KJOFQkOxbzFB-paFLe3Y2P9G4TkUJ0bXvLeE19twpEND5HG8GJolup5XOi3SwXbTS9GCSEtvECm5gK6w_25ckEzGl5Dg0c572-kxDZHvjOdmAcGK8_T0I04nAWfRqga763HhNi8sC3HpvEL5FCUP2weL_-lz5oQVUXVdZbbxU7MygUsEHAABtdDmloIbvyO7aUe4zT_Rv0GFI1BRVkHxf253aCZj9bwkWp0zS8f4qL-iVRpb3eZVpIXz24tb3zW9A2uY1eexuGS_qr5wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=BDcnJo9AZ17ln4-Xh_VxgT0lfDhNdCFPcRbRqv6cCiIdmhEoSMfE7BKDRxgSi9xzDeFZ9KJOFQkOxbzFB-paFLe3Y2P9G4TkUJ0bXvLeE19twpEND5HG8GJolup5XOi3SwXbTS9GCSEtvECm5gK6w_25ckEzGl5Dg0c572-kxDZHvjOdmAcGK8_T0I04nAWfRqga763HhNi8sC3HpvEL5FCUP2weL_-lz5oQVUXVdZbbxU7MygUsEHAABtdDmloIbvyO7aUe4zT_Rv0GFI1BRVkHxf253aCZj9bwkWp0zS8f4qL-iVRpb3eZVpIXz24tb3zW9A2uY1eexuGS_qr5wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79170" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79169">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭐️
المدير العام للوكالة الدولية للطاقة الذرية:
حان الوقت للجلوس مع الفرق الأمريكية والإيرانية لاتخاذ خطوات ملموسة.
سنشارك في المفاوضات التي ستعقد في سويسرا بين واشنطن وطهران.
هناك خيارات عديدة بشأن التعامل مع المخزون الإيراني من اليورانيوم.‏
الاتصال مع إيران في أدنى مستوى له.
إذا لم يفتح مضيق هرمز حتى نهاية يونيو فسيكون الاقتصاد العالمي في منطقة حمراء.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79169" target="_blank">📅 11:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79168">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79168" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79167">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79167" target="_blank">📅 09:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79166">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=FTAFEYDvhcSsJ0ovv4HRqKtRUutYkEfCA1hXZp1uTH_YYr75MXWQXvrVp_zDv9p5DOlkXehBAN3um4DR0oPB1wRnDBkgLEWKRQIgppFHuLZFuffjDknwiPsu3X7J3BPhcfeN-kjGl9F67AJAwfnr4u1IPj9DMF3pjd09c9kWWd6YoiGbWE71nqxxjQEJfRAwjAFhJxXy5i0bEXpmzEOp9ECeySXnMPyfkZQPhBZPuG3FBNuDjnUp3r2x_THp1bzQutb7Ej21xN2zrS3muYFiZKzbHl4jpQtK4v6R1negvw53zOuvvAiEsC_POInGbwiIvaQxXfB1q_UxEoLaSmeXLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=FTAFEYDvhcSsJ0ovv4HRqKtRUutYkEfCA1hXZp1uTH_YYr75MXWQXvrVp_zDv9p5DOlkXehBAN3um4DR0oPB1wRnDBkgLEWKRQIgppFHuLZFuffjDknwiPsu3X7J3BPhcfeN-kjGl9F67AJAwfnr4u1IPj9DMF3pjd09c9kWWd6YoiGbWE71nqxxjQEJfRAwjAFhJxXy5i0bEXpmzEOp9ECeySXnMPyfkZQPhBZPuG3FBNuDjnUp3r2x_THp1bzQutb7Ej21xN2zrS3muYFiZKzbHl4jpQtK4v6R1negvw53zOuvvAiEsC_POInGbwiIvaQxXfB1q_UxEoLaSmeXLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79166" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79165">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79165" target="_blank">📅 09:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79164">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
لا يزال استهتار البعثات الدبلوماسية الأجنبية في العراق مستمر
اصابات خطرة لمجاهدي جهاز الامن الوطني العراقي بعد تعرضهم لحادث سير من قبل رتل تابع للسفارة الأمريكية على طريق مطار بغداد ؛ ثلاثة جرحى كحصيلة اولية من الضباط …</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79164" target="_blank">📅 08:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79163" target="_blank">📅 08:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsVfl4qgC3oXjheRpK-ARbL-oYys_SRQhk6NYIHHgi_PWSslVKvP4mTcAuhIYrxc-fFp2As1hDoc7EhqIERltsPuThRY65LoeqibRBxlEAHi-lZPAQZqR5Mi61Mt-Ba6RCJfCatJ4O7rqWjojLQTRhmtHrJvvLKAdH-yioGbS0wOw9Kps4UndCBqi59-Dmi4QmD2Lt7YDskVR3Wu1ccPbaSGKyuQjoqwDvRYZXu6du7GSSQXOLMPLkKYta0yYKSWYlVwtuxsch5N95iaLVkFDBHtevSeOHnVrTFkQzBCS6UauBKK7R45NXTDws201HyVSE73M_tvGEa2vXl0Xabzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=PMFvH0UW79SY_hpuPO1Xju1k0Fk8F8cQxaKQ8FhtVqOMJ-4nt61bL3QSz31W5YQGRPwojkvB_qnp41o1XbuBJUSiv_r8kQd7mDGpFJibeGZgPe2SyWCUH40vkMqv3xslJ9zPkFn0urj52oMDOhcjzYTAPaQUBxqAyIGtNjkkWul7NpxPg5U5FJJjmMudBdHe2VAqleLRKwLAsfbsNmZHF3mw16tbfNM01LFiw7NHmKj09YvlLbqMcCkaYUgwkYGasPYG1JMmBgU3wBiJqXqd1ZbPKYMWtFdEac9sjTHvMCUSazCrVXhjgqQia5_BuzvFsUvg_hK6sw71ClT8Cu9b5XAjD80Y0b0tU7bRwkPusm7YtuYGzZ5MQ4qeVMv9JYFC05erMrimaag05_XKP9Cp3kNJI1QZVY6yAjaKfIe7LqTcZ4OVfbL7sdGscpAsYzzzrL_9ELD6XYQTMwM5JAhAzsZTVC0HEXi9ImfjOIGEbDnB3kM71hC9I9lSP4HxHDMgWkJCuo814fr1AjACZTYWDYaolaiwC5KRlDEP1RbYdzzcxj7qxvgMRgu4R3Jy2jLIdEhBFOgs4WxCStQewniThRlj33xshltApJiaRmh4dGZj8Uwz7hF7DbqSYypySuWTpaoQOaOaO068MLlvPy-RLw_4hS6PPEkpgzsDUeIiyAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=PMFvH0UW79SY_hpuPO1Xju1k0Fk8F8cQxaKQ8FhtVqOMJ-4nt61bL3QSz31W5YQGRPwojkvB_qnp41o1XbuBJUSiv_r8kQd7mDGpFJibeGZgPe2SyWCUH40vkMqv3xslJ9zPkFn0urj52oMDOhcjzYTAPaQUBxqAyIGtNjkkWul7NpxPg5U5FJJjmMudBdHe2VAqleLRKwLAsfbsNmZHF3mw16tbfNM01LFiw7NHmKj09YvlLbqMcCkaYUgwkYGasPYG1JMmBgU3wBiJqXqd1ZbPKYMWtFdEac9sjTHvMCUSazCrVXhjgqQia5_BuzvFsUvg_hK6sw71ClT8Cu9b5XAjD80Y0b0tU7bRwkPusm7YtuYGzZ5MQ4qeVMv9JYFC05erMrimaag05_XKP9Cp3kNJI1QZVY6yAjaKfIe7LqTcZ4OVfbL7sdGscpAsYzzzrL_9ELD6XYQTMwM5JAhAzsZTVC0HEXi9ImfjOIGEbDnB3kM71hC9I9lSP4HxHDMgWkJCuo814fr1AjACZTYWDYaolaiwC5KRlDEP1RbYdzzcxj7qxvgMRgu4R3Jy2jLIdEhBFOgs4WxCStQewniThRlj33xshltApJiaRmh4dGZj8Uwz7hF7DbqSYypySuWTpaoQOaOaO068MLlvPy-RLw_4hS6PPEkpgzsDUeIiyAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لحظة توقيع اتفاقية التفاهم بين الرئيسين الايراني والاميركي.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/79161" target="_blank">📅 03:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79160">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
🌟
وزارة الخارجية الإيرانية: تم رسمياً توقيع نص مذكرة التفاهم من قبل رئيسي أمريكا وإيران.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/79160" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
🌟
وزارة الخارجية الإيرانية:
تم رسمياً توقيع نص مذكرة التفاهم من قبل رئيسي أمريكا وإيران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/79159" target="_blank">📅 00:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79158">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏اندلع حريق في الطوابق العليا من مبنى الإمارات في دبي
‏أبراج فاينانشال: سبب الحريق مجهول</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/79158" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
قالبياف:  بمجرد أن دخل وقف إطلاق النار حيز التنفيذ، رأيتم أن العدو قام بأعمال في الخليج الفارسي، و تم الرد عليها على الفور.   وكان أحدث مثال هو الحادث الذي تورطت فيه طائرة هليكوبتر أمريكية.  بالإضافة إلى ذلك، تم إصابة سفينتين حربيتين للعدو كانتا تحاولان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/79157" target="_blank">📅 00:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30ecaca4a.mp4?token=cK8NXCd3KBwU0-83APIrS0WuQVBuu-9izAV9KO0Bh3euHEyN_ClNm4qRst4L5vZmLPEanIiTdpqqBOQxuv35cEIhluMihai349Lby8t-8Z5jYsnILyZWt_-9uSejVWDvlkeemPJsy6MK5RQPy61kv0tsC4JmhJZ_4MLbevil6OJxcYtsXV-qouf72t_iC4C4Hiqm5Ge5LwMj6MwNcQMDWa0PlLv3TWNcV52FVGHCMrG9GIdp0_t_4aGIs56ElrEBak-hADQzWHX7MboWNYXvmv1gM-VI4tKgHWWgNcYLLck64ZLq76DtkYr_AqB-8rICkeW2S-z-plhqlIMrsGUdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30ecaca4a.mp4?token=cK8NXCd3KBwU0-83APIrS0WuQVBuu-9izAV9KO0Bh3euHEyN_ClNm4qRst4L5vZmLPEanIiTdpqqBOQxuv35cEIhluMihai349Lby8t-8Z5jYsnILyZWt_-9uSejVWDvlkeemPJsy6MK5RQPy61kv0tsC4JmhJZ_4MLbevil6OJxcYtsXV-qouf72t_iC4C4Hiqm5Ge5LwMj6MwNcQMDWa0PlLv3TWNcV52FVGHCMrG9GIdp0_t_4aGIs56ElrEBak-hADQzWHX7MboWNYXvmv1gM-VI4tKgHWWgNcYLLck64ZLq76DtkYr_AqB-8rICkeW2S-z-plhqlIMrsGUdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالبياف
:
بمجرد أن دخل وقف إطلاق النار حيز التنفيذ، رأيتم أن العدو قام بأعمال في الخليج الفارسي، و تم الرد عليها على الفور.
وكان أحدث مثال هو الحادث الذي تورطت فيه طائرة هليكوبتر أمريكية.
بالإضافة إلى ذلك، تم إصابة سفينتين حربيتين للعدو كانتا تحاولان المرور عبر مضيق هرمز وعانت من حرائق واسعة - وهي مسألة أكدتها أيضًا صور الأقمار الاصطناعية.
ومن ناحية أخرى، تم استهداف أي مطار في أي بلد انطلقت منه طائرات مقاتلة للعدو. حدثت كل هذه الأحداث أثناء مشاركتنا في المفاوضات في نفس الوقت.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/79156" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
‏ترامب: سيتم توقيع الاتفاق مع إيران خلال الـ 48 ساعة القادمة، ومن المحتمل أن نبقي الجيش في الخليج لفترة من الزمن، وإذا كانت الدول الأخرى تمتلك صواريخ باليستية، فمن "غير العادل" بعض الشيء ألا تمتلك إيران أي صواريخ، والغبار النووي أقل أهمية من عدم الانتشار…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/79155" target="_blank">📅 22:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
‏ارتفاع إنتاج النفط الخام في جنوب العراق بنحو 500 ألف برميل يومياً ليصل إلى 1.5 مليون برميل يومياً، فيما ارتفع إنتاج حقل الرميلة إلى 650 ألف برميل يومياً. كما أعاد العراق تشغيل حقل غرب القرنة 2 بإنتاج يبلغ نحو 150 ألف برميل يومياً، في إطار تعزيز الإنتاج وتعافي عمليات التصدير.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/79154" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
‏
ترامب
: سيتم توقيع الاتفاق مع إيران خلال الـ 48 ساعة القادمة، ومن المحتمل أن نبقي الجيش في الخليج لفترة من الزمن، وإذا كانت الدول الأخرى تمتلك صواريخ باليستية، فمن "غير العادل" بعض الشيء ألا تمتلك إيران أي صواريخ، والغبار النووي أقل أهمية من عدم الانتشار النووي.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/79153" target="_blank">📅 22:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امريكا وانهيار سياستها الخارجية؛ ‏الرئيس البرازيلي لولا:
لم أطلب عقد اجتماع ثنائي مع ترامب لأننا
نتفاوض بالفعل.
‏ما فعله كان عملاً شائناً تجاه البرازيل. وهو يعلم ذلك.
‏لهذا السبب قلت إنه لا يزال يتصرف كإمبراطور.
و ترامب كثير الكلام وقليل الاستماع.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79152" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhy-hhp-dmBJuDcgspcP7wzu0YyCi6RzW1EfA3d1Piq5XrBjmp3Q3x1Yag0blZ9ququsOY7N4c4LN_EjWRySzV9ZOz7takZO3a5MhfLJuLNWwmMLbBA44CI0w71kB2vIZWLtrbkEciLRG66cFjluUAQb7PElohkUAIZdC5u759FOAU577zPJlXRJi-9HeMxp0gc7P7aWHmagrN6-fgtp4m1GLBBLi3CW_tpVENLbibwO-kcT2njGlGORaOd5yy36A5JKCvMbfx_VTJqRY9f9EqTNI9AbZ91oTDgMx0MXxxALXOLCNIou85NniEUjotiwu8p36DChuSMvjge-QMI9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إيلون ماسك يعلن دخول ستارلنك للعراق من خلال زيارة توم باراك للعراق !</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/79151" target="_blank">📅 21:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a82aaa5f.mp4?token=NGgbmamBJVcgvLeF8cHGqE3SP8Kpk1AgnFvInz16HJIIGoq-aNWHHE900-sfy3840PzUVCRn3_G49s0NHAmo0LNn5iR8TGUq0ZcdP8wCHQ5y7h5m8MA7bI3iOZvji-EmhS8TN1q9RIUwOXgLA-H38ifjVp1Xl_4dtgyj_KQIfaJvwBUKocNOMfGcogvLMf1HZ0QQoIP9cUNCqT32EOreRhbKTJZjr1v0Kqhy4Jo1hyj0IK4TC2xLnSpAoPKGodoLlCHpjpCGSZd4vR_O5cfsmw97IZo9n_mFYqBrmzNZDEC_1bg_mlVJAffoSkkDPz6_b_fc5bjaBMCcIM8ehFwIdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a82aaa5f.mp4?token=NGgbmamBJVcgvLeF8cHGqE3SP8Kpk1AgnFvInz16HJIIGoq-aNWHHE900-sfy3840PzUVCRn3_G49s0NHAmo0LNn5iR8TGUq0ZcdP8wCHQ5y7h5m8MA7bI3iOZvji-EmhS8TN1q9RIUwOXgLA-H38ifjVp1Xl_4dtgyj_KQIfaJvwBUKocNOMfGcogvLMf1HZ0QQoIP9cUNCqT32EOreRhbKTJZjr1v0Kqhy4Jo1hyj0IK4TC2xLnSpAoPKGodoLlCHpjpCGSZd4vR_O5cfsmw97IZo9n_mFYqBrmzNZDEC_1bg_mlVJAffoSkkDPz6_b_fc5bjaBMCcIM8ehFwIdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ضربة قاضية من طائرات إف-5 على القاعدة الأمريكية في الكويت خلال حرب رمضان.. الطيار الإيراني يتحدث:
تم التحليق على ارتفاع أقل من 50 قدمًا (بينما الارتفاع القياسي 500 قدم) لتجاوز دفاعات الكويت المتعددة الطبقات وأنظمة باتريوت.
العمل في صمت لاسلكي تام؛ على ارتفاع منخفض جدًا لدرجة أنها مرت بين سفينتين وكان سطح السفينة أعلى من الطائرة المقاتلة.
احتراق مروحيات العدو في الحظيرة  قُصفت قاعدة العدو بقنابل متطورة، ثقيلة، دقيقة، وساحقة.
دُمرت مروحياتهم المتطورة في الحظيرة نفسها قبل أي رد فعل.
دُمّرت القاعدة بالكامل، وبقوة ضاربة هائلة، لم نرحم العدو الغاشم.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79150" target="_blank">📅 21:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: ندرس حاليا فكرة توقيع مذكرة التفاهم من قبل رئيسي إيران والولايات المتحدة عن بعد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79149" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnC2xEeL0bxWlVJJzkBWUrCZVRSbllN1FlkVoBqL33g2BTBGX6Nk2rbxO-ZAxbzHNRN7xYFA7tqnr00a4FvUIK_CZcxuDnnzG99izX6TUJvR453k3Tg1JFJFEiuAxycfva2AMs-8h7DSWIvYP6EFdVLqwfCf5t4cTVdc54AQS_OR7enzbAQEPBOwwwpVDcg70m2BPz8aIZVvCbqIzYDRFefvnK9C6GdbUnJUiiJdooslPDYm6k-sMJB0iHXEFXfD_i7AHmGb5LCcJx8iXDI-qJIuS4yHhAZ8wn6OMHi33Gqj1yMdnmnhkbEw6fBP6sUHYpV1t5sF7wh4Z0X7PGEnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏اعلام الاميركي: ترجيحات بمقتل 8 من طاقم الـ B-52 التي تحطمت في كاليفورنيا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79148" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
ندرس حاليا فكرة توقيع مذكرة التفاهم من قبل رئيسي إيران والولايات المتحدة عن بعد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79147" target="_blank">📅 20:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني:
إذا كان المقصود أن علينا الاستسلام من أجل رفع العقوبات فذلك لن يحدث أبدا.
غير صحيح أن جيشي أمريكا وإسرائيل عديما الكفاءة ورغم قوتهما هزمناهما خلال الحرب الأخيرة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79146" target="_blank">📅 20:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O4IN9pbA9IGFCSx0tCkwIjaM73qxmw-hjMSeLrAa5xNc8j3Kx3xfMSE2CKCqBJdMFsZhflxp--viSApeYtXpWWHWwSa1TnfTRxVKAePS5SuU1tzW6fzpkHVKXjnOIT8xQltEo7bzYjNPUPgASiVnzU28qBrLI7589v_5N1obOJaOw-wrnOaOCVLNKkL1S0CR_KHsA8tr15ybXJjIPCV1q4WbLoKPNrfVMfnVKxWGjXQEF9ITwOOszdwHxylsB-V8LCfl4WXkzaRhSmnoFqRcspPULudSuHvXmPTVQNCM232VpVGWsZJ5tZsVV2AkHLVddkABD2jlt0MdGFziEG8fcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O4IN9pbA9IGFCSx0tCkwIjaM73qxmw-hjMSeLrAa5xNc8j3Kx3xfMSE2CKCqBJdMFsZhflxp--viSApeYtXpWWHWwSa1TnfTRxVKAePS5SuU1tzW6fzpkHVKXjnOIT8xQltEo7bzYjNPUPgASiVnzU28qBrLI7589v_5N1obOJaOw-wrnOaOCVLNKkL1S0CR_KHsA8tr15ybXJjIPCV1q4WbLoKPNrfVMfnVKxWGjXQEF9ITwOOszdwHxylsB-V8LCfl4WXkzaRhSmnoFqRcspPULudSuHvXmPTVQNCM232VpVGWsZJ5tZsVV2AkHLVddkABD2jlt0MdGFziEG8fcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد محمد بن سلمان.. ترامب: أفغانستان تقبل مؤخرتنا.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79145" target="_blank">📅 20:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=Gn2_1CGEj1uwdxmrWKOCvrHh8hk2CDqJLLDSwU5aiKboGAFxIfx-npuQVFpJhHkQShGpszdAayJjSo74Iz-dVXUfqz_v4HlqBdvP4jsU5bhUISugKEtebEzOKVhfcAOcruv6XY3W_bAxA87a36Lnq-rypfQbsHrMxPU5CI8DTZbskkY1D4BzOUmFdP6mjFGXN0PkUganSP96BWsBSgZjbekY8qxOohEGu-x7Pq6bKlWYcMlafgb5axQ0mhhVZ7rnZ4sjyc6rxoo6uF-MMjyNUGvHExMDArF0pbjnZwMBMmHFTNP4iTDZ9p-VBtX-6z-afjlNNa4s8BJMj9203i7U_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=Gn2_1CGEj1uwdxmrWKOCvrHh8hk2CDqJLLDSwU5aiKboGAFxIfx-npuQVFpJhHkQShGpszdAayJjSo74Iz-dVXUfqz_v4HlqBdvP4jsU5bhUISugKEtebEzOKVhfcAOcruv6XY3W_bAxA87a36Lnq-rypfQbsHrMxPU5CI8DTZbskkY1D4BzOUmFdP6mjFGXN0PkUganSP96BWsBSgZjbekY8qxOohEGu-x7Pq6bKlWYcMlafgb5axQ0mhhVZ7rnZ4sjyc6rxoo6uF-MMjyNUGvHExMDArF0pbjnZwMBMmHFTNP4iTDZ9p-VBtX-6z-afjlNNa4s8BJMj9203i7U_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن الحرب على إيران: أيضاً، ستنفد احتياطياتنا في غضون أربعة أسابيع تقريباً، كما تعلمون، هناك احتياطيات في جميع أنحاء العالم، وستنفد بالفعل، وسيكون هناك وقت لن تتمكنوا فيه من الحصول عليها.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79144" target="_blank">📅 20:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79143" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79142" target="_blank">📅 20:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=VjD-IZtVy6bx0J3UtUB8VZKfPD4VJJTvkp7urYmU4OVW9KTmlkvgf2ZAWERF_qzT3jShoxe9Dt46RPfiM4IR9hD7fEGUqZo-xWeq8sLX1ChcIHV3W-enpIho35ZD0-wko2xBO2q48y5LO9kPCsI43UQebF0RyBLIrfwgy0o1ywQENZaLaGOpb9S22Iv6IH_Kc6GzXfbQiwwBQwuuAolk69B1DOk25cErvYcmwZRz7ITNU5iAQdn9SB736j6gU_8SVldJtgPabUMbJDApo4FP2PddNouKtCf9BFK9lqK2p0BE-iBZQjMbUkUkXhhQ1QHgW7Kk-UOLAVWViqKYvlRRPy7OT4sIjOk_g4CDAgGfrwFFTasnE7fXPs7JH0hVQjHcpGZbmrpyB0b0Ky81WYu9kFU2Oq4PBNsFr6ZuEHf_kCJQJlJ9aUthPHBX_xBDZ2MTjbSoVmk0etAzyFUlOMRbYz6HSGtFzTxNltUgriheIqdr9Rk0-24SIWCUZOSTfu-ZUgBQGEXADbsQvM1qOZXj-sO13Keb-IUZJ-5JgGjem86xwyk7ypaP_zhcHNeohIlXgZKTGNINLeuPlDMRqm99IPR5ZSfsQZ9R9X_c4Dj__aovSTJy8mLfgsaj-gijaIPTI2z1AaGFEfb3ivaSIe9I5i0F8CCLBOTzIBoinhgG3OE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=VjD-IZtVy6bx0J3UtUB8VZKfPD4VJJTvkp7urYmU4OVW9KTmlkvgf2ZAWERF_qzT3jShoxe9Dt46RPfiM4IR9hD7fEGUqZo-xWeq8sLX1ChcIHV3W-enpIho35ZD0-wko2xBO2q48y5LO9kPCsI43UQebF0RyBLIrfwgy0o1ywQENZaLaGOpb9S22Iv6IH_Kc6GzXfbQiwwBQwuuAolk69B1DOk25cErvYcmwZRz7ITNU5iAQdn9SB736j6gU_8SVldJtgPabUMbJDApo4FP2PddNouKtCf9BFK9lqK2p0BE-iBZQjMbUkUkXhhQ1QHgW7Kk-UOLAVWViqKYvlRRPy7OT4sIjOk_g4CDAgGfrwFFTasnE7fXPs7JH0hVQjHcpGZbmrpyB0b0Ky81WYu9kFU2Oq4PBNsFr6ZuEHf_kCJQJlJ9aUthPHBX_xBDZ2MTjbSoVmk0etAzyFUlOMRbYz6HSGtFzTxNltUgriheIqdr9Rk0-24SIWCUZOSTfu-ZUgBQGEXADbsQvM1qOZXj-sO13Keb-IUZJ-5JgGjem86xwyk7ypaP_zhcHNeohIlXgZKTGNINLeuPlDMRqm99IPR5ZSfsQZ9R9X_c4Dj__aovSTJy8mLfgsaj-gijaIPTI2z1AaGFEfb3ivaSIe9I5i0F8CCLBOTzIBoinhgG3OE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران:  حسنًا، إن إلغاء التجميد - إنه سؤال سهل الإجابة عليه.   لقد أخذنا الكثير من أموالهم، وقد - أموالهم التي أخذناها منهم.   عندما لا تكون أموالنا، فهي أموالهم، وقد جمدناها في وقت معين.   أعتقد أننا سنضطر إلى إعادتها، أتعلم؟   إذا لم نقم بإعادتها،…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79141" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79140">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=ZalJeWOuYeyURHRSsMpbFjuJDS_vjY6torhNwxupl3cKSekLQCii9zrpqlDNB5-DWUbwAHNkjZN-MWS_fzyvfrvh5CZWgI0ykdN5smWX7QjGN1ElBiMYsKLChc5D_icmJWbDjyKYhCgmdh2OSsq0ddEEfIMwTiTlkOHoM1-HGLcAJpb5fm0o2oNtgtto9nWf95jRt3MMYFsSWWA3_juXT45OI4z2dVXfTfxQcguSCFV2dpdaMYTcvB0pAHCQ_WXOJA0ONlTHCvQBr7gg5jvyHdzXRnTggeayX4DXhzR2499GUNIxZw9pW4O9SkJfKfETxwsmnOzIG58gWPxj0I5ko1_bCfsFEUx988LguUVPgHtsudyhHlTp-kXgxgmg-H2_84N43MWFfPrppv8wclREm0oZcS9MU6UAgB8aLksBwcTARE5ncOBQPtET3x9cBh6u5qgx_Ln-EZt6cCPRNz_mKnQv83zzA-_yrru3uNzGof3qjODCIbhxZ5F3qa2v8xRtos8vGdhNkNT0Md2Bx5U2ybeJIXOFcalhXsh83KGChIF_jQccdO4q5Bbe-cUFwdbGmo-lk-WWTnKcC_aqKUuYohST5yVfGj4oAhCu3MCZbxNhGyltNdicbmr4Qs2Da1lDncNsrsWtaZ_gNWQbkXOQNiAROX2Ach0ay9WHfzuj-hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=ZalJeWOuYeyURHRSsMpbFjuJDS_vjY6torhNwxupl3cKSekLQCii9zrpqlDNB5-DWUbwAHNkjZN-MWS_fzyvfrvh5CZWgI0ykdN5smWX7QjGN1ElBiMYsKLChc5D_icmJWbDjyKYhCgmdh2OSsq0ddEEfIMwTiTlkOHoM1-HGLcAJpb5fm0o2oNtgtto9nWf95jRt3MMYFsSWWA3_juXT45OI4z2dVXfTfxQcguSCFV2dpdaMYTcvB0pAHCQ_WXOJA0ONlTHCvQBr7gg5jvyHdzXRnTggeayX4DXhzR2499GUNIxZw9pW4O9SkJfKfETxwsmnOzIG58gWPxj0I5ko1_bCfsFEUx988LguUVPgHtsudyhHlTp-kXgxgmg-H2_84N43MWFfPrppv8wclREm0oZcS9MU6UAgB8aLksBwcTARE5ncOBQPtET3x9cBh6u5qgx_Ln-EZt6cCPRNz_mKnQv83zzA-_yrru3uNzGof3qjODCIbhxZ5F3qa2v8xRtos8vGdhNkNT0Md2Bx5U2ybeJIXOFcalhXsh83KGChIF_jQccdO4q5Bbe-cUFwdbGmo-lk-WWTnKcC_aqKUuYohST5yVfGj4oAhCu3MCZbxNhGyltNdicbmr4Qs2Da1lDncNsrsWtaZ_gNWQbkXOQNiAROX2Ach0ay9WHfzuj-hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-06-2026
ناقلة جند تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبيّة لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79140" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c093a28307.mp4?token=PWA78GswI3w35KVRutouPwOmEKqc1nlcdo7DCvDinguctf-lOB87JLqjjoNOUgckFNV_utDHLJlpqE7Rt4i-DgNLFwfh343G5NGbFmoWjDQ1RTVdi55K7DwMfIJX8XdiTUTSQGamaD6pZDQpADebFqof4eu001cZrg1UteIbOsyVlFXz0rp4ZSUHmMbYUzQ4z5rM296YPYI9m4j0ZwSp0qsKID1pCbaqF8P0FcX7DLTs2HrhJ2Fjyvh1LTT2FvcmdHv_MIKAyS2RT129GebYCnpo6tG-geKO-nliKc-RWYysWBvXe3eLu1oplzsShmy8ZoB9o14VkdBbn4kdrHDaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c093a28307.mp4?token=PWA78GswI3w35KVRutouPwOmEKqc1nlcdo7DCvDinguctf-lOB87JLqjjoNOUgckFNV_utDHLJlpqE7Rt4i-DgNLFwfh343G5NGbFmoWjDQ1RTVdi55K7DwMfIJX8XdiTUTSQGamaD6pZDQpADebFqof4eu001cZrg1UteIbOsyVlFXz0rp4ZSUHmMbYUzQ4z5rM296YPYI9m4j0ZwSp0qsKID1pCbaqF8P0FcX7DLTs2HrhJ2Fjyvh1LTT2FvcmdHv_MIKAyS2RT129GebYCnpo6tG-geKO-nliKc-RWYysWBvXe3eLu1oplzsShmy8ZoB9o14VkdBbn4kdrHDaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يسخر من محمد بن سلمان:  لقد تحدثت إلى ولي العهد السعودي عدة مرات - إنهم سعداء للغاية لأنهم لا يزالون... يجب أن تجعلهم سعداء أيضًا، أتعلم؟   نحن نستخدم مطاراتهم، وليس أنهم يمكنهم إيقافنا إذا لم نرغب في ذلك.   ذهبت للحصول على ذلك الوغد الصغير. لكني أخطأت.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79139" target="_blank">📅 20:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79138">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvr--IaivEkw9Mp_lPCNPCCFUqXGvO3aJLWfWrmXINTp3QUcfoWxch99V5Bk6MtKCPK1xVVPQKV0Vp3ulJlI-Ri1HEBP82sFIcyOo2r1D7zrY4CwcTQPLtDRD76DdJ1gUmGMRXPG_KQy3uIdcXmPh9xozzU2rtUZtg0phwJuLkbBAc6-ydk2PoWvC_3zdGNG5HrIhEOnsHGDKrtDjDATmoZiHZutXgBQEzajbjZAYUdbJG9a2r8LcCrl2MFopqzCDn9AV-pjC9yEwoscGwTcyRnLzKC8MfJONnQsg6tXB4_ypnU4uV_gmiZ7p9MJDba-l7ckVRjUwWjzGJVfx9BMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ إعتراضية في سماء مستوطنة المطلة في الشمال الفلسطيني المحتل دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79138" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=cXzwuaOEh7KMM79Eucne7h-4UJgCcKYIZOe7R86tueImSTHeD62syMZ5bmMzdHxWxB-tIxGbX0a4B_D7esz8W2MInKpWwHIWLjffdel8iqLPfYgDmGg0tYIOpnXspwh-ELGpxydq9DW5skSDA7WCUG6Y0cBCKjlaMfciwVHE2rGXUFM5Q3NjVyinWYQoM-GyOcdDHEiRNs5QQxGhp0m0qVRazGTbVuOpnzLgnZTTDT8pjtIQMZ-erp7Znhc9KgCT6qse_UKqneNe9Etl_efPVJuLmnpB8DXHnNvh6DbrOPJqmp9-kLTwPnFAzufs4PT9q5Fd4UPxltQhXMii5DF9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=cXzwuaOEh7KMM79Eucne7h-4UJgCcKYIZOe7R86tueImSTHeD62syMZ5bmMzdHxWxB-tIxGbX0a4B_D7esz8W2MInKpWwHIWLjffdel8iqLPfYgDmGg0tYIOpnXspwh-ELGpxydq9DW5skSDA7WCUG6Y0cBCKjlaMfciwVHE2rGXUFM5Q3NjVyinWYQoM-GyOcdDHEiRNs5QQxGhp0m0qVRazGTbVuOpnzLgnZTTDT8pjtIQMZ-erp7Znhc9KgCT6qse_UKqneNe9Etl_efPVJuLmnpB8DXHnNvh6DbrOPJqmp9-kLTwPnFAzufs4PT9q5Fd4UPxltQhXMii5DF9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏إن توسيع نطاق اتفاقيات أبراهام هو الأمر الآخر الذي نأمل أن نحصل عليه. ‏وأعتقد أن المملكة العربية السعودية، إذا قادت الطريق، ستكون قد قدمت خدمة كبيرة لنفسها.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79137" target="_blank">📅 20:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
🇸🇾
‌‏ترامب: الرجل المحترم في سوريا، الذي أصبح الآن رئيسًا لها، قام بعمل رائع، فقد أعاد بناء ذلك البلد في عام ونصف، مثل بلدنا إلى حد ما، عام ونصف، بحجم مماثل تقريبًا.  ‏قالوا: "لا، من فضلك لا تضعهم هناك، إنه رجل عنيف للغاية، من تنظيم القاعدة".  ‏قلت: "حسنًا،…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79136" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79135">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=XsCI2e9VKqzdn47aIDn10OBnJBehJfpjHdeAvKNXuBUIIve4oFnxyxlMqlSZ4znFTfKeEOupPIKczlfJlx-RgOb6kvA2BOP7dKS6uAQ5tpQ3XGDFo4rlWZsdR4lNRoa3p6GyyllO5d27gT5TXeQVwCgwjlQGEbhrxpmTG4JSWIvnkJzWV6EgE0jKv7nX6BGWRsge6wrgLloYh5A8Ysv5-32VnJD7jUy1kt6W8-VCyrq-4m4G4NsYnMsU-BxbGfj2SVHw7EBchyxB2J5hcaZtZP51Bjw3Pe5WkpPZWptEldQ_C_h1p4POaqrOTNziTAEQAMY_N5OgJ15JYsMSansiVzfwuVtpJNWvbtK4RPHIgTm5JgTh9YYZW89TPCFuuTPFcJHu6mfIC6RI36LxTlv7-s_PLcyzDRinzn0wXPjo_wN-Al2dJHoLS_ABd2E5ZcuOZ0bgqDXUUZZEv59Ii5DFYbYHXzMlK0JUVKMaijZ9NIG4A4DSdn0A1VDDs8lFcINiuETeMNXBtv9XzdrIR_mJWEdezOpd27JEYJ8S_zUeQwFouA1oM0oA2ILBID55LWLqxXTfB28hxnfa5hjY_ovxp7XsTFaN-LTvkQu5qp_60PlyppRoGxvzoQ2uSgnqdx408EFoLSKy2-7hWJfGxdMD7fkYnBX0Od8tcqmt375y3sM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=XsCI2e9VKqzdn47aIDn10OBnJBehJfpjHdeAvKNXuBUIIve4oFnxyxlMqlSZ4znFTfKeEOupPIKczlfJlx-RgOb6kvA2BOP7dKS6uAQ5tpQ3XGDFo4rlWZsdR4lNRoa3p6GyyllO5d27gT5TXeQVwCgwjlQGEbhrxpmTG4JSWIvnkJzWV6EgE0jKv7nX6BGWRsge6wrgLloYh5A8Ysv5-32VnJD7jUy1kt6W8-VCyrq-4m4G4NsYnMsU-BxbGfj2SVHw7EBchyxB2J5hcaZtZP51Bjw3Pe5WkpPZWptEldQ_C_h1p4POaqrOTNziTAEQAMY_N5OgJ15JYsMSansiVzfwuVtpJNWvbtK4RPHIgTm5JgTh9YYZW89TPCFuuTPFcJHu6mfIC6RI36LxTlv7-s_PLcyzDRinzn0wXPjo_wN-Al2dJHoLS_ABd2E5ZcuOZ0bgqDXUUZZEv59Ii5DFYbYHXzMlK0JUVKMaijZ9NIG4A4DSdn0A1VDDs8lFcINiuETeMNXBtv9XzdrIR_mJWEdezOpd27JEYJ8S_zUeQwFouA1oM0oA2ILBID55LWLqxXTfB28hxnfa5hjY_ovxp7XsTFaN-LTvkQu5qp_60PlyppRoGxvzoQ2uSgnqdx408EFoLSKy2-7hWJfGxdMD7fkYnBX0Od8tcqmt375y3sM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب بشأن حماس: ‏عندما ولدوا، خرجوا وفي أيديهم رشاش.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79135" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79134">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=qg8lY1xyphEwuoSgF6tnq8TF4GaPwuCb9SL0j8m5SbRS2eEtuBsQOTpKEf3EDTrFySotiFj-Y_0lpVfrdRiCLw6_Vr1UGiq81doFDFe_HRn84D_ytJQozPOryp3Kniat_CjaYx0DqOeSc3m_c1BKl6nw00y7H7JPqWDzzU15wsvzA0r3uIht4JfOyyTxLd1lsZOJUtpbNh7g4EcrlC1cATOrAqGO4lMrDVwOomFhDeLdViHuZ8rh2uMqdE_C73MXQnRD5hN4f8rRGdmVtuzGpIx8wFq1gAT0FRlXAbKtZH2LdnnC4S5knVThEnq22RXQ6e7-gxsQbXd65dnm4B3u7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=qg8lY1xyphEwuoSgF6tnq8TF4GaPwuCb9SL0j8m5SbRS2eEtuBsQOTpKEf3EDTrFySotiFj-Y_0lpVfrdRiCLw6_Vr1UGiq81doFDFe_HRn84D_ytJQozPOryp3Kniat_CjaYx0DqOeSc3m_c1BKl6nw00y7H7JPqWDzzU15wsvzA0r3uIht4JfOyyTxLd1lsZOJUtpbNh7g4EcrlC1cATOrAqGO4lMrDVwOomFhDeLdViHuZ8rh2uMqdE_C73MXQnRD5hN4f8rRGdmVtuzGpIx8wFq1gAT0FRlXAbKtZH2LdnnC4S5knVThEnq22RXQ6e7-gxsQbXd65dnm4B3u7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
‏ترامب عن محمد بن زايد: ‏محمد في الإمارات مقاتلٌ لا يُستهان به. كان يُلقي القنابل الأسبوع الماضي، فقلتُ: "من بحق الجحيم يُلقي كل هذه القنابل؟"، كانت الإمارات. إنه مقاتلٌ بارع.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79134" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
