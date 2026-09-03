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
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 08:17:51</div>
<hr>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrYFBIyj6MshT__ZXmWZqWqBO6cxH0TRWxx98l3OaoGUko7XTnwxn4oAt-WGy8Omd7No_HashpolWyOoYOfmY8lUugxQ9PsryBso2D1C9jr5tZuY061wgefkszURYPRWc0s3Wbo3q_ph8dZqwUI9ayEkCpmOMAcleEKvxmCzFkK6b0OOlEQ9z4hCgHqnCHDD_6IBvflSFYkBQVLcTMqZqJ4t1SlvYMGmkVIYncm2hxFybOsI9UyqmYLmUtLFFfT25r7dSBAQGZGTlm3QPy6TXeOvAE5belluu-afMY9RcyqznzbhZ1xMEM6_F47Qwjq3bs67_YV0jmxqk1j2q9VP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=ElQ2QFI_aC37xpEMpxFKCNFD3N7EX4acSDDdqvNlDslvvqPNuygWLeYRlAIhBBQsVj3dbWhakQFvyoJTBLQTJhZtVoFHta5gJXht0alOskw6Z1qRSMWRKzDxbmP22QwxhSSDYPPW3lw35XGHO8cHczgmwJVUa0gP4JWoLsaFofwgegvUo7SRw9dJfHrkddfXiB56HZBOHfJ5BmH1fRXW20pjQf98tR5rl4yDpeBtsUD2fp3Bd1YJzOKsjKZOSd8KjlwGDyZQgp-T0EGNLWcK7D0G0pcaFf41JM119LC1g4cMdsgWSeHLzRB0056fGkwz2fRZMidyNN7s54gKm6FCiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=ElQ2QFI_aC37xpEMpxFKCNFD3N7EX4acSDDdqvNlDslvvqPNuygWLeYRlAIhBBQsVj3dbWhakQFvyoJTBLQTJhZtVoFHta5gJXht0alOskw6Z1qRSMWRKzDxbmP22QwxhSSDYPPW3lw35XGHO8cHczgmwJVUa0gP4JWoLsaFofwgegvUo7SRw9dJfHrkddfXiB56HZBOHfJ5BmH1fRXW20pjQf98tR5rl4yDpeBtsUD2fp3Bd1YJzOKsjKZOSd8KjlwGDyZQgp-T0EGNLWcK7D0G0pcaFf41JM119LC1g4cMdsgWSeHLzRB0056fGkwz2fRZMidyNN7s54gKm6FCiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuiNmWMs1c6Q0FTLPyNML_qWy9G5R0IX5JEnzGOumXy76CQPTE9-wIAZdpJ5vT0ZEMHUSX_P97K557qMaBw7_jZFCdJ-dgEvaip7sCpKZmUe_L5d1mmeLLf86Yt3J5CNePd1lYpbUFg_1MO15jhSIgJajIR5_1r8mYeIjdHBRm4o3kQEmNCo1Kd-lpTpsIorDl3s1BzaF9JLpAUMTddICsl-ge03tdxHy6cpvru0jkcxDCO7x3WV6qG5DQ8kS3LkZ3hcSD0V3z2GpLgRe-rrTSxFuLvzLG4_JyqvFdBG6NYa_YITv1w076z-t3X-fbQ7Wfjr0_w_PU1nU8P53rdUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=T9itzoYSOGkyoRsccA_1vRumwIP3SUHCrKpQYBGBIjWkLtVwL5bf9e3_t4NBSCV0MyNb0f2_QpGUzEPImCNJnMNu0eK9IgU5ltUQwgvW4VeFucJY1Ya7LlTZkrTQayKGesZBX4mUbTdOMsVm_-3MNEQdEplYvM5GsYSsqjTsHGdXKBMq7Zkw-Eo8h2-lPDH1rzjLTBG9DU4l0-lXhsP81OhOG0znxxQLPjmVpaOyHu-RIns52E-lrDB8JeV2Gr8mw1UZr-JKXXnLPRTNQBNavG2viScrEYstij-CPEGkRI1XZE14Jej_ubzQG5k4eFAgrSSnvEEsyl5MonwX-AmAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=T9itzoYSOGkyoRsccA_1vRumwIP3SUHCrKpQYBGBIjWkLtVwL5bf9e3_t4NBSCV0MyNb0f2_QpGUzEPImCNJnMNu0eK9IgU5ltUQwgvW4VeFucJY1Ya7LlTZkrTQayKGesZBX4mUbTdOMsVm_-3MNEQdEplYvM5GsYSsqjTsHGdXKBMq7Zkw-Eo8h2-lPDH1rzjLTBG9DU4l0-lXhsP81OhOG0znxxQLPjmVpaOyHu-RIns52E-lrDB8JeV2Gr8mw1UZr-JKXXnLPRTNQBNavG2viScrEYstij-CPEGkRI1XZE14Jej_ubzQG5k4eFAgrSSnvEEsyl5MonwX-AmAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=BRvt73bzbI_bMJd_4DxOMhjxjPFj8ErBUPwBzxjBndzHgeSgE64ohTISnOjhWj5mEX7wEuOCEf8M5bOu2sz6Sxia-jFHX-UQZAbC6cYKl1zfoFVzEgxDP63xZHC2vfvPUOBut0VZIAq4ohkfVctINMuoXo4Z699P-0shZryuGJKWaWS2XkOt_mQ8kI-ApPd3IeMl3hy9qi5gcgrClOGEy10N-M9ZGoPzBb2ov9eBgpm5EETSfGWmxAAvhZmvLFMSW2EPmjXc08t859sBznawkE-jRxZNgA-hDzwkNXvm609IcdmyhP4JAx9hQ4hy-NtMebMcD1jR5wXZNcw-jOydUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=BRvt73bzbI_bMJd_4DxOMhjxjPFj8ErBUPwBzxjBndzHgeSgE64ohTISnOjhWj5mEX7wEuOCEf8M5bOu2sz6Sxia-jFHX-UQZAbC6cYKl1zfoFVzEgxDP63xZHC2vfvPUOBut0VZIAq4ohkfVctINMuoXo4Z699P-0shZryuGJKWaWS2XkOt_mQ8kI-ApPd3IeMl3hy9qi5gcgrClOGEy10N-M9ZGoPzBb2ov9eBgpm5EETSfGWmxAAvhZmvLFMSW2EPmjXc08t859sBznawkE-jRxZNgA-hDzwkNXvm609IcdmyhP4JAx9hQ4hy-NtMebMcD1jR5wXZNcw-jOydUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzsDCAPFz9BX0h9ys6jXqQtjeAo-vJ83OQqg0hXDvQWdaXWKjLq88jgYbzyblJehVXzyvgJmByIfTrSPYCS89HKgVjmBw1PWrhjujZbKajd9jMZyKG9F1Htjh_tx8hpWM615h5izj_nNBuLGhZMtOqjXvGGNf37tAe3P_TCGYY5pQB3dTxfu5HxY0AimbdwQbDoluaisJCCsLlq4U_naBPMSHL03KxJlu9vowtFVMo02Vsn_FtNKNKZBlyyoWf47U8SM2YyZAeVzLcqS5i4K_qETYhKbcFVyb4yCtX7tu94sJe0BukySvB8ZDEFGCwlkEDMFzwESdUBrPCw81lKnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baYY48YIae203x13l62TUuRfTiylJGPhGIh6vNtf9iskeqaYBKNIalBwQjOg3roeVF0OSkjDt7KoE1Ak1JjvVC2ckGsplhuEJShF4lz9Xja-uIBt2snYsa9C4k7uWyAQ44bH-tbXG3sFZSoeRxWVim_HyTYQO7RFypvWq30-0iCGdRM-Zvgi_7ZVLouU5IKfj5TOhaQrJUmB33tcm-X9H9gkWUsYZZyS8aRN-xTwfEjaHNKrkKxbLKXXOSguaH7dcEyyFcjt4xjvcvDqcJD42DLCT_wdlzoWsvBCzE7RPZjEyR6iBDJqNSusTcstybbE1qT32xduNMwjq8RqkaYnEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=jHlXhsrc-hiw-EiT_E7YipENOoFF6Cbbzm56P4oO1Jy1DQhXHJp-47wdPqAe9_awf1x8WCXiW27NqydInDiQuRhlqAT8amPiohYVB4oQn3X52NnqtSQk4BWtcMZFC5YLfUMkc1DTarjj6GhCtjHSb1WTXlWvX-Pr6-7zlp2M9deDvww81lASdoHGYDq6xrM3oOpMZJt69BnaKyrfuLj8VygJ6y_lH5Rwb6GHMayGE_v0N3Vu7zQf7yyDrn5fzgjG-xOG0Umm25GKso09lsIbn5-tUiXuOBjNdlh13S4Al0WEB8VI-8h6qMTUDhLyPYnLz4u9vO5sgTnTpjSO319Tig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=jHlXhsrc-hiw-EiT_E7YipENOoFF6Cbbzm56P4oO1Jy1DQhXHJp-47wdPqAe9_awf1x8WCXiW27NqydInDiQuRhlqAT8amPiohYVB4oQn3X52NnqtSQk4BWtcMZFC5YLfUMkc1DTarjj6GhCtjHSb1WTXlWvX-Pr6-7zlp2M9deDvww81lASdoHGYDq6xrM3oOpMZJt69BnaKyrfuLj8VygJ6y_lH5Rwb6GHMayGE_v0N3Vu7zQf7yyDrn5fzgjG-xOG0Umm25GKso09lsIbn5-tUiXuOBjNdlh13S4Al0WEB8VI-8h6qMTUDhLyPYnLz4u9vO5sgTnTpjSO319Tig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=Lus5V2NfJdROM1LfGKZi7ijfyIQYIWzQVQjxZFaWk6Dj-zmDSdPsHjp8MT81XmBFEzHVR4qD90ASdu_LDrZL5P79DM2YbGhMJZuBovietU9sYw3fQSrmZuSqSV_szbn_HQDrsO2HscCymvaNYmQS-DhwGZFlebXXDMtMB8WRaz1lvpQyEPYijpxrN3_zvEM3FVxREr7QBEPXfoWkLsgcR9KXoUzNjJDijiwb99KlnRlLFfPlwYx4c0RVKw4egxJaSMg-sNEmSxMHOtjJewWMH0B_fZv6sG58s7cFtEQnOl4P6LZW6Xn9d6a3M9TxNX9nliPXYdG7_wLPk5EWqbUUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=Lus5V2NfJdROM1LfGKZi7ijfyIQYIWzQVQjxZFaWk6Dj-zmDSdPsHjp8MT81XmBFEzHVR4qD90ASdu_LDrZL5P79DM2YbGhMJZuBovietU9sYw3fQSrmZuSqSV_szbn_HQDrsO2HscCymvaNYmQS-DhwGZFlebXXDMtMB8WRaz1lvpQyEPYijpxrN3_zvEM3FVxREr7QBEPXfoWkLsgcR9KXoUzNjJDijiwb99KlnRlLFfPlwYx4c0RVKw4egxJaSMg-sNEmSxMHOtjJewWMH0B_fZv6sG58s7cFtEQnOl4P6LZW6Xn9d6a3M9TxNX9nliPXYdG7_wLPk5EWqbUUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=exqdaYmKGGVRNfTOZYB3vxGXhSc5kCgznSAsFeVNaXSx_sDHpNZryNgBuHjJhn_pRNXdS5ewWIck5aRZC1Iu365eictU-IG-kuIvZ7s2S-u-TolXdkGei-6626TiFtrllDTpLw3NT-9SEPTxEcxPVUrZHBtKzKtByGqv1A5Xw2to16p1hykaHjsdmE5F86hiLDI7vB0grrhkp9FNJ0bjx_8jqUSds0Z-MZLwLvMMu3aLxy-ZATh5LuOBzh8w6uUwYqLRiCqmvQFx8hiHCzsTNP4CdTlZScLoAMDCflZ_-TJpOdPJM82f7bWJ9ZTAREe41uBMrjBqvT5vjEOaPPFIH3MikzAV79GgaG9aIoBjk_4l00PJh_H7VdqDw41lY7RclhwpxsiGgS726ZtaKCZ1UYvWsoEaWJnhZO1VKppBtS91ORrCAXDkcOwlirkiy1t6S0q9stCDuqEronnvpuKGAdFFUeQnznQrLKhvVyvRTfj4a12l9nH9zrTIOMGEnadLMggUfHLAuTBn7FuWTtL2oezb-PKiDkzotL9_30900TpoNSZmYeA3YyyNUc0xQrR7NCgmWHo8cKRBO3vM3hhdzp6u9SMePHJcDWeYo85JHt3KL4Mm90-GC89BAFPZbbiQRgLJo80OWxA64ck3y_x23ftzCGuNOLT6QxocmoPHDpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=exqdaYmKGGVRNfTOZYB3vxGXhSc5kCgznSAsFeVNaXSx_sDHpNZryNgBuHjJhn_pRNXdS5ewWIck5aRZC1Iu365eictU-IG-kuIvZ7s2S-u-TolXdkGei-6626TiFtrllDTpLw3NT-9SEPTxEcxPVUrZHBtKzKtByGqv1A5Xw2to16p1hykaHjsdmE5F86hiLDI7vB0grrhkp9FNJ0bjx_8jqUSds0Z-MZLwLvMMu3aLxy-ZATh5LuOBzh8w6uUwYqLRiCqmvQFx8hiHCzsTNP4CdTlZScLoAMDCflZ_-TJpOdPJM82f7bWJ9ZTAREe41uBMrjBqvT5vjEOaPPFIH3MikzAV79GgaG9aIoBjk_4l00PJh_H7VdqDw41lY7RclhwpxsiGgS726ZtaKCZ1UYvWsoEaWJnhZO1VKppBtS91ORrCAXDkcOwlirkiy1t6S0q9stCDuqEronnvpuKGAdFFUeQnznQrLKhvVyvRTfj4a12l9nH9zrTIOMGEnadLMggUfHLAuTBn7FuWTtL2oezb-PKiDkzotL9_30900TpoNSZmYeA3YyyNUc0xQrR7NCgmWHo8cKRBO3vM3hhdzp6u9SMePHJcDWeYo85JHt3KL4Mm90-GC89BAFPZbbiQRgLJo80OWxA64ck3y_x23ftzCGuNOLT6QxocmoPHDpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=aJORI91Hcdkr46wMstUD8JnsZpOetjXWGB9xV34-W5wt2eOai_b3oCyV9QO9lZcrKsNE-9eBdpcdm6k2dr_2arhUxGUtvNRgC8qMoAf_ptSOdQWxRH4aT9Z_eAhbXA_gzOWn7_KuM6LbitlviLBNza4my7irYrjYJSq_u1TNgh2pxeLKw91XnRxorQS58RX_EzXwbpaobexmv-iHaa_woWvf2xqyctSvE_gR-6KfLZdOCleDItkuR3fGaJW1L6liARLKq9SSpgtVTXXU3vxwS2JEhhdjuHLOvu_xB56U1aHDAzW_fbLgapKpfyXOi__GjtEZy7V5KLBvsv4VHHoreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=aJORI91Hcdkr46wMstUD8JnsZpOetjXWGB9xV34-W5wt2eOai_b3oCyV9QO9lZcrKsNE-9eBdpcdm6k2dr_2arhUxGUtvNRgC8qMoAf_ptSOdQWxRH4aT9Z_eAhbXA_gzOWn7_KuM6LbitlviLBNza4my7irYrjYJSq_u1TNgh2pxeLKw91XnRxorQS58RX_EzXwbpaobexmv-iHaa_woWvf2xqyctSvE_gR-6KfLZdOCleDItkuR3fGaJW1L6liARLKq9SSpgtVTXXU3vxwS2JEhhdjuHLOvu_xB56U1aHDAzW_fbLgapKpfyXOi__GjtEZy7V5KLBvsv4VHHoreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=tT5_Lfpt6-AjZ-UOYqf0LDA3jM_OIIYBjUhAStPbpiGW91zVIeA-a07hFPDCRtcQFAs3pas1kwmo-OZ4MhqvhCV25wgbMDAgigFPZbwDTvYJjUAX4vryzPNLan4juXh2svk5Fexe-rgllHSmPnFZ_xxk1QR6ZUv5ZRKYVctdlF8BRFh0hCn02K1M1bALrO5Lj9BUbrCiGdcPJUWoe2Wn5qIa4jpJK8DI-CTOya9QPARw_RgFz_LBSpcNfpWYkhZ6yaGwcb0fSUf9-nDL654Fo8hATfa6qqRhA0D5VHmWuR2dnpmF_Nv7vbowhfvU3Kb2BTOumNUxtODnbGQG85FA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=tT5_Lfpt6-AjZ-UOYqf0LDA3jM_OIIYBjUhAStPbpiGW91zVIeA-a07hFPDCRtcQFAs3pas1kwmo-OZ4MhqvhCV25wgbMDAgigFPZbwDTvYJjUAX4vryzPNLan4juXh2svk5Fexe-rgllHSmPnFZ_xxk1QR6ZUv5ZRKYVctdlF8BRFh0hCn02K1M1bALrO5Lj9BUbrCiGdcPJUWoe2Wn5qIa4jpJK8DI-CTOya9QPARw_RgFz_LBSpcNfpWYkhZ6yaGwcb0fSUf9-nDL654Fo8hATfa6qqRhA0D5VHmWuR2dnpmF_Nv7vbowhfvU3Kb2BTOumNUxtODnbGQG85FA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIUWbj5IAmUuQKv-MGjWdb498P36ZUJyLWyhktzEZ5V8TnOPf1kZLalrNStdQkYN91LXzmI7l5ngD0bgGeLPpDa5hpdDNq8HIHuSVwxpa8pYY3k58NfuLRQ5_71_VGtpWm-PPqMxz4FEHPStckSLqtXKw5KpWIAW19jTS32VDL-FlQlxAZ5NMCN2c_g73Ma3wwz3pK1_ueLsYj7ic9GLByYEZdliWXg5Udmdq6--osqF2noKIufj-QgJG3wG9Qaym6QKW0dezjYOOVY9_zLZjlZDyLIiHzhdcdAUJCe19pGIMzYg5eI0n2Fh2wYtuj06qYeV19S-B7MvUoL39MOP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqt2X-v4QV3z3uq0j2VIC0EwVKd0cG3UvghSvnaJ3XItPuOAi5idLImmcpTxLBfcz9VQ98QJssGPTBYBV6JxJA3Dpmf682j_R57e7_SQWT6_16gcMgsNPcPadx2todzYzKMpt7fguY7wMNKCgY5xPC82PPBexRVTU9oxnDKQItIMPCPe7xBaOD0AzmEulXI54hbtVOn9qnRc9DBAd383I18Hj5dsucKohYID6NVHJTD5FgZUV4SGnxMlFkS-rEpLBAT-siFE40tOiwkYIN6S8bSsgr60dtx-o0ZHeWts01JGYNqfzeO6C9iuQv_H_dzrMjchivbrdMywAs0biZ8m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=jlho69FEz3W7XU3D0FWFrQJ1OX9p0XUh_tPXxRxHWmrlVXCkAJX08-l9yZgQCvDhJdOR6FleInhQJiRxQBUYrpeUbHW7FJ0I8MN365RptQLShmZGmTvkMKlVwanthQH9UgdgBGRxDcBXsckjA-ND-Ib3Ofl--Nz65e5QL4tXAZ3SlYcwJxwn0TSfU0B51AzSEmiWhphgBBF_b0tRAb8d6TT8LkR6Ygeg0OCtVeS6df54TaZsBHkfQbnmTj6rjSWGD58l6mw5qyy7bNRI7VWXxzCyNgdCIOQ2AUDCCl66se57OsXR017cRlbkFFtu8zrFVx6iLbrKZly1PybWT4s66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=jlho69FEz3W7XU3D0FWFrQJ1OX9p0XUh_tPXxRxHWmrlVXCkAJX08-l9yZgQCvDhJdOR6FleInhQJiRxQBUYrpeUbHW7FJ0I8MN365RptQLShmZGmTvkMKlVwanthQH9UgdgBGRxDcBXsckjA-ND-Ib3Ofl--Nz65e5QL4tXAZ3SlYcwJxwn0TSfU0B51AzSEmiWhphgBBF_b0tRAb8d6TT8LkR6Ygeg0OCtVeS6df54TaZsBHkfQbnmTj6rjSWGD58l6mw5qyy7bNRI7VWXxzCyNgdCIOQ2AUDCCl66se57OsXR017cRlbkFFtu8zrFVx6iLbrKZly1PybWT4s66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=QQhqFOF3uFeMlrMotuFHe8JpRQBoMXIcGusGXs0Xidbt3rb1Uv4DYrtrykVaesvGDYPYR8pVS-eYPCTErt2SJBog-PN0hHkmlMY3fvP4aeGU2bBnR3sWs2kgkl76_ZZsb9fvxiKvPXTosEGBnOsAYur3HOWQbRrjAnmJFVvwFPgZ24j7TGfeH05bEI55e52lQAzXNiNMLhnVqrb3dA2cM3BIUP3eAfxdBbT4czu0X2859j4LRAYfVHHE1ukvaIKJrB1AJIA3fjQTmDhOguabEfrVj3zyPHv75lq9yxmWtPfoI1D4OU-wCOth0wXrZyUs3TLLyBocD2ZO4rnDJukqlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=QQhqFOF3uFeMlrMotuFHe8JpRQBoMXIcGusGXs0Xidbt3rb1Uv4DYrtrykVaesvGDYPYR8pVS-eYPCTErt2SJBog-PN0hHkmlMY3fvP4aeGU2bBnR3sWs2kgkl76_ZZsb9fvxiKvPXTosEGBnOsAYur3HOWQbRrjAnmJFVvwFPgZ24j7TGfeH05bEI55e52lQAzXNiNMLhnVqrb3dA2cM3BIUP3eAfxdBbT4czu0X2859j4LRAYfVHHE1ukvaIKJrB1AJIA3fjQTmDhOguabEfrVj3zyPHv75lq9yxmWtPfoI1D4OU-wCOth0wXrZyUs3TLLyBocD2ZO4rnDJukqlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=Wznchs9wKg4W2Pvc8tbvuWeMohedO63XuDoJ48kNSxp5IpXfC2FHeef9SjHskbxmr6feXX20Lk2G3jpbxMjFQ_nHr9fF9yFxh9mFln_Y0sck1g6ke3QUjvpZ8vD2yRADbrzewVqRrPuWAfHJSpAfZx3ksyjsgVVByAI9KrdyAYM0eEFLB8LJf2ir1PCoD4SvPFE1-OqdjqqvpQYmgw-sJNZDAL1-VkNfzd8AA1AwyTTIoLuT5StE9wauH7fgy3aC_RFrkHVINmXWJ-BeauVDyhtMDT5jVPj4X82ar0aXfXY2b6XZDtzO2lItP4cuzxtSwgjsE3hqIgpqD2gIGhtzZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=Wznchs9wKg4W2Pvc8tbvuWeMohedO63XuDoJ48kNSxp5IpXfC2FHeef9SjHskbxmr6feXX20Lk2G3jpbxMjFQ_nHr9fF9yFxh9mFln_Y0sck1g6ke3QUjvpZ8vD2yRADbrzewVqRrPuWAfHJSpAfZx3ksyjsgVVByAI9KrdyAYM0eEFLB8LJf2ir1PCoD4SvPFE1-OqdjqqvpQYmgw-sJNZDAL1-VkNfzd8AA1AwyTTIoLuT5StE9wauH7fgy3aC_RFrkHVINmXWJ-BeauVDyhtMDT5jVPj4X82ar0aXfXY2b6XZDtzO2lItP4cuzxtSwgjsE3hqIgpqD2gIGhtzZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtky5z1WrJU09CkmnFZBrwM3AmN17EIkDdRr0wDPODMh3hhHmFyHAWGKtQBdUd86GS_4iLuSwzQzcrTbyRB5RkJ8bJlIetc5N0j5dtthrl_p61hQUVVIB5xUg1CUHdDIbpkXFF-qJc9vIBLmpGcrC5VzZJgmNJL-ot29rR2lDQLGtNwNEWOBvyCko4I2mIoGf23rj4lCJ46fIe9HiM7lbyk-bCArLQjHBv8TuoIl9_fLY0L_hhRqTctKKpTKjHx5_XT9HrV_Jpe7BGxpQPOe4ZOfLo4umd_1vaiW3f0NWs8eiSbzovNNQ35m_Uea_wSSYWQQ6HQHoOuv5GHhlqtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EodhnD-DGysUWNu2JKgxJWhQxt7Sf62drKC01s0yYQa-enQexTcKwDWR6siEd7g7qVaoFnyHa6UrdpQaIWM2fFqb8aJG08Nz1V4FjMF9qS875vDPe3Y-woHiIphLzFaO3wkpyX0qQDoRTj5W7LpoflNdprl8zJIsmfzE0Jv6jpNhKEQU08DhFR-gBUN8MCwSC7X8LEON9Ejih8qCVPBcBk6lx25GJnE-AD-e3UTDkMICTN8IZ-R5NwCEmMmmjELtFdQmAXHHlJkmumYHGiMD8Goc0w4FxzEEFAMQkWOPXS6JsdoVBXXuQSJCjMfQN593YZEhdomy_LWwSzkCy98jWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=QVdB-4ffC8mObp-C0fCKdghDEazyRSdv3v0kgPX2nSHLY-wjM_yJoYtHFseKrce-eIqHxxBF0puW9hCezAOPruXjHK5H9zU8XVucHjH9OLBb8Qaaj4TSrrgI-4b0SXJgWOFJxnw1mzcA5eJSIjiCxBX846LmO_J8pP6hKezhk-TpsfIvghDnVkWfNVgJ-ao63QLG88BZsV7p2jHNTyFKBxMxx7_YqoRQ4FnUEKwHQLfVt5CwSiU1GgNauZPHkzPtG_lpclHaI2H8xPYBrZAKROePxo8zkTtatwJLlTs5myVfVmXh_D8va02rRokHWBRWfrHsLC9ucchr3w4_YmAdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=QVdB-4ffC8mObp-C0fCKdghDEazyRSdv3v0kgPX2nSHLY-wjM_yJoYtHFseKrce-eIqHxxBF0puW9hCezAOPruXjHK5H9zU8XVucHjH9OLBb8Qaaj4TSrrgI-4b0SXJgWOFJxnw1mzcA5eJSIjiCxBX846LmO_J8pP6hKezhk-TpsfIvghDnVkWfNVgJ-ao63QLG88BZsV7p2jHNTyFKBxMxx7_YqoRQ4FnUEKwHQLfVt5CwSiU1GgNauZPHkzPtG_lpclHaI2H8xPYBrZAKROePxo8zkTtatwJLlTs5myVfVmXh_D8va02rRokHWBRWfrHsLC9ucchr3w4_YmAdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=WtnzwMeVAN6rePwVe0cLwjJ00O-Yz7q2Oj2ZMygwIY67xnUAeB3r0YVo75NwvbmUEXuYA_BBFbwjuwvvFUMVd2z4HmqNofjjBeMwkadPQmQmVRZYmlQ7psom_m0uVFfJrxphWd3-GxEyZFFJbD2VOjnC5qgeDYTQqMX1MZxus6W4Kl9R00oSo8h5zg44xpMgg26ZZEn4TnxYBDgihnaPekSQjuFBFXZn72MumA3zHYQQ0vPy9WlbxfdAbvxZurcZuKeXL7WGbHZmRhbf6cQJHjuzdJtV-91f8W4uDcNhcdGtUIoLPMlwhztyNMUO7viPweuTT2YTL-LtsziEv0BFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=WtnzwMeVAN6rePwVe0cLwjJ00O-Yz7q2Oj2ZMygwIY67xnUAeB3r0YVo75NwvbmUEXuYA_BBFbwjuwvvFUMVd2z4HmqNofjjBeMwkadPQmQmVRZYmlQ7psom_m0uVFfJrxphWd3-GxEyZFFJbD2VOjnC5qgeDYTQqMX1MZxus6W4Kl9R00oSo8h5zg44xpMgg26ZZEn4TnxYBDgihnaPekSQjuFBFXZn72MumA3zHYQQ0vPy9WlbxfdAbvxZurcZuKeXL7WGbHZmRhbf6cQJHjuzdJtV-91f8W4uDcNhcdGtUIoLPMlwhztyNMUO7viPweuTT2YTL-LtsziEv0BFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=BZa6Z54C8jo75hrnP_--Erc2Lc4q_5A5KRWEqb9LBlnLw3miT_1APnIuPQiD0Dkh6SNeVCEwI2RWTXYJSyRFkbbwGc9oseMuDqhOrEnMDpaVlm4WXzfJukXelJH5Hf-LpxTUa3skZBFpLwUe1CaBO4k1M0E7ZPFH6b7CnzFESTuarCxifWG1LnnHGKfR3s5Few0yB2v2d_uinvRsR5yswczRGbnBnCMLZ9nnxd7a_gptSMeC_Wa6VNoa44tuxyYDhuNnOFNlh7FwxJ6x-GK7CyfUzxvm8Rrptxu_TqnmYXR4bmt0qvfpfqKvAGsxcPZHvP6Zni0JVGgFxP5QQrugYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=BZa6Z54C8jo75hrnP_--Erc2Lc4q_5A5KRWEqb9LBlnLw3miT_1APnIuPQiD0Dkh6SNeVCEwI2RWTXYJSyRFkbbwGc9oseMuDqhOrEnMDpaVlm4WXzfJukXelJH5Hf-LpxTUa3skZBFpLwUe1CaBO4k1M0E7ZPFH6b7CnzFESTuarCxifWG1LnnHGKfR3s5Few0yB2v2d_uinvRsR5yswczRGbnBnCMLZ9nnxd7a_gptSMeC_Wa6VNoa44tuxyYDhuNnOFNlh7FwxJ6x-GK7CyfUzxvm8Rrptxu_TqnmYXR4bmt0qvfpfqKvAGsxcPZHvP6Zni0JVGgFxP5QQrugYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozIPmTXB3YSnOwg7yenhG0_UcilTCyoSncsmNt0buJWk3PhCKFkzDeRxGma0FgI6mKV8JOLKs0R5kWyiCwcWn7eoBm6i_NyryBvj8_Js5ddPM_Xu4A6MlkBoK7GxbirHuWfQLLsOaPz9lraBv5nGHAe6q51BT88YEUaQhHRuj8ULButC4iAFwcokpFh8KPtKOSfBkxlcjFn9D2ZaCAYGkps3IP0yn4ynHX4QYioIE4_0FhvEiEo4I2IiHuk2aeCb73gBLW_6THZspltLr9EPuBLQMl__tZQYr3bRk1rXvb4su604K9szwgmEucoN481njuIFT4O13OPy0hBpcY-qNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwCoysPeNzzK9S6mGEzre0543mAV1EWRM69xKYCTi0b4FlMf0vM8IY_lnHxE_aL7US5QSUjTOXtbsnKoQhOp9Zc12WuQ-D3CZwzjWg1eeQu4EnyaG8wecxDcFY8zm9zBuHyYO8I9IgM4-9phX8dmSOMm-64jU3oRONXkrpXgjMVAmo9vDOFg94e8em6sQazl_X0iXJhFVkS9QL8qkrGpYF48qAG7uS4IvtjAb135vy90qXAiiXTDwqIZOPFrQqokbvVASQnqiaC2WX1SV7eWpNjrPfsQLHk5xSYc1i1n_Lb1xg4CcmqKtZK8nRyZKU348ODF9Txoe7E0yfmEm3FvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LDjzT3jXyDggwK0FCbuNUErJuc8tcl2Ay1MXTlChegLVVSDfwshyAULuLGaj_nQINKCglXxXYCMXLYswSYd3i4mMOIWLrFPQfAK28YpO9wq_0Fb4XVr1A2o0OaWvUzc5mLxE771mKC286SOlP9JaEDuMbU3nfHvt3DDFqs-b4CLB71u1sRUAWqv3VGbXLB4e_eHO6rXjnKieJwS4YVlS8ZbBZMEq0xQ2Eo07zC3vR83pIYs1LhedG_o96VFvR_KPxrauV5RJsEHAsovVHaYW3MHOA-BkB4D_rhvTpqNl3pRwgz0Zje3rd7thfIn2unYN_BOYl2RjXfaF5mxRIKlo-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=sU7behLpKadcv8dqwiz8Wok-K8Pw-qytkfoUFX99BWzwei1fppIRYYqnTz7NVWjFydif_EVMBT3JjmMDqV7u1jqHK0Hc_FdWCd3vO0As-C0yyRnobRSQdJYL2n0qizJFPAJ6DEuJn-6WHn-aJ9vju5sGwHdDyrZ46XoCAmYP-vyqTX-JE-N9Du3OaBKFkb3MXsna8RolE0KlvhvnMdJf-cJ-MGJrAuvcMfRjtA2A6xihtKqJFdldv8_VLLKE0oPIUPmZOwEcGyh-3xhig_URaGdyxZgW5iItFxZRt4pb_HEtFq7Fb876Bgker5tU7b6QFBVFX9NJmFEwC76gWQ6b3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=sU7behLpKadcv8dqwiz8Wok-K8Pw-qytkfoUFX99BWzwei1fppIRYYqnTz7NVWjFydif_EVMBT3JjmMDqV7u1jqHK0Hc_FdWCd3vO0As-C0yyRnobRSQdJYL2n0qizJFPAJ6DEuJn-6WHn-aJ9vju5sGwHdDyrZ46XoCAmYP-vyqTX-JE-N9Du3OaBKFkb3MXsna8RolE0KlvhvnMdJf-cJ-MGJrAuvcMfRjtA2A6xihtKqJFdldv8_VLLKE0oPIUPmZOwEcGyh-3xhig_URaGdyxZgW5iItFxZRt4pb_HEtFq7Fb876Bgker5tU7b6QFBVFX9NJmFEwC76gWQ6b3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIIgNoxFYiAsWnmT9Bk-OuCG7gox-q6eZpFLwRMadvTXY6xn-LGFK5hniDuuAZxVfmO7lBF1iBOz1dDi3E87dgI_aoOeammctaJr6i1HduVlIa4tHgAoRF2_M9sU8APL7WCU-WAbBwg-YNyseUV7XU9bUbzQ_rS235nU6kppjUiPXxfOQfrHm6owJ_TGJroNR11wzaLmoPzn1oFqvBpYOS3O7NOi6wvgrvrNObGote9OcfGTHwcNFT3Qwv5OLTDw2R7JI380FeJB1T9W_ZvBk1P9FEFt0yed7tgzkyEEaBvVPOiQBykhsp_pCLYP9e0CKgOw1shWPXrW0cAvq-LQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=eV8xjkLM1PuXLSRFTwuzt8PMWMbNzWAIps8Qsoh1ALfjE44Kl7Xi7Q-dFr4vTDgLgtGyVl3WX_zYbF5n6Zy2vCfVw2CGnm1OM1O6_kGRWb-IA1Hk0ubeX5Gsoz5kTUelTloSxtdsTF_BYX0naMwvdOb0149_HMveAnbQXuyytqgbNDd_BK6b58kHQx6wGa1rT1qHq1sWdrPAhwFaBoYZgpINdTYeYj6Yczy947UA_KILoBySPffw8yb5kgsI3jEdlb1N90b63YZ_cb3GWAWeiHAkO7aMMVpYStk9IW99FMDP9LqS3JPRiJoU6UvF0vTeJwP8IhpKqB6xn5-plTNH-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=eV8xjkLM1PuXLSRFTwuzt8PMWMbNzWAIps8Qsoh1ALfjE44Kl7Xi7Q-dFr4vTDgLgtGyVl3WX_zYbF5n6Zy2vCfVw2CGnm1OM1O6_kGRWb-IA1Hk0ubeX5Gsoz5kTUelTloSxtdsTF_BYX0naMwvdOb0149_HMveAnbQXuyytqgbNDd_BK6b58kHQx6wGa1rT1qHq1sWdrPAhwFaBoYZgpINdTYeYj6Yczy947UA_KILoBySPffw8yb5kgsI3jEdlb1N90b63YZ_cb3GWAWeiHAkO7aMMVpYStk9IW99FMDP9LqS3JPRiJoU6UvF0vTeJwP8IhpKqB6xn5-plTNH-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه امشب یه خبر بد هم داریم، در طی حملات آمریکا تو بندر کوهستک حوالی سیریک، ترکش حملات می‌خوره تو یه مراسم عروسی و چهارنفر جونشون رو از دست می‌دن
🖤
#hjAly‌
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70966" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70965">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBhyrFvL0s9TdY4WgJsH5hRUsPOR2BbXhuHcEU5rDj8u5aWR_rLYZTuJ7t00DzQelClhW6OfnH27oFmrXIaWKQx7R9n3CFSPHA5XYrG6NyGO_x-Dq_rWT4QcKrQJIZSbXF3l3_Sc13HsX35lvD8qweJXoJ80A3SHcbxxKR1BfF0FNZorKL-CMg0fx2kZ6U-t_dcke0tUgVwG_nOntCZLfKP0C0_V1Q3QTu_InPYYsYFRvCmbDwBQk4cikhmh4cXrVwnRN9N_1Ta_cdNq484_nLxRRmyy3Ec4vXvJLkneyI0C6cAWEkW8wWksGlcmBYt3hcF03XZG5_DqPKs1XEPjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70965" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=UtG8u8b2mJ1rS3kHJfG0PsaMuWzww32c5G6Os2p1ljtiUUjYrso6L9wuwNonbTc_A-2_qeq_LWSmKcAVVjbkcziQNKpQ92ina9Og0iefwR12r_v2G-ehJ0TQzaoVUke56u9SNMk2SH_AiacBG2jTFR0p-xa-tZeDHK_TEvElhCHx1YgZcc87YH4e0lxTufALrEJfhr8B7hFPSQD8EbK27JlYAPFu3uJKCfqB1W2A9Gm1Ly713Gw0CLLrSN8RtbVcnvPF2yPqCQ6dYYAK5wKhRHrQSI2_zgDI_pcoSUh2W9YcoNqClVsRFkOGmz07mNbXgskvGJuiQ2tpyTnikvfjcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=UtG8u8b2mJ1rS3kHJfG0PsaMuWzww32c5G6Os2p1ljtiUUjYrso6L9wuwNonbTc_A-2_qeq_LWSmKcAVVjbkcziQNKpQ92ina9Og0iefwR12r_v2G-ehJ0TQzaoVUke56u9SNMk2SH_AiacBG2jTFR0p-xa-tZeDHK_TEvElhCHx1YgZcc87YH4e0lxTufALrEJfhr8B7hFPSQD8EbK27JlYAPFu3uJKCfqB1W2A9Gm1Ly713Gw0CLLrSN8RtbVcnvPF2yPqCQ6dYYAK5wKhRHrQSI2_zgDI_pcoSUh2W9YcoNqClVsRFkOGmz07mNbXgskvGJuiQ2tpyTnikvfjcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تو وکیل آباد مشهد یه ماشین به تجمعات زده ٢٠ نفر کشته و زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/70962" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70960">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddrNUoWFcnLcKYIGMpeDzBtvRVsqX3j8Xt86yK68tRiX8hKnHeuXqLcn_YUASI0Hulsvh3yxLBCv3cENafctYYclzI0aiae_M5vezBsFuHTMcTHC3YtYMOAmlbsC-rBCEjOszx5Zeee-Bp3t73aFMrCvxOLtDv_k7nUfx7UI9q1UUwPX3sYI1s96wY_97zob55SvRf9iOTlvDpWrTbLJ5zfQvaVT7DQwdlpTuCGz8BHTv7QBY8HVdCOoikz7yQfl0pjAsVqbBHYQUAqsgNN-ndotDNXOY-eF8Xo_D0lDop58L71tnj3bPFLRyDzqZ8jsP6TWzPs0ZrPzQ7k4tZfuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=heT7ms-1CM6ruY2LHUdRctAqnnllUxZBXXqoa4JUyGSPN31WLvGVEfoFLkjoffzM4utnT530A5mruZr7GXn0jHqcKjOaVE0gdl3V4MuztWemuyeiacpN06iJ3U5BK63bDxOLCbnw7f1-eh9gueeMQvjOAYNnolsnqREG-7d11TrrpEkWAhbnfNiPzfkATdYB_eHTkKIvdWa6zFHXkPfLLi44PE_dCw6zn-nxCmDhWvrTrpuvTVlzhB6hoD-WXm7zqBwufL80c8EM_karCkcJP46uMWXO0De7VdnHzCI41RWd0ue7JhiWw5W-DCupzR2HdHtHlF1JugZVGJ1YjhK7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=heT7ms-1CM6ruY2LHUdRctAqnnllUxZBXXqoa4JUyGSPN31WLvGVEfoFLkjoffzM4utnT530A5mruZr7GXn0jHqcKjOaVE0gdl3V4MuztWemuyeiacpN06iJ3U5BK63bDxOLCbnw7f1-eh9gueeMQvjOAYNnolsnqREG-7d11TrrpEkWAhbnfNiPzfkATdYB_eHTkKIvdWa6zFHXkPfLLi44PE_dCw6zn-nxCmDhWvrTrpuvTVlzhB6hoD-WXm7zqBwufL80c8EM_karCkcJP46uMWXO0De7VdnHzCI41RWd0ue7JhiWw5W-DCupzR2HdHtHlF1JugZVGJ1YjhK7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به دکل سیریک که با پهپادهای انتحاری لوکاس(کپی شاهد) انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70960" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70959">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=lSUfWEgTj5Aws0aHOKqDtjLGeA1tS-yZoBlhcaphW9U8AcEtAZDPM8jCHjacmwm3pDfPuCNtU83VT9WNA_5rY9A2t1eUlS0TD1oVrvjy4vjxuARA6EhAc_syNeOOSukKKnXkXNpVd86YI1T9-eEmcJHysjboocLtbJq15GqhD_ANu6XYzs1MmAiExvcj_zUHlp1LF8GpIXLMxmsNn_nEPME6isHxKAF-HE9DL7Grwql7OD6xRQh1BOXpJEFmSfY658qEDThRNstgDat04WxYmP6Ju0spQlekw9gmlG4K5I-UxDh8tSFMinwnVnxeVTLp5GUj2t9X9ygi33dYg3P4nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=lSUfWEgTj5Aws0aHOKqDtjLGeA1tS-yZoBlhcaphW9U8AcEtAZDPM8jCHjacmwm3pDfPuCNtU83VT9WNA_5rY9A2t1eUlS0TD1oVrvjy4vjxuARA6EhAc_syNeOOSukKKnXkXNpVd86YI1T9-eEmcJHysjboocLtbJq15GqhD_ANu6XYzs1MmAiExvcj_zUHlp1LF8GpIXLMxmsNn_nEPME6isHxKAF-HE9DL7Grwql7OD6xRQh1BOXpJEFmSfY658qEDThRNstgDat04WxYmP6Ju0spQlekw9gmlG4K5I-UxDh8tSFMinwnVnxeVTLp5GUj2t9X9ygi33dYg3P4nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اصابت موشک های سپاه در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70959" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70958">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
‼️
وضعیت دکل مخابراتی کوهستک سیریک که امشب بهش حمله شد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70958" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70957">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خود ترامپ، هگزت و بسنت هم پشماشون از این حجم از کله‌خری سپاهیا ریخته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70957" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70956">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
از بیدگنه هم دوتا موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70956" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70955">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
شلیک دور جدید موشک های سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70955" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70954">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من فکر نمی‌کنم ترامپ قبل انتخابات دست به حمله‌ی گسترده‌ای بزنه، سنا تو تصویب بودجه برای جنگ نقش اصلی رو داره نباید بیفته دست دموکرات ها
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70954" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70953">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=XXlL744wHwostSbRXmDtNJb9GSxShpS3cqDkEMUXuSGUkUBluHW5II_k54w7QGr9BwAOyCsCuCo1ZrB9N6rHVzzEWlHvdV7EnnAiyuzvDts696wCA1vrCMekSU7tYS0t9nZ_ZCiJrMW0ocSoqMPAbeRQSn-DNM5GtGH_lAl0FT6I0n5ShgReSysL-uuhsiONf-PdCxHeR28ECQdlyn_DBjMxY0Gqkp03K0NUgwKbWxfD0Qn04mznQtMoEfFbol77dKF3qvB-cG5VzzecvgifwLuRWZd0I-oEmTXepqoxWgOSa_33jhu4_K2_74LgAzbi6Dpu5mH7XDelgGAn0i4XBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=XXlL744wHwostSbRXmDtNJb9GSxShpS3cqDkEMUXuSGUkUBluHW5II_k54w7QGr9BwAOyCsCuCo1ZrB9N6rHVzzEWlHvdV7EnnAiyuzvDts696wCA1vrCMekSU7tYS0t9nZ_ZCiJrMW0ocSoqMPAbeRQSn-DNM5GtGH_lAl0FT6I0n5ShgReSysL-uuhsiONf-PdCxHeR28ECQdlyn_DBjMxY0Gqkp03K0NUgwKbWxfD0Qn04mznQtMoEfFbol77dKF3qvB-cG5VzzecvgifwLuRWZd0I-oEmTXepqoxWgOSa_33jhu4_K2_74LgAzbi6Dpu5mH7XDelgGAn0i4XBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم‌اکنون حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/70953" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70952">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=gJLJuww8JmRxyznmW-MEIkdr2UVlITRl5u4fjzjyp9I7_n5yP9EvCXXYMUrEqWFKXDONxwVxxRma2gYUZ6zCgZu3EncSl5QVhWAb_ZHV4pNjMKVMgc5OFLFIR_bheri5ZMMMJt4tW-6ddi3GaXbAK9dAdFbj8qQ_L-81ZMV_3-x7kwIaBQftuBEtd1T58CxnCrj4C3nKGkvKbLuYbXf6hQcW9IWcROZiUstJebQTWdWqwzDr-76g55YEYZBvl3Suob4s7T-OOR6MxabkobnPvTmbbj9It3Vtrz4ktjENUc-_spj3u0bTsadIDOPeGIZ2A7ZMVMUdQKSwqho1Gkl8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=gJLJuww8JmRxyznmW-MEIkdr2UVlITRl5u4fjzjyp9I7_n5yP9EvCXXYMUrEqWFKXDONxwVxxRma2gYUZ6zCgZu3EncSl5QVhWAb_ZHV4pNjMKVMgc5OFLFIR_bheri5ZMMMJt4tW-6ddi3GaXbAK9dAdFbj8qQ_L-81ZMV_3-x7kwIaBQftuBEtd1T58CxnCrj4C3nKGkvKbLuYbXf6hQcW9IWcROZiUstJebQTWdWqwzDr-76g55YEYZBvl3Suob4s7T-OOR6MxabkobnPvTmbbj9It3Vtrz4ktjENUc-_spj3u0bTsadIDOPeGIZ2A7ZMVMUdQKSwqho1Gkl8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70952" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70951">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه های حکومت: آمریکا یه مراسم عروسی تو سیریک رو زده و چن نفر کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70951" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70950">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همچنان هیچ ویدیویی از موشک های سپاه تو آسمون کشور های منطقه، منتشر نشده
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70950" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=RHHiOsHrXw7sLOaOGBU0EktlVyp9GnxcKlLv1-QYHUXU6YHQmcieSvcI7ggUPoWef7RdNGF5aZBNp2cHYN0i8KGkrGDOQANGv66nVkvxglpiQ2aLUzysgsP9JmhwPC2rCcEksbEBpUlSwuX98soiSZY7IIN3F7si_9wz4UvJNcpnfzZ69JUZnyrRKAYDe-h56cQeXaeqBBCnleTwh7nLiiefieaxc3_eNcc4W1r0laYVl2g9udYbxqif9bEr-Gdx7Qhso1utGWLeivKIgDRLpq1BfufZ5c-RRvOW4Q2Va0ikkycgg5hx0RHiJqjRvmVawTskeVZ8JDXMxGfzePtEiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=RHHiOsHrXw7sLOaOGBU0EktlVyp9GnxcKlLv1-QYHUXU6YHQmcieSvcI7ggUPoWef7RdNGF5aZBNp2cHYN0i8KGkrGDOQANGv66nVkvxglpiQ2aLUzysgsP9JmhwPC2rCcEksbEBpUlSwuX98soiSZY7IIN3F7si_9wz4UvJNcpnfzZ69JUZnyrRKAYDe-h56cQeXaeqBBCnleTwh7nLiiefieaxc3_eNcc4W1r0laYVl2g9udYbxqif9bEr-Gdx7Qhso1utGWLeivKIgDRLpq1BfufZ5c-RRvOW4Q2Va0ikkycgg5hx0RHiJqjRvmVawTskeVZ8JDXMxGfzePtEiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Irb1f5WUNRPERjw-CM8b84qgpeWKWrttUz_5lA93sZHZAxECf7OLTAr2JT-lxhP84OKmwx85b63ASdMpC6SCcb_fllt4uRfD0ZqtOdJ11lV0ACWDmYI72LNwTExx6tgLcHq5rNTQEt0FvFX4qNm00KWXz58ynsmoxvuc5I8zx3ZHTUq03ogD-4pDNQBOO7sB6UHTfDKeNhzTppZvIxTg2HeXg81xuqeHbZ6npJbhbhykHG5AEX__hr-vxxNfC6Kdw4E0UHMK0P8XlX2E3yqyLW9qh0HEM_Qw291MRd2OzxQtpIybpgYccrIkqHzOh4WIKDKb1mI_2hXzVeuZmUp9yal9gD4YVLyl_LmwrXUdFAlJolH1T6SaGcIpUjAlc0kW8Ijig0QTTFE59GenQMP_ktvTfLEwthkM4vJA6Y3_vQFdEbeUSZMcTHbcXbg3fjKU9j_1GOsQAO3ODOvUAZYLPXFeJgMjqGbN4gHuvmTyjxPZqPjW4RHlFgvS9G8CGkmUt6VCvBdRB1N3xmVhdTK3om8xuniVmcUP5jaJkyvBbGbinHibQ6VbH2idrQsle5L9w1INo1RCMV-VcRtWCIWCICLHlE0FXbWnE3I3__z6F27nyScFP3cm82RlIlQ5NR0DfygoLgmT0hQ8dNtnZuRaHesmlyFqKZx3mhf0QCFikgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Irb1f5WUNRPERjw-CM8b84qgpeWKWrttUz_5lA93sZHZAxECf7OLTAr2JT-lxhP84OKmwx85b63ASdMpC6SCcb_fllt4uRfD0ZqtOdJ11lV0ACWDmYI72LNwTExx6tgLcHq5rNTQEt0FvFX4qNm00KWXz58ynsmoxvuc5I8zx3ZHTUq03ogD-4pDNQBOO7sB6UHTfDKeNhzTppZvIxTg2HeXg81xuqeHbZ6npJbhbhykHG5AEX__hr-vxxNfC6Kdw4E0UHMK0P8XlX2E3yqyLW9qh0HEM_Qw291MRd2OzxQtpIybpgYccrIkqHzOh4WIKDKb1mI_2hXzVeuZmUp9yal9gD4YVLyl_LmwrXUdFAlJolH1T6SaGcIpUjAlc0kW8Ijig0QTTFE59GenQMP_ktvTfLEwthkM4vJA6Y3_vQFdEbeUSZMcTHbcXbg3fjKU9j_1GOsQAO3ODOvUAZYLPXFeJgMjqGbN4gHuvmTyjxPZqPjW4RHlFgvS9G8CGkmUt6VCvBdRB1N3xmVhdTK3om8xuniVmcUP5jaJkyvBbGbinHibQ6VbH2idrQsle5L9w1INo1RCMV-VcRtWCIWCICLHlE0FXbWnE3I3__z6F27nyScFP3cm82RlIlQ5NR0DfygoLgmT0hQ8dNtnZuRaHesmlyFqKZx3mhf0QCFikgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=jXbnFTdZ3YkXzF5CvoWDOdJpiBxPoJ9mCrpdw4cmc_le1CBnucv-Uor1Gso1EHmmRDG7xmvBgWvmC16VX_kn1dGbI0ZBbHZ8842ybVBnGBMkJl9cU0YV27qJyxqKYNVaxlzd7-ChlAuYu6YYklHYtNb6mgIcbXfjIhSNToqVSyI6CsbP2ErPZwGjtE7yxHRWF_qeX-5QJnIRsok_3YvjpNUPOfa4VfGohoISYYcvvNejT-VxlpjT_16ez9BIM7eIOh85YQz3bAIfj7xhkZ7bV-bid7B8qgFqClfGCEUx9wyoILAY2pUfSsyFNtqbpFXf5k1Hgr3kEoMR7eoRT08_tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=jXbnFTdZ3YkXzF5CvoWDOdJpiBxPoJ9mCrpdw4cmc_le1CBnucv-Uor1Gso1EHmmRDG7xmvBgWvmC16VX_kn1dGbI0ZBbHZ8842ybVBnGBMkJl9cU0YV27qJyxqKYNVaxlzd7-ChlAuYu6YYklHYtNb6mgIcbXfjIhSNToqVSyI6CsbP2ErPZwGjtE7yxHRWF_qeX-5QJnIRsok_3YvjpNUPOfa4VfGohoISYYcvvNejT-VxlpjT_16ez9BIM7eIOh85YQz3bAIfj7xhkZ7bV-bid7B8qgFqClfGCEUx9wyoILAY2pUfSsyFNtqbpFXf5k1Hgr3kEoMR7eoRT08_tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=eEQPWjVQtd9FyMerJBqwPsk2SyCr5pxT9KJkPOX0SDILmu_bGBPuC37RDBtfsn68IEXjOzadbTfE8tFFcIEgsgcCvlSAl6o-7wbR0JfjhEB-VlcGm9atT5KAL2k9WhPAo6PZjCBAJwLpA6T-yw_61TnimxoIYNbaB60SUbhbly5JOtFjeEl_5h04_dVX_FizgBBzYmfy1J2AOshBUVztVMEyiv90adziRA2morJS6E4FWYr458hw3rbyVtxVi7GYLBz2eWqb0O7iJrj0Rp_g3SqwNlLXxyW8gjtK8GAF7E0sZJlxIvXHVtj-s64ZhxoRmtKPTvomWB53yhfFreSyOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=eEQPWjVQtd9FyMerJBqwPsk2SyCr5pxT9KJkPOX0SDILmu_bGBPuC37RDBtfsn68IEXjOzadbTfE8tFFcIEgsgcCvlSAl6o-7wbR0JfjhEB-VlcGm9atT5KAL2k9WhPAo6PZjCBAJwLpA6T-yw_61TnimxoIYNbaB60SUbhbly5JOtFjeEl_5h04_dVX_FizgBBzYmfy1J2AOshBUVztVMEyiv90adziRA2morJS6E4FWYr458hw3rbyVtxVi7GYLBz2eWqb0O7iJrj0Rp_g3SqwNlLXxyW8gjtK8GAF7E0sZJlxIvXHVtj-s64ZhxoRmtKPTvomWB53yhfFreSyOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGzcIj4vw5nNTjZp4F20RCQOnb6w3CMkKMshoR2EyN6dk40eMDvS4ggLlnXJeLyGMcAlEo_BP8U132fJwOKQEp6QrThcitctk4xTd-G7dM703htjaUhd8bIgkSkK3St3VHj4Jygdn2rcG0ef7ejr23ekXbF2eC8ZnWf4OZX4Kw2S3wv9LSv6q6dJRElNsZ_fxrVd4KdxSJUDTJVRu0gpb159Ht7sAmKzbmSxnAZGaHLb56BuYoai7TC_bD23NxqlPC2ui4DkFvFcyuqio3QXQq8OA6xD0BXkfLLi1tP-zptWUw-MlMFc4KX4to5NqS6WttOcGxgMmgtgEt-wteXE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nixh7jZHLZnLUC0yJ8IT06OHnA18OVfPIIVzR70tqoY6HZCvEPnldv3sHAsiFs707C-HcXsGTl8iX3Z2hXu4NVX4Usc1vTjaQ16gksCbPyKTqHUSIrMGZONirZRcU12Nbkd802FeisHe-zP54Ez7f2k5upFDVT8P_u6aigrU19135yRAzeX2hlF2U8tjJLQhPgCIDQNXIRQIhcc1-B4IahkWzJ0q0BrYpy5uDkkSmGYYTjoX2paJrOJ6vxQoxRnDaX0t1pR6h1se9ttM4qkO61yACTZS3ep-WC-eRPX7U6lKq9zSj1SoNYHyfkd401N3jQK75xC9kt2W7RMsoQxR9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70936">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏺
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70936" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70935">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNlYbMsU8TNpo2YpesEr2qtvwRFVrEm5CZPVNXxJYUNZiAE1VNIIueIH0r59xbV52ZYABxWpque397-Tj8kREErZ1acEWCXFm1XupT7cV5aKmRuuROHtEF6gANA0lUqa9DxT9Dlp6Tk__KQlFZEzbm9T-MO2DI26JNX5HIJd0J7mdCoyf_JogIAzb0mZl5Ov5s3aAK-LQYszcCspnUFLwf0w10L4YWxgFhuNWBRhPuTJyFJ84xOIaWyMlSP62Gwz_4EjWQ2pH34dhjW_Smjw08CFckES0Wgn30Rqz0Wp2aoVVgfeg9DTfXH6D3OLZ2vzurN-N3SE77YNBabXt0Ey3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70935" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70934">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
تا اینجا در چابهار، جزیره قشم، بندرعباس، کنارک، جزیره لارَک و سیریک انفجار گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70934" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70933">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFB5dv5HASgyxIG16QE3aw_ODA56IgfE9mQ9DLZGN0ExcQldsnObm9YlF0T8MUqlbaW4Kc2bCXIjTgGc_yJ0qFNDxP9CmXpaRtw6czES3emdMtKqEZaWJXwUYKIjBhGUYCt89z7Pxbl1-syE0BxvPMwbAX-RP9xQakZXZjU8CRf6C1sFOVdMP_RzEX2-yb1rms_AKs_86822vVDgf6G2LBtxKgJotx_gXZP1FT_HksXTvjy3GfvMY9ftUjGhzhxAk1OZ_CGvNxUilqJk-UQSdTAkJmxj_cIfnVPS1MTUv2lh_Aa6IDsQELbv7hdCvv9hwuah0k7TdonzOOHp08N4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
〰️
#فوری
؛سنت‌کام:
امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده حملات خود را به اهداف سپاه پاسداران انقلاب اسلامی در ایران آغاز کردند. این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70933" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70932">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70932" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70931">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EraVQlUloE6mBOPJWfsgi51mDXf7muFciT0O-5TrUByaNDSjfw4W4FItG8njXwBqBCat-VnG-D1HMHK8B1O7kz4gGIyxMiwFHF61GPkI6bJVO6_OvgiAVdhtpdVT8NmN_4rZOCPPXAJFuPSa-hT3drZvpQOeRHhTc9AiX0y_ffgx1oNmuof70NhGFi5iVU21QpDAUULsymcMToQ1fqqpG9n6GOtBOu5SI5ETFL2hxTuVMKCLMkxguCWN7OpDTSKq624Kw_unNKiNHjvRhEHlOfNSU9fX8LF4d79cjcVN-jRn7WdnJrh7ch0CxZjkciM-IDZmhBwMIrwejGPn7Nye1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70931" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70930">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
گزارشات از صدای سه انفجار  در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=CALCn23EG3WNpenfMdkZd9EYnKqbE2fJJOvMaW4jSPsSPKbeN-ahPZFM3jvTND2kjPd1alyvyK_NK2ZJ0-iluQi9ZubuoneEn6OHNzWAxnk-P3b35OEwVUDUV4dnW15twMn6BjOkoX5z2Emr0yhRzuPqvkwbWk-k4KFck8JW-K5FH1FJ6QwwY6FFhbxCBpfkA5PJLib2gumSsZLY9yhXarbtWoa6pwfF7VIZYifF4dJmWsLG4sNIFfq3O3CgUIr5ODpb5MOfNtcd3MERsRpYv1nnXYKmgTxTVJky0GM2yhg70ZT_ryQHcu1JcUnp9JDuOD1CPqyRf6FkaBLwGndy-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=CALCn23EG3WNpenfMdkZd9EYnKqbE2fJJOvMaW4jSPsSPKbeN-ahPZFM3jvTND2kjPd1alyvyK_NK2ZJ0-iluQi9ZubuoneEn6OHNzWAxnk-P3b35OEwVUDUV4dnW15twMn6BjOkoX5z2Emr0yhRzuPqvkwbWk-k4KFck8JW-K5FH1FJ6QwwY6FFhbxCBpfkA5PJLib2gumSsZLY9yhXarbtWoa6pwfF7VIZYifF4dJmWsLG4sNIFfq3O3CgUIr5ODpb5MOfNtcd3MERsRpYv1nnXYKmgTxTVJky0GM2yhg70ZT_ryQHcu1JcUnp9JDuOD1CPqyRf6FkaBLwGndy-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=Dsv1Zawyj9l7CG6g0qsjnFPz_pVbWSPujzEsJkSAFTO0u0XYip_UAK24zfZ4gDvry6HRF86y-ce7fE-PDJeDWn2nE75F9rodxbwGJ5yxIK5G9UHRlosaVF_UuOMLUnMeETjYHQBSlMNLvRLfOWhfQNQNPg4mEO1hAuNCZ3j5k8dult_A8tgf8cDrVhJWGouNs4tzF-nvsqeQzWT5Rbp38Ieehr9D5RIo9xniDSz5yMvLA1Sgg6efUZdcRERBokHtTnxI3vEzD96yZG9yYhGnWqU15TmvIJsCoI_GkO7gIEhqPonVSdt-GAGpffhrA3FRpYfEgVREiT8SYhv4H6HtXHaEdIO9J00fiFdXJfl3AsqiWNnR4Bjfwpi_S0HF1ei42AX1tKSlqDqpqMnhgWr8nRa7CBgrhGQULoNFL34LE8oJw-bLdxh7X26TkyxGDzrHVRLAMFl4F9znydnfb6uRitheuhNmEwppWm0F9ko2ft5V5dtZXyS78grdF28RXOjz-6MLHGoHwRxErutsm0_O5lOz4h7fZu-N71e0Oq0-drtCCbYNKu5m0qM48gF0cN9EvLKlE1liMHs96f-2K0luNxitxLoTRk46zD92IGJmlNgEsiR_0I_1wZjHciD8aICdwhe3a-DeXViUzDCjV5IVpfvc78-Xh-yexOYzu-TeoOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=Dsv1Zawyj9l7CG6g0qsjnFPz_pVbWSPujzEsJkSAFTO0u0XYip_UAK24zfZ4gDvry6HRF86y-ce7fE-PDJeDWn2nE75F9rodxbwGJ5yxIK5G9UHRlosaVF_UuOMLUnMeETjYHQBSlMNLvRLfOWhfQNQNPg4mEO1hAuNCZ3j5k8dult_A8tgf8cDrVhJWGouNs4tzF-nvsqeQzWT5Rbp38Ieehr9D5RIo9xniDSz5yMvLA1Sgg6efUZdcRERBokHtTnxI3vEzD96yZG9yYhGnWqU15TmvIJsCoI_GkO7gIEhqPonVSdt-GAGpffhrA3FRpYfEgVREiT8SYhv4H6HtXHaEdIO9J00fiFdXJfl3AsqiWNnR4Bjfwpi_S0HF1ei42AX1tKSlqDqpqMnhgWr8nRa7CBgrhGQULoNFL34LE8oJw-bLdxh7X26TkyxGDzrHVRLAMFl4F9znydnfb6uRitheuhNmEwppWm0F9ko2ft5V5dtZXyS78grdF28RXOjz-6MLHGoHwRxErutsm0_O5lOz4h7fZu-N71e0Oq0-drtCCbYNKu5m0qM48gF0cN9EvLKlE1liMHs96f-2K0luNxitxLoTRk46zD92IGJmlNgEsiR_0I_1wZjHciD8aICdwhe3a-DeXViUzDCjV5IVpfvc78-Xh-yexOYzu-TeoOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgXnrXSl8-IVy1KuLxCU0S1Ay3ayl6G17sM7-ldnrnHDtIlf9y0UEMLaS-6KNcRXxjaqM8k0NEXqfXDhZkBS9waguXeNLIVtVJ8DjvSsKi-ihmlgEHaaS54ccWHJBYzLOnyDCrAxWe5zrd2k3n31vGZnFFDJSOKpXHbuWr8GxtWQUHacRaQPIR2Dn-i3yHdF9MOYPxYFoWVUZknxhg8c-YP5nwSUb4blhovshpA7X3RExXQJgCnD1j83wNGkHrnOIcM8XXlAhRbsyW0ek1KGB7JgCgsWf2h-9SdcTwSY0lT6_MTXzyS9vG0Os_AasLDADF6vyGZCxo28g_r8i4mvNzuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgXnrXSl8-IVy1KuLxCU0S1Ay3ayl6G17sM7-ldnrnHDtIlf9y0UEMLaS-6KNcRXxjaqM8k0NEXqfXDhZkBS9waguXeNLIVtVJ8DjvSsKi-ihmlgEHaaS54ccWHJBYzLOnyDCrAxWe5zrd2k3n31vGZnFFDJSOKpXHbuWr8GxtWQUHacRaQPIR2Dn-i3yHdF9MOYPxYFoWVUZknxhg8c-YP5nwSUb4blhovshpA7X3RExXQJgCnD1j83wNGkHrnOIcM8XXlAhRbsyW0ek1KGB7JgCgsWf2h-9SdcTwSY0lT6_MTXzyS9vG0Os_AasLDADF6vyGZCxo28g_r8i4mvNzuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTkcH4iX2IQWFg2SZ3Zj7vDy4qBja-9C_P5OFD1UQeGRiEVWdE_iBjS7IQuuo7AaopRHR2SDj4ScVs_rrYDsOaLhtM83KqTEEtSRQrU8XtCSJQV_uudQB7wEeiaG20u3xpz2CpcJ9gZhZEb-JbSKhSDS-YFbPkHooLZUzGZkqZD7srVBoFZKqPxwW2GoXbmuDdtjtF_uVxzEpc-FFXc7eF_OU5lSgTK6qlLDKp5AZ1KfD3D46h0gPPq-k9_kkkdgBEH5n_eBs5TpZxK4qO45rD8dDuX5izFblWa4xl493sn0S17EW1fCAJchb_-TlceWO4lv05lusJDUVDaJLfWCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70924">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0mnjr0hcd2ZTGmZuGCEL6rgyjXOGQ0tAb-NjRUNnB1LyW9bZKdCIGEYBT0lx-2bTDqyiR-j960kGyymeYOpWMmEB1wE-pTUNyVHr4DPgZgNlMb0Vq4THnT93XG2Lp8yBW73r-8swPK1anhtFwyDKsoqUmBxYI4A_pV8mGwArZLVkNC2Bof1eGvMZk_WAGtwZO-I_3aoXh_M_9KDTC07P02ehLOTCHEeuMlrqzfRs0XHpBKdJN4XLnzTO0UztM0IPXcJBWNEYuDCNLLYCg3LTEwQv2b29UJqA3U13h04sCxIsPby6Wkh3TPIFqix60i3NokgUf2AaAVh5TWPbGd3Zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70924" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70923">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=jZjD9GfN3rdFs4A8w7m0oTRGlHj9TReMxAstawnyhZ0aLzPZ7-SzwN3Zkka2Pe3Vdc_l799hsL4UYOtQVr6MzdLK1H3bGSNBIrYP0CN3uXWarRPnaD4pWSG-FGco9OWEqPZupsij7zYS3q_R9LeAcHLH8w3NAS8dQ9N4K1Fq5n3sv5Y0uHG077WKpyUW2QWinCbPf_9hXG3uupmSRmE92P93NOMnL5ph3UpPHu-ylBPLbfhmfIfZckIYxnFhs5rKPTdxB3lAExGQ2SWf2kmQnWwHCl968iz8rnfaQGevV8p9MIKKX8gH35M559GB0reTUDB_ywqKdzapNzyiW5A-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=jZjD9GfN3rdFs4A8w7m0oTRGlHj9TReMxAstawnyhZ0aLzPZ7-SzwN3Zkka2Pe3Vdc_l799hsL4UYOtQVr6MzdLK1H3bGSNBIrYP0CN3uXWarRPnaD4pWSG-FGco9OWEqPZupsij7zYS3q_R9LeAcHLH8w3NAS8dQ9N4K1Fq5n3sv5Y0uHG077WKpyUW2QWinCbPf_9hXG3uupmSRmE92P93NOMnL5ph3UpPHu-ylBPLbfhmfIfZckIYxnFhs5rKPTdxB3lAExGQ2SWf2kmQnWwHCl968iz8rnfaQGevV8p9MIKKX8gH35M559GB0reTUDB_ywqKdzapNzyiW5A-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت وزیر خزانه‌داری آمریکا:
می‌بینیم که — باورکردنی نیست — این رژیم در کشوری که احتمالاً سومین ذخایر بزرگ انرژی جهان را دارد... بنزین وارد می‌کند. بله، بنزین وارد می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70923" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70922">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=oosrW6G2aHYe-gUF2f0UZ1RLkKix000XpLMw1C0G8HMsC9uRzB_j20v_xTc_Mm-gvlQVtc5O_1is0deNfifp4V25pPWvv9ZlP4X01guMFVbTo37nT4gzB7JlG7IrPp5tt725Sn1m_PncZ9GCyeSeYxyD9C5LPoMmRBBbav8jzMKO7qZzqvMrfLMVJ9Yo36GaSTI9-CGO984AznAcbYeEeaZ2n0AyCKRZhzGVsUevvdqcRCCFta9xnb5UOXXw6jiEyS-WI_HIh4S4iLjGXIJhC2yu9wje5_MfQVVOULsI6v39OyUZYop1MKD_l2-7ijggtby5zmjSDSE9ydSVsDde2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=oosrW6G2aHYe-gUF2f0UZ1RLkKix000XpLMw1C0G8HMsC9uRzB_j20v_xTc_Mm-gvlQVtc5O_1is0deNfifp4V25pPWvv9ZlP4X01guMFVbTo37nT4gzB7JlG7IrPp5tt725Sn1m_PncZ9GCyeSeYxyD9C5LPoMmRBBbav8jzMKO7qZzqvMrfLMVJ9Yo36GaSTI9-CGO984AznAcbYeEeaZ2n0AyCKRZhzGVsUevvdqcRCCFta9xnb5UOXXw6jiEyS-WI_HIh4S4iLjGXIJhC2yu9wje5_MfQVVOULsI6v39OyUZYop1MKD_l2-7ijggtby5zmjSDSE9ydSVsDde2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70922" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70921">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=dd5-ELWTfVk1p_pBeRNj3DIgAlGT5FoBGky0fy9TWjJUdJvo_vMCRkYTiEg7BAITNV7SZSb5LhnOGtuyeaeOj7eQDamdDdU6eZbrekYcwokoRIlgbiuyDaLqGJTup6alRUj5vl4em-8w81XYfQbys0v025r1t8tDD5Mm92vTKHmSoc9Xj2gXNywmkDNvkNjHUcPcd4vGnSh_aR68-0NaHPZpFXuX_dgmds-oPlUmCzmPndMAmgI1Pfn-lHQDSZ7J4IaYI-zEkQ_867oKHmGdBQWTqsjmdoQ-xjhf6hLX0AD4FdyEY9r2QovuNKO75KpS9dXVTF4hFW8Q1XKvagm3xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=dd5-ELWTfVk1p_pBeRNj3DIgAlGT5FoBGky0fy9TWjJUdJvo_vMCRkYTiEg7BAITNV7SZSb5LhnOGtuyeaeOj7eQDamdDdU6eZbrekYcwokoRIlgbiuyDaLqGJTup6alRUj5vl4em-8w81XYfQbys0v025r1t8tDD5Mm92vTKHmSoc9Xj2gXNywmkDNvkNjHUcPcd4vGnSh_aR68-0NaHPZpFXuX_dgmds-oPlUmCzmPndMAmgI1Pfn-lHQDSZ7J4IaYI-zEkQ_867oKHmGdBQWTqsjmdoQ-xjhf6hLX0AD4FdyEY9r2QovuNKO75KpS9dXVTF4hFW8Q1XKvagm3xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکا قصد دارد با نقض تفاهم‌نامه، از مسیر جنوبی تنگه هرمز عبور کند و ما اجازه چنین کاری را نخواهیم داد.
پیش از جنگ، روزانه دست‌کم ۱۲۰ کشتی از تنگه هرمز عبور می‌کردند.
حتی اگر اکنون یک یا دو کشتی موفق به عبور از تنگه شوند، این وضعیت به هیچ‌وجه با شرایط پیش از جنگ قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70921" target="_blank">📅 17:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70920">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=MV6MmOAtQ1cfeYhOwLo2JyUGPRPL89Dlfn0i-1nzMWrLBwP0N8SsvbdgWTlrgzX4H24LgO83XT5H3W-q4eR0Mj_-Yn1N84bLZP0eghTr44MMS_etB8c1W1pxkIsFeV6syD29RWXf7DZ03lDfnNr0fXbbWFN3eVOGBxcGeymtC40M3FrqgYT0XR3RA7xztSuOsLUonlbzOqLAlRJBJ1ylNl1A3ekbgDcV6xtxOMaHn0yEGw0a4n4MxgpzbMEnuZIJLJZZQahLghikTuUvsDJf2aN54OTgX86Gt9KGNCmYPWKaLVud8ZDBXnB-WnqceJ3PpHGul-Gds4d59wvS5JOyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=MV6MmOAtQ1cfeYhOwLo2JyUGPRPL89Dlfn0i-1nzMWrLBwP0N8SsvbdgWTlrgzX4H24LgO83XT5H3W-q4eR0Mj_-Yn1N84bLZP0eghTr44MMS_etB8c1W1pxkIsFeV6syD29RWXf7DZ03lDfnNr0fXbbWFN3eVOGBxcGeymtC40M3FrqgYT0XR3RA7xztSuOsLUonlbzOqLAlRJBJ1ylNl1A3ekbgDcV6xtxOMaHn0yEGw0a4n4MxgpzbMEnuZIJLJZZQahLghikTuUvsDJf2aN54OTgX86Gt9KGNCmYPWKaLVud8ZDBXnB-WnqceJ3PpHGul-Gds4d59wvS5JOyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خانم بخاطر اینکه شوهرش دائم بهش اسپنک میزده، ماهیتابه می‌بنده دور باسنش تا این دفعه شوهرش ادب بشه!
اما همچین صحنه‌ای رقم میخوره و یه شاهکار خلق میشه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70919" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70918">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f47777b.mp4?token=a2tAnoXx2S00PMCmVi2IfcVNopyLPbCzIPfkG8SXEzDHCO5uTHvGHvP2FUTicc-_BJbyT_yDx8ugNAELVd6A92ugOdx3lpmQ4vLWPiO8-V74tCjmSWVaNlbbn5UkfDpYA-By4BsVPU2Gbi5ME9YY1yoKDZrovyVh3LeUHctvRDyYQnt9Ib30ZorbritI0dQD4TrEelb2p8o3p0n3ovQ5HNqvWRh_aXS90Gc078xLV8uxxwIsj9QN8EFCFZA1ae3Q68u-fzUVwlXX44uczyCGJQvRAgmIu0NFwWBTUc2IIfyy3ZEQ28ELwEE3uHgCfPudpztQbni4CHGYnZGEYzua2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f47777b.mp4?token=a2tAnoXx2S00PMCmVi2IfcVNopyLPbCzIPfkG8SXEzDHCO5uTHvGHvP2FUTicc-_BJbyT_yDx8ugNAELVd6A92ugOdx3lpmQ4vLWPiO8-V74tCjmSWVaNlbbn5UkfDpYA-By4BsVPU2Gbi5ME9YY1yoKDZrovyVh3LeUHctvRDyYQnt9Ib30ZorbritI0dQD4TrEelb2p8o3p0n3ovQ5HNqvWRh_aXS90Gc078xLV8uxxwIsj9QN8EFCFZA1ae3Q68u-fzUVwlXX44uczyCGJQvRAgmIu0NFwWBTUc2IIfyy3ZEQ28ELwEE3uHgCfPudpztQbni4CHGYnZGEYzua2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=m9jxdIz5NGs0r9I3kwOFvaMagyEnKhUJHSOZ-FQ5ylieXlt2rnCTzC5213Yygrcp4SJxsEjvxsd7f3TW80NE1pF39TsdQQtkUn3gaJPnhvs7MPRdEy92SzYHPDeJekA7WzrY_l13L_5q1DwkELZybkpESrYcYaFkEq1gWE54oB5XKRMhD3yBw2JwYYIRXrnOodKZdHp8M0j-mPGFzOgy1c70aC6m2Kur6zBqEVNjYTEy3c8pN9sb7i5P9hXyih-joE1zZO5DrT9iGGl84Z3UdxcMYED93GB5wIzfVJNkytdhA69jYiHZurOFsdU0FTz2MwyvdXk8_73WTsQT4guh-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=m9jxdIz5NGs0r9I3kwOFvaMagyEnKhUJHSOZ-FQ5ylieXlt2rnCTzC5213Yygrcp4SJxsEjvxsd7f3TW80NE1pF39TsdQQtkUn3gaJPnhvs7MPRdEy92SzYHPDeJekA7WzrY_l13L_5q1DwkELZybkpESrYcYaFkEq1gWE54oB5XKRMhD3yBw2JwYYIRXrnOodKZdHp8M0j-mPGFzOgy1c70aC6m2Kur6zBqEVNjYTEy3c8pN9sb7i5P9hXyih-joE1zZO5DrT9iGGl84Z3UdxcMYED93GB5wIzfVJNkytdhA69jYiHZurOFsdU0FTz2MwyvdXk8_73WTsQT4guh-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر روز عجیب تر از دیروز
😳
جدیدا یه عده میرن به این شکلی که می‌بینید، یه مداد دستشون میگیرن، رو زمین میخوابن، میچرخن و نقاشی میکشن!
اسمشم گذاشتن " نقاشی با بدن..."
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70917" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
