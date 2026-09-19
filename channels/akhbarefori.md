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
<img src="https://cdn4.telesco.pe/file/QVXn3d0oSKEdI4e-U-s8biouUjj9p-uqeX4bnbJeDT3t_d-sOkfNgihB2j2qSg6cTe0z7jnqlHGvtB1u1lW2wKJrJxPRplcHoxTVMIjypRJG062sOsFHKOTk4S-nwHMJ9yv22l4anleSmjKf0rg5UwUu_0G8fAtmWyzn533B6kLukAyEENSdx7UAZrdLO4fREmCvPB8AHGk2JXDxEhpzWlINwTiWGyiPsAAczVxupWCBgltZAVUEjeSPrjG3P4JBkJURzOBIA1KvAwb6YqD7A7qCipizHf1Ozg5VFOLBqJlYkSr2amwqijFnrMAZsUayqCLjifnJg4Z1H6a-5CwupQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-691241">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
محسن رضایی: اقدامات آمریکا و اسرائیل این اجازه را به ما می‌دهد که از معاهدهٔ منع گسترش سلاح‌های هسته‌ای (NPT) خارج شویم. هنوز تصمیمی برای خروج از NPT نگرفته‌ایم و این موضوع به رفتار واشنگتن بستگی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/akhbarefori/691241" target="_blank">📅 19:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691240">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
محسن رضایی: اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کردیم. به نفع واشنگتن است که برای خروج از جنگ، شروط ایران را بپذیرد  دبیر شورای‌عالی امنیت ملی:
🔹
ما همچنان به فتوای رهبر شهید انقلاب پایبندیم و دکترین هسته‌ای خود را تغییر نداده‌ایم،…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/691240" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691239">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713eda6e84.mp4?token=VsGWJeDNHKXCBiMVw-kF2OCnlO7Xxb8UT4G4qbUHbLUZtcmX1NcCYhkftrskr-WQGrMQKNwORbGkvjJZKsa3tJBKHM6BWal5pKHok76CVQGMjYjIzvLPgl7Emjq73LYGxZM-ALPENrUNhx8Ss9FPMogpxDmg8w6aa9oItv-r5HLLIQTeYVVSP_COvQ-FeDC8P1kkDg6ckK12UpQNgPhkNpiOiEZkeS9pOsr-PNWve8_vHtxhzF2S04tZm6b3wxTTBoBquYT2eDREH8d_H7tU1MgYqkEsvdqTInuHwNHvtdf6TKZjg1lLiWNwcXn1dYEy8AvQ11tem6NotgiS5mu5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713eda6e84.mp4?token=VsGWJeDNHKXCBiMVw-kF2OCnlO7Xxb8UT4G4qbUHbLUZtcmX1NcCYhkftrskr-WQGrMQKNwORbGkvjJZKsa3tJBKHM6BWal5pKHok76CVQGMjYjIzvLPgl7Emjq73LYGxZM-ALPENrUNhx8Ss9FPMogpxDmg8w6aa9oItv-r5HLLIQTeYVVSP_COvQ-FeDC8P1kkDg6ckK12UpQNgPhkNpiOiEZkeS9pOsr-PNWve8_vHtxhzF2S04tZm6b3wxTTBoBquYT2eDREH8d_H7tU1MgYqkEsvdqTInuHwNHvtdf6TKZjg1lLiWNwcXn1dYEy8AvQ11tem6NotgiS5mu5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرخ زندگی
🔹
مسیر موفق کارآفرینی؛ داستان کسب‌وکارهای نوپا و موفقی که با پشتکار رشد کردند.
🔸
روایت شما از آغاز کسب‌وکارتان می‌تواند انگیزه‌بخش دیگران باشد. در یک ویس ۳۰ ثانیه‌ای، داستان شروع کار خود را همراه با تصویر محصول یا خدماتتان برای ما ارسال کنید تا در خبرفوری منتشر شود.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/691239" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: به نفع واشنگتن است که شرایط ما را برای پایان جنگ بپذیرد  محسن رضایی:
🔹
ما برای یک جنگ سرنوشت‌ساز آماده‌ایم. ما نقاط ضعف ارتش آمریکا را می‌دانیم و بیش از هر زمان دیگری برای مقابله با حملات هوایی آن آماده‌ایم.…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/691238" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: به نفع واشنگتن است که شرایط ما را برای پایان جنگ بپذیرد
محسن رضایی:
🔹
ما برای یک جنگ سرنوشت‌ساز آماده‌ایم. ما نقاط ضعف ارتش آمریکا را می‌دانیم و بیش از هر زمان دیگری برای مقابله با حملات هوایی آن آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/691237" target="_blank">📅 18:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: سخنگوی کاخ سفید فهرستی طولانی از اتهامات علیه ایران مطرح کرده، اتهاماتی که بخش عمده آنها، با دقتی شگفت‌انگیز، همان اقداماتی را توصیف می‌کنند که خود آمریکا آغاز کرده، مرتکب شده یا از آنها حمایت کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/691236" target="_blank">📅 18:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd708c6b05.mp4?token=LtgXpHxBVuL7OpMyZcmpeaEM2wTQsgLx05ZB1ukqIhkNR_tKbQqYDmzAwKrUoSM704mSRZGd8LxSBRcsjtTWHCBP26UZSZYSzpo37XZ4mooH7SMzgs-eAd5bTxy8M4sJ91x9JAbU-pn0CDWTka8hLw1Q2tX4sNEqESwkYpjCt_Nd_nrYLh90gDIXugBqe0jw45diIRdzEECLtS-guoSC5-5J2syuCweGmKGFjoTIyFdalT6s4d9PbdpGG8f_kYb9UJa4F9WVGqZtT4JE1k4CtvTfgTkl1El2SqjIdHXKHWWsVSh_dM5r4TfgVfCGbJsoqhngfZQhhXWBy1_94PaSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd708c6b05.mp4?token=LtgXpHxBVuL7OpMyZcmpeaEM2wTQsgLx05ZB1ukqIhkNR_tKbQqYDmzAwKrUoSM704mSRZGd8LxSBRcsjtTWHCBP26UZSZYSzpo37XZ4mooH7SMzgs-eAd5bTxy8M4sJ91x9JAbU-pn0CDWTka8hLw1Q2tX4sNEqESwkYpjCt_Nd_nrYLh90gDIXugBqe0jw45diIRdzEECLtS-guoSC5-5J2syuCweGmKGFjoTIyFdalT6s4d9PbdpGG8f_kYb9UJa4F9WVGqZtT4JE1k4CtvTfgTkl1El2SqjIdHXKHWWsVSh_dM5r4TfgVfCGbJsoqhngfZQhhXWBy1_94PaSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش نوشتن پیام‌های طولانی با گوشی سامسونگ؛ بدون دردسر و محدودیت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/691235" target="_blank">📅 18:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aobj1cjjyKPg6KWO4u54HrQVEQIG59OKjKA_fntJA3VbpHZH3mdzlH2En-SR3zBa3qXkdpfRk2q6MkH962TxnjHWdRSlMzfnpYMBL1k8oGdqoT8N-Rt6d-QXxymSTz8lNhy___F0xTqecGDuyzvJnHWaBR5Pk7kTVKPrBds2XUvztHz5TlM2c1V7udDxJV2kJB6xUYal2aanaegLlul_5_rpbPzgs4Ha51ClazuZLwj46B58Tn4U7j0CJ2WlQhd2ssLx0GnQ788JMykXnLnViud-lQwAD-7zjjBjZFNuuyjsrp8RxVR_vPInzMXSKgeLPdHRjNvyDNuTRONgUU-TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8Ls33LCJew7q5iU1IE3PvH2WTGnsA1t1ds9AtDqDlrghFvjeLKsAGf74b6C7CEzf5XUsj4PgmFHXL-Yxq1COB5kair-2EENtQM8lltcgIbutpOMWr3bIk5Ghfs6ygfYGdVI6Os2Selp5HgNZlD9R4JEJACxt8A8UpZZzTpPTczvV0agfTHmrFF8eU32ZJyhdCKG6eXziZsVQ6NwXIYkQYE6hgt0aB8-bn6gcAEMtAKZ8vyUcg6z0v7-QukIDxE87_FXqBFC9xWJOi6JsbMTXjEUVuQdzN3edowe2V03XjTfqKQPQsjudqHYThK9li4qdDtSWuRhlBqFiWe736WsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCU_r-5K5cwS92K72HJL5RJldcE_aXjUcE7MZBEw4iV5eUbHGRdEZ_v15CcGMEFDe4OmJsWPTjIpIXOMREznXdXZYzzZhURDGCp9Bc2GCROlAOek5D0j9UVihJVHTPoL3aMBYQqGzD6UKWBKm--omRZ_u-0bdu_kCDUCG6FOKE2MCsJLTuiHB9d4SdXdgNKZnn3GSioqOnE6pe7BH4TzGKzwnqgygkORbG4XUY1-S-O_lBBUzrvk9QbF32YyNA27RudBdhN-zDTHi1bK3G9I08jHxYW7wf9BUyO1BuLk7cj-efpiFprN4oQZhDVm8lp-hULT0PrG3mCX_TpBUUkxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lucoR2zLlRCRl9iZI56nJVIp9oE67mVbo3ZNeQUbeF9tPwjSCvjD-q7Oh15nsfOUmDhYSDDBm1GhK4t5JTyJFSIb_vcKewlJ4bRNsma5itVdwKP2YjfWgznbu6OonoJLpmGcjavMHj34psRNRVFoD6MsTJEdv42oHD9c5Ui_-lY1urNPam0DiuLFsgyIHVaZBBoW0FuT7YwS_ZnfeMNBuhhu8kVFUCRPAxxuMvUo28EO_6ffY-7MtnA3zRRMV82A2TbNn7Qj4EUmxlGDurxL6I_Zf13dKnwnMMFqsP7Urgtu9MoL07kXaoGYNh6spRwf9K8MjQwcEn87IRuxOHWtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnecApdm_8xhj_Pta1pbx9FXquQbLgdS_PEHg-YLh6K7wr6joSx2TJ26HUpKNxdTHSXpiemjCkwWDJd5SncXid3fvGxaHi2vAJxHbXmnxu3mvrwnFnLifIjNiLufk6D4PbQ1Td1lhdQLyQs1i4s2wTdoFjo5jj1T5cPxmDwBU0fX-Kc_COjOZbIIDcE6nFi2wnHumIBi5fbrjGYO6Fh9DfslFAuCpvzrQIUVhutKP2WcXTzx-9UZp_Cff-qVX0wcJEZVZcv_jdWll783EbKwybvh-8V-LMjTUIJCEeUiq4_WValTkCZo4LvkWSAEaT3iAuVPoBR0sA7n-Ozi-Xt3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5To3_Mxv_sqY9lQX3Tdo9fI-GO47_8Xve__1zY41TIkO1SdbAX4ong5yUu6S_VaS-RT4GBcY5aeADnwmjDTwyJh5TVFT_Frle7AmrgAW0iwTaLa0D56eIV1j7sqT0P43NcOVh3_XmexlidpXwn_dQcNzgD_D9w0-72KZ6FPdkeWXAwJ5eYmmC1LRUxp-UWxhsMHz6a2j8RaUtiGrBYkgLaEJ64ybOBRTWtvT7IUB0EAg81dfRo9u3nEd3u2OY2Y9706ZZ_xyVGbJhUDrq5hnKcY52AKrcVM8qlIhLQG1cqrlKn4UZxeay6rBHbGAq6EUEqq7ELqcIuuyEWdWox7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4I19XYfQ2iZoDZH0nJumtWhjptpC2_V7Pn9Lk8ufPnTNrXHi0k1aXa2tOMhqRt_0lCW38tlqYv0Vjsb0Qvn1fKrZaSOr51rD_AE0mctYxjzf8Vn2hZNpA7T7SESuzHIhj0yQ3e91FhxWNX3osUVGs-5HzxCCoCmWiYKZtvdzvgwYSfjYBjAxWVRcXrSKTNv7Qo5SzVVBDfNp3tNbH0xFNMnEAsrE12u-e0TMgs31UHpi29K94I8Wni62hX_KGvMSgd_B0ITmoGZ_NRtJ2ZxbSA6nemsYEpvDSWU0lUb1C7Ocdillj8BCYLOx9_1rev4MRUk8JzUWzBGJAh4CItxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyiTRsjbVfyrrKpk7Kjt6nYIClY-QBP5h8edM2aAF1zLFFoUF2TsPXk1d8KYT44yJKbmRxXwNKMi21GvnrjYmjVJ_KKkp990ZVh5I2Da30ZVnA2PgsEJjC_artMjQBTefhFAPSMs5-f3XCo1aq6ao7rQhcTt_1PovwSswp-STmESiyeFUm7yA_MehXSkm_A3Rrp_QqPWgk0bX0QnSBjGk5UqlMYFm_KuZw11pvHDcBnyMgFY5z7PBA93WPLhxZgUWwko5m8hXQ9NV9_o2SRAB9Q62YsraoWAa-w48kl9P0DRPYJn2puTyKZiL9n7sf-bIkEEPouhcrboyvza4nwfAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوشش مطبوعات داخلی کشور از رژه جانفدایان ایران (۲)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/691227" target="_blank">📅 18:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uROMedK3W0n4fLDQqXfRK3nZ2hJDeT7dP7f0KBEI1PcDdc9tRk0v064QvXZiIs6rdVQL0BNb4kFNkFgJRgsn8_RBZ-JsUXBhC3049m-uMIcByrG-8nUBWN9Zkj9ifZXWiKJ7OEiuR1p7xsJ3Sfk8IsjEblDwQcUHPGrYM1fFbxJWeO385fiYjSE3Z-WrGysd3U0pfDYZ8bGljKIVwS22YNf3cx2Qz_iep8ABjK4aBHZK2PVVNlYC4cVyQbQTYoOzRi8EuoEIAcKpEp-4UNnb49xmqejVRwoeut27UdkYlmq2g0hZE5Hs11YwsZxfBYB60JJkJz_vR7iArXCi2daqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام
انصارالله به عربستان: حملات بزرگتر در راه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/691226" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtyDqyGdF80OYMzZ6hfxNo1Jbi5OF745YfBUQLmp3IuxMniWFi3qoqiKpIfuVA0Q3q8QX4XtSpbTEG3_73cq1tazSRShaOVf6SAmpXydhthXcTl6M56FfhOWePd6aPmuCrzaGC0anCdKyTiZlBCZ36YiDBbH23miCOEX1ERE3lyCVCnyCy9zl4OfJjN5HS2saYCAb1aM8jLswts9nQzE2rBBpNavLxZktiagRwvBeuz_RzYLPdp0ROnwWllMDpuDAq81npYBpzzgtWQiboyvsjdJ1A4kEcQ79I90LL4US4ShtrQNVNaflODX2KDP19TJvmVoW0txZC0Bm3BuaQ5jDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wkjg2G66nq2c_FRNVopWoAmD-oE7KWGfYR1BVF4e4--uCEvs1K97DCFFdRDVtPf7mGwMzW5PsQuSaIRmdqyQQi1PcXZNK_ZOolTUZWNey3zBSTocFJjXQouPKr5GuHMFtq8keoVfwm8PO-23o0zIjK1oz6K0ly0aTILTSVjhoAB3-l8CfLk_rjYriIPwjjKllpp536ZLLROK9YjIqrhhBgOEdSA-EybrKzFI-AgAPEHQ0R_L_md6ejUje91OOXLN9umsk_HgOFZ34FZDSDZ_Oy-v0ouUA3nOrJaDgho39JY-qx65l7r7D9WejczmiwNfvoUCK0VXvJUg-Z5ApN8U0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جایگاه دانشگاه‌های کشورهای اسلامی
🔹
بر اساس رتبه‌بندی تایمز، ترکیه با داشتن ۹۱ دانشگاه در رتبه نخست کشورهای اسلامی از نظر تعداد دانشگاه‌های برتر قرار دارد.
🔹
ایران نیز با ۸۱ دانشگاه در جایگاه دوم جای گرفته و کشورهای پاکستان با ۴۷ و مصر با ۳۵ دانشگاه در رتبه‌های بعدی قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/691224" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f01df87d.mp4?token=DHpQ5A6LdEt7KBGQZaTOpLbKo8D7U85l-6xllKQqe18LNBqSsoJ8IYnAUWZ7922qajgpafs8y3JQkNlZ4YsLEyd0UbPi3A2uJvY1u4UuEL0lNp_nZkCTRuDeH7jJBIqqQSKeOPRSzck5wU57XZwN5i_RDDPllOadgMjMnqsyzTci31xc-X4U4tvrTuH0YUZspA1uwgWfRxDkyeuDihmiTSRHQKGpIfH659nemyi6bqypO7sbq9s1rcWCUvwPITvm-5l7XN-cpDenYyZ7axDVQQHQ-EEsBYPASxcc23go_Sojp0QkIk9jxFnGNRx688bp2CHNIorfFksufsTjNVaZ9TU4rsDfg4T4xfvpCo-pEbCN36Y_XwMjdYv3VAxXCSZTKkW-Z6iRUrlP1-KuZymRjAtH-iHPM2PJaVkgjMZbLvyNUHGrmUPnKTq6b_0WS0UmDweeaXrtqZ5VNzVsfnnQCLaKGnzT40o5OQ9Aofg2ErlBI4VRsT1_GvvJZ7qemPaA6uvoGTY2ubiZKlkpo6BGEG2JygwnFLd4rwN0_zOWJecDCpdW74VSNa7J7KO8P-TsmzGiBp98oaSa5jWpEoYMthDypcP6JXKFJLz6k3MUW9EggpAZyeFiXxJvFJNXvHJO7jkRoKcHUz0OKquTAaYv9s6LBakkKxRT089IrBldE1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f01df87d.mp4?token=DHpQ5A6LdEt7KBGQZaTOpLbKo8D7U85l-6xllKQqe18LNBqSsoJ8IYnAUWZ7922qajgpafs8y3JQkNlZ4YsLEyd0UbPi3A2uJvY1u4UuEL0lNp_nZkCTRuDeH7jJBIqqQSKeOPRSzck5wU57XZwN5i_RDDPllOadgMjMnqsyzTci31xc-X4U4tvrTuH0YUZspA1uwgWfRxDkyeuDihmiTSRHQKGpIfH659nemyi6bqypO7sbq9s1rcWCUvwPITvm-5l7XN-cpDenYyZ7axDVQQHQ-EEsBYPASxcc23go_Sojp0QkIk9jxFnGNRx688bp2CHNIorfFksufsTjNVaZ9TU4rsDfg4T4xfvpCo-pEbCN36Y_XwMjdYv3VAxXCSZTKkW-Z6iRUrlP1-KuZymRjAtH-iHPM2PJaVkgjMZbLvyNUHGrmUPnKTq6b_0WS0UmDweeaXrtqZ5VNzVsfnnQCLaKGnzT40o5OQ9Aofg2ErlBI4VRsT1_GvvJZ7qemPaA6uvoGTY2ubiZKlkpo6BGEG2JygwnFLd4rwN0_zOWJecDCpdW74VSNa7J7KO8P-TsmzGiBp98oaSa5jWpEoYMthDypcP6JXKFJLz6k3MUW9EggpAZyeFiXxJvFJNXvHJO7jkRoKcHUz0OKquTAaYv9s6LBakkKxRT089IrBldE1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کافیه این ۱۵ ساختار زبان رو هر روز تمرین کنی تا خیلی سریع انگلیسی یاد بگیری #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/691222" target="_blank">📅 18:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c94427c5.mp4?token=aNjewiKspeyecyG9Dtt7qzXNP8IEztwo54BZZZk2R3KMGGKnkhudIId-LDMXHBEidqvp-iFkk1HQVnFh-vHtA4xdWBd527DgOX5FtujdLrWpPx8QA6fm5Q4bECo-jhskiOOgbyfgfaiJ6DCPWVFzRFMWc-y7lytut8W2Je5WUX-elIY7vUBTG7zWHecB47KbNf0b0WUY2ODvrRFtzLn0X6RvPB3gz3o3X57E1t3AXUJfXslHEab5BXySPLzDMiPvP62NyXn4jRga9CmKSSqk8myfcHJb4ydA1-G3XD76qQTysbw5MRm1VhDzj1k3oKSjtHWqFXyHg1Cy-ScZ9ZQsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c94427c5.mp4?token=aNjewiKspeyecyG9Dtt7qzXNP8IEztwo54BZZZk2R3KMGGKnkhudIId-LDMXHBEidqvp-iFkk1HQVnFh-vHtA4xdWBd527DgOX5FtujdLrWpPx8QA6fm5Q4bECo-jhskiOOgbyfgfaiJ6DCPWVFzRFMWc-y7lytut8W2Je5WUX-elIY7vUBTG7zWHecB47KbNf0b0WUY2ODvrRFtzLn0X6RvPB3gz3o3X57E1t3AXUJfXslHEab5BXySPLzDMiPvP62NyXn4jRga9CmKSSqk8myfcHJb4ydA1-G3XD76qQTysbw5MRm1VhDzj1k3oKSjtHWqFXyHg1Cy-ScZ9ZQsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک قبیله بومی منزوی در آمازون که از هوا عکاسی شده. آن‌ها نمی‌دانند ما وجود داریم؛ و ما نمی‌دانیم در ذهن آن‌ها جهان دقیقاً چه معنایی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/691221" target="_blank">📅 18:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691219">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caugzHpFW6s2DYbzwaVOKXFAfRKNnOF04FgPLISBCS4VaFaJ2kZ_3ETA5nGrKWwL2O7lvNxHemWMfoGc-WEpB9mxc3q3MHNiBW2lBW7tzl90ps-2JWAIt1MaY8rszayfmFrQ7dSmgcPVhcTYNt_09L9wNtBowAFt9me28ciyD9ihhJY0u6Uz9Nx7Xi-I-HfrA8n3j2AfY99dFTHdyk_gTcOMvrWM30TwsSQO8i8wZ-a_UthYzwf4DKKJGGXksOrPpSOImFJKCXEkWavFGrhoaowI5jv3PRg6E5EH2riMk1EMX6P4N5qYIbvj3YiU_y5YKhFBFjT7eiWRudh2V6r4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخبه و مخترع باشرف، خانم لیلا کشاورز در بیست و پنجمین دوره مسابقات علمی و فناوری جوانان و نوجوانان آسیا در مالزی با کیف مدرسه نمادین به یاد کودکان میناب ظاهر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/691219" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691218">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcP3JuqO4dCpK0xS4U2VkfG7Ew7dodngbMzXKq6cOtGaJWNd97SfnnzyZXPq_cgGKkJua-6n-8CNTmeSuGqsBKfc6MIN9TQkmcEnKihV4qWpnoWFRLFoKjvumFXK8I6hCZh305ybaOm8gy5EiC8DT9JpQ-yueXzT3gratpNYnIaN6ak9E23ajfx-rn1qS5A7p2CA82QUzLAUNf39OO7t2JKa5Q0D9Gkh2vJKi53XwGMjjUzLXfC3m3Jq3QTqNIDg4QKN_FTRs9Ds4dWk5Pfe-b-f9IgZDBUlG-IAGFa6blbvfpI1kXVsXJi-gG-Cg_yUho9mNcbcnCg_eKERWIi4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه سفارت ایران در مجارستان به بلاتکلیفی ترامپ: راه خروج از جنگ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/691218" target="_blank">📅 17:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691217">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40dcd9622e.mp4?token=FHWcjkTRV-6xOOBB7fh_HMVHD2ziqmSIEzBln9IxE0YmWJZlVEE-SsFYPWAYwEbHGbQPZT3AYqdfe7XJ-hMOQA1fhjzNn3AOjhjBWoRoVCNop8uyYeZ0PEc4-60X3glxaQdsGa7EJFw8_rF8LniPv1Ed9W9TedH82Ylceb7UM2xcsolY8zjRLvRC9q2UZP3wHRepzcstaAMgD49rgf_GFkTLVUFcoqe99iCDeLbgorzljLclleq_jC5PVdfjN2Thz0EIUyR9aZ30-dkstmg6plcyiR3E_Fd3N4FD49dsDIAmZU04EP8Ce-PdCG3oLJPJeEPRooU3Dqj0gKzXyG4IZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40dcd9622e.mp4?token=FHWcjkTRV-6xOOBB7fh_HMVHD2ziqmSIEzBln9IxE0YmWJZlVEE-SsFYPWAYwEbHGbQPZT3AYqdfe7XJ-hMOQA1fhjzNn3AOjhjBWoRoVCNop8uyYeZ0PEc4-60X3glxaQdsGa7EJFw8_rF8LniPv1Ed9W9TedH82Ylceb7UM2xcsolY8zjRLvRC9q2UZP3wHRepzcstaAMgD49rgf_GFkTLVUFcoqe99iCDeLbgorzljLclleq_jC5PVdfjN2Thz0EIUyR9aZ30-dkstmg6plcyiR3E_Fd3N4FD49dsDIAmZU04EP8Ce-PdCG3oLJPJeEPRooU3Dqj0gKzXyG4IZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تند حامد مدرس، مجری کودک‌ و نوجوان به لاله مرزبان!
🔹
چطور تونستی چشمت رو روی ۱۶۸ کودک معصوم ببندی؟
🔹
اون جایزه ای که گرفتی چند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/691217" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اوضاع نابسامان درآمد پرستاران، ۲۴ ساعت مراقبت از بیمار فقط ۶۰۰ هزار تومان!
محمد شریفی مقدم، دبیرکل خانه پرستار در
#گفتگو
با خبرفوری:
🔹
تعرفه خدمات پرستاری برای ۲۴ ساعت مراقبت از یک بیمار حدود ۶۰۰ هزار تومان محاسبه می‌شود و پس از کسر کسورات حدود ۵۰۰ هزار تومان باقی می‌ماند.
🔹
این مبلغ برای مجموعه خدماتی که طی ۲۴ ساعت توسط پرستار، کمک‌پرستار، مدیریت پرستاری و سوپروایزر به بیمار ارائه می‌شود، است.
🔹
در مقابل ویزیت یک پزشک حدود ۵۰۰ هزار تومان محاسبه می‌شود و این اختلاف یکی از عوامل نارضایتی و کاهش انگیزه پرستاران است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691216" target="_blank">📅 17:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رئیس‌جمهور لهستان: پوتین در حال برنامه‌ریزی برای حمله به کشورهای حامی اوکراین است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691215" target="_blank">📅 17:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c66205bdc1.mp4?token=ShDwsbOitQ9s6f8oaKpph83wRGzhEW8euOLGe9zyWbeBwrIO8Gx6Briqu8Q0mg1pavXOp9HZc88GvNtZUblI_zEgOBMy-XWGggYlyIHgq9jhISqpSv5ITHtIeEXYi-_wv4-ZKstVX1SnFtY1GUnv2pxgyJrxGJ5v_ZKbpUj4cw3tRz0RBa2cSTPB3PzAwR-U7R7lduqHIcCLZ5EaiSThkKNlN1ZxwG23KxzWXxlPYtkPJOLFKrvChjidMX6OqxCMllhDP7vDarNH4O0snw2IakO1HX2kboDmOaFsGjRIXCtV2y7asswU40rUQMri6xhyaHLuguXT37TNgotFU4ojgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c66205bdc1.mp4?token=ShDwsbOitQ9s6f8oaKpph83wRGzhEW8euOLGe9zyWbeBwrIO8Gx6Briqu8Q0mg1pavXOp9HZc88GvNtZUblI_zEgOBMy-XWGggYlyIHgq9jhISqpSv5ITHtIeEXYi-_wv4-ZKstVX1SnFtY1GUnv2pxgyJrxGJ5v_ZKbpUj4cw3tRz0RBa2cSTPB3PzAwR-U7R7lduqHIcCLZ5EaiSThkKNlN1ZxwG23KxzWXxlPYtkPJOLFKrvChjidMX6OqxCMllhDP7vDarNH4O0snw2IakO1HX2kboDmOaFsGjRIXCtV2y7asswU40rUQMri6xhyaHLuguXT37TNgotFU4ojgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال‌شده از تهیه و جمع‌آوری تخمه آفتابگردان با لاستیک ماشین در ضعیف‌ترین وضعیت بهداشتی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/691214" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTahagasht(Tahagasht Social)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs835RAb9d4R8TUcsja6G9pJUvdEeUa4fFs1SsIrBDFJKYO4jmDvlbABJ6tLIALfo5VZkxGqPujfJyAb8cjsAAoOsoVG1VadDFz9dJdhTOuIvbnMTRemQ4lnO2aArhKWHF7R8irkeB2a3i1eG6VYQqS0UezUo_bkbw6tT9XVTpCLTxi4WEJoqJqtFTpWFV91XSSpJXJGUu4s99LkUpEFCgP492i-dLEuAnvhiJ2FnqIG-GIHMeoXnvRzpcVXIZuhfvr2Xkx5BjhwjXLKEiuUBnsfK1O3SvBy8IP0bTXcr-yJedkhM0bbaDAzYVWc-y0Mlk4x2smZBr_EHIztr3Se1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
تورهای تکراری ممنوع!
✈️
سفرت رو خلق کن!
سفر رویایی‌ت از همین‌جا شروع می‌شه!
✨
🔹
بهترین نرخ پرواز و هتل
🔹
تنوع گسترده هتل‌ها برای هر سبک سفر
🔹
انتخاب مقصد، تاریخ و مدت اقامت
🔹
طراحی سفر متناسب با سلیقه و بودجه شما
🌍
همین حالا سفر دلخواهت رو بساز و رزرو کن!
📲
تلگرام:
https://t.me/+2wRXAjoDIG44M2I0
🌐
www.tahagasht.com</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691213" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای مضحک سنتکام: ایران به‌لطف محاصره شدید ما حتی یک بشکه نفت صادر نکرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691212" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEU1ecrEKoMCpl_ftYt-6pvpK6m_4Z4F5mkJ0HE5DMP2th286mMJv0WrrrtrNuUN9uM6ZU58hjjHjnXqb4tnerImaJXiaaZ40hOc1lTOG08Ihw1sB47AL3FTMaiPztH2Sg75k6difw72r_dUqSwo7bjSKaN4rfmuO1biTYffZv13KmaB_Ev2dtvEPmvyNJVcIvVnhWTyNBWEZVF0SMcHGjMvnA8RlS-mhSjlrxjToP1RcVVHs_emRSjqanV5HkJPB84pFtj0bKcbN9hNpwnxJmKWboUZZjNLcsimtDtf65kPjjKPK9tKi418H_A9YffA1CWJM8ux4MIMUthGnSgi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نان مناسب برای دیابت
🍞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691211" target="_blank">📅 17:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
فروش نفت ایران در شهریور امسال از ۳ میلیارد دلار فراتر رفت/ این رقم بیشتر‌ین میزان ماهانه در ۲ سال گذشته است
🔹
طبق آمار سازمان برنامه، درآمد نفتی کشور تاکنون بیش‌تر از سقف بودجه محقق شده./ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/691210" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLVBtI4CNETbRTUalq91VpTTgqU7SKl4tDbGJuuubMHd6GTxT_QwFNd7SwphoewbGCHn-irYjnOTm2b8vwOcO7pd7f42Jd3iB7GQmpMiZS0YNcSLGhtpcWcZFFifR9wSjfvPMm3hImNCkYDVdAMuWlF5g1qgmzs4YyDv_SjzfwZF9xZuPcUo75O-Z8STTxYVul50uLviMyx__dYed6UMAUwibTXUK4KQZL9WCZOocUZPppyMjnP0pbwIRASqF5x0C5tg1aRnghZzqH5LIddqh2vvrW4qEvOD_Cu8RNzGdBdnb3_RUTkdXo25qLZrYO0RMvEJpU6AHheHaehF4MsJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CNN گزارش داد که در آمریکا میزان جستجوی "قیمت بنزین" در گوگل طی یک ماه اخیر ۳۵۷٪ افزایش داشته است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/691209" target="_blank">📅 16:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فروش نفت ایران در شهریور امسال از ۳ میلیارد دلار فراتر رفت/ این رقم بیشتر‌ین میزان ماهانه در ۲ سال گذشته است
🔹
طبق آمار سازمان برنامه، درآمد نفتی کشور تاکنون بیش‌تر از سقف بودجه محقق شده./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691208" target="_blank">📅 16:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ba6c7af0.mp4?token=YN5Ml1Yj3Db50natfkzsI-Z2mGpWDsOkrXGtHZB0hedLCUCTZ1S0xG0m4s6EDKnOjKJFY2VYBsq3QU-Mj1rQWf8qOb0sLbT9472RUaBhx_Y6Bz_1wIZHTsGQ9s7ojJqtXgGl5IAAr31QT3DaSte5aAL5-0EAjmherdhjBRialpxvR42m5qND-Wxh8nh6tjy7ncG6lPhObgfbwkMNe2FVNWVTfl_5cMiz5UQUsEdLrhOKYbZu9BF_c-N0DTLg0z4OIk0K4uWDFz6ujoCHeKthhqGdONS2OqXADmq3M1Ddljqh88YTHI6e0q7EIr5gijIjWCHcEdTSlyA0dl9nsTsF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ba6c7af0.mp4?token=YN5Ml1Yj3Db50natfkzsI-Z2mGpWDsOkrXGtHZB0hedLCUCTZ1S0xG0m4s6EDKnOjKJFY2VYBsq3QU-Mj1rQWf8qOb0sLbT9472RUaBhx_Y6Bz_1wIZHTsGQ9s7ojJqtXgGl5IAAr31QT3DaSte5aAL5-0EAjmherdhjBRialpxvR42m5qND-Wxh8nh6tjy7ncG6lPhObgfbwkMNe2FVNWVTfl_5cMiz5UQUsEdLrhOKYbZu9BF_c-N0DTLg0z4OIk0K4uWDFz6ujoCHeKthhqGdONS2OqXADmq3M1Ddljqh88YTHI6e0q7EIr5gijIjWCHcEdTSlyA0dl9nsTsF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این پزشک در لیبریا با روشی ساده و به گفته خودش مؤثر در هر شرایطی، نوزاد گریان را در چند ثانیه آرام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/691207" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691206">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
قصه‌ «پل بیات»، قصه‌ یک سازه نیست؛
‌
قصه‌ آدم‌هایی‌ست که نگذاشتند یک شریان حیاتی از نفس بیفتد.
‌
این‌بار، تصاویر حرف می‌زنند…
‌
🔹
پل بیات؛ روایت یک بازگشت
‌
#سازمان_راهداری_و_حمل_ونقل_جاده‌ای
#آزادراه_زنجان_تبریز
#پل_بیات
‌
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/691206" target="_blank">📅 16:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691205">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عوارض رفت‌وبرگشت آزادراه تهران–شمال در روزهای تعطیل به ۷۲۰ هزار تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/691205" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691204">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccb9c545ee.mp4?token=LEwvs9m0U8ypLqOr4PvTgjevJDlmHRUauS-QeK4SBWS1XxvnZHPUdOE2E_o3MVtBN0fJMmEuAlmfinsbryX-LU0QZb0Xu8tYAeCPH0niSgi6g2g4J2DMtH2xFu_A12M42cLLcRClj6aH4Pp66Ez4-6hGjvfcNUllWNYAHk8DNX0czto9SHbMIj712MbiY1FExpTyi_gRaTAc7qtUdiYx_27ENNT3QYFsfFsFAykRrzD-f_wCQGKZjbrRlz6JmOdDOg6BejPmRRM0ztj1xHqH9zLYV096ZgC890nNr-mXKIrdkK6Bp2CEzNffYBnGWI5uJRsy-QLeEy0z5Q3pRmjWM0EjLPCtXdKzNiZeYSqjxftHIW1hgTJzzInu1mpt9AKS5Q0zgvf1b5ab-KDfApLwLLKx5EO9rDPXa_btPPS9J4mrmBVKjOy_aPRMj0mdALZDmQxaayqAflgEvB4VjESR3BSLjAEhcpnaUeakZzzbF7SZRCeqHI-36f44Qv0hHW2nnzVgr8zfrn2fiJn5dg-M4g3_YSn2SWOEunsvf01rCoenrEz7mtDjJdf1ZhguJ7kq3k4cWRFOeyUm-vcPPqgQE1GlOGwUxJPNqvMbdEaeF5B6FvcnxmxsWQ5sRb9ctaGQj0IXR8_jfLVzcGUKCfCkX1RI3nCyMbShd04uw08aw04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccb9c545ee.mp4?token=LEwvs9m0U8ypLqOr4PvTgjevJDlmHRUauS-QeK4SBWS1XxvnZHPUdOE2E_o3MVtBN0fJMmEuAlmfinsbryX-LU0QZb0Xu8tYAeCPH0niSgi6g2g4J2DMtH2xFu_A12M42cLLcRClj6aH4Pp66Ez4-6hGjvfcNUllWNYAHk8DNX0czto9SHbMIj712MbiY1FExpTyi_gRaTAc7qtUdiYx_27ENNT3QYFsfFsFAykRrzD-f_wCQGKZjbrRlz6JmOdDOg6BejPmRRM0ztj1xHqH9zLYV096ZgC890nNr-mXKIrdkK6Bp2CEzNffYBnGWI5uJRsy-QLeEy0z5Q3pRmjWM0EjLPCtXdKzNiZeYSqjxftHIW1hgTJzzInu1mpt9AKS5Q0zgvf1b5ab-KDfApLwLLKx5EO9rDPXa_btPPS9J4mrmBVKjOy_aPRMj0mdALZDmQxaayqAflgEvB4VjESR3BSLjAEhcpnaUeakZzzbF7SZRCeqHI-36f44Qv0hHW2nnzVgr8zfrn2fiJn5dg-M4g3_YSn2SWOEunsvf01rCoenrEz7mtDjJdf1ZhguJ7kq3k4cWRFOeyUm-vcPPqgQE1GlOGwUxJPNqvMbdEaeF5B6FvcnxmxsWQ5sRb9ctaGQj0IXR8_jfLVzcGUKCfCkX1RI3nCyMbShd04uw08aw04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا انسانِ معمولی هم می‌تواند با فرشتگان ارتباط بگیرد؟
🔹
پاسخی عمیق به یکی از رازآلودترین پرسش‌ها درباره مرزهای غیب و شهود در زندگی روزمره./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/691204" target="_blank">📅 16:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691203">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a90b8817.mp4?token=ofeiGLNpMQVJJU5bdQeAkoxegg7s1_CRDMpK58Iql2A7RFzM6_bOKjFWxSRPeouIr0TQPpfn2EWO1KJn__ffQrhNKUUUXU9TYBqrMMoG2HmeUU22V-YNxsPSbLxeDEU4Hafvry-VdM1r8bdEHLh0dJRew-PcTHA3ujV09lTrFwCI0tFeakCNHczx1TAXbBVBhPBvPNRuEMtmTsYO07n2k_aQrcMK6nGRgPUGyENw_d0VR9_qkSm-z4xIonWWqOEmDHBG_QY-AMksaTmSsKHPN0xBj4cBzGiJJhRudBLhQnTLuNYFkhRTekOYLW4hLhvX44EmK1TqN051dtM0EJdInYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a90b8817.mp4?token=ofeiGLNpMQVJJU5bdQeAkoxegg7s1_CRDMpK58Iql2A7RFzM6_bOKjFWxSRPeouIr0TQPpfn2EWO1KJn__ffQrhNKUUUXU9TYBqrMMoG2HmeUU22V-YNxsPSbLxeDEU4Hafvry-VdM1r8bdEHLh0dJRew-PcTHA3ujV09lTrFwCI0tFeakCNHczx1TAXbBVBhPBvPNRuEMtmTsYO07n2k_aQrcMK6nGRgPUGyENw_d0VR9_qkSm-z4xIonWWqOEmDHBG_QY-AMksaTmSsKHPN0xBj4cBzGiJJhRudBLhQnTLuNYFkhRTekOYLW4hLhvX44EmK1TqN051dtM0EJdInYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر نوری در پی یک حادثه رانندگی و تصادف شدید، باید جراحی شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/691203" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691202">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGx5Je1YNTP_1DuEnnzmfLfsZeVLhaBWooi4BOhnLugHJfTx5-7oPnwPDSwF3QsoWdaQD0DcMEc78QP7Xv3Wh0QeAK6A3BXMKnqvFzGElkbxO8rWMs_NpQUzSCcELf53rr8FiDY7wa6dFqBtW64iazZMoA7X87HhMaMwURGVEukNjP5i-TR9Ugfh0uGStYQGYuzqUx4iThgHdbuntPwNReIZp2Q3PYSVnGgYjFZqebqNYKRUuS_1uGHpef8sbFGSifYjtCoR0V-LWBXreku1OrPqZ4VS-Vle8hOp6bAzNcNP89MgWtvFziGZwCvDd2xxTz_JNGuzD499imcHBKidjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش فاکس‌نیوز
:
قیمت گازوئیل به دلیل تشدید تنش‌ها در خاورمیانه، به رکورد میانگین ملی ۶٫۴۴ دلار به ازای هر گالن رسید
🔹
فاکس‌نیوز، رسانه طرفدار ترامپ، چند روزه داره مخالف ترامپ پیام می‌زاره؛ شاید جمهوری‌خواه‌ها میخوان راه‌شون رو کمی از ترامپ جدا کنن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/691202" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691201">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047145406b.mp4?token=AVVTmQSrYLrl28ic42WM6XB8_A5o8jah5rLWYxlEDsMi89usMxcZyXeYCRaBqUq3cU5ck61VjiWb8kFuSUp3vZSAZc_bxcYyhQbTPR4ACdrP7EgeWOzIjcMIcDAnqRUIwEJvIK2vBmdItcmghzKBI6zhLdxJ1epGBoXrnvzEmqoMMsnJ-tBpEMOHA-qU8sxmCOGmu6Gd-WQKFt-dvD5CAx6psaH2wL-W6bdlVIxpGBlKJJ21-6hVAtzknUvT5lLL7hZWvQ3We_-WU-6TCSRXP8NLkxZqibhZAlKkL2EtViEB1ufSZU0i61mMBrxY7SjArAaoOAOQo9XJ_TZuzKYbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047145406b.mp4?token=AVVTmQSrYLrl28ic42WM6XB8_A5o8jah5rLWYxlEDsMi89usMxcZyXeYCRaBqUq3cU5ck61VjiWb8kFuSUp3vZSAZc_bxcYyhQbTPR4ACdrP7EgeWOzIjcMIcDAnqRUIwEJvIK2vBmdItcmghzKBI6zhLdxJ1epGBoXrnvzEmqoMMsnJ-tBpEMOHA-qU8sxmCOGmu6Gd-WQKFt-dvD5CAx6psaH2wL-W6bdlVIxpGBlKJJ21-6hVAtzknUvT5lLL7hZWvQ3We_-WU-6TCSRXP8NLkxZqibhZAlKkL2EtViEB1ufSZU0i61mMBrxY7SjArAaoOAOQo9XJ_TZuzKYbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: آتش‌سوزی در تأسیسات نفتی آرامکو عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/691201" target="_blank">📅 16:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691200">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4mCW2gWIP9q7m_VGC7dU18JVF0dnIoUoBcLs094rQgh_G82FsiPze4d9mAUNqJIGuV4O6aedTFEMJvDXc5b4SX2PY9dVVTb87o2L62MCVsjaPohLNBRcb55WJkM-PUG5o7yV_PfPM2snbpkgmJJxh60SPOX_5FiuHKAwBhcRDRLLPPKLk66XywKE5eNglmy5rklEL3Dcdz4R9SthmD6GvoZrD563lP1A5b3Cugp7CQM_RlpsT6RpmSLxSzOygc7HxTwmomiZRYBaNRv5o93azlpYvmsDBVDyp-pbK8Rl9FbyjWEXo3dXCewf7Fgcy60mcrxBc8JhzeNeiFx3ksM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
واشنگتن‌پست: جهش بزرگ قیمت بنزین آمریکا هنوز در راه است. بدترین بخش شوک اقتصادی ناشی از اختلال در بازار انرژی هنوز از راه نرسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/691200" target="_blank">📅 16:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691199">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
یک مقام ارشد نظامی آمریکا به شبکه ABC News: ترمیم خسارات وارد شده به پایگاه‌های آمریکا در خاورمیانه در پی حملات ایران ممکن است «دهه‌ها» زمان ببرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/691199" target="_blank">📅 16:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691198">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745d49995a.mp4?token=Ur0wsf1okGIrvqVLpF5dlbxpohc1Q4-VadL_tymsTkekO9p3vMOOT4xqHn9leJ-7HUdWtNWVRT1H2F3ow0A6fVhl-8f85ZrLmjuFyTqN4pFvzQkL6YJ-ufYi8aEwEUST4Ty-pwl4LxeAkBoOd5t-BPt7DOYpmZkvf5mFyES3LaoeWse2HcE6HAH3uFNPzsAx-rz33Nhd_ShXELpgjSwAGICPva2NjDtRa9Zd_W3odpYZNdqUWjNyq7pvePxdLu_9XASvNyhfbuZr7XRlqMsyIlK8PSegKqSnU0FPkg5t2El2O9MvHPyf8m-oVGLc0q_7U6wIPMElRdaqIExIQEPX_3jUmL2kjuClNpQHa891mJiWidtSy9XP_NEVW829mJtzjnE8ZYCi2kZLBQNVl186MEQPFJAqltR5syHT4xhKJltrTryeYZBUmpEXcbytSRN-ISCe00rcAOGSz26gOE3_zUupaHxJhxSOripXemat7aGRNfY-EWOtZfaD7KamgnTzv06NsYFt9y8twLukgAdbR5WM6KKa98V_lEVV_KrPXZrkYq7kUFXDdQmAifEzZexsiux9xlg5x40k6HwOXZjW_6t5t1zAoGJxu9Zq-D-S-jC-n7J6s7jbpe6Xn2cAaGpGp8Bz2QjIUWdhtj3Oyks6YAvALFONS0dU4VRq9fo3jh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745d49995a.mp4?token=Ur0wsf1okGIrvqVLpF5dlbxpohc1Q4-VadL_tymsTkekO9p3vMOOT4xqHn9leJ-7HUdWtNWVRT1H2F3ow0A6fVhl-8f85ZrLmjuFyTqN4pFvzQkL6YJ-ufYi8aEwEUST4Ty-pwl4LxeAkBoOd5t-BPt7DOYpmZkvf5mFyES3LaoeWse2HcE6HAH3uFNPzsAx-rz33Nhd_ShXELpgjSwAGICPva2NjDtRa9Zd_W3odpYZNdqUWjNyq7pvePxdLu_9XASvNyhfbuZr7XRlqMsyIlK8PSegKqSnU0FPkg5t2El2O9MvHPyf8m-oVGLc0q_7U6wIPMElRdaqIExIQEPX_3jUmL2kjuClNpQHa891mJiWidtSy9XP_NEVW829mJtzjnE8ZYCi2kZLBQNVl186MEQPFJAqltR5syHT4xhKJltrTryeYZBUmpEXcbytSRN-ISCe00rcAOGSz26gOE3_zUupaHxJhxSOripXemat7aGRNfY-EWOtZfaD7KamgnTzv06NsYFt9y8twLukgAdbR5WM6KKa98V_lEVV_KrPXZrkYq7kUFXDdQmAifEzZexsiux9xlg5x40k6HwOXZjW_6t5t1zAoGJxu9Zq-D-S-jC-n7J6s7jbpe6Xn2cAaGpGp8Bz2QjIUWdhtj3Oyks6YAvALFONS0dU4VRq9fo3jh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تأثیر جنگ بر هزینه انرژی اروپا؛ بنزین در برلین ۵۰ درصد افزایش یافت
/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/691198" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691197">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
فرماندار جاسک: انفجارهای کنترل‌شده در جاسک هرمزگان/ این عملیات تا ساعت ۱۸ ادامه خواهد داشت
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/691197" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691196">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qREtlmnhf2IUKpTa7lpdf8AsLOBniVJmLgl1idDbroyHYHXMIhk88LgPyihRrAWaiQJnSlsg2qhnD-K-JVzqJKrHMWGzPK9oXu0PQMeODj6JnB1dXlJ0wdlcieQYAwb19CtZsu_Hy4wLGVffIRibNKB55JGqHlsg8AulE-BdKb8LisJ_9U8nzcLl9rlcj4us5dUvFU268fKuFzwQ5x0030SNbHXqy-sNpeqyPC68pA73CJJ07FQcgxXf1PgOOpu9v0UwiASUeLBjK8ccoNTiKmo0WIeaoaTYUiALobvyLl-KdF3tOdQoBBFxwOHdvYfo1ORxYun6uoaW6rsdvyNY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت جشن ولادت باسعادت حضرت امام حسن عسکری(ع)، اجتماع بزرگ «امام زمانی‌ها» برگزار می‌شود.
این آیین باشکوه با حضور عاشقان و منتظران حضرت ولی‌عصر(عج)، یکشنبه ۲۹ شهریورماه، ساعت ۱۹:۳۰ در میدان راه‌آهن تهران برگزار خواهد شد.
از عموم ارادتمندان و علاقه‌مندان دعوت می‌شود با حضور در این اجتماع، در گرامیداشت این میلاد فرخنده همراه و همدل باشند.
شهرداری منطقه ۱۱ تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/691196" target="_blank">📅 16:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691195">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBF6xsCJRKIPgpGZghDb8orfcsNl_Wt9HhVmGhVAwPSz49aVlkIhwI2T5F3GPPs9kjrhaOexDIFURf7mUTWKEsIdCVjNV2Lr5CzLpMkCScE-sGiiMnAzAKm67oQdMxjYyYY-hPe6u5QKjM81dJ7hzFtxeu4bDPvnGST-vpHTfrwg35kUTN7UbI-_ZWbiFows_VTui_vln2RH7ZL7Pvy2oLcqYkBrE9b6NHPQ0nEVMiL7hW4lTzd0MuNZERD4clp-7YlEsdt55U0MEsNAtSFrngWF0_kbrVBMCgAz6E9fs1bEQsDrOugVujomVvoWyf3pdBzgemdOH6W3Zs5KwjT3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: عربستان دهه‌ها برای حمایت نظامی آمریکا سرمایه‌گذاری کرد؛ حالا واشنگتن پا پیش نمی‌گذارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/691195" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691194">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تکذیب تعلیق فدراسیون بدنسازی/ ملکی: هیچ ایمیلی دریافت نکرده‌ایم
مجتبی ملکی، رئیس فدراسیون بدنسازی:
🔹
هیچ ایمیلی از سوی فدراسیون جهانی IFBB درباره تعلیق فدراسیون بدنسازی ایران دریافت نکرده‌ایم.
🔹
برخلاف اخبار منتشرشده، چنین ایمیلی نه برای فدراسیون بدنسازی و نه برای دیگر نهادهای ورزشی ایران ارسال نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/691194" target="_blank">📅 15:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691193">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjiR_yCtsUtoQoGf4LqraRZ-w-8UB75siyXXLOovA1mRTSpofZS8pgEqKVzFzolwNwc9q__hiYwCYFRB5CNIoYpI_4SOP4MjGhCfPOQfqefSmIDZ9qfVSlSj4w7rhkG9bdvS7Z41CKMpJS0Bmv501k78sE-QLHdNeqOdMFv5CQkWatIkWDQU7Sv8RRwG3xZoeIjqQN2f5WhjqICh9g6XGWjIGR2lMGhOFAZAqUPvbdZNWkbwAIvXm5PUOGSYU2wE3WKRh5U7nnFxwrWgXOgv02Cbjf3byuJsJJiSNVDOp6tKiDU65cRvIUZMtZaPKPXxiMAUu9HdT7PAm5UN-HGJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آندرانیک تیموریان از تیم ملی جدا شد
🔹
آندرانیک تیموریان که در سال‌های اخیر در کادر فنی تیم ملی فعالیت کرده و حتی در جام جهانی هم روی نیمکت حضور داشت، از تیم ملی جدا شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/691193" target="_blank">📅 15:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bbadb7e5.mp4?token=CwUU9ng-I45O-NYUCs6CD0LUJIxKgX8RbsJGVdv8VFLMU5BhNd0w48u35bK5D6NuXqboUvt4EoDK5e-HZv7K7YzmDnh55aadsaXd8aaYZ0vPiuypLqGExJ3vExEde-1cIiXCuTRvj34FRee8Q_VnMWBZmED3xs8Vww83ybYEe8ByAQYW3LcveOiBGa8SUR3TyAKau3LFXMhSixe_NuMY8GAk6-GRDXREAnNUBFB6-wqYphUW4C0UxbDvdckkBWyDtyRmraOJBEPTYHZBw95J9IIM8Av0rVrBZRs6JiYssiiX-GoZHRpR-UdYjGeD_HIJb2yHMnsOMQ-ZFfAS8j85TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bbadb7e5.mp4?token=CwUU9ng-I45O-NYUCs6CD0LUJIxKgX8RbsJGVdv8VFLMU5BhNd0w48u35bK5D6NuXqboUvt4EoDK5e-HZv7K7YzmDnh55aadsaXd8aaYZ0vPiuypLqGExJ3vExEde-1cIiXCuTRvj34FRee8Q_VnMWBZmED3xs8Vww83ybYEe8ByAQYW3LcveOiBGa8SUR3TyAKau3LFXMhSixe_NuMY8GAk6-GRDXREAnNUBFB6-wqYphUW4C0UxbDvdckkBWyDtyRmraOJBEPTYHZBw95J9IIM8Av0rVrBZRs6JiYssiiX-GoZHRpR-UdYjGeD_HIJb2yHMnsOMQ-ZFfAS8j85TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فینگر لایم (لیمو خاویاری)، عجیب‌ترین لیموترش دنیا
!
🍋‍🟩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/691192" target="_blank">📅 15:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691191">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANdCmk4FWhk1bQA3owdXL_M3pxDu-il0ua58gvgcjm9zNek4mPFQFJNZUTOzwe5wcZYBr-ZiokFGMFfLYPbci_dTDAsHu377rktwmTmE8uUiqTNdHCyYqfvUR1pxndPXEceLtuWOf-9rYDfihwZt4VNomofVtQvRLkAXL-jrJ7HyXIQppxcnpspzx_iUpN740iCgWwcv6NaYNxqTFSYGzXbX39CIeALB7llc_SAxGoxhn9iB34wi-o-kkEMMx53gv4UfQkasu8EgVe96xR_42yRWPqV6vHjw3AaTbFHeGS8qD04glvbUZ33K5vLbnWGyQ6wshFX50mn3DdZiJypn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش کامبیز مهدی‌زاده (داماد حسن روحانی ) به شعارهای تجمعات شبانه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/691191" target="_blank">📅 15:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691190">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26362f645a.mp4?token=o5dh-mlLcHQI7EljOnFurt9vcMDtRIvAhtzT7Vt6lC7JTO9-eSO6uhqX8ZMwD91jnGUVmp74AOLOTWOMLstUfKx0MHcfSc2U26CyS4qNxPFWKvjz6jVJPVnaFEloc_pQzzGnU-DEG8SiURB3Vd570BgYKxdIasUa2pwnoRmIKXieE3Ms_Onbu7ghjiioh4_-7lfUdALHVOjzkxijy2G8cgeQkztyHM9WVhdhyTT4peEaHq30Jb32dfNHmtuYriplnQbWNsRsOpjzj5GgQUVnvpeqweu0Dx9Qu3nRL-SE4D7E6ObB_9k2eaUaLPpEcPmmg45akZOpaRA2NJ48DTavUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26362f645a.mp4?token=o5dh-mlLcHQI7EljOnFurt9vcMDtRIvAhtzT7Vt6lC7JTO9-eSO6uhqX8ZMwD91jnGUVmp74AOLOTWOMLstUfKx0MHcfSc2U26CyS4qNxPFWKvjz6jVJPVnaFEloc_pQzzGnU-DEG8SiURB3Vd570BgYKxdIasUa2pwnoRmIKXieE3Ms_Onbu7ghjiioh4_-7lfUdALHVOjzkxijy2G8cgeQkztyHM9WVhdhyTT4peEaHq30Jb32dfNHmtuYriplnQbWNsRsOpjzj5GgQUVnvpeqweu0Dx9Qu3nRL-SE4D7E6ObB_9k2eaUaLPpEcPmmg45akZOpaRA2NJ48DTavUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جالب از دیافراگم دوربین در چند گوشی پرچمدار پیش از عرضه‌ آیفون ۱۸ پرو اپل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/691190" target="_blank">📅 15:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691189">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naLYxHDPH9Cs4SIOAarUxLS_lDCd3HoTw3rFK2rP4gs8bbHHmvd_iNJaN1dyyiBXJwcOe_Ich3maFDtki4QR5COYR_936909mdwgHaldU4z1gm8zZHy4PIKrb5BlbcfbO72SnieXMXm4YYYy8RxEGLyhYSjCjhy4KqeY-iSwqnBvJaF1BdHKpSQp1gCfgTuOoWHzDoGzwQRwyEFFGDKr-lfRDIMlZDOcRdEaKSAX-3LEWZ5fqiSStTFMoAow65Ioe3O3niDPR07Pr9fIVpy46yMdzsBHwECgNRcGkDst9Hi-vb9xq0EkRm0eazrpLXYTgTCzCbHC_d2oAxGIM3PisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از افزایش قیمت‌ها تا جهش ثروت میلیاردرها؛ اعداد جنجالی درباره اقتصاد آمریکا در دوره ترامپ
🔹
بنزین +۳۹٪
🔹
دیزل +۶۹٪
🔹
خدمات عمومی +۱۵٪
🔹
سوخت جت +۱۰۰٪
🔹
مراقبت‌های بهداشتی +۱۳٪
🔹
گوشت گاو چرخ‌کرده +۲۵٪
🔹
ثروت ایلان: +۱۲۲٪
🔹
سود وال استریت +۲۲٪
🔹
حقوق مدیران عامل: +۱۴٪
🔹
حقوق واقعی: +۰.۵٪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/691189" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691188">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52586b2c2f.mp4?token=c9P35NFXL_B6P1hO1F2uyngxt_mFa6lfPYojkQLzOh42XOzPFjfUDcP6j8HXbxeY7ovKXEry_XQ4Jtv9puPRAUIy5BEqYg6LFOQ_ccCMyvy22DOrol63gs_dCqRPz4P01XU94JNqqarGdBOwe5jfo22A7CHJ4h3lbpq-vpnx3zNv0vVzjL-FVdz6zi7P0AIDdAJn4LnvDXEhe1PXo3o0Wxb_nbmdvLuH4xv9xOj47ZJAXrzSiD6Xc-HqUZvpH5ePKOr06RUrnukK5VlGI-ghFAdgX2mvewnu8hxss4i5kLdJ-qHmt-_5wkfaCVab5-_HepsKFc4jGUvNiGPjmW5FI4xKE2QxoYrFgyMYdwZddWo81TECqj64KxK5MnU5-KqANu1FucbqWREVM05Vl5zDnQdmYmdeXnks-V7w_9WprMdi0ZH-HgbIoQ7bKLSP4ECDsIKBIB90kH19WxGQcPIdPGqW78C1DN9nBc_HPllcQMOm42h6DI3AbWbPwRiOptrm_LJVpFNcGeZJu8NAeSzYBL9TXOwexzC6k49czieuTspyNDHE1hxt4QqtwkuJOSYsEJcaSuxLNnW8nNsFJvXrjBDSdHV1GLJ3l5qij0ei3hMgz8J77Wiv7S8t_-0ALL3f3vSvWDrWZ41oq8QMRO-l67dSRpeFl38b7J5KQQCKNRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52586b2c2f.mp4?token=c9P35NFXL_B6P1hO1F2uyngxt_mFa6lfPYojkQLzOh42XOzPFjfUDcP6j8HXbxeY7ovKXEry_XQ4Jtv9puPRAUIy5BEqYg6LFOQ_ccCMyvy22DOrol63gs_dCqRPz4P01XU94JNqqarGdBOwe5jfo22A7CHJ4h3lbpq-vpnx3zNv0vVzjL-FVdz6zi7P0AIDdAJn4LnvDXEhe1PXo3o0Wxb_nbmdvLuH4xv9xOj47ZJAXrzSiD6Xc-HqUZvpH5ePKOr06RUrnukK5VlGI-ghFAdgX2mvewnu8hxss4i5kLdJ-qHmt-_5wkfaCVab5-_HepsKFc4jGUvNiGPjmW5FI4xKE2QxoYrFgyMYdwZddWo81TECqj64KxK5MnU5-KqANu1FucbqWREVM05Vl5zDnQdmYmdeXnks-V7w_9WprMdi0ZH-HgbIoQ7bKLSP4ECDsIKBIB90kH19WxGQcPIdPGqW78C1DN9nBc_HPllcQMOm42h6DI3AbWbPwRiOptrm_LJVpFNcGeZJu8NAeSzYBL9TXOwexzC6k49czieuTspyNDHE1hxt4QqtwkuJOSYsEJcaSuxLNnW8nNsFJvXrjBDSdHV1GLJ3l5qij0ei3hMgz8J77Wiv7S8t_-0ALL3f3vSvWDrWZ41oq8QMRO-l67dSRpeFl38b7J5KQQCKNRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت ۲۳ میلیارد دلاری آلودگی هوا
محمد درویش، پژوهشگر و کنشگر حوزه محیط‌زیست:
🔹
سرانه فضای سبز هر ایرانی به ۰.۱۶ هکتار رسیده که کمتر از یک‌چهارم میانگین جهانی است؛ همچنین مدیریت پسماند و شیرابه‌ها کیفیت و کمیت منابع آب را به‌ شدت تنزل داده است.
🔹
وضعیت در تمام حوزه‌ها بحرانی است؛ به‌طوری که فرسایش خاک در ایران تا ۸ برابر میانگین جهانی رسیده و آلودگی هوا هزینه‌های سنگین درمانی بر کشور تحمیل کرده است./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/uH-2rlDLEnw
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/691188" target="_blank">📅 15:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691187">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxevddRvwomw1rtsZ4_bXA7FIRuXew-jMCbdAQtZmi96Al0ZuVihQndRu_BAAUF6tikkUB8snY8Z3CyTzgJmdOk9eRcZcLdwt_LkVRyFNEO675f-kV5Eb62Psr1VBR_ufZc-T-MBAz2ZHNmrBU3gqzFHvlb0v3XWDvx02a24sXkswAv5UrLHR3btZDbZnj0hbpq3XBpdtZrd9f1asOrw2mj5BAdCHrr2592pzCsGTlnoH-l0vH1IHQd1c877Ygigimk5P_CLsnJQH683rjJxWz1hxSJXZTSp9_1mRNSZW1xJ5rzupn5MV0jGTFf-djLyCdjuRBqe2_ICLUivNhpqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش المیرا شریفی‌مقدم به افتتاح بزرگ‌ترین پروژه کشور به همت شهرداری اصفهان
🔹
بزرگ‌ترین پروژه کشور که به همت شهرداری اصفهان در هفته دولت سال ١۴٠۵ افتتاح شد؛ به سال‌ها حوادث تلخ، ناامنی روانی و عذاب تردد مردم پایان داد.
🔹
زیرگذر شهید رئیسی دروازه ورودی شهر اصفهان از سمت شرق این شهر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/691187" target="_blank">📅 15:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
قیمت برخی موبایل‌های اقتصادی با ورود محموله‌های جدید تا ۳۰ درصد کاهش داشته است
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/691186" target="_blank">📅 15:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af8fe0907.mp4?token=ja0scrUisnKmMM_VGXDTZewYknRA1GBlFtDOuajArVQh7Gc7ylmHFXGuxPJZ9XOz2M-Xm8kfk1l60kQ1nPNYrJpW-_baxEEkFp-AZVk6BzUigI5Ud9KiCn4N8A6YuNl82pFl34uVAZSsRM5BhWiS48DSd_M49pyemRANemKJBRCqDszCXiQnAu1PvVWzdFDEuOnoy6SWhyv336Ds41AqwCbqj1TNcFqFEhZ_gCxlsPEYNJaRyTt2C3w3KOZXy292QVmg9CZ0rFR4OJtyOEMxPZQkdPW1OqE2ZCtc8MiXSU7mc2sAMjEmOvhSJxMRSMhWcXxSbOf30qd3APg6hp0VxmWRsRS27qEK_nATbVu3iZDVgSQJeN4ZGlyNdOqbqwjS6kWCn8wW-UOvK52oh0LqiUyGSKgnZlBuS6VjGd_sOxDDMqUBVoJ8goV1eIHwmCilWZ9e6tuurbcsofnKGc2VAh4DPsN6mu7hp-bJ8_vbKjJbvK10THrQ_jQN_u0UW88DjrSQcQADOnklNdHUKPh8WXih66f7nQzLD35CEZhWRulD9YuVQ9N879dp8A_voFkWyXTudIdJA4iNOnc6GhIastu1FxdOANH4Y0hb5bTm0WINCbXI4OvkngCaZye0Rj7o4jemwYXoLw5-v_lkDI12R2qKLHzxMXu7G1f6W9KB8R0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af8fe0907.mp4?token=ja0scrUisnKmMM_VGXDTZewYknRA1GBlFtDOuajArVQh7Gc7ylmHFXGuxPJZ9XOz2M-Xm8kfk1l60kQ1nPNYrJpW-_baxEEkFp-AZVk6BzUigI5Ud9KiCn4N8A6YuNl82pFl34uVAZSsRM5BhWiS48DSd_M49pyemRANemKJBRCqDszCXiQnAu1PvVWzdFDEuOnoy6SWhyv336Ds41AqwCbqj1TNcFqFEhZ_gCxlsPEYNJaRyTt2C3w3KOZXy292QVmg9CZ0rFR4OJtyOEMxPZQkdPW1OqE2ZCtc8MiXSU7mc2sAMjEmOvhSJxMRSMhWcXxSbOf30qd3APg6hp0VxmWRsRS27qEK_nATbVu3iZDVgSQJeN4ZGlyNdOqbqwjS6kWCn8wW-UOvK52oh0LqiUyGSKgnZlBuS6VjGd_sOxDDMqUBVoJ8goV1eIHwmCilWZ9e6tuurbcsofnKGc2VAh4DPsN6mu7hp-bJ8_vbKjJbvK10THrQ_jQN_u0UW88DjrSQcQADOnklNdHUKPh8WXih66f7nQzLD35CEZhWRulD9YuVQ9N879dp8A_voFkWyXTudIdJA4iNOnc6GhIastu1FxdOANH4Y0hb5bTm0WINCbXI4OvkngCaZye0Rj7o4jemwYXoLw5-v_lkDI12R2qKLHzxMXu7G1f6W9KB8R0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگرد جدید کلاهبرداران برای خالی کردن حساب
🔹
پیامک‌های جعلی با وعده واریز معیشتی، کالابرگ، حقوق یا ابلاغیه، یکی از شگردهای کلاهبرداران برای کشاندن مردم به لینک‌های آلوده است.
🔹
اما حالا با ترفندهای جدید، روش‌های دیگری برای کلاهبرداری به کار گرفته می‌شود.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/691185" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383bde4a6.mp4?token=d7ihF5eViFkSx-2lBt7F34s2aYEJ11d1n2hhDvhLCBld0DISAcGfTEmcgfjdEYLQJFvTdFMWg_nO1CZ8c0YvuGhJKRX2q-Yp4acbgspE-rSZhS9t1fa2ty5Oq_jXRY0W9U2qz_6vJOJhDTrrRpX8s7FfDSAyyVtIUWE4BZ4XtoLVAfEv_mb1BsfH_NKdUyIhDsnp2ngodT_CEavexp1y1aMB-zgM-2cZw0zNUkymijjZTa-ApeKHroN3FmKKom-y_CpblK46V-e6h603D1faMxUDvewN36MKyjQknfLBPvZ2zyVkPsoRlBtcaezYPDNfo3K-sQxlTaucf7MV5e7TDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383bde4a6.mp4?token=d7ihF5eViFkSx-2lBt7F34s2aYEJ11d1n2hhDvhLCBld0DISAcGfTEmcgfjdEYLQJFvTdFMWg_nO1CZ8c0YvuGhJKRX2q-Yp4acbgspE-rSZhS9t1fa2ty5Oq_jXRY0W9U2qz_6vJOJhDTrrRpX8s7FfDSAyyVtIUWE4BZ4XtoLVAfEv_mb1BsfH_NKdUyIhDsnp2ngodT_CEavexp1y1aMB-zgM-2cZw0zNUkymijjZTa-ApeKHroN3FmKKom-y_CpblK46V-e6h603D1faMxUDvewN36MKyjQknfLBPvZ2zyVkPsoRlBtcaezYPDNfo3K-sQxlTaucf7MV5e7TDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز پاک کردن لکه وایتکس یا دامستوس از روی لباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/691184" target="_blank">📅 15:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
معاون پژوهشی وزیر علوم: سال تحصیلی جدید در مقطع کارشناسی ارشد و دکترا کاملا حضوری خواهد بود
🔹
آزمایشگاه‌های تحقیقاتی فعال خواهند بود.
🔹
در مقطع کارشناسی ظرفیتی وجود دارد که ۲۵ درصد آموزش میتواند غیرحضوری باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/691183" target="_blank">📅 15:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyEe6SuBm09t1UrvPTotaY4SgTDapyUXq49ZNkBUfdXIdGUFVFUqOzagiFLVCXGyod0UYLrrSaBbdlnGIsQhsfVuPTcBafm_ee3hBmhmiQDHBO8WhGqRKp4OCfA9TuHXFFqMLxO0dEUh_oO0lAKbf3eDQal-6IoXsNj6L5Lht7mN_uk6N-ddq2C7QuDoZe1S7TDCWsDFCJVka1HLaQofcQwkkSegxz4M5ab-Z-4TyQjddRUAeQ1-hYowlF1RbPJwEG9QaecGdiu-UFpDbfnRdyUYYXEd9xWfdlw8gF0o08T4T6FmKLI9f22J60apC_dSosGHOZFEJDRVPH6Jb8hVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیان‌‌های هزار میلیاردی در شرکت‌‌های دولتی!
/ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/691182" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38d91cf74.mp4?token=X8IFs9yBopIbUleCm4Cyd67xvJrOkIDCbLNoFVtuY7XPWGD3eemiMHrv9GPoHcAd7ZAIl-5n2NibqMJIF7xOHPNQhaX3KlIfnup846eiErujvWxf-6S4oTyIiTD3RS0QrtDHmGGqfTKtnkNvx7qFekFKIlTVxrDP_FTtoloss3sMmO_gn4HCtjqHPXpeJfpVoh0j01r8TWcTEW_qGs8hmxwfQCf_cbQl5qI0I7wSgvEGNya4HtocRysnz7hklS9JMsB-UjAxBz_A6K4YeclDkd7a2W89E1pUSofnQwFrdnp8VtstZ-7tMcRVIsZRb-_IS7ejY7o7VnIck8dQ7pSTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38d91cf74.mp4?token=X8IFs9yBopIbUleCm4Cyd67xvJrOkIDCbLNoFVtuY7XPWGD3eemiMHrv9GPoHcAd7ZAIl-5n2NibqMJIF7xOHPNQhaX3KlIfnup846eiErujvWxf-6S4oTyIiTD3RS0QrtDHmGGqfTKtnkNvx7qFekFKIlTVxrDP_FTtoloss3sMmO_gn4HCtjqHPXpeJfpVoh0j01r8TWcTEW_qGs8hmxwfQCf_cbQl5qI0I7wSgvEGNya4HtocRysnz7hklS9JMsB-UjAxBz_A6K4YeclDkd7a2W89E1pUSofnQwFrdnp8VtstZ-7tMcRVIsZRb-_IS7ejY7o7VnIck8dQ7pSTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهندس
اتابک
وزیر
صمت
:
بانک
صنعت
و
معدن
در
ارائه
خدمات
به
واحد‌های
تولیدی
آسیب
دیده
در
شهرک‌های
صنعتی
خدمات
خوبی
ارایه
کرده
است
▫️
این بانک در زمینه راه‌اندازی پروژه‌ها و تأمین تسهیلات سرمایه در گردش مورد نیاز واحدها نیز عملکرد مفیدی داشته است.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691181" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1HD6tK470Z9CELReeybUrN2-lY_Bp4d-uGZsZD4TB_Cjfu26QCYYtDuCKCFVUjt3ZQac4u9WRopdWKHe-N1DHmznoClYi6KUMIGL2Z4ZfOIwcVYsj3EDSqVTWbjUwlni683TZRfY1G1CHAnWzYdrH-Cwge4B7rbKriAUi2Id_2keq2pSvFD_Y1VVLO6Li9ZgThjTPKDYTTV2h9ig2c6lnO0wRjoSODXcsJ9mhEVP8F-eDioMYa8vBSIMGFqHRC4T5BmRq5XWwHxnYOxLXg2T15pYMmCunHw2ofqt9fGSPQad1-WoKv1DuLCS8UNAz9lUxCovRKVhKVCKwIfFlKPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXUs5VqRJgnIifvfQsab3FAQwca0MW3QgRG_KU4vSbzKRkS4V_Ft0dBxxMNTlbrnPcDEY9rQTSTq4kNEC6wEmi5YUEF0k18eR0G-GvOvF7v_qmUVhjhOkv6BFFzath4NFwGWDEMndLc7Z4-ju8EejJJmcHNgBhMQo__cfi_9zyKJ739z7zmgV9OtGArzXwrd0F13tN2q-_e1AadegUd-z7bJWYsda38XjFZa5s17JKVX0Cd3g1i7wJ3oPIFREUY1N0wj1i5a7S2m6wWLNcerVMmUUHyGnb8xqrixOfP3SstnwLbdEK2MTqqeAX4c2YdYSPuo7NNB5cRhszO_Al8LHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض گزارش شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691179" target="_blank">📅 14:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af90ba159.mp4?token=rja-nkJIdgv1jpUc393sMVyEy9JbBPHhffGWYodyqEbzXmjhNmNnCZ8PtMcOxssc-UoKWaCHma9Nc3J8zIqgInIRtKJBtetkGD7GbQfOOsghiN85rmJx_SwUQZ9PIkFfDRELzfbMqp52J39aqkH7CVnymGf7WQqUCXGbawb-FmPbC72eg6sFn6FU5ZcQfCguaprjQ6_kAyPjOBZuszxKWJHb9CyNMdB4f8HC1E35M5KXiQAT7sOJNA6K3KHLlHvuKVIFoR5fi1ia33JTmbwPLoTrkVHk5HlP9BF3maNGjS21PFA4iDOn7ugWmZd6-2Nm404M8LnckkZ2oCuolBG6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af90ba159.mp4?token=rja-nkJIdgv1jpUc393sMVyEy9JbBPHhffGWYodyqEbzXmjhNmNnCZ8PtMcOxssc-UoKWaCHma9Nc3J8zIqgInIRtKJBtetkGD7GbQfOOsghiN85rmJx_SwUQZ9PIkFfDRELzfbMqp52J39aqkH7CVnymGf7WQqUCXGbawb-FmPbC72eg6sFn6FU5ZcQfCguaprjQ6_kAyPjOBZuszxKWJHb9CyNMdB4f8HC1E35M5KXiQAT7sOJNA6K3KHLlHvuKVIFoR5fi1ia33JTmbwPLoTrkVHk5HlP9BF3maNGjS21PFA4iDOn7ugWmZd6-2Nm404M8LnckkZ2oCuolBG6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجه سابق آمریکا، ادعای ترامپ در مورد «التماس ایران» را مسخره کرد: اگر منظور از التماس شلیک پرتابه‌های بیشتر است، پس روش جالبی برای التماس دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/691178" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
فرودگاه ریاض هم‌اکنون/ ستون‌های دود از فاصله چند کیلومتری دیده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691177" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8d853409.mp4?token=bcIjlzrexFwf1wa-9AUyt1WJzUZeKdzrNIo9Oqgr36s9Zrk_MnKwEB1dnPLlxS9eXYK2nfONcg7yois9iGjgYBPY40sIydXGfratNufM94Mx83QzUoNffPoyM9bwIeJ6Wr-DlcNxg7n3CPgW9nT9uHKWq2O8hlr80jBesanQA87GCGJhcOLpiGgnm_8I7wPvH0_SBwqFfekHZH2AbgpIDCz9PKzTwSx1nffQYSk0G4wjONJw8dWGkHxoJf-gZp9YJiIecuh_3kcjoVt3w2JGP0my1qZbD3IF83-9L9ACidKt-y8CgkW2JNKp0e8xCaWuJW_YjPUwvakvHhzCf5LGdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8d853409.mp4?token=bcIjlzrexFwf1wa-9AUyt1WJzUZeKdzrNIo9Oqgr36s9Zrk_MnKwEB1dnPLlxS9eXYK2nfONcg7yois9iGjgYBPY40sIydXGfratNufM94Mx83QzUoNffPoyM9bwIeJ6Wr-DlcNxg7n3CPgW9nT9uHKWq2O8hlr80jBesanQA87GCGJhcOLpiGgnm_8I7wPvH0_SBwqFfekHZH2AbgpIDCz9PKzTwSx1nffQYSk0G4wjONJw8dWGkHxoJf-gZp9YJiIecuh_3kcjoVt3w2JGP0my1qZbD3IF83-9L9ACidKt-y8CgkW2JNKp0e8xCaWuJW_YjPUwvakvHhzCf5LGdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فؤاد ایزدی: انتظار بازگشت آمریکا به تفاهم‌نامه یک خسارت بزرگ است!
کارشناس مسائل آمریکا:
🔹
توافق یا تفاهم با دولت فعلی آمریکا امکان‌پذیر نیست. انتظار برای بازگشت آمریکا به تفاهم‌نامه‌های قبلی یک خسارت بزرگ است و تنها احتمال حملات گسترده‌تر را افزایش می‌دهد./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/yRIXrUwC5Xc
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691176" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bd5beb93.mp4?token=NC5Z7b0rcRtDL6awOIf-X7naBty-UUwoqTUivJ5aOQKa93LD1WUhTnB722cW_UaAdSZWuHyhLNvEf0tlcVkCg-SPaq5lB819tYVKfp0j57kLFoGMLeLn4a0VfKCuVp_XPmlgFAvWgAlFMVQNrY6x-fMndoDlH4izCbyFiHsZugY7KaZ_40kxg3-fdrkzr0edBvYNbbedNY1Bjp7HstZWEDcn_ElESV598roN4YJs6ke4i5s2LOcamt5_1IYwVIyma7z6_Sun2lQpX8WjcvRwC8DArtqsi92Fufz16ngTCEO-VuTXqdUa8sizqbveJ243hvRNoWCO3CkIZMnO_6_qkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bd5beb93.mp4?token=NC5Z7b0rcRtDL6awOIf-X7naBty-UUwoqTUivJ5aOQKa93LD1WUhTnB722cW_UaAdSZWuHyhLNvEf0tlcVkCg-SPaq5lB819tYVKfp0j57kLFoGMLeLn4a0VfKCuVp_XPmlgFAvWgAlFMVQNrY6x-fMndoDlH4izCbyFiHsZugY7KaZ_40kxg3-fdrkzr0edBvYNbbedNY1Bjp7HstZWEDcn_ElESV598roN4YJs6ke4i5s2LOcamt5_1IYwVIyma7z6_Sun2lQpX8WjcvRwC8DArtqsi92Fufz16ngTCEO-VuTXqdUa8sizqbveJ243hvRNoWCO3CkIZMnO_6_qkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاطم شدید در پرواز
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که یک هواپیمای مسافربری را هنگام عبور از تلاطم شدید نشان می‌دهد. در تصاویر، هواپیما به‌شدت تکان می‌خورد و بال آن نیز از داخل پنجره در حال خم‌شدن و نوسان دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/691175" target="_blank">📅 14:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_3CyR_YtimBn3cTErAjWWKp1N_Yn7t3oFacIjWKzUB5m2zhwlH-1XTLPbfaYXqSxYGa1SKW-qxZh4UpH5tcrzngLY0yIKOKeLEidk0TMKaNFtLlcOBxu0sYtlujKCqM-Xfrew3xlTVJouUrRs18q4kY6wVq_3VBrn4_VhbTx_HTMYcURM_b9scH0Ct0LZobWkL1afr9jKbyZa8ik-YcytmbcVJlAerCONlbLhbupZUU8h6qPh6B74sBSxctzhoNX_XTgNLwLO4nPIdwDsqqU1cZZ0W9mgWRX3DSbJBGo6edGjGBoJyNAgP6zNfs5z70VBx53J_zNUhuBEwrGpT73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با همین گل‌های‌ ریز می‌تونی جیب‌هات رو خوشگل کنی
🌼
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/691174" target="_blank">📅 14:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835123f205.mp4?token=Zc-UEeGmdHHPNzvnzguvhkzk2VUFhX6eOPwXX7WxIFt-e5ehc15oaPyGsFGTKolgaiC9D-mz4hxC-pu1cYLg_05aEjgqm27dDCiGLhO1HZjAsh4GzKxkNWwfmsk-fbTQOv-v7qhhujKnAPCFYZPiGH6oCF4yQWij5JKdQwV6xD6H8HDKZzwcBJHkNKsgG95V1Ps5bwCjoWCuaJpXJ0sboNeueWv8KNcmhf4oCWlFOGAsAg4IEVXGExZqnvfL2ukvdaq2jkVXrmPLocPO7kw-vUmG1fIOB1Qn49zyao6rBwzhWwZSJUqK3qMKr2WKSI21EqRYffHheyFVAiQ2oy_mR0fgFAVkHDSE5j96SU-irc3bJvyqNdQeff-Yjhn8X5tN4iY8AXiHUz5fhxHq_nVzlR2HP4yGbn7xr4ls4BRBBV_8Ci70e1pGdB0FN4q62ku5EObdpL1Dew0J8l9IdJ94cZZSCKMcb4Yts4Aj1miPRZkV03xMPLJ7ucyIFVb2foWPTxvPLPc-ICegBLvfdK0m0hxlnbaE7dYj3uDPxoACuWNWley_KxSSYT6ijjJNqBhedr_IgcihE7N-uQ74_Fa_jUejy501jxfhogHSFmMgENwr0uvMteKvC28OSbF5tx-vLqQQZYuxecdbwsIVHY3JQojVSuKrfGeSWhub8G4NuHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835123f205.mp4?token=Zc-UEeGmdHHPNzvnzguvhkzk2VUFhX6eOPwXX7WxIFt-e5ehc15oaPyGsFGTKolgaiC9D-mz4hxC-pu1cYLg_05aEjgqm27dDCiGLhO1HZjAsh4GzKxkNWwfmsk-fbTQOv-v7qhhujKnAPCFYZPiGH6oCF4yQWij5JKdQwV6xD6H8HDKZzwcBJHkNKsgG95V1Ps5bwCjoWCuaJpXJ0sboNeueWv8KNcmhf4oCWlFOGAsAg4IEVXGExZqnvfL2ukvdaq2jkVXrmPLocPO7kw-vUmG1fIOB1Qn49zyao6rBwzhWwZSJUqK3qMKr2WKSI21EqRYffHheyFVAiQ2oy_mR0fgFAVkHDSE5j96SU-irc3bJvyqNdQeff-Yjhn8X5tN4iY8AXiHUz5fhxHq_nVzlR2HP4yGbn7xr4ls4BRBBV_8Ci70e1pGdB0FN4q62ku5EObdpL1Dew0J8l9IdJ94cZZSCKMcb4Yts4Aj1miPRZkV03xMPLJ7ucyIFVb2foWPTxvPLPc-ICegBLvfdK0m0hxlnbaE7dYj3uDPxoACuWNWley_KxSSYT6ijjJNqBhedr_IgcihE7N-uQ74_Fa_jUejy501jxfhogHSFmMgENwr0uvMteKvC28OSbF5tx-vLqQQZYuxecdbwsIVHY3JQojVSuKrfGeSWhub8G4NuHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری رئیس سابق دستگاه اطلاعاتی مصر: واشنگتن در سال ۲۰۱۶ از من خواست تا مقدمات سفر اوباما به تهران و دیدار با رهبر انقلاب را فراهم کنم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/691173" target="_blank">📅 14:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درخواست وزیر کشور پاکستان از ایران برای جلوگیری از انصارالله یمن
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
در رابطه با سفر وزیر کشور پاکستان به ایران بحث‌هایی انجام شده و درخواست‌هایی نیز در رابطه با اینکه ایران از نفوذ خود استفاده کند و مانع فعالیت انصارالله شود مطرح شده است.
🔹
در این رایزنی‌ها قرار است درباره تنگه هرمز و تنگه باب‌المندب نیز گفتگو شود.
🔹
احتمالاً امروز یا فردا مشخص می‌شود که ایران با سفر وزیر کشور پاکستان موافقت کرده است یا خیر.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/691171" target="_blank">📅 14:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be121f01dd.mp4?token=XLWx45X-tp34k2QboFFGihKpXaEtz-qrpt-z3siOcucA_ztLWZWzdTID_94YlVB08ALUaH9mEh5g00VyO3EfkiZRzKnByTFNFu3Xr9f3QgoMoOWgsZxr5z3vWIgfELg7_elpwzk1V85o_wwrN4PFigzHftcxuFxkMVGGeXGuUxFu3mlo_2EWtD2dQiI1ayGkPDhj9GLsAxXMVcg4KkAVdiDkIlly4DugaKOjCjkQ5yfiWjPrfaPuEH1l92NkFCdIShP4Q7N3uaSHV2erMkygBuSghRuh81upK13RJB98aJEVr-na-g1aOTeOKLLZRU-b6FtEjL9u-_lEvgrwHJgJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be121f01dd.mp4?token=XLWx45X-tp34k2QboFFGihKpXaEtz-qrpt-z3siOcucA_ztLWZWzdTID_94YlVB08ALUaH9mEh5g00VyO3EfkiZRzKnByTFNFu3Xr9f3QgoMoOWgsZxr5z3vWIgfELg7_elpwzk1V85o_wwrN4PFigzHftcxuFxkMVGGeXGuUxFu3mlo_2EWtD2dQiI1ayGkPDhj9GLsAxXMVcg4KkAVdiDkIlly4DugaKOjCjkQ5yfiWjPrfaPuEH1l92NkFCdIShP4Q7N3uaSHV2erMkygBuSghRuh81upK13RJB98aJEVr-na-g1aOTeOKLLZRU-b6FtEjL9u-_lEvgrwHJgJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض گزارش شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691170" target="_blank">📅 14:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691169">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عراق محدودیت پروازهای غیرنظامی در مناطق غربی این کشور را لغو و حریم هوایی این مناطق را برای پروازهای غیرنظامی بازگشایی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691169" target="_blank">📅 14:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691168">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رویترز: تصاویر نشان می‌دهند که شعله‌های آتش و یک ابر بزرگ از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691168" target="_blank">📅 14:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691167">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975513a38.mp4?token=INAEw284je6wNZKXQBP50ix129gX6SFrSLzjJwvDNMZqdX0gGbywyYCMNRM_Q9urLM8RE1nN64dTNG9Rbkan9qPx3VqmQF05lCUqDFXo_ZX4RNjzMdifMdD3kI1x1wpRy3qVOKNh8IrUa3t0lGKptpg_j6LGDsI6ZA01evgDGO1mj-rM9Geasg66D7QKWDuYRziEFKeyVt-6Lgxgy6PP6NF13-sVYw7ZGxQiDjnNFzqIjRSA10O7AnnPUSOxHVUt_dz5uVi_H-2Nq87VcNYJt6r9FkAzXIxbLDIf_XJ4mXmpe-PSitdhp-uxznP3s-tFTs1mfolI4kuDAAZx2ERUdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975513a38.mp4?token=INAEw284je6wNZKXQBP50ix129gX6SFrSLzjJwvDNMZqdX0gGbywyYCMNRM_Q9urLM8RE1nN64dTNG9Rbkan9qPx3VqmQF05lCUqDFXo_ZX4RNjzMdifMdD3kI1x1wpRy3qVOKNh8IrUa3t0lGKptpg_j6LGDsI6ZA01evgDGO1mj-rM9Geasg66D7QKWDuYRziEFKeyVt-6Lgxgy6PP6NF13-sVYw7ZGxQiDjnNFzqIjRSA10O7AnnPUSOxHVUt_dz5uVi_H-2Nq87VcNYJt6r9FkAzXIxbLDIf_XJ4mXmpe-PSitdhp-uxznP3s-tFTs1mfolI4kuDAAZx2ERUdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعتی ۲۱۱ میلیارد تومانی (۱.۱ میلیون دلار)؛ ساخته‌ شده از شهاب‌سنگ ۵ هزار ساله در آرژانتین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/691167" target="_blank">📅 14:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691166">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN5yo4cNRzsDYOd4-HFgeKa2J9J1llvq9IbaScUio6Ty6Jjv0_zIcIecguYZr3K3hSbC586CfMmpwNMiY9xMxj08nRphzVLmHLlrKjbx6K3YEw1JhE7oLN6-N3gxtZgJhxAQbPRjia2gHK-S6o1pla-adXk3eiKpF9IGOG1avlF7kfIRrUhXRapU-0cPf3XxVMomuy8GbhnHF3F8OAdkFjMk2RMq_tmmCnSS1ppShujWW-9UV-jxfU6A2sHZrYp6stRYNYY_sVtju3WcX0hKD7_ctLc1ZaMsRJSXaAUs4QkdIIrR8gsklrgmuACrg6NyIFnssWQe0UdqQpZVYg10Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا خبر داد:
رکوردشکنی بانک کشاورزی با ۵.۳ همت سودآوری/ اضافه برداشت از بانک مرکزی صفر شد
🔻
مدیرعامل بانک کشاورزی با اعلام رکورد ۵.۳ همت سوددهی این بانک در سال ۱۴۰۴، این موفقیت را دستاوردی بی سابقه در تاریخ بانک کشاورزی دانست و از افزایش درآمدها، کاهش هزینه‌ها، صفر شدن اضافه برداشت از بانک مرکزی، بهبود قابل توجه شاخص‌های کلیدی و ثبت رکوردهای جدید توسط این بانک خبر داد.
🔻
وهب متقی‌نیا در جلسه مجمع عمومی عادی سالیانه این بانک که با حضور وزیر امور اقتصادی و دارایی برگزار شد، در تشریح عملکرد سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ اظهار داشت: سال گذشته علیرغم چالش ها و بحران ها توانستیم با انضباط مالی و ریل گذاری درست در مسیر گذار از بانکداری سنتی به بانکداری نوین، دستاوردهای چشمگیری را در زمینه جذب منابع سپرده ای، افزایش سهم از بازار منابع بانکی و بهبود شاخص های کلان مالی کسب کنیم.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/691166" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691165">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
منابع عربی از چند انفجار در نزدیکی فرودگاه ریاض خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/691165" target="_blank">📅 14:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691164">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqgZeJ-2D-lKCt3gWjW6S0nDuGg5PTN1a3XJSZYymRp0BiSegT9O8TjoBRl6jRV2fq4WQssag_rnMfDEMj0msaja02645F0HnFxIZqDO5Ek0aOEIMcAAPgLUVSSCQ9eC9_VvKvtMBf7AWiQGTDxZ6unxwwkAB7nu5lSfzpXsiS8MnkHzppWPtNbK-DnEbBnkYkZq8Yi1QJMK9HBQDUjPoONWvEfgrHzVBSanEjLp927JD_ylbjBiQihYs4h1Kh_UXefcTlYXe-i1Q34bQT-07WPmV4N2QFVyHtZt36S7wX5F_QQSZvuLinx1F5nVmNoH7ra_McZubUwudhq7H3adWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: تصاویر نشان می‌دهند که شعله‌های آتش و یک ابر بزرگ از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691164" target="_blank">📅 14:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21558efae.mp4?token=KI3Kr6KOFo93c4zkv-GdV6Imle8h79ZxRpLTROCH1dz2Of77Y6utQ_EOA7QEDfBOES1k04Q82qsBrP6Bcqva0zH3QhZzH11M6ygsjbgTD1a8mtfVGk7OAoar-Hei_ddOtqsIcbApWc3rK312wpAmFG6UaCkqzLJmInZBRsawq2SvILQqm9dA2eZQWSrY7jLnDfEXT34DhNEApXw2EQ-9JYcQ9M91Hy23rH0WBnl6grBD58NHWihvC9R0h9tk_G5ypzBIr9X-GOFMrX-67bPhlqJH-ps1RmIoQeriavDf94BRuTOOOq4FMC9WBCz5vUNjFLp-bikpii-U2SU1N2vcGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21558efae.mp4?token=KI3Kr6KOFo93c4zkv-GdV6Imle8h79ZxRpLTROCH1dz2Of77Y6utQ_EOA7QEDfBOES1k04Q82qsBrP6Bcqva0zH3QhZzH11M6ygsjbgTD1a8mtfVGk7OAoar-Hei_ddOtqsIcbApWc3rK312wpAmFG6UaCkqzLJmInZBRsawq2SvILQqm9dA2eZQWSrY7jLnDfEXT34DhNEApXw2EQ-9JYcQ9M91Hy23rH0WBnl6grBD58NHWihvC9R0h9tk_G5ypzBIr9X-GOFMrX-67bPhlqJH-ps1RmIoQeriavDf94BRuTOOOq4FMC9WBCz5vUNjFLp-bikpii-U2SU1N2vcGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها اول روی مذاکره و توافق اصرار دارند چون به نظرشان کم‌هزینه است و بعد وارد حوزه فشار و بحران می‌شوند و به عبارتی بحران را جنگ می‌دانند
🔹
آرزوی آمریکایی‌ها این است که ایران را به سمت تجزیه، تسلیم و براندازی ببرند.
🇮🇷
…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691162" target="_blank">📅 14:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241bc7b57f.mp4?token=kdHIq_m0eq3-wf9Bv76UHAZ5LndTvWZFWuSPNt9nS7RSjFfh-YjLyU6USF7TE5tsOY7L_sZi8GD0rqM_Janu8KhbNIxrcvyoO-0ztJpLrDbbGQ2Yh1N27l_2g_n2mfwQUXuIwidDfOuczsytBn9KJ1rkC3nIgbJP1MvrCwkvL4CVREbSvhlb83iE4SwPnQQ06OGoYpnueJR-lNkWRnjuOLvcUlh32gaipKnOQAnmWCxY9YAMZXuq2o-LY7Y0BLCR4ceJrOWKK7G-40aWycUixMyfNkcvHBQiA7BR3pdIPt4nhsQSF7U0IXgYLXgGynOg-pzUuV1mALoMaHHHa6QxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241bc7b57f.mp4?token=kdHIq_m0eq3-wf9Bv76UHAZ5LndTvWZFWuSPNt9nS7RSjFfh-YjLyU6USF7TE5tsOY7L_sZi8GD0rqM_Janu8KhbNIxrcvyoO-0ztJpLrDbbGQ2Yh1N27l_2g_n2mfwQUXuIwidDfOuczsytBn9KJ1rkC3nIgbJP1MvrCwkvL4CVREbSvhlb83iE4SwPnQQ06OGoYpnueJR-lNkWRnjuOLvcUlh32gaipKnOQAnmWCxY9YAMZXuq2o-LY7Y0BLCR4ceJrOWKK7G-40aWycUixMyfNkcvHBQiA7BR3pdIPt4nhsQSF7U0IXgYLXgGynOg-pzUuV1mALoMaHHHa6QxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقاشی عجیب ۷۵ ساله؛ اثری که در بیمارستان روانی تبریز خلق شد
😳
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691161" target="_blank">📅 14:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691159">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e48bb36d3.mp4?token=CEuSiQAaRmbsh5xZlQsKzM6xO79yS61Hwt5SzVmUz0lWDZgXWkFRUnJ0lIc1rOX0_ithr68tHtATOczUXMvwpvdDlqRZIeD2yJZUcsFOojXMceAwy42PXIAXgIOBvQCIWgOpBrhUEWCn7nnAUu9zW0yMo9ulYmdNI8INxd0DdwqSMys1_LVm76yjlk2tq3jLgHlFq8sdj-TokaPancu3-yy-yHYSkelQwE-3JMJUSL7OZKfLfY1O8LG-hgMpdhcubv1SfiTR7z7_ib0PxtsSxAHtXaiHSzn7hlmsGGbYYVwlQVeUMKoBD1tihr3xW8SQ05heZTcror7NG6oK3mT_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e48bb36d3.mp4?token=CEuSiQAaRmbsh5xZlQsKzM6xO79yS61Hwt5SzVmUz0lWDZgXWkFRUnJ0lIc1rOX0_ithr68tHtATOczUXMvwpvdDlqRZIeD2yJZUcsFOojXMceAwy42PXIAXgIOBvQCIWgOpBrhUEWCn7nnAUu9zW0yMo9ulYmdNI8INxd0DdwqSMys1_LVm76yjlk2tq3jLgHlFq8sdj-TokaPancu3-yy-yHYSkelQwE-3JMJUSL7OZKfLfY1O8LG-hgMpdhcubv1SfiTR7z7_ib0PxtsSxAHtXaiHSzn7hlmsGGbYYVwlQVeUMKoBD1tihr3xW8SQ05heZTcror7NG6oK3mT_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عوامل درگیری و قدرت‌نمایی خیابانی در چالوس بازداشت شدند
رئیس کل دادگستری استان مازندران:
‌
🔹
در پی وقوع یک درگیری خیابانی و قدرت‌نمایی در شهرستان چالوس که منجر به اخلال در نظم عمومی شده بود و با انتشار فیلم در فضای مجازی امنیت عمومی و روانی شهروندان نیز خدشه‌دار شده بود، موضوع در دستور کار قضایی قرار گرفت و عوامل این درگیری شناسایی و دستگیر شدند.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/691159" target="_blank">📅 14:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691158">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها اول روی مذاکره و توافق اصرار دارند چون به نظرشان کم‌هزینه است و بعد وارد حوزه فشار و بحران می‌شوند و به عبارتی بحران را جنگ می‌دانند
🔹
آرزوی آمریکایی‌ها این است که ایران را به سمت تجزیه، تسلیم و براندازی ببرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/691158" target="_blank">📅 14:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691157">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJOeocpr1vE6Iv5KYt8qpxJD9wfQGM-X9LLN7phnRUGMLc43HbqoI1iQn3JtOCyZV6ppxdtJTCnAit0rmeXUrKCB5eT9IyXl4aCvU50hVUbMx0q8SxDk4AXlI3PebGmvIC95fzPJSGc9qJf8_gd36J571JOMpeVFSBrHj4Y8ebRwVx8WRcIc8Y1GDFBv31uwxYGbcHJ_JjuePg1XUjsTOZrXnWsMNEJXPA7ucSVm7AyOIekI1ockwjkTwc1VOIeKvlduH23EljX-tidW6TgbjPFhVEd19rNIPaYbyF5HIk6LMv5KWmCOwxjrVZ87pyoJaLKQpBgRP3nUFo-rcJTy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنهایی چیست؟
روایت‌های متفاوت از یک حس مشترک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/691157" target="_blank">📅 13:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نماینده آمریکا در سازمان ملل: ترامپ در سخنرانی خود در سازمان ملل، به موضوع جلوگیری از دستیابی ایران به سلاح هسته‌ای می‌پردازد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/691156" target="_blank">📅 13:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b00b674dd.mp4?token=iR3WunQewpsXDMTJFNXIMWXEIRuwuZnM2yQBQnCoqK285n1DMeeO3LFPfgaNRAW3sS2O1ByRrZHUoNYiM7eXvVwi2dLXFNsBmcWBjqK2UY2Y-Wuf0ZbMcTION7GjCgQxig4GWYUqYpI3_Aus_u_uffGGwHSoQMVO_dJ8xBqVeuSNUuKKhbwVGSZCQyG7ZUQO0igT9LGJzFkaXQaUy460tqLvg53gvRGwqAzywIMPVlQO6uEn2-Udb0KBne67pOUgWkBgWyieb0lVAjVz5xXVZmt-WUsUnp0hqWDaLklCZ1_aKKzuYtyZoU1jetzhjotvTGq7EZ_kkLh_npx99WNDq5xdqxmRJ1b-E1U8Qltsw1Isge-ejdXY1wQdh4_JZktKg49B1MBsFc8mFCEEF8JyfW9t83VaXI3VIQySXNLfvb5n4RarXOuKHgfMz5PsgbPlUjWjXK_wKx4gYvA8KU-05BFlA0sdQfpg8Q6Aisr_co0R85SBJaFBTaLHcFryS27ZINj2WzNgVoOyFXdvChR-CstM_xsolZqAOjGTqOyAiI2eVmSK4aFCvKG0FQ1KY6vWv2uUo3pxa1bTeE9L-r-JIv-MRvz0q5dD8ZAkK04Ghq3nZ2cy6c5QhiGmZqIRXtyHL0_R9vABsmz84neDy8iGiZ3iLvJorqawjHlH0ad4p5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b00b674dd.mp4?token=iR3WunQewpsXDMTJFNXIMWXEIRuwuZnM2yQBQnCoqK285n1DMeeO3LFPfgaNRAW3sS2O1ByRrZHUoNYiM7eXvVwi2dLXFNsBmcWBjqK2UY2Y-Wuf0ZbMcTION7GjCgQxig4GWYUqYpI3_Aus_u_uffGGwHSoQMVO_dJ8xBqVeuSNUuKKhbwVGSZCQyG7ZUQO0igT9LGJzFkaXQaUy460tqLvg53gvRGwqAzywIMPVlQO6uEn2-Udb0KBne67pOUgWkBgWyieb0lVAjVz5xXVZmt-WUsUnp0hqWDaLklCZ1_aKKzuYtyZoU1jetzhjotvTGq7EZ_kkLh_npx99WNDq5xdqxmRJ1b-E1U8Qltsw1Isge-ejdXY1wQdh4_JZktKg49B1MBsFc8mFCEEF8JyfW9t83VaXI3VIQySXNLfvb5n4RarXOuKHgfMz5PsgbPlUjWjXK_wKx4gYvA8KU-05BFlA0sdQfpg8Q6Aisr_co0R85SBJaFBTaLHcFryS27ZINj2WzNgVoOyFXdvChR-CstM_xsolZqAOjGTqOyAiI2eVmSK4aFCvKG0FQ1KY6vWv2uUo3pxa1bTeE9L-r-JIv-MRvz0q5dD8ZAkK04Ghq3nZ2cy6c5QhiGmZqIRXtyHL0_R9vABsmz84neDy8iGiZ3iLvJorqawjHlH0ad4p5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از رؤیای شهر آینده نئوم تا حراج تجهیزات؛ شکست بزرگ قلب چشم‌انداز ۲۰۳۰ عربستان
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/691155" target="_blank">📅 13:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رئیس سازمان پزشکی قانونی کشور: هیچ پیکر شناسایی‌ نشده‌ای از شهدای جنگ در پزشکی قانونی نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/691154" target="_blank">📅 13:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4156983d65.mp4?token=stSTOD6clEToGrRY4SRemS-Ohxmsj0QpPy6dEhYTmsm68z1LKe6UNv8c-vUKA-VlnaVKSV3B_k9eWFck2NQc7mD-UeW7-hH5_UG7J5jxCZhSACdhQyjHRoGKXHqlAOMEIWX0_6BDPiPjKCtJcy7iJizaTcmz8fMjukR3jHqiIOEQmMyFwcqk_M7qt1c-I12vtKeHck-_6UXO2fbgTSBvtSgqNHMdvKnhIliTjGy-TWAahlx168WWU4ig0UxhcdJFPuKwkiN3R8QmRhLczDjn2LVZb0UTdDGkZUk6rEW4LAarIcuoEW-YM1BHwSqBsYx-6jd8EFRtGHX78RgDy7aDRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4156983d65.mp4?token=stSTOD6clEToGrRY4SRemS-Ohxmsj0QpPy6dEhYTmsm68z1LKe6UNv8c-vUKA-VlnaVKSV3B_k9eWFck2NQc7mD-UeW7-hH5_UG7J5jxCZhSACdhQyjHRoGKXHqlAOMEIWX0_6BDPiPjKCtJcy7iJizaTcmz8fMjukR3jHqiIOEQmMyFwcqk_M7qt1c-I12vtKeHck-_6UXO2fbgTSBvtSgqNHMdvKnhIliTjGy-TWAahlx168WWU4ig0UxhcdJFPuKwkiN3R8QmRhLczDjn2LVZb0UTdDGkZUk6rEW4LAarIcuoEW-YM1BHwSqBsYx-6jd8EFRtGHX78RgDy7aDRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابزار Claude Code Projects برای مدیریت پروژه‌های طولانی برنامه‌نویسی معرفی شد
🔹
این ابزار می‌تواند دستورهای متنی کاربر را دریافت و آن‌ها را به چند رشته کاری موازی تبدیل کند. تمام شاخه‌ها به یک حافظه اشتراکی متصل هستند و تغییرات و تصمیمات مهم در سراسر فرایند توسعه نگهداری می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/691153" target="_blank">📅 13:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78ede1a158.mp4?token=AtcJVuH8J0CIR5J3UJnNbd5sbMDw8Gtd3rYlJHYI6mQ4MMtmeEiIaIBpVqjUs8rtjDeDiscAQe_ZJpIbdGBdvRoTaksuIh3ETY5winehbMjXFG8FSqzw-UHmUAYWPENyXn9ALvQlYr-uBCEwuwFQVUeCflrUsezOHd4KICau486skZgYMUqjl0QlBmRg3eh35jcSRFmKhIb3LPBUTBVXlPw6Wr8AJNhW2KTlCXsAzhO6CB5cQH0W0lkjpFd3EsWL4bq0-SDejti1oQvmRY0Z5C1eXC16Mw8MBLBW2R8VP9FTyK6--JCphZW_6BqEzLnehWrS-2Zfsx5oyrhzqAxSrIapNSe4p5IDkMU4vf936iapV_PL6v26x1SDjff7f8neHJilcmIjFgmwpCodUnwIOTERW5DoNAMdawP_3X0GpB0b_E5tvGmP-x0JNO8K-0M6GsX8Ba6vyVUF61oN1nRyqNsTHaympR2HYRLUuKFmDB-UMrX-U-Lr0iJmqy3QlT2t1NKGFeU6fb0eNOvzn6K86vtWCGK8oYwdP27qjuM6Miq7SQA6leOFzyrw6nf7X557z-1gjafsQdmyhiQMLZ1BwLDl5WF7pO1ZfYbPFCUFow_q2xzMJvWiKg4TaR2MyDHvoj0CEJgR-rzC-iLzKb_B4XqOjhqn_LVq9Frs_D1Jcr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78ede1a158.mp4?token=AtcJVuH8J0CIR5J3UJnNbd5sbMDw8Gtd3rYlJHYI6mQ4MMtmeEiIaIBpVqjUs8rtjDeDiscAQe_ZJpIbdGBdvRoTaksuIh3ETY5winehbMjXFG8FSqzw-UHmUAYWPENyXn9ALvQlYr-uBCEwuwFQVUeCflrUsezOHd4KICau486skZgYMUqjl0QlBmRg3eh35jcSRFmKhIb3LPBUTBVXlPw6Wr8AJNhW2KTlCXsAzhO6CB5cQH0W0lkjpFd3EsWL4bq0-SDejti1oQvmRY0Z5C1eXC16Mw8MBLBW2R8VP9FTyK6--JCphZW_6BqEzLnehWrS-2Zfsx5oyrhzqAxSrIapNSe4p5IDkMU4vf936iapV_PL6v26x1SDjff7f8neHJilcmIjFgmwpCodUnwIOTERW5DoNAMdawP_3X0GpB0b_E5tvGmP-x0JNO8K-0M6GsX8Ba6vyVUF61oN1nRyqNsTHaympR2HYRLUuKFmDB-UMrX-U-Lr0iJmqy3QlT2t1NKGFeU6fb0eNOvzn6K86vtWCGK8oYwdP27qjuM6Miq7SQA6leOFzyrw6nf7X557z-1gjafsQdmyhiQMLZ1BwLDl5WF7pO1ZfYbPFCUFow_q2xzMJvWiKg4TaR2MyDHvoj0CEJgR-rzC-iLzKb_B4XqOjhqn_LVq9Frs_D1Jcr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: جنگ، تحریم و زور نباید به ابزارهای عادی سیاست تبدیل شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/691152" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e33fef086.mp4?token=pcXheaUVE2EoS8jhY7gqhN2qZItlcx0M-t-iFOUaRtLTQj37ANfrWMbP1E6dXp8JPDn9f8ldnTNNqVPmAaXRZ32Tn-MjAwgMRCO0fCYtSJtTyKTkhUDnv8XoLE2gsT-LOK3_yilrFXVArcHo-t9Jn808j2nqGzAQbGNqaN05zz7TgG_fZiAMqVdNQCRGUG7D41QmOY5g06zA2Cqm9HqmaXpYY3HTT385NrINR3Hletn14RG8P_xroj3M-7aCUI8xthJndFJUrbp7BnNZcbNouFCxtpqc4t0lDwDuH6oVvUIv0BxBiMKEvrB3UHBJbd9p4qkdWp4uQa7oYuT3jfe6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e33fef086.mp4?token=pcXheaUVE2EoS8jhY7gqhN2qZItlcx0M-t-iFOUaRtLTQj37ANfrWMbP1E6dXp8JPDn9f8ldnTNNqVPmAaXRZ32Tn-MjAwgMRCO0fCYtSJtTyKTkhUDnv8XoLE2gsT-LOK3_yilrFXVArcHo-t9Jn808j2nqGzAQbGNqaN05zz7TgG_fZiAMqVdNQCRGUG7D41QmOY5g06zA2Cqm9HqmaXpYY3HTT385NrINR3Hletn14RG8P_xroj3M-7aCUI8xthJndFJUrbp7BnNZcbNouFCxtpqc4t0lDwDuH6oVvUIv0BxBiMKEvrB3UHBJbd9p4qkdWp4uQa7oYuT3jfe6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب دوربین روی لاک‌پشت، سفری دیدنی به اعماق آب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/691151" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVmN_IjMV7HFMMyIsDu4X4C65fsnMiqczNvkCqgv7xGwAUifjm6gLIjuK0ZKKFJ5bwvMidQoQ25PeCZkUzWQq4IifDMFDE0rQRWYbcbxJwPaoNy-Wu5hxUUVjK97CVLfmbQosOmDFwSaWZQMe2mh-WxegqrFG1YdIAH1jOfDk9QXBoPl2tFzjjwGGWfk_cfhDUWMGV_T6G_aZ6D_jtCDt3w1f0Lvs8E6Lg_47kJ8PfGoW1HNLurIhYVtfHM0_ly-u-LKIHG83dZjsaBDL9pfnqczi4jHIZM38Ozrm9bO6qQWCRTklrgQGAdyQRMNPN0sidJW2I03ot-MD-NUFkoTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۸ شهریور ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
همگام با پیشروی دلار به کانال ۲۲۸ هزار تومان، بازارهای طلا و سکه نیز مسیر صعودی را در پیش گرفتند.
🔹
امروز هر گرم طلای ۱۸ عیار با رشد قیمت به ۲۳ میلیون و ۷۴۶ هزار تومان رسید و سکه بهار آزادی با نیز، به قیمت ۲۳۲ میلیون و ۱۶۰ هزار تومان معامله شد؛ روندی که نشان از بازگشت تقاضا به بازارهای دارایی دارد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/691150" target="_blank">📅 13:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf41d4a0d.mp4?token=WtlLb2bm18oxYQgfC7Ds_eaY3fVSoBloo6Y-UtGs6zP0E-uwjKiQdEm2kyU_pX_OqRILLN0JPLzKTxVRf5zp4Fl2n2D6EmUzRaUTOktjnQYBqs-qgcDglMHL9Mw9TyjCMnC698j3LXcacJzlPCFR0OrWLyIU8cWgW1-NfPPYvPwahrXl6NxBYGUWq9Jqu2Rxo6Fwu9UIlXAopiDwkxTg3kJtKGuCoQChxYX8bZ190h3ZlUIPJ3p4zxIWMs7k51mni-bgGFeYBZFU-mSDKf3PF4dGSGzT4_dPVBVse56wttPTaenM86Y0OGHKclWE17I02zpIX6kwLJFgAWhRMl5yJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf41d4a0d.mp4?token=WtlLb2bm18oxYQgfC7Ds_eaY3fVSoBloo6Y-UtGs6zP0E-uwjKiQdEm2kyU_pX_OqRILLN0JPLzKTxVRf5zp4Fl2n2D6EmUzRaUTOktjnQYBqs-qgcDglMHL9Mw9TyjCMnC698j3LXcacJzlPCFR0OrWLyIU8cWgW1-NfPPYvPwahrXl6NxBYGUWq9Jqu2Rxo6Fwu9UIlXAopiDwkxTg3kJtKGuCoQChxYX8bZ190h3ZlUIPJ3p4zxIWMs7k51mni-bgGFeYBZFU-mSDKf3PF4dGSGzT4_dPVBVse56wttPTaenM86Y0OGHKclWE17I02zpIX6kwLJFgAWhRMl5yJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فردی شبیه به امام خمینی در یکی از تجمعات شبانه قم؛ فیلمی که مورد توجه قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/691149" target="_blank">📅 13:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5119c00ae5.mp4?token=PXVyhKeHWPtD6MJYrHGuJRxa4xx8umNy7P172f5L-q952JGrrQggecAEeNcRpJ8fbUIQgbmrgO9WHEJbi4kGXAVG-N2QR_xwaac3t_KKPO10lhzZ6y69y1PPr90n6DBKdAnd6FCWa9mhI7Ebk1k6XjRSbOM89DggzIu3l2wMfpNk4zauVuw1WBM40PEUy0PNIW49qcxXLMaB3p3j8lrpsQaImDDrrIns3obtzsAal-UIS3PZ47DKQCgrmMYM-WDw0kN-_0C486vqIkGTzCnrSGMRuLsShf2ux0caTLdfM1M6BEYcD0QWJQJCEDzRnmUxA7ihGAhr_qakVHC0OK8_qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5119c00ae5.mp4?token=PXVyhKeHWPtD6MJYrHGuJRxa4xx8umNy7P172f5L-q952JGrrQggecAEeNcRpJ8fbUIQgbmrgO9WHEJbi4kGXAVG-N2QR_xwaac3t_KKPO10lhzZ6y69y1PPr90n6DBKdAnd6FCWa9mhI7Ebk1k6XjRSbOM89DggzIu3l2wMfpNk4zauVuw1WBM40PEUy0PNIW49qcxXLMaB3p3j8lrpsQaImDDrrIns3obtzsAal-UIS3PZ47DKQCgrmMYM-WDw0kN-_0C486vqIkGTzCnrSGMRuLsShf2ux0caTLdfM1M6BEYcD0QWJQJCEDzRnmUxA7ihGAhr_qakVHC0OK8_qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژه کاروان ایران در مراسم افتتاحیه بازی‌های آسیایی ناگویا ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/691148" target="_blank">📅 13:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f660c917.mp4?token=MOGGnwb3LV_FrR4D-1Auf1KyzDNyMZj2oyvN0MoPaSekZ7OSVMyCrq4X3-r6kA9m2k9JeQB9NGXfXXKLyLCceqYDmpcHWzS7pI5zFDYcT-fp3maqtXkjWfzhYKWD9kH26cm6mJWSRencFHE7U1W5Mkiqq-RjtSDuXZ0ocXztFCOCeK8XTQPB79KAolNWgfyOSg6HDTakNL1zo0wwFwRJFUT__eKv24yEPeelJTq4Q-eM9TLJ2ydmELOXVs6kgNgoGzfQaCuZaiVVnBOM0A9u5SSqoVR5GBg_q5fdUnp_I4UFf1o2x2eZyVMOk_zaGG0eJ1r2vmmMo2XetmAVclf8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f660c917.mp4?token=MOGGnwb3LV_FrR4D-1Auf1KyzDNyMZj2oyvN0MoPaSekZ7OSVMyCrq4X3-r6kA9m2k9JeQB9NGXfXXKLyLCceqYDmpcHWzS7pI5zFDYcT-fp3maqtXkjWfzhYKWD9kH26cm6mJWSRencFHE7U1W5Mkiqq-RjtSDuXZ0ocXztFCOCeK8XTQPB79KAolNWgfyOSg6HDTakNL1zo0wwFwRJFUT__eKv24yEPeelJTq4Q-eM9TLJ2ydmELOXVs6kgNgoGzfQaCuZaiVVnBOM0A9u5SSqoVR5GBg_q5fdUnp_I4UFf1o2x2eZyVMOk_zaGG0eJ1r2vmmMo2XetmAVclf8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرده‌برداری سفیر آمریکا در اسرائیل از جدیدترین طرح آشوب‌های خیابانی در ایران
مایک هاکبی، سفیر ایالات متحده در اسرائیل:
🔹
به نظر من، در یک مقطعی شاهد یک شورش دیگر در ایران خواهیم بود. شاید راهی وجود داشته باشد که مردم بتوانند بهتر آماده شوند، مسلح شوند و واقعاً در برابر دولتی که به احتمال زیاد بسیار ضعیف‌تر خواهد بود، مقاومت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/691147" target="_blank">📅 13:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: میانجیگری کشورهای مختلف از جمله پاکستان تعطیل نشده و همچنان در حال انجام است/ حرف ما هم روشن است دشمن باید به تفاهمی که امضاء کرده بازگردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/691146" target="_blank">📅 13:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691144">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879a9b5c0f.mp4?token=kbWn1886bcSzIf__5WaHISviUDb4rHqpUjGRoGYX1_pwxthL3qSKEza-F61dUaw0qNHQD5IFAKxEd7QUFTEfCONweLKUOnrzBnHB_2bdIw8TJrJUccsNrH7E5vpb56dNoys0W0dHJAZBsVvL2Yf0JZ6g6XD2Iw3rd_7d61bgLgoREAb_mO4MXder5wLaBqTpJzNQfoueCE-3nxFXrhn2WB-1eO8qtyFs_03__AEUdQN4_HEz4Benxqxw8JiZ-Yy3eEaOZ6IE3uJIi9bW6v2RbsQn2iTN71thP75K-THY-p2h11TlJYNCdcZ1awDftb8wCi7H76grTR0Fa2COPjGbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879a9b5c0f.mp4?token=kbWn1886bcSzIf__5WaHISviUDb4rHqpUjGRoGYX1_pwxthL3qSKEza-F61dUaw0qNHQD5IFAKxEd7QUFTEfCONweLKUOnrzBnHB_2bdIw8TJrJUccsNrH7E5vpb56dNoys0W0dHJAZBsVvL2Yf0JZ6g6XD2Iw3rd_7d61bgLgoREAb_mO4MXder5wLaBqTpJzNQfoueCE-3nxFXrhn2WB-1eO8qtyFs_03__AEUdQN4_HEz4Benxqxw8JiZ-Yy3eEaOZ6IE3uJIi9bW6v2RbsQn2iTN71thP75K-THY-p2h11TlJYNCdcZ1awDftb8wCi7H76grTR0Fa2COPjGbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین
روش‌ برای تشخیص مکمل‌های تقلبی و اصلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691144" target="_blank">📅 12:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691143">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رسانه فرانسوی: موساد تلفن همراه مشاور ریاست‌جمهوری فرانسه را هک کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/691143" target="_blank">📅 12:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691142">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GteM3y8sq6nlo5eqeHTiba5XIm4WpHnAHFqKmpXBFFS6jgCXyAcBnPWm2xwq981qBivZVpIiFcszzOQgGitMM11Bi8m8X5536JPsTwhA2U1OfJ18HwwTX9PE8wqOq8WqZroCuc02lvYrXeiFnJEews5wUs6UydlGN-_0D0ut-9Az91qePEB_XTczITQEnXo6_rJr1NgA49gXslLSWFu9cT9VdBB4JJzarod5n9V_ea18xThOr1oR6rjPG4KT72YT5pte2DIVAtwhJoIE1MxjE3QQj98-AVlhx3F0wi7C7-YipzqwbExm53w5Tbue-0G3nWpThRVhujxZDuvQ5ejSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه ABC News: هزینه هر باک بنزین شورلت در آمریکا پیش از وقوع جنگ ۸۲ دلار بود و در حال حاضر به ۱۲۵ دلار رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691142" target="_blank">📅 12:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691141">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
الاخبار: مصر درخواست عربستان برای اعزام نیرو به یمن را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691141" target="_blank">📅 12:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691140">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuiBjD-uZXLkTfQkBtFYCixDxIChWQ_bJr_pGD4qVUmmyz5EzN7tEbX8rtV35IaVBFw4SLJuaPhPveHxIevNLn4FBA3nOIQaKbq9uZZ0hVMUJ-4l1lKXvT7_Y2fEVoOpFfbzGese_RMHaQKaah72duk5oR-FqGq70X3E5ZUz4VBx5qNYiaqSt1Y6tTq4sTxB_Xe9yd8Egydus6SuvyuOaMUAg3vIWbyQw-i0ExouEEEkMjgOR9iUwtptS1DcM6jPzugYIKpydTLk3eMTH7JPsNryZwWnsDqEU40ASi9eX1g07I-McPMHWKC92XhHotsBAzkht_42E5g1rQ7AcaUz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری بلومبرگ درباره حمله فاجعه‌بار آمریکا علیه مدرسه میناب
🔹
بلومبرگ به نقل از مسئولان شرکت کننده در تحقیقات داخلی وزارت جنگ آمریکا (پنتاگون) فاش کرد، برخی از کارمندان پنتاگون طی نخستین ساعات حمله آمریکا به مدرسه میناب ایران متوجه شدند که این توسط واشنگتن صورت گرفته است.
🔹
تحقیقات صورت گرفته نشان می‌دهد حمله مذکور نتیجه تنها یک تصمیم فاجعه بار نبود بلکه برآمده از سلسله تصمیمات و اشتباهات و فرصت‌های از دست رفته بوده که می‌توانست مانع این حمله شود.
🔹
کمبود وقت در تثبیت اهداف مورد نظر و اطلاعات ناقص و تکیه بیش از حد بر هوش مصنوعی در وقوع این اشتباه نقش داشته است. این منطقه در داده‌های آمریکا به عنوان یک منطقه نظامی نشان داده می‌شد این در حالی است که تصاویر ماهواره‌ای نشان می‌داد در منطقه مذکور از سال‌ها قبل مدرسه ساخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/691140" target="_blank">📅 12:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffefffeb8.mp4?token=NnwJLTc7B6hgwBY_WYpm1putNfn3wvqgVN7nyUpRNUUtItlDF2SIg09lClMLZCtQ469uP2DKu_lIPeSCeox1T3H-B58cXtqTHKc3BOwAz0AZiZz78whHlsgSUcH2BvCSIwx9lL51jQsrE7hO8D5iF5W61cPQStJdPCtWfALRWvPsPo6UquLkt_hV5uNhEv6AeQQqAhJSBulpZpM0Tu0Nh_NOKOi3-reyB7MUjvBoBCF0tcXzApwhezaF9WZkWYeCxKqyc9-Y39ANu49fht-rVufaw6Vgyg8S1cDu6e1VTYGo1vamJ1SZ30Ii4T_VHR_dTaZGPJpPbPTSAjHNHLSGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffefffeb8.mp4?token=NnwJLTc7B6hgwBY_WYpm1putNfn3wvqgVN7nyUpRNUUtItlDF2SIg09lClMLZCtQ469uP2DKu_lIPeSCeox1T3H-B58cXtqTHKc3BOwAz0AZiZz78whHlsgSUcH2BvCSIwx9lL51jQsrE7hO8D5iF5W61cPQStJdPCtWfALRWvPsPo6UquLkt_hV5uNhEv6AeQQqAhJSBulpZpM0Tu0Nh_NOKOi3-reyB7MUjvBoBCF0tcXzApwhezaF9WZkWYeCxKqyc9-Y39ANu49fht-rVufaw6Vgyg8S1cDu6e1VTYGo1vamJ1SZ30Ii4T_VHR_dTaZGPJpPbPTSAjHNHLSGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ورزشگاه محل برگزاری مراسم افتتاحیه بازی‌های آسیایی و صندلی‌های خالی هنگام شروع مراسم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691138" target="_blank">📅 12:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
عضو ارشد انصارالله: کشتیرانی در باب‌المندب و دریای سرخ به صورت عادی و بدون هیچ مانعی در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/691137" target="_blank">📅 12:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691136">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124c79a75a.mp4?token=Vp0drqYlDPfMB2f74kTDRrbScK70pOh36nm6D1rPkPnegmQ64SKkAYD7oVNzMvcuupr3TCaa-pXF5s9iTv5ojfiMQJV_OHF8RW-QGi3WVmu6pFCZr5xqCJmdE9VRO91HgUD4tDrkBLDMbu6aUZNl573zPvQM8f6YC8ED2c8FGNu-ueqFI7PCLizDgLyJUwF8PcsvQx03OB6GhcpKo0Hkr7ORAQp9OCyPuJkD3No0qCCm1a3ftqetQXZtirirZBdo1za2UhsjVAagLACIZ4vZTeJXcMwTTgwIjn-hUAWet8vNuQVhofJxuClL7ZjrJ10PpaQhgWn9egIqkuEcGkCY1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124c79a75a.mp4?token=Vp0drqYlDPfMB2f74kTDRrbScK70pOh36nm6D1rPkPnegmQ64SKkAYD7oVNzMvcuupr3TCaa-pXF5s9iTv5ojfiMQJV_OHF8RW-QGi3WVmu6pFCZr5xqCJmdE9VRO91HgUD4tDrkBLDMbu6aUZNl573zPvQM8f6YC8ED2c8FGNu-ueqFI7PCLizDgLyJUwF8PcsvQx03OB6GhcpKo0Hkr7ORAQp9OCyPuJkD3No0qCCm1a3ftqetQXZtirirZBdo1za2UhsjVAagLACIZ4vZTeJXcMwTTgwIjn-hUAWet8vNuQVhofJxuClL7ZjrJ10PpaQhgWn9egIqkuEcGkCY1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اضطراب چه زمانی می‌تونه مشکل‌ساز بشه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/691136" target="_blank">📅 12:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691135">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04455021b6.mp4?token=AhZ3raaUAOwlVgZ49DkH-GipiNWrWMG6bQgmsHQ4pFnVc1EIrrX33nJ1o1sOvSF-kJBL8-QeGb2VWsCLlOEgev934qyoEnCrzyM3I2UMjofYK-wBtA-ahCoPnHdPU6WgPY1AUnao5Pplx0AliCSXp-q2W74OxZNw4MAl8Uw8Sy57csBbeXG4I0I9784mzvfC-78dn22VJCPA_-K_JidQdaECzS5vYvVwaefcDDkcqyTNafPhgxZzomXl2Xcrx5oBq6ydlRabCBHiRNganesg4AIDsvzmvdOtEFIBpRM3wD8KxFtDf4JnLeA2GJk9FMM5XLGo8UGPiy7iRadSUtyJug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04455021b6.mp4?token=AhZ3raaUAOwlVgZ49DkH-GipiNWrWMG6bQgmsHQ4pFnVc1EIrrX33nJ1o1sOvSF-kJBL8-QeGb2VWsCLlOEgev934qyoEnCrzyM3I2UMjofYK-wBtA-ahCoPnHdPU6WgPY1AUnao5Pplx0AliCSXp-q2W74OxZNw4MAl8Uw8Sy57csBbeXG4I0I9784mzvfC-78dn22VJCPA_-K_JidQdaECzS5vYvVwaefcDDkcqyTNafPhgxZzomXl2Xcrx5oBq6ydlRabCBHiRNganesg4AIDsvzmvdOtEFIBpRM3wD8KxFtDf4JnLeA2GJk9FMM5XLGo8UGPiy7iRadSUtyJug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر کره جنوبی «سلطان قلب‌ها» را خواند!
🔹
سفیر کره جنوبی به مناسبت شصت‌وچهارمین سالگرد برقراری روابط دیپلماتیک میان ایران و کره جنوبی، به همراه تیم ارکستر، ترانه‌ای فارسی خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691135" target="_blank">📅 12:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
نفت ۱۳۰ دلار شد
🔹
در حالی که قیمت‌های مرجع نفت در محدوده ۱۰۰ الی ۱۰۸ دلار معامله می‌شود، صادرکنندگان فرآورده‌های نفتی از رسیدن قیمت فیزیکی طلای سیاه به بیش از ۱۳۰ دلار خبر می‌دهند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691134" target="_blank">📅 12:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691129">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyB_eiACycE7--o6Ukx8jWCViSBEc1MsYtDJsM9BOCkrPAf-ruIi6c94iImZUUuFyuZMbWhvliMM37iVm9fcKCaALKk1PLw7caZevVsivHjNCrGmO8uIbfjcBYaiLBZ-VgSFt2vnRvLV5PDEFbHFSVa3yaZQ4kpy4V82kqyklEiPD2zGErPEl_L5KEztnhrC2cDnsVR735PzP15Kux_vBq8yJHmZ9y8f8Z52eBZ47sJgUI_Kt5l8tJY9wOWy13gY1TUeOLL6l8Gn7ShmJg-sAqgBTXMCPZiFMWap-zMm9Z3k9aws-CQ_ZViQYK0_HPhyS4Mtj3d-HO0-1mZWiiHqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEdmX3YoeYnzGz40iCIC3KxuJRRwcyCagunPA66zFqWTIJP_Z1AqwnNljV-hywArwI6FSf2PIGss2HkRGWQpOee_yXCxYXu6tJ-Hnzzw8OL249rtfN_KUZWMROOjUdPfM9uq4PHoEAReBn7RcD-zcdbGqeCh-cwGmkAqUiRiASh7HPYo-DvDP5XMcYAOksL5bfa8O5NhYNP8Akn56SYHgTAFiY622SV-XjnJIgLi_MleUcIk2G0dH4uxSOZhYbcXvVzHldYaGc9Y5P1VKUqgUBp8dyDlpBWSyU_mA1fE8u4ZS5yUzB5j40c9BmlBIQPtbuFUWZ1Bx3ZEApQ33mLSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzHFZhb7z_7mNQ5yAJJwJy2Jgq6LlQStY7GoAjrJCMZdu7RWGYpDZ_CybgtTGm53rNnA7blQmhTno0gLfCSTSR8l4Dces4dHraqIFi7RNEJJKWSPdBE3ojDGebmydCDlDWgUUFXcBIljH4LvedDt5mBDfl-ZZP-CNbsEmAadPHprWarnp4kJsL9Qkz-xX6ATTjIKq2i9Y3ffsr7P0es1YM7h1PV4d29N48zcvHk-ZDFpuNp68hVx7BD4j28U8ZudiX6r7QNkx0pzbRRnuxKZ8c3N4TNSBPuQlnP8im2moQmeZD3ETDnkzZ_XYNi37-waeAHLtGFtrUS6LvnTJWKZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtVTCykOfYg_Pkxx9TneJ8tHEH9Clg1MGpBzRF8ZQU4nei-cwI3eSgub8jmkjOh2h-J6etsBlRWn8FQjxxRew_vbctADfOayuMxNRyyN-uDp_9IZLnvEIWfni9Q5kCs6SMj8knVVdlDsREv_Zpk_Y7E_N6tlWgWEbn19y01JXcbSBicViZjBmrQRIu_mrv0DxO38K_2DcrFd3hmqJsQIk_PQbDUoeDe2TNlX8owum_KA7w_xfrlwWQH0IVcyQLvaSRaVlxYiKtG5XILO2Ma9gAEJZj4tWEg4XgudlcvJfL1wnx1XMNXz7O04SRMJCKlAUHXvp81hAy2LbQLh6ddpew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsHfR9WYZzaVKwKgAY6Lir-PSIb9hwWgJl0jkAlkKUcAnq7-K0n1yCF9khfiuer4RcLuG4wnIJQiE-RyUdTmb-tJw5_r8W3MAl5-X3kgagm4pQDAucC-uhtQE51Pen5yTs6qra-Z0r09E4tfimDaA_NsyHlN4WDszJZ00n7PFl3S0QhmsGxwq-UmASjc4yWNcBNT3wku4ZVb49A-WxmreTYvVaIWciwbb_w7wmYirWkMVz9gIIAQ4hi0MFE_MjQHxFcfKndJowMaXwvWB1x7uGb898s4a24-YRMNmWeWcppxWYgflAG82FWCjz8p4gLkMRC5g0M_aFCSZp8R7Bngzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فراری ۸۱۲ منصوری، خودرو تبلیغاتی جدید پلیس دبی
🔹
پلیس دبی یک فراری ۸۱۲ منصوری ۸۰۰ اسب‌بخار به ناوگان گشت توریستی خود اضافه کرد.
🔹
هدف: جلب توجه گردشگران، نه تعقیب مجرمان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/691129" target="_blank">📅 12:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691128">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228e62cfa8.mp4?token=edSsK972uNgRvV4GWDf-nr-cLfImN-0i56XBKkecfsbJ_BzpkVFx6w7DLCaukbKeBNC2k26tudX2NxuicHob5pwT2Pkw1FDCd46cPlVnpI3xzeYGxYvjgPXAIOcsl6o9_C7SM0oxqTLEZKMR2k3owoyQ9fxs-GqN9alKdafGLb2ZecZCNvty574mStzpCfDUXDhJdd-jm5fjxzvH8FTO2xTumW3pUOqyyP1XAHWWZ47NsDJHaXy3jlQwuO3IawHFJpHwkCTWCJyhFmopXFf9aFhhIOpfYW_vv5Ggr3Q_cxlyfovsXHwg9Jf8yZeYThEs97GRiY2kZCmVyFtbqVsc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228e62cfa8.mp4?token=edSsK972uNgRvV4GWDf-nr-cLfImN-0i56XBKkecfsbJ_BzpkVFx6w7DLCaukbKeBNC2k26tudX2NxuicHob5pwT2Pkw1FDCd46cPlVnpI3xzeYGxYvjgPXAIOcsl6o9_C7SM0oxqTLEZKMR2k3owoyQ9fxs-GqN9alKdafGLb2ZecZCNvty574mStzpCfDUXDhJdd-jm5fjxzvH8FTO2xTumW3pUOqyyP1XAHWWZ47NsDJHaXy3jlQwuO3IawHFJpHwkCTWCJyhFmopXFf9aFhhIOpfYW_vv5Ggr3Q_cxlyfovsXHwg9Jf8yZeYThEs97GRiY2kZCmVyFtbqVsc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: هرکس پلیس بکُشد باید اعدام شود
🔹
اگر انتخابات را ببازیم استیضاح می‌شوم
🔹
مدت کوتاهی پس از آغاز به کارم، یک فرمان اجرایی تاریخی امضا کردم که بر اساس آن، هر کسی که به جرم کشتن یک افسر پلیس محکوم شود باید با مجازات اعدام روبه‌رو شود؛ و سال گذشته، کشته‌های پلیس حین خدمت به پایین‌ترین سطح در ۸٠ سال گذشته رسید.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/691128" target="_blank">📅 12:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691127">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
آغاز واریز حقوق شهریور بازنشستگان لشکری بدون معوقه  فعال صنفی بازنشستگان لشکری:
🔹
معوقه ۴ ماهه فوق العاده بازنشستگان از طرف سازمان برنامه و بودجه تامین اعتبار نشد و ظاهراً پرداخت آن به ماه‌های بعد موکول شد/ ایلنا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691127" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691126">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74e8d5c73.mp4?token=Egepmgs0giXdGVeougSRMykdY7awzRfQ-Hx6wyEnRQzRCiMyUldKLzKoZVO4v9QJqQnDlcoqKUjWQWXKZgPukwbvmo-l1p6boZJc91WqK4cim7FIe7vi9JCdxYJAVQ5yM7vOocwct8GKFzeDbfG8-5OMgPDqDNV6-Ixu3lW7RkjRWoWIAAywXFfSJS9Q49JYYlyQ4etCorfs6460TkjWqkZmB62AA4ryFfB--fBZZgGVQQlGuYmMG_F2EG92yMI79nSR84Kuq0e7iAfSQP8s3mffmtBNYY2LubHiRONJtn7p6yhqEnFSMlBiavvv_NjRsSmkV2wcedfMVrFbsCjwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74e8d5c73.mp4?token=Egepmgs0giXdGVeougSRMykdY7awzRfQ-Hx6wyEnRQzRCiMyUldKLzKoZVO4v9QJqQnDlcoqKUjWQWXKZgPukwbvmo-l1p6boZJc91WqK4cim7FIe7vi9JCdxYJAVQ5yM7vOocwct8GKFzeDbfG8-5OMgPDqDNV6-Ixu3lW7RkjRWoWIAAywXFfSJS9Q49JYYlyQ4etCorfs6460TkjWqkZmB62AA4ryFfB--fBZZgGVQQlGuYmMG_F2EG92yMI79nSR84Kuq0e7iAfSQP8s3mffmtBNYY2LubHiRONJtn7p6yhqEnFSMlBiavvv_NjRsSmkV2wcedfMVrFbsCjwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
تخفیف  50% ویژه هتل مشهد
گروه هتل‌های درویشی مشهد
🎁
هر ۴ شب اقامت = ۱ شب رایگان
🏊‍♂️
بزرگ‌ترین مجموعه آبی هتلی ایران
🏎️
🛥️
تور های سافاری/ یات‌سواری - رایگان
🕌
✈️
🚆
ترانسفر تمام‌وقت حرم، فرودگاه
🎮
🎱
گیم‌کلاب رایگان
📍
۴ دقیقه تا حرم
⏳
ظرفیت محدود
📞
05138080
🌐
darvishihotel.com</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691126" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691125">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK1vChY8e4ZKqr7MiBMEBK5toMagPN8R1cUWbPSBQGgyJzZ_DmtkRiKW52VuUCZE6BWPWfIrx80L9YA1GktqrLP5pY0gk1eAzuyvxUyibgAvrjeOdERPC4G59ciN_Gyv5xMRi1Q-fqaBthcIa7wezMbbX2QfTe7H65G1nT8j_XiRuLgMMbKsYAllZKq1jWEKcATsl8uQo8iMjpmJRj6lJ5mYbgSsjtL9VxA9GjfGssetAePi1zbdhGV7K8knWN1IpvlmXfUGskdX5I1VuN0eKYwb-vQExHm8RarYzcm9-9vmRdU1W5dn5Oq1shk-59D5HCqvoku5_hRXpjmv3TI0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفروش‌ترین کفش جردن در حراج آخر فصل
💯
رفقایی که توی کمپین حراج آخر فصل خریدن، 1.4 میلیون تومن سود کردن
❗️
قیمت قبل: 3,299,000 تومن
❌
قیمت تخفیفی: 1,868,000 تومن
❌
پرداخت درب منزل شما
✅
وجودی محدوده، قبل از تموم شدن سایزت سفارشتو ثبت کن.
مشاهده و ثبت سفارش:
مشکی
🖤
👇
https://memarket24.ir/product/fast/46467/180124/
سفید
🤍
👇
https://memarket24.ir/product/fast/46468/180124/</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/691125" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691124">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c22e0a68d.mp4?token=tJqmpxiYPtKYiDCLCZy9yj9eYfjSfoKSjxi6jvSEaVS54HYoo6NhQ_4V3Pv57BO3R4GUPrvtJeiq7vdJr0sIbOS6Eh6hBpkXw_9MQLaEKRYFAQ4fkuK9iqpylSKtQLI7P0RzgfNDSruLvnhdsohO0zV8W5DpIbgjBUM-SDYp1-TA5ku4d34SLTxyX7jeyM7GO1VvVnxrVn1UNjGV-bsKWuqsHQaZFDNGPzUIRhrBj_pXxTK4mxO8kD2T0jzmTGuMuxKl-81VQa0MspJ-Pr_nOh8Kw6QdgGph-8IMjJ9WqCbXtcqrty5ngcBMZ7L8o0Vk17gVpfTmHf_gf_OQwQTQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c22e0a68d.mp4?token=tJqmpxiYPtKYiDCLCZy9yj9eYfjSfoKSjxi6jvSEaVS54HYoo6NhQ_4V3Pv57BO3R4GUPrvtJeiq7vdJr0sIbOS6Eh6hBpkXw_9MQLaEKRYFAQ4fkuK9iqpylSKtQLI7P0RzgfNDSruLvnhdsohO0zV8W5DpIbgjBUM-SDYp1-TA5ku4d34SLTxyX7jeyM7GO1VvVnxrVn1UNjGV-bsKWuqsHQaZFDNGPzUIRhrBj_pXxTK4mxO8kD2T0jzmTGuMuxKl-81VQa0MspJ-Pr_nOh8Kw6QdgGph-8IMjJ9WqCbXtcqrty5ngcBMZ7L8o0Vk17gVpfTmHf_gf_OQwQTQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورزشگاه نئوم عربستان؛ میزبان جام جهانی ۲۰۳۴ در ارتفاع ۳۵۰ متری
🔹
این ورزشگاه در ارتفاع ۳۵۰ متری از سطح زمین معلق خواهد بود و انتظار می‌رود حدود سال ۲۰۳۲ افتتاح شود.
🔹
همچنین، قرار است میزبان بازی‌های جام جهانی فوتبال ۲۰۳۴ باشد. @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691124" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691123">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آغاز واریز حقوق شهریور بازنشستگان لشکری بدون معوقه
فعال صنفی بازنشستگان لشکری:
🔹
معوقه ۴ ماهه فوق العاده بازنشستگان از طرف سازمان برنامه و بودجه تامین اعتبار نشد و ظاهراً پرداخت آن به ماه‌های بعد موکول شد/ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691123" target="_blank">📅 11:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691122">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4c4d3ed2.mp4?token=Rw6yjUjef7fJewyvrnz1Ww5_GUSeWLdwWoAS0_cKNo2Kh3n-4bAZcaBeO7Z90kY9XsqJho-EL72mhlPBqKzKZM8OByEQKGxk58otCx-S2PP6Ma4wxONJ09sFI-DhwE_oXSbcFzouOmMXMyW2HZbpVerpWZuMQpEHJEGEixqfE_lzIZFC2XUFwxXFMgd8IAczvrj-TOgrSCP0O0JHGD0zicEDnrToGD4VzEzjAD-ayacCL7BUs9uqLdce8tpVw82ab9sisQ1_MGEeVrVLU_fTMKGlSnLxo_kNZylqz6enKJMHbRNiNpmo-Qs5bMrfLXLpnCGyj46Nvn-JBdtTabz9miXaJk2OxRdeCgZYiyaJSDkno16IFjQUDxpR4TyDZPd4finJ2RVxpC5hq8hQVTEHmtLNQFl5qcQCGVTSyJ-vZveH9Ql2bujwbkcsLr7DPzvo2BGVQHw3YjrKH1j5p-zRWAKX67y51MzvCDOCYfwwkksZX6lEI0ieSlSadn-yAYHT824BGerkF6DUAByZFiOoMaCyB-Y3zGbWeL2uCPI4iAeuMkWx3-JIGsFwcULHeQhLdjiF41e6PSbZTOUIOvXnt0Zb6Lt2FRpwGzqZmNxaO5Y4jdW4BX5sSNhU4o5ORwHhxLadibKfDpZ4PH2Eqq3qWDNnmY2y-O2Y4hhHQUIen2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4c4d3ed2.mp4?token=Rw6yjUjef7fJewyvrnz1Ww5_GUSeWLdwWoAS0_cKNo2Kh3n-4bAZcaBeO7Z90kY9XsqJho-EL72mhlPBqKzKZM8OByEQKGxk58otCx-S2PP6Ma4wxONJ09sFI-DhwE_oXSbcFzouOmMXMyW2HZbpVerpWZuMQpEHJEGEixqfE_lzIZFC2XUFwxXFMgd8IAczvrj-TOgrSCP0O0JHGD0zicEDnrToGD4VzEzjAD-ayacCL7BUs9uqLdce8tpVw82ab9sisQ1_MGEeVrVLU_fTMKGlSnLxo_kNZylqz6enKJMHbRNiNpmo-Qs5bMrfLXLpnCGyj46Nvn-JBdtTabz9miXaJk2OxRdeCgZYiyaJSDkno16IFjQUDxpR4TyDZPd4finJ2RVxpC5hq8hQVTEHmtLNQFl5qcQCGVTSyJ-vZveH9Ql2bujwbkcsLr7DPzvo2BGVQHw3YjrKH1j5p-zRWAKX67y51MzvCDOCYfwwkksZX6lEI0ieSlSadn-yAYHT824BGerkF6DUAByZFiOoMaCyB-Y3zGbWeL2uCPI4iAeuMkWx3-JIGsFwcULHeQhLdjiF41e6PSbZTOUIOvXnt0Zb6Lt2FRpwGzqZmNxaO5Y4jdW4BX5sSNhU4o5ORwHhxLadibKfDpZ4PH2Eqq3qWDNnmY2y-O2Y4hhHQUIen2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف یک سارق منزل درباره نحوه یافتن طلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/691122" target="_blank">📅 11:44 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
