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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 21:31:18</div>
<hr>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4enV613tviTkG1rNbjW-QfEtzvRpR0pgJoXqX_IVFEyP8R5T_D6tz8h0kvsMCb2JNvCXf2gm6ocdUDG5dnRnpQ4_kwByLFaSu-wTHIVkOR5Ge5Q2wC9ouSqiIKVjXJBMQOH2ThE8-SGY5pQdcHGYgyhNTZnCBdyCLGs3bhv3TEQD446ANYlg6wM5lXawBb3NKwn3gAyldxcuknQ4DhLEKjWdQb2IMdFM1xXV8pdhs_mMb-_EzTf-1YqC6AqW43K16amu2i1kfWQGgH3CtrnQpU5J_hUpoCRPn0XapqoSzyyuMQGqV_7OCWZdpjXSRhvArbQdh9xK69nKF6_9Ovnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7yIxMOQ0NST0SzWnC7K_pSJcuMFM7DiF5cDv1AInSrH0AIEd6sMUcbdW7ukIaFnLKIS3pgwSb4wDBc4JqpmTHMW49IDxsn1VGcvmKW2GlQVHQ5XOg5acIJZuiZt1cvNmE7nu4oDhsiDeUkXPIkKRKunBeTqUVQj_mhnqdcGELi_gKDikv0aghaITHho7FV6JlRi-Ft8sTkrlgAl3Vsrl-LoLDWRdw036RMBuExmIxVVJST8qR_OljmUpLPZU5D3ZHvHEHX_DvV5MoUeX9EhO5qEvAvMTSjGg7Xu4iP6x5Lzffa_-J84r10VN1E2rkrZUgXhgbA-Ug1UXs06uXHCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqX8FribtVpU4_08FW4wP9OmxIMZB0UmpWEZwn2dUBhsRCVEZHWez1XJ2-ZzUKptfXuysng0CEFUAcxNqkn0ZsfGHRbLqfBsmGL33kM9UYfnLgeT1MLN1CprusUYUp6x0Z02vPbsvnIHd5JTklEpRi5lefQ3B1fzPuLYyyprJ6r9gF2PyTgd9GgkmlLLNS56J01l1ZbjawVloynONtUQ0r9tJPh5HgMt47xxDKENGp3G7LK1x4llyVV-qxyQnTLjgB_SmnPt0mkyG_QH-YBM8Xej7JMIXrXkex-4EwlgnrcQk_RJpqxiHa5ms0pU4WVS3EdfvEjESZYP1UN0yZS1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBBGY5IQaxH91IgX-1umuzHXc6j3FqdahWwbWpakKuCpQagbQZDBn9qiAD2kTfLLC-O1_3ZpqVeL4tca3qRY3H3JY92CJH99qJTqQEgBuaocLv8nbrdxkl9eQmNBIPTwXhGjZyzIzkKcUdBjYq4Q1GgyWg0XBv9TnI6g11nc0Wk-FwK2KC0PaXt987DUvgLdPh_1n8E48Z6rHPU0a3LFYNyT9yUyhecYnCyLdfunjL-I6b-r99WJRXHIUmbincFunXUzKjqcBJrwDD7iKJ9dHRv3-PEdSPOQvCSQWBSmESZHvvbotiykZ7HE21_Ur1kT1csoQVPvU5WkLUrt5R3zLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRUAyAzoDb05wyBhJnXVYKOivp7ycAlDZiHoX8Z9emv9-IXk5QaVjJCU8k3MJifo76LVQchAZj-KyXJQ2fjKAnTdj52THv79j6YNPvCZmJzSBEBK03WvSe-FVQl0PmcITU0rXWdXl_BXlf8akY5_ITySI7dqV1-pSAjM5IsOHWipBPcsyQ7Xd2JoQBmFUfUcPraJ7r59NuOxa1kcHIaPnB6EnPhhs2ZZ0wEBLf8YtOM6_1O_op4IjqehoGjjndfoQJJqWfN58Igar48ww5LYXcJS3JVYilp5Pkz9gH8_8EDoTXuhwjg4wUH1hiVchWLrW0ohWcTPCWTuBwsUtNJCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-KDG06Q8oaOI1p3w8btIzBUKCZpncZUppE_hBK2NC3bRCQvVVdyeXdfgsHguyZQq8fy-lQoollrVZP8Gkb5npKf7Fgnw0u7rgTrW9DeUJ60N79_wUEAf7NpoNWGJs5sFJUkIbtVM9ZCK_rT2rsYhmwFubd8q_2yk4wKuEB9zxjaEFIYe0PvhHGKOxwzPiR3wKbVKJxqa1Vkn6HXwhWWNHw5OHZIAKZKmTG4SZTBzaSkq-DekBuaD5cmQpLafwiWo_BZv5iH_m-NxGbmU5TxjkiJI1Vu6DkduDWGQbrf3JoHnYSvJiGebkmZoPHLBRFGTabSC-BCh18C21PsTjm_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxQLDfDk1HfGjuejyLWK2z_SKUVMUcpW4gIQUY0ulbQlSNw1Grg6138N9muD5WjF9m_nkKttSViYH6hAI0fDlowyjG27ylQRrV4QoHKDCMsQfCF_yAP9RlJ-bwLsvuankLuspbt8TACBDRfgp8C_22oEguMHE_5eHaFGTxfJRt47evVkQazvLSmlze02tmzJ8VoEvVmNmfbPtyLThMpE3eW4yJoknu9qwAtQytuItbqlU6VcojS_mrRcMHclCsQ3stHxWmk0tBloAbs_mUI92Or59A744QsIFMfJMj25QbjdX6J1BVE3u1H3JUpyWkK7mWP5hR1R-Y5L7i7IGcOiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWQ9RaMKFObftc4S5JZK5sWHIWQFUqQx6pQruIYT6QpKfNEbcREhPKZT__tNGECTZJa9mvgZYo8JkQIxIRXGkwx7hhsjKFZ-w1y5qv0lxxvekIIDSoVjrIN9lsW4GoGlz3NEsb8_coS_sUc7LKKYOyBt-NSsYeTh2KoShJX5HAs3roZLXIzLkhimhr4fJPO1ba0RNxIkv0nsFP-SGHkykpkaZoyHWe6RZKmleArd4ag95tNFV7EoPa-deABK8Vvqst9q5ZXuYNHxwMY5zJz096wahCMXWzCAwtWhWLU0KlOvXIq5nCDsC_vNV9CnwdT8Vv84DZQspT7gndoyiaB7FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAFcWJRJYE_2CCzNKCmM8r7t1zSbtSXjBAGBMTJyfjzrSouAS4OXtAUes__tktPp6J9_64QIEWELROK52c5GErSi7Feu9S6N4S-jTa1DDepQhAZcsJepExzCJ8aBU04_6EKNYKTmErYUihIMg9pOt9z92FgTnXsqPXRr52wZ_549g6JdMqZvrXpjuFjYsrNv6OFuWhAkNHzckiDR1iEhd4oJejn7TFSQsU3CnNyLG3NxHyxcdnNnq_nfaSDN1nDKhWVfEEZA29iHGKw8JI21nH-GKVrJJ-UcKGVJdZEVQ9n8Yi8IEBMZdBymnk9Bh5rXtspuSiRo0VumsxLhdpKWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=nhWwWH4If9IDetXOWNpm2z4u4SG_NxNpvv_bWSfC7ZpVqnEr5JrbI0fRhY4e0VfZBDmJmciV2d2yKfyliRr0vwjm4bbE9GHAsYoatZSxh4cSEH-reDxOQ82vzxpfaltszaSpOtPSBTR3ZKNT2o3lQzFhQQBJpF7WL1acnRwmAp8NY-Zxf3tNKQKQlyZlzI8OBWON8KvfSNNHWkcu1lVQqCwQJ5z48UiqJYyWEs5xP9jVUG1SfCEmtO71uj-IsLOMbFEfci5vN4_wFaKp_GIL8X1zAm3Qsi4Kip0Oyi8BGgxeXqAsDf2t7cVtIiv6QknlCxpBf-JB7_O7Yec5tEKdyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=nhWwWH4If9IDetXOWNpm2z4u4SG_NxNpvv_bWSfC7ZpVqnEr5JrbI0fRhY4e0VfZBDmJmciV2d2yKfyliRr0vwjm4bbE9GHAsYoatZSxh4cSEH-reDxOQ82vzxpfaltszaSpOtPSBTR3ZKNT2o3lQzFhQQBJpF7WL1acnRwmAp8NY-Zxf3tNKQKQlyZlzI8OBWON8KvfSNNHWkcu1lVQqCwQJ5z48UiqJYyWEs5xP9jVUG1SfCEmtO71uj-IsLOMbFEfci5vN4_wFaKp_GIL8X1zAm3Qsi4Kip0Oyi8BGgxeXqAsDf2t7cVtIiv6QknlCxpBf-JB7_O7Yec5tEKdyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SM3pBrmaV7rOUtPhzJ5jAPyIKgrMWMfzB-Mpjndj-J_klc9LPoF76qBkqHoxHpMbvvhLyB87Tn0kJdoQBYrkp3CmuNaXHqNuvTqxD5PhfLgFNYWhr55qL1ONxsJHDICV2kBlbRvV4tlTJG0D7bWqDPwIXjT99FlNJMYfCXj7BrvPRL_TSIqZbj7LzsU0Kp-AoMLDDaweS0Z7sOG61KLnQ2tm6la8VPDMLrfBSJRyb7x4_dVUSJaJ7ZzwKrp30RwbbL48l8hY0lxeEmdQlYRsaWwpCmyQp-v1JeuehYQat9TSXiLHfUV__VtbbIHzcB6TPudy8oQCU3vDc8j77Hwq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd12tsPxQ_2Fbngy9PhVu-8A6MNrVoDR0D0-5KWF-vUJf06vBNZn9G4eXEwuawBcfGs3guuEEgMycuDsDn0K01wIYQ5Ppq6eQajs33H6VQ69nRqANuARLsF614xn5KPIZnsGD8KiaZTtTwORv7ObFI4Qg0oC6L2ubro7aF3Qhu4MvGgp7L2v8Gbr9kIcwamwyPZNtFlID3tsIpGdB0B6h30cA10cZB1l9UaFyaVbdY4s7OvhpLqrAhlNrVLhw8YGNmXNQCgxbo58dT52PBaEk-fZYj0eWDrcq5jLDnXXigTPKK6vt8dtg3_4sq3ldm3qp_PvYQEy0U3d9kFJZyL_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F411UyYP8Vl1328AK0x7kU79LGHOA_uk1FluS0vMKOOzxXWggoAGbTfTAP1Hz-vcBvHmUxwCk4cBJlREdlbQjcKp9zLoHfPYxTIMlZiuqVQps72F_2QGl1JZAUaINZv5oaNneSmSNWa6D6C2iDdEggbvecjDb0F4uCaQwIMyNW0so8we_rtl3q8Kuk-h8CuEA6GFJILMCTerI796ay8r3Cdu9T8WRvmbIKa4rOlQ03DsLKRn1qdvQdKYLIu_elQn8mBV963b0Rn-ugrFw5JW--SW1DkUVUACVCdcj-XyvAgCUsbOLdbIADhttFoffsaHn6v1qgUxPpi4ttc1eqJPDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs6eFGVo3ZpUZU_wYpcU1vi6b52-Mi4QXw63ISGaCSTl078SPDJ1uu4ioK5wtIBAXsjnHdCV_L9a-zcpBJHkJ10frURaticxDVFgSzS81pW2D2q02iEZ0nhR-RrM96dFDd27U6DBSMh8P6oIZPJWYuO7L1Swx4SWxi_4hCIpjgTPTBcqPy_9kIuxSZVd4rZbKU96R6CmZX3Ra_bJ-sU35gBY8Ja50Bn5sEHvC-jxaKZjSW5KwpsXOsPppoK_nDzmUC5GL4YAkTVzEQ0SfZzS3DQpNhzoHy8OrYDi659wWHZweDqxIatXIM8fC76udVCVHhCeA-WBM12ZTUiG6RE0og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muXxC2UhNFzEP5KB0IEHRSknYL1WwSyvLE8oncRaGknnpylzcrq_4HdftFu0W_dsvTlZUI71O_MXhCuQQVPi7LR4Ua09bpQAgNQ-u9qC-5TIona31xxV1RWKZ4CrmWyov_4HhHFQUnnLGRG77eGhQWKDD7gOtguDk3_kcxIyD65KE5Kr1FQM_nQZYLVM-7Mr5uLmGRa9z089s0-Hcma1nWeaAhzNdPHewP4sZCP3tM9vOI_vP8ribahrzTvFFC1rChv26D5-SK_f5_0MDxPTzvDy4WHp3tsAl3OQ5vH-UYZ74rLeIYjHDuY9jFBXxPP5yKDBRbEC8p1FQj_LtK2geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2Md4AJtKROJG8wf-aKpWX8yERNk0CkRdpaOy5N0H-TLTPCyUhhpR67lOrOhMeVuKBP0ctcqtfq-u37lon-Rb_gcZOdXVtHPmW2zQ9K-Odfc4taKF6ksGU4vjCAfkSjMMHtP-HHZ_K47RhUqmGqJjm_He5pCbmYa25FqBmbQ-kwhavAJbFWzpYcNIJe98XhYjAdxhZH_TH1RgaghhcCdRVFgyoipKOcFOoENAL8ugX14-pVTVs3G1w3UkirAKy0fE45_-RYe_m1oKZK-qimxGkpMGm83r5E6mitTjdUPet6MWQEG1-A0hBZYDteUEhVfE-YvyU6pOUvSIOaCQFB4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpb5YLdlayqawbn3iyOORiZJ6Yoz1D0MW_NzoeKCUALdmGS_JivCmV4DxKsObbFaLcS1Kw773QD88oNiVzAPVG2og8ayISHWr7XVZBn3ks4LiRaH2aGrNvCNmkjreAV-JpQkek9CtY2Nk_bPQyFl4lCKCZQCDjMshZFSNDwLnvtbeVJcUHCOb0SdYDedINDy9KiiwfbofMaS_qik1IJl5Da6H-a3cTBedX10NVGDnDowA-n-thJKtp4JxrFMBVtn80MXMvqD7h_4Jm_JGzKQsOwIIhx6EJVmjRigym3BDdE1LDbOl_HOiVgQJ7LsGpeKJRsigKsIKglvz97H6s52dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4Q1ZGw4hl6YJNHjjSrru6-Y_pC79q-AOvXiC1Kg-ga068Hy5rnj6ilEVLPVjTGgjGtkGeW3FM2ODC1Q9J0KfdZVZTmXViL4Brucgg73lM4fyVwDbNepvyjvAN5yxEmNMv_OI6G5ntWSXUCOLu5jjOJZ1J2zQvRq7p_Y18LWeY9t_-GQhux1tNpkA6YVHfFuKZNE3DJj6n4LK0dqvTzaLDPs3xcllB4vT-D7OcqMXjgXTOBBE2e02ZOdk41JXoVERXxJzx_Eydy3w6AxF8uSa60tSgpXHuP0JPVuz7M8-ZYoJc0shAU5vSO8PW55WHWK239yyVAa0LY9v1Mamvfwkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=CG1NepWazmwq9yRKbUV8yPbsI6PVBbH6U1B5mkfediHzQIzTjNTjgGTbXb4sDKNapsaD56r4z6jhYHR1uU61bPPphiEJOjub5sYZPH13v7y8Rdy3pMhyS2ix3G3BCPo0g1NMmn5a8JXi6VWdudVrbkN7AV-lMw4qcvre6xMEd-cw9bIrMQSn-5eCCg0KVAIFY1mjgLnZ5EYP13maVgIeivkJLxz2QERb81iddEDRvMtl3DeXMek92xZpftZG3a_IjErl9YKk9FPzDtOiz3CI1gb0cUbkDpSx_y1AjhNrhHtEuZQRJh_VpoEueHDpz4E6xnHiheGs1YhfaffdQkszCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=CG1NepWazmwq9yRKbUV8yPbsI6PVBbH6U1B5mkfediHzQIzTjNTjgGTbXb4sDKNapsaD56r4z6jhYHR1uU61bPPphiEJOjub5sYZPH13v7y8Rdy3pMhyS2ix3G3BCPo0g1NMmn5a8JXi6VWdudVrbkN7AV-lMw4qcvre6xMEd-cw9bIrMQSn-5eCCg0KVAIFY1mjgLnZ5EYP13maVgIeivkJLxz2QERb81iddEDRvMtl3DeXMek92xZpftZG3a_IjErl9YKk9FPzDtOiz3CI1gb0cUbkDpSx_y1AjhNrhHtEuZQRJh_VpoEueHDpz4E6xnHiheGs1YhfaffdQkszCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5anEiwJUkPfVJuwF2qZcrrEz-JP4-yAwiGjfAFpTs3aS1LBMUSg3xkfgAC8xDQTWDMiswh2uLlbbxPQOuEyyjqrCQyIq3-XX9EjmNII4Lc9uWC2yokDWYyx-YBeC4eIDx5T7KhRtGMJFJ-K1-q16cp-2EbLCeig1_BpOtu6AZgjXnLfQx8z-9qFvfYr40DZm-_LHnisVtFvw4lSfoUeiDA9gQGZgGFLWEg-YJ3kZ_P_erCLJkjt47Lcr5YyEuMGFPnqalzH93sRba36L_WpA_Wj25aivNdDeHY35zv0Co17onnPHmnMMUktJP9QOHIiuybEOO0NcfgqBKa68k6V5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVTyWqYLmcIQjTzAwZe2g4mDSuzpIJ4TRuX1PEgIhlFpkVUxsJfTdxW9K5iP7r8PBos1zaXnH2KmNXcgkjjh4rkia9RV2_HyI66676Syfl0rpE07qo0e8Cxrtg3V_kllGd6jtdqU2Z04wo7V87-qo39g8uKvLi9unWypqpFSZkS9i5U7PJ2IKfVxSAVNkBM4Ac4rwXtM2Xaxr4_ZmlEUjiq790z2no7wUZPKnB8ltOIPXAqHDvdXi3GIH4BHoeOtaSNeXu41K3pmFAajEnkGAV6KpzQyMczt-CjoLhzT8qGJdaswApXIjQxjnXymP6q_7a0iRM-m3EhIfdXXmqBTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHsVufnbO17UrZiix-DEjERq0Z_OzoKIYgwOh0udwfVaC6RSIx-bygdiWGRQQYqFOUPSVtWHmfk1HsaEbG0TRbVGrJvW3yBStquu8gGQEhKxp3ld-XLsoh5A8gzPo75N9ppv3K-0OHf1mgAgPQZx4a8Twt7WmlPt66gE50sOLC3GYU3Im8dncb8pnDziZj0M2scBDErNobVueExX56PZ2rSYfMqxX47fNF37BDS3HobFsMormPUbkHAZdEGfDwAbiVRA7lSTFoFzGPUI0YwhwDyOJap7cSQz81GR4Qmzm7P5qEIRkm0TceXUpEqfFIqBbYzgV8paVx4_avvA2qkdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De1ZoDudlJTYZf9bSy8Q-p3sgQcxbpW-XceHHAokhqqbkd_zzOS6QpeKfqC2dfhEeQ8nN3H4TydW93G5VxX14BLEtRHgOXP-f2Mqg0I-HWsZg4D5zkGwFswUPBAufZkl451g60CQID94O8oObPcMoE24LoIPEL8XK4dtaobauk_Gxiy_ycv4ncBcAM4fTaOVbeoZcl0lpUc5pMY10vZP5YTnXVuFKBCcGVWaY7K26gU-ogVFOIDcv14II6e4oGbZkm6SFFLl1peG-xgCljAhYff-zOmQvHfIh1jwY_MgLV1kyK6f1i2hB-cz6v-vVYiHcd99H0HAALIZjkB7_I3z0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsWQoWqAsTa236Nb5Ix4AQ4BDQPVeRy5GSbXiff2EEzFT0uaVUNtNE3aILCy2g-iLUhu8GciS9dWH8uR1Yxl9cHPZO-9NWmZKF4hBTCHQOEGX-5J0qTdCwzVBtfy3zuO3Oh-YigqmSAwWC2dU1SZsGqfDydTp7j0hYoZiR5hs6NXOxU1Nfx-Pf4nBnUyjmQOGh5xws6PgIQy2z8QGON-X_PJTYpV2ska7hvghEP0zIQgLjrHhSMrmZMDief7kQlOo-O89A4KdWo3v6bqrRxClO_GX4fcjh6Q_3cXHEngP-3l18y9j3ySrLyGu4jG71kOFdA1OmMO1YDmuRKQ2UkDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehFfdaVirZK2wv4Xfcv9K89ESemzO4co_yivluZ4LQgXJD_aJmjk2xHCqe9yDfCF3U3Z8tI8n2YTaOnPRt7rHDyyYTxX4xlwdt5ffX2XREbaV0V-gNhFU2bxGklz1L7nLbq6st8c4E_0NSGC7JQ9O-uqLOaC7LRDR-vsqJVNOKZjcCXg4a1xaGqg8S6hF_71tTfd5MpSMGoAIz6hfma2vWescbHbjjSTCHDZIIT6E1_OC4wrNMd8nErxKyp2sCNw1PjWQwLqHIn1IolmDdb74DBpnOhAMEpYMSpvJbZEDBbEi-VsXKs7N2du3DIVN2u6vkvsxDurAeuiRNUYemLxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoIp2UD1AMdhGH-io9zAsqP9gSkzn0f99YkkY7jG-GL9wFnfYRNujKkBRQ_kxaRUmtaRMSBsFscSA_Evu2C1xP17TRnBUF3mjqKPTm_IpupeH9iWzmMrYb9RQUSEuTXE0408fNQDcmNZQop7qG57jyoHFH3YECXQAf6Qz5xBMlOcZkHXyA8fhwX227NjWYMSmv-EOXC-LS7fawtmIA7KqSr_26SXf6CmuARmjdRf5RgCUFL1X23YMUfoocbGiA21d2HnEI9-69X1s39U0GoIkHb7RsoOgU55EyA9sprEJVTIH9q6q2UHtSKJwyyU00C7h4TDX7lm9dA84dhYgfCgQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=FUiL73qRxBgaZ1YtuMMTcSEDI04Ec6H6X1Pvs7YwPBMf077k381RHwosmS94fK1i862KhtbcUsWubDNwZmfmhndUAGe1Y9ZvVHhRkdix_9n4O9zyrcBqAnmflNYHfX50foawTJfN1Vwgv-ShWd9Uo4qPC3gquxcLn_fSOQMQuC6oRy_enSlebD8PXOPy2_Zh8j8vVXyhSWdW-EOaPRlGqv_XIeeENec7PH89YJtijGossrk9pKLO9RhZRRodQCp3PRHlI6i9-b80THTg9APRMZn_RQoBXia6IZXV-S3d1S6AxGbIShpWjW10SyBUjABDoCr8h_w7nF1m0BXgb1we4wo_szK27Mu7obDt7Y4LRd73_z7tKqz3QrXWSTN89xCzyDDx63cEPPZ8lp0MEmfi_6PczFzmVDUNL9FPebWIa08BFqTqofeIZS3Oz7WYXWGh_2vHv5rAB6rlJdvesyfYxM5jhEa3qqZ6cTBawFJHC_ZWLqz-cOcQgDFcOep8lUnWDOa517MqZBacF2QCxVYrEHbE_vao9H_eP3Q7ziGycs14W2Ihw1tsY1rjumUCCvWEST6Y6WLYGNTMlPd3NY6KYsjwqFydlrYMOGDcM-oY930djwU1FHHmDr2gAQLFavCRjO2DlTK2ixOlptyMy8pGVlTRrQfcshTxJr_K6xWu1Yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=FUiL73qRxBgaZ1YtuMMTcSEDI04Ec6H6X1Pvs7YwPBMf077k381RHwosmS94fK1i862KhtbcUsWubDNwZmfmhndUAGe1Y9ZvVHhRkdix_9n4O9zyrcBqAnmflNYHfX50foawTJfN1Vwgv-ShWd9Uo4qPC3gquxcLn_fSOQMQuC6oRy_enSlebD8PXOPy2_Zh8j8vVXyhSWdW-EOaPRlGqv_XIeeENec7PH89YJtijGossrk9pKLO9RhZRRodQCp3PRHlI6i9-b80THTg9APRMZn_RQoBXia6IZXV-S3d1S6AxGbIShpWjW10SyBUjABDoCr8h_w7nF1m0BXgb1we4wo_szK27Mu7obDt7Y4LRd73_z7tKqz3QrXWSTN89xCzyDDx63cEPPZ8lp0MEmfi_6PczFzmVDUNL9FPebWIa08BFqTqofeIZS3Oz7WYXWGh_2vHv5rAB6rlJdvesyfYxM5jhEa3qqZ6cTBawFJHC_ZWLqz-cOcQgDFcOep8lUnWDOa517MqZBacF2QCxVYrEHbE_vao9H_eP3Q7ziGycs14W2Ihw1tsY1rjumUCCvWEST6Y6WLYGNTMlPd3NY6KYsjwqFydlrYMOGDcM-oY930djwU1FHHmDr2gAQLFavCRjO2DlTK2ixOlptyMy8pGVlTRrQfcshTxJr_K6xWu1Yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=qoOgfk7tAZ_mQ2ayXLxT9QQWWXCHNGjJJ9SOvpmnjDOrHqGznBaBYSqSoB-hBHVMu7woPvK7aaH2hJfoZ6BnCNmIu058DVuS4A4ANP7INFM3cK7MEz0pH1VWKqhWEr8Azz8ujgZkjkaEU0mJW1iDcs-vWeONDzmyV_fX2K6s6GZRn5Zqsufg5ExmHf-OvIuolPPsTquMgOYIQaROqqF_p6h2vI7x3NzPgbfW2uMNCXgnzwQQH4dArBYznRHaotyfuouQiOdPXcPW-TBNdmxSBEIPLzHOgA5crutubdgO9cO-Dvu1OTh8eVzievOkwCX4KY808EMT6d1yuFYQ_70y5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=qoOgfk7tAZ_mQ2ayXLxT9QQWWXCHNGjJJ9SOvpmnjDOrHqGznBaBYSqSoB-hBHVMu7woPvK7aaH2hJfoZ6BnCNmIu058DVuS4A4ANP7INFM3cK7MEz0pH1VWKqhWEr8Azz8ujgZkjkaEU0mJW1iDcs-vWeONDzmyV_fX2K6s6GZRn5Zqsufg5ExmHf-OvIuolPPsTquMgOYIQaROqqF_p6h2vI7x3NzPgbfW2uMNCXgnzwQQH4dArBYznRHaotyfuouQiOdPXcPW-TBNdmxSBEIPLzHOgA5crutubdgO9cO-Dvu1OTh8eVzievOkwCX4KY808EMT6d1yuFYQ_70y5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClZPIYZrb1vQNFK_2K2lsP4J8n5kTt9vXD78JSQM5kXnc0udM3KNRvoCinRy_otiZBueN3lpInXC9-xgtVKEhw3c8S_nolMXvD6AX4RSU0A6Gr3NpF-2ciU5nDpiUB8hsheOuRnFSgVmhTIp70moutX_HS28-lubIwl0tVs7h20TLZHXOOW7-D9hKJxSkBNePFTNLQiYeShZD_10T0RZLM8l6BiL8WcBHfQb9dgUO9TfPBh4knoZav7cBgJFBmtkD2Ui6xdINRJgFbHLGyTh903x_MZMhhg-IXH5V_XlNGs95ff6u0nPsOhXge3SzrrvNtSBCohEv-lmE3wTICN00w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ661grBVhoprcoCnkWXgOn0h6237_eGFHhxTF02G8nSfkYrj87C38UgmRzFYIUbfgDg8FVZGlk_8Mwwpj0tfp-0BbEywwMLVgFw151A60ZEWl980a8W_OZb8XDIG7Oo6k2fYX9OBsxQvm-kCbW-yXPhqXn75bmmTWtdNNGtGs2t9yKUAVRB3lR9dJM59BjoRnXk0v0QtJyUa5HNMOY1VeMmJbOAy3FNQoXc-_27W1qUtghmeLO5EIiZWhI_tNYoleBJa_AxSGrUqjbp3ndCRWSmoYRvUnueAv5t50Ytvy43U3qKtjt4qJz0uLiYjbyyZZqB9ksUIgwi5Za0owrLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=Ra8Zy6oKDn36ytcSEW7pT1rQXvWcRbE0jA-JnKyJ8YMea4cmmS7z1a8YW53BLjXlBvBmFLpl8NlSGcIO0Qei7BaB7OSbSipmrMkrcBFXiwVnS2RtwYUn0hq7FYdeHIpdE3K-NvgIRvrfnkqL1_l65ELtengbKnKv2WpJHMh6tJVCPZ29HgFip2DV0A80NYqvUUmoqwZr3Sid-UNQMomJihb0qO8Eks0IqlnbdlQ5abkLGa2_w1zVTiNiBSbCN56qs0Us_Yw7d39jMNKesrIvd5Eo-RE5kMHJgCiMgra9MJRCSQQK8ebOi9nt5PAgyOnUMkkvPDef0a1x4PmVSGEH5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=Ra8Zy6oKDn36ytcSEW7pT1rQXvWcRbE0jA-JnKyJ8YMea4cmmS7z1a8YW53BLjXlBvBmFLpl8NlSGcIO0Qei7BaB7OSbSipmrMkrcBFXiwVnS2RtwYUn0hq7FYdeHIpdE3K-NvgIRvrfnkqL1_l65ELtengbKnKv2WpJHMh6tJVCPZ29HgFip2DV0A80NYqvUUmoqwZr3Sid-UNQMomJihb0qO8Eks0IqlnbdlQ5abkLGa2_w1zVTiNiBSbCN56qs0Us_Yw7d39jMNKesrIvd5Eo-RE5kMHJgCiMgra9MJRCSQQK8ebOi9nt5PAgyOnUMkkvPDef0a1x4PmVSGEH5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEY7qmtigF_4kAtwHO9af7Dq7omZ5rLuDZt-gQnkRLo2UJGcZ6Kglx7O408jC5GREk8oyWQjhiR91pktQdDtFUf1VCs8V060T3zoudyFuT4RziUoqw1rsIw2kkIMR4DvtF_QGSVthQfYuG-KQi_6g1Iv_pfv5A_dd5Kf-ZGyHyF-1U0xf5begt2ACuphahSYCPACXFSYKU3ZuvanXCu2WY2S2LHsf1nwm4KtAUmR_O6NgmZgpdphCV1nZV8ycEnzh-z_z0J5vZ2ghRlun3GiWwVBT5Ji-apvO66mjRSF7hi1Kz48ugDf4JxAuCBoU1NK5bS0ddYxAEB9AheNvPwoPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuJ_FJUjUGXI9DtIrPJTxKeUhpbDO_y84A-Rgv9IQ48i78G_uFxm8sGcqwjnel8OWwJOIpEYh4VzGYaEsMrTiyvGq2Yd0ao-dA8zjUgJub36a4rIGMeUjJSJ6XUnXNuXNyzGRlpzCKgIh9sufW330kBrXKEFLJWBOUTFjKi5kywt7y1pbzMx2Jl7Wwc5phPZrCxVV-3lUF3v7h_FzMFUzV0ZAYeRPGyKat-mpmVI6g9voYjU0WpsjekUN-VmvHRgbA7FF0NiMqlvo7vyy95VPCmaWAzKHHT8ceQHyd-MDklvmt1CNcHyyRGPbQffptvFLyJKWxzT-4-EwoHq4z8lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNI4zawYDU-U8GKgEgFp4glrUKYeeJIM8mbVSkoLGFpeJZDp-zBbCt3eIGQXV1viJyEj5pz0IrxOeWJTRu92XH98LkwgQWkmAxhuQBkmDj-IrG33qs2D6hj9aRIh1vqcGkNx7OyG3x5FTCI_ggRi3w2kc5wFGo83AhEb8E4nE7gUP6f5ESLxy-HmZq0x1nVhc2AvV81ZA6ALc0egvJyux_bQxk-bT3dbpK6ECq4h6GFdTerSCHeFlKGZuuoDe7yXur65JbtSAMg1M0A2sshvTfIdKfoZNylqACHOQ451-IPXN5auwkAjyB7en6nMUHalE8gxu5k59reRX03w6-Veiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTODFbVFBQmDlNYZ9GEr1bG_fGg3lbvw-ZW2B3OkToSGh3DvmAu9ZyUuGtWB-OQrbw2trXtU_8WpWVkNzJAdRfufkq_9Pj4ntA_4OijEXaznjcdnU70GYE8YUIViPtKUIa0rY1a0BT3HUjNbDBmmVVXBxnTY8Z5QYm9C-68kjkAFD-kQUCtMkSnMwX4odniVKFn-58Kb9mW2n_zxJXELOSJUn6eLWejjy6t1jFS5YCif9y6lpjufTXJkufjC6Bs-vUS6CHfI8L263_tvpArmJBJFFbKu3-TA3Z3muUgsbSJNtU6sjcjKnBgTp_liM2p2FKlfhX30c-UzAaO1SHwVhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge88OlnEsfZAwvsEd4vhIMi1941hfj55Cl3412xmtTkBjZ6F9YkXiLNx1CusntXTyX-wVr0H67IHfZaP9MLmpnUUed-0PHuu2r8CI5e_bjgXMDgBSlKnrjbF6UGuubvYp1h6uoMmlR6Qr6QidPAxnyFrs9wI0WEXgDUaM_UilZPqkeW9VJ4HCrDOeTQsN3Cls4-nAdSbMe-3KXvdxX4x9mrKzq5a6bQZTA4kE4NbEKx1IIsMaspgUtXhOKHWYPmGpQLggDqtNJKmNJT5KGh8Ut2TS8Ix6QaTu2O5sV_lPnLZ6VoOxNMo-bBCUCBHjVclaPTL5X1IVnlO667o43wa6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5SfH2J-jZGu-q2vCWSOOH36ad_Dt5zZluNDuMt-U7FDQ3RHrbbl6NO9j75c67uHWuQOGrlX80Q1gR0lJVrBj-iQ1pXOROqR6GUm8XB98y54NA6LLQ4ZAkPYgELeQzs_R79-vy05h8Pd5t6Q-PND6YtT6-ey6AueyR4YjuAtQw3H8sA4GOd11mLd1byRGyB-Y4qmY-N4TTcDhe8FUigVhM_imjs6cANvBnYuCTMBy4dxNc1Y246TNTPYMRSK7j5JWIdYQV1LKYucIuYiK_StFGjlLBdDmQck3QgMFfRV4QVL083H4sia-dWjnZTtmG0mnXwTsIG8XuBXDPTp9BrYbUD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5SfH2J-jZGu-q2vCWSOOH36ad_Dt5zZluNDuMt-U7FDQ3RHrbbl6NO9j75c67uHWuQOGrlX80Q1gR0lJVrBj-iQ1pXOROqR6GUm8XB98y54NA6LLQ4ZAkPYgELeQzs_R79-vy05h8Pd5t6Q-PND6YtT6-ey6AueyR4YjuAtQw3H8sA4GOd11mLd1byRGyB-Y4qmY-N4TTcDhe8FUigVhM_imjs6cANvBnYuCTMBy4dxNc1Y246TNTPYMRSK7j5JWIdYQV1LKYucIuYiK_StFGjlLBdDmQck3QgMFfRV4QVL083H4sia-dWjnZTtmG0mnXwTsIG8XuBXDPTp9BrYbUD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=iUjCe8N5MAAK7ldhYaGVDeoz2SpEBxSc32nMbwXao87ivwnoQpkR-A1vqHxs0Ym8vJgXSrNIL_8ulGnLHZ1E17AKzOZrZ6PhqOUGC17JNAiKTv_DW8S_2BZSIa6xf3Iog3ebR_Y8-yzR0zq2tMlToSGwvjDmT4eT6BKwaGmWNKr8prxa_MKhS-_49DEVTpeQmd6guKRA-8F1qfrMbnCRE5VKnPJpacBqKrnNApeo_AU8plZWcP_amdhXXXCKGe5QnYRSeO9SbPegKyyK1Exy_G085gEXzAzdWAsrWT2m_hN8F6VP_GW13zFpWnLBlILA_GLadxQcZO5dabB1LFvZbQ4U_L2o3UKO0qnsv9e0kLmkNCihHyXZVy8-1F-3kYey9Ksd5HthJ2XRbt4HL3NY5fXWLhGCC1WlFEJJX2cSOYkhgwsJpHq_yeAz91vETYaWk41mmFMOFqL7gMuMCM0_i1msTFeY1vFUKsJF-Ygij1OkjGI5bhC_5mPqPWA0dVBhR_BqAYzvgdpt2CrIZwA9jLRVJ8D-g3e8d7CF6GkugGLwUsHtWypZn6D0AvJsXBc07N89HLo0jF8JwKVGir9IE9sRT-MI532bboljhDViLTNHkyre4yn3MTMXTP25l271a_5R-hrzt2lWQqHrJ-PL_ZiQT2Qwp9aOsBBOSGgSCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=iUjCe8N5MAAK7ldhYaGVDeoz2SpEBxSc32nMbwXao87ivwnoQpkR-A1vqHxs0Ym8vJgXSrNIL_8ulGnLHZ1E17AKzOZrZ6PhqOUGC17JNAiKTv_DW8S_2BZSIa6xf3Iog3ebR_Y8-yzR0zq2tMlToSGwvjDmT4eT6BKwaGmWNKr8prxa_MKhS-_49DEVTpeQmd6guKRA-8F1qfrMbnCRE5VKnPJpacBqKrnNApeo_AU8plZWcP_amdhXXXCKGe5QnYRSeO9SbPegKyyK1Exy_G085gEXzAzdWAsrWT2m_hN8F6VP_GW13zFpWnLBlILA_GLadxQcZO5dabB1LFvZbQ4U_L2o3UKO0qnsv9e0kLmkNCihHyXZVy8-1F-3kYey9Ksd5HthJ2XRbt4HL3NY5fXWLhGCC1WlFEJJX2cSOYkhgwsJpHq_yeAz91vETYaWk41mmFMOFqL7gMuMCM0_i1msTFeY1vFUKsJF-Ygij1OkjGI5bhC_5mPqPWA0dVBhR_BqAYzvgdpt2CrIZwA9jLRVJ8D-g3e8d7CF6GkugGLwUsHtWypZn6D0AvJsXBc07N89HLo0jF8JwKVGir9IE9sRT-MI532bboljhDViLTNHkyre4yn3MTMXTP25l271a_5R-hrzt2lWQqHrJ-PL_ZiQT2Qwp9aOsBBOSGgSCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Uq589T2RRwFuhKBL3h-xA36p0eFJgVtlcFdi5Qarf-IvRZxBqbAaZfC6qp3F9_dZE9A90bnHb43mjWg03XWckrQDs6s_qExl60vwMKHl4vXdxv_PYaXuWUZEQqgsEfrZgAcHCkr-XnnqN5uhRd9na5HfYvnmbVUazeAhcSrVKBssRmp1pKU31I4q6Y-CFQFowXT2GTHBdAF8q9JfRf90JYUXNo5MqFRg-j6zpFUEFJsW6F7Je8feVb6WW7QT_xjw6DLT1AI9N1NsdEMptBmUwuNi_Uz9XQckG_80Xt6ZH2T8jn1RwVVK0yJ8PqIbICadp55BolE5RQPeJVhXXnSYfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Uq589T2RRwFuhKBL3h-xA36p0eFJgVtlcFdi5Qarf-IvRZxBqbAaZfC6qp3F9_dZE9A90bnHb43mjWg03XWckrQDs6s_qExl60vwMKHl4vXdxv_PYaXuWUZEQqgsEfrZgAcHCkr-XnnqN5uhRd9na5HfYvnmbVUazeAhcSrVKBssRmp1pKU31I4q6Y-CFQFowXT2GTHBdAF8q9JfRf90JYUXNo5MqFRg-j6zpFUEFJsW6F7Je8feVb6WW7QT_xjw6DLT1AI9N1NsdEMptBmUwuNi_Uz9XQckG_80Xt6ZH2T8jn1RwVVK0yJ8PqIbICadp55BolE5RQPeJVhXXnSYfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juBQNlA-Vh4GYTELIlXNhBFKFMzL29sVpi4rtvJ4M-d6pUj0WLXV5pnrsXZ4e_Kc4pxR6iO3WarV-5i8DN5zL3w0pZ827aP9nPJwPzkcj3Dtl1MbIwEEdGffKb7BjWSCV4uQtWvSdvdsCx9OECzeI3HJsGM8QQOx7akGmY_CIadrOtbrJtBHsqdV9TIlEVDCUy1wQlVfpJM1umHLdyo-Civw3SWR9CXv6KAJe_VmP9-EpzIQ-X20UN_Ro0td7sA-3rTkUEeUPyO0yYGkAsZIT--MJOYekt4z8c-oXIfsaiInHmxhhy87qUSwyQLQJR2xG26pQFqERNl7CXIOFdSRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1IzP0sxTvTQG2tQuVH_IMsB8KuCMtImuLAgzOenk7gsSB_8JaCijelV6QhVBT7-xVmxzuKLQl1BFs-b75WWKeDEfZCmpt9DBC1fTW0hU-cBJYBnPwAkH2UmLN26Qg2y9e2Mtt3FADkvqrgh-OIzUgZ6gDVTbXc0VoCZR3VCcoaM304xmcC6vnWVMx1HFda8np0ilbh_CXuygx3bB2ep1ZmX2aQxeStpGFOOjoL-QbmtjcpET8QnnVLILTmINlmSVWm0ULWFWqs3BsuNW5lR2oMLrYyxAGqv_Kuz_A7_J6Z3nh6EppddzA-g3-XRY9Re-BJyVMXSPg65KUWuMIH6sA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=p_nh_aWFw104BJxIXFh1cVont02zE9Dw3x-IKJ6sLQ8oSmJCzevZlunvMbZ3phmOHmwGW7gN9KvNFvHGwdAeVaYQpjlF18fMmp4d_QgvJVArctxuEgWoAvvK8cUSCNxnK2zUgiKeQh4Gh9x1NgpNIHTaZbkovlbTx7t5fVJ0ExSas5nfpnFiTw5wtqHHdmqTSTkMvPPcLk6qU03A-H6k1ZR3VoJoo2zuke7ugiJDfEFnWL8EyzQFFpg6UyLXbiGo6MHMhhd2-zl3gwwFoP-WE1K3s-l_Lg8byv0NQ6eoSUYvklajT0rM8ktCD_dA32ncwpaAKIY0cFARnXgywdx2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=p_nh_aWFw104BJxIXFh1cVont02zE9Dw3x-IKJ6sLQ8oSmJCzevZlunvMbZ3phmOHmwGW7gN9KvNFvHGwdAeVaYQpjlF18fMmp4d_QgvJVArctxuEgWoAvvK8cUSCNxnK2zUgiKeQh4Gh9x1NgpNIHTaZbkovlbTx7t5fVJ0ExSas5nfpnFiTw5wtqHHdmqTSTkMvPPcLk6qU03A-H6k1ZR3VoJoo2zuke7ugiJDfEFnWL8EyzQFFpg6UyLXbiGo6MHMhhd2-zl3gwwFoP-WE1K3s-l_Lg8byv0NQ6eoSUYvklajT0rM8ktCD_dA32ncwpaAKIY0cFARnXgywdx2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnDgTIXVDS3mbCgG2USFlgngv09o7463H0nEybadMPPFpr-8J00PIsx4S-wULprzJ7MAzkaC6eBnM84laUB4FDul0q-GqHl1MPzIT49uUHGBke-MXt-vegnUTxK5mYAhW_4eyAfjX7f_b2ADU6mwx662fN5pWKgchcxWNHmXIEajYecb-jMVLq154XnA2LmKS7KF1EYt3dQTI70bABGw-ya_Osgi5ErhcPt7VZG8eRSitXuzYlo1FUcbvEUnxoRVraZdQ8t_cV4K0UY8r0C8tuXLhNvXmQH6_1x0QGfSxAQUN79cxah3LFnVXrJGivPbO57xn60_cWam0XQji3lelw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzfF_4onIUPLot3WU5oldIZ0tz36Qzm18UUXAf6_71NOJIXEMJpwgAJO-qQ98JUm3W_x9XFpo_t2k5-vOt5ik4-fNuzt1npTDvc-mLRNbRtG6_rBsLhFAxSA6RPzQnZ-IwGO29mtVn1Fdp_DM9VJ9EaUab74JIn-6rEyzmhdT5IMjCdIBu8GuRywPBP-Q4FD99j0oS6LgZ94hZMxepkqHVBFRgXrtFUHBH6vFEiU4JbP12qGewpHuHhKJmahk2_luBQlx_f2fKQaxAULJOrDDG4LlJbCOTjxo75Dtd919VnYYp_AodbKXVDql1wiws0bN_SymyCx17enoRV8gbdpOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=aOqzWDdJTRFfYz0HmOnBrFmRSO65lgP9WBYYKL4ZM1xE77bMmW66YWPS0h6rtwfqIylteXpZh30nvQRZ-nd7GJh5NKCp0IkiaQhBIq-un2xIG5UjQnNBEpvvqTaYiYjW5aNhegYkIPoteaQxttpogbGzugXcUpqXhKS3jyyjidTPun9ORVDkS2Nm5TKkqSDcv3CgS4_2xWuZqMxPAgI2RDHQOFNSkoo13xDNkq5unA3LhcJcB_r88dWMccVXvWIfCgFNpdlxQoQb5y2KHtlqBc3HQOoq1G9YqEYKmGbcO3XtOaGAWEOoVcCQ_S7C2bLmY5A4UOVqowlhGF8VW53bFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=aOqzWDdJTRFfYz0HmOnBrFmRSO65lgP9WBYYKL4ZM1xE77bMmW66YWPS0h6rtwfqIylteXpZh30nvQRZ-nd7GJh5NKCp0IkiaQhBIq-un2xIG5UjQnNBEpvvqTaYiYjW5aNhegYkIPoteaQxttpogbGzugXcUpqXhKS3jyyjidTPun9ORVDkS2Nm5TKkqSDcv3CgS4_2xWuZqMxPAgI2RDHQOFNSkoo13xDNkq5unA3LhcJcB_r88dWMccVXvWIfCgFNpdlxQoQb5y2KHtlqBc3HQOoq1G9YqEYKmGbcO3XtOaGAWEOoVcCQ_S7C2bLmY5A4UOVqowlhGF8VW53bFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=kIEXrEq0TrvpBuVBK2eDbVFnXsi3XeW4nhEVRA7_NYXg_DgsvlmWxoMOWhOJ48hXCHgRL2uNoCONfdaJIlWBsxVqRvfueBNm4YyekLZ0qXMjq7-z1ab2ZuSWN-S6lDYoIN4WBhjTSqMsH4QvTbdYj5GbMpKhJhQWp-x1NSK3ppwyQIKCaTyD5LqJPU9rrPbSs04QAmHlsXCKxhg549MwRopJ9-jGoi7IqPNPm15xCRkE6aUU_KIuhkpd9dNJOOiUtiZNp3YljJaMVW9A_v9E-Dz7klRR3Lzpg2RIbts1oWVQUST-7zmjGpU-EVyC2-W4oG1A2WS2inZdj1SiCs3jTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=kIEXrEq0TrvpBuVBK2eDbVFnXsi3XeW4nhEVRA7_NYXg_DgsvlmWxoMOWhOJ48hXCHgRL2uNoCONfdaJIlWBsxVqRvfueBNm4YyekLZ0qXMjq7-z1ab2ZuSWN-S6lDYoIN4WBhjTSqMsH4QvTbdYj5GbMpKhJhQWp-x1NSK3ppwyQIKCaTyD5LqJPU9rrPbSs04QAmHlsXCKxhg549MwRopJ9-jGoi7IqPNPm15xCRkE6aUU_KIuhkpd9dNJOOiUtiZNp3YljJaMVW9A_v9E-Dz7klRR3Lzpg2RIbts1oWVQUST-7zmjGpU-EVyC2-W4oG1A2WS2inZdj1SiCs3jTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBO7BhEaTJxI8w1J4sYO-qOodvgwP55O9dPnTKjRAJijVhbsLK3AnFa00Xfa3Y-l556g8sEwT6AKAKksKjZbcf12J5PutegHfhFkak8D1JM_7HNQBzNT0ODabJBodbaVLFR_dTfb0_QHjodt9oqGJ4lrba4S3MkeZzJJT5BvMqMxEXhOONgy3pvOFHnSvxREBBSO_ztGhhdgb1WJbiqd6CWxiORC98bQnL4YRyXJpe3fHKFISyhkBU1wp8LQ4Ey4cO0rIOpqJKUKQUa_Lk3H7kbc3gqrO9SEntVOR7ZXFGhcBoFf39rydfZwqbMIEMqu-j7xZWYyNs1G1l3JpRVOYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NejOP9DMc3Qr0OyYEB4-CD1FMwDnDUqc7AcI-5BPTB9WlEfBJo337PvbouCy-82CMlo1zWHjTW9YKH1GHIH3TOuCOqO98XfkyvenmG2K6JX-3fAXKq0orvEw5juckrAeYtTAhfYSuDV3hmSGqAYdG2U3bdYwoVI5GbdK6i83yIsxbDNomLQVfvtRP2VEelnsJl0XrZDl-4KTVMobceJX36ZZ-ev0VAd6sydfFNp6BR7mS1BkwskiligOZsrBZuDwudUrUDCagLqIaJ3YTYxP8U1D8mD31tI9Y5YCxaCe8sAZBQRo6Rc_e5PIIxjT2GCtFfpTiHrG77ZaBE_HS5xEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=gehu3LOGhC7KHr8M2HJ65y4FWX41s7bt_WuAcxseVXgsky-r0cezOofT2vK1tMDcbT8poGKZcRB76v5xioqXcXaTUQkNXBq52_t2P5n4vTnzQwXQhhcA0JMWAMfwbw-dMsIw0PKkgpv8TuflXSKlMQ9TwoenZ4bTvZfeZyxBoA_hCuBMG4Ve9b8mpPL0cAz_7agYtlzxWHbN1wChYYhfbfskKAdU3EasBg-MRXiXqWqTV7eXKnbmVx97VjTP1CY64AY6LgXPA9P_IUZ0gSztpqzXn0MaFL6GLxZbCx3HsKXszcD-XeSYLbiwP8J8iLf18QT18IJOAVUNDqTgH8xgfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=gehu3LOGhC7KHr8M2HJ65y4FWX41s7bt_WuAcxseVXgsky-r0cezOofT2vK1tMDcbT8poGKZcRB76v5xioqXcXaTUQkNXBq52_t2P5n4vTnzQwXQhhcA0JMWAMfwbw-dMsIw0PKkgpv8TuflXSKlMQ9TwoenZ4bTvZfeZyxBoA_hCuBMG4Ve9b8mpPL0cAz_7agYtlzxWHbN1wChYYhfbfskKAdU3EasBg-MRXiXqWqTV7eXKnbmVx97VjTP1CY64AY6LgXPA9P_IUZ0gSztpqzXn0MaFL6GLxZbCx3HsKXszcD-XeSYLbiwP8J8iLf18QT18IJOAVUNDqTgH8xgfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNX8w2Lv3MPtxpvNVRfHpE3mUi50qrbEo2gRK2GFGyTNZhjAkATr-VFyFgMDMSpZlzK5dTkmLGx6jIUsaQWk2MXjxCOqp79egqV49LVE8Ep6yvQcoQphmUKXzCDQZn8cDa4d8PbSUhb2AFX6GFc9NNZZPqNi8YLs5cTvvRu1HqcAgL0yZiEFXOrZaMVV9lbiGoUaftRh-H7XIqPl6vFaE569OYTKml09ACbh6ezISoxg2b8XdTXop2dJlUlR8evpfbcwr3JSGC2pDyLGM3o3djJzhyAIhrXlcBjVA34RPDOO3poyFh69izeJJX-KtoHe4YPM5Q2vOqn_4b7fzEc1Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiA6yY1tWhvB4e6ERe82oNyyhtPlcqG7q8erz6rQFxztD0YZ4hRWf6t56kJkIOZj5wG8WVGjbkG9eoeU3Hc960cPlFH_gP-DlVfgREWy4XbmENfoXp7_SvdH8s91_tm8pbaRO7dngGyS0J8VennwCqQ9mqefv-D2UurRqIUPfydQdl-6-659M3DY_lxAXYmfqxAw16-nTtCpf7DTAJarmRn_g_dycro4DzBLLyzSc1u088WY9Hepd1M4X9tHNgF_QHQwZN5dCNtESUWBI-dakW_EGRN6y6ZnNTqVtOI18l9nu1n93Z8CKWAZS-sCl_htTP02WaouG3bORsk4dT_WiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGIy7ImatU5XEXVlFfVW5CIZxDLThW7valrVhpHjcDqv5mYZ1LZuXwla4a9NZB2D0y0ynAgP-WhKbjV7ewe8GPZjepUIuJA7woaZDVHMPPBmNS3vp_HuNtrKrx3eTIMca4RLeEfge1ZLYk8hz89o44wqJb9Ro_sscmmp4V0GuQd2nUZUcaAJQPGt04gyQ-EB-L42scGlIqYXUT66C6xYU2rpp0pxSKT2hlBl6wF9WNSyiAPvoa49CwZWYFF_MoMLch-M69eLyLztuJP6ymMiKua46HAHK4iQhpHvss9m3t4N4jGUwmMSYkS7aPYQ-Wx2NHUIfJ1cHZfpQ_C5HBXb_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=IMsUy8DsYT1QPxa188V02J6sDw7-e2tNENYrgW9Ghn4Ecv446C8W1ir_TFIDYBbXzcrQon2Qfe6xKt-c1hctZiMEsDhK2KtDZPSkERYIdl2x_bqOj240Gtc22bYpFQCNYvLFGCxsiCILbZbX_F0f3Tq7bH82_zrVxuEcamvjCrsUBtkb9muXZra9BhotO0hCKslr1Wge1XO1mSAMfUI3OXk5jkAV3gc1toYlqOpWAYwu29qg_ExCy9YPWzDNJSJoRFTGnijB2tSkvYix_kY6l-UixB7ANspiSgTtnRVw7n0aIjBKvut3Lv7DmOrGnZEfWypHw9vi6j--ytQ-IXt1m7FR0uwydSoYG6E9Ti7QTgtft2yQdGi2MS51i9HI7_9U9T-4e9dKBnqzs8X_BTNYVofSVSQg7iYtRMO0dRrY3O6BXF1UWMxlTt622AWiagylby9vYZdz5FyOXCJXwRpTGeK0WDVR8nVREIBUbsH0RVWQmPFd7vFGg8cG8OnFxiPzNHHmpiZMJShc98lusoDuhHI4eTF33SEudhSXHivtcazkfkaisBuhNobBgUiGM_UVkLG-qtT0SIFJqZin-vaQZl2X_ZFymmx0E9dWVMx3F-2-i00cCYp1r5OtEd_LErq3Z8YzHOCr0SUAWb_WB-2lB7OHpw4eVSyU9NJN49EjoA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=IMsUy8DsYT1QPxa188V02J6sDw7-e2tNENYrgW9Ghn4Ecv446C8W1ir_TFIDYBbXzcrQon2Qfe6xKt-c1hctZiMEsDhK2KtDZPSkERYIdl2x_bqOj240Gtc22bYpFQCNYvLFGCxsiCILbZbX_F0f3Tq7bH82_zrVxuEcamvjCrsUBtkb9muXZra9BhotO0hCKslr1Wge1XO1mSAMfUI3OXk5jkAV3gc1toYlqOpWAYwu29qg_ExCy9YPWzDNJSJoRFTGnijB2tSkvYix_kY6l-UixB7ANspiSgTtnRVw7n0aIjBKvut3Lv7DmOrGnZEfWypHw9vi6j--ytQ-IXt1m7FR0uwydSoYG6E9Ti7QTgtft2yQdGi2MS51i9HI7_9U9T-4e9dKBnqzs8X_BTNYVofSVSQg7iYtRMO0dRrY3O6BXF1UWMxlTt622AWiagylby9vYZdz5FyOXCJXwRpTGeK0WDVR8nVREIBUbsH0RVWQmPFd7vFGg8cG8OnFxiPzNHHmpiZMJShc98lusoDuhHI4eTF33SEudhSXHivtcazkfkaisBuhNobBgUiGM_UVkLG-qtT0SIFJqZin-vaQZl2X_ZFymmx0E9dWVMx3F-2-i00cCYp1r5OtEd_LErq3Z8YzHOCr0SUAWb_WB-2lB7OHpw4eVSyU9NJN49EjoA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIAVgnN6SiuL3v8TJu3Hp9z_tAK_0QgrhBvKy7wTQOaoi1G2kRocMzpjszGsptkvgX6CFqjkJaul8cYFwaK-WqOrlgR3DMgZ5krHg5k_wjKabxFVEeAYmXTrpkivSKyf2O8NgInnl5cb3pPO9g5BGWniwnXnCVfd8Y1A9hYnSPHPrHhBZe69gBB-yiTUtPdkX_E-kuLJJFR2NGZut6JTZtD98rVOVCJ-SOQoG2ie52VYQSNiPtjJ8jsQVcrZdn1Hd0l5iX5QT6HRaktCvjmBcj64lgu6Rlbha2sDI2Ar-00wELrQ_NMhrtV3ZUgRtgWbI8jjMNlFMXQSVRfvMWb9Lw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=nwG5eoKW7ibafB8jfP5EjBci9055BluizFRZjRSmqjFYMQG5I5W02-8zai-Cr6supVpO6-5plxEALOhwiOUfsDfaapmI2d1LrXg531A7SHxqT5nRX0mSE0ExtO5Gx97xyELDWvkk_2UCr7UipZznZte6X2S58ouIgppaD_ABb6IjHimHyd7Z3KRObo3_SilQwn8KrfP6DyGs9fZo1VfiLdTv0aPrhbAlPsjFhaWcXz5waEMw3Hul7mH8MAVuSWewa4S39b2pDdcizZjj7hR60joWMsVkgkXNAuLAOn_vymFycvnd5TSTA4B45DKX2xvCeQgT3a_nB0AGSGGRhP7yDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=nwG5eoKW7ibafB8jfP5EjBci9055BluizFRZjRSmqjFYMQG5I5W02-8zai-Cr6supVpO6-5plxEALOhwiOUfsDfaapmI2d1LrXg531A7SHxqT5nRX0mSE0ExtO5Gx97xyELDWvkk_2UCr7UipZznZte6X2S58ouIgppaD_ABb6IjHimHyd7Z3KRObo3_SilQwn8KrfP6DyGs9fZo1VfiLdTv0aPrhbAlPsjFhaWcXz5waEMw3Hul7mH8MAVuSWewa4S39b2pDdcizZjj7hR60joWMsVkgkXNAuLAOn_vymFycvnd5TSTA4B45DKX2xvCeQgT3a_nB0AGSGGRhP7yDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=LWnIM6p9VNLZt-Kvwixu64O6W8tlVQaJi4HVbOi09ISbMZP2m1hd_3t9fPwSwlF6GeT8zTNzERTeBC-eVTBuLfYDf0wjl4ZB3lVFt_kjevWHdVMeunMUqtuuTDJCknbCL4RuDTiUNwdNUyjKLhQRsvkGSIjg1Y3gmg-KMJji1t9T_xdrSWVICbu7h9ki0_hO60uKd4QjZIxXg9CDu5MVvughau4i4m0akoCuN7AOc2Y9lojGezWYaspMk-9k-UtUI3kWU-TV7EbuB7aQp0sHh0jc7g9odD9Q0XN2XvFV5mTxM0nZDPQPIMb77VuiitYhV6rXwrLcpGPQ9YpAKxFpzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=LWnIM6p9VNLZt-Kvwixu64O6W8tlVQaJi4HVbOi09ISbMZP2m1hd_3t9fPwSwlF6GeT8zTNzERTeBC-eVTBuLfYDf0wjl4ZB3lVFt_kjevWHdVMeunMUqtuuTDJCknbCL4RuDTiUNwdNUyjKLhQRsvkGSIjg1Y3gmg-KMJji1t9T_xdrSWVICbu7h9ki0_hO60uKd4QjZIxXg9CDu5MVvughau4i4m0akoCuN7AOc2Y9lojGezWYaspMk-9k-UtUI3kWU-TV7EbuB7aQp0sHh0jc7g9odD9Q0XN2XvFV5mTxM0nZDPQPIMb77VuiitYhV6rXwrLcpGPQ9YpAKxFpzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLHV--1x51oiRaJGsVIGBLDT1KC8erJbKULq4cfEZONO91cCureuPuhng4RJhDF4657QTGgCyQalnxMZzgxEMIL-Ibu6c4GgcT-IWjI4EXORTPFWv7I6woXR73RhfBTMeLzaycGjfaql4IDjJlnP8AqORE0RUze_pcMTYnjI7ZFwXDSnX8mhqRqSrS7VLZ2dGnHDC0R1OG64J6p0nzTikkjA3DLoHsjnr2JEromNObLqSr33gp6VgLfs-6MUJX3AvW01bizdYPhCGGHEKQKlzfv2BRwOt_mWddlJXbjl9U7KMnZuu2cofzuZrBVBsEKh1frYKPk1JH2HygX8LNa7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBJmqQiMUz1WwF3F5Vi8qnGzd8RQc4T5xRUeMmMlfTuTKWsyjUUjnl28uuVtsXp20zECmwSAK-uYBAes1-St6zNfVSpt0i-xU_mPms3hNGtWR7gV6MdOhyL-LKOCwMuKXAbmZI9IrqNwRDBXp7_jATtvoDQnrLybKt7C4ROL4PkP7C3ky_z3RY3EbEARB8Etaz1pno7Se5AKidAIT9amROj5Ejb-IGJXlb4qp8nFcGw-lr0kUx97FDsMhDmm3FdPgpQVFrKXGX3KX-Y9DqBVSB4p-J66259AiPNB7bz3w_OHB2JtTF_2zvOWdTzYVsaxhmzuXnmrhehHmGzEZ2GvSg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Fpn3WAjxYzwYHfWRqkin09bjTJAVG4flduSgdDKIKeixEmZ00EVg1W51renFlV0k8Lrj5aYrcQVYLS-vCaeJ9nTTWUC5Nspy1ChaNVAstrWqxnCK4WsvTbYpatfgPknU4K4jA4PqmJFtcYTByyxgfYe6v0HhBlF34DtdeQ-g_dgonMvMJgo_emkap1Dql5urGei8GeI8x9ZoXDiAzvf_6GnPnhc00vZ0fpRQvJmHq7GyHUUTwCTXhYRS_SM2LjC1mIltbuPbZBcZLKlrpvc9_fDuXfayHRs3FCqpT3l5l9Bf_tcRpYKRzWZ0h7JwRw5TfL9WN2JitaCtfpqS6D4s1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Fpn3WAjxYzwYHfWRqkin09bjTJAVG4flduSgdDKIKeixEmZ00EVg1W51renFlV0k8Lrj5aYrcQVYLS-vCaeJ9nTTWUC5Nspy1ChaNVAstrWqxnCK4WsvTbYpatfgPknU4K4jA4PqmJFtcYTByyxgfYe6v0HhBlF34DtdeQ-g_dgonMvMJgo_emkap1Dql5urGei8GeI8x9ZoXDiAzvf_6GnPnhc00vZ0fpRQvJmHq7GyHUUTwCTXhYRS_SM2LjC1mIltbuPbZBcZLKlrpvc9_fDuXfayHRs3FCqpT3l5l9Bf_tcRpYKRzWZ0h7JwRw5TfL9WN2JitaCtfpqS6D4s1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=tSZfmDbR7zIdnvQQogosBE-FtQlVIpAtY4ucVDJpZsMzZiE4BpCI8wYhguNrp4dR8eqmHxXuuG7GiurBCW_ix6SjIfnKqhETT1gu2QyiT96_K0jXsejUplhW1kndsyL2sWj0L6uHcmfaGSQViwEOkcEp3SyNLHuf95bbl_cOAbrZZqrOYEFfN-xgmG_AzeGCTnUQR1qvF81WVr_zLDibqZSaKn_pGhr-6iiHVnQwvQVx-Ls_TRTu7PsQ2ml4_Gw3PQnpDeVVx5vUy_ai_0NphYoejjA_KEDVr00Ie4hkz8E9wO6TcjLTQLXAPbltHf3nLsF-gYbZs92IWA4Ne7Cfvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=tSZfmDbR7zIdnvQQogosBE-FtQlVIpAtY4ucVDJpZsMzZiE4BpCI8wYhguNrp4dR8eqmHxXuuG7GiurBCW_ix6SjIfnKqhETT1gu2QyiT96_K0jXsejUplhW1kndsyL2sWj0L6uHcmfaGSQViwEOkcEp3SyNLHuf95bbl_cOAbrZZqrOYEFfN-xgmG_AzeGCTnUQR1qvF81WVr_zLDibqZSaKn_pGhr-6iiHVnQwvQVx-Ls_TRTu7PsQ2ml4_Gw3PQnpDeVVx5vUy_ai_0NphYoejjA_KEDVr00Ie4hkz8E9wO6TcjLTQLXAPbltHf3nLsF-gYbZs92IWA4Ne7Cfvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk-14bxyEqHQMboaDOW3ZWxLU7u647LwqRHNOKp8MlcQJpX1M73_XEySKYJ46yqLYEws0y5RBOjD5UhMWcR90PBymob9jsX8VEbp78lNu3Pm0GIe6sioI5DGRBQbQWCF461IjqVuUORI-E4_Zkg9QeFhOnuyy3oJTfNfV36SfJbYRi9s5KL91svaw9IAcKenoX46ok3_zUzWw0z0CapBQ6kxn1Re7Fhl_36aEr6cZ0pCDsA2vf9cu1g-r0T6ACLd1RnUX1EadtcYcKvURLwVLgBnLrAtmJZWSn_MXlwfZQM1Um1gLcktA5tMau3XrPE2VIgeP2HpHIMfczF8wMf0AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfy3x2hmrnI4Q2ysftn4DaEUgYkNMwLVm7V3FovF9AT-AX0JvQppuAW4Ec9KtQj9b8pnR7nN-yLzHUZY4G-HwNXUiJ2xR0OmxVZMizr6cJ1rp4KUN9M2zOdKpvLSdP81youz3OPoPsYTAXda8RDHd8aU9LYCs92GTPi8nASMJHWzwDWwEvyfdfNRhmHhb3wyQm1ZUyYtj4usaf8mpV0JZkgWOg5OjJHhl33Zhey3GdKe689En0nDP3hYUJd76pdPf8G6l1Dt0QCEm07kms_S7R3USbMZLPblUrI5zVTgsWJS8Obd73hH_-0WAMSEIElF79uWWGM1m_MoEqaZPTUZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhjoEk8oD1HJXvP0pvFSBiRJJ0p9aNTjeVPaXgR06XwRJ9iyp4kzWtZ6aLTOHL-GQgLqn_pmVAETjONRikvmBMZuCGUv8MFDOrYbtwThHUoo5lRnZaEJJaE_wyRcp5KysWcXI_5JRGDEQA_-9izNbW3GMA2jHLK2LbG9r7EyCAtNO2adnKBOjoWFklDjjs5mupLpvrQefPAl7__TwhGPd__1QoQISqZNmvlpoOp7V0gHoqn_Xl8NwQvUNWNp3A1BLiQ2myp_c7-HuWLW7Em1k1oxz1jMyDsWcKYeYTsftKfK5cq4KtEKxEltiWwUMo6D8UC1Yu6nO84gxidAImMkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
