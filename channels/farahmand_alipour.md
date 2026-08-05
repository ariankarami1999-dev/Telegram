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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 23:32:41</div>
<hr>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=i61zJYjSnGB9oYYwmzssSiV-3exBySCuo5P7VgZ_L-LhPagQY7FiOwwWLbaWiyNfGGKyanUAuP0ZoU9TscEMYJenXhORBTzUoy3HW_BcMC7L2s5qrGWPdzUqhL1p5askknWPfU44gsHBqSFoBsdparff5tcgAONUx-uLtpfwE2z6_zHFzIKiNw7likd1Xi_dPALFuBg8zUL0N0K0mR3c2Puycja2Qr6nLt7z-0ns2X1ZqLNCNIeAtyahgM2eVg8snsU-zEtR7BCm3Sj8WHnTeV_L9DoXOVxEThhSyqj8MlSY8e0ZBeeQUjLbPNbqiubt4F_wtn4y2JwVa_rFDYNOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=i61zJYjSnGB9oYYwmzssSiV-3exBySCuo5P7VgZ_L-LhPagQY7FiOwwWLbaWiyNfGGKyanUAuP0ZoU9TscEMYJenXhORBTzUoy3HW_BcMC7L2s5qrGWPdzUqhL1p5askknWPfU44gsHBqSFoBsdparff5tcgAONUx-uLtpfwE2z6_zHFzIKiNw7likd1Xi_dPALFuBg8zUL0N0K0mR3c2Puycja2Qr6nLt7z-0ns2X1ZqLNCNIeAtyahgM2eVg8snsU-zEtR7BCm3Sj8WHnTeV_L9DoXOVxEThhSyqj8MlSY8e0ZBeeQUjLbPNbqiubt4F_wtn4y2JwVa_rFDYNOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxcbJIctp1pqBy-vIPYMTXfkOLYCdVVDm8-Uvvwr3MTwml3DFKTfdgV9GGgBOPB_D4q3cVWSL55CN49zFU1oQ9MxtTcRHkDi2xHyuv18yIIE69cJeHy4xu0t5iPQb-BsTFskwTPK0SYkHHPEGC_tTASLAC2vZRt6yO0MLPYflJKVjiqovmNG53LDhCvxQZCxqS-F8tAUL-XojFOAk12q7V7FX1QhreXYI2tt1hc6ZdizKxO1JWCML9tNcek48j9MeaUBk5g9xuK-FNTbso5aNppDeOa9kMvYYzQapRYKqDGwmNTC8x_McUB8lrZDgQ6ld_jkMwgiFqws14KX0NXBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvtSvsV1bcM7QDFgdQMfXNB90H8Uw2AIoDqxs-2vOLWIh2-Mn54CpzsfOpp9bMHORlPY9EwN0TcByvoZC7M7yIp07kS37by5HpraL7YV5ifPUeTkVGSJEbZAmSIjbMeXWnBCkI0GHp2Y2OCZNfUOGZAd77Dtbd3P-dJzAUI9C-zMbwgaAJDs63HtrrKnAxfzvTAJIki4pH4kZ75CRx5pULvXrJuMJyR1aZLcBCwqKPB4xvI-bWZw8RSo2q2YuSvieJF6PS5ilZuTUOOmFlh_RJ4ZUoo34EjNkiRDBg8hMBJzBXtSMdyujdLP3m7vu8x2s-gkWE5u4I1dfHfXUqYEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecwIk7MdzeiOmAtI3huYKz8IBgEYx1uQrgOMebq433RwZpR89mvbqNk4SDCjP4dIJkFKg6YbT6QsdwxIKLnWYwdRrqWkfqCxw_wHrK1YGMraPfZtbNGnBMlgXqR2q3mMAsAUjgsJhpzoiqiSNAa05EbO5bl8ursccFNj0K6i_JOenLAL4ZBs9FXiIOvtSDJR2hUIWe7fTrYIJ9gtZVzc0LQX7yIPoU8jgWA13FljTCXe-GsakB4X1br6ccXijxUWd7yOaFlnB_k3ZAFT0_fRq0pmjtR-w5NeMkF10l2XU3HiznS3-5z9FnqaUeqtM5EEcauQmF4ZbJUEaFTo8aXarA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgJH-DpHeWuv0ZLhgBy49J2-QBSxpZ8F20L60CRCf7DxGgZ9K2wzGDgzVwSfEc8hwR-kl6sh52Djn-_6zxhHu6vDN5FD8kbTQD7RatoAh7VSzaKn5WElSvurnTZJIRhjwObOGA9n9BRQ3kX1cj0HIWG1OZSKuu1dMNhRYii9pliUFL8zFipSLCq_voOttJAU1EwOnKbsddxQd_aOPq4l2R_ThVnoxWhwHJpqbVrJ6nh8fBJVxzkebhL6WR36XYgCBSBPNVINi0Gbca_k5YJwtBWOESqvDqwN5PjyPcRgIn7un6KBxqS1UtmYfLsOma6rGEmeJV2xhk3NOrhHZ-xc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTy_rX_PbdDDvkJDS8waWiRnumlRfGy_dTwP_EQzJodkkvIYvSB-Qva6VdV3AmsK_v2cLyV1Epwk0tJL7Qisiv1-Kum5WnxCMOHhOAdVi1QmVs3ZjF5JNHeYq5MWwJ2Xcdw54bLdEh-tsMIkM_rUf8KTz1n_Uzp1bmn1qay9C9I0lyRgDl8tswsMZM1O226eGS48EJom_aT5ab-_w_x1AMLm8zje_m9IqXp3y0R2zRu83kVM7fAETdWJIcQNU9hXYFo3_nOWuukh3lt64reulbTnwsBdT2juK7zVzkxrQmGdG0tjFfmYt2JpTrcJp9t4wM1LZRCDaR2ZyqUqCfT_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hp9MIxZrFojmZM_esq_1ShMsZm9S0Y7GosTm3P6Ly0WbYZNnLYixEDhlj40v61PQyYmi7VxZmrdiH2hdMgnUyvg5s0s7PWrgV1fA8WChOYh31xuSBhh12ppZEphU7yXS0TMt0idb63GtRg0yIsf9OQ3rQrl14ZfcLYj3Z3DqzwazPzhEGkpVkH1spA6Rl4xOwDoPNHchPkdmCHFchVMxSnRDzVtfAqTmwHcxva4E5Blx5kZjsMynjFWcf8WY5Vo3xIvSvX4T_PrSjkXcd0GwRq_Lp_IvaKMNj_p-KxthsXnCV9MW3BEXl8TFCt74i_lG7L5BOaZ6PMJf2TdlUZNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO3Sc_bpYjKNFrKAIizf-6pqX5hPt_GCitc7VupxKQPv2RByhPBM9-MWXkNLTiZECzsl7Efu2twbJZblHjEMTMU-YfMqHBtfz5sJXJdFU0SPR11lcV3nMPdH6OSnToImddZ_Kw5_TTlkGepPnxQMIfiOnQ9PkoMq3GBVWSvroZM885VnrXVn4Wopc6MpvZe0EzsiE2IS-nTfXl8zEVhnRKlG5UX_uc1Yjof-uJkE1ubVjJoZ3X-vxIvNQ7YZBbSbfFABQyZLCCQEBeGil4UQ6ovBtsyhxk1QN-HmIcXlKMyYRJeS5moxzS0DS_MBYxwm-NNhhsK0h85p1lzyEGn3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwk6Svy0mG87jpzBPWeAFD1XOKU1a9cSdKuINg9DFFjZUus3AGFIjVHM0RGkauri8zY16Rf2dSyQs1eC0wQvkpShJk64xT9UfIE8cqmpMAjrJRgcwKlFSMXT2qt8nHKhEOOoxEJMGWDBsjEJs3DLa7m6Zm8ScjPjVKvnnl4jQ1TzngoZMfCpnbKJTOPi9nl8wzjI48xA95MrXy213OxZeuudZZETUBZlYUZvghjkCTs4mJGKRltBu6-qVmxMSKgO6rXr1h-o1jkOxAEWJ6XX_WDQQVfnpBIAuliQbcvJWJHLIF8RKrPn7wgIcCNHnSmBpRxKZaEzK9iYsSj-FUeYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH4LGqNVP53z-HQ4PSTbbeIfaG8CYaXRKwPMhSXLYI7H4c8iGpFRPkCtxbUiz5FqHuxnokCg9HA3UfcCnS69zclW0Zk9-DZcId-55cfSHYXxqmMOZdehOpsEwhzlOdIilJjHiG7XA3pvpBAblblsEs6B43jzg59eIS_bHyMqE1TH4370azvr95Ci33tk6kBwo71SQY0GpOSes62_SOyBLOKQHoTmWAxw5ivQtDkzTq9DYhSkJnnGd9uuhShrUroaNV6P1v_ONEUKE7d_A81o4tMFf9SnAgcXEq-b_Y3YbcCfQpyQwPiQf267WAd3nBOq1ahnNmvzw2g1v8Xb0lZv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px-CxRkGj_DcpMeqMN8gtvJplKqd8mmIUAKDDwqdqva320zJejkW7UJoWYJaNU1diN_i1M6AkmQ74mQHQ-TCTitue75yif5_1AYb3zDM9ZPATZsqvhbfrXTE7XeLwR6NN-KjCRFFYHkOxQijgE1SthYjFy8-kSCMfykPIywz6Mylacu-2VYBgiduCfxiEqaggtcmUJRaGGmNZ-6TmEkYFwAmG2IXgBVB6wK-IOBZ2R5JWzpqyleS9L2SsFvCZaio7Nn6LG4L7YQOb1zvK4wRAiUFOyVPEBQYyxCzcJTMriM2HIg9nJolBr162wdgl7oWp95wqaR2k24f2Sq-RBnN8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn1T4C2-oOT3USJlO2YeeWPuDHN6W6idiW8iaNaunr0_w60zKPU9ytDVCBUarUoVQ4sX43_AgMfkBcuYQNsMz0d6pvfgoj3m4TlfbiBLwW1-0fQ7P6nKg_bCVPKGU8m2rOMgC1DDjESWp6buUrXXwKEInaAsqutULASPosIFcLq0JfGy97tNRkiT_LhbEJdjcp3GBNWtym6RzN_VPFlCTGovHAVWh_mDqfDRRbzrCf0B_shLWfSjaIZmVubX_N_jZKa_AI90Y_dOGHfkGt2w0w_SXFU_8rz1cCp9buAnwx_9Ym4c09jI--4hnHN8AZNNnguS3F01-ORHgZkWP7ltNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=cLl-NoYs-6pw0TIonKgCOrYr0-VNOZQEAXfmVx1t4fkJoaARC3-s2ecVAnfvq-q23B3ZMA7PehaFB3R4fEOrSy7ZWwNc8lJnJY1C-5BtgblvEwVQ8kpIGgRzVMcnVy0rz3c4OnCHB1K4MeWS1ioHuRuTLO3fqfx4IXpvxd1tabAM5VGL8xGHbDHbZLEpyoOJc0LWiosnX3UdSA3eeA-fOMPf5PeQkcobBK-ixvxlpjruLswob-W2BQC7Rytc07hJ_ad9y3wLwDdbz2Bp289EAraAtaAvJS_vHiFBa1MopHsrWNSjpiKnBt-I1l23YmP9p24voJZPXh4V43XSiRJyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=cLl-NoYs-6pw0TIonKgCOrYr0-VNOZQEAXfmVx1t4fkJoaARC3-s2ecVAnfvq-q23B3ZMA7PehaFB3R4fEOrSy7ZWwNc8lJnJY1C-5BtgblvEwVQ8kpIGgRzVMcnVy0rz3c4OnCHB1K4MeWS1ioHuRuTLO3fqfx4IXpvxd1tabAM5VGL8xGHbDHbZLEpyoOJc0LWiosnX3UdSA3eeA-fOMPf5PeQkcobBK-ixvxlpjruLswob-W2BQC7Rytc07hJ_ad9y3wLwDdbz2Bp289EAraAtaAvJS_vHiFBa1MopHsrWNSjpiKnBt-I1l23YmP9p24voJZPXh4V43XSiRJyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqz65LI04FsStkC2upZqPSZ8NCWm3huOKD0gqsLXRUaLANC_s-rMuFhK1JdSA6QVt8SQHPx67Tu02toWehshir-symtci0ZSqVe8fcwTHXaHAkIR-valCCk6XJcXMnz0_tCnQcCDiUhzXWI9HNUnYDT4phlRjYKFoxKC6weSeohSnpm-7fTUnxxZXmlRC5c8QMqPL97bCP94OxBad-0uWChsboEFjS36F8B2Nrtdgbg84o3yQJjSsZN99woYD7dt4D1riFd75F5y3Wp_pi7K-ho2ahfRX47yY_-mLDsy9MvY_ke3UR_AC2wnntBNINy4yktbpcz3ChmTDLJI2KXrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzBytM5uu1R55Q_8etAoGL_4LegkucKruyWahGhiIkCesDAatM1WN9AgiYfVlvA2dgo8Uw9picQHjBO3j72822aOjzxt-nNPBJdY_2yfA0ZIwDtCUsd1BinNje6Ho9cbT2HUInT8OUWyz3QCYhKgg8CrtYCeOUkf4aFlK2i13G1hcJZbyBAddgCUesvbTYbhTpD2MapKyBHTyavnmzhxM9l3t7CUAnbfpWT985ujOo9XVJwYfgemJUHm2TEBoXnfaFMXesV9uKO6nxVGhAYX5l3edm5Hv03BxuXSvmr1dHsCRXgBVcZhPnmdeFtkob_o6f5G9jMq5s7ePNyiFk6jBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpMDpvGiNZfE3H47LDT1r7G_tcCZgzpK4Qew0DT61O6TTUJstw6_kmKpdY7I5efSPbCkIdSHo3KYqtz-K7VpovxOtggFxMTJomQcfyubKGxKJV1t4KYKje7Ur2_CoPgSGGr1kMtvnkQietdHbNs7pm6UVUrMPJuCbpkvRCb-f8Ux1l7uzQcFLd4mnpyS87dtxBp1vlb1QCHknb-a5JvRwHtNXHkMwPCuPQWhgacTnAJBmwsv2wYZfBA3GHnA5FwWs74uENpPNBlIBCn3kFAAB9G_33y7aVyNLvhhcyHfXECLxELPuqOUXoeVAWPYqI7GohwLPr-IVG032O1ZOiTYZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2dR_ovKamGSf6Dox3Z11LswUcpROiqfJBNGTtMXhyGlBzTOdfSiMUNuMDEVc5zUNmlbygP6iZcwjluERSpp5_vI8mCQ-DideT39B7RUDTQNqlRAC4jtOM6skJEyqgl9V7x5NvqGXvBTcnXdUavpEndHx7Nys-Xt3JIf2IiIorn32JtYLfMvbuiSWKVV4Bt91nDLPycEuV8zln1T0veqgAEU-Fw2bmDTrLvrrtpDhn3fr96TcVJYn1QRGmsr-vEtT6RDKtTgD9abP5IUkDX8zbrX20EwgWHHqDWCACWPpho31xzjSqNE4Ydcamlh0BVNRVRShq0FYld0XLcmnxqnJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjRAJk4lj56HaORB3AcR9qcAN0GENnhZerTSwpSwl2AL4dh0es9BOaX0ClhVIXrmV_9kiGbkKEnzgvJftOXeSkpT8SZFa5_6LqQI6YqR2sukpJ3yw8IDlpVpGJbGLC7BpIQwCvrnDXitq_w_Ex7hn1ZsYC1o34UEBG8ASJOKCtJ2woeqIPyFDiCL3oOHjZYb-eimZKKrFb_uKoYyvjiPbwwM8IAflNOaVgte8WkP4ou5catfXtS_6oYrg5EgoyIyFb9Bqb9_n9SG-tyx93iSv0AhX5CMoxtBqhY9QtFHlDn7BtI-zWL1JvHXLVkUlp57r7qy698t2ridBxAMsvrFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noScq1pwm_szp9QivJmEe7BZmn7nZFhlLI7LuKcZPv4VpgnMGLaJeoqBSGQq5Jf-7iEpmZUPqlDOYco8YS-LlIT_Bl5mH8PGeoTdrX4rTM_x5XGrKqpptZwafuhpmA_40swCbggwFb5WXV7uqiXbT5uoZmJQzHNaoWlNNwbc9E39iozA6uKN7M2SIRU3BsT3hQxAE1folkCI2BOlNjBxb6nmsbf5lFibH9RRZCxsMflBKpIupH-LCvKfchg4RhX4qGJQiSAlYOqk-UgpqqESGQPPqQYj_je4hgxyD0eU3dU3mjXUk6Tgz57p7bhTibUD-8RJI3M6loEePIM4UuUoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpjap0G7VeV_9AAEJb8huJo9qSFkejPjsU043rGOQ7y8w4TTKwk84NAgAeHNxYhy97Ok4njlWIt2Dek2wSafyLl5xhdmfOr_7pOQyj8fC5_DVupZc5u2p8P8SF9AusAIQ3dC3WgKvf_A0_h_QkJxySIysRdI5LlFFf_-uw1mLZsRZxQj7rxLZjx_G3_ehplXjJiA_zQFb11LJf9PCI--fhxXEM75Ff4pHPCdrDpzSUmcEZbAcM8-KWKTN1iOCUrcwhIdpIHYwVEI966JooGmEM2wggmIe9IqEqS7a_XiJ0NUrxJz0SyNXWvnSDUyWy67BvD2Ss0Vd74RW5-BB1zuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfIZl0gdzElBY8cRDpuGnRCwni6U9j7R0XV6Y3I2RjERuZPiEd7e_4kSO-Q0ScB2jqlrtKgDhKIm4-HDEDe7Zh_CghYC9ao83uavfgSeNtED6K4UeAvt3cuTcKUXj-8HReiXOT8rCSVLTfaIJgGjYhqJLf5t9V8GWVWHaUPQJKo8p6v9ytjs5DT5elf2WVLhyZA4PhRQhpOEFsaaEZjnxjTcORn7UCtcgSIbd1NUcxYMMuc0qHcrj3sP2MF_psRF-YIafWiTVGoE4i7rCP6emJ9u2PFvDfIQEaCGv3CnGQcsqrs_Nh-hWmGWJ4HO4f8nkXMlOnhOFiIYhVPde5vN9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=Z6O1kiDMRgVCt14t7AE394-q8yv9_IEQrQBDB82w_8_uP7EXbDXDW3B5YysvpKpR0FcFFPxdCoy9aH6MZp6FI77bBLkQVvpxkWR23mO372rklIsy2AVPxiLHyGncAC3F6VfWPTTaB_me1mWyH44YtTnIHYJTC0QFnM7ottZbf00BgGB9liKhjOjPTPLudOhTysT8B8x5HofwR89HIz6wQgHJueF6V0eWI5_73srWD_O5cbE7BMdod1cZ0MmWhhOrOUfR33CThE_mEHiEIfl8EJY-kyClzQ-OHt8IvQEVon39XXbTGFRyHKGQlJGUngI8oxqPnFma_xlySHhtOu801w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=Z6O1kiDMRgVCt14t7AE394-q8yv9_IEQrQBDB82w_8_uP7EXbDXDW3B5YysvpKpR0FcFFPxdCoy9aH6MZp6FI77bBLkQVvpxkWR23mO372rklIsy2AVPxiLHyGncAC3F6VfWPTTaB_me1mWyH44YtTnIHYJTC0QFnM7ottZbf00BgGB9liKhjOjPTPLudOhTysT8B8x5HofwR89HIz6wQgHJueF6V0eWI5_73srWD_O5cbE7BMdod1cZ0MmWhhOrOUfR33CThE_mEHiEIfl8EJY-kyClzQ-OHt8IvQEVon39XXbTGFRyHKGQlJGUngI8oxqPnFma_xlySHhtOu801w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUKu3GgD5nndvjAZ4h3LqADEk4ygGwhzriQfPm0AxF6I4LQs00oLviRV87GIDoPPLmoMYkyNgIAHlpGCXH02TTBj535y1S1DwAeihtiMnlFqmlYgOC-RO1On84D3_CMbQMX-ZaS32T5L8e7t6fvsjRHaAJt9Q7O3_Itk7qYQaiHFxWIHDpJdVvNdEPpm_4hcjG4E0L1CP58Re00zfd9V_7CEcwJgmmu8lWEV-JLSIyuVC-txvHDUsM3lQDA4tafay3AGJiK75IW6is-bV7-IMACVmiEV5zA2bORb9xMVN5zUg48RIgczKwDU67qeeEO_Wq-Bcgvr2iCzWpogdRoziw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nArTQfHaAt5jB8LGNz708wXzrVg6KOuO0tGiD-xlSNFEsWKuazaznC_ZTERtRYQAX7i-GKf-LMCgDgvXgZB6r1sQML6jEcKtM1K3wHUmbO3CBGjTUdqQeEfHw3EtqDb9-WvtruLEMVAfNHpv3gUo_3PhMSl5GWXeTl1tqL3JVlBpbnxX4276_FEEz-VX4UVGT4Qk_UEsSYxaulRuw-tWrL5FCYMQrrUwZjDGtIqf-tr21-X41lYwQT0glApeBCwYqvvqdfgR8hL7I-B7pKAhxaorPD1Ymrl8vlpG4s2s2vRn6HTK0TMBnDydCLiQwgT1veYsXFbNHjQObl8uldhKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2BeN2FzRYAL4KnE06qiRFS1_MUZOy6_imZK16Wb_9XsdXuVgAuTOmaHhlTBPBtWTHto9OwgcFqpSYR19vf1RA4YqcCgh6RycYCYISKFc-Yi7SASj1MI79uX_ZrPQ7IPzDNkyICyu6Tjq_Ra13liF024dYCZuO6oLR0EendLY3mjOZyy2GwEF3IJmfKXstNxomDZW3DY6gf_8nBNx0nxbcHYYriFfYs0GcSAjPstqG1XK2DjLLVhwBu9wWvqYzznScNrVZnlzAv52wveuY5LUiz78yy1yt_Lko2-FIXbjYx7BgilVnVCaCjBEiaUKRHyee6q5Hx4YkTgEbXGCFiBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSFaNb5ItSU7QJJcsGTr28tVKtNDGjVj1paS6sER9QZng_y_M79WCxSYNW64ibmRNnaKm6M0O6cCCfavP8n_ZpIgzSJk10TNxD7Hh9MRrZqxGmbFco240FKZnIu0PA1Njy1pV_S-NPjQQSvMUSRTLIKXyChxXDwyHBt5aW3DdC9u-9_S52jNFqWERFkgBR459g0aSm6-5P8u33a-vugoa1YGdTcTp_n5Gf_Z3tLvHtMJ7L8tH1e3zued1QwRLhbXbkxKRr7u-AHiIl7NK0E-vzh1GKj9MTFBSTgB_Yc4E2AJMaiL2CRn59g4VyOTuJTxI_IntgvPb_kTf3A2JnT38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouc47lv6tX5QhKvpeFT6TiZm09Zo4CoZowMQG8az_xIiUToqjpmFrQalEciM8YDZQdjYEvaSzOmAEvDuv0Iv5cb_dHwNhzAiUFZGs7nft_ykARwEyyJ6U_J0pljsKG33_YoHPA_l1wwF1g4V_YqVr2yknd4E4u62hxtZdl0vFD25HpZ9CxPw_jlyH7OhevAzeknchZN1UVDNwaEBXOO0MFoJq71vGHwqRDC1lyVyb_r1P4CuNxS06lTtpfNhyUrSbgcErxvNNkgfLga8zlLS9c2v7bCgqqwH8gGFJK4IoO-GAHGIDYOSgauEbmrNIfIYAYbGoOJ8Qjr3dnOoKfkBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6Dhg5-giUsOanykG2c-RKpyWQNd1OwgruqsQPaNylzvGXNNGpBZDZbrGgPJWnRRotUc8tgsprvcViKneWZc6JZ_DEdm5PXW2FOzco2e2V55hbTrEscrOphL5ci1cbXqVaxFYiUAa9gj_kag1jSLw78kI6iQrZpM4OXh9FdxViGJ5xwYILkBHRjwoGLwj8DLoHzHRGz1VrwAOrMP-XySTn_DhXHfDqSUlIG3w5GGMjg8RLECftgKNrI5Eo50FMTdADaam-6vZAxD72GPkyqIlRpNV_8ql-VDqzeBZrQNPH5V9SZaLVHxu1nbgu_1PraKDx_lNYdjvpC2sn3ImHH1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6zZGdhVZMkOWss81q_vB06lMaCx-fXtkg8sicKMM4tfgfB47Ty98INnUrdZdlg6EOkYXOcK3savo5u_fZgEdVVK1ll6E1gM4_DWhlfNttXxASM5iRQ-WzvCEAfYjHtjxSaWCnLmCuUgvY0n1Cqy5sn4XzH3kctzlZkMihj-ztQfc1Xkf62A3mciuXezXeOB8TqlN2MmbaPpNmGoHRVdvzoNOR-93BLDVG1CV4cxt8TmknSNBhqiwSSNK8h01I5piJHyIXI59R3BwD2s-1jCjDzWlvyCw1mxfd59NDjJM4T1ZrAdAHoxfPNgGjpNbCJW4KoK4MBqY51T1Y3whawWVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=u-DkM20eJONMrcStm4rWhMz_s8DlyKjEKMp1A-9fCi0mBAA0tmyBYOv6FPH4LMOA6wJz5Z9hbTD3vWkE_xB734MbUrPwh_e6erQyFDauX45TeBKJPd3lxWrwqPSfm1JPwMxK998_0F2r8lbSeQZQ9-PXvg4iN0DJDdKwpUW8nKkbxPbLPWpjmo3gCocurqXpFr8mw9p5OtQnVmBB5o2BJMuqOF3EtLBUOIDaL8Jkjix2z_HJF58ZwXU3ZzFNIzKrs3nIgHWmZDwKK4uYu44xtf21A8W0LJj7UGUk7ZpsA56xrI_RUWvs0CVz5xThnk4_5XUMLr-2MThTMR697gToZIjJAi3OVVl-jF5ZKao67AvLW4XbWoNXvvYAMUoCKmo0CBylwGMDQx0Mgr9BkZL1SpgX97uUUuBzS5eJmqzoOqsIm0NQCgYqgvXVZgqRo7A_RWzlEjOQZiC6n9VjdwKsCvNAYiqnhfDslRh3M6Oo-I9A3aCWBh1sD9hrysubCv1sxdkwSv1h__24iZaxvveBhQMWCZpNh3htjypeEYFN9oINdeB6XIIQoiWMyl39KtvU6K62LbmcZp4hXYdSTVwZMBNi611qhR-sNhhsRtdNaqJsarAaCuIB7L0sy545K-td8jl0m2rwaSLSI-tLEpD-XmYy7_cKmGIKNLe2adi4k6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=u-DkM20eJONMrcStm4rWhMz_s8DlyKjEKMp1A-9fCi0mBAA0tmyBYOv6FPH4LMOA6wJz5Z9hbTD3vWkE_xB734MbUrPwh_e6erQyFDauX45TeBKJPd3lxWrwqPSfm1JPwMxK998_0F2r8lbSeQZQ9-PXvg4iN0DJDdKwpUW8nKkbxPbLPWpjmo3gCocurqXpFr8mw9p5OtQnVmBB5o2BJMuqOF3EtLBUOIDaL8Jkjix2z_HJF58ZwXU3ZzFNIzKrs3nIgHWmZDwKK4uYu44xtf21A8W0LJj7UGUk7ZpsA56xrI_RUWvs0CVz5xThnk4_5XUMLr-2MThTMR697gToZIjJAi3OVVl-jF5ZKao67AvLW4XbWoNXvvYAMUoCKmo0CBylwGMDQx0Mgr9BkZL1SpgX97uUUuBzS5eJmqzoOqsIm0NQCgYqgvXVZgqRo7A_RWzlEjOQZiC6n9VjdwKsCvNAYiqnhfDslRh3M6Oo-I9A3aCWBh1sD9hrysubCv1sxdkwSv1h__24iZaxvveBhQMWCZpNh3htjypeEYFN9oINdeB6XIIQoiWMyl39KtvU6K62LbmcZp4hXYdSTVwZMBNi611qhR-sNhhsRtdNaqJsarAaCuIB7L0sy545K-td8jl0m2rwaSLSI-tLEpD-XmYy7_cKmGIKNLe2adi4k6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=dg8uyTu0mL8sKFM7oNdOwfg1PR50Hb6xk-cyqevQQ2t1GQFR9Fgmu28NZIPvwse2r-tNud3ofJc88lVrpYgmZ8rndowMFegvVT-0MYzwYBlN7a7U0E8nD6zz7TZV8dNRmb0vB1oEE4gaYxK7HLPsRh9seUP3I20sZMGPmUlHADXgRM8wD-lJQRfM1HZRmi90a8QGyChHwNqKr1-5m4VNsB7Wl1Oe8YwmcAKmxjSkeZ8oPnH5_wo8mV9D4N20E0BhzH_tmHahI5h3mFIBlill0KQkmM9tT2jcqDwSi5RRindZrtUoZ9fVUBwXGpGKmZkEUkdmsN_3O7MR-GvgUrwTTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=dg8uyTu0mL8sKFM7oNdOwfg1PR50Hb6xk-cyqevQQ2t1GQFR9Fgmu28NZIPvwse2r-tNud3ofJc88lVrpYgmZ8rndowMFegvVT-0MYzwYBlN7a7U0E8nD6zz7TZV8dNRmb0vB1oEE4gaYxK7HLPsRh9seUP3I20sZMGPmUlHADXgRM8wD-lJQRfM1HZRmi90a8QGyChHwNqKr1-5m4VNsB7Wl1Oe8YwmcAKmxjSkeZ8oPnH5_wo8mV9D4N20E0BhzH_tmHahI5h3mFIBlill0KQkmM9tT2jcqDwSi5RRindZrtUoZ9fVUBwXGpGKmZkEUkdmsN_3O7MR-GvgUrwTTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKlUdNda9n_ImlyVdVmqfJk--8qT7DPxQMOs_NmuBxLC2ZEnw9VTmQkcD4-AViabgHdGSrRn5eTQb76lYRFBRZQDAzWPGIVABJA7HwwjzlmRYahrtGDg-x84RA_va7_d6nyfzX50QP0czPOxWyG6e6-iKKJFw-1_zHgCR82i3omOqHy35OrfBt5A5tG0eHmLop6zrmlNfC02ddBczPUNBN1vLX-XSd7yXLL0DIlBDMzLWdPzSG4fO_dnz5nox6Zu0gR0tnKWrDcOshv6CX6inZ36y0WGkgvyppiemAhG8O5rNIPUxzWK6s7u8t8xlcCS7iFXRLwCvvfKJWjim0XZEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chLKgj90Xc_d579t2HJpYFD8siTAUmXeqseFviG3-x0I9GedS2VyGpLc3GzrFf-geOCmv5gJecigr2i6UL2KYTEg02eUJgtSsRv_AGPcA9eIJv8Fe_uWBFW3t-rNVbnWWRwiOQ5mamJztXBhGlzIcKdDiIqFCku9Wol2x3Iqv9wumb0VDZLs-Qaw4b3E72ksA0tVN723zYDRQybUeK_xwD5-gZYPyQMBtCHWT2wIGo0xq6B1il3suXnlSZs0sVbVFvLOVdH3dO92lCwMKRQAuqhw026hjGn7pqQk2-XiE-LGbDrPwbLte07LOHVLAiZtSH2CSO8e2Hdv0nBhEJfYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=EJEDQfNJa5U-BIrab4iyxA3GrPp2tvUhyUvg1IP0o_ImMznKHgY0a-3aone4vBYl_B4OEK-KJdE8_bsgMjQplxlo4mx-PsaZc6Hvwfj8mjEYkPfrPofSDDVPcBFG-2tTGGIMQCj2gJF7xC7bPfw1gq9PX_EuYP2yC192BzmGhkYCRs4V3EYfdWnZKBHxO7mDe32jWrw_c84rDHuw7JReWfI3hu7AFGD0Fn93rTn2Bo8Fd03KTYV47EeLR9xMnD2XjxC7fulrR5nyHXH2q9HFwogKfFpOvlKBL9pe6pMHmtqy9fzy2yBeiF-Kex5dkWpCv_Dk4hVGdARX1lDxlRsFtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=EJEDQfNJa5U-BIrab4iyxA3GrPp2tvUhyUvg1IP0o_ImMznKHgY0a-3aone4vBYl_B4OEK-KJdE8_bsgMjQplxlo4mx-PsaZc6Hvwfj8mjEYkPfrPofSDDVPcBFG-2tTGGIMQCj2gJF7xC7bPfw1gq9PX_EuYP2yC192BzmGhkYCRs4V3EYfdWnZKBHxO7mDe32jWrw_c84rDHuw7JReWfI3hu7AFGD0Fn93rTn2Bo8Fd03KTYV47EeLR9xMnD2XjxC7fulrR5nyHXH2q9HFwogKfFpOvlKBL9pe6pMHmtqy9fzy2yBeiF-Kex5dkWpCv_Dk4hVGdARX1lDxlRsFtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDeFOPLvdJeIG6DmemRt3zdrqaSPUFsPGEMM_S0GrT39PS7vARSOAG5asYig3YnapNca-ftXpITRD6TIKRimAPT6v3LvE8IJC0iQol12oIgE-c9LHkFhkZ5PI9C1RjeuxBqVgp6fNTVwFRD5RLIK7U7B_bV5QuVnolU312LQp9jjXArEJ9cQF_53blsUZYrZOvTcdt-PuedPZ7Xeo4gUmibIX5cQpb8aHcphU4xHDF3_d3rfraMGw_4z6v1XQLnnx8DOi2aNXHCPuVTbwt1f7E0PGq0XXhSg6y0_DZ1EKy1Xx1MJb2gpj50VksUZFD_LLGk7_J6ydVUdPc4sWBcYhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUI-1Qak7IOaXmkAfV-JebDXD1JAQxI6_NIqyk6Q1XY-ep51H__fef-QhmurRL2_qQebnIMUbeHfmhElKeVbLL7qoWAF9IiNzqZGmqQL__t52IblrkKsKNkzeKqKaK3Fn9iPlasviJH-sWTz9BNrwc3bG76G44pRpmS7PuutSkJhiIbfWtJIDD2YzCN5fjyqTQHEPxL0r4KgtI3GkDoYBMGxI-SPLU4SvkE7VHyTrSefu1SFP2hia0NhJwZjFMf3FcA2IUf4t-am-BySTq8qqxvh7uLO6vt4er79KfbVY08bhvAVmIXYrvI-xpNZCC8KvKxgYoPu8FbL7x9auiWC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZf50uGdv4ehu8kBZp5qInwpKfo8WBUdhtaK0AIDwClhqZPIslBtBb4td1W-Jr6BbVtfXUjR3hLmzz5Q6PqDb0uR9qGtqWUSzC71vM2JjLATSYHpWDH_SM9yslsE0zfzUgyRK1rFALf2gERlHdJ5p9c29h-VcQ5rJrtUXR6kDtTfz715-J0RJTP5AuZUtyNVdG_SnXtPyWHyUvkqU6e5nYMtw9dyRNjz-g9W2GVYII9AEeQdG2lMoeZ7JCTMoOwGutb4u-D3ZtxgRQHHpG6Nygm-YuKFbMbv-t4LXIjMPwjyFxPvj9QzZ4P6GAxVeMMz6TYcpQJ_AK52I_k0X61Jbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1ewyjJpcRQp9LaKk9n7_9RZQVMzuWM8M6X5ltju_kCsi7DFZ2YEU5XjBuVtEQZC_OG1i3qqzk7cWpHeYYMOjzzxNY6TPohWyZLhNOHVfNT0PrSsSdb_g1J960JJkMbNLJJCw1JDefgTNc2WM6rX_x7YXdM7XEGyMv9Q3in1v7PrLR_giZ2MRTCL9RXiJuMM-Mh9Yy6PkLy29EGmknZw1T5Wo0aeRM5XrDZM94A9Iw3DhQOi0V30ab4OQrnNTDjdI03KElC1LNVqtBqcCW_AQPkxnCxrp2HBuYnj6g5uZEyiNdUPWQ1-XJJBAWd6DBaXhz6QNZOmnr9XGw-9rcQScQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxT_wJzpmI9FKyWRe1boStXBGnjjvvVju3LjVYEQ0iZkrNB75KZRWmg5gBAbo_AoJ4MAETVaCiaVSph6Im3ksAEhrsiX58Ux85YjGRhHksnQUHZZcJ7I46MMzJvV4ebtGuug_nBmEUKJfnQ38aTxZxDTjoLZXpTZzJuacN4xh28YE16E5yhMlNRuNW0L6EnUSIbUfux4mX7L7Iu1AYOBvEL49l-oYPC2ZeXFbzb3hzXf7lrwLGgOd9MrxqLGbtIKID1GApiD508ndQJnVIuOJgPiDnnqnp488IPHoUb3qO8_0NgJlfAjIF8kbRTQXyB6IKIYHmbZ0VoBrx9JjBIu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bfAKbIaiFRTqV-T31CCLaUFbjBPxnqcAZvGIhp0PxZ79FhXrynCxOAd3n7IJsyr8pJFdmjkCEjlF3bYG9hK19pkEF0aB7VEZf63w3O5Wd7QIyK3NC-71Irv4FXDGDGCEYxNPH7haUf7Mumm0ov8GsNDZ16SOfzCHmRieVI9MF_ZaadEqaZ4b3iuI0_Gaoggx2FJ1MFo_zveKV7FhjBwVE-POjt7rb7pCcmKtJ6bS5ruU-r6WipVZaN7hL6u2CuZpILEcXDFIM7yvRQbvYSsbG9KV5w3W2j70uzigV3tGR2uIptZbcutKUsKpBoxtzrJo5n2cWpvquRRijOJBdPItM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bfAKbIaiFRTqV-T31CCLaUFbjBPxnqcAZvGIhp0PxZ79FhXrynCxOAd3n7IJsyr8pJFdmjkCEjlF3bYG9hK19pkEF0aB7VEZf63w3O5Wd7QIyK3NC-71Irv4FXDGDGCEYxNPH7haUf7Mumm0ov8GsNDZ16SOfzCHmRieVI9MF_ZaadEqaZ4b3iuI0_Gaoggx2FJ1MFo_zveKV7FhjBwVE-POjt7rb7pCcmKtJ6bS5ruU-r6WipVZaN7hL6u2CuZpILEcXDFIM7yvRQbvYSsbG9KV5w3W2j70uzigV3tGR2uIptZbcutKUsKpBoxtzrJo5n2cWpvquRRijOJBdPItM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGvhmHdat1iq7BZSJ48Q6H92wqqmC6iSateHNMv9prQfzx110rpX7WugN05UQHV8qZpYpQQFN7e3xHeI9EeSBXZLL6A-IpBTsDe0lr_ke3yj7AS7BlD00wStzq1XTobE0NmY17aYA9dJbOJBKk8dxG19LodT2o85dq_or112Z7zB2QcCwIFlArz-7psQh_pRrSzoe6GZSq3cIe_reWjlVb8EBspSJuBwD2SK9994qAl552vlPHv3LgaCmI0H3veIKcsPYzBBsG_CUgYYo2MldIMLbeXloxc5IBX7CyfMzjZUC4qGlBC8tLfD9I8ZSfDlD1nF_V_zaflX0TDuzRqKBYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGvhmHdat1iq7BZSJ48Q6H92wqqmC6iSateHNMv9prQfzx110rpX7WugN05UQHV8qZpYpQQFN7e3xHeI9EeSBXZLL6A-IpBTsDe0lr_ke3yj7AS7BlD00wStzq1XTobE0NmY17aYA9dJbOJBKk8dxG19LodT2o85dq_or112Z7zB2QcCwIFlArz-7psQh_pRrSzoe6GZSq3cIe_reWjlVb8EBspSJuBwD2SK9994qAl552vlPHv3LgaCmI0H3veIKcsPYzBBsG_CUgYYo2MldIMLbeXloxc5IBX7CyfMzjZUC4qGlBC8tLfD9I8ZSfDlD1nF_V_zaflX0TDuzRqKBYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=jGR006EkSzcw0C55XFnj0TQ9iVH11jzsRFAQes7jr8W44zNF_cBsxhfqEduOQam8ci-KDRFXssVobO5HRFU3WjtMWdWgYwjhY1FdPCDOcIgebAAwZ3vLKBXY-9piZMKcq6DDYThO1BmxSRgvvHtra27vNqEI09SFwlYHjLdPiDOuwlPU4C2syxxTlTnBEQCE807mRV4Wlmw_DGbaPWFdxOmtX_km25vP68p-bSwhQjmtmb-qFFAvbCzk-Xpl9pc92qTjecqbt4LuXNJGYFy1JV3cWoz5tQJQ09_N4ydjZ8GmMxJwRIj3g9AojuyxZUSXLegQ1rywghz6GMz6UA9hOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=jGR006EkSzcw0C55XFnj0TQ9iVH11jzsRFAQes7jr8W44zNF_cBsxhfqEduOQam8ci-KDRFXssVobO5HRFU3WjtMWdWgYwjhY1FdPCDOcIgebAAwZ3vLKBXY-9piZMKcq6DDYThO1BmxSRgvvHtra27vNqEI09SFwlYHjLdPiDOuwlPU4C2syxxTlTnBEQCE807mRV4Wlmw_DGbaPWFdxOmtX_km25vP68p-bSwhQjmtmb-qFFAvbCzk-Xpl9pc92qTjecqbt4LuXNJGYFy1JV3cWoz5tQJQ09_N4ydjZ8GmMxJwRIj3g9AojuyxZUSXLegQ1rywghz6GMz6UA9hOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7lEqPDkzRhcORDL-Nwamknl4_6QotTyQuatGHyHIw9PGX22g-rR8t_VUj4QlDKoZufOP8JfgKiwyGAd3Afqz5Lp0qE_FCBG3AqAViWiWHICAA87pLKz2OaUMiTBOVhSqNtDXtSbw7M3Ay5N0J0bmcip2976Q68cNbOAWaBWuTzwfSMDCZkKmHuYJC1qqNZ9cnVFiPvIlC6HvzB7uurOwUF899M4qY1XDwnWEb-LNjkTuHY7D0HQxiV9Idu7mvxAZxj1SRl2ZYup4goGKznuvTjc95TfFmm9JltTZSkc4MxU6EuRNSVKdhJv4iEuRoNuOftT4jzBHxNNE1O7b72AOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWPSXdIo_JP_2A7vQAlqMwNtiqcyOmms8KxmLBF6sQ64PSB1_NKC8LelOKl5uA02QaeT2BaiYkmJerFHBXTPcxLSjkrn2ovnDP3L3yQ9MjaCmpzqPlADDUSlT8Y-Oqo839IBi-8a42yrB60P_nNqJhkhIceGutV4RSpRcSnYt_wu9ingCNoOWlt4vKs3a4DI-I5TTFr1MBsgjQQncBT84xVfbV-HVgy4I0fDvku9ApTfNjDzE6lgQe9R4ulgsO9_l-8b3PHGQMH47XErUB4SHqzge9JyM6n9vkBE6roZ_qh7PgjTXFFN93nzYwoaki70MOdQKGmPDrKQU7YTlh1yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Hp4O6vqagGsNRLNcjXFPWSt0cSCO7UmbzRhwVjjJKoQtd_mKaslcH0wiJNkQvCrEZV-3uJfupzjYVBvLUx7mc4Jg0983m2i6wzBgMk3l-C7UPbl3xmv51EzhMT861B0l74cB84gyXLNBJU_p25fSojCp9K8H5F4K6iTEZM-8kAfeVEIFy_Gf22HSMGn3UMe_BPUxv9QILASFZ0CeMS1jSG_dI7Qs_G0DFWT5vW6vy7QZfkDJNHjsnen7y8tsQHbOd38bVPu-HzMUFhLytWrzyJygKhM4wJ6KOztzDUBUVNSxX6mTz4EGilKpV9Gkvqmt-umT4FD76KStGwDygGzSQGPHP_bltAO9WLkpMFMi3jrIYKe3QGwhd82lp1DRRW41KGhBO2qiWerBVDOUhrW0C3EYcq5uJ_4PSnigEX0n6GeW-X-imI8sh9enRCoJLSeYktgjtwJ1u5PDpuEFEOlD2TKhQFvbYU4M-1jYFJBF5C1l7mAbXTkaPBQE6mFQ0_AK6ttBp_QQijEEFpyUAFL70S-FljyXTgXZEh_AKxx9tjlORFs6KEkAMtch4B8FqMP-FgOrGUNKa--dJOlhu5DL-pNNVdcIWgD0VlML7jrJvPtO6jTtB8lelQUdtBh4vjTbb5HV1wSPbYaqV8BlZBeOQ-473PZiX3Rq0Eper9otQn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Hp4O6vqagGsNRLNcjXFPWSt0cSCO7UmbzRhwVjjJKoQtd_mKaslcH0wiJNkQvCrEZV-3uJfupzjYVBvLUx7mc4Jg0983m2i6wzBgMk3l-C7UPbl3xmv51EzhMT861B0l74cB84gyXLNBJU_p25fSojCp9K8H5F4K6iTEZM-8kAfeVEIFy_Gf22HSMGn3UMe_BPUxv9QILASFZ0CeMS1jSG_dI7Qs_G0DFWT5vW6vy7QZfkDJNHjsnen7y8tsQHbOd38bVPu-HzMUFhLytWrzyJygKhM4wJ6KOztzDUBUVNSxX6mTz4EGilKpV9Gkvqmt-umT4FD76KStGwDygGzSQGPHP_bltAO9WLkpMFMi3jrIYKe3QGwhd82lp1DRRW41KGhBO2qiWerBVDOUhrW0C3EYcq5uJ_4PSnigEX0n6GeW-X-imI8sh9enRCoJLSeYktgjtwJ1u5PDpuEFEOlD2TKhQFvbYU4M-1jYFJBF5C1l7mAbXTkaPBQE6mFQ0_AK6ttBp_QQijEEFpyUAFL70S-FljyXTgXZEh_AKxx9tjlORFs6KEkAMtch4B8FqMP-FgOrGUNKa--dJOlhu5DL-pNNVdcIWgD0VlML7jrJvPtO6jTtB8lelQUdtBh4vjTbb5HV1wSPbYaqV8BlZBeOQ-473PZiX3Rq0Eper9otQn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=cByXQpLunL4_W8MM_-vqxhYZOYJAEiGlz6g_P-9oiDDGTm64MN0tkpJlcyZOoL2VdJYZfsg97WPtgXJpSgaW14iEWuNpm9ozTBmOvPY5qvnlI0-Ac7IEIGx3JOPnX-bhNrTnWOZRaarEckOFzb_QtBpgHVFLY1-Eggp_gcaqqfi9WO2zkxsQd1DNis9CxDrYTq6e5XAvlNEaJNHtljy8_TCPT59GzouAmw2SGX3hqSF1q2NUBzydyMXR_Zz1llHi_mw83c10UB9DWzeqtvdB80OrFSCHeH6901TpE7lilhtRVr_VFeS2N6Y63vpH9lQUnLEPFSkjMChPVm-_pBHhXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=cByXQpLunL4_W8MM_-vqxhYZOYJAEiGlz6g_P-9oiDDGTm64MN0tkpJlcyZOoL2VdJYZfsg97WPtgXJpSgaW14iEWuNpm9ozTBmOvPY5qvnlI0-Ac7IEIGx3JOPnX-bhNrTnWOZRaarEckOFzb_QtBpgHVFLY1-Eggp_gcaqqfi9WO2zkxsQd1DNis9CxDrYTq6e5XAvlNEaJNHtljy8_TCPT59GzouAmw2SGX3hqSF1q2NUBzydyMXR_Zz1llHi_mw83c10UB9DWzeqtvdB80OrFSCHeH6901TpE7lilhtRVr_VFeS2N6Y63vpH9lQUnLEPFSkjMChPVm-_pBHhXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_3ugsR_An3dMJHyKCxHyYVcn_Egry6nWkp5RhaLPl9ZaXjve3rKagjlP4bInegw073gFFjJt6miD_ntDWuaIJoNwxTmomhEfQXAHnlUQ6WuHY9sJJVGWhE6OLkMq9v6RgyCBHve1CdXdfJL9uNtUMuR44RtbI7K6VvEm6xq07Jxddbncu2JEvalaKG7f0o-c3pG72xNoY-Fnwa1fKx9HW4-aWtihR8CDkdAiNxDpiLPbE3-WjUg6rXUpH2-daSOVv_JtSZMPy_pLNcto3bKoGdkD3OQ3bob0enlvdLYO_GjkGxd59PxRTfEEazEYN4h8m-moWBYqIaG5XhzVFaqoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUfaTMx8ORoWGymOrm1_qazA6cjoQOR7NqFelO4iJ2cbq3sGTGmFV7USDNE_cc1DmsYel--HGzhRpN4_w-jYh6YbkRFw1rXk8ygBBSnTnhOWCawUXB3MoJ8mdT6XiAG7FY6W7F21AviKxdzDhfVOPyrR-d48V0ubVYAkzCz8I7OA5P42NUwCy1QEhjtzOWegObaSQuxZlDYr6d6i2frIl-Tj1jZPRP7-V08Bfep0SbD6ZT1d2HlyU-B0C87UL7gXGTf4GtiPP2KluLGpFvm09-hEVm9d7TukLjnocJNBv7_F8G60Rcv1wpRk0Ediu4Pl-rHHCKOGz6cm_U_8Ue83vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Esj2hVdrKtYZEnGcHHqgCii-3rYPQSCvMwdkhD8W8pUrGDiH0ODGjU1Z4mGjzZgfcy8bp0hdDceVIobQ4isMK8rohDF8Z68zZeHEzKzte88tiRe_Ad-Tpp7nEgjRhSUwUz9DmIsRMTIlSNkCA1xA8Ot8maK6ajWMDElJI2unoVpOlPljJc8c2inpUUWGl5H7e1CX1yAsw8OWRNjyGZBADsO4gjQzrUby9UX9BynkGPZ9pKKSLmp3rhW0sjNcCqSYNVmcEwM1sbl2VxQcJRmLBZErXEiV8NORryDKZCInN4vclQzduccIXU5uYaNlhVF2IOlQR0sxZBSgAox1j5ubUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=q1zN7bbZUa-l-M5UacoGRJAuaNl_rKt3dpG6zTgBJCAEhImtscdXrVJ9j1S5AV_plFcplgYS2Kcrsck-2KTgw6QNHffbutSabWAPrIFHk8pmmY6jGyA8m_ANYws5hs1-I06yLA_XXJmSnrnvkzemqgVYVMLf52VNqaWq3OSEmvB3x3WHyIQv0HJWQyCefeMdgrdVQeYeROJcHOV1aGYokCtL-3ETtrFefAulPy5NqY63lw0EjTTAD7l9xclgkthAeLNt-R8T6DOoL11yFL-5NmM70tequ1RTfgXtC7YPEWS5mD6gTNw4tY6gArg0gaNqXNG80uqtM0nqj8PoNZ7agg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=q1zN7bbZUa-l-M5UacoGRJAuaNl_rKt3dpG6zTgBJCAEhImtscdXrVJ9j1S5AV_plFcplgYS2Kcrsck-2KTgw6QNHffbutSabWAPrIFHk8pmmY6jGyA8m_ANYws5hs1-I06yLA_XXJmSnrnvkzemqgVYVMLf52VNqaWq3OSEmvB3x3WHyIQv0HJWQyCefeMdgrdVQeYeROJcHOV1aGYokCtL-3ETtrFefAulPy5NqY63lw0EjTTAD7l9xclgkthAeLNt-R8T6DOoL11yFL-5NmM70tequ1RTfgXtC7YPEWS5mD6gTNw4tY6gArg0gaNqXNG80uqtM0nqj8PoNZ7agg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=T1ZV3b9-LUwOxTnnqO1LJlG16bZ4cOMjhdOl_lMp4NvLiMi_x4uGHQ2YefwNp506Y-GDKkCtBCCuo2R7lqYd9C_VqxTrnM7EoMPjAIqtP3ilkPQj0VE3h6WQB715fp2SVWJ_AIs96BTPT3TtWGgrB-Nn4LTAscHyq7kx3NYfih555P-NEw5IRm_PwpC62oROwYDvnCaAgD9z4hhJeptlSEofI-uK92cj2KxVMqRlzQrjQTDpaYUJYq4w7vdsu7hhmgmW_bkW_f2IQz63Ss11a_5TYqupd1by0TOazMu_XYgmy6MahJ4fFDKDsmJwjpbHNiBuN120IwnKs1KshUcfNg5rtpXx21cno3rGGPnlJqyCdKYzBaIWwwuqgzdVdNbwRRZ6I_12BSb4VZntfjBye8GUYRXd5luo-KoOtl2HCtu2Xjej4UM50UyRaG-3v-ySAd7IyoPYTFYjfNefiJxsKxR_BWVrfTN-qu113a11npLvJjbogKbijFRIygwKyiIZNrlvu63LCrYJxgU-TC0xx7As9b6_kmMBNt4fbLomsE_npmghOh1E8aq4pe9PnClEOzLiNMTCv6u5_ZYlWns8Qqhq0QNhN_vN8Xby6q5baAhFUj2-9qIW6n7ucPwTNEwFz4FdxX8pK_AoZcsTF6qe_J4BZTLUe4BehBee03cioS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=T1ZV3b9-LUwOxTnnqO1LJlG16bZ4cOMjhdOl_lMp4NvLiMi_x4uGHQ2YefwNp506Y-GDKkCtBCCuo2R7lqYd9C_VqxTrnM7EoMPjAIqtP3ilkPQj0VE3h6WQB715fp2SVWJ_AIs96BTPT3TtWGgrB-Nn4LTAscHyq7kx3NYfih555P-NEw5IRm_PwpC62oROwYDvnCaAgD9z4hhJeptlSEofI-uK92cj2KxVMqRlzQrjQTDpaYUJYq4w7vdsu7hhmgmW_bkW_f2IQz63Ss11a_5TYqupd1by0TOazMu_XYgmy6MahJ4fFDKDsmJwjpbHNiBuN120IwnKs1KshUcfNg5rtpXx21cno3rGGPnlJqyCdKYzBaIWwwuqgzdVdNbwRRZ6I_12BSb4VZntfjBye8GUYRXd5luo-KoOtl2HCtu2Xjej4UM50UyRaG-3v-ySAd7IyoPYTFYjfNefiJxsKxR_BWVrfTN-qu113a11npLvJjbogKbijFRIygwKyiIZNrlvu63LCrYJxgU-TC0xx7As9b6_kmMBNt4fbLomsE_npmghOh1E8aq4pe9PnClEOzLiNMTCv6u5_ZYlWns8Qqhq0QNhN_vN8Xby6q5baAhFUj2-9qIW6n7ucPwTNEwFz4FdxX8pK_AoZcsTF6qe_J4BZTLUe4BehBee03cioS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSCfEU1v0g5f8iHzuuEzHEtIkeNhvwb8x0SHdAfBIgYmsCZTxiVB7OxCPOzeJxN2ZVNW2iJd-BHlZzXoDNlOpimlgBGelkSiHWZirNeZo5B0NcQc3P5uIawzVOzwC1CLrrBkvoQqo1nC121qJgiGglEhTrt42tkI_F9YAWsCkJWS1iR61ShnuBZrZUJJrEYMKixj-7wM857EDNkWr9zlmy8fuGz33XOnYgiULYgAIdW1R8bGxLfmS3OJL-UYIbvQNhQpv3LDjc15HkF8BxCf-tt6RZ4qEu0J87pHsTBNbFLJeHd7u_pUvFeNTkTCf3g4PGeOPvXEwdvhek-EdtpHdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZNrF_ZToaL_-6u0uxmou0MBVGHpZae6tRfvn1CrDYznro6mIRruys9OKYTB3u96sFRJ0TktFW8tUD2XqlgDA8z-04z-fDljgGG-sxERcLuELBQfkiTTU-8J4Pn7eJOmV1dZaE5WwEEcSPf7Nq93XysD2EBdYIaF4U3sv9mbba_YcR2nsUJh6HZwLDSpYw30034iBc_t1rhNJyqbstB8tpZ5rnd_6z9Q6LY0pFNtfQgByUZQPguPr1Ok805yDUzanHQ0QLvKuYoDHoRO7Ql-PYcyIxvlpmLRDF2L98y6Q-td-fCvNdCUoYgxrZSmnPQmU-C5GIwEjbKz9wXyGDUquA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=gL_A3bBih0j1raHG37zrTr2MozGRAJrp8fP9YNdvqFf4R0Go4bHOVe_Kjsalm7ds2cpId6SdHrL5G8zeA_7PNOyGyJcMk0BlNfNV6E02QbS9qO9qpflobP9N9n50ofbNz-afRNDlb3UxO0HtczrnuRkjVDYUtH78jqtP_3yrKtf9pvYQgjzFFvGZ4LLSdkWI-2wsVBIUt0ZhziX6ymqba0ubcSHOLOJn5YreuY-xw_NdPsytZpCAXf9yOOdKjU3QCB1hqx9toXoO48LriBYzjfGOKYMpgNom8EIG3-FAVdjAoAGmlOFDAUlUXmXa5YB9Qg57wTUZtdo9-qzZiivv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=gL_A3bBih0j1raHG37zrTr2MozGRAJrp8fP9YNdvqFf4R0Go4bHOVe_Kjsalm7ds2cpId6SdHrL5G8zeA_7PNOyGyJcMk0BlNfNV6E02QbS9qO9qpflobP9N9n50ofbNz-afRNDlb3UxO0HtczrnuRkjVDYUtH78jqtP_3yrKtf9pvYQgjzFFvGZ4LLSdkWI-2wsVBIUt0ZhziX6ymqba0ubcSHOLOJn5YreuY-xw_NdPsytZpCAXf9yOOdKjU3QCB1hqx9toXoO48LriBYzjfGOKYMpgNom8EIG3-FAVdjAoAGmlOFDAUlUXmXa5YB9Qg57wTUZtdo9-qzZiivv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUcFwoTMSmvTtm9sIiRD-E1Gl3CN73BZTfAWl-icGkVK_M4lg7VrNbHhB7Uye581edBIgGtoKg2jnoco135rD7wfke9G4frDco4Rs9nx9ouU-WBbGAjem6fkbz_-vaIci_CustYy2n3WS-rldRlQJ_XiTXJfDSOaXN4-sml5LgdmtBZm3eGZwWRek7mwj4_DQ_lz6tfzxn0ufTRTSDRNHxoNcmUt7uc7Gl5gosr0bmkC012Ur3AQwxqS547TcLml_X7jr1yYEwgzz1zzKHqjlWvN42CUH7B5zJZh0pW6cHUukx5Kk-J_CCioIzXFJm71p00mV77OYh7zpsd-RXV8UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDEcoevxKuL986-rts9znHRT0cM5vaQAczbY4fgh7OzPiLWPgpbnXw5_F0To_TI1l317BSQk3Ss6hXAwggT_2osAnEqjH8da9k7HznM1s1fQftr3pZXOjc-lZ1ZBVdC77_LMxImMUKZuknju7Z_rSRMOX4opxWKlB4wt7F0vs8tBnCa6xqdbZkREH4ccb0g6UX9Tl_bChMPtD22ad7u8oBFLIkTY-pAfpYxbQXVS75kgCMR_tNGwCuwmah1-ncbx4U-AexeiCBZcZiGodd3TnLuWHhjn5WbX27konE9QHH9rLBq1VJJoLl06z1iaviyOXRBsORgY-5w5YvksH-Uaug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iajr1CBekd--DsmREoc_jYN5YNGzkNijZDMRkkTGtYF5WgV6CCAmQ4pMoDMZo3bBlIOie6ExN3-knXzn8eviXEKdMUL9VwZ0zk-kpbwGjZj5sJojQmZFPO-2vAxmOWLURCd1Fc8iCzo0zyVHWozW1DwjmkM_Ixz3j3l-J26sx8oTbHmuA60STcvvUz5qOdWuzlhEYHiQcOKnKbNn76AzI8uDn1AuY8qqbOB8CDRkOZ-nWuJdbegiBH17AGlkBYIbag-1xwgzABr7ydjzcGfyHH48QQSoOZvWvoq9923xWYPWd6wR8CkjtqByv3ttRqWwxYedy6jBQl5IlVYIGkI6Ew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLRVqK1yE19WcztxHhPKDStodp3XExr4VCvHkQwgYPOstfINmGs4jnKKCXIoTxvxpeDM7eqt8JPiMd5Jj8aBzGNtdfmi2YTgL8TdMwvtUF2ZvzH26YNHDmsC_-5odTDDyKSmdO6xLH-mRxNnoSiZeKYpVZEhSz-WcWswOXdzi3IECwsCpJq8sDHfzvqQ8M17QwnvVq9KRnB_i-cC67_0L6qG5xi46oWxEJX1f52D7taHelHr8u29Ooa20j_wrP3J-yTbrT9uYyJUZIxlQXFvPsT70dMph5BUrh4bWd9An3nlDSY9KraBoF3QOH-PDZSnakQxm2fjhecHNTvCYRJAN5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLRVqK1yE19WcztxHhPKDStodp3XExr4VCvHkQwgYPOstfINmGs4jnKKCXIoTxvxpeDM7eqt8JPiMd5Jj8aBzGNtdfmi2YTgL8TdMwvtUF2ZvzH26YNHDmsC_-5odTDDyKSmdO6xLH-mRxNnoSiZeKYpVZEhSz-WcWswOXdzi3IECwsCpJq8sDHfzvqQ8M17QwnvVq9KRnB_i-cC67_0L6qG5xi46oWxEJX1f52D7taHelHr8u29Ooa20j_wrP3J-yTbrT9uYyJUZIxlQXFvPsT70dMph5BUrh4bWd9An3nlDSY9KraBoF3QOH-PDZSnakQxm2fjhecHNTvCYRJAN5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLEBKdJCMZEscnfTGYs3sNoDt0z5YEB9GOUigTcQ-KUwOBKgfEyy6DWFK--rOfoQQ7bxLEJHz8cEf_XlkuAOCnk80Kcov8ezdCUzIh2sYehNYZbaU3eipq8-xtQ59-omuDFNXHmeHYrH1G-aVvMq7L6C0Q_m_uhyIMA9vDCiPr0uIXDim-Lq3VTNogCcoOGrQZq_sweEFPW6P56l0QyzAkKQ02CKx7QJEqO8V-YE48f0cyLpacajOHwfmOU1l_g-MpbrM5RrhbW0T16kTxy5MSbOP8kfkVTlrCPaedDKyH4_9x1TUfM2L6LDSh12y6VI7TtCiYvqTKFUCZbsR5o2FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm7OH2enot0rW1sH9GhZipZ4vJ31rput37ywj9zAOo2d7p4POUKVoikgqeWZzolCGZgD6HPqV-iFkafICsOdNWpY4phUHlRFKfNefQ3dx3v68MASB5QL3_gfLP3bw6WxISRvJfhOJL3Y1L8M8_WDl-G42sI0tBLT6ay_OPzuSgddgR59pLIQ6S5lBWibiYHeV6br-SDfGos6BPZlxdywHHCRex0YtAb12Xn1l-mcuSU1ldbTsF5eUDQ6oQ9wbJhxjEsHUZQFUGrdeKGN945uOq_8wjirb0V61H3VriazDjEFTjPhvmrySDxiQQXLb7ZzCm3FjN5RuglAxp_74glYYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=MaR6zYek3-qRnt5sG0fWcdoRyaLdAUPyZ0dGUgFNVmW88J9Va9JC-rHtKYkhWAWXCXWw-pOFuHC21K1uvuJilKaDa-qQpqOxOToiYE7aoBztMO5EbrHnvcWSLpA9LJ8oYsAyFyYIOtl4cTSzRy2Pv9677P3ITUIuzNcGgnzZQeIrLeW1x4tXR0oyvID7iItedq9eUPHheZZqGpsFklCIuQuFxAe7-__von1ZKDYEV6tUpyskorGDonpQsfFFQfnHXmStbSfnzqL4rTLv91VaR5dkGbGWA_E3N0sB5kkHsbD5uTfiaOnWBER2YNLVoswoBRcfCnpHzl8QOQVLIzOw2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=MaR6zYek3-qRnt5sG0fWcdoRyaLdAUPyZ0dGUgFNVmW88J9Va9JC-rHtKYkhWAWXCXWw-pOFuHC21K1uvuJilKaDa-qQpqOxOToiYE7aoBztMO5EbrHnvcWSLpA9LJ8oYsAyFyYIOtl4cTSzRy2Pv9677P3ITUIuzNcGgnzZQeIrLeW1x4tXR0oyvID7iItedq9eUPHheZZqGpsFklCIuQuFxAe7-__von1ZKDYEV6tUpyskorGDonpQsfFFQfnHXmStbSfnzqL4rTLv91VaR5dkGbGWA_E3N0sB5kkHsbD5uTfiaOnWBER2YNLVoswoBRcfCnpHzl8QOQVLIzOw2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=J0DntFHjL1zhwuBph5_i83rkv8Z8KneFI7CfZGh5wyaCnd1sundZm-cSvbPiaVtpTS-3b6W9nIpXoPHS7vHmQmYtqXhNGN3IkGtpvlYgTNHFOBfeq6kCYY1e4B53oBYnWj0BfYpZ2PaDUuQHWBMHV3sOgWFIkoNI4UeZH1sBYnOkJt-xWWVVuHtAKFfVV0ILstLI6XzvH2HsyCWLcPq_HKFdMXxdetELizZgeUN43NSV8JzhSXoqf-X68DJnpYG4rSFuajRY-d_gIQ7HT3eG_mBb5nFMtHuihfD3O9rCOqYyGrOOD-7i2FjAs4E4oAxb8JqsOPg4GjvJpyp6VnWh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=J0DntFHjL1zhwuBph5_i83rkv8Z8KneFI7CfZGh5wyaCnd1sundZm-cSvbPiaVtpTS-3b6W9nIpXoPHS7vHmQmYtqXhNGN3IkGtpvlYgTNHFOBfeq6kCYY1e4B53oBYnWj0BfYpZ2PaDUuQHWBMHV3sOgWFIkoNI4UeZH1sBYnOkJt-xWWVVuHtAKFfVV0ILstLI6XzvH2HsyCWLcPq_HKFdMXxdetELizZgeUN43NSV8JzhSXoqf-X68DJnpYG4rSFuajRY-d_gIQ7HT3eG_mBb5nFMtHuihfD3O9rCOqYyGrOOD-7i2FjAs4E4oAxb8JqsOPg4GjvJpyp6VnWh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcMvi2mG_3nx_zdUqZUviMFffE31np7PgFP1BgUtZgsOeBjD0HBEibvY6yUH8sA05E2ZlC1igMW1Oz-o1L1GKwKKwbL3Wi3sYKiekGcw6VSVZyF0a_uRZtzw6JSZsz3UftfMTBzMoOIi-owTYePbaGmuzCgUZnrFmASQhdiSJM6lEEuezuix_WRmMxtki2PuinKYtsF292-HW7Iev_Uw-nn1O8oZ18Mq7-cvcJWkHTB36wjYi5l-xODo5fL805khJfllwvQC5h6pJ8YTU1I7cJ7qgMRqE2oDmGd65P1VUqbHjvF11u4VHEW_DfAdtYKvm7Fvpqm2hXl92BzdnMJvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGU0HU3fufQemMQE7vWOs8xoXSSpTdVXNfv9GVNQbPY4_AcH6CMxO3Dnlz4UybDIrX3JuGvDvLRQZO9HXDFQQ414uaA8zh_rRuCRiKbzNcpy51eZ4G1MIBjjc9XgJtVaAyhQpTRpaqc7FY7R9vLg8K5uDDfKq8d2DUBL4MobzxZonswr_XUdhoeiI7s8b0iP3QlE9p42kZPodAHNWUy7yb0DTiXOa7zJZvsWqFd57kVgkPuYWga6iT1eGJhRkDZzasJTS1sxHJusE54kWlIVHctdW8x7J8TxU2PgTK1LBMapXOFmuB3BW4DMXonCeFaUbyOuZVKNDAVnkbw9SW5vtQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=DjBEmIGNET1X1ja8BHZJdmLtKdhtHdKUuWKZCrdC1igrukW1h7cdoTjoRyUmp0NHnaQHdF0zJOOt-7nFbFXRujk2K3CEfVAHm9EQIhV8h126GsuGMf1O1nc_wh36oVJRYNpQ4ML-VWuWQWTMD-5eX-_g-OiU2CCz3we8PMnJ_RKHOjvS2VhRxfdhKHFvNCUlpeMEuU8hec-xms2t6rSqsaN8sja6FMOxIije28b-JD65ViCht3IJBTf13j2gEpIQR2UefNkgbmXC6i2uXXc_ezN_5TJVLz95oK5uHlIIYWUycg5wZ__UxTnyw_IYJUQsi8sVel40kNpyfU0ZB_nSiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=DjBEmIGNET1X1ja8BHZJdmLtKdhtHdKUuWKZCrdC1igrukW1h7cdoTjoRyUmp0NHnaQHdF0zJOOt-7nFbFXRujk2K3CEfVAHm9EQIhV8h126GsuGMf1O1nc_wh36oVJRYNpQ4ML-VWuWQWTMD-5eX-_g-OiU2CCz3we8PMnJ_RKHOjvS2VhRxfdhKHFvNCUlpeMEuU8hec-xms2t6rSqsaN8sja6FMOxIije28b-JD65ViCht3IJBTf13j2gEpIQR2UefNkgbmXC6i2uXXc_ezN_5TJVLz95oK5uHlIIYWUycg5wZ__UxTnyw_IYJUQsi8sVel40kNpyfU0ZB_nSiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=T-3v0_Virl4Bn6vasruARIFigrQ2eSQLnCmtDJWE2-scLMY7VlZexHkzzd0VobjFaD2At1FY5L3C9jUxzvx2WKZVZ8ALJXrCx_mGs_vB7kmMPVu6b1qMCQ25Yt6PY50IYKQFgLzQvMgnThutVYu5R5xvM4nEpMs9PM5-JhF4RsJH84irx3-S59rPDptZAsO8426MmO7SFX9FR16bLoJlEFkf-BZnc0662oRi_FnoPdteYyZsb3cvcgWDf9fTtj9ZVpNauV4NGkO8NmnQ3qeTAAIF9HuO6Nl4y8YYU3dzV8HZMzyZXbSAgwGmvf5nic1DzCQKcVdeePkHBMwjwnt96g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=T-3v0_Virl4Bn6vasruARIFigrQ2eSQLnCmtDJWE2-scLMY7VlZexHkzzd0VobjFaD2At1FY5L3C9jUxzvx2WKZVZ8ALJXrCx_mGs_vB7kmMPVu6b1qMCQ25Yt6PY50IYKQFgLzQvMgnThutVYu5R5xvM4nEpMs9PM5-JhF4RsJH84irx3-S59rPDptZAsO8426MmO7SFX9FR16bLoJlEFkf-BZnc0662oRi_FnoPdteYyZsb3cvcgWDf9fTtj9ZVpNauV4NGkO8NmnQ3qeTAAIF9HuO6Nl4y8YYU3dzV8HZMzyZXbSAgwGmvf5nic1DzCQKcVdeePkHBMwjwnt96g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhMls5UuMhnn847HBjPYEXhIXvsyILxCjAHVRKIaK5wIOGDCxCxs467r3rU7tYtWAHvD0BjejUVn3CostRusfUY2rkXzk45B8LKnckj8V4RZOPJRGiIF7xxb9UGPYcQ_OJ9gDfmKzZbq-zvdu-O8l2uxWS_NKypXp7J5hupCEKSJxyb_Dy2Oyrmzk-Ya71-kg84fRw2p4jDLAz37zfzEgMSbnwstV7Z_nYbRSnwx_giSt5fJAMcXkORmmf1nfPT9nRIcgOot8tMTMwcIM3aMsLoKhXlcX7N9YTwm4HHOQolMIdXpnI1Nb5kTDgWrK7n5ytGRqd6Ige0KpB8qEvqs6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT4Cn4jPPg9B6lNL0nbmt-_NuugoIjusNVnjnxEBUbgMHzPBkzItnuLnFJNYvLZ66ncexcKaE3C9I8ofk9o4R-MDRHw0uLTSBUpfShWz3XLZiefgeiWY5qoOel1Y6I2zhJ4Rjn0sJbrnfkigHkMIEXl6U3UwovQbpkMZAjYjDbf5fxugPuBsxXErOu9xhYKPAJFaEvQm-xFQSv55QabQhkL79McwXbi5O4UwiPGdbUQbWCZmPA8tztOyrs1YRoAUw4-B0BpODKnNf6hGatdOk8sQ_cKoEp0UzjWzVbJWfTXBr2VLMOhf8rpNpNDnUo9H5F1zriXzslAZndu12Rm9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtjVKKiZ0bLgVCiWQQed9RU0P9toRn2F9LhPBQ_M2RRCrYkM52q5Odhi_nTWZ8dSiejVBdxROuhgAx2dIzLDuNH-JhyScBrI8lPzYx98H1aZ059T6mPg9EJHrIlUgeVte5u4vm7f9sxEoj4n41qIFiYcEWLmDx7VkfdZsf6lYzs57735rERctc04634iUongxqBqx81K7RDObDfDjSfPj8yLau7Rl2C0rcSUVE-lG7pu36Ze6047lUzGSFJPcZ1jerbO5oH5qHijTwl_d9u6eos2vY-Dci3PafODfJTx-lxMym7FhvOg-BwH0m3PpAD9U3BbHjRtzCnML2hD_0Gpkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
