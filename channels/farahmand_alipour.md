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
<img src="https://cdn4.telesco.pe/file/l3XCj1zHx-5TpoF9_7laM280Vc6kMFgBWVeioevFRmucSq9GhVQYLlM07zdyy_mTyNm__sD7Z3FnAYfAoiqKC7_tl_zTtC66OhnEjqrCBrdjznwnM8P18cdbShcQD_Oh8jMyluDA5VZ9ni42Q_L6iiX98glykT7grMi_122j0gf1091yZ7dLugp9AIij2H4QUk3lPZ7vjsjd-ZFgXM5eOFkm5kX73KNMKZa_cy2IwQ_LUqBBRgDhVCSkluraZVxgx6TDAh-n10dXWJY43XrlpyTovppLHKZ5y72aHKVMAE9yEHKPqN352nMG8b2Oznj6bHAWBIt0cnFWk2-Beb0D6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 19:56:33</div>
<hr>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOFfPu9UP_Rr5RkzqDCAgWftVhz5kbhOCzhtEQjT8Bq_pc2sbfY9FGuQu9faWbfc9oCu4C45qhoocy5uISJGosdQtMzII3tI9il-srGQ8ZOtQT5NeAkN7ACXuhMMf865cYEXECNr4GXfZNOU3ZY2gwSfifESoBNz68-qbAtJPq-5C8ToxDW7T4Ij2YxEgyMc9QmTOXK49QT4GDmCyVxR-SMnMifCECnP1zFtKTdwIo2Ojqbd5UC2QnMkd3Y730zbc1UZhDGH-oYcBsFMHUOAWfWSz9aSA0swKKs-nAuqknBWtaI8LP1Khg_xzXBv6xplyGuttt_Qx_emdeL1mqHaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=F9d7aGP3aNdl6aDp1bhYUTP8C7RShiHwzvdCxJsN42STQnfgQ7CA-clCl6_FLT_FsQzDEEJmK9085VMRzMl7NXTZXo9x2VwU0RWSe8XSuHf8QgLPla8OSGQCOsOOsMu1h3MYLkRoDEULjtpjKCdpOKYLE2qVdmNf-pPVw1Afx8CN6z49oXKgnJe0XEIHjh57D3MYucOf9fVCkSdnQTAK7q7jkjlvTHEDMlUxwbKMe5mQz226Zb0Y8olVFngtGGxPyvLBLoCz2kxLBBjg_53YV8vhvZ-9g0BSuBCBK-YtG8CaJWufMsE9XNc-YdgV6NKsQxPBq-tGbLg1nNiG-UnDXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=F9d7aGP3aNdl6aDp1bhYUTP8C7RShiHwzvdCxJsN42STQnfgQ7CA-clCl6_FLT_FsQzDEEJmK9085VMRzMl7NXTZXo9x2VwU0RWSe8XSuHf8QgLPla8OSGQCOsOOsMu1h3MYLkRoDEULjtpjKCdpOKYLE2qVdmNf-pPVw1Afx8CN6z49oXKgnJe0XEIHjh57D3MYucOf9fVCkSdnQTAK7q7jkjlvTHEDMlUxwbKMe5mQz226Zb0Y8olVFngtGGxPyvLBLoCz2kxLBBjg_53YV8vhvZ-9g0BSuBCBK-YtG8CaJWufMsE9XNc-YdgV6NKsQxPBq-tGbLg1nNiG-UnDXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cY-kW-aEjtnJCHLGEGC_Uhshm-KrI9-iqPl-1qJ-zG2Q8xno2-T4s6Rg0gBHB6pwcZDXCYIO3q650D66Z1VMzAOZDO7bjT1reSwtLe5G7d3NGPNwM2cLdySoYOkx_s_mZbB0jst9cbIJ0v8PKJDkfC8JtRnosGYHafI8Wr0tIYfxvwbDAli3aZD5hz2TZOcHBw4BmGmSg5qzZd4balUOzcdpDcDL8qCylzvi0Jvp58amATRUtDzJBAGCvDpSVvi7npL1ANtXZ9441_C_W4iLUSVJUx-017yM0ltSwT5dAK09SuJkmDxw2WDg3U36FTH-bKvwwtaGp_Sm5cIyw19tSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cY-kW-aEjtnJCHLGEGC_Uhshm-KrI9-iqPl-1qJ-zG2Q8xno2-T4s6Rg0gBHB6pwcZDXCYIO3q650D66Z1VMzAOZDO7bjT1reSwtLe5G7d3NGPNwM2cLdySoYOkx_s_mZbB0jst9cbIJ0v8PKJDkfC8JtRnosGYHafI8Wr0tIYfxvwbDAli3aZD5hz2TZOcHBw4BmGmSg5qzZd4balUOzcdpDcDL8qCylzvi0Jvp58amATRUtDzJBAGCvDpSVvi7npL1ANtXZ9441_C_W4iLUSVJUx-017yM0ltSwT5dAK09SuJkmDxw2WDg3U36FTH-bKvwwtaGp_Sm5cIyw19tSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLNahGyWF7UcqcnDLCu9HNZYRFPxkLpGNItCZ1wry48AvlHqDYmOTyUydgP6068YgC-m5YGJtchqhJvF4SkuR5EQJxgHo-pauQ3b7WDOiN9rqUgrVDrxmtHwomLnfpVMFrG0M4BmGbmls1IAQfp4cRPvftqlbFi50MZ21xJwLycvQZaD0MWEoSTY_re88Jul4hLRFnsiKO9pHshlphcU0LRmt8RoFIdj43MIi6Tk-aWpx-u1b_WrAhkJPyp2mLBFIO2DGRh0053WEzqyRJWSioHu4CRhWjKM4ASkjEf_9Y5I883BeAzuOBGk6Xtly-3RuYvC3lAYeu-uxqrJWcrJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=QmegI3wJRHE6Z68AKejtYXjTqDwhC2CP9umqFi0zdFI28dDpMNZQgG6QXqfIOkFE5UiV4bj2L6VZqKtbGFa5DSkBbGxULTeN7hq5Wiu2ZfMShT0kB0Msr6p_3ZRbdV1_CG3Zlz1Ty-_PshJ4K8BbdXCYU1GlWG1iL481MaQ7qQ7O4ceomIEKMWafb1YB-6aiEyRcgZ55kkWTDI_YMPZO_uqXXT5-IfSwvA3xkxBKkTnk_zQfCZ0R_VUh-eRliSWTwGcOCzk7oxV6DQO7vmzL8CT-DYj5I8dnVNsQGF9ODxYqVc-RZc9Ybv4DNO_dHwoG_JfWCqO-TkZN7Jz1uruGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=QmegI3wJRHE6Z68AKejtYXjTqDwhC2CP9umqFi0zdFI28dDpMNZQgG6QXqfIOkFE5UiV4bj2L6VZqKtbGFa5DSkBbGxULTeN7hq5Wiu2ZfMShT0kB0Msr6p_3ZRbdV1_CG3Zlz1Ty-_PshJ4K8BbdXCYU1GlWG1iL481MaQ7qQ7O4ceomIEKMWafb1YB-6aiEyRcgZ55kkWTDI_YMPZO_uqXXT5-IfSwvA3xkxBKkTnk_zQfCZ0R_VUh-eRliSWTwGcOCzk7oxV6DQO7vmzL8CT-DYj5I8dnVNsQGF9ODxYqVc-RZc9Ybv4DNO_dHwoG_JfWCqO-TkZN7Jz1uruGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r7X-3-vboGHzU6442C7jbjplfboxRFRc_Qqdh1stWFaqGtuDoDT7yD5anUiq7US2o1CKcnQteTTyzYziZKuTSdWI3oGrORjJ13-RGGophaXcwj-p39FTSrus0n3Q7KbbJ49yC5fEIRAk_GQ5s8JfAuKush2TcPFGqNqerbKhjiXZgrCr5tEdJnpvH0dwMdSLkonyqx3AB8yQToQsFWXKb0f69CvMOO18V3ko-dN0g9w2t93I3RNTJJ6807pnVVLLx7faB08AYReVByhpyzuGcl1hBNrn_snYuTuddwYpaV4lTnXmoWn7bg1-LzfiZqPYwTIIzgTyvxsWF_o69S_lUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r7X-3-vboGHzU6442C7jbjplfboxRFRc_Qqdh1stWFaqGtuDoDT7yD5anUiq7US2o1CKcnQteTTyzYziZKuTSdWI3oGrORjJ13-RGGophaXcwj-p39FTSrus0n3Q7KbbJ49yC5fEIRAk_GQ5s8JfAuKush2TcPFGqNqerbKhjiXZgrCr5tEdJnpvH0dwMdSLkonyqx3AB8yQToQsFWXKb0f69CvMOO18V3ko-dN0g9w2t93I3RNTJJ6807pnVVLLx7faB08AYReVByhpyzuGcl1hBNrn_snYuTuddwYpaV4lTnXmoWn7bg1-LzfiZqPYwTIIzgTyvxsWF_o69S_lUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=oQDKhv1syiJG589vcwNswN1MM_JA009gCGsFI84BoglGSBmd5OEL6JUNvKEPaN2_2BcizXtdvhdlaj2SAIy836OC-1AjZJ3HqXZ30sBbRdAeKYOANWwoTIupu_g9H97lKuBeW8wgu8B3Y3NC6xNspio1c4DLjg_URRP2fLJJbMuOPgr_URYEkdg_vAngy1hPknn_2l99j8nZI0tr3MiltzdMwQPXaJ8_5ZqtXULdioQMLjwpIdWerABMMRnApHnalJer9mFaaYre9l6wS9D_PMRWUtvSrp5v3HsZnDeJpsnV2U3OQda-kiurAKS8guXJIMTlNTvLZ6-oBN32P7OWVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=oQDKhv1syiJG589vcwNswN1MM_JA009gCGsFI84BoglGSBmd5OEL6JUNvKEPaN2_2BcizXtdvhdlaj2SAIy836OC-1AjZJ3HqXZ30sBbRdAeKYOANWwoTIupu_g9H97lKuBeW8wgu8B3Y3NC6xNspio1c4DLjg_URRP2fLJJbMuOPgr_URYEkdg_vAngy1hPknn_2l99j8nZI0tr3MiltzdMwQPXaJ8_5ZqtXULdioQMLjwpIdWerABMMRnApHnalJer9mFaaYre9l6wS9D_PMRWUtvSrp5v3HsZnDeJpsnV2U3OQda-kiurAKS8guXJIMTlNTvLZ6-oBN32P7OWVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=lK6y3k7hlCU0wfaWTyVpV1jiHKCpel-FG7JDNzFW-dIimq4o3-BV4eYJnXpWTRSLgKQyf1kOypQuPGwf2m3lN-wJCi7cBR-wrH_KBin7d4CXthn_iLQxF5rt8goAPtLPSDZpgrom8r1u9OPXBvcnK6Tmr6qYR16afW0f2TREIRSOPJCDsTaQ3MUXo8W--HyOtV0GTD0EEDANlDZqgaqBZpshTrVn-v4iiliZ93z7eHE5j95k_-6jQkYqxdYp6MHd6Je0Ec40BrkxduFfz_OK66Y3BU7kcSOjIVCHhLiA_xofErl6r0yGHqpmbxrxSj12MciWQPOyQstrt7hso5OzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=lK6y3k7hlCU0wfaWTyVpV1jiHKCpel-FG7JDNzFW-dIimq4o3-BV4eYJnXpWTRSLgKQyf1kOypQuPGwf2m3lN-wJCi7cBR-wrH_KBin7d4CXthn_iLQxF5rt8goAPtLPSDZpgrom8r1u9OPXBvcnK6Tmr6qYR16afW0f2TREIRSOPJCDsTaQ3MUXo8W--HyOtV0GTD0EEDANlDZqgaqBZpshTrVn-v4iiliZ93z7eHE5j95k_-6jQkYqxdYp6MHd6Je0Ec40BrkxduFfz_OK66Y3BU7kcSOjIVCHhLiA_xofErl6r0yGHqpmbxrxSj12MciWQPOyQstrt7hso5OzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxcbJIctp1pqBy-vIPYMTXfkOLYCdVVDm8-Uvvwr3MTwml3DFKTfdgV9GGgBOPB_D4q3cVWSL55CN49zFU1oQ9MxtTcRHkDi2xHyuv18yIIE69cJeHy4xu0t5iPQb-BsTFskwTPK0SYkHHPEGC_tTASLAC2vZRt6yO0MLPYflJKVjiqovmNG53LDhCvxQZCxqS-F8tAUL-XojFOAk12q7V7FX1QhreXYI2tt1hc6ZdizKxO1JWCML9tNcek48j9MeaUBk5g9xuK-FNTbso5aNppDeOa9kMvYYzQapRYKqDGwmNTC8x_McUB8lrZDgQ6ld_jkMwgiFqws14KX0NXBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvtSvsV1bcM7QDFgdQMfXNB90H8Uw2AIoDqxs-2vOLWIh2-Mn54CpzsfOpp9bMHORlPY9EwN0TcByvoZC7M7yIp07kS37by5HpraL7YV5ifPUeTkVGSJEbZAmSIjbMeXWnBCkI0GHp2Y2OCZNfUOGZAd77Dtbd3P-dJzAUI9C-zMbwgaAJDs63HtrrKnAxfzvTAJIki4pH4kZ75CRx5pULvXrJuMJyR1aZLcBCwqKPB4xvI-bWZw8RSo2q2YuSvieJF6PS5ilZuTUOOmFlh_RJ4ZUoo34EjNkiRDBg8hMBJzBXtSMdyujdLP3m7vu8x2s-gkWE5u4I1dfHfXUqYEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecwIk7MdzeiOmAtI3huYKz8IBgEYx1uQrgOMebq433RwZpR89mvbqNk4SDCjP4dIJkFKg6YbT6QsdwxIKLnWYwdRrqWkfqCxw_wHrK1YGMraPfZtbNGnBMlgXqR2q3mMAsAUjgsJhpzoiqiSNAa05EbO5bl8ursccFNj0K6i_JOenLAL4ZBs9FXiIOvtSDJR2hUIWe7fTrYIJ9gtZVzc0LQX7yIPoU8jgWA13FljTCXe-GsakB4X1br6ccXijxUWd7yOaFlnB_k3ZAFT0_fRq0pmjtR-w5NeMkF10l2XU3HiznS3-5z9FnqaUeqtM5EEcauQmF4ZbJUEaFTo8aXarA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBrGm3N2XO7Vu0qxqnqhWzs26GL-wBz0sXgSCSg0TkL3PZaKh2VZ3iZRTGbtiNSd3CbSs_xJkF1Piq9VDQlmenJtxrKuxTVR82WlrS2FN_-Px9JAZ5XEebErwDvI-CbnXuENC7Vyo16jGsaNkciRnkEm2iM9YMwVOReY1T63ejfv3LSps6FcHT922ijr1cvS_csm_lwubSD_dagWiMArDZv52fZilKNIw69TPGU8InnY5wzF4UiavAnwtDSfmijllKFUQu5WM3iGniBDqbwx6MxsQCsaeGf8R1y-YlXh4V98ord3QT2-Pl_t_kb6SBHYsoKXyqAEMQgdEEcRSKM7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4enV613tviTkG1rNbjW-QfEtzvRpR0pgJoXqX_IVFEyP8R5T_D6tz8h0kvsMCb2JNvCXf2gm6ocdUDG5dnRnpQ4_kwByLFaSu-wTHIVkOR5Ge5Q2wC9ouSqiIKVjXJBMQOH2ThE8-SGY5pQdcHGYgyhNTZnCBdyCLGs3bhv3TEQD446ANYlg6wM5lXawBb3NKwn3gAyldxcuknQ4DhLEKjWdQb2IMdFM1xXV8pdhs_mMb-_EzTf-1YqC6AqW43K16amu2i1kfWQGgH3CtrnQpU5J_hUpoCRPn0XapqoSzyyuMQGqV_7OCWZdpjXSRhvArbQdh9xK69nKF6_9Ovnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzPoq5xH8zDyvq5t2UFbiJ_V7hk3yOioeCnGUZLqIQQAEH6hQau0UsF_NOGshGDQUExfYFLBpnxvedOsw-Z3RgBzO9flIqhjmNfsFL442YJQZJNQwaQzy_an-yJ-aDLUXDW_YxtgyyZnwg_wxNrqfYmvRRJKk3TOMcYjzlQLKRlzvqkrN5x9sYFRG4gzYywDowL4Xiv2p9hEPQ3Gi4OR9vr4rcDEQm1sBChAWxLf_Yfx1wl0zbOququiPWBhdtLeL7gysGjUKgUUkS-KjdOkj0eOZcIHz8xwxwkNP_XI2KfT5h28R1pSWo7t7DTFMi_jKF6lT2wlOyKh0pE3E3y8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrTBwJ5lftRL1d4TgJs6Y89H_bcOAGIqhgmKtbRSSUty3zy1ELZyrV3lIItqIGWSqnmiquKZE7ryw8aRg9aBVv4OCUBHmtWQRS4CW_KzOVEB8PRkuiB7oa18FT3aa0KswlvleagASOw8h8Q8H3voTKma6SQdRza03NaqXejqSicvcirLz3HvTymRopsPk97CGdKC1EwL30ZqbTn3NHzFVFhX1MSEaPN35fXR-IHQBG_P-ibHyKp_U4BZDbbzlI0ykYB82egIGJ5xK3v51A8PxgIpENUecmYfnRmxi5nS6pMEdKiJRzXwGX3fQrLUwYFGTcPU6PfPZUB5tgsc0YR6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJl7SjeFczgA3VxX-ywxxO3mjDY2EYCRIW3KDVYmP-zOYz-7k6Zas9Z1EIYXDUOafvWO9fOSd2is9Mm_V9XPCDTUHYTLr40pLU4fYeiM3HJcNGMm6Ufdo1J5LXluFWOCAn5bsWvZ2l5vtMMohEyRp1QnfcYxIoT0vvKhAIKsiyjEixaxCsqkkgheAJQLJxAxHC_pd6S29YPW0MGDVfIN80M0adS090fBXQxCk3nWIkVtxSe5Jh558NVOjdGVD-D3sV6GFsqzuVmF73yVaFZl1gLQrSCMXT14aetnp4wZW-gZ0R112CTTfY0Lwpat5dl4psJta48a0w7I1HI8pW--pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT3EZ1R7gm8fnTd6r_zFBtOMtghyWZhMoLbknqPzIstnYzJrrtIvYtQczEqliLLsMbCH9cJuRprjV6YLUiQ05FjutYwj84jTCPM6j-9-KdXlhLvw_T0uebOiZHzI_agR7TigqBHmEDsLbV_9-sYZjZpNTIxkxvy_EgJzUrx3zMEJU9bsQ0UvDZBuW4Gl2qWNF7b1y3IYrH92XEqPv7c59W8FBRuP6qxFMLwfWmDm1jnEdlPP3038Be-rT4dzaQSzP4A8RRRZdJlaSWTb5YeOLYWiHMH3gBAFrRznmbb9WgZ8Q2XiS2gJrzHhleXpXQ8AAWlZYBWf4kH4QbwFhXQ1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sypP8AJbTt1DaSl1Tj1oX78aF7_Q95vYlreoVfwX41p5NOR9U2OAYOKHwElk5_cNHgQsF0GLzIZSHaPLhmZt_X0flh19WIPrC4USajn64zAg5zKbliIhR-v_b_a_0QrLBIjUA-FnfAbiqiJOdr04DQ4Yqqzvk-zOSdGx4KIpjmFIGdpDjWo5Pwot4AWPLZ8L7UsMvGAWVMBNKFg95SefmgyJ9RELYR-eI2Xc61oKc0ksLmXIbs7RtmWBcCrA5BAWnE8cNTgoo_A_JZcK3t6s0vy2HPLgqoCVJvziTkvWhvF89uxBG-oQl1AAX2hvkEZsRkgdUyCU96JRRZ0D1PBwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhjgIXns90l--YxpZmQDuJ3TuFwJS30w8C8YPUHQ1la5pR0s6zDezy2rE_yBaW57r-L0PHwig3GDSQhFEReuCIbVx0l6zacnwnyoMtIhsFdWClZr3oZyoTeZDlwm13kK1FTFPW1YGm4pBPjEWzKjRxwr2fmDz4yVcpzWbzRRI5PyiO3zebRMYp9vZul__hBKcuecZUxzgi51QFaE_vMhM1s_81FlM3qF7IIH33YCStYs-Uy3ZJ9-5z0HW-xLSnycn3fASgNJqj00C7GXpjiZvaBbF1QC0rOgKEwV30AX8ghRK6_-RlMWnlCsI5rx_k4oMDVY34VWzOGnvU2lf7VGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRvhGzNTBoAsJhW381syHUwuqOkmr3C5HELywNAcMS1U06HDNPxda-UifG988enlAc2tPuXO66hyXw3YPDw-qgGcsRs9fxTtRLylXK7J-ZA5KMvpQsFdLgrUmLIcNTajk7-2EoFxPrTOq3XsuDOwpRt2go_iQ4PbEkk2yfcaz6XVZv5fkUIy9UAwSj9amWllzcRYGmJ8w--HiAES8EOzmGUFGack3jEml5FsC9K2ZsOA8OhC5w3r4JGC8rqqUteY0TspjpafyhOuVR4RM2-zT5_oUwDaR3L--J8--0VCsLJaZirSBRz6E_Y8l8B9TeSbR2xDDpsUfGaLYVAJrbcSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIIT-NiQVER16A4XrBpDD5ezfxJNTgJPMBEnkkevXIfM5vN5ikXy2yMtbgFlWiwNoM_EdWpUZrKGyTp1_m_9SyxBP1GEHZERU4d0eeiqw45bKM8bDbbPgofYENVPMBMuA5xgZmiF5B02SjeS_BSLyZ4Vqk2VWboTl8uwHaLDMkHODRmN2Xa5GNcZFhXcAWhKgbp-MPZVOZC1gyrkIviDDYPCd05ckqM6JH1qZOW5tnaNmtoZgtOIY9Uw6BGdfUxZCq-2qX-SYhi-dSlFKgEL2Yr6BUzqQUp-ZC0Aku0s4vFbM8I1xGXBnFqSbO_N-QHX70nYyzPrI5CTdg_jeK_NSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=uViX6rgpuEl1LEUQ9VVKPz8HakvjBpKvAg62jo3byTvxhyOyEiQi3WQmfXibkd8L2w5KV5zTWWlgM4o1hp-IBnANvnTrnidT6x4buKEv9GDCDKsMqj2DXsc6KigbT0miIJ3aEDNacxP4o9B_7URmQ3GN897EdQYKjeG3vAI62XpQ-oPJk2WSHutY119oCxM2tgfrZyZ2F_TjQVbvpScCtDo3r839cpf7GL-Lt9iMr4xACnGpq5-js7oi6MK4iCwIqKYXx4niHs3-dnkouAAvEJGVSEaAqJ2nCVbkTEVT268gWePihTa3jTrsanLkO5xFd410S7sad0WxnSXKjbPoBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=uViX6rgpuEl1LEUQ9VVKPz8HakvjBpKvAg62jo3byTvxhyOyEiQi3WQmfXibkd8L2w5KV5zTWWlgM4o1hp-IBnANvnTrnidT6x4buKEv9GDCDKsMqj2DXsc6KigbT0miIJ3aEDNacxP4o9B_7URmQ3GN897EdQYKjeG3vAI62XpQ-oPJk2WSHutY119oCxM2tgfrZyZ2F_TjQVbvpScCtDo3r839cpf7GL-Lt9iMr4xACnGpq5-js7oi6MK4iCwIqKYXx4niHs3-dnkouAAvEJGVSEaAqJ2nCVbkTEVT268gWePihTa3jTrsanLkO5xFd410S7sad0WxnSXKjbPoBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJlEDAt0zhpj6EZZ8Jd0-viY9CjUOyMB3ilIu0sK_p-nx0XUVaVDcf5vbv1yu6ZA9TAtU10YeFGs3lRutOqwWLAQsh9oU8gMOjrIh2rLvKb_aiUmE9V44V1z7wBqLFGMhZ59WdSLIVB7GAiDVEPLKIbmXIuM87oogNMPzwL_gJPkJUMG2JESbPOVlZC7_uiHYyRpFW1ocHV2gFA3HFzbbQS4MEMTW4-FH3WAZ_HCAr0r2WviaMzz6XCnCpHs_6Oy2orqRY3cMCXPG7VbefVNyt2yAmyYq7P5W91NoyCaa5gPBq2XXm3Zeizv8SdMuiSAY__Uw5hZs4EOeFW81eWh4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVKsnifmgP5jUweiwyOE_pbQprepSg5XrxIOWnz0ILZEG8bFF273pOGSs4O8IkN7CZ2S5guRuJk7dFicAiJvbUL-zfI1--JTtGgz9JP52bqOJCCEShzdUTPZKxUiB0stZVgQr29MVs2IJmk2U8a2VYnS_ePyUutbZwPOOoOPPyj_UwRdLHgSVYbIEXV3U-4g2W6JZ0QvzQUfX19un90pHsIhJZtuL2ccFqkZfAwg6JB-NPC0LmwHAaaOZgYY0vjc8B-KlC7psad0KThtk5A94NM46c1YJuH5NtsAdKmm5G9ejSZ3cLRwHYk_8PMRrb-yylsSIQFPhizRFEpc7xHQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXjqR8-19cnwoa5fPzm_cN5M4bASQcSj0wACV6UJAJFBAYcPvY6eyl_l1ujbXZQLRGpISV59Lo8Fw5VGBwzKqnf2MusXwzhIxO-6JW3WW1AEIcpgqZFPdktrgLgQwHxX4rFMmS9BCx4SQTk9LAU3YwRIFMraD9VlhcCSwKnw13CbnDA7ZKposIVn3UvpHYayBS5Sr2tIduNk1acH-XC0eChvp9WDpK-6wbCyg7yWvUtVpvdVwxwU_6KTx3L6w-JzSVm8JEpSfdBdH7h2cxPVJ5rwU3rLC-f96Y2MJiaG0ZMg9-iREA2Yxv3nLx6IprMIqz34jBv6na-7GRUD794aOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RslSvOu2cfrQIhqRx4twB_NYRY_Od93sDNWBuz9ob3fZndM9f8NgoqWkpoGjdtTCdbyhX8Pa8U0qjfmu6cqa4xTkW-wICEhbggTgNB_16Jh4DKAEvfBcFRNUU1h1gNvDYIgX-aN1y6QMXBK6Oo8ozxG_TEJ6Cx8wgDFL_4OPOSn40WmOWbTQe1jyzrmLCH1RrqPV4S7rWcmb_bxTRRZgQJ1ejSRSp-R1QNwAxQWW61rHcrBIdmCPO6qlqRMvCKx9juqwKrxVhKqGgJw_J-W65ZQ2rwTclJ8Hl4bMiw7QWCGsxn_RVUnKFumnN6GVE2bCYCVZPSz0WrI9EKv8-WiqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqucxcJni1DlSRP8X2FIzDhFSTv29gTs-0VXEnGpwg8mw4UUMZv2oPXM8E88km4z4U3dVhGspRmTSUEEVl2jjoOWoXvPVK_KD65tCSM_CGqCy4XU42HId4xngrZwV6PRBpH4oZh-c2bnLEq5kkOQ8FBad0UyvoxDKxfEqZAjDpYqlFJMsMht0t1Dbn7t2qpB89HkzRrOPpDlEiHSygc11ZLQfu09_tg5jk1a_3vxCuFYlWqk_B8GKpMZkWffnEN1lZaEac6tCKgvTAYDJqRuGTRHzsmy1nibL02irjFs75GZJ2Xrsvz261hRGZmylHSXL9MAwv98xAsQlWzX16dBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIBT3QkH39PdTi5KaFzaJ72Go7mwawQyafA0IaVwaEr_UQ2HvzAjkNLDXbaKKlYpr3TD5muJp7NUZVAoRsv6ABePSD6ExaWcqku63m703TRvkpCQX8DFe8hDB5LLt8w_S6-wUoAiQHEVT_btK2JlhaJmb4yd4jyiv616SDxLuaWl7Ad_InSgF83-yuQKCeIYLy7JR9zh65OF1n15TwaCrSSvd-jiXbUIWPLqZQsdmqTNcdbGG6tOXDIXbHH-0hAsJA20E1-cxZh6z6EhFyg19NpC8AGPEofC3WjGbsmRs-PcsZWQGXe6185ZP9zP1FrzPSzLFEZSPWDsfpceH-HSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWCR-eNNwnP_OUIz9OMEue1YIBIu0-jPZ88TQdacSTNHDFTtza7-8hYK8m2nN50nH9QQapRmYd6F2lLOY4SYNShSpERkwCstS9U0_zA9GLOP__bnvFBES2-LwH3U67O9LnDI0zsMBZu_FyqVxx1lfE1H0D4pe-QFMtp5svDnCEpoALrR3Pty334qk-4LqcPFzvrA_Nu2koIjGA31ECHsnrXso2KsjC1RSVwmhsuWMzprlaZTS9FALDK9tbaFoCkKunGK4H5N7coU-_vIn6-uA3MH7XfMM9HYCGg-nRJmyOYHR_mHdbrecbyiACad72mgwhILmVoTfMbpKIFZgdmDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtYQqCW8NuWYeEX4c7VVhDCPBkqsdcgJpcQE1XWvcUgJJ39YAReFqDKNsoviOZI6Cat-G0duQhSikoCtd-JbTdYT0H8IUkGiV4gt1LpFp4xq55CTY3zbpi87hVDFgOq9_YOG0y3rAXmA8wT-WDpvx2GCI8nbEta_-juiNyYlyNeb0Y97FJ2uolWqJGccFM357tGhlAVZ29J3ZYMPteV2fFJ4wNIZh_Iy1PEHXZ64BJ_TKBh_cwmP-a0SIt0PyK2NjdlgITIluEvOZwAWDG4DWVevS9ly9v9RTiGGFDbkPCin57wk8DX2PV3oFIISuQ6EF8zOqhBwUCSRUyt7ZUDYhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=DCt8igsIDQ9yW34n-qOp7JE0NH5EiR6d34PxnuCkuq5ORLQDjljumT9ojibkyyePy7wmbQXRUeB3dOj6luL7CD5xTA1WjQP0AKVbmx8Wk8rPsUXyiswSYNM8jdsx6kfVgnOXfsEF9Q9yodX7CSSk66LJZI2LJ0CuX_Ml25re7rz3_mHFbTvjsfRt40mARy3b6NkJ4Z3n62MDDfD-KvwsNscQG6NdjDgvIztrHUP3RI-XPsbkOcAGR-ua4Zwv7kCEFZIoI8QxKJJJInB8Www-RomZL0x_hxaSRYXgrAVXVyNg9fv8Og8H7f_IIAp1CCpkhM7kJa_8MQtDclm7amUt5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=DCt8igsIDQ9yW34n-qOp7JE0NH5EiR6d34PxnuCkuq5ORLQDjljumT9ojibkyyePy7wmbQXRUeB3dOj6luL7CD5xTA1WjQP0AKVbmx8Wk8rPsUXyiswSYNM8jdsx6kfVgnOXfsEF9Q9yodX7CSSk66LJZI2LJ0CuX_Ml25re7rz3_mHFbTvjsfRt40mARy3b6NkJ4Z3n62MDDfD-KvwsNscQG6NdjDgvIztrHUP3RI-XPsbkOcAGR-ua4Zwv7kCEFZIoI8QxKJJJInB8Www-RomZL0x_hxaSRYXgrAVXVyNg9fv8Og8H7f_IIAp1CCpkhM7kJa_8MQtDclm7amUt5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REJxwiPrXRMnLRW3IWKDWG7DGoClSJyM1obsDY8D3f1zbfQbOJjYfi8B2zpdsOFlOqYsh3Tbd7K0JosTFJhW4Kgg2YHo85r1Zd2xEBMTBBSGkfUvqhCWhBHEka5Y5i0snknbO0WTaB_UOa1xB-NOZ9sYjG0QQf3r04MqY6Tt1VzrPqjn1eZV2C8hALSA4JvlHTqyBNUAqXheV-cLM_8up88OudpES34wxsMbXMNdmAMuY5GEUE4yEENnvcVO9FAy_CCVCu__X7P1yMxGqD1-63yQ0l_FAoQazQaww7GOucw0QcbgGXTl-MDZ1qvQJxpdo35qjF2Ro1Oxx8JJOVVu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuZOS2dv9fVCckJp2GBzCxkqb43SwriPSNVe2KOFXTFLCEfFO5xzCr0Wl0u-M-D1Zu6Tg_vJTnxU0U6j_GaT0UHARecHn-fIYl0n8FnYfqTfhehn6YmNcCebR9w4j_mLZ3STqdZ-j8UCUb7AW9j9Xk0GjAu60sfHndCGLu286FP8TEF4dnYk-KD0KqI1TQAZv3uV1Nba2w1JVQmUENZQ5kGuEZ0OKKBiRrHuNfOMHNZ8zGZbstLRf6tAv35-Z7YmXn4aJEu-UXLO5GFdxCytsS6jomQfvGKNIzDIC-B-_mUNWn3E15MDQgwYoWR4Np8X2PoKXC1_M_-KaHhovBIBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJbFau-y5gDc-aCnOdBS9Q4VzmxY0SxlESJyLsRdn6EQsnpQnoNMQE8NkBn30nSs7OugafLFME9Whl08LBuYjeyVgM4L1RpnGD0Ipo0xjSeGjuQM7bj6WIesAlATsKyMHNRIRKQTGUpW4Z_1embcdoJUf4l3ageXKndI2lV_xIkwMBnxJlczbBr_uITP2o0JJZhqXmFhD-DtErY65wDnID3aJhQNW0qM3t3eGfctxaUXPbQN-9Le9FqnEEPDe2HlPWdvYl9nFG8QUQvI4FEsnOK5aVsVkb0zihrW-BGjHDHXJspE10KU3l1ShaJGQbVzexd-Bqau9CZ7VYv4V10gVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOZYrelip2g4nznWbcTu0bY8tF4SpWGGU5kktyhmmbkC6jyH8xZ84JW4cHxrnBRiu4voZwm4TMU0FWuFRDxn45TZ51j1umYMD3afIaUeeeyn-Ong_wJ85uF8H-TysDcBlihiufomt0TPkM8CSGvO0COPuR4c2ViOXYZUINirqhHP4KK0NLl_wiSnskCO_fYUA6QbCyiXQEOpkC7SAAXN8YUC3_qBGk2kypnze5iUUQr0NzHPIXy7wEho8mNFI6Ya-heUjSNI6ZqaDHly_kHTLCZLiQHe2Fdx4_LCtqQ9ECieF1zB3GN-bnh3aM2rWyIaMe3ECcRXWT_7T2B9ffijrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7JSI3UUHifWJbHu-mwOzWev8xE-3RE3WNc8WO--bsxdOd0r2QKmaS851rZfi0dIHxEuz3blu5nfhiFfh2E7s8B_fvE_5yeqTPGYMp6hYFqnGtnOOfSyOiAIj1wreZYdBY_JF5OqBk9xz_CVrmAPTovy0n-mdyX_toKxNcjAb8y4QpXuPtg9fOX4P2y2lteUcMXQTK7fgmdwXCPO-YYmyfFKMEVO_BRt5A2yZHV2RFIfTi_T0dNdjXIup3TXzQFo92CSh7kgmYsJIllAFene7wZrohmcZQMHU256Lg3-MS3BIINVdi4etTE8x4LaCsWwAIfa8rn5-P3Mn4S1bIAFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehFfdaVirZK2wv4Xfcv9K89ESemzO4co_yivluZ4LQgXJD_aJmjk2xHCqe9yDfCF3U3Z8tI8n2YTaOnPRt7rHDyyYTxX4xlwdt5ffX2XREbaV0V-gNhFU2bxGklz1L7nLbq6st8c4E_0NSGC7JQ9O-uqLOaC7LRDR-vsqJVNOKZjcCXg4a1xaGqg8S6hF_71tTfd5MpSMGoAIz6hfma2vWescbHbjjSTCHDZIIT6E1_OC4wrNMd8nErxKyp2sCNw1PjWQwLqHIn1IolmDdb74DBpnOhAMEpYMSpvJbZEDBbEi-VsXKs7N2du3DIVN2u6vkvsxDurAeuiRNUYemLxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH2iaFcbaht_WNo3myYwntcEpcRhZZaZKtftLU9_3iBzSGOTFJUAiRVHXaP0DeovoBjm-v-LnXajq4cVJvYHYxYmFKbFqcNprfuMMA59it2L3cRDi1eCn7nZrYYEyXXu5u8cvaQNYEV0bSAgaIIY-s1IqK5lu8AjBySgDvLg1aUicNdUwVwIGQMoCRjx_QJVH1bSqt1Gkmix0VClKxjwwG5PZyF67RvcSzZlc_OOp0Dw-L_JavZznwWNazQ2qaGmhHNM-9ArHUIJuHJMdR3Zi_8J6TAZIWAnW24smN42cE6tPQzUX75v6NcQGwCNxL82N1HbL4UEqSSZo4PwriByuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=ltPiCDxHKNSG_HKYypAxbyg8_DmagnwrKQxVNNIxAFFBSOJK1wdeoLRfjVfZcQfbDbggNi-vEqnrB6npRQ1YluSRiTex2k4eSkWdfwreIRJOF4YCGKkg3pzOOME0z2bmzhZbuQCaUQfR7uGIpXoH4k0FwABdJy42R2q1o-emlQxbXjMz3MC7sjLg0BGCeIM-tswMO7Tx7fvRajKk7tO3CBrtS9dNBECB6R1JY6vYSM8qDbz0k7Gt7AQabYrabePLaalochcxLXR_XlHd4dECgCDu_aU0uqBGnXTOrQjYwyZvOj4hVis9P9jS7PrL1Zk45SLMxc_NCdvpVKerx1My4q3CfQNPMoaR2-TimLAkyGLBFYKPRg-9UWktw94KxGrwCFSVNwA6mOgJX11vyMkljm5LR4ZPhwevyDEYhD8m3n_H440XnjYMK6oJ8XS5UiH0H-zsscjyC1-UfJayIXTgVY55PnYS4oFpSMzAeSxKczBODYvHajgWkAuuuCV8b_C1rrOFHBZxdHCMz_VgdleW2fG6CY5jvfIepFBDWebPo7KijsOIcezRK1IIsJD7HJBR0pQGr5b75UVDOKVlVM4lbu78Sc6oSR5NMIuU6HX7u79WqMGG34xxSQMp4BD6uQ7w6R68k_AYjRe2BELzQ4CJzEndiH-y1suxeWlwNwt4O6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=ltPiCDxHKNSG_HKYypAxbyg8_DmagnwrKQxVNNIxAFFBSOJK1wdeoLRfjVfZcQfbDbggNi-vEqnrB6npRQ1YluSRiTex2k4eSkWdfwreIRJOF4YCGKkg3pzOOME0z2bmzhZbuQCaUQfR7uGIpXoH4k0FwABdJy42R2q1o-emlQxbXjMz3MC7sjLg0BGCeIM-tswMO7Tx7fvRajKk7tO3CBrtS9dNBECB6R1JY6vYSM8qDbz0k7Gt7AQabYrabePLaalochcxLXR_XlHd4dECgCDu_aU0uqBGnXTOrQjYwyZvOj4hVis9P9jS7PrL1Zk45SLMxc_NCdvpVKerx1My4q3CfQNPMoaR2-TimLAkyGLBFYKPRg-9UWktw94KxGrwCFSVNwA6mOgJX11vyMkljm5LR4ZPhwevyDEYhD8m3n_H440XnjYMK6oJ8XS5UiH0H-zsscjyC1-UfJayIXTgVY55PnYS4oFpSMzAeSxKczBODYvHajgWkAuuuCV8b_C1rrOFHBZxdHCMz_VgdleW2fG6CY5jvfIepFBDWebPo7KijsOIcezRK1IIsJD7HJBR0pQGr5b75UVDOKVlVM4lbu78Sc6oSR5NMIuU6HX7u79WqMGG34xxSQMp4BD6uQ7w6R68k_AYjRe2BELzQ4CJzEndiH-y1suxeWlwNwt4O6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=R7iN4Knej2_5quRlThEOqpoIZNBRS2JGbfN8BrY6-DXtVZ0n3aMOV2YO0WwwcVxgCLtrBucIPAYuzRqW6njmsv74gUM_mbBWFSqtsE6s3vRPto-Y1e5_NZlIFRqY0onBIxS3WwkWwsicIpcyRBRSOrAugw_N0jr6PYouz7dpd1LKKdt1BldbxzCbq-hl3yRFJiLQ9pBO3zwh1LTbGYZ3IXJOogvjUHoPDBpwN47bMgD6707d_35efns3h1P9soIqt7NHah0C3LNE7wEeUroNuGWbR56azxcCxAS-0yu1hHYwXar1jl82xtCVv0KDEZ9C3GTNWVpnQuuPk9Rk4dWwyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=R7iN4Knej2_5quRlThEOqpoIZNBRS2JGbfN8BrY6-DXtVZ0n3aMOV2YO0WwwcVxgCLtrBucIPAYuzRqW6njmsv74gUM_mbBWFSqtsE6s3vRPto-Y1e5_NZlIFRqY0onBIxS3WwkWwsicIpcyRBRSOrAugw_N0jr6PYouz7dpd1LKKdt1BldbxzCbq-hl3yRFJiLQ9pBO3zwh1LTbGYZ3IXJOogvjUHoPDBpwN47bMgD6707d_35efns3h1P9soIqt7NHah0C3LNE7wEeUroNuGWbR56azxcCxAS-0yu1hHYwXar1jl82xtCVv0KDEZ9C3GTNWVpnQuuPk9Rk4dWwyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkh5HNTVa0_PII6rReubze_EdAnG0n5WlxzK2Rl0BdiSgtu5mDbuQaVFchyKDEq3yvRTe8PFbq9JOz2gbZe2dhXTKpLAgdYy3TVWEUkEM_l-9Jti0OHvVIiau6dspyv161qDEkrohT0qbQFx7IBOJ5WIYPKJGNG_HxDZC4a9JCIQkNHIqBT-rGjY5GYTM4L5-ZdoZEHCiOQLL3z1-etaGJMbjoER2nwSo1Oe1WAoezokll8KlSipR9-BOPKGaAeaQyvAWULV3h8w-HFc515hyqaUGLX_6GNEZpi-W6FwzF-XISG4Pw2LGnPlj-v2sCF1J5DevkUdAL_c1OAmdDy_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgaEHaJLmiI1aXZKNaTBhhfXQM7V669A39dW4NG-5o8JvheTQp8Xg-Ctag57tC8STwi6hXueWy-6eq_OuzOuFgTE18W28deozATwj5QG3JgzVvcWs72fF1wU4gqnI8xYXSEhQt2qbRzJb5ZBLFDANAKSIUAZF148YGSRcaaP54Y81sKKBOIt6mRvirh8PMWMMJ2htuRgq2DiYtTKHvLRwR1YDf1X8mleb5H3wflCh747QsLX6p0zmhDyR0d9SjDfWFbqrhgh6Kkp4d-HnDo4OF5hwaaz6uUo8jA_PNZVIbTJnekgC4YB2yIsMFVnvCwPgzj78EEgr3yMA_8ztejvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=GvUbweFzd1Z8lK3x3QrWR2l2z1AbprhJTEKZnsxDgzddD1o9Q50f4kvltddGCsmSgIvo105T7ATVQfGj_kaUf2ALv974CcDh8udFoa0U4gf4P16bMf3Tqg3ByQPAiiiRmQD5VOhViIlFuGNP0xMyLBvUttCG5mMjXYrQQtB6y-wH4Hjf78vQksHTVkqijhfUOJgFveneGJb0kom_SJRz7q-OFnT-L7WB6jtqf_762Zy9l1v4Udo4S1oL8MSfRj7Ad8YJJsEsGv6Twto3bcbBlW1VADMyng5oVklZ6aO5pbjwLztmABOMn3R2bKOm2DEgTzwpBhWlb6fQgkWspqiXWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=GvUbweFzd1Z8lK3x3QrWR2l2z1AbprhJTEKZnsxDgzddD1o9Q50f4kvltddGCsmSgIvo105T7ATVQfGj_kaUf2ALv974CcDh8udFoa0U4gf4P16bMf3Tqg3ByQPAiiiRmQD5VOhViIlFuGNP0xMyLBvUttCG5mMjXYrQQtB6y-wH4Hjf78vQksHTVkqijhfUOJgFveneGJb0kom_SJRz7q-OFnT-L7WB6jtqf_762Zy9l1v4Udo4S1oL8MSfRj7Ad8YJJsEsGv6Twto3bcbBlW1VADMyng5oVklZ6aO5pbjwLztmABOMn3R2bKOm2DEgTzwpBhWlb6fQgkWspqiXWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neRpdp1anIwb3xY0k7XhISg5zgFIdW3nS6hXB3lmLtzici0uq-eHJ-KSlmU1EL7SHkWBEHZRvirDMCGSxKotls-UzaLABetFgZVph3OfjXpVhOV7nR3ssNpSSLYqNYOKPT1mOeWlz8QRc_dEC_adk8-l6id5QYc7debH9fjHPnEB1yR4a-wXmwvA1UANqYPPn4BYGAD-gCW_zepVL0rPOTypvb550E9y3GSjMUBmIaZ8WEVc7FI3h8kkHowP9RAisqk79hdAfUe0Rg6adr_tCvkqXA7z-uc7oZzR7KIoy6f3TQ4E3df3GuUxnmai81DqlUfBN-y5tqLU2NqDiWkqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9SICQhU_Et9ik_WKzs_NibKR-k73sdW4sONQzGe9lYeScRDFB-whp704FxHaUfaR2qX256u9N7JdwqeRvwMpPMy3ai3e0yj12O7pou6D0RT9RZH3DKtJYJjLnGwGlV3_vqgqDEyqGLjx80ywNMbhJnujOEj3O7Zzo6oMF1Bl4GsMR1GuSm_fFF6cR40s9uje6y1jVI0hrBaxcehc5oS2r_fdiCqfxPrmo_BdyH-kF2a5rM7JbCODYJww9Wc-JEYYgAA2fLf-qCCC5TsHZEhAOsvcJSRNyipUmsEJKMnP6I6wU31yysYJRXXFKFTD5bzGoySKCpQgezy8bPg0FKtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxa6kseAySbSeCHc-AmAtzRkbLxmzb5wxJiyUPiAc2RxjxBq2DFdF7RzTjzFlGfsgGjnNog4vAPI767Oh-SjOlWEO8sFn-y3Eeym7eZ4F2qozjzq8H03xSDF6yyvl4cAwmysgzu6iKP6tddluaTnsZv1e3McFyoAQ7fOC8qUQZR121-Pot58o8xI0L8UdcWDKl8MmM_b6R1V0-uO7rDY0kYBKJOu-yh6axw-czsjiwt-fziJ_pPgq11XdGm73oU8uA6ej4hi7KgTsesLJ8itHUAD4vRNFgLuxlJesSrH-wNst7s-6IEFIUKxAK1TIO7iqrdpUb03xrU249t8x6lvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0x2pv0_9r_ctUEVn2PAYwCT9nxOXWzjxoz1Q_tbrTJyDyOH18n6Kwl_XWl2x6hSuJ3QfKWMdKe2o7-YZYx_bmaeJ-vJbPIQSkNXcE2VES_V4es_xOYTlmVXEdCfRpefw1Giv-UO_dpLoCrrknd2FbA26DMJbJTWa75U5nO35LxdjVMGXjM3no7GxSedD9ZUw_TBwhm_kh54Vxj92DB86NrZht8QJvw8SIORjA7v_ir3pKCtbuyi_uv2nns4OyAQrmTDX805Fyu9GGplroBmWh5n8RMN7v40Qdi8ivb7rXzvcK74bJ8WUs9H0ovJe1Eas4RSDg5yACgTXYSpjCPfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJV3ZnWlvUHSmCf9TRXwfYacgeVqSI583u7k_uXATEqQHDtVIcs1uVjsB8YxKM6b3AV9fNzqecHQZJdqe_gJCza1GyuJjsZ3og32TBJH4YoU4Fc_qMy2vHFXVMUa-gavClbn1bgBQOD8n2u3RQAQvZ41TNU3l7cHQsIhw4mYa7NcqLRu84tXcBD9H6h4p-AhVzyGfCwXatIi33jJdAsTRVB8sfZYXqDAYEpRFmzlv1STSGoffCYnOqUbnnpPxbX2CmqKvs0R5gPQctXdqrf6fhuVrGlMSf1RhSKdx-z-BA0gOqA4eN5J32x_71Nfiki-nEfpiy7futHkX-7OMPyloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5W7a8zPZworQjBahc_tA2qaU-a9rYfsKAwy6Zzgl3xQbA5iZGH5Cv6agP8m0KgkE6SvPFunXEjFl3lx12Vbir_stUhexM9_CI6ed3LyY7iP1M3KDKJ91bZ0M_fJR8kmu-r-m1rqeOEbkK4AtTGPcUM5VLR9cEEJgJI6qVT3dVImN1lVOmjrqMWZmFH3L6GmVAa9M_tT-lXg7gcHAiK2agd0TTUZwZ_7D-hK14SHli6R8TXAwDV7WoHChC65QbLCYJ_D0R1RjZZVwnTvRoCnG6BY3yVHYMEpkdXdt9rHYYFV0CX5sbWoQpNqCus6ZUvhQGPePsqkutbZz3H-es82GfYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5W7a8zPZworQjBahc_tA2qaU-a9rYfsKAwy6Zzgl3xQbA5iZGH5Cv6agP8m0KgkE6SvPFunXEjFl3lx12Vbir_stUhexM9_CI6ed3LyY7iP1M3KDKJ91bZ0M_fJR8kmu-r-m1rqeOEbkK4AtTGPcUM5VLR9cEEJgJI6qVT3dVImN1lVOmjrqMWZmFH3L6GmVAa9M_tT-lXg7gcHAiK2agd0TTUZwZ_7D-hK14SHli6R8TXAwDV7WoHChC65QbLCYJ_D0R1RjZZVwnTvRoCnG6BY3yVHYMEpkdXdt9rHYYFV0CX5sbWoQpNqCus6ZUvhQGPePsqkutbZz3H-es82GfYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf20kicaej0YW-hM65SUJ-7ibW_RkeA16-DoheNzw7v3qKn5dPFI1U6hAxGElSwlvxOAXSfyVxsy9nBH_CfRB830QUf3TYuK-a7bdBx-8F_V38oG2MsU32ktVJYd4mlIcuFeHvc5DnQi9q5mrt8b7UAXNhPxmZ0htuLk-l1ljNbDupI9lG5mPNwdJWWBQXCMbSke4N_2KYvE5raiTzgBW3l6BCAgkIphPAbWX2QAOJ5RJosOaW03wJNofllFCEs7jQpwY-UN8a_KqBEQIiUtLfKid-2oCT5AYVxkbzcxO1H0jSLacZbCH1LF8-FZgF1c3eSs-4E6X8MKqrgMc3kjhZew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf20kicaej0YW-hM65SUJ-7ibW_RkeA16-DoheNzw7v3qKn5dPFI1U6hAxGElSwlvxOAXSfyVxsy9nBH_CfRB830QUf3TYuK-a7bdBx-8F_V38oG2MsU32ktVJYd4mlIcuFeHvc5DnQi9q5mrt8b7UAXNhPxmZ0htuLk-l1ljNbDupI9lG5mPNwdJWWBQXCMbSke4N_2KYvE5raiTzgBW3l6BCAgkIphPAbWX2QAOJ5RJosOaW03wJNofllFCEs7jQpwY-UN8a_KqBEQIiUtLfKid-2oCT5AYVxkbzcxO1H0jSLacZbCH1LF8-FZgF1c3eSs-4E6X8MKqrgMc3kjhZew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=OdjxchAtZuZyCNjmwGgbdEKh8wo6w1pTlV3CxTnmT5fKKLFgoX3tk9FIP64wlhOvdZtPjkNieh5W8ZUaLuF0NxUCIm1xbNIoUQ_n2FtYd3ZvVaqE-g-hkqW2EvGLz_wwvjjuZvc9f4Vn-H5B4k5gCZFFZse0TYUfVQasvDH8WI8JCWgFs6Gfseg9imkevHqMcfwpTTNTmXq7DMhN_Ire5ebjc2wdeFcYMeklUkWQ8kBV35APn3_V0fhWP4FMCdS4aaQJ1Jzzt9vNsYpRQ97EjA8hsgE6bMb7F7UQQO64KojWeMB_zEemjGNcGat21YEhRt7nmPEopWMkrK3IUr-7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=OdjxchAtZuZyCNjmwGgbdEKh8wo6w1pTlV3CxTnmT5fKKLFgoX3tk9FIP64wlhOvdZtPjkNieh5W8ZUaLuF0NxUCIm1xbNIoUQ_n2FtYd3ZvVaqE-g-hkqW2EvGLz_wwvjjuZvc9f4Vn-H5B4k5gCZFFZse0TYUfVQasvDH8WI8JCWgFs6Gfseg9imkevHqMcfwpTTNTmXq7DMhN_Ire5ebjc2wdeFcYMeklUkWQ8kBV35APn3_V0fhWP4FMCdS4aaQJ1Jzzt9vNsYpRQ97EjA8hsgE6bMb7F7UQQO64KojWeMB_zEemjGNcGat21YEhRt7nmPEopWMkrK3IUr-7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghGyG6Zg2ivy_ydvYaD_easlUN4SbyBcnoRvx81XYqZDzsN_-4TL5qk1drB5AjR82SMpoh70PwvI0epdQ6VqTqOBrF0v6pcrFXwody61OcjKw9WF0Doi2q681DJWaUHhRr0GmHSYxfbdp6Vx8KSp6k6TF5NOX6HotU86MiEDaz9X4ExL3A6LOVtP0Y3uvR9L7pZPkvKFL3w9t6xH19tZR9UBAnz-Okgtww5cw6uB3-ZOuOPn9S6PpDSvCX3ykBzF-xNJUaI2Ys2Ry0xxYyLVfVH-q2Ucn1Qaa1M3zXvCitpZ6yJSlBhTQSWfsTkwNp52y7FZvigwPf9EmnBqagquKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmXpV0Zul7Z6xGtvpuVXAz8UtGc3DVmXSW_9s0OLGmB3joHWHMoGzJdlLxVg9SW6chlPGfdEvACB3Gu0phqIgCFR0JIFEWTtsh6lbfcgNknS4am9pOaTW9mZxyiUVr3STPmEAA6r3u3kqEVIpgqRYWEWddVSeQZc6Qzz3RgaewHYkI_mdMkYnisaGiG1tgeC1JX3xelWZOSURjP-qVptpSvzgAjIuVVyQaet5o_-J61j0Bz8MwWEBKE_RwZJT2uc7vxMo1ioalK9ZLApA6RMa21bPDSw-GPsEckBRfdFyYW15a4ktdaNUQuQPsNXRs9UxxmhSEuUZ9sQHTMnfkoQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Y_NfX83eQ5S6x9c0hr3k79Zh41mfnke0fenE-Op721XBdym5tD6RSgf8P-pOo6ERq-KfjfsOECYvbLN0aM0T-OcDKnnrBHg0_o3MZn_3Ar9CLFpb2ZYtFuWAp1eYjKtsmqBYDh70wxuv8W_QY4DtsYJ5pyNgKB2boHzYwmdwgCCBS2CyjOrtuE7BdJsCWhyk4CdIkiKgi840C1dznSNxJ_D5ru2H9aWD6SmUDVT8HNn-RZHofPtko2FnlLtpP3XujYPchptlKPbo_lMyarHZD1zJoiMpV8kAnGBpHOeU4rPmF1NEFU62-ouch1ZWsHvwoOnisFzTB8q3BvPblFpBUxmXHvW2-5aN6__pOuZr5-0FvMLdQ8ddVqizhcGoeiy4PF19UhhBt4jqe3zTdhq8uj9KG-kRGMXTQuyYf8cZuQmtv3XZyTAf_0EIf3ITdKLox5zojRdnAPEp14i08n6ni-3uxZlCLPSe3ITMrSZi6O3Guk6oBGOw_Oz4IR_9-eWIkV5xjVX0VCPBc4g8xTfywFAZUwzEsIbQHnEi__oYqKnYA2LD6hsKYrjsGsqJ-E2jh_enfXFEUh7nR5Ze9_mjeTMrTqYz2zJONJWjRcebSVQu9eeKf2EahmT_VE0A2918XzH0MG9NxYprTwRK28JFmtK73GvEw0mxXQUSavOHv1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Y_NfX83eQ5S6x9c0hr3k79Zh41mfnke0fenE-Op721XBdym5tD6RSgf8P-pOo6ERq-KfjfsOECYvbLN0aM0T-OcDKnnrBHg0_o3MZn_3Ar9CLFpb2ZYtFuWAp1eYjKtsmqBYDh70wxuv8W_QY4DtsYJ5pyNgKB2boHzYwmdwgCCBS2CyjOrtuE7BdJsCWhyk4CdIkiKgi840C1dznSNxJ_D5ru2H9aWD6SmUDVT8HNn-RZHofPtko2FnlLtpP3XujYPchptlKPbo_lMyarHZD1zJoiMpV8kAnGBpHOeU4rPmF1NEFU62-ouch1ZWsHvwoOnisFzTB8q3BvPblFpBUxmXHvW2-5aN6__pOuZr5-0FvMLdQ8ddVqizhcGoeiy4PF19UhhBt4jqe3zTdhq8uj9KG-kRGMXTQuyYf8cZuQmtv3XZyTAf_0EIf3ITdKLox5zojRdnAPEp14i08n6ni-3uxZlCLPSe3ITMrSZi6O3Guk6oBGOw_Oz4IR_9-eWIkV5xjVX0VCPBc4g8xTfywFAZUwzEsIbQHnEi__oYqKnYA2LD6hsKYrjsGsqJ-E2jh_enfXFEUh7nR5Ze9_mjeTMrTqYz2zJONJWjRcebSVQu9eeKf2EahmT_VE0A2918XzH0MG9NxYprTwRK28JFmtK73GvEw0mxXQUSavOHv1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=v_w-lREMrzpMxtIQ2KNdv61LiuqbX_ChgEkKbLr_8ClF4rVeEycyTeWmI5q6-I1BeljukxId8xmu9tn5_pxNylu-BdLwXeMeXm90exY8H1ijtVrSS5jq0XDzlnggPMTwFAxmUiVrk-mxO3T080k-WpLr-eWZ9pwTZ_7bnYejOxfIX2e5iPkn6YaUjSR7-lLxkrOshnU9cqkBo3Z9rTURabo0smTn4-pfFGOHfsfOaWIfGqBKQRBGxI19-ylE1LIgmsnzVHV4qJUQySwqwtwl2XhU1S6q8EyIRZVVY2ts2iBvvKrDUZxbPG24zi40tbQMai7n_jVcDGVT_dPqC3BTxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=v_w-lREMrzpMxtIQ2KNdv61LiuqbX_ChgEkKbLr_8ClF4rVeEycyTeWmI5q6-I1BeljukxId8xmu9tn5_pxNylu-BdLwXeMeXm90exY8H1ijtVrSS5jq0XDzlnggPMTwFAxmUiVrk-mxO3T080k-WpLr-eWZ9pwTZ_7bnYejOxfIX2e5iPkn6YaUjSR7-lLxkrOshnU9cqkBo3Z9rTURabo0smTn4-pfFGOHfsfOaWIfGqBKQRBGxI19-ylE1LIgmsnzVHV4qJUQySwqwtwl2XhU1S6q8EyIRZVVY2ts2iBvvKrDUZxbPG24zi40tbQMai7n_jVcDGVT_dPqC3BTxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwl-Lg_HIlhlTq1vZla4O2sxZG0k8ATZioTER1HH7PqXtMnocyh35AnN-GHgAA0S3ZQxYQKhav_SlfAYWUEtONmbhuMr74LE8EBtgIKp8H3QETOuipIdbVq9ym5YhNEV6oe3wKVI9vIlVx_TdLGwpgxl_k-RP93o0q1wlj5CiVkCrWpPuAqyVi7D-d7_oNbHlke0SSRPSiwepCbx4JWM5ofN9KTlT3D_W6f-i-u74p2yZLv1R-pg5CultC_nVFKZFoFrSiiLHPHJ73sbL5J04hCrDhQ7FU56KBfjNOVQvOuGSzhACo-LtBSAqtMLH8rmU1UzEWxIb--umutRCJad9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRnGBkrfnuw-Eydyb6vGwtgB6ym6GdCMCpMvuLWB2G6byMv9CdO5e5u6FNVX6ZSRrxTXLkISkGzaARpX3CVVUOooMuYTp-Aoz_ihTdgrEwIeJh3nM3TEV9-3VGZIf-FekIaRO7bvvpIfT0EHcTtgZ1VW5jxBzjRxFllympUHvcfvedwqw2hZcOf55JL6KNJphs4Z-IjdsKUNcfGJBNYmH3b-J8q4hr756MrXb6HxcWu1ow9gICOLKsM3ZbXxWoNp9Tq0YKobIgOx6UarGtSGYmQn7ghJX9uWoNNAq5U1YMqKepowDHx8UjWVwDJgtw5BSUukZWqt94dDmGIy1Vd9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgArz-EtuN7hxnMXRzWlY1dbSMoZFFILmrB78sdTmX1vT6JSjWdJYNeOSA-97sDi8rs_sZ1BtDQ6ObjO0iNLhmZ2PT_WDa2Dd-tVKoYHXoBhRVL-LztVDsK9qh3DWfh4a6QgfdTDMZJN8P16NpTAnUm5f87VzkCoSiYj_-4YQYkrvNp0j10N65wAmaXku1uOZsO-hqkx20qCVry568szsf7_XmE4MQj8dWny7FK6Ff8DWTJTbG6zwtVWdAPgFzhap9aXW-VNL7PYtJV0aRDRz4b8mD_Spnc4Y1DZ0Ms5vtlBChoCbUp__YXD6xC44R0O2PSPDt2iL3K9Cay6llIuFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=JnvagZOQZvXaRtPAq07bjrqDbMwFJJsjLDrli5EGC40zwa05_lZwcgJQxSO4jtLcuupC6M-lF7rgv1moD9DlvfJVJQf3zeF1pLSq0p45MZsFgHC5D5gF7bxAVyF5soGyYFc9ahdTLBPaUelVsNhZ1jAObzM-LTBKf5Dg3_t6AFqKoUW6BSutJRr9yInJZY9U5hIFJ8FSRNwx_O2QVUe489UEUJeQKxf2mIWHNCB1cgiueWLmFdpq4NkZvmrxw42hZBfPD3SEly1ociL5tQhI200AphZbPxG88nuCT6M9b5Q2u_dkmz5RmC7ANMspHPOT2GTKxfLJZQTvlCSq2a7-jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=JnvagZOQZvXaRtPAq07bjrqDbMwFJJsjLDrli5EGC40zwa05_lZwcgJQxSO4jtLcuupC6M-lF7rgv1moD9DlvfJVJQf3zeF1pLSq0p45MZsFgHC5D5gF7bxAVyF5soGyYFc9ahdTLBPaUelVsNhZ1jAObzM-LTBKf5Dg3_t6AFqKoUW6BSutJRr9yInJZY9U5hIFJ8FSRNwx_O2QVUe489UEUJeQKxf2mIWHNCB1cgiueWLmFdpq4NkZvmrxw42hZBfPD3SEly1ociL5tQhI200AphZbPxG88nuCT6M9b5Q2u_dkmz5RmC7ANMspHPOT2GTKxfLJZQTvlCSq2a7-jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=EbAFYhrUIWhg-1cnJ1NFnIRn1ALgE2HQmXWLbUfpaD6_zBavrBPubHfVzcfbhpxUZs0OEJLD4OtBmNmw-gZOadyBukrq0GaQA9PgozgKFixyR0U0-vs4k00hSpduSj7R1yZJrN4njv6a-rTmOqweZrohg4MGOoPeY96B8xkAt-Ml4Zdzfty8LrBZU2809-eUunopi77Xa1VRXBxi1lGgG6vKPlhGDn-bzslXTH5OAylJMJ8ZwgQwY7pAA3CCFkvWtHzOHvTdAZBaBnPnmlp438gNJHOMPMOSxi5hWWxqg_2MIdEy39c6niVCPIjVoQrAQOFLkf-5gckWzIyF5fMG-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=EbAFYhrUIWhg-1cnJ1NFnIRn1ALgE2HQmXWLbUfpaD6_zBavrBPubHfVzcfbhpxUZs0OEJLD4OtBmNmw-gZOadyBukrq0GaQA9PgozgKFixyR0U0-vs4k00hSpduSj7R1yZJrN4njv6a-rTmOqweZrohg4MGOoPeY96B8xkAt-Ml4Zdzfty8LrBZU2809-eUunopi77Xa1VRXBxi1lGgG6vKPlhGDn-bzslXTH5OAylJMJ8ZwgQwY7pAA3CCFkvWtHzOHvTdAZBaBnPnmlp438gNJHOMPMOSxi5hWWxqg_2MIdEy39c6niVCPIjVoQrAQOFLkf-5gckWzIyF5fMG-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec52cMpCjkeOYKlKsqQJGSYUbkatYDNdZtneSC5qleALfeJsQIODAou4ZYEcwltyY_tMGpkQOAE9j9uMjsUvIg8e0VlyJm_skPdxbYoaZSPahQZuP2R73cm4o-eJmvJhDYkdMl5dIqPUkKarfcV-Pdcika4D0qvk1K-Eh5BpIZxQdUNHMuFTpREUGZvsvxAfs441yRHBhrmMzYhywTa01qa9d_B4b5sc0pg6aCS0jWZ4h3KJ2vIlGscpwDHbfh5FUHLaK95x7GVJev-vQwznGOKHux_ZT4cGa441LvV2phS_g5Q7yOSpvXksqM08QlMR3DWH0hweQPoDZx7-JD5MYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LknmGGpStEbSm5weeX_aM-k58goqdu3GfnELv2lZq1NWRp6n4TxJ9TNYQoAXLnjmgTR4np9ezZUbXgOoTrRQ5Pmn1p1vLfWVEw3ODFKg4zcPCWDcQ7yV1x7vIQb1rVN--M7ZdSSRaqdGN2oRf4JyNPdkNJEdHt34rkDOq1Xh90yCAyxMsY7tYZoX4RFtEjSS118TPFxju0xgQygOkMh_pfsPHWlYF_5OHFXKMlGBt5X2Gc5cuh-w4gGTKctW9CIQN174At7kf4PdySrcLAoVMm_K7xBYkSxuCngnaQtVF7qGwVd-9UuXmjdQcF4EJDDi-tjt9936QG-PdRQtk1xsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=OyFNQmf_UaeNcLVoJD-D8oMEnPaoOiENm47fPrXpJNgRAQNONuzrWoPlLH22SO76e2FrZyWbt8iOLUKoiV9tbebuWfNtNYv4viKon_ShwMF9FUZy1CxYU5ziU1XccdqRz2f10Ek8e0yCwc65qxfptRzY2BTvNPdp7Dr37q4hedcuhp8W1PfVywXH7cbqiRZVsBF2zHB8fG0NgrTOTs-05gi9udkDmWdso7Um_0QgLokitYpytwKGHsuda8PbHS4uHKK0enpoty3CYfCCPyP5K8q2-IsQhcJVZy8nhaF1hGCNcsjZsc3fKjbkq7NCXdjx64rg4XCZQ-WvnWt4q4O2Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=OyFNQmf_UaeNcLVoJD-D8oMEnPaoOiENm47fPrXpJNgRAQNONuzrWoPlLH22SO76e2FrZyWbt8iOLUKoiV9tbebuWfNtNYv4viKon_ShwMF9FUZy1CxYU5ziU1XccdqRz2f10Ek8e0yCwc65qxfptRzY2BTvNPdp7Dr37q4hedcuhp8W1PfVywXH7cbqiRZVsBF2zHB8fG0NgrTOTs-05gi9udkDmWdso7Um_0QgLokitYpytwKGHsuda8PbHS4uHKK0enpoty3CYfCCPyP5K8q2-IsQhcJVZy8nhaF1hGCNcsjZsc3fKjbkq7NCXdjx64rg4XCZQ-WvnWt4q4O2Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mdw9L9GqH0P94_bxygBlj0hPdJJKxWltrjJVsviaPn3Olf55-QaQ7NjjKnnLrg1Bbi8S3_2mxZfG0mPdMjVdBXxjq4jHCRKH8M2FUBaEnkHcUuIfM5rSMNMLa3bQ7PNCmrlw6QOuz9pS6wjDCgj6b2Sb14o4UGRIBgmhXqzWauAs4tbRESIDdAXFv3t8hnWMvmBtd_yTndbSijK9Q8hEeXX_XI-VwTXbhWA-7h57sL4elab2Pn3kDp9IVax18vNfbqYgy5KT31GXOI9XtHI7EUdvdV3_uEb8qa56MHIrmIW64aTG8fE7aLk6gvbmIpVK2VWAJbFr0kb3sDesnr3dEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al6AoyUGbIq4ob6tlzAmsDTPu-cozHo_SUmTOOKiAXX-pCyvI6JU2bnrZvpXVt0wHWgYxvvz41SrSjYGYtkweTNyPqVR9OLHVA8A4zG7opRAmsmOR6K98O2O8ykfsHhIVGahQrSKon4KAcq4GYbeCd6oVEzLblif63qcNgxhUfMCPChKcAVoSZ20MUO4gTnr2M2G8uenFFqB4uaHVRUmm_5Mgn_Y1wQqQpjA0VJYOzHlDoR4ddMsDSnNEP8f8tpQ74Bhmm7KxfDzEoBR6-JvVjYwtsHx6rOBugAXKuV_uuhOoCmeFu8TuMEavnD7zeBXMkOBwPcTrIrGOVSQtLzaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Snw_PL0LUyWRsEUijF_JpIAb9hnmPicmUvrlTlLp0mHhpIh7R5cbRRDa4saLbXH-lVIh7-T2vADWfQ89HxhhmOO1-CM32NhCBFoBXq3c6XLAna3K1nJ0mxA1gyI1N4eJcrGXdq--7iLUO8gZubayJMg9nc8d5nrq_-us4FUXxpglpnY6e9pc6T4RXu2U7-RT7sK6m5y_JYua4MAsarcxsu9qIHNJZ-P_Jko-sBatRe-j_6NM62CTOLJYeAUlQdeWqFC4r7KSUSygJQ6u_ZyA26sHm4Jhmw4JCcy2ygGu6_Xcnldes1NA1B4FchPKu_Q-h9NxAJ42RVIM1qxB8fFDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLbwMO8QtkkY5m-yTZD7WxHLU6TnykCtF_QG--KAEN2IjqsTpdDrHN3l7P8iR1a6iaF_jGCrEmU1zYFqZE-fz6K6OjR3yaGdqNsewY0qkfYNhf9_-tMpg8_8qwfSW4V8RD1-hYdxceokUS0b_EIg5xnlww-zkyu0TRK-Jmdeaf4MDGyI8PH-o2xme7CvKcsIKuqfZzXdsftSZmkM6_76EmgeEQ79mZuifVf-GfOZvBa7RFTXngpWIDebZJ1IOtrc_kKIh_8VIMXG76e9KT9FWWbhYJTcd33hI8jXjnHQGJ7WCekFKhDvCeVrU5vbKD_6iAhsIYStlJlTfmHfH8O7s9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLbwMO8QtkkY5m-yTZD7WxHLU6TnykCtF_QG--KAEN2IjqsTpdDrHN3l7P8iR1a6iaF_jGCrEmU1zYFqZE-fz6K6OjR3yaGdqNsewY0qkfYNhf9_-tMpg8_8qwfSW4V8RD1-hYdxceokUS0b_EIg5xnlww-zkyu0TRK-Jmdeaf4MDGyI8PH-o2xme7CvKcsIKuqfZzXdsftSZmkM6_76EmgeEQ79mZuifVf-GfOZvBa7RFTXngpWIDebZJ1IOtrc_kKIh_8VIMXG76e9KT9FWWbhYJTcd33hI8jXjnHQGJ7WCekFKhDvCeVrU5vbKD_6iAhsIYStlJlTfmHfH8O7s9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oD1baarerXcaujaVh5G-aQcmDy6H2gIywmV6VU5IvpZz3S88YdFZjPkarb4WyVEezR6EMgxwKynyOiKudGCehbPfEvkFqF4tx-_a96uH8RzLj3LnW5aZxbqcjAk3sAXOkCYPEBJNY2e8EdhEq4MMqltDayEjrz-4RurwL9PYKJdbX6_bO2kbOh0wKl1aeGsHo97jD_aNrAfwy03_fmGWJH3aF1FEE0jNHs3-NbXm1LtasdR6FrYVcIZbH4xSggYzRtEkT4tn2lZptVZC4akCF1epGgipCkFuW6qC3y8MKF60I4gfvsBKn_aR-8sVMob3cpiy8DuO9NBRrXxK1zqc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y20JRsmtZiqSN8R48LAyiDYqWcnuKlgneJEE43DqSVOjAtbEL0TKTM7wXVN88MqYkDJDYfmCFukQJVa_x3JN-Ve0Tv0aUGG0OavWQUBK5aQ_YSPoWft-Fm6lA5BHf7iddJ7168A_u8u7lrc_KJWMA9fPNiMOH9Umm2RQ-K2ao0yAjbCynjP_EvRLOr1lUVtNUkMv7-tsyrCNHPvDZ_Wcc0lIwVtRvfRWHFlOx10ZDjZGxdskfOhMYwfxZZ9qrV03pz_d_FX23WPj_jieuxaCz5hy5EgKUEqKhCKJrTE8dJClnBvSwbF2kL80qWD3JLtgrkF7fTz4A_74j5Wv9jIt8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=D2DTHkJztiPiCuE59kxh1hV_YwXlceekgciOlZSWy1ZAOhHQMDCzp8c59r9Pd-5Y4t4TPQnsmOGxotBA3VqBNlXWJNcOI1WkgJMovKIvIVShuofdpns6K_lpqokbSMNMKt3dx-IiFYYwariuoS959bgGGAygKV3JnVE-0ihuGlPeUSl_fZO0OVvyyPYmI_D8tQJZ2RteoJEUsncjD1z_6JMMGT-weSu7cYvrdPDcTTM1OV-3TYVzBBzkK4nxvmn7XFT1orJ3SlchvKdxYoW2N1AtmmduaRmBXGBwHkJ8ny5H8undWu1XDqAeCgxnFsxe-u5Vj54qInr1o1_FgvFJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=D2DTHkJztiPiCuE59kxh1hV_YwXlceekgciOlZSWy1ZAOhHQMDCzp8c59r9Pd-5Y4t4TPQnsmOGxotBA3VqBNlXWJNcOI1WkgJMovKIvIVShuofdpns6K_lpqokbSMNMKt3dx-IiFYYwariuoS959bgGGAygKV3JnVE-0ihuGlPeUSl_fZO0OVvyyPYmI_D8tQJZ2RteoJEUsncjD1z_6JMMGT-weSu7cYvrdPDcTTM1OV-3TYVzBBzkK4nxvmn7XFT1orJ3SlchvKdxYoW2N1AtmmduaRmBXGBwHkJ8ny5H8undWu1XDqAeCgxnFsxe-u5Vj54qInr1o1_FgvFJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=VubbO0tKP8DO8lcd9bLmDTF8M7BTlnH79idIDK9AnLVJXorVMEEQVfhpH0_MQSfDx-be2tNuoufjRDeswmkpj3qwE-4C8veTGV5CGJO4wX7-zuPm8HtoPjT0N1aH-MRODBUIn1vlr8ufApc_hE8tCk1OeZwp0BjU-UHBeioGBtFEP54q5jYlS0bo4F_b5kk35CIQtb8z8FLwpcDuJMqBWjKRAfBIaNyaTpvwCnHvzD6P8sqbXK12VPaCAjvawjILP6RwHZ_TI_MeYhdOHIWcIcOcULLM7NkGRYWui3faM7B-wF30b5Umuw8E7Ol6_d5LmBkteO8ohRbf1BXBHVd8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=VubbO0tKP8DO8lcd9bLmDTF8M7BTlnH79idIDK9AnLVJXorVMEEQVfhpH0_MQSfDx-be2tNuoufjRDeswmkpj3qwE-4C8veTGV5CGJO4wX7-zuPm8HtoPjT0N1aH-MRODBUIn1vlr8ufApc_hE8tCk1OeZwp0BjU-UHBeioGBtFEP54q5jYlS0bo4F_b5kk35CIQtb8z8FLwpcDuJMqBWjKRAfBIaNyaTpvwCnHvzD6P8sqbXK12VPaCAjvawjILP6RwHZ_TI_MeYhdOHIWcIcOcULLM7NkGRYWui3faM7B-wF30b5Umuw8E7Ol6_d5LmBkteO8ohRbf1BXBHVd8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq-XwCyPJ35sIQDPuZ52dyKAygNXHe_0XJjOygYe3Y0vbM_OE-u4vTLmtjOx65g1KCikZXLq3Hm2sqXBwUJyLfOACsVzmMr5Ayzg7QaKwJ1jo0DPG2KTnFJS95F2oNC3VMAqY_EKsRcwsQwUigO7hunWI9p993ZeQD2efAGDrrm47c250AIELdHYdAN13awxT5yRuQIzFMz_gcwXEE3UgPSYrXpbfe7juokeoL-LYfOiqyUGn5K4mSI5JpuE3TkihWHAa90rUzugELqGAb58hvu3FfXcF-_on8e7gGZ2Iojv1jO53OfFr6ZmYZ-4hVvSwiIbpf-vMLf2xTbkbXYXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvJxARA_c10tAv351EAWFrl84hQJ4QVf6x8m1qgO5Ztx5TyYCb5zvM8diX-pL8C7zEnr1ZX_vc4_i8oeNNH1DLPJCXzlkEDk3xHw2RjP0e8GiFxyxVaZX9PlAZFyTXZ4r9n0lAt7MKK6HGLcu90Zs5CIxfxyWSEfnGdU7eyYmm-vhpRFrc2jPxy4WgmeMpTOHFRvaeoRAcb5y11cWxo2i9fqXQ8MbBOh2Qev5iOOO5ZhSMLgKo2HjPQZVHhgtaguz-1c-1C8WwTYj-7EjsZAvedSBbLi91Vn_x4iMv6MnW0DZY_4Ayx1GporPU3CD8fo8-NCLILDpVXpz4l7k7Ay2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=snhBlkGgHstUY4N5PatvrO-jjN6_zLffDKw44XDneKlspb7G8ntMCVIT4YxjQEedju4YEAPdaoqfgiYzi5o2H2l9MvrE9i3j42bxQPeunoE-rfvg5yog5Y20Bbz-5TLNeZUs8WKbx7o8YmX1CmlRZ96FW3l8lZereC7O04n-NCjcKRLUbMBWfWSusWZqJ4Cs69UOwu58x1DcxFagHumhe70ItCnS7XU7WZ-Zcr8tWGzz50bL3RvLK6JJ4lBJycmxKPmkebuWtdc48pOPyHi3TmkSYaFFgZUL4OkOAjRJgvB7xTYY03jYfx-4YmpKsNtYGbEnJITxK8g_Q6YYc1HLYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=snhBlkGgHstUY4N5PatvrO-jjN6_zLffDKw44XDneKlspb7G8ntMCVIT4YxjQEedju4YEAPdaoqfgiYzi5o2H2l9MvrE9i3j42bxQPeunoE-rfvg5yog5Y20Bbz-5TLNeZUs8WKbx7o8YmX1CmlRZ96FW3l8lZereC7O04n-NCjcKRLUbMBWfWSusWZqJ4Cs69UOwu58x1DcxFagHumhe70ItCnS7XU7WZ-Zcr8tWGzz50bL3RvLK6JJ4lBJycmxKPmkebuWtdc48pOPyHi3TmkSYaFFgZUL4OkOAjRJgvB7xTYY03jYfx-4YmpKsNtYGbEnJITxK8g_Q6YYc1HLYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=UfISZ-AaMb8TyXgNFGYxaYoOGjhrKKxTY7k5Hw-y_1yfkoXcbry7KIRVSno1BIlSEEu8njmIGvbpG6hAgOfaWDHXW6hNM6o3uKAmul1XvYIAU9-ShSIouV-VXkfrDQAx7x8mj85VTz8QI2NnX8lOxHzJoMXYQOrLE6kK4c2CAXkE2iwQw-unQjrZ1KhY3LXzmjm-4r5pzAD23kbckzLcCMjTf_eDfV3xB2tUTy_LbWU9vB4NgTVwREiaGFxAPUnUmTwoGn5gE16S_kxI_qckgqXgcEG5DzshkUohg6znUFPffZBxSFOv_YcUiLqbjz1k8rkXx1fvmKz1gNF0PLiFaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=UfISZ-AaMb8TyXgNFGYxaYoOGjhrKKxTY7k5Hw-y_1yfkoXcbry7KIRVSno1BIlSEEu8njmIGvbpG6hAgOfaWDHXW6hNM6o3uKAmul1XvYIAU9-ShSIouV-VXkfrDQAx7x8mj85VTz8QI2NnX8lOxHzJoMXYQOrLE6kK4c2CAXkE2iwQw-unQjrZ1KhY3LXzmjm-4r5pzAD23kbckzLcCMjTf_eDfV3xB2tUTy_LbWU9vB4NgTVwREiaGFxAPUnUmTwoGn5gE16S_kxI_qckgqXgcEG5DzshkUohg6znUFPffZBxSFOv_YcUiLqbjz1k8rkXx1fvmKz1gNF0PLiFaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTufKbZEZ9YRNcqxNsiwj5VVQuJ1_11SL8L9Cuc4wSewIlThuPshyaYDR_7aYSXSlpm83pQh9fza9pOkwc9g7gYvIE2K-JeeTQdH3lYMYLJni5rCy7Xufp-D_42CGopL4r4XFL_3ZZTTuY2CrIc8h0uyql_sxCAWM-IwkmKIS_hApApB1mbDbcJebQ3T1pMrOeusviluKBettExKyjq7zQG1zjDnqP1aTW0dW_0x3fcetIcrFQ5qa1DN40ghLXk4010I4O6ajhvwac564URbHXvddz_pACfAARCyw7DLwiii-xFzGyKqDIKETf5FY-S1FbFKUY9sAnl-M9KbvQDuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK_lWEX5czMwF0W2WZPcgF6xt9lCJSWsYUj2T75czbE-X1ap153C_7sdQeGvWWnLbVnk7CKO6B_I2xYooRTkgxnrcBWV7v-mV7o9ylNhjk573LXooqBpLPlueIKUd6XonNBGOQCdKdgSXLa2PgFUj7_7DrzOaAyvlU4mtnumxLvmU2QTjriHgw_STKoP8DJJpyCJvTftWzO03KtPLXnZPfwKjcob54C-mObzPUkT_joyjV2a8q3DH3pnNaqadaqNQS7gLGdQBt6MqbGtKZrI_Ot2Zja0E9GBI9aKnO9ZMxIlCCn6ouhtP-W7Qfa4_kVfvFrX78S-zJOaoz7ImcMu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn3NvjlyRVThwzIO1gSYTKP-qII29vXnli3wqu7EHZ7SsYhOAfH7nmr8WgMgytlHedEXgzYD6KMvJykREWoHQn2ejMcvSYpPhKstrijJBR88TJxrG4qCzQdsZgR-yXeALX66Mk0fSP6y81Uu0zu_fuJ2GlTwmRYKivrinMJWDG_JnXq66JDpOnLAhfTEyxv3qe-armlq_3Fp-Uhenz8OLRyO4cDlLzBMi_pQP0nE55TB3PxeXZq6gNwozDPqIssrA0uVlALej4ghxdQ0er0ulYxNkW3EsN3elzkdYHdeGkmMbpZlgVGaFXXDR4IuI5rDz1unod3vVNGvbI-kjHiT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
