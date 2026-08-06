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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 13:59:38</div>
<hr>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2SgKn4EnNs6qzviU80TCo9WFcTQFjEu_EReNTw24Zdl13i3skjsQK5m2p2k40jOI5aCoLRn2XBSshIKOKjXla-ZDxl1KycLOHUAmoIzEljKdqR7IrkRiCeVwT_9Z9bEeNlectpAm4R3uIbu5iBi_SwHkouHi3x6OII4koxes07nbV_FneL3hTsvFyy_hAciLzqtVHhorZqHP_2afJRZchgveexLZBi8KAjUzyUUh8fkKwvnufhomjQjiW9l9jtKskFGMjA7v1LNSxGGsOv6ISYdnFVDJbDWkkj6lz6U9zZUKBVZvhCm5c7-UtBLRF9hyMPJWAaQHmxB8dnanyd11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtvY7pvASyoNzE1MgzbmI19FAUjQSKLVX8nP1mr0oTry5Kco_dGNHIQ9lAHysx--cf0Z7hZQSy55Vg8Bgz-QvFTNoUyQeLDjQ8P02-Ezl5HLd1wFmqqIU_bAy3nN5pNfF1nfEzGD5pexnsHeZUlbHlwLvpsgFG3hZM5kUEESUUUQA_lNis7IPYPF1SS7BD3UvdFDmxDU3raBS55ep2ntzcFhEBxD8jdZX_f3mwq1QFKbRObBZF_RWkhZLuqLERybPOSpyBy3vUrU7C1FMffld7xaCTB2f3TL_qaJWlYieYDODkb84q25478JeTGCvAspVqpdIXQEvfk0NNyMU3-Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=QMFT3BBrF9lkX1bC_SLgfuiVnq7zym8mxaBIskSTIIzpCA7YnWqi9DbPz8Z0Cwdipb-HSaIlAKkV0vTsbAghZGzSjvAyiMCzJZ8VdxCB211U2xkUIQrriGKlWlKv4IRHWHHvzEbBxelcTOIs3je-bL7A7_KLC2etMFRKgaEV66MQTMOAZl1rJWMW-guFOC62xz2CsC1PL7nD--ReQGEoYPGjYH-c4SHRy08PFHgX6e_82o4oZOl2jaMfYKShlxyZ9gmDh-Bt34qEm7JK3RVPIXtNw0A5jja1A3Y6YmbNSTs784kbDSkVRV43f7SB4hr9OA5qBaNG0TpvNSN2nZfpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=QMFT3BBrF9lkX1bC_SLgfuiVnq7zym8mxaBIskSTIIzpCA7YnWqi9DbPz8Z0Cwdipb-HSaIlAKkV0vTsbAghZGzSjvAyiMCzJZ8VdxCB211U2xkUIQrriGKlWlKv4IRHWHHvzEbBxelcTOIs3je-bL7A7_KLC2etMFRKgaEV66MQTMOAZl1rJWMW-guFOC62xz2CsC1PL7nD--ReQGEoYPGjYH-c4SHRy08PFHgX6e_82o4oZOl2jaMfYKShlxyZ9gmDh-Bt34qEm7JK3RVPIXtNw0A5jja1A3Y6YmbNSTs784kbDSkVRV43f7SB4hr9OA5qBaNG0TpvNSN2nZfpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_0-ptsJ4efHkAQo6huPuY_EM4QKUmw1vw7Fw2yb62dglPo2dDtFjm13hBcPVJAYPoD7IXEcdAK3YJ4IoHY1IcG1oY00nzsuQPf3WsFcks194zbKE9VNKMT3gxQzCG3qFkR4ya953IR8ekNef8XFXWsflG52MVqq-Pfwg24Pf-SokaCr6QI0O7kY0_gTyDIeIGrbkgbPVbeW3WALodJhZXGJYsSl2KaJhSLWbLPHWO9JUWQD2QdCAyPo-vAn-LsqVDG9AA_RN7iVdVmu_rtZxSH40UFFDAXQh9545lW37HDkYmQq1bSSN1JeHd8Lbg_pghpsu5eYS4FMh19R7wiWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=IpRhCsMC4c3wKwKUnXR_ZhJjS276aUs5zeyt8wuY25CENPWkGNns_A6symthQLnmH0_MTEZZ3psGxiwWTqCHRjOPCgpP8iztlI9juVLHKQCBSTmWncqHXAuY0uq5X--kU23_B0OH5uCzvM_EsAObLORsGOIe1Lt_k53IEbKItrEmIKYjkgV621PYgcJMARLL4u8Fmqfux5MEme_27nQqcaFuXC5uVWLBRQ0grNlqke6J9hs4LTo8k6DTnyVej4vif10_k1k6Md4RxqMwoHQB_sMCUr_aK0DOnn7KBMi1teFJ608Mjsg5-ROFV8Uv2ZNGH-BpnwAUot9F67bvc0Uuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=IpRhCsMC4c3wKwKUnXR_ZhJjS276aUs5zeyt8wuY25CENPWkGNns_A6symthQLnmH0_MTEZZ3psGxiwWTqCHRjOPCgpP8iztlI9juVLHKQCBSTmWncqHXAuY0uq5X--kU23_B0OH5uCzvM_EsAObLORsGOIe1Lt_k53IEbKItrEmIKYjkgV621PYgcJMARLL4u8Fmqfux5MEme_27nQqcaFuXC5uVWLBRQ0grNlqke6J9hs4LTo8k6DTnyVej4vif10_k1k6Md4RxqMwoHQB_sMCUr_aK0DOnn7KBMi1teFJ608Mjsg5-ROFV8Uv2ZNGH-BpnwAUot9F67bvc0Uuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=kB4dfD8yCQkF2RCyzHJajeGGeaspPfsUf_llYjsY86XucisTnlfMuDsZMTV3moHnsbf2XzkPZFme-2e3UN9WZian8wJaHUnUIvr3AKK2kfqQeuynB2GtDEwgXiKk_tjk6yUWO1yI_ydc6hFuMeGuicIBRtVKvTuE8sbWfG-ttJjxhhSYdrvtO9Da5l0dUeRONirQdWgjNt6dD9xjjG1rKYer-P7Pr-ngqR2D9VlvpxZnIWVzf4mMtIrfsk7uYQKcQc7JO0jwmwUc-8KUXI4SIb-RrxRo81vYMgXgJX5beWNoCSGZughwNGlESe8ENXlRoT8rihkPvU8CEUETNXH3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq28r_HDUU1tnm9TOJhXRfT45L-e0SZKLHhy-2nnSN8g3xv9KhOCBVwJEDrrVHGZgzkzUrSqs8Q-gOP6VPATGJ3SITWBXE7wYPIQxz8tGvVvUCcOWqF5g0iOJTvhyvLoEXMuYBJBC2RJSpY22_fJCk7UJoIg2OQGGG_Im63v308KEA7lD356BMlEc3Ydmen2PK_UcS3leUoTYPq7yKAVPFk3zCSPMNzD5MhUmPvXTzzlXH4jQylt2tTmnjzuFwqA2CHzOH9kewT0DHxegQozurckCeKaj4nChQzR4wnValAvt7jGwi0lyt1Jqf2fPw8V2vRdxvwY7EKh87WYqGmonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlTaQd3YujCdMsAAdnOqUNnvnssX4hU42AsnMrjE4_DwyJRxnUyJxbfLkFCYaVebEa-89wweq3UcBMrotRbMGOx4w4ay8A4riqB38YIf5KuxbIZfreXxvO24ZongRCNK7rnmHkzqsUU8vubq_Q6Ilub5DMOZHfEUjClf0k62khXkNcV7R19s3s29pmDMedamUnOh2ngg6zmZBYOF-A_oDrI1LLeL05lk9Q6KCINFrNcmuMOMYX_1dFmKESkmMT8b1xAqSVN3ZAL5ypZeeIaaoeYVDcQTet-Vbwj6eFlwlu6Ai522R3g9GOmLrjFsmKBmyXAQn-g_xkv022RURZOlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLNahGyWF7UcqcnDLCu9HNZYRFPxkLpGNItCZ1wry48AvlHqDYmOTyUydgP6068YgC-m5YGJtchqhJvF4SkuR5EQJxgHo-pauQ3b7WDOiN9rqUgrVDrxmtHwomLnfpVMFrG0M4BmGbmls1IAQfp4cRPvftqlbFi50MZ21xJwLycvQZaD0MWEoSTY_re88Jul4hLRFnsiKO9pHshlphcU0LRmt8RoFIdj43MIi6Tk-aWpx-u1b_WrAhkJPyp2mLBFIO2DGRh0053WEzqyRJWSioHu4CRhWjKM4ASkjEf_9Y5I883BeAzuOBGk6Xtly-3RuYvC3lAYeu-uxqrJWcrJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=V8KeysVryVPZCisIu-J-nUo-EXE_6C0vqHwZ3pavEhfklxtodFPyBI0ve8YtFHiQL2o8cTVWVywoJkUtnYUi71jlMmyl9sXpzDhQ-NsiCjoCh5qUIzjA6-V3yVRrIM4D7UQ1IcO4a0hJMDcuJQrrm_r-GFGM92jUrhiK_T9CAztiu18cP7413Z6Lt8a5qeIXrX4zTMnmD48MxlJUooz1UpJuYG2m61dkNfgcgOYgNXpWRlia231L1TMXj_v2FgCdxd7dGfHiD3CjDrVJI_9dg8mcoGXlH5K2aKIsvnQcI8P1c5zGxD6ubn-HD2JjX4HbLbTKpjSQZd9vyCsu44NxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=V8KeysVryVPZCisIu-J-nUo-EXE_6C0vqHwZ3pavEhfklxtodFPyBI0ve8YtFHiQL2o8cTVWVywoJkUtnYUi71jlMmyl9sXpzDhQ-NsiCjoCh5qUIzjA6-V3yVRrIM4D7UQ1IcO4a0hJMDcuJQrrm_r-GFGM92jUrhiK_T9CAztiu18cP7413Z6Lt8a5qeIXrX4zTMnmD48MxlJUooz1UpJuYG2m61dkNfgcgOYgNXpWRlia231L1TMXj_v2FgCdxd7dGfHiD3CjDrVJI_9dg8mcoGXlH5K2aKIsvnQcI8P1c5zGxD6ubn-HD2JjX4HbLbTKpjSQZd9vyCsu44NxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=dqeGy92s810jBbo5Y2MHQcoY8sUu5tKYOR_fvFpkrkcPdIjZnYhz-rR4Zk2JyKFkSTaXnDn8iuGwWLyXgPIWFdYzfpOVKYODU4pdXYygSgSg3sqSONbkIu2FltDJMatWOM_dL4_8q-1c7RIH2oZqspyyq4kH6Njb9sSjt2Mqg5L43FlAnv-OdHSsZobp1Gw7atBUlVSI7ZFjBbKL8Il9dNzcQkvRC6Ot1DXL68M4Znq4eR2P-BL98i0qIWE9sPjVDkZCx5xklTPQl991Tl39-FICv17jsiY67dCXkufRYzv7esTqPhiy1daYrpHFfKFhS5EIIGsd92QbF9aAOL0zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxcbJIctp1pqBy-vIPYMTXfkOLYCdVVDm8-Uvvwr3MTwml3DFKTfdgV9GGgBOPB_D4q3cVWSL55CN49zFU1oQ9MxtTcRHkDi2xHyuv18yIIE69cJeHy4xu0t5iPQb-BsTFskwTPK0SYkHHPEGC_tTASLAC2vZRt6yO0MLPYflJKVjiqovmNG53LDhCvxQZCxqS-F8tAUL-XojFOAk12q7V7FX1QhreXYI2tt1hc6ZdizKxO1JWCML9tNcek48j9MeaUBk5g9xuK-FNTbso5aNppDeOa9kMvYYzQapRYKqDGwmNTC8x_McUB8lrZDgQ6ld_jkMwgiFqws14KX0NXBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebLmprlv5B29-ycbENvbpkaPG3Wy5RTVgBVw6zIKGeGOq5VMbsa0rybXDqbuAz17D3gphJq-iz3-wDCbjIGq9pr0om0C-T_6IJhpwhFgGOJTXXitbWzZvWnMzD6RegLLwYNHKnebt5dBSgB_BgcAjQg8rRCnUkc-tcbGmhYS8noqpLUR8-be1Jo4idENs5P7_ebtqx7VzLR4aJRQXqkyqfl2R5vfTY3wIOefgtwqL-Tkn1jCYs0QSECMzCFGCXHRkbyWM2L85T1qz1sHzfi8TYWXOCBjZqnaum18pWFg39CBF0mdjBk6bW8Fd8DpTgtsvDQZqGJ82ffEr0oj5AFAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvtSvsV1bcM7QDFgdQMfXNB90H8Uw2AIoDqxs-2vOLWIh2-Mn54CpzsfOpp9bMHORlPY9EwN0TcByvoZC7M7yIp07kS37by5HpraL7YV5ifPUeTkVGSJEbZAmSIjbMeXWnBCkI0GHp2Y2OCZNfUOGZAd77Dtbd3P-dJzAUI9C-zMbwgaAJDs63HtrrKnAxfzvTAJIki4pH4kZ75CRx5pULvXrJuMJyR1aZLcBCwqKPB4xvI-bWZw8RSo2q2YuSvieJF6PS5ilZuTUOOmFlh_RJ4ZUoo34EjNkiRDBg8hMBJzBXtSMdyujdLP3m7vu8x2s-gkWE5u4I1dfHfXUqYEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecwIk7MdzeiOmAtI3huYKz8IBgEYx1uQrgOMebq433RwZpR89mvbqNk4SDCjP4dIJkFKg6YbT6QsdwxIKLnWYwdRrqWkfqCxw_wHrK1YGMraPfZtbNGnBMlgXqR2q3mMAsAUjgsJhpzoiqiSNAa05EbO5bl8ursccFNj0K6i_JOenLAL4ZBs9FXiIOvtSDJR2hUIWe7fTrYIJ9gtZVzc0LQX7yIPoU8jgWA13FljTCXe-GsakB4X1br6ccXijxUWd7yOaFlnB_k3ZAFT0_fRq0pmjtR-w5NeMkF10l2XU3HiznS3-5z9FnqaUeqtM5EEcauQmF4ZbJUEaFTo8aXarA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_2nK03BpL2gwgAxOVGNkCbIzY3OPAf2pvcoYznQda3pbxZmcxjIDfeK-StyFg4dCektMLgGgepX79uWQx3ZP4KD_4Q5eEBrkUX2Qnx4B45oxlpDkOiFQoau4nJLGXmpg0EW6W_4muLcxo2cprmXOBZ1Zr7mhD4cTunUjnRZx04UulbJqgjY0oPXS_6t6hEVKW6ZCPsVM0UsRFA-IDPlS-KAZeeo_iqk2TYHicAaF7Y1R3q0OPbWsbUoN57q-6VJTO25IVB6Ou543yNUM3sT6RiYfLNP3eL55gYJrfGYvtmAjn5_OYeClLvHgmbEaJaOxBM6vrrQjqr5zy0lMB-UQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSlT7TONnKHJjadOilJ4L1tdUuZJ9ZgdBZ0RzAdM8pbCHSBkizKX9ZGPLLiWkOOVi-FaDqdowVpJS5vMleE0bnFR2rPUkgJMGb-Ebq911ZXFUI-26nh3CydpZ9IEJMIQn2cLUjCdnVK5Q_z6mHE0anl25NsF6Pyo0AUww8a74euqyxZOB9etkj-IEKsVcPEN0_kUYw7Xa_LewcDQHVtvDo0oLhuBHN0Gm_FbUc1jqQN7UV-tVlXOWXauxg2-PIU4G2aC4NtYy5zEHAEXqViVfNBUJ5ILAVTn1l0ftHhZIunml2OoK_UCkikvn7SSimc8p2pbHapAS_K-1Xzcyg3oGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4m7rr9sewVnYHS6Jbs1RR5In2j3gnVSeKrwgknvjKt8epHULjndmOuGi5wVBxPRIKKILbEUxtZ7S6oNB94X05WzXc9pSUceOJG84d7cCkynwaGUKYPFuOwYj4f5ZgDuRKjwKGpmEG5gJ7B4Wt0QG0up27rrhVGr4K9dpnwmmAq20j1NbqYf8IEV8uJOPUHNeyAGZEnwvjeNIlKUaeMXadghHvK_SKna5h_ub7SOrUo5EvpLyYF3FyjzZY9auORssDCoskT0KmHfz2G0lE_bjIXC-CpKBxSpILvK6tFIJT37_4omWdSdUPCuI6p0vQWL4ijZ9BQp0R-4NXfa_l5oKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_oQ4mmQNfU5zm-263yLCwK86dZ9qngEuOah0zBUp02EzzaQbmzWvCQmTKAR5oEDvuTyIUloNSIAsDl7Y7AYeYhUtHJUH1_gSKLZB9wDEPhi-b6bHpL91Ivxci51vWTIyYsRr1XWQ4mSa8sAEfr_VssQ09gULUQBF66x4IQWx9kkTqLtP6w-4xYDNYZN5hSQnNM8-YnpuI62MNetx9WcN6P-N9yk1YQlKta_Cp94YNv-_vsF6r0YFmc1VbzNK_qezzErA94HKwCYNaMFTB4WzTXS1-ZF96yJ45iUX8RVORdODP9Y9PsdDdtbTxjyWQ84HSEecmKP_cUlKqp6bg6enA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWDAdmIhlXvFJi_EJfclT2XdzMhllkyHMyTMnTd5hzQY0ZxFzY7dLN5lIpZNOP8tKd9r4ACl1bmksyxE24tc3s88D4ryjR1wA-4AQ-_okrT2ToOQC7z5fdUk2BtSht-XBtHgVDHc2493hr30msbFuTmuBquHM35rg8di-LGk8WMVVNMC9sFPp8E5HWN3F-hfJ5MrHUZw1QIK0HvhZntOYnqTuYZE12igPuxuRctXzDMA_wGulPXyid-EsJuDinuUo61VpXxV0M1pfVNa9AnW6sEVsMF-4ZU7O7X3Kkn6MDKGVhul10KkHWvJXyiCbEkc9IfF65c-HEbnFmAanDkbJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMc7fLVZF-7YQW7eYj7eSXnsXec68XNHzGPjL6-RO1viiwKjoYUEw3Y8seVV0-oEJDSLj-6E3qDodTOYSwU4KqSVonfmb7aw9uf2gZyQd5hFC6Lx8uZP_WgBNlMt2WpuXf_MrNdbqci6OdajFAfM3d3sJZvUuTaZWqsTKVMvr5ZiSSqrZ6UR4k1su0DxFFogFf8qYlcQEsQCOMXQr5pssmHE1fau3Q8QPUgj7j0Z7NtJYFm4wTcXvkXT2RvSHZYfWPMLt2jzwr4qwMCO9kq3-utkFZXN9SeIV5kcKmqsud4Pg1cfY4GQUhc7TxHzVMA8gHRn1zjuq_ogmDsRfldZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnTuf84ZGIr_FKV-mxQiob9oWi2xWfY65u0NZLdlKzjdouVdWGc5Hsqxs4wTGenBoCWJ0RSXP0Pq5B5ZINGZJVMLP4nq9ncW_R4C7YXHB1tJNTmEz-7V95Nza2383xVseyHRx2IYv11K_GCieUjBw6VCKT1nyAwExAknFgtXDAs0acIz5aRsOlMQ3-DJE84APRD2stl1XKzZ7x9vfjdigmjEcnm2ZqCpc2nOV91q957AJ_X3NiUk1q1Vfxmk24YGe-mDMS4FJGVRpAOG1jOMgk3oUwJK1Ohk650HWl8XzR0gmwhZJ5aPi8CEkRD65Lwd_RoNYBTXsN4cXmAPTzYc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEM0FUx62CjU4E504ICrsUhXU6wgBwBlsgq_jMWAwgU1rFBW5zDypBuS6Tgj5Mg2Q9K3hq7RBbzJ0twmzaiDwKKoXUDlz7EDnMke1MW5q_6xgUROcbEw8p6f4PcozyogeZQRHnlwjWFHjLgUG2k1mrw2u2igAi0dxM2S02a2H_j4i42N4kIUNWXEj6lv0ycY-RlNWQOqKW19J1JIoX4QT5Wgp6Hix5KwIAY8H-hXOmWE_AbTLeWmojPCJWcDRz3axBv7eC9iUtexcCJG2uLWP1wc_YiVrgTlDZhJQGlvrl0TTQdrq8WZj_j8XMEA65f2IVTmnr9Llp5qeH2egrkOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnksn1QFcvWOkdjMxFlFsgL3kzEc3F6IPMafbPdB55Py_YeA53g57prILat3XJgx_mgkZ9vVHJkP0rN5aAclgwxsdzkvcCeHtmwYCswoYzIL7R_BhSYpgc2NC2EWh3bwXf84VoThI0N8K2IYNt8x0qSEr4yS44zuPCttSQvUS7vOZaPE4tK8vvAmckvreBeJdbFqWGKv6jNJcdSrGteMMq9qBLBVWfO5DR7z0263WPjfFSiCYbSqrMyVS2qZuEDzG8Ftyp4gmKykCR6d1vDFITxnCN58Rya1tjCoV_UdCaiOVdx8J8We_AD9JeM9RmHkpMYI1LF59WMNbE69gfBOug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATX8oQ4SEbw6vKyG71CtbJmgUWtnKA5daEiBGhDqkKmAXWC59G7xXq2INiu6-QJlNus5bhmBgl9njI13dnvEg4lihSt4g8qbloeiye_Uw-MujL7a67nIOiKMnatbdVqY5jJnB4Gk8Or_Ph2E2oapNfa9_yiN8aurva3HoTW2mRGm_n-YUTBLR9Knr94FxQ4EHFd3Sh1ozscolpsokqeoETl3fEHGnwFGpPilK-5KsCleAdNmPRMJAvTP7QH-Gaj_HSQP4r90dNtfmir7As1EQiL1AcPEIPFP4FQwmn20aX1MheI5xXgDEQHsVuGmuxyLUQS3LhxgwS7SHmgpDGwuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=VhI3J89yB8tI07ZdQGHT8QMU1B0hqHRHWVn7tL_qNGUMTaf1_Mc0Aqr6COH7vplOqbb7n-pLyZDNnlTMjtriCRSyYyMWzaVHr05SnreP3hHs4IkGaEnjL5OiVVRX1kbaRm-p6iS0cUbBYzPFJuh9Z6r1Iv9MoyjxedPH9SHX0BZplcfvmZQCHcxl3IRYQV4ZmAMw1SuicH_VBp_GgFkEpxwomjtF6klL3PlNohcOWCBkJvk-9hs31i-H_wPpduVAHFtMKl3R-AM-ZdGz1SvvPyEVLXlWmL2vKdyfe_mYrqF9ipQ0nF191ve-Z-pV5zcwJMwAhN4-YGxreNZIJOZong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=VhI3J89yB8tI07ZdQGHT8QMU1B0hqHRHWVn7tL_qNGUMTaf1_Mc0Aqr6COH7vplOqbb7n-pLyZDNnlTMjtriCRSyYyMWzaVHr05SnreP3hHs4IkGaEnjL5OiVVRX1kbaRm-p6iS0cUbBYzPFJuh9Z6r1Iv9MoyjxedPH9SHX0BZplcfvmZQCHcxl3IRYQV4ZmAMw1SuicH_VBp_GgFkEpxwomjtF6klL3PlNohcOWCBkJvk-9hs31i-H_wPpduVAHFtMKl3R-AM-ZdGz1SvvPyEVLXlWmL2vKdyfe_mYrqF9ipQ0nF191ve-Z-pV5zcwJMwAhN4-YGxreNZIJOZong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAmjsz53KKjlbojRDXnNyoV0FGXYEG8ZtwGXi4f-nW7Bhvn6UoY0gDrXbzSDyTEXqiWA9cVc5LJt3k1iJ25qDeALHV1ahoOwJQhZdteZmrcJn66fzE4iXiPW-F3zY1XlCwJOKyDzvG5j_cFI72mS35bnJG_K4dzBA7Kex_hWelVG9uXepFXkLYcjGjSGu2KbbqyGvo5YE7jhKzRVtJrDISdTfppuW12W9lFLOR-szFiKdZvgaP5BB8iGTgFu1b9BuqsUBFKth_BGdTqtou1FyOZ7RNItonsowj3wjN6JZpqsK9Tz7ryzM0O6ejL16Vev_X-Ajl51qMVP8wYDQrgY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q--v_K8Jznh-i3ZteSS1D8hZOYfyntFTI1Yn4k-0TXf453QyOYTHddG7tjWfDdeLmLW02pZBX1jAn6tZLGQOOQ5CjcPQGuGmB4DknESM-9Jb9wjJUlYktDEj3j6_VVteb9HMQRSWRsBeP0XNUX6o9hUd1ZMHBLkpw4KZIQaCdURHrd1kVcU0DUHj6jAy7dvgYUgOd_KpAGG7hUoxrd_8ncjifMeIWzh7-JKTh1IWTQsZ3qfsOgE1vx5f3FifzF8eW5DXbi0I0wslLJS-fONr6smU8iChZy566425_t983TWtkRQKdGBujf08z05xfX_Yh8claKIK4PTS9vYzyK6nVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCLtSwz_BKIuefaPmyr2527erpd1HPCogxv6v3wqJVn_xFLqz6UlrWeS2hqKadKUzKD-fgYWujS53FTHOJpL1cydfuO0E05A0CuOT3hvH9LGUeUq4bwQix9eRVcBUk2DfGIz7agqCdxSmV3pNG3mU_EVU-COxK2upQxsCmZJXkqLCsSl2NM_cBNoKDcGWaqTBjOmhgziyzhsb-QAH3V6hX0D1F4cVddOUpih2vn_T1S7Jmt3QgfgeB7x_luYkjgQ0-C23Fe0eE_xhf171McKfcTT2M8SrE8UgfAv6G3yihiyjH80BgVgyL4Vj8mT-Ie-QXd7kPsgAVPU9G5NuNUFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KulzWXRlNxG_tuwahaTXXLTijRzNSPmiZC7FplxurO5l2fjYzIa7iyki7P2icXjCNB5NcONt91QS_BNYyk8HLgwfkLqs-aZImQpH3R-jl33d5oFlUS7V73H5PVtaj_KU5uRao5MjPfC60yIX5SiWntgStoiB3NifeVy0g82yjpLLaF-HroCXg3BBG5XgjQTOKE2ZPdn2TbfGgR7IA6FSH8_FMt1dcnkbKuB_LBcGfst0SWjY56ZZmRBhLlflS90ci7CUF7Alz0bExu01JLxqLKDyJMJrsn51vngFKTgoG_YQrKZZBZdwL9BumiizcABppUkIh77IIZKmOVaY3TlAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEAxmsoSdXuHmq16z6_dcTtbMb9CpV0fLvNwOzzTK9COwjpQjqTcrBqyu1e0QFW-GahZeWu2FUzYqF9_ELs3x-DJANbBUMUt5GO7odRHpJ6vrKcpx9CWga_7eZcZ8L4OgujqOLrTOQuxBPunhAbdvXaLCtfaX6vBlr0QkB6zVcq62pPtN3zDynvOARXwlPa_FHRTu5AZWW2bEy0jvTb2IribBInnoi4F94vxGfKlc4zjyfPMEa5IjyiKtl9WbizbhSbhuydRrgAYVWPnJNyzQ39YhogF9mvDkQa2cLJNGel84xFjgQDItZATN1mAYjjUKXrYyRbYBohNXT9V97qeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNsxC8UQPN2mVddbAHI-xrixuG3DBNxbiVKjOSQVl95ToPw7RZd_2hMbyeAGBmEcBn_2T5mrMgmoCOrbofIVuXmVCXIi9Ct7U_9IX-XZphI23SYVDGlB5LGnJ5aKUR2_oe3qgwcmSu5O2-RVjLSG4wQjthOPNOOD5Be_Ur22ue0hmhZJD-zDfBGpZL0EouLp-XZdnD3d5I63omopKgpDda7zUWlETgCKJ2plQes5YagNauOaSGCGn9Ges4oxvHxK0QalmNiqetKzU83enXf-wqZ_njwQh9r3RtOHfbrFNgIE7YOwLKQfqGxI0i4g9JYRmjNluQeNUYvI9ob8tK36Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzepUKR36jEnoLzR1PqE64ACwDsrcmlaNI_WmP5tcqJKNnpljR7K89Z5g01i4QD2Yi0oxgOjtM8CI7PwHJOrUZzH-91T8ZKFe3z61b8FIPwrl5Cbs2915kKNH5nb9acDd5aKyz5GV_SokaFa6NJuWQcRXkVJAeYOvHZZS5g-PXY3Gkc-BzJWoPAWW-klFXXKL_ICf_j7uI3fywTxA8TR9mTWnFPfTtTxJk7l4cbd8ZPxvmjh9XWYpkvVDJwzO24Rpb30cw8-FlzvjJylgnucoX6b3Nkm9nVBUAlziSn_pYuaLfdwxg34HIdLe10P-QDc-KOL6x8adUlY7SVPjhAOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuBtKzE_6WkSTmbajlOwOEPmjAOpLyNuOvmE26zROhjyP0kDZwmirwH2CTDaRpG4-MeG_y1rQB8yQi60mNPccDTIMDBgQQYc_AvN3AFFl_CvY4zttg6RcwIf7hKHXGKny-AAJKBg0OZ3unZ6hkQP7_eMc3sy1bBc9OWFZt_ha2jyx9IqPip0Ck1qjL6jYEj2BzXyoXKakiTnrfFshKRXg4A8BPNJd59ZWWcuGSGrPkCRPwxzijnD_mYeAtnabIKPUMnqWjk-JI4dQvUfAOALFM68cZQU8Z4wNCkQ7fz1XIPlbRu3k7Hy1xn4OxAB7mSG57li1T9ewzT2ycd1V6kUvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=jAUbBDrYZVkY8VHnh5B3LBqEzyiZ1aAEQ_2QA3nWY8GFOt1zli2-VqL8PGdX66Zsra1X0YVgGNrGj3FgPZTeOknlfPQXFNPawo61F27tQwxnxibNd_IYF_-O1_VlxKUL_ljFCAzbRjzkmWhQpnY-DPhCi-2TycwCnR5MsPpEzcGB7UKqoX_zxcVvuzcoxF_46tgk1EvnNUxbTmw_SdI17XS17cMKLTjxDtlPS9WQHDYKqi_DP79i816IHAif8EQqNDKbx0eMNo8EtWXgY0W6Cr7xaeIIs5WOUYnHmFXpX-a52v9RR3UEUsQX6T6BDKloqW4it9JM5uzKER8fMTgXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=jAUbBDrYZVkY8VHnh5B3LBqEzyiZ1aAEQ_2QA3nWY8GFOt1zli2-VqL8PGdX66Zsra1X0YVgGNrGj3FgPZTeOknlfPQXFNPawo61F27tQwxnxibNd_IYF_-O1_VlxKUL_ljFCAzbRjzkmWhQpnY-DPhCi-2TycwCnR5MsPpEzcGB7UKqoX_zxcVvuzcoxF_46tgk1EvnNUxbTmw_SdI17XS17cMKLTjxDtlPS9WQHDYKqi_DP79i816IHAif8EQqNDKbx0eMNo8EtWXgY0W6Cr7xaeIIs5WOUYnHmFXpX-a52v9RR3UEUsQX6T6BDKloqW4it9JM5uzKER8fMTgXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CelvNseY8wicrtvQ5xhgvUb-RIuzOqNlyRa8FYztcjQRdqgOTjTu3SfY-GmsCzF9Oh6GHPbXu269hi0MQnU0j7T42AmPoPxlF3h38Y-bbytlSnDWzbTyBGBo14t9kip0j52AXuSzriqL9bMvPEXEgQ0DfEoqxGkstrZCPIZpwhNjh0_TRVAdCOTUXG-pAgLG8L5zYq9zvocleWZmF04PUjnwneD_Tg4x8WHvT6CtvKmf_xNttcVyaM9cX9tGvitzYsIZJYzpPd7sjE3-H1UF1DsNkq5oD9Xsfn0zMweozLF6yOMFKyigQPMYOR5RYYKQw2XgG-YDT-qcqC1hPx_aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjL7wgHiCoX_F_5BcIy2a4VgDfqtiNe23GGTLrLFpEPLqQW64G9CFguaEscgQJj0oGBVSQFRklYlB0DSR7U1gg83KahaawoCXnYHh4Jv8GQkv6bWAdnDsgtJiIp-kTLp_6rmpm-2qfRLw_55dwcy5aYo3pg-EnvNmShkzpg7tgM2NgHnIV4Qkw3hIM-DA4-xNT8XiFxTYyuEZFkJ9E1wpYcZvzJBE5qhrAEwgM2tgNjcibgdDwI50BPAE4oJLnWrGqmyve1aCIR95aoafe5ZP5zp1ZtvVrMVhtn2yzY0RKlBsfJW31PRug43YLHGbDsx29sPnDHEX-9wcMzOb4IeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPqs8XytU3PyCS6XNOJDSlGEzTLkBeaguxQKfqJeVgplGUG5EKeg-KZBvpVcwKzEKRmtYB6vuvT_CN1ip6yqds8V0qqyJqj6DLaGWaNlkBrXmUtKbhuPS9Oj3RzX5fNmw9tuXvYQl_ZpSfXvhn2XPPpwQv4GLEQBxlHVkQxfZ6Cr2902KJnrl-6MHr6ccWgvukoajW93FABFmamHFV4h_G1_UNanWy_blMOhZlmGlXJjLQmCbdGBemfnUA3pPRRhykNjL4Ua5I-jVmt4Voe1bzQSHcHYot-e5krt_9bxPWf4BznEPTklFNAiExzHEKrdO4boIY_3znHzgHx8tjiyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6aXkWohGAV2jgpDnqGUIDisoPc2rjzfRROvA0KSdgBgTEUwPXoS0MIJch4yF3RymaRfQ1gVpA2uJyG2usehWUAjUQI6qZx1_-QRALjH_cityJlAz3-BBjXzDbxsPzdDBCeaFU0UfVOuuIY84XHnUmD6CNDiSFpb8YVqaX6WOAa5aoY0w77y26L1GKGgNXH16Rvhn8dzAm-W1PjfxjbhWPtD0v0s0WwrK5hNiT_HZ9ArnwK49OhEu8Skf5nfIJ4s0nyp5xUTYkIMiLPE4-hjfQZ6wIAw_wbZPaDWuasM3zdlGMIdD8EYzURCk2xUe0UNhjoTDvcl8Yzjx45C6l_cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKwf8mhwNEVCNM3bysmlViZjlwO4yk8hCZUHM-qhJjFgY_e-V-YwMdtf-FJe7aj9laY-qZ-6P2w5GlQRqjMc_H3JNThl-1ebphulYBlJbkzR6sYROC_yhP29m1dokL1QFnhHRqWpwIebbprjQmdYWSs2qTaE3eCb2hzGyT1ELgZ3LGa8svDp7NGBLv8vTlObrk6ss4449LZQsm2ZJfoaXDtA6Xm9ajFvXIe0DiJVJc7THD0gpvbrFrN5To7czKPnSBVhfB5OTSeB2fGzOd4d3j7IBc1xro3EDYptWSIzE-jSzusY1ZE9FyOkiSnP2oNx8SMeo5zzP29mhCHdtazuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpYL3cD8unI8btxFENJs38ycR8NHuWyiKDts7OgHECWDzzRfn0wPnUZvyRgxrDUh1mszlMuNNcl5eC2ODURMpir64znEBrFOYeFUC84W99zm3Ebub6izwvgeglMb_QUG9ymEwKCjwyHGknnP6DZUH9jEF7AxQd4dhBJjaDtkwMu2IIsoysJB2KyNtYkzgqfQwU5Cca8af3Fx3CSzJosuhPqYd266KWJP91mN7AQF4WiyYDie_hV3s5Mv5bVH-_-ZFA5UotjWe3RRtaSCsh9eDsmG0zAP0PXyA3gjg-bgH-UOsJZwSJl1HwW-wy1aeJZyiICvP5TPyASZ4nE3YsjQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chLpeeloIUI5Y-_YLWSepKZir4hQuh_xQSb0VC3BuJkJkXjitBz9ziBj3MZm_UfK6xDb0WRMzwxtcmbFvVH4v3dqhvtAt3iZbJzW9CbrHbMACp5xk_eQnPoooCwxChYhtRAtAjy_Ze4buTjGie7X-wDmorUjOCi2cLz31sQsWThl31J0R2b7kyRCpDYPoS1vWAUeRSvcEcj2t7iXSzP6SgDny3qS3UZ_p9Z3BatnvxF_HA7gUzPn6qAYoWPSK2u7vu_EFz61rmV0gktg7uIuDbfzZzvG9N3xea3EsbJXOOUs-q_kWPZ2PGufi--EL2y_ZVJWwIjSRaDtP0IGyjrJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=EuAWGjfOxjEIR6Siq45XfVu9Qko6YpaBtsEWpVHncr2hWMPlp5Zi2ziLp5iE4GvSacuH6m6YtEXqsKHDqgnXZbeynMW4Jd0oeHszyFbnj3ox7Az0OAcJvO8dId7B5ii27BqH2E8N66VBpD7qYPoi5JXBLuf0CAOuCicF0iTdT6G5P4aO6MDI21OpLlsptPffic4ary4_DaSxNnyKeKh7A-aki2p5Buh-BZ74WDqbiX6HdqeagLFJ4s1Mol1cRTZa5bUt20amsa7vGhLUu3TcgevLg_3AQLqX8ZFFsfEcpldGAOfWrmN4kKh6wivIDvH1RY-AkvZSq4-Il2_lv8nqzHCbHqB8UDzKmszkOnrbY4QIknXvGLebBZXNBkdwHUoaY-zBOpRHms0XcQrI1M-FJpxfnUodjsrMMwWmiBFpX81R2KKiueSunUrEI9TC2eEsFKOxyUrP6ke_ze4Z-oPhuxnKPbEtVHSFUF-jOv_qXLm6DWP-5lUM7l5A0KDeM7Ej-9PeT4elDi1UpQjtfVpDvphVY_3hvXX-lXzjJRgVneJjNZ-1CwgpbzXU79aM_1G-0iRQcGka5WBGKIBXYNe5qxTOfu7u6LWkshTZ6HQkirdElrh6RGnilJzd0Iy0Rr0CSpGwrQbbm6Ki_nYet3jRtHsdQKSboexxOSWDbKORukU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=EuAWGjfOxjEIR6Siq45XfVu9Qko6YpaBtsEWpVHncr2hWMPlp5Zi2ziLp5iE4GvSacuH6m6YtEXqsKHDqgnXZbeynMW4Jd0oeHszyFbnj3ox7Az0OAcJvO8dId7B5ii27BqH2E8N66VBpD7qYPoi5JXBLuf0CAOuCicF0iTdT6G5P4aO6MDI21OpLlsptPffic4ary4_DaSxNnyKeKh7A-aki2p5Buh-BZ74WDqbiX6HdqeagLFJ4s1Mol1cRTZa5bUt20amsa7vGhLUu3TcgevLg_3AQLqX8ZFFsfEcpldGAOfWrmN4kKh6wivIDvH1RY-AkvZSq4-Il2_lv8nqzHCbHqB8UDzKmszkOnrbY4QIknXvGLebBZXNBkdwHUoaY-zBOpRHms0XcQrI1M-FJpxfnUodjsrMMwWmiBFpX81R2KKiueSunUrEI9TC2eEsFKOxyUrP6ke_ze4Z-oPhuxnKPbEtVHSFUF-jOv_qXLm6DWP-5lUM7l5A0KDeM7Ej-9PeT4elDi1UpQjtfVpDvphVY_3hvXX-lXzjJRgVneJjNZ-1CwgpbzXU79aM_1G-0iRQcGka5WBGKIBXYNe5qxTOfu7u6LWkshTZ6HQkirdElrh6RGnilJzd0Iy0Rr0CSpGwrQbbm6Ki_nYet3jRtHsdQKSboexxOSWDbKORukU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=md26aAO1aKuEibZcLDDsc25Z9IvnhN-XDwGkSZ2-2J2bsUCO7dow77MbCFkeOViQ3gzZoyHLa6-fLO68tSMzr8SqxUlYaUa-f9OMo5CLLUgim20BCi_EBjTulUsRoXmAxJQfN1r7hNYKVKwyWckF9iozRMrWZtrbDtfdBU3qL9vaCJlt9wjtdmwRS9feaGp4EO2k_bMw_N7iNeqeQWxT3tMl2JT3gYN9EC-isG3iztwSvZMitXGe5RqnXaxbzph_qz46rB6wMZWwFirFgITxP_xoni6fwLQfmh6r49ZRmBY5mv24bDPhcPdW_Sv02O1JcRYmwZ1mvrDSTsHJeIzURA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=md26aAO1aKuEibZcLDDsc25Z9IvnhN-XDwGkSZ2-2J2bsUCO7dow77MbCFkeOViQ3gzZoyHLa6-fLO68tSMzr8SqxUlYaUa-f9OMo5CLLUgim20BCi_EBjTulUsRoXmAxJQfN1r7hNYKVKwyWckF9iozRMrWZtrbDtfdBU3qL9vaCJlt9wjtdmwRS9feaGp4EO2k_bMw_N7iNeqeQWxT3tMl2JT3gYN9EC-isG3iztwSvZMitXGe5RqnXaxbzph_qz46rB6wMZWwFirFgITxP_xoni6fwLQfmh6r49ZRmBY5mv24bDPhcPdW_Sv02O1JcRYmwZ1mvrDSTsHJeIzURA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpfCp06nGCVWe5sWro51ooIG6ZXtLz4Nna1j9SFIbWalKYTvwTC7cy5XuHIgJjE5w4txLLtdTNRK0PrM4X04E7tQ_xA5dzvj1YtypCJHJiEsivxH64gV6Uc9Sk8h6f5juLbToWbmySbv-wCeg2Gjy4lmUSZtrbFvloGWmQ6sCvxpGNtG_J2IZSRf2h4Obt6b2kj2lGMnrDdQ24q0hpPvqzCzoHyTTXWxB4K3BVS38LcAB4jKmx2nee3EV6t0hSSsy6YiLSTv3_yuRs50nu1g-zvB-wyEYUzlWoYMHvK1BCfUmM9FCssDd1H9z84WzpSEQhadK-CNalcT-WtXJqy6jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrRGu0LaUVQxwfcitsMMkhJiSsIjjbYx1QfyLkfBIAEXIDh3wdxHX8jxFU0l6243alFgOTOPz0twtjTjEiOKJOe5uIucovpfSJO32yURNfWtnrJjeP4amSwC3R9GoScJacCfunqONFJ502dFDgYSx80ahn3kG2hLWcJJGA2_2FjY9KwUHdGgjOyvg5OkDw6J2sXaWrxtB6HvnnY6VVW1aLyfchlq81LSE__1S34-dpKy4eo35hXJNDBFYrwDgHQ3EeS2p1mTws1rH5vnijoTqbB6laME8h1vp6IwNFL479r_VJb8WRr6lLoDGo3d50l30JV2AWM9fYVOS4wgy1eByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=u-9_QyKEM3FesaKfQbj_K7T2zb920EJ0FQoKWhrpwXbal1Ah12FU13pfODXcRq2C1V5zqYbG8fuKxh9XDdaF5Zk-KGPobJ7DumGAENh1Hp46hV6aX4rKP7HAhrEth4vloTy3g92YeUqxI838pefKRKsKl0TDNyDuTkG22anVu3t7LJCGZvOHURD8c6AhAo3O1Jaqh94hrs0dQLbhILs7uKZyv67xOewrAx9GATXkBI8oIiFA3PHwVFRIejw0znDurooFS9J6Cvor5wU90o8mQWuTEhG-dRL2FQUtbDisTdLQwqrmNI8-YvTwYjMrfZTMiG_2FF0uR-PfPJQgGYXWjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=u-9_QyKEM3FesaKfQbj_K7T2zb920EJ0FQoKWhrpwXbal1Ah12FU13pfODXcRq2C1V5zqYbG8fuKxh9XDdaF5Zk-KGPobJ7DumGAENh1Hp46hV6aX4rKP7HAhrEth4vloTy3g92YeUqxI838pefKRKsKl0TDNyDuTkG22anVu3t7LJCGZvOHURD8c6AhAo3O1Jaqh94hrs0dQLbhILs7uKZyv67xOewrAx9GATXkBI8oIiFA3PHwVFRIejw0znDurooFS9J6Cvor5wU90o8mQWuTEhG-dRL2FQUtbDisTdLQwqrmNI8-YvTwYjMrfZTMiG_2FF0uR-PfPJQgGYXWjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ourTu0OGHh8uLKYFSbmwczstGFstbmqwXS-wJU5BT6LpaKJjmKHG6EtNwEljSOjP9WB2uUmDB2Z6-El9UsOP-jB3woJnSlyWjAqjYLern1As1RRNQxxLGK8IGKryBDlKrSMLPPs46DQDvnbuIBcFw3UO166aSCNLnwk8gezu7v-_PG7E5xapaJygsL6WSLlXPsNg9TzUNphrMTl8I-1MV6ww6YDTAIuF8eh0iJumcZGQf_e9ZDpu6qVSdNouFa5QZMh714wCtIf8fNllHYtwVnoUYXsc63nFfsf2OjntRd3i6fJbashzkBEWp4WG-LeMdFI6dO36V4bTUUZLZ7EOiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBphZnuiE4jemvsSJ1Bqy_rbaTQAGRL3AzDCJ65YzKJO5amDUK5OUqw5DnPQXtlohf9TbicsfYGdet8s1JyzpKR384d-5HnzNEavKSmq0Wv93WZc9hJu2NQNVzzXnE-LzyO4mDGK0sphJEbEMUMKbuZb__d3RVNLX7nUgQPS4qFc7hYn53OMNiNMTVNlpeWuEhDVLLvIzlNfNCvgqRYDGdGAyDGrtNRaXBFzCvM-te4dgpd3SEFX4IkwWpcjlvJopM0rIWdWIQXXUn4TwudvJdnsMZruOUMFSzLJrJamomzIqTEKgABkac2RG33gJGVJIQ-EP-FeFOBoxFNZijgGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwM2HEMipnu4he0YEKophAmah1CJckywbtKaJPq8uWs2zE1daEgA9UnpAUGtO8AQvCBgSo6yr_-SVULyFE4bWYfU8k-nfw-UCKviG1BiW6rl96ZhpLgs7eGx7gxlkz-U6xufJKDIWiCYX0oQHgDA9CGMpm0hdE3Ez7zC_n6NtUtIqRG0do6h1KT9QKz3y6jtk_xN1LN0dKhUuLcpX8Uks6PrXUMyMX3WiH4QDO-nHKwa14j17IGqeGUxqy78QrVcRS_Tkip0ZwReyxJr-8p8IsCJnilugb9uhKOxEdSScU8OASEAf7GjQ83yWr5nudPKSTXDOAt-iS2ziyfkLPvkjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKUl0IgyqW42_80FXmGiW4IASHchJEXizHwgdRS2nzIAq00vgyc3qQa9wqtp7sMGaqo85PHLL_uS40Iq2N6jh-a2PDS16bIpz8N1mEQE2Fp7Sd4Py-fe_0gs3a5fLLs4ZDeuc_D_NerIGkjPxw9manzS-is9M_D9JPOCV5H_VBooTbQzOr4QmF57Vo_WYrvUQMI5K1dGp-qHGUGw-i97CloBFIFedePZofvYCgeklkoM8DOVq3eavwc4iFas96KTMBQpkJ_-jy37tOiRqLXWpw_SUPs2k4cyDDPQm4hjd1EoI0Cl-xhh_3KosyxNSUMW6Js_R4KHG7wXvXTur78Xyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6XL4wyhc2ZMgKkF4GLQs7kwBHFW_3iIl0TT1dvo15c1je6yYb7wolI5lEgArs86mc1fxXOmWFyGI5baV4ZRPLm0PQ6dUtYU2nsrE07mT5e1NA2-a1LP11X97SYYju372mvHytTX7Cq3moA-m-awXAhmkcwbP2aXP6kD7xvstCWCbJQVvQ1e6qehomjSYS2jTgiwJjxIlYCxwLUVggvgoEXfav2Masp-QF1BOglZbhjlJja7rEVyIkIoTBydQwjNBsdaqsJeIeSF1GPocRXiIogPdDYm32uC1IRCf0J4IOBwiT2Fy1Z-YuAq3jR2ntLivbJ2A1_olcjiIXyzrpTc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5U-UsK2NxGmthSGg12rssSmBgAlS9ul1Z3E7tQimafUcPrr1sPEO72rkhXSv2rB8eeeIhaA5U__Azw4Vw0LwAUSpQI7QI6K_twah3PhALSH0WofkzVS30ey2LgCay68y9Y8c3A0nqZY6bGNUmdt48BjzY6fLVb5kBlV3GRQXudV_DEmIWhxfwsZsRpTpDmNv-qvdznXgwxoBfyQKTUA_UvUrrqgkb2sk6zz44CkEpcC-PwgcsH0U3YbevjH78Tmbp2AHi9kC6r88XC31eN-eTZhpMf3yJGCOkVsdIGdGXD0Xria69RhHlIETeorDPtsTiDkFLTZ3RJYp4yyDL1GZl8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5U-UsK2NxGmthSGg12rssSmBgAlS9ul1Z3E7tQimafUcPrr1sPEO72rkhXSv2rB8eeeIhaA5U__Azw4Vw0LwAUSpQI7QI6K_twah3PhALSH0WofkzVS30ey2LgCay68y9Y8c3A0nqZY6bGNUmdt48BjzY6fLVb5kBlV3GRQXudV_DEmIWhxfwsZsRpTpDmNv-qvdznXgwxoBfyQKTUA_UvUrrqgkb2sk6zz44CkEpcC-PwgcsH0U3YbevjH78Tmbp2AHi9kC6r88XC31eN-eTZhpMf3yJGCOkVsdIGdGXD0Xria69RhHlIETeorDPtsTiDkFLTZ3RJYp4yyDL1GZl8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=p0NGBcoaa0QloQKIHk-4oRCz8HWS4YNQsdVJzCl8esjmOvGrN1Ac4ome04cZZ77ZjW4z6aaX56TU9Sj8aoLpKz3x85nPi3kek3cJLX8gzMby9wqu_5WkR6a_MZUTXjOX-9PkaXl4Hj4UT_-mBECUrngqMWT6GSUKJezuDEiIZXhBrmmaSyvAz6Zwkg5TjHtr3tpfIwTSUbrjm3-7evsixsWoLoTi10Np9wczbMlXynxPBre13q-46-0CuJfQCtSOaID15GoQgJgCVBR8seHz2tnb_5zq2KUlWNCMkcV8t-Fz6ptaqKNRrALfFNSMtr6Hso81AbbLPeUOVvBRS8_t6T1yiYtyJGugQLzFH5UPm7NB_zfRBe1UyVf9KiDmDj55y1O1QGbIRxQ7p0_pXBWGppR-t05XVjXGYxU0baUAKrWlnD3a-quvV43NbhzOm0J2qv2wNqKkLBtWKcGAPLk-1McDlQVc3Dy5nCO4O14XQieJVYamMvf5VqxtClK18mn_HHKakmqsvZylCrMYVynlGEd4fnmgb0Yj2cg_6CBteWIyh18cESsBhVujuxn7jH9I6YaKzXkXA1JHt0Ks0XmtI9T6a53zlH9UPFaXw_RkEPmRSXnWWJk39A_2CTTnYg05NJir7wmrslnmcaP7Tkw9RlzfWx-CEPuIPfT7IKajeSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=p0NGBcoaa0QloQKIHk-4oRCz8HWS4YNQsdVJzCl8esjmOvGrN1Ac4ome04cZZ77ZjW4z6aaX56TU9Sj8aoLpKz3x85nPi3kek3cJLX8gzMby9wqu_5WkR6a_MZUTXjOX-9PkaXl4Hj4UT_-mBECUrngqMWT6GSUKJezuDEiIZXhBrmmaSyvAz6Zwkg5TjHtr3tpfIwTSUbrjm3-7evsixsWoLoTi10Np9wczbMlXynxPBre13q-46-0CuJfQCtSOaID15GoQgJgCVBR8seHz2tnb_5zq2KUlWNCMkcV8t-Fz6ptaqKNRrALfFNSMtr6Hso81AbbLPeUOVvBRS8_t6T1yiYtyJGugQLzFH5UPm7NB_zfRBe1UyVf9KiDmDj55y1O1QGbIRxQ7p0_pXBWGppR-t05XVjXGYxU0baUAKrWlnD3a-quvV43NbhzOm0J2qv2wNqKkLBtWKcGAPLk-1McDlQVc3Dy5nCO4O14XQieJVYamMvf5VqxtClK18mn_HHKakmqsvZylCrMYVynlGEd4fnmgb0Yj2cg_6CBteWIyh18cESsBhVujuxn7jH9I6YaKzXkXA1JHt0Ks0XmtI9T6a53zlH9UPFaXw_RkEPmRSXnWWJk39A_2CTTnYg05NJir7wmrslnmcaP7Tkw9RlzfWx-CEPuIPfT7IKajeSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=pwAr0xjUFZy4zjAgduhOe7WvLZwmZKrp7cy8YJ-AKF7nwPU17M2shuwGDif4i__5E9pCipgJ-zGke5BBro0g2uey6yWUc-rYMdn8u4mqYecdK87xbL5pUEfoi0y-QiIRA3FQpor4NFIvozLeEY07uf_jG7p4ZLOrGtZqBUZFq5KVnTbGzuWoykpPHSvmSziMa4gesVIpv4w2McF3mJvV4nwxHyQIY0cYMHrUu0bURK3yOssbInT7n2qL_kt1yhvg3U618LRCp85WNlqd6C7w1g6O_urcSMG1aKfUKAlB0-4zJN1GQ4Vp49M8mCe-ERUUAxV_YMwAVoRi0bAF8p14wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=pwAr0xjUFZy4zjAgduhOe7WvLZwmZKrp7cy8YJ-AKF7nwPU17M2shuwGDif4i__5E9pCipgJ-zGke5BBro0g2uey6yWUc-rYMdn8u4mqYecdK87xbL5pUEfoi0y-QiIRA3FQpor4NFIvozLeEY07uf_jG7p4ZLOrGtZqBUZFq5KVnTbGzuWoykpPHSvmSziMa4gesVIpv4w2McF3mJvV4nwxHyQIY0cYMHrUu0bURK3yOssbInT7n2qL_kt1yhvg3U618LRCp85WNlqd6C7w1g6O_urcSMG1aKfUKAlB0-4zJN1GQ4Vp49M8mCe-ERUUAxV_YMwAVoRi0bAF8p14wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAau5BCZBzSt5k7rrS5gr88HqZXEeJnqChNAJdzfHQrdapHY2n5YQmMXwXRCdhRFIqxmm2LT-X0r9uB4LuUbtIjZ6lOGdJFxEuh6LmfWzO9_66MMfcZ2W43fI3Sm_8k-DIIDhCCG79bo6LPuvVpFoq2BbJc8GTToaBlIiz10qLVoS-HJNYqUTGzodMexre4N79pnWLHhEK8kOZoC4d0DWrL2ub1RShQTrSdQynKF98Ue6Lx_Uy13dnrTqBbDye5zZJWRNysttsznJDRBVPWYtTJ3UMPL_nyGnn0YFhOpjXMvHE2oobA-CMyhwHe4HiR5wHTVoAC0dOzkCkriJ34PVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWx1ZRg-C4NaRMpIiFKSbXFl8PpDY4wew0KMokl1m-2utwFfI7KnFQXDDfkH6ixB6zxOagOUWFJY4rZRJl7eu8Ry-jXPNXigWnGi3jLGFsRv5pKm7XkMrJLM_FDvtbnDoxbuJGy9uxu26FjSIQ8ShijU8-jvkk3C7eiXPpUpQd7n3ud1z1xQqGPRIXPh_i2jutiIBz3836WVxYB7Z4fznrV-JxlfO8KOurJmyy-cjnd7OjW4ib4BMZXhUdet-_1feRtFblAyvvbh0A-I96iBwGkUy6Mfmc1Yu-3MZau1cUCq0vWAYSPi3b7dpjGi7OBQ61OjZGMLAnQrhQp-xkkotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NFAK7r3q2y7iZoQpXKSURW4ZagwQva3lsmZLtf5d_u7pdngkz10A3nQ0K6A7BrvL2MiN0lW1pGn_pGe4Po1LbbOffFLjcFcYwNgtNLGkdwpFavNdkrE1Uml8JZSDydyze4WhfI_hTTXbAZzyGjU7E-IOCeZvOWwM6CxlClUCGBzd5G1lO-3Ww28v7g1zUaQDu0_FfKz5YRpgagf5ZFCi16uxmbwU2bN487zYK9Bf7MtBy3CvYrH0uc88LQlyFOkyfbdcvNufPDRDu5eKEuboXQCCKsyhkKulyTv7dRH2Fydfpkx3XAH2RqiPgHpl-GibGDarSKpPEIf1xRlE2JGpoFapBYr34QP541kxgi6ApyGKYbvqEtpiLisYQqsLDWkkSrZUs7AmiWVcv42xMyfxki9MBU265eomV9dTEUAG1V-iYF4Q6VmfMEkws95kazJO1OMvoNaeeyMC0YCVbWldX9yIBDxik8KipNGg7gOWnbc7cj7bUZ1ZxH3hptqV9XGDg9idbnlqVP3gTmzJx0Ych89DMZufF8QQPcP_RGoMhTju0k6hWX1rq2yKcaUwKFswwVcfc3EOM2D42wznuD5UlLu94FKO6yK4YbG5W53zSRt0sqX3KI9dRADeYdypoJ2Do7q2c1O8uTXXC3Bcg0tGI96WJc0-krk2uMEZZ6JGSmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NFAK7r3q2y7iZoQpXKSURW4ZagwQva3lsmZLtf5d_u7pdngkz10A3nQ0K6A7BrvL2MiN0lW1pGn_pGe4Po1LbbOffFLjcFcYwNgtNLGkdwpFavNdkrE1Uml8JZSDydyze4WhfI_hTTXbAZzyGjU7E-IOCeZvOWwM6CxlClUCGBzd5G1lO-3Ww28v7g1zUaQDu0_FfKz5YRpgagf5ZFCi16uxmbwU2bN487zYK9Bf7MtBy3CvYrH0uc88LQlyFOkyfbdcvNufPDRDu5eKEuboXQCCKsyhkKulyTv7dRH2Fydfpkx3XAH2RqiPgHpl-GibGDarSKpPEIf1xRlE2JGpoFapBYr34QP541kxgi6ApyGKYbvqEtpiLisYQqsLDWkkSrZUs7AmiWVcv42xMyfxki9MBU265eomV9dTEUAG1V-iYF4Q6VmfMEkws95kazJO1OMvoNaeeyMC0YCVbWldX9yIBDxik8KipNGg7gOWnbc7cj7bUZ1ZxH3hptqV9XGDg9idbnlqVP3gTmzJx0Ych89DMZufF8QQPcP_RGoMhTju0k6hWX1rq2yKcaUwKFswwVcfc3EOM2D42wznuD5UlLu94FKO6yK4YbG5W53zSRt0sqX3KI9dRADeYdypoJ2Do7q2c1O8uTXXC3Bcg0tGI96WJc0-krk2uMEZZ6JGSmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=ZMyx9taYTGCTIf08uUgpoPqXRXmeNQbpTNk3hBVxnBf7eE0GYZyCiNrkyYmC7mST4oSBmAiYIaJ8GCNqPK7CiZ4STFNrfOjUinyz2_N-7vh-GKLJu4g0-EONb912QnU7CtWRVhucDQbFB2XKh586p8YrLFjGYLph6DzNR145hFnyDVwcELa-B2xx4Qgfikj9zenBHnVYtOhFmkLPq2HV5ApgvIpY9DKth5WWCBcSmFHGkyHk4I6Bixgg2oKKG-EzT-3ZYILCM7uJraVlMaB_y-fLiza0oXLmsMW6r_bReXalwFGa3l1XP_v1C983J-7TRp62VRKkrRcXeOKFG6Ydrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=ZMyx9taYTGCTIf08uUgpoPqXRXmeNQbpTNk3hBVxnBf7eE0GYZyCiNrkyYmC7mST4oSBmAiYIaJ8GCNqPK7CiZ4STFNrfOjUinyz2_N-7vh-GKLJu4g0-EONb912QnU7CtWRVhucDQbFB2XKh586p8YrLFjGYLph6DzNR145hFnyDVwcELa-B2xx4Qgfikj9zenBHnVYtOhFmkLPq2HV5ApgvIpY9DKth5WWCBcSmFHGkyHk4I6Bixgg2oKKG-EzT-3ZYILCM7uJraVlMaB_y-fLiza0oXLmsMW6r_bReXalwFGa3l1XP_v1C983J-7TRp62VRKkrRcXeOKFG6Ydrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ido2ADQT_P7q5eRv8M2Eofz4KoF4QK9Nxn4v-3iEIBcJNf9XEukaHyGczZ04naL6sxr-rbxj9MDL_mxqkaJpJE9tsAKnPz5F5hhcyM8tp5sopGwA3H2t7TpfhtIQTTAvGaAHfqRTsbV8ExdG57cy7VnABxto4h9eMTQWpE6GZQjIp-i1Pxf9FLJCnYfYXZsNN20bvkHUKoUoLgCim91wAzBnOqJ6DD7LOfwHGSVH0RYlaWnH2Ef1N8gvOY80sqCRVg2K9sA7-VbTuKmf3GqOtjtHOCNoEYHIknIuHcWjjS6ZoRjt7ITAPZ9V3qrhAm35344X5SNKwQy4uPz6WBiK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5rk2nemknGMB9Kllkp7DyNvHdN7IkcwpskLg0s_OeRfsNND-Qh7FXC3Dv6USxxJMTZqXn9dWv3TeI9fsihtQRelqbasggTzzU5hvyP0nG10q92iDtakDG4CpBI24raQnRL7GoqBOC1ENWD_HYLZbzeImfD1b1Qyxm9YGB9GmE7VN2mhG2ENCImgrqsOg78gJT5oz164lSYZ7CcWLMYltEqcdvv491ol9Qsk2oMi60btbzWdnhS5JMkWAlxy1JyDSMTrORe1wrNqbjh-7RUa-1z9Nnsu9EQ6fUwnv9E-6cxPD8SQWACikxBg9p5prp7kIK6M7D_MsdZDRIg_uRo7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQwOAwBI6-Ecfd0MrVC5RPOGn8s1kXqvWA0nSVnisMW70baFQ6dB_TdGxmHyaiRU-0RAeaC5G8Ahsf4MEU7aC7MxwepDZjJ0jG6AIDnr2jJKyYgoA-Q-nzfOltTYvejMXmaxg40AVC6OmsD7zIJPEnwGezn1DKiIe-yuyUCuSURS7pu_4Ba_P486OGw9Jw0IHNxFxdJHeNmaQvEIy5KnTwNNkHPfr-MhiqoTxVBtgTs9XPJLRtL2SQVcP47-3xblmkKOgxM_Fpmj3nCGJ9tV-P5Vtf8bDL4snatzt9y6uiz_zqLIxfVUai7Z1-xt8f2_iBCNgl4hvnheEKs6KCPu7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Ec5GOVSGGztl0fW0TI3GK_EzXoEv1LANHSaXtPp5NqDtJSOx5E54zFSUNIsu0OoxUI7xb2Q3IgXoxXQzzt2tLyaaQV-n0_xcthyQAxU2-KU2P0FI1HlxHtIx2dy5a-_nUS1Lca70atgLCoe7uZ3RS8VkEyhHXaB_s8EFgGNgLT9wefsXUp183UcJWLLO_Jhi_GkCQzwHeotjyfvFxuxq5Km66DNQmtRgexE2Z5f-4CKzlVWGvBsUhk6GcrsdyGUjzfEEm4H8Y-oqPGyZhcT_u9aC2jucJ2Q9CHI_yZuu4SQ5n3k7rOA-iq_7DhohjfAgr7OOvur2YVemwRGviEsM2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Ec5GOVSGGztl0fW0TI3GK_EzXoEv1LANHSaXtPp5NqDtJSOx5E54zFSUNIsu0OoxUI7xb2Q3IgXoxXQzzt2tLyaaQV-n0_xcthyQAxU2-KU2P0FI1HlxHtIx2dy5a-_nUS1Lca70atgLCoe7uZ3RS8VkEyhHXaB_s8EFgGNgLT9wefsXUp183UcJWLLO_Jhi_GkCQzwHeotjyfvFxuxq5Km66DNQmtRgexE2Z5f-4CKzlVWGvBsUhk6GcrsdyGUjzfEEm4H8Y-oqPGyZhcT_u9aC2jucJ2Q9CHI_yZuu4SQ5n3k7rOA-iq_7DhohjfAgr7OOvur2YVemwRGviEsM2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=OleprcC-7wcyXjZyfXzVmmvxXYDqpCEUJ1dRgwxTnnP24873Mx6zsIhguB_vJBWXGyB_dJdKypGh5P9iwMmfNoQ3Ih4aES7fI7tD8QJbHBrjt2lRVkbb8mSwzMLvMj6zKlUyds9QS8ZjyLOqhp7_hkOjGzNQa1DaktdgNzkg41uuHJmXb2wnzeO-LKV2k4oF3gVOWCbs0RAHXpvEqKmcZCk4cERum5Zqqz1IbbDk_T1WLfQhA3mwpryFT8NjFueHZaJ-xqsU_lkVD8SRtvZlYmd2sNuBVbstqfCGlaRI9WSw4S42sccjmDjSxddSgA2FI3-8Blk3Ia9atXvF-BDtNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=OleprcC-7wcyXjZyfXzVmmvxXYDqpCEUJ1dRgwxTnnP24873Mx6zsIhguB_vJBWXGyB_dJdKypGh5P9iwMmfNoQ3Ih4aES7fI7tD8QJbHBrjt2lRVkbb8mSwzMLvMj6zKlUyds9QS8ZjyLOqhp7_hkOjGzNQa1DaktdgNzkg41uuHJmXb2wnzeO-LKV2k4oF3gVOWCbs0RAHXpvEqKmcZCk4cERum5Zqqz1IbbDk_T1WLfQhA3mwpryFT8NjFueHZaJ-xqsU_lkVD8SRtvZlYmd2sNuBVbstqfCGlaRI9WSw4S42sccjmDjSxddSgA2FI3-8Blk3Ia9atXvF-BDtNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmt0BvbX6Gbtn_5WSU3bDvYHQu21vlZad3p5uQB2777nGuZ9V5PBpYoCtem8Zv7-fM6YuslM6Ex2ukUYJtTEdY6cPqLR4p9J1Ashn8F2WwHHQMDw1x_ZolZ1VjBkpckQTdaE9dlNVqiM-L7gIDnrRDsDTQECCEax2A-x3W2d5su-qEMiVdpYHMPsjEoN0UOdyaF9ntZ7M7-fmAS2DkMNUvxe9iQvek8te86qHXJ4Sr2yuVpqV5GgMoINUNRtl39fapHjRdd72NcscgPR6VuNjQu6bHMAi-gnwWRGcBHvBqqnwCEaaRb8FzYmKxKfqnrLsY7_ZmhwI2MKj8eDHsZ2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSme3mlIZ3eIIoTl9I64Wu-Hq2Crqhl0_aoyopS9ZNyBmA1ApLjLW7KAFZOueZ4C49mzIJoo9gnff6UuZFn0ErLd5ftCBTpIoLh31NGlxBE77ON4BrDdytt-fZuUOL4FEyvUWeRi_kaWZwvE8fVcNJo6KK5xUnnl2n2QUW1nY-w4MNSlG_oUgzXRl2xTsA4HYPEt1Wc1RUvDBIBZl9EaR1oDTGFULpXS7oHpPs3Yks0Bkf2eqgwWCnT8rcuycARZsgFvmi8UK2JlJ47n8kcbQVvbreKc2S_zmdUKs4Po9Ho4-lbOFyOh3aek9Ma5EvrwN7nDCFcEvMmWoQxuzSDmew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=ZcaZs-SI6LW6fp5imGcI2YqAWW4mPwU6Q-gopTscatw44lhOukllfbo9quowt_F9pUPzpeKp0nqrL9mbmip-n1nFhMOSw1UaIXSdLt2m3p9prZMutVc5pH4m-64XFiuaaiPB2burTXrvcXnpomUxUcTm_rRrUK984HvIlgalYj931Y8m3KOE531W00OsmIkqv7eaQDe6VQrVYseUL7I5P-Ny5V1SSZF5LclrwBY7mv3ey1p6Q9nXLfklXfYnUdFrnKsuNL1hFifxXCFDxvA0uvtK5ZD13OrMEi2QJpb7xaAuHIDogsHET7C_Q4nN_yMLy3_-2Qf-n_5Tpx2mTH8Ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=ZcaZs-SI6LW6fp5imGcI2YqAWW4mPwU6Q-gopTscatw44lhOukllfbo9quowt_F9pUPzpeKp0nqrL9mbmip-n1nFhMOSw1UaIXSdLt2m3p9prZMutVc5pH4m-64XFiuaaiPB2burTXrvcXnpomUxUcTm_rRrUK984HvIlgalYj931Y8m3KOE531W00OsmIkqv7eaQDe6VQrVYseUL7I5P-Ny5V1SSZF5LclrwBY7mv3ey1p6Q9nXLfklXfYnUdFrnKsuNL1hFifxXCFDxvA0uvtK5ZD13OrMEi2QJpb7xaAuHIDogsHET7C_Q4nN_yMLy3_-2Qf-n_5Tpx2mTH8Ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Elb6siux-fDNM52nfgza9LLDyyMDnBsmSUvRAFPdcD5G9uuUQp_ngDd6RSrreMXP0sKd5oh6Ncf67pOnnjS6nkG1jGvZiJtn1obsqVdtNUYex1RV_g5sJrxNWteZTsKDL4DQKYYU-vO8IbbhdI9WPLXkyofJHIqVcoE2NUHsoI1JWJtaQNfzUL8RG7jt98sVE9yHa3sl9oPepUmLLGVN3hjtt_Xu_l6H3wBi6AtFeVHGm7CqvctGT7TD0UEtIganHnMZ-acLUbFUNkJUbc8rdkDhMME-WSYcNAclt5V8hxqHUD29VUdZZ_ICRtsXSPsDufrvzpKy8k-CUKprNx4m1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR4dNWPqYY4h5tCwXSiSdPpf7onG1Rvmd7SJZJ1K-grAsgj93AZDY4ggzw_oBZlijG-inh20ti_8ir3BBHirScO7LMysInZCp0Io_6opidMCNiFr3MV_Kci-IqqO_gsxx8bFajGCRLdaAjL9HjXUQmXW0rsIh3YyIwz42GThmkropGKJb-l2pZfj3py59U2fSvxoQEGX9Ke_FvSTmz7JlrIUvvi9ZW1a4gbw_3tRpnkVsMvPTK_yUJuDph-OEUSukMZ7TBarZBUpbtrCYTmrK5H9cDPnpzx5PqjCp3ukN_aPcopRTYqEiPxXYS6Aa2epvydu-tS1dQy6PfFA0OSeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJOtuLgXEnKGe-fjWuyhCqPSQqi2K9bQLHwJMiQ0S4qcbLSh6mX-BZb-k6OuRnZxhqgEZEVH3kqHYchL_N1eVZF0rYSVHFAGZpqkhbK1UoPxjluOJcmz29zBV26OxAhfhJc23Gnzek7mfEz7G_NdKYG-bJUdy-BwRZgjeA1LvYHVPW_IYG20qS2BAygkcsBNNvplC4J7O0jVraDny8qwyS-jiKcAgT7puC40yFUcnaIo8iAMm3Q1_ugnQ0MOnltFOM5VMAHOe7VsQcywMK67WWN60yYqZUq7LM8cHH9XJsW-rktMs0GKZs1WCiv6mvwY7bWw6_jWxI7b2vx-qRxakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWzzpZ3yb0As3QcWkpw6x-OtLGY_4YZABktrXVNRIGszmG258BUsh8FfJPLCDUKQHZeMSQFCU21eIXksoMC7ts9A2hviD1q-CsxZD4hFVyD3fT1ojpHZ24EzxeqGIIGnjQDwZPQHXvuuf5nwFp5UcUG82WhxCIvMbiqaOqJWdI-OFQbEtN8SQaGP5UQPZbkqQJXqrgdhLoAsUOm6uCBHfxoIMJF3F6QjBaarp59GOCLBdtYdV2cCeAGx0gujGx-PaYqRIiS4NwT8kc9Omp6_Gp_K6CS_Nm7VyFSbOnv8oaoC0ZS0d8FctkPc__xH6z_aReeUDfdKaY5s6xUAh_Iod88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWzzpZ3yb0As3QcWkpw6x-OtLGY_4YZABktrXVNRIGszmG258BUsh8FfJPLCDUKQHZeMSQFCU21eIXksoMC7ts9A2hviD1q-CsxZD4hFVyD3fT1ojpHZ24EzxeqGIIGnjQDwZPQHXvuuf5nwFp5UcUG82WhxCIvMbiqaOqJWdI-OFQbEtN8SQaGP5UQPZbkqQJXqrgdhLoAsUOm6uCBHfxoIMJF3F6QjBaarp59GOCLBdtYdV2cCeAGx0gujGx-PaYqRIiS4NwT8kc9Omp6_Gp_K6CS_Nm7VyFSbOnv8oaoC0ZS0d8FctkPc__xH6z_aReeUDfdKaY5s6xUAh_Iod88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuhfCB7YdaiUWKmNTAT3Gkmud88FyRV4yKwzyclb-MBJGQWrnQLXggzlvusodadI3mY69DodSRDR2DMoUCI_Xcvu3pqtR0Pp1GJgTtfYQ4OGtaVw_LnqQhwqgZa28AIevoohxxiCOHRgId3f02Ljq6Fh6N8BuAiFfsufEZflYi081moMGT8dgTjGXvIDpeU2ElmB8c62eY8UTIz1Fr7gWS10kBZ5dMKzTamzWzkIdxWENokf06Vo0Q--VNn9dRjlhpwrbxHpM8gQCszAzQnkseMbmmj4hYRljX9YRwbIhRnMNsVBbRE10EwtcOP0qV0p2AJ6YEjsQU3hJl3coDCp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlHBrqGssGr08iB8wYq68MMMXZHbNAu8JyXxF2VvhPnhs1yPTQLnZ4pFyy3FpvUkaMFHQeQTWBjSUT7s65JcA6qztg17xThByP74AcHsQfdoC5jv-KAE1G9ZmnTr_VqKYMoUk85ZZUs21j7HL41IJ56q2txbk7WF1Mx8zm4STAewKi_SmfRWZ6yczIGfksfe8ncKyojJX1XH7ThS9wp6UCD1FkogE4UxP8epDlzMam5Br__Irbp8xNaHLDgx_dedo8gN4Arvl1ua7z8lFx8zPmbJoFJ1V8PYADn3ndwz19hguPrT9IjCn1vAwV5ot_KF8z7T6nEBNXBTnBA-FJfQqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=kWCPuCWgBbt6Vwy073NCfqw_zHCxm41wKRuShvyo1-pMOOV3azPZlsENHijWamLRuqxWq-qh_gwGphEHHDjvXlBoz68Pd4cx1FUmm0TuKPTjwfJzmsC-q-6MmKLlqEqr7110zD2xp0CgO8DGz_ZiSLqJRyLpOOJf37FqUW2kz5xCgdhWHQ0cTLmYRksWkJnZo0LKbOWkaKeLvKjTalxbnOGTbOHxYua6VnFbNj5mDU8PE5zCx2xd2Ok5Tt4KWZh0vKevF_10gJajcy6KuI_HeteotgirDFo8iJdjh19VOoJv6gSLbFhCY5rCT6qhOVCGDlGcG4nk8TcmrM1L3JfqsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=kWCPuCWgBbt6Vwy073NCfqw_zHCxm41wKRuShvyo1-pMOOV3azPZlsENHijWamLRuqxWq-qh_gwGphEHHDjvXlBoz68Pd4cx1FUmm0TuKPTjwfJzmsC-q-6MmKLlqEqr7110zD2xp0CgO8DGz_ZiSLqJRyLpOOJf37FqUW2kz5xCgdhWHQ0cTLmYRksWkJnZo0LKbOWkaKeLvKjTalxbnOGTbOHxYua6VnFbNj5mDU8PE5zCx2xd2Ok5Tt4KWZh0vKevF_10gJajcy6KuI_HeteotgirDFo8iJdjh19VOoJv6gSLbFhCY5rCT6qhOVCGDlGcG4nk8TcmrM1L3JfqsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=PYXgmeb5hFssVW7DWpCLGgLoRzIq-3CFdAH7GcarMGJueWNAd7fn-5IqSDg26V7EyErv0tdUW0dera-4f3NrnuH450bLs-_H19m3xfJFKr5GPoeS18gvqttpepnZSDzapv5KpdHKeOEBc1kt9BcQ79_Q0go_pieio_yR1vN4Wx5BgNUcJqV44riTVBN2wU0-VQhDzOKyQUISDGmO2n2RApIPKk6e_PeQjeKyir3xFCSkVv0FJsTYpQoBrPLBdSsDYdcrgFJ3Iw0aYsIfxYauLtCZoOmz4LF3riB4IAdmQsyRFyMa5GD2WB6sPEtRmByydMAEcmQNa1H16RLYMdMY4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=PYXgmeb5hFssVW7DWpCLGgLoRzIq-3CFdAH7GcarMGJueWNAd7fn-5IqSDg26V7EyErv0tdUW0dera-4f3NrnuH450bLs-_H19m3xfJFKr5GPoeS18gvqttpepnZSDzapv5KpdHKeOEBc1kt9BcQ79_Q0go_pieio_yR1vN4Wx5BgNUcJqV44riTVBN2wU0-VQhDzOKyQUISDGmO2n2RApIPKk6e_PeQjeKyir3xFCSkVv0FJsTYpQoBrPLBdSsDYdcrgFJ3Iw0aYsIfxYauLtCZoOmz4LF3riB4IAdmQsyRFyMa5GD2WB6sPEtRmByydMAEcmQNa1H16RLYMdMY4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1T4NFVrlQ0PUUGR1051t8D7JtTaT4972BXs8p2z8888M-QT4cmShepoGObEp3muUGtnmStZgW5mGAIaJHCf1C2k9Ci2_D7F1ITvyYqbK2btc-UrgkVPXfCxGR62wa3_D3W6m4KNbSzoVteGsxKf2-alzL4pWsJOTspLrUTi6AOAftiW6_iHtiDuNcnVOiOAMqVxv91x-MNwD8APeuISUlEAF9lOIYz1IahmsxFe4-woEC_PcPUjrmZQO3u2pXQMkpcJqcfvPC1sFy70IzP-MEM7k6RpVZJFSTPcFRLjPIK3uqHhGeCRGZkywtMbJMAmlI22c4Yuxl5ESW-j9zq4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAi-RS4iElL_7aqs6gD3r8aVD9FsjU3lighNdHrzz3PnEoq8QLhJKp25UH5hauLcZI5WeOpbgorIyv7fUCtKnTReZwZ26wK-SnIiCttSqM36ZOVLuSdiItmIuBFz9UsLYx8X0jf8VtJvSvmGSSvn8hlQREaHE_ZftsE6kfgM7ZD9oncHPORjSdxzj3MIhAzA3iOCR5PQfnsysyzJuhJH-VW11ZJtRkadacPzKFHkRqJduCr0pGy0JdLThWlLfRDtwa9FMzVsRS2PoSFlO20wcNqWtg4qmDCKX7Z7Fm1SpjImJsUbubkgdqhPX67L9TkFBxfNX6cWEXov7g4f3I86gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=lXsSOFvdnDWEk9eOzGBKlKXQpHWAd7ID5-X2_yJoSRTL62Tt712Pfv6sz6GOnHHQY4cdrBrcJRWLy8xc36akhTmGZSKZWTixp_wplHfsnku1v_72KR9FG6ja1X7aZPEpP7vBIfsri7rCA4FSbwvqyUBC-aV4ismlDsXXULF0HeEWPmOzIqyR5R1McWWlor9mZxQVvmBm9r0piVUKnuIZC-dRGbGCKzIBvoV7AMq8jJnCq6D2tCUoX3Bs9X-s1iAZ5aeMCtNpM1vtUJiGNeUEADozSmj1DU0RW2d65tmPEAqO4Ii5Jef6eQeqxeOcMEr3q_dqggU0H-6vSJ2kBfw2yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=lXsSOFvdnDWEk9eOzGBKlKXQpHWAd7ID5-X2_yJoSRTL62Tt712Pfv6sz6GOnHHQY4cdrBrcJRWLy8xc36akhTmGZSKZWTixp_wplHfsnku1v_72KR9FG6ja1X7aZPEpP7vBIfsri7rCA4FSbwvqyUBC-aV4ismlDsXXULF0HeEWPmOzIqyR5R1McWWlor9mZxQVvmBm9r0piVUKnuIZC-dRGbGCKzIBvoV7AMq8jJnCq6D2tCUoX3Bs9X-s1iAZ5aeMCtNpM1vtUJiGNeUEADozSmj1DU0RW2d65tmPEAqO4Ii5Jef6eQeqxeOcMEr3q_dqggU0H-6vSJ2kBfw2yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
