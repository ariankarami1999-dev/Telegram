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
<img src="https://cdn4.telesco.pe/file/R1HZZNtyKhHoULqsmat5ydJQJDdZTvK5WwR_8l6rx-IOAF1Ba2DaAdFmwp0NXGhMZX_fwIhCPeKKIBNeBGUCu2jkdGdItxRfHZVTaP8lHTN1gz8jBF9M-evlkrbTUBbq5hMc4VEY_cdmGagwpjk8ODfAUptwJArX9pYlSDAW_eKr1p15nYFlVVw6aePmrRqjWTToNCnND9Hn8yCTiFs8TVELx-dES1p99KoJMNfrOA20r83RBiAT0y8DRoITbbk-sUdTOOegtsO_1bhu8y49lp-FVuke4uwdRVfkB2PN48kfMX8X7wJecVmCtlV1HYLv4gRiUwUiYZubc9OX4_I7cQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 113K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 23:03:40</div>
<hr>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=OZDzubA_-lp1_fo73IFIMqYOrO5QfYa6A7s8pKyJH_keOtk00HMHV_XMNfpoBLE5ZhOR2edkJbOzqL22Mt7ZvOIxLX5qVBrCkc-YH7z-Q7W8DJTRU3HnboHKymFeIX9zugdEsgF2Zjj4DtfnOWokoNuYtBhsmovy5lehTP5L0PVBkbYgUhrWjeakT3XdFHSppPQq1Jx37fM1EeYA5WhXxPZZ3zYI2gi3jDU7PonzaiHD755qm7H8f6JJA80PM6a3vVjLYP0B3OwNaxfKmCmM69t0w2crL2WcWNhQ84Lpm09EH5rxRDRueb1xrDCsAy-Ou6-GraiBweF46IuudqXLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=OZDzubA_-lp1_fo73IFIMqYOrO5QfYa6A7s8pKyJH_keOtk00HMHV_XMNfpoBLE5ZhOR2edkJbOzqL22Mt7ZvOIxLX5qVBrCkc-YH7z-Q7W8DJTRU3HnboHKymFeIX9zugdEsgF2Zjj4DtfnOWokoNuYtBhsmovy5lehTP5L0PVBkbYgUhrWjeakT3XdFHSppPQq1Jx37fM1EeYA5WhXxPZZ3zYI2gi3jDU7PonzaiHD755qm7H8f6JJA80PM6a3vVjLYP0B3OwNaxfKmCmM69t0w2crL2WcWNhQ84Lpm09EH5rxRDRueb1xrDCsAy-Ou6-GraiBweF46IuudqXLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 336 · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=g3J2-rCidCt4HiqufqLpzkGX9vjtVOIAZQ28VLqKSp3XFx8lXzrkCUfIfCOy_zNBSGpcMAtfyRupLs5e4guOFxRkL5SIQjSLX1eCbITQRwdpYSenspEKQEsgdMPMQtVVrp5pGBTCp9-GxgHywlizc5RiP6VfaBar_dY6xUvMnJyGFlAVSisamA1GbYrGEZz_8nXzaAFcOreOnxWg9a0t8Ud6ucVN8jM1XUdqGIMcXL7_24uSb-Vk4QPdDkAW0iMvp513AUCGCrCjurFNtBAR0TL09qTiyHaI5BDl6e_kGf_nqwbeupu12Nf9Y11EjdMQJnXlUASS4t0p9LOilKN_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=g3J2-rCidCt4HiqufqLpzkGX9vjtVOIAZQ28VLqKSp3XFx8lXzrkCUfIfCOy_zNBSGpcMAtfyRupLs5e4guOFxRkL5SIQjSLX1eCbITQRwdpYSenspEKQEsgdMPMQtVVrp5pGBTCp9-GxgHywlizc5RiP6VfaBar_dY6xUvMnJyGFlAVSisamA1GbYrGEZz_8nXzaAFcOreOnxWg9a0t8Ud6ucVN8jM1XUdqGIMcXL7_24uSb-Vk4QPdDkAW0iMvp513AUCGCrCjurFNtBAR0TL09qTiyHaI5BDl6e_kGf_nqwbeupu12Nf9Y11EjdMQJnXlUASS4t0p9LOilKN_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره انتخابات:
من تحت تأثیر انتخابات نیستم. خودم نامزد انتخابات نیستم؛ حزب من در انتخابات حضور دارد.
به گمانم حزبم به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=A6gNDme_6isf9E2nK5GFVJfLtwlDMH2a-6U4z0htyJRlFtw5ekaIJzIEQZ24pwcn9h7o2mibewe39lFwONdXo-CKkrwYKx9m9njAZax1fD_E49I-ppT5tuJEPg3LHnkz3XoWAlAytXGncRG3T2Bv5oaZmkGCpnqQ6WXGoapO8sF-OXdnH-ZiEkB4p18EjMX-RXsRqcwiK6adcOYAUt58DDbDTbzfpDsWPLYTgToc38UKjMqohsgWkP33pU0ZCtdz5DhXhmDj03P7NiELizJQYbkh6lAWr9m9pM3sH03xM6BQGQwQjsSyougXVqALtb8QoEFUXR1uNRkkut5yFaQ1EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=A6gNDme_6isf9E2nK5GFVJfLtwlDMH2a-6U4z0htyJRlFtw5ekaIJzIEQZ24pwcn9h7o2mibewe39lFwONdXo-CKkrwYKx9m9njAZax1fD_E49I-ppT5tuJEPg3LHnkz3XoWAlAytXGncRG3T2Bv5oaZmkGCpnqQ6WXGoapO8sF-OXdnH-ZiEkB4p18EjMX-RXsRqcwiK6adcOYAUt58DDbDTbzfpDsWPLYTgToc38UKjMqohsgWkP33pU0ZCtdz5DhXhmDj03P7NiELizJQYbkh6lAWr9m9pM3sH03xM6BQGQwQjsSyougXVqALtb8QoEFUXR1uNRkkut5yFaQ1EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
دیشب حمله بسیار سنگینی صورت گرفت و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=CmPaub4Co3UBaKvkHnZLFS9tZRBM0dTm4knpOpWj_bJm6ERFzbAQD9s_GJawgYPC04B2tvXoDpAl_V-awzGeuCUH_GVzOOC6ihWclRwoD-3oYlRh-MJifZbu7PvoaJ0AM_nhK1aAM5RO2HX4VGH5VNkDMF-mrss37pPNSMzjI-IA3viDs9PULPhwbfooo_lG0nkCNy1RdU8Ghtbg5boET5AQSi5MmbaMomiaJ084YdBKzq_scUge4MTlOLw_7SA506UMgVmDT9f3zaHJoPWgevVpTmTpCOZDCHhNUw5RA5WnjfI9kF-djYK1vfwegXWsGrO-iImYSJu3O5jYLHVOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=CmPaub4Co3UBaKvkHnZLFS9tZRBM0dTm4knpOpWj_bJm6ERFzbAQD9s_GJawgYPC04B2tvXoDpAl_V-awzGeuCUH_GVzOOC6ihWclRwoD-3oYlRh-MJifZbu7PvoaJ0AM_nhK1aAM5RO2HX4VGH5VNkDMF-mrss37pPNSMzjI-IA3viDs9PULPhwbfooo_lG0nkCNy1RdU8Ghtbg5boET5AQSi5MmbaMomiaJ084YdBKzq_scUge4MTlOLw_7SA506UMgVmDT9f3zaHJoPWgevVpTmTpCOZDCHhNUw5RA5WnjfI9kF-djYK1vfwegXWsGrO-iImYSJu3O5jYLHVOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
یک ضربه کوچک بود، اما دیشب ضربه بسیار سختی به آن‌ها زدیم.
ما تمام تجهیزات جدیدی را که سعی داشتند در امتداد تنگه هرمز مستقر کنند، از بین بردیم؛ تجهیزاتی که برخی جنبه تدافعی و برخی جنبه تهاجمی داشتند.
آن‌ها تلاش می‌کردند موقعیت کشتی‌ها را رصد کنند — چون همان‌طور که می‌دانید، قادر به دیدن کشتی‌ها نیستند؛
ما تعداد زیادی از کشتی‌هایشان را نابود کرده‌ایم
آن‌ها نمی‌توانند کشتی‌ها را ببینند چون راداری در اختیار ندارند؛ چرا که ما رادارهایشان را منهدم کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Na9JbyvBTzqQ9MQnp2cfA8QcrJfr_Tpv3ygdMDjvlxYSu2SJT7J9EonFrTzd94swtHxrC-8OMUHLXICHWO3VYTW-8CxlYb7nbWs9irnlVcaNhDsYlN4V3UMIle7WgDco-XligAFBGsjb_5J2KieB1SiUgyJYZrTI2jI9_kyPu_tZ_Ond36BxAVxjtpdvHkC8jKnslRL5A_Z66kPoPXD9ctkafvitGZtj-KNJuovbaLUSi8UOscLJko-pbYFWNZjzxCl5pkQCTaZRnsOimav2449UCgUuDXP9Lil-rSIOpLnUSscw1Rh0vBMk3pJfJamsuQCFjaszbw4BPae4kZJV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Na9JbyvBTzqQ9MQnp2cfA8QcrJfr_Tpv3ygdMDjvlxYSu2SJT7J9EonFrTzd94swtHxrC-8OMUHLXICHWO3VYTW-8CxlYb7nbWs9irnlVcaNhDsYlN4V3UMIle7WgDco-XligAFBGsjb_5J2KieB1SiUgyJYZrTI2jI9_kyPu_tZ_Ond36BxAVxjtpdvHkC8jKnslRL5A_Z66kPoPXD9ctkafvitGZtj-KNJuovbaLUSi8UOscLJko-pbYFWNZjzxCl5pkQCTaZRnsOimav2449UCgUuDXP9Lil-rSIOpLnUSscw1Rh0vBMk3pJfJamsuQCFjaszbw4BPae4kZJV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ما هر کاری که آن‌ها انجام می‌دهند را می‌بینیم.
آن‌ها حتی نمی‌توانند به دستشویی بروند بدون اینکه ما متوجه شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=aTrzgxxhxRsmZe52SoVQv8b9oZ5LlLKWplhey6dgjflMxFUcpW455XCXwUX0ELH9cb2dYpRzSZpzqMd6mPUhSkzUG-dhXw8l0JQR0NSNHjC7MOIgck-rUdYI0cra8tlXIgC1-C_1RRgVOA3Z_L0b9alTgZzMYnixu_RBNEuByXIA32VrZYuoVYZBQEtE1TlQx7aHUcDiEV0zpr4G0jBE_LrsPkmn-kcGxblHHBCRekuGjBcdUDBc3CWWL8QNhkxqJ1Zo2FqVuXUiqbgq9sJ_DzViQNpj4Uy3q76j043aosvJMmMfiAmMvPiUkB_-BlVLAv4EPsYt2nRd7mrYjrKKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=aTrzgxxhxRsmZe52SoVQv8b9oZ5LlLKWplhey6dgjflMxFUcpW455XCXwUX0ELH9cb2dYpRzSZpzqMd6mPUhSkzUG-dhXw8l0JQR0NSNHjC7MOIgck-rUdYI0cra8tlXIgC1-C_1RRgVOA3Z_L0b9alTgZzMYnixu_RBNEuByXIA32VrZYuoVYZBQEtE1TlQx7aHUcDiEV0zpr4G0jBE_LrsPkmn-kcGxblHHBCRekuGjBcdUDBc3CWWL8QNhkxqJ1Zo2FqVuXUiqbgq9sJ_DzViQNpj4Uy3q76j043aosvJMmMfiAmMvPiUkB_-BlVLAv4EPsYt2nRd7mrYjrKKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
بیشتر مردم نمی‌توانند به این شکل آدم‌های خودشان را بکشند.
بیشتر مردم سعی می‌کنند منطقی رفتار کنند، گفتگو می‌کنند و بعد شاید کار به سرنگونی بکشد.
اما در ایران، آن‌ها مردم را می‌کشند.
وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند؛ درست وسط پیشانی‌شان شلیک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=S4OyeIMPksSHhJW3_z_K73DH441LgYjuSm0IHPMO1t68ClIrfJ2E-Lc9SGbe79-FtpRIzYgNz-yAYVsTb9s7EvyK2lm2-6nAE8Kbd3kMiBRACh2ZYOhoAzb1ALddfMDsjIznMy8gwUp-AZcAGlRxWcJEgc3lDLy5accywmLz7H1LNK5NbkrHDjrjpAPL175Y8KmsyG3zEOkbU2dFZInXpU_BXbdrv2LZgeJ4mRAOaHWC1YRMbcldXZYZT58wwm7t2YRclB9vxvdhFL9JW1U1GCxXjrf_XLew0gpz73onAPQVr6qE79AujmmomQuQg0Auxd104M6ToB2y_Po5VC1Tmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=S4OyeIMPksSHhJW3_z_K73DH441LgYjuSm0IHPMO1t68ClIrfJ2E-Lc9SGbe79-FtpRIzYgNz-yAYVsTb9s7EvyK2lm2-6nAE8Kbd3kMiBRACh2ZYOhoAzb1ALddfMDsjIznMy8gwUp-AZcAGlRxWcJEgc3lDLy5accywmLz7H1LNK5NbkrHDjrjpAPL175Y8KmsyG3zEOkbU2dFZInXpU_BXbdrv2LZgeJ4mRAOaHWC1YRMbcldXZYZT58wwm7t2YRclB9vxvdhFL9JW1U1GCxXjrf_XLew0gpz73onAPQVr6qE79AujmmomQuQg0Auxd104M6ToB2y_Po5VC1Tmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
تا سه ماه پیش، پنجاه‌ودو هزار نفر از معترضان کشته شده بودند؛ می‌توانید چنین چیزی را تصور کنید؟
و حالا شنیده‌ام که احتمالاً بیست تا بیست‌وپنج هزار نفر دیگر هم به این آمار اضافه شده است؛
یعنی شمار معترضان کشته‌شده به حدود شصت‌وپنج هزار نفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=MYQkGIlYlr9lGEmCr12XCGaAHWpgDD1OGJidVakgJJ42rfkPlUwBNY8BAHB4Bj8hBk5O2e2isj3i6iInhwbTTCWsveoTQXvVrDjjjGQtaS_ZMJQntF-i-Zn453m_qatx3ZrfP2sakXvfuHN_gQSj7OPy2HuhXDzXOOKBFDR6hRMbuS-x0bLEfhW6sbyFCPJx09m6WCWM9T9vEcjzkXAWO4n9s2d30bCVKr-kU3IiEYEnD9qvw5iWyM7fsZTbJA8qU-ICdvAFFTM1abiwql3IKB8GAwk5n47nh94EbLZGS4w7ejBZ4LE0tEhhdyPhbY-6yA_46Mc_VYN1qeRVHfOxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=MYQkGIlYlr9lGEmCr12XCGaAHWpgDD1OGJidVakgJJ42rfkPlUwBNY8BAHB4Bj8hBk5O2e2isj3i6iInhwbTTCWsveoTQXvVrDjjjGQtaS_ZMJQntF-i-Zn453m_qatx3ZrfP2sakXvfuHN_gQSj7OPy2HuhXDzXOOKBFDR6hRMbuS-x0bLEfhW6sbyFCPJx09m6WCWM9T9vEcjzkXAWO4n9s2d30bCVKr-kU3IiEYEnD9qvw5iWyM7fsZTbJA8qU-ICdvAFFTM1abiwql3IKB8GAwk5n47nh94EbLZGS4w7ejBZ4LE0tEhhdyPhbY-6yA_46Mc_VYN1qeRVHfOxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما امروز در «تروث سوشال» (Truth Social) نوشتید: «مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟» خب... اگر... اگر این چیزی است که شما می‌خواهید، آیا سیا (CIA) را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
⏺
🇺🇸
ترامپ:
خب، پیتر، من نمی‌خواهم چنین چیزی به شما بگویم. خیلی دوست دارم این را به شما بگویم، اما... اما گفتنش مناسب نیست.
ولی... منظورم این است که من وضعیت دشوار آن‌ها را درک می‌کنم؛ آن‌ها هدف شلیک گلوله قرار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=KL6uV-k4foLmRz91ykRL0ZFCPT1-hDZt2eQl9cg4FWoLkwYGh3MplH5sFOup_xkHXdlBHs7mgHyf__6lIXpuXmy9wRB42GKCTf9ZGFg5_KbfrSR-8npknTZWxy9d9xrHkGM_kkjcLB0Ly6jU47yZvr6M1nWpV_4wQ9qK-qYViiy-iYqKXhWRTIqYgV4OWYZmOmXcGSgXikmsmoD2rgy2iz9EFbjHo4NKTRvESXWcvIlZNF7XYEuTBGIhaLe0c9Pi7Je2KAIzcWM5RIR30EW8IQvcUKT1R4o2zQV90z48IzsO4n9dtzVMQt1ZaDIU2ZzrR4e6ghoSRFDSRHEI2UTOqnVKnOprXet-AtPNeNkpzfWZ5ZhpykmP0XIrL5eqXFlYQHQIxzwjnax3Dyb05AUOWHUpu78mGNtTSR_EmxKpYfbWFEVYV_f2dHVjBIbiyoYNFysQqDV1McH-5tLOdk5pSm_689EOXmjzKJlIX28MaHbQDYZzoRhDeRPsRYffjxfT_YpgXMGEtLyKhsBnrAE1vVH3mxLOgVn55-s_4xw52xZa-5QskXmF27gZYlBvWHQORQA6JGoA27yMiW7Onlq2NNkbT9lGGGyI8HOeBoVBfKoAXOZ6h5AMVAwGrVRHFtmwUeOXQ-QlyMLC_yzIcyiLs_-3HotEgJkOGhaM02XWprM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=KL6uV-k4foLmRz91ykRL0ZFCPT1-hDZt2eQl9cg4FWoLkwYGh3MplH5sFOup_xkHXdlBHs7mgHyf__6lIXpuXmy9wRB42GKCTf9ZGFg5_KbfrSR-8npknTZWxy9d9xrHkGM_kkjcLB0Ly6jU47yZvr6M1nWpV_4wQ9qK-qYViiy-iYqKXhWRTIqYgV4OWYZmOmXcGSgXikmsmoD2rgy2iz9EFbjHo4NKTRvESXWcvIlZNF7XYEuTBGIhaLe0c9Pi7Je2KAIzcWM5RIR30EW8IQvcUKT1R4o2zQV90z48IzsO4n9dtzVMQt1ZaDIU2ZzrR4e6ghoSRFDSRHEI2UTOqnVKnOprXet-AtPNeNkpzfWZ5ZhpykmP0XIrL5eqXFlYQHQIxzwjnax3Dyb05AUOWHUpu78mGNtTSR_EmxKpYfbWFEVYV_f2dHVjBIbiyoYNFysQqDV1McH-5tLOdk5pSm_689EOXmjzKJlIX28MaHbQDYZzoRhDeRPsRYffjxfT_YpgXMGEtLyKhsBnrAE1vVH3mxLOgVn55-s_4xw52xZa-5QskXmF27gZYlBvWHQORQA6JGoA27yMiW7Onlq2NNkbT9lGGGyI8HOeBoVBfKoAXOZ6h5AMVAwGrVRHFtmwUeOXQ-QlyMLC_yzIcyiLs_-3HotEgJkOGhaM02XWprM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:ما رژیم ایران را سرنگون خواهیم کرد.
ما این رژیم را شکست خواهیم داد.
🎙
مجری؛
«شکست» چه معنایی دارد؟ آیا سقوط خواهد کرد؟
🇮🇱
نتانیاهو:
سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این رژیم به هر حال در آستانه فروپاشی است.
🎙
مجری:
آیا رئیس موساد، رون گوفمن، برای سرنگونی رژیم ایران تلاش می‌کند؟
🇮🇱
نتانیاهو:
تمام نهادهای ما، تحت هدایت من، برای سرنگونی این رژیم و شکست دادن آن تلاش می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=OM1gw-aa84bQcDDPG_S0s5cwWVMitkosF67arMccQSv_FyQx5tx2HS6_tcigcPddG4wYnN2HpIV3K4CAL7Sq_2tRgqWi0HsUeN0MslHxCvT_AwJwN5602WIdQESU7peFp74SaiDhnyWlXV4Dw1YM9SYh8DpGorNBFNItuOlTFR7_F2bOtKUp7Z-yhSmI0Rwgq7-M-SGRNzUd7-lAfoofWye3i6ebh2_W4m6VGr9gM66PbkWk7urXol3EfLyxUNpgsYjb19kVHYuGQ6AJfNMhF4VNc9bOL2DV8JDt25aO1xrn2gZbW-LwSPr-1ZqmR2R6j0PehK2Ri7J6GsNgfNbNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=OM1gw-aa84bQcDDPG_S0s5cwWVMitkosF67arMccQSv_FyQx5tx2HS6_tcigcPddG4wYnN2HpIV3K4CAL7Sq_2tRgqWi0HsUeN0MslHxCvT_AwJwN5602WIdQESU7peFp74SaiDhnyWlXV4Dw1YM9SYh8DpGorNBFNItuOlTFR7_F2bOtKUp7Z-yhSmI0Rwgq7-M-SGRNzUd7-lAfoofWye3i6ebh2_W4m6VGr9gM66PbkWk7urXol3EfLyxUNpgsYjb19kVHYuGQ6AJfNMhF4VNc9bOL2DV8JDt25aO1xrn2gZbW-LwSPr-1ZqmR2R6j0PehK2Ri7J6GsNgfNbNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از دیدار محسن نامجو با مجتبی خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5fMGAXuaXGaC4m5gyoouDGIpcDGhaSQW1MBkRIA22pBz-K2lZjJHjP-g3FW3fHzbULrY4v3flI05N-dFxujZz3tjohuFbqQTD5E5slT4rKl9xd7e_kLCp6ErjF9cYf5m4dDd-fLt4KLmLWc_xzjfENcYQgVSXJwyABWpQJgQiuOMKLS-o67ru0lLC8Wro9inpjwb0F0BmGcb2DibqTO4IFNXG9z3Rq-lIpj9GOLfB192hco3aVJA19MVW0EB_Q0LXyM7QxNh2dEBO1utjIXIb6h1qGh6QE58aMxAEhCVnfbNxEuALOSkGoQ25Dc3VVULwEQuE0u32FOSEEEgsbfMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDQc7T_0bOY3oinUIIRDSis4McC7mSMWbxC6G6Dd-dDxSCvLC4UB-l2QwO8KK_2INGVM7Eq8OZNzCV-0y8OFWm5ozL5u7SJD1k6qgO_S1RZ19V7I8TU5KM8HnElgmMNrRoBlY9cvDCfA0RDwDE1_30y3dkJWCML863apjBgiry8i_QW7KSspWL22cszI6k-5X2Bx1eLWwU86jW3rHVLBa57Wc7f9UzUAX9mGwBZTVaGdw_MzdsccxUGKYFK2xXEfTXSQbTn5oDaZ_qMRtyHB-mb0dXNGUeGllz48IwTJA2YwAgyT9kLLPBEgsAIHI3ZEcaDMALtJk0n3e7sRjbhouw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuiNmWMs1c6Q0FTLPyNML_qWy9G5R0IX5JEnzGOumXy76CQPTE9-wIAZdpJ5vT0ZEMHUSX_P97K557qMaBw7_jZFCdJ-dgEvaip7sCpKZmUe_L5d1mmeLLf86Yt3J5CNePd1lYpbUFg_1MO15jhSIgJajIR5_1r8mYeIjdHBRm4o3kQEmNCo1Kd-lpTpsIorDl3s1BzaF9JLpAUMTddICsl-ge03tdxHy6cpvru0jkcxDCO7x3WV6qG5DQ8kS3LkZ3hcSD0V3z2GpLgRe-rrTSxFuLvzLG4_JyqvFdBG6NYa_YITv1w076z-t3X-fbQ7Wfjr0_w_PU1nU8P53rdUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=RZjMEJCz2JojqW7T1D-7pYiH4getjHxvAv2itND65usCVV1mujvGjI1flVbs3CX7aLm6KdAYzSc4ayjH7yM28Y2uKgyYmHUvLc6aFC3ehJccxKGPnkhAjcFFxxNJm5N8zFQiJKG1L9ecHtkdm2uLgaYPcLk3m6MBq8pGs1ewAd9yiKonvk_EgxwqZPAAySYf3lqHH1zhs_nQbGo33PfFoG49Iv-zC4M5emG6GLW2kGKOkPhxcJsQH1XhlzItbjtxh_3syCUMqZlPaelMaujQkCCkEZZzbC17T9L_62tAiCcXDrErGB9U9LKUoQgaIUokVEZAshvaziZ1md3MW1MDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=RZjMEJCz2JojqW7T1D-7pYiH4getjHxvAv2itND65usCVV1mujvGjI1flVbs3CX7aLm6KdAYzSc4ayjH7yM28Y2uKgyYmHUvLc6aFC3ehJccxKGPnkhAjcFFxxNJm5N8zFQiJKG1L9ecHtkdm2uLgaYPcLk3m6MBq8pGs1ewAd9yiKonvk_EgxwqZPAAySYf3lqHH1zhs_nQbGo33PfFoG49Iv-zC4M5emG6GLW2kGKOkPhxcJsQH1XhlzItbjtxh_3syCUMqZlPaelMaujQkCCkEZZzbC17T9L_62tAiCcXDrErGB9U9LKUoQgaIUokVEZAshvaziZ1md3MW1MDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=TVJRojnAj5wO_5XnECAvqk9wzOwdtLNn8qy1ZCFnTHy7Kg3Mw6hMBl27CdIlta4C7BDgIV6L_ELFqNSrTNIgvXBr3J1RneaSxmtJbfovJ5bVwok_wrH0uwX3WRdT2WoDs4jf8-zWIpsWGEul7qKCma1Ey2-eYBRpC78TTbZoMH601dAur66KXwi1MsbJCq5RMPCBwcgCQEaSmWMeZnSmvyIw3Vk-LKPzhiMkPJKoSYsWJfddKGfuHs9tI0i740qtS-wbWriizobBR3klkDS95SzPzFn4GbNOHNQAznLmNPP0Hu4qWjFeFbBD9lw0RQbYMk39jl9hb8oYrtZaX63HPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=TVJRojnAj5wO_5XnECAvqk9wzOwdtLNn8qy1ZCFnTHy7Kg3Mw6hMBl27CdIlta4C7BDgIV6L_ELFqNSrTNIgvXBr3J1RneaSxmtJbfovJ5bVwok_wrH0uwX3WRdT2WoDs4jf8-zWIpsWGEul7qKCma1Ey2-eYBRpC78TTbZoMH601dAur66KXwi1MsbJCq5RMPCBwcgCQEaSmWMeZnSmvyIw3Vk-LKPzhiMkPJKoSYsWJfddKGfuHs9tI0i740qtS-wbWriizobBR3klkDS95SzPzFn4GbNOHNQAznLmNPP0Hu4qWjFeFbBD9lw0RQbYMk39jl9hb8oYrtZaX63HPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8kp4bjeUF0zsV5Ia0vIVCs1I6WO-NIpzUx_nEqvbxN0Ff3j4TWI8u9OxT4NQEJka6qkX0LNG7V-uVwaOyhn2jF2mykFom1iKVlWUZXANl9VDNyIZ31BkV3TDNRXlECEmIsfar0JesdxfXtuBzBTfBEWU5ed8FLCE6LJy9avAyqGuuVK92Zl4Yit84WwSBffuzVQgPKRdsmkEMiiQAqGamsYZXN02ztDWA6E-Srtdtnp6WU5U3lTAOPF6FAuz5GbuuqUxh-XJUMohwzk3aSCzZwQHo5KoAiUoHTQ66J9padQwnD4l4tu-gzxLb7uqJSC6sNM7gaj_I-VbG2xTM0zXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WicxAaqXNTY-EkEgclpjCwOaC3G7B1WW3M8yTfXh0Ttphh5cLdzyw8yrwlmkhMWnkNXvm2fuigamrGupXx69A6S87Dm1stqIZv4BhXba9sCHDoyZXyX36gJuEKfARjybrPszpGMJM7g8lc_7a0b23bXTGRMnz-z-neN7WSztKKdJ7nKSBtjK0NnwAUnuMnJkOr48SW34M7FvdxHxyUNQFjEH8aV18XColnWIxDcLXQ_WxwqKb1d8kFRBCmzHQlM7kTZnzbeD-ZllVD243d_khMVAIRdvLMRCAgl43KFOENw3clhTTZMddzy-bUBlE67_kIsw4pD9v-Sqad_5QFzoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=n7Zk_R74YU9iEMFUFjgchrM6XXZ5B8egIWx_jTccD1k_pwxZf0-4ogSLKEKnaLMJTj6ncz5lH7vkYa2Kq99t4TtNv7cu27k43c-u_r4XGZOAHiNjNz5QNxOuXRhBgjGW9fI5GIpYjVM32Q_QX2vbkkTeVW2xlk2LliR_DYU5N-P75KH9y_NoJE-xHtI3C2XWtFOjelEK-L-p_19-DwVwBA4Jpo8bVzJSyDN5ia0_FSqzQdRtcz6yYPJEenAZedwT5IirYXtwyN_jcaAgAFoIt6npkm5QAcQdwPprIypjhwSur8Vy2Svr5kSFr30jz98YHBg_ehT1N3z_2KM3ucmRzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=n7Zk_R74YU9iEMFUFjgchrM6XXZ5B8egIWx_jTccD1k_pwxZf0-4ogSLKEKnaLMJTj6ncz5lH7vkYa2Kq99t4TtNv7cu27k43c-u_r4XGZOAHiNjNz5QNxOuXRhBgjGW9fI5GIpYjVM32Q_QX2vbkkTeVW2xlk2LliR_DYU5N-P75KH9y_NoJE-xHtI3C2XWtFOjelEK-L-p_19-DwVwBA4Jpo8bVzJSyDN5ia0_FSqzQdRtcz6yYPJEenAZedwT5IirYXtwyN_jcaAgAFoIt6npkm5QAcQdwPprIypjhwSur8Vy2Svr5kSFr30jz98YHBg_ehT1N3z_2KM3ucmRzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
اینترنشنال:
⁉️
🇺🇸
🇮🇱
از شهروندان پرسیدیم پاسخ شما به پرسش ترامپ درباره زمان قیام مردم ایران چیست؟
یک شهروند با ارسال پیام صوتی به ایران‌اینترنشنال خطاب به دونالد ترامپ می‌گوید: «چه تضمینی وجود دارد که ما بیرون بیاییم و تو بعدش مذاکره نکنی؟ ترامپ، کار را به نتانیاهو بسپار که او بلد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=M1YFtlvegtipylG83i9QHpshHCDvdkPcsyYggJeguTCRV0xut4tpO6cNpY-B_75a3zmqSmT2MmnBT2GtyVKn7aqsAJED9l8gnP1FuaZu2ESUnAtNL3JLFWDQDek_J493uKepmfZwrJX4ncXy_D3QflJNC0QTY5bJxxirvbpN0xQQcEYyLTz1rEWz2xDPRDEAKgHHcsYJjHARUAJbjLGIIAdI7JYBaJfMxj5IS2NU9zSYgqwQbIYuhrju_XtWeQ4SWt8CaL5L5aWNR8fLB1dVQ4fh_sUIHUr9aVoGW33pHAqLWnKFwMKDEGuPfAXqOM95tZ3NTbGpeI79nIrk_Og4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=M1YFtlvegtipylG83i9QHpshHCDvdkPcsyYggJeguTCRV0xut4tpO6cNpY-B_75a3zmqSmT2MmnBT2GtyVKn7aqsAJED9l8gnP1FuaZu2ESUnAtNL3JLFWDQDek_J493uKepmfZwrJX4ncXy_D3QflJNC0QTY5bJxxirvbpN0xQQcEYyLTz1rEWz2xDPRDEAKgHHcsYJjHARUAJbjLGIIAdI7JYBaJfMxj5IS2NU9zSYgqwQbIYuhrju_XtWeQ4SWt8CaL5L5aWNR8fLB1dVQ4fh_sUIHUr9aVoGW33pHAqLWnKFwMKDEGuPfAXqOM95tZ3NTbGpeI79nIrk_Og4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=lzx7Lp8i5ofRG25bgBSTtJiF0Eo5RQKpw4sqFvUd-7PY7TqTEfVoWWw5KnI-JXhJ7BlzYKxSm74sxtQJygNLBrnlMBydwXd0vV8J9W-YlJBaCYd2jy2-whMOnHCXVaH9XuI4Zbty-fsIaF3xZoiwa55kyjj1fhzX6ufg7YtR6h60DzJJ-rsiVsg_aPwq5y4FMR0isSt3Zodzof1k-6Ush8ZiPGXXyQRejCR4HHj5DZfTcKFtDX8UNzPdkIU3WRYUA4gXyNSxsioy2WtuiP1uVHm0lYuHfRCZPztIkz1XzXtg4J65uHlisIeXqcaTESbjqrWDUT_i51a4UyKUMlxH7D9K9EYiYzze8Za2bFGp3vXqwWp5Pqn3hrScLSdKeyj_1s4CfSra3eujGy3FfIAN5iLxy3Pc1Tl5Ul0-pVLgV4-4TomdhRK7mmI-1UTw_SCEDUkyqj_ROrw5eASaZ4y3xQ7_wlrQvaQEgSkzmQqWE3do2QbB9pUI7_6v3C5f0fhzHIVl7g0pNF83O5Hv5-K0w_ENKa00uFdDFDKMBXcFScrHv10qdK6dQ7UjcfuPCe5fh7_SXDxl5Uzvh71gPTzt3ucmppWq71dAJCAHuI_l33WhRFU_tAiiq4zGB7quPbbw0rszUxKhBZ_UQ87oMQeTqakafpY7mlI6DLPXgbxIGUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=lzx7Lp8i5ofRG25bgBSTtJiF0Eo5RQKpw4sqFvUd-7PY7TqTEfVoWWw5KnI-JXhJ7BlzYKxSm74sxtQJygNLBrnlMBydwXd0vV8J9W-YlJBaCYd2jy2-whMOnHCXVaH9XuI4Zbty-fsIaF3xZoiwa55kyjj1fhzX6ufg7YtR6h60DzJJ-rsiVsg_aPwq5y4FMR0isSt3Zodzof1k-6Ush8ZiPGXXyQRejCR4HHj5DZfTcKFtDX8UNzPdkIU3WRYUA4gXyNSxsioy2WtuiP1uVHm0lYuHfRCZPztIkz1XzXtg4J65uHlisIeXqcaTESbjqrWDUT_i51a4UyKUMlxH7D9K9EYiYzze8Za2bFGp3vXqwWp5Pqn3hrScLSdKeyj_1s4CfSra3eujGy3FfIAN5iLxy3Pc1Tl5Ul0-pVLgV4-4TomdhRK7mmI-1UTw_SCEDUkyqj_ROrw5eASaZ4y3xQ7_wlrQvaQEgSkzmQqWE3do2QbB9pUI7_6v3C5f0fhzHIVl7g0pNF83O5Hv5-K0w_ENKa00uFdDFDKMBXcFScrHv10qdK6dQ7UjcfuPCe5fh7_SXDxl5Uzvh71gPTzt3ucmppWq71dAJCAHuI_l33WhRFU_tAiiq4zGB7quPbbw0rszUxKhBZ_UQ87oMQeTqakafpY7mlI6DLPXgbxIGUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=ge13axpbD29N7ShSSnfOEEcuyWkucHEAOmAlDanza3u00YSoXZs-lzvEM5UIFzZjxBTx1iYV2AXeEDub6MMhlye1P5jkWzJocSOjw3xCHCt0mBcXJjGUKbeockSXAedxymJo1gm-P2721KbojmFmLeg63JYogoNDBOXZOV6KcmYGZ5K6puNUhIwNqTLSnclljB6oh4gJWGciQJjmUQKPQ3JgGGucApVablFEOXowI14Zms2AfewMCWab_GtZ25uVRKaXXCZoBPwUSsb7rWzab5Z6VlVrieLEKEYSuMpb1QIfrIV9lW9O2fvtx6-qJ4Hzv1OXJBlnd3W0f150AOu-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=ge13axpbD29N7ShSSnfOEEcuyWkucHEAOmAlDanza3u00YSoXZs-lzvEM5UIFzZjxBTx1iYV2AXeEDub6MMhlye1P5jkWzJocSOjw3xCHCt0mBcXJjGUKbeockSXAedxymJo1gm-P2721KbojmFmLeg63JYogoNDBOXZOV6KcmYGZ5K6puNUhIwNqTLSnclljB6oh4gJWGciQJjmUQKPQ3JgGGucApVablFEOXowI14Zms2AfewMCWab_GtZ25uVRKaXXCZoBPwUSsb7rWzab5Z6VlVrieLEKEYSuMpb1QIfrIV9lW9O2fvtx6-qJ4Hzv1OXJBlnd3W0f150AOu-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=uv1DB6xBbVwIakwLVdQ4nZ9ssEmESqhfa6lpklH3OSgZzFB1YxmpZZJE8p0VtnpHMvG5jHEiW4EID2frrQt6DrEw3t9jSQiGpwv_Gy1st6pbC_GsvlhRphvJcarV1r_F0iDaknL-hs57-uA-LX44t6gA2EZI5kq5Le-IQuWqQGU8DELGmXWdOs_2aQ85MnBr45LQQNU1OfxqqRT0Togmrz9AT94-_D7jvRZa7i7yOKqsjhlHFDVF_SbFX7g31fUjf4sfEDEskvQA9En5pTAQaYibJkk-Kwj5SAFPFflxjfnAtlF2huGYY6oK1SoXcS5Op6vfSSdu1m99L1ETflndjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=uv1DB6xBbVwIakwLVdQ4nZ9ssEmESqhfa6lpklH3OSgZzFB1YxmpZZJE8p0VtnpHMvG5jHEiW4EID2frrQt6DrEw3t9jSQiGpwv_Gy1st6pbC_GsvlhRphvJcarV1r_F0iDaknL-hs57-uA-LX44t6gA2EZI5kq5Le-IQuWqQGU8DELGmXWdOs_2aQ85MnBr45LQQNU1OfxqqRT0Togmrz9AT94-_D7jvRZa7i7yOKqsjhlHFDVF_SbFX7g31fUjf4sfEDEskvQA9En5pTAQaYibJkk-Kwj5SAFPFflxjfnAtlF2huGYY6oK1SoXcS5Op6vfSSdu1m99L1ETflndjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcFUN7YKD6yVwVtOMJ22MF5fYbGtcQXXKYbD5qhAAAfV0FXJ0GCFRBnpafGYvpDOag1VKIVR0-YqX19t1RsHgtxHaI7R3dU4xDRutuLqLwKIQi4JzdekPc1q67N1xSPstZDnVcytOOkEI2F_QqPm7JlkSWWNxJ2q5M6SD5ckdiRrMd55lBzwnkE21qJ5F0f0WzAuaGx7K6isVSRLVhXnnCW98H-_Rr5NKqJo8kddoxsMF1xJvxAp4Jag5ON7u-uZutpyrpU_ANdqAyDwCo5ynxUjdJRzwejOEYV2DVDmWFpjtmWe5b5chaKZ7KOENpOKV2IW2qo0e_9O7o3VshNT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqt2X-v4QV3z3uq0j2VIC0EwVKd0cG3UvghSvnaJ3XItPuOAi5idLImmcpTxLBfcz9VQ98QJssGPTBYBV6JxJA3Dpmf682j_R57e7_SQWT6_16gcMgsNPcPadx2todzYzKMpt7fguY7wMNKCgY5xPC82PPBexRVTU9oxnDKQItIMPCPe7xBaOD0AzmEulXI54hbtVOn9qnRc9DBAd383I18Hj5dsucKohYID6NVHJTD5FgZUV4SGnxMlFkS-rEpLBAT-siFE40tOiwkYIN6S8bSsgr60dtx-o0ZHeWts01JGYNqfzeO6C9iuQv_H_dzrMjchivbrdMywAs0biZ8m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
پوتین خطاب به پزشکیان:
تو این شرایط سخت، داریم سعی می‌کنیم هر کمکی که لازم دارید، بهتون برسونیم
.
قبلاً هم دربارش با هم صحبت کردیم و داریم کالاها و اقلام موردنیازتون رو تأمین می‌کنیم.
با وجود شرایط نظامی و سیاسی فعلی، همکاری‌های تجاری و اقتصادی‌مون رو با همون روند و قدرت سال گذشته ادامه می‌دیم.
همون‌طور که بارها گفتم، ما تو روسیه کنار مردم ایران هستیم و باهاشون اعلام همبستگی می‌کنیم. شجاعت و مقاومت شما واسه دفاع از منافع ملی‌تون واقعاً قابل تحسینه.
لطفاً سلام من و حمایت صمیمانه‌ام رو هم به رهبر جمهوری اسلامی، مجتبی خامنه‌ای برسونید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=YAbz3HkcVcIPBFXRtegc-7zwvn3bOopzbXssA4Xx0VL2mPWyQ4QsqjSVF1BuJpvOun5HAjQ3tzkaZBzr98pweV_-ef3jQvDbDiO4TNnROBRah3KYdS2PfK2o9g4A6lSGFYKTsbNZ7n5Lp3z9KcAHQLbhmTSnyAfoy-kjuooF34aAKadSDcyK2EW68dgHVi1TNiscfngAnivsa0h6yJyKgTAbOAHD8QCuS1SidZJ9OPPjDh0SAAuvBBL0TarpoPVFgnhTHAz97BQi1FXa107AJY6B6WBanPvAwrdHOq_NlheKE9DXWvw84Etv3VkcyYy-6Lcz5SKs4Dbf9tpsYX62dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=YAbz3HkcVcIPBFXRtegc-7zwvn3bOopzbXssA4Xx0VL2mPWyQ4QsqjSVF1BuJpvOun5HAjQ3tzkaZBzr98pweV_-ef3jQvDbDiO4TNnROBRah3KYdS2PfK2o9g4A6lSGFYKTsbNZ7n5Lp3z9KcAHQLbhmTSnyAfoy-kjuooF34aAKadSDcyK2EW68dgHVi1TNiscfngAnivsa0h6yJyKgTAbOAHD8QCuS1SidZJ9OPPjDh0SAAuvBBL0TarpoPVFgnhTHAz97BQi1FXa107AJY6B6WBanPvAwrdHOq_NlheKE9DXWvw84Etv3VkcyYy-6Lcz5SKs4Dbf9tpsYX62dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=d35grFsfeVMOa6RKAYPdsrqN2tkv7AMmGEAWWBcKkAac44Xm1PJZjo6V9b9k6Jim6hB_9gB0ZidB9S6_56V8cKyUhOTqqeuazS0NUW53ymkghV27xtUl0b8LpjsENvw_JxZG9W2l-XOJFfyaGeK84yH45q01UEmunXRQbgaR5FajD57mh9JWf2olMR4ie5mdI0seI1MOuMCwMGRWbF_RLSevAP5iD97kT-dNq2o5wc2VW0zmzPha740q-AaZeIrmH9G1lqxjvIJiGl4BLRC_Ab24ZaOpILmKK-uJSLPbsEYQA9JKnKFaNC1GPh4IiuFHF_4sSYMrVP8KgyqxyeYQ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=d35grFsfeVMOa6RKAYPdsrqN2tkv7AMmGEAWWBcKkAac44Xm1PJZjo6V9b9k6Jim6hB_9gB0ZidB9S6_56V8cKyUhOTqqeuazS0NUW53ymkghV27xtUl0b8LpjsENvw_JxZG9W2l-XOJFfyaGeK84yH45q01UEmunXRQbgaR5FajD57mh9JWf2olMR4ie5mdI0seI1MOuMCwMGRWbF_RLSevAP5iD97kT-dNq2o5wc2VW0zmzPha740q-AaZeIrmH9G1lqxjvIJiGl4BLRC_Ab24ZaOpILmKK-uJSLPbsEYQA9JKnKFaNC1GPh4IiuFHF_4sSYMrVP8KgyqxyeYQ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0_TbRrE_WbbIRsAd5cDYdt1HZh6FBd3QBJsYkZasQFuDyF05g0ZL_YnABVoeTHn9QXnAt9G-Nm4uVIB5Dectfd2q6ACviCAOCuXEALeL7X7fOFhGf-A0qE6GQJx3GqA2wY7t-McPqPKklXn2VgRBcjpTStuQqg1VYy2fZEnKZ-_EAvWl91vz16QX-XcGYDt5ub1G3izSWWOdIBA5Ye9xuA8Z8HCLXVXw5rqxN5uHTKawdaOgaB-7WwknuPU5CV6j57k-2fTRVbnVsR_toEMXMlxGbvLVshGo3CXspnQz_Kc4QpRiaWqd8ckJ1-BIlxO4ChSn6zGAJJWb-PGGZOmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=iLpRTRdb7jw8FTRWjJgJgVTcpsIqTqOeQfcO2f4zGyNVCdGamSdUuhjR5FsqAkGoefs3CNySVq-65LVNjgcX3__Kfmg4wn-b5XxV1AOlv5Qby9fuCSCpH9dPjcSnuxVN6AZEs-148xZF1TRV75c0fZlXsTg1jFT4-Q4_ThHAxws2khTmD9CZ_WrYcQ3rg1vyvOiog_9408qPVVZlh2EIxqv6Ac1x9MQM90Xib0toJQ_fREyBSTT0GZNQrZ7cQKxyaNocNW0UNJIFQ-J4xe6m03FjxNUKi7hHxdkUw_S7B5evYVoCa5BpeIyvCwSB0SrJkXHtHvzBOO5bqfgv3XFt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=iLpRTRdb7jw8FTRWjJgJgVTcpsIqTqOeQfcO2f4zGyNVCdGamSdUuhjR5FsqAkGoefs3CNySVq-65LVNjgcX3__Kfmg4wn-b5XxV1AOlv5Qby9fuCSCpH9dPjcSnuxVN6AZEs-148xZF1TRV75c0fZlXsTg1jFT4-Q4_ThHAxws2khTmD9CZ_WrYcQ3rg1vyvOiog_9408qPVVZlh2EIxqv6Ac1x9MQM90Xib0toJQ_fREyBSTT0GZNQrZ7cQKxyaNocNW0UNJIFQ-J4xe6m03FjxNUKi7hHxdkUw_S7B5evYVoCa5BpeIyvCwSB0SrJkXHtHvzBOO5bqfgv3XFt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇨🇳
⭕️
حسین مرعشی دبیرکل حزب کارگزاران:
🍆
چین سفر قالیباف به چین (و گسترش روابط تهران-پکن) را مشروط به موارد زیر کرده است:
۱- باز کردن تنگه توسط ایران
۲- دریافت نکردن هیچ‌گونه عوارضی
۳- پایان دادن به اختلافات خود با عربستان
۴- پایان دادن به اختلافات خود با آمریکا!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtky5z1WrJU09CkmnFZBrwM3AmN17EIkDdRr0wDPODMh3hhHmFyHAWGKtQBdUd86GS_4iLuSwzQzcrTbyRB5RkJ8bJlIetc5N0j5dtthrl_p61hQUVVIB5xUg1CUHdDIbpkXFF-qJc9vIBLmpGcrC5VzZJgmNJL-ot29rR2lDQLGtNwNEWOBvyCko4I2mIoGf23rj4lCJ46fIe9HiM7lbyk-bCArLQjHBv8TuoIl9_fLY0L_hhRqTctKKpTKjHx5_XT9HrV_Jpe7BGxpQPOe4ZOfLo4umd_1vaiW3f0NWs8eiSbzovNNQ35m_Uea_wSSYWQQ6HQHoOuv5GHhlqtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=nLC-kWYNcJCoVUt4AmqBz2poCJ9l9mwNYwXTJkE04VyqshK2gigQIzbtmh8OkPr6rNlXElxl-GzrAPQAllkNi1zhotH2R4mho1jAPyQOcR-XIGmN4Eacmp55gVqe1Z5YaxZLie8X2FopXttGHp3lNtc2eHErbqvjNCj3Pg_BtDepIlR08O9TQOct_WiVuJYG_jvdh35xYntTrY3Tx3W-4HGerXEtqao_5fTL7eCBjweD30skv9T7QZSGkjPKKqCqTDLMZngFKk-aAVwbenACAlbzv8S4LX-BFttjNygZZSdgqoz2qnGfmmPa0tnFsgEJKAToWc04SlqUHuuXEoqfaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=nLC-kWYNcJCoVUt4AmqBz2poCJ9l9mwNYwXTJkE04VyqshK2gigQIzbtmh8OkPr6rNlXElxl-GzrAPQAllkNi1zhotH2R4mho1jAPyQOcR-XIGmN4Eacmp55gVqe1Z5YaxZLie8X2FopXttGHp3lNtc2eHErbqvjNCj3Pg_BtDepIlR08O9TQOct_WiVuJYG_jvdh35xYntTrY3Tx3W-4HGerXEtqao_5fTL7eCBjweD30skv9T7QZSGkjPKKqCqTDLMZngFKk-aAVwbenACAlbzv8S4LX-BFttjNygZZSdgqoz2qnGfmmPa0tnFsgEJKAToWc04SlqUHuuXEoqfaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عطریانفر، عضو شورای اطلاع‌رسانی دولت:
پزشکیان اول توسط شورای نگهبان برای شرکت تو انتخابات ریاست‌جمهوری رد صلاحیت شد ولی شخص علی خامنه‌ای صلاحیتش رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EodhnD-DGysUWNu2JKgxJWhQxt7Sf62drKC01s0yYQa-enQexTcKwDWR6siEd7g7qVaoFnyHa6UrdpQaIWM2fFqb8aJG08Nz1V4FjMF9qS875vDPe3Y-woHiIphLzFaO3wkpyX0qQDoRTj5W7LpoflNdprl8zJIsmfzE0Jv6jpNhKEQU08DhFR-gBUN8MCwSC7X8LEON9Ejih8qCVPBcBk6lx25GJnE-AD-e3UTDkMICTN8IZ-R5NwCEmMmmjELtFdQmAXHHlJkmumYHGiMD8Goc0w4FxzEEFAMQkWOPXS6JsdoVBXXuQSJCjMfQN593YZEhdomy_LWwSzkCy98jWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF_FM40xtk5Dtk7ZvGeij9g-WDI-v1l8iXlutOAg2Jqs1jmLCuWj_JKTzzQEJiXGuzZTXeJlSgd22F-SrLgaTTuUIDCfgSJbb0iuirb4SkIZalhsTqM8vjPFjezgHojKcrAMuv1U4OgPVJqq--R2BjHmiuvwDk8DkZp32zTt7jh2WKXL36_pSsWswQAyoDaaEriOf3tjzrH8R5I4bess2EQivF-cHdRVFVMHIfCAVftFl3a01FeuNVDr5zXKznX8V-b3WCqhtXDk00qLqL6Xa9rFYrtpJdawujz5FYRjS_02Kq_l-1YpYabJX64qpaB12w0z8qr2rYd4arxJ9tnagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
سایت جهانی
TrexBet
می‌برتت وسط
جنگ
بزرگ!
⚽️
استقلال
🆚
پرسپولیس
⚽️
اینجا فقط فوتبال نیست… دربی‌ـه!
۹۰ دقیقه جنگ، کری‌خونی و هیجان تا آخرین سوت!
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8ZHKXX3wORXXs4FC5WKnnM6cH5nwBgwlVLosAk933YKfQ_4wYYOJYr49OkcatItMWjEXk_67rU0WiXBwPGVcEoZ7aL_keGC2Mf1f4uAE4G7nrFMq-GoCSWxW3-WhrisqZzQct0ioCztAUckfV_LdOpbb9fleUt8-dveIcimX_8j-x7EhRveTtY5SrDDFJXbJfJP-efgm-yzKG_pzOvwMMFqX7bIx26hIgvsGBuwFeMlR-KVz44uLSVtkcnJjP9snEf_YaFrmeRAAlLzGWkE9MC7AYzReSs9NpJUc_2IYhrT69eDwAT8F29lg9wPAoLEH_B2U8NFCNdIfbElIWSADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiJlWaj-c_PPN9JSJevyuItRP2VDpMosZBng2RZ7SEs2V7EThsGVRH4w7kv6eilwl7DsuoEoUNZcp-Gjd3mwCnEw1ujEthWcWimP4SaGt8fJs1bYGc5ZN-W0G65wwgoDxqnmUOSygNe65iTWfot6AVFZq7tJU_C4nu-BRqorbTO0kJB0-ur1owVOjwahdFAIzN5CBsm_qKRN8durMNGLlX0hNi-ywR4KHjHmW4YdBbX63ID1tXldO52a-xIxaS8F9gbeZAKzA99pinrrQz4ITl0dsESm_ar2IHtmF-cg2PJNfbFBRnkSjy7PRZjOObd1iT3ggH-VVuNLAxREQw0-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=ViUczCcA9EGzuurd9ybnG3DwJ7mrOYhyc4omP3gjIylRaoDG97YW7aqOWhUmvrxLbc1nhUm4aWP5wigaWEM_q0Pk_aH6KG3suapc4fwNSCqqJ7xW3l2FkgxrdNdKUAn3bVzCUnY0ugWL72TXUc3HBwHSxbyGywpMvBKBUFOaMr8cRe5_eU9jw1tVAnIujRuA9U-xqlUEXnsOaaeY6Jaq7btzbbXyzPQadzLR5dEACgppo36Qqzasupz6_No2C9RmIlwJ_t6HX0S2_yx1WzwFRv7g9YHhxQKE7SugBAnol0_V0TlZY-_-X7_SX5oRkcDVNX143oB3HZLc9GXUbgrSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=ViUczCcA9EGzuurd9ybnG3DwJ7mrOYhyc4omP3gjIylRaoDG97YW7aqOWhUmvrxLbc1nhUm4aWP5wigaWEM_q0Pk_aH6KG3suapc4fwNSCqqJ7xW3l2FkgxrdNdKUAn3bVzCUnY0ugWL72TXUc3HBwHSxbyGywpMvBKBUFOaMr8cRe5_eU9jw1tVAnIujRuA9U-xqlUEXnsOaaeY6Jaq7btzbbXyzPQadzLR5dEACgppo36Qqzasupz6_No2C9RmIlwJ_t6HX0S2_yx1WzwFRv7g9YHhxQKE7SugBAnol0_V0TlZY-_-X7_SX5oRkcDVNX143oB3HZLc9GXUbgrSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70966">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvPK03hqCNKfYP-64NyzB9TWhDeHY2WFVIuwwJlhE9LzQwPfTSZK-8gv-hw0wj62hXj5QKKUo1-HXK8X1RvRqyReHTFZIMOat6IaGaCs607iNMqNkHIGWiTzeeR_jD5xkLk-jsVLoqdRuj7CTymjE5ax7ffhdXPhGc8AZY5dcEuzM5G7Quc4igwP2d_snjodrpltFMCMya5go7cfawebE4F2uDj3pd6nlJGPaR2q-OuFDQOJvNlfFIexL7UMd_grNWu8BWHWV31GomFSPBCBvORBTxzlxMPpgiToL9-kyUsv1aWch_5oV3vDZjpX1PtWbIX03LvVEomUW-rebHsG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه امشب یه خبر بد هم داریم، در طی حملات آمریکا تو بندر کوهستک حوالی سیریک، ترکش حملات می‌خوره تو یه مراسم عروسی و چهارنفر جونشون رو از دست می‌دن
🖤
#hjAly‌
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70966" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70965">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5sbLrh2S9YEo6puEPW2FHUrF-XY4wIpSVZCIH8Q0JKTBdB7_56VsCUaQhQ6z7eXXE7vdEREqP-0QXNpKkFmX3hyCA9SUnzVsQ590kDaWq79-ICuD07eUdTg-ZjmA_RaFHFc8fVLwEPZTzxQoVFkKkN9wJCgsZNISSF4xHGKuFzKCk40mtaHH1TIu-AiP2Z2WAtQfE1bwL_4w0f4vNlz_eiUsi9OFDWcIfuU5ClbuvXCYk7kVmXjD63V3TOj7_jTy3eiKhLjZlLXB1_3zVjVis4GYAT8ezNWzUGlihnI7XO23fu-Ls572Uaqs5XyyOqYMqda7pMFbJUSHkY5RTKdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70965" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70962">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=NEmCw1EqkG7u-R-CMvlSeIXj4g8Hi7WYycJCbINMANdZrhI28yAlG3445iHZVQbNYzB-Hxnz8tdRy-XsAmj1fPKVtGoxOQMoUsidttLbonoDH-Lw90dozRgz1NaMvh4FGx9pGfgv3zhJwzvj1QfPK-l2pvllYf3C46__vYat0EPXaTk__G4fnVM2YmZipJScNJqFx3AngiqXXm0x3BIJg9kNG4c27mSMQXqLCBuD9zmw2QUfaxbCnj0TznelkiqCBIz8YgOfjaGHkeYYN0CMwCn-VQjEQzgdQgmb4UDAnjTQ3ucAGCBi0MXlt4S1L9-EooZ6yDP21l8tRLEkaAxpCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=NEmCw1EqkG7u-R-CMvlSeIXj4g8Hi7WYycJCbINMANdZrhI28yAlG3445iHZVQbNYzB-Hxnz8tdRy-XsAmj1fPKVtGoxOQMoUsidttLbonoDH-Lw90dozRgz1NaMvh4FGx9pGfgv3zhJwzvj1QfPK-l2pvllYf3C46__vYat0EPXaTk__G4fnVM2YmZipJScNJqFx3AngiqXXm0x3BIJg9kNG4c27mSMQXqLCBuD9zmw2QUfaxbCnj0TznelkiqCBIz8YgOfjaGHkeYYN0CMwCn-VQjEQzgdQgmb4UDAnjTQ3ucAGCBi0MXlt4S1L9-EooZ6yDP21l8tRLEkaAxpCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تو وکیل آباد مشهد یه ماشین به تجمعات زده ٢٠ نفر کشته و زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/70962" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IheemEU9hD3xHqqE4kS1y_DwGGmsNOrsqyKCLDoAzbUUSLHgAXpUZpyzq7xQTFa_2CPCNk2pk0v1Q4F9kvcWH5PH9N6eklrcqQ1uxyL6ss2QFQNwTBR-1nyKMt9Md13rQ2trxCnW9sEyVTTwOV_IkcYNPKgbvxNk_wriecVVpx1dqTprNFB4E1Z0QMXleh-7v2O2GjtxmrHLRQzokX-Biad8kbzpeHDpHtVHJ_5F2w5a6PZ0dyNiKDcMxg7MvKDxz6h_oGMFq4iE15Rcf3iK_N-hTb5rLdoVc68SUVjCrssPTn_UTiOHpBmiLmL5P-Vj9RBRshNGnsFjs8yLhjGKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=JsFSPkmu81aqBdoH5cnH6olURY0awFSmwNCteNLNEQUQA-EzSfCIFMKhyXeaY5tWo7njjylvVVBOBLy044h6FU0yhw7gdUaPPQ91AEJwt69JrLpXy8vg6Q4G0WjoPIalYVbgSOotOBwI8GLIYXZlFw2UgZphpzwi6bAKSbcMm77RE0JrmeKS4YrJoqaBCFTndQx_QAnu8kpPOiVWUDyykOfItq2iXRAHJz19BduZtnWwthxBOcNbOs_ET43PFNYnxTxJYSB9b6bLqoyBsgF2VC1TXXw3BJ4ijwXOF5dXMNwfwvwSIgVnh79gJF-1och3q-A2BrBNc0wrefWVQIFf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=JsFSPkmu81aqBdoH5cnH6olURY0awFSmwNCteNLNEQUQA-EzSfCIFMKhyXeaY5tWo7njjylvVVBOBLy044h6FU0yhw7gdUaPPQ91AEJwt69JrLpXy8vg6Q4G0WjoPIalYVbgSOotOBwI8GLIYXZlFw2UgZphpzwi6bAKSbcMm77RE0JrmeKS4YrJoqaBCFTndQx_QAnu8kpPOiVWUDyykOfItq2iXRAHJz19BduZtnWwthxBOcNbOs_ET43PFNYnxTxJYSB9b6bLqoyBsgF2VC1TXXw3BJ4ijwXOF5dXMNwfwvwSIgVnh79gJF-1och3q-A2BrBNc0wrefWVQIFf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به دکل سیریک که با پهپادهای انتحاری لوکاس(کپی شاهد) انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70960" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=CRWzw69EkpsaPyjp_Ay4TiayuIvvOD2xuQqielMMu9OxniwpVD_lM4siD2k3WB1g9BkWE9mcc2sNAlxm6Sp7fC01Qwdh3JAU7dvU8ZGV69ogh_ef-R3AcQ8m51rLHxfpB2wIni7EdB8n8_g9rHgMuWXkMBgTzGNCxmcEgWNFocTo3clfL1t0c5Engf84Ji5IS4Sz28fc9yjt64U9FnvJFqPcQo2inzLD-8xSpKqPRc_dONVko_c0f9CSJjqJdGHgwcUgY07NfRod-pc4vz7YIvV0XXFpInVAtJ-Dp0IqTfxA9J-QjRVWSnlLlw_zvf1WQT4TRBRGT5HI1EWkT-M9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=CRWzw69EkpsaPyjp_Ay4TiayuIvvOD2xuQqielMMu9OxniwpVD_lM4siD2k3WB1g9BkWE9mcc2sNAlxm6Sp7fC01Qwdh3JAU7dvU8ZGV69ogh_ef-R3AcQ8m51rLHxfpB2wIni7EdB8n8_g9rHgMuWXkMBgTzGNCxmcEgWNFocTo3clfL1t0c5Engf84Ji5IS4Sz28fc9yjt64U9FnvJFqPcQo2inzLD-8xSpKqPRc_dONVko_c0f9CSJjqJdGHgwcUgY07NfRod-pc4vz7YIvV0XXFpInVAtJ-Dp0IqTfxA9J-QjRVWSnlLlw_zvf1WQT4TRBRGT5HI1EWkT-M9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اصابت موشک های سپاه در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70959" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‼️
وضعیت دکل مخابراتی کوهستک سیریک که امشب بهش حمله شد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70958" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خود ترامپ، هگزت و بسنت هم پشماشون از این حجم از کله‌خری سپاهیا ریخته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70957" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
از بیدگنه هم دوتا موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/70956" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
شلیک دور جدید موشک های سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70955" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">من فکر نمی‌کنم ترامپ قبل انتخابات دست به حمله‌ی گسترده‌ای بزنه، سنا تو تصویب بودجه برای جنگ نقش اصلی رو داره نباید بیفته دست دموکرات ها
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70954" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=GLPo55mYflPFN2pUB-SAtUz3wHcMpPDlcu95p6VoH65WQyg46ePWYaFqaNBpXrqUeWxVRTK8YfS73GdVHGqk5a77r-DmbgCCAKYb7O1ltNSTYXSjkC_3qlUdud200q1MgTzWuVfWKjk7q-l4uZOyWKPBNPA6rCR44_1n-Aw6YE8Oc0dJP9YV6Wd8ew4hrhEq7novy64sgFIDs8YYkoD3ohh8ey4PZVeAG32bkn3MrJVSBrPpJnvcSpkow8BRyriWk-JoYwz1uf3TgNx9y7xnAtGMIqptKVIyb-j8QbYue_Gdj_lUVlUxfOhl8mWmPxS63L60Y2NFQ6NfKqRfjJ2r6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=GLPo55mYflPFN2pUB-SAtUz3wHcMpPDlcu95p6VoH65WQyg46ePWYaFqaNBpXrqUeWxVRTK8YfS73GdVHGqk5a77r-DmbgCCAKYb7O1ltNSTYXSjkC_3qlUdud200q1MgTzWuVfWKjk7q-l4uZOyWKPBNPA6rCR44_1n-Aw6YE8Oc0dJP9YV6Wd8ew4hrhEq7novy64sgFIDs8YYkoD3ohh8ey4PZVeAG32bkn3MrJVSBrPpJnvcSpkow8BRyriWk-JoYwz1uf3TgNx9y7xnAtGMIqptKVIyb-j8QbYue_Gdj_lUVlUxfOhl8mWmPxS63L60Y2NFQ6NfKqRfjJ2r6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم‌اکنون حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70953" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=r1SRGvlX5u4V7Sb9by1DXQXTtjw-XPJgLkU8qI7LP9ccz32nWXpT4rV7_NmptgpVvsIpfjOXGkmKu7yLFWVqOekE9D4Av7wja87GKVJ0qzynR4W-Oqxw-G-EnKQghPzEYeWMFbeYQahnVSSKriPb5HcVbnDhsLDfOZP7OsWHcu8YrMg16pPWdJgyNcwU1vYCpP1LJl1oOhmdAzrC9MmFHZIpSZbsyis3GKDtq0eP5UlIaMGImEo0NCjjFvOxyT-r7ftmwFTiqdJp-Y9JxhzwJCY8_oiqqWl2PNvmniNCioGychZcuvOiU-xgNGsMr6wbLl_6YDYYgD6Pj_H_bRl2Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=r1SRGvlX5u4V7Sb9by1DXQXTtjw-XPJgLkU8qI7LP9ccz32nWXpT4rV7_NmptgpVvsIpfjOXGkmKu7yLFWVqOekE9D4Av7wja87GKVJ0qzynR4W-Oqxw-G-EnKQghPzEYeWMFbeYQahnVSSKriPb5HcVbnDhsLDfOZP7OsWHcu8YrMg16pPWdJgyNcwU1vYCpP1LJl1oOhmdAzrC9MmFHZIpSZbsyis3GKDtq0eP5UlIaMGImEo0NCjjFvOxyT-r7ftmwFTiqdJp-Y9JxhzwJCY8_oiqqWl2PNvmniNCioGychZcuvOiU-xgNGsMr6wbLl_6YDYYgD6Pj_H_bRl2Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70952" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه های حکومت: آمریکا یه مراسم عروسی تو سیریک رو زده و چن نفر کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70951" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">همچنان هیچ ویدیویی از موشک های سپاه تو آسمون کشور های منطقه، منتشر نشده
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70950" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=IP-YFVdYCRnBhgsv4c7e9nm7dSOFztLJSDlCIJtMVOP3CooEGGYGQjBk8KMpEf_78ft6LssqNJQ7sUIv4Kp8mAyFZQxSFBSlI26MLns_UdhBH0UPBHeKWHRpWi5cUPyHb-bVjfNu_LYdTRrGJjlW7WtZaPfe3GwRf1IL-aWWr5xpggP0UzSMUMAV2cobeiE9dwxz_pXVSgBHT3PEC01NXxIhsOgI4XSgqwToi48Qebczkr5ypGk7vQjmdJe0N_kczMKRunCe-XL_89HrAClXWr8mkKLQuuvuD5UBvMdFfkwvEWKKWVCNZGmvwPDFUZ9DN89_8I8kOu4vUXnkBlf46w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=IP-YFVdYCRnBhgsv4c7e9nm7dSOFztLJSDlCIJtMVOP3CooEGGYGQjBk8KMpEf_78ft6LssqNJQ7sUIv4Kp8mAyFZQxSFBSlI26MLns_UdhBH0UPBHeKWHRpWi5cUPyHb-bVjfNu_LYdTRrGJjlW7WtZaPfe3GwRf1IL-aWWr5xpggP0UzSMUMAV2cobeiE9dwxz_pXVSgBHT3PEC01NXxIhsOgI4XSgqwToi48Qebczkr5ypGk7vQjmdJe0N_kczMKRunCe-XL_89HrAClXWr8mkKLQuuvuD5UBvMdFfkwvEWKKWVCNZGmvwPDFUZ9DN89_8I8kOu4vUXnkBlf46w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=oXJeisMtx3vQvg7pyJYHh0aOvr6oLhNkQynSKgTh7Ivo4poNWzcEyBh0j8kTEQUrp_2iCF_Xg8lmcjas4svugTy6OYnUOYp21_UgYSYBGksFsUcQDqOV_GcwmBrvqbykj8eSUiEAbwAj7ZFK48lMxOSytJpStoMl-5M3zYLvcaqociXMrZSwx1mFlCtaTGoAX7ccV8jko841w2DC1tVCvI0T5vKiqrQNI1YrbFFsz52jclVb2jXddIVO58vszBn4-3vHSDpYrdS4s0mtIxZzQ-gDfpA86NPFHbBlC4-tTjU_Cwi6mUto9JMkrJbV-AuANNB3eSzrSAc7qcQZlw_7Yy_eSMwyV3lKE9nxB8QktPL0-WECup_bElTk7jD4aKfAN-CfzCxEP3Nhapb4BsDqA5XvTMMb057EZKO6UEVjRPdhVIl_7c1buue2pTf6bWgZneAdSLv5dwRM1zWqveZWRjdk1HQWKdzscyGyJ-zTGiPsWgwvEaz3AfcokO0Yh75ZvZyWONpJDyjJ_diA01Rux2HYhdT9Ddqguhtf8nyQSmSL15d78oi8h6HpEtNbEm-FjKRm7aHOPwgK_pInCDQVd1OIUomDQoq4huOpeOrDIp6kgo-zATf8OaW5g_nmKeLd-cydBUB-pwr_RnM3YSNIPqRoWs4D4L4l1PgGBr9Bt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=oXJeisMtx3vQvg7pyJYHh0aOvr6oLhNkQynSKgTh7Ivo4poNWzcEyBh0j8kTEQUrp_2iCF_Xg8lmcjas4svugTy6OYnUOYp21_UgYSYBGksFsUcQDqOV_GcwmBrvqbykj8eSUiEAbwAj7ZFK48lMxOSytJpStoMl-5M3zYLvcaqociXMrZSwx1mFlCtaTGoAX7ccV8jko841w2DC1tVCvI0T5vKiqrQNI1YrbFFsz52jclVb2jXddIVO58vszBn4-3vHSDpYrdS4s0mtIxZzQ-gDfpA86NPFHbBlC4-tTjU_Cwi6mUto9JMkrJbV-AuANNB3eSzrSAc7qcQZlw_7Yy_eSMwyV3lKE9nxB8QktPL0-WECup_bElTk7jD4aKfAN-CfzCxEP3Nhapb4BsDqA5XvTMMb057EZKO6UEVjRPdhVIl_7c1buue2pTf6bWgZneAdSLv5dwRM1zWqveZWRjdk1HQWKdzscyGyJ-zTGiPsWgwvEaz3AfcokO0Yh75ZvZyWONpJDyjJ_diA01Rux2HYhdT9Ddqguhtf8nyQSmSL15d78oi8h6HpEtNbEm-FjKRm7aHOPwgK_pInCDQVd1OIUomDQoq4huOpeOrDIp6kgo-zATf8OaW5g_nmKeLd-cydBUB-pwr_RnM3YSNIPqRoWs4D4L4l1PgGBr9Bt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
"اگر آنها تلافی کنند، ضربه بسیار سخت‌تری خواهند خورد. و اگر دوباره این کار را انجام دهند، دیگر نخواهند بود."
"آنها متوقف نمی‌شوند. آنها دیوانه و احمق هستند."
"آنها سعی کردند رادار خود را بازسازی کنند زیرا نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و سپس به آن ضربه زدیم."
"من فکر می‌کنم توافق با آنها ارزش کاغذی را که روی آن نوشته شده است، ندارد. ما به آنها فرصت‌های زیادی دادیم."
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=pRxEDawiAP8LjCPc1qrPwyQnyGhYXvidv5YUTNYM8GeRQrzCvbFVi_Vo0MYWAOZ21aekWiNZ2XwHBDT_AHYjAVNxV6O1dEAm3awYPPe6WFruKwREcw49ZAGE6M3cCp4KiqQp6GzcOvcwT6L3_AWV6QqGKEqKM2NFe7eU1nI8QIjVnkoNujNt_bEFXUydnoZj51kRx37rYF3NLldVaIpyq4GEPoZfLwoAArgcx2RD7Oc6iqwM_Qqp90ZZJO6ijkp9AuFxh-vE6FJRo7tpKQBoQ6XOJpCcbsd61oxBn-9OjTeVp16MLz2ZlluFwL_zAY8VqGfOT4NqLJtfNSB1hsaO9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=pRxEDawiAP8LjCPc1qrPwyQnyGhYXvidv5YUTNYM8GeRQrzCvbFVi_Vo0MYWAOZ21aekWiNZ2XwHBDT_AHYjAVNxV6O1dEAm3awYPPe6WFruKwREcw49ZAGE6M3cCp4KiqQp6GzcOvcwT6L3_AWV6QqGKEqKM2NFe7eU1nI8QIjVnkoNujNt_bEFXUydnoZj51kRx37rYF3NLldVaIpyq4GEPoZfLwoAArgcx2RD7Oc6iqwM_Qqp90ZZJO6ijkp9AuFxh-vE6FJRo7tpKQBoQ6XOJpCcbsd61oxBn-9OjTeVp16MLz2ZlluFwL_zAY8VqGfOT4NqLJtfNSB1hsaO9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=H8rBEIZk7_fqlBgxiEeBbLHSuxY54EOUg7dEQL0HUx1TB_YGlMR_cFAjC5Yg_4nUOgyxtUPZJeyeFnOAlTMc3SvhX_mTtQBkqVlkxd21aoPFFOCulm8bflys7uYsvqC4tkTKHYud_lmXRJ9_ScnL4vgZm_LKBiXm-4PNhuhJ8vpRZrdASfSB6DC67nPaf2XauQkAb2uuDSnkH6Ithvvkwe0bxHf02wd4O3RheFO1Bit0fypyaRx6m9mpd6vUoLyanm6TuiHQhjic0zN29JQH1jKsK4wLLQkEiAF7gzK_22QMWYs3lBtrFLr5rSSGj0mYhEztt9zpGz_v9M4CRCqLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=H8rBEIZk7_fqlBgxiEeBbLHSuxY54EOUg7dEQL0HUx1TB_YGlMR_cFAjC5Yg_4nUOgyxtUPZJeyeFnOAlTMc3SvhX_mTtQBkqVlkxd21aoPFFOCulm8bflys7uYsvqC4tkTKHYud_lmXRJ9_ScnL4vgZm_LKBiXm-4PNhuhJ8vpRZrdASfSB6DC67nPaf2XauQkAb2uuDSnkH6Ithvvkwe0bxHf02wd4O3RheFO1Bit0fypyaRx6m9mpd6vUoLyanm6TuiHQhjic0zN29JQH1jKsK4wLLQkEiAF7gzK_22QMWYs3lBtrFLr5rSSGj0mYhEztt9zpGz_v9M4CRCqLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdk9ZDscHrkNKdRYQpFJqttLR0_oIGDSwrchSYeXFObEM38lkGjjGfy2FUxcfPtlYHmdjOwAijczFMb5HCXj-h5CiwsLU5zFbxnv8AW8nqkLz3zDWzOyw_81FcSUPI63I18WK2OURJIFoL56HynUKZO1VkW0QRKewJDXz-omPUGI87RJxsZlBpaAoQQmCaEEmlSO_3Eu0frgQEJpMiVW-wi7e6D4SX9pKAsnLzn_tM_fnxVXJLDsvWd-i6nV86ofipT8LpZ_WxpNf6t94kQJcancQzx6tEVqPkloWbDH5QaByl69OcSRcfGQjWuTTJHlvXkMvGnLU6r9bkMKZNkWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPr4xLS5Hg4CEU_vy7e0pGd6S7ID7PRiBVRYnSC979La4YgrFyMuJp0lYNy_wbGSFWQ40W83BNlDvHcFUGtVvOpMxG5DTuYUw-FijzIwi89djECNOIbLeyIHLoFAfR8PeBgWrQtuUsSddXJ9iGmJcu0hiVTVTGQ1swnBbc9jPBioYZimGE4hHA-QLRVJzl8oOGMZHaF324CKH41CPz-XCVuJr8koAoKCaYZfrmvBiuBRBAwvs4qyl0C5yOUItRgGKGw_W6Uo0S7I5a6V33PVNBkdCL6JgBFjv5mwBTjH7gyMkPQ31o9EmnvTib76qncVsyVYrFTIGfTT6ad8kBvPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:ایالات متحده همین حالا در حال هدف قرار دادن مواضع ایران در نزدیکی تنگه هرمز است.
🔴
این حملات گسترده و سهمگین هستند و در واکنش به دو اقدام صورت می‌گیرد:
نخست، تلاش نافرجام ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه‌ای که در حال حاضر فاقد هرگونه مین است (مین‌ها کاملاً پاکسازی یا منهدم شده‌اند!)؛
و دوم، شلیک هشت موشک از سوی ایران به سمت پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر ایرانِ شکست‌خورده بخواهد به این حمله کاملاً موجه پاسخ دهد، بار دیگر با ضرباتی بسیار شدیدتر و سنگین‌تر مواجه خواهد شد؛
🔴
اما آن حمله، بزرگترینِ حملات نخواهد بود، چرا که حمله اصلی در کمین است و پس از پایان آن، چیز زیادی از جمهوری اسلامی ایران باقی نخواهد ماند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70936">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⏺
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70936" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70935">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK5h7-1dY57-imhVfxK_Bl1VM0dvRj1zNEujtfzQ9gskZ_C5wYZ3G_IHKNptWCMJNfwv1FkKvAG3hb2BysHd-P3GP0vNABRmSVDPa9Oi9e1SuTotK_tm9bSX40Al2CbKMVwuyvm1ImCkdS6vR0uZVLRdZazmmNa4mJD01s8HBwcdZAuZ5A8JCYTCD1GOLYfvPnCZRB_FQu0iU5Q-o0Evf4w48NZDSMLEth2MBoeV34QYTZYcOiE7Ok_N1CrTxPnCNHy-kh4OnhEroEZyWkNuylYX4qWaKSgFl1KfEaCtEY9_qbIKgwsAvhuZWSDml7RFglsU6azb1qJMTka1SPxi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70935" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70934">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
تا اینجا در چابهار، جزیره قشم، بندرعباس، کنارک، جزیره لارَک و سیریک انفجار گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70934" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70933">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNPxdIjel5PBGmektJA0Q6N2PGkbsR40hHknpaeUGB9tKbqa6UpyHOCUDzZzAZCCnZQEgYZZoTEXLa5JdV3TtEr4l3vb4RPxI5uPljOUDAMUsvgoNN6WCu0F5mU7yr2qAr0OwK-hLTNe4mc9UYeMp4g0AVEX8jNTUXkT1IauAbzLWJYT9DTkcEzNznuOVltj7OKEEzqDLZWSApP0OP74-d_Bc-RJ3FrZuV4S0QruOT3rbnQTSINigruGPEzkiweCG1wKjRN4ix_S6D7-a4CuXv9N-U-F-7Uutq7FLtAEgkV_knyyZLGCoLCPRxftyFnpFkBh8l5FCWV-Kc85xe4woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
〰️
#فوری
؛سنت‌کام:
امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده حملات خود را به اهداف سپاه پاسداران انقلاب اسلامی در ایران آغاز کردند. این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70933" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70932">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70932" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70931">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tS9lGcKFXQ41nYtwtwhnv2B16EaEjSFXMuqou7dj64yGZclWtXFoNMFTL9Pd9Ogi__Ymg2h67KbLM4QOQmVyZL8H1UBzAo44ridT0M3AByjeeVhWP54nLRXj-grQwdXFmDeV8_uxhVkHOsVIqosMluWjcRLRciRQbpoPNgTbrrBO-ZK9srene4jEQ6AHR_wW13IGb18XNoAoQG67K3Qx8oFPpFuvLSC_AZwYbLuSeaGQxbq9f8lvHl4bJKe_C6hftY_2y0inUTHwfMpyoTy9lSWgeznkGT4ajjygK0tfkDP17-rkp97TWAjV2mdJGjfmvnmzlKzQKoVxIQHT-zWZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70931" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70930">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
گزارشات از صدای سه انفجار  در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=dMlviKgqaZM1oDR73hofiQkea2n-s3ya_RYv6IjFyeK0U7grxn7JfFaodE2XCPbTWOjecW-pONoEcM7kxN2H8ZD35oY02NQgWsvnEQfbAci_lAueq1Cc5x5peoJAcQObfPI9cPAuBIwYBWi8Gb_mv75abljG1m9SiAZIHRjvN88xM4LpiOZV2Lc0mIfKEDbtFvk8iGYfW0tCgYZbA-tAKOShNzrbUPiNmiihLE4s1Kez68w6RJlNLiYiALvbtNlYXf5MUUaWOv5UhqYknThNcRxrcofimD43GYY5ktSIV4lSARiX3sfZnlUEhfyp7BkmBA_kJic1M7eVnIbXYY8vrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=dMlviKgqaZM1oDR73hofiQkea2n-s3ya_RYv6IjFyeK0U7grxn7JfFaodE2XCPbTWOjecW-pONoEcM7kxN2H8ZD35oY02NQgWsvnEQfbAci_lAueq1Cc5x5peoJAcQObfPI9cPAuBIwYBWi8Gb_mv75abljG1m9SiAZIHRjvN88xM4LpiOZV2Lc0mIfKEDbtFvk8iGYfW0tCgYZbA-tAKOShNzrbUPiNmiihLE4s1Kez68w6RJlNLiYiALvbtNlYXf5MUUaWOv5UhqYknThNcRxrcofimD43GYY5ktSIV4lSARiX3sfZnlUEhfyp7BkmBA_kJic1M7eVnIbXYY8vrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T7AAo_IMK0gTdVdv_rVbXr8AVkZ-QBDZfW7RLVJMpDhjTf-rvECv8U1my9iY0gq6JqyxohaF7BdO1uoWjUmcpn9PmWxaEBCWQVy8BdlTr_LRaUimLDDPyHItpGzc9J2p_7JhkICnt44AYSrbPOLw-wGphsdkhpkIc-YPVyo-C_jvvEGeAyLVCZGFP1kVtjookJvzRO1e9uHW6HVoGQbzVv3BBGSl9E9MIUqeNcsIAMSHvU1d7vn7wpSAEHj9c6XCVwx4J_BFoGDQXjTI_eCHgkXYsBGuOKN-JQaVUhCovL0HfvPtXOe88xPJvbf0vhpY_f_LI43AL_wbs8luxSz_5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T7AAo_IMK0gTdVdv_rVbXr8AVkZ-QBDZfW7RLVJMpDhjTf-rvECv8U1my9iY0gq6JqyxohaF7BdO1uoWjUmcpn9PmWxaEBCWQVy8BdlTr_LRaUimLDDPyHItpGzc9J2p_7JhkICnt44AYSrbPOLw-wGphsdkhpkIc-YPVyo-C_jvvEGeAyLVCZGFP1kVtjookJvzRO1e9uHW6HVoGQbzVv3BBGSl9E9MIUqeNcsIAMSHvU1d7vn7wpSAEHj9c6XCVwx4J_BFoGDQXjTI_eCHgkXYsBGuOKN-JQaVUhCovL0HfvPtXOe88xPJvbf0vhpY_f_LI43AL_wbs8luxSz_5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
بسنت درباره ایران:
ما داریم سرِ مارِ ایران را زیر خاک می‌کنیم. این مار هنوز نمی‌داند که مرده است، اما وقتی خورشید غروب کند، دیگر تکان نخواهد خورد.
کارِ رژیم ایران تمام است.
و آن‌ها هم متوجه این موضوع خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgUOIlNXRce-YH03h7GJ5YZOh_6WVrHY7-UgouncmgsV7LGcOwD0JQ5oZhJxVssnmKrfQx_D9LEKPOeN4Jfhl6KayvMR56hEDNhZd7HQA3qmau-KTyyOgSNzt1SaREQewrHu5r-Zr6hqpzjXVrq3XXg04S7JFyHa1Ut_o7lXmdMnC1yFIxpsnpO4o9n6Zn6n03qqJF1nSanVGxni71iSZLbNzejPot1oElo75ykB9CebDgDEYWFT3cg6-o-0tiNrwSFICJwOR26s_hc-9K_CegbGRGnA_mmDFanvIJUjNvuQ4Igvc272YSzhigj3oeGdAJGwqGGvEzcdslcVzbnXE6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgUOIlNXRce-YH03h7GJ5YZOh_6WVrHY7-UgouncmgsV7LGcOwD0JQ5oZhJxVssnmKrfQx_D9LEKPOeN4Jfhl6KayvMR56hEDNhZd7HQA3qmau-KTyyOgSNzt1SaREQewrHu5r-Zr6hqpzjXVrq3XXg04S7JFyHa1Ut_o7lXmdMnC1yFIxpsnpO4o9n6Zn6n03qqJF1nSanVGxni71iSZLbNzejPot1oElo75ykB9CebDgDEYWFT3cg6-o-0tiNrwSFICJwOR26s_hc-9K_CegbGRGnA_mmDFanvIJUjNvuQ4Igvc272YSzhigj3oeGdAJGwqGGvEzcdslcVzbnXE6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrxQz4r0JcyrTMmR-gpijL5HsOIl3caVvlBb9DoBIH7gg88z5-ee1dtSe0uBfMKwPM52V1bSQUw2tmxAy1ujIyatdwZb-kfm9SRp9oJm0Zfqcjm7f0lQ2rVAZo21mr5h-OGG54QjjwsqIIy0hYREK5l_A_cYJu2qqAMi51Halp3c59OFn6K_l3hZWtrdK2BJMCYqzaZbPqduLipRV44ZSUgArA8TlHKoCWzrhrT7yJokLc6dmra0mMh1lgSrBtL2cwUzq0clTsuq22b0O9ePbDPehs0-eLiDumQb1x9svUpBt3A03_hmENNxF0NfrsSpYCaQiZz49OXhgpo_qukn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70924">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoiqB-i7y0Q1r-VA2iGKOhDgO-MeQZCy10Rd_lUv44aPdgwZdFM6qTjXN4XiiMfUmBElaFq-UmuCHpBcbKhRGVpmLHGelcza8N8JEDEJH-ifmCLcvUpLzxWNE12OnOYyqbkRwBvzBvNuIJl7Ov4JZxprcLdVp-QT4_riqU7sVfXV5ZgNOcltAfYrnMkNL1HPYSCzfr2aNWC-gC3dT3YLhBbigAygezqXOOXqxJ3rva9Xtp8wPENYNL-iEwt5oq0VUWnlwoZGL6BRDvqhDH6Ye41gEwP2KnHuVCWjn_JKbZMBdwKSuwT9VSo6_GP3dFeEG1EqeI-PckdHc5fVcHrBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70924" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70923">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=Nzca2-uHVaswX5rvjCRJmj4f_sRCJkHpf4GUgOQszxIwfIdQVenD7HrT-7PoWAeJRq2n9NvFHxgIy7CV7eQFo6UamkmWrIDvUpjmOunz4jwEiL5q0i_JCvkwFi9F9K6-OOpugQQx3zIFtd0fuSK1ZFcD3B72C7Q7HteWruz6YtFwRj4OVcTr50UkD8whlR_BS6k6ZlKPz8D05Qi7GkvTIPvm-5jCQmj8BsLhEgBVo63guFpaA1m1cG7IYmtZX0wX_CGirdYtVwTRECNLT6VR59exHAUDz_I-sQhP5tLMwUz9ot-Ye62XZtc01iRILRVh2OVMJrBaurOQvjBZQi3cuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=Nzca2-uHVaswX5rvjCRJmj4f_sRCJkHpf4GUgOQszxIwfIdQVenD7HrT-7PoWAeJRq2n9NvFHxgIy7CV7eQFo6UamkmWrIDvUpjmOunz4jwEiL5q0i_JCvkwFi9F9K6-OOpugQQx3zIFtd0fuSK1ZFcD3B72C7Q7HteWruz6YtFwRj4OVcTr50UkD8whlR_BS6k6ZlKPz8D05Qi7GkvTIPvm-5jCQmj8BsLhEgBVo63guFpaA1m1cG7IYmtZX0wX_CGirdYtVwTRECNLT6VR59exHAUDz_I-sQhP5tLMwUz9ot-Ye62XZtc01iRILRVh2OVMJrBaurOQvjBZQi3cuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت وزیر خزانه‌داری آمریکا:
می‌بینیم که — باورکردنی نیست — این رژیم در کشوری که احتمالاً سومین ذخایر بزرگ انرژی جهان را دارد... بنزین وارد می‌کند. بله، بنزین وارد می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70923" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70922">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=XpxgvfCgYm3qRAYzjnN-WTa6DZutes4D7Xn9G9cZcvTsGRIJD3vKavPFMeHzJnMZ6pk3M2sAS4ilWs82EKS558Qow3jMgdfOX2fzE6LKiGUPtUOvM47ZnsOd0gZlzpNQqZfciav2_KXZ9TgoWrX69g_kog9WW-fXRfKDzxG9aQBYThDadFReAveT0hPn8aZ_er6_5w1agJA5pG_6U9Jr_beWYdYgOwsUIvfnzm8MkfhyXZetwvNA3hgtemfnFY5338DBuK1_wpIrSkB2wuc-rInlSBPOc_pKZ8nralVm0ZbvvPxUdzAHIg6RmXkzMaKL3KxJf6u9SHAKjUOONmmcJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=XpxgvfCgYm3qRAYzjnN-WTa6DZutes4D7Xn9G9cZcvTsGRIJD3vKavPFMeHzJnMZ6pk3M2sAS4ilWs82EKS558Qow3jMgdfOX2fzE6LKiGUPtUOvM47ZnsOd0gZlzpNQqZfciav2_KXZ9TgoWrX69g_kog9WW-fXRfKDzxG9aQBYThDadFReAveT0hPn8aZ_er6_5w1agJA5pG_6U9Jr_beWYdYgOwsUIvfnzm8MkfhyXZetwvNA3hgtemfnFY5338DBuK1_wpIrSkB2wuc-rInlSBPOc_pKZ8nralVm0ZbvvPxUdzAHIg6RmXkzMaKL3KxJf6u9SHAKjUOONmmcJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
متأسفانه شعبه‌ای از یک بانک مصری در دبی وجود داشت که بیش از ۱.۸ میلیارد دلار را به سوی رژیم سرازیر کرده بود.
ما از اختیارات قانونیِ «قانون میهن‌پرستی» (Patriot Act) — که پیش‌تر از آن استفاده نکرده بودیم — بهره بردیم و در حال تعطیل کردن فعالیت‌های آن شعبه هستیم.
ما آن‌ها را مستقیماً تحریم نکردیم، زیرا نمی‌خواستیم کار به بانک مادر در مصر کشیده شود؛ اما همه باید بدانند که ما هویت آن‌ها را می‌شناسیم و خودشان هم می‌دانند که چه کسانی هستند.
احتمالاً همین هفته تحریم‌هایی را علیه یک بانک اعلام خواهیم کرد و هفته بعد نیز تحریم دیگری را اعلام می‌کنیم.
ما با متحدانمان در اینجا در حال گفتگو هستیم؛ آن‌ها همگی پای کار آمده‌اند و شاهد حمایت‌های گسترده‌ای بوده‌ایم — چه از سوی اتحادیه اروپا، بانک مرکزی اروپا، بریتانیا، امارات متحده عربی و چه از جانب بحرین.
ما قصد داریم این رژیم را از نظر اقتصادی خفه کنیم.
و همان‌طور که رئیس‌جمهور ترامپ گفت، دلیل بی‌نتیجه ماندن آن تفاهم‌نامه (MoU) این بود که آن‌ها آمادگی دستیابی به توافق را نداشتند.
وظیفه من این است که اطمینان حاصل کنم آن‌ها خواهان توافق باشند؛ و قطعاً هم خواهان آن خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70922" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70921">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=Sn4AGRb8BLlAy8dFIokylGKvg6XGX_AdszBkAmPyfZHN8yz2XkPfhN8EkrZ88QSPYoiT4Vbq3wbVsSbqcZSDzQtAKUcfYUStEV3_mb1PMSdqoLSegDD0hdV9kZFAydEGp2e0Z8WlVvcpv6vBJydUryfQxpCtR8V8t8Wlv2Rtm0huVgew9em3H3CeJ6j1RXNChkAB6AMMYU_wh1FjAyIrOjMbL3KBZc5aYkghHvTVeQJFXsPI_wLCPkWZ9bwAHBc-eBqerw1XHbZ01_paaiyH60LrxcabG-H7TyFywvZrAIOLrnXvVnIKnFqqD9wRLG9zZMIyrQhFEogwwp1HoaJOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=Sn4AGRb8BLlAy8dFIokylGKvg6XGX_AdszBkAmPyfZHN8yz2XkPfhN8EkrZ88QSPYoiT4Vbq3wbVsSbqcZSDzQtAKUcfYUStEV3_mb1PMSdqoLSegDD0hdV9kZFAydEGp2e0Z8WlVvcpv6vBJydUryfQxpCtR8V8t8Wlv2Rtm0huVgew9em3H3CeJ6j1RXNChkAB6AMMYU_wh1FjAyIrOjMbL3KBZc5aYkghHvTVeQJFXsPI_wLCPkWZ9bwAHBc-eBqerw1XHbZ01_paaiyH60LrxcabG-H7TyFywvZrAIOLrnXvVnIKnFqqD9wRLG9zZMIyrQhFEogwwp1HoaJOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکا قصد دارد با نقض تفاهم‌نامه، از مسیر جنوبی تنگه هرمز عبور کند و ما اجازه چنین کاری را نخواهیم داد.
پیش از جنگ، روزانه دست‌کم ۱۲۰ کشتی از تنگه هرمز عبور می‌کردند.
حتی اگر اکنون یک یا دو کشتی موفق به عبور از تنگه شوند، این وضعیت به هیچ‌وجه با شرایط پیش از جنگ قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70921" target="_blank">📅 17:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70920">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
ما در ۱۵ ماه گذشته، در حوزه نظامی به اندازه یک دهه پیشرفت داشته‌ایم.
در هر دوره از درگیری، عملکرد و نحوه نبرد ما نسبت به دوره‌های پیشین بهتر بوده است.
نیروهای مسلح در هر دو حوزه توانمندی‌های تهاجمی و تدافعی، به مؤثرترین شکل ممکن در حال بازسازی و تقویت هستند.
این اقدامات مرهون آن است که فناوری ما بومی است و جوانانمان این کار را انجام می‌دهند؛ از این رو، نیازی به روی آوردن به دشمن نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70920" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70919">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Aase1juWnzh-fHAx17I4rMrystk7YG3ai1wxiTFyXKtwwF85WyExCdRKQuFQY4dYHv9tNrUTuC_O3YC1xqrSSulo5uMja1VnaCsHsGBXNYQz33jzVVTSqmS7wsXFTMcKCurTZ47TVxzybp9xP4kh0ElcLimCSOvcB4kvUGOfNgJC5gTry4YKd1NsjzzAW5Gs_de_kWO1HDyjsfJR4HEbvCiXQE5QYZE38EY96Czn8DdGmQGQX9GCBoSEONAkx2hshRa-mZBbV7fpyprH5U8DVqEhTsgjV5dnupI48vDqEhK14KYTwyI6QN7phgCAjirHSSxNYmfWm6vMsHchh6GnGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Aase1juWnzh-fHAx17I4rMrystk7YG3ai1wxiTFyXKtwwF85WyExCdRKQuFQY4dYHv9tNrUTuC_O3YC1xqrSSulo5uMja1VnaCsHsGBXNYQz33jzVVTSqmS7wsXFTMcKCurTZ47TVxzybp9xP4kh0ElcLimCSOvcB4kvUGOfNgJC5gTry4YKd1NsjzzAW5Gs_de_kWO1HDyjsfJR4HEbvCiXQE5QYZE38EY96Czn8DdGmQGQX9GCBoSEONAkx2hshRa-mZBbV7fpyprH5U8DVqEhTsgjV5dnupI48vDqEhK14KYTwyI6QN7phgCAjirHSSxNYmfWm6vMsHchh6GnGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خانم بخاطر اینکه شوهرش دائم بهش اسپنک میزده، ماهیتابه می‌بنده دور باسنش تا این دفعه شوهرش ادب بشه!
اما همچین صحنه‌ای رقم میخوره و یه شاهکار خلق میشه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70919" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70918">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f47777b.mp4?token=EzhtZIOA71yBilz3zBlB18p3OUmISl6Y54LuA4206moM-U7xJQ5GeQJNta1anAAznsrr8iYDv9N9IGyCB3hcz2VPXl0kIT-s9fLXQTrWBx5VBMZPlPNUi3TJK49dJHXbUbfpA9oPc68GpBRvie_qbgw_viHozoeCnHBYBKGRS8oSx1_VZMOOfpbM-Fz-WoYf725O3rKsHoSSgkWmPVMfW1X3OmVn0WLa1xCWBENAyxs8oySV0tOOzJ88--RSpqAcL2YLGRON0MfXL2pPrgWWPOeFT_bUF-d4eJk9y-mHJkVGP6ofV7yGZlKbqjDnyylyznCrD2yQacxQ_t_GejaUtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f47777b.mp4?token=EzhtZIOA71yBilz3zBlB18p3OUmISl6Y54LuA4206moM-U7xJQ5GeQJNta1anAAznsrr8iYDv9N9IGyCB3hcz2VPXl0kIT-s9fLXQTrWBx5VBMZPlPNUi3TJK49dJHXbUbfpA9oPc68GpBRvie_qbgw_viHozoeCnHBYBKGRS8oSx1_VZMOOfpbM-Fz-WoYf725O3rKsHoSSgkWmPVMfW1X3OmVn0WLa1xCWBENAyxs8oySV0tOOzJ88--RSpqAcL2YLGRON0MfXL2pPrgWWPOeFT_bUF-d4eJk9y-mHJkVGP6ofV7yGZlKbqjDnyylyznCrD2yQacxQ_t_GejaUtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره اندام های تناسلی  حضرت آدم و حوا:
حضرت آدم وقتی اومد به زمین دید لای پاش یه گوشت اضافه هست و میخواست اونو بِبُره
چون حس میکرد بدرد نخوره و فقط تکون میخوره
که یهو حضرت حوا از آسمون ظاهر میشه به آدم میگه نکنه میخوای مارو بدبخت بیچاره کنی؟
حضرت حوا بهش میگه جریانو و اون منصرف میشه
آخرشم میگه حضرت آدم وقتی حوا رو دید اون گوشت دراز مانند لای پاش دید یهو تکون میخوره که فهمید نه مثل اینکه بدرد بخوره و منصرف شد از بریدنش
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70918" target="_blank">📅 16:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70917">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=frE36cIoQtcSZ-_oeQz9cP-00BDfNSx8F2AZGir-mGZwjk8ObHlL23wY3qjO6-b9jnehamCbYmBM5_Ri5MnMZDqCVmI1xsxqGkZcWpeS5nqv_dOQR8--N4-zVPOd77g5KYQTG7dJ7hxQGcs_Cw3QjhNDJmxPtXXUVsms1JDQhkbZw9MYzmRxVqPY0bTRSX9tIAS51c2RblSTSE255CZFjP4GvGXjCedZMJrYJvOM8VxoaswLux4gmb3e5ApJhy-nO5vs0uE1f_Ov62U2e6iLqbyR_OIMY62szxdiXDJU1C9U4Ca9ulsq090qmtIRwXIelI3NAVxUhJU6H5UXxLmrHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=frE36cIoQtcSZ-_oeQz9cP-00BDfNSx8F2AZGir-mGZwjk8ObHlL23wY3qjO6-b9jnehamCbYmBM5_Ri5MnMZDqCVmI1xsxqGkZcWpeS5nqv_dOQR8--N4-zVPOd77g5KYQTG7dJ7hxQGcs_Cw3QjhNDJmxPtXXUVsms1JDQhkbZw9MYzmRxVqPY0bTRSX9tIAS51c2RblSTSE255CZFjP4GvGXjCedZMJrYJvOM8VxoaswLux4gmb3e5ApJhy-nO5vs0uE1f_Ov62U2e6iLqbyR_OIMY62szxdiXDJU1C9U4Ca9ulsq090qmtIRwXIelI3NAVxUhJU6H5UXxLmrHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر روز عجیب تر از دیروز
😳
جدیدا یه عده میرن به این شکلی که می‌بینید، یه مداد دستشون میگیرن، رو زمین میخوابن، میچرخن و نقاشی میکشن!
اسمشم گذاشتن " نقاشی با بدن..."
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70917" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70916">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=W2CLfwcoEtUnQGd_wsNGx2sfxkg9QXbeJdd77QPUtLTpQGLp2L3pV5il_Ue6JZBo4srwcNu2uwZb7Wj2o9XHagagJDrMDUQHvYgR-N_ub9nBdmlj5xcaygU3kPHmYy1dgVlojQurDR_8Po8bqnaTwTEH-M16av-LPTphbQ9wRoBx-Nke-LwAK6RBJtQGQZsZ5gpooN4XvRJRkzT5XfM7ASr8ynCF1EDfRTxQ5bjoMeEc3i1z_YPL6mKwE6Nd8EsqO-8d1xqLG3eNoK66dVeFFlLOf4Q2iSB0KrBajyjkMMEQnvdXkbUIbsF5Qjv_Fza4BQG0dv3Y_wjHh9s34Vyt6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=W2CLfwcoEtUnQGd_wsNGx2sfxkg9QXbeJdd77QPUtLTpQGLp2L3pV5il_Ue6JZBo4srwcNu2uwZb7Wj2o9XHagagJDrMDUQHvYgR-N_ub9nBdmlj5xcaygU3kPHmYy1dgVlojQurDR_8Po8bqnaTwTEH-M16av-LPTphbQ9wRoBx-Nke-LwAK6RBJtQGQZsZ5gpooN4XvRJRkzT5XfM7ASr8ynCF1EDfRTxQ5bjoMeEc3i1z_YPL6mKwE6Nd8EsqO-8d1xqLG3eNoK66dVeFFlLOf4Q2iSB0KrBajyjkMMEQnvdXkbUIbsF5Qjv_Fza4BQG0dv3Y_wjHh9s34Vyt6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏺
فرماندار ماکو:
آیا دولت مقصر گرونی هست؟؟؟ خیر ما مردم مقصریم باید به خودمون رحم بکنیم
قیمت ها خیابون به خیابون فرق میکنه تقصیر ملت هست که تو ذهن هاشون فکر بدی دارن
یه عده گوشی و قلم گرفتن بر علیه دولت مینویسن نه آقا ملت به خودش رحم نمیکنه و خودمون باعث گرونی هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70916" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGLKTbRJuTWYncKPQxDhwjy9xhGOTabESKKFbdaMP09te35RSWH-ne98DjpqU3NSRI6JIUQbFDla7F5ef8XAsZm-6kdC1vugjLWOYbUUswogHA-K54eVDy6MviWx58-Tqwvhfcu7uVqNkM_YDN7aCyNyEnIQNrwOQaHdJcbcID-MojW-b22yqRv6i-z7BiZCuJeVtXAf2ALWjgX3wKyJIYWk-9wEB1A8kOjiw8xp_9RPozlM_EU6vOchJYBLelx7dsC7A9b_Pr95lZp0WEmqpWq-fnph-hbL1HQIgpZzWG3X35pzU7P4dC74xkedi8tDGblYIAn0G32eFZwJPW-D9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qv8wKy6JzrovfEE7BJ9799uZSz2AyM2WxzoIDn_DJKJJk77WB-n3-5nbpD5ybQDakD6CCtcnc3RC7-dIHO264S-jSCsEEc5CCNqhlx2mqUXrztRtEhFRL9U_fwhMhNmKZMQAHX3V2QsHYOE_ufJRkCBhT6gVlemH7RImOc0qcjhsIjW0j2Y9VRi86I2tNUzpZekhEYml7dEoALeGs7ZbySWIteC-VcM6BxTjE1Q2_cWXt6QylbekcKmztu1an1nfjkrOgwK9ccXJaw1KAfSgfYG8z9WkthLcS83iJCFuVBWM6l259lLX9Oovzux32elLJhkCHnl3GXrJU3PtnXoOaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f05211278.mp4?token=WrQF_beZ_HoD37xZtcEmWOFiJycBPOrSvZbqNck_oM3148FwxU_MSSlcDkf6MghIL0hVzyI0voZQtUSomlW7wVhiMYzIlw_5oa0L5-gUu7evx6_cUD_LToyGrHdwYdJItzmcY_4pAMA8rK-bwV4RZeODCl2siIBkwRvm-NfwICjY_GPI6I-rorjpM__iholek73qonPwDc3FdfFVklT9A8uUMs6lqZ5icDVN1-ZEWTQ1P7mA7knrFmf1-QAMO532PuU9TGjSsDG5KQGu6yvn5s_u9nX2bD0V03cqLxzRh6WDwqE7zP0TZSjDmOKdyRCCdFA3XZWmKxWVA83VMVnamg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f05211278.mp4?token=WrQF_beZ_HoD37xZtcEmWOFiJycBPOrSvZbqNck_oM3148FwxU_MSSlcDkf6MghIL0hVzyI0voZQtUSomlW7wVhiMYzIlw_5oa0L5-gUu7evx6_cUD_LToyGrHdwYdJItzmcY_4pAMA8rK-bwV4RZeODCl2siIBkwRvm-NfwICjY_GPI6I-rorjpM__iholek73qonPwDc3FdfFVklT9A8uUMs6lqZ5icDVN1-ZEWTQ1P7mA7knrFmf1-QAMO532PuU9TGjSsDG5KQGu6yvn5s_u9nX2bD0V03cqLxzRh6WDwqE7zP0TZSjDmOKdyRCCdFA3XZWmKxWVA83VMVnamg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ز غوغای جهان فارغ!
شمال تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70913" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983da46010.mp4?token=icOtyMITGopwhzjtG3yTklRo4Qy4QEbcm6KGvMFAJK0oC760i3u4_KexiqdqNxdPwn1b51W7R4O58uVm79ub2pwr6C0FzhJZXNL9A20Fx3-R1M9x6_NZaRqSmZOCjevdR63J05DsskkSz4oJC1VGh7jcq9LjDK6mWYwkztu6fsNGZ3VsWQge36vyePvoYsh8ZpP0p4dMvIHWBLvLuBadwzo5Tc3WUwfTK76DyWDvfSDaQCRUkTpSTEPWJ8zMSrAAuI93TdcURMqKvuo3OxrvS6_a7nxGUiBJWMbQgmRDw9I9tNqIrTZhxq0AMBoq-vU1LEUqaXCgT931a-nSGIOnLxtecH8eJPUxV8EVxIo_43OA6fiy1JXCxEtP0uGnh63TOSVJCAK2Lh0pE0ckwoxrS0-rl0xuUUP_GTxRqgZ_9DvQlG7frvW95UKu6zqVNDeO6Qtjh69vFPOyfaSAJvQLdy8W08WbgazaxaIJcs_GiBS4YbhJ2ocH6m9ChAQm0ZbtrGoJoUnonfNevTb5rlW9pQ6goJ-aTsCdPRPu5n8Vv7_EYJDoB5SQrc7xbah9ZvCcDACyiW1fhJSRGaLWiwhWDSHS0N9kUYjwezNjXMd239P2RtHUB-dgFXEH1QHw7Cyd8jQNimr34qL6JKpqb8nuF9l-4EcB-W7BRW_W85cy4wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983da46010.mp4?token=icOtyMITGopwhzjtG3yTklRo4Qy4QEbcm6KGvMFAJK0oC760i3u4_KexiqdqNxdPwn1b51W7R4O58uVm79ub2pwr6C0FzhJZXNL9A20Fx3-R1M9x6_NZaRqSmZOCjevdR63J05DsskkSz4oJC1VGh7jcq9LjDK6mWYwkztu6fsNGZ3VsWQge36vyePvoYsh8ZpP0p4dMvIHWBLvLuBadwzo5Tc3WUwfTK76DyWDvfSDaQCRUkTpSTEPWJ8zMSrAAuI93TdcURMqKvuo3OxrvS6_a7nxGUiBJWMbQgmRDw9I9tNqIrTZhxq0AMBoq-vU1LEUqaXCgT931a-nSGIOnLxtecH8eJPUxV8EVxIo_43OA6fiy1JXCxEtP0uGnh63TOSVJCAK2Lh0pE0ckwoxrS0-rl0xuUUP_GTxRqgZ_9DvQlG7frvW95UKu6zqVNDeO6Qtjh69vFPOyfaSAJvQLdy8W08WbgazaxaIJcs_GiBS4YbhJ2ocH6m9ChAQm0ZbtrGoJoUnonfNevTb5rlW9pQ6goJ-aTsCdPRPu5n8Vv7_EYJDoB5SQrc7xbah9ZvCcDACyiW1fhJSRGaLWiwhWDSHS0N9kUYjwezNjXMd239P2RtHUB-dgFXEH1QHw7Cyd8jQNimr34qL6JKpqb8nuF9l-4EcB-W7BRW_W85cy4wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
اژه‌ای، رئیس قوه قضاییه:جمهوری اسلامی از هر وقت دیگه‌ای، بیشتر آماده‌ست!
کسایی که تو ایران هستن، همگی درمورد امنیت ایران یک‌صدا هستن.
اگه باز محاسبه غلطی بخوان بکنن که آشوبی یا اغتشاشی تو‌ ایران راه بندازن، مطمئن باشن که پاسخ نیروهای انتظامی، امنیتی، اطلاعاتی و قوه‌قضائیه از قبل هم قاطع‌تر خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70912" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnLxoDtCst_e4vPiskCHrmUnrh02sfZlpMBQjCBYA2Hf5ElLJr_E6O6e-ZaZfJh63R53STaNBhyhJR-Nl0vmuR3-XbATAefR62035LtGBaueP6iLpfqKLcY8iz2YB13QmQrbSDBFDPgOotjpzXSFLhsQNFZVTBHL8bX_OAa39FfvW_ltZNogfYn8lOzQf39eTNpjcVIelS8djefiZeMSNItcQpAJ1Mo-Sc-tjvEPPDc_mNhiX-5_Azx20okevwL8NBTKpw-QWyU_3dHbRRln7aFujrUNT9aFZysHGhD5Z8CMd5_Zk5FMUSYhLtLKgqsxNZ9S1sAH2UubiRoZXOsX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
ترامپ یک مطلب از Breitbart News را در تروث سوشال بازنشر کرد.
⏺
تیتر مطلب؛
ترامپ پس از نخستین تبادل آتش با ایران طی هفته‌های اخیر، وعده داد که «سخت» پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70911" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
