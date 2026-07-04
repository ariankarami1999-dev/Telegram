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
<p>@persiana_Soccer • 👥 366K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 14:00:23</div>
<hr>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxdFMyNz1CDeKA1BM-MNw3G4vatX5PolSQyDmbLAByHmQXWg-pIgjbwof2571l-b1MDTtM7_6snbz3FOWZtnLy-835eqS69sIx8MLCAt7CISOuKPwy_XGHjQE5uu93R_ypjOg5rqlOeYRtreX0mPZWLSb86RFZkyspVXpCmW05skWdM2npcZhsPRTJriArFjwvbhe29Jsy-3zkIZWMepBcoCosgI_1oUAnhzEe-6Qpta1B9ACXdzGDFnVL-X_uvHZkfpGjD2Hw472aTIXvoHJtzUdoK3iDvTE_85ElJW3B993O3m4UAA_8Fy1Rvhmdbr3SUc_lcudza8c_wxRLUp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KtLBInV4F-JrTNqKc1KODLiOE-Yf6erWUjR-u2Fn_x61TFksSpxujX2r2eY-iQ3BIoCrqw3nJO8W8SCDhL7Uq2kcgJtvAxsw6s6Iff6nkRcCYuxRAMfGemybhNe9FjQaDqYWbbTLYxGgs7wlc5pko9kxAh3askt-3xPSh2zcRpIIG6si6EAwBxGviTmC24St9WRAkfVE7WZ7wR3JMfTNd8otJppPZ3RLx2sWrtFOlzidTxXk93PEHW8mNv-yc0wOZKZ5o4JSujxh8MZEE9viNpnqCbNkz4nL6GNndcLkQ91q4vB-olRkZ9o4jmUrH08uCa11y4OqIgVMJfpt4J7v4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbkK_1IUJkf1_veiWDw0kO7cfFYJov25sN30tPC79y2Xdot0KEvBnJGq_O4QaTgP1DEUef-Nldo2HqUKh20wbDR9aEcTBVVImknjDSTL82abrRG0mzO2OUAm31CB-lEKspo1pQug4uLrmPF3c-w83cXDtG9lM0Yq4MN1MqyUldd-9X2y7wcHWWoBtO9YiMCIInIF1QbFR5G4bl1qQO1hLTny9sbJy9B9JGi8b-hjKyiiMitoBXIQhJ2KCpq1KoMWyuSdQ-wZlyhI-D8v6hMihELnV09laP8LPZTfvX87f7jKAbyouiUxBsNHbwN38sxLG89fa5cmpiinm_mmR40Ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcMrsEwVAIcmhPGJCCyUgfItrU8Me4PzuWdKu2aKhN4mjMUK6ojJKi3En9vgDr0pemuU4AoQOOXSg3tQweu2MJzahpXvUh4BjtOmqn5WReMaDNyOaZDaUf8qe7NJcbmsBaK4UQWnQsulyV6PLpgs1bCOUi9_xUsNgeu19InUoj9yIOwQfKx5AFIMYbipvObv4xDLK2ynO1J45QSioiuUeZQ3iTGJVrwD4P1xZEd4eKnEEZOu9-sZ2stffAcEBa4tQlPBlMHISpqM19pOmLx2kyrhp2-8TeuNqcaunduPmJM-aghqq4FadnM-Ja6AVvyh12k8DDxSGT6g9Y6-QBPL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHC5-rsS28BYvXNHyrj5CfgwE1JhGcLUve2zcS5R_i9va8EfquBijFh8gCFL2azAkHSK7s7uVmt4pRtNiExRaQ5ym2cLcVHN6k41cooPqVualk6Jris_eWDBNbaPpAMrI5WFBOiykaSc_qXGHBYRDRwFUF9Pvzr0BvgCeuc6glWy6OWjiX2tTMcMDntL6pDndzgWmRcrp76FWS3O8aJi5pcDOTTVOmZQ5b_MwyXH8mANx7ePs_wK-fCfHdIMcUFW1Q1thKnBDOtad2RwlBCueKyG25-kXQE3EwbdEwMKkecEl9cDqCGuj_hSmmD7RJNcakrpbvDX3ukXImdPqXlr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSsPJA93VrcaG4xa4mmE3IeOtlvUiT6ZVWVlq1p2iikERG-ZsGe4qebdZb2P5FKHgyCF6Uxgi5IF14M9-_tmjzzGkre47hzaZuWtN7DG8gzA3e7h5o7Kv29f-jPj_gT9SLqslqPasZrnPRmk99qX8BaSbSVzirA5NdxRsvIaDQXva83-1OY9e6Mlf6NBhCDMe8P4QIodA4R5r9F2k3KCo_rL8hOXQYhggaVYW9ZyWe3aoO6UEbVwmwfpOylM7K3rI3cpn5Z1UEcQjxE1wJ6yvIhtLVJ_JQkgiJj5qTRTi-b00x7Zzsgzg0MWOB2wAtjpU0WWw33WFBE5OcbwRdfljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/but2wGEVpTys3ug7hC90Du-HvBWm3Sg3IllQBRQMq4YGn0TWMIJddoGQl1Dd_jyUUO8XuiAJ54FmIjsu0lEVbAzzO6D9M5cnay0jpEiHQSIYTw2RFVoJ9qeGdqEE7l_E-56KLVh_mIxxRcSpUB3Q8rHlZRJZdjboBEqUmOTv9Q-BSyFOrtuKpVAb-ft8s1PKBiiOvWS5IfQxsXo56E3V32xLwDDIrh9Mo7N8IkZZFAFjNJE6tJgBcNd8i4Zq7pq3AcggJA3fx1F61Xo9oY7Sr5_m4GfRnNf9iM-OfrOOniDl1E3YYZU-DKmNnjJ-5PhKzbukqMMo4BZaR-Xls0IROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tM7CrLGjOfpd19CX-8TVKFDD1GGK3gb7MbwJ35qK_uTk9D7iAaMChZnddae2eqmbsOggjoD0bXcTOxZHdRqWS_jO9nXR5uWemacT00ntWTQftF5zZYQL2N3q5HGbR4PqKxqkcsFYHEBlmrTOZtvwU3SJxaSKFBAqJSj86QUr0WneUYjTDXzPtNlhcUAGfW1istM0gIM6rGs7BEeAKYnesk4CjhLYXi9UDHNB-3a7eSzXFfIynmTdlJMeeuIUIufM1wPgR3QJUIvFTj4lmVD1SOPaS_ZvNz4s196YSL-UKNkGKQzuB-wmAFXqM64Cz4EovoiKzVH4bFwjPWMBMvsITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STt2HdsJaZBdenhhPRLfcQKnP1ieiNQ-ROtwxg8JTXBlaxrJNHzheOaX3tx5YgsPwk2YXhQivsJNd4hA0zlPhogweYwUsLA-dC7zt2kx_SD6i9IT5lS5bNB-IGJ5iO1xhtXelNAbw7SevHUFpAWuUJ3z2HCOl77iaZrlAWBtKQ1xUrwvj-7pZOkrgGGrPNaLTGxl4ABRCIhs6Pktq7r_VBq8UMdVmXwCFM7nRSKyn5JbYalYsJLBoiZFEwSOAGnWR5R8hWZ1WkvKP6iQWtPOEy-_nTy6wazcCQW-lkxsdmXu3v2TCsSnSI3aWIkZT4WTTbmzrF27cXNpQeYvCOACeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWBRyahzwuLZ5PhJcikjtkfXs0lmicLLgz5-DsCxeo3iw-kRpkM3O_dQYTpxdGtuZJYKaTFNY1yjeTliBhpt13Kj1y8Mx31L8Z_GGv4oqhoYH1z2QjRPdzwcTOQ2px3MrvGqDyFnCu8rJ5qs81bnm5ot2yCs5dMDx0VSJ_feXj2ykIt1jFw44QoE-Lija1lB5VJxVmKCjJ5w-p6qPoXdPhDpVdZUkF2lR-qP6aIGV48FPS8ZePOy00yFpYybtoo2rBndCEGvCS-uoz4aWBRKGvALRVaUgD_BZ_OI37DZBdmPpn2D8QX5tQX1L2jCunfihD_Qr8YH21BtvIyNs-CYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RITVlhu0cuuiRVMTwrB581tu6bsdOIM4wQXp2q3nusAg9qQT6t1PKKZfoJ3beuyuCnwCd4G-_1Xg1oYyfzssW-aqMkApw972lkYHn8Axsq6v3xSPK8yUxMqbXNW-MH0QbiE7Mv-Co7IB8IqjjU3mIKA2iCUixgj9BseUmF7iV_-XSpYTC3-dFXFCRvMomWc_Ze0-5oa3BcyAxUo3649zwM9u2cDvwPXja-aDlkGwQAhUqPy522pxbPIU52StWXQxyXoO5T1hk9-4NU4aXYSHhGJ5WKbaWEp1pFa3VooZBNvfkrzPjl7I8iCBkDhFEIQNP8gXZeFkuXkM-1Tm-pYtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3NZRm5eyRslINHkopFek0rx9W8nRLzJN7S79rtiMHOSP_S_UgsmNV73AAqr1rc8_bcCK8FvUPoJhGz5Chp9CqxLS3Cfi31JUMS4MJFwYPl0_38pwbrGoMK4n6eJWOfplx72C7n98E6cPUnbC-_D0PRujDNV9eNv0C8dd2it13Kb8gJJQa9GrXX62X_zkr5wwWf0-BnE5rPk6JSUXI7wSRtqNdYBcViUsxw60ztScLU28zCpIfT_0UQEgXESmx53R5RMj7fd1nzkmkKYVVl79ELdXxYDLjud_DW2pTrH-mOHtCimX0SqQWT_GaNNQ-MAWrKEt4AShLw-bektTIfptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9IcGTPkLsrQfHu-FcXc8EJVeVDnRvzLvYRk73cw_oKistLNV_WgE8F0dEZg5NBOXX5VdLYAONARIL9fax_pPZp24XFSWLhsbSPeNwXwI-slhmbz_kdTsDf10ymkAjhMujW8uGrIwvMpYNKK3k6Z2qCmV7BYl0D0bEu5r8T4J4yN9OabScir7kcuL2DghqiECdTH2M64CmT6sFzxZMWJw7GyxLczsE3cLER3eIVGWsbdvHyLD57P4dZ64rdG_MTicb4OxDmkpYZA9K19v4xDwHIN4LbjEwFr6MIkqbndtniJYVODMoW3KZagxZStJFg-HE9Swlww6-VU5EBW7NnBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLjllfsmuXfbcibNoi--GsrxTxLNpP9ioirNhlt_JV8JpBBvbHQr4WGbVzIEH9KhbOv_tOchEIblV9CNGqWI3KTvj_F_yLUHf1pg5sFGD0zpJSLBSwLx6UfVV4GhukRN1UPaxDiFjEbucj_-Z5n8GfpcG-1M9mSwWUw7ldEVS6P4e-jQMeqZEYWURN-tFxpd4TnvvzJJCaqJVYtK8Xg86c4WPWYE_Jyi8DG--t8XkA105Cxp1PrNEyQSl_WbM_jbj1uy5nxzveMFmoFkhPdPzk_7yXWWlewxZYUcdUC_ctLtr0-mTTwkeZtXNFPKXBKNf6TCxlsRXEGzhYaeY-e4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj-qI4HKsGGxE-fA7yIEyrYqSpOCGWzMI7zYsrjJLFME_FPWRaVRepQrr6EBAptnAlCW9587T1_uTkAdsGItUOTQd7tS-o1zmQThOKVDbSCsBWAGTHmijX66Sh3wA-MH5fje_KAM7q36n-E6ASRR6jkj8zDViEZACOto2JZ0nivWVFmthPdUSfD3TVTVE8z_ErLf72pK8s2fgqH8GPTSyEZ35Ro_5FINHkC0JwQnoykl1RD0RoQElucZoHgo7xyLiWf2FbaQjoBE24WU1yICZN1tWfhCFsl9gyfYgxbARoMkwLRtzuVGXmPII0d1pUgmnOm6Jcl3r7t9MQv6pKrDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT5mubd8P7zF3mqZZZoRIKSxzoguTDfb3Y-dSxt9pmgAIzk3Xb7hRxSfuO7ZzHoEHaVkYYtJtQXc-gNwrhRLserWU1b5QR3nu8MzYJHvDKrIK3s3tviyWgTgLfCZ9FL5F3mPZLjiDGjz5HCPVxJ8IEyCWTGdtNPZGG272sidl7DMbKjyVepZOUZGLK2NRTdxgKwSeIIcwgARU9GIohh3U8QARkzScvUvRunQhgi9kat3FjGGWftS4CkgzEsqC3aAyBDv0pz-2vjg9x4KHzH1C3lRqa0FOcGG_inKn70GByx-4ddaUX9TLLEfqyZnNeGW4josBVGO_KqxrAhBsHEpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmiVKSZd_Kf-a-DDbWxCXSMVeQYDxq_rsdTWR0TQPcK8Q8zTaOndnQ_YGg4W6VwlZASP5QmaEV3z183OinExzdBRsSYNh_sFjVTlbXVhU78w9pvs5p8u8YC72BRmsZix2QQwQfjnEZB7UYCn_AngxBSYPB7VLazTmH7Hv9NMowik_ZXKOY7BS-fCtVhIIzaFUZCpDrMExjJHU-xb7mNgtu29CQLwlJFlWGgnpolSUHdm_snSWejhAIGs7W_nE8OdWUf3PPtd5vZId7JWkXsLeq-i-Ng81YiEHeV0iqkUVc9ac-TsVrM3ZXsWmFzxAfPsvDxpcf85hTYkjGNfED2gRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXlMCQMZ3SS9P2bKTPwajWgxciKFgs1deA2POZVCvvNykoXQ1K2EoPINuhTDzJLKE_MBiZOPVrucAMom0x2onMp4VKcqUu9GNG51AR4RLjy3E57oEPc2yFoCAiMxBjrLqt94IVdLs6pAmO32gW7ZSVSBdFA_GZ7hxNOP3KZAUi7ew0gUI_8w7oUp5NSql689KPLEXlRnrljUlVYUuR2t-mFLy4Am6PNzzPMxXEAKW9m_sFUadDKFdlpbXzhkoaXTI40Z7LcUAB1xyN3CUotYTWrA_PnolaDs_J4SzccLfxSsiMIIFE8btJHf07vs9yKBqaHkKG7q7iF6jSAtV6zl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBDsDFkUv-MEcmMZ_VzTas6SosvvyuxtIxp32VP0QIv-biCsq0pWXR9RW9RJWC5BP2WVFT7feLVB1CZwFTLaTvZX-XHdTkRMzegSSDiHLN09k4GO2ORt0G1c-yjEJk3clyyp5fzWo76qPrqGbpQxNodY42ZcL5QD4kYIQIBQkhPaJcQ-E9drSoYjj9A1_vIFW4i5OkJ3-T9wptZgR46srbya8i2PNpb-LL8KnpydY-N4fAV1yCsxZ0AibI35dvVoq1NZOYWGd7dv4Gz9i8XCmrmsk8fvGgoqvyJx_uWjEn43zYMFKoZzrRlruQQpSL8KV9E0HbFdlkoHJ-2GjwlWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ3m8EBCRxGPCPS_OV_Li5DZ96jrXENx9fSZIb7v1VrAk0DOxzoywRJWlmdHJe-NQVIYxqckDEHiriO4ImB1OzsngDclGuFJFVJg8Fkb7Jy34QTWXQMEAL2pwxxM-GohBMs115tOv8DWc1pSKkQk7dBgpsX3coeLwnfTuFdLzLnWg-RMEAaUX4QRnKPcc9JpsR1IXJxyMxsBc73WoAghu0bFXqGug2hv8KJ3CPJh_t8bxgVAPiWoaSbctFrSIQiW8jkZoSvAAwPhm2nd_K_oKYoJiS-AovFnm_pebempJP1Dnu8F2JJad6keNzk0ohIwBYNTSaUaF0cxQFieI18CyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUV4QWK8-GdRfRu2dzDVKXBX-4CpINwBBjWrgKFtVRbPTNTTJcdGmnLSjEgHa7WZhPOablTiey36HQB6Ns8rE9SS0LJtRFLHHMDyiKHHj_mHQJ9kYTg7DRSOj8Wr7n20HakWe5j_5YWUXhZDGqkZkdlWFCa4vmUxizbQPni3umksLzeKNn1hMSUG1RQZcyO_GBK9raXELbA5G4GQg0xSNlF7n2JpPtnN-Uv3pg30tZ7FcM3YabPaM-U4saFjeg9v5FNRQg3cHk51BBgmQQNC-LrLgU6Jo2dWRNuuE_fx0FxcZVfDfWeO8VLVNmoIxif8TSZD6rFqApjzfeHYD7BQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Hgf9fxLNhq0gF66M1clv5oN4ygh3PnPUj6fIHVRxr99ZHsi-O9XUmz6bkArDGVBaq6OlwP7_Brfqxo0_lSdPfFuXrwr5pgyuNSsAlKGZBKUud2DY176sM9xsxDWbEscG6JdlUywSePsuQWcscYyWp2XSJPb8Uae6a6-oTtPoC9Nn_8-WQvp_YI15uoReywQX3kVgbUYf09imd_YTQ_ieT4rE_ij1eLku2MH6z5bZ2dv-aCBkQnDMFIGoP__JMIOQN2hBkuo4Jl9iSz7pUOAvxwhjSjgBMh1mFNea-tMmkGmvrGfff-uMwosV_NeF5F3fv7JBcpErn2lB7nUomyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XbEm1EMMQ08_opBMmiIEI-u27AnO88GTp6F7VhN7XAWF2ttqPa41KYomLUWDQEAs4XkVGDWp3HXVMwCLyAREdTDpSGevGlTMn7UrQHGG8AXhWP3Zal0HI6GhQBxfMVxz1VdyE9KftYMRvxeWC0pK47F7O3-kvtexiLnhyz6HAdsq3BvoIuULNcqF4h5_0Lq43XTnCzWcdycIRtDUuEz7HUMjEib9DgP7GBupTI4vHXB86vuxs9zN-jmP_pn3osUxYnct482NimCyqVxhK4_ZhnieKTvk_sGNx3vAKqVePnaujzmBdWpmP6n4SwkkfOOdUleps2P2GR_WSOCtPdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHRC_mxpjUNERLOiUZRK05AaYdF12xaJ9OJv16XD_zowJYw2gaAqL9h-yQGGy8u9l-Cb27pj2hpyFaC390uxz4uzqYX5PixDmAivm6VGO0NqRmSWELtkGNg96Ampf2GLZ6eOk23ulhfVtsPvwbj_CW1IfXaEAkEoVyd6QIqmwcgEHrbR6y9s2tZCAOL4eQez6MwJ4uqyxN8ja1JDWa0M9kEjf8tNl7OsAEL7WMAhOjsc3es1R6E0bCv8Xg5RZYAYairhBcSYj95iDjlm4NmFuNcui1NjFGDj1jP7gSb2TYgsmsOfh24D-yhFwabvzOT5FD3L9dQg9hqF51xEueolkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF0HAadMuXlnEQGt1-qQLh40UDr0GPOwiti44sYeEzQj7UfPh17ASGWw0sNUExJO85k1aUpXpnScI7ZdaZhutPYIjHIPhKjaCOjCLBtMGQMVwH9mVzEM2mi1qo2GdFNOgNOosO6_DOqIUExGGp07Zkmwrr87Yqi_2tl7gnOtMZet-RM6lC3XoPVPmO0d8e8BlxsexxXIc9jm4uj2hzSFaHxYqyZIawTwMQT1wt5LwF3jXtNcbIr2qlAn9jqcQeoMaqEPaQwTpA7-bW3sOCpuXWV2THURjwh0p7urXFDRICUpzekhVFsrVfsr0yZO8cNyXnuJby1g4gWW4qOBwUCRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsUElJ4kEmDTovOTQvhYxD41_rLQNv1wiGk_FKfWn59-urN8mi6mnHK7VnzkUHuu66hcbDvJMTpv13B-xOasbTzk19LrbQJ7KSGIIi7QnOxhqAhOL2EyiK0BIiCTj5jiqKQUPyUFdA69zdpwDEx9rNTUtCxs_EoIqarFlRFN0jweEmgSv9yflR8u4eW5DWmmdcIC1qU2BhfmPKoBjvIMBSU0VPlFMLojoWPhRqx14yFv4Azo7nJHxeneCY3cP4jIrAOWgEXwGEwT1mH4_nLgsAgu_J6cXtN45u5-rPXkrxxQerXBQUzOVKdBMeYcKKWXpmbFUeomPph18hJ9watvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO_8rJU3qwUeqycduwFJI1-4oF03sB1krJqGnDakoKHjIYf9OTNPAbaRbedzoo1YkUTls9Sy1SfWyqNhGXbAUEgkI3Mb_Cmblz73Nwnyd1CHgCB5l5Ov1kYI9boOOgA2BoXEs0fM6DdOWeOpc5twGJAfIrKdSgdlDY50Ey5MJkKHlSevXUvWRrmsP-wEdaaD0vQoY5ZyJdmY9_LYS5UWEMItH0y-VFmfj20CYfe2PaxwL8UDdfEzSqXGxOpRoeHFmEojU6dOAXDr99Ayby0Je80kxG3BBbsoeJ_hdaGATLQYqz5Gz_W_GwDNCnj2geWviE3A2D_lDhnOVpPaHyQ8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r48c7rKX2P0D9KML4NLF4PeBd8Ykvxqkompp17-A5s9kmR2N4NM36RXFpaziQI4VU8AdCDaoG9tZT5gptKbpfZ3gETet51Vl8oY2F-VAQr07RYNT-av97h7t88q-1Xop2vLEbpoBQSrJnAgXMtXqHdI2aYtPcneaxd0-8LQ7V75vSBkABVQW7je-A__e_0HWlzn4fDlrjRBAToJH3koUx2JIIrCwj9fWqT2mc0z3PniJAmyYRGhMazc0mO29sRg9HLMID8Mz_csAMRNRUCQPrue4tUthc9X6PdIwU5FpWQ9lrtObKNRPgB5-y4z67Nh8-VbtgrBd9908UZuvbzQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knnXXb7ru_Hfd3xD5wgzv773G5_DeNtWeiPOe4GTmp-HvfXDwxaLz02VJydWZFoEUHgJTn6ARA0PkP1h33ywdXYuGgkUKmM_nhuVpDz0R061M45w17I4kK82mkXfjYX1dOQHfW31oKykjkt4iUIviSg8k1CcfxS8VmhO4-fkCAdqoBGRHv6EYQy5tDAa5h21XTVqf2Zpd8ReV4ExDFQcnHtp5Nl57oxq6TTqAavM8rz2DCLOi3NRn5i0CthJD-jt2p63CtP6CSM6seg-DjjkoYZO1M-EyRWVr9TCpCEIccQuEie_96GnfpkLSLaSSG0IcJ1-vcpakQ5dm22vKjtLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U--WAwQRlCQ3gQC626NI_Oh8_0HBz-GuRAAvxJMT8OsqB9THDqX4XP2mnhGtvgE1eF7o6WyUMeVwag-T7dwSF1-xRzf0Vo4g1mhNmuNoJkvwgfohfePcITtsWKoJp4htDKV3Tt5VQCEU5FfsktGJ7RfLnyXvuf3OtYbvVpyn0vpOsgN-gafwzmy2eXR8xOubkMXO-emX1dSU7PtzqwYG3cIiwcHubXBjTofEPS7R2hNZCXaTNuvvraNFF0QGjWSjxnaUDQnhFGpwezYjDkWS8tfg6OnMmqqVUGwq1f6-rrjOVA47DYOno1d2GBD1RDbt_mpgTcht5ajK609hOIk_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL4MDitR2bPWq8WWIfWszTYA1VQgxvVR5SVAD7lL6-iMHdCl1OV40zL5nz_P7ESNgQ2kwEIF9gwsAcwujFh6sPn-JPr09oB9xFiKQs7aWXLahYdrevA5Razm-rUCjK0jzj8GG1fK6DcDZz74QMa0COf--qggc6_dHo2ca5KMd_3LcM1nA7xZR5VZ_fQW4jTXydARy2R57stkL39m9N7ujug4vrUgoFi-FmI7gOkDbc4Pyi0XhNkPws-V76OxhKF4ewdQnJ_YVLdyq497zUvuspmRGSUzKPMbiUk6_TMcYMvPWT_k-zvUQml6kJwVgTL3HkglursVUKEDxZOYQoW2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of09jyHwSvjBNW6CAMz0zAE7Nw8Vk38rw-GhyhFbCx2JsQ0n-syk6AeznR6cEony23vWmGeWDpRP0XPKV4mrTcTxWRG0oXkpp83eazBbkG4h2x18I0qKHHQp0rXSoX-iRO7kOayl-oBqaMc7lIjxFTRT7K05CHg3R4a2DgypBj2TlM0DEubzrej-O2beIqmxAQ9TpE1T86djQFHDoIZbWTNqwgrloOec0w9iiSVWQnG9egeX7b-4YTYMI5eC6lV_bCCzG_q9hh5uMnSBbRgphyMh1kXi64JLrSaFfx-YqL9-xXTU5CzXqnAYSgheqqbufiWsm54MU4GXUm_lhSX0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz6CXeYEv_jzs_NUvesxiMphyhTxBODUnqiCDNKWimRF8XccnTqHh_zK76IG4DwqEioN1Wi41BUgeZEJ2jGpW2hYDVhTXrdsq-3vwWqRnZVOwQNclpJuZkOfGAOXMLxDSV0HabFnNCRcnssuYvv4T_zpn-LzIHZ6HUg3uKxBgWTPnCl8dIvWh0NN18qAZ7DMdVHmAGeKhzDho9RX3AHUtv_kSpys7IsolqO4VT9DchvGfPoHuhdxq8LBoCMdhza3ZxInoa1Vf0raM-_HQnEZF4E-TwGVPfexWB5OQH0vdaiVWj3X2t9E4XK0OBiuEEG1Aw616YbMoof3z6vwMG2VvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=SbscPT1ySG4LSdJBIqPGCG9BIQyZI4vAUK3He8dOqlmd6mJnhUkz2tAUbG_MhJtxDaeXlopFB-yN4nZv2Iq53eBcHifs_AMWcIVTRVfdM4ynS0PKbj7X4t0GTKp2UZf0EFf661zCSSKZHs4UwL-8lpOxwM1jAQqL9L73ZA5OGzdSiiBBYy0fjPMr2PXrXpGk39PIf0LDBHad-uG6va12r268wAUHU21cdQ5BMIMWTgWyBBTuPI-0GdYElE5IlF069ZxfU4OlYbvGG6F1KKW1FkjZRm2ylrAIu4-QHUz75T60rs-fIUR9p9B0du80cfKKE-EXB8bhHxx7kw_WDmDN1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=SbscPT1ySG4LSdJBIqPGCG9BIQyZI4vAUK3He8dOqlmd6mJnhUkz2tAUbG_MhJtxDaeXlopFB-yN4nZv2Iq53eBcHifs_AMWcIVTRVfdM4ynS0PKbj7X4t0GTKp2UZf0EFf661zCSSKZHs4UwL-8lpOxwM1jAQqL9L73ZA5OGzdSiiBBYy0fjPMr2PXrXpGk39PIf0LDBHad-uG6va12r268wAUHU21cdQ5BMIMWTgWyBBTuPI-0GdYElE5IlF069ZxfU4OlYbvGG6F1KKW1FkjZRm2ylrAIu4-QHUz75T60rs-fIUR9p9B0du80cfKKE-EXB8bhHxx7kw_WDmDN1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=FDXfjo44g8CIPqxegjhXP1M1V3EyoLwU-FODK7enWiHJNJmCCEQUkCRgZ8uPjaKU2jt15hpT7cAafxgPFO-BJ0y0GCzZh9TAHGi-d3YIOVT1jkWqWZjtKLkwGZW7R9Un52fDltXi5ou65EHXNV-AjajVmrGimvj3LHX_0jWXzthkpmXRVDnZIlDJl6B0ltMaL8AkM01cryjHNKCIlL_i_01qTfebs3RZE3D5o7QiHvQMdjY4OYAwZ1GQeBXsU1Im9XsE6RbluGVS37J5gh8SOkCxqG11dQXEyYd2NjPAW3Wt0ZaShGhjqxKkoj8dqsSxvPT9LGbXWX-j1LvFRdXeqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=FDXfjo44g8CIPqxegjhXP1M1V3EyoLwU-FODK7enWiHJNJmCCEQUkCRgZ8uPjaKU2jt15hpT7cAafxgPFO-BJ0y0GCzZh9TAHGi-d3YIOVT1jkWqWZjtKLkwGZW7R9Un52fDltXi5ou65EHXNV-AjajVmrGimvj3LHX_0jWXzthkpmXRVDnZIlDJl6B0ltMaL8AkM01cryjHNKCIlL_i_01qTfebs3RZE3D5o7QiHvQMdjY4OYAwZ1GQeBXsU1Im9XsE6RbluGVS37J5gh8SOkCxqG11dQXEyYd2NjPAW3Wt0ZaShGhjqxKkoj8dqsSxvPT9LGbXWX-j1LvFRdXeqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=TXCu628-KE9rlfkKxNkih_XGiIix0IKBUWleP6G5-KxqgYDj951JR4saKhmLnz1i8LjTgZkTQmjkO0IbVeLVcAspoL-V2nxALv7VL0rj4MAcfyO0VVHY5619E-9bY01Sbe1akVJwZHkxDjat3uncP2dNRhDGBzczKyeo94dvmPrQgXSCM2La1eKYtXAKNdt56gLjl60zPI_7kDvhAvb05E0sbmNGeg5C8C-HUjzzcsHYVWV1wzPwQvRL7b5BgqbGcTQ5B26Lyp5wQSgk2qOwvRJ-9XpAtURKBvWrjN3N7BqPQf2ut01mavf4vdVQ4dg4F6DqvAYktQ5y-MtofA2gkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=TXCu628-KE9rlfkKxNkih_XGiIix0IKBUWleP6G5-KxqgYDj951JR4saKhmLnz1i8LjTgZkTQmjkO0IbVeLVcAspoL-V2nxALv7VL0rj4MAcfyO0VVHY5619E-9bY01Sbe1akVJwZHkxDjat3uncP2dNRhDGBzczKyeo94dvmPrQgXSCM2La1eKYtXAKNdt56gLjl60zPI_7kDvhAvb05E0sbmNGeg5C8C-HUjzzcsHYVWV1wzPwQvRL7b5BgqbGcTQ5B26Lyp5wQSgk2qOwvRJ-9XpAtURKBvWrjN3N7BqPQf2ut01mavf4vdVQ4dg4F6DqvAYktQ5y-MtofA2gkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYX64bKFjmqWP7RA4teUW5yCawY1IOORTcryv9rYWq-Git-iJFOz9AaKXMgm8VsWNVmvNZ7xZWQpv_cFWdmJK733Fx3Om0JS91YAwUVtFyPfj8UEXXz5Gvl8_lL2coV4adeDL8p5_q22B7eumyi25epGG-gu-j79Mh7lhYytb30SlCEfizCbIhbtjXkV4ji8lMhxesPFurvj3yoOWgDLp3CSHNn6iBmyXpjb_bcdVGM9Y5nihvYEc0O6fzQc5FYPsg07JRWGCmVeg4quMQbQO4uRjrbrJ3qzQTJNloqv7aKIw-JNMMqsohETFacMy05v5HeZcVqkgV3SRZBXL_Nhow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIK1JhCEPImW7B73WJdRu1JXRlz4MWX93aNT00VAiIGLvYDLbBCNMq81RD9lK5e3V2ImNiLcb2N3gtGpN1gq2GG0k2OLwDJfLhUCSUOrBItpKWTQO8H5QH4fG0YEnP-KrK7sujH2OPgZ_5NhjudBa6gwDFAQeAoBSpNJmo0-m99sOGpe3dqwd-z9Svxq216aGliUCI1j5_XR-2xsEwIKWJbYfaIVrDYR3DGmKzHt4d2SKeUb-7RcSp2-6Bsrw9hywQVQVTUPbWd32N_v76dd9v_MbKT9BSkINgPEByrj-PiEIjhjG5DQ6EWrZ6G0hBSlmjTFvQIBIotn5lkS8h3_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwf7IlNKWykXeX7ZLMj3wx38I9lSvkxjml5YdBLK23_zQIdJWvqW5kz9gjul47TVpKgqYqVmqV4u2nkBhepoCuB4sREk20KyRJ4VDGO-QSPl9qYy1knWB7NAcyvXFFoWG2jGygEYGnfJBuJ-ixRP7gKarAPcCUQxUk9nP17v-XgQg4CJ9M5m5joXdSbQAunw1tj2qpVFcUUFP0Y5mFwt4QX7OjOiZq2Nr6mEPCNy9qyao2YkcUziVqCaj8rV1tCqM22gBQSSJ9ioL5DgecPd8RPLXTCgMzpgP1aiK-fVy7prwAi_CZFTgNQ5HnWBEPfl0laJe0dNZzSzXnqVaY61TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpde3n8d471K8ELwnUQKgsCznR8AKgtQpQQIBBo7zdQLTpKfsZFAjXt7tu-NRDKr_Q8xmVMUphtSIf9rz1ehk0TrXPmu9i4-Gtk5NC-731i1KlssZMvFHHZf8NIni5Bqkc7VE8wyeODW4Q5qhXVcyZv3ZjjAns1dolkmmUpqw4hXxbuKp9DUyD-F0fFz6RGQ8rNulxXIyRFq8kVo7VX6ecAGRYDqSEAo-QpMfXei5mDgN5Mt154liyzEILJrdlO2V9vAuz1EtrXkU6WVXMnc3-WvcM-2J9CZ3SaNqpWNiWZRJfaiSpBnyuR-gXUwCrJ3XvH_G2LS0kMryEKBl92nIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pduZV3BJO2FxpEh7rF0sy_xccY7KezP2Bsc5T4Gdb6YBv64ToZvrdO13EQsLLg_gpZShcsnNq7kxsY6YejBekI2iBvwlafyPagKfQPr9lLSMJQ8Haye23zYKYYWL5XraFXRLYAtUI00A-Z0vGapG0NWaem6saGs0giN94yRWP47gDeCJAcTdLfb4Qzq5GVv9YhdChvNs4xfR0UcvcC73_9rPTWHLmwMd2OUICT2-4oNIlGNZVEZQP8Fuh_xs6fLu7IFS9dDI17SNfXQgJC-ZJaAyFTZnjdPVanBxAdX7UrZ337ZoZ32tzLJ5cDzSLMCUoDQpUBJygXC7UrOdOsGJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yri8pyGHDfvpf7Tn1guHOqdTAp20bxg3HpBIUKFDLErr4Cp4cfo_nIX7RhbbKg30aT4BwIjED8bx3GqcLj17GsjiXHWhA14P0RF6TRuPWMXmfXcABnZjVh0_YbbV1D3CG0ui6evLJNXP7cflytrot-Ob7tJ4jYJSXwK1c3owrj3rO0b87et0Pk1WBxkrbCqvrBYAWj1NjKi1cS8HnxUKSUOKrGSRnDxHlKSXFBtMGEJTuVkO-xlGe7g010Jqxb-N9hXHv_fP2CU0Ud97SUvtabtG7mO9NJxkhbRuSNZa7oWL3KFuD3PtVBfuKx2lbDJ1IoIUA3AubZL9L1keLl_tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=NgY3KagQNAcZPZpz8P1qaWL031Bbfyd4RxHmqgPg9BApuAyMOSXdG2RMNMrG6un34YX1TN-51Mz1TMdQg8ifFUXSZWkvT7FZOWJ1lX1svT1JpgEqGEZnZIbinaf7VHZLDYmoOkI5JLYfoc9k2UAAJ5l_YL-ZfhmVai4Kg_69pya-MZprElpKwXPRYxhCxjkxY_3sO1OZauNGqzVwN6xnOEVn51VJvtZ6EXC7pTKAZvCUXMUMHBZCZD3A85CGTQazILrdb_j6aLYDohf6vr_ThJCj8xUSaVZ8IoQMba3oLRFZIec1DX4pr4I4yldXQuZCfv4k7LpR7N4sbJWQH3zsbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=NgY3KagQNAcZPZpz8P1qaWL031Bbfyd4RxHmqgPg9BApuAyMOSXdG2RMNMrG6un34YX1TN-51Mz1TMdQg8ifFUXSZWkvT7FZOWJ1lX1svT1JpgEqGEZnZIbinaf7VHZLDYmoOkI5JLYfoc9k2UAAJ5l_YL-ZfhmVai4Kg_69pya-MZprElpKwXPRYxhCxjkxY_3sO1OZauNGqzVwN6xnOEVn51VJvtZ6EXC7pTKAZvCUXMUMHBZCZD3A85CGTQazILrdb_j6aLYDohf6vr_ThJCj8xUSaVZ8IoQMba3oLRFZIec1DX4pr4I4yldXQuZCfv4k7LpR7N4sbJWQH3zsbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE_Fob7JMU7ax7UrBJCZt3Gt8tkHwuqQGVWkIZDm9Uzq_L0Dplp7zJ_Uxvv0T56CdQ6Nxzcdjt9P0CZBa9iM1dZa8kBscAMfeyYuObzgSOT6WSFE1TRHsUxQip__9F6SVUNaYS7wnDdKTYegws4yxKDtWAqevIl5cgE28urwINf2myv9iaKSdwldXWQS8Mi7h_Mg6H7t42t4C3NEVHK3sHa23C0712RNV7cODEOhJDDMLEvyIXkpy5m_nsXG5gYh9n_ia2P_limxNlIuoq3pi0nnqr_eT9TJDYODgm2P1mDhcK8bbXwW0h7vHasqifSzU0EU3ODEPshiJuH4LG20vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaNQF-D7fymRtq0se_XJitPSaVBrazBc4QmYFB6mWBbR1AIe27c4g42T0T7VyyGAm1Da7BG2Q3GzM8-J4-xmUHI8nVlVqjuO_bbqZcLc02L8hUnJBlrX-ZnGkyjS7hO94yJFYCuY66t_KEpa1XNA5QqbNeCzGfLHSnornIP2i_8hqhwtRk8p0Kbq8TFpOQ1YdoTmWpHFMz508YfPjdSCyTQ-s8wW99lc2aKbdWlU-bPO7GHpolTrx-hmKQbW4Tw6Lh8-5_1Tji5Wx1jKYcqxonHuw6r_qJNwpDVVnIA2sP_GWr3OwdTrkGLUyW-7CvBP-FFzDIvyJ_iXI3UfPpzQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvOrH9JX4jWlMW4rIP1fq_5tHT6ZXDu3rDB-FrsPULsIrUUXi0RXgv76qyVWcZFShb3ZzJGcL-m02Vv9jr1xOHb7zoi0jegoP4bwXyMwTeXtMYeslW13IfbfcQ8sXFczfUaSNPMF_HZlkJgZfxY2THkXYz2huPsRSnc3KrnbuIcQCzbEXmMvGIFblZsmCc_IlqEc4p2_4ARz3SCsSqCag6AukzYI69JP6apNMuA_Q3rbA3dLSxzPDXfkiqVQpNy-VT5X5xjsgP-qJqPOkNCqKQnBHK2hXT8XBoLHOirVQrlNjUiUNPvPaLhtRX62g8FLEox5PFS_qMjE8IMWeMr-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4FkfFvu5s8vQX0vdNGeR9syQWAnJIDIvDyL2ujzp9KIGL5wO3RSpbq63uXAW3ImAfjrrLKvl0BwvIS71SXK3_5s4DpQ8MT0LZ3BPcngN20E1jsSJItIrXGAw3lN3VqMLJN6b1fmtPObX2CH2lohjt03KZIqM2D1rMDQ3FYcp-5gIt5PyAbThQtCliRUppizlK7iX69OReMiSVL6Q0fpzFfIy_WrDOtc1EmhHo6DsdINFy207d505Sdi9SH52TMMxefnyfsq7dYPOOSi-qi70EJ6SRB3gkccDKTJuaQ0w6HsNKB9RcNZp95rr9SscupSpB5TWfpPk_i3oKdG7B7sSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VRrA3_AAn-vJaLp02d0A7nTLEF-GZyK04EerKWr_edt7U0-7McZ6Uz7T_y7i-Y-8MjjsWIr8uJosqXQrE57EAnoILVIMOf1N02s5nnGd1gg8Os20xK8dzflvZnZz4BKG7iVZ_FnICnP-sD_uG5hxj5wXPjnSvAMdMKuRFOLvox9dOzTfFMRXuNxtcfNJuYOQRAm6uAhflfbzOibr2HnOdi5e_lP1W0G2oXvBqz-6FpTYxxhirYB_vBUFV-qR0OMdErizOCC1NJXMizLXhT_9ASqjwRp2SZLacC-qK-mSmuZp0cozLMalRx5FMLGhrIz7Y3NpGjGcm6yQ1LUzoLOnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsLm_VcAF6-lMleyt_87fqOx_V0GyzHKN_oD84z_GVeQvEli2xNxT2MLlXjxKe2sbQdToMeT6YkZe9HljogPPm3g7JHKzHWZzapNwp5fjl5xz1KhE6lKkrIvar_ObWq_gnW72OOhgBQiFh_Wykg_Z8XhgPaUajpnGeScXsPbATn_nK4xq-9SQw_X_LiVeFlk3Izop5IqXCrhN1PtuWxGXqt7SYxH0YUSHbzKt28GxsCEHdL8GHSPUgwEoa7lgufdJhuugG89G6NjnAAa-QQWKdCN_A79oXl-cRoT-KC6GOcddoQ3S8hoxQjIHeAoLxbGY4lq-rEKz1ZBc-qMl2aOhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=ISvTUekaIANoGqvai--3LCRmNw62TDlIwU5r4Wx-XluFAnHqEgO9Hzjw4aqyQ3tS_nAtwWFRW9jTlyRmyqNGROqfV3e_rJbX2LvsdOq3T1DA61Diam0hBcpKxg6bhcWRUWgUqqBkzxrq9i2p1yLa8yNkYBxz_OY3qT8aL2o-OhVWlKUQ0_0S21fHQDKJfJbKG0Ay-WZS1EC23u_t-U5szKqbdkcrcxMVChuPEEUCfd2JBY5-Mu3R22SISZylZgFq_i9mArlfvVHmmrgp3fBCUjgM6vbpXl9bqYrxHPFjV1LO4wRYJrFuUHX7cvCSFsAFXxyXZQcRs0tr9_1ZXNXqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=ISvTUekaIANoGqvai--3LCRmNw62TDlIwU5r4Wx-XluFAnHqEgO9Hzjw4aqyQ3tS_nAtwWFRW9jTlyRmyqNGROqfV3e_rJbX2LvsdOq3T1DA61Diam0hBcpKxg6bhcWRUWgUqqBkzxrq9i2p1yLa8yNkYBxz_OY3qT8aL2o-OhVWlKUQ0_0S21fHQDKJfJbKG0Ay-WZS1EC23u_t-U5szKqbdkcrcxMVChuPEEUCfd2JBY5-Mu3R22SISZylZgFq_i9mArlfvVHmmrgp3fBCUjgM6vbpXl9bqYrxHPFjV1LO4wRYJrFuUHX7cvCSFsAFXxyXZQcRs0tr9_1ZXNXqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=bXxvGyiqlv29EwTZD51Y8KFDfVbw4BSXwYbXiNJjnUT5ehg6jP059sfYbGDT1fKF_nC7qK4VKJrVSaMjEcI9MZe_SxcfWPwen1GuINGEwWMX3XcXSQ9mFQAmLk-2ziVda_vrMFwxU-hrPSoWGFynNAJ9pw0FzEMk42rv3SjYzOCTKVplWaTwQPCQ4zYP7sc9VWJi0L8r9nw4RMcBCFVtOP9U6HP7vANxMptLcgZPpdMSsv2TAZbNBDBgHH5574QMTKqCvCL3bYv3_EY_NpLJfdkXXsub1tcSotlOsxBescUnPRjlHhECYzsHLOVnzgjwHWnwvTpCxHHrEE4xee5n9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=bXxvGyiqlv29EwTZD51Y8KFDfVbw4BSXwYbXiNJjnUT5ehg6jP059sfYbGDT1fKF_nC7qK4VKJrVSaMjEcI9MZe_SxcfWPwen1GuINGEwWMX3XcXSQ9mFQAmLk-2ziVda_vrMFwxU-hrPSoWGFynNAJ9pw0FzEMk42rv3SjYzOCTKVplWaTwQPCQ4zYP7sc9VWJi0L8r9nw4RMcBCFVtOP9U6HP7vANxMptLcgZPpdMSsv2TAZbNBDBgHH5574QMTKqCvCL3bYv3_EY_NpLJfdkXXsub1tcSotlOsxBescUnPRjlHhECYzsHLOVnzgjwHWnwvTpCxHHrEE4xee5n9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buhaIwk2FxVJT4JN_luE-vdyuQQKQjofjfHviyf9csWyvyCAlzfEzVgTCPoJFoQr1MKX-gUK6yy9DHOu0qHuiFUBrpvecUDHpZ4aDeeskR3t6EVCcckRUscI73qiKqNBNvS0xZXLn9i3lLkTKDPnrpO7M4PKDHMEuFDOZy6z7cXMiqCHtz2wR3QGBGpgijVyK9mwKMs40Qap2xXc3VYDMN2wXBq-wigkjzFd7TcJ7lLdBmm5rugJp2Msdf7mjX8UuK61u5RD4X1vGCHwEunwIUdnV5jsG_S9AN5jly7qOHJtPiuQRONKvkdt0CwQ7pZF1YsvWqac6Y-CsZCIae0fSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=llNLhXtGyyH5jdPm_zVMhzcThSWlGOLaJgaju2k1mR_kwUCyDf_z5jzEMcgZdwPn9eMjTqprvfPn7Aafpuvzojw3sxwsEC1PJ8QhnIVNKEDbuE3mi-MQr0ihWvHI5iQRGFu96BZ9Ad_04lP9WQhKiFBIuP5siY2c8RpSdP1GBmBx00wITFZBp-jWqLl_f_C8XwxtomKqakErpELM7hbbTlat0kYch0pW88KZVkVibS2pxB4nbQDmkyu3Uz9zwocXOKzgj_l3VzcThQJUkbvM5x2C8RcmrC74xSyvQkgkUpKqysaDuWz2LdbXvlCozjB-vnNPM4vqJWAlezasXQGAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=llNLhXtGyyH5jdPm_zVMhzcThSWlGOLaJgaju2k1mR_kwUCyDf_z5jzEMcgZdwPn9eMjTqprvfPn7Aafpuvzojw3sxwsEC1PJ8QhnIVNKEDbuE3mi-MQr0ihWvHI5iQRGFu96BZ9Ad_04lP9WQhKiFBIuP5siY2c8RpSdP1GBmBx00wITFZBp-jWqLl_f_C8XwxtomKqakErpELM7hbbTlat0kYch0pW88KZVkVibS2pxB4nbQDmkyu3Uz9zwocXOKzgj_l3VzcThQJUkbvM5x2C8RcmrC74xSyvQkgkUpKqysaDuWz2LdbXvlCozjB-vnNPM4vqJWAlezasXQGAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvItN435lWfIze-c7KVFNMyhgehD5G7qgVsgl0s37HJR2aUAftZsRzcSC5zmh3hISLiZVBFq3hYC2cZ0BfmvdsMEe4ktHq_5ZH2MVzkeJUvWu0s14RHb0jcZnTkrKtbBiJtID3Pau1omnwC2uEzeA2gGP0XnO-cU10WCl75C2-CWUqff7KiGWvQh_9fASOcRC57C5SPfqMZWu3WD1FADsajJnMwmQQrFi9D3EhieU61RdLklutxODIubBiw6zxxcMZg_4DxJI-nK6w7EJB8Ga42bfsWUeaUButgD91pvcvESZFq2VN-IOFjYLXoqZDE5KlpbCT6juGlY7kf9V0zo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCSPsRzFfFU1yJWo2xoyS8WfglU34MBBWUMpiJqsscLm9wc7GCuv0HySrpJByzU7mGzLsBFdHotDGDpsgWHIwt_UmquFmlNHwzd446H9DYpnOkNkJpIKMt2M42EVlrJfr9R6FF1OxkyziUNnL8S-R2GoNg3DETiaapUuY6KHXg0z-1jMzk6DuYyf8Fg9qHcYFtbPesoKCC8MFFZcoOujy_F-kZkpkSrSf8Pf6uKXdKLPx61m3piPqY-kUbY2wIhXqhjthd3QhHBqPWIGduFH-ivmtXK7hj7veNvJsYAukPhcZRsF9G2Nq9dmsSB8RNIshHdnpEnmrttdXsppDAO4Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-gl2kX-bdDYhh-T4WYV_akoXD3Dp2_Ek7X7Z5eex5ddT9WxlqjRKSPcDE45I0_RGRSpDgrZ93AW2A9eEWCSJgVUCCh7NAFagFIAJfY_WYqCcY4H7-WkkVbM-DBX691smAXgGKr9k9Y3M2GLfB1pWghP_aI7QLs9-y90DQYe_F8zHrbphtPoea-N0V4FDDuQYZuhaKaQMHCclcWmsHWI0mHUnGchCl_AnaEtT3CJ0Ps3s2M17njlCTIlyy6sgz-IbNIZjXujj9AVfgODGnsRjGlF_XPmPTn9_V-g_8giJFjlu5BlCzv-s4SDlOwJjfRlj9XR1NBCN5y8sptETR5lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgPIV4hWqzOcCbaJmYTA4dsnB2YBSSZooIyUbfLN39RAX79RKJGtCBNdnxmjnwUPsVaQIwt0eokBn3w80e8JlGnSxF6PoHBjVpM48Ruzfbwm_iq5PiksGxCh9ZInolWzDgNHxKHk-mq2W8mkna-pcx1DhQTaM2xianQcz9_7x0yc3CmjqrVwZyDVnF1sCv9EUecYKEECY8qlTlnrQYAkuhkZFCr8FQCIkAdXju4hrYeIUtjmqFuw5t6OQr-rxo9GD3QsmKPN4R2b24Rv3TPoRQL-02f3WApbLfNRSiKRqVF4xWQPMIUsaNRIR3AXUVrIlX2F4n-7nNJnCc31DIVx6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teGwNie3dPNRIXtbmEdJrMalbpdRibCsCg8wjrX44RSFGmovl_mWsSUeGFfVxKuGFaVd2RDP3XfBzE9TglOOyy-mGws7dHNXgjgExPULFON5CSYfJJPD0Ek11mRNDDTjaO0KkNsw2edkZZsN36yL9bERxX37wmPVFcFx-PKY0z-rpWv7PGUM5IRxj1aAu5T6qeHz6OrW9-VOvmjQyl9XDoQ6W27_dlnuZ_oEGPugNa5Rf2oo82hDz38vk-AYePVH0X40vcWl8JSqQj1jaNLx_Lo5Lt6N7cWfip7N-dK7GsyrdTwXyrWHv1xesd_6FLtGJabeg2ZHu3C4fiNwOB_zSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=pkuo6DbFicLiEg1QLnlmRaCZ1gfbv6Dy0wY9Cl35GNDiTZ2ViqbWo2SqHw_LB1Z436zCYdzFKhLDEOjmtvA_h72HCf5OKc0NYuk0UBch7WPVIs7WjKyCM8Iw_nPEbaNeD1Wd-2C7QC9LGXvZTPJS1FxY0JOmGhYPCG7L8v1dN4ViWwe_Wj-vp0ziSuADAbQOn6YU4LI9AHAdLfXkyEZWNkLwwO0X5hnRBHy87yi2CUE5vit_0Zlbs0ovdkHAXYFGxtFUeERkqosIo6WR4uEPvlRvxtPeT2OxNxYUouSxF1weIVkCpRQTLA95BoBXJULRfWJzQPD-NKTXw8DIwYI2QregCeqFISoFn0_Phz7pyYYmpOF9tVx0ozom2gT5iApwIFodFAzHUnjIFlwXEUGWTe6y_f5KjzGH8fE1hVguOHal5T58nsbl2MZIuJsIDF8IBgxsCDZEJz_PPMAfOtZWyLBeQuSksO_Ah2YJmoM-SwB-ZMmI0GbdPHxbXNRqLHsVa0SLM0UuZL7n2uQoJsCNfF7lm4DTlKWPbwX2Hblq5Y65uL8dUUjvMMnoOpfql01VI6-6oTbVPmbp-vAoO7R-FuaA7gzu0rTY4eb4i0MkRMwmoeJpj_lkVaXJMcsxoma-up80s7t2onZBDfPIL95O9MdgO3TMwZ_hkAkgJOOyAAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=pkuo6DbFicLiEg1QLnlmRaCZ1gfbv6Dy0wY9Cl35GNDiTZ2ViqbWo2SqHw_LB1Z436zCYdzFKhLDEOjmtvA_h72HCf5OKc0NYuk0UBch7WPVIs7WjKyCM8Iw_nPEbaNeD1Wd-2C7QC9LGXvZTPJS1FxY0JOmGhYPCG7L8v1dN4ViWwe_Wj-vp0ziSuADAbQOn6YU4LI9AHAdLfXkyEZWNkLwwO0X5hnRBHy87yi2CUE5vit_0Zlbs0ovdkHAXYFGxtFUeERkqosIo6WR4uEPvlRvxtPeT2OxNxYUouSxF1weIVkCpRQTLA95BoBXJULRfWJzQPD-NKTXw8DIwYI2QregCeqFISoFn0_Phz7pyYYmpOF9tVx0ozom2gT5iApwIFodFAzHUnjIFlwXEUGWTe6y_f5KjzGH8fE1hVguOHal5T58nsbl2MZIuJsIDF8IBgxsCDZEJz_PPMAfOtZWyLBeQuSksO_Ah2YJmoM-SwB-ZMmI0GbdPHxbXNRqLHsVa0SLM0UuZL7n2uQoJsCNfF7lm4DTlKWPbwX2Hblq5Y65uL8dUUjvMMnoOpfql01VI6-6oTbVPmbp-vAoO7R-FuaA7gzu0rTY4eb4i0MkRMwmoeJpj_lkVaXJMcsxoma-up80s7t2onZBDfPIL95O9MdgO3TMwZ_hkAkgJOOyAAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Bro0CPb4bD9xgbUeXZp8wnT3amPBKxpiO2B8Hf8CQt3htPnfc2In1nblJGIQxwFLKRK06pkJqaSpVJEEa6xyON4V9fjkNSmQRf9LtAzdLXvL0w58fW3GCAR4lsL23BaB085u30PqcjswJjkYN5a-jRUs9X4bAsKq3U4tbxDeKqiLGxgaBEhW0f-oA8L1F3BVB34tVHeutZF9CXCEq06Q2PdV_5cjYz3Mis2h-eTCWvfit5kEQ7gCxkMwZ0kDnXBGDwXVn8ZgY4Qqzrd1-JqUGmFQSD--uIeA7f4nYrxeZ9VItdOkUYmyVtysaFPzDlKA2CftuxPejZNeIsWD6ZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQDATx14eu6JF7Tmm7n1jmTbwqw_TDYEBpxGcTLLxS79Ugr2_SlCZIEpoAUg0QNUCACl7Zkrc70ouYBX40RX6MR9ITKLZ-GFmZPi9h-jJjmSE4ag5i6x5pVIoQ2OJWYGwx0EXOsXx5-SQXc8Vt7vHRjUrM4HhPMxbLPNK746LrUYZQFBtIceu1rMV0mrrd1Ri5JM061eAZGHLYU77cE1R7G__V9x39ure1WphNVk2Gse7ILcoWHXPa5dtGvmoa-iXc4IytvMv1Pakcfa8Ngo4frlBfFWah9NidvRkC5SQfZnxyZdycLVo_kF0Oan9H-w76t5x4W_KgkuhmwzmsuFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vzn1EM8VxtmJvqVftp-LsZJJxEp0vzz82jbvXiD7UIOADv9WpZub20B0G65gfa1WRBmrjEH8SoIf0cOcGHZwpEs7UaFmcGqwv7-MwOAIKvunY-y2zSs_G8hExHBv8oQsj7j6a2raZTgB9tK4XnLCBoD3kmtqIs5nbtgrvKUana4EfeLRoTGTB_cr1n7KNTstFe3ENxD18rTTjgtlh-aTEBqiapeT3VP-sC3SIYmvM6c1ikFlDR0FC-4IvwztGS_O5OXC97_YSsPaAklORK70V9k2mJCo7j1Zjr0I8vbD38y6Ay1oxjNEIrSn3LFO-3thmAXO1m0Syc7nQ4ksmzNYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAikGMdMXJW7ZzeLGWzMkdDguFrsDrtbiB9KXIfG-3Edv3c97XL-BzmNUjy2uKmxYc13YeNDM490a3_A8e0enTZtx_1gK7Nv8TjMSshpSOXiGMLmDPhbazek1dWLmb_Rpo-OAK1nAhAMJLVlcRGhEBs1VeYl5TenYhS7x0DCQ76Hw-JRtdjmA0u0SGWg7VE-l3YjzhamnTQCPRNDFWy7op33_kBIpiWL5ZFybaCa-cw5WC32hBeXQilZHLBHKActjQYwv2JHXjar6JOelqa_dzaiES3_zxKAqGI4_T3P20cmAEVMeeBBzBPWMV2OSvS_IvkS48oBfdIlBuYlEqiVIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkngX_7CPYYvI4pozjVP1lv3GySC7DSwoOoWc-UyEyeDOmun4bXVpP9XSyhnzyfWf_-x4D6PlokYeR02rr9SmGflHA1O_ukW0vpg18HlN4p6tcMJULkfsD-q0vxRes9pwaNe_8msiov0Yjp7HI0CWWknJzwDC94MJlywEIaTkNHFYxzq8-B7BVowUmAogyREC-TsRs7gBLyKT1sykaOboRInrgLJzORdmon23ckErDUByJTtRH8uyc0_O1Jf-i7jk-54vlj-BRlvqKMQi2KqxLVI2WCawBmd2Kh_nC_BWq5BAUo820M4XWbTPDFPpxYopJkblRStvzoKmkvLo15Adg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxaaD-khm3DuB_7MRDR0qYHfwwGfGPDOND9hXen842ph8TTqFbnqSCA4JlY0dtrEYxtxQ86M9gzYDb3MAFMlIHjPmgwj4Vc88qqAOlIEewtV8csKL1DA6TUq1XjcSGI3oGmn2KmOAxDI4hfcVpSZAg8rAO9BvG69as5LMG4-Gh4N8lp5mNA6Iu4KwmkKqwVEaGAlZTfq4pIXuhRG7wTYaisiN_MtzBw_17iidtoF6uejAQ29xiPnohSEVcEpoQ6GF56N-kXrqcXJhxKBj5KP3_aNzWVxcHDkQ6REhE8r8soh2cmQ3xxTtEJNKYdSTEe24_RaOazD2z11Ug6oWze7aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsaciZsAsUeERprZL_64o69xxOCW1UCTstlLeXOcMEhAgYySLm5nnTUs8MW578UakHBF3qoBTVO6TH8kGQctKBIBUWjI8YuNA9XySTu8pHOI5O55-7Vzh8ECLlKLXvH4v_Z7G8TGCL22d5a9uC6rFxpjQ8H96W6fr54rSSawlsGmvizkvDlslXXyvzINrAHrRxqMi7LdXeYT--Ocape7cmBG84ny_qY0_XiyhGgrgdXqIbDdnpkGjZJ_2AWRvqFEpcDY23XpLaLSgaKYExlMaI-EUH7Qn_Ux34nd2jksiDsoGrexWSQxH3hRMFiwNytrFgF3Ym5k9bRdYxnFNVLFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=qg_R_8KgiSEPgCcGdvuojaV-G_ojrf2zefgk3VFShn48V7PQ3G2vqAJKf_5uvQ6Rkft6n5iZ5eelSb5D7Y7LZjMreYbglgZ4BchDfzccTMBNGRlF4qmIiRtLRCb11Pgt_AETMj8IQleh_sqE4YBE9onsxv8figMFPbHJ54Wpl7ZcFa4FBpH8rQUmlDgvpZ9HgFekXvS2ty6T4NX9Xh1jolGbaAPtQ-PX6I2oggKEYhrYhZ6CIuopL3kxS3o8ER8RVFDIflMVvWXyY4bWZ61cK7Ecqrkb3kcW0Jl6N7vTroMxFSPf_LIiChiUYIfs4m8HcSoqkcXY7_i5zBdOgMPC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=qg_R_8KgiSEPgCcGdvuojaV-G_ojrf2zefgk3VFShn48V7PQ3G2vqAJKf_5uvQ6Rkft6n5iZ5eelSb5D7Y7LZjMreYbglgZ4BchDfzccTMBNGRlF4qmIiRtLRCb11Pgt_AETMj8IQleh_sqE4YBE9onsxv8figMFPbHJ54Wpl7ZcFa4FBpH8rQUmlDgvpZ9HgFekXvS2ty6T4NX9Xh1jolGbaAPtQ-PX6I2oggKEYhrYhZ6CIuopL3kxS3o8ER8RVFDIflMVvWXyY4bWZ61cK7Ecqrkb3kcW0Jl6N7vTroMxFSPf_LIiChiUYIfs4m8HcSoqkcXY7_i5zBdOgMPC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y--eVRichbNSH1oSlQmuvkvzxZ8VZGl3clpIGg7JPNCyhTNptBWsr1a3ctrmuIsrxO69Eh0m93TH5T8S_oL7p8qU4RRu-soqCgSgz7AQsykW6scGtqXSQQ0wRmV3YzdhFE2JvT_PL_3S4gOjl6fajWT43JSTXX569inlgAvgibPqlW2-o-d7FZ4qOpxQ-QAE3V4mplfmYF8Om1UgLqpR1kZ09S6OfS7BeTsmaArwwMbN2neLYXjWilnDfEx2vVOOMt-ZVLzdYATb9NzW4-vVUzDHrKj8S4ewjoVStTRtgdMis-UraH_stsr2AGqqvnHbKMBFpsKgopF6LalHJBQSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrjgWLoT2pzoDOLNH_PEGRqrZ2BCUGpKY5imrdaJJ2HaN8X7YrZxPpTWj0jdCVdO2c1CObPPrp05wy8LDGJbWMLrHDWxydWTrEanmqvJ_cS99_sgkb1ALlHNvBaimrjOKQcN57IfYVjT92y7FeEqKWMV97e435fdsWhOy0oE_Pdj_0V8NBCWxogOpNBbsaQhFBYX4Uk7w-zunENXwErwFuD-up_mhxtuM1Rv5IfXWkWs4m0sXll6WG72NaNblcWU9aX5DcFOto8BjZP6GdHid9ZTyeRYyIoppL8bMOJzhqvwUXJX28WB1fyxTs2uT-YakMboJfOul_Lh_lsKLZlVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3pY9kdXfrynSwZCOOEEf2HW4GA3QIvG8DbyIitVo2CUhzFVH8kVydhXV-qa3Z0lPS72Lx5Z7R5NmiPdyjEahqhKxdydNwMeSC6MPYfnFCOaHEVixTA5980w7wQBooI6YNcqAE7ziQe1Ie1M8DXWrk1fuNwDUIOM45cyqP-Z9g_00Cc13MU_tS_xV2w8Spcka5Ug-XwQq8j4Gq11KTEV4FncH585NZ-qEy0WG899Ai15UkSyo-dOu9cqqgvqKga0bP4xsQHjmSMBlweeqKGNB9y31HNDV7y8-Cup_EzlfzXEjUIPP6rhAAsbyozp3X9YlUeTp72MpyyPN0yOWHxw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=GNGFOlIjvBV-8PVYDLiz42gNbNAlJA_lAH1HM1nhJNrXnSu84ungaNEjfIqfzicFDwR4o9KUm-vtlI6O68YypwvT5ALvlymL-PSQcv7kYfgnuTRkMsw2bEUM9A5U6P1NMbr-yVhV1aBss0J8GRtDoiTqt83ih6jcV4g6I56gxbrdi4wdVlGtjTyYPPJQY1zB59szFNVDHTX6Wyqmv-qO11J6Hjnw-u5dUCnJC9_uRIsw4Qk83KCx8j4C0E8AGcj_xO_05CG8eeExKdvVe4a9lXMQtPaH5uFwgg2dY91M2OeewOhy_cqUm7yJEO3scGvsEBeDipnRr1p59zIpiQ3iBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=GNGFOlIjvBV-8PVYDLiz42gNbNAlJA_lAH1HM1nhJNrXnSu84ungaNEjfIqfzicFDwR4o9KUm-vtlI6O68YypwvT5ALvlymL-PSQcv7kYfgnuTRkMsw2bEUM9A5U6P1NMbr-yVhV1aBss0J8GRtDoiTqt83ih6jcV4g6I56gxbrdi4wdVlGtjTyYPPJQY1zB59szFNVDHTX6Wyqmv-qO11J6Hjnw-u5dUCnJC9_uRIsw4Qk83KCx8j4C0E8AGcj_xO_05CG8eeExKdvVe4a9lXMQtPaH5uFwgg2dY91M2OeewOhy_cqUm7yJEO3scGvsEBeDipnRr1p59zIpiQ3iBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mly3424L1R_T965Wx-0Z7NagkF0VFYVF6tLM_UMN2l2cgrwxwO_nCFEe0jSMgwtyC4x0Wh1GCaQEme2nqc9K9CuLB_GpiWxDi5cS5qU6OjVsSrtwMWvjj79-v8kPEq5N6sF7ex7E_lax8ZXBczhwkvsTZZxSF3eFl81xYA97rHRO6A74x-AG0n2egnuxx99EBIy1sqaFqoFSbJqvIReDP8Xy5zOEmf6O40XAqtgab8RZHfkDIyiI6rgzAVD2zVEtOIoB-kK8Kia8j47XEYuqbf02T4G5rwt1mkOcCx9cSuoh-YOEl6YnrCaiZowo3gDeAMes2nJZdqPZLVRnuLlyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=Co46P5kuXo_vXaXKw1ALDTcof7ZMO1OmXDTp-w9fYIUrWBE2gsa6U0tJWZN0woIhs-rRnQsPBgrZ4H0K2iyrMWed5k_0FZQFdPV9KbAPErSj2mW8JcjQ9XyKyVvjn_5QechJzTsLxeC_xnfazb9SRL1XMIFpbirnrF5CumKgG281nHFtkjGQeA0HCypoLKYNaGwUsGUh920r6W26emwAaZm7Rz5_-CYd0JewWAq9tAomC_E1RC0PJNORdcpHCaDLWPzJGyQZ2I755H-50MMDwsI7ehgWc4ub1U6Zg4qpSQ03MuvJPCMIoiaarDKWG83rsxRHcdDfzmNX4g9ric7n2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=Co46P5kuXo_vXaXKw1ALDTcof7ZMO1OmXDTp-w9fYIUrWBE2gsa6U0tJWZN0woIhs-rRnQsPBgrZ4H0K2iyrMWed5k_0FZQFdPV9KbAPErSj2mW8JcjQ9XyKyVvjn_5QechJzTsLxeC_xnfazb9SRL1XMIFpbirnrF5CumKgG281nHFtkjGQeA0HCypoLKYNaGwUsGUh920r6W26emwAaZm7Rz5_-CYd0JewWAq9tAomC_E1RC0PJNORdcpHCaDLWPzJGyQZ2I755H-50MMDwsI7ehgWc4ub1U6Zg4qpSQ03MuvJPCMIoiaarDKWG83rsxRHcdDfzmNX4g9ric7n2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcbv4IC-zyNm02dEnnLxeqwfwv0enHn1ZSBHQ79KShaCOy4kxllcDa8aY9MA3GybKf_MpMp-wFt0m7V3TGZH9Oq34VgwTK725EWxvCDjoAiQ9aewhAj5Gp8kDUAR0iPnNmTWNfxBVoH3XTOSLpJxrM6V85T00k50lSvq6iGxhjXPVeT6itUJVxKcFNzcCwrasGPDkHloA6gcvl5kilH_Fif5WdE7CE2nYdcLVY8iTHq11O6phoqLSZJgEh56s6poUcjdTVYbQbGMrNFSK7Nxj1-CB79ADNFkRVOb0KGvMwvFPXThFENLNiTP4XC1CdhkCV2XW8FjKYx6KTxt9ZXnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeThVH1VL1yABjkoH_qYcuOMgsNwmXe9n0_PmWogRE8eDzEBQn8fR6MiJ4G6fjj2jViMDRgHv9UlL3YLnzK0qJRecjM7233ZA5DREf-MVTV3jOqpiowQ7WzkXTiFmLPYsy9Zs_MlV79Dx74ULeAJMj5WKBGkN9r8UvxzfzgmPOQXaNjF5DHelLMwaSbtcZJHJcRbG8IP_wpQK6VYuz6bUR-VOaTngiFFEn5vFZ1qfRUWYpDilapfLzhjDQeGGaaagFJ8EiqE__QLUN9UeORQsu4BMySP3PSpcfybWfSkZy0KpCLuwpeIq9O4YpqcwGRGP0z0srR15kHC184Qp3Clog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeGEpDGd9f-bz499jMZEKOcaqGxmPFpZTqQ07DZJk2BHU6Np26syUSfbg6fydoEM49Rv6WBizrnwoxU0BE6Wm84t-7oK6u_EO83jOlWv4P457_RbT3537i0wqPbOTrwEIHibw8oInwyq0aiX5F2QrhDVUbcE135jBcgRmRRxHOhkPPkt00Yz-miYnKiz8O3VYnkjmmC-xRCeXPpevCOnFGAPupWUOdQSYywwpMx_AM1Wrnk60pgdwZAik-YZ9Yzi-NE8GSbZ7CF4zw0ki1z4p3xHq9t2Py71oxwMJbWuj-pIqaHH-CoBqqdUn8lSydDkPJ5nr30FqvJo_g7uMoPo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHtjKP666pltAFiYEbZfU07Yda9X1YCUgNsI671oZav6MCAzIv0iZHvvBZw-dzifClrQaOklBowaX5i7ozGssCKReOEBwutfEe9XFnoS7WiIKhLYa8Jcn9V_-8BV19p1bar-IuysuVMwTOA2aNnO8emy05NpdtOkfyt3a4MFhZ_gAeokIRyUTACA6pgVG_BQLD1L_qM76U3ln0BX0U1t6Avcs1kHhikTZcrfPN33Nf-r7b3fvlR0-uPgHPttMisBGlruPzK-T2jTqSfAjlA8SI0uz5k8HfdKUO3YBUcwr_dZp12TvHFsY0UV9Iji4jnPzw46S-INUxagWzSlW03UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dre3U6fyyjCQxCwHTqBFOW7lmmqZYSB_CI4xsi2mPcwoIUPz71tdpZbz4eONl6NDCtNtCHpiSV6sndtxwVQEwxStWpql8zupO9V-Un_YPFKr1MQDZr9bu_V_mGIpM3QoF94VOsmXTl2PPFtYkEWVlI63jGhfdNOn2MSDs4END3xbyDtxxAsntAuaz3xTKE9RPGtRoEgM2EaZI8fZpOcSvZn1lYmBzBcVp6mHUAMDv3IU_n-rL8eDMNhzq-i4uFkFX6p4guIO2rjfbh8fNId5VG5iA34vVBslUWjG4JCGxfPBhj2KYM8e7J5boKk3QM6pZ_Nyp1mAmLV3-ABMUGGFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
