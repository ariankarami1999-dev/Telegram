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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 11:06:32</div>
<hr>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_0-ptsJ4efHkAQo6huPuY_EM4QKUmw1vw7Fw2yb62dglPo2dDtFjm13hBcPVJAYPoD7IXEcdAK3YJ4IoHY1IcG1oY00nzsuQPf3WsFcks194zbKE9VNKMT3gxQzCG3qFkR4ya953IR8ekNef8XFXWsflG52MVqq-Pfwg24Pf-SokaCr6QI0O7kY0_gTyDIeIGrbkgbPVbeW3WALodJhZXGJYsSl2KaJhSLWbLPHWO9JUWQD2QdCAyPo-vAn-LsqVDG9AA_RN7iVdVmu_rtZxSH40UFFDAXQh9545lW37HDkYmQq1bSSN1JeHd8Lbg_pghpsu5eYS4FMh19R7wiWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxcbJIctp1pqBy-vIPYMTXfkOLYCdVVDm8-Uvvwr3MTwml3DFKTfdgV9GGgBOPB_D4q3cVWSL55CN49zFU1oQ9MxtTcRHkDi2xHyuv18yIIE69cJeHy4xu0t5iPQb-BsTFskwTPK0SYkHHPEGC_tTASLAC2vZRt6yO0MLPYflJKVjiqovmNG53LDhCvxQZCxqS-F8tAUL-XojFOAk12q7V7FX1QhreXYI2tt1hc6ZdizKxO1JWCML9tNcek48j9MeaUBk5g9xuK-FNTbso5aNppDeOa9kMvYYzQapRYKqDGwmNTC8x_McUB8lrZDgQ6ld_jkMwgiFqws14KX0NXBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvtSvsV1bcM7QDFgdQMfXNB90H8Uw2AIoDqxs-2vOLWIh2-Mn54CpzsfOpp9bMHORlPY9EwN0TcByvoZC7M7yIp07kS37by5HpraL7YV5ifPUeTkVGSJEbZAmSIjbMeXWnBCkI0GHp2Y2OCZNfUOGZAd77Dtbd3P-dJzAUI9C-zMbwgaAJDs63HtrrKnAxfzvTAJIki4pH4kZ75CRx5pULvXrJuMJyR1aZLcBCwqKPB4xvI-bWZw8RSo2q2YuSvieJF6PS5ilZuTUOOmFlh_RJ4ZUoo34EjNkiRDBg8hMBJzBXtSMdyujdLP3m7vu8x2s-gkWE5u4I1dfHfXUqYEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecwIk7MdzeiOmAtI3huYKz8IBgEYx1uQrgOMebq433RwZpR89mvbqNk4SDCjP4dIJkFKg6YbT6QsdwxIKLnWYwdRrqWkfqCxw_wHrK1YGMraPfZtbNGnBMlgXqR2q3mMAsAUjgsJhpzoiqiSNAa05EbO5bl8ursccFNj0K6i_JOenLAL4ZBs9FXiIOvtSDJR2hUIWe7fTrYIJ9gtZVzc0LQX7yIPoU8jgWA13FljTCXe-GsakB4X1br6ccXijxUWd7yOaFlnB_k3ZAFT0_fRq0pmjtR-w5NeMkF10l2XU3HiznS3-5z9FnqaUeqtM5EEcauQmF4ZbJUEaFTo8aXarA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBrGm3N2XO7Vu0qxqnqhWzs26GL-wBz0sXgSCSg0TkL3PZaKh2VZ3iZRTGbtiNSd3CbSs_xJkF1Piq9VDQlmenJtxrKuxTVR82WlrS2FN_-Px9JAZ5XEebErwDvI-CbnXuENC7Vyo16jGsaNkciRnkEm2iM9YMwVOReY1T63ejfv3LSps6FcHT922ijr1cvS_csm_lwubSD_dagWiMArDZv52fZilKNIw69TPGU8InnY5wzF4UiavAnwtDSfmijllKFUQu5WM3iGniBDqbwx6MxsQCsaeGf8R1y-YlXh4V98ord3QT2-Pl_t_kb6SBHYsoKXyqAEMQgdEEcRSKM7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twwplYWwgs8eVRrgiS6JahCttmbyjr8mNa4AQ7bEiFHfpEiuDQ0VwB42zychZIeCuPSjiH48CydFt-2XFHpDzEv8boRVFRbE9QYi45DJpTneiCFRlfxshMPBmtpBFNfaryZiLbPsg5Yyol3wGDz7NFD4FY35jcKhJfnUUbI3Nk88jq4KT2VrVDzPvpcXPyKQG8NmFYwWmK4u4uo1BwnAFnr5j_nwC1nCcxqGaE2K4KoayVA014zQGUZzRCBAVXp6O4U2Z2cLXxBw25R8Hx3z4FxMv7-U8drr2wXsDEtSU9YeXBsFycJcLyT2LkZ2fm4x4G68YurDxoPlSfImmq2dLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPM9JTNuYbrbe0JD8YEDZfvXQyj7t4FzQDY8wM29n06ao1wnTyfljWrxIDRvOrdbPmpiAnU3qCEWzsehbLs7SW6x92KR3ran_VMjpHuiG1JMDsM4anUVVRpqgdpUYqNX1pKAt4OECbsjBr7tjuSYYa-Cg_457t2eKDdff_ED_9q8fvf4AVNibEBTWpD6mGGTnaXGbptq_0inm-X4SpUjBLcv3_8qi09mSib4eIteZJiFPOsBPqpQriXKckwGH5NdWvWuUxmwv94_5fn3BbfUsOxzz53YuQdlloGERU-stpAfbUMzRkHFSTh_NhBzG0AYztD02Zq4cHevf7bpen13lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUBQym7NJVphElQxklFu_P4bTSmeNHcWBFfd1xcbtrcorVOzas1a4Raqg2GwayyMobPZjcV28UNbn2zgfkfN6NJDGSw1oXGvfgIO2NzC6MM80yvpaQgB76Di1EdenUr3fJYfQbANOOK9ppSIDKldTZ2ADxqIhsU21HWAsjc9dU0Ot7rJdnhHTmP1fVod22NOkW-HYNwv-DROfxRnMG2CWkmw-NwUYTG356s3mRW91IZMVG_qCoV37eWQD2FbWC19mVxAchfVO9syUo2ob2j_IWF7jC-UATkGneJ2DfJeXxZLusDZA1WthSMgQ3yKR4Z_DF_gpjYMJptiyLzDlxA36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcO4FF5b4dTRMQKJtwCL_bihH35_uARNlmMZOVfrek-UuGwopoSNdDQxAFXIk6MiRpFxIFBbfv32f2QTIpPvMbbhx95asNHtu4Hnw4p7med1AhAS28GrKG4Z1agNIyhQ2WVMADWEqW5StUhrlnRJ1eAdcxhnWXyA30_XHCgnvAgQVDZRxodjmq3e7TMW83qSzK8FowlY9sxSnjoiLgKCSXmsWdH3CDWH3JrPbt8S784w06Nu1suxAc6K9sSq8B9e0fyRF3JvNdYwq18_Axqo23AJosaMhevc4Jytrdh7ict4fAQogn73gyzJxQSQCTlHMGu5QSM750gBB3WMV3HRTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO3Sc_bpYjKNFrKAIizf-6pqX5hPt_GCitc7VupxKQPv2RByhPBM9-MWXkNLTiZECzsl7Efu2twbJZblHjEMTMU-YfMqHBtfz5sJXJdFU0SPR11lcV3nMPdH6OSnToImddZ_Kw5_TTlkGepPnxQMIfiOnQ9PkoMq3GBVWSvroZM885VnrXVn4Wopc6MpvZe0EzsiE2IS-nTfXl8zEVhnRKlG5UX_uc1Yjof-uJkE1ubVjJoZ3X-vxIvNQ7YZBbSbfFABQyZLCCQEBeGil4UQ6ovBtsyhxk1QN-HmIcXlKMyYRJeS5moxzS0DS_MBYxwm-NNhhsK0h85p1lzyEGn3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_GV_tV3L3Drebzfjfkp5nkl4xFbVtylYepHPHaL1EsMrKTIQ2adn7fJT0WkE16ZUny_4ENAgNagHzOLCXC3FFZRE-KZpzXtQkWQhOzyLKl4islQucY-hUqgK3SsGbohBXEInE9sQw46G1mQzv81DAhqjvy94kfPZvNB1TD8nl9aSK1NCn1m-j94bjeErvd3kywb8xAz3GH6VM9U6mc4Zu3XAi696o-whX_WW64XVwbX_QFYb8LbcggePDASwn1eMgEu29nx_0gm_oBry8nTpt2QdiFJ-vrPk9CbSdP0Ag9Ogulclh5pJlB1TO7j30pEM2j2B7lSScx8d8E2BKQ9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccoP9b_oq68nX4EaTFdbFoUcV1NEYZeB7Wu1UFCnuAitIzG50qwRjgVjj3W8dJfYbVS7ndvwl26_e5dV7fBlcyhU8nmXfLP0MwdgNiquvzAtEyH2qvjKHujDMGX1W0jg7yVDhXRflVAQh3WwRd8LMQqeHNCdM-ygsloV2JYyky3wN3zTXpEUw4QNU-2Qu2AGu7fiBLqFoynFW739Oh7xPvYB-CPeh3wvxUzYJ5f_kOvZpcGDl70CoQ7WDR4ru7F0xFT8Fh53zpExj3GgME2wQYLb8Y_JVKt23hnlTNizQ47cJYW0uJSILiex6i2ehTQPVzRHXq4BayUDUgOf7vetow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUTQAlMPiaGVvE5dIYwnOr4Spv71Hvz-FilMu7fk2CIkCetvkfaV1lQBu53nW7HljD-x02b0TGHPNx4o_2O39ZJZBBjdP-piTYdJ7KhC3Blj42atvICZ4R50TXCZnKkjeol9583h3ewNnYfibKJIBNUQHyRpkLDzmo5hQgix755m3B18sIPO-3MY0VADNGtP7jJ1Chv3DRI_71saj8S3XD7rb8YYC44uUgmn15terq4IriFdhj2Jma0E-WVFwEgNgWw5dttWfQoeKS500l2LeRpCfoVoIbw_VISiZPa1_KHGinrYatc_pAoY2B4W3N-IwwHrpikRS5xsJihsAaS9rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVYJmemV4pT9JsFEm34I-UIoBIJkyObcRachMpP6Iyeo7lyetX2otEFiYVBCXmhShDoMORxo_QBhS0hONQ_SgyEyyVoytVMBJpgw7A38d6S8fGEsgZYOpxVVJ3jBfjPnj9sibpXXgG_5ApZ8Ckk0av3MnIdnwWFV-7G0qbd36LfDmIEdqgYHCCuOcFMMOoYdN6ysMRvrt6LwE9bApACQ5hTC82Tw6-aXnqVi0mX8suWhY-l6EccsMFKXB_XW-NrWE3bEQWg3Nreg9TEdH6kzr8Gx1CvpVOorQOtimKEolCUFCRzz05D1AzXGDeTFxX3KcFsU1SwqDRY06nzVEeJt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=PAYYvBA5z_j0YVz8Hn3_AEoT_Wm6gCu9dGwiPmBCKi-zM5iJu9SlTlVd0kIWbZ6yfJBCFLbcECRPixVCHKSuQlobQDT4cNROfm-IwH2uXA6GpftrXnd0YNR6dyl7rXMdNeSXYlHhXScoZQhz4LdF5Fa3bQJRck0FFnh071BBI9YkCRojsxCVGSHoKT9Xg14_qIwsfhH2OjMxHq6VYlFmSF4BX2X4sSSntUSUrVclkJfLKUbfNXBY-uey8lQZLr63gqlYVG2XJmlcCHhfPFpVbwTgHAGVcTbgKy_qp4AoOicxtVJ6BwzexjsQPPH3QlAmoTXnGH2FHE3xSWbzZmLH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=PAYYvBA5z_j0YVz8Hn3_AEoT_Wm6gCu9dGwiPmBCKi-zM5iJu9SlTlVd0kIWbZ6yfJBCFLbcECRPixVCHKSuQlobQDT4cNROfm-IwH2uXA6GpftrXnd0YNR6dyl7rXMdNeSXYlHhXScoZQhz4LdF5Fa3bQJRck0FFnh071BBI9YkCRojsxCVGSHoKT9Xg14_qIwsfhH2OjMxHq6VYlFmSF4BX2X4sSSntUSUrVclkJfLKUbfNXBY-uey8lQZLr63gqlYVG2XJmlcCHhfPFpVbwTgHAGVcTbgKy_qp4AoOicxtVJ6BwzexjsQPPH3QlAmoTXnGH2FHE3xSWbzZmLH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqz65LI04FsStkC2upZqPSZ8NCWm3huOKD0gqsLXRUaLANC_s-rMuFhK1JdSA6QVt8SQHPx67Tu02toWehshir-symtci0ZSqVe8fcwTHXaHAkIR-valCCk6XJcXMnz0_tCnQcCDiUhzXWI9HNUnYDT4phlRjYKFoxKC6weSeohSnpm-7fTUnxxZXmlRC5c8QMqPL97bCP94OxBad-0uWChsboEFjS36F8B2Nrtdgbg84o3yQJjSsZN99woYD7dt4D1riFd75F5y3Wp_pi7K-ho2ahfRX47yY_-mLDsy9MvY_ke3UR_AC2wnntBNINy4yktbpcz3ChmTDLJI2KXrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6rrDMfXs2a6l-Y18m8IegCOznTrJkqU1zgEWA-smZb09Fsq1Tf3S1oc_yJ8sn4A0PX8xhHVQGNrxGYcg0sLj7uh9R9w_hARxNAX5Xp8UUec0cwCp7x1_UMnSqWdxuobFBtuek3nnpyI_X1y77erZp6Qo3KHWqaEcoMZvPS41UXdkoCNp_H5MEyV0NeTin5pOsxDubUyDG6gm3lRM5r--yYomtEMVlB1Cbk3NCGI1eJ6X4p78NYpKhZgE2IQz8VS1lcba7l96dHoCj5BrEYE8zpGjtnYfif2nZLipaRSMR9a1wRRJJOFyTBn5CtyUigCff3h12iSYDTp_t5OObRBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeJQoHhgUCwX4OVXYuxI8UTW8euTJVr2N_0H_9v8rEZiS8v4CoZRMi2H4OfSWXaOXPdXhoRdaWWBu4OD3cqIvcrX9Z8pJtB_7mbuEtgb5SCL9qZqfNMsSopvbpbCdYSgjUW1-lshlIhHD3co5N8taiwDf9jbyGrAVJ1FdA42jtXFa4ZfI78uMnVHxQ-MLBe_cnl-PbLiRyjKmBs6z2X8Wkg8rjqC6LRQb7IXmNt_t-vVenKuokMhC4wqV0XXG0n3fT51BZpRb4W_lSboYOvY-2dmmra3NqYxFW26MttfyCCEw_fHwNzQ7jPqhSHE147dd6NkQAvkQqMXTWy2ngGluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_QRr8NlAIPmGBkbbjAJu7fZRhNoBGQQceSTKBiVbcuEt2fmMacqc6PxSIcY8oHTWd1eFz14xGvJmdElWPNDa2jZlaMyoidUE_KPb2rPJWAotjQ_EOXoimzawNQ8Qhc1apCBhnCC2nxPn_8i0BkV1aZrn3QID3EJS25Xr4uRhdgjyDzkjATiaYACkQkgtyjNL4nktcDq4Y16TZ6K68f8dFdeY2ifBTv1_9N2kGWJRcPyFbKfZhnNQ2R6hKorGiuswSnw9fcwxSecGDzl-tixog9GPIH53pbBr94kFD7LCZXfETCGiXCPiarCqA2MqPaSFbPoo5eslbKyBkAoB5T1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzfJ5Ac5r2-xuGLAg3H77nMHggbBZbo31ROh039s0KU5Qjjm4MbYFaHiDBHHAbxTvd8-S5k_nvnu5o9jUEG9feBefHetqsoW8MDvQ7GgVa-tEAsEbf8SXtlksssAlLfrLrzTQ_it4mG5CvGLPL01utS8DG9lasP4xZQ_UfVYDqck9RHLpW-zI95x3lP5XVyiX91DMKP0AalBg__sQYjc15c_JJk7L5t_VjqpYfxQ408lwuS-msGXabkz9abYPUE-JrNKHUe0G3FDYTXY3lZE_9Dx63fzrIv2rcW3Op1h27tp_7CS6MZroRsNFTbpFlIOBwh8jM3f46FrNIcWPJnXEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ssks4Ce7iFKaDMs36lSXf_apG-fHjXAWNr3gjob7t6fDltS4AEt9ETSZHMUARsNVNldVFhZvBZQ8nCJ74SsxkXqTmJ18EC-eAkCPxyPGnxSyqIvqK_AEAfaQ6AtySw0Z5GGN6No_UL3vKW9ldcA3EhYKQb048h8f_5Qehz13t1NtEcyw70S6dXqp4bDCIxLPSSNLCSYkFFiq-gvWNKhUxhPUtaniPA2yKLC8YVLlovHPF7Pryi560bZBxYFO4EEhNdjYbauoIH2kGxMI5x_B_u0pBq6u39G1gLJtVRTiKCECffHy8lLSMXhZ87NEf2JNhF2Pto5Q5ZShuHjqUzljHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ssks4Ce7iFKaDMs36lSXf_apG-fHjXAWNr3gjob7t6fDltS4AEt9ETSZHMUARsNVNldVFhZvBZQ8nCJ74SsxkXqTmJ18EC-eAkCPxyPGnxSyqIvqK_AEAfaQ6AtySw0Z5GGN6No_UL3vKW9ldcA3EhYKQb048h8f_5Qehz13t1NtEcyw70S6dXqp4bDCIxLPSSNLCSYkFFiq-gvWNKhUxhPUtaniPA2yKLC8YVLlovHPF7Pryi560bZBxYFO4EEhNdjYbauoIH2kGxMI5x_B_u0pBq6u39G1gLJtVRTiKCECffHy8lLSMXhZ87NEf2JNhF2Pto5Q5ZShuHjqUzljHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsPDbylwfEZ_u7DN1ghe_-n-y2K1osIBfe-ELVfFPJELpgaU6C1M5q3TfzLw2bFX1eY68FxjZqGWWQ9UQpMZFJ8Fqi2dYkckFYzByjiaff_wyrqJOVXNBl5yu31Y2ElJKpj_w_YBKG2rptZqSURH7TZtLwDvETjIhfe-UFNM9VOzIiafAoYPiGcYlqseHk5FWefXkIKJLkPEliEmytzCbBiJ9OdBugkecN4OVN2n4bkKh3LR_D6EJ7WcO4ZQmAdmWrH0kKfSLmdVZKf5v7-k3XpjytYpxjbPzP5vGrkpOEszVnkT5WswByYO8bcacXxN9V2WyUJYtvZnUz-lOuVBug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwF0LlE__WNdmnnMJxJEp7oeQfstaPSQUPusKj326LRpohda7IIMg8YGONqdkMQcosNfhxzlcGcJA8o0lWwHjJAZfdBHOY7HeTjqAaizBifOH6KFMVM4rnU6BpH0HURpC7h-tEZgjhxHUzQQg7ClLLPvoxFBPpijTQTWRFP3P-d_fvlFCLm_E40C5attK-Y3p0BBPlCJVH3sAM7Pdg1fNSh8jHa2ysB1UbqgjwrH1ciVLC97Oy0n9OqD3e6zRLq7ddftqOVGMYr8QEyJNpULmxt6wHNgTl4NlB8aILXXHWkpVJK38sNfPAxDoJEhcH7keeTZ2NL71T6GMipr_aecmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l24HU7nRhLaiBBNriEP_tP7Fib0wDN9K9lJSoosHdsxUDd7u9Ve-ekQDLDYhU_tIlg6pA4AoXcWefplbNSETFGdx8NxsEbpGdfxjAwnzHBFj1vDQQwVRlXK61tDLWse_umGsnajYDOgH7bR0mtkKGPPoYFfE-eVskHRX6jEn8xswu19Zrqjn3M7y_16xFICGPUVPzdSALYTS77htNthDrcqCWE0gO92-PhVqPdoKWKq8NekF9MZv8X_vvp7CVf-psXl6SQpRnaV8FKhH_gRiaU4BCxGe2-M9I6V7Sj0AX4nP8bEVaT_wlWyew0Gn4VDCcAQC8jwPkd_Jqi-GWGy_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwOE_SkzvvIRv12vQQ3PKa_L_2CWG4jrByMvRQzsEKzyCpmA1wYKYhA1gsdJXJGGj54jvyb9DZGMnNvg-eml_nBHrDbAi-k5ONtwELwup3oB1PwLEV4ItqbHFuKKAYCa1WcgA4HkYR-_X0vgKhGlDocKAytS85Y24VApn2P-gOj3iErX9rBZvgUhfZW2WDGKagdChYv4js2CTEigPdUSsQKRm9aARfYx60indcTOan8ZwRIe7ctOQQGCkkETR55ecEqT-CCNvMuSOCuyUfB3mft5_Ub1WRZHKr_wYnmgPd4BjUXjY0yuy0azlN2iDGwMpR8pbOIlLJ0Ll3-KvqJzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJyL3BWk8eJnSxKxvn_7Ljf-OkUhv1dNgmr--GxIBloaKpdnxjZWqan9YzVjJ5zlai3r_rvzGHtCpwm5fV-9WYz62HWr55Ksf1q4vAxC8ZQc3BLm7azItmsWMmcJYrG39BN_uYLaaEqL7cUWoZD0EfBdtkzwdxb3GmVprnLCHSw2prLzTCrLna0gV2IEdY1Uf72rnFi40vggtzVKQVm0kiY18vl8niEegIKGXXkfM2pF-_bX2o0GehfwSx2SwnWGXy-rk9XjOUl9PQUBF_zS3rRG7uxLeK5pfhdo7M7JZiCw76AcZvTK-1CF-fl4Qfjms5pfZiccafJQ8SdMeBdsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANzRKsbO43qI10KnL8wlA_JkKAOZEWnfWNh116TiU13GhD4JswUuF_mczhjUp1tDKNRVExzlGNfelfW3k1aiq2u4l4wo9b0OGP3VCMCLFiZFxzAw3YEngo4kGVn2RyNYSbQB-qfrI26pkKNJ-cfpUISEMwnWXFzPb57zJo7Di2Vx9jcVA6KqO7Z7Vx9eCf6DDlwiN9gmBmpJ_FqpYRjAdlgoLyYmeqc575bep3wWsi8mVC3Q-mx0HUVMKT_6Pjbrac4NZevKSqEoBtLlz9WU7H4DEeH2t_4wWDcmmv6feaGbk6rUk4ps7jwQUcG5-ctEDdf_nRvN2EvLBJgsc7780g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBPKW2Y-TVYDfYOQ82nX2Wku4I0fIx4KGWvxi5dif0QAb79g_aWk4ktzVlI_9HSfTU3Xvwoy3r36KOd_kyMrq3O3p6X7vfA2vbcwIII_Y2-OfAVrvUiB-azZRmRGlFI9Ob6hqZ5ovHenxFyks284610F3c2enQ6eyAQ-DLEmuMsE-lJgoqQA-r6QhORblbOLKvAQcdX1bwE-PZVWPLkkNuWnf043aBil6WTeS_bblUeZfY5Z9pjybSgGmnXBgrrnG7SdHAZDR6fg2R5TosYL1XlxH1NaCBiG6M8jwW81eFI64lEq2UrF-y5lLK_QheVMAsYqNMR-IMv7QVoWN-0-bA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=WBNxEAkkh3XVSDv0Hz0AiGF7Rz0upFy1e_A-83mZcSe4vZ_qYy5JfLlpLx3r0teFXIjeBH-wsZx9XHEAHdliHm3kkASFZ6NGOKyxYtHbvGEV0Ef7V8oEqcy-XdYh2JPzsD1zha0hCBuylgg29ZHpXNvoCs8Lwu5Wo13xGv5A1bji_GRvaEopqCqQNM9e00tuZTYDJEPYSP-XHF_9x1-TUTAbNPo8l1Fpori09FIK3l4YYKcCU0A6UO0sWTGd6vyE6Rnf1nF5uWelLsFcbclgHO3IRbvALs5RXBqCkpgvWGmImLrLj-cUlxHIjXqQ4eyqy-HSbWX24xQB0kAhwNXl3xPix4Lb6U7bOeRsCID1nmpIJrnGmnBERskQ7EbAx-yT8xqI42neBf9L681UOEE7kQcRJcmhAkk4R6kN8IE-uYzNjppcWzeYqSbWq7VH-nuv676eqtJD3vAjMqJPrFXylqWNypJx-ITzFH8Bl9KrP90r9NmSnk-Sk3NQWsjE5dk1dnLQszWj5sOYUiTKHYXvI3YEww6MImaHEmrlfW43Cvbk_ctSZc7ujZhVEND08jHMkV6vcOWREHNNVoEQ05Y8yhwOWb0vlYeIRIU27gnlBJymqY6AmbSBexEiPqwhF5fqDzMdA_MgQPGcq3hUd1J1EB9APGVsQaPtHAezgazknHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=WBNxEAkkh3XVSDv0Hz0AiGF7Rz0upFy1e_A-83mZcSe4vZ_qYy5JfLlpLx3r0teFXIjeBH-wsZx9XHEAHdliHm3kkASFZ6NGOKyxYtHbvGEV0Ef7V8oEqcy-XdYh2JPzsD1zha0hCBuylgg29ZHpXNvoCs8Lwu5Wo13xGv5A1bji_GRvaEopqCqQNM9e00tuZTYDJEPYSP-XHF_9x1-TUTAbNPo8l1Fpori09FIK3l4YYKcCU0A6UO0sWTGd6vyE6Rnf1nF5uWelLsFcbclgHO3IRbvALs5RXBqCkpgvWGmImLrLj-cUlxHIjXqQ4eyqy-HSbWX24xQB0kAhwNXl3xPix4Lb6U7bOeRsCID1nmpIJrnGmnBERskQ7EbAx-yT8xqI42neBf9L681UOEE7kQcRJcmhAkk4R6kN8IE-uYzNjppcWzeYqSbWq7VH-nuv676eqtJD3vAjMqJPrFXylqWNypJx-ITzFH8Bl9KrP90r9NmSnk-Sk3NQWsjE5dk1dnLQszWj5sOYUiTKHYXvI3YEww6MImaHEmrlfW43Cvbk_ctSZc7ujZhVEND08jHMkV6vcOWREHNNVoEQ05Y8yhwOWb0vlYeIRIU27gnlBJymqY6AmbSBexEiPqwhF5fqDzMdA_MgQPGcq3hUd1J1EB9APGVsQaPtHAezgazknHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=XW_aWqP-72CM1fbR1Fk0zGScaQH7YqPQQoqpgfQHgrG2nG4OUQOI9KgKyJ54ixVNBIFzDfMXATZHW-zsJ81NmMiQC526FPnxcWYWpHvMCCXeIyXBzC912aNgF2KyrwMxtEzVYw4cSl1CvNZB9ZTcRZ_bCIHEB3sva-jnGHAg3BZVLJ5OIb6Ky1cuekoprW-_2jShuXxRwVCnRNAjwhcNwZo7gLX-8EU43z42gNTQ-cqsPkVz8lKujNMZkFUfToFnKxFOOeOFKjgll1E-otszxEcezU_vnfJk8d1fScGmCvYihZhre2R7AJXaU7fEyfaluqvcfiXKOlE8bc4pj7Sp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=XW_aWqP-72CM1fbR1Fk0zGScaQH7YqPQQoqpgfQHgrG2nG4OUQOI9KgKyJ54ixVNBIFzDfMXATZHW-zsJ81NmMiQC526FPnxcWYWpHvMCCXeIyXBzC912aNgF2KyrwMxtEzVYw4cSl1CvNZB9ZTcRZ_bCIHEB3sva-jnGHAg3BZVLJ5OIb6Ky1cuekoprW-_2jShuXxRwVCnRNAjwhcNwZo7gLX-8EU43z42gNTQ-cqsPkVz8lKujNMZkFUfToFnKxFOOeOFKjgll1E-otszxEcezU_vnfJk8d1fScGmCvYihZhre2R7AJXaU7fEyfaluqvcfiXKOlE8bc4pj7Sp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsWiBHyilw9TkIetTyGQbIwLDH_KABvW1Eb_TFNU6z2M4bf3oFb3hlR3PBvi1J5wu_-2Bnm6WDqgxpYo0FWUNjmm_MtRuiz3Gjn0-3vzki46glpCwPSXoQCysNMD2PH1qpdPFskWFra9mO0H0UQ5fnrEj2DtbdQAoOwID4b2vY6GwzmTOXjyJl-Iy4_2KPb7_UAtrUnLcIG-bdibLqbUPw4BQ5cKwjFozZRSmCOvjuH0J6ju-Aj637pyrA_x-FsKZzNi1CutwbDwD1FIlT1vY2bVQccRGzNIvfJ3ggMrHnPHXzMjt_Sp-uic07ogm0tqH70j0JFk_V0RbWJatUr4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-82aNkKDH1-dZK0sN8ZUFD96OLoVKL_qMrAYSXAsBkaKWtztf3NH-as-ySx60JTvrb0mz0dgtVNWP-vBktdzyjnVJZ4oI00zUWMVootOsFEmZh1nrKB1n_12GIb67LoLdvCcbjmB3gYdZirc_GgK4TCvKaPDbNZqSUvl7WlXRfRhsWsZ98e3Rfbww_2--ENvqZFhl5gBOqE88YuOcFQvLFOOF1gwN_pwUuE1Z_4CmVNb_Xo924O6YsLvLYZN5BLeTZsyaEhTCfabBrwWwxHkSX8sY9IFmAY-Ll4UqCC2ZGfv3loonx5FydtKA0L_kfXtIggtRQEL0-NzOQf9rLaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=CfqCO8vqokMkJoxmE0Cmx8jes_5axMn9qksTV6mtO_VbXisvReFSbHZEG18UZmLVtltcAp_26rWQAYxhNy68FAQ3tSwYAlR5ilGgCCNFPr6U-UT1-u99LnJH3NM4x3PYY--rUFDaSW2bsbYXXavXa0BkXfKQVDZ-LMOKThgzOPr9wGZ2nDFaWuMPNtA1inub6FFJjSBYYjYnI4gH4dhSoghDuVxDHZIqlrXKer59AMizEaSadGpJiIJ5Qhd9_C--FHJK4npr-EIRSKh2di6qiN-wu7Pyx-WvLLi0r8orlVMOgArIibLfEij_H41tmsu_xsXyYAAAR7DyRGWH3jQxADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=CfqCO8vqokMkJoxmE0Cmx8jes_5axMn9qksTV6mtO_VbXisvReFSbHZEG18UZmLVtltcAp_26rWQAYxhNy68FAQ3tSwYAlR5ilGgCCNFPr6U-UT1-u99LnJH3NM4x3PYY--rUFDaSW2bsbYXXavXa0BkXfKQVDZ-LMOKThgzOPr9wGZ2nDFaWuMPNtA1inub6FFJjSBYYjYnI4gH4dhSoghDuVxDHZIqlrXKer59AMizEaSadGpJiIJ5Qhd9_C--FHJK4npr-EIRSKh2di6qiN-wu7Pyx-WvLLi0r8orlVMOgArIibLfEij_H41tmsu_xsXyYAAAR7DyRGWH3jQxADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy44RGaxm1PvzHqc6bG3jj9Qn7FnV6GcCEd5fu5bWj3n9tpPqKSZfzKcYFR94CWw5DjnpqtS6imqbSOZ7yq9YG4M55LEAOsZoO5QBXDGSDKnDPMGLYN6OYbJ0-ROBczmImeTL8AMPJWI-4IhoboMgLfIkMqywcocn1prCANuDwdk-z8C28avxTpAFdw70SK_hK3sh2bypJNCvZISMprmYdQ1TsW0qGOqnDkPTKb9dpYtE1UA9IsxsMQMlpHZvUWBltqV-X4ONjS7pFi2T9MvNkzbntcFEEQARZw_8nTLpuFLkSWInKXxgryY6zm0THqc07rkWkCehNRV6kHmnZXGIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh-I-Ym2-o4DLq0SuTJNNMbYoorQT3nJvSez8H955Ditsdtk-PtA7Ud5VVI-8VN2-wRPpLW5LND98k2GmcBJiXUj7EHFnthAbTi0a5Z1ufu7pWOLV8cs6i2tYjgKsRHauPSZ4RPqUDY3HDOYZ4A6ri8BPGZKklr5xghTNqmk337_hItZhDp-j6fxKXi62F2fIxyns6U8r2GnJOii2fzQy0sqNX7HuE8xU-msyU4ylKvhGKpETQjSeJjPklBwWp3yIW4-UHaBtq9ylLq0QFp00bRgWMbzIpPBQ_ot7rYzy2OcXMAqQpVtpLeUnSQoGEdD2EMcZ-YgbLV2mk2QZEqngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShPq0cpTCy9gsg76dosjeA7TYHSf0YiUbJvzYCcCbDgdRFp5_Ds-35_ZsXuwOMKZpX4JKHolZDc1DryULU0YzkISIEcRQIpcK7i6blWfikAuRTxQ0c8MPR6IHljisCzuNBlODBhL1EfCLAUdTP24UZDTLLOsUagrxpl7x9zAi1AYG4AeZI7FlmSGByFOGjgwrt1CQN-7dXqGMSeT3GL4OPxk89K3IBIpATh9T0lB2mKHNcuQJrObPscPjA3tLaG1ze25_i3CByT2vKq0kj4BL8TZmDJR_HYSFykRf7Y4_-CVy904k3Muc8f5Y9N0FWZJ9lq8mg8XVaBMPNKFBsfjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5G3Vw1UnhSUPUtg2YSmtCyQW59j-zxbCAmadJwda2Wr54_FHGQd5AoC9X3M1vd-yCyqyoJS48yRtS-UHFniPYosWlM6ZfG6JfZ1VcB9flDzkzeJJ53fN_lkgBlWKw2wc_bCgIV-6QpMk6t0DgcpaEqKayhC1mrcrNzykQqf7nOTt5rHYE4Q3FwzKLRNwekXDIs7sZjYLJExvjvZbom2rgPTz_5pSdnz2bmqDMDM5tASWY2-HNq1m23oonCz8lDUhfsxY1t1uJIKZlcFKcPCRkxvUAtMIzMvoqxnVnu_tk6WDNQVxoWDxZFMjCUj3f9uWSchmn3IJDCMYkiSvwfLig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y70EJPmQpSrOMWEeueCZTUVoiYx9sUzUmFAZNleuOGyoSRu68PbdH9_4PKDSud8-XArtc0msPBjqk7wpsJ8OoBIgWrFB2PiCREJssOy_7J5KnnaGUCl2irftcxhkix2tj471s9BE_LYtSr6Qlh3gnU_iTcesKKdVuk65Djlq4j3YcyeEBMxAp_KytrDVtYbzeYaefZozWjzb0FyEoDvj6G9tzH4349pFobe6fq48XVWxT_n5rAwZqnbgxSulbsGi_DwoxEXp6waY8ZKiicz6kGLbOdu5sUfjiokLA058XXHuGYP8cYDSFdKS2uIplvedimKP0OLAkq1CAbKZnYckGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJRV_luRUL8eu8K1Mw8gzkxa9QfoytESwPZEwaJjTeU8ogp8k5srpBTlvdHoV8545OQFwL4dh820z2LIsoVb9xep07oabLLXjv9iO9Gy70eq7Onz6jliUPgrt_uwuTWO-O2N4V5jNC4QdcdmRoJNtUuyTjUrtVL5FQcVrL9aJnIFC9sBY9kF7vqvGy1AzzsjaNd4_NJDf_76zUSj_Cn3M3XEnsStsCaDC-pdCd_mthpy6V_i789WQJw9sjbH38IwE6K3TB22_BCjbnTYOYVhluzaDomslFHqpkmoZjoTzqTOlyDgQacqWmjX8C9NyS1h14VSeS_rglIm0SuXGPpW72AE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJRV_luRUL8eu8K1Mw8gzkxa9QfoytESwPZEwaJjTeU8ogp8k5srpBTlvdHoV8545OQFwL4dh820z2LIsoVb9xep07oabLLXjv9iO9Gy70eq7Onz6jliUPgrt_uwuTWO-O2N4V5jNC4QdcdmRoJNtUuyTjUrtVL5FQcVrL9aJnIFC9sBY9kF7vqvGy1AzzsjaNd4_NJDf_76zUSj_Cn3M3XEnsStsCaDC-pdCd_mthpy6V_i789WQJw9sjbH38IwE6K3TB22_BCjbnTYOYVhluzaDomslFHqpkmoZjoTzqTOlyDgQacqWmjX8C9NyS1h14VSeS_rglIm0SuXGPpW72AE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf6r9YAISq5z-gzveMeQ4X9GXENEpyhMLpAZ9I7hBuogc-7v1oH6iJN8B7v9lOsNpXsOQTrRkXMaD_Ao-7zleLTH9Yv6gmg5mCONW348hs2QmzEDRuzHaO3buhmBhtoBY4nFsco5RELbFNGMHQPh8JIzDjZcdg-1WNgRd8HgvlIyN5NXBDV7PZL9NiGeff60spbkk170rpQK9xifoWqfH27HVvwQ526LMAzSrvm2Bp-7UAYhJ5OztCs7I2ypaitCJi414MRvst5lOtgCdE5m0lEXIk_gg1pP0zI1adJJslvHzTr09LQJJC9Nm16WSDdBlGdFF_VcweoAfaxKFekNrKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf6r9YAISq5z-gzveMeQ4X9GXENEpyhMLpAZ9I7hBuogc-7v1oH6iJN8B7v9lOsNpXsOQTrRkXMaD_Ao-7zleLTH9Yv6gmg5mCONW348hs2QmzEDRuzHaO3buhmBhtoBY4nFsco5RELbFNGMHQPh8JIzDjZcdg-1WNgRd8HgvlIyN5NXBDV7PZL9NiGeff60spbkk170rpQK9xifoWqfH27HVvwQ526LMAzSrvm2Bp-7UAYhJ5OztCs7I2ypaitCJi414MRvst5lOtgCdE5m0lEXIk_gg1pP0zI1adJJslvHzTr09LQJJC9Nm16WSDdBlGdFF_VcweoAfaxKFekNrKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=JgXwEa6srGFldz-4OWOWxAnPKiTSeZzt8JQVv-b4mbTVc-zv9nnvQ7j6gQenJaahwvckAQ5NWZEQITXL8jUjaGHdoyH2QEPem1HWdHhfUn9RljTnQYlg7J5nc1djfQDsEI2dUG4A_POp5azylnXaIIbtoeXC7O5Bs4yVm_jAnBNLpZScPyzXSVE45ZnjeQf3uyQBwmbBec607LVANsdxkVDcPOPVBFSG9sKvBF5oq_avzpXNk4y9iG76YSPeM2PCLjr0ErSqb-4Kj4xa3W2OTjrxkj40laNuU5a0m9XgPCfJnwwqAax071MARoCBwktMnXfVEdIxjhwJ6DEbYeivoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=JgXwEa6srGFldz-4OWOWxAnPKiTSeZzt8JQVv-b4mbTVc-zv9nnvQ7j6gQenJaahwvckAQ5NWZEQITXL8jUjaGHdoyH2QEPem1HWdHhfUn9RljTnQYlg7J5nc1djfQDsEI2dUG4A_POp5azylnXaIIbtoeXC7O5Bs4yVm_jAnBNLpZScPyzXSVE45ZnjeQf3uyQBwmbBec607LVANsdxkVDcPOPVBFSG9sKvBF5oq_avzpXNk4y9iG76YSPeM2PCLjr0ErSqb-4Kj4xa3W2OTjrxkj40laNuU5a0m9XgPCfJnwwqAax071MARoCBwktMnXfVEdIxjhwJ6DEbYeivoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrl6LIcHretPwx0Sz9K5_i60dlbvA_lPBjDbrS4ijxwHtashwzj9PAy-8ihzohEt3IQfGvuXz6R2I5xO9_BZFOjyi8n6hxbRnMeGu0yDUmsLNuP46K9TQNvNRZPvin3RTwb10anPQa8SSNBfrn4omAxU1AvUIvWqoCUklz29oN23ElXC_cGgJozmZp9ZV7xWM3Z86Jrs_UIMes5lS8k4PQY82YPRevAF_FI-9Jcjn0pZx7oTYLfQinFNkK2KodTTurSpXbh3aiQ4CqTE6pC-f8bfr1RG_WI7WOW3Pz2eiA1no-8JfQ_1la_Hnc6D7gLx0KlUsZdiuZCaIONUaTsVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cCerzKF85xsdEPiEsB5Y8mczqbVg9iGONRtaASbKANo4vU5N5xyifrdS-6-8QGcOTOOfjHIBnsI17yGVqulLlxEFUQiJyL4pUJp0mdcrb573cIuofXIJL0VLtuS_UQIRgv7jwPqM2bEI61GQrN6oiiPFm9kshVLbNPJebHkBYl6YNK8buSiBOx2ebHgwFvJJNKU8mzJphyh2E3CTGjsfIUmfgZrjqOmRuDYkzcAzESZG9rl9-1l2HLkM4kASJ3tC1xduV_VlYO-F8rlVmxR-_-8A1IvzFzQduudkWazUmsBKJ71J901cwY6YSVkHka7oKHi6y2r3zkL0eP26lEXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=bYj26n2xxpQS7fnak-ETO-RVKImMFiUKdXN0hJEZb-goa_quU_p6Akm00KYtAkuYfuTarttQNzT1mg5lIng0qO7lG_Q8AHe0owvwRtFSieZckoKJiACoRjKF_qzDO2uU_2kLokCV4RLUq-VFkFgzXdJxMa4Pp79cZcMy9MaDiUAeBCXxtslpguGy8dkb-kuYdTuSuu7C7ihDu3c-eWhAE6s4t7AU3Pdq6EQwjBNRFv8By4Geum3Ry22mtV0IQn4twn32d8lAPaFGYR6QWZRxlnOG5w4UoAmt1QkFcpXMGcDD4j7tnn5eXt0GK5MQJN-sYxIN53v1AWq85DBXdSyTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=bYj26n2xxpQS7fnak-ETO-RVKImMFiUKdXN0hJEZb-goa_quU_p6Akm00KYtAkuYfuTarttQNzT1mg5lIng0qO7lG_Q8AHe0owvwRtFSieZckoKJiACoRjKF_qzDO2uU_2kLokCV4RLUq-VFkFgzXdJxMa4Pp79cZcMy9MaDiUAeBCXxtslpguGy8dkb-kuYdTuSuu7C7ihDu3c-eWhAE6s4t7AU3Pdq6EQwjBNRFv8By4Geum3Ry22mtV0IQn4twn32d8lAPaFGYR6QWZRxlnOG5w4UoAmt1QkFcpXMGcDD4j7tnn5eXt0GK5MQJN-sYxIN53v1AWq85DBXdSyTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7Z-CkU-4wd7Exw0t9wJlBQ2zkVOtORDs3o-wXvJeTnnoIX4PmXBoZ-WK6p8K-ubV3hirzTuL_2IsrVf4mGqeAD69gLX560fYl0NtIPm3uFOUpCe9xQOlPE9yrRrVke67kb0yRaSv-YHAZC9RG4lGeFVOovX8NdqUuqVqwF1zeTwyMEwcb-mfoIsZHHkrgRR5MmmIKzhJi7m9GA_EnVNVwrixeBmSwpCSh_lYYvBAEZbA46SFWY91oPRXQIXurv9xNXqrK3o7v3auw4inZU_ufw7K5oc6ItjyOd8qd76nb3TLepi14GeVPCKxW2U00OXFZ9YJq4skb9Ihkqim8MWtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgDGDj7zb6HHNe4ASs8drGq750FzT4X2n6z5dCalxGrPew51M96zE5moy8Ut9q0S5zDJ9PbsFutiO-mDQXXCY8JrdlyujcLgSSb018_zHYPGvZNCRDolb7MGbWQzbhTtP2l57NZQZXhLgvns2Y--SoQGaeWAn5cCmm9qRb1G01yuHHYSbZa-aIfEgccX4vzjMd2E-6OFL_04FhJEuLPiBY_LzwhlvHBU3nNy4GBd9QpqrZ92TEHfk3c4wUwJYBoSlX4VtfJYgsRrD8N7C4AQcXtRHfbgnjaXyHGIT0JF42FTTt41QvD7QqdrIn5Jp4zANlEKQURVHbMx5TxLiK6qPg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=vC1J2RahmALBd1N5giEKlxCh6gTRni-UV62mJKS0HIij1jxTZlwZ5zujn38DmFM4DU0UuA5LjldK9063d5YJz8H5qH9hZ9zbpGJRq9cUu5FM26zl56jbVqStG3NJJpvzzuHEEk_c3RU4Lcg44BwAUpA4RQK_TgXxCwx5SmeoVA-KU9u995LSW1O82D_ZIohg7CYouZQwjMWGKcu2-fzi-KvHxVO1MUgYUgRxUGMSP61FPJChilKjf2GALqDIZHv07JQBSlWAwEFSPO_qENbmso7CShiw3Bs9s1Ntj-XTPw6gSre0qCJ8eXZ6b2a3a443ySrtaZ4rGuyO69zr22XgRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=vC1J2RahmALBd1N5giEKlxCh6gTRni-UV62mJKS0HIij1jxTZlwZ5zujn38DmFM4DU0UuA5LjldK9063d5YJz8H5qH9hZ9zbpGJRq9cUu5FM26zl56jbVqStG3NJJpvzzuHEEk_c3RU4Lcg44BwAUpA4RQK_TgXxCwx5SmeoVA-KU9u995LSW1O82D_ZIohg7CYouZQwjMWGKcu2-fzi-KvHxVO1MUgYUgRxUGMSP61FPJChilKjf2GALqDIZHv07JQBSlWAwEFSPO_qENbmso7CShiw3Bs9s1Ntj-XTPw6gSre0qCJ8eXZ6b2a3a443ySrtaZ4rGuyO69zr22XgRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=f6-qfrAgOUWVVkEcToTn_akhN6zZm4fNJQfcXEeoNEw2icvMsgZpfLdz5lFS7w7PdErDv8YMWXcyVoUzfA7ZRElBHcBzmPJ0v6Nzhr_00Z3GUxP2g7bqBdPKnAYrDtInHN3GR4iwHsBEY5A_PICpFuk2KkAFKcoWwhRwuMlNHa8x17TusO69wSj10RnahFIvXPkHQBGaL2gP1LBR2Yu-wKGQBLaszaWBwc3fjOuqfAlUPWQuX3O5Zv9yA6PsGktpHT31LNCRky7gNUc6x9f6gZwlhWUi7gpv5p5qHvKq9C7k2vTeYd5FYkxHFSPOncc1L_SfF8Hd-rme8GLLhnQ0S1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=f6-qfrAgOUWVVkEcToTn_akhN6zZm4fNJQfcXEeoNEw2icvMsgZpfLdz5lFS7w7PdErDv8YMWXcyVoUzfA7ZRElBHcBzmPJ0v6Nzhr_00Z3GUxP2g7bqBdPKnAYrDtInHN3GR4iwHsBEY5A_PICpFuk2KkAFKcoWwhRwuMlNHa8x17TusO69wSj10RnahFIvXPkHQBGaL2gP1LBR2Yu-wKGQBLaszaWBwc3fjOuqfAlUPWQuX3O5Zv9yA6PsGktpHT31LNCRky7gNUc6x9f6gZwlhWUi7gpv5p5qHvKq9C7k2vTeYd5FYkxHFSPOncc1L_SfF8Hd-rme8GLLhnQ0S1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQkp6m3X6c9cjfdHWTv890s7wYC9vUqXQ0unbq7wxnwVYyLKtPfL8rhwMteZkSv8pWV1QXyhxQVjG6aEs15UaMNUZFWfVjCDKjxljz8-3r9DHZ86X3R3jATp-sCMMESrY2_BzWm19ZU-hK3XV0zxc4fl--fo6nN4QSL2tgyQyZHXgPjQjRiu3xVv8aRVDLZOewAZthyiPp1eplDH5peZc4w3lO0veVfQXzgACHhdTbgEjJ2fpIQiTTqK9-LwuId4VWsl8NcUbwav4R082DT7qpOcOevRQoVUjaSLPFrZ0XeCI23OqHFxOsBh70Sd09zS5a4Sp573Ke-FymzTfY0cFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mstaW552BNZBCIkDciP20NvmOMLV-t-dq2Rl6RAHvnwhntB9bVqqpq02gQ4vfDIaZ0Iw_ueDqcwL3DorViXiNyP1JiyaQvPWh5uHo-raDN3KHkIKE-5cVcmtSMzLLNMa7zB2A5noIsudu6XnKs-2l8pj3f2vAX1HWOp_NPuyIcvl7CCbccIdjHdkjzsVHiJBHyUOJvJeL5wUEh69rFe74rQXUOQBZcJ9FCChDrH7izLKPyXzuuIozcArv9G2XP4i23socbsff97kOlIZ6Hh60lKVugp0wsbvCpIYgJTsLt7QVT0pBVX3ogVUz7SNxRnCgoOnwM0TFIeuse5nti5A5g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=gb50wwWNqpHpZcCaX6ZEvhwjohK59MxH0i2b3Wa5ZEw0WLQONCezRpsodzneAaaY5eU9aPZSqxjYTrL9ESboTNwOSN5k50Pmp-WmL27jto64dDmlsSe2QMyFaspXPngAiFfcfDykOdXQ3VCwq_859S5HyoLYkMiIN5hCKyK2G2r8vFGEk2dnELmCaTjnKzNGvv9KajpYuTI2eY12Bka5BI7dADTBC2vJakLn07sBPmSrKqzOMhOX8zulganshX36dw8kOiEdvI-YdT8wIAb-JfCoc-A2gcl2XBqxqvQZGw490kv6j0Ph6Y6ZgKNJ3aOnIpDUXwLVRPdYEGRLGLhASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=gb50wwWNqpHpZcCaX6ZEvhwjohK59MxH0i2b3Wa5ZEw0WLQONCezRpsodzneAaaY5eU9aPZSqxjYTrL9ESboTNwOSN5k50Pmp-WmL27jto64dDmlsSe2QMyFaspXPngAiFfcfDykOdXQ3VCwq_859S5HyoLYkMiIN5hCKyK2G2r8vFGEk2dnELmCaTjnKzNGvv9KajpYuTI2eY12Bka5BI7dADTBC2vJakLn07sBPmSrKqzOMhOX8zulganshX36dw8kOiEdvI-YdT8wIAb-JfCoc-A2gcl2XBqxqvQZGw490kv6j0Ph6Y6ZgKNJ3aOnIpDUXwLVRPdYEGRLGLhASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzMZqpccksH1B1Ze-SUaD7URXSHLIvS54H_pWCoZrDgNxC4bH8EhQG96drgS90Bb5tS7EkvUxVG_J6X5BOSLBMgCU5kWeLhV4ffMybHI1hWiqRfTZIvW-FBCYx2JSx9Z304x5qQZuKnn_BIqvsKSw8pemPBic8kbJFSgSrjO-fNYs-iJ2eWIrrvgkMcW0Qg2mVr0hHaGA_x8CRzqKnSO3XUfJ9gbWLOk7s7wBaTR1M2MkFXZRPiDtc70CmeHRitqFD8EglGHQJfZ8B2ac3kmxVH8-HF1gO0shsusqvwIqqkzqHwdbaxydYbDTLdXGI2IN5ZC8LFCp-DfjAZOfxFJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzNZMfUwkIz8jo8ukJcVOGgXtonLFev-oaK2C2jZNMaOfCNKBpblFdcdSiGRKye1SMGvx2AgBXPOSCHrzE_zxAQsPcvdZp4bB4D3tn9UUeCbN0liytCusgWu4H3ljFVe0hVXFdYYQbYzvaimVjk3afXzVD0aLrhiRAsend-1HNTtfDz_OJp-m-_PsxVvSiw2vRmsYMcVvY-eIpZl3N_MoTg2w821VwBtqhJ4EtX9sCxoHrJw4OFpSloETXWj9P2O0Z96_ITgyK3Ydl9XxyOPkg_RekidbGkXBzZ5GS0mO1CSsBW-GWBjFHYvR2RcBorQKupuskneJiOCUmu_m_wlag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDbM3swnjL16rTFnk_pUVKQsqMWPozOCuMpNkRJroh3-rkj3aMgGfz4ExQKvG9oqqIfMbmxRTnvzTp0ikIzirt9NTwVgnEnpNprvj2RvMjXtIy9yRUtaF-tTOYh6ao47ULFyik_leAKTdyuCp9fzOfmqhUC9quPWpi9lIj1WLdA72CLOlSXg6HNzjknZXu-SRCCBZiSSuYb7hjK0-zU7Kv96Tm6E6B8qLQ36Ba4CdHzxW2FoQts2fla3IOtUFkX_X-dh18DKIiHcXso1V32NlLHnRZi8N7UdPUS81uezye8NeOU-M9c_JDkDU3DX4sb4Lfcwjw-VPpAdr7lWNpa1XA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLUKGXu6RXjR_X7p7nqcNeLnr7qSTSUhgxMRY4__WywcFwWZcdOIGEHrzeryMVBAQW7dbzXEm74FKRGwsgKTSMbbxckEue6WXT2RIm-KbwDepKV10P_7UzkfCd5qajg7O3z2I7Cts6tzA-Hd5s2bhu1GLN6S-95hCyJMIeYS8uECg511bpmXpaC9yLtZg1FJGjDuyPVKuWncFkdty7oL_Rl_10wKzyDjTlUn-eiX5g6g2BkeCbPA9w4rRG08th0gm1qj5mqEzKPsLhCFrNb6aweA-l59XVmKzZIeurNYqIKoGvMwVfA426DsdONkLBMjHRZbouvBymLwvBzvyqCvQuVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLUKGXu6RXjR_X7p7nqcNeLnr7qSTSUhgxMRY4__WywcFwWZcdOIGEHrzeryMVBAQW7dbzXEm74FKRGwsgKTSMbbxckEue6WXT2RIm-KbwDepKV10P_7UzkfCd5qajg7O3z2I7Cts6tzA-Hd5s2bhu1GLN6S-95hCyJMIeYS8uECg511bpmXpaC9yLtZg1FJGjDuyPVKuWncFkdty7oL_Rl_10wKzyDjTlUn-eiX5g6g2BkeCbPA9w4rRG08th0gm1qj5mqEzKPsLhCFrNb6aweA-l59XVmKzZIeurNYqIKoGvMwVfA426DsdONkLBMjHRZbouvBymLwvBzvyqCvQuVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOB-TBr2Rfu2pBXpNoyysHwWGNk92HZmCuKmYuy31iyMbDFKm2WPCW91nC_VuW4n4zEvGNIJfS50gwP3kgKZQbvTmtHS6ZDFcnZauWZlJnf8iB41ohc-gVgB82TaMIraN3pcl-eJlXmI6WZLJatlAsvDG3MGqD1jq6Uf4_dBnVqXjsHDNwYziIQRQwXIauaDBFcKkQCgQgB7pSr1t5wurXbovCCbHbMgHHuOhRT87qrooIC66xB9xLvPufop5lvml_ZfdwZe7N4ZAGh3uENbTA3t2VJkoVON54i7y4iDi3J8d3oRF9eZYJSWbab1EJqwFJXfBQyg6pjqH3TodzYxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQvLKr9jvZ467d2yETKHrFUSoCXB49vlW8bQhK1krk8GIHsMLgsY93KNN5mszhEFYpgryuvt8H5oR_NerllGeKflYsEnBj1Cblp1Z2G5161VxrqbyuTGOS1nRVZkt_zpgIM4srRPsqFyKlkjxGQnTvaKGcwwXj61Q_U1WKDcMfQo0mDo7iThDiPk6oLIH9FcJAKViwUyGj_knpKGmWXlB0kh0DOhA1dnZZZm1AeMzb8VJlWyyRgDAhm99wc1d3K2R26HQR1ttoBXi9_KqZQn46lYmE4SYB7Px7euoJ5cD4Xqrj4p2EfmV3bObCYb6VfJYlZzbiOWnKO1rkHwpr18UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=mA_qkVdNUNpCt7UeGMPMFA3-qQ9SqyU4Zjm9dsPTyxcOQ3uLZ9Z8t6AXy0lZ0FyzvNCBmueUKzuGnB1cBpsAhQuEMVErnYTcwsbgla-3v4pVaiAD7mxs-FTtle4ki56aYluPj6Voez7xI2X2wVlpIstGfSnuX9O9l6AQ22Cyr2gfH53NSCLXBm1nvNQ8_G4BVeCnbMKo3MeYaHKmWLZAI4jkpF5Bfh--xVg2kW8xcLb42eh_rCkWyZHFFRo7j6g_9i_INQ60cWEg28CWqBOLGbCOYNt6FY4CKxIMhLwCH1phc7y0oPV_ztzOZ1RtVqNEjXKYDLris0X99V3slknTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=mA_qkVdNUNpCt7UeGMPMFA3-qQ9SqyU4Zjm9dsPTyxcOQ3uLZ9Z8t6AXy0lZ0FyzvNCBmueUKzuGnB1cBpsAhQuEMVErnYTcwsbgla-3v4pVaiAD7mxs-FTtle4ki56aYluPj6Voez7xI2X2wVlpIstGfSnuX9O9l6AQ22Cyr2gfH53NSCLXBm1nvNQ8_G4BVeCnbMKo3MeYaHKmWLZAI4jkpF5Bfh--xVg2kW8xcLb42eh_rCkWyZHFFRo7j6g_9i_INQ60cWEg28CWqBOLGbCOYNt6FY4CKxIMhLwCH1phc7y0oPV_ztzOZ1RtVqNEjXKYDLris0X99V3slknTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=nhzuKM03aTLJl4AY6_9ZKZYKhViDRQ5n2vk7hQBqkiMkjAmTKGvUly_-KRl8tHDIJvcuJO2HpabV3Xrt32GyX8yqzitxXU_53CptSdvjp_rJOl588qIWBo4CT4FQdQ-54tmLPswzh9cfo1zjp3ZfW2e5Nc4bD2y4Tazfb0aLEPPmMCFDamLh_CTDFAw3kLMbAFQi0rxK07Blt2mIQYlBtqMDBu3MNvQrz0n4m89CldG2rGc9GUGcyB3d-z0gBRzqe6c1wJSwFmbqKN2xYF2cJv0z5IvORTLUMCaKQITtXYBjBsXlpQK-0YYxKBjDRzNM8UThsjj1tjyUhs_u0eBxUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=nhzuKM03aTLJl4AY6_9ZKZYKhViDRQ5n2vk7hQBqkiMkjAmTKGvUly_-KRl8tHDIJvcuJO2HpabV3Xrt32GyX8yqzitxXU_53CptSdvjp_rJOl588qIWBo4CT4FQdQ-54tmLPswzh9cfo1zjp3ZfW2e5Nc4bD2y4Tazfb0aLEPPmMCFDamLh_CTDFAw3kLMbAFQi0rxK07Blt2mIQYlBtqMDBu3MNvQrz0n4m89CldG2rGc9GUGcyB3d-z0gBRzqe6c1wJSwFmbqKN2xYF2cJv0z5IvORTLUMCaKQITtXYBjBsXlpQK-0YYxKBjDRzNM8UThsjj1tjyUhs_u0eBxUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0xJmdSY3WNnx9kNC4cYjt752HK5bnm4uz5wLbGE35K680g4bke36rSEa_ieuRQ0V3ZwTMfxPZu92PTvulP91vKAmsckHH_V0FRRE7bc3Nh2lXfAQu_OukAunHKyedA5UfPR8nwcyWnNYW2aotxBIQSDBKK2fSjl8SUYl1Y50Elbr8nAbS5vwUDtBleDcjfy8Fx0FGRqxz0n_6c1Ga16T89kYglm0Np5EdPEYVl5x3CBb3wXnKOv-LYPR0og2wv3VXezDh0jfX-_FdzuhK_ySJA-BqbGv88iQSA7ZIY0imQa0cdKDl1F703K6ZU-XgggPXcqskDyMg7I62Zt5wyuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKwh1hle07dHbkqncbbWNpk60xJ4ae5dnGoDOxLHwpj0TlR5cmcEF-nUY4_5zLdyXoz4HGdvoTfTaeYNwTs8WQaqy-BVxi6TzqTpL4AbQlOKpXY01JLdsdmgc9yANQArN1KHS7d9iA7xhFvyIoDBnDwtuqMnKeuA49bZ3zVEq2jOst_RkL2ek-c61mg13JPE-VVILTTmWAkRUGpiA1N2yf_O_8_rNDdiDoYUIz88OjMNjidparFR5r51T37OoU7rZ3vd50GIPdRTBUpEt4X4KnAhdVJ7QTwtuQJFqu1x11fcIjE0mNjV0Al1oUWs90LFBmJxZuPpjCPO57YozmtArQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=kBBKtICl9DN2s-P1WcMiuxAi7ALwaPEbcwJ-GKgojR-kgcTtulGVXJi_DqHNVzSK6Ib8cIzTZvpIrwcT7bULDcWcO_9QNiFMFcYnMaC1QoEDMLJwnnkrvrAZcZlIZsG1H5S2ZkWN3qcny8sDKMfWxYjRohZKLT1fa7Yt87BOE401DRgffGKJNZKahMsN7hzuTRf2--19ewg0zlsmD8yG40nbg9I9_AfGo1CQJnhI_fFqbumf694bzg15jdlSCBBlULx8L7kjH7CQsI0RF7K0zBqI9iRmpqWW5Xx1JfbAliCG5oaiQOO7n8vNQ2P_4yCNG_kTaRPSv1_AGJKoCt8Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=kBBKtICl9DN2s-P1WcMiuxAi7ALwaPEbcwJ-GKgojR-kgcTtulGVXJi_DqHNVzSK6Ib8cIzTZvpIrwcT7bULDcWcO_9QNiFMFcYnMaC1QoEDMLJwnnkrvrAZcZlIZsG1H5S2ZkWN3qcny8sDKMfWxYjRohZKLT1fa7Yt87BOE401DRgffGKJNZKahMsN7hzuTRf2--19ewg0zlsmD8yG40nbg9I9_AfGo1CQJnhI_fFqbumf694bzg15jdlSCBBlULx8L7kjH7CQsI0RF7K0zBqI9iRmpqWW5Xx1JfbAliCG5oaiQOO7n8vNQ2P_4yCNG_kTaRPSv1_AGJKoCt8Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=PjBHKsimELDtvePqaQJV_10hBxPhoqRpVt-pIcnnemmvjE6IgS8ynx_gQ6mE2jYrqZ4-9oDVUA4gYj3WfG3gT9gaRcHDdaiI2CvO86ZbJwRNQaCegMSMSux9h2aL3zeJWp-tDiFkMbpZHZdQZP9pqofbRC6SqYT1I2iACsNwUxf-fcW1mifPCtcg6i1Ljhr1qjqhmewULZ0AySEsgamICZ33lJxH7FyObpJlUMZpX76XBoeqgedf4A0pGgsnMW1elrZdSLwl4G_DeHzJ0lHjAkWCTecV6cez3p5ewL4Qao_jGZARj88mec86iniTP0Zfk90i9gTCZg97989u4JkFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=PjBHKsimELDtvePqaQJV_10hBxPhoqRpVt-pIcnnemmvjE6IgS8ynx_gQ6mE2jYrqZ4-9oDVUA4gYj3WfG3gT9gaRcHDdaiI2CvO86ZbJwRNQaCegMSMSux9h2aL3zeJWp-tDiFkMbpZHZdQZP9pqofbRC6SqYT1I2iACsNwUxf-fcW1mifPCtcg6i1Ljhr1qjqhmewULZ0AySEsgamICZ33lJxH7FyObpJlUMZpX76XBoeqgedf4A0pGgsnMW1elrZdSLwl4G_DeHzJ0lHjAkWCTecV6cez3p5ewL4Qao_jGZARj88mec86iniTP0Zfk90i9gTCZg97989u4JkFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe-Hoqh3jR0ktDGS2ztJYg5P0f7fCnVJqiq6udu6R84NAf5j4VLOMBKEOmHuDEhH27UX44SRl-29U9v_6WAVsJKVXWORZdVgVgsLdmaf1LWnwWJ1KS483G-mKHw9mXQSQ2TBCPUYBedzVA4doNOgkvySRcTaAJmz1V1YLYSOmLn_qjM07b75OVJ434MPU4qT9idwm065himhuqz9vGn5fjJVpXdWKcumnVAUfIEOEdgxTwtHE_l2_mTurTVEiuyRnC_3WfTvql40QAeI-uqGMJm4SnuhTpcKCjT7szbpGDP_iTJ1spXrVStZ1AtjWePamUMdCrlt97uig7Nx3G9LOA.jpg" alt="photo" loading="lazy"/></div>
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
