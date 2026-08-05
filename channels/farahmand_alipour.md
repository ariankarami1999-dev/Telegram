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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 18:13:32</div>
<hr>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxcbJIctp1pqBy-vIPYMTXfkOLYCdVVDm8-Uvvwr3MTwml3DFKTfdgV9GGgBOPB_D4q3cVWSL55CN49zFU1oQ9MxtTcRHkDi2xHyuv18yIIE69cJeHy4xu0t5iPQb-BsTFskwTPK0SYkHHPEGC_tTASLAC2vZRt6yO0MLPYflJKVjiqovmNG53LDhCvxQZCxqS-F8tAUL-XojFOAk12q7V7FX1QhreXYI2tt1hc6ZdizKxO1JWCML9tNcek48j9MeaUBk5g9xuK-FNTbso5aNppDeOa9kMvYYzQapRYKqDGwmNTC8x_McUB8lrZDgQ6ld_jkMwgiFqws14KX0NXBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvtSvsV1bcM7QDFgdQMfXNB90H8Uw2AIoDqxs-2vOLWIh2-Mn54CpzsfOpp9bMHORlPY9EwN0TcByvoZC7M7yIp07kS37by5HpraL7YV5ifPUeTkVGSJEbZAmSIjbMeXWnBCkI0GHp2Y2OCZNfUOGZAd77Dtbd3P-dJzAUI9C-zMbwgaAJDs63HtrrKnAxfzvTAJIki4pH4kZ75CRx5pULvXrJuMJyR1aZLcBCwqKPB4xvI-bWZw8RSo2q2YuSvieJF6PS5ilZuTUOOmFlh_RJ4ZUoo34EjNkiRDBg8hMBJzBXtSMdyujdLP3m7vu8x2s-gkWE5u4I1dfHfXUqYEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecwIk7MdzeiOmAtI3huYKz8IBgEYx1uQrgOMebq433RwZpR89mvbqNk4SDCjP4dIJkFKg6YbT6QsdwxIKLnWYwdRrqWkfqCxw_wHrK1YGMraPfZtbNGnBMlgXqR2q3mMAsAUjgsJhpzoiqiSNAa05EbO5bl8ursccFNj0K6i_JOenLAL4ZBs9FXiIOvtSDJR2hUIWe7fTrYIJ9gtZVzc0LQX7yIPoU8jgWA13FljTCXe-GsakB4X1br6ccXijxUWd7yOaFlnB_k3ZAFT0_fRq0pmjtR-w5NeMkF10l2XU3HiznS3-5z9FnqaUeqtM5EEcauQmF4ZbJUEaFTo8aXarA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJyQnPgj7vOfE0EK7pBKZ0i8qFsUQYIq8ZDe5gRbvfAhV5NJZEIGn2K0TIAVHFSmnZDT0i7tRFiJagXuPDEuqWqJX8cJmbEZuJgQDT3L8VWzfForkcKBVluElTCjbAxe8EYblzqiuqjt3CEmpFTbY1DTQ-d4qoTDF_HsAOxwKahfdZhZ3L2pAoMlv3INrvgMumFPTitqoORW6NE3xIdtnG2Reu-EbBn4axidBYhpu-L_vjEP5ZaMNrRXNcQI8-PgxkUuR9kKdyhNowbnO8rWmpWuaeTbuW_vySC0ly3BsVrYtpoIxLtebTGxm0jDzV539Bhw_WKKDpCGFz2ia4mWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaMaNHjlqIfd47pwWe__gqzAwv3Wa12nVmhYzynG3e4wQcAKihShk0a0AglYarpbeSZxuXyUZyjK5O5TxazKySkUlOizCKywpdVqyLMi3OAOT-3ECWch0TGOdWQT-Pcw0tbKo33B_GcvNp7m_h1xCYGe0fpiP49q6Gzz19WlAEf7ajwneepuzShTLVSwc7vTYjykd4hxxuU-UwoSUciSWBNUl1gBWRQ0nFAYPU1K1lwe3BIyL00Z_WMXPAnvLkzabHtgBBmyxVTYxqfY_0EhnuL8CjO8RY00473NUWSAGWsSYxoL3Ho8ni8z08lUOxyyEy40lX1ZTTdGQtd2_x1fKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwYCAH5h39XhFjlrTgF2LMH4e9c-wDHnKe33K4JWy77fXUeCYOm7JCzGw6QYPRKiVPgPqqW-7ufn9av9oR3H19y469woFdFQAhS6iKHpHv-2nrN_9U8YjVisFKk-8pF2lHW2dZ4TSKLZjYNy6KOD_XnVwa-4W_SY-lKz7Pk7NdMgrpQl3I5UfQiPfnjh7aSEi8dA3j3i2aqVOxMdP5g8TVQNSLTJiEIcF6iAFpA6zQrjilE1w6qEc16riDCgiQFnOJ0NCgH2qjEi6mc0dMjUIqS9HhQI9q7YdlxfBDuoHwppsV-SB6Q7PzoNZvgVPfSnfKp0BhlNWLXXfvfyLQCevA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1uLyL37YJNAonV8Rnq6uicdN6aJqbIgKktNt6djv5LwraWfLRFqf7Hbaa8KwjryQ_HPi1Q2D4SMM4YR5j8uC0Eva01rAFV751cuZuuKq-H-9iwyRXgK04ZNkY1o4ZGS4X6OMAdpmsZlGSQ8Bvo1qwru48xZthFEacxZWOwAQVXjsYePpcT2yzPW3TZyDFIqoBXQ5AGsM7MI8l81Iul-UwTRtARKZ99_3UQ-3Zf18UiPpot4UxTu6Iez-F2XOjFKNzNg1EvypltujWfko_UqHoGBXplzDB84soeSha8ZJ0iYwYamlfyoBRsPfxmx2c9Y9YQOBl0WfM0afN5HI0_brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOxvOj7AKS03L4Wdf6z2NIpmcq50wv4RvcbgHa0dJvgLg7ilw1Fm63lLbFd1EpbEYwzGy2SwTi4TM8c7iyPdkwju6jRe_Xf2Q9c2d2iwWmJxRMm1LfWKLdyYh3f_pui2EtXZj8nc35gJWriBYhwdMlE7W6J4FuApo_dDvqXYqKhOnanMqb6LGfLT6UtCI0CmdEDycoD0eKo5w1dvKNagzwZZY_Mx0s5pN8FS3pzcwhuh7Z4BlUbxxo1P8hMmqPI_PjvCFu1GtBZLU_HkoGtY21hoRNDbIgJnlRbeXdOo1RKtLcB7gy7pFbMecs5eJTTnFbOKzwycJd35JRxaf90aNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-9ZjDUCZI26_ktlYF9hsKvFBibRjOzyAgsRf_RQ4ayv5BcZVdDjFK5MC39OUEas-O1V0Zs8HQkFMfnZ5KG-T9HLPdctS5vqUy6AZizJe0fXVM68iCASsvloFYsDRHhtdiNAOK2ClflVl3kKoKQtVyfhV2SP5rg6QgssCWr8GCY8WcIObNj2HCnQyCMVnIiizqnlTpGdzY2IW9RAH7TkthPiY9TtRHMxoyQocrfbjmrklnSv7xr6ZfZDQyPjg6U73hmSvlSXgFjnI-bD3ngZqX-KXE07A8_t3mcE9vhymsxahBTXQMbaJmlARBpcUScDhuInlptcbkWYmnl_bgCzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK-xyAeFI1Jejvx-FrMtd6T4OsCezmL-Ruwl7SsytfEv02dmVJUGpXx4Tic0h-cRRSAVHEbd32r8vAP8g9Ge1lIXh2_mGt6yMMTPnNL_o-MNHiOkA47lr6k-GHowAJmmBmE_GVJ9coABQimfyhwpVbEmnFVhABLKcVczRpdXpU7H9GYXkO_q2XFbVpF-JEllR_36fFggJDs3ziWUCwk45jDB7_vfQ8kmxfH_g9oFFG6plbUf399FCjaJ2ABkHQZ97TYOkr6TDZ9viUI0eSKUUP93QZhnYIh6XSP139HthtsTNlp4QmusguwhfuNh1Q_NWe_QVHC15BZhaj6G4wZVww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5HiTiF83JVvEJ16GBBiQUg08q3L6wnkkKl6zGRMX1-v0kxx5vqhpUsl8duvcXTwdtHuNVcQQl8SaywVZZ4vXEwgT9FM5jBRfEfr5dg59vL5yOsBBhcgsfaaTW9HaOGC0GWntpS8YOAqcft9fVSuBcZxqhWqEV47k2ugCcQkqMUC3VDp8EstYFpopY7G3rZuRVlJWsTmOhzqpKdwQYoWvJyEvXSxnEzsTKpwkdgxYiEOgYjbovaqxFI-Jt32vsstHS21x4huDMNT6xSZAcYxLy8Q191ENYj1jPIvBuRac-gPWN26Rl76iTOSr0OOGOWaGbGRPkfOqLLLm3brwGRBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=X22YeIHD5tsz2DUl4oxCEwIYrDUWLvqBbMIwRc2KwB5WpOGl_n2eLdMJXtfI-iqBHAf0qQpnzuBD8Q-mRBLg611uOKxN0C9-aUBcGtLVilo5b6Nd-M1XazJSMbhSJ6W7Ar6tOXp5p4Cu1t4iHXr_hnz6N8V0Eg_vz0E7BMg-8DKaulxa2WlTv7or3ZJyXXPqZBDwO4EQ0yZnG70cAbHfM4-MBBPqYQhzEjnH__6IWiNv_BrP_wEFr5-CzeXj7UYuGUYiF4flxa6Tc3wv9vXKFfevsT0Plnac8BSWNog4vFcbQAYJZ-Lx77bxPfvUdbk_zey_Rb_WqAnRT1HpHZXjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=X22YeIHD5tsz2DUl4oxCEwIYrDUWLvqBbMIwRc2KwB5WpOGl_n2eLdMJXtfI-iqBHAf0qQpnzuBD8Q-mRBLg611uOKxN0C9-aUBcGtLVilo5b6Nd-M1XazJSMbhSJ6W7Ar6tOXp5p4Cu1t4iHXr_hnz6N8V0Eg_vz0E7BMg-8DKaulxa2WlTv7or3ZJyXXPqZBDwO4EQ0yZnG70cAbHfM4-MBBPqYQhzEjnH__6IWiNv_BrP_wEFr5-CzeXj7UYuGUYiF4flxa6Tc3wv9vXKFfevsT0Plnac8BSWNog4vFcbQAYJZ-Lx77bxPfvUdbk_zey_Rb_WqAnRT1HpHZXjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5wEfEgb1ewcJMHRlBeQyI1VpQUAXTrjBxPvhHL0MG-cDvb12ba2aIvBvdh2_xd6HDO4cjt0B6ZizXruz4oPia3gRAtTjieDoo69MbILyFquvw2-iSIhHjcbJdBEHPQDRALbUy5fdhFedrazwKl75-FLUjcxHB6jsSpHCDoo1pFltpHQ8ZfN-kS1yOvBNZyvC02vJDfz8Ia4bC1Nc4P0e3fRGBna6A4F7vbEWqmBqwoBsslhHa-sg0iE6XDWO-i1IBK6gP7qJvGRHrx5RO1-sX2Yi96p4rS4g2f2Sgs9RGArpNc4yjK_rQhm0QU3EKG82T6MqIkfSw_vO5xE3PFvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1QRhL-xZF96QSh5wV3Q6a8-a6WBC70M13oxs3PVX1y9TDbO6mlUWfUlb3aj6SZbSILOFS4bmkAowL4i6EcNd0WyaGZeGjtP9eccKsbro-EG12bKM4EEKOMX31jIU0jjk2es4SP4yWORcs3l5J9VnA8STFWXaZuPm9UJ1zyjz5xG5VGp1hQZqGlhwrT2oIS4v3lQ_PZP94khM7zP9vnehcyJJWbm2IuMIYFELtaLGRPUKkrOrmuY65WxLvS_TRM6Tu2zZOMgXfN5NBT4l_wQ47fj7rwuMbO-iSFRvOLPywN1FRBYtM57Elktryie53S_Ym0YTTqOnegcuNE8p1BavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhiOTJZJ0qqepQadhq4R2brTEPSQsKxAjgqLOGmL2V-WDwSofOeOqi0GX8hnoDA7vm7BSSvQHkCVAlf_ACvqRiDe1iljBPDhLaC4i_CvrEO788HQutrR4ijnvE0-ZL61JXdMMjCyz7blm8g0DSXKSRrJFKaRVCtSI5y9FWoV3G9ZsX6K_6LwxrldBdc0nnXkIz_E8_ssSHsu4hs10toPIjBM-I6Iu0KmggRediKDPmeLerV1zpv4YG7rPh07WPMwwGMpFhzGpFNgtSyxe_SWLJuQHvTkCv2qWqIPfEQQXspKuGAQ0VJzq_UaiTGINF-WXQg6-q55sz-H2yHGZgK8zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJPaO0YAWjOUxhp7F75w7VcCheRonxlIsP2drCgQl5a2Gr_KlgRyVBiLRKiXcEwAp8RpruEsM7ip9KsRJ4htJ1ZE4DIyJ2OpD_MY9CLGlfeBJWYY7qJis7dquPi9evgoxFvP3uvv8I6-GLAzETFHY-YifmSH2lBGduriyel5j8aauTZxdgymiXmTvsZy3soQITtzxWvulTewriue9-KFToBZwg2z0ZBnd8BUSAd-AtMiaLOfuvlQ2bj42CafeXBPvTloukpYuIFOygbWnBEWUDc4JxW4A67g-22X4Uc1gK51fNXm35Uz5_xa9pF6xXgYvdWPrIvQTuwYb8SIXzPwjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuMZKL9eXXtqDNEEoLSusZUvq1uSp16PsprRfK8HO8mF5sIILFK3CDjSY55sLxhaNWkXxBjTYBPA3QIkYUcMEQsp6a_11BLHN873fto1VaIAGdYEIgPW9bpcZiWCcoum3qFrs-cltqpIaD8_5LoTZfa6ivUS8sxUpNSRKaFoM8G3fkEECT77asvRZHVuT830EMbE-CTBn6nIh4VocAHfwN69Dd_mhPHMQOiA22H7pJLaCjfnIM3gHzzk3k47WYGehhcLdy-M43RufRC_EHN6o-YY-p3p_C_DjZQ9bqrboeClU4ZTSc1SF9IDyE2kXJ5V4X07pg8Z29wTZQRlxQsw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev5LXy2_l1XqNkKu-KgtQ3i9jSo-_y1_gtPZs3gdPsRhNHjWSq_6KvuVzzfHtA49f-UR8I7RXLRZWPFfiHkKrSJVpBUr3mnxny9zoBotfEBduaNwNnXG_KYmPRq9DWvbMdriY6sD2eAZg8qhofYHh5RB-391zZnMA8aOBqFZ4qFxW5oWnZ1Tme6PwFiRADHEYq0R_Tjv9sEaTg_CHbzfPBGHEXWxocc_xVKQU3VIsDOxNy3YqS7fcj_29U-LyJxqtSNBbotdLZpgMZ5qZLFWPCZzs-amna7S-Trjzba-PcbP93L_NYxFWYLvqX8MqXYJZ-vVy1RiQwrVD3DV3c6vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_dEbtekUFK1XKOJ5yGx4PQBHZK6XOGKclvicDVI-mcjYEAiQFifyraokv8I0hxoXr9Gr3471EW-qWRHuXIgPmuTliQOOluQk9NJnvZow4rdmYX2DI0iUtebVhpzm9DZAF1B8QugoJ_nqQhuUTfbUJot8XPUqImRoIsjymANP4pxVNW2vMeNageeC5HXt95U5Ranu1xEbqA2sws338e-tYnUQqkJHYt_rVAvBPO6Y6u7y3Uwk4Z-gHLtPDWr4civafDaufX2059tvoqk8WVEBY9Yg8RE5ukB7P7_Eh3GacQrk27zKh4pm_9Vst5DnoETCT2sGs6ScxkskTPQoyYpQg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=CzXZMiPlpb2JOS6KvWa7zDT4LDTfSs7K-0lptthRmKspPFaSWoOpjvVvv6jLqG-4KoA17PlRtXt7LzedVC9xRxtIqH9ytCZbD1lAEtwitjxJb85xn4BOUdpGw-C3_1zZlTAI93CWYbgOvsdig9JusZydTkq-TI4FOx2Hjsa4scz8ugPNKi0dNiLCfNxXTGx5UDP5z9ZgVM6WNwZa-phvdqnJIEKmJ30sCkVO3yIyjtiaZcvfhg0NRCxDxNHUtpIDuv3QwJWES3BgfktHuuVdzOZ00_CHSRWN13NMZf7bPrYzjxtyCVrUAeK_rPQY_Y9VRx_hVbJy2azJUyLqnDHasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=CzXZMiPlpb2JOS6KvWa7zDT4LDTfSs7K-0lptthRmKspPFaSWoOpjvVvv6jLqG-4KoA17PlRtXt7LzedVC9xRxtIqH9ytCZbD1lAEtwitjxJb85xn4BOUdpGw-C3_1zZlTAI93CWYbgOvsdig9JusZydTkq-TI4FOx2Hjsa4scz8ugPNKi0dNiLCfNxXTGx5UDP5z9ZgVM6WNwZa-phvdqnJIEKmJ30sCkVO3yIyjtiaZcvfhg0NRCxDxNHUtpIDuv3QwJWES3BgfktHuuVdzOZ00_CHSRWN13NMZf7bPrYzjxtyCVrUAeK_rPQY_Y9VRx_hVbJy2azJUyLqnDHasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILPuA6hYZIA-JS-JcNJSM91w8_7A8rAqzNNh2uty1x43KVBQP7fs-Noa_ET02XaxNsU5hE8ycSy3IhpVUU652WWnpcCJHo4DhQBCtxdR7v6UqLGb7EyyK8nXd4gq9fQfhfTIkhq-igS10Q0ARuZiEh830MSgbWHrqr3_VEVzsgEez7DEfacpuhDdtEPyClFvb3T_zYqGcIFGdXOpp8c0RL_HkYqDo5kJ5anUn-iSgKGwXsEbOxuquy0odwb-dnM_G1DfHMKndAZ8kOKN-87j7iHjp7VqQ9SV-5rVuZPHtYM4cS9CWUGo3IpC8zHFlRsbTSExZSGNLk7mUOwKbvZxgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7uFc0lKOY80e7HFQ-Ri-AckLL1JCjWWtj-5D52eHNxxzoWgULJErovg-vZtkY_lG8CpgabdWOg7hWl0yMh3eFqnpgwgHJnR5T9kNFHbXY4YyqN642G8qoklQAX_E06RXg_fXvsskS8Dy5AM5HQc4AsV3gZMN2cFceTBwabOTCvA9YxsfaW8my5fnYunYF8fBugSQgyqeIq8KmIBF6b4Di9AhojpTQxE-CvBF9G8EQnxGORzVoEXpas-jPbyOVZQ5Xu8EFwyOY2ji8VzesQmy8OfaUzRe2g0i9gm2eGXE3SuQehVE9TK2yf3UeAzHTjUhX1zIb0CR9nxzv0d9ZnBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR88EX_GitQiP6QE1AqSUJYXPVMxzW6aeQrTpoKF0m8d-JyX2uQX1BcvdQzQsh1aoS97ygTMKdKjnARfZEtJ9zu66FX00nk9uw0FU9WScg1y1RcNoBhE_wsvR0uk668-j84_j2Q5kysAz9clIfzyVVpN89fGPC-7xkmPjm9yKIfLvAor1j3Va88RpHQ5C84s4IybqcnF1i4wJ3JEP1Xx9bbCkwJKeqbip476QgQaFiM-CSOCj_1Kp_cOeU0Sy3Vg1mTiHacZpB0VP-4AXwZ0LndAwKu6wFzeUVQXJLEGB7vN0nfdhYZcKhfkTk5w3gLHs6q02oPHVcTVhtNb9C1PTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks67kWcz9mzrg3cIGSP7msE3SQMGeA9SjIETBVfbohxSRf7XlmjSGPh1Bz5WnTOEhPP1zwUNBLbByFvDr17ADeiJyROHhvWpOvJi36CR-dzrq0Vn3gfp4zqvpcKfc4bLrTRL3Jx_4IRakkr6h7vO3T6OjRviggcvOnqWXvtLsPyBIIV0eMsVsrMghVoK7InJ3hF98VoJqT5BKYGfGTaXTFYY8oQT0ScoPh7dk4Kmgakwel-noOea1L-XjzSfqKIFfFSJDnTc992vra_fKkgzRIoTO67iaky6tWHumWh2j_halpOZNb5Le9aHkuk2a1Zb_DWVA2rH5ZUKg38n4gvzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o12hEXqTbnKSJF_BRyaNfc2e85A_F7rfbULRqnFKSugr5Fb_Y08tXw3Sdgdse6BIOgu_zPanxqbPFeqfJDcKO_JSKJNDXg7Q4WdMwZoNkX0VFw6pcRk0k5oEJdSL1FL_N-UfwHRhHQmWZumwZV_mMFhwAUQX_Mn3_r9sd8WIoOq1SV_fz9mJp4wK93D3ULNhAS8m8G09paqUYIgIkREeDoAJetQ6x68b2Ap8lu-rTlKXPT5cJBTr_LWm-iM7EYbEmaq8Rj6abS1PGl2RkknGImbjznfOfn0joomnpXXYijazEyc9QLP2mbZ2loyFedj59Tr6TPVmNOvUlKSyV13PIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Piiw4P6pt2pvKDtMuk2eMQ1A87hqdE5mEWIV1Awd4jmj3b4aaVL0pUOaeMb1GLuel9cKYMXPr34tTHFrYiFX4RYowZEiczy7IVuSeb13CTm83OTyBT3G0Ql7HUKVQL6sHcgi07K1IXHdbxHTBCchOQMazcg-w8ukgnJmmwqNUEOa-7oDMQdGWjbKLRg0wUHwKlyxeQfxeGXoyKv9ZUcRzLi2OXmlF_JcK-WjYB_rumu1u3jp8qU5Qr6tn7yxKhLiLDptJAgbSGbWFdf0ZR3bp-8tZObnVJQwrCZce3IEj_Koj_n8hszCEPH6iIu_YHlRayPw328ZNHptI5LMk8sA_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=gKi6oAuA0o3uuwj7NDVBY5SJNKy3z7a4ezm2WX33btGWevx2dq3UzqETfOJYGaYiXXEos6JZy8SnNzjmZCCPphKoPqBZyYBx2RVTsy0dlITuwHvxhNmy6YrQAuP7egdvbZRv5w43fSYJL9cl8YwhUp-aNmmGkgC7N-Ev8jcVDRCJAsE6dk-bo6z38Re-gBTEDOJRmmF4CFEYQ_5NoCFEgnwSSU0socD6BqyggzVPkvFWdDtOgVFGxyyJThlVlol9eEUz6b9tHpSSwVUDBtNgpaFaDxzBFwG4jI1qpdKoeqvykXvDrs-NCxH_rRxvy36fVPczRJZWDntYi-57iJh5S3uyawQGJJ-YzGJtDZm9vr_N5VCMUrAgoHMACIowAw14k7OI6EeeI_XEuV-J8v1gOd-_30IzOkHobB2wPQ5fv-lNMIzIgylJgsFqPbVcqVTarOxKft4D_hK2UGnuRSMVwa_avJEn-oCiTf3j8jnVm8AOnG06vLuT3Ko4L7AvILMlQJ7s8TdQ-4RjNzDRmR09rBXnXuDXT2rxKBJnFNLM3XT2mWBeliXy1Akytf6-VxB48Bm4lX-NlsxfsqSWnFFV3GVOlIFo-5lZp7bsqUGctNFTIXXj7HWaSlk4zVhLfHq9MHW-ogAYPMRPxbgfbZi-dr0iPdLoRLSBkT4skz1zxaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=gKi6oAuA0o3uuwj7NDVBY5SJNKy3z7a4ezm2WX33btGWevx2dq3UzqETfOJYGaYiXXEos6JZy8SnNzjmZCCPphKoPqBZyYBx2RVTsy0dlITuwHvxhNmy6YrQAuP7egdvbZRv5w43fSYJL9cl8YwhUp-aNmmGkgC7N-Ev8jcVDRCJAsE6dk-bo6z38Re-gBTEDOJRmmF4CFEYQ_5NoCFEgnwSSU0socD6BqyggzVPkvFWdDtOgVFGxyyJThlVlol9eEUz6b9tHpSSwVUDBtNgpaFaDxzBFwG4jI1qpdKoeqvykXvDrs-NCxH_rRxvy36fVPczRJZWDntYi-57iJh5S3uyawQGJJ-YzGJtDZm9vr_N5VCMUrAgoHMACIowAw14k7OI6EeeI_XEuV-J8v1gOd-_30IzOkHobB2wPQ5fv-lNMIzIgylJgsFqPbVcqVTarOxKft4D_hK2UGnuRSMVwa_avJEn-oCiTf3j8jnVm8AOnG06vLuT3Ko4L7AvILMlQJ7s8TdQ-4RjNzDRmR09rBXnXuDXT2rxKBJnFNLM3XT2mWBeliXy1Akytf6-VxB48Bm4lX-NlsxfsqSWnFFV3GVOlIFo-5lZp7bsqUGctNFTIXXj7HWaSlk4zVhLfHq9MHW-ogAYPMRPxbgfbZi-dr0iPdLoRLSBkT4skz1zxaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=U8E1q8v9wA7bEL2CEA_Ff3XFZNybY18ErZIfMXB7FyU3FOb5T2uuxOaHVdF4HVr7B3yPNOpvDjTWvYZwpnEksiI_9LbAy08LV5mdzJKuFoJaKeWRcdOMd_4bux6QT875F2qmQCwa-rCFh9SXsRvHRdqa5uS0dlNKIjUOKJizf3x7inZt-WMbgEd-HrRwyVarJehNYKMfhvrTOqiZLTfyTLwHdguzOZu70C9iYalA2_cQWFLuCLPqrx4Jbex1GbjgyHUO9GZywUkhyNWQd32DR__nqEGN_1FhKPwuXFTig66RxmKtP6zYRY_kLX8w_jIIlW7NQyeT7v9dU1tpy8nG7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=U8E1q8v9wA7bEL2CEA_Ff3XFZNybY18ErZIfMXB7FyU3FOb5T2uuxOaHVdF4HVr7B3yPNOpvDjTWvYZwpnEksiI_9LbAy08LV5mdzJKuFoJaKeWRcdOMd_4bux6QT875F2qmQCwa-rCFh9SXsRvHRdqa5uS0dlNKIjUOKJizf3x7inZt-WMbgEd-HrRwyVarJehNYKMfhvrTOqiZLTfyTLwHdguzOZu70C9iYalA2_cQWFLuCLPqrx4Jbex1GbjgyHUO9GZywUkhyNWQd32DR__nqEGN_1FhKPwuXFTig66RxmKtP6zYRY_kLX8w_jIIlW7NQyeT7v9dU1tpy8nG7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AatoU4C1rHpmXcjJCzNQ568w1ejBEHe9g2bhm_b_AMoGqJp8yBusHJpmIJGxQ-5P6-W4N1sEkZSgtqRik1eMURLEFIK5YKnyeEiTKXigsIP0SdMvY9PPsjaEy2tq6BfkOAEidG3FaA5nD4zwBcAZkU07ywGhY1b44UHcpEhKKXSc8l9Ng1bSC-y8-Ys5A9X3EU0ELKUHF3WJSQIWMRL7TDK6LKBkpIYYjj1riW4SipchuCTtnIBgB0xgm8PB75Q1V74uZkM-M_tOEMjx2ZDJcrPPxE-c5uhLc7waVwe3tlh7WAZcPIU6t1TlYE2akjaYvUCLf77qcBlGCUbKAg9OrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKfZCIV9qS7kW2R5qfKgVDEo5pt9k9RhFs08itY-TrC40dXI582IA0PVPWZ1wBT5KNqzx3rcYeCag-_fDxZf3__26hfl3mPtoJ6Q-V4Iwzqb0UbtvxXH0qzQyKmla4N3LM6G6-CNdTivt3_mnKHNnYCTukWs2KKL8vtnYwdZDDOVBQefiqbcn0VJWG8w9CmQ4xPudJb0h_yBrvTJ8Gf-ORDeK0vSKCgY8L_LkG_YnxjQM3GuqbtR6KJrqOlZkbByTWwJ_KVwyTUYHiP2q-JqzQ96DzT_4zLxEakVnr9xobxjgGSFHxOuvnFYgJ53uzFhEW3tuPbqOXEodGEJFG2avw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=oIv25k80VipOuby_GUE9S8oyKryhSo5QH3wKHmDn8tDm5Qsx3uwNUG5rndhpFtQuNJJbH8nP9TphpUbY1f9c_g_KMId9fki-kITfAvvmYlTMYbSbnuHgEEUWU1gyzNSDsJOBR7XAkDxkQt2rshHZVwPfJOJQAGbgFHDLYdoOi2boIb6bI94l6rsnolgWaqgz_BOHku2kG_deFhVgWbtafNN4kizssdoqO5cJareos-_ec_m21IV2s555ZaNUJrx8xkVEizIqovWIvbUhgEW0AlWZrMZCoXtiq8sFtRprglm8-8bZADlAfp7HnoOS9ccAdTK5wkSjgGV15mvba5tSkjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=oIv25k80VipOuby_GUE9S8oyKryhSo5QH3wKHmDn8tDm5Qsx3uwNUG5rndhpFtQuNJJbH8nP9TphpUbY1f9c_g_KMId9fki-kITfAvvmYlTMYbSbnuHgEEUWU1gyzNSDsJOBR7XAkDxkQt2rshHZVwPfJOJQAGbgFHDLYdoOi2boIb6bI94l6rsnolgWaqgz_BOHku2kG_deFhVgWbtafNN4kizssdoqO5cJareos-_ec_m21IV2s555ZaNUJrx8xkVEizIqovWIvbUhgEW0AlWZrMZCoXtiq8sFtRprglm8-8bZADlAfp7HnoOS9ccAdTK5wkSjgGV15mvba5tSkjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v28IdYqghUfTsv-JMi1v6cZiF6zGAAXhflgV-kEXJrh3FudPeleZeMQfP1hqGTJ1E1uIYwY8WoViN9Iv6pbqlD_wtaB2Cnu1qiVlA9z9Iav-wgIG3SJhYl-RL7Inmc-hVcifri6jXD2D4WHzX9GpcYIUI5eYSnoWh8piR1ixrEkYjrpXeXEE9dwiYMukYyjiwVnZpaL_rs2O9VKtdDHrsetrUJzWVonLt1it923UorvNKOZTakZHp4-XjeORl4CGyC_2x6nlCiwi593pSD5nTMk5uTCmf1PvwvM-ACTs-nc_oM1ctwQyTD1SQy3dIoy5bLwzhL0KTuJeKHUffED8Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noZZo8RVJSpwl4HJcEXjnUksjJVdVBEtVXVZWrglSVQkmAeyAFzPTHe0ja5zYBXL5dmEGFYwTL5nkQjrfDpejvp9wu7KEfoUA4wK-MRJxM1KUQ_KWxQ7NbTb17oAtEbm3nL0Amsf4xTgcQwTGSVIBH2-n4XqTKFRHDfRlraxEgS1S4J6WGKtnnbJ7d-kUuO5oFmEdWpWfvayxR97BnOSZd9f6q6e4kMJS0I1lfp8sWWjqEVC4t1FQu2ZOm0mnhCZkLnU3SS8tdWmUzUxJ-Tjh4xburjn-Dw100YT5dQaQ5DWexutn2wVZQpZCQLmE3gcEYvhEV_QEhhxlEZeKEdNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJCqahLlOq924MJ0dRLBK8geyXly6HaPn0gGV3KFpOU17vZLypfD_krnZE530Tg481IfxBrlKtGe4ufHANg84FcgVoY5uxqHAOYHkKYuSOMVIWMpf574Bele7PTJc4YLzbspXgXns-7JThQckWujSxV0QPGziWtUesnWoHE6wNtYoBiRzkRlGoGCC9jyBaX97-k12_0OBz-5nwyJVY0-FJl8gD1pEX_xtEczzRSobkVCFJ3SfTMvFyw14Fn7uSTYQBNLoN6-LI6TZ6KV4td8gDsifrm3THROZ32JArW0LE9xAiF19MYoM5LaBXWeAAoaEtEgL67gUgTpHdJ43lFIsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogM8z6fivn77PKP45-MFjc5LGXSk8j6-hfin9sNlrF5njhpDXdFNIDbSIzgaVNCUkUiAQ2YmckcLSA-XFAH4G0IM9AfG0yA-Fatvma9PcKjJg0egGAX3fK1ijvQalxeybZtJk6KKxBEsj4_31P-ib5U5oHG0LE4SM7vrh_cNrLkptZxQTSfhabq0zRGzpO6TeUeuLVWkkcWGa6GnSDQq1kno01H-nbixw0zBKDk1wZrpoOlopTApc4_eJCsCJb2CWop_LvwyaAbq26LcyXCvDPHf0azmzDAQJUTGdelfYnmuMVqDSBePXSHnRl6qSbX5s-FjNnscvyBZQ3GPXzvxGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI1KprGTL5H4jb6dwNcH2Xqyvo6aFrVEYjPnU-JbCOmuLrKa26TM3dpu9ty6jFTyr4XMdeLVGG9u2QQEoLc9a7E1BeBYf4Uj9hAJ_QKYCCyLEXXxQzy99Nog9Exhc5PlPVExpNRiUaF2Qo1a-m_1YptCn-PBFTq2hMD3eM-BOxsOu3OUbEDuiueugddh7Nwjt_qYBc8FUnZJr0k3YAYDeekfUrALgIbRj524HVP9ICyc-tKARGMaVXKr-KwkiQ5GqokulSbOQdoghWDPum-1Hkv25Ksz9O_P0SOhvq9225Ld1TD2rZ964igyKU0lfHiF2GHyiMgOq44zteSeqAw8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bow-_UUlH2m-IVZ4us8OriG-1kaJzlm2MoQ_kkVmb-TNSaRxNaYFOwDN9DJlBZ4L11DFmmpNqGhUEf7T5q6W49v0e3ZRUVP-jlgi-rFFejOQYR1LzDH5kPIBRlJhUBDdyRcEoynwygBkaoLTfid6q7WFLsoA71qSjZ7VwrAfZEQZYpiSkeWipR8cJjPMS7Ew4LI3BOqB-m5iBKYXyXWwxyISfUI5NEaIv6el-vtzUq5KLJRreDpQ8Eaw9kFuhncKMdxggaUM6xGTYltpcqhf1mOU5j3MYUaiEqoxPqWQkkqdsM25j5RSRtoQNlYGuiNmNTrho1p6QWtstlAKn5FbEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bow-_UUlH2m-IVZ4us8OriG-1kaJzlm2MoQ_kkVmb-TNSaRxNaYFOwDN9DJlBZ4L11DFmmpNqGhUEf7T5q6W49v0e3ZRUVP-jlgi-rFFejOQYR1LzDH5kPIBRlJhUBDdyRcEoynwygBkaoLTfid6q7WFLsoA71qSjZ7VwrAfZEQZYpiSkeWipR8cJjPMS7Ew4LI3BOqB-m5iBKYXyXWwxyISfUI5NEaIv6el-vtzUq5KLJRreDpQ8Eaw9kFuhncKMdxggaUM6xGTYltpcqhf1mOU5j3MYUaiEqoxPqWQkkqdsM25j5RSRtoQNlYGuiNmNTrho1p6QWtstlAKn5FbEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnBh7ZHg7D51VGTyQ_7JVIIek4SEB_HU1AYxjBIm3OnHf2lOwI7XjM5ZuhugIK3njccCX3GGYPLl-TL21dicozuQSQ2FYGehX18c1srOJoganfGQulp3sGkXW2tXrbJhRPMYR_VukAu5FWI2W9KAC01SDTUX7hQVuuPtZkCN0Sf-7ggWlO9ZFP_8gfeYYdvS8OAX_155y_R45qLVMabY0OA8PiH2py3FxqnbDX6q3N5bB2CfEgMNPsiio661qBb_BXuQHSVPLe-JVeJUEl1ne7j5iOuiVnSqGeJ37Z5YfZob3NgLBs0tCVhM0_C8AC8pS1ugoMgxvfMWbdQ4oXpq_kHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnBh7ZHg7D51VGTyQ_7JVIIek4SEB_HU1AYxjBIm3OnHf2lOwI7XjM5ZuhugIK3njccCX3GGYPLl-TL21dicozuQSQ2FYGehX18c1srOJoganfGQulp3sGkXW2tXrbJhRPMYR_VukAu5FWI2W9KAC01SDTUX7hQVuuPtZkCN0Sf-7ggWlO9ZFP_8gfeYYdvS8OAX_155y_R45qLVMabY0OA8PiH2py3FxqnbDX6q3N5bB2CfEgMNPsiio661qBb_BXuQHSVPLe-JVeJUEl1ne7j5iOuiVnSqGeJ37Z5YfZob3NgLBs0tCVhM0_C8AC8pS1ugoMgxvfMWbdQ4oXpq_kHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=sfVj4Of9dq193JqcfoLH6uTA15uWL28IrdqYdzZNSDBfCdyqlSVdfqFiaavA5o9WhT8cTt_mbLOFWYS30y8YTbCo4szRkn_mCbfOkxyOfrLg5VhpM7EIJBDO1IziMyKma9rL3L02Sz3vjqytymE6IXIdyrY7XBDf7KOvDr0Ms0yw5ac1rI0DnEYMOvswp2_cV7Nl0zRPblY2_ZhrebQNnX4blfOe0daRnfHqVfb59dgQtBA5bJOaQPU7LfaA4FPg7z7OtxKxFFX8kzpA0Ka4FgI9YqiHzTJXH4gbJiLsunKtp7KTo1nfueqZNi_Y2G3VO96yPLqxA4TD1Qs8fKyosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=sfVj4Of9dq193JqcfoLH6uTA15uWL28IrdqYdzZNSDBfCdyqlSVdfqFiaavA5o9WhT8cTt_mbLOFWYS30y8YTbCo4szRkn_mCbfOkxyOfrLg5VhpM7EIJBDO1IziMyKma9rL3L02Sz3vjqytymE6IXIdyrY7XBDf7KOvDr0Ms0yw5ac1rI0DnEYMOvswp2_cV7Nl0zRPblY2_ZhrebQNnX4blfOe0daRnfHqVfb59dgQtBA5bJOaQPU7LfaA4FPg7z7OtxKxFFX8kzpA0Ka4FgI9YqiHzTJXH4gbJiLsunKtp7KTo1nfueqZNi_Y2G3VO96yPLqxA4TD1Qs8fKyosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH6ITMVeKoSHyviwzigfRxt1YFCuhTbZMCsS-b4vB-v509C_hcqDgGQP6LR6mCxM0gzRgCX4_TnmGjP1V31HZ5J4BFVBjYkyoZZldyirEVVcYU8ueXRVR3sC9wPfWJVNbiKKHVu1x58ekEgSnsI91R81L20Ud37Rn5mJ33OYsHgdgI3OtKuzqToBT2kgxr6dYngrQhoR2pS0yoIeePVpPOI-oAnwA9-jOF7_1yoKzoSf4ZCRW5rhzhXHcUQpRUzTxHNEKX2zRg4qy9mhjMZMMgD5jKo1AabY2o5A06C0JdN6DEoBIq7EE_5qdgqqsZyp8FWl0LIKjOAfGALfJjbROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrKkiQ1MwRLEHM3y3Qq2tw66AxIOmkUgjQPfKkrrcuy9dWafm67vxcpZyEhu8UPwHoCxhM83NF-nmE2d9muXJUM_Tewe81Qz1gtlcPm7aaPMHQ9gZxUnROqDxrojEu5xpW5m6wUQMfQE59bkTYm1LapZwHju9Xwx8UYZ2YXMb8yFU1FMFH4oXHthjV3onhk0gBO60bi3z4_d4wVf-CEMV0RMXWR8pH4aVcS-uH4uaS1d19FFKM4kVh238Qn6R51rrDcoZMxqu0BqmVOw_QPIY5341FjMcenkM9qls3LvP_vA0pnHFHIJ16FRWcTwUehX8XvSsoUzEf3aHNBkWFLmzA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=sck5pBANSfRSCw0zuc9FAQXc-8lzM74Q-rTZJikaUYBMmXH0GiWTD3cGA3RJFT13S22n2OtZ8am_oGpLkJDJpjhFqoB6xNbsbXNSV2EPMXzbMMcK_mX_eEb00y8Ka9g2AxxadD17lmlyz-JYh4nTBQMIDjQi3vyF5aIjQc-EKSWb5MMtE8a-sgwjZ-0liTB_mp6qVaJ_kIAkEWiGVXUQ-FMF7zPmuP-LVNc5-a7UhcCINWSk7gOZRfaZxQZySq36VKcTXUjmgoGF09XUSL3NPfzyK0dirHWFYD1XUL_gVsukH-nlQ99czvJnFqmy0MmFgbMFYp4fgkGLQecQdRsCGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=sck5pBANSfRSCw0zuc9FAQXc-8lzM74Q-rTZJikaUYBMmXH0GiWTD3cGA3RJFT13S22n2OtZ8am_oGpLkJDJpjhFqoB6xNbsbXNSV2EPMXzbMMcK_mX_eEb00y8Ka9g2AxxadD17lmlyz-JYh4nTBQMIDjQi3vyF5aIjQc-EKSWb5MMtE8a-sgwjZ-0liTB_mp6qVaJ_kIAkEWiGVXUQ-FMF7zPmuP-LVNc5-a7UhcCINWSk7gOZRfaZxQZySq36VKcTXUjmgoGF09XUSL3NPfzyK0dirHWFYD1XUL_gVsukH-nlQ99czvJnFqmy0MmFgbMFYp4fgkGLQecQdRsCGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8N61soFwhO6NG3vGInFGU4SjLyls2uvChfCewrgdYEsFzrB1jV9VMKjLf-Yog_5nfypUVdCSrrA3a_6NfRBRieIKWszRLwpxffLGuxElV1LjkOp0LvmT765i0qh7vg3yBoN6COn0Q_sM042BRcK_AI4JJtOSlM2dhoaAIr8kIq2qFGCh2W5gby0gUAFOuqmE1HbXO5I1IkGaT0xbWtz7Vyt0EEyzr8dTKlPIysMgcTiqKG94RezoAkyIMuyH2oavY1tg9UuiZ0LgNasThXMTkJPS4iPYGlJ_wcmQKc1ebpdZbvQafiEl-Cm16Zc_xLiqb9IjQq2SYgM66l9MEJieQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULXt54GyvFLvaXtKSZWPO3Z0tpxwjVzdMhiLwzytVYnwC0zSyvHZLBwOcT0T3s17n2X67O8jYOlYdA7lLM0szyR4_zNRFOJtKyLn8mFPE8J892Rl6bb7wu4xRGwm8b4QUyyNpJDNBBt1cajeLsqHL9k4CNxLHssToGPhEN9LTHa-JhpY-jLDK6wOFY03VNjNrn3-YwvbhQ_HCUP7M4qNNrKyx0j5SOJpwKcB4X45aRwUF7SOHoqS2_qGsi2Mymhv5JPzd5nDoqDTJVZUH83iv3WCJfapeCj5xN95_IKRt2e6MXhorGv7ji1TuZxS7QYsVh9MMvJhVhbbwz88neVoQA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=HFPS_bI5IDRk-hDv79AQN_zPgc57tOmPNvbdq_xXHalplcmBuETk3aIIDsxjMIkcceZhk5yaeiDQT0OKTuUOOy3tZk0cczH_-AmZDpWbjsHJn88AOB9MnUpKgpUmlTSEiRoZSIBwD2b-DSiPOHeaaNQrP2xK4U8nRXwpxqGCKNpsa3cz6qWrJB4u4dwNM3lhOwVfbUivwsbGdPdIgZVZsTpgfiazqt5QlRIOwJG_8S8h1ZW_xPebd2_Z_HcOgqpk1px2iAt7dfMs_IiI68sK4zTlQHZ41oWwnTBXR69QoVAdS1VhNeYFFYrYTKw4LgJ8yxAI_A0ObB2mRngDrpE84A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=HFPS_bI5IDRk-hDv79AQN_zPgc57tOmPNvbdq_xXHalplcmBuETk3aIIDsxjMIkcceZhk5yaeiDQT0OKTuUOOy3tZk0cczH_-AmZDpWbjsHJn88AOB9MnUpKgpUmlTSEiRoZSIBwD2b-DSiPOHeaaNQrP2xK4U8nRXwpxqGCKNpsa3cz6qWrJB4u4dwNM3lhOwVfbUivwsbGdPdIgZVZsTpgfiazqt5QlRIOwJG_8S8h1ZW_xPebd2_Z_HcOgqpk1px2iAt7dfMs_IiI68sK4zTlQHZ41oWwnTBXR69QoVAdS1VhNeYFFYrYTKw4LgJ8yxAI_A0ObB2mRngDrpE84A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=ORwD3dKTsBBSp8D2u1nN3wfHxrIdFGP-UaciwE0IwCPh0-g0rS_C8Keu2WsLhSkJLnphXKp5Jw-Wpdnt5QR4YyRkJxmUD2NDs6LXbbrQqr3D5PwnnyYr_Oegvpfv88rR0Ao5t24I3mfbvS_41Ly-EeDClbqdFw81xL-XNTi39RZwfNZK_-dY6moufE3Gvaht-ie7Q5PlVczDuxAU41yTB_kO---SAySF_yjaCBGOZUjpf7lSk3v-KNq1dAZezXvtFjzUuzacXtdvkT_Njg-3ANhudYhfed4iYD4ZXYqpveKs_bkpbqM6lIylBmbIRwkxolgFttWCVRm1X-Mtck5WV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=ORwD3dKTsBBSp8D2u1nN3wfHxrIdFGP-UaciwE0IwCPh0-g0rS_C8Keu2WsLhSkJLnphXKp5Jw-Wpdnt5QR4YyRkJxmUD2NDs6LXbbrQqr3D5PwnnyYr_Oegvpfv88rR0Ao5t24I3mfbvS_41Ly-EeDClbqdFw81xL-XNTi39RZwfNZK_-dY6moufE3Gvaht-ie7Q5PlVczDuxAU41yTB_kO---SAySF_yjaCBGOZUjpf7lSk3v-KNq1dAZezXvtFjzUuzacXtdvkT_Njg-3ANhudYhfed4iYD4ZXYqpveKs_bkpbqM6lIylBmbIRwkxolgFttWCVRm1X-Mtck5WV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-f-p1oeNBYI6ntP6MB-5XKyYS_Ye4bEYYr-4HK0gjnqi5G1Nnyuxf4QoCMrLhjx01_5WnKSVcUMMLn37fcuncuYb59rvNoqGj-KmTQ-Wu_1IdMjUQ5OQG17IpcuCc16kvaea5B9Mciu3B94bHmCiB1W3mp0_GpQ9tfIFBxXOhbbRAa6pR9-nVCfsKBPN3H_4h0sQqhFw7Carlj5hZiHm5gAxuiU7E7-qKNGKNRUYFkwKvGPJMwihMVel_sxgO3-ruc4UglBx4tKHYzPLwZXZsPAkv55pbxbmBumKyQ0C0ZzR4TiK0oFwcIutY7OR-vV73YdJZzj5gATM7Z3DErc2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGrL5y0eihQZB_IG0wABUWBxGBrHESuNtrFpKg2VsgVIahoQf3lSeDqNaWd3x01FV8c_kGEVeB-mHuT-EPU0HVi8bs8688RtvekdBKCARRrrtyhfx-GQ-QrylNABWwoQBjFKk6pFZFoUXO7ikHbYUEPYxMJpzBkeZFlF1ifjMSADVY9nmXng7NzYAWjsqw83bBxIqJDlzJCnHG70EGBxzVB9YmY2gBBTyqRSCIjKM5Hkn6i3V0wsFqtkMrHegQLMiwGom0UBf5zoAiIH8apz_IYDMWEBjnP3HPK-b8y9A24N8cDSbdCxS-jBh9dSlhG6wXVYedJtLywF9Acc6v5DEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=KxRuXxASPjt7RZpQCDp_YNJPdSatT10QCOPXMiXRw-j-CSvPccV9b6R_Jyayg4XWzGZrcNdDBCQw9aHsGIzj8hz9z7qPJXhXd-buAMapmn7Dq2e5a5RYxxD9wtUUjXQSMN46phtf69Omiz9AuzWgcWHIQ3QGE3JZKn0_-4D6d66aOOVcTPk-giY12FpvDAIqZzETYO56FwxslaFHVsc8v8dzCarzSP_iUzTpy1gyJK8ijNkPyX9KMs7JUZEeikiIqg2TV8Q_mXlsbNReiYBUUZYNNL8tvuQyHoYIr8eD9hdMv_zfseOrWt83zh7DinUe2B4VMwEdlwRIN9kDEds3Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=KxRuXxASPjt7RZpQCDp_YNJPdSatT10QCOPXMiXRw-j-CSvPccV9b6R_Jyayg4XWzGZrcNdDBCQw9aHsGIzj8hz9z7qPJXhXd-buAMapmn7Dq2e5a5RYxxD9wtUUjXQSMN46phtf69Omiz9AuzWgcWHIQ3QGE3JZKn0_-4D6d66aOOVcTPk-giY12FpvDAIqZzETYO56FwxslaFHVsc8v8dzCarzSP_iUzTpy1gyJK8ijNkPyX9KMs7JUZEeikiIqg2TV8Q_mXlsbNReiYBUUZYNNL8tvuQyHoYIr8eD9hdMv_zfseOrWt83zh7DinUe2B4VMwEdlwRIN9kDEds3Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo12h161cG71kB9N2eqG6Yb__9gfn9O--FbgDslTumG1tZ6FRHGuNs3tirJ5eqHNDFncXhFDa-UU6feFt38aciAK6hB14X68ptGFL85cxBj9MOtX6kTwuaFKsCzqOQTpz7qwO6GzG5fvDSzq1yOFmP51lZGhVwCfKArx_XGANXG-MAAtjUGBnQu2K4DIAA9yhw64Mum52jED58cIlQ_49Erg7DFE8pZvaiOPAKxNzoUEp1loIyXuqlic1CpxmC-xNxXZ_eRQZCgTxa4pGh261merlKzE-xRIiPfpoBWUWN0ryIC3qqRD5UYHJWdm-sgXwOpYSCUpR5-HiggCT2jz3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ooQssY_rioPrPoRrfD2BPRDKqNI0XRLuwuOwQDijaBdWXSMSj3hHbvfKNCFa3z-u_R6Y3U0-ZjZHQvb1W4l7MptTg2DsF6v95qR9pZgIRWmffg0BYH5Ex_VoeyHMxzj4oi-X7yAg0FzwscCIH1pWz__sBz5FGwvk5gBbNz6Z_evobvWHNjrw96RE0qJF-zctTtGswdCL7BjMGZanlVw5_P8ZlVIPSCPYutKBeQyU5oA-ov3k811rxsZWt0XnM34XM1tMaAdwu5-mA-q0eHH4QnpliPLChMAZPopz_d61FJ0uY8XobSdZfaowIK_zVEU0M863BKnWdX3TxgfasxtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDf3deLeY_FTNwf593quPF2BXonZQVAtdLG-LYUs27_nYkWZ_Cjv0btwWJi0C74LozHAD3EJlv0Qbn_SoOAN76b0GD4lsTMds9oXzfKfmXc6PXlEhT0xU3jSZ2dtNfCbEDBUxFmkwM_li2UrVMQFT_UL1Ny-6ReDN_HwR_UD4gmZvS1Lzd6VVL9T2aeGfd58d0LxdHXKOVWQijFxYcs7xd0KoPiVdxXo5qplJSjQydcQsAtfeFMOqHi3hfMWxRj1RL6l5sgzoDC8MKEgEmZ45H2U_e1Lv2FfH1rJwTaAzjlcmWT9Kv158a3LrSnboscHLe5-Ix66F5k68r3YXVIH8A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLV1Cxh5o_LQtqTpX3Hwk2gbTu83qTkRpK5NpUrEj30yrhWlbREiA1z59DfrSTWFi2S42BF1jsQ5dJpC8PO07GM5L8Cj7xfFcS18s8FdCGW26kmDNIS_SGHsEVDhDhuldcqymr1LekV4uAEvHo4IqOgnVGJfmx6nkBYFB7O2yKZe-IiR0OkjIlA0hAxqnlyR8uD5i7p4M7bgwz2yuGaLwf206sJ_3dgPh3gbyR5cfo4DseuPxMwvSeN7zkMlsM0polEDQbiZCAEv-kyuvycnlbI0-QvpGUL5z47QGgat_nXvSkdq_GwE5Oo84I2XedFhDESZw2cL7WrbROoRsnpFwldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLV1Cxh5o_LQtqTpX3Hwk2gbTu83qTkRpK5NpUrEj30yrhWlbREiA1z59DfrSTWFi2S42BF1jsQ5dJpC8PO07GM5L8Cj7xfFcS18s8FdCGW26kmDNIS_SGHsEVDhDhuldcqymr1LekV4uAEvHo4IqOgnVGJfmx6nkBYFB7O2yKZe-IiR0OkjIlA0hAxqnlyR8uD5i7p4M7bgwz2yuGaLwf206sJ_3dgPh3gbyR5cfo4DseuPxMwvSeN7zkMlsM0polEDQbiZCAEv-kyuvycnlbI0-QvpGUL5z47QGgat_nXvSkdq_GwE5Oo84I2XedFhDESZw2cL7WrbROoRsnpFwldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iK-4ebJw75rd-JrmKDkXocLZt0lRydiVVOm8ViOLVpa3YGxKmQ1vCHnxYy8g7G6MB0AgAje3_wyQh9ORvVXNY0FxgHpnk2Jme52QhhtjHtfBgZJOuVHIXcErscPbP80m1fl7yrTkwXPhHIl07dY92XoVpM88Dct4181xTjKMbhcK5rzHRYN5D1AOjQZENL_-xzjaS8bQ6X7Tg1-v3sRy1IJKKZ3gY9cFEGevgK8xmXiaHv6qFBZf7DAqj8UWO_0KsVZRBRbqDtkTuvs_nRwxjsbKL9WY7lVu4WgFIMw0MFTJxdulPTLnik69_4j01lLzocK301kQPBTkgEFNPrmrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alzMc8d-o7Ky1JMbw8vwVZ-mRFR59G1NXf9HFKOmXI5pdssJlnSNJ5zHv1rwfZq_9OVDkKyYYc2sbXz0C8pDiB5Uc0XathDFo_mgbbK-PtQh4wl8hEOZtUcolszxoaCvhmkeM5gxC9wca8gab8ew95U6xvVAomkUpaKvodSBN27AlSJkHjYYxMgyX54WUxLSJHt_fYqsl7XImxu13c7rRk4vkG3Tst28R6K3boR0vUH4tP-y8_g2i1KnZlYAkWSo3eYp7VewHfohp3YBOkYvqeGgNJi5zEdYm2oBDGQ3sIg_BxWFXdsh90pQU3PBN3Gb7QO3SKWQYSRZcnua0lHalw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=N2xiH4FPBNnMSKEzU79-BxjDZDwY9mjKBgOdzC0yZBAokc96r8enjQrVAwc6htS5HKXfElCZMCw_3QQvKThznCxPHzPS2ON9U44OzhCHr9EDA5zJYd2cUHqvhDkVolv2K174d37G2X4CjatGO5ZNXbkNwx6-tDQIrnQxQmZSwXjVBbebrZrW6SbctZnCcuMfCgRr7jaNAo_K8kYacEZGWXpgJMlYpEb2o428UE3oYg6nWLVb-BgwxGP2dH-6vpeVSMJMot675GtfFe2GKKJQP2tVL7TeIWQoNG_VlbZaPNRNrf-_2yyNg9awmtcW1Y5HbDCBtwZht5YH7uz9F-1NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=N2xiH4FPBNnMSKEzU79-BxjDZDwY9mjKBgOdzC0yZBAokc96r8enjQrVAwc6htS5HKXfElCZMCw_3QQvKThznCxPHzPS2ON9U44OzhCHr9EDA5zJYd2cUHqvhDkVolv2K174d37G2X4CjatGO5ZNXbkNwx6-tDQIrnQxQmZSwXjVBbebrZrW6SbctZnCcuMfCgRr7jaNAo_K8kYacEZGWXpgJMlYpEb2o428UE3oYg6nWLVb-BgwxGP2dH-6vpeVSMJMot675GtfFe2GKKJQP2tVL7TeIWQoNG_VlbZaPNRNrf-_2yyNg9awmtcW1Y5HbDCBtwZht5YH7uz9F-1NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ktMtxFQp8BBeaKVxEBcUyREEah154FvGpDvW2aFSxl-mx0Z1rQffwZUSCePj0Y8AN9ldvPOHxtvw4I0OdsT6Yf26vn8hBmPlUXN5M4nbcowOZ9SWMyUzcZF5342cTYSjubJSAltzYIwToUS7Xn6qH8PmlidAz2yDLNb31RWa4_Zm3m1VgY4b8SklRfQG5nBY5dgBpDV749wTWxo6pkMKJorZi5lcK4GO_mRYlTo1t9Wv9arap2xNvxjg2pSA5GJ8T5FcWl3od9bP5SQ2rAiIXSItqsMAU_s8FkJhyStKnl46b71j5XnKV3IYCbBBdbFVIHG7YwaO82UVCdAn_MdB5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ktMtxFQp8BBeaKVxEBcUyREEah154FvGpDvW2aFSxl-mx0Z1rQffwZUSCePj0Y8AN9ldvPOHxtvw4I0OdsT6Yf26vn8hBmPlUXN5M4nbcowOZ9SWMyUzcZF5342cTYSjubJSAltzYIwToUS7Xn6qH8PmlidAz2yDLNb31RWa4_Zm3m1VgY4b8SklRfQG5nBY5dgBpDV749wTWxo6pkMKJorZi5lcK4GO_mRYlTo1t9Wv9arap2xNvxjg2pSA5GJ8T5FcWl3od9bP5SQ2rAiIXSItqsMAU_s8FkJhyStKnl46b71j5XnKV3IYCbBBdbFVIHG7YwaO82UVCdAn_MdB5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFKcN6FkDwo3ripoGyFhaj5dnzSIXSroN-ezu7c1zC-DOT3Rp5hOdANRdJqx4T8N9hmDjZB0wDCnlVef9H4aZFuU1yqsA8sEUbdIUQ85aWI0ILbaicOs3-v3TOi-Q_7mMOF13Y0-mEobUpQPtUIIzyhsd7NifpvMLP5PKrIrCCHjbNXMuel0lu1Rw7GXfOBi3ceuHFIpfLqMw1kqOrT0qf1i-Yp4_LK8v8nfGa3pH44fThc9jP1BUOp6_UEJ9d37eSkwku3rFQPtVMKHs74v4f2oHGg6NlNxhFGaxOQP3sIbaZeNo_llUCzT0LJpNgNfOnEGWKF3EE27coK75YdDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvTbo-eyc-ye3fEGrsZil5lvQcC2WgbnpJ3gZ4zM2Z1S9jVYp_qWB2I8YFprdXmz00bjCUrY7n2qRiDPxMtdtCBV-NTQzJf9XWFwIyTnN4iNC11-O-RndWf3jDBPZBAHgrSypd4ff8yNFzaNkWzjrVAFobLiwaTfNqoFQN9A1_DkxPIT8jJBkhXIM2_6Mz_SZPhpx20OzaKmvkMQfNOCW3kAJcmavNV7wVcYQpIV9r04Sr9ZAF6sx1N9qYGFPPS0Ba3bIdw71EyovrgGeBakXk13Kerv4Bf7GPXLGfaP4IQfsGiFksr6TCdU5xtwP4b-BZ2wUkcoo1aSXBiIZV1EOQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=rfn3l4PhzZN5_YmC5DuVsa1N5NHhHY0KU4m68WjgFLd93-t1dZh3UquEnH9ZUUZPJZIFpsv9kmhtMYQieHRtlkYf8knoAuoI9pYr1wNYuokhknMD7lKVY6-_PWP4e9_1gOuGMNnfePM6Fv74jKi751VC4rrt6nDuaNiJ7HdTuHaYus4ofK4ID6bK5eCbax_gnE2vczthR7dk0yLgtng-5qMeuOWY16rEpDjv9gDWj7BzCMdmYftQgITe8VgLIqtxxIf-0HWNOUVbaFwH2p1Uf5BfvYGKZKKsF-5hRuDrMV2NR6-eMJ_GPKXQVINrSNlEJtjcRVIXLWT9uzivgKk2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=rfn3l4PhzZN5_YmC5DuVsa1N5NHhHY0KU4m68WjgFLd93-t1dZh3UquEnH9ZUUZPJZIFpsv9kmhtMYQieHRtlkYf8knoAuoI9pYr1wNYuokhknMD7lKVY6-_PWP4e9_1gOuGMNnfePM6Fv74jKi751VC4rrt6nDuaNiJ7HdTuHaYus4ofK4ID6bK5eCbax_gnE2vczthR7dk0yLgtng-5qMeuOWY16rEpDjv9gDWj7BzCMdmYftQgITe8VgLIqtxxIf-0HWNOUVbaFwH2p1Uf5BfvYGKZKKsF-5hRuDrMV2NR6-eMJ_GPKXQVINrSNlEJtjcRVIXLWT9uzivgKk2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=rZ9hww-36MZk5YrJBR4PdqkoYBOpA5GDB_7L09Iz9hXna0s7QJqOvBw3WDWX9uVN1gA7WQCw5LYcpfJIfh_YPsiEEDMq5C58StOxnqqq_jcJxXkXeULXFJpTazAOnBUx94f6EjutkXya89at0Hj9wMpkza7yX3O860F5pvYJzuX3qHNa_DHylMlRbFrFVcwlAn3aoOPWJATLbtVKnziJyzy4WiNDh5dbKGdEVkyFx-Neh79jkvL8i90GbnAuiFRIe-3lblXW5zPpglxUY4E4oc9p3pJodSvR6Ka1EST6ZvXB0qRfuHNSHuOVX94X-1PW_I3mjBmHk6d-P7FrJq0gwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=rZ9hww-36MZk5YrJBR4PdqkoYBOpA5GDB_7L09Iz9hXna0s7QJqOvBw3WDWX9uVN1gA7WQCw5LYcpfJIfh_YPsiEEDMq5C58StOxnqqq_jcJxXkXeULXFJpTazAOnBUx94f6EjutkXya89at0Hj9wMpkza7yX3O860F5pvYJzuX3qHNa_DHylMlRbFrFVcwlAn3aoOPWJATLbtVKnziJyzy4WiNDh5dbKGdEVkyFx-Neh79jkvL8i90GbnAuiFRIe-3lblXW5zPpglxUY4E4oc9p3pJodSvR6Ka1EST6ZvXB0qRfuHNSHuOVX94X-1PW_I3mjBmHk6d-P7FrJq0gwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYEvFlbeXrG2R2OJiXPkLcavK_au9oXArYk6eetjDWtJpVy0B2WmgbnDWGB8TyjYpg1eGQ_Qsu-Lrh8p_jgpiSKnvniCo3eRStiqPPQyD5uIq5o7GHmwJo8vpJ7epkpgZZeGHRlVfdJ42NW8QisB0vm5iurP6j_jjk3HAQiyptyTu8UdTBg-N24dIRn2a8FhqXzw6gJYiQvAFfXNwtvPJHSAL-Tz6GojmVx-elmZEUFWXgVxHeU-Il_Zx3JwwmR_CJqi44hbhujCq57REtwgfJ4_5P9XdPQT1geR18RF0ZaXWqphRgaUCUC2bUJFcaYsXzGlWXtXV2lxjCmtC7TAVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6HqDhU72cPlM6B08QUYOQwGxC3shtRiv3NSRmGe0sAxr296HaF-R975gdZdh12aXHrUZKiVY5UECId7d9smyB3rWqTB_Tdz5uT9vc8aatleV7CEY4ggv_2oL5kfAH5zYqjjDSmFMjGciY_NqQdd5dyrP3XjJLDDNANWyuTE3EvegoYFldzk8pgl6AeUlaSshzXbGJYV5WVSJtjKfq5YudzW8sYrwzukHkQ5UEkGp2EA3uPO6PZ9soIRHxLwh2qKLLkcIamdeThaKjMR6UoooeNr241snXBudCLW09exboOIcN48K54_r5rraoBxvsW4ooHodDJ5VCw01nUfDDUPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utQ8ZgsoWbMPcyc1Bi_2pXWCVCeQmxKZJsdYYCuC5RRZNCmeXfdy6NPWjnhM0CHxPCYT3gVoMqVSZSAlSToRGo2NP0xRTr4qWCcdcvM4ogH2yoU0Nr1lzEv1d9-_ScHCOXFSnPFP52J-uX51zV-Gh_vNBsyuDf40pQZ0dL-yfuxiKQE-RXJTgwhQSecZM5ACTD5mHaChJA_VMkUIpRQ6N8FDquREW4EHhVqu3d_SDYszXfaWjNhQNv7wA89vaQyAflmnLtch7ir0Z77hJXTHxWBhT0oxf4-Vz-ebAYiH67E1_Tcx6ny4h24kEzQNCVu1XpbESubk-p26Fv7_Fci_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
