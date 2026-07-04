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
<img src="https://cdn4.telesco.pe/file/JIQpRkqx9NoEyOi5Jl0u1L23smQd2f63yAJjQOI7E2VEAQlxNTBHbyTEAfO1_IqwReJGL1NMDUTkq1tMsllVgxZWCrXLglrNa-4cG9gN3A4H9OnlbGo1pIkcZTYbOMkELZmD_GUW0_yd6Tw2GpTfLJ18TvwOTo3H1J3ROlCEE7jY0CszWmQQHEHUTQcY3qDTNvJqgWPUpk6uqIY-0WtLSbYkpdMg3KQg6V9ACp3UWmS7Nt9RV7MNLHdqsdL1kdXnEeKlkIU2qOWA30MwM_fBlzokPHDaWpPz2inAolF060B_SqzudOn5XJRIxsEH8NNLBzBxmUiKzYtZvyqu_DdNUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 371K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 15:31:30</div>
<hr>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjR8KmeD9QxSDcg3D32hAmqATswLSytytuWZ02v9cF7EjcqTvYK-llg8ywl3TadooJGAAGi2-H_4dGGpCnIZ0JcfqiOkV9wex6_FBLeyqr2PDgZs-zgZgi2d-f7SF3qyh1Xf_rs-7b-Wy6jcfnVQ9o9eTfjW-MiKI0ivrMzmAe5hSxvQzV4eGLSK9MrcHBDqZ-gpZ07x8iYjplRhag12TBGbBF8hHmybN8hmbSwPXL7VF5AvHSdFG4dxpR96dQKwz5ooS1G9a20rqoaAUkjuGQhudPfmHAzHbl4nah3GCqJ4qyoZ2tt8LSl65GKlRUIwkdRVt69VC4qQWyDsGAMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ2AVPrtOvWGswWDe9bOlhrTywd97EmPNduteCgg7vW0Az7J15MQUq-f6MfyuagpIwgK9QHmnxDz9cJB_DGLwk10kdMp4JO4fWiJmP0q2XU-DmVrf9XIcof0EbXu6XZXC9jt5N9Znj8wug4AOBGVCOPwtBmup3fDZBovcu8xuOPpSplnUqnmyS0ApnAA_UFrEKz8U_rh_2ASpCE8JH_5RhcKMwTkcc0GWiHkbC44HwyB2zj8kN8JxibKHxE2FXj873FIhymxLru8WJvqs71KZg_8QaFOUxpacvUl49oOfxeN8I3GPFqUZzsSVjBcvphTX9eNpJ8rk8W8jP_BqEgk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRZmIF_azQyJHTdKoqBTG-MhOAH2x3Ip7_CiRc6rTmZsZqEXp3X5BufR8oQHlnVb1ObC0Ri2hCUtnicdUlvKONVeKvB2I8P3RphPgJe_DuM-qxpBVktuS6QoBFUCbxOQPaltvR9yOQFzizm4nM7cuDrTCOn3ESC_A_ZRNHIrAUOoFKv7jbAug1Skoghb4ZgrANsIaHgmCB_da7Rd7wZbZBr-v12GZBKVCy3MOvfzTZz76w_V83S7whPmrT3N2VcBvYu1NeE3ZAjOk9U9Mgi31fGcUNk7x3UvNJ610EC9_4Bpc4HevTBwX4qV6mB-8R4LXfGPs6DigV7Exp0G3HY5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxdFMyNz1CDeKA1BM-MNw3G4vatX5PolSQyDmbLAByHmQXWg-pIgjbwof2571l-b1MDTtM7_6snbz3FOWZtnLy-835eqS69sIx8MLCAt7CISOuKPwy_XGHjQE5uu93R_ypjOg5rqlOeYRtreX0mPZWLSb86RFZkyspVXpCmW05skWdM2npcZhsPRTJriArFjwvbhe29Jsy-3zkIZWMepBcoCosgI_1oUAnhzEe-6Qpta1B9ACXdzGDFnVL-X_uvHZkfpGjD2Hw472aTIXvoHJtzUdoK3iDvTE_85ElJW3B993O3m4UAA_8Fy1Rvhmdbr3SUc_lcudza8c_wxRLUp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KtLBInV4F-JrTNqKc1KODLiOE-Yf6erWUjR-u2Fn_x61TFksSpxujX2r2eY-iQ3BIoCrqw3nJO8W8SCDhL7Uq2kcgJtvAxsw6s6Iff6nkRcCYuxRAMfGemybhNe9FjQaDqYWbbTLYxGgs7wlc5pko9kxAh3askt-3xPSh2zcRpIIG6si6EAwBxGviTmC24St9WRAkfVE7WZ7wR3JMfTNd8otJppPZ3RLx2sWrtFOlzidTxXk93PEHW8mNv-yc0wOZKZ5o4JSujxh8MZEE9viNpnqCbNkz4nL6GNndcLkQ91q4vB-olRkZ9o4jmUrH08uCa11y4OqIgVMJfpt4J7v4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbkK_1IUJkf1_veiWDw0kO7cfFYJov25sN30tPC79y2Xdot0KEvBnJGq_O4QaTgP1DEUef-Nldo2HqUKh20wbDR9aEcTBVVImknjDSTL82abrRG0mzO2OUAm31CB-lEKspo1pQug4uLrmPF3c-w83cXDtG9lM0Yq4MN1MqyUldd-9X2y7wcHWWoBtO9YiMCIInIF1QbFR5G4bl1qQO1hLTny9sbJy9B9JGi8b-hjKyiiMitoBXIQhJ2KCpq1KoMWyuSdQ-wZlyhI-D8v6hMihELnV09laP8LPZTfvX87f7jKAbyouiUxBsNHbwN38sxLG89fa5cmpiinm_mmR40Ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcMrsEwVAIcmhPGJCCyUgfItrU8Me4PzuWdKu2aKhN4mjMUK6ojJKi3En9vgDr0pemuU4AoQOOXSg3tQweu2MJzahpXvUh4BjtOmqn5WReMaDNyOaZDaUf8qe7NJcbmsBaK4UQWnQsulyV6PLpgs1bCOUi9_xUsNgeu19InUoj9yIOwQfKx5AFIMYbipvObv4xDLK2ynO1J45QSioiuUeZQ3iTGJVrwD4P1xZEd4eKnEEZOu9-sZ2stffAcEBa4tQlPBlMHISpqM19pOmLx2kyrhp2-8TeuNqcaunduPmJM-aghqq4FadnM-Ja6AVvyh12k8DDxSGT6g9Y6-QBPL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHC5-rsS28BYvXNHyrj5CfgwE1JhGcLUve2zcS5R_i9va8EfquBijFh8gCFL2azAkHSK7s7uVmt4pRtNiExRaQ5ym2cLcVHN6k41cooPqVualk6Jris_eWDBNbaPpAMrI5WFBOiykaSc_qXGHBYRDRwFUF9Pvzr0BvgCeuc6glWy6OWjiX2tTMcMDntL6pDndzgWmRcrp76FWS3O8aJi5pcDOTTVOmZQ5b_MwyXH8mANx7ePs_wK-fCfHdIMcUFW1Q1thKnBDOtad2RwlBCueKyG25-kXQE3EwbdEwMKkecEl9cDqCGuj_hSmmD7RJNcakrpbvDX3ukXImdPqXlr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=SS5HJ8XA6F8fM_YJCcMXnOqcJobprPaYuk4sPzW9GS3HHrfJuk3xbD09nSH2qEF4aYAKMk1EuhGPKjiZYMG2eHfi9E13OFyXd8SIQXD7DX2jX2ljIYRq4TsheD2ET5vyKGhkNjovKUFMCJv3vUDsQnrSa-nD6YFFgOyqCgCmQWHGbvW9J9zYNs-cLgRmE243tvrpJX0apH6ehvdDz76uTfD9kFe22fuyCMuh90UxPfYce_FEidJmlxbblDtDtoYhEYJGGZuSikCP_MVyyzyDe_GrabmPE3KJsr8BKu8LniO3Nbd2TH9ukLT9F6jhN6gHKP4K6lO5x7yLlg_RZ4iPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=SS5HJ8XA6F8fM_YJCcMXnOqcJobprPaYuk4sPzW9GS3HHrfJuk3xbD09nSH2qEF4aYAKMk1EuhGPKjiZYMG2eHfi9E13OFyXd8SIQXD7DX2jX2ljIYRq4TsheD2ET5vyKGhkNjovKUFMCJv3vUDsQnrSa-nD6YFFgOyqCgCmQWHGbvW9J9zYNs-cLgRmE243tvrpJX0apH6ehvdDz76uTfD9kFe22fuyCMuh90UxPfYce_FEidJmlxbblDtDtoYhEYJGGZuSikCP_MVyyzyDe_GrabmPE3KJsr8BKu8LniO3Nbd2TH9ukLT9F6jhN6gHKP4K6lO5x7yLlg_RZ4iPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSsPJA93VrcaG4xa4mmE3IeOtlvUiT6ZVWVlq1p2iikERG-ZsGe4qebdZb2P5FKHgyCF6Uxgi5IF14M9-_tmjzzGkre47hzaZuWtN7DG8gzA3e7h5o7Kv29f-jPj_gT9SLqslqPasZrnPRmk99qX8BaSbSVzirA5NdxRsvIaDQXva83-1OY9e6Mlf6NBhCDMe8P4QIodA4R5r9F2k3KCo_rL8hOXQYhggaVYW9ZyWe3aoO6UEbVwmwfpOylM7K3rI3cpn5Z1UEcQjxE1wJ6yvIhtLVJ_JQkgiJj5qTRTi-b00x7Zzsgzg0MWOB2wAtjpU0WWw33WFBE5OcbwRdfljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/but2wGEVpTys3ug7hC90Du-HvBWm3Sg3IllQBRQMq4YGn0TWMIJddoGQl1Dd_jyUUO8XuiAJ54FmIjsu0lEVbAzzO6D9M5cnay0jpEiHQSIYTw2RFVoJ9qeGdqEE7l_E-56KLVh_mIxxRcSpUB3Q8rHlZRJZdjboBEqUmOTv9Q-BSyFOrtuKpVAb-ft8s1PKBiiOvWS5IfQxsXo56E3V32xLwDDIrh9Mo7N8IkZZFAFjNJE6tJgBcNd8i4Zq7pq3AcggJA3fx1F61Xo9oY7Sr5_m4GfRnNf9iM-OfrOOniDl1E3YYZU-DKmNnjJ-5PhKzbukqMMo4BZaR-Xls0IROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/24924" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EyodCo0mL7MVtDfZ8G35nCp-fSpKAEVjrsz-_J_PRSH6l6U7kkQsFm2N1wfhjCBYJ4Un8J5BI6uama2FlwMtgh5vqXkHWs7Gb1TFNtvVMtpksYr1WZH7U7FqfzrVUNTHiFKvE1FM8w0Dqs9TPVp-1MhTFKmqNHwwxj7_pX4dkC5ojMJGLRDtTbXWt-H3FQJPWiNcF-BO6FucVPTGWfz1nm7zM_SwvUus734yZKnF1Op_5ssTmnbgeyszgurbqP-6-OIOk7NP2CHMJFBNm0fm7GNrHHQAGMBQ6r-dGYu0zk8leMU7FimFF_bQcuoYdX_NmWKlfrzMBVJzTP4wpo_K5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tM7CrLGjOfpd19CX-8TVKFDD1GGK3gb7MbwJ35qK_uTk9D7iAaMChZnddae2eqmbsOggjoD0bXcTOxZHdRqWS_jO9nXR5uWemacT00ntWTQftF5zZYQL2N3q5HGbR4PqKxqkcsFYHEBlmrTOZtvwU3SJxaSKFBAqJSj86QUr0WneUYjTDXzPtNlhcUAGfW1istM0gIM6rGs7BEeAKYnesk4CjhLYXi9UDHNB-3a7eSzXFfIynmTdlJMeeuIUIufM1wPgR3QJUIvFTj4lmVD1SOPaS_ZvNz4s196YSL-UKNkGKQzuB-wmAFXqM64Cz4EovoiKzVH4bFwjPWMBMvsITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STt2HdsJaZBdenhhPRLfcQKnP1ieiNQ-ROtwxg8JTXBlaxrJNHzheOaX3tx5YgsPwk2YXhQivsJNd4hA0zlPhogweYwUsLA-dC7zt2kx_SD6i9IT5lS5bNB-IGJ5iO1xhtXelNAbw7SevHUFpAWuUJ3z2HCOl77iaZrlAWBtKQ1xUrwvj-7pZOkrgGGrPNaLTGxl4ABRCIhs6Pktq7r_VBq8UMdVmXwCFM7nRSKyn5JbYalYsJLBoiZFEwSOAGnWR5R8hWZ1WkvKP6iQWtPOEy-_nTy6wazcCQW-lkxsdmXu3v2TCsSnSI3aWIkZT4WTTbmzrF27cXNpQeYvCOACeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWBRyahzwuLZ5PhJcikjtkfXs0lmicLLgz5-DsCxeo3iw-kRpkM3O_dQYTpxdGtuZJYKaTFNY1yjeTliBhpt13Kj1y8Mx31L8Z_GGv4oqhoYH1z2QjRPdzwcTOQ2px3MrvGqDyFnCu8rJ5qs81bnm5ot2yCs5dMDx0VSJ_feXj2ykIt1jFw44QoE-Lija1lB5VJxVmKCjJ5w-p6qPoXdPhDpVdZUkF2lR-qP6aIGV48FPS8ZePOy00yFpYybtoo2rBndCEGvCS-uoz4aWBRKGvALRVaUgD_BZ_OI37DZBdmPpn2D8QX5tQX1L2jCunfihD_Qr8YH21BtvIyNs-CYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RITVlhu0cuuiRVMTwrB581tu6bsdOIM4wQXp2q3nusAg9qQT6t1PKKZfoJ3beuyuCnwCd4G-_1Xg1oYyfzssW-aqMkApw972lkYHn8Axsq6v3xSPK8yUxMqbXNW-MH0QbiE7Mv-Co7IB8IqjjU3mIKA2iCUixgj9BseUmF7iV_-XSpYTC3-dFXFCRvMomWc_Ze0-5oa3BcyAxUo3649zwM9u2cDvwPXja-aDlkGwQAhUqPy522pxbPIU52StWXQxyXoO5T1hk9-4NU4aXYSHhGJ5WKbaWEp1pFa3VooZBNvfkrzPjl7I8iCBkDhFEIQNP8gXZeFkuXkM-1Tm-pYtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=QxL8UVnxM9-CJZZxQ-hT5rEsdqMaFMVaQBpBCHw8D9cNwRbYrPm1959gPx2Ht0U3SCVnuCQ1ss8FZR_mKwNdt4W1LrEu_-ZFCsPj-n8PX1w-KArOeHRYQy6z0Wdd6WFPvsx51NG3WZ--izA27AFzWPP-FmM1NsU3fRwmUe5pyZ26i__O8OPZs8ZWBXNFGOVrF0z0epC5sESxYcP5V_UQEH0KW9SLGyZ_6yDtxIJGggbgpdUKAFpzcDTCLHjm9V14hmMJhqM17-ijFhBlWZHCEsTCl_Xqydq2Oaov_Zut6Dt88QRbqGsfRgc93AuUTalecpCNBvmIjYCLT7jS0qSYZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=QxL8UVnxM9-CJZZxQ-hT5rEsdqMaFMVaQBpBCHw8D9cNwRbYrPm1959gPx2Ht0U3SCVnuCQ1ss8FZR_mKwNdt4W1LrEu_-ZFCsPj-n8PX1w-KArOeHRYQy6z0Wdd6WFPvsx51NG3WZ--izA27AFzWPP-FmM1NsU3fRwmUe5pyZ26i__O8OPZs8ZWBXNFGOVrF0z0epC5sESxYcP5V_UQEH0KW9SLGyZ_6yDtxIJGggbgpdUKAFpzcDTCLHjm9V14hmMJhqM17-ijFhBlWZHCEsTCl_Xqydq2Oaov_Zut6Dt88QRbqGsfRgc93AuUTalecpCNBvmIjYCLT7jS0qSYZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3NZRm5eyRslINHkopFek0rx9W8nRLzJN7S79rtiMHOSP_S_UgsmNV73AAqr1rc8_bcCK8FvUPoJhGz5Chp9CqxLS3Cfi31JUMS4MJFwYPl0_38pwbrGoMK4n6eJWOfplx72C7n98E6cPUnbC-_D0PRujDNV9eNv0C8dd2it13Kb8gJJQa9GrXX62X_zkr5wwWf0-BnE5rPk6JSUXI7wSRtqNdYBcViUsxw60ztScLU28zCpIfT_0UQEgXESmx53R5RMj7fd1nzkmkKYVVl79ELdXxYDLjud_DW2pTrH-mOHtCimX0SqQWT_GaNNQ-MAWrKEt4AShLw-bektTIfptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9IcGTPkLsrQfHu-FcXc8EJVeVDnRvzLvYRk73cw_oKistLNV_WgE8F0dEZg5NBOXX5VdLYAONARIL9fax_pPZp24XFSWLhsbSPeNwXwI-slhmbz_kdTsDf10ymkAjhMujW8uGrIwvMpYNKK3k6Z2qCmV7BYl0D0bEu5r8T4J4yN9OabScir7kcuL2DghqiECdTH2M64CmT6sFzxZMWJw7GyxLczsE3cLER3eIVGWsbdvHyLD57P4dZ64rdG_MTicb4OxDmkpYZA9K19v4xDwHIN4LbjEwFr6MIkqbndtniJYVODMoW3KZagxZStJFg-HE9Swlww6-VU5EBW7NnBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Qa7-pBrMB0NcXbcQDBwGBrKkVNsXW9S7rUamf_v3ba95kjxpeEKm3xsSpbhVnTczSv7QsylRFcu77mqmNRGjvfDSr7zwSCQxaOtro336NBq40e9QuX5YPv8BodkynzcPTeEizGOwebtkP0CguqxM1SCcxUjFTKA0uKfAAK3f5mvcvzd9x18yClmLLjvagVFOsfz7sfZNenWBILtGjDAuqatLwtGLBD_juNgkkEI_nOk5sS9VJeJhJxc3U2lR6mUIDANbWlQB2ZyFnRAldy4vez1DelTMnmCcLPe0gyp_3TlieEWkngTL1diCKDgmpcqCt0FTTo2jwwdFf6lpYHSz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Qa7-pBrMB0NcXbcQDBwGBrKkVNsXW9S7rUamf_v3ba95kjxpeEKm3xsSpbhVnTczSv7QsylRFcu77mqmNRGjvfDSr7zwSCQxaOtro336NBq40e9QuX5YPv8BodkynzcPTeEizGOwebtkP0CguqxM1SCcxUjFTKA0uKfAAK3f5mvcvzd9x18yClmLLjvagVFOsfz7sfZNenWBILtGjDAuqatLwtGLBD_juNgkkEI_nOk5sS9VJeJhJxc3U2lR6mUIDANbWlQB2ZyFnRAldy4vez1DelTMnmCcLPe0gyp_3TlieEWkngTL1diCKDgmpcqCt0FTTo2jwwdFf6lpYHSz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=oliUuWK0lCX5I-DzFMJMggt4ISJGAXnnoJwX0LTa3TeG0F8Cpo8NMFYTG5NBMjxOiwDP4GIMBwtjV6Z762ZxIcU8vRElaX-fu_bldUeSqY9JMEcrKs9IKOhDvKig9a03fJ-dLyiWRQqfNF2phRCKkP0pLjoUeq1bCwZvZ5p1dlUYEnkPKqrhiekLUlaRZbHuqP-NK2h_YgiWgk5vscLb4wtEfB7fPCjjcyxUGoGboAOsdZZt6fGMBaG9m2pEi4FjsGuMtStKoO_d15nQJ5uZWHXW3LOA53MnE7X-ScLVKAPIP4BXHdRcHxgFN1nhxcG1WMk5SV3KRhuf3_vcRnKnZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=oliUuWK0lCX5I-DzFMJMggt4ISJGAXnnoJwX0LTa3TeG0F8Cpo8NMFYTG5NBMjxOiwDP4GIMBwtjV6Z762ZxIcU8vRElaX-fu_bldUeSqY9JMEcrKs9IKOhDvKig9a03fJ-dLyiWRQqfNF2phRCKkP0pLjoUeq1bCwZvZ5p1dlUYEnkPKqrhiekLUlaRZbHuqP-NK2h_YgiWgk5vscLb4wtEfB7fPCjjcyxUGoGboAOsdZZt6fGMBaG9m2pEi4FjsGuMtStKoO_d15nQJ5uZWHXW3LOA53MnE7X-ScLVKAPIP4BXHdRcHxgFN1nhxcG1WMk5SV3KRhuf3_vcRnKnZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLjllfsmuXfbcibNoi--GsrxTxLNpP9ioirNhlt_JV8JpBBvbHQr4WGbVzIEH9KhbOv_tOchEIblV9CNGqWI3KTvj_F_yLUHf1pg5sFGD0zpJSLBSwLx6UfVV4GhukRN1UPaxDiFjEbucj_-Z5n8GfpcG-1M9mSwWUw7ldEVS6P4e-jQMeqZEYWURN-tFxpd4TnvvzJJCaqJVYtK8Xg86c4WPWYE_Jyi8DG--t8XkA105Cxp1PrNEyQSl_WbM_jbj1uy5nxzveMFmoFkhPdPzk_7yXWWlewxZYUcdUC_ctLtr0-mTTwkeZtXNFPKXBKNf6TCxlsRXEGzhYaeY-e4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj-qI4HKsGGxE-fA7yIEyrYqSpOCGWzMI7zYsrjJLFME_FPWRaVRepQrr6EBAptnAlCW9587T1_uTkAdsGItUOTQd7tS-o1zmQThOKVDbSCsBWAGTHmijX66Sh3wA-MH5fje_KAM7q36n-E6ASRR6jkj8zDViEZACOto2JZ0nivWVFmthPdUSfD3TVTVE8z_ErLf72pK8s2fgqH8GPTSyEZ35Ro_5FINHkC0JwQnoykl1RD0RoQElucZoHgo7xyLiWf2FbaQjoBE24WU1yICZN1tWfhCFsl9gyfYgxbARoMkwLRtzuVGXmPII0d1pUgmnOm6Jcl3r7t9MQv6pKrDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT5mubd8P7zF3mqZZZoRIKSxzoguTDfb3Y-dSxt9pmgAIzk3Xb7hRxSfuO7ZzHoEHaVkYYtJtQXc-gNwrhRLserWU1b5QR3nu8MzYJHvDKrIK3s3tviyWgTgLfCZ9FL5F3mPZLjiDGjz5HCPVxJ8IEyCWTGdtNPZGG272sidl7DMbKjyVepZOUZGLK2NRTdxgKwSeIIcwgARU9GIohh3U8QARkzScvUvRunQhgi9kat3FjGGWftS4CkgzEsqC3aAyBDv0pz-2vjg9x4KHzH1C3lRqa0FOcGG_inKn70GByx-4ddaUX9TLLEfqyZnNeGW4josBVGO_KqxrAhBsHEpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmiVKSZd_Kf-a-DDbWxCXSMVeQYDxq_rsdTWR0TQPcK8Q8zTaOndnQ_YGg4W6VwlZASP5QmaEV3z183OinExzdBRsSYNh_sFjVTlbXVhU78w9pvs5p8u8YC72BRmsZix2QQwQfjnEZB7UYCn_AngxBSYPB7VLazTmH7Hv9NMowik_ZXKOY7BS-fCtVhIIzaFUZCpDrMExjJHU-xb7mNgtu29CQLwlJFlWGgnpolSUHdm_snSWejhAIGs7W_nE8OdWUf3PPtd5vZId7JWkXsLeq-i-Ng81YiEHeV0iqkUVc9ac-TsVrM3ZXsWmFzxAfPsvDxpcf85hTYkjGNfED2gRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXlMCQMZ3SS9P2bKTPwajWgxciKFgs1deA2POZVCvvNykoXQ1K2EoPINuhTDzJLKE_MBiZOPVrucAMom0x2onMp4VKcqUu9GNG51AR4RLjy3E57oEPc2yFoCAiMxBjrLqt94IVdLs6pAmO32gW7ZSVSBdFA_GZ7hxNOP3KZAUi7ew0gUI_8w7oUp5NSql689KPLEXlRnrljUlVYUuR2t-mFLy4Am6PNzzPMxXEAKW9m_sFUadDKFdlpbXzhkoaXTI40Z7LcUAB1xyN3CUotYTWrA_PnolaDs_J4SzccLfxSsiMIIFE8btJHf07vs9yKBqaHkKG7q7iF6jSAtV6zl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=Ufgi4GB9k4PjO2ohhy_4K72FFhE4ZfiBaMtTUatuEhQIn_BUdN6-SlRAx86q4-PhvBFRQP_syvEpA36sncAICpZz-vMKQLjBEegG7WxgjS2AqZskyoqIBPbIazpYdsmnK9CeD03AOX55sfiEqclU3sO4iVrKG9CG8SByC40RtPPY8rEvR8TQvX0RTv-LbroK7ICzF9h9mC6_BBfk2Wytfq7g_t7EEP7nboICXy6zW5O08aG1YJD33ODL7U8HshPoU5QV-yZ1-1-MyohOHbHIcC1LtHPV4kZhDpJ48EyJazmIiY1MbQD_ybupylK2G0yXNflLTK4AzfwP5LsgkYh4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=Ufgi4GB9k4PjO2ohhy_4K72FFhE4ZfiBaMtTUatuEhQIn_BUdN6-SlRAx86q4-PhvBFRQP_syvEpA36sncAICpZz-vMKQLjBEegG7WxgjS2AqZskyoqIBPbIazpYdsmnK9CeD03AOX55sfiEqclU3sO4iVrKG9CG8SByC40RtPPY8rEvR8TQvX0RTv-LbroK7ICzF9h9mC6_BBfk2Wytfq7g_t7EEP7nboICXy6zW5O08aG1YJD33ODL7U8HshPoU5QV-yZ1-1-MyohOHbHIcC1LtHPV4kZhDpJ48EyJazmIiY1MbQD_ybupylK2G0yXNflLTK4AzfwP5LsgkYh4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBDsDFkUv-MEcmMZ_VzTas6SosvvyuxtIxp32VP0QIv-biCsq0pWXR9RW9RJWC5BP2WVFT7feLVB1CZwFTLaTvZX-XHdTkRMzegSSDiHLN09k4GO2ORt0G1c-yjEJk3clyyp5fzWo76qPrqGbpQxNodY42ZcL5QD4kYIQIBQkhPaJcQ-E9drSoYjj9A1_vIFW4i5OkJ3-T9wptZgR46srbya8i2PNpb-LL8KnpydY-N4fAV1yCsxZ0AibI35dvVoq1NZOYWGd7dv4Gz9i8XCmrmsk8fvGgoqvyJx_uWjEn43zYMFKoZzrRlruQQpSL8KV9E0HbFdlkoHJ-2GjwlWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ3m8EBCRxGPCPS_OV_Li5DZ96jrXENx9fSZIb7v1VrAk0DOxzoywRJWlmdHJe-NQVIYxqckDEHiriO4ImB1OzsngDclGuFJFVJg8Fkb7Jy34QTWXQMEAL2pwxxM-GohBMs115tOv8DWc1pSKkQk7dBgpsX3coeLwnfTuFdLzLnWg-RMEAaUX4QRnKPcc9JpsR1IXJxyMxsBc73WoAghu0bFXqGug2hv8KJ3CPJh_t8bxgVAPiWoaSbctFrSIQiW8jkZoSvAAwPhm2nd_K_oKYoJiS-AovFnm_pebempJP1Dnu8F2JJad6keNzk0ohIwBYNTSaUaF0cxQFieI18CyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUV4QWK8-GdRfRu2dzDVKXBX-4CpINwBBjWrgKFtVRbPTNTTJcdGmnLSjEgHa7WZhPOablTiey36HQB6Ns8rE9SS0LJtRFLHHMDyiKHHj_mHQJ9kYTg7DRSOj8Wr7n20HakWe5j_5YWUXhZDGqkZkdlWFCa4vmUxizbQPni3umksLzeKNn1hMSUG1RQZcyO_GBK9raXELbA5G4GQg0xSNlF7n2JpPtnN-Uv3pg30tZ7FcM3YabPaM-U4saFjeg9v5FNRQg3cHk51BBgmQQNC-LrLgU6Jo2dWRNuuE_fx0FxcZVfDfWeO8VLVNmoIxif8TSZD6rFqApjzfeHYD7BQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Hgf9fxLNhq0gF66M1clv5oN4ygh3PnPUj6fIHVRxr99ZHsi-O9XUmz6bkArDGVBaq6OlwP7_Brfqxo0_lSdPfFuXrwr5pgyuNSsAlKGZBKUud2DY176sM9xsxDWbEscG6JdlUywSePsuQWcscYyWp2XSJPb8Uae6a6-oTtPoC9Nn_8-WQvp_YI15uoReywQX3kVgbUYf09imd_YTQ_ieT4rE_ij1eLku2MH6z5bZ2dv-aCBkQnDMFIGoP__JMIOQN2hBkuo4Jl9iSz7pUOAvxwhjSjgBMh1mFNea-tMmkGmvrGfff-uMwosV_NeF5F3fv7JBcpErn2lB7nUomyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XbEm1EMMQ08_opBMmiIEI-u27AnO88GTp6F7VhN7XAWF2ttqPa41KYomLUWDQEAs4XkVGDWp3HXVMwCLyAREdTDpSGevGlTMn7UrQHGG8AXhWP3Zal0HI6GhQBxfMVxz1VdyE9KftYMRvxeWC0pK47F7O3-kvtexiLnhyz6HAdsq3BvoIuULNcqF4h5_0Lq43XTnCzWcdycIRtDUuEz7HUMjEib9DgP7GBupTI4vHXB86vuxs9zN-jmP_pn3osUxYnct482NimCyqVxhK4_ZhnieKTvk_sGNx3vAKqVePnaujzmBdWpmP6n4SwkkfOOdUleps2P2GR_WSOCtPdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQs-rYT9yCYjNjMuCQ2VsBW_3FXPqCKDrfE92onji-jcUze6i341--qq7M1GDG8LEy848TbAsVzB1DQPulAjYSS2Jc3PEmPyxEksq-YhIhAHWnIuoj0l4Y6s6FYvlv485bCyIOd0Y4StvjcS0QzoLNY-4CFawnwGRjziHvSDq0g62I5TGh3MSwEJamJmZ4AmS7h1uywp76RZZmpjQ5fcB-KdlFKhdhz5HOuwqirxQUstmDkCU1XmCwwbnQGRQNgWfMV4oPUG8PN9raLiDK4wTDFEqWuOpm6SP12AKibeCmpUcfO4oUvmITzUCjBhNr8slv1q5M7-HK729hggzmZMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIxl1cQP_yygWpZoM5XZ-z64Z2dqZKUWzCPD1MVQADkeezR4v_BuDOZ5BoyXy1YrRy4HqqXYqkCV3-MMgUGFspb1sxUabvHhiYfVTBTN58f78gnih406ipPQCCZpkI4wHirefmVqwnMMmGlP8jKa4zAWMMsGnvo_9r29G8rWQlhzWze4q5DCqJFzfkJfPRvBfXZXKLAOV6y5OF3MBj8tnQA2vjK4v4x48NPBiBmUcL-8GmLTN2wRQMp5pzF1fJp7vNbWELOKjFKsdYWHhWzgOj-1Gbocn2uretZVA-DlIhqHZE6ZGhUHMj309Gb-c2h-RagMqFj3cm-aV_8TifxqBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHRC_mxpjUNERLOiUZRK05AaYdF12xaJ9OJv16XD_zowJYw2gaAqL9h-yQGGy8u9l-Cb27pj2hpyFaC390uxz4uzqYX5PixDmAivm6VGO0NqRmSWELtkGNg96Ampf2GLZ6eOk23ulhfVtsPvwbj_CW1IfXaEAkEoVyd6QIqmwcgEHrbR6y9s2tZCAOL4eQez6MwJ4uqyxN8ja1JDWa0M9kEjf8tNl7OsAEL7WMAhOjsc3es1R6E0bCv8Xg5RZYAYairhBcSYj95iDjlm4NmFuNcui1NjFGDj1jP7gSb2TYgsmsOfh24D-yhFwabvzOT5FD3L9dQg9hqF51xEueolkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF0HAadMuXlnEQGt1-qQLh40UDr0GPOwiti44sYeEzQj7UfPh17ASGWw0sNUExJO85k1aUpXpnScI7ZdaZhutPYIjHIPhKjaCOjCLBtMGQMVwH9mVzEM2mi1qo2GdFNOgNOosO6_DOqIUExGGp07Zkmwrr87Yqi_2tl7gnOtMZet-RM6lC3XoPVPmO0d8e8BlxsexxXIc9jm4uj2hzSFaHxYqyZIawTwMQT1wt5LwF3jXtNcbIr2qlAn9jqcQeoMaqEPaQwTpA7-bW3sOCpuXWV2THURjwh0p7urXFDRICUpzekhVFsrVfsr0yZO8cNyXnuJby1g4gWW4qOBwUCRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsUElJ4kEmDTovOTQvhYxD41_rLQNv1wiGk_FKfWn59-urN8mi6mnHK7VnzkUHuu66hcbDvJMTpv13B-xOasbTzk19LrbQJ7KSGIIi7QnOxhqAhOL2EyiK0BIiCTj5jiqKQUPyUFdA69zdpwDEx9rNTUtCxs_EoIqarFlRFN0jweEmgSv9yflR8u4eW5DWmmdcIC1qU2BhfmPKoBjvIMBSU0VPlFMLojoWPhRqx14yFv4Azo7nJHxeneCY3cP4jIrAOWgEXwGEwT1mH4_nLgsAgu_J6cXtN45u5-rPXkrxxQerXBQUzOVKdBMeYcKKWXpmbFUeomPph18hJ9watvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO_8rJU3qwUeqycduwFJI1-4oF03sB1krJqGnDakoKHjIYf9OTNPAbaRbedzoo1YkUTls9Sy1SfWyqNhGXbAUEgkI3Mb_Cmblz73Nwnyd1CHgCB5l5Ov1kYI9boOOgA2BoXEs0fM6DdOWeOpc5twGJAfIrKdSgdlDY50Ey5MJkKHlSevXUvWRrmsP-wEdaaD0vQoY5ZyJdmY9_LYS5UWEMItH0y-VFmfj20CYfe2PaxwL8UDdfEzSqXGxOpRoeHFmEojU6dOAXDr99Ayby0Je80kxG3BBbsoeJ_hdaGATLQYqz5Gz_W_GwDNCnj2geWviE3A2D_lDhnOVpPaHyQ8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r48c7rKX2P0D9KML4NLF4PeBd8Ykvxqkompp17-A5s9kmR2N4NM36RXFpaziQI4VU8AdCDaoG9tZT5gptKbpfZ3gETet51Vl8oY2F-VAQr07RYNT-av97h7t88q-1Xop2vLEbpoBQSrJnAgXMtXqHdI2aYtPcneaxd0-8LQ7V75vSBkABVQW7je-A__e_0HWlzn4fDlrjRBAToJH3koUx2JIIrCwj9fWqT2mc0z3PniJAmyYRGhMazc0mO29sRg9HLMID8Mz_csAMRNRUCQPrue4tUthc9X6PdIwU5FpWQ9lrtObKNRPgB5-y4z67Nh8-VbtgrBd9908UZuvbzQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTwD5F0k3TC5lLObNGIGmLs4oF2SHrbBzmRkywxIsuw6Wq1_rESuGoUn-G46LWs8W2j-qZ_cqZNZDKE-ICrbA1OpTPpkTZmUDljX_UVFuqM0ghn0hPtDXohKg1ToC7GpeFDf097gUE0DWYckSw2eWZZJBZQKeyfKrQDvddzq77SX91Czib747bOrt5femvg3aHux3Tr8UWrq3JyJxBAbmVJhpOzvrryKHX7Qk24Z7tYPC6a51Zd5zK8btHYcqc8PDQHSdveh56jXXBAvCA9wr5vn8CCK-wIv-vcJ7xoNGx-YypTgMNi6Vy2_c6cTxh2h8-2qzKAoTNGS7N9kHKhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۲ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/ZKTRF62467
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/VGPXN72923
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/DACCB49184</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knnXXb7ru_Hfd3xD5wgzv773G5_DeNtWeiPOe4GTmp-HvfXDwxaLz02VJydWZFoEUHgJTn6ARA0PkP1h33ywdXYuGgkUKmM_nhuVpDz0R061M45w17I4kK82mkXfjYX1dOQHfW31oKykjkt4iUIviSg8k1CcfxS8VmhO4-fkCAdqoBGRHv6EYQy5tDAa5h21XTVqf2Zpd8ReV4ExDFQcnHtp5Nl57oxq6TTqAavM8rz2DCLOi3NRn5i0CthJD-jt2p63CtP6CSM6seg-DjjkoYZO1M-EyRWVr9TCpCEIccQuEie_96GnfpkLSLaSSG0IcJ1-vcpakQ5dm22vKjtLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=EYg3jn0Ape7JXWXxhr9_eeibCc5No5yPG7xynZDtZl0LGEY6SdHhHRp8ngVYP9DeKofft7fPf_3Eyuw_FspPIrokp1RoaZQYBkXsVZYp-fidjm8FTvtoX2WYU1MTkM1GYszPzMJHHRT_6CanVWfvEClAJ__GNvLBdmCtdCKmF4acBDUx8A4ktpHzSzQEacrl9WiXE4RvMxNmX2bloCo-cu-bS0mvsm_8ClnUyHY13BdzssPYVRW2pnzd8JVO-lFjk_SXxo8VaszaTEpD1xiP92OA8-bGjpc0QlpGfy28ojqBC8pTlewCUp_WBUMr6HB5lsboXkvjU0Arqgf3waeSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=EYg3jn0Ape7JXWXxhr9_eeibCc5No5yPG7xynZDtZl0LGEY6SdHhHRp8ngVYP9DeKofft7fPf_3Eyuw_FspPIrokp1RoaZQYBkXsVZYp-fidjm8FTvtoX2WYU1MTkM1GYszPzMJHHRT_6CanVWfvEClAJ__GNvLBdmCtdCKmF4acBDUx8A4ktpHzSzQEacrl9WiXE4RvMxNmX2bloCo-cu-bS0mvsm_8ClnUyHY13BdzssPYVRW2pnzd8JVO-lFjk_SXxo8VaszaTEpD1xiP92OA8-bGjpc0QlpGfy28ojqBC8pTlewCUp_WBUMr6HB5lsboXkvjU0Arqgf3waeSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U--WAwQRlCQ3gQC626NI_Oh8_0HBz-GuRAAvxJMT8OsqB9THDqX4XP2mnhGtvgE1eF7o6WyUMeVwag-T7dwSF1-xRzf0Vo4g1mhNmuNoJkvwgfohfePcITtsWKoJp4htDKV3Tt5VQCEU5FfsktGJ7RfLnyXvuf3OtYbvVpyn0vpOsgN-gafwzmy2eXR8xOubkMXO-emX1dSU7PtzqwYG3cIiwcHubXBjTofEPS7R2hNZCXaTNuvvraNFF0QGjWSjxnaUDQnhFGpwezYjDkWS8tfg6OnMmqqVUGwq1f6-rrjOVA47DYOno1d2GBD1RDbt_mpgTcht5ajK609hOIk_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=czVFRkF6VSmMmdzpS0gjOs6v_Vxh4HNs80JR3BzpG_cycbVeHRqaXjtr19V2rOpnrs3pAyZXfeJaNTXICLPHxJlnPJpMfV9S_NVYCCPYKqRCr1ygfjLCn3hj0cb_aK2IAiMo2MsXkS_bDiDg1hEENkbL6QIWpV-aXN2k9Agv2w6OHLK5JVNTQtJjbARl7xxg3C5FEodWxUMVPTR1pB-BarLM5hVr2caoo9KbBJ8zD1Aa3-mK0BmKVqtfJJZ02uXESNIBQri2viAcQ28bjeJM2VLsy1IeqN15sHdAz000g3j8l5ik46JXpmdRPTxpS1LR_4rvjzw9NFbGBE4rZvZ2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=czVFRkF6VSmMmdzpS0gjOs6v_Vxh4HNs80JR3BzpG_cycbVeHRqaXjtr19V2rOpnrs3pAyZXfeJaNTXICLPHxJlnPJpMfV9S_NVYCCPYKqRCr1ygfjLCn3hj0cb_aK2IAiMo2MsXkS_bDiDg1hEENkbL6QIWpV-aXN2k9Agv2w6OHLK5JVNTQtJjbARl7xxg3C5FEodWxUMVPTR1pB-BarLM5hVr2caoo9KbBJ8zD1Aa3-mK0BmKVqtfJJZ02uXESNIBQri2viAcQ28bjeJM2VLsy1IeqN15sHdAz000g3j8l5ik46JXpmdRPTxpS1LR_4rvjzw9NFbGBE4rZvZ2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL4MDitR2bPWq8WWIfWszTYA1VQgxvVR5SVAD7lL6-iMHdCl1OV40zL5nz_P7ESNgQ2kwEIF9gwsAcwujFh6sPn-JPr09oB9xFiKQs7aWXLahYdrevA5Razm-rUCjK0jzj8GG1fK6DcDZz74QMa0COf--qggc6_dHo2ca5KMd_3LcM1nA7xZR5VZ_fQW4jTXydARy2R57stkL39m9N7ujug4vrUgoFi-FmI7gOkDbc4Pyi0XhNkPws-V76OxhKF4ewdQnJ_YVLdyq497zUvuspmRGSUzKPMbiUk6_TMcYMvPWT_k-zvUQml6kJwVgTL3HkglursVUKEDxZOYQoW2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=GMwJF0dXieaTaBFQtYvW7bTGYiCq5lZNmkWzUIjFl_8H_k3liCM-zl50Q8lVaaXd547d7pZt0tfyctfqYFIb_4IQ4LCRStI9SwTia4HJuAt06fNmKfnUxyb6gxpjws0SfAKpvbgEmkFvPoOXStn5WkvzTqDoQZbvBo9L1SIn3-VkRZsS1iA0bo6te8m4KTKhWr59iTOj0IF3t2_OF0_-d-APoDwDWC2lbCKU3mMkMC5mWIKFflgmJ6wWA5ctznqNjPLFgY7b7fuJ5nr2zY1ZYJrL51G30VLjYMR-RdY_5NNnUQ9Xq2DJTJQwNXppE_3BdiU-8Xb5jjFk9k5L4c5i_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=GMwJF0dXieaTaBFQtYvW7bTGYiCq5lZNmkWzUIjFl_8H_k3liCM-zl50Q8lVaaXd547d7pZt0tfyctfqYFIb_4IQ4LCRStI9SwTia4HJuAt06fNmKfnUxyb6gxpjws0SfAKpvbgEmkFvPoOXStn5WkvzTqDoQZbvBo9L1SIn3-VkRZsS1iA0bo6te8m4KTKhWr59iTOj0IF3t2_OF0_-d-APoDwDWC2lbCKU3mMkMC5mWIKFflgmJ6wWA5ctznqNjPLFgY7b7fuJ5nr2zY1ZYJrL51G30VLjYMR-RdY_5NNnUQ9Xq2DJTJQwNXppE_3BdiU-8Xb5jjFk9k5L4c5i_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of09jyHwSvjBNW6CAMz0zAE7Nw8Vk38rw-GhyhFbCx2JsQ0n-syk6AeznR6cEony23vWmGeWDpRP0XPKV4mrTcTxWRG0oXkpp83eazBbkG4h2x18I0qKHHQp0rXSoX-iRO7kOayl-oBqaMc7lIjxFTRT7K05CHg3R4a2DgypBj2TlM0DEubzrej-O2beIqmxAQ9TpE1T86djQFHDoIZbWTNqwgrloOec0w9iiSVWQnG9egeX7b-4YTYMI5eC6lV_bCCzG_q9hh5uMnSBbRgphyMh1kXi64JLrSaFfx-YqL9-xXTU5CzXqnAYSgheqqbufiWsm54MU4GXUm_lhSX0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=VNuJhO9Wyr1b_fWxI3GehcLGYCeQ6XTvgecb-slmZs2Q2-RMu7YZ6D6T4aIW_wFa-ODjEMdrNbqDnjc6f3e2ddClpxT2iYeX4PqgnopFc287ZinP4uBv6IHW9mbf6kT_Jye74Pi57l_7RDL15zda_MP-Qk01b7pEk29vS314MLeVxmFfCw6rB5XzPaOfsG2W8zjrHMUM3v6myRomoogoSw4Y09-h1mD5U2UgIPPel_VDYbBBM3g0r7LZf7KB6U23KX-_g6rMN99pCazzWiDcQLemONnwABO4LZL-scVDtS7ZqWhiWHpj7GZDQ1RBbBTIGLpJ-fj8_gx9at-7UPyCMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=VNuJhO9Wyr1b_fWxI3GehcLGYCeQ6XTvgecb-slmZs2Q2-RMu7YZ6D6T4aIW_wFa-ODjEMdrNbqDnjc6f3e2ddClpxT2iYeX4PqgnopFc287ZinP4uBv6IHW9mbf6kT_Jye74Pi57l_7RDL15zda_MP-Qk01b7pEk29vS314MLeVxmFfCw6rB5XzPaOfsG2W8zjrHMUM3v6myRomoogoSw4Y09-h1mD5U2UgIPPel_VDYbBBM3g0r7LZf7KB6U23KX-_g6rMN99pCazzWiDcQLemONnwABO4LZL-scVDtS7ZqWhiWHpj7GZDQ1RBbBTIGLpJ-fj8_gx9at-7UPyCMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=FinUi7x3eMJKPMGEEScGWKLFJn3pcV-ZjZ6HRs1IuzlpuGrczPhfThcbl22CdbZNZx5kFC3YjDJpW1VuMica4xfkCjNmJja3thYHCbgcQ9PjuJPm8MetYNGN97EQvn_PQa4fUcfQDTHUeI5v7899Yy-eO1hWYWzPyxudpNxkxBWBUH44T0yL8vOobSuJ87wrQRdldsfHTw8UX-V-Ae_2pCKesPvMAUfqx7tI8-VTa958kXGoyt7Jtf_Reg042DfPVvrijjHUtR-cFdVKRlhUyt_qThXvVMmfWMxznKAgdeoPlAw858_p5ftu0xl939taRca7YqqKFvXvLmkBknx-80Ush7R4Iasr8PoRQj8Bu0WkTawGv73LhqDfURKRsdpNAn5Mg9uTrVxcMADO7Rqbfa2FaPyMu86EaTfWySEUjFG56cC5xbAf-ddNNhmP1B6fUmH_NSyZrEwdL9GmCQ53wuY3Qn5LAv9cIgz8jgeK8UG3bkEyt_GKiN7rnO-f0AavUCWFGJ68LfVrPd36gHU5E6rI_abNK3Gecn-qQ7iHiOTEcsSKFevouQWjumFHV4xXGi3TG217dCccidK4B-bCU_M_b19SfHWmpKO57swDdtB8K8S1Y34BL1x8VIxIRPaFrXYbsl62lKWN0YECskDzalYkQuRS25u19aZHrqfio2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=FinUi7x3eMJKPMGEEScGWKLFJn3pcV-ZjZ6HRs1IuzlpuGrczPhfThcbl22CdbZNZx5kFC3YjDJpW1VuMica4xfkCjNmJja3thYHCbgcQ9PjuJPm8MetYNGN97EQvn_PQa4fUcfQDTHUeI5v7899Yy-eO1hWYWzPyxudpNxkxBWBUH44T0yL8vOobSuJ87wrQRdldsfHTw8UX-V-Ae_2pCKesPvMAUfqx7tI8-VTa958kXGoyt7Jtf_Reg042DfPVvrijjHUtR-cFdVKRlhUyt_qThXvVMmfWMxznKAgdeoPlAw858_p5ftu0xl939taRca7YqqKFvXvLmkBknx-80Ush7R4Iasr8PoRQj8Bu0WkTawGv73LhqDfURKRsdpNAn5Mg9uTrVxcMADO7Rqbfa2FaPyMu86EaTfWySEUjFG56cC5xbAf-ddNNhmP1B6fUmH_NSyZrEwdL9GmCQ53wuY3Qn5LAv9cIgz8jgeK8UG3bkEyt_GKiN7rnO-f0AavUCWFGJ68LfVrPd36gHU5E6rI_abNK3Gecn-qQ7iHiOTEcsSKFevouQWjumFHV4xXGi3TG217dCccidK4B-bCU_M_b19SfHWmpKO57swDdtB8K8S1Y34BL1x8VIxIRPaFrXYbsl62lKWN0YECskDzalYkQuRS25u19aZHrqfio2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiQAltzbkp3aS5QBrj599_UTVZhkVOlwGCHsfWwF0l88SPHvVevIpdRRbbcCctxjX1YLJi4Ki_1Gk-sLWqOqItuib94vDLP-5X9zhRgMBR4BH-C2PXbNhiuXWzaVf7r0Wr1Zf9jaJI9bOJlnnSpDyHSaGO7kZbpc4yuUcL8TtkwAzcdhXk3HslFpTiRineSyi8l_tyuRur1dNuZtLDh47bkV-sWUd_b71550jr4Av7BL_5ES3oT3lIo2IQQ2zFGYqVJCVf60KPpfwvFSdSgY4N5vEUkB2DAxSUcxEI60T_RvwONaiLKQxoN1hSYKp-4JYIqvuc_h669_cEDPsJ1OwkeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiQAltzbkp3aS5QBrj599_UTVZhkVOlwGCHsfWwF0l88SPHvVevIpdRRbbcCctxjX1YLJi4Ki_1Gk-sLWqOqItuib94vDLP-5X9zhRgMBR4BH-C2PXbNhiuXWzaVf7r0Wr1Zf9jaJI9bOJlnnSpDyHSaGO7kZbpc4yuUcL8TtkwAzcdhXk3HslFpTiRineSyi8l_tyuRur1dNuZtLDh47bkV-sWUd_b71550jr4Av7BL_5ES3oT3lIo2IQQ2zFGYqVJCVf60KPpfwvFSdSgY4N5vEUkB2DAxSUcxEI60T_RvwONaiLKQxoN1hSYKp-4JYIqvuc_h669_cEDPsJ1OwkeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMLcMHxmLh_jH0yNab1SW_09F6yq6cuCw-wj6LJc3y7QwCTRHsyu-p70zjaldfjYelXE3TOO1SJYY2hTL9onB7-XPpoK4LnGLSIU0Gnllo4BZ9bohtTIoWvD157rTC_w8mCh0-TKyZIP1Nu50z54k75EZzq1k-rNohWYDzsdYxDLBRH55Hg92MDjToYTHcXNoxEwq9XEDi0DQEBkxM9fLS4C6efKXWGpHkP_Xfr87mek_HKHj1CRthdqR0vWvw0WKqHscjg84ZZS1m076XH1grS1s8NRyBmSYr1WOCzN2wbT0t5nxSmzUPwXVtZg8kokrlIILWODqWUtX6hz7Gb4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=HrCDD6v77QwYY_QrLlAIWEBQ1ZdyU2w3Yn421ezmI3y6qWY_DvEunof0ZGNq9O-80X8R1J5Qu0b7myFYYntFvc9mdO08z4Yfh5WCoUkNeGXHWRGEAY8YCP7Bw7SirWL8whOU5YQCrBQIMC7-PjOOHolIN2Zkfn0U9QDwQjy1wX2z9AKYjX6Z29vSPbwfbgNN2MrgQ9KK4EFZIrjfJOYR-BwKiDUz7v05rMsMPjvYlFFeLeBBXe8eLCH0U0U4x2_4m05bCEwSj2G8e1H5BmQAepUcfkjnBRcQMQO9KeNkqyH1ev1Jl504EY59D1KklVUc008PWomtf6LG945H0jgxaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=HrCDD6v77QwYY_QrLlAIWEBQ1ZdyU2w3Yn421ezmI3y6qWY_DvEunof0ZGNq9O-80X8R1J5Qu0b7myFYYntFvc9mdO08z4Yfh5WCoUkNeGXHWRGEAY8YCP7Bw7SirWL8whOU5YQCrBQIMC7-PjOOHolIN2Zkfn0U9QDwQjy1wX2z9AKYjX6Z29vSPbwfbgNN2MrgQ9KK4EFZIrjfJOYR-BwKiDUz7v05rMsMPjvYlFFeLeBBXe8eLCH0U0U4x2_4m05bCEwSj2G8e1H5BmQAepUcfkjnBRcQMQO9KeNkqyH1ev1Jl504EY59D1KklVUc008PWomtf6LG945H0jgxaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=VIgVfze0989rck-72vnq8GwtKqpcfhQ9CVWRmTF4Z9W3WOPUG4fSYJk9VhsysSeWFQnKrMGFr1ldx-EgX0-Y0qBfFfXyqSHwxKkWvZ0eNjK0vPFWuBLuZUwen_HwLnVQP8qmHr6oBRAG2Gc8CVasqoEP4vfJKdg_X3sYznAoeVJBRuul8znqkkt5ymBrnKuH6dO5_sMeVKXi18hAOKDJbOBCRZ1om1VNlfEmwJUJ4xOUjSJsDgwBIfPRPovaVYvMPxfpJXWgwusDrAL5vKaDjmLqVO9gFejgudjJQ7BpSa-MB7DdfmP4RvjVNKbpk1TiIr6pC-_fMR9CaJxl0yxDoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=VIgVfze0989rck-72vnq8GwtKqpcfhQ9CVWRmTF4Z9W3WOPUG4fSYJk9VhsysSeWFQnKrMGFr1ldx-EgX0-Y0qBfFfXyqSHwxKkWvZ0eNjK0vPFWuBLuZUwen_HwLnVQP8qmHr6oBRAG2Gc8CVasqoEP4vfJKdg_X3sYznAoeVJBRuul8znqkkt5ymBrnKuH6dO5_sMeVKXi18hAOKDJbOBCRZ1om1VNlfEmwJUJ4xOUjSJsDgwBIfPRPovaVYvMPxfpJXWgwusDrAL5vKaDjmLqVO9gFejgudjJQ7BpSa-MB7DdfmP4RvjVNKbpk1TiIr6pC-_fMR9CaJxl0yxDoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=PJVkZKX1xGW_XHg7laYWM_HqFVbXZfrgIk5CSneQTNjpNuEHgDaNYTW4I5KT9_KFe2M3xvoQW1xSOmFiGVnXUsrFLRd_XiFKszIe1JMBV_bVOOJ-yfflCLfPyCsezMBMHu8hs_lrg5NK7n2uf53gtJiOqPygP_a0xbg-2THrr0g4bK3pDmkPDIUL4WAKWklTC7zg5d7YmZqAiHq3gRcMiqLv32G8xZW6uyG_Gz7wUPWzxkvsSzy7w7tvtkxdDie54O797vt7pXqbLteVScYUexOVfvZqBSNfugIK66gcAFifb3O_wEZ_AsxHJuI629TQgiPbDZ8MT2Dn45KJ_Il10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=PJVkZKX1xGW_XHg7laYWM_HqFVbXZfrgIk5CSneQTNjpNuEHgDaNYTW4I5KT9_KFe2M3xvoQW1xSOmFiGVnXUsrFLRd_XiFKszIe1JMBV_bVOOJ-yfflCLfPyCsezMBMHu8hs_lrg5NK7n2uf53gtJiOqPygP_a0xbg-2THrr0g4bK3pDmkPDIUL4WAKWklTC7zg5d7YmZqAiHq3gRcMiqLv32G8xZW6uyG_Gz7wUPWzxkvsSzy7w7tvtkxdDie54O797vt7pXqbLteVScYUexOVfvZqBSNfugIK66gcAFifb3O_wEZ_AsxHJuI629TQgiPbDZ8MT2Dn45KJ_Il10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i98I-jHfI54eMn_EaY7K6j8-vuSajC3p_mY5rBLHmvLJa6LGEysJYuhEo23RwW9jZrOf8PCKKC_YPH1FCviFdQyExiOUb6pFzFX_g42fW3rYW6ce6Pls9RFbdT7tGPmzAJ96KpQoPAk8Ah0Oxqp_pfNfGVkY0ol2gN6cZgxMYrPwFutSa7CI_sTwQIYGGhaQd3rRN7XSxthtZnBXh8DJIavZwIs3xajOXWEzMhPoKYUuGhza9OY4YQ6IUEVuhRjJuBo0MR4aB2iWme0jCDHXMxnzY2pyV894NIu8oAP9mnQQg3m8p7hEKj5rcMiJD4pE9___a0GrQiQbV8fTWqfI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtKJPGXEsxg4xHcxc1NOxUgJJaAGvDziBABVETwwr6HgCK9GWeInDuQfA19iIC-laXisriH4_ZgFnwaUCZXlrbGSCPZPXrf_597b1W6msI9eFcf3XVqu-OMwH0dpxQYIYQ6x9uiaVa2oGNeGJ4WvER-SoUa0HFqXDXhaQe-Vvx7sgo5h3sCO6NmzP4ixByb48TQKQqdzU9YCm41Gh6NT3CEgMtMakmAfr0WdtInrO7j6YlhBGT4HaFoU6zsHBW_b-0nCbsBCATk-Oaj3gxiTMaSD3y9V5IVlAy3Sn7pErzxP6H-VxsBFuHSz6KAkr4nrAGxVb47erWjeTkMZPcCwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLQ0P6d18vYDECxX8PhSm-ijp083JhuUWMQDl-zBRmSB2_eG7_jX3-pAnn3FzHxs8HfoneUgcMyCQbfi494lQmdEWIYgMNG3WbAVV199cTMswYev7TTAxgx98LyYFdKcZkeZt83J7acRHSkb_cqqwas3MS7RoQMugaQ04eVnbKKLguUfH84nFugm0rKud--2tSQDQeYvbxsA9IxukIV_x_10o5WUXcteEqOM4wpeuHUhng_unDR6ZPyhfJgE6pzoud_M5Vb1sBXTWnWkf9m-KhfbzaMjM2N9q3HhT2ST6f4cKZfzOaaPNIwQWHWcMqDbY14dfXp6sbYsE5l08KucxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwlZ_j_jUoTPMomJt5Dc9IY4TqNzmzUa00y3A85Zl4vKr_Ccf43zIp7XOhrz6J5Xe63bwMZSC-6E3FjGlJ-Bl-gBRgJ6zuPaD4jAZhnweVmSkPTph9xqZlXOh2PrNGThWZAa83XU_-jZV3YU4ZZ4d5eGJ_CX8HzJJ4Cv8nB6LQXo4lDYVbgqidj23-tm0f8vTkAk76ZVuEf46D9xs1xB5phN0Rd57h9wprovOPA2S264UbP7vJlpFo9sdF3oMD2EPH_h-c4yHPUg64SYdL_Apqg1FZgd-TXFnxX-PfNqNeOJyplRLU5fOTk7jPWP-sBZh-ujQhBvLLzEMH8zeyULCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6mPgcjP1KNURkVy0t2zBu26ez4TKMkXUM-9p_2JSNM0IWXyoLKUbxpFPepjONj6kErGua52Z9xHBnOeTsNv44606NaiYks8_boSsRUVIsvtK1Dk31IzuPdFl4SISjmjCFCly2cXZxzWXcfpRJpHWWk4qZWzbYsI7QAOpRM_CmdjSzfMnAAW7lKahJKn8V1l1POaM_4Hh_vNvoZqxEEPuPQPKtwOOzeSwl74tCt3ycrE4fcQE0hf8CrQEEV5ZwrzA_G8zg_rg3Q9Z-NaaqPv4tsI5-CLtcZVcdnDmohyyPGuDtH-MQ3Egh-oroYszTJBd-H68NfcBVR-rzu9hUSyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSycpS-GUhJiUA8b4YVUwMPliJT2f060wi_oXryt4B_MQtXzn9Ui-H57G3Gntjdc5Fo0Rq2SUU3TzaktZUjHm4zWdQrYNc049Wqb9hcKrL7CSeUyZgNS1HQY7Csbr_6diEwPcDwrmdTukC2NC2Lhm9wtj0DFd7U5Eh7fzpVfEKBhTpPSToCRVgJrQWzVX4g7IGK652C2dmyt2BEEqWXfygWsD7Xo3V21wISAVx5LdUnndxnQ1Qb3Vi9MlcQDBsN6erAiRLqyBZLBC_RugbiwK1nDBg5MFgLwVNN-Vf_bfEnGuBpjgAV39XWB5HSN1Dn3oKOMcMs5JY9AYY9CrFY4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=ACsnqZa02gr88xATB1rXNJox30b9VcWH6Y8i-GuQHj9fBzwTFGUZR_cGb-gYFD6CYKDI2x1Gd9N9j1q9exCWi8Ui2mQ1G4yqxvbwPeQAVhD8Y6u4q4l2zsbQOR4KpEq1Vn-i0x3k5YMjVOuhddSMZ4NdFQA-epj7tysTQgGpcBT6TZRPZDqQ5Pu1fJbGBHAmgqocVG-fBKVpPjBS2HxXxKvrHR_uBPf0W9jt2qwq8QOnhX5KbUzioqcgfvauSKJ5INx_IfN4l2WNIyL0uvdr13Wbsteu7_LT20J2oVBKpkHBqTLyr8okRKl529tOKHvBYQY3aiwJu2Y2-DSBs9ZhZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=ACsnqZa02gr88xATB1rXNJox30b9VcWH6Y8i-GuQHj9fBzwTFGUZR_cGb-gYFD6CYKDI2x1Gd9N9j1q9exCWi8Ui2mQ1G4yqxvbwPeQAVhD8Y6u4q4l2zsbQOR4KpEq1Vn-i0x3k5YMjVOuhddSMZ4NdFQA-epj7tysTQgGpcBT6TZRPZDqQ5Pu1fJbGBHAmgqocVG-fBKVpPjBS2HxXxKvrHR_uBPf0W9jt2qwq8QOnhX5KbUzioqcgfvauSKJ5INx_IfN4l2WNIyL0uvdr13Wbsteu7_LT20J2oVBKpkHBqTLyr8okRKl529tOKHvBYQY3aiwJu2Y2-DSBs9ZhZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjJDVuOiqqC6BjllZ7VCxAcOgNRowov3E5tbieU9v1-IuoKqaNa3nX6xuWDm764imvJvD7uvRxinyUv4AV3NBdONZZOpReYyQ_FMj_XGDcPaPUC_Z7ZVG0uyuUNfTgorUzHAAQFYKF9hsgitcyP1lm7TgX3EqO54ZoL_bislZwtvIZ45bMAJI2ECK-t9zpclP6Gpcd-8ByUCtgfEnOJcTRL9yVDmusPbIJ0sKYN1ko3ka3BaJ2v31Bx3-b3ByCnxFRrIyL0E6PHzY7EbDAeqw4UhtA24muBz8WYbtOGjcerXAE7boL_A3rSHA7W68qatFzV8sVpWWRxD63d5cMfsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB2MQ8jrUutEsiUzrDz93sOZJeyb0dKx4Qrsa8pKuEeESU1JxYL5wDGkYBr3aAgkgMXVxuiOUQrNs2axiTF_l4z3tQ5AHLOSR_Jvrluv9lWjxKnt660p8OblYlHAbdiOPCH5SF2aENgtBUPv6oolZ3KLpFjsMvaipsFUre8D0KFYkY0JFBU5wsLVKsB6U0vSuwgcLf0TWDeEci1nivQjVWYaTzmEfHfBWt_VAYsS4Z9WA1_C-QpzSn2MUywxVZrgy8marLQIy3M0BMvgJTJ2OGohJys8ZlLJLFk66tCHNUqKk_3CX-HTNma7kM_VkDJcUqAoSPjKfteHbiSo5ybX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGBtgBhyurMbXr4rBU357k-jm16cmpU-C87qc7HXXJbu_BGF3t6ZjsNWyR_L_kaDMh84c7dRxFz9scxh280B0te5GvWZ3dQ6knBOg1q19aN6gvc8OTK8H5SghXonPEjYc4IYpCH_i99CaH-QJPc7_B4k3YxAXRvhdYGDRytVTW51rn1T1H5YGR7yS7P2acrTVpfr8rckmzEv7ZwVsxkInksvtq8sRuBoNlS8skstVQFRBFNZpenoVNEXCpAmpuAKC5RzC0Iu78WIJiBXJCeS_kl6Mjy3gAYAnMU6olgAQU9bO4Q_dPXi8k9Yb6oLMlQnuQAEJ8Y-PB26S4xr4LNA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4ALf-rs51XpCivp98oN_z74RPZea9noYUmfX1e7GJhQKmwUKknoPirSLjVbVN3xj_0RV6SalyMmxjqt3bWfMJZtLzTj0a9AgfN7GOuxDBgZQ7pSTQAt4HisPTcn6o0VfIp8xaInkefTE1BvqSnCXeBOWcm6EiLO6GwtgTYCiLwyyRzM23PaBCQQ4gFPhvkryT6Jkvtn35FL3pd-KC8mz8CSh-q8cigpxtra4XuQyToU5XMDpvvDlW74SVhKWaeG4e7UXAMjli2eyfBLpJlnZigJWeh16N7KX4acUWUazlpNFZhf0VWV7ZpmUMakfGuSpSKvxaoa5LkEHNLzatCmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiOFXT9tp-Rb5ZCylwxb7v43SHcotdK-NEnQCLhDzDxW0XrS0PmblYGeUGVbM7DH6sl1wKrBzTVIXSIxqi2SRDHajEbl5fIL16E9a1Z78lmA7wbVB2R4bZCfV2D1XV2DE57-iMMoSjzeUAt2eygrs_fFKiDTLaLuyDwwr47ydO_gzN_PuVmQlXwVT2a1OQtecLUPotVVuAcZskL8xcGyio4Z4QYAcf0GduQRjvRsUOI9J2Yk_MtCU6JlCVwzg3WkaQz3UP4YDI920mhBoMQkbQCqmWnIVjWzvIRHCDV9jlti9KVsU84AOEWQM-kF1PVCfGyKsLtHuOzqVxxp5FPzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsWQBQ2PyUpxY_MBzrX-6uVCqk8MIVd58OIknjBbFh6Ylv0Ka7EM2a5u9doeNzCoQ1BHMGXxjFepkGtXSRd8kFkccWT4seaHqlwFdpi0F9CbdKfXCvQJ8kJ77acVHNqaX1-abZNdohHvelzaA9zi1msjj98s315O69XBkueiy4xwEE0uAXoBZk54wVeQlL0r7tzRI32NWxfvwVr2tHzYvcWfb-zqe2ZbuMhg351BTAtx11-10yoF1NkteCxdalFLRbbSB0C_DKCp54HIn2KhkaFJdnnMV7g8NtkpEUysQyLtchJ6B6vFmzMT3ML2okxgNhdcRQDTjo-Ixha8kNxW5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=cdfmy407Mxsxx3HTKk10Hf4JyolvMN2vkXhJp-XQAM5-t1c87k7sgZDCryNFlgR-PVNUVBFTzoxDdPCz5AuLafpPHmwm57xlkUukWb7k-kxDwFw_Xv1GBaZ0oBaPdz9TH-7ciARS9vpqvAOS7XwfsOStQRlpMXNlUVWxeKUk9ojFzW51AY3S-tUIB5CQSTEn1KP4b5ihGY946jnWlIxVCCTbEjEEz8oygspEODGA5evNOeQ1bHOpd24n31lPZ4cN2bTYSyj7hBMB04qPwqz9lyidTbLSRX4yzaj1gvmlbK9EZ1OxNDbs5iQGlpWrcdkK8-OoBNc4vQETvv4VARkwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=cdfmy407Mxsxx3HTKk10Hf4JyolvMN2vkXhJp-XQAM5-t1c87k7sgZDCryNFlgR-PVNUVBFTzoxDdPCz5AuLafpPHmwm57xlkUukWb7k-kxDwFw_Xv1GBaZ0oBaPdz9TH-7ciARS9vpqvAOS7XwfsOStQRlpMXNlUVWxeKUk9ojFzW51AY3S-tUIB5CQSTEn1KP4b5ihGY946jnWlIxVCCTbEjEEz8oygspEODGA5evNOeQ1bHOpd24n31lPZ4cN2bTYSyj7hBMB04qPwqz9lyidTbLSRX4yzaj1gvmlbK9EZ1OxNDbs5iQGlpWrcdkK8-OoBNc4vQETvv4VARkwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=sQMYADSDFg4oHdg2ZeSjMonTEkDw8HM6vi6QrbAMVF2n4rZOl3bVVZtIb3QS3ReMFM0UiI33IQgEPbrCnMUb8iF6cy6tLXHpjVa48N9QY0Cz1tYCveeZbJ_x4mEJKnOvvmyFoGVtN_S_YLayAfOEsNdDO9E_x8i5q1_xour-wwK2sZRhBXvjPq7ckwUeJnHV810Oiv79V73aAcJolxl7WX8fvBjbz04szouj1zwGWTMopf5JI3QPmldoNrYY9Qv3elE7-XRhGsDBWHh_BAogDFOQmllGDJvSTdsIgLKuBiHDMGkv6Kyg0gnuIyqwoH6tFAlEzZ1DJXLqCNYOiV335g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=sQMYADSDFg4oHdg2ZeSjMonTEkDw8HM6vi6QrbAMVF2n4rZOl3bVVZtIb3QS3ReMFM0UiI33IQgEPbrCnMUb8iF6cy6tLXHpjVa48N9QY0Cz1tYCveeZbJ_x4mEJKnOvvmyFoGVtN_S_YLayAfOEsNdDO9E_x8i5q1_xour-wwK2sZRhBXvjPq7ckwUeJnHV810Oiv79V73aAcJolxl7WX8fvBjbz04szouj1zwGWTMopf5JI3QPmldoNrYY9Qv3elE7-XRhGsDBWHh_BAogDFOQmllGDJvSTdsIgLKuBiHDMGkv6Kyg0gnuIyqwoH6tFAlEzZ1DJXLqCNYOiV335g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgLoEtfNHzhsNNaNsFGe2DfdGUgrrq0tZ3-p3YYB6xAA-xqOFaNW2Cf7UVW-deZmYPtx1oQKIkFz-iGlH7SfpSCvX3_2mEr00kSmKn-vAwY_PBeoFE1fQBnDQU8SHawZCDo_Pgl8eizyPeKKlkL-hmgsNlCpiNnSHVYcM1d6FXhWAJarWg6tW-BOpaCuNU6YUZq_5dD7pev7-pOF1zwFJJR7CcH_OM1Q290sZOZbqIx8zTH_rVHnhbuF-gy_jcFarIe8v05RYAOKvDNE-uXCX7_wm6WyE-WWpD1lLO4cqWodth6mVMpRN4hno9qH5-qvr1A5AkDQ7zMW4WxeO-8nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=TiI4eVpUVFzG8SF7YCCHzl4C0ww0l0nY4o77-QrJjYoQBRe1hMibHyU4ssnLq_VpHHgR_cB5CdC8JscjbQVg0Su9YlmS66s2G67uWJijtoSnsxfNmwI7VbmtCn4C0BaQkXb7iR_vhjPPVFSU2IhYyrhtgROoGHRIwbGo0rK_XZgTLH9roFdXtNHRgrHP0Tt9-yKxgSZNMZOKsvHWPvSdaYAJN8i_RDQu6KP-wyOYNun8qBx7E_ap42Epblj1a1824GwSakv3wMnlxNjvBf6kZnIW83z5T0Z6Ra5N5PuznVBhfROkdOyTcnUPu26bKx_MZ6CzpKYipkppqViPiBr92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=TiI4eVpUVFzG8SF7YCCHzl4C0ww0l0nY4o77-QrJjYoQBRe1hMibHyU4ssnLq_VpHHgR_cB5CdC8JscjbQVg0Su9YlmS66s2G67uWJijtoSnsxfNmwI7VbmtCn4C0BaQkXb7iR_vhjPPVFSU2IhYyrhtgROoGHRIwbGo0rK_XZgTLH9roFdXtNHRgrHP0Tt9-yKxgSZNMZOKsvHWPvSdaYAJN8i_RDQu6KP-wyOYNun8qBx7E_ap42Epblj1a1824GwSakv3wMnlxNjvBf6kZnIW83z5T0Z6Ra5N5PuznVBhfROkdOyTcnUPu26bKx_MZ6CzpKYipkppqViPiBr92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-o6_wFDEmQ0graX8F7hQ-MY5ksRHkHgvoyHPz9bicNtsRd-4YTRxqmooRS2ATXoUiKl0-NDSE5Yys2Qwp6wKHyCjsWJCb0f9MWZRySQ8MYrH2lu2yr64oFPzbBg1xD5y20VlAylUQ1iy99YX3sTHMiYwJ0slOLi3wvrhNJJTByI67zv8YaauTZ_d6DHcCtnG5bGXoWMrWI6XX_-4c7waYWdns6F6zk2Hr9nd7mPLJe28g5Ha6HaD7daEEt7pYpOOEHM-VlvAcButiUXGTcjVcnE6xJ93L4rF4uIEFS5C9n4IXGrQmWu8oGOpnAEBymd7aE6hmvtjXIEZ_Qve3F8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVgZZ3BgBBjy3sn360I3eUt_RDhFAZXBYqqP8glogW9GBSEBRsDmafPwTG9RiwMWsU-jgLHi9Qx8wAgw8w8fCsHh1ADaKsyPJQW93tbZLYwes0fETDvDcD17jnWdmuovf2LxhimZARLDgHw1zZZAc0Ih8v6LMlOIfNRS_WjpJHHyzHTjkR8T9jBWpy2kg7nsHt71vG8JPo_ZZHdnz15RHSLukPBnRvnR99YRQ0X9gKwYzUzyJNfFgYsDikp4RWqZgD9dEn0pP2k8wA6bkpxe4_jEJ5l0V0rO9IxV2tO3EpgAdWucjgno_ictSk-Y9C0LnMoXPf5os0Pr3AfyvEgWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQRsZJ-64hl2RmuC-mBUgDVjCoFVxnTJGodEZEuOj6s0lWh9QsftMm8nLbRk198dW8Yo4RqpsXXdEpsGwJkrZPaG0MatzTO2QBtI3JoLMQp6KBZZZYrR4pujUBocwbwtQFD8Te4gl9-UkL2man16ROzaMENHbCkZ16jckaSmYfMXsYt6p6mDYo3qR2cpbpHBIJJa0_UHtVhWD6ybs9fp3HyC0Ua4mKzs3-ZJcbFxuN5ycxeIXSNJw3Nnoz1wlD8CSMO6KFhlf12k8gQGHMf5ApwU-S1K_HOmGamve_leFZS6Tax0f-qWwmFbOhZCk6iwQfi2MDkExP1tFdOA9fNFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjxUlNYHwvdMhEs-SEpW6oJXsa1U-xVfJHlekp0aFpTOZBvTNE8kyxgDWNBr5rpjVu__KjBTsc9-cmt-G3jlaE3Yu7La2wTtMQfsr7Hp7KtcMs2txpkPFDhF4CG8T1FQbp9jlAthsGvHpCqzJTPBXJFq4SgEEguZvVIyC9QwatyXb_6NL9_cbcgh6f8AY1MT-WODiQZt6viGUBki85PRFVaCbJ_ha53u_gnlQ6h8epQb743mJjxfR5_34lTWNiUCxoidjsPKnJjNJWmFehcGVhRa8qCjYfr3vGcyzvc-ciahk7ckAPzol1R1ZrQehZuq1xI9rKznPskwVx97ToDQDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I31f1BPCohxt0ntVFJgeROoYhT-yupmf7bN4Y8DLOPYoOUWQhgjnmqzg6BNoeAs_gORztURL8K2fvSTfFQkg-2IZLjeLteUa8dIve8koyou18k5gZenfLN7jonwTEqve244vAZ-tyzd6XwF_HzRCIVQd7CSEQvuhuDYJYKJ0t6-pboW38LMzNNlGecKEwyZrpCGxBzGlmN6en7O1PRazi7_YmN6T7VrRcN06qiryPsZ5Opuieezwlf3XPKzuI6FpxU4e3s1yqmTekXz1PG9TZdVb8SymTuIgAuglHsN0VBg2KJb2DKTygruK72r_EJXywFw07ClSqIB1yZ7CxGJylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSELKVLCqu3Z7P_XJQCfwgoXNqh0M0mOMQKhKID0kS8dAeE6baQREJ7-dX1CZYRS867zUhic6gJYFAMTx1AVwyn5ML-a7r01LrzYEiwYhsDiiD_mzlZP6J6NpCHdn7OTShQ_yyOCUx0TXgVwLljUwGAcTIhpJ8_LU1q6zP-Rk8gagMgWRxqY6U5vNHl-MkbqXwuUdJwOtsWTaaGRQmDaRDaTC_V1Q-YiaBucFKeRoOdGf2NWy-QGyfKJ6UFuR3ZtEi5MMKIn3LApRx5EwswbpNu3oiAM2mTq3m2sNaJ6EIiCpaMhE3bCrhlOyENoAL6sN5FV6I32nEIHC6aVeoV8JLnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSELKVLCqu3Z7P_XJQCfwgoXNqh0M0mOMQKhKID0kS8dAeE6baQREJ7-dX1CZYRS867zUhic6gJYFAMTx1AVwyn5ML-a7r01LrzYEiwYhsDiiD_mzlZP6J6NpCHdn7OTShQ_yyOCUx0TXgVwLljUwGAcTIhpJ8_LU1q6zP-Rk8gagMgWRxqY6U5vNHl-MkbqXwuUdJwOtsWTaaGRQmDaRDaTC_V1Q-YiaBucFKeRoOdGf2NWy-QGyfKJ6UFuR3ZtEi5MMKIn3LApRx5EwswbpNu3oiAM2mTq3m2sNaJ6EIiCpaMhE3bCrhlOyENoAL6sN5FV6I32nEIHC6aVeoV8JLnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqVJ7VxTCGrod6HwpivNBDQ0vVFeTAkuEnfCjbk0uz9O-amkjFQAp8mQ7qZ27_5RzAnAKJlGI2gM8-jm-eqjeezOPh7bmBHof8hpkeyd4OhF3Ya6bxZ3SDDPuSW7VjaX-c3uKcR9AYnhpiVUkROXpZbxFgmkTMEub4AdFdVXJ_I7rRiTiP4t1V_zMbQ13zaoZQNYatiluyQ4t0vKI_H4ZBb6vSpqHbO8bt6rO4iBwcs4xe-exUKbVmjFniHq6Egim1niuP_UKaPrGdtWFiauZBsnhWV-2kpDKZOdD4NaQkNR7oaIXWGt1FifmludYztlM7BrVdwEuFaphDPVR0JEFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV1pl2lkiqOEyOnrHTbLAK6r7AXJcTE1sX7nW7wZfehlUjO2hvW-E0CQJhurlFVAtBmzFlH8rBQfN7TC9BsSpElYTYiBAFOb0ipenQwyx5dBdX3QFJ96q6HlxmvR2FFg7IDDdDDZzWfb-IB24PbwNvDIL3tQRu5wqho5_SRL8djwV6cUBkldUf6W2LCngGyi8xQ-v5uW15Hrt6ByKYzVf9VRwUUJYspoM5P2BKKBcdZDFaRhV86X3qtLayjsRxp_1ySrRGeCpoaTM1AtMsAn_f_qm3Hj4vCWrKBHZ7PmUqtExantPZzZ2X2RLYlxC3QIeACDtoD2UMH86DldGzAADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwZYNpFbxFFUTq_nHYR992kAJvIZYrivwIdzneJpamXbt4RFzLjkCkR-nVlPhAz-Sy6ubSZPpNiahopY8BcqK8Ve7CobdVmIMwnIdMF5zNikZs-xl0P9FULU2RQit16uZ4ls9p--QE56dCao-18gtuM7Iu4CZR-q5di6taUROCR__MMv7o5TInhHBx-6Xjkj052hEDXBY2qHgqe3u93D-lva_ZHedQtQfS2_ls8jbo_2DDprZjZquqaL5LK2nL3M50Z0OPr7EJrw3bgBghtLaCi0W0-8-dy2XJngGecKt6FduqgYaodXdYnXhzonBGIR7VCeyBdc_aTszwFn2obPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgzsSEv4uS9KKGCBHh5qUcTW4AKa1O_wC0bmotOgr35y2BztD2dvvqeQfigQENZZEq1Jvl-9GlFlAOjlbJyz5xcb8u8Df537UiF7AO8-RBmRc2rQZzI1jSdWDmTgiDgR9iHbB1IgzTIozq0UzHxiw0lyIU2mOXRXAf4LYzhVN8uJw--UZcc0McicQQnxuvShdin40kLIW5f3KCxE0bi657fAiPQ1d84A1OcpkjWS-Dj7FdT6crAwrI2d3HmdctSWVQcUUlZiidC3oT1SjkUpwaH-FTtDb74o0snYBQ82XcAcBX9FIuk8UFZtbt6cEubsaYa3Pwl3AMX8LZqYg3F76w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFNpWRe0kKJzvNIY1ksM8WTNx1_d4cf0T5_blXP9BhqaoWVeQkZyH7KctinhrxPYLiszMRKAysLTeqCcf0TDknRtBhCod2mlOmBztBpjKw691zMwtNJJjInE-4ZOa9QEgaqsqcZFka4-hOyj_HSwQHuBLBtHPbwIdFQ2fCnS4ydBdZ4safgSI1f8f6ixKjVKJDhTLBpDTHosgLIjEtKUJbDSV24qA5JkTYvqF9H_EEcpkWfhRWrnqSjY_gbYfkMt3Mzuh-2tdGOeYG7zJhcry3Yj3Qsl6bNZUkKkqjezt49VxllJ1FNok7LUNeq5LOUWc8scO9fBEUu9BYTvBuUTeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2_5PO5c1Es_dpopL1Guwl3q-fgdhsc-ZCU2YH_JajhMykwZXwrjAJOBdKi0NKYjF8926SFmQqw3rol4DDzzV_bF037_picwig5G_XWH2fOYTrvDsnOVMhQBm41iAzwmwSI4LdfBOxzrKlMF8oaLrqICm4Cr2uUzuZDRDPaLe7mY_vIdCBoYoqVDopHffb5InRZRHL0jdfIOPjihiU5jIxvLkiFBvaCfhqdg49uojDkZbxN8TPWGyvGlfQzZVhFtyAREQ7GzSNKm_hbcO2ygr97ZtQbZeA6Yld0UNG8Qa4PLp2uohV3echrDr2Zz0fBMfc-WkSEGlfT7nJsZz4zDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRwP6ZQDUb3L9b9HQLvRggdP_M0FCyPwdMvvITmltQB6VYUr2wCVaomdYeybGdWRg2o6RFIjuoVNkLmtVw1O0_33EzWv67dS53JOBmOZdH7jmpnc06ksumISnd2mKUC1qssnFg5XxnmWoDaEp49B8GzcDVvDqqVTZ9RgT85QX1ucEez0qt09TRamhtW-9Ee9YalCCPevGygvOAJO0r1nbzzf4gctoUbT8fnnG8Y7oBWvJbbLDC4lRwKqF2RdV9UZmEQJBVRn1U1TGxKqqUwyBPgGg909TB9RakSj76k2U2NGhIszWAo8E0qgkRXvmGQCvk0-rWCxR_D9cRihyz4NqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=qr0M7PIPWp3bsX2KJBvELe5V5pPPYSdJToTp_HT3MAL0RTumV7vA3PhDzmROoxT9DFBPA79x1vh5kwsFmQ31gjy8vz--DBaD3GE6iI_S88zQ3hB_NwnaMU2i3htL0wkciisQ7kjiZEmRyW9YG2oVyL2i6k5G5HvV202XRIhttzUJWMKlXOP8gXW3us49hSLeitILhjKNLhkiD4tb_28N-O0_3ZR9mRcibeUQWjKr8hRDPoSU1EZQAYlUZQRjXyK0WXPI3szncWfcysOcYhsx3c3CF41rlsMWCzeDuFBEV0DG7wcUywHUxhJTrUfEXEeN734o0lgeSn_CRepLP3GOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=qr0M7PIPWp3bsX2KJBvELe5V5pPPYSdJToTp_HT3MAL0RTumV7vA3PhDzmROoxT9DFBPA79x1vh5kwsFmQ31gjy8vz--DBaD3GE6iI_S88zQ3hB_NwnaMU2i3htL0wkciisQ7kjiZEmRyW9YG2oVyL2i6k5G5HvV202XRIhttzUJWMKlXOP8gXW3us49hSLeitILhjKNLhkiD4tb_28N-O0_3ZR9mRcibeUQWjKr8hRDPoSU1EZQAYlUZQRjXyK0WXPI3szncWfcysOcYhsx3c3CF41rlsMWCzeDuFBEV0DG7wcUywHUxhJTrUfEXEeN734o0lgeSn_CRepLP3GOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpPRG3uWZDXXj2TNEGaYtYq1kuCZZkIA73rpkl1_DZIr709Ju-rNRAqqAgUH5VKXBHywONvFud7mdFoGs6tzTai7gV35uFvUy1s-FMu7akFzhp2FfHMu991rWpIoXhsr8ieh0m3HPwxNmrZNcl1D8A9w35cDAhDoPGMrjBgOEoAH3TLBdzXZPVreKdyZdcJbfkKrND5tuFSUnWpCWSNewxrWMoCDAfKXNoGU5LrRJSUMRwS2d1Upze99z1hUFs3DpDfH5UgTpwd1xocPO6gABqPRcOfIVygRGuhKQkyxDf5HHzvSfhrdMtLPNv0MZnlQ5vy9VNu07hZnGWEvpYg0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfOt4RAHFniJQN8ePGPItiUtRmwiwbXENZxobiVlkpwODIj4wQhsoGz0IGksVQZsoljjSFVsl8Zk2eQUG7XG-9caUHFe5Lml4y-ne-5ucki7UzCihzNjE17KjCjEkoEehqvE1iWSDWPflK7N9SC0fX_Na2MFmTnnkHrXQQYZRHO53rQVysFdE1WF6z_5mMaaPaej4uHFNqjRxpiY81H5dLgFgHsFS6LNe5cxBFDBY90wyBt12TW4DTMMoCf5A1UPLRKxNaCiJBQaU5NDWAmsNtc6DsSzUji4UPib3rHTadfAdGdF1-CUix9mP7kIeQbTFlemy3Yl2VjK-VElyCJkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at99kOYm-cC6XD3NlZWa1pNLSIinciwlow5FSkB8dq5I4-grb7SUVFbPivQ0iAm5Ufre1pQP7ERokzJch7f4TmZ9iwHhOHy8IkTl4GztCfH8fHXkDZeNH5clBk37aJrTwt9wJBFWbkJCT47IyG8TB47r1bNaQ0zQ9Skup3L6Ma_ju6Lk6M1ozuChdYZeTkTfnp8_i1Tk9Qs8XthYWXc6X1Q8dfkVUGGJE0_FNLuEqCe2-ksRHyImTXkz90hVeEOuTZD0sN7nbhML-emH7QsmHChFj7fQURF9rdYPevv4p8b3lJielibTUWJxP__Hd9cID4AxdSGh712kq4X2jiwSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=i2cIaTPPW3EjadCIKAelYVVGlZwrYbB4FrrNheXovdjdT2NGNmB-oFjRCC1u9wOPcqbajAPWkvRzKw0QPmUrGTNdOOX8d7aCbfSb6cbu4tTydyJewSPfi-cZFnpTuNe2zTCIN4lEJX5P0OAxED_k2_-eckziKy-i0O8N35CmIoN2ZerfrbodAx336EigTjzHVttVdVSSWskANk7ZuEv7WB9GDlRb3QMfFAq4uL6d2dW4aFkLhPj9pIVoyfOB2ttxmTQ4-nLP0ys3JWpfe2nLVeFpf6gaXgQp2amEPYlZR_tn-DJ8HAjxzWShpuVGlpsmcEscpmIxyrS2nbIsPEmZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=i2cIaTPPW3EjadCIKAelYVVGlZwrYbB4FrrNheXovdjdT2NGNmB-oFjRCC1u9wOPcqbajAPWkvRzKw0QPmUrGTNdOOX8d7aCbfSb6cbu4tTydyJewSPfi-cZFnpTuNe2zTCIN4lEJX5P0OAxED_k2_-eckziKy-i0O8N35CmIoN2ZerfrbodAx336EigTjzHVttVdVSSWskANk7ZuEv7WB9GDlRb3QMfFAq4uL6d2dW4aFkLhPj9pIVoyfOB2ttxmTQ4-nLP0ys3JWpfe2nLVeFpf6gaXgQp2amEPYlZR_tn-DJ8HAjxzWShpuVGlpsmcEscpmIxyrS2nbIsPEmZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZAP86ZMgHHymj1rcpIjnU0xdpQ3x4d8JPIEtj6ByHwkuTUasyJppcKnvihwtOjQHuZCxkK9Xc4gUWJRSX44R5NXg4pqTt3C5D9savI2pV0vw5zDUNaKXDLQUhvyhxHO9KIuuqHmlbJMu_1aQncaBBI4XZUZUB-1nI2vkOH4S21PG7TWlBNCETCjkiRQ1VgM7tPG2wFXTdCylcmJbruccQmB60ZWJ9folh1z_Oj_DOgsZJuwdY-SAdXKm-5h514dsmCdFWiZ2_38mCdfFq8bqarwiRA5IZYHuD4r6-_J6EYApUIEIg-kIBfbvhrziEXPI05_E8qeCC4DCo7mPlXe-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=c-keS_UdIeSzsGfyIzWnJyCbDnWNKof96upAKhMkUFRbaEiPM_-ZxF4s13Zypie54K6cQ-LC4kSzY-lbgZ8Hsv_ZBSMus-Vgwfh9aJSZYUr5H9CX8XcST35nz_S4Z43HwJY7AYWeLtlqEGzV9r9T5XY2vGRZUsRIDniziHxl56LeCg8pJq9UCg8Kjc5IIjI6_T8UxjR7B6mw359hKzMjO9ZUeO0siB2-BNfuduKSwAGdX7DQMXr53YLuDDRrQhQwr8X9r35SsBlOVw_xVTIJiENfghHDcjhxsdF9uENgInVsvT22_MMXqbR8Tzg7nzqKxd-mCSDruY4GFRf0Pcg0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=c-keS_UdIeSzsGfyIzWnJyCbDnWNKof96upAKhMkUFRbaEiPM_-ZxF4s13Zypie54K6cQ-LC4kSzY-lbgZ8Hsv_ZBSMus-Vgwfh9aJSZYUr5H9CX8XcST35nz_S4Z43HwJY7AYWeLtlqEGzV9r9T5XY2vGRZUsRIDniziHxl56LeCg8pJq9UCg8Kjc5IIjI6_T8UxjR7B6mw359hKzMjO9ZUeO0siB2-BNfuduKSwAGdX7DQMXr53YLuDDRrQhQwr8X9r35SsBlOVw_xVTIJiENfghHDcjhxsdF9uENgInVsvT22_MMXqbR8Tzg7nzqKxd-mCSDruY4GFRf0Pcg0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDOIvWdBy_HPfesirqO-8ZmzR5bwS5UC9sSzaavolym0-BPgvYidueaAV-yp7uYrFLbBdBSmcz1cvS7PQsANwe_MIr0hPbwQgaWXHEAiStJDy48Z5gzKtuXEHTLg-T2-8wX826cclpeoCbuF12a9LlcWiotFlSQEp9_FWd-iaRAlb30O5xMuWYAB_kPER6H2q35kGfxhePI1qOV27oBS6SQZBye_2ASNIkZpaTHawaZPXcZxTdPm9vFSQUGn-_AoaS5G3eusdIXVueLafvYQxx58BDSPhkyeMnUb1bdUJFNgW77dtyTfiIloefhtYaI_TN3Y5JFi7i7higa6H7KsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7BCio_tqOKZ-eFHMEBJx0Li627E_FLeahv2-8RLi9fjxyazzgiS9EMmo5praqV7ID0Pikt4KNXo3V4kSjYJJg7WVqPs_vtaEngbH-4HrtFQKXeCb4lTG-EmaIuf9CImMr_IW8biibj3R82Tx6rBEexJZ8jKBfTiQlYrUT4UVQLQ9VMfKYbvv05nXXM7ioIFiNbAp-Ifv7sJHulEJ2pD-XISM04b54UsUhhNh_uWU5Or0eSeQ1ia99bHGGNybOvmV4SidN5ptB53T6pgayjDOeTjMqUa58dRnfyi9HHZwclD-nyySnzx5UA7oy_IxXcSQuDN0FuqkTbnLDtFelanDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
