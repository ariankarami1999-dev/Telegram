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
<img src="https://cdn4.telesco.pe/file/KEpbMtAUAUHx6xRkQ1PyrR0B7qORyftpajmtBDAZ0omrbrEbEJN231C-04sbKzH9SjwPqvuhtyI1Q3grPBOadhweWZKgpZUUY7GhiL_zr-yUF56K5oeNOHYCmhCBwVrElfmyyNswuvjJWfrIDW8v1myjFhKwORrLgc1x7jHg6lL6PWed0iq9p4AvmnKw4Lm-Oh6XK8T4qpoN9zYF0pWm89MiY9EPgRh48oY0JwinTSm7cVE2zUTEAlieYQSJ0ro4f742eqOOtd7O4xQxIi5zpGhiaUUZ_Skx8S5fdAMFpjVaJLIwOjjqT6wXbolZybvbRWiJXu9y4C4zSV-o7fw2gA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 02:09:42</div>
<hr>

<div class="tg-post" id="msg-84091">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الجيش الأمريكي: ‏ بدأت القوات الأمريكية اليوم، في تمام الساعة السادسة مساءً بتوقيت شرق الولايات المتحدة، شنّ غارات جوية جديدة على إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الغارات إلى تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز،…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/naya_foriraq/84091" target="_blank">📅 02:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84088">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d2c62fd5.mp4?token=UJfSpJfLRkzdfUJ2S2AbNQ4yXFajxLQWYSO_eK0yDch9qmBTjJDR8jgJZwRjQM-FHKPApV6-2CFa6wHyUlSnbOCEnH0zv_0vwPf7Zrnbc_OOMVkWZc0f1ADokhBrwRf8GldORWVd8AdPAyfvdj7GCFfs_ztmb_7UbZISiNjsyPLCyveYfjhtc0KipaSr34lgajBuKccptXfPh-q70sxy5BpmTj0wRXCFKe61x01snsPqzHDtXRXWPsGKgFeLmSyLtUTudxuokBOw2Q-cDZumtuiBilnGoDjUY3yNfvm6jb31iO_EbeJ56BlSVtU2mvhrttPKt8j23h6VVLWPnxCGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d2c62fd5.mp4?token=UJfSpJfLRkzdfUJ2S2AbNQ4yXFajxLQWYSO_eK0yDch9qmBTjJDR8jgJZwRjQM-FHKPApV6-2CFa6wHyUlSnbOCEnH0zv_0vwPf7Zrnbc_OOMVkWZc0f1ADokhBrwRf8GldORWVd8AdPAyfvdj7GCFfs_ztmb_7UbZISiNjsyPLCyveYfjhtc0KipaSr34lgajBuKccptXfPh-q70sxy5BpmTj0wRXCFKe61x01snsPqzHDtXRXWPsGKgFeLmSyLtUTudxuokBOw2Q-cDZumtuiBilnGoDjUY3yNfvm6jb31iO_EbeJ56BlSVtU2mvhrttPKt8j23h6VVLWPnxCGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولة التصدي</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/naya_foriraq/84088" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84087">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5bfaab8b.mp4?token=LyscgWvWY3He7NgOm0s5iQ5DRA2xpgfXLzShkSpvC4IfjgEUGUBEwfj-1qcGz_Adv-D0M4Z4hVi-5Bp6GbmokNrnsAfFemr35CrkKu3eXWEtZXKEn0O0nlBl6vlUNHr39GroT0E563GxUAM3EfXuPw_qWoOBHOB1KIeYF3JMkqkU1TU9ztfXWYrOAiTxt9dP0M5wJaRU_FEoveYfTVRIeB2XiMD0R5op0iw40TfPJLb2P1E3gKOE46H_BrLQd0O6WMmUGaSmEeQ-asgYGj86Ca8MgX667bZ1drgvpcuNnUxwLsDX5loN3gqovdYhfiHIF2n46j4USgwccmsUjpikrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5bfaab8b.mp4?token=LyscgWvWY3He7NgOm0s5iQ5DRA2xpgfXLzShkSpvC4IfjgEUGUBEwfj-1qcGz_Adv-D0M4Z4hVi-5Bp6GbmokNrnsAfFemr35CrkKu3eXWEtZXKEn0O0nlBl6vlUNHr39GroT0E563GxUAM3EfXuPw_qWoOBHOB1KIeYF3JMkqkU1TU9ztfXWYrOAiTxt9dP0M5wJaRU_FEoveYfTVRIeB2XiMD0R5op0iw40TfPJLb2P1E3gKOE46H_BrLQd0O6WMmUGaSmEeQ-asgYGj86Ca8MgX667bZ1drgvpcuNnUxwLsDX5loN3gqovdYhfiHIF2n46j4USgwccmsUjpikrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابات مباشرة تدك مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/84087" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84086">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اصابات مباشرة تدك مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/naya_foriraq/84086" target="_blank">📅 01:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84085">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الجيش الأمريكي: ‏ بدأت القوات الأمريكية اليوم، في تمام الساعة السادسة مساءً بتوقيت شرق الولايات المتحدة، شنّ غارات جوية جديدة على إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الغارات إلى تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز،…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/naya_foriraq/84085" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84084">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTD3mdfa9540cLZD-jlv0jtEa6KmrQUc_50kabiQObftEoheDHn_vGl6--2OW54eNln473N9G8ns5W0F8I53rNNXwk5DOEYsqlMtjGc7RY1SLcLBSxNCwRhpxnTtl1sIAxsiedGAuZxF6C8NxWSjlswyak5fAaMh_s9ojwMIyqSZlgl0anthGyICfvdiNIJTqISqxrSy7JHT_r5NtqvNclcssY50iRoearmdG9GYrrir5QEE0oOcUtgyTNshUSoEnl3SBAF_PrZdnZQMdPVatFrUxPP6x4QgzOPpXPqOZmw8U8V7vkvZhiGtF5MYoLs-VYEYmp5xPIKVXlTJHRjlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
Trump said months ago that Iran has no radar, no communications, and basically few to no missiles and missile launchers left. What's all this panic? Just go home and relax. Trump destroyed Iran back in March.</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/naya_foriraq/84084" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84083">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9fba2651.mp4?token=j18PQ9IuoPvuNjGamyDVw3dvkfM9TERBM-OaW6elfZtfR5wLEaQ_C08Bk52CDg3XR1EyT4W5DEKJbfErZ1wyMupY-tVBpmWtQOsJLAWo6YbI5yyAhOg290EDj8eBCln65w0bx0R6Ki_mii4h6XDc1aPfhy0PSWl5DiKFYcy7l7Z8qam6RqxrNEhRadB1VpYQKTyOqUijSCewMVMqePYNwXeCQK2FankNl_0L2apgnk8VCjkrpUEkJucXEoinEL22xNuYaP8FkDGj5qaBMm2GkiWop74y6VPN-wrj0jRVISUE3pRawb5vP4eb8xVqTe8FBb1AZUh3xF3CcuyiLDG0hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9fba2651.mp4?token=j18PQ9IuoPvuNjGamyDVw3dvkfM9TERBM-OaW6elfZtfR5wLEaQ_C08Bk52CDg3XR1EyT4W5DEKJbfErZ1wyMupY-tVBpmWtQOsJLAWo6YbI5yyAhOg290EDj8eBCln65w0bx0R6Ki_mii4h6XDc1aPfhy0PSWl5DiKFYcy7l7Z8qam6RqxrNEhRadB1VpYQKTyOqUijSCewMVMqePYNwXeCQK2FankNl_0L2apgnk8VCjkrpUEkJucXEoinEL22xNuYaP8FkDGj5qaBMm2GkiWop74y6VPN-wrj0jRVISUE3pRawb5vP4eb8xVqTe8FBb1AZUh3xF3CcuyiLDG0hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابة مباشرة والنيران تشتعل في مرتفعات خليفان</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/naya_foriraq/84083" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84082">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/84082" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84081">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8926a4c0e.mp4?token=dkRoRaDqBQ-k4UrMw4Ju6wx5ejPhC-lUgRA-YsL9XY9ULauskCGPzMzN2Pc2Q1A9o-Gfmpo703EDXYGu4bLo4f5QBr3ZfQkmL--staNovvyYwZ0BHNkYF8ffTTnQnlPCtw48AzWb-Y0KQUixuHS0_ZizRLUob4YtDw7YxDQWNWcP5pkLuchzW4PejTVHPHHpBjoG5hx23wUKudsWbCjVaI8lbgaGwFUm4SMy10rTaCl_t9zUGS087VG2rKkj9xhQpASFzgkFHEArSJA7TYT218-l-hP0Q07cj0BtiOu42RrQRCX8yKW7Ie-PsLg9ORGwZfQcVl4lXLetS-s6apcKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8926a4c0e.mp4?token=dkRoRaDqBQ-k4UrMw4Ju6wx5ejPhC-lUgRA-YsL9XY9ULauskCGPzMzN2Pc2Q1A9o-Gfmpo703EDXYGu4bLo4f5QBr3ZfQkmL--staNovvyYwZ0BHNkYF8ffTTnQnlPCtw48AzWb-Y0KQUixuHS0_ZizRLUob4YtDw7YxDQWNWcP5pkLuchzW4PejTVHPHHpBjoG5hx23wUKudsWbCjVaI8lbgaGwFUm4SMy10rTaCl_t9zUGS087VG2rKkj9xhQpASFzgkFHEArSJA7TYT218-l-hP0Q07cj0BtiOu42RrQRCX8yKW7Ie-PsLg9ORGwZfQcVl4lXLetS-s6apcKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران ترتفع من مرتفعات خليفان</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/84081" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84080">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اصابة مباشرة</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/84080" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84079">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf6625b3b.mp4?token=gMzEDzbS_S8SQmhTCSvdsuCCul_fuVxcILt2kJCmbLRuC62XkVFeqxaeX-1YHgrp68g3df0LaCQH-fAjw08f7xdJGzebVTO5X9YLk2_-43OLMSz_uncoqXt_HalmVcp6-E7I5vd7-JSUK7NLDHW6oleyB99W5UZLOR1d7HTC14M9m819BxU5ilwM8Y54s8CrdOdsgvmrqKAuztAigI9K2Vp9Wc-GcvCDenJmLTXdqRVK2iL9K4gWc8dBmKNHFUDgtNqpCdNFvbFR1iTg4anS0Pw3bpBQTshj9WI206EnJSp_cpJ_4EQ8XWi_0zomFmliRY944kIfsURCi_uPdkqBrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf6625b3b.mp4?token=gMzEDzbS_S8SQmhTCSvdsuCCul_fuVxcILt2kJCmbLRuC62XkVFeqxaeX-1YHgrp68g3df0LaCQH-fAjw08f7xdJGzebVTO5X9YLk2_-43OLMSz_uncoqXt_HalmVcp6-E7I5vd7-JSUK7NLDHW6oleyB99W5UZLOR1d7HTC14M9m819BxU5ilwM8Y54s8CrdOdsgvmrqKAuztAigI9K2Vp9Wc-GcvCDenJmLTXdqRVK2iL9K4gWc8dBmKNHFUDgtNqpCdNFvbFR1iTg4anS0Pw3bpBQTshj9WI206EnJSp_cpJ_4EQ8XWi_0zomFmliRY944kIfsURCi_uPdkqBrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مرتفعات خليفان بمحافظة اربيل شمالي العراق التي تضم قاعدة الحرير الاميركية</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/84079" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84078">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a68e1d05.mp4?token=WL5qC1aC9GDd9MumuXgbSkkI0o8ZPbLTISB4E3of0p0PCyjCaRhoti2Qwp0RxPIqXYyMoWmI4VN9XpD6lvggldVzAP733rYTn0m0Gwadq6C-xtDF6B1pJ2b0xXhdkdoTSsyF7ZwWZbFR1T1BVDsOAs2yXZtysLgrdLM-Rhx92yhYltfXC_3fTTYgseTVJiQ9xA5_2qmauPpx_NDwb_ugyMshWuQNP2lIrFnaF5jFDKG-IJD3ukqXcjfoHh8plC4eK_z6BfVGTW77V8p7Ciel2v2cRIFvKxQHRJ955eGp-Rogfo3H-JbDPNxeAon_5bgMTzUYuWuHs29uUybTdhcJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a68e1d05.mp4?token=WL5qC1aC9GDd9MumuXgbSkkI0o8ZPbLTISB4E3of0p0PCyjCaRhoti2Qwp0RxPIqXYyMoWmI4VN9XpD6lvggldVzAP733rYTn0m0Gwadq6C-xtDF6B1pJ2b0xXhdkdoTSsyF7ZwWZbFR1T1BVDsOAs2yXZtysLgrdLM-Rhx92yhYltfXC_3fTTYgseTVJiQ9xA5_2qmauPpx_NDwb_ugyMshWuQNP2lIrFnaF5jFDKG-IJD3ukqXcjfoHh8plC4eK_z6BfVGTW77V8p7Ciel2v2cRIFvKxQHRJ955eGp-Rogfo3H-JbDPNxeAon_5bgMTzUYuWuHs29uUybTdhcJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ ومسيرات تنقض على الاهداف المعادية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/84078" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84077">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d074ad9a.mp4?token=CXBCw3pG6LE21UPaslAw42QdkX_yPyg4TgBkc5kquAwADiwMYSQBHSOSRjRfhBh2IHuMOStHK05DWdEqhas_nvI_WG4oiEhq427i5rGjRE1qoCkTGGhf5XSZVRL2JaARW8g6UzvTzm04hvZo8Me25FqqPwSkiZiP3smUgKLVBUBKIa3yHBmassvFzygbYh-_fWNvqG1BLjJczFQHiqD2f5PIWyaHTUmSBkWBUX7UjznkDNwxff4oR1cS5vxzBOkPfK9O8mgd2w9Y3HoKkCT-NXo0AD7oNMyZoYvmGzfuiG4Fsq4FbXFZqMHfDg3dYRf6URpxsdI-02_oYVZqTaifaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d074ad9a.mp4?token=CXBCw3pG6LE21UPaslAw42QdkX_yPyg4TgBkc5kquAwADiwMYSQBHSOSRjRfhBh2IHuMOStHK05DWdEqhas_nvI_WG4oiEhq427i5rGjRE1qoCkTGGhf5XSZVRL2JaARW8g6UzvTzm04hvZo8Me25FqqPwSkiZiP3smUgKLVBUBKIa3yHBmassvFzygbYh-_fWNvqG1BLjJczFQHiqD2f5PIWyaHTUmSBkWBUX7UjznkDNwxff4oR1cS5vxzBOkPfK9O8mgd2w9Y3HoKkCT-NXo0AD7oNMyZoYvmGzfuiG4Fsq4FbXFZqMHfDg3dYRf6URpxsdI-02_oYVZqTaifaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة يشهدها اقليم كردستان العراق حيث أماكن تواجد القوات الأمريكية ومقرات إرهابيي المعارضو الكردية الإيرانية</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/84077" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84076">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات تهز السليمانية مجددا</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/84076" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84075">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">استهداف مرتفعات خليفان بمحافظة اربيل شمالي العراق التي تضم قاعدة الحرير الاميركية</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84075" target="_blank">📅 01:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84074">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c486bb3616.mp4?token=THzQyyUHolfbydSMbfSn8rg48ytWnPc7nOEZaPZkwMwtZOI90iynLbH9ownJJw62BFNIlJFnzKJ4ysLE7VLAtJvvwcQKg1Z_xkjQSGN3-kYtJMHviQPPbNryP6scAPxJ1M1Mwdxe5SE7QxM1Fq55wKSbN1tTDIwQnR7TwIUzfC674Ldv35QyuZS58AgDc9ltRLtAu95phe104Op0lf78jcmkcfxozv43ImxB1HD4AJrRR-Tvtds6B5qRXMAvW6VG0OVap8RlFOi3mEFZJdSfoGW2wWwA4MyabtN1tMDyWoo9KVkFQlAqEdp3tnBSy4KvvArDAqCNchavIQpHPKVq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c486bb3616.mp4?token=THzQyyUHolfbydSMbfSn8rg48ytWnPc7nOEZaPZkwMwtZOI90iynLbH9ownJJw62BFNIlJFnzKJ4ysLE7VLAtJvvwcQKg1Z_xkjQSGN3-kYtJMHviQPPbNryP6scAPxJ1M1Mwdxe5SE7QxM1Fq55wKSbN1tTDIwQnR7TwIUzfC674Ldv35QyuZS58AgDc9ltRLtAu95phe104Op0lf78jcmkcfxozv43ImxB1HD4AJrRR-Tvtds6B5qRXMAvW6VG0OVap8RlFOi3mEFZJdSfoGW2wWwA4MyabtN1tMDyWoo9KVkFQlAqEdp3tnBSy4KvvArDAqCNchavIQpHPKVq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة يشهدها اقليم كردستان العراق حيث أماكن تواجد القوات الأمريكية ومقرات إرهابيي المعارضو الكردية الإيرانية</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84074" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84073">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اربيل مجددا اصوات انفجارات</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/84073" target="_blank">📅 01:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84072">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الجيش الأمريكي:
‏
بدأت القوات الأمريكية اليوم، في تمام الساعة السادسة مساءً بتوقيت شرق الولايات المتحدة، شنّ غارات جوية جديدة على إيران بتوجيه من القائد الأعلى للقوات المسلحة. وتهدف هذه الغارات إلى تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز، ومعاقبة قوات الحرس الثوري الإسلامي التي شنت هجمات على جنود أمريكيين في الأردن الليلة الماضية.</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/84072" target="_blank">📅 01:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84071">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هجمات تطال القاعدة الجوية الأمريكية قرب مطار أربيل</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/84071" target="_blank">📅 01:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84070">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اربيل مجددا اصوات انفجارات</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/84070" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=cKimJqNO40-m6LSt72Zzo7slpoagHryTZre-B0R6mInnV5ArYm0fkuLxlenEdCD-hB1SxgbExoz7An_-jj6O-lBFmD39ZbpWLoP-t1q6NM2maVVHImc31tmLW0utMrnPx2D0z8PLHplORYPIv0S5eAwVWPwu-tc5qY8ZuCadAeJOCw2hZurEmJywmJlNMpsDQH01F2vK95i14fS1VXdt35BwJIPTxJuEmcqwu-Iyte3tPOdTis89RNBOVCHxbn_G2L_WdBMswYid40LKnK74O-QGU5DNFC9nWBdztHALet02Ds2xoWSuioyXRNdc30QKBw-uOWiQba0XA7l0Utzaug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=cKimJqNO40-m6LSt72Zzo7slpoagHryTZre-B0R6mInnV5ArYm0fkuLxlenEdCD-hB1SxgbExoz7An_-jj6O-lBFmD39ZbpWLoP-t1q6NM2maVVHImc31tmLW0utMrnPx2D0z8PLHplORYPIv0S5eAwVWPwu-tc5qY8ZuCadAeJOCw2hZurEmJywmJlNMpsDQH01F2vK95i14fS1VXdt35BwJIPTxJuEmcqwu-Iyte3tPOdTis89RNBOVCHxbn_G2L_WdBMswYid40LKnK74O-QGU5DNFC9nWBdztHALet02Ds2xoWSuioyXRNdc30QKBw-uOWiQba0XA7l0Utzaug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء محافظة أربيل تشتعل وسط تفعيل منظومة السيرام وهجوم إيراني واسع</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/84068" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اصوات انفجارات عنيفة في تقاطع قادر كرم بين كركوك وسليمانية</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/84067" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ef38c4d2.mp4?token=OU3RA4jToLb9NaKKMO9TCjB2dRCR9DTmTYXqDl5TUrTLT3FFEEC4sxdOAReedM-0cnJ0wMQzY5eczQGksB3XJZxEZWutZD0IHSZ9qKVlcMdKexAAbK8l-Yaiu_7T2CeG7RKhBQgars-mmlr2OJ2gShZeZftwxq56alNCVyy7EPg1Ou-29e52-pkXH9Cbl0997ACL2-6iCTlGBnLg-1sA-t95LvaA4djw5pnvOv5lr7xJ1IdIid1ASd8IWkOHyUXysYcxKdAvmG77wwG9sgILRbcrO9iR_75eTegq6N7xow4as5dl9qA8LUW21yTmu2o-WwedLGmv52DVLfDN9va96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ef38c4d2.mp4?token=OU3RA4jToLb9NaKKMO9TCjB2dRCR9DTmTYXqDl5TUrTLT3FFEEC4sxdOAReedM-0cnJ0wMQzY5eczQGksB3XJZxEZWutZD0IHSZ9qKVlcMdKexAAbK8l-Yaiu_7T2CeG7RKhBQgars-mmlr2OJ2gShZeZftwxq56alNCVyy7EPg1Ou-29e52-pkXH9Cbl0997ACL2-6iCTlGBnLg-1sA-t95LvaA4djw5pnvOv5lr7xJ1IdIid1ASd8IWkOHyUXysYcxKdAvmG77wwG9sgILRbcrO9iR_75eTegq6N7xow4as5dl9qA8LUW21yTmu2o-WwedLGmv52DVLfDN9va96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/84066" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84065" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84062">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBF7Kphaoa11pJfwEoL1ffNnFVNoHM_YnOxZ3K1BPpmwyhZvB4HD2YldxCVz8VD0XJ6LDziPq0FK_OndDjFo2qi6Ek5Jws-Op9zpi1FTpScD5PhBqcLaTZYZ2LOnhEy9-6j1zNs_WOcnLYSpZ4jsEwXeEToneSBdAhm44yMw4Gt_YTR5raebd558qnf0AKI6mCkjHl8JVlpmeOGuMvEvFTYrp-Eh0zEoPHLlI1DFC7VGhUCcerasIWe7i5zrqrppPyOOUKobLpTQC4m-9JiR0vVzjW1C55_na5rMS_nBgqU9sCLoz0i3_q3TyMNst96D-5EbFLkYDBsn4k5ICSJzXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4197f5de8.mp4?token=CNxmkwhBbK7FRxac7PF6bV6VldRcIjoZ-UiIQzDXp55ZvYXDSA8BjegYw6zTtbUyJEz4vHLNfeFvt8Iv8yhWuU0vs0NU9hLoygG7v-zZfaahDaLDvEr6FZN_RMKli01CW4vFlZbWDFDmPqbiD5gxyycijinC3Z_vvItXBsj0tkvw6x-GIMpj0TnB2a5y0CB56L1XQibNSoKH_K2WGY7Fc3hNhZFnUmv1AARQahYnld4-FYiYcFsV133JVAtBpMLMee_tyrD_fbOujGKEDsrvmYl8-coxFY7-PyvGGLu7hLq76lXEKN7cT36_p5cNz0jtLItZ2wHBNXZt_hAC44faZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4197f5de8.mp4?token=CNxmkwhBbK7FRxac7PF6bV6VldRcIjoZ-UiIQzDXp55ZvYXDSA8BjegYw6zTtbUyJEz4vHLNfeFvt8Iv8yhWuU0vs0NU9hLoygG7v-zZfaahDaLDvEr6FZN_RMKli01CW4vFlZbWDFDmPqbiD5gxyycijinC3Z_vvItXBsj0tkvw6x-GIMpj0TnB2a5y0CB56L1XQibNSoKH_K2WGY7Fc3hNhZFnUmv1AARQahYnld4-FYiYcFsV133JVAtBpMLMee_tyrD_fbOujGKEDsrvmYl8-coxFY7-PyvGGLu7hLq76lXEKN7cT36_p5cNz0jtLItZ2wHBNXZt_hAC44faZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/84062" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84061">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اصوات انفجارات عنيفة في تقاطع قادر كرم بين كركوك وسليمانية</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84061" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84058">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac91c700b7.mp4?token=CuziVxFnsAD3CBqsM9rcYywyz_P-xwpKKB1b7Kta1HrAW0R8c1hwqJOKVfZDLj0jypDi22GGh3mcn72gbzjLPmFJXfg72XuFe_I45XP132OO3T6CafxD5hKFxLZ0Nnuv4JTMJvGqxdEJiYf95Ohdtu0kvukbqIGTYsM_JKYbqQORBXIODg6sltAABzNInTpGmjELCjhV0_4M-688upo-pBZapEtRWuVVVC-4j35P34XFElGXBSZG_gJ3q_-bdNK77kXg9Bb2CA4D6H4IJi8HFOPpFGd7kXs7xCz94kBq3_Mr3UWBT2kF24CdPJgXlKZUZF3smWLQS2sXoRn9J2hafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac91c700b7.mp4?token=CuziVxFnsAD3CBqsM9rcYywyz_P-xwpKKB1b7Kta1HrAW0R8c1hwqJOKVfZDLj0jypDi22GGh3mcn72gbzjLPmFJXfg72XuFe_I45XP132OO3T6CafxD5hKFxLZ0Nnuv4JTMJvGqxdEJiYf95Ohdtu0kvukbqIGTYsM_JKYbqQORBXIODg6sltAABzNInTpGmjELCjhV0_4M-688upo-pBZapEtRWuVVVC-4j35P34XFElGXBSZG_gJ3q_-bdNK77kXg9Bb2CA4D6H4IJi8HFOPpFGd7kXs7xCz94kBq3_Mr3UWBT2kF24CdPJgXlKZUZF3smWLQS2sXoRn9J2hafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات هي الاعنف في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/naya_foriraq/84058" target="_blank">📅 01:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84057">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51e0d7ccf.mp4?token=Tfilmqd7sKZrhTJFw67IjBVG_IjjKHtwpWIVze1lc1KZFCCwVwqsvIM3eW491f1FLBYWkPgFCqYlrmrGy6K9vrw60KQY6nB5tgu1AU6q9zU2oU99XHI3L3ZV9aeS7LQ-W9bjz2DWivc536jcoHHsKMLNwHp9DEz4pcFRtIl17ID8SIBOJuQdjDs40RmbfCkfU6jtX_Pueb49wMK1LesFPYNtpcj5BzzsUBCbPfTAZL2w_34LQXK32IIT4qU8tksMUYscpJmwdQmpGn6tFNWPfoX5zPbQ4nnUXGaxoM6GrerJIE9G8Mssfo47gp857ML-BA7vWGBBF6xrN_ROzSMdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51e0d7ccf.mp4?token=Tfilmqd7sKZrhTJFw67IjBVG_IjjKHtwpWIVze1lc1KZFCCwVwqsvIM3eW491f1FLBYWkPgFCqYlrmrGy6K9vrw60KQY6nB5tgu1AU6q9zU2oU99XHI3L3ZV9aeS7LQ-W9bjz2DWivc536jcoHHsKMLNwHp9DEz4pcFRtIl17ID8SIBOJuQdjDs40RmbfCkfU6jtX_Pueb49wMK1LesFPYNtpcj5BzzsUBCbPfTAZL2w_34LQXK32IIT4qU8tksMUYscpJmwdQmpGn6tFNWPfoX5zPbQ4nnUXGaxoM6GrerJIE9G8Mssfo47gp857ML-BA7vWGBBF6xrN_ROzSMdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات هي الاعنف في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84057" target="_blank">📅 01:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84056">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca653221e.mp4?token=XlRdMtpxvE9GlhhCi9xxtfUJH6hl_AG1qbhslEghLD7HinJhDQF0bZeL59fq0MTI1aaClaWBG69qFXYGkQ5on6UJniYJVseQdQkJ8xW7SPihxCaO-xECDWDgyKQ_GjmJUSHE9UfKfIQQLqd66LH33UbZDszz8A8fd7yRWBkQLG8CcA30Bged8xxnnmdGxmLyXXa_r4EK_NyWoRONPABAQ9uqr6NTUhmWeqwiVNtJKNwEFbfKKHsrTpLMOnTAMatcuwkKIJCsp0RnMNtEWsrcnodBHX8Mu8tZ3SFbXaa4vz4LW37ChUB_34vidZHLffZm24_hQQcuFkBPUQeTxFAHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca653221e.mp4?token=XlRdMtpxvE9GlhhCi9xxtfUJH6hl_AG1qbhslEghLD7HinJhDQF0bZeL59fq0MTI1aaClaWBG69qFXYGkQ5on6UJniYJVseQdQkJ8xW7SPihxCaO-xECDWDgyKQ_GjmJUSHE9UfKfIQQLqd66LH33UbZDszz8A8fd7yRWBkQLG8CcA30Bged8xxnnmdGxmLyXXa_r4EK_NyWoRONPABAQ9uqr6NTUhmWeqwiVNtJKNwEFbfKKHsrTpLMOnTAMatcuwkKIJCsp0RnMNtEWsrcnodBHX8Mu8tZ3SFbXaa4vz4LW37ChUB_34vidZHLffZm24_hQQcuFkBPUQeTxFAHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنون يوثقون عمليات مستمرة لمنظومة السيرام وسط أربيل</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/84056" target="_blank">📅 01:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84055">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa58189a6.mp4?token=qsGfmYaojkm_nEotyXHFV87aKZdPdkg--Q-CGRleZVJH0Dre9aV6lrVvLa_FHHA1e119Zya98pBgXYjc7Mw8eygm6sVckGsf8unaI4SacxknLVWtR33WWNQi4jh-_77fgp7ZswytPJhOkvpmv5jpv2Emy7zfqd3efdflqOroJVd-5ACOCfFp2Ggilv4JeLeH-oOQ9Wjhy51OhSBH8bUbt9Qz-j9IP1X5l_hB8tlXAbgYneGx-qpdMUnwTWsPotvvJl7e1JWou8cQOuJDkCX7tvEBefMUBUYACKA-VXV0RGHOzWoMqZRAzu_qxIm0JhJTySG6UWqHKCXE2jS_7x5ndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa58189a6.mp4?token=qsGfmYaojkm_nEotyXHFV87aKZdPdkg--Q-CGRleZVJH0Dre9aV6lrVvLa_FHHA1e119Zya98pBgXYjc7Mw8eygm6sVckGsf8unaI4SacxknLVWtR33WWNQi4jh-_77fgp7ZswytPJhOkvpmv5jpv2Emy7zfqd3efdflqOroJVd-5ACOCfFp2Ggilv4JeLeH-oOQ9Wjhy51OhSBH8bUbt9Qz-j9IP1X5l_hB8tlXAbgYneGx-qpdMUnwTWsPotvvJl7e1JWou8cQOuJDkCX7tvEBefMUBUYACKA-VXV0RGHOzWoMqZRAzu_qxIm0JhJTySG6UWqHKCXE2jS_7x5ndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالة من الرعب تصيب سكان محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84055" target="_blank">📅 01:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84054">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd197e3d35.mp4?token=YW5d2fEO-gOLLhV0xkqY1gTengBk2F7HSNvzHFzhoVmicZT9PC_GpIP0Y8fNWhYHrv7WSv9CgRIUC1vN9SG48K75O5lpUoZzap_OiCMODQxoEkD-7Ydtk5Zwlk7LMp79b60ToX-cJPiypRrMbbO1aFnj88ucDZK8aUVREfGslVjqFmKKJPyzZntjLeUaQbbIFWu17iD9326GPAK0RZZrA405T54RNLYEEMHhYAmUKlPt2bGlo94jjDk8Zfd_NoNEb8mCu4J7DTzZAITj1MjycspYanEYw3ZpFecYwSXkXbnO7xLoWzregn4ZoVCinLNRQstcAYDbLhn-zQV6weBokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd197e3d35.mp4?token=YW5d2fEO-gOLLhV0xkqY1gTengBk2F7HSNvzHFzhoVmicZT9PC_GpIP0Y8fNWhYHrv7WSv9CgRIUC1vN9SG48K75O5lpUoZzap_OiCMODQxoEkD-7Ydtk5Zwlk7LMp79b60ToX-cJPiypRrMbbO1aFnj88ucDZK8aUVREfGslVjqFmKKJPyzZntjLeUaQbbIFWu17iD9326GPAK0RZZrA405T54RNLYEEMHhYAmUKlPt2bGlo94jjDk8Zfd_NoNEb8mCu4J7DTzZAITj1MjycspYanEYw3ZpFecYwSXkXbnO7xLoWzregn4ZoVCinLNRQstcAYDbLhn-zQV6weBokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدد من الأصوات نتيجة العمل العشوائي لمنظومة السيرام الأمريكية في أربيل</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84054" target="_blank">📅 01:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84053">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88f7ce6e89.mp4?token=vxix61dsBPkzUS17dIpeOZ3pgcCQFe5Tp-XqbcnFr7Pvc9Kq8kuZE8ZBOX_qtnf1T6uSR2bBhrOuMmxLJ2EuQI-ce-DHJ21OqguElf3Mx2J6HF_DMBsyCBWqvDIkz51JBYpLYPH1skYUZ03rmof4YuaTHLdAubiPNYHgeoQ5of6e3Cr0S1cPXoz74Vm_7uYBdCNInGgqg7fd1Mug6B2T9U37TKqwHnyvC9Z93BzD8aqO3Kq2DRzOJh7MUnUUwi3RUkdGOtMcgE5yAqTyJ6dvshfLEN7UWWohlCqcvMtc_eUrGw8IHKyz01CE2jhL3QLGC03tKNzT-DXS3iWdIBKiFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88f7ce6e89.mp4?token=vxix61dsBPkzUS17dIpeOZ3pgcCQFe5Tp-XqbcnFr7Pvc9Kq8kuZE8ZBOX_qtnf1T6uSR2bBhrOuMmxLJ2EuQI-ce-DHJ21OqguElf3Mx2J6HF_DMBsyCBWqvDIkz51JBYpLYPH1skYUZ03rmof4YuaTHLdAubiPNYHgeoQ5of6e3Cr0S1cPXoz74Vm_7uYBdCNInGgqg7fd1Mug6B2T9U37TKqwHnyvC9Z93BzD8aqO3Kq2DRzOJh7MUnUUwi3RUkdGOtMcgE5yAqTyJ6dvshfLEN7UWWohlCqcvMtc_eUrGw8IHKyz01CE2jhL3QLGC03tKNzT-DXS3iWdIBKiFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات جديدة في سماء أربيل</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84053" target="_blank">📅 01:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84052">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e272f194.mp4?token=S61X6z33AisFqLKBV9JWvh_lV90vzmjK7_N6Edj8dZ748XTN70fuGRN5Qrchd-ugb9lI6zte6AAvBrlG-5bms7rpkTD49jBlMTAPnXx1lfE-aQY6mBTelJizuyuPDJfi_F-1WTt722cWykxSMXUlMA7pwDMiSeVJa9b1uVoO8RXb7IepeyxPpr4bovNmdURJi45CZDUSGU0GEglTbck47lGCvxBLZv01MJc8dphzcRSo_OBhIYWzuumYaUfHZ6P0vMR-TvmUxGkr-EnkKhPE_wvoZp94Q6ob8A6T6eBeeCjgymIypWuycg9nbi9a640GTXTDVzA29KSxY79LAM-aHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e272f194.mp4?token=S61X6z33AisFqLKBV9JWvh_lV90vzmjK7_N6Edj8dZ748XTN70fuGRN5Qrchd-ugb9lI6zte6AAvBrlG-5bms7rpkTD49jBlMTAPnXx1lfE-aQY6mBTelJizuyuPDJfi_F-1WTt722cWykxSMXUlMA7pwDMiSeVJa9b1uVoO8RXb7IepeyxPpr4bovNmdURJi45CZDUSGU0GEglTbck47lGCvxBLZv01MJc8dphzcRSo_OBhIYWzuumYaUfHZ6P0vMR-TvmUxGkr-EnkKhPE_wvoZp94Q6ob8A6T6eBeeCjgymIypWuycg9nbi9a640GTXTDVzA29KSxY79LAM-aHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهود عيان يتحدثون عن هجوم غير مسبوق على عاصمة اقليم كردستان العراق</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/84052" target="_blank">📅 01:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84051">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d68492ad.mp4?token=rzIGbCiHBEc9OhQoH0ITdYDr_77morsBt6QCFwNmtgeMh-2tp59Ck5hZHYIrVjcH_fbaOcefmUJTWsxo7yq-kn1Ued63D14LRacnMUT32XrNCwQ1tYKDL2lgClZ6p9UPv6Hjo3YVGFkIfwGmguBFzbD9C3JI2hg6tfrXpFXqJBdUn5-CvUCN4O36Tae0GasEVHj1Tc2kq1eI__f4a_bPy40sNvxo8QibE0vThAlM_cihhHwj6XSID0MAvihjSDUVsPdA2d5_z8TBayzs4DlEjw9Hvo7FSD5DHxTnMsSM-J94z2aR3LD8iDjLdyih0VWglx5pZ4gAzSCx8kgLkRX8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d68492ad.mp4?token=rzIGbCiHBEc9OhQoH0ITdYDr_77morsBt6QCFwNmtgeMh-2tp59Ck5hZHYIrVjcH_fbaOcefmUJTWsxo7yq-kn1Ued63D14LRacnMUT32XrNCwQ1tYKDL2lgClZ6p9UPv6Hjo3YVGFkIfwGmguBFzbD9C3JI2hg6tfrXpFXqJBdUn5-CvUCN4O36Tae0GasEVHj1Tc2kq1eI__f4a_bPy40sNvxo8QibE0vThAlM_cihhHwj6XSID0MAvihjSDUVsPdA2d5_z8TBayzs4DlEjw9Hvo7FSD5DHxTnMsSM-J94z2aR3LD8iDjLdyih0VWglx5pZ4gAzSCx8kgLkRX8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء أربيل نتيجة هجمات إيرانية</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/naya_foriraq/84051" target="_blank">📅 01:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84050">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f6a72c3b.mp4?token=I3H6Ru_qWuTcZ_XpNY9VDxdhnZeJ3mmzvXdmL4jxrDJEfhIfaD6r9YrvDo8ovJ16DkYs8qGgr4LckypV_OKP41x3jqAV0MNmzi6cGx-RcoXp0y9gGDHt62ZW1EkvvrjY2Df9r5zDkvFTyxUembqinSUm5roiJpjiBFVw9qKhGLqlWR0YuCpGHMqbaK491iRBIpm-Lkfm6PQjTaj5XPXxBFgG-RKKltg0reGE1tczCh_8s07HGuhzSms65ngPqGjoDIWcS5IXHKp6NQ3CrAJy2EqADm_qDpggRimesg3a3CEgM-ZFm42Wa5vxt5V_xItXC-Ch7uXywcBeFegXS8SJ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f6a72c3b.mp4?token=I3H6Ru_qWuTcZ_XpNY9VDxdhnZeJ3mmzvXdmL4jxrDJEfhIfaD6r9YrvDo8ovJ16DkYs8qGgr4LckypV_OKP41x3jqAV0MNmzi6cGx-RcoXp0y9gGDHt62ZW1EkvvrjY2Df9r5zDkvFTyxUembqinSUm5roiJpjiBFVw9qKhGLqlWR0YuCpGHMqbaK491iRBIpm-Lkfm6PQjTaj5XPXxBFgG-RKKltg0reGE1tczCh_8s07HGuhzSms65ngPqGjoDIWcS5IXHKp6NQ3CrAJy2EqADm_qDpggRimesg3a3CEgM-ZFm42Wa5vxt5V_xItXC-Ch7uXywcBeFegXS8SJ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اخرى تظهر استمرار رشقات منظومة السيرام الأمريكية في أربيل</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/84050" target="_blank">📅 01:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84049">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9e66b991.mp4?token=NuOqIZ0Wv2yWLsE1g63Od0Sl8y68Gb2hph2w1jITbP4xlU7ITJNIwJsmQshraP0wxX4eTwMcszJ53MjqJ97ycHcae_hlIEQ2CNCraq4HYrGVFglmASv5D9LPGA1R2E5gx8xgw9sLWlgfY5zsWOeMberxoSA0vkfGwU5GPmwa1nnbZkZvlbojBWlbCV20aua_yjJwUuzWfrlN6jMF_elkI0FQyoq-4s9yHTqPxhZpn8jXAbxah325yBSrZPREsDwIkhsh6Lrjl907DSRZhMsE1jqWer9GaGzaKtJRPoeJlwuzeaZFsRv93ybh3unKY9BDuqP-gb793f2Rbct1ZZhJhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9e66b991.mp4?token=NuOqIZ0Wv2yWLsE1g63Od0Sl8y68Gb2hph2w1jITbP4xlU7ITJNIwJsmQshraP0wxX4eTwMcszJ53MjqJ97ycHcae_hlIEQ2CNCraq4HYrGVFglmASv5D9LPGA1R2E5gx8xgw9sLWlgfY5zsWOeMberxoSA0vkfGwU5GPmwa1nnbZkZvlbojBWlbCV20aua_yjJwUuzWfrlN6jMF_elkI0FQyoq-4s9yHTqPxhZpn8jXAbxah325yBSrZPREsDwIkhsh6Lrjl907DSRZhMsE1jqWer9GaGzaKtJRPoeJlwuzeaZFsRv93ybh3unKY9BDuqP-gb793f2Rbct1ZZhJhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات من منظومة السيرام الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/84049" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84048">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d962d086.mp4?token=Z8nSBrSbPU0uHWCWLPG8Xwu9mrtVY_8LCRS8o1Y3XvpRtHDR7Wmyno6HHc-WuRUaVwvAKmz3akpHCNdWmQOdj77OJylBjgsEyD7BLQ94oSCA_HPtkrXB57h-fDxAk4jLQUdoxXb_zIxUYPkeRG6UblIrSUSMWirAxPFJFLltUOSEiVOYU_NeSgfqySc7YuEpjZPLWLjSnCcS4awFJxO6Fh7zJYDvMzrVVEMeFzjly_TSHQw9gKcz4cgvKFCl4m-WGT6T9Cu_H9xtfiuvG98JBfGjnrsX8EH3ce-S54V-mlq7xuf_WBzrfJzlW13HAJkHOQvX7XV1h8LsId476y4Knw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d962d086.mp4?token=Z8nSBrSbPU0uHWCWLPG8Xwu9mrtVY_8LCRS8o1Y3XvpRtHDR7Wmyno6HHc-WuRUaVwvAKmz3akpHCNdWmQOdj77OJylBjgsEyD7BLQ94oSCA_HPtkrXB57h-fDxAk4jLQUdoxXb_zIxUYPkeRG6UblIrSUSMWirAxPFJFLltUOSEiVOYU_NeSgfqySc7YuEpjZPLWLjSnCcS4awFJxO6Fh7zJYDvMzrVVEMeFzjly_TSHQw9gKcz4cgvKFCl4m-WGT6T9Cu_H9xtfiuvG98JBfGjnrsX8EH3ce-S54V-mlq7xuf_WBzrfJzlW13HAJkHOQvX7XV1h8LsId476y4Knw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الأمريكية لا تتوقف عن العمل</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/84048" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84047">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c3c9c371.mp4?token=d8ALyNeTf3W0LErQ6EW13hVeWohMQzsTRcHHxZy11LDw25zekqs21YoE6UvvV2GVpo_1b2z7EbLDGWf1VPqu2tg2r1VKkq-irjcewE2Bs0H5_wJuBkTY98ZmPOoaLYEiztnvu46h_xYgr_p0PH61M6Ge-MRJ-VfKWjShLBP0sRxG5L3JlJCNVRZ6RdnrIUJ7AIEaC-gPxJvdET_-F5Qbi3uAE3BsUD1bMMVYUXDII9kSOt1dj5EnvchA485i1T-QGZizr24o6778W-FtW_K9-ALkmN0zwNCU5KWO8SBG_Lczv9oQjhq1PrujiXuPvUXvV7lbtOHP8ovsFwfTE85UfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c3c9c371.mp4?token=d8ALyNeTf3W0LErQ6EW13hVeWohMQzsTRcHHxZy11LDw25zekqs21YoE6UvvV2GVpo_1b2z7EbLDGWf1VPqu2tg2r1VKkq-irjcewE2Bs0H5_wJuBkTY98ZmPOoaLYEiztnvu46h_xYgr_p0PH61M6Ge-MRJ-VfKWjShLBP0sRxG5L3JlJCNVRZ6RdnrIUJ7AIEaC-gPxJvdET_-F5Qbi3uAE3BsUD1bMMVYUXDII9kSOt1dj5EnvchA485i1T-QGZizr24o6778W-FtW_K9-ALkmN0zwNCU5KWO8SBG_Lczv9oQjhq1PrujiXuPvUXvV7lbtOHP8ovsFwfTE85UfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تسمع من مختلف مناطق أربيل</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/84047" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84046">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cd878a2.mp4?token=ATLT48-hhzz0BG1QkYKPI4BajlmROSbjqAqRRiTAkzQH30lTfzY4JgSeo-bileG-uj_idGIwbHs97ndTIJETLKRLY-ReETfoykzeCg45MfaN5LsqPRfVAM4xlZPhVlmDaDgNA6YT6s2ITI026-KCp8Pmd-QoDzslgIOZ86wA97sluEx44powZ_NWDHMt2B0PMikPLE1K7iOEc6A1KccHquZRRw02kHhXovYNsKkOAArk_lPQPNKlBqSIvr9I9b4P9axSYe6v4-9688pWRUFYa_7a0r36Nk9s16NjlZ3ZOgUI6mihmxq2V2q3l1o6E6zJIEJZedJ3l-5t4N2JBJSF9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cd878a2.mp4?token=ATLT48-hhzz0BG1QkYKPI4BajlmROSbjqAqRRiTAkzQH30lTfzY4JgSeo-bileG-uj_idGIwbHs97ndTIJETLKRLY-ReETfoykzeCg45MfaN5LsqPRfVAM4xlZPhVlmDaDgNA6YT6s2ITI026-KCp8Pmd-QoDzslgIOZ86wA97sluEx44powZ_NWDHMt2B0PMikPLE1K7iOEc6A1KccHquZRRw02kHhXovYNsKkOAArk_lPQPNKlBqSIvr9I9b4P9axSYe6v4-9688pWRUFYa_7a0r36Nk9s16NjlZ3ZOgUI6mihmxq2V2q3l1o6E6zJIEJZedJ3l-5t4N2JBJSF9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة السيرام في سماء أربيل</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/84046" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84045">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c5324770.mp4?token=Kh8uB4_LlWwz7CrrptmAXsjiEe02SgA76HTTIP5XpNtktP-7Oajm-1tZi4qSaMFtSeqKej969Pd4AW1d3Q4Fm0DoMoNUIeWJBggZC5mKk3G7hkuCDNFNGUxYjmwqVQOd8n2dOH94R22_WbTOIFpFCvZo539L92XjmiU_Wx3HEPdd3saUAAH-h7pxBcDj0tYJSfEUFjZ4HThRTfu9syxK8e_uAbGhQdmADmAyIw_qguSuhdzTkSmdiD-qWeBtidS4-Mjye7RHGuEO1FGHz_3wjRFv52naElQoBJOjK6yXnMJ9vd48OBpSaHhcscj0s6xgE8LeS55jJ2u9F26pi7OObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c5324770.mp4?token=Kh8uB4_LlWwz7CrrptmAXsjiEe02SgA76HTTIP5XpNtktP-7Oajm-1tZi4qSaMFtSeqKej969Pd4AW1d3Q4Fm0DoMoNUIeWJBggZC5mKk3G7hkuCDNFNGUxYjmwqVQOd8n2dOH94R22_WbTOIFpFCvZo539L92XjmiU_Wx3HEPdd3saUAAH-h7pxBcDj0tYJSfEUFjZ4HThRTfu9syxK8e_uAbGhQdmADmAyIw_qguSuhdzTkSmdiD-qWeBtidS4-Mjye7RHGuEO1FGHz_3wjRFv52naElQoBJOjK6yXnMJ9vd48OBpSaHhcscj0s6xgE8LeS55jJ2u9F26pi7OObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة السيرام في سماء أربيل</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/naya_foriraq/84045" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84044">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de9926e24.mp4?token=Gzf3KlXRvlqJqwNnvnR_k6W9bidlPT80pp9O6-BU6ebGGM2cGTiSUd0BdNpKGcqJf1YoVTV3ixLIU8j3XegDFay6X8fluBXeHV6Do24dqDyhY0duPtQ8UyC-hl8xXKpAXIQhrWDDak7sbX0HoIOCoNQIuJdxcorHMpXyJqjNT_f-2gN_T4-zI87wVfV1MeR1Ctfc2aALZpfcPYNmZXe2iVm60l0n1P5I8Mk4gHBVF6NUN_hXF-I72AsJ6qddD1MANr5eqybgJEip43HXI5vLEWBksWmgp4x1FdP9kqDZyY7PFNNWjGXhB3hG6xvT63Pa2RidqsJ5Xs22UujR_i-Mwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de9926e24.mp4?token=Gzf3KlXRvlqJqwNnvnR_k6W9bidlPT80pp9O6-BU6ebGGM2cGTiSUd0BdNpKGcqJf1YoVTV3ixLIU8j3XegDFay6X8fluBXeHV6Do24dqDyhY0duPtQ8UyC-hl8xXKpAXIQhrWDDak7sbX0HoIOCoNQIuJdxcorHMpXyJqjNT_f-2gN_T4-zI87wVfV1MeR1Ctfc2aALZpfcPYNmZXe2iVm60l0n1P5I8Mk4gHBVF6NUN_hXF-I72AsJ6qddD1MANr5eqybgJEip43HXI5vLEWBksWmgp4x1FdP9kqDZyY7PFNNWjGXhB3hG6xvT63Pa2RidqsJ5Xs22UujR_i-Mwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات لاتتوقف في أربيل</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/84044" target="_blank">📅 01:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84043">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0992f4548.mp4?token=E-Il7Og992a4yruG1Zb_SVt0sIJSaEggNiFADUKR0pj0MdG1VSL5VuQOEV5MVL9S2SfdZLe7VGSGDBny3TlL9slGa7BHMsHdb7Roder8zvggUXnhKyr7F7LDD9wnL3QS8O-e_gvAl3qo8Vw6GB1RLYlSIGZ3xBuztz1t4qedjiPdTHmfYEQx5qirqHByW-tPOxDJO1PhGh2Z3hwxhpU7W6ONMPVZVQCqFpDmUlZ9XUQ38xt8ztI-j34xYdZKhMSD8223laGEdcmwLhti7fu89OsJiXlldezqrz_zTKicQNOsw3XJxZtE5NbUTIJX2dtnlExhwFxJ1K5S-LcOd5pPmWjmIgjisSo7lJ5jq0pcN-CgNZHmPv1M7-8BSFOVC9KbF3eDtgyo817KwizdarOrFrw4F9HmHLVbuLGCAf6mAAF3wLKp5eGG-KSO858aGk6MvwL_cksDtG9RUWhC_OnaODpzeBaA5UGXBuA-2On44byoAAdftTqxBGO0aFFe5lXaM25R9Rfxgb9FgFJugVTXIG0ZSEF-EUcrUw417pFjSeugKzX7Yd6bWV49Xsjxh6eW2fywGgZOv-kyfvbtkJfNVXBsUzOBP7Ujy4ziPdu4a-YSy8GR3GcXO7ep1kOxm3g3QZpbP0poLk9wzxjVKgBWTi3uV0F0hNwlbCL-0iWcO14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0992f4548.mp4?token=E-Il7Og992a4yruG1Zb_SVt0sIJSaEggNiFADUKR0pj0MdG1VSL5VuQOEV5MVL9S2SfdZLe7VGSGDBny3TlL9slGa7BHMsHdb7Roder8zvggUXnhKyr7F7LDD9wnL3QS8O-e_gvAl3qo8Vw6GB1RLYlSIGZ3xBuztz1t4qedjiPdTHmfYEQx5qirqHByW-tPOxDJO1PhGh2Z3hwxhpU7W6ONMPVZVQCqFpDmUlZ9XUQ38xt8ztI-j34xYdZKhMSD8223laGEdcmwLhti7fu89OsJiXlldezqrz_zTKicQNOsw3XJxZtE5NbUTIJX2dtnlExhwFxJ1K5S-LcOd5pPmWjmIgjisSo7lJ5jq0pcN-CgNZHmPv1M7-8BSFOVC9KbF3eDtgyo817KwizdarOrFrw4F9HmHLVbuLGCAf6mAAF3wLKp5eGG-KSO858aGk6MvwL_cksDtG9RUWhC_OnaODpzeBaA5UGXBuA-2On44byoAAdftTqxBGO0aFFe5lXaM25R9Rfxgb9FgFJugVTXIG0ZSEF-EUcrUw417pFjSeugKzX7Yd6bWV49Xsjxh6eW2fywGgZOv-kyfvbtkJfNVXBsUzOBP7Ujy4ziPdu4a-YSy8GR3GcXO7ep1kOxm3g3QZpbP0poLk9wzxjVKgBWTi3uV0F0hNwlbCL-0iWcO14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الأمريكية تستخدم منظومة الافنجير للدفاع الجوي قرب شقلاوة</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/84043" target="_blank">📅 01:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84042">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تفعيل منظومة الباتريوت في أربيل</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/84042" target="_blank">📅 01:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84041">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d8ee3662.mp4?token=Syf65VuIXFmUNUbBRebUjs1oouqcrtv5HYJ0ziEc6m13D7-uI8tGtaQoKSVYJhLs6EP3p1_LU0_mMuG4Eg5VnYUGleceNlJKoAFTPtMSOvP6zPFlM4INYBpslTLSCYu9QxRDwHWcGFHWWdHg6hK0JQeiwlyPjjrbqkFiiGj4XSZ4vbqEn3o62mHR_VsHHCfm5hQbtfhJp9JQWIaJCAOwwlYhAWR-6vVfffdBHdxYXrfazmndis2hX8ULa2VsqknEVvAD8pR6zc3ArZc1yxREiLA7TFpZvxJWXjjZlOL0D6HcDBc9LfVLbDooSq_yyrpyyb_COCmiIVrps-j6BJv7lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d8ee3662.mp4?token=Syf65VuIXFmUNUbBRebUjs1oouqcrtv5HYJ0ziEc6m13D7-uI8tGtaQoKSVYJhLs6EP3p1_LU0_mMuG4Eg5VnYUGleceNlJKoAFTPtMSOvP6zPFlM4INYBpslTLSCYu9QxRDwHWcGFHWWdHg6hK0JQeiwlyPjjrbqkFiiGj4XSZ4vbqEn3o62mHR_VsHHCfm5hQbtfhJp9JQWIaJCAOwwlYhAWR-6vVfffdBHdxYXrfazmndis2hX8ULa2VsqknEVvAD8pR6zc3ArZc1yxREiLA7TFpZvxJWXjjZlOL0D6HcDBc9LfVLbDooSq_yyrpyyb_COCmiIVrps-j6BJv7lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تشعل سماء أربيل</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/84041" target="_blank">📅 01:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84040">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a480946d4f.mp4?token=XjOV2madpaM2vfYntxXDCi_Cl5J3aLzSZjYxaABLhV7USGthMvtKuQOZ28PY4W7I7Eqm8K95i6FWc6p0iDU_WVjeW4IV38ifFQRUq9t5DTjme9D6ZvIJGUySshQW2nt-6DBueGeg_d3wBJnJnoL8M2G70_NzYTVvS-ViJ1VeXRm9kUbrBvZhVja-Y86X7w8SexwIBdEqzG5Qmf6TZoDv9Q4Bhn_cZXU3pWDwUGEPQ3INI0MBzH5uZyUPEs_6x7B_NBkmuoc6rju5x2g_umdhZgz2VGS5AWI8yTX9CtQPZfZDhapKWiopK9wyzYl9o9D8dyRpJ5BeLEGNUur3n54REA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a480946d4f.mp4?token=XjOV2madpaM2vfYntxXDCi_Cl5J3aLzSZjYxaABLhV7USGthMvtKuQOZ28PY4W7I7Eqm8K95i6FWc6p0iDU_WVjeW4IV38ifFQRUq9t5DTjme9D6ZvIJGUySshQW2nt-6DBueGeg_d3wBJnJnoL8M2G70_NzYTVvS-ViJ1VeXRm9kUbrBvZhVja-Y86X7w8SexwIBdEqzG5Qmf6TZoDv9Q4Bhn_cZXU3pWDwUGEPQ3INI0MBzH5uZyUPEs_6x7B_NBkmuoc6rju5x2g_umdhZgz2VGS5AWI8yTX9CtQPZfZDhapKWiopK9wyzYl9o9D8dyRpJ5BeLEGNUur3n54REA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منظومة الباتريوت تحاول الاعتراض في أربيل</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/84040" target="_blank">📅 01:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84039">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1dbfb7138.mp4?token=OTg9YK8-VPUNo2IQuZpBahAJHneIgLXsUD_qeqIErxSnWDbiloTu3Qs4bDTzTMj0VRaifenQZZzYarJc01THu-ZeAqwSOngWGPT_8pnizfdEUNtY_F8gSNRe7PqBifTfgO3tmtfWzyj-odGTAphV2ngYJCyiYEeZqceQgFn1zskMxCcXawu1jIiwpkSTg0iCvxttombtKEY5IpHxlcBCgyVKIXLDDbyftbC1jugbPh-yyMDQTOcgQV3PGKM7SwVQnHlpecOqVndOO8SZ6qAdbbbXes8u6TlUQ1XO37g410AvMmUj56W4h8I4kBEKh3u2veKLcDCHr1yug701BzeCjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1dbfb7138.mp4?token=OTg9YK8-VPUNo2IQuZpBahAJHneIgLXsUD_qeqIErxSnWDbiloTu3Qs4bDTzTMj0VRaifenQZZzYarJc01THu-ZeAqwSOngWGPT_8pnizfdEUNtY_F8gSNRe7PqBifTfgO3tmtfWzyj-odGTAphV2ngYJCyiYEeZqceQgFn1zskMxCcXawu1jIiwpkSTg0iCvxttombtKEY5IpHxlcBCgyVKIXLDDbyftbC1jugbPh-yyMDQTOcgQV3PGKM7SwVQnHlpecOqVndOO8SZ6qAdbbbXes8u6TlUQ1XO37g410AvMmUj56W4h8I4kBEKh3u2veKLcDCHr1yug701BzeCjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباتريوت في أربيل</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/84039" target="_blank">📅 01:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84038">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تفعيل منظومة الباتريوت في أربيل</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/84038" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84037">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الطيران المسير يستهدف القاعدة الامريكية ومقرات المعارضة في أربيل</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/84037" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84036">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/84036" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee64ee42df.mp4?token=VW806WBpoyT2rQOxQXjEGxpEBfv0UPDN8xBdQrRAQT4IHirzmoZ16rHiYl6h1AzjtfO-AY7i5T6PETolmOgYBICdxDbzMDXFQ-hdaoWoPMs9-PzmmBujvde8nYZ_e4u6ffza15BzZcpoRT2-7aDTuMeIs5FUNj4EJFjeTKfH2z7CNxem5LVGGRKoLZZkF8KUjvMulYaNDIURoqElcqD3J20NIDIGTnMMpGNn8OuYnJJrPUUzNFbFFXPWfbIvFrAP6sK2GuvNfDVTwSUZPEO4-BU7EkYlvEhkrMPimPWyBqTiIuChuPdt2ng3NAuocX08UjzzJ0WM0c8Hgn80K4nHgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee64ee42df.mp4?token=VW806WBpoyT2rQOxQXjEGxpEBfv0UPDN8xBdQrRAQT4IHirzmoZ16rHiYl6h1AzjtfO-AY7i5T6PETolmOgYBICdxDbzMDXFQ-hdaoWoPMs9-PzmmBujvde8nYZ_e4u6ffza15BzZcpoRT2-7aDTuMeIs5FUNj4EJFjeTKfH2z7CNxem5LVGGRKoLZZkF8KUjvMulYaNDIURoqElcqD3J20NIDIGTnMMpGNn8OuYnJJrPUUzNFbFFXPWfbIvFrAP6sK2GuvNfDVTwSUZPEO4-BU7EkYlvEhkrMPimPWyBqTiIuChuPdt2ng3NAuocX08UjzzJ0WM0c8Hgn80K4nHgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك مسلحة عنيفة تشهدها شوارع مدينة أعزاز نتيجة خلافات داخلية بين عصابات الجولاني الإرهابية.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/84033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/84032" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/84031" target="_blank">📅 01:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز أربيل</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/84030" target="_blank">📅 01:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd841dc7a.mp4?token=OtQtTWtUU7KYUEZyeQG2yk6LzbDa3hM6Mb0ciZbC51eP9M7HXrNEefKo6dz1JURHT_frodKbnMGN8URrWeJps_fW3tc2HGNf2-d9cbCg-eCUxijtB5nVoHhjtpeKxbg9Z0V4WNk12nYtJdexVcLaD9l1-YC7NVmNrMwjdxWZAPvrEzEXEfzLT8Kz29Q01xWo39UvCxO3ZD5qmcj80GxNs-rHUCBQQXkTzh7SAhP0uH2QuuukopwN1jyuG4nEXV8y2OcYir3sCNoTUU4lHNTxDaMVXwOjIUMjAr-csVdpcN9OxEV7Lqk3YsQKMwjV1aeWLgxSwABq9Rp69vU3ve7ILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd841dc7a.mp4?token=OtQtTWtUU7KYUEZyeQG2yk6LzbDa3hM6Mb0ciZbC51eP9M7HXrNEefKo6dz1JURHT_frodKbnMGN8URrWeJps_fW3tc2HGNf2-d9cbCg-eCUxijtB5nVoHhjtpeKxbg9Z0V4WNk12nYtJdexVcLaD9l1-YC7NVmNrMwjdxWZAPvrEzEXEfzLT8Kz29Q01xWo39UvCxO3ZD5qmcj80GxNs-rHUCBQQXkTzh7SAhP0uH2QuuukopwN1jyuG4nEXV8y2OcYir3sCNoTUU4lHNTxDaMVXwOjIUMjAr-csVdpcN9OxEV7Lqk3YsQKMwjV1aeWLgxSwABq9Rp69vU3ve7ILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
🇺🇸
مواطن كويتي يتوسل بالحكومة الكويتية بتخفيض ساعات العمل حفاظا على ارواح الموظفين ، يذكر ان الكويت تعرضت لاعنف هجوم منذ أيام القزززو العراقي القاشم عليها ..</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/84029" target="_blank">📅 01:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5f72fe7a.mp4?token=fGbGg0a4erjpea6p26STenSjAioL_-0L05eFWqtscvKNG0XVlX4VyhFcGirhuEF72kd3Lb96t95UBI8eN5nXA2Zha6dyD4tw2uscYfWZRO8b_5SdQxKw3HVNzcQq6k568iuXibl83Y6rwMsGnfrpbgRxcBI8XJDyxaZ0Yls7v8Qou_k1P1aBz_K_omeUP7msnk09MLevfxn2FZizNq32bTEGttT122MLY1X3w1YpWTAvNEDT8iZAi4zGXzUtzuFbeyFhlTy3vd0wmiCaDO6IJKbAHVx-zwVRgx8bvnEjG0IIoAR1as-ZSiNpGGGsD8LfPlSAF8S_HD4U4s73MXpwcXTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5f72fe7a.mp4?token=fGbGg0a4erjpea6p26STenSjAioL_-0L05eFWqtscvKNG0XVlX4VyhFcGirhuEF72kd3Lb96t95UBI8eN5nXA2Zha6dyD4tw2uscYfWZRO8b_5SdQxKw3HVNzcQq6k568iuXibl83Y6rwMsGnfrpbgRxcBI8XJDyxaZ0Yls7v8Qou_k1P1aBz_K_omeUP7msnk09MLevfxn2FZizNq32bTEGttT122MLY1X3w1YpWTAvNEDT8iZAi4zGXzUtzuFbeyFhlTy3vd0wmiCaDO6IJKbAHVx-zwVRgx8bvnEjG0IIoAR1as-ZSiNpGGGsD8LfPlSAF8S_HD4U4s73MXpwcXTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة بين عصابات الجولاني ومسلحين في مدينة أعزاز بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/84028" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrhvkSs0ER664C7paIf13-0HB85JEY4Cv86Ps5NkfqFIoUUN_e0H5YJ2Vlaae60GFgNX1O1O_whuvJrGb85h-fH3XlKvHaaFKqxbmp9XijRiG_PE-8s_A-G3VHF7oPaFCUWt-hKuVokm9RQgWtaNqhiUrqeOBCGuA8iyReTPmTkqAGMswsB5AK0PVx5OSt8vTn-Qofym73dcOHUtu5ZTtZvnpbxoCU_i9acN9edb0KUNH9WQG2vvupjtzuCYiv7g_FaAcdcCkZHbP_UjhhgGQt5Ti76IIZjLvxWdTis0LPP0dMkl3lNhMV30WPJU9Hh0E8p4vnvwzo9-nZwUEPqLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇺🇸
مواطن كويتي يتوسل بالحكومة الكويتية بتخفيض ساعات العمل حفاظا على ارواح الموظفين ، يذكر ان الكويت تعرضت لاعنف هجوم منذ أيام القزززو العراقي القاشم عليها ..</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/84027" target="_blank">📅 01:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84026">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8e8f0181.mp4?token=Qd853wnbWfMEFsX3rtloUdDvbrPQTQPYZA17GlVQsEUMOoI3eCDSW6gPzFp6qmdAom2mH91ztlbOZMNAtbY9mEOmCJCSxj9dyR_y9GpStGYzcYACJ8Irvq1MlhctzYgiFj5crChYOm8MY94ZBdjyFWX3lqVbJzs6V48lXGnaRnBgfdmTFgzWWJPoxf2OXGOuklso8BDJKg266DijiIAPzqgBbt2BUT8DF63ZiEkbZ3OQNwRYdbenI7NlKK5skBTYGJpce_63voBC7sIFfLVfRcnhy00YtUWZN5_14OHPYe1w59Yb57g3PzI9ZJ8GKBIrIw-jPd11OxoGSQOekAr5HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8e8f0181.mp4?token=Qd853wnbWfMEFsX3rtloUdDvbrPQTQPYZA17GlVQsEUMOoI3eCDSW6gPzFp6qmdAom2mH91ztlbOZMNAtbY9mEOmCJCSxj9dyR_y9GpStGYzcYACJ8Irvq1MlhctzYgiFj5crChYOm8MY94ZBdjyFWX3lqVbJzs6V48lXGnaRnBgfdmTFgzWWJPoxf2OXGOuklso8BDJKg266DijiIAPzqgBbt2BUT8DF63ZiEkbZ3OQNwRYdbenI7NlKK5skBTYGJpce_63voBC7sIFfLVfRcnhy00YtUWZN5_14OHPYe1w59Yb57g3PzI9ZJ8GKBIrIw-jPd11OxoGSQOekAr5HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
توتر أمني كبير وإشتباكات مسلحة عنيفة في مدينة أعزاز بمحافظة حلب السورية.
😆
Trump want to use them against HB</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/84026" target="_blank">📅 01:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
🇮🇶
مصدر امني لنايا
قوة امنية عراقية كبيرة تنتشر من سيطرة جسر ديالى باتجاه سيطرة اللج في محافظة واسط تضم قوات من جهاز مكافحة الارهاب و الرد السريع ؛ مهنة القوة مسك الفضاءات الخارجية ومنع اي عملية إطلاق محتملة ..</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84025" target="_blank">📅 01:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84024">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/84024" target="_blank">📅 01:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84023">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O97hxx087W3K7TUUvY5GQdUcbMeWTaIuHvjJM9Ti-gNKHNclQ67Ix2qoUXPm1_LHrlmrGJ7gyU0Z5MopVuno4Bj8U9vYUdCf8aZPHI5iL2bdY0omPhMgxYLzU8XRTECLRZK9NEdvwZu_1PGtaK0KmWDBHab7b8jCZrcHO1uFI1wOo2tj0GsocMEu8tNE3V88I-AVR0k6JuoLT6OElT3GZNKZ_VyzQ3L_wlcKQrkbun39AkvheFQiQwAZSAiK9eB0rGE8PRIuiI9ggScTSh83jJ1fNn-PG1gvPmSXP0oRJai0o9H7RKwTeIsuYmkd61aia2hn6ZP8N023PKTN_qOOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
صدای نایا، این‌بار به فارسی
کانال رسمی نایا رسماً راه اندازی شد
همین حالا عضو شوید
👇
🔻
t.me/naya_press</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/84023" target="_blank">📅 01:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84022">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b4b301ce5.mp4?token=akFNuWUKm8BYCNR4UWpxk1S25JL1NdkXLjkiYbYro2pf98NeUrYNLFi_NwftxaIlj8X1fM-MwnmQwp_Iv96722sTD37mBHJeaTPfF1339-9aRB3J6H8GfiGJW_u5d-ZHfVMZHpr35__lSWK1b2Fm0OVhQhhDq_IoeJhRzU64fOJl7-Uy6k71e90hDjKMIdjviegjyIXUSDfa9W5ru1fZetN3505hC2JS-UMJ54sEkPU-r0rrNUZuuIbbzmg7dGQ9YLJG6-IimaQlN7hlovIXpqzeoO5qINeEOI7A71oiA7mlf2sfsb9yN_FtGO-TRcYJNa3NLMFqJn4KarBJQY8p7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b4b301ce5.mp4?token=akFNuWUKm8BYCNR4UWpxk1S25JL1NdkXLjkiYbYro2pf98NeUrYNLFi_NwftxaIlj8X1fM-MwnmQwp_Iv96722sTD37mBHJeaTPfF1339-9aRB3J6H8GfiGJW_u5d-ZHfVMZHpr35__lSWK1b2Fm0OVhQhhDq_IoeJhRzU64fOJl7-Uy6k71e90hDjKMIdjviegjyIXUSDfa9W5ru1fZetN3505hC2JS-UMJ54sEkPU-r0rrNUZuuIbbzmg7dGQ9YLJG6-IimaQlN7hlovIXpqzeoO5qINeEOI7A71oiA7mlf2sfsb9yN_FtGO-TRcYJNa3NLMFqJn4KarBJQY8p7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
توتر أمني كبير وإشتباكات مسلحة عنيفة في مدينة أعزاز بمحافظة حلب السورية.
😆
Trump want to use them against HB</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/84022" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFMUOI2OhgM-o77JSKWKi0QQmembGmfP1zi0GKW42kUZO9_QQ-a2FxYo2aMWY9ywqPDhX3U3Vuc7tM-5DTkqGM9G1p7L9NYjXt6UaxfR0u_LDmxstKMXn9tprMjm-uB4Q5f3VQeXNpfSnX63ZAcsAmu4mqBlYUtSIey3Ed6oERGDHe5IKl2bi-SuHfdoRgtTmmfPDTlEojNnhDXtbCWcCDR6tByuuCSRyumowas_BddLbLUdRgR-YFFIDTybLenqmkx5c35hyPDiW6CX3As8SqZBLuHcfRpqoo62K0meYOBq0GfnU0D77TdVM5c9rL3281kttyx1jDf_43l3qSOUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تشارك عاهرة اوربا بريطانيا حالياً بواسطة طيران إرضاع جوي لدعم الجيش الاميريكي ضد ايران بسبب النقص الحاصل في الطيران الأمريكي الذي استهلك نتيجة الضربات ..
🇺🇸
عذرا لروسيا والصين وكوريا العظمى نحن نواجه امريكا وحلف الناتو لوحدنا .. ايران لا تقل تصنيف على انها قوى عسكرية عظمى</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84021" target="_blank">📅 01:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله أكبر
🌟
مسؤولين أمريكيين: قواتنا بالأردن تعرضت لـ4 هجمات إيرانية خلال 5 أيام أسفرت عن قتلى وجرحى.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84020" target="_blank">📅 00:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTfbjLl2klOI48zk4YoQwaW5Ny-sKiDRSZ6OWRGUsGsCHS_72YBY3VXInra77jhXn5_fRacgj2qbEK7Q-xpzoX7uAU1ORUnvKoV1lsp3sEqiCH5M4xLm8LLcniA4FyueJuJ6pV5A9HR9uOcEwZrY8TX475zkHnn1jiNM9Ftt-AkiL5olO9qK-YFaPbMIHixtp-Q5ioUc43Yw13N5xeV3E8EIZ4EMY7ZGwRe0Bf-Shp8Z89IdHIAU1EjvWqDG2l4Do73XwDC6IyOU7OTdrihk10NjmxXtAO9KWkoqNwD61eXORO2HyHTqlBg5J0y6p-9PqWbWVyJaJUWrrM5zwly1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfLLJRX5yA5Nv2ozZIlo7pjAohvnk0Wvi4AobQekYf-xTVaumADqJWeimFCxUF0Y3VoYvHzKtjdRUyGL6jn5MGA8w4Rnjmos-6W7UMwpewlNl48AMZcxL853F6gbREPcCXbLCva400AnrMXuqVi0_1Q52F5vTdIhJDAqtp1lrXd8lt4W8wG5Jlo_S4rBnE592_J1awVRdVtY73jyvn0d3JHXYEWE8rHm376OyZhZLYasZSK1PFmEM6bsSwjbNrD78nAQOzK35_Tr_EsmAkRQxfKyAUg6JHXgOMoBQW3S8Rj_3NciOyUWAl4Wprv4u5UiWRuVnY43C1BEMAfrmOX9og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نموذج للدعارة والغباء والاستحمار على شعوبهم قبل ان يضحكوا على انفسهم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84018" target="_blank">📅 00:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84017">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
ترامب حول مقتل جنوده في الأردن:
"نحن نأسف لحدوث ذلك. إنه عمل يخدم بلدنا." أن "إيران لا يمكنها ولا ينبغي لها أن تمتلك سلاحًا نوويًا."</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/84017" target="_blank">📅 00:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84016">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWDz4iSrbcUtuQ9dhqPjFuup5Oaz8pQNDI0kbJkpPISMgqVVdv1CdqBURMMynUvpXkPsOXbZAaT1Zonna6tiokc9cM11fZAr_hNxH2uNOjQsKgLhRHmkAsfAGCAWnIWyg7Du91N3rm9pJ_2b1orjMswHzim-nhNCxs8TcYLuYsrBBvfS0fZsmeFaoq_Wu6IJ0Jr_1-LgBn17TQps_FOW_UKvWHUAs5U78DLV8pzKME1fMhod3rRrOSWTyIiU8PGz4yuRbG_ChKTKbm1PbqtPiUy1t456D0hij1MFwN3BFy4YYlulZKSmS-GJWWivLJQR_Yf-eEFJhm0xvQzcMHpDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرح وزير الخارجية الأردني رسمياً ان لا وجود لقواعد أمريكية
إدانت دول الخليج الضربة الإيرانية ..
والنتيجة مقتل ٥ جنود امريكا و٥ موت سريري و٢٤ جندي جريح !!!
مثل هذا الحال سيكون في الكويت والبحرين وقطر والإمارات والسعودية
هذا نموذج للإنكار والخبث الي تلعبه دول المنطقة تجاه ايران البطلة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84016" target="_blank">📅 00:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84015">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله أكبر
🌟
مسؤولين أمريكيين:
قواتنا بالأردن تعرضت لـ4 هجمات إيرانية خلال 5 أيام أسفرت عن قتلى وجرحى.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/84015" target="_blank">📅 00:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGgemVyCB-vTVqkeFOo3JESKsRAUfcUsw9NcSSInB5tHARc-kveDGBsFy4gZtrEEaABGPbuOItTuLWnYfWmjsF5ggeZ204NsPxn6gUM3nMaxIVXsKLkJ04BciI7TCMnVI0zWhObtOGR0xcU9BGT0kw6Q_EThxtEQ_6fw3VR_DiERhb_O5kj-l-KHTYW4T0f_oBR-ItcxwcrlDrs1ufg8URY0bpqfFShl8_Zh9UjAN45c-s11zpnddBzvONNg-HMUc7J-dUijlZIjOx57l2PNhHSgRPhuwJnWoX8JtOuKgq9u82CCWolz7ZmIwyMwprJhXOuBxTESlhr58wQP8hrfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدير مكافحة جهاز الارهاب في إدارة ترامب السابق :
الليلة، سنضطر إلى توجيه ضربة قوية لإيران رداً على مقتل جنودنا في الأردن. بعد ذلك، علينا إنهاء هذا الوضع قبل أن يتفاقم. اضربوا قواتنا واسحبوها في الوقت نفسه - أزيلوا نفوذ إيران وانتقلوا إلى المفاوضات الاقتصادية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84014" target="_blank">📅 00:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c527d8591.mp4?token=hKNBIFKbHF0ea4Tt1NIriVTzOxV2oiWrj7o5EiDq5Se45OvZPtsTlF4kSepGqVDhjFqIKo1R8qowJ2VtFOgmA33henL5PAhVuZ6UyFLD5lAtCCqpUNJopOClF70qMhFkcJHAPKDHqFGqliFmDRhTuSCdMmN9xJ9xtxNkgaWdcXPhppfIJVOj5exa7MVfH4vO13JbtlqtczMW84spHhFri-dinQ2qQs0cU6UnLHTRHL1vLVc-VC80Hsy5nMJjxEyo-zgVt_lYDW-CwyAbWcChCo3NUYvH6LoZW3yyJ09b2exhhpwtJH4yC6V6Lq6lmcxP_JRX7N-RiQakVVzRrR7RXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c527d8591.mp4?token=hKNBIFKbHF0ea4Tt1NIriVTzOxV2oiWrj7o5EiDq5Se45OvZPtsTlF4kSepGqVDhjFqIKo1R8qowJ2VtFOgmA33henL5PAhVuZ6UyFLD5lAtCCqpUNJopOClF70qMhFkcJHAPKDHqFGqliFmDRhTuSCdMmN9xJ9xtxNkgaWdcXPhppfIJVOj5exa7MVfH4vO13JbtlqtczMW84spHhFri-dinQ2qQs0cU6UnLHTRHL1vLVc-VC80Hsy5nMJjxEyo-zgVt_lYDW-CwyAbWcChCo3NUYvH6LoZW3yyJ09b2exhhpwtJH4yC6V6Lq6lmcxP_JRX7N-RiQakVVzRrR7RXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🔻
It s our session
پدر جنگ نامتقارن مدرن ایران
پدر دفاع نامتقارن ایران
پدر مقابله با برتری هوایی مدرن
پدر میسل وارفر مدرن
🔻
با افتخار سرباز
سردار سرتیپ پاسدار سید مجید موسوی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84013" target="_blank">📅 00:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
مصادر إيرانية تنفي وقوع اي انفجار في سيريك</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84012" target="_blank">📅 00:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84011">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
مصدر أردني لنايا: وقوع عدة إصابات في صفوف القوات الأمريكية نتيجة الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي بالأردن.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84011" target="_blank">📅 00:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84010">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وول ستريت جورنال عن مسؤولين أميركيين: إيران طوّرت أساليبها لتجاوز منظومات الدفاع الصاروخي الأميركية، وذلك عبر استخدام صواريخ تحلّق بسرعات فائقة للغاية وقادرة على المناورة خلال المرحلة النهائية من مسارها قبل الإصابة. هناك قلق من التحسن الملحوظ في دقة الضربات…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84010" target="_blank">📅 00:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر   إعلام أمريكي ٢٤ جندي أمريكي جريح نتيجة ضربة الأردن ٥ منهم حالتهم موت سريري</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84009" target="_blank">📅 00:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رستوران آقاى مجيدي در اردن</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84008" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQY-oFEv74i7b4bBiDihjfQpMqAP-IkkY2ljNG6Qmah6c8d0ejPr-VOfpGEJOXzfKi3LKhL3sYA2p5LRUJLgM51VvIeH_ht7SoJ2gVOuIT8goeO1OuqKzaY4bJUkI6kCgX4SQ94UbnYtYF6TMH3JID1-o0yvX9knGPq8tjDh4J8nBdXetsM19vifTBvOQo_s0M1r0kr_DoCBhcRhZ4xAf3eWVU-UR7fJql13of4BJ3xOb5ZbQU6YIu3tXC9NC5TU8ttY3z5AQdu4kb0ks64r8-Kz5uLAO2SdbD6XIe9F3DglwkFJAL5sBv1d5OUXE6WuEkZJcECXO5AhyUKFcI9HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رستوران آقاى مجيدي در اردن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84007" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84006">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=JlEaYmvERz9v-wCKkdfNojJWMyX-IRWU-hjBX8aKIBQoNwCfmrWb09bVIIbikpEhU2AXrIT-14osal1jFSPCljhfLemB8H0lTMjpatmztCmyw0BVejI3WzhhWdJFLX79VP792QCGPVL1hlfH2Rm8PIfE8o_ehrfVTfXZU6OoK1cOE7lZjYAFkWDBIPHNGMQIbB9SEUa97H-Sx_PhWNtAIxIdUNYMoD2REUom9aTyDrMR_dD3UqcSjJw48sfFCedNkQibNy-zfhA7DU7xMVXDdNLeP4a_SoJnV3m8sNyq22ONnp1JayWYcfWPUFyKDVV6iX0C4Wl4bKSE9EkZmpl2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=JlEaYmvERz9v-wCKkdfNojJWMyX-IRWU-hjBX8aKIBQoNwCfmrWb09bVIIbikpEhU2AXrIT-14osal1jFSPCljhfLemB8H0lTMjpatmztCmyw0BVejI3WzhhWdJFLX79VP792QCGPVL1hlfH2Rm8PIfE8o_ehrfVTfXZU6OoK1cOE7lZjYAFkWDBIPHNGMQIbB9SEUa97H-Sx_PhWNtAIxIdUNYMoD2REUom9aTyDrMR_dD3UqcSjJw48sfFCedNkQibNy-zfhA7DU7xMVXDdNLeP4a_SoJnV3m8sNyq22ONnp1JayWYcfWPUFyKDVV6iX0C4Wl4bKSE9EkZmpl2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The peoples of the Persian Gulf today.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84006" target="_blank">📅 00:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84005">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0bf4fa41.mp4?token=amULmUt4cnz0DwCaRlGDkFE31PEQCaLQJpT4LMYEO_GjraGM3SnbbvzZkjKD3n6SQyMPDshedJXs3F9ScZbQoZe1NNjg2Poh9exptFZxgFQcwvCo0wUeho1IbppY1fhWG4cBG-wcM4Rlv4TDGYMpemvNpgd9zJGfdb_XUBH3EjC-uMhz0uV6S8opvdBkRuZaQsHpiHWp961xtznqpt15QLzzSB2Nq7SnzUUsiEY5VvG7eAaYkAvaINKBg_AcFoipls1s4O5SWzhW_4HqgVrlMSifZnYZPuoix4fiiR1M03QJrbJeJLgQcefljFTHvBHzxWXOzuDjil3yeQVfwcTPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0bf4fa41.mp4?token=amULmUt4cnz0DwCaRlGDkFE31PEQCaLQJpT4LMYEO_GjraGM3SnbbvzZkjKD3n6SQyMPDshedJXs3F9ScZbQoZe1NNjg2Poh9exptFZxgFQcwvCo0wUeho1IbppY1fhWG4cBG-wcM4Rlv4TDGYMpemvNpgd9zJGfdb_XUBH3EjC-uMhz0uV6S8opvdBkRuZaQsHpiHWp961xtznqpt15QLzzSB2Nq7SnzUUsiEY5VvG7eAaYkAvaINKBg_AcFoipls1s4O5SWzhW_4HqgVrlMSifZnYZPuoix4fiiR1M03QJrbJeJLgQcefljFTHvBHzxWXOzuDjil3yeQVfwcTPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇺🇸
مسؤول في شركة HKN النفطية الاميركية: الشركة قررت إيقاف جميع عملياتها في العراق وإقليم كوردستان، بسبب تصاعد الصراع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/84005" target="_blank">📅 23:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
🇺🇸
مسؤول في شركة HKN النفطية الاميركية:
الشركة قررت إيقاف جميع عملياتها في العراق وإقليم كوردستان، بسبب تصاعد الصراع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84004" target="_blank">📅 23:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
‏الخارجية الأميركية تكرر "تحذيراتها الأمنية للأميركيين من اضطرابات في الشرق الأوسط"</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/84003" target="_blank">📅 23:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وول ستريت جورنال عن مسؤولين أميركيين:
إيران طوّرت أساليبها لتجاوز منظومات الدفاع الصاروخي الأميركية، وذلك عبر استخدام صواريخ تحلّق بسرعات فائقة للغاية وقادرة على المناورة خلال المرحلة النهائية من مسارها قبل الإصابة. هناك قلق من التحسن الملحوظ في دقة الضربات الإيرانية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/84002" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbyAkdgagRQzACaugyGs2-ySwNwPLBt55UHaK9cvhn5r-wCZO_ofNARIpyb5Q2CDSsiFbmcMtb8sH2N8WmMhKi19TZ81lH_xCanMjwP-8kmaZ92AEjEaY_an_0xKzQ8BzUYUkyhMYbjRY8f5Odw1Gfmy_CcAYM4o5Eu5ZE2EoTk5-BmkJwQpXOoaoki1rQyOYfRmx9weilgGbLtIYAnXym0hjwNtrqExgiIEDtigs4Vde_JP0Zt0aPy-BpDUY5QNrZLvrYQ7TzBbGznV9yfhb3hVYIMWRIHztuY5lmhtL4OdyqqoVqkWfG7Re7VnIwE7gzidneYx3IFdHEGHTwGCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام أمريكي : وحدات السكن المُعبأة في حاويات (CHU)، المستخدمة كمساكن لأفراد الخدمة الأمريكية في عدد من القواعد العسكرية الخارجية، بما في ذلك جميع القواعد تقريبًا في الشرق الأوسط، لا توفر حماية تُذكر من الطائرات المُسيّرة، فضلًا عن الصواريخ الباليستية. يشير…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/84001" target="_blank">📅 23:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
🇮🇷
في غضون دقائق قليلة، سيتم نشر رسالة شكر قائد الثورة الإسلامية للشعب العراقي بمناسبة الجنازة المهيبة للإمام المجاهد الشهيد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84000" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
الاصوات المسموعة في بندر عباس ناتجة عن اطلاق الحرس الثوري قذائف تحذيرية للسفن المخالفة لقوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/83999" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تستعد المؤسسات الأمنية الإسرائيلية لاحتمال اندلاع حرب واسعة النطاق وخطيرة في جميع أنحاء المنطقة بأكملها.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/83998" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
🇮🇷
في غضون دقائق قليلة، سيتم نشر رسالة شكر قائد الثورة الإسلامية للشعب العراقي بمناسبة الجنازة المهيبة للإمام المجاهد الشهيد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/83997" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عمليات إخلاء طبي لجرحى او قتلى من الجيش الإمريكي من الكويت باتجاه درمشتاين في المانيا</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/83996" target="_blank">📅 22:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9oH2rchW5adQGS1Dm_inFqfwwjAUppTAIlXRvWV9rLDtwDG0PJHHCII-koPO0YVi986KIJeBZioYH5L0DmhtdrBLYMGg5nqWa5ZaD34CocCW7zlFXso8Oo8iVIvTdRjeJy_o1aPUPwa9J3Ce-3t0zkcj7TYtWNEeak_ZXxOsTZEJXEwtJM46DP9pO8tN7kg0H7oAYunLISC18F4fzvKnWoham0ouUutS51fGb9WKYXSygrZBCQW_JYAuG3gjcINoXsSsdtPIz6YzBRhr47CkCUVDmZdo9WPREqUPmiKp6kmpmmAoTM03bQ9nFJYS8o7Iet1QjggOWyQtxak_O-04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/83995" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
مصادر إيرانية تنفي وقوع اي انفجار في سيريك</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/83994" target="_blank">📅 22:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الاعلام الاميركي:
16 عسكريا أمريكيا قتلوا وأصيب أكثر من 430 آخرين منذ اندلاع الحرب مع إيران في فبراير الماضي.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/83993" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
اهلنا شعبنا المسلم في الكويت
حسب المعلومات المتوفرة لدينا في حال استخدام الجيش الامريكى أراضيكم مجددا لغرض الاعتداء على الجمهورية الإسلامية فان الحرس الثوري سوف يرد بموجات عنيفة لن تكون بها مصافي النفط و الماء بمأمن بمعنى آخر سوف يتعرض هذا البلد المسلم لدمار شامل ننصحكم بالتنقل فورا عبر الطرق البرية الآمنة بواسطة العجلات  " طريق الخفجي ، منفذ النويصيب ، حفر الباطن منفذ السالمي " لا تنسوا ان تحملوا معكم مواد غذائية جافة بطاريات سريعة الشحن ومياه نظيفة للشرب انفذوا بجلدكم .</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/83992" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6808cb44.mp4?token=t4CL4UgrPOGNu4IIbYrxgi8wGOMw7kADZWIhh_YAuD1zrSQTwI5oqJIbKduZ1BNk14hKjprmcKfJZlDLvGw8Jpr4ZjUyiZce-vHaok4fBgSzD2UgVK2eX3Hwq7klHpKkqwsxUdwF5FlJ4O7rKgBFeC2DC5AnVGNj3CotzYyB1ePWmmmsXlBh5xan5UHx09zenZTuFfYCRps-miZ3Qz3Q1cbdtBHNXDMx_9_yi7zr8nQp6xqFSiWKPJHUbG-E2tstmK7KSjbdaQAFrQ-u-xen9rXkm96MayMewoNM6LzHRXB-Wfz4ENdmXbUxUY_QJ02iMF-iJBg1NIQqHJbyWrSVUAFcBu1Xf7CnwoaGar9J3Oj6UriqoAMDMXsqL-x4AWNAlIXR-1NUzQioYN00O8hBFy2DSnQzNIETrQ7YJjnk8ykhuv8vnJpfCfvAutYHBygoG2qmcd8FdV6qwPSabf6Qo0K_1cWzPYLBP3VPkNWup3mkSv9veu0NhrA5IkhBNoWPzsh_7bZLb_U8yxjCJPhR4UVk339tQLovyBYZfeE-G8zzUEZY1CS6Xo6H61cZe_s5UThxizhfyBhpV5s69TcOEOqqTD1VGRuDv3AkjVpTfIYlA3xwHktGeUW6OBBx5QAK8EuDzvxHljY6b4Q9IfdYieikD0uTjKWCyg2TsBPWbPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6808cb44.mp4?token=t4CL4UgrPOGNu4IIbYrxgi8wGOMw7kADZWIhh_YAuD1zrSQTwI5oqJIbKduZ1BNk14hKjprmcKfJZlDLvGw8Jpr4ZjUyiZce-vHaok4fBgSzD2UgVK2eX3Hwq7klHpKkqwsxUdwF5FlJ4O7rKgBFeC2DC5AnVGNj3CotzYyB1ePWmmmsXlBh5xan5UHx09zenZTuFfYCRps-miZ3Qz3Q1cbdtBHNXDMx_9_yi7zr8nQp6xqFSiWKPJHUbG-E2tstmK7KSjbdaQAFrQ-u-xen9rXkm96MayMewoNM6LzHRXB-Wfz4ENdmXbUxUY_QJ02iMF-iJBg1NIQqHJbyWrSVUAFcBu1Xf7CnwoaGar9J3Oj6UriqoAMDMXsqL-x4AWNAlIXR-1NUzQioYN00O8hBFy2DSnQzNIETrQ7YJjnk8ykhuv8vnJpfCfvAutYHBygoG2qmcd8FdV6qwPSabf6Qo0K_1cWzPYLBP3VPkNWup3mkSv9veu0NhrA5IkhBNoWPzsh_7bZLb_U8yxjCJPhR4UVk339tQLovyBYZfeE-G8zzUEZY1CS6Xo6H61cZe_s5UThxizhfyBhpV5s69TcOEOqqTD1VGRuDv3AkjVpTfIYlA3xwHktGeUW6OBBx5QAK8EuDzvxHljY6b4Q9IfdYieikD0uTjKWCyg2TsBPWbPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله كادر القناة يشجع رونالدو
😆
سييييييييييي</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/83991" target="_blank">📅 21:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e223e42f10.mp4?token=XFT0495-Q1gZyYiHioETHuMRKh_J6PkNpTPbXMyuLF72r8zYxqWCcyDQnVPd4lFRpJWWhro4PYh49EfDNTmhh0Lrxj4wJDhugbt43f8fPzhFyTZEsx0Ct6GhIXvSYLNmA7w3Vu2TygxiqwEfoAp7zLnAqM5ksMzEhHqSSnaNn-OcpTahzuPQMxF7ejf5T-BZzKRPEwP_Jbfcc1dFUQu0glBK0bbV5qgRYIzsYK5a-1e8k3cas1oY-zwPGUuZZfU8XAmIBbC592cvV-FBhrm8lfuEnfi6OlsriEA9gSME7ytXXwSYQ2dAY2UTpZ4KA7AOboblGu6ugr8VlybnDrl7iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e223e42f10.mp4?token=XFT0495-Q1gZyYiHioETHuMRKh_J6PkNpTPbXMyuLF72r8zYxqWCcyDQnVPd4lFRpJWWhro4PYh49EfDNTmhh0Lrxj4wJDhugbt43f8fPzhFyTZEsx0Ct6GhIXvSYLNmA7w3Vu2TygxiqwEfoAp7zLnAqM5ksMzEhHqSSnaNn-OcpTahzuPQMxF7ejf5T-BZzKRPEwP_Jbfcc1dFUQu0glBK0bbV5qgRYIzsYK5a-1e8k3cas1oY-zwPGUuZZfU8XAmIBbC592cvV-FBhrm8lfuEnfi6OlsriEA9gSME7ytXXwSYQ2dAY2UTpZ4KA7AOboblGu6ugr8VlybnDrl7iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يقول طيار سابق في سلاح الجو الأمريكي، مقرب من القيادة المركزية الأمريكية، إن ما لا يقل عن 3 إلى 5 جنود آخرين على متن طائرات الإخلاء الطبي "لن ينجوا على الأرجح". وهناك أيضاً 15 جندياً آخرين مصابين بجروح خطيرة تهدد حياتهم، ولا يزال مصيرهم مجهولاً.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/83990" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui-af23-DcR3h3IgxBB1AnPL_9hS7tTOtBXamP7GDqKnv4uuDsblWnU_Ycod2xUWGdSmFtTo9LVpdf5tFS7WxAfc_2l-_d2KvuLPGN9iWyntnH1NB-aO85GIEEl8q-oDUqSUAKiEVheRDWlvkdBXCEX336zBBW-BA3yuml6QeW6_IFSs0nOuyGuEziLh__Ye9lwIF-nGs3JEKz4VO-Z4F8NOyn7P_FKyCa33SUlOcmk46so6T047WP5vRJGin7RHRQ1ZWXZjdl6RewiNc68n2bT6eOTA6f8UZR3NQxaxYqeHY1TNP028WhKDuZfUOVJ6vK0cXgt_08W3Qsxvafi--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يقول طيار سابق في سلاح الجو الأمريكي، مقرب من القيادة المركزية الأمريكية، إن ما لا يقل عن 3 إلى 5 جنود آخرين على متن طائرات الإخلاء الطبي "لن ينجوا على الأرجح". وهناك أيضاً 15 جندياً آخرين مصابين بجروح خطيرة تهدد حياتهم، ولا يزال مصيرهم مجهولاً.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/83989" target="_blank">📅 21:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a333c8aa85.mp4?token=ozA_Oaf-gnqbhMaEQgj9j9t-ALBOIMics3Qs-1eMIeBL0nfhZpQEwfYzciUxtI8PQ26hU9HG4QAaHyyhVql3iUaIb5Awo9l7Ga_Gxgc4t-lffbPyz_SRlWHnVjCseyPQlbHqpPdY1oKtV6yQIB9fJpeHZjDVkdY5miTm9yFNA3GyKChdmioeVlZDSWP9nHHy1czvTCWF63uynvNSnWtueBTsadorAAQniZzDK1_Jvpy0FrkknX4ZeubQPJPFSWFsVDKF461Ukbeq5-cnWJw-Jm5XK6HvfdhZ8vnovkUJW2TvIWAlcId0F7CQVH-gBChBRQX1qsGUwfHvtVOils8UOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a333c8aa85.mp4?token=ozA_Oaf-gnqbhMaEQgj9j9t-ALBOIMics3Qs-1eMIeBL0nfhZpQEwfYzciUxtI8PQ26hU9HG4QAaHyyhVql3iUaIb5Awo9l7Ga_Gxgc4t-lffbPyz_SRlWHnVjCseyPQlbHqpPdY1oKtV6yQIB9fJpeHZjDVkdY5miTm9yFNA3GyKChdmioeVlZDSWP9nHHy1czvTCWF63uynvNSnWtueBTsadorAAQniZzDK1_Jvpy0FrkknX4ZeubQPJPFSWFsVDKF461Ukbeq5-cnWJw-Jm5XK6HvfdhZ8vnovkUJW2TvIWAlcId0F7CQVH-gBChBRQX1qsGUwfHvtVOils8UOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لقطات حصرية جيش الاحتلال الأميركي يطلق وابلاً من الصواريخ من الأراضي الكويتية باتجاه إيران خلال عملياته الاخيره.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/83988" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYIrQZZoXAQnMALIF0CHxZvscpRCzu-mEeiBeyUO2AQiX3_6yctkvKh7Dcf_QQu8XT3FAgnVcFJNdrj9gG6qy1KPDmI_zT5LqluDyJ1t77FCK1MkbyxTRG40K4QUXr4fInmrHtY5BN9Ggd7HPA9njObV5poRpR_f9r9TG2uJvkeyaJsIqLHFXUxxdhqKvcfnodPaof2FkZ6uj85GGZpPtkZDWl9PKWKNvU4lWUCxOUhkTFosQM1yIHbrTMGWWxfJ0Hty5hKIZz47Fy7MDuUkNmPlkORWXeeDaqXOm7W4CPUeZ5N7UbLYk9vj1iBk3e4yOxmr01-x2NrPmk9CFgZJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام أمريكي :
وحدات السكن المُعبأة في حاويات (CHU)، المستخدمة كمساكن لأفراد الخدمة الأمريكية في عدد من القواعد العسكرية الخارجية، بما في ذلك جميع القواعد تقريبًا في الشرق الأوسط، لا توفر حماية تُذكر من الطائرات المُسيّرة، فضلًا عن الصواريخ الباليستية. يشير مقتل هؤلاء الجنود داخل وحداتهم السكنية المُعبأة في حاويات إلى عدم إطلاق الإنذار، أو عدم امتلاكهم الوقت الكافي للوصول إلى الملاجئ المُخصصة في قاعدة موراي البحرية الجوية (MSAB).</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83987" target="_blank">📅 21:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc325e131.mp4?token=bj7Vipqhr_gaDia6UM7ZY__SZEYFfPEK7tcM-DbdeEuD64rHU4sAUIbM2wCLnthYyVIx7geyIWYV0JeDAcL4LbSnrIO16LoJ-6bxjCEcSsUNwH4EuXFDCIEghIDMOGGog0CetDaCV4vWeK2kBswosLHpnSu8Rxg-vSUqeFkT-d5dRYU0hoABPoIn24JeWpK9RVVnxDnN40_YVvMwDxIoq0Stqnlu7dgtljum6soL0RIxkGo0RKFDydWPu5hqM2ig1Pu7o5ZeWNqEu-JG_zKcBLvfZ0IHP4KiSrI3GCjdmLWhBDfSIU3YJjiM0N_7DenBRst-k2s5juoibzgpZCX2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc325e131.mp4?token=bj7Vipqhr_gaDia6UM7ZY__SZEYFfPEK7tcM-DbdeEuD64rHU4sAUIbM2wCLnthYyVIx7geyIWYV0JeDAcL4LbSnrIO16LoJ-6bxjCEcSsUNwH4EuXFDCIEghIDMOGGog0CetDaCV4vWeK2kBswosLHpnSu8Rxg-vSUqeFkT-d5dRYU0hoABPoIn24JeWpK9RVVnxDnN40_YVvMwDxIoq0Stqnlu7dgtljum6soL0RIxkGo0RKFDydWPu5hqM2ig1Pu7o5ZeWNqEu-JG_zKcBLvfZ0IHP4KiSrI3GCjdmLWhBDfSIU3YJjiM0N_7DenBRst-k2s5juoibzgpZCX2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83986" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83985" target="_blank">📅 21:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=b5dDPvdQ9Lzc-e_JMBUvCReT6KQQeatU63D4RyIy_aYk2XS5r8Lzb9ZzI_vJww2_6NTE3NXguMxsVpXoI7MC5UBCoGU7Av5d7qLkYNaRiHDlzVaDNU6M2zOrKT4Xv0Mxoz2qdPZWMsgI1Ys-fuSpVuXTqIuQhY8FPdmW0wQ_aJrNYVhYld5OLDrBwn_MuLdVhTQ1SbuDYA7F5NiwhIbzjBEIlSx-ddB5jF3bSaMYERMyHysv2c_wNU5wMEjSB0VaQIpyVpLqAvUbE2QFf6QpIqUdD41em8iRQIO6VgnmQuwnNRrufUmmTn2U0I92ekLX9TiVK-pvZgkiyD97X4cv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=b5dDPvdQ9Lzc-e_JMBUvCReT6KQQeatU63D4RyIy_aYk2XS5r8Lzb9ZzI_vJww2_6NTE3NXguMxsVpXoI7MC5UBCoGU7Av5d7qLkYNaRiHDlzVaDNU6M2zOrKT4Xv0Mxoz2qdPZWMsgI1Ys-fuSpVuXTqIuQhY8FPdmW0wQ_aJrNYVhYld5OLDrBwn_MuLdVhTQ1SbuDYA7F5NiwhIbzjBEIlSx-ddB5jF3bSaMYERMyHysv2c_wNU5wMEjSB0VaQIpyVpLqAvUbE2QFf6QpIqUdD41em8iRQIO6VgnmQuwnNRrufUmmTn2U0I92ekLX9TiVK-pvZgkiyD97X4cv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لقطات تظهر حجم الدمار الشامل في دويلة البحرين نتيجة الهجمات الصاروخية الإيرانية على مجمع استجمام يرتاده الجنود الأمريكان في ضاحية السيف</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/83984" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYauBM5wLu6Fscj4sIIFCRTqHmAGynAxZ5AiANhrEU5GqGtGtVXcMqsadFQDWqBJCBGpmlG1hofTwfbDP99Lg85Auz6_CaspUhMBIDT6ReARNix46ozYwg-O5ia-p6GenM6OJGbrfeOQncTmSneMUMVSulMTPbg0mARQssBup8jYJJwmGSIn5CkVTLeSkGwROJi_xR-AuATpZJUyMsdgc9l5liC5YQP_qxFT9ZdLSM-9H3OysRvFNPCwJSzhlw7uRbeiB1og1BidsZ8BUm37T6Zp2fG_3MedZdWblNBOyUnHabRUfkgObReOZDnynWpwrg2MjMkTxVJarwJAvLIhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83983" target="_blank">📅 21:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله أكبر  من الهجوم الصاروخي العنيف الذي دك القاعدة الأمريكية في الأردن وسط فشل تام لمنظومة الباتريوت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/83982" target="_blank">📅 20:54 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
