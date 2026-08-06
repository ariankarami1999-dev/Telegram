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
<img src="https://cdn4.telesco.pe/file/WSPDdbV-aJjQQMIz5ThQIjd5dfl6uHf6Ug4mr5VfILPSffdy7mHfhEY3HI_COtP-1t_Fszc5Tr16oOX6_0PgsgJw8x7me0gVR6gbWjqBOzpJ4SCgHCS82X3gfgCm0sNGxzXJH6DQ-NVArxxvdiXkv1ZHrzc76pq8t4Xi8AnXTXqYHGHwSgZD-CaOuucaKPi3xdNk7NUhKXNUJLGmdeYNccmMOlgfWJHd6akgKWiuEawYxt_HKpDVxIHxqxHwXVbqPxjbtpbg4-8z9QlbyVJMl1UxqschC3iAVVC5_5GnrLCtJxTvYhTc1I4IDxS58D8287iYGuh6PMZAu8CCHOepuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 08:27:30</div>
<hr>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_0-ptsJ4efHkAQo6huPuY_EM4QKUmw1vw7Fw2yb62dglPo2dDtFjm13hBcPVJAYPoD7IXEcdAK3YJ4IoHY1IcG1oY00nzsuQPf3WsFcks194zbKE9VNKMT3gxQzCG3qFkR4ya953IR8ekNef8XFXWsflG52MVqq-Pfwg24Pf-SokaCr6QI0O7kY0_gTyDIeIGrbkgbPVbeW3WALodJhZXGJYsSl2KaJhSLWbLPHWO9JUWQD2QdCAyPo-vAn-LsqVDG9AA_RN7iVdVmu_rtZxSH40UFFDAXQh9545lW37HDkYmQq1bSSN1JeHd8Lbg_pghpsu5eYS4FMh19R7wiWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cY-kW-aEjtnJCHLGEGC_Uhshm-KrI9-iqPl-1qJ-zG2Q8xno2-T4s6Rg0gBHB6pwcZDXCYIO3q650D66Z1VMzAOZDO7bjT1reSwtLe5G7d3NGPNwM2cLdySoYOkx_s_mZbB0jst9cbIJ0v8PKJDkfC8JtRnosGYHafI8Wr0tIYfxvwbDAli3aZD5hz2TZOcHBw4BmGmSg5qzZd4balUOzcdpDcDL8qCylzvi0Jvp58amATRUtDzJBAGCvDpSVvi7npL1ANtXZ9441_C_W4iLUSVJUx-017yM0ltSwT5dAK09SuJkmDxw2WDg3U36FTH-bKvwwtaGp_Sm5cIyw19tSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cY-kW-aEjtnJCHLGEGC_Uhshm-KrI9-iqPl-1qJ-zG2Q8xno2-T4s6Rg0gBHB6pwcZDXCYIO3q650D66Z1VMzAOZDO7bjT1reSwtLe5G7d3NGPNwM2cLdySoYOkx_s_mZbB0jst9cbIJ0v8PKJDkfC8JtRnosGYHafI8Wr0tIYfxvwbDAli3aZD5hz2TZOcHBw4BmGmSg5qzZd4balUOzcdpDcDL8qCylzvi0Jvp58amATRUtDzJBAGCvDpSVvi7npL1ANtXZ9441_C_W4iLUSVJUx-017yM0ltSwT5dAK09SuJkmDxw2WDg3U36FTH-bKvwwtaGp_Sm5cIyw19tSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLNahGyWF7UcqcnDLCu9HNZYRFPxkLpGNItCZ1wry48AvlHqDYmOTyUydgP6068YgC-m5YGJtchqhJvF4SkuR5EQJxgHo-pauQ3b7WDOiN9rqUgrVDrxmtHwomLnfpVMFrG0M4BmGbmls1IAQfp4cRPvftqlbFi50MZ21xJwLycvQZaD0MWEoSTY_re88Jul4hLRFnsiKO9pHshlphcU0LRmt8RoFIdj43MIi6Tk-aWpx-u1b_WrAhkJPyp2mLBFIO2DGRh0053WEzqyRJWSioHu4CRhWjKM4ASkjEf_9Y5I883BeAzuOBGk6Xtly-3RuYvC3lAYeu-uxqrJWcrJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxcbJIctp1pqBy-vIPYMTXfkOLYCdVVDm8-Uvvwr3MTwml3DFKTfdgV9GGgBOPB_D4q3cVWSL55CN49zFU1oQ9MxtTcRHkDi2xHyuv18yIIE69cJeHy4xu0t5iPQb-BsTFskwTPK0SYkHHPEGC_tTASLAC2vZRt6yO0MLPYflJKVjiqovmNG53LDhCvxQZCxqS-F8tAUL-XojFOAk12q7V7FX1QhreXYI2tt1hc6ZdizKxO1JWCML9tNcek48j9MeaUBk5g9xuK-FNTbso5aNppDeOa9kMvYYzQapRYKqDGwmNTC8x_McUB8lrZDgQ6ld_jkMwgiFqws14KX0NXBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvtSvsV1bcM7QDFgdQMfXNB90H8Uw2AIoDqxs-2vOLWIh2-Mn54CpzsfOpp9bMHORlPY9EwN0TcByvoZC7M7yIp07kS37by5HpraL7YV5ifPUeTkVGSJEbZAmSIjbMeXWnBCkI0GHp2Y2OCZNfUOGZAd77Dtbd3P-dJzAUI9C-zMbwgaAJDs63HtrrKnAxfzvTAJIki4pH4kZ75CRx5pULvXrJuMJyR1aZLcBCwqKPB4xvI-bWZw8RSo2q2YuSvieJF6PS5ilZuTUOOmFlh_RJ4ZUoo34EjNkiRDBg8hMBJzBXtSMdyujdLP3m7vu8x2s-gkWE5u4I1dfHfXUqYEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecwIk7MdzeiOmAtI3huYKz8IBgEYx1uQrgOMebq433RwZpR89mvbqNk4SDCjP4dIJkFKg6YbT6QsdwxIKLnWYwdRrqWkfqCxw_wHrK1YGMraPfZtbNGnBMlgXqR2q3mMAsAUjgsJhpzoiqiSNAa05EbO5bl8ursccFNj0K6i_JOenLAL4ZBs9FXiIOvtSDJR2hUIWe7fTrYIJ9gtZVzc0LQX7yIPoU8jgWA13FljTCXe-GsakB4X1br6ccXijxUWd7yOaFlnB_k3ZAFT0_fRq0pmjtR-w5NeMkF10l2XU3HiznS3-5z9FnqaUeqtM5EEcauQmF4ZbJUEaFTo8aXarA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBrGm3N2XO7Vu0qxqnqhWzs26GL-wBz0sXgSCSg0TkL3PZaKh2VZ3iZRTGbtiNSd3CbSs_xJkF1Piq9VDQlmenJtxrKuxTVR82WlrS2FN_-Px9JAZ5XEebErwDvI-CbnXuENC7Vyo16jGsaNkciRnkEm2iM9YMwVOReY1T63ejfv3LSps6FcHT922ijr1cvS_csm_lwubSD_dagWiMArDZv52fZilKNIw69TPGU8InnY5wzF4UiavAnwtDSfmijllKFUQu5WM3iGniBDqbwx6MxsQCsaeGf8R1y-YlXh4V98ord3QT2-Pl_t_kb6SBHYsoKXyqAEMQgdEEcRSKM7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4enV613tviTkG1rNbjW-QfEtzvRpR0pgJoXqX_IVFEyP8R5T_D6tz8h0kvsMCb2JNvCXf2gm6ocdUDG5dnRnpQ4_kwByLFaSu-wTHIVkOR5Ge5Q2wC9ouSqiIKVjXJBMQOH2ThE8-SGY5pQdcHGYgyhNTZnCBdyCLGs3bhv3TEQD446ANYlg6wM5lXawBb3NKwn3gAyldxcuknQ4DhLEKjWdQb2IMdFM1xXV8pdhs_mMb-_EzTf-1YqC6AqW43K16amu2i1kfWQGgH3CtrnQpU5J_hUpoCRPn0XapqoSzyyuMQGqV_7OCWZdpjXSRhvArbQdh9xK69nKF6_9Ovnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgJH-DpHeWuv0ZLhgBy49J2-QBSxpZ8F20L60CRCf7DxGgZ9K2wzGDgzVwSfEc8hwR-kl6sh52Djn-_6zxhHu6vDN5FD8kbTQD7RatoAh7VSzaKn5WElSvurnTZJIRhjwObOGA9n9BRQ3kX1cj0HIWG1OZSKuu1dMNhRYii9pliUFL8zFipSLCq_voOttJAU1EwOnKbsddxQd_aOPq4l2R_ThVnoxWhwHJpqbVrJ6nh8fBJVxzkebhL6WR36XYgCBSBPNVINi0Gbca_k5YJwtBWOESqvDqwN5PjyPcRgIn7un6KBxqS1UtmYfLsOma6rGEmeJV2xhk3NOrhHZ-xc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTy_rX_PbdDDvkJDS8waWiRnumlRfGy_dTwP_EQzJodkkvIYvSB-Qva6VdV3AmsK_v2cLyV1Epwk0tJL7Qisiv1-Kum5WnxCMOHhOAdVi1QmVs3ZjF5JNHeYq5MWwJ2Xcdw54bLdEh-tsMIkM_rUf8KTz1n_Uzp1bmn1qay9C9I0lyRgDl8tswsMZM1O226eGS48EJom_aT5ab-_w_x1AMLm8zje_m9IqXp3y0R2zRu83kVM7fAETdWJIcQNU9hXYFo3_nOWuukh3lt64reulbTnwsBdT2juK7zVzkxrQmGdG0tjFfmYt2JpTrcJp9t4wM1LZRCDaR2ZyqUqCfT_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO3Sc_bpYjKNFrKAIizf-6pqX5hPt_GCitc7VupxKQPv2RByhPBM9-MWXkNLTiZECzsl7Efu2twbJZblHjEMTMU-YfMqHBtfz5sJXJdFU0SPR11lcV3nMPdH6OSnToImddZ_Kw5_TTlkGepPnxQMIfiOnQ9PkoMq3GBVWSvroZM885VnrXVn4Wopc6MpvZe0EzsiE2IS-nTfXl8zEVhnRKlG5UX_uc1Yjof-uJkE1ubVjJoZ3X-vxIvNQ7YZBbSbfFABQyZLCCQEBeGil4UQ6ovBtsyhxk1QN-HmIcXlKMyYRJeS5moxzS0DS_MBYxwm-NNhhsK0h85p1lzyEGn3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwk6Svy0mG87jpzBPWeAFD1XOKU1a9cSdKuINg9DFFjZUus3AGFIjVHM0RGkauri8zY16Rf2dSyQs1eC0wQvkpShJk64xT9UfIE8cqmpMAjrJRgcwKlFSMXT2qt8nHKhEOOoxEJMGWDBsjEJs3DLa7m6Zm8ScjPjVKvnnl4jQ1TzngoZMfCpnbKJTOPi9nl8wzjI48xA95MrXy213OxZeuudZZETUBZlYUZvghjkCTs4mJGKRltBu6-qVmxMSKgO6rXr1h-o1jkOxAEWJ6XX_WDQQVfnpBIAuliQbcvJWJHLIF8RKrPn7wgIcCNHnSmBpRxKZaEzK9iYsSj-FUeYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH4LGqNVP53z-HQ4PSTbbeIfaG8CYaXRKwPMhSXLYI7H4c8iGpFRPkCtxbUiz5FqHuxnokCg9HA3UfcCnS69zclW0Zk9-DZcId-55cfSHYXxqmMOZdehOpsEwhzlOdIilJjHiG7XA3pvpBAblblsEs6B43jzg59eIS_bHyMqE1TH4370azvr95Ci33tk6kBwo71SQY0GpOSes62_SOyBLOKQHoTmWAxw5ivQtDkzTq9DYhSkJnnGd9uuhShrUroaNV6P1v_ONEUKE7d_A81o4tMFf9SnAgcXEq-b_Y3YbcCfQpyQwPiQf267WAd3nBOq1ahnNmvzw2g1v8Xb0lZv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqz65LI04FsStkC2upZqPSZ8NCWm3huOKD0gqsLXRUaLANC_s-rMuFhK1JdSA6QVt8SQHPx67Tu02toWehshir-symtci0ZSqVe8fcwTHXaHAkIR-valCCk6XJcXMnz0_tCnQcCDiUhzXWI9HNUnYDT4phlRjYKFoxKC6weSeohSnpm-7fTUnxxZXmlRC5c8QMqPL97bCP94OxBad-0uWChsboEFjS36F8B2Nrtdgbg84o3yQJjSsZN99woYD7dt4D1riFd75F5y3Wp_pi7K-ho2ahfRX47yY_-mLDsy9MvY_ke3UR_AC2wnntBNINy4yktbpcz3ChmTDLJI2KXrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzBytM5uu1R55Q_8etAoGL_4LegkucKruyWahGhiIkCesDAatM1WN9AgiYfVlvA2dgo8Uw9picQHjBO3j72822aOjzxt-nNPBJdY_2yfA0ZIwDtCUsd1BinNje6Ho9cbT2HUInT8OUWyz3QCYhKgg8CrtYCeOUkf4aFlK2i13G1hcJZbyBAddgCUesvbTYbhTpD2MapKyBHTyavnmzhxM9l3t7CUAnbfpWT985ujOo9XVJwYfgemJUHm2TEBoXnfaFMXesV9uKO6nxVGhAYX5l3edm5Hv03BxuXSvmr1dHsCRXgBVcZhPnmdeFtkob_o6f5G9jMq5s7ePNyiFk6jBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpMDpvGiNZfE3H47LDT1r7G_tcCZgzpK4Qew0DT61O6TTUJstw6_kmKpdY7I5efSPbCkIdSHo3KYqtz-K7VpovxOtggFxMTJomQcfyubKGxKJV1t4KYKje7Ur2_CoPgSGGr1kMtvnkQietdHbNs7pm6UVUrMPJuCbpkvRCb-f8Ux1l7uzQcFLd4mnpyS87dtxBp1vlb1QCHknb-a5JvRwHtNXHkMwPCuPQWhgacTnAJBmwsv2wYZfBA3GHnA5FwWs74uENpPNBlIBCn3kFAAB9G_33y7aVyNLvhhcyHfXECLxELPuqOUXoeVAWPYqI7GohwLPr-IVG032O1ZOiTYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2dR_ovKamGSf6Dox3Z11LswUcpROiqfJBNGTtMXhyGlBzTOdfSiMUNuMDEVc5zUNmlbygP6iZcwjluERSpp5_vI8mCQ-DideT39B7RUDTQNqlRAC4jtOM6skJEyqgl9V7x5NvqGXvBTcnXdUavpEndHx7Nys-Xt3JIf2IiIorn32JtYLfMvbuiSWKVV4Bt91nDLPycEuV8zln1T0veqgAEU-Fw2bmDTrLvrrtpDhn3fr96TcVJYn1QRGmsr-vEtT6RDKtTgD9abP5IUkDX8zbrX20EwgWHHqDWCACWPpho31xzjSqNE4Ydcamlh0BVNRVRShq0FYld0XLcmnxqnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjRAJk4lj56HaORB3AcR9qcAN0GENnhZerTSwpSwl2AL4dh0es9BOaX0ClhVIXrmV_9kiGbkKEnzgvJftOXeSkpT8SZFa5_6LqQI6YqR2sukpJ3yw8IDlpVpGJbGLC7BpIQwCvrnDXitq_w_Ex7hn1ZsYC1o34UEBG8ASJOKCtJ2woeqIPyFDiCL3oOHjZYb-eimZKKrFb_uKoYyvjiPbwwM8IAflNOaVgte8WkP4ou5catfXtS_6oYrg5EgoyIyFb9Bqb9_n9SG-tyx93iSv0AhX5CMoxtBqhY9QtFHlDn7BtI-zWL1JvHXLVkUlp57r7qy698t2ridBxAMsvrFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noScq1pwm_szp9QivJmEe7BZmn7nZFhlLI7LuKcZPv4VpgnMGLaJeoqBSGQq5Jf-7iEpmZUPqlDOYco8YS-LlIT_Bl5mH8PGeoTdrX4rTM_x5XGrKqpptZwafuhpmA_40swCbggwFb5WXV7uqiXbT5uoZmJQzHNaoWlNNwbc9E39iozA6uKN7M2SIRU3BsT3hQxAE1folkCI2BOlNjBxb6nmsbf5lFibH9RRZCxsMflBKpIupH-LCvKfchg4RhX4qGJQiSAlYOqk-UgpqqESGQPPqQYj_je4hgxyD0eU3dU3mjXUk6Tgz57p7bhTibUD-8RJI3M6loEePIM4UuUoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpjap0G7VeV_9AAEJb8huJo9qSFkejPjsU043rGOQ7y8w4TTKwk84NAgAeHNxYhy97Ok4njlWIt2Dek2wSafyLl5xhdmfOr_7pOQyj8fC5_DVupZc5u2p8P8SF9AusAIQ3dC3WgKvf_A0_h_QkJxySIysRdI5LlFFf_-uw1mLZsRZxQj7rxLZjx_G3_ehplXjJiA_zQFb11LJf9PCI--fhxXEM75Ff4pHPCdrDpzSUmcEZbAcM8-KWKTN1iOCUrcwhIdpIHYwVEI966JooGmEM2wggmIe9IqEqS7a_XiJ0NUrxJz0SyNXWvnSDUyWy67BvD2Ss0Vd74RW5-BB1zuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr3JOH54hWOra1vByLQpHbKRrBoz6qZINewV4MJC6jBA1waRtZTmZiav6rIoOYANylhWMJWUAR4Ke-9oeBFO2_BR6xBszM_9S-PkGQIJ-5RjtDy8wpGr5nzzysbFQzZA9sUvmThHFmRR_7AzzW8xER7CqPO93jK6zAjtZiOWHUGOmKvjjNYB5B3_vvECTUxegHkDm3EENwReiiEe7AyuiupYv3v2f38yNqjBmz4fdqU8Be1SrWapUVuO3nj4F8plR3LzOXfBA6Y87tmtvrDtGTHF1qazN6N_Mjs3pfPKCgzSH6V3vfqqGYp0IFomUok6g1n6IhVDrLUZ7OFDReq5SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=iSPzzweh-hHsPVD_2w7isvB1TXbAIGWPTRwGZZOe9mclBSHCrK75_q5KImbDETsyADxRg78Xvlg5aF2inm0U_u8HXbZfY-0RHkaXSKSnxZ1AZt8NgGI4YKMboOn_E7cFbVNDNzq_FkzrGImVdAJvbsTnYIpJjPrnAM_U9agobOtEE_aQbwqotOLqVVoU3U1P87_bGAsTxapKSoyNJPa_rGKTBiIpI5al0zZInIZoTPROhRFjarG9QRLpVcdj6lzQFGtqr2DkvI9SZso8isso3bRG_3FgHu-Ve9kDuqJvEhiOACo9uuSTZ1ctuOZ6OaLkA64r3lZY3_x3JBQ8UtxGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=iSPzzweh-hHsPVD_2w7isvB1TXbAIGWPTRwGZZOe9mclBSHCrK75_q5KImbDETsyADxRg78Xvlg5aF2inm0U_u8HXbZfY-0RHkaXSKSnxZ1AZt8NgGI4YKMboOn_E7cFbVNDNzq_FkzrGImVdAJvbsTnYIpJjPrnAM_U9agobOtEE_aQbwqotOLqVVoU3U1P87_bGAsTxapKSoyNJPa_rGKTBiIpI5al0zZInIZoTPROhRFjarG9QRLpVcdj6lzQFGtqr2DkvI9SZso8isso3bRG_3FgHu-Ve9kDuqJvEhiOACo9uuSTZ1ctuOZ6OaLkA64r3lZY3_x3JBQ8UtxGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgrZz74YJ7mEvB1dy7XeEG_lZe0YjEDQH57yZOzUn0DIcbVt_AO3SG4SubZ5P-FJYo-ajX28KrzE80_KRiig0qcWNz1WHjqF37dQaOiStVta_nsPn8aN_5NUDkbBxbjPHDjA9TZnO5EIQmu-MuGBQG6xAisTEuq2qZqvCO3gXEbduR3E5svv8sNTRtIL65Uhu6Efncx9-83knG4ioNXto7wc5cZB4Y1eU3RGyTnggVrQSoD0b5TvPQBhRy5LIcnWjrDKKRWF57PEAMyF45T3BwKLs2X8eqakVSmhpFvGBqZa2U22tK5Q7IuRqRqjLl23oSrak40GYgWhPuCKhZ-0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttgxWfTYm0DLVEi0stT4yVL-3Vy9XtjqXX6TrrTScKD4Wah3e-yi45dNNN857ok-v9RtEAFL28seafDRFUu4KoS_bUIw4K2RoAz3CwMJH7qOofFb6EADECZMeU3u2ua6x-IEe7Vv5qJaJ62hkxZ8HdXVIRyixPjPQE5q9lydk9uZSoJSbveU4EBfQnGPOwsGFbpy34Msykh4qapNZUvN_9KpF97nZXhW2__j4VEBaKNyArK9ioC-V25TqJlGIvlSPPbIJBWWledSLnYTzjcbQ9uMFITz_DAB5uCvWzlVF-FUomd-Jpi85GB6MINI6eiKyg2CxSAd3EQ-ECdf7npUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtFWkMT-OaE1QznVoye5SgDAQCm_iVXfdEZDI4zM-zGFp-vNXpDNVxSNj6evgAB1DXpgwCADvn6Aw2ELzBOLahn9v1V3vKifg5SChLvSQEanoFnYx2NQDKem2tloNu8WnwDJxa5a3avpVMr67MyCBip4HC8ZjIyTtmd5tOxmSO255jF5hSfgX97FzueYLY2wj2yIi5GJlrRfVLzXb8swEUOMBRQ8WFoNKdkhpDcHnrpx-1WZmu66VEfBSXjJjxjxaHTRPFP-s6_ICn2ann-7v2nNN-x1rL_r72oYlYn7CrjpYd1faz_hxdlqLvzwnroIT8Rex9bQHJclvYIxVfSHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdYIAkHssiER711V_w55ba5S3rJdwmFiKA6hcK6WYAxUavmu3gGZ3ZpsHlB17SytiWrlT5fI2kHKqWEaxgxHJPBE-XwIVEGHJfP0AW9JlXlwnVyMrqITWQHqaSqeJ1LkBHsKijX8W7fX_WXhEyjHsLpht8-LA3vyuhRfycmWBUZJaVlRCSPN_1EVW12c24a5uRue4RszmGwf_egMpsUY2zdAq3-ym1VO20PJHbZC5M8apVT8iwVg7iXmB4mkC6pw9xv8DiENgEDB35dn0VlImYR-VYgHY1PQ1GlIDe2XIfos1Lf1Yud59KqZhtLcv2VAizsdMd-pzwccku1P-DBXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRdsFZIQCSQKCXbiDzOkQZn4P0U0i6Hq-7wi4UmR2gww-LEe0Ufx13DPuevgjhagX5fKu-dTCY4UFKlF94u2L-_35yWW6LCP3tqbDjx5bo-hvezyofjIYeRw7LDl8vZbpK7IhOnXOjOOWFpyCD_KAxi7GVB8r7OtA9xCo4_HHinRvdle0ZWMF5395RTm5xs0eWUMW_kN9oV7Y311REKme3IFznq_JxtJlC0bV2-SbTfDVZMq8e_qjy799h42AF9xBkiMVvJGyNjlZSjuHV5YhDILP8qSXMVYXlLtYFiQI5ODrNwCasCvQkEtJSJIa4--iBjisnqFaEj2Rki0NrfKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6Dhg5-giUsOanykG2c-RKpyWQNd1OwgruqsQPaNylzvGXNNGpBZDZbrGgPJWnRRotUc8tgsprvcViKneWZc6JZ_DEdm5PXW2FOzco2e2V55hbTrEscrOphL5ci1cbXqVaxFYiUAa9gj_kag1jSLw78kI6iQrZpM4OXh9FdxViGJ5xwYILkBHRjwoGLwj8DLoHzHRGz1VrwAOrMP-XySTn_DhXHfDqSUlIG3w5GGMjg8RLECftgKNrI5Eo50FMTdADaam-6vZAxD72GPkyqIlRpNV_8ql-VDqzeBZrQNPH5V9SZaLVHxu1nbgu_1PraKDx_lNYdjvpC2sn3ImHH1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnm1cOIgpMuKW6WeeMwvGECGZer-wQ4HDd4LD4t25ao5qW7sCaASj5-dUb9KzRsXVE9gtbCViVr0qb4mcWr97YTEeN3fpiMCL67LB9VQN6Iki2gC9x4sc8JqEZ2YRBKeP1Y5Yvo1IsdF29j6lS9yPHSosQnhEVy4B-SNOTt-z0nZ612fHR5K7-RiHnhFAyIDBZUGY4gsnilC39KP2lvfwDqlvc25-K127sDSxYZN3dySGq3dkktc5GRLOb3jAoMXiYgj1YReGAGFl7XgsV1wPNCy0Lh84O5THFF2hchS-iJT_KVZ9gKXR1MilozWnosyUqPpa7Gy4Tv4MKG2vjneLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=hxYk92BYQidYD1t4XSsDlgMXatgHbZXtbr4_DYdWu9q89mzjwdyf9YnZAOxWfK0Xj5uuz6wBKUzSqm-vwnLtrSZ3Py4TZQoA57GZajUQGjfgqdArJTbVtN-leu0m7COt8tcoi9NjfBj7sUI0C2PKly6Aqr-Ff-RusBxEc8Bhme_xv4ffhNJNlkPfEZW_BPCVduanhv7LpYNleJ-0f2guzaY-TGoA79wnROAtvy3HiaWzfhLT25aTZIJ_UTToRtRF7vOqmehbpu1Ax8GFGgw53wTaAjOlA2dtX19gZTIYCskh_3caSLLx1UbxEAsOqM-a9QVAA548sUMIqhyRzxxNCknWzh3_3MYXnZGzOAZjBDtfmxOzRzgHvj_XIDvYPWKyBgeGXwopI9ycRD9L-XjPLjn9uYKNDUk7JE3oF-2wlQbcMCvxg_hIJJxcIx6bz-wWn_6D7SzChuu3Szj8hvnLbgNIHXr2M5wBlXzIM5FnXMTJ9G6IbUkPdAlReiVY7zhOytbJ51WC-P0cwo4gA1KDopwETGidRCMXSG1PqEkM6MkQXoWID30FQx08fxw5T_UqcZZF0x4LNi9q4b-ZZda1E2Vw3FUXaygiUZUNnDqKhL08BcWOT4vZp54lziu9FoTkJ7xyEVEFLQ0uWCIUu3pnVyUBC6tn2EbUT0emINeUFsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=hxYk92BYQidYD1t4XSsDlgMXatgHbZXtbr4_DYdWu9q89mzjwdyf9YnZAOxWfK0Xj5uuz6wBKUzSqm-vwnLtrSZ3Py4TZQoA57GZajUQGjfgqdArJTbVtN-leu0m7COt8tcoi9NjfBj7sUI0C2PKly6Aqr-Ff-RusBxEc8Bhme_xv4ffhNJNlkPfEZW_BPCVduanhv7LpYNleJ-0f2guzaY-TGoA79wnROAtvy3HiaWzfhLT25aTZIJ_UTToRtRF7vOqmehbpu1Ax8GFGgw53wTaAjOlA2dtX19gZTIYCskh_3caSLLx1UbxEAsOqM-a9QVAA548sUMIqhyRzxxNCknWzh3_3MYXnZGzOAZjBDtfmxOzRzgHvj_XIDvYPWKyBgeGXwopI9ycRD9L-XjPLjn9uYKNDUk7JE3oF-2wlQbcMCvxg_hIJJxcIx6bz-wWn_6D7SzChuu3Szj8hvnLbgNIHXr2M5wBlXzIM5FnXMTJ9G6IbUkPdAlReiVY7zhOytbJ51WC-P0cwo4gA1KDopwETGidRCMXSG1PqEkM6MkQXoWID30FQx08fxw5T_UqcZZF0x4LNi9q4b-ZZda1E2Vw3FUXaygiUZUNnDqKhL08BcWOT4vZp54lziu9FoTkJ7xyEVEFLQ0uWCIUu3pnVyUBC6tn2EbUT0emINeUFsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=nnUBCOYljflIk3TY82t9t0RssTswKyKtWsqt2vcg4GAOyrs4ya-4HH7k4U5HkQybO1zzkKNhVLaWoyhnEyQQk4zk_JedoCpDuV2ff0LOscl-pIPOFiftII1Yrv1DbiXZWqn7jOqHJoMQLOt9RR2Zz5SZs4w8Zcrsew-U9ZyJWVRT6cbJB_f9P9Esd73rZ54hiBN2nq5KtmtYamKxlJA8SVm4VSKPgD5UCd6NaJwPYQPpyl9jJ8QBtPinmhpLldeBn2JtAYRg-l5vMpHzM7pPvNNLAyy8MwnLdk_I51x1wzOh-XoLFcht9rtIPyZO2x4X9I138ya0i6G-6BkJt68FMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=nnUBCOYljflIk3TY82t9t0RssTswKyKtWsqt2vcg4GAOyrs4ya-4HH7k4U5HkQybO1zzkKNhVLaWoyhnEyQQk4zk_JedoCpDuV2ff0LOscl-pIPOFiftII1Yrv1DbiXZWqn7jOqHJoMQLOt9RR2Zz5SZs4w8Zcrsew-U9ZyJWVRT6cbJB_f9P9Esd73rZ54hiBN2nq5KtmtYamKxlJA8SVm4VSKPgD5UCd6NaJwPYQPpyl9jJ8QBtPinmhpLldeBn2JtAYRg-l5vMpHzM7pPvNNLAyy8MwnLdk_I51x1wzOh-XoLFcht9rtIPyZO2x4X9I138ya0i6G-6BkJt68FMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksE2EBWBKtnaswZKKrGsoDlQcW5eEKK2y0BrDvJPqVibEMjV8vPFxFfwgcSYU9g8zz9vb1Ds-gMss--aQTN_kDiV29TFPQinFyD2jE1kfVsHOuS0e4TdF4afFGxv7vGRYAQS89r9P9mSow_69TJGgtBWrFv5D2LUcNA042fw07NKYNdz5dvygRrvaFBjXENsY9UV6omRhC8sNT5Das8eWH-V7FODoqNLxk8X_EcdhBJTWdFfGo5zzCZ21SbRE8DkKPqRXueZJlo7uKVBPpkVBpb0bRNoh1roGhCA6EULB2nOk6Eio4j1zWEqHN7YipDkWnGFlAGGDt6KMYWrFRcp1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlT_oPEXB0zbeVGYoFBGmV0nW6g6lC3DSdVQ5FF5iV1xUnwnIYRl13h68s4AIz_LsbwHsiwxFlayEpyEItrsbAgo1_9AnpGLyK8vO7kP4WyJA9fix1ff7QFkazNphckRMENBYSHsE_fkc2EJ33VWzVmYogBlXW9SnRyvPLumjtD0PfP2obZT_kDX5faTcXyPdSPtYKeOtohKwoxRXtmG2LGKTaIe7XqX0cW6cknPH9fE-a4Zqz4smqgfuLlQt_gWG6PRfT-vaOiJm_fuJXkAidWM-HC5I-KmBsGihuwHhECcbTuSmPbV0PRQeOxLSNFWXFa5OTSn7Iwn-M6cs9bFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=SpVI4a9wa2od1XCoGKfOEgoc1ptWzRDMJrnBszkdbgEfePqlJK932PQnEk1g68oWgsK-d45SMZ7-v2o3mWwaM11CcEc3z2XJ5cyERmm1TL1dAeLHsgozTgeuCUz2AvhIB7_2S2Fs-UGk70Bj9oWuz4ANWv324jWGCcRM42skAaH2mlpHnuaUP9e0_TgA1MpaK2MHVsM-PUcicrtYg-TUHJI0zg4YY5ZcAkagPeWeCQO0bkcK2X7bCyENnC-slqOc-pccW1ufKrE5_fLTfO7rYObe9NG3HHFo3F1OOAoaHyhmGNIx9oCN_nMfAH7vFFGzaNcoVBCFmzMI_yGvs0lw-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=SpVI4a9wa2od1XCoGKfOEgoc1ptWzRDMJrnBszkdbgEfePqlJK932PQnEk1g68oWgsK-d45SMZ7-v2o3mWwaM11CcEc3z2XJ5cyERmm1TL1dAeLHsgozTgeuCUz2AvhIB7_2S2Fs-UGk70Bj9oWuz4ANWv324jWGCcRM42skAaH2mlpHnuaUP9e0_TgA1MpaK2MHVsM-PUcicrtYg-TUHJI0zg4YY5ZcAkagPeWeCQO0bkcK2X7bCyENnC-slqOc-pccW1ufKrE5_fLTfO7rYObe9NG3HHFo3F1OOAoaHyhmGNIx9oCN_nMfAH7vFFGzaNcoVBCFmzMI_yGvs0lw-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EScvaKFcAvaq5TDLnEWDCscUIo7oXaE4-Ib4DCyvk6EtEO2rq3Q9HtKAu6M_F353zWYlRB4paDO8MtxBsQAK_Cl7dPa0PjwrT70WODUeTML9PeVZilCVjg35RWCktHrxPhk4CLBYX-7vSEe_Gt_FnA0fTSyLv5uxgtX0VQJgBYPWH_pDexF9aeI-qEkJqqTkohDl12PDsQnOE9Sj1GOhEZ7OVjI8HNQ2Gi1ytEJfKiYCmKb38yTns2F2DnElvdSfKhVVx-_5j6S6wdLGn1hcLbAwbrrBKv0R5qBkKQO1NcM8LBjj0mDTp8pHCOdIS6eUbqvBELAdeQiOfjvtQBiNgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdvKqe98vFolRYfYUZfIBjwMPi3xwYFgiVfqNGx9brBZsR5WsO6zVS6J1rvhwynXZWbZOJN1eC3OhgsbNSlEDeNOUsvNfNcc9-fV2Kh0oufoqfa2ETtQIY6qRLhNVU-FM_C-BN2D5GEO2OyoV74cl0-ESKC0JHAevGxbKiohKeyV8Ktk_MT1mFvaBxXou0GpL1rrqDGCiEBC-9wKYwOVV7CM5IvMSztMuNw65iJWvRO-kgMcn22LWOwq2V1Q14XEvcB7eTKnKK8Nopat3JpD3psJ3YM7mpw5Oi_D5uLotkm0lnwcyHPleiY9xcq9vtWJTYQTXCcvBoM5_6vm0AK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcKiRPBfGHI5qN7lUNJoFp_KYPL9b8-A1gqQaJgXLDP6Lt6IsDaWU14fQxPm81-f6J6w0AABXWd2oZMnzHgpmY_ZDlNbKz7gWwKfY0v164VzeYVzKZ38BrPbCSyFdaM6hfdcN_-8RKBBI9TDUQDETzuysUgqq1mlee0Q-3WfumThK7KJxWeZzgl9aCG0szFMneWloXDwNONfIBJA853DoyHMD-ogSI-xaumnS84U8Ln0uxciXH4QfHINYqn2mTiI-8aPOgSk7xjc3fa-yk0AbN4L-ZoH4-dFCkymqOL2EP4WaXLjBtY3jCRsyZjqQ6L3KZN67EzDeZeUbBHGXHVwhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMcdbadPwmUropeqmV3rTR0vX-WlmQiUJkzscr6hRR1gGuUlfmGSRQCX0_T74WUGK7VmJaby8lrgHd2Ilko_epVXwjtIat150ZVLRxKHCtaD0aRlcDJMxLHLCjSlQMNW1PzH_KqPrjfWufJVIdhIUm1iH2KNGkIcN-6vJw6p4ZZu05tA4ZayJfjSl7YsT1peGzdo0WNXNUw3_NSvvycQA4QoJ6qjDc79sKKYdfPQyqujlkd2QxXp0qJ5pbKId97jPLa2naWiggvWjw-2zzNbbntObqfHMu08WUeOOWcYxb8n9nCwhjrDJgHo8MJlnjv3DTklOje6hzdRHq4VPgS1WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmCdDi3VxNdS0Xvm0BTYrE9C5KuNyiWxm15BWQlOMrBKYwSu1REtqoYDUNTMfBRLu9Gu107Lpbyu90Fkzs-nZtRpk2DclgmonEBSHyqceyjUBTmH0DUnCj6uF2mIrDrf7npkE5tuUJEXYK3wU-qe4gg9aXzmaNxgM78zJHe8EOucbx85TnFqtHleP8q2Z2NKlQ5aiKXOHZMtUEN-yyp8figy_XTfzauvWOnv1TWDI2thebC9-0hUhtAm7HSZmYaASblGQpWFW4PG9NcSXQ-z039eCfylHPJUkkH9E5njfPecYs3SJcB6_zOIOsO34-z9_itpAX0xjGbkYUeDmlf1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bc8vyqa53ij36ytGniRiAwkr9t1ejyHVYkebg00csAFI8aKhK2NKrsDSERnrqzribarM3I6GE68LHA1CNjI3PPKGlayMp-ehmkpvI1HYvJNU4Ty3etqdBjbDNLRBfkW7-W43LXL756_HLct3ac9ydiGFqC6lvUBCGJotnsWaucWGmAUvuyd36ZZPJdatatBJNDCGsAFqrcvZVdUiQKRBDaHM85DyzAPcE1lNbb4TwqZ6EdWLZb48yGm1mTWV8eh-F3P1ekDophrDF5LtCUMWiDSBuj-IOeGSAFFcgmLJmLc42Nr-lUsC0neUrJSML-wmTfg7-5oHI8LwyFvMc-uEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bc8vyqa53ij36ytGniRiAwkr9t1ejyHVYkebg00csAFI8aKhK2NKrsDSERnrqzribarM3I6GE68LHA1CNjI3PPKGlayMp-ehmkpvI1HYvJNU4Ty3etqdBjbDNLRBfkW7-W43LXL756_HLct3ac9ydiGFqC6lvUBCGJotnsWaucWGmAUvuyd36ZZPJdatatBJNDCGsAFqrcvZVdUiQKRBDaHM85DyzAPcE1lNbb4TwqZ6EdWLZb48yGm1mTWV8eh-F3P1ekDophrDF5LtCUMWiDSBuj-IOeGSAFFcgmLJmLc42Nr-lUsC0neUrJSML-wmTfg7-5oHI8LwyFvMc-uEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnJHM_7IEvlcn43cTOaXoVJx_9oCdSh1fwaN1CvEMGO7VdxFqgk0PgA1ELmaLvu1QCs83pp_oA5xrdjlCUfvedQ8n2MN56E9fCknLP4fvnKWm_MsiLxJMxWMOMaxHTmr65sYI8-bfvzY2uLsSAF-g3GWFp3Kz_pGEI7LEEj9SzxphsEOch9LI7ZKY17fyJ_n7STxXA8uThSfg7ce40tEDVxONjbXZPfKe6J2kOrFWQT-oWA-3BFP6tUR2sTFlogxrqGwpCM7dRceCU2CGy6nXrmErih7WoCr1YZN9Xo2f-jaWMDbXK-_I02d3OPi-4IxXbOw7ykYM5LV-KSCMBtt4A5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnJHM_7IEvlcn43cTOaXoVJx_9oCdSh1fwaN1CvEMGO7VdxFqgk0PgA1ELmaLvu1QCs83pp_oA5xrdjlCUfvedQ8n2MN56E9fCknLP4fvnKWm_MsiLxJMxWMOMaxHTmr65sYI8-bfvzY2uLsSAF-g3GWFp3Kz_pGEI7LEEj9SzxphsEOch9LI7ZKY17fyJ_n7STxXA8uThSfg7ce40tEDVxONjbXZPfKe6J2kOrFWQT-oWA-3BFP6tUR2sTFlogxrqGwpCM7dRceCU2CGy6nXrmErih7WoCr1YZN9Xo2f-jaWMDbXK-_I02d3OPi-4IxXbOw7ykYM5LV-KSCMBtt4A5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQS5lj-qjMGjBQsAt2M7zwm9rrwrAvJEXFQ-ykPtDX9cdvad4TQnxBH5ZIqsOHJsv06-JwNXqg0HuRXSC-rYCCZZHS1rR4VxwIK3jiYm0agm5198sQEaYfZQlcW9Lfq8wRCjbkpJOicIyUJFxWzDvhIQTFNqplMix2Z9wHnnxBTtZ4QoKZkZQmKUmqXDZzzD_6_2vZ9XcjwSi3qlG0i2d76tTeSNhdPAb-fNqmd-bzXHV0S1H8Hy7qgQbrBebXhxpC0EiPozQrZYfTPDML8oAE2M1TUk21XgoZtfSppnh1AMtwLIKRn1Y4ij5vVi0e--q3P4U6DFnfitJf8bFKf4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQS5lj-qjMGjBQsAt2M7zwm9rrwrAvJEXFQ-ykPtDX9cdvad4TQnxBH5ZIqsOHJsv06-JwNXqg0HuRXSC-rYCCZZHS1rR4VxwIK3jiYm0agm5198sQEaYfZQlcW9Lfq8wRCjbkpJOicIyUJFxWzDvhIQTFNqplMix2Z9wHnnxBTtZ4QoKZkZQmKUmqXDZzzD_6_2vZ9XcjwSi3qlG0i2d76tTeSNhdPAb-fNqmd-bzXHV0S1H8Hy7qgQbrBebXhxpC0EiPozQrZYfTPDML8oAE2M1TUk21XgoZtfSppnh1AMtwLIKRn1Y4ij5vVi0e--q3P4U6DFnfitJf8bFKf4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOt9aY1y1WjGr26XCUOaGmD8a2ZGJy1KFiYX0i0fWsNNIYaMvYoDXYc0TIZK_F6JZZcwOumYBdfanVKxCUSG2W4kN3f1h8hr8p1WrcOixAC1KKaIe2dv5F2ONMA6t3pBVGlBNq1pkSIt9GsH0JDw-BLI_spJMwY7X-htgQHXOuTBURX1iC1kCJxCOvCr-Mh_OTSfEe5bDTItvEG3e-ztjV6lzvLGLt2jAcEJuXbS9_yYb-qtGwy6B2uXf9D38Bzda0joOmevhy4Ohocla4t9R9s6cGxvBLyI9RD3ZEsKnaSgEoDT5NBgXDrsU1U008FBcpNZ9cj3XbQkaHZf52Ld-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNf7ic3mbObrhlwDOvvTYjkM6IzvOqELzAsttP4xG9k0dC-g2o8PFqW-nxB-rhrwOy-cQlB2_-zPHT8qbwUAN9vFX45JiEa8qbZ4bpzLSitvSpS8LbnFBjT1GKWOe6kkKIJMBgB1zDu45uGwc6R-faE9Ny5a1e5UUAZj7I11MrIm_-3-lY2sJvm_6sIZGU8p-jIUKP-kKmnZNWpYTtf84rSh6XC7nLMvLtCntSKJQmASslsaOrHpdlJteUFX9aoeJklogzaiv1ZoKJqpsasYL2Y-Fn3ZOPw5smS5tygtH9bNAPR5obrPEswi9bv3_SLyPW4QlwHDJsFMRAmwewgicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=vfhI-xTBc2ntlmDQ_kpRNUjh1Xjx6d2jbomzBcxXhX_yVDOylwoO1TrfpVWksLf9lIExpYgQLwuHBOiEy6dPhGdTBTvox9NlfA7fXjM-MYBJkHZ2nesEncjd7W0brG3vHIk3xBUDav8-ugifjTW45XKe1oPSVomGR-3g0t9DGF1RJFq0DRtqSDXtFD-oUhh6ayhH6DKcug1mQ-9_RO5UUeptQkEMPKMV9Qu5uZ4oBJvp6iqYYv0vLvAjgVN3zL-LkdsvsuaZaUE0FMO3kWxkeSxmzcMhoXXmTRIDaEHmle_jlYQe2o6_JjYHMNiCyOe9HoGxaCuwRhu16aiuSeIkJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=vfhI-xTBc2ntlmDQ_kpRNUjh1Xjx6d2jbomzBcxXhX_yVDOylwoO1TrfpVWksLf9lIExpYgQLwuHBOiEy6dPhGdTBTvox9NlfA7fXjM-MYBJkHZ2nesEncjd7W0brG3vHIk3xBUDav8-ugifjTW45XKe1oPSVomGR-3g0t9DGF1RJFq0DRtqSDXtFD-oUhh6ayhH6DKcug1mQ-9_RO5UUeptQkEMPKMV9Qu5uZ4oBJvp6iqYYv0vLvAjgVN3zL-LkdsvsuaZaUE0FMO3kWxkeSxmzcMhoXXmTRIDaEHmle_jlYQe2o6_JjYHMNiCyOe9HoGxaCuwRhu16aiuSeIkJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sai6btx7gqAGdevxvGUtJKCEsn3dWRebvKJHPyn_16F9ZuyaMySfH_7Y3WPWbsOoCSxJzWy0YxOSMZ463_M3QAlRVWT-schayhNTaPhVkENX8cKctSC32grYCWrHBAn0zALYo7zTLmRfFwtUpCxujzcW5CG7_MRQd5ySjSDH5GCZ-188hPS5GnZGHsIIATEMMBAKamsckUgE7n3S-L3wC_mvRoLmZgKLZ3bc1sv2b29gtRfd1dlXETOzj25O5lRo12j8X7XE9Nm2GqECen_VPFyYmkWWloyEC74dZOkerJclHroLN7FyBzVnJ8hZstcNM_7fUdQo2pozHCFP78kMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUfaTMx8ORoWGymOrm1_qazA6cjoQOR7NqFelO4iJ2cbq3sGTGmFV7USDNE_cc1DmsYel--HGzhRpN4_w-jYh6YbkRFw1rXk8ygBBSnTnhOWCawUXB3MoJ8mdT6XiAG7FY6W7F21AviKxdzDhfVOPyrR-d48V0ubVYAkzCz8I7OA5P42NUwCy1QEhjtzOWegObaSQuxZlDYr6d6i2frIl-Tj1jZPRP7-V08Bfep0SbD6ZT1d2HlyU-B0C87UL7gXGTf4GtiPP2KluLGpFvm09-hEVm9d7TukLjnocJNBv7_F8G60Rcv1wpRk0Ediu4Pl-rHHCKOGz6cm_U_8Ue83vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XC2gWtNB9HgEKy75RAvQkrM8eQDvVhzAfcp3Jow1ytgUzd4_GlcK7-3w-PkbYbw7yIUL1HECxJ3_gl0vVeKsNYd2BesOEwPx9K9gT_5l6ZDUdlBn5hFrg4bIW--Nhg6yoHbOfZnyzgiOnkfRmt59V284ucZ6_Jz3MXWtXtf6hRwkP1cAk9EyFoZY9E3x6b2useQvcgtaxmva-qgKV74MI9P9veCI_lBiPVf7M010_UOwYW-9WvtJnY-3OipRVc9fWfkn_vevSLNvrz8bO7p17yIiZ2A6yMx2lZwKVpfZA45wXrryxXHu0n_NWKB9wOrsbFfBEOzFVUy_-H14XLVNyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=ZfqiVeeQdoWgxzyIZCv0vfPLVbRg89BbQ9NYlqto1W4sFa691W1IURqHaL5QZ8kMAk0CKmAovmdnKJvjPgwiGSGdaMDjW1wcYRSoeBgPA20657bML_rpiGBrzqXCSFpyoxZrBw3dRiz_CUpYf0K3yWex54uBkoLmHWfds4hkSgdurD8zQk8BxCisuieijcAvwc8nlKz-m1dA_wURPJVSiFu7xTZ1clbYJ6vUoNHymUAEZmKDwNThRq8PBtGENj6hRRKf-rVH0dXwCXvrcuIKfwxBPOXb9cTQZtkO9Ixdr7ly-kjgNVCKSNbQsKZK6NTHKlWSSbzuEa70X7Z1GkKh0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=ZfqiVeeQdoWgxzyIZCv0vfPLVbRg89BbQ9NYlqto1W4sFa691W1IURqHaL5QZ8kMAk0CKmAovmdnKJvjPgwiGSGdaMDjW1wcYRSoeBgPA20657bML_rpiGBrzqXCSFpyoxZrBw3dRiz_CUpYf0K3yWex54uBkoLmHWfds4hkSgdurD8zQk8BxCisuieijcAvwc8nlKz-m1dA_wURPJVSiFu7xTZ1clbYJ6vUoNHymUAEZmKDwNThRq8PBtGENj6hRRKf-rVH0dXwCXvrcuIKfwxBPOXb9cTQZtkO9Ixdr7ly-kjgNVCKSNbQsKZK6NTHKlWSSbzuEa70X7Z1GkKh0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=ve66QkxHOIe5V-Z8PUHd-i6VWNpPLC57em__rZQZ72Nm1N7uz7aJW2W_DRIosmS4EkVWybIuh6R8ziPFk-YjtqieoekdXwUX_UQeSrljaL8Be1j2D8TlDQfW06GF7yxYoxpgq5lXDRKXdmELveEWdOSQnhswF2uaQSdHA7eaLY21iGQVfrwAzNSvz6Jx_OGUh0rTcJLN9X3BZgmWVkWaNh1dEFF9rG9zheLhr2B7Uhx8UgRD3gxXG5WhySM2mamjKMEV4cs5Q_uabzsyGmRw8KuElMFaN2m8IBRCUOJco3A3Nj9_OFEvlK8eVHzPQYtzhZ16rBj_f3mmuASRIfFO0QXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=ve66QkxHOIe5V-Z8PUHd-i6VWNpPLC57em__rZQZ72Nm1N7uz7aJW2W_DRIosmS4EkVWybIuh6R8ziPFk-YjtqieoekdXwUX_UQeSrljaL8Be1j2D8TlDQfW06GF7yxYoxpgq5lXDRKXdmELveEWdOSQnhswF2uaQSdHA7eaLY21iGQVfrwAzNSvz6Jx_OGUh0rTcJLN9X3BZgmWVkWaNh1dEFF9rG9zheLhr2B7Uhx8UgRD3gxXG5WhySM2mamjKMEV4cs5Q_uabzsyGmRw8KuElMFaN2m8IBRCUOJco3A3Nj9_OFEvlK8eVHzPQYtzhZ16rBj_f3mmuASRIfFO0QXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE7VZ8H0q8MOg-z0UUQs1Re3gsNUkhInIpYupoLO_t-TGng1XpAJxbrWoouN8p6GAwbruF1y9GwFodT8awDfi8q_yn9b9d4DA0bv3Otldv_DOPq6s9aLeziGBufvDDhXtdKHigaN2_Vz0XW8-FqPtoa1lfzWp6lihAYnlrOSr0vv9eugdzsBxYWw_yf64K4KEL82Wy7dEbbXMgtCxpH_04lqg3DTQtc9JaZbfp7QcxbL2tjb5Ihqt39Lx32WkxrjsSreH_-xOqQ0zGEIvwWCSywqEkBKzH81bIienHWjqqtSVH4oDS0wYb_Cwra7QJvRHKOjkKztKAF-H8Eqca-Gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guH8tV8GLBliOcrS02DIsr82X47nwsimYfRINODNSA16CFZYZj5OGwIETwBn-P_dlO3ITITBfwET66kEdaI8e733y13wall296Lr95_mJrMsc08VrCssSOlUy1ndFtu4GdCM8_VmmFt8VvVvBpIRxClGwFaTyExZvZUgmI3uI6nCXJjBM34Drqz5hqHYd-zfekOcU-LeZ3-tywefTyHoP4JpaJM_WAftrcOXoJkgfbLAI-GM8GeKJXVS-8xo-nyklP3HalVl69WoNIiDaa4HQwGRzy9SC0BT-27lhxdta8mC4BTrKUHmDPNajWznOBRMmUhrOhzsmAGD2OoGRbcKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=nyGPomwI6YbEexhac4CM1hWxr_Wj6m3ZhrRq61G5cXJioW1ImBG9OPQCAdMzdK100S8H4jZBKaQPWMmdcfRBULJGDoreGql49BjoUXUy87a3_mY0SlNR2beh6EoWNPdTK5mCcqR8HKvhcIX95iU9E49FdB0nlrymPr16HVeGadbbxW7olwxPyhFs4wy17YOCP9oCy3S9v4jasXEEmxM5X-9LVJINilNHxbVupz28W-W6RuGxnWSmHWVpuletI44fEx2BxosfbSrBUIabvuQeXjw0ZTLxA03nUj7FaHswKYYA95nli7qCuLQDTBmTjJAKdcqlVK2AdbkbHA3xyN5v8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=nyGPomwI6YbEexhac4CM1hWxr_Wj6m3ZhrRq61G5cXJioW1ImBG9OPQCAdMzdK100S8H4jZBKaQPWMmdcfRBULJGDoreGql49BjoUXUy87a3_mY0SlNR2beh6EoWNPdTK5mCcqR8HKvhcIX95iU9E49FdB0nlrymPr16HVeGadbbxW7olwxPyhFs4wy17YOCP9oCy3S9v4jasXEEmxM5X-9LVJINilNHxbVupz28W-W6RuGxnWSmHWVpuletI44fEx2BxosfbSrBUIabvuQeXjw0ZTLxA03nUj7FaHswKYYA95nli7qCuLQDTBmTjJAKdcqlVK2AdbkbHA3xyN5v8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOn1cXcLLX8RmlIKGv2sSKfNDl5b4saj7VDjTZUj9Pr7VCctXzJ5ALEqty8YP9HFS1NSbGV37ZMk5hV7r_4AunibNggK3W3BZulJJd-W3cajZ3hZH3ZAx7umfHekjBfAf42QpwTML36fxEDGrPoZYUI66BffST_LPsZZf7G95MSypVKCd3_Lyi6ObddTO3mBwaW9fuXMoS4ptV1R8KUDvItn50wX7zjd0SEzzbnUWx8bq-f4D8YmRQ9UOFhDqwEeyCwCB-J_yjPdTlz5NJD58aBLEqkRxBLARF8mLL-DqQoyggxqj2o5dscV8gnFp8FYLyAHimOLW32GHOGJjC1hig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGP_zNwrwysZ1iR7vGoTEDOrI58CRPFZwhTPFsiLEkJ4u7MqsFyBCn5bxmfrcnckwsEk4kcN8iSHYpFsIin8XH3DLBB04OzeDmKFc3sSI8hBNZq4CScJzl9l0SKrp0BNaz3ymWRmO8b5OVX1a9PNkdU1IKNxiSws4CxhZR1yEf_ym-Lho9cKGRKu9Vwj--TLzNApAtaOh4USPu6sS3oBVTWfKtBoLlFLuZ9Q5VZIWmX6p1dVHxlgMhU_lda_I5lOO6xvUkuXMXeS5ofL2nMZosD_XKl-fPMyYXvVoJfOB1B2PIRXvMLHmOw804Nz-a632GmuHMjhhG3RP5m7U7Gy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veU_Lmj-fRWOh2ctHNQNfutT3svtaSegGxfe5dBtIBVYetow1F3L4QUhDHIHWHg9hV3etU7S2vkFWFhUCYiy0ZAfgqxqUF8DCb-aei0NAjjkasLj98CM99nVYjNz9IGG-bL9NbH4zl6BjjtvxfcgPLbm_U2hhs_hwKbwL46lCuAuzJqx8KTJRTTZXXYgj4VUA9GwlILoN3z01mFnjHheSVNh5PxhfFNi445U2jGPnu20dyd6zzL88VOubijwwyxIHMPPmjCSM58Vq-T3SYhnjoO9xz2xgvujY2PuTxfpp3_W1r0PkA_QS8Mny3U8vHSm5GiUq14N6HPhWe4kT3K2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLUAPcGPtgc0J3U6_GdyysOeihrroITWzknBWvYB3UGXBjTN8v8XJUQiXZMjO9Os14vXwiOPOOuc47vPFulV7CvQNLbO6Vec27h4tjK3PjD629Umy22WCY1rTM-YjN_E4XlYJH6ODAbxpl-QZ6uqpC70HWeaYhmax9-iRtJKhWugLvqM91IYkJnbczT-KRdM6_oxoxhdyXObJuHH25ATTp9CeFzzoIQBly859fSMATIg4NPHoMB20jXK9Vi8_N1F51lExnqZ7CiPXobFQBqbh6jgaJ59-YkPmYmEsk6HQFpcJOWGjUx7Qc0OIN4v5bTpR8UGrXG-YpFlKGTQ5A5xt7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLUAPcGPtgc0J3U6_GdyysOeihrroITWzknBWvYB3UGXBjTN8v8XJUQiXZMjO9Os14vXwiOPOOuc47vPFulV7CvQNLbO6Vec27h4tjK3PjD629Umy22WCY1rTM-YjN_E4XlYJH6ODAbxpl-QZ6uqpC70HWeaYhmax9-iRtJKhWugLvqM91IYkJnbczT-KRdM6_oxoxhdyXObJuHH25ATTp9CeFzzoIQBly859fSMATIg4NPHoMB20jXK9Vi8_N1F51lExnqZ7CiPXobFQBqbh6jgaJ59-YkPmYmEsk6HQFpcJOWGjUx7Qc0OIN4v5bTpR8UGrXG-YpFlKGTQ5A5xt7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTuFJJbB5uZ8mlrkxMoZaa23Ee1oA8E6JjW7w2RB8d9MEFEO_oy4BWP0opmokl3LENkbxnHfjAKM1lEHYkqKA1Y6d6RBTTGXW8m7bVFuo10se7-NIYzYRAc0ojoJ2a8bbvBCtAtVa5mwXuNGz1y3n-eg1kdFt0ng37wuo4U3XAipCTjtRItaw00_4fbXSwzCL4ahAN-zjONqmDddXkMR6R_jpu9RNFq8A36IOTFfJxonksMsgdpSylGPIMqIBEqnXppMa3pQDnurs6iMvAJkcmOm0Du4Ynz6DG3VbAFru4wMIlGT_Kt8iUZjtup3qsgxnou16-rweuNFdWtobki1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm7OH2enot0rW1sH9GhZipZ4vJ31rput37ywj9zAOo2d7p4POUKVoikgqeWZzolCGZgD6HPqV-iFkafICsOdNWpY4phUHlRFKfNefQ3dx3v68MASB5QL3_gfLP3bw6WxISRvJfhOJL3Y1L8M8_WDl-G42sI0tBLT6ay_OPzuSgddgR59pLIQ6S5lBWibiYHeV6br-SDfGos6BPZlxdywHHCRex0YtAb12Xn1l-mcuSU1ldbTsF5eUDQ6oQ9wbJhxjEsHUZQFUGrdeKGN945uOq_8wjirb0V61H3VriazDjEFTjPhvmrySDxiQQXLb7ZzCm3FjN5RuglAxp_74glYYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=VuszUc4sG77Lyo7GFu-ElYEE4niLUQ_ZUSqdYkMtrseQ5DGu9jXyyHbWQYF-pAfeoV8BDzI49O1cAEoHdiPzR2xy0AO0u-52Ta-ugFv_nBRD4kdklDmS-_7XTVgwCsUYOOFTnFoU4tsIF7ef8kgIJw5JyFMrWVzGgQ7-Z5j5KJ76zxJn5NeYuApRqOMCFA-du4YOiY4IzN-BoNdafjqOu0JKmRG75rETgwD2Xcx-_xdsmswRoOUnJZ4f3EMBskbCqZ3lXX-xN64JW-Y7sGRjyFhtujImIW_AFjqDFOmR4RfL9V8QyAzWXSCuFyB6LUB0yXc0VCtzCvxoSYsjYD9FnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=VuszUc4sG77Lyo7GFu-ElYEE4niLUQ_ZUSqdYkMtrseQ5DGu9jXyyHbWQYF-pAfeoV8BDzI49O1cAEoHdiPzR2xy0AO0u-52Ta-ugFv_nBRD4kdklDmS-_7XTVgwCsUYOOFTnFoU4tsIF7ef8kgIJw5JyFMrWVzGgQ7-Z5j5KJ76zxJn5NeYuApRqOMCFA-du4YOiY4IzN-BoNdafjqOu0JKmRG75rETgwD2Xcx-_xdsmswRoOUnJZ4f3EMBskbCqZ3lXX-xN64JW-Y7sGRjyFhtujImIW_AFjqDFOmR4RfL9V8QyAzWXSCuFyB6LUB0yXc0VCtzCvxoSYsjYD9FnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=bProgljLFtCoYF6kMFO5HL2u1ESDuhX0V9Ky4dS1nfR0vRo6ldQTQX0pzVAZiTDfmpxh9i8cYQQ-50RKjyll-NJBJhiT68DJT8cHdVA_tx9w3xxDfvWXHdstz-GPmHHGdh8HhqgSF0f5aanqjj6qd5nvtPGzjdA7vzV7TUE3APjcCO9vaJaNPic3dfBrFeOL_rNsJ5uk5V4tXfngXzF2BKYI8Gw43e9GfmzgaGUUZhkUc84TZq22YBghAhW1nEi33lyukKrHbJwpxnJNwFpDL6yezkSPAA83qYkFC-eouEB-FCT34v5yGmgRIYslGKeHl_h2QMWxn5ViJWcfHDwouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=bProgljLFtCoYF6kMFO5HL2u1ESDuhX0V9Ky4dS1nfR0vRo6ldQTQX0pzVAZiTDfmpxh9i8cYQQ-50RKjyll-NJBJhiT68DJT8cHdVA_tx9w3xxDfvWXHdstz-GPmHHGdh8HhqgSF0f5aanqjj6qd5nvtPGzjdA7vzV7TUE3APjcCO9vaJaNPic3dfBrFeOL_rNsJ5uk5V4tXfngXzF2BKYI8Gw43e9GfmzgaGUUZhkUc84TZq22YBghAhW1nEi33lyukKrHbJwpxnJNwFpDL6yezkSPAA83qYkFC-eouEB-FCT34v5yGmgRIYslGKeHl_h2QMWxn5ViJWcfHDwouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWxmPBLMfJ6L8T6EqhrLptYkX3dFJ1exXdmeoRirJEx7mcAtzPhNJr06wnoqihbsJRCIAAVRRC2IjBh5Ylh2Afeze2cOpfTH3Ra49PXbuNWvhc6zsIwd4yvUu5GGZB-wY3MZ98M6h4wgOVhVtnnXaiNZSk9K6biVwgAqeIE2NHuQFeedIzERREDMhzQ9A2usg6ukYfY9bSTW4ZdzoVk_KLu0eUhpb86TnyVMO8kcOf7TbgBfmubRNunb-5613K26W_cozKM-D2bboVpOTc93TCoPm6OC0iHY29ukab-V7Q7qif0nLbz-gBn-TwDcj4luhBbanpaDtmQ5d8l5-cboSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLUIFfPq6ZquRMeWBRIiMmv9RgIEBrqf_6oKIrYWo5L-PwX_03eXeqNDG5UF_xULys9VcBn6ONZl7lsTKJXvI8tFEri5M5Ch-xZFDF6cduNWRDqsWSYN5RoUOsUo-AnDFhPMLUJr_zeSefDzdU8GMbUaVCYldB1_7X4ekEfvPolcq213ewWKkDozxCvH9LfmzMxEBmuT_CDSzCCZDvfvnKZRy6FvK8bs0zJe34hPG3A0FC7L6HCTAnX5I8e6Fkj3C0OdNi9ccUxiRyhowww1JG4JjbKFcDSDbunFquuQlOZAMAdUO5fpBXC61GmlAQgIOaQmf1qAMR2Nm-QTA_kxtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=isdgvlTZOlfMGb4KCo5jsdSSBrfm2GnJBk0XMzMBcr1F1e1CRRht_XoLGQiVm2-88dKRvtEJVBIknX1XVquoq6c7ChrJm4cyb0bGLfSD3wwsKYnul8DGJmn90OyUrJ0542JWyDQm57gLuGM8vwF-Gu9tGSjQqWMvuyeMLboGDRv0tn3JxLTtunSuIMXyU2OM8xCfob4i4ShDD0HIiZjExS8DmmuStpIhQ3S0vOq4rubCBlMbbutSCGakJOy6cztVP24qSP-yWcC3QTEYlAL_wRu03vPq1wgWWp-G9m7wOYMG9hd3UQMZDOUwtnxxtiNQQH2WVfwi-5OM8nNJmMpYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=isdgvlTZOlfMGb4KCo5jsdSSBrfm2GnJBk0XMzMBcr1F1e1CRRht_XoLGQiVm2-88dKRvtEJVBIknX1XVquoq6c7ChrJm4cyb0bGLfSD3wwsKYnul8DGJmn90OyUrJ0542JWyDQm57gLuGM8vwF-Gu9tGSjQqWMvuyeMLboGDRv0tn3JxLTtunSuIMXyU2OM8xCfob4i4ShDD0HIiZjExS8DmmuStpIhQ3S0vOq4rubCBlMbbutSCGakJOy6cztVP24qSP-yWcC3QTEYlAL_wRu03vPq1wgWWp-G9m7wOYMG9hd3UQMZDOUwtnxxtiNQQH2WVfwi-5OM8nNJmMpYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=QwUuJEUUzwprIYOWUC1HOEXk5Y3l65lgVeO6rKSoHOeWUV_rNkaZiEo-iCkgSDFWZmRcTCES8XhxcbfjeeT0UjHMoN7aJRlbPB_qCCeQplG4LtjyefymaWTQOUm75MFJFOh8jKTIzNHztoRzrZj8l6TTtl6DDfAboXOmvDkqbMOWkN3cyRjb49DLsnf_TFXHLrLu5yKlDHf7x5EUO-xlGMtSnJDQ_a-dX4OwkHR77OvD8MlrZwqul-MuOaILvL-0QC2mpm4vMxufuOi_vP9NKJkNCb3iKN6AvRPuWrVZoOb8sWpb5qJsImnswfk6xDkDSf65fvkFkYJo8NeCjZ0pQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=QwUuJEUUzwprIYOWUC1HOEXk5Y3l65lgVeO6rKSoHOeWUV_rNkaZiEo-iCkgSDFWZmRcTCES8XhxcbfjeeT0UjHMoN7aJRlbPB_qCCeQplG4LtjyefymaWTQOUm75MFJFOh8jKTIzNHztoRzrZj8l6TTtl6DDfAboXOmvDkqbMOWkN3cyRjb49DLsnf_TFXHLrLu5yKlDHf7x5EUO-xlGMtSnJDQ_a-dX4OwkHR77OvD8MlrZwqul-MuOaILvL-0QC2mpm4vMxufuOi_vP9NKJkNCb3iKN6AvRPuWrVZoOb8sWpb5qJsImnswfk6xDkDSf65fvkFkYJo8NeCjZ0pQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqb8Y--Ee3oXcXpRfNVWVNkQoH5Ywcs5pd2AByTv6GdBmAUhDtrWOtYDAq0yiluBucwZ-bqLfzwxYnbUtlVT8KyUV4O5qMbXAbatSB-7CdfbKLm1v_uIlf-DZlXT0qGBNl92Bs5XGz2_fxJiHEGB172a8B07yQrUMlW9ItcbghJ3XBrjgL8WXQ2hugFY_FUUOaeyfoD54lHqlnG27p6GDmZul7ZmFsAr1APi3y43qrexjNeDNKo8rGxD98UKXs6Jkr82KRK9mLdFGpU-OcNnbCF2Bgxk-UnCKduf9G95f1YxvftbOHd7C5xj1EuOjw8FSD7R7xo0qhMJch2YKgVgfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
