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
<img src="https://cdn4.telesco.pe/file/O1ufRcbpQuYmcEa_PWk8cWFAOxOdfa-dHNLw0QOpTEz4L00tD9Sy-ssiK_KdfWVQ5PzVQH8AUO8nM-umZ5h1Qdgrukb9a2Tb5gJnGMtZftCqRhnDQ4g8b1MeUJwI7OGuHnk4bM7dRPgcjZCxIQjo1PIQFuLj9fJxs7cYRFGzR_3iMW3Ng3oea7bPVYI24lzsKEeEJSNoUj5JZ3Lb4oHDMtJIr2ijSNp85Puu_nqL2lBQ3kUbSwHGK44UBDMH8SLiiku1oBFkXmnPNNiZq8zLeYZjF117xWQMiTmZ87YLTpG4FYjGj7ZjK3VpCfAsl0jTWtXt_-WJYeSJt2UlshduJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 313K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq8-9Xhd3PiQZIoVUq3BjhZKXpQQggyhwiIiV_Se7GQmAlwyES5NRKwPUKQzImMKBJh9az2twss2PhTM9uBdS_c2_VV7wxiyLtTf9Om7qeXOuOe_33O5NlPdGehHfrjaRxmVuP9y4yUBjzL36I3TXIOx5-uovTuUwf60Mr8tc9IrrrLCPyEOEXrc9B-15TAfcF6dGtAP7lv4uv1M6s8alQlalNr5pChCcbun6fGWSI98Iql3XqgZo31tJsYCBEY9w6oa5pyjkDwSJCZs0OwB0AKJ7mUk4jIk7yjWevZ_DWrS07HWwIk2G2pmSLZGP2wRapiezvlHfNbn4-7P4b1ekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/persiana_Soccer/24000" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=Gwv9g5vwN7uaOmMD-JYvtnXr_KpsHO-dj4BUk5-CYucPOH2DVv1qoqOlbXvslNtTuW5zjkiqJZEf1LBFRYPjQk65_7cudTTPXMD1g2GWuNcc-bm26OFDImjWsPPgj9SVXN-HWDXW4gAZWoFOzMFJwHxZ8ZcnonabeLuDsQDttdx6_YY42s7djv7KH2VVyyPe3JvYMXwyQhaX9one-hHmWa-WvhTGKJsoA4ki3FJyV3pQQeEZDVeeqD19YstudOaSRpPJYh_LD14l1e9Sp3hmkucQHonnbZhbEOU2ciWqvG8_fgSnVZcGymeJ_1odYDme8DRlK9uKYHuAbDdFYlUNgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=Gwv9g5vwN7uaOmMD-JYvtnXr_KpsHO-dj4BUk5-CYucPOH2DVv1qoqOlbXvslNtTuW5zjkiqJZEf1LBFRYPjQk65_7cudTTPXMD1g2GWuNcc-bm26OFDImjWsPPgj9SVXN-HWDXW4gAZWoFOzMFJwHxZ8ZcnonabeLuDsQDttdx6_YY42s7djv7KH2VVyyPe3JvYMXwyQhaX9one-hHmWa-WvhTGKJsoA4ki3FJyV3pQQeEZDVeeqD19YstudOaSRpPJYh_LD14l1e9Sp3hmkucQHonnbZhbEOU2ciWqvG8_fgSnVZcGymeJ_1odYDme8DRlK9uKYHuAbDdFYlUNgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعدِضربه‌موزی‌شکل؛ و حالا ضربه پنبه‌ای
😕
😂
رونمایی سرهنگ علیفر از دیگر نوع ضربه در فوتبال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/23999" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLw7tRCiA34Z53npyIbruRCAPXaB-Qa88r3k4n5dtOzUtbMkbhnI1gsCuQFSADWRJnvFm9nyhUSnv7eFNwH4DDaMXgtciND3O2Fp9NQbgqsd9kzvknED52a9PVW1nIH2ueMKalJJXm15qtSC7fiRjhhA3oLpJP-LRqEWW9ZqT5a58iU6yW8refQhGv5UOUtG1rOySq1kwFGGybRKac9nZtRqqjKx9c9GYGtpD6yUjFgzT5JBqSW-4MgswpyuGNaLWSAvdiWQf9FK1P0hgW9UUdYy2zAq2WHyl6lm6KHbfo0qlEVxvI-LUXHsn4FFChN5MiMFcnTrcbl1PipH4u5oJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/23998" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6qLibO7UkNqsAfO0zKMQz1rvxP1pALSmkqjuMK8X18kAryFMmAJmdQhMzIji4mpef0iUv59XWprMXxEzA4YfTU2mhalBtV7WfIvsPUoYxiX2grMq14IKNFC6vGGS7Fi_vy7Eb1GPw5z-3pLTYJQkyAn_pfPgyqOD-qkkv7GdSF-sywcTwgzEABcVm8AQu_Y2xDd26nxxkfpBOrvDzVOZ6G1tvIzWrLcX7tpxoebZGcFK9-yPC_Al20xYTqdMXEYgDEi3iCSDpKCpPtCvdMiH-lucWyrtRMx5oe6WFc4do7MZcCL8Akt9oA15oNUucEorxI0ZbaxutQn3beOSJLlTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/23997" target="_blank">📅 17:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQir_6GEV1gpNzxzHMd3-LFgYUaxNp9bgQrBl3m6L-s4QUip7UJoabkWrVkPCpNBWyrw2yBf9POLLhx73QquFhZ1clYEv5jiuH-41ymb0r2Zsq0jK1lNw2IplqOdbN4WeedSs1RIM-rcOVM336oQ0mJlyiqqEUPFJDys9doGZhV18eGlK8VsgLOseEazRxHf19sVAQ2Cdi5IT-0lTdL9v3dItdMdxmz9r0HGh0PUJkIubDRHdEhVUBGNAP6qfxow1O7zTwUKCRX7u-SweuXP-P9Rg8ZOutqdAu2FTwVQdq8MG0zlDR_DH6fhZdvnb2A8i6XsUZ9UjFcPifdL13fsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛
رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23996" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlUXFXRTCZGWFOfkQG1eMMxrm8gkXr2PwsJ46bcxF4jLVKvyNpfIbHI0Vc46LzZYcy9-SxjqJtsr9Og3WM07V8jSvFIBz6mnVO5C8zdpKsrDzeaW-zUk_RQYcKC065BNMV4LUSMnfbi1S5Prl9WmD35uRHFjVPXtu7hJ1qR2WBQQtlol5cN6RNHAsWfj4v_jb-aCuOW1wkAblqRIzJvs3BeJ-Dt30XrkcSAm1IKAX_kx-i7l3EuZOZ0Ud6CAU1_5RDhP9fAdQ17ALES5heL6e1Xi0uQ-VoDo3Ju0S7vuvOan9l4kD1FL-M3gutIsKzrQqFpku6FiW6n5LCjk-CBN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23995" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1N616fbdVmnzzseFgvu2n5cPjGlizCWazq1de1KZG8dr-VVDrymqZpnl0REBci45b_2e-MI2nsokwJqlnNCsmnId72_p4nIBjqD6GsLE0PZPYYMF56pzmjBi7r3JWmfcoCEWvm8YK4wZarVwC30SSrE5kzDvgyo-DXCMnazapIcFM2rKJdQ8GbklEy7UGCRyRyfTHbaj46GvS2tzczSwXGOXHd0kAdkPl-SuZUya3JtnqgPNX9P6xFGdL7qbBIcnGFixGVKdmF6dA8yvm9SuJafnAkN9GAqTQoWYlzV-ckyNSULu6BtOlOGpJCQwBJYm_fervBTwpBfCiE5eEix5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ: باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/23994" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=HUF0w8xIGLAA6330ru9JMNwuCHYAreS9yu7mcFRrClymGzVQbaKJho-l6YQ-78pqrhqPeoOZXZTZ1iBHnmItRyVGxrbWUu_rw1iRGjL2xuiso2CwCQefFUtRVAH3WrI12G4H9TK5yUDb-6aSdjMz1nfzHLhlrKzBTLYjgFpwjc_NhEcOvhZWoRmFJbwAsa_26fSqhNzCYtoAKfVkwLmg_BhKzNosnf7Ubf1nAV0mT7jQgxsFdH-PK84eXjZORC8zk9ajbsWwb72j6ahPS53vh_ITSg7u2k8GygUnxJKPzIs1zRdiEiBHwIQJ3MAIeySQKe_wbj_DdHjGIUYn4zwc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=HUF0w8xIGLAA6330ru9JMNwuCHYAreS9yu7mcFRrClymGzVQbaKJho-l6YQ-78pqrhqPeoOZXZTZ1iBHnmItRyVGxrbWUu_rw1iRGjL2xuiso2CwCQefFUtRVAH3WrI12G4H9TK5yUDb-6aSdjMz1nfzHLhlrKzBTLYjgFpwjc_NhEcOvhZWoRmFJbwAsa_26fSqhNzCYtoAKfVkwLmg_BhKzNosnf7Ubf1nAV0mT7jQgxsFdH-PK84eXjZORC8zk9ajbsWwb72j6ahPS53vh_ITSg7u2k8GygUnxJKPzIs1zRdiEiBHwIQJ3MAIeySQKe_wbj_DdHjGIUYn4zwc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باز هم ژاپن و باز هم ماجرای عبور کردن یا نکردن تمام توپ از تمام خط؛ توپی که بصورت میلی متری از روی خط دروازه برگشت داده شد یادآور وضعیتیه که این تیم چهار سال قبل مقابل تیم اسپانیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23993" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23992">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuWO4QBIn8piKxdlBwryzEkk73S-5NXorVN_g56kGr_nd3FZQqjDFeR_qDt3aW6h_pD1fpdAhTmd4gjU1gusA4ySbjrjS4TdPK4UKDNeHP2qv9Lp7VpNYnPlTeIQiVs2Y3jaIEshL6hfqZsRtuBSkgK-UdzCdRn-AYy6rsbRwuKris8ejvX504fKiIUPjanMiJEVKWPIo3HPNUa6u3Zcvm-YAsi0liAbE87Tq8mzybo1PW8BdjC39yEnuhhdtv8AYNKYOKM8wL3KM_eZEk8WsN7BEi8cSDTBQUAkjhsimPlCXCkZnpL0Ifo4T3K8gKm7cRTSXvnNerl38hL-B7sLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا رئیس هیات‌مدیره آبی‌پوشان اعلام کرده که فعالیت‌نقل‌وانتقالاتی خود را شروع کنند و دغدغه پنجره رونداشته باشند فیفا بزودی‌پنجره روباز میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23992" target="_blank">📅 17:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23991">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=ZI5_aU6ERReAnNDY29Gf7JGdMP0jr6hln5OL-GrRS-vwOwwHmh9-QTBjBnLpC-Tw5khVMAT5XQUEEt_OnYCsiQ6M4g93A7eFgS3br7DLUOGylvGAmwGoR-pw-EOdOk7vI7yJlx0tsKnu69bOciAavYdUuapyG07SJPCiv4s5OItgq0dZ4qStwmRcxb1g89gx5EUMjqYHrny1K-nv5jArFR7PDKd0zKYelzkZNrIB_hXIips2N1qqn8QfQgofV86LRUFllLw2WTuQUsaug4K_FT-mGT7NHCXq50tpD5y9hQ9r4CUyZWb-kT951X1NM3_Qe6FhWSeJrSaO3yfrP1ryCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=ZI5_aU6ERReAnNDY29Gf7JGdMP0jr6hln5OL-GrRS-vwOwwHmh9-QTBjBnLpC-Tw5khVMAT5XQUEEt_OnYCsiQ6M4g93A7eFgS3br7DLUOGylvGAmwGoR-pw-EOdOk7vI7yJlx0tsKnu69bOciAavYdUuapyG07SJPCiv4s5OItgq0dZ4qStwmRcxb1g89gx5EUMjqYHrny1K-nv5jArFR7PDKd0zKYelzkZNrIB_hXIips2N1qqn8QfQgofV86LRUFllLw2WTuQUsaug4K_FT-mGT7NHCXq50tpD5y9hQ9r4CUyZWb-kT951X1NM3_Qe6FhWSeJrSaO3yfrP1ryCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهنت سرویس ابوطالب
؛ فیروز کریمی‌ رو دعوت کرده گذاشته رو دورتند آخرشم خدافظی کرد و تموم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/23991" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3qaxn9Kj6T_SEh3QI881GfZee97oILLJhr9uTpNB86EwfZoSsS7ZornEPLMYziT_syACUEg2UY9W4F1z4Il9icethf8qUQwgb1uIXkgIlMgTEd0Vwj2xWJGetBVdl36CzV173KisJKZSijpaOTb8fHk-iwW1HyQyaHvQvyb62Dh8WTsT-y4QvGsL7iU0Kf3foR6MIS_kOgOhovSp5oWPz6xd9LTzku8_fH5NzsK-bJxiE3-bj5xOcZWbz0KPpvKUDBGX0RTJeqeNcQcwsc8soPNfUXoacqffSVSLsBBxpSg12WahMT8894yYQAfM8NUB2AT3u6hjEYfK0zTTxoqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ:
باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها به روش‌قدیمی‌ برگردیم که ترجیح ما نیست‌ اما مطمئنا چیزیه که می‌تواند اتفاق بیفتد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/23990" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=u6GmKuv9O1Jx4Sy1eCA4QjiirLsFepKdgPtB-VIIg1C_WgVZjiCZgyA6inEHoMHFuZEBWmCvVYvmFrEIevpPVJ3MNJoLB1ZNnb-uQYnQxirnsKEYUYIgqJjzBlIqyQjqzyEybvki4Y6TazySDaoTcw_LpsfxFuiJeR60PhDLuSkmgdYIzLOGSCRGos2Q9oQV3hWXtKwmc6A-1yacho_gCO_EUG3AheXs13R5-f0i7a_Vl4YWa-wQJNK6_c7JGeSmIXRZLqBBvgFJWauBjJKWrgM46RWh22vNTwNlFVE_nmajIPpZQcQflogt2shR-lFnhpqOzX8hJ2_-K2YZb2l8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=u6GmKuv9O1Jx4Sy1eCA4QjiirLsFepKdgPtB-VIIg1C_WgVZjiCZgyA6inEHoMHFuZEBWmCvVYvmFrEIevpPVJ3MNJoLB1ZNnb-uQYnQxirnsKEYUYIgqJjzBlIqyQjqzyEybvki4Y6TazySDaoTcw_LpsfxFuiJeR60PhDLuSkmgdYIzLOGSCRGos2Q9oQV3hWXtKwmc6A-1yacho_gCO_EUG3AheXs13R5-f0i7a_Vl4YWa-wQJNK6_c7JGeSmIXRZLqBBvgFJWauBjJKWrgM46RWh22vNTwNlFVE_nmajIPpZQcQflogt2shR-lFnhpqOzX8hJ2_-K2YZb2l8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساعت‌داوربازی پاراگوئه دزدیده شد!
در جریان یک مسابقه‌فوتبال درپاراگوئه یکی از بازیکنان، ساعت هوشمندداور راکه درگیرودار نیمه اول بر زمین افتاده بود، برداشت‌به‌مچ‌خود بست و  در نهایتاز زمین خارج شد.  بااین‌حال در نیمه دوم ساعت دوباره به مچ داور بازگشته بود، اما نحوه پس گرفتن آن مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23989" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpehE7gVD72gc_GC3TnrRPazBjYyavhVsQ6NaAZuXdq7yL3JY9nFwft0c6O938gnpWG65yZTF42TIFvUYFiqUFbU5Dzk8FFD_VScEvPVLsvuV8rWzaAL1YZ6fBRTA_oZz6j6-9I4D3DN5ncu0fk2KALSkj4hhhUNzYoZc3enVvR8OPOFcH_IKJ6vSF6BFKfexC5hk_0Zs5RFnfKJDwBL5au1D1lQYNHawa2EwVCR49KieElvHLF2YIFZkQPFe4w95n90qoYfoeWVdV37BdOXwndhHJOKcO7MNHgKifsbUDMxdk3muwG_Y5gMKJJb1VOMwvotOVvM99-ggEisCtVQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23988" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHfgW_7S7cAroy5oqrgpB9wK2-pyPSNYjE2b7Ddi7Ae3mxQS98qql-ouByEMdUEKrpKEPaneMYR3lxuQMKoQlDp6wrpQRyaZGE2VECQj4P30euOFuv3mdyKQ79wFzXDKYiI4QMZ0Wo8T31tNszTjQ82KkNshZY_3eV0wSByuErD5ADKeX0A34sr3EVJTU1VCc0YY9SlHUAk4nym1JQ_Q9H_kunzgCVdoXV3_EBXoodUDDQRQ4V4CJVFUMVcvM9zx46tZbMmePQ9egsG1G-2xI7Hl0TuLzvKuvbVsU_HI_1vj9IZvckpy-CWekIZXGRm2_GSCgu68dIgB45hSmlF6VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌قدیمی کوکوریا در سال 2019: حاضرم موهام رو که علاقه زیادی بهشون دارم از ته بزنم ولی هیچوقت تحت هیچ شرایطی به رئال مادرید نروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23987" target="_blank">📅 15:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر: از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23986" target="_blank">📅 15:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTgrSJhrsfsY2NnarsaBA9ia_2WS-3avXB0A8zlcNNux-l6bHdOosMcrE7kzFYU4u7jCCRGwqNd5KJ3Lj93togFdCw9Jm56dSQfHY_vWDcggue0L7ONk33dgMZXenN-0tQ4roKOccxMendd8CJYg-eA8WhXuYuO7qdqGxfJtjXDgZ74rDsFoyHtNaV6MirN868qaokypyaW4JHDvEx13HsyBZr637rsLyj0nYKzYjDV0knATImodGN074PSQipYB-3K3rc1KUKc5NB1GW7Tw9tTjD1cmdZqGeM_UhTEL9FlKnz1U5i2nPg_XMlyjPp39qqZuPk5utlSlBS7ChAjfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ آتش بازی سامورائی ها مقابل شاگردان هروه رنار + جدول رده بندی گروه F در پایان هفته دوم رقابت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23985" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرمصدوم‌شدن‌کورتوا کذب‌محضه‌اسکای اسپورت همچین‌خبری روکارنکرده ولی باتوجه به فعالیت‌های دعانویس ژنرال‌ممکنه‌یک‌ساعت دیگه خبر بیا کورتوا و دیبروینه سر صبحونه کینه های قدیمی رو دوباره کشیدن وسط و سر دختر دعواشون شد و گارسیا به دلیل‌مسائل اخلاقی‌اونارو ازبازی‌کنار گذاشت. ویدیو بازکنید متوجه منظورمون از کینه قدیمی میشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23984" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23983" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
50 ثانیه از دیوانه کردن خداداد عزیزی توسط جواد خیابانی در ویژه‌برنامه‌روزای‌اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23982" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFvRA2Wcb2NNkrOhMoFHR664ongzcI7kIZ-pawYut_U1PIxgvILtxbsQbNdu2JaiDoHzdLv5ej5eqOistFC50QwyDS7cwk_uBobiLAf77lKxygIXlW4FlHG5qsByW3GI5iqdFsq_hKUaeO4AQvyP0fPcqNFBvyJBv-9nqL7tDGJP5aMGnhueIc8kGjSZZx7JOZVoBpK5lIkzJlKZAUMqPfMISPql7hHuluP_UbA0sZNXvstHy8VBTHbj07pIwgKTlX39qmZsSHmVegT1rrOxvBZ6CFEOJZZyf_0Vl0-Hal-pfHYxKPnfukcujIdIlLm4aFfxW63cZtAl0MmRAlHNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌ بختیاری‌زاده سرمربی جدید استقلال امروز صبح باحضور در ساختمان این باشگاه قراردادش رو با آبی پوشان پایتخت به مدت دو فصل امضاکرد. بختیاری‌زاده‌درباره تقویت کادرفنی و جذب بازیکنان مدنظر نیز گفتگویی مفصل با تاجرنیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23981" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUWVD0MIVFt0ZoLkLUEsS0K55xTg7TGBqCr4xF2LgoNAJx6prMfC0gKTXRvduJu7G4yGMk6CblZXWwbJflDX8K773ng_e3UFudivckK0J50D5VxpMSyU-YffGuXTsJYTIeqPZEvYsq_fhMi_iYJSl0NEk1wZ0yntbWWZmjizszbRwgQqfySTiyjwpzQotLmYbd9WrCKBo3Hs8O-nvh333msV9CZ49hmBnbz07OHkqw6gBU5eAZ8-3CJmDaNbw4U18T-qX5zgPmcPcoev0vonelMNNduWfGMEu_VqNm_mZzuLgmf2qpgya_pjdHwq7pZpXbRsktXYzfU68Z-uSJyqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23980" target="_blank">📅 14:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nESqrOxQS1v58VqVpcF9gZIDGu5jGzHSjisDBvXHFGnQV8IjSpGzEEMuTIa6xbG3ghR_M5Ol1peNq4YzJX6W9qwdnqP9rGUT9ayxc9JhCtFQDbtXwo5eylvo3WCmJsW7_M54f_CD0J2bWzZBC8XPLWbcPQrn_Dsjc0B3ry56UOL2vSdZyvWr9zqBLejvtW4NLQoIo6ecR08oEKG_vVs1o3SS8ho8njttlAGsxbnfLVLkASYRXEimOTNTzm9y-Vnwk46p3I9qOX8uxBgd0RKgWd04KQuaplxLEN7FaDSMdLoPogWNOOGVG7AO3GNEcyNYiiWOrJCKJyfr94122A-4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23979" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هاجیمه موریاسو سرمربی تیم ملی ژاپن با دیدن هری کین کاپیتان تیم ملی انگلیس فورا تبدیل به یکی از هواداراش میشه و باهاش سلفی میگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23978" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv7peAJ0HMOrWAZjVfKn9m_7EasSoZf3YbttEWgZhLSSNQRyf1R6gQ-e1QnsTQ5JRanvp0O2w4RFgC_CUdlF7ixe2OZuZWOROreBPfGkjlncCHAHNh-hae4st1Gfsa8wY-m7z_8UYL4dFQPqfqRASu71jPle1JChiLoUqDjXIPvVWYhUv8KH2ZiGDzuvHqr6QqJMQdNDfETdPBFwHmzXgkP8-9JGjASU26WWPTae9vogo-zMvBgNty4n1OiSlQDcirHbXn0GYGEzOzkbb_m1AvKxIfSVWfi0Fv2k-CJOWAYeuwS2MX4CjFZis2qqQVCDvZch3loexSIHNXyk3qEWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه‌رسمی‌تیم‌ملی‌بلژیک: آقای قلعه نویی عزیز دعانویست‌رو از تیم بکش‌بیرون‌. ما اصلا با شما بازی نمیکنیم سه امتیاز بازی‌برای‌شما. تک تک بازیکنانمون رو به دلیل مصدومیت داریم از دست میدیم.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23977" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGr2AO-3puRbQ-APZ6wZ4wT29u6WZQ_E88a-c4oVkTswasnV920zWKZsrM_9us6XJLv0YZ_z6uK5vZowQRjjbgnKnEAnc2TqxT-nHf3FY1SkQk58dSm4WcTi9MIi0dnmV87BVusNV6peoWGJiVXzYBsOFxzFg42h9qfUt55kU5hplIOmLCILETmvjPlwn8ODB5s_PhVK_KZ3NeEZeRx3LNaxWO9mrEZLUCPLULf-fG9lrO3wKzMu3D0R9IeMwHo1NMMM5RYqq-KbvxWTkcRThdKgFesYN65aRXS3uzkcCTg5rHiPUtt3DKRFgER7woYZiDCME4kTXVWbt-8jzZ9RKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ مگه‌میشه؟! رسانه‌معتبر اسپورت بلژیک گفته لئاندرو ترسارد ازناحیه‌کتف‌احساس دردمیکنه و ممکنه دربازی‌امشب‌مقابل ایران فیکس به میدان نره. پزشکان بلژیک در تلاشن او رو به این بازی برسونند. تروسارد جانشین جرمی دوکو مصدوم شده بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23976" target="_blank">📅 13:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tizu5hK7fOUkzjLexAFvcH7vrkcDXhFm3Y-H7uC7wX1DtIZ98wgcNmbwd9khxEPWGqMBaIm4McqCbOpy0ThuG-mvy_q8MgpZ1I8YQ_RSlXiHy_2uYSv6usSoVrLh5QxPVnKJOXb9QLYaK9p-KMIhrBHqAfc_Mp37HXmgeaRa5E-5XowI8gAkFrUdT5YUqelIVr7CCoV72H_ju2Ec-cw9D7AkBxVkSn88Akk6loKi1OikTbK-ywpG0auEzAe7MfQ57JZByoll8MVvuHNXEXKrEfmJC5pieiEONe2TNG0y5x4kE5ZgGUgBQiz-tnqUAg-yePR1w8CcJzcDkNWg-meHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌پرشیاناازباشگاه پرسپولیس؛ امروز ساعت 14:00 جلسه نهایی مدیر عامل باشگاه پرسپولیس بادراگان‌اسکوچیچ و نماینده‌اش در ترکیه برگزار خواهد شد. باتوجه به مذاکرات مثبت روزهای اخیر انتظار میرود امروز قرارداد رسمی بین طرفین امضا شود و اسکوچیچ بزودی راهی…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23975" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEvCzClHh7NqUSt1XrWxypbg6c1DYd02JASn6hIINB3JvZ1xFfXDZye2fpLaJTgyKZ8N44vRvkbb_pK4CkDTLL6sMymganj-nMNeiGc2u3n4lnawwlcABV0q1S1hzcmQInT7uyUwPeFi8CPZUOcAgMkWkkN-6FyqigYCjyanB33AvJMGEaXM5tuaKzTMGS6Vd5-tcwkHux548eBb8xS-sCdKqKKXlJpeoTEbj2cP-qkbpBe-q6B7qXH5wx3G-WgtgtHhfT2tYezIvi3P7v1SXzxbyZzNZV5eo7aVBhpKXMYwhEFsi774r_GjS5xOKsxKkMDNtb3xIAbnPXxpAnrq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانا؛ با اعلام فدراسیون فوتبال رقابت‌های‌فصل‌اینده‌لیگ‌برتر 18 تیمی خواهد بود. هیچ تیمی سقوط نخواهد کرد و دو تیم از لیگ ازادگان نیز به رقابت های لیگ برتر خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23974" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=SmVVNjp0g1M-EUS30eKaAttygDK7i5qfnqtwVxLH7dG23tX6vcebLHPbBxUJmDPHdtY7qGPOmkIYLWSsMLuTzgTykuFQiQYiX_-duLi6tJpbWiNMaRavkW9dcPGkGhFUR2r_fyHx1acpJoNDq8D5Zf0a5leQ-17mjfex6PiBp2Is3rioZAJ8kMr3XF6wo4Yz9WkA7lxBHDr7_e0LLHTQ_ZV3te--Mb2oSGQYy1aUuMz42O26ezk8hoTDI-kwTxRkhKpJKq6b9YBfjeXiin5SSMDawKF-M8BlmNKjduj1ik19G8hXlClpC9CTmm-yNV6RXuJSuxaVccVSstBiqzQHWnqk2paAsK2bpI9qeKHmtVCgRU42ER_JH9hssXHTF9E3a7sJlL8Id0w7lFsII3hwRdWx3UJzFSG61VNM-swrwhzM-7_2sEFwqydgdCG25mwqItxjJrRInMuBZnPf_MiMSYtXL2-2_grmDKlGEy-F0TmmmfAKEx7m5WRxWY-DjYZk02YpaHwWaZIMCRmFxW14BdKkOLZk9LYzip2xurJ98gekeJfjEUxgAqTjEO0E16GiGbhh79ckp72q8tLiawayN2l0SMHkRZeWUrmPevMm6WFlIQJfSTkNq1zfc44iyfSBxtBkyUZl3WjfM062gm1QbIWEGzdiCUvhz_rzWRWNBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=SmVVNjp0g1M-EUS30eKaAttygDK7i5qfnqtwVxLH7dG23tX6vcebLHPbBxUJmDPHdtY7qGPOmkIYLWSsMLuTzgTykuFQiQYiX_-duLi6tJpbWiNMaRavkW9dcPGkGhFUR2r_fyHx1acpJoNDq8D5Zf0a5leQ-17mjfex6PiBp2Is3rioZAJ8kMr3XF6wo4Yz9WkA7lxBHDr7_e0LLHTQ_ZV3te--Mb2oSGQYy1aUuMz42O26ezk8hoTDI-kwTxRkhKpJKq6b9YBfjeXiin5SSMDawKF-M8BlmNKjduj1ik19G8hXlClpC9CTmm-yNV6RXuJSuxaVccVSstBiqzQHWnqk2paAsK2bpI9qeKHmtVCgRU42ER_JH9hssXHTF9E3a7sJlL8Id0w7lFsII3hwRdWx3UJzFSG61VNM-swrwhzM-7_2sEFwqydgdCG25mwqItxjJrRInMuBZnPf_MiMSYtXL2-2_grmDKlGEy-F0TmmmfAKEx7m5WRxWY-DjYZk02YpaHwWaZIMCRmFxW14BdKkOLZk9LYzip2xurJ98gekeJfjEUxgAqTjEO0E16GiGbhh79ckp72q8tLiawayN2l0SMHkRZeWUrmPevMm6WFlIQJfSTkNq1zfc44iyfSBxtBkyUZl3WjfM062gm1QbIWEGzdiCUvhz_rzWRWNBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ماجرای جالب آشنا شدن اوسمار ویرا سرمربی فعلی سرخ‌ها باسنگربان برزیل‌ و لیورپول؛
پسربچه هفت‌ساله‌وتپلی‌که حالا یکی از بهترین‌های دنیا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23973" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLm1iF8HSEcLdl2i_TJDuNTDcJL2KnZpc97ry2bgXVcekwpyeETQwNSrGLL_SV7nSG_TjDw-yaomZRdjtgc4kTmaQr3e1tEwL5S4teLGEvc8JLrSbpR2E_JuOZ-c_4CeKqoKphtdvk7Baizn0CpiWxEUCxFK80AvqzougnifrNi0nYAPrGu3yRmvoW8m4TFOwoB4lnwLOBN3dSK3YB1fpUdpvJO8EnQfwTHpKvYRcF4KFvjusqtZhm-yeqc_DGlNDzJNkwR5iBJmGtuTp3yM7t8-fcGwpTa0EAFdcTlEevrpIk2ziZjld5TmB_2JZfE6nMIkoUH3yRm8VEN8-CJNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکوردداران‌کمترین‌درصد مالکیت توپ در یک بازی جام جهانی؛
پاراگوئه با مالکیت ۲۱ درصدی در بازی با ترکیه، در رده هفتم کمترین میزان مالکیت توپ در یک بازی جام جهانی قرار گرفت.
‼️
ایران با ۳ بازی، تنها تیمیه که بیش از یک بار در جدول کمترین میزان مالکیت توپ قرار گرفته است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23972" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJTnP7zdP33z_VmBBDSGjDVrgbhx32bVftzrIVjySxoLcid67jXNOxkbyOq03Z6qPZSNNhauF8V29pJG81ZZs0oDrxvyzmAax5pLy_tbWt8GhWDbXVwvFJeFiUdsVqH5aBd00qtCts35QdNmc-5IYgtorKrtLcDEFFpZVMGhdoMIKJ4UtIz5FQ56rvQZt1R9HBP2NzqOA0b39k_f2eV23mMHZXbi84aB8l19ClA4y7x-XTnQAfxY5Av4QDtCWcL0JqoZgrOZy3vEqWNy8uBHbiHqjsrgH5fz3DeZ9d_L_iyIMFhci_lKxSpwoP3PTTfV5MgMd-bTilgueLz3znkSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
فوق‌ستاره‌های‌فوتبال‌جهان بابیشترین تعداد فالور در اینستاگرام؛ کریس رونالدو با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23971" target="_blank">📅 12:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3e56w_BRo_ed1CgvfpqM-NC2nKHIYwrqAoKq2IfraL7Q2U565A3uTsYjV65OFkr9jOYyzPYVpwiLQo2EgHqcT1Pr9hk9eW2Z3pP0CP8-q0QwGZiGnlbxo_DBJu6jBVBk8u4wXezUu9b774Mj33ernqSqKR2zV8_w80nSOcW2Kq5aUICnprIfmLg8WHgjyl5Xgt9RaOr2WHvW4UxhSxQ8NbBCt660nDphCQXnqQokSY_dhcuUkBqzIRuOzkJfbK9pGTzBH5BdO0gHdBp-eXT3snYzfYFboLNcjTDDbrSx0rDd2aqq817UMVyhs-HsdWKAmyU0zEiwrqtrOiCZ4xlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23970" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23969">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d78439566.mp4?token=eFzU5_BEqMIOdGa9g8AifJzTs2OYeAE5vSbQkA5vRl6S2xrI0YyVWPzTW70pJF9GL8p7-pcGYl6JD4p97Jk9KUxF-u3jYMGaj2ow99J74OIa7pkQX2PPTVIgD9N8joN8fODJaET_1j_dxn0YhRvHShduF7EssGCQbfpNX3zAYdCZ59SdjEqsMyKKNsFCjGF5NjqC_62hd-LCQziyaD5GG7vr_t3swqih8FmaJ_srzSfZ-S6QI14E7LIxKxGzrz0cRrKgdmYvE4wMAfdqNIERfh60fLzxmUmKoxdCzvYVMhbxkuxVeuCrCqglqQZ_yeRgahZrj9H5WASyeQBwxtIkcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d78439566.mp4?token=eFzU5_BEqMIOdGa9g8AifJzTs2OYeAE5vSbQkA5vRl6S2xrI0YyVWPzTW70pJF9GL8p7-pcGYl6JD4p97Jk9KUxF-u3jYMGaj2ow99J74OIa7pkQX2PPTVIgD9N8joN8fODJaET_1j_dxn0YhRvHShduF7EssGCQbfpNX3zAYdCZ59SdjEqsMyKKNsFCjGF5NjqC_62hd-LCQziyaD5GG7vr_t3swqih8FmaJ_srzSfZ-S6QI14E7LIxKxGzrz0cRrKgdmYvE4wMAfdqNIERfh60fLzxmUmKoxdCzvYVMhbxkuxVeuCrCqglqQZ_yeRgahZrj9H5WASyeQBwxtIkcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇪
بااعلام‌‌رسانه‌های‌بلژیکی‌؛روملو لوکاکو دیگر ستاره خط حمله تیم ملی بلژیک به دلیل مصدومیت جزئی در بازی‌ امشب‌مقابل تیم ایران فیکس نخواهد بود و احتمالا این مسابقه رو از دست خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23969" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23968">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد
؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23968" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23967">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c204841a.mp4?token=YKcWRpPjfCHrO-2F6JhoZb3Zad465M3PSEcvYFuJk75WPsUrkO-OBaSY2-73L-ZewLp6U9jnWDhPA9FZVPY-HtKIANAN6dYso3-Cd3h6k8Wd1_9KtY5Xk7HEjxxJmIq8DFg-J3Zu9nG2GxeEog5C6WqF7QsBf4gBbxkrHD6e9O3OAxF6dfW3tasj8r_HHN41bkoildwDmR7D5gr8puCclPXiIIjlPr_5uCCHiCWI0AXCdey18v6-4R7DemI_qsJGu3bpcWIddb6oO6h91k-HKWw7Gkce-OlfLzTrh59xBaton2J86DWaU389xazJ_xVOwcDuZK2bQhYpAJ55ve9hAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c204841a.mp4?token=YKcWRpPjfCHrO-2F6JhoZb3Zad465M3PSEcvYFuJk75WPsUrkO-OBaSY2-73L-ZewLp6U9jnWDhPA9FZVPY-HtKIANAN6dYso3-Cd3h6k8Wd1_9KtY5Xk7HEjxxJmIq8DFg-J3Zu9nG2GxeEog5C6WqF7QsBf4gBbxkrHD6e9O3OAxF6dfW3tasj8r_HHN41bkoildwDmR7D5gr8puCclPXiIIjlPr_5uCCHiCWI0AXCdey18v6-4R7DemI_qsJGu3bpcWIddb6oO6h91k-HKWw7Gkce-OlfLzTrh59xBaton2J86DWaU389xazJ_xVOwcDuZK2bQhYpAJ55ve9hAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فیروزکریمی‌کارشناس‌ویژه برنامه جام جهانی:
خانم‌های ایرانی می‌توانند داور بشوند. حامی بانوان هستم‌. داوری بانوان از رانندگیشون خیلی بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23967" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23966">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVuD4MRKyo937jXO1k6e4oGHLLYKaeQ4XgJaJoZmiDYtCFcWuoaZqn-kx9oLKhf042h9XqC2tuy15lY6rA3AA_0dOYJYNiLmtqgsm7iLKwLVPhbuhvyinGpQjLDpthsl8nzskknGs3GjXzi8ytCK5uaJzHVwUjB6NYjQiSdHkUwqdyIPmdlN9IC0FtHjJVmLNoHsJB4LcuHsK3-ygK2jMWKr-77XRHu-g5-Mot4_RboJpKpfTErzQAKI6HjtM-cshq_GGG2NGDOJdu297Ld8uQX4qxxDE5bKkv5W0QkLsyCuuKe3pf0NZw-g9FAT1tQAcCiisOz-1a3Nm-CQEhU2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهادویژه‌فقط برای بازی ایران
🇮🇷
- بلژیک
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان‌دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل‌مبلغ.شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا er31
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23966" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23965">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6YyB3C8ZqFOGHuXZHeGzIhox2dgRhmaHXrTBE4OpakHxxmwzNpijjqmEUIJjI0AIBRakdHdgPHPAOJlyzGjGG5QGopfFelXybviG_A51o20SMAHvwtik32nOTwKsNRkGkpbQCXIwjIfguyPm6Nbv23vSLfa-AgUnba06y_QoIXd8Bs5dNW1lRcXTv7BN7rARHvfN5fWP7vbevBY6_vS2c4nChi3hqhzkb-1BkLWW-vs82Ng5mIMMneGvtoKQWlMbMHp-Oun1UEEQixuixCxkF9EjoHugk8m2BY_pF8spJZ8FS2cBNMKt0XdvqpAg-iqi9NwGD432K-qQ0Fc3KyRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
طبق ادعای رسانه‌های بلژیکی؛ گویا روملو لوکاکو ستاره تیم ملی بلژیک نیز دیدار امشب مقابل ایران رو به دلیل مصدومیت جزئی از دست داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23965" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIgZsA_mTWr0cQFyT1o5vSVkSIz7I4KK4w05mWwav8yx5I8MYncoD9EGaTht9TXBCuqkFlP4-W6hgGl5N2PsS2U0wP3zGsxV70ExfnlQcYV_KO1TlvUMJVB4XDrXxgxGj9OfnL1hj5g-Io_gpxSAseBTpTtji9MfBuabAIAYfXUy2CT5a8ilGjkAU8RqBn8N7GKOnB6_Dgdz3rUfkJhL77w7sr470J5rnvNxE_7CEzVvzYfhHxR7wxdLJPoAP1rvEYdpk_xHZ8f_EsgtnrUmRsbAffrnaDxc-Q5fCowkivF6_2wC7ZH8zoCducTX0abUWRJ3KC4PuydGPP4oMervMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23964" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmAz8XWI6zu5xgXdJP-Jel1z6FjiFw8aAraS_ump66hb6x6NjUON_1ajTmwYetXl6l8GPS6Bg2QwBT_eTmOZMieBssXgxDLb33tJoJjpMNm_DhSOY1u3sSBpYkAKww_6rHcurrAfGwbAyR34sW5JqyJcOBOHxNlpUOLlQge8yy_A8MBJFW0vBORiQoZ_JNouutPTAhbCPeLv3OV4kYVgL1jn2Nkh5FM9z8UFjAjiuUc7TqEkfVYig64h0LeuBaYCR00bYXn9dk85xZm-z30Va9ga_cv9GBerBgN7E4sY_ollnxq2PnGnTQCay8cvDuLVCgo_eNpp00yqqdX-fZ29yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛باشگاه استقلال امروز با وکیل‌ایتالیایی‌خود تماس گرفته که این وکیل به باشگاه اعلام‌کرده‌است که نهایتا تا پایان هفته اینده فیفا پنجره نقل و انتقالاتی آبی‌ها رو باز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23963" target="_blank">📅 10:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bsN2EGRdzt_Dv3QE0D78Q4eYRWOnRU36S2gp7pWgGvr51nOLIOFoh5DzWHoyCkn3OMhJaEoUMQD0VyK2CHfHYcjAvRGWQYuJsca8dPsRymKCiNWu6p5aS24aRFaAHC0Q42wt5JGce9XHayk1bFPb15Gd4pJy_BZAtmQ4_syuPhn_xyJT1YxK0J7fp7B9JAvVikHw2wfY-ufUTRXqn-drOZWvc9XwmGallVuehqMfYzrBxPA5ZxZ4JlxCs7KzL_HjaYeajl_zgD-RrYn3JS_0lVsvbr0w4jKkfBO3f0cKmsL51prUoyRwAnjC7TazQzv5kv0weALK1tcRGivjBvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرچم‌باشگاه استقلال تهران درحاشیه بازی امشب دو تیم آلمان
🆚
ساحل عاج در جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23962" target="_blank">📅 10:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rax1S2ThfEDX0VcH3flGfa_1tsnoMd2ooFj13OQNjFhEtWH7E9ASojyJI4cS1whky9x99KgAOM7hgltyzcXf7m2zFgRKICSj2xgr3BS8mg34uGricsN9pLaXURABIlKBZ-v7UHqnqmKQ9rQinr_8PAZJ3ogTyavxu9w1UKMggeAJTUyy1CDdPOcuGrJkzAWI7m8XS5I7NqhJl3uxhIhAbkxx_W8jbIdWXIk4Eai-uCNpHNV-5cws98YEQWP4tgx1gQT_JFFWCg1XHIVOJ8xIYNy9jXdNkLylA1VXoIyyWHlx34Eig8Xm9C7oJR-JQah7X4cN2eDJPKZ_cvqO18fmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار پیروزی تیم‌های‌ملی‌آسیایی درادوار مختلف رقابت های جام جهانی؛ کره جنوبی فعلا در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23961" target="_blank">📅 10:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=QCefCO_7oq9LkN7NA3kzXbaStI6mq7n2T5bJnAJlA81w5pnVHNqzXkQv38oKBPIB7in3Lka7BMiU2HOM-naBXZqC_IeaKV_tv_5GUn4CgJi65JuvWJ023_tPEQpm-wZdDQK1JM7a292rUt5p1FRz3SjAWE7VS46E_Kh7uef82f_NJNC651hiShrfbwnlh5fyrNLLmb-jO1-bPH7ycjaCxBwp9Tkb6Ff75Rqb6e3icJW6msKnQr5e_VMEtXqrY90GfRg0gafE7thBM5U1YAWMCWcX-QjrFKijUYDaap2boBoH7HlA8V47o32QFklbsqlyk3M9Zdsdf16jv-OethwUqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=QCefCO_7oq9LkN7NA3kzXbaStI6mq7n2T5bJnAJlA81w5pnVHNqzXkQv38oKBPIB7in3Lka7BMiU2HOM-naBXZqC_IeaKV_tv_5GUn4CgJi65JuvWJ023_tPEQpm-wZdDQK1JM7a292rUt5p1FRz3SjAWE7VS46E_Kh7uef82f_NJNC651hiShrfbwnlh5fyrNLLmb-jO1-bPH7ycjaCxBwp9Tkb6Ff75Rqb6e3icJW6msKnQr5e_VMEtXqrY90GfRg0gafE7thBM5U1YAWMCWcX-QjrFKijUYDaap2boBoH7HlA8V47o32QFklbsqlyk3M9Zdsdf16jv-OethwUqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر:
از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23959" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZox_iem1rOdn3mRHlUztAXjABhMAWxE70Wk-dHArBl-OmosfOxUoH_1NO2yq51S-E3_aFmkeOkuBt9BBz5DsAxWKf0iWWFRBARJXnfNS7wvBn9G_7Tgmb53SwBvep4HwE9SWTA1S5wRijNq-elA3oBkCiWLl9leHuLlAC1Jvt9H79BOLjlzaTYeuCj6igxTFT0mdemvnsLzftXWd4s7SRJeSHiPigIFrQMvRPO8xRrHaxYBXZKuNoUwVsXx8DOLZbaC6ny9QYobe2wEdOobgZpV3uemKAGa4SLZUEIbQWunRj5EqCStGRGJAwaHN4YchF58oTd744sxaUpjJdI98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeGzLUAYwY5N1PqkoRuMRBYhVOKzu_CYgwxz8Cdsu3W3nDf7JNz5rUkR-y1YmL1-geMowp93Ou1TwEDgYEJFRt6_crrIAlO3P0ojmuVa4A3YKVN-xh0brnD3pSXTr0uyzdTg-yXN2-k9Gf542RhhZNQXBkaT7zFo1Na20nLD7LvchNNZL_ANS2UtTv89Y2W5S4K7X5vTxZOWsMsJVeXxxCtiNFBsZlx8GyWSUaVXW4C2p2PzGLrU6pUk_RF4g3_pcIpKXy_LUIowkXf9IPrxc_9j8Fh7oG4_q5wYW2DuymfiNzXXVScNJoI9Hc4X6fObyDNNfOkEyzb-qjL-qhgcQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23957" target="_blank">📅 09:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgvHoDp3JCg0PBEZ9gmfVD_iFTWgI7RxsrTNHIo8PS8Ai3-RLPQEtRG7tlmGRItTtvk2_LkWru70pCU70gJVM6ECYy6zhgHSpJ--ipiRpitrXOOS4q_bsFZ_Pw9oPtwJd8fJsL71XhAKws_KhVyFjGwH4SolN70wKEJpAyOl4-TULNLggZEKNfUZakucM5W6HwHlXzTnKhSD8BxXt9pdnzLyipsVyHEElxiup7ebs9dbrggHGpjZF9Xu1zjnl6VKaUBs-lVoQgZpJcsTXquJhq8pFT1HoKpkEV0p0zUoOGSZBqc-f8b86EqiS2GHpkv5NZjPGv4F9rzx9NVLyKUWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی‌تیم‌بلژیک:
مهدی طارمی، سامان قدوس و رامین رضاییان بهترین بازیکنان تیم ایرانند. رضاییان اگه 25 سالش میبود الان در یکی از بهترین‌های تیم‌های اروپایی میتونست بازی کنه‌‌. چند تااز بازی‌های او رو دیدم فوق العاده بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23956" target="_blank">📅 09:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXJdbWJHSxMpfjW05hkeXk_aIqPl6yEE6pyv8O1htwxfxVpFsjut7fgwe5Whan8LPmqb-FmBp4-NNVQ1dCdblgSinPmj2QehABoKYO6FCfyR4ndpy9tXlcaGfJ_5vOz_RExUvIONRvc-si2yAtXU7hP_HLTvsM4mz6HjxUqDAMinT8UOs2Kt2gU6uBSy8glzUfQ3U3buCn3lKLLKVWOhahDW0XVrFqTyKVrcQh_hUEmr7KqiX6DKwzxPkagHjuhBDnBm3fCLqxhr0mgYNUmN79dBXtvQQtAnAJYnqVfamkTUVpRMogBsW4C-GEHZl0nwNoCnuG6uTdd-yyyVzPQmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL4FcC-nWkWb306KvSlGiO0ceiwnT23p7C_KA9GM6uKhbbsLLaWAhnbpuG-eBj9CGzXaVebkrcqEjCsGR8Bf-dCuNv8bPO4EJU68A2lzWlvgIUwa6QjSLrZKx9YNuEIZIqclwgJ9xyOkHUqAwnSVL_IHKqgbYOtcMjUTR3TT0gB7vV12rif_G0kavkyRoInmUkvjfWjSc_yEIgcqzYxRNvwBFvsm_jdWnbIKkLMOzhv8PrkpBAm_McZkBvWwDuOJ4EAHJZOI_g_RSKlSoSX7UxXvr6qoAw8KYXbHxaFLXV_QSdUg3KXRqp1egc1usKhsZUqid-SaijKD0EZyAKbMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFYcfF6NapvZCC6C9nyjAdXECbQ4E3h6hFggLzoJdhLxQnwOofw2udxxiTH8NjPh2KkbMvT8tEUEvl0Rua-SSDTKBcA9Pf6fuC7Rt31gramEt-b2gTWelpVMkqj4KV_NfQ-G-Y3Nzpp82JciIrryrZQG_2sD61eztcvJb8pPpEbnYMua0waIbwo_4xqrmNbTpGuyFrpcbQ_nTNmzvH12z6dDPVbJy6ffPwwHt5oIMQ56t85cmZoKR8qtuond_O9MhNMPp--sJjWfy3pjWFVpDm2htWpJGAMDzTwVMG-yc2YAK81FKWE8zLM3FNHPndYKylpZUOfvGZVfbaG7QNUp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbQivrAQfqDfYoTKHedwa8j_4RUZbwzGBaKbFS5KMfJ9DuO5zCYCAXIkLRQs8rKqPn4i9ru3vUbO4TrDv6uY0uUFxOBuj2g7qn6jBHWFjSGYjtLLVwEHxOhuXQuURKMJgh6Gm2CJo46M7690X0MBO9KyxR8Tf2w3oeyR-dcaGqXBxkdcRxVEResZC0BFy6TwN4Jmi55nttcsQtsPAIlMVAR52vAlnrnfWXgsEQ_rVzbJxBtQ6vlKsfGSF8rbbhxTWbx54VSKVMNQSBXES20z3U1D4O8v_jhHJbej1uUiMgIv7eQLZsSwlo5sCPAFmliw_nb_5nD2sUQEg9fd6H2M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=Bq-MCWhLbMMyHM7QLTxbyadtR6_Qr83fjXLIiM4QLxSP-qLngzzaVkGbqVLFLza55LzwFu-JKBQ1GItWw8jQ2FFx-7C0Em8l8jGVN3ZSYGTsVIWqmrQgSnv7JfI3iLxnupg-eu39yEZ6LyfYSQEf2ytidOV2fz6HTmKMm9zt8WoF5Bh_t--zLTR7o-GP6w5beGjxvE8qHB8X19bs3gxshSf0VePXn_X5muu9muf57Fj8tuUE3zk49WuUcY2edbw_Nf4z-j8aNNIafmRp2DObtp8ghBIZT2IIfOIV9EmEdCE3GANfYMiYqqq9Qmntoi3ZhXl74dPP3z_oW_0ad062mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=Bq-MCWhLbMMyHM7QLTxbyadtR6_Qr83fjXLIiM4QLxSP-qLngzzaVkGbqVLFLza55LzwFu-JKBQ1GItWw8jQ2FFx-7C0Em8l8jGVN3ZSYGTsVIWqmrQgSnv7JfI3iLxnupg-eu39yEZ6LyfYSQEf2ytidOV2fz6HTmKMm9zt8WoF5Bh_t--zLTR7o-GP6w5beGjxvE8qHB8X19bs3gxshSf0VePXn_X5muu9muf57Fj8tuUE3zk49WuUcY2edbw_Nf4z-j8aNNIafmRp2DObtp8ghBIZT2IIfOIV9EmEdCE3GANfYMiYqqq9Qmntoi3ZhXl74dPP3z_oW_0ad062mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCwxuqjdPOPk-z--v88YPYPfEZ2RznJlNEVpY6yTeEYKq80qX1XH9_fZhshq_auaCtFkHVvWsVGKVIJjSeG0_KnJlVZxd8zU33uq0rs0ScCqSKFcGQxKIoSzE0ODbSEJGoA2yY_93aJcvfHbJV6Wf-qXNGFUZ3XX4Wx9HUnNj0sgBx0Rzo3-s75ROGJUuCz7lNHcH_R-CGSPE6YbODSMjIH-J6FRtINqw4kMe6BBFjj-pypyULHa_tiiFnF9MyZAEXBpAAZF-dLOpP6bXf6ASKUpyaN7JrmiEoLOq_ywQgvpC5Y4CFYOfaCyifd3tITpW0pTvNxutsdquGkkIF9vvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌ گل‌گهر به مدیران استقلال اعلام کرده با دریافت20میلیاردتومان‌رضایت‌نامه پوریا شهر آبادی مهاجم جوان این تیم رو آبی‌ها صادر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23950" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5U1cuxvT3IfPoScQhv5pkM-hiNrQTY5J6fOfm4AmR_7jc0kGeRZqHyJrd9J8tZlZnTe3XFoRW8MrGtwm1VGa2Ms--ba8xTMBeetjQltdG0vw1-Yb0kWeXYCUYO4oRjupzH7D8bXbg6GyHR648rrDeGwu2spPDOnqHAvnkabC8Qht4xD-3Ylza7vvnRFP7duMSS2vHqwroJ0JDz39JPLj1MrGtwy34e3dytEQ6ZKuKXgCgMQiGfBKGL90Ze2JD9Wcy9fqXhgQ-cTORUPpmprJWpV2jnA0jA-I_p32w-p2V0j6r04gN97B4dIao07yH99_ADU8iMuQIqpXDMA__nZKtVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5U1cuxvT3IfPoScQhv5pkM-hiNrQTY5J6fOfm4AmR_7jc0kGeRZqHyJrd9J8tZlZnTe3XFoRW8MrGtwm1VGa2Ms--ba8xTMBeetjQltdG0vw1-Yb0kWeXYCUYO4oRjupzH7D8bXbg6GyHR648rrDeGwu2spPDOnqHAvnkabC8Qht4xD-3Ylza7vvnRFP7duMSS2vHqwroJ0JDz39JPLj1MrGtwy34e3dytEQ6ZKuKXgCgMQiGfBKGL90Ze2JD9Wcy9fqXhgQ-cTORUPpmprJWpV2jnA0jA-I_p32w-p2V0j6r04gN97B4dIao07yH99_ADU8iMuQIqpXDMA__nZKtVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23948" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP6V0-r9RGBcjGXxbEDW2D1cSu0lz4cITENYuYdmc2QzJTANmePapmF1P4xDSpfXU4B1ghwfWMXMp65xHlG-z-rU9cmqXEm_vOYXX6PSoax6l2BpRUf-_tQ9omQzSg_26Z1QMUaPWfoa_elv2sVrSYgTENDaYiq4_fbwPLhF1A7x56OkgRXpc27YEWQ6LbkqS2BiXRbvX5F107FhkbzwfPvCHH-wo6TZlM5e9cEiZgVyDsh9d0OoX8Z5uCjsptvlRWeSTHbulsGyuIPAzE6cIhi2liWs7c3ejHohHai9L4iKaCy2ykJugiyPfsZF02mhmCAS_vu9mWy0BmoirN76yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
گل امشب تیم آلمان به ساحل عاج: ندیم امیری بازیکن اصالتا افغان پاس‌گل داد. دنیز اونداف بازیکن اصالتا کُردگل‌زد. اونداف در دقیقه 60 به زمین اومد و8دیقه بعدش گل مساوی رو به ساحل‌عاجی‌ ها زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23947" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4ptpsIZj10hfCbyK1I5I01BheI69BDZ3W7c3ukUYMi79NJ7DMsZersKQLgoP4emvQT6o8rtSpZqsBsZPSYkt9hQoXejFvgvE2Xfis91-U3eWEgY-K9AfR4aPM4W_zdvLU18Rug19kVKUVYPk1jC0i8_bMMy6k0rJ-y4TRu9z3kkeB7-JhCacNvIbZVc6ij3ttgss2KPid_qHq6ntXxiRPPgkBnXIhp-ZarwHVBlhtIh29XvmPigTLu2cOv9a_yH4vGS8pTiAPT9M4qte72iJqmp3RTHs7hEN5DDgmSe7xOdpaSoVtu4HPurukWJqjo0bMw3_KHEoviQdxK6-DCaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23946" target="_blank">📅 01:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6Ynw1PI7uTwquyzRQFtqDZ7J6Ipi0Z9ZI_vqh3VlBNXkoawMqQtlio5PIUF2THGdGqD_v2uUuXBmQfh1FYGwiSlIQIIqT9BOlj_QQUXbFwh8hV1Ce0j1z5bG5M5Heo66NAG5O7tJw-Xl8wnUhLVSORZ0x6stGSd35bMtZlfKP8SQAeQQQV6xRcm9rcFMl0elIdL582Is7zlFWh9a2_YDyAG5burCMDXEYfFrO7voDuh2OobrQMsETR78-dlR-5GUNtTzk0ZfzkEGzrzAWONW8gkkwagJgke-FPM4HdNx1hWhSx5EhTqjSMM6Br1J0nEDepgE1V7FEmMzHy3ljVDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی سرمربی‌تیم ایران به این شکل نشون داده که ساعت رولکسش رو پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23945" target="_blank">📅 01:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=WhMdjARRhxjw3ugmGWkslsrnudhgrzxUEXvLWipY9O7jsDE62EaknBg0s7dk9pDgcS242MpogXWMrw3MQJsIzUp6NRzhgV3OSdfGffA3BQVfUh1znOEgc-53fT2QtUiTsq0LbfjCakL8GBEFiQ_2BV-7D091fVuyrEtqKsx4vCYxVWMni83WbmaevLp2a28kECjGqE_xVQlssCSuSRjMjMFZpIBD1d5jyTpTcS2yDP2srVDwDKEGzkVC1bjvUrdglQtStXV8p992z3yQUFSW2AnExdVeX1K-KXQvLGYTDUcatS-p_kCGV9nWGAGzOSybd2n_W75gVdXZW5sL6zKtbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=WhMdjARRhxjw3ugmGWkslsrnudhgrzxUEXvLWipY9O7jsDE62EaknBg0s7dk9pDgcS242MpogXWMrw3MQJsIzUp6NRzhgV3OSdfGffA3BQVfUh1znOEgc-53fT2QtUiTsq0LbfjCakL8GBEFiQ_2BV-7D091fVuyrEtqKsx4vCYxVWMni83WbmaevLp2a28kECjGqE_xVQlssCSuSRjMjMFZpIBD1d5jyTpTcS2yDP2srVDwDKEGzkVC1bjvUrdglQtStXV8p992z3yQUFSW2AnExdVeX1K-KXQvLGYTDUcatS-p_kCGV9nWGAGzOSybd2n_W75gVdXZW5sL6zKtbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزهای اخیر شایعه شده بود ساعت ژنرال فوتبال ایران دزیده شده که عکسای رسیدن تیم به لس‌آنجلس نشون میده‌که‌خداروشکر این خبر کذبه.ساعت‌امیرخان
🟰
خط قرمز مردم ایران
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23944" target="_blank">📅 01:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYzuQ3NiB-g_UHmmICyJsdNzX-vJWlCBgMB2GmYXpaAFAf0hEll5KQEhljW7nehAQp3R2fwi5cuA4DOTHyZAxbVdnvFUfcJPMImcxbKjQwkaa1IRTf4rMJZA5ZYAHNb5_NBvzIxfNBGDhsbIUYcgFSlxW2LOzT8ClEx-PQDkBfKJjsecqgmNlpLxwd6qqJVRs4LAbxYx_shcBgLf1djB4RP_LWlFFqO3OeiX0Q-Cc5Wfnb0fq_3VrewveuJGD5ehOVKvyNISTkZfkCM7cq5NaqiwbeyoO_y6fIfoF5zCzjXORJJ1vYGEUJQst2M4ue27qFL5EnqDpmP1aVGvyRRINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23943" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af4fvtGpzjyLHnRiNohcCK1w0x8M0JD9qGzZ2NtGfhUwi1L1RjLuYCe0TeKzlcl6z6h7gbAKKVikREiICffLAtrudCrQRpMpLtX9avOC7sVXoQEtk7Nd-KrjLlmdrv2-uELOnIAq0F3TCJvqCLN9_w8CLdYhSrnbWVa0Apfu6vO9n_qXEIlG7zsOntdyCkoXuPMtRr-z39IQoLqcjR7hDSyFW1J78zEyD9Q0pJsHJYuw3lo68P9COvnlthIinXCFQVTDZXECQ441LDBEYxz7ctmZ6CiYhOTDB8QbG5Ss2OLZvhyyG0EsJrgKMC2Ld9RkVSLMTn5RJJaZ3n-8dnb4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مهدی‌ گودرزی ستاره‌ جوان تیم خیبر امروز از طریق نماینده اش آمادگی خود را برای پیوستن به تیم پرسپولیس در نیم فصل اعلام کرده و درصورت‌توافق دوباشگاه‌این‌انتقال انجام خواهد شد. احتمال اینکه فخریان راهی خیبر شود نیز زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23942" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=B_3MZ7IXB8Z-mwGURG6QTqytcfoUUbWALOma85OS91YAdxHWa7jlrpRgE7JrmvzXUSRWSUMqkndznLxwrlLyrDZeIer-dBpfkYI_NR0a8zwSyCD50Zz-wlRET71QBJ3qW30Bd05cXbuouWJTkIYwG4beZNK4AlwJpgzSulxsh6MdWoVkcqSMaDuuYepTxlt0JapeVW6iElEvfAgC1QUZLFTnf8bmklTBNAH3RIfQ0_9zWdheKsHFysUzonrJcQnSFVSzkcznJaEFPYIsPjRJmkZXwOr2qV_65doV_HcM3dvu5IqRZguS6Z6Yg98BQloex7hLKUBO03L0TGihBMek0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=B_3MZ7IXB8Z-mwGURG6QTqytcfoUUbWALOma85OS91YAdxHWa7jlrpRgE7JrmvzXUSRWSUMqkndznLxwrlLyrDZeIer-dBpfkYI_NR0a8zwSyCD50Zz-wlRET71QBJ3qW30Bd05cXbuouWJTkIYwG4beZNK4AlwJpgzSulxsh6MdWoVkcqSMaDuuYepTxlt0JapeVW6iElEvfAgC1QUZLFTnf8bmklTBNAH3RIfQ0_9zWdheKsHFysUzonrJcQnSFVSzkcznJaEFPYIsPjRJmkZXwOr2qV_65doV_HcM3dvu5IqRZguS6Z6Yg98BQloex7hLKUBO03L0TGihBMek0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtDgpqK1-Ju4C-u93tddkIrwDPDTPUYZ3MIynt_Xtgcjj7DpY-II_9ebbYN1SxJve83B4fC8rKQyg59pMd1hOnRW8l38ShK-WhlZlsA1-VEnSAPMbkNekRd-Ash4MEy-F5c-XHcdp1hH7htgmHMN92r0BDK6aiCeUAOjwF8eCQmQDB0KmXxCgd6o7RgLtBRgQAgzaObC1fxzkVEuZxtSeLiTOpD_L2DwOrrOr58fzIJzoMBBrY2nIG0JYvxN-3jyH4ZqbMJjo2BbdcQMcvWV0nd_hcnvto4qno-DxPqT_UdcvaR-Yp3fJwlY93FFRwjBSPT-4WBRsHSZujexT_RBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpQsRU2SWrDp4A9JyZfv_kddKtEfW5z7IZH5LN3YHzaUskxwSqmFMrrBwnOjVJtUk9O11McpoPdw01Cay6j9V7qcGS5jpTTrRuMjXhgQxRpj57IRvcfufG0DLreDqLY_T9MepKeWhHJUjQCLll4meo1_19ZqEu_Xrew7G9kp4CmpxPcOtVIL59Kb3yx4G6FsLFzHeFzP15L40Z4MI7WmJDQenMdfG3X9AOtaittl-0I3YgTnsCqG_Y0kpZ8LvboSPYq9djGy4yYVMOOHUBMtNb2poG65K2rmpQgXlf4cK3Ro69KGEMwPOnPgJjzRFH1ug1Gaj6Pb2YI2Y8wgILRZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_x-cw5XXnbDBi0VU5t9tXg4NLPCphlRoTu-zi1QoiBkuRPGamP6uqQb1vMnUqmNpZ5zMECdmDhxE6XU4c-YZ7UyoQcQn7erYjJ1OgHmpXYahhipZdPIh-RvWemSbN7s8LE82IB1FLEumHuYps5JHKFdLXCqEURqv7WL_nESw92aWTuIfQxYcphnV-SK74hdk1tzd2XlTT0qYssNU8REJG_vgCmdvnn9_8KzNNzTXIPSt-qPLTxwOkTsYd5GTAt2HqaCI-N4jWiob9qVIQsA9xZa65Yqm452bWDKi73wHz8s79iMSzne4X8xBEg8P-0XpbcGvyWWHKYf9e8qbN-Kaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7jXPry-h6vozDZ9AmnujCKzTg-Yeknj5shotfLH0yyDARedHFtXyOeGFrrMgRR26lgArYtQswgBU9nV_tAswGvIWUjGVIRlUl_CZOTR-3jkyF2nqUuMkYtsE6A-kBxvfeTPn8p5_JBtwaqwP0dWJV0XjMxTOqWBThyjo6vWjS6P4crj_7RKqu4NPZuVVwcdaDP1_xjw9bi4iFsZAk8aSpTsumS3ETYg7WxIbck-Cq1KgcTXBJ7So0COTltAbIEKCPbtQix7Hil__4sDLd7oN6udHRDbLHO9JqplWFuZH6Z11f9aR_9pZHgjwHGVvJtQoeStzzfrEway-maIa9qgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kJTapmUrXBlYycLZWPTOywPNMaHgy3j5xTLHFQu50icMjzqsPR8TQd7idkrjxIak4FdtUUHLfa8xaNGjfU3Xuyl-lQwV3_d97MXJ-lCTHoleaSQxblWR2BEgofVIDlhejdE5Ue5fg8iAMDoaVD-fsZSSi9fBG6nb2gEkXhuxCbUBeQJQUESBBw_RhRmVHOX4zB5e_I_1aCS4q_KCC81cCxaYsleQI_axBONaRFiATfmDlmVdN1SDoiBQA4j-eVmOdRJGoVI807REXn60e_x13N62E_IIUioAvENkVeQJjXzv53f8HvMWz0kilzXtyvT5NFFbn7C4Vzt6IyAjTh9JH2GADJUeYINAnhOnnKgBhNH5Aabk4HHTcGEz_ajzsWDOEyS0e2QuHhPexQqirAoW--MEXaO6H_-SPMifyB35L5vnW1BIkYbGtvd2X07EqaTsgLJtinKJZS5EoQkFY51PBtUBJCkjsPtJW5SgWEnJWqLP2n5pbyZ0PAafYEcZxuzyqRRjQUKuj5_ODYyJFy-XVte61KmRsUrgctEP9iBtNr28HSwbmUoCmCQW5neOhGtY2jBwK4RBBn7XNoGM9_l2nEG9CnX4qp2JKUV2xY5lC4ms3R2PqUGfrq683FA9p7RvH2d466b2eUK3mYpcKLbrcqo_9MLGNR2CXb0uW4bH8qo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kJTapmUrXBlYycLZWPTOywPNMaHgy3j5xTLHFQu50icMjzqsPR8TQd7idkrjxIak4FdtUUHLfa8xaNGjfU3Xuyl-lQwV3_d97MXJ-lCTHoleaSQxblWR2BEgofVIDlhejdE5Ue5fg8iAMDoaVD-fsZSSi9fBG6nb2gEkXhuxCbUBeQJQUESBBw_RhRmVHOX4zB5e_I_1aCS4q_KCC81cCxaYsleQI_axBONaRFiATfmDlmVdN1SDoiBQA4j-eVmOdRJGoVI807REXn60e_x13N62E_IIUioAvENkVeQJjXzv53f8HvMWz0kilzXtyvT5NFFbn7C4Vzt6IyAjTh9JH2GADJUeYINAnhOnnKgBhNH5Aabk4HHTcGEz_ajzsWDOEyS0e2QuHhPexQqirAoW--MEXaO6H_-SPMifyB35L5vnW1BIkYbGtvd2X07EqaTsgLJtinKJZS5EoQkFY51PBtUBJCkjsPtJW5SgWEnJWqLP2n5pbyZ0PAafYEcZxuzyqRRjQUKuj5_ODYyJFy-XVte61KmRsUrgctEP9iBtNr28HSwbmUoCmCQW5neOhGtY2jBwK4RBBn7XNoGM9_l2nEG9CnX4qp2JKUV2xY5lC4ms3R2PqUGfrq683FA9p7RvH2d466b2eUK3mYpcKLbrcqo_9MLGNR2CXb0uW4bH8qo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های فیروز کریمی سرمربی سابق پاس و آبی‌ها درباره‌ اون‌ویدیو معروفی‌که ازش بیرون اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23936" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM_jXLY8cSzeNybjmLsY9W4wW9r7rhPx_HriOnorrOsooqTvdGhoxwPRFkJg3MH9CFNadR7eP0w8RI4_VujLz9OCDEoh4TAoG41EMdtFwrmb3B4Zh82sj-vSvfLTcuNmL6Sr9e207OH7fSDiKARK9b_x6BeDC8uxDYaWBq5ZFVy6NVj_uu7404DowHMdRgQfnwTYec1KjA-TC7H0Y0hSFZ3h1edau2mK-TraqDJ2ScKB08JiSxLAIq7X_9UrETkZD8TE6xQTQvzeu-m1mjsnrKKYUqttI-1izyI4yx-ULP1Ba4XWzpo_XolTpzxLZM2B2f-E7SMgNQlb9-mkJrQ-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23935" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apsSCAJjIJ5edSwSVFyBhGozGb92OEO7JAeWKe9mOH8J_rh_haSAL79oBmB_dPjWxzqKCgd9gtz5UCW95I9xbVAslIlLXrC0vXeOMvFgTojo0VCUC9Wk2lf9knkW34fz1TDm9d_ljdrb5KGVP8cjCRNXsZ7hyX9wChKZEK4pf2r4A9k-enrjhxR45P3N13pvHA8ucFKsYT--n93qCcCwE_0ugel00VQglGx1Xf_hZRFLZdrySia16s1_MvJu7RkY2d2Fgks0B11Ab-sJAjMt7x-XmZm2hAuJy94CjrF-dVkODvNrGc6O41hf38gc4UYL6e_HVvlF4C5A5BnNbiJteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGD1_-ImH0uGRWmBc2x5PlGVfdTdWpw9EESHK4qCI61E6XkRQUme41ehdYpBbCH97E3GD93lvtkom7K4HKQrrz_AuKcqsdjEIffr-qi6hwhbvRuTk2ap089p0H571yjdgbZaVBGvnG0o07NTyRS-9eOx1Gi2j8YRMs2F8ceLvDWKeMgOgke35wdVlVRY27AsFOI1JhzV8zxktUL4kG-pWTjnD3e0sO3xJCVB36AkKRiGDAVCwPpWOpTJBkMmaqJ_R27gecW1v7igBd8M8B-Ejj-GoYFtwE8k4hk6ltojEzUVPQdR8MIm_JAJsSqDRpI3CLkqsn5GsVw4TskLdFZ39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okVVOb5X2sVFxRxnJ-ePRAD52FP4zOndGjcPx2heIWkKe6oassPKH__AO753PllWXQ7vJeZSKwN0vgvoBZ3GJ6ahR_2hWf4bW7hC3HikAJd87zA41tIMhlwC3JS_YZrDJQ22KdkstX-Z8alXBGAW9wgGSyXE7-rvr6Rg6TQgwmML_LkJvGoIzVJAe--jU894HkRyUjbNC5QWsHKZ1vtr7muEN3T3YH2uQksAyXKHfkJ5jdKVfQ5Xpr-fpnZhfyAyGgadraIcywqSYjXLDsQ00X6W8EmI9g097pXR6PytCF9JftTLF7PUjthrIMpImHtmb3bzaKbmDF1Ri-f8tAbpsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDaPpdIcN10PlUVPXLvy0kdDtT2vM1BjqFYhH1MWta2WQYbe6OVoUNVjNu8Bk-yvtF324-hNhx0jgfa9AF4i_c7n9fpuCSROTOjYxN_6Lf2DEQ_KGVwnv2VU7DIU_1byxetCLvu_jOTuhXDvtouPmiramSmtXuuJpHJmP-2yPfU6VRq1mzcwvlZsubhiFeJE5AWdmZz7MOU-sJHHFO3imdTXfR8vk-IrYc5VzUQWi8dk3iKaODbQfKQBUoL2TPnKA62GZszbYPu6PLX3H-RrMfNKuxqT3Jm7tyUGIpFc9ITEjTrqjd_z49nXtcgRFUYgpwiu61FEJWiD6jfIp8BndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=Mk1YeB10U7Ta4G_JsZalPF6jpRspoBcvmAFALMg45PY9uvqcMLoTKw6o3qEFwu8nsx3fC3c3swTi8pqr5fU80YnicdwunMeGgmGh3c-Ajb6Skk8x_a0u1dDpPv3AOLhmtPtnivV8MrR_Z272BQZpMpyksduOBNTwY5en50n0kGZIqT9b24E1bqT7VaIMoVOZQgksHgCDZLLc28gpvXO-hjRVtyxNE2FeSU7Hr8l6eRhddseu8MfIpMy4XKybXXSRdd0uQ9Urdkap-vXMdhjaoa7Pqfesd5vY4Y38HC6Kx29xQbC1eRBEisbLrCNWleiiHi6GeZASPdozjxOlXQBr5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=Mk1YeB10U7Ta4G_JsZalPF6jpRspoBcvmAFALMg45PY9uvqcMLoTKw6o3qEFwu8nsx3fC3c3swTi8pqr5fU80YnicdwunMeGgmGh3c-Ajb6Skk8x_a0u1dDpPv3AOLhmtPtnivV8MrR_Z272BQZpMpyksduOBNTwY5en50n0kGZIqT9b24E1bqT7VaIMoVOZQgksHgCDZLLc28gpvXO-hjRVtyxNE2FeSU7Hr8l6eRhddseu8MfIpMy4XKybXXSRdd0uQ9Urdkap-vXMdhjaoa7Pqfesd5vY4Y38HC6Kx29xQbC1eRBEisbLrCNWleiiHi6GeZASPdozjxOlXQBr5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=I_qqoiScW9zSnPCNYZIZGGynsOv_gcZAVJiN4QADg7KVP8J2MCsbzR0XuJpunrUTrlJQkuzBFkTGgAIgQvepvFqFVb5_ueGRFcXIlAUF--ek2tCsanPQ0N8CACNvq3myo2TpZjb_0ohI9PN_G5frqBUKl0izyXPhA8QIN85u_QhaI5ZM4AVxYYb2iGgnA6vJUWUt09aLLlSAOloCNB8mjv_xAoi03ObOMRH6Vu1qrIoKhzgJywMQh-HjMLz0aCUOcAoHVu8NRK2Pud7xAJocnKmXrbx-M5ibNa2qsPT2SkgT08HIF3DPilQuy9pzEICJvVc5yO2r0wmnB-15lyrE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=I_qqoiScW9zSnPCNYZIZGGynsOv_gcZAVJiN4QADg7KVP8J2MCsbzR0XuJpunrUTrlJQkuzBFkTGgAIgQvepvFqFVb5_ueGRFcXIlAUF--ek2tCsanPQ0N8CACNvq3myo2TpZjb_0ohI9PN_G5frqBUKl0izyXPhA8QIN85u_QhaI5ZM4AVxYYb2iGgnA6vJUWUt09aLLlSAOloCNB8mjv_xAoi03ObOMRH6Vu1qrIoKhzgJywMQh-HjMLz0aCUOcAoHVu8NRK2Pud7xAJocnKmXrbx-M5ibNa2qsPT2SkgT08HIF3DPilQuy9pzEICJvVc5yO2r0wmnB-15lyrE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNInUcjelL7F0IqutO8uwm9iCLjuk_J2enso-qPr7PIj9MCobX-iVZxq-a0m9OV9gv9qFXXYMOTIL9E8YjCg6f7SU9clXPqdcs0Y7S0lKwxVw2KoBqkT8TfFXWIRuJTCT-b11jfjJvZJEAU2JdBNGKNCONTgzVwa5aEPGmmvfXENfAA8cQpEz6ppLy4ulqb-iJobZOLvxMVMAPY1pj4rsfbKdI4ewo0kmD4FJlFhweZMOygOpPGu2bqpGH2U7hB4wIMDR-hzkVKS8_WBG1jiXORHJFFP5nwpmVrf0UHxGb8n2CusxTobJRJSxzv5YRxIMhBXqmAIlswhzTbjJoSTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTcmvQeEQ7biKqatP6eFDIIAp2XxUzCm5rZzO_vzn3Zpq7H6E02H9ra0RmD4YOOR8ldpzIzbHzQU6ma_dmlwJylSPJOTAVAVgfDCg7Kbyn-RhvgscPlTH9pz12SIVNo8VrffIwbx6oc_23iJsw-S1qCf5EDRXgWUaNvQqVeeXa-idnsuvxNBbgNmQlD8w78_1oaXTgphQUgKbbd3LsuHnywQ-GyOlRAbkUjnsz6Z7i_UV0YcuADFAmeG_I3zbxqLq4r6PQ2vfPR0t1KvTpS-hThrJZubpaVtytidYPqDJK93X_WS0Ym2zwDmXKOTOw2K0m0TLpLm-6rp5uMxHoK4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CadFFV3I0vJvHWsJrS10LN8fX5O7xlYaWwzyBZDTT5fnvjDl9Xj4IW-i1FN5AtE9Y5wfZ01iGCrjP3fbA13GOdXNPjP_1BcbXDTJ-1yKXu9N3L4xHpl82nQ78wed5xZ3i9_nptC_L9Rh4dQfEZ8FbY99Qi4fhQydadSmYGCYJzXTwiLOwUJIbDPcNY16mdiMKRoPCWrH9RSqUCGRd1GNY39vfjhCbIMYnXxzC_h2nVDNfLIUDHpXsDsVX7plCeRzzfkIlE12qVDuAH6UQihT7-BNe-V0GXDbKBBXoTq5GR8xN7xqVLiN8RmEPQAGYuFUpkcEjyFMJuhtwdsXKT2S0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23923" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=s-TQVTGw9ahmBE78YqT67zp2-UltMFDjyctpEpWb1HnTgUxgYNYkd9PETO3XzZBwFRl0sMXt7WE6PJbr-FkOCuTM4ARvOF8royifFLh0Grl3CU7Wx_CBzg-K7AoETL5yto67Bxhog6MFHQ-UqPklfYFRBHr3GMZ35D_CGXwWv77MBrHZ12oiv0hWepZX42d885CneLs6ZTyfwdMEwCQcdejiBv6X9XeAmQKGGBhUMXhsMCFmlFcQzkCoP-GYVNGjkPto3cZpf8LgII24WH60HVieO_hUAUg8cukqA8B8LzhrlmTFKXC3bS0ZPRQ7vfmHXn24OASxOdI4xcVJi7LHBG07wg4hyB5O1CehPkn5Mgw7gONhwiTD6yhP6w0IX6vg8YjypVNcxFij7L9WrDlneG4GwJ-fmRUAM3KM3Zc7n4UAJCBSGEJhktshKxB1-MVmZhu6Ga0sB2KyVg8-kITqkZNYA1DYYzIpcP27TNlVU-FllRIjL9pPiKQjUZhJAU6H9fDkLIKNYZSBqbwSl019vKmOUtQXjRa9Hkbm2id0A3RCKIBarYMg3SlUn6KaEednwY44BpPuhKVPeKurCB7kyM90RfFi0Bj37mKvT4VLYdTg1RlRFsFjkrwwcNZRu3WVsJg185Oie7YxDnrBmrVUzk6IwBauj7qrKK68UUkveIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=s-TQVTGw9ahmBE78YqT67zp2-UltMFDjyctpEpWb1HnTgUxgYNYkd9PETO3XzZBwFRl0sMXt7WE6PJbr-FkOCuTM4ARvOF8royifFLh0Grl3CU7Wx_CBzg-K7AoETL5yto67Bxhog6MFHQ-UqPklfYFRBHr3GMZ35D_CGXwWv77MBrHZ12oiv0hWepZX42d885CneLs6ZTyfwdMEwCQcdejiBv6X9XeAmQKGGBhUMXhsMCFmlFcQzkCoP-GYVNGjkPto3cZpf8LgII24WH60HVieO_hUAUg8cukqA8B8LzhrlmTFKXC3bS0ZPRQ7vfmHXn24OASxOdI4xcVJi7LHBG07wg4hyB5O1CehPkn5Mgw7gONhwiTD6yhP6w0IX6vg8YjypVNcxFij7L9WrDlneG4GwJ-fmRUAM3KM3Zc7n4UAJCBSGEJhktshKxB1-MVmZhu6Ga0sB2KyVg8-kITqkZNYA1DYYzIpcP27TNlVU-FllRIjL9pPiKQjUZhJAU6H9fDkLIKNYZSBqbwSl019vKmOUtQXjRa9Hkbm2id0A3RCKIBarYMg3SlUn6KaEednwY44BpPuhKVPeKurCB7kyM90RfFi0Bj37mKvT4VLYdTg1RlRFsFjkrwwcNZRu3WVsJg185Oie7YxDnrBmrVUzk6IwBauj7qrKK68UUkveIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLMtzws6Al2wHoP58dvDEXQkpkaOiyCKr4rNdKFc-XBXGHQJMgb9eNorzxurFdr-m3pmrcsIobVIbrSIvMbz7pZv6K_3AtOe091OJNNxQ8RcUacxZ9MgI7qSg7bijw_h27UXmEvif1D2q8oqVtOoSzMQz_phJrKSWpc9vGZvHevEoIY5Oti7SazbCwLFkCdzckIf4yRL3YuzLl4WJGrUEhiB_Gb5j_Mp58QakbECxtDVtfnXUykuapToI-WTTh5x1lHhinNlStVHmA_KFug4WtM8p8XY6dzpsJeOE0YOetCG6PA_v0rejUErGFwXJKDhzOCbrJTRD-e3Hhl_avjAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkIA272vVzl3HKllknmnkg4Fqe9zYs7NX6m-jWNzLaMKFpZPNMfgB8w-wta8pQe4tSVONIN3Usd_Pcn1ZAFnCCfoPZfwhvb72KMwB3MgQSmKUZ6kF4M2Ec8Gk15SsN0XRKVeN9ACmv5oRu-fYsVJdwx6Z-FKNGI_oIQjChipbJp1jX1rhWZvMT0OGh4BZRdFYe_X6qzT1iFozUgoPTGBitVf2Ha3_qo-pcef_F-5YTAU0WYaUc5SsnymRt-m2Bw002gb37hFJVNdGeCG8mxG5MuhC3A_gvexbAbjou7fAQ76Lc15_NAA5BaqTsl6BePnMw-PHavuFv9PTXcskan1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROadM26H89d7bqrmZp3d0gQ2JocgPJRioZ482VcvBGsD6X4217srS9qpUFU9jIyuSyyZiGe5iu5HsqjqlP0v23qqsfgAcKbnp8XdmEEJdJaWjKE8aqKaSa93LsOLdNVQpNz6RojKH28Oz8DfbeUSsO21swBChIDDhYgOv8GsOqPht5LhnpET5imu8KOWoT_jZvFZpyzIT9nJbPtCSIzCugJ8mPXgopWveskHOVsteEtKt3n30GjnpD7v-lkrjuA8d5wiYNurJwo5PdGvmILxC79IoLPmH6S8wE9i4nWdc7IE64f4H2zCDrqS7QFUZQotI5Wq1zAFZVvFCa-A8w3ftA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=W1u2xOrn2kvhm9sjkwA_gKYjTCv-UduUiP5mVRaRkjbSX7Wzr9PMOLjKHuMZZQRTg43uoTEa0Dq8EE4LgGVrXSFdhSrGE-aAbRtSTcHaufkk-UwnsGh2zkaMleWk3_hXe0Pp0PJDWBPWBBQchA3ga3kYqtBOJdTCDJpZAHMGqO1InRpGUEe90fyzfZvXXu4ubtBqLNFQrK54s049mkIdp-caK0QeJZeKxvvY3rwzeaUUkMkk4rNJzRHiSNZAR9KR4-Z3JibpU38dVNJmWSXmos8RRYb9jpt3yAh_EO5ArfyGqMTJTwvYPwbfrp_rN52MbiiHSIFG07-GgNwWN1hFlm9PeOxPXh09L4iElWdlhqizY8k5I9_dnba0v_ww6g14jYJnbRaZbjqEe74BR3i_9VtYAuOl-SytNvEPVyJs_lgwy2dnFRBeY9liKiSO_UcgC16_aRaLnn4MJKD86MtP2b6Yb3kgitQ6rYL56PyUI9Us-h2NXo8OvGpflqxmVsB5C1Ap66N39m_wsqPv_IecFCaypHgUlZVBZTd5d_N0BpTi_6GyjIwdm_vBhVGZBYzS3aOyOQiQPA5R15Gaij4NTVCeEIoA7w2428MfcefD1wGGhGd27XpBeVyS0yr91UIrHf26NtWiAMKxC5-8ttdO4vHiZ2sedw3GglJMD-MFbyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=W1u2xOrn2kvhm9sjkwA_gKYjTCv-UduUiP5mVRaRkjbSX7Wzr9PMOLjKHuMZZQRTg43uoTEa0Dq8EE4LgGVrXSFdhSrGE-aAbRtSTcHaufkk-UwnsGh2zkaMleWk3_hXe0Pp0PJDWBPWBBQchA3ga3kYqtBOJdTCDJpZAHMGqO1InRpGUEe90fyzfZvXXu4ubtBqLNFQrK54s049mkIdp-caK0QeJZeKxvvY3rwzeaUUkMkk4rNJzRHiSNZAR9KR4-Z3JibpU38dVNJmWSXmos8RRYb9jpt3yAh_EO5ArfyGqMTJTwvYPwbfrp_rN52MbiiHSIFG07-GgNwWN1hFlm9PeOxPXh09L4iElWdlhqizY8k5I9_dnba0v_ww6g14jYJnbRaZbjqEe74BR3i_9VtYAuOl-SytNvEPVyJs_lgwy2dnFRBeY9liKiSO_UcgC16_aRaLnn4MJKD86MtP2b6Yb3kgitQ6rYL56PyUI9Us-h2NXo8OvGpflqxmVsB5C1Ap66N39m_wsqPv_IecFCaypHgUlZVBZTd5d_N0BpTi_6GyjIwdm_vBhVGZBYzS3aOyOQiQPA5R15Gaij4NTVCeEIoA7w2428MfcefD1wGGhGd27XpBeVyS0yr91UIrHf26NtWiAMKxC5-8ttdO4vHiZ2sedw3GglJMD-MFbyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj16sucjgD20zuQaawOHJDvTh_aNTMmz4yN8ufr9jk0tnebDzT6QC42IFpNdNbCTtqu3JH4KT4c0ejO8hBDDa1q8JL4uTvoV_mEbCYVEQWZA43TFUlyTd_owePtlZZ06a7ta4-cf5bCPlOGNPcOhTgIeilJg3pNrlil9RT-EhlvT26UgBv6WRCF700ffKOMn3NWhPbMT9oQQ7su1FywIb9bsL4LSMhEgwM1L4bC0vwNRdbE6vNEEN2TNTgix01c3je3pfCFLiCX3tojHHpLZjUXz8qDRkVJlxx0YBfh_iomemKpL6nQKWy0u-BhlcHVT26cpBT4nFyGAtp15z9U_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX3unjzZLbqoSHU2PbsL5aUsr6Z8RY4TtMyVz8OK4TGOFNcYgEYFZSX_uqL8d4lf8fh1el2I9L8ASKYpe50_7-fN4_voEKBoapJHUB_rM0ofBfvjh2-XmMyKBFwDoXz3cbWQJIdjGAXh0ByITaSEnMQSkhv0vkCKbJwF_QgSVea4BZHpHTuDmg9KKWvTPx0SCZsQrZMc1YGB8bHphEZW3Ih3AIABDq8VJGChNXQGP_r5t2PB8ZAC5ywh3cC4G2zMnbaP-bJXxKr-VYtt9o1KdybqaMifOBEY0YuplfViTsgGSxKFqKsJTZdEcGBM7_coyWaJfwhabwqvHMR23r95zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=MZefql0jSOLlnMFrjyDInuaZRyMts8LgY5N_YRdeHyKwZOD3xsDWrL5qbsoVgvbFwWLkgaB1BrtD38_rGCM1DFL-jj7vA6Q5_Y5IvKOClsCCheqBn1xIOp7QxBQtPVWGCQQ_cyUjvZdr26wN9yBrLV0oP9VuYpp1_WAqjiZ8YfW-dn152iis0KnF_3H2iZBD3mxO-uxePRp1Fh2gwJ0eSOeCC_hcxPEivnIH9_SO7G2LoeC6U5PgRqPeJ7Dw9VmJkdY9x2gysGUX9Bv35Qzg6sGAUtf9qwvtpBehPViXR5DRfsV9nqnFfu2MMojx50NWWKZR5K3DpCUaYYPj9cQTUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=MZefql0jSOLlnMFrjyDInuaZRyMts8LgY5N_YRdeHyKwZOD3xsDWrL5qbsoVgvbFwWLkgaB1BrtD38_rGCM1DFL-jj7vA6Q5_Y5IvKOClsCCheqBn1xIOp7QxBQtPVWGCQQ_cyUjvZdr26wN9yBrLV0oP9VuYpp1_WAqjiZ8YfW-dn152iis0KnF_3H2iZBD3mxO-uxePRp1Fh2gwJ0eSOeCC_hcxPEivnIH9_SO7G2LoeC6U5PgRqPeJ7Dw9VmJkdY9x2gysGUX9Bv35Qzg6sGAUtf9qwvtpBehPViXR5DRfsV9nqnFfu2MMojx50NWWKZR5K3DpCUaYYPj9cQTUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=QmFKe43kOhxVHjjCWSxpH91LmOiAPD27wrAzPhO2uAks5moabnjh8MBCFh1xElR81TkMLoqqfX2OLw1TOxHqQ7l0XWCWj-nMFdbULCDiJ0ZrHLdAThtYRiwuH9zCvbsTn9jziWOVPXboUHoXH0F6CpvW_Xeq3M7KdnlPtRMdr0BIHAePuRh-UbOIVarN2kOyMCmkCZx4wnyMFQXetK3W5YavT6CbORSlD1phr8BEo1Y41nURlsw2wqAWTxHoJyVABuvB8SnwgZF_37gid76eS-FB_OH6LZlVNmmJPFDWhKaPBBsL0PJqHaAzzfbiUXckfyDwe0YmM_5NyKJPk4PDRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=QmFKe43kOhxVHjjCWSxpH91LmOiAPD27wrAzPhO2uAks5moabnjh8MBCFh1xElR81TkMLoqqfX2OLw1TOxHqQ7l0XWCWj-nMFdbULCDiJ0ZrHLdAThtYRiwuH9zCvbsTn9jziWOVPXboUHoXH0F6CpvW_Xeq3M7KdnlPtRMdr0BIHAePuRh-UbOIVarN2kOyMCmkCZx4wnyMFQXetK3W5YavT6CbORSlD1phr8BEo1Y41nURlsw2wqAWTxHoJyVABuvB8SnwgZF_37gid76eS-FB_OH6LZlVNmmJPFDWhKaPBBsL0PJqHaAzzfbiUXckfyDwe0YmM_5NyKJPk4PDRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9CtGd2ILW8x-Btjt1H8ilHvtQAd-BwkEorccqAldTJXf1ZLPPf-AQcxajjwBGgIinxAeHL_gC4hSBVPQxfDkC-PY_-wqN2mQVDfZ21BoaRVvuQSuFATIx_oBBkAhfatBxiooubiF-aN4r8TOJVM9CDueUwx7MRySp67d34JG5Did8GaR9_WfwQ0FAWa_6DjMmbHQuJHv3hbg5iem7WaSk5HoQynvRw_MnEU6Jq7qsDwdsqE1lfNmWP1hqWONsgAo4SQYld8Qq2awWpZ_aZpUUmdUXCmsctk7a2sAujVDz5wDO_OiIF1rS-5hEq7_Yk9puGYsuIHzShk3hbrPWO-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYSA2_sF1Uo2x2bXOUYicY8UHuF3J8Yjdy-ED8P5Ae9XaIfC6bchJXkQOwmpPvxnd4cL4LBSfoBCyEP5jeLK4rxUq3drL06PLQMO5TwJTRpwXhZ3iNSnQih6Cuq7RSg-Vhn4Nqy0mNZ2IQbjOu_ICqnEnuQB225F3B6qE-_8faKw8XoI70Xxo1r5P6lKXL_eVBHgmPKP687hJAJq2epddxSKkkuuzvDPy45mAxG2OLZNtWcdEpfsxYGjUzVBXJeCBMjvVfyDJfsaPzg3Qt1w2WyLZSY77MJPHHQe3frBF_yHYAoJG4UruaKRHyqOsGfA3wL9fAqr36bEYVGHtryxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=TICQUOYz9htK27CD7dDtTv07qqaEB5SoFOVtbwedTc3DbAxqzn1lafTmprKKhUqtSDK85CB84blvjNofPb6oZnSN2QLnQjaZ4JQLLrI9xSDqbLR4bY-LvqdeEnDCX14A6gjE9S9HRdW5r3sDgM5zVUlNmLqEOGB0IGSR07Y1CL_y9jbfFCTwwb0gwuYm56QP0bgklaEsy_37wm6lnDty61SmoaG1_fDRD1nCOfQWr7mPaDXU4No1-EKUTrhR2bdW4pVn9v6PJKzCOABvUUEh6T0fOwtTPF36nSb348P-1eP2OIE3q4Sf_jCRlNJcUQ7sM3r8oWZ47A9NEq3x53P85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=TICQUOYz9htK27CD7dDtTv07qqaEB5SoFOVtbwedTc3DbAxqzn1lafTmprKKhUqtSDK85CB84blvjNofPb6oZnSN2QLnQjaZ4JQLLrI9xSDqbLR4bY-LvqdeEnDCX14A6gjE9S9HRdW5r3sDgM5zVUlNmLqEOGB0IGSR07Y1CL_y9jbfFCTwwb0gwuYm56QP0bgklaEsy_37wm6lnDty61SmoaG1_fDRD1nCOfQWr7mPaDXU4No1-EKUTrhR2bdW4pVn9v6PJKzCOABvUUEh6T0fOwtTPF36nSb348P-1eP2OIE3q4Sf_jCRlNJcUQ7sM3r8oWZ47A9NEq3x53P85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DODLu4SsK4MePtpUkI3_MGNRUJXTcrEL9rbEbWHv-HzNKKjzE3SzzXRkrk_sD5QLWLQtsi-tNBrf2Ocdcl3GTdTe5dRYZofp8OjrCM42CtI8uEeiXpRG3KZyo_ePe-Djm6eo2NRN6-ils2BBuuJXV0uPlZsP1lySU4l6hxOkNSmAiMPiw5mcMFLoQGIurJOHRyoUkIC-ef8p37KqA2kdbFhR0EGSiJp9raZg7OcQ8sY9cURyBatMfsNS56KsdlTqWZ4RBAV8o0Z3z5HXuJPALM4YbxRRHy6LEWjue8zRzxlW7uHdHSmu7gqng8j_m2UH6Rlsz0BpA1cS1LbQXffxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoVPs4nGgIzkkPDtw5J9kq2V1vaJ2KBTk60XnsFMfjArzMCZRqOMLj9N0WX2cpeSxc2kOrB1vfAgL7kgLq_qmwSEi5TWzIFR9AB3OfBT0TSkO3-GcCDgXLgM1WL9RXbIe2Svy7lY0ujHlkH9rzU9_w0Jd-omCYRJRHrjbomt_IUDy_Jt0aTgrDTu2RcghmO2wDL1PCKLB3iUWGPqxiFPDu8fcjt8hk3Yz4G0YMrE17vP2yLSRZ_MlaB0GKrfo3VRvxgZSzDCgWaobvs8TqBRczYl5ytQooUcSffSwdGmTgkw5nvNQ5Z3xsJ_xSNoSXi6lzMe8RoL5umw22BP-ttffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOZ1BuuKnILJ9dzg-N3RiwK6eq0OxSJapQPx3HeX6rL8G_Ez-FyB6tkvk8G3oqVDh5FKyM4QfVwiBX615NDkxP1Rv662G-R-a4yERXX3h-x-ZPjZaiut-7BVPt59z4IuZWMIu5yDZbFdwYM04rC7kIVKXIwkJJSUWPIOxHBHk06cby14rcbO_s5iNlpot6PA82piJxUdzMMeKNITwkIsnCaqHh84zvyFAqFqT7KYcfwhKamHN-m2qCsHE2cMFXH5y8h77V7QHufhFFwSAZPB7lUzIFOIz78UVewtmZEvGqh_nNFo2pLfDzxasjhKMhkYsmwj0oXuyu-U3_UJqILO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI4mNIWBgpRtdTji8iabCzls3pCwYQa4O7ekzw45yLOa7LO9flU-5dJg5YmgHBsCY4BnDodHvdBsxGJ7uKo9PTT2aGXawTOEbzi0QX_k0bA7WLyxZi12ce-cG0yh1CgP6NKf2nJrR8Heh0qdG_r8n4VvIgaZprZxISS8RQkzGnVy4aw_uwNVB254hmFTwiZsvgIS_wE21tQnbljB3tJ-LORrkcS-JcRlfOsnSgLkSRNnu0DRuKOdhW-koWLOCZjQKgvLt6nBT5mjFpPD5ipKBfYkQxYNhcTrHqvgVhX-miicqp_JLSPemNJcCxX6skHBneWyezYusdTEgpId9zvdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=a4JTfSFJXj2XAVFVKrL5VF8xBti4zS1ZEqxnbGoCGBKhYwbi6Fj_UKnNecIcgyDg1jK8tgje2kfNGnPHLQLNx6kEQQiJPlFlvlVbuxCYkYkV2EIPgikFo3KlZb-ZbYP1dg1FB-yg1lJ3abHRqKeY3Oa2efWTDq_QMbhdyoaEAdB7jSIJ2hXtv0BT9a_J5r-An2_QiPNwj5oDTbCR7LnPaKR-0tWIKWkr_W1JkpNXPWxt_68z7HfjPBeTeTFLcTftPwa4wM-gghNAYXs9GFPTE1PKWpAjSwHvdHWXojGhq9HEpIg__2gC-6TU3rSx9XNtdMNWjINlFbS1oVBAAOhhNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=a4JTfSFJXj2XAVFVKrL5VF8xBti4zS1ZEqxnbGoCGBKhYwbi6Fj_UKnNecIcgyDg1jK8tgje2kfNGnPHLQLNx6kEQQiJPlFlvlVbuxCYkYkV2EIPgikFo3KlZb-ZbYP1dg1FB-yg1lJ3abHRqKeY3Oa2efWTDq_QMbhdyoaEAdB7jSIJ2hXtv0BT9a_J5r-An2_QiPNwj5oDTbCR7LnPaKR-0tWIKWkr_W1JkpNXPWxt_68z7HfjPBeTeTFLcTftPwa4wM-gghNAYXs9GFPTE1PKWpAjSwHvdHWXojGhq9HEpIg__2gC-6TU3rSx9XNtdMNWjINlFbS1oVBAAOhhNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7R4c_L4QBsoiOvWx9564fvYeRf2Ig7qvAs2hv_vuOxHyHhxu_KTBtimi0jt17rXfWd8Ozt-Xr7XSXlDESNNK01J-UE2ChozIYpTmqc1vC9i7-f7o7o6gL25tNFLrtrg2rstWN6lKH5K-c7Sy2SuBx5kA58fnbY-t0Aj85PfRMKt3Zej_y5d9hYIK2EBhHsOkuf2Wzo_HXs_wscPcgLJTl76-IYJbnYWqAio20_OW8qfyqh_aNVQog-6Qe3r8mn-2M9yGHaKNwwKk7x0evjifm_H-_P4e7yoxPaRM5qDrA8W5oUV7orX18VJlNGYDwdZjogDfcQ5hmjYdCrJOKB37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqI-BTcID5zJmsRWgIIKHQJzmA8in1uRzAD-sNgGgyBbWdcHzwOPepcak6qiLdyWWganGiCfMmQ7khVvJFlzEPSgmYxeZcsFcI170G2ufwgF8i-AQAZk7JUDCwD5xTAsGV53cLWhXyNVDq0rQWnEINwLDo3oxXuGTth1jY-CXac8n6FZJEdUxyZuR9CVzLZkZF9TXGWnEZyZxBTrSFXSWjuAYuC9xx_dPNheK21goKxHtpBM4zvWbMvU4xiUxqE9OtGNMF_bW45qXlHHrnMWddMw_GlpgztIWKeGLA4kDwqmcxfrMxfnOyHUpqCfPTPHlbe-rSwsCVQbjRkkuuTwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml_wYWAvrqdZf2y4qDiL0-J80myLEAtJ848WAY6njgRrxy_J2GCXHo94OQUlRdiT9FNei4Nmf4hDyDx0G2VAKdrQrVhJfST8-M1kwcrWY5MeRA1uOw7lsSHeuWpYGJIxMkgga214LYjgOEtJweCSbiAjopojm5H9WdTil1qaUyVz3bfxUmXfA3ccI-gYl3mltwCgJggCDRZm98nGGvptcorlTkHwVXiCsDMRhXBqNs4e3FfNyaVkuRjQ5DyWp_44LgxGhyg3DIJcBHvfJ8AiGDozq_aj_K_gpwgOJjVq14yySsFQ6OSKSc32kdfZls1HDZRErAozHcCsVOWl2CunHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnuZnLdaW6oHQCo4ely1qbjIlh00Ps3TrQtwkIOlO-ZKtKix0piZw0Ve2aIwxJ1q2UJGLkjK8dvTS5qPxaB11Dg_TyYzshe4BGk9b2rlUznCjgA_bczk3Aj-MGLkWi5lpn9zjcZKTxu31oGR5J0u0XCocjtz0E-GnEPrGO7rTm4gL9AIo-Nvn9hnymaYK5KZANAPeOPgLHbvYK76-lbC8mn1hNmeDFMCPNzRW3f9A4DdrepgCd9y5cloBLGN8eb1lfcedhTA3OkIcrI1xJB1fu3kgkzJs6u52J04uybm1wxDaVnU8HNvs7DopIn3CWv0mB7d3yOPOCjby2bUs8ykzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=WgitKQNkaEpj2B0Tsm4Kd8dPyXzW7FG8kdb2Yvmsd-IeStto7zRoKl0bwpJwVWppyufdvyMhq0IIpnHB_lzAn--m05CCtcBfqCCrRH7yvlI1elZLfn5mixMbfhFlAhilbf5KmoahvgCRjuCbmyq-69HHmeGG6-gRl8j6G7lGLFWJGuvtPaQ0uJ2k35fInDDyXcdMeK26jlSrMDSHQPd5b7LOjYKlQe2gQ005e-X1CWGfNeaUb1URHjSxTuBA33rPDypiX7inrz4sDtoBTjPmsWpvXsB9_Fk5itE3mGhMOAJEzJl0rWkg6ipCzlH0qI65fua0tmsar_bbY1n7Qr_fJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=WgitKQNkaEpj2B0Tsm4Kd8dPyXzW7FG8kdb2Yvmsd-IeStto7zRoKl0bwpJwVWppyufdvyMhq0IIpnHB_lzAn--m05CCtcBfqCCrRH7yvlI1elZLfn5mixMbfhFlAhilbf5KmoahvgCRjuCbmyq-69HHmeGG6-gRl8j6G7lGLFWJGuvtPaQ0uJ2k35fInDDyXcdMeK26jlSrMDSHQPd5b7LOjYKlQe2gQ005e-X1CWGfNeaUb1URHjSxTuBA33rPDypiX7inrz4sDtoBTjPmsWpvXsB9_Fk5itE3mGhMOAJEzJl0rWkg6ipCzlH0qI65fua0tmsar_bbY1n7Qr_fJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=qSGEfZ_8CLhSEWOonQ5lzjgIULvxAUPPfcVqCSKQ2ISWdm5mueHmtXCtrFtoyvjRvT2Z-8mmcKPutQ5idoBP1wfTypszUdviBQdsF1Y9-4TFa2cXjksWQmEV1TAaRKGwhaubmHIDu5-GoTl6V3Pmct0lx10hEvzrr9-GiZhXZWEuDXWLjtyUejv6j9gmsZrBZSXtLqR-npGpSTFMaYfRS64bWPlT4_9fxWQ325I0fkxNJIDBGVkt5Ov-zEKjhulk5904Df_u_jyCPj7I-1e9rTnd-5PGFBRDMcqg7dyBWq55iq24yp0StxHuPNgmoL7v5bJ90F2lia-s-0osozjtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=qSGEfZ_8CLhSEWOonQ5lzjgIULvxAUPPfcVqCSKQ2ISWdm5mueHmtXCtrFtoyvjRvT2Z-8mmcKPutQ5idoBP1wfTypszUdviBQdsF1Y9-4TFa2cXjksWQmEV1TAaRKGwhaubmHIDu5-GoTl6V3Pmct0lx10hEvzrr9-GiZhXZWEuDXWLjtyUejv6j9gmsZrBZSXtLqR-npGpSTFMaYfRS64bWPlT4_9fxWQ325I0fkxNJIDBGVkt5Ov-zEKjhulk5904Df_u_jyCPj7I-1e9rTnd-5PGFBRDMcqg7dyBWq55iq24yp0StxHuPNgmoL7v5bJ90F2lia-s-0osozjtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOJ7GkJ9qWeUDqpwnOzs36DDaWSeSJZqv_maZDSkAzGVr6ipTC6haPE8hiC1gDvhkXPgYNLoTa9E6fAtthFJ5I-ykL71symBb4dGICuGtPZpZ78dMDOyWPrdid6UwpdmH2am0tfr-I0u85Caks3873Rl-V4-ZmCYKDqUUaaCGTwJGkeS0QdUnK07mpea-QP5nKoiUYTN2ZD_sL0FgNW4Q3YN3VyL-199COdRWzsVvdHMnGls6kGmOvIWIdHSs8OpquvJuzSXmqODEakkJh5yUQNgJ2E4MfqHZHqhi6EHSV1IGSaCd98mGBUC2ttAqnUqpVx9ylYaKXWLThDg2Ey7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9YAyMrzudaRHweLsIuwICh5abZG5b2slEvTsoPgBujYlJsuhdoptqhXqUeUfiSyFefu42YBEbSXVmWlYbJUcx1daAAOQTfsY22CO2R9sWEdJndNiqOK6AlXTrLIcoyb4h58cVtbz2FyYqRMzT4K-w3H41cRclTgVRU2YOaxEefe9fkwgTsRW0CoINcRDMw4r8EBiImeNmsEFkzhzB38XvkvxFvN2nIH_5mqVmdm-cRPQiACrxFgv5YNh4H6Jx3e5VDlaXtcKA-f2oqYWyMMpYevzojvWBrWla3u5hfS8gvskSpyeCiIHWHN_zCq6VYYQsAM_sfR8M0qlSNWF3edrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td0sN8QCkCelARc4NO7ueSjD8Av45pyk-jyIjnJrO_WHP7F1dr_zOaJFS_fq0gn_Dp0xr3eJW0QVzXHrIYBHzN5ovvoWTK6XpYnt3AS0bJW7H0UlL-oPd9DWWLrRu05fGDHqoQ-G9nuJhvLqVQm-39XfoY1nsZR5d62KfyqCqfT5QhOzE6TbiQChrijFij_Q6XYjd8KV6pIeHUqhO5eV5F6hKPhpkM2dDxgRO69-hEQwOQ4idfZ7ovGPm1KKPRQBFFKouFNxfzizm1TNgwlhsMRAETzSL0XxkrW1Dhq5bMYtBbr6TGO7LdSYzHVnAO-v3vKw0VU_jxH5lpYwuQu7bWmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td0sN8QCkCelARc4NO7ueSjD8Av45pyk-jyIjnJrO_WHP7F1dr_zOaJFS_fq0gn_Dp0xr3eJW0QVzXHrIYBHzN5ovvoWTK6XpYnt3AS0bJW7H0UlL-oPd9DWWLrRu05fGDHqoQ-G9nuJhvLqVQm-39XfoY1nsZR5d62KfyqCqfT5QhOzE6TbiQChrijFij_Q6XYjd8KV6pIeHUqhO5eV5F6hKPhpkM2dDxgRO69-hEQwOQ4idfZ7ovGPm1KKPRQBFFKouFNxfzizm1TNgwlhsMRAETzSL0XxkrW1Dhq5bMYtBbr6TGO7LdSYzHVnAO-v3vKw0VU_jxH5lpYwuQu7bWmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGZrDe_RkQNO7UmtVyrnzfTENGE9AlkVkxEJhzWTrVaVga2ZrQ3rN1xx3eIRLY5EwaeWVMXrn60nbWCOBLmEkye2iVAbM-i3-fMNWrhftWU8HUPwKMTBkdtKyxdL-o9A4hnsbU_SUgUfor9Yle918mPHq9U-6Uzne2tOwap3Yjq4tOkH57RQRKpHLb1N0q-pROm3Ex7L6qMSN_MVQo5XT9GuykODBahEcT5JENSTkQUrR7B03VA5mQLwBlzNY9dEOfecAPlain-k_tzUygGmnujW81DqYXa68EJLd5b4_YkEgbnV5RkHD8cuDgJTZzCzWFFCksyd-zGFltJzEC8qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
