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
<img src="https://cdn4.telesco.pe/file/TrEjqWgMaauxzy-gDr05EfZ5RbaxYGAMpSrvwZZBsmVPwvLEYBin5bRqGy3SPlyiNstqtRrWxcZJc1fWfbzrXIyCbqqJ3TS6mAJlM5IvWeTfdNdB8cob5xrXRqwx36_VTpUpHqTE8KdrI4oZB8M8ZhyWQZqBnepPWCHRDXn-_ETiByDolgABXDzfgQHgcGE769o0zOZcvGb95Fzp0Gdstg0fJ2yx7aSpsITJ198uccPNQhw3JnFNfYONCVRaq1N0SFdOytNNdU9TgOQPuDCyC234-BNdMBvK0AN4vUPotnWltCA44xMD_dr2L4jd9wBC8UtXGUUvgUWqHhI0XzAQlQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 148K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 19:27:59</div>
<hr>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=RJX4lCMY42g8TQZvrtNXrpXe4X-iRosCsZjfUGoCO_nMM5U2BajoujH4acuj91wY5-4WQgI7oCZfE2D0OwMBoDDvZCjKmXr_tnNJgHqrsyEwtwZ-FW05fm87fwuXwKxpPOXMkXajXMS8_Z7_blULx_MKDynAmgtVksVKa9WsBPlWP0ezXzHo179jcOUKwob-HduxpkWxhv6dM1Qju2u_-Z4BuhUIZZ0epJES1Rh-tIK_SmfcxhJS7k_tkOqRCr4eNRsHr2iPMAq8UFz2xV_nPJILV2o2dvcZXmg_-pzl__KcFADbS5cIU6uMRgUtmwHak9IClUni9qvTuNltZckwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=RJX4lCMY42g8TQZvrtNXrpXe4X-iRosCsZjfUGoCO_nMM5U2BajoujH4acuj91wY5-4WQgI7oCZfE2D0OwMBoDDvZCjKmXr_tnNJgHqrsyEwtwZ-FW05fm87fwuXwKxpPOXMkXajXMS8_Z7_blULx_MKDynAmgtVksVKa9WsBPlWP0ezXzHo179jcOUKwob-HduxpkWxhv6dM1Qju2u_-Z4BuhUIZZ0epJES1Rh-tIK_SmfcxhJS7k_tkOqRCr4eNRsHr2iPMAq8UFz2xV_nPJILV2o2dvcZXmg_-pzl__KcFADbS5cIU6uMRgUtmwHak9IClUni9qvTuNltZckwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2PClXiEqbSsa_uWNN41_BXOSvYVF0ZXVYsG3fmaqUdgaLOwTUIKrbusCjqlHFKOq5DmNd2AOPfcIuNzVlxL-7ovLnn4ConUEfFTPIlVdwkDyPhR2eIxt0GkOW4qUcMuhGpE5TyWqMfP4Nbd9dcgf5sbg7Lo7rc52unwrpBC3m4ybO1n7LdTTT7SGuct-3w95nvAk9odHJEzmTR5pZn49Qf5kW_-PwyXnBKa4iHwByIxGyyxwPtNlgyArhv1ZzuHg7OTijTwEVkMsvCxGedwxcx1btkJa8W_dom8d9yvL9YQuM76O2l5r_LJOAk_j4vC5sEwev3bDsdqUScdz8YAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIPb0qJGxwRNcC7Trz290fARY-JVHJmo0Mb9N6jc2pqI94U6z1AXl7BkPzGV5LwOZnNIfLzCmrnX75aJw2RPMqIuVqYbERhXv-5mU9FAt3sXDYe6cGwqp65qkr0rStgGExx81hbR10e6p0g-L8mva2oaCsoHeeqjw955w-KYZ28MyC_d5zCPKabhyciHsm-Lw9QzHfeaYbfD8UQGf96lsSUafbrlkwbjFG3skOD-pnJpTBkzm6-eeYS4J0Yc8J2nghgMFZrduBfijNmYzLJ-bLmGv2PimvFXAl0xa1bNM9rLIdGTSJC8iQUAScY-9ogSb-JjjTG6H7MOUtlxOUkY7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9YXVOjBGwDqIl9YmkfmX9INKyq0dd6Sc5_B7FvRnN9W1ln1ATwDwk3rlvsKQNHb-AOTyfGdfAcxfcJgP6xSmRNNhGtMZKPkNRjJl0P7VIclsj9_hE3Y3Q-nrS8Q8fHWFyxJ9_ZDL6gL1K9KVVimXd5h0x6LlBtns68Hd6sG4z7uxsfTmJ5HvYBToBQY1LzvhmyrpYD_SI817AVGVJ-8cIiGttoKXu1c1q4XfWXbvRbMD4O_BcAPbW7Xu0K0CO_XpzVSgSnKKHjqfLPUr2s36P1NfhUkkGcOYT8wHHKpbyhFZEl5TqBZXL1R6PCCgGIiOsSNXa9sDjcPhwW7kZH7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=DAH77JyTyRlsfmkJ_B3SqBA2U3KB8YulZgrqRXWWO9LkMx8f0687Ki8BNrZY0O3oY740NXTwYK1UdoxHsLks8Im2GvI26ogJzvVDCvUa81KHkULfW0AjGH7YWhybl_K4koD3uYgGXwBxchrG5hFDc_52owELJ9AnNIZZ3rPFUATgFApWUUULOMTfJ1cbysw-en6gTuj9XFHHmK07iri_pRAoM3tpHhoRhdlazw-O7BgzEY3dmMM3FN2nhdmVsLDXJ_X5Vl25WhGR5x-N0QTZvgBE-FBmi_g7vRPY7UovmQslF12HRRy360yuIgwIlcWNJLyq0BpquJERzxgLUIIvsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=DAH77JyTyRlsfmkJ_B3SqBA2U3KB8YulZgrqRXWWO9LkMx8f0687Ki8BNrZY0O3oY740NXTwYK1UdoxHsLks8Im2GvI26ogJzvVDCvUa81KHkULfW0AjGH7YWhybl_K4koD3uYgGXwBxchrG5hFDc_52owELJ9AnNIZZ3rPFUATgFApWUUULOMTfJ1cbysw-en6gTuj9XFHHmK07iri_pRAoM3tpHhoRhdlazw-O7BgzEY3dmMM3FN2nhdmVsLDXJ_X5Vl25WhGR5x-N0QTZvgBE-FBmi_g7vRPY7UovmQslF12HRRy360yuIgwIlcWNJLyq0BpquJERzxgLUIIvsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=O098DWCZ1bPw3YMcuEQ5dMeHxaWfR1qq85akoLEEMbBcohaQV1i0hdFaAFhFCTUJ7GiT4DpjT-TbM1j8uVVFDPxVH9cfFKjz46coiR1s1YjHGi_PKYzrNImzrjud8Z6T2Nf9iAmGSWnak3u-z2GeLcHi0A642pxxk1cxNf7mYm3os9XpOGB2sYKQbjp_VFbiHJZljJtmxvhfiwXkbqXx6PhcX83TinwJOnIhfA4zdE_xLDQVv_-hICOeip_m2agHB_3GQpaPwt-r-wp8lAIbSzOrJbprjTVFyD05AIpSgOWjWBGubstfrzjJIk_qBH4kArAK9P6hfc6Y4hwZ3UjD4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=O098DWCZ1bPw3YMcuEQ5dMeHxaWfR1qq85akoLEEMbBcohaQV1i0hdFaAFhFCTUJ7GiT4DpjT-TbM1j8uVVFDPxVH9cfFKjz46coiR1s1YjHGi_PKYzrNImzrjud8Z6T2Nf9iAmGSWnak3u-z2GeLcHi0A642pxxk1cxNf7mYm3os9XpOGB2sYKQbjp_VFbiHJZljJtmxvhfiwXkbqXx6PhcX83TinwJOnIhfA4zdE_xLDQVv_-hICOeip_m2agHB_3GQpaPwt-r-wp8lAIbSzOrJbprjTVFyD05AIpSgOWjWBGubstfrzjJIk_qBH4kArAK9P6hfc6Y4hwZ3UjD4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puY_PXyNfAmJTYn_-G9TQ4frA80b4cSGIyGfKJ9ZHzVKYMFyN_UdPcswvkb5yc8-yi-y1-X-WSosXf_zWoXRN8aaVUFqrU1OMXRv7z7Zffg679YfhKUbUeQJnp9bT8_5SQjHzZWG4s7xRjoF-QJx_zToveNJ1tz1UH-Z8-JyiEfcdxy50iDjkC3hPpyTWqmxEDZvMAfWj1CUpU6kKl0v5wDvTZqoICI0Ov3qhlJVThV-6sv6f2puMZSjYRw7YIsYsaUqwzvwLmcftPOHriu66zIg_xyCTpywIJk-GfYxKJAJlQq2ASrj2FgcMrazbQFz7pUy9nNrS0a1mDcfcqA9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SZ10BblTmDg8nmJtTBcsz6p-Fjkz8_nH78mBogehhJ9zk6XrirWaneX7KAg3dw3HQaoxiNWVN85j_qm1XejlkJNOjmvTfa2_bjjAZVOLtlOp6mQqlpl6wFZl2n8rC5gKIw9CR_21KI6eMBMpXr1xx2DK3M_uqbPuj5dt_363AwxpCjkIxeTe20b_MfI1H5_Gjsjauuuu8by1w5l2BIPxXh0yQyhjKhYnA3vd9baW7dK_Ew4e8JRa_wF_icS1rXIUfCDrTWaY_RrUMieC2mM9xUUULOGHI_NJhf_utwYR_nOrM3WxD08UPKBXxlXidl3QYQUPmqhniPLsPvx6zdchOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBD604YOn2QEDa-Z8wYqvzA3_vgTTvCe2mHfJskdz_vKvh9pZCD01CSzhWrjcLcEitWenPQsNNhI7hz8U9s23OwnqKdUDfWJvY677qe3YnskCX1i_UAB4xNogPpL0D47YJByL_kHhFt1Hj0pjCZBiZ1i3s66_g7s1C7rwk8jzZkXifZK4pyjr00z07DPua-Ss3bN2DuAIjffcGXSd1Da_gBYBp02AMZa_uYfrA0FBNDsM4FHm2rfJ0rpqwxwmVeOPG7dSiN86-oXDhEQyZbYan8w5iSstDGgzwS6fzu88f6sSujbS3SS_R9G95Gkl-xeubqhGjcC56iBQgVfP3MFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJwKSdyBf6wW9w4SMf_s95Q5k45YrGZ-D6Kpx5dKD3kqeeh0NptosA6d-0g6E6KH5YQxlOrLGcllOeAVCJ9X9LKmtOHshkvCfAmzrwsTQNkTvGaotdMP5BtEyXYzZeqC0pGQZOofzUbKyjMS0ADMpCThgj1lZby0XTpsgOrXxBtNZbzyGB1opslw988wcO0xKeTC7tz1adcS1JlM1stqLnMiZ6TzkTgEKjB-ok1-NaxAdHXIGZPhu-0WqugMDs0Od0959jdpa46J6axc2-YgoIk1oebx8Hey0ZXzqOJq-r_StwM68GWQT86PuWhyNngkIp13n5P20KsCU_B0pK3fZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5eFKWVUFJu0j34tuUCALoknLdSdplxvFkcEpZfQJpNZhnw5x-O48aLfZkTk4Lj5_b0_uPjb1KyM-dPAu5zvxhaFwHSgsm1u8IzGPaNoVu4Y-wf6q0mD0cJymYRynhV_rD83CRXOGhie-nEYMXlCE6RpWQBrD7M5r9XdDmSYlWwLdCWOtTshOsK7L-fxAam81pQowGAhKG0xlVo40caco_e2yi4TgzDC9M9M8j51e6cXvv84BJR152ZMIuFSislV6Q8wvnOORcmGZ-wJw9dXiFzmoQc7Pe4xBsKUBkR3fly2VwmMM058YcDFU73cosaq_MtMDcSEojpirNJzkeqMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=YduwnEEs14zhFXoTxOBR1kjDIi87MX1AlgIS25dxt95wavhMuDHuGQkQ9fZkdHNC6Qjh-41SsAyLuCcr7ZVwxkqd_5aqGm5CCNkqW2O2Eu0Kg6I9YFiXCib4-NhSDpqiGCdYw1E9SgIepCleOBHg2tWKF1_fhQpb8YtFz9fMpa49M6bUqxpYYpkRjiimFR1QOqyPTBsmFhKnUBpf1sIW7H3darzvW2PFCqES20TUUrWVAm8oJvUShjiVXfnL3LBm1un6lljXTCNbavLmwSyfHgDgzO1sf8SEBvQ5fBasOTtpEKBWQ3cKRmeDbWkw0JznA8_FTo280AqifGB38UnTBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=YduwnEEs14zhFXoTxOBR1kjDIi87MX1AlgIS25dxt95wavhMuDHuGQkQ9fZkdHNC6Qjh-41SsAyLuCcr7ZVwxkqd_5aqGm5CCNkqW2O2Eu0Kg6I9YFiXCib4-NhSDpqiGCdYw1E9SgIepCleOBHg2tWKF1_fhQpb8YtFz9fMpa49M6bUqxpYYpkRjiimFR1QOqyPTBsmFhKnUBpf1sIW7H3darzvW2PFCqES20TUUrWVAm8oJvUShjiVXfnL3LBm1un6lljXTCNbavLmwSyfHgDgzO1sf8SEBvQ5fBasOTtpEKBWQ3cKRmeDbWkw0JznA8_FTo280AqifGB38UnTBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=rMa7kXJP7xaJXaHqb7MaV1godjC46PGgciJOxafyAo3fiHwBKQBRPbih7zF-Ko2CoU0koViEzKhTuFCTtL5QURphlBCDLgXvCctWyPjQ8xu4xyEQIEY5lqfye7cAItRt15wekGePTGhedFbR5Y-Uww09fNuxF2o0nCebQz8u8YnYXJ7cU3Zmr4Yv2VSzGEHWGMGpspKUN-ok7F5YHCmDAvNZM8pG5hpv-cFZk39H9td1L6XFKN73VLXc5wtjHVbmNMz7fQ-qBE_4KVW8mEUvDvltzlJ3TSno_jtdrBfblNr37JzNl4tsZ5tb2E4C4teNzOLc5GkSKl2S1aZ5aV3yeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=rMa7kXJP7xaJXaHqb7MaV1godjC46PGgciJOxafyAo3fiHwBKQBRPbih7zF-Ko2CoU0koViEzKhTuFCTtL5QURphlBCDLgXvCctWyPjQ8xu4xyEQIEY5lqfye7cAItRt15wekGePTGhedFbR5Y-Uww09fNuxF2o0nCebQz8u8YnYXJ7cU3Zmr4Yv2VSzGEHWGMGpspKUN-ok7F5YHCmDAvNZM8pG5hpv-cFZk39H9td1L6XFKN73VLXc5wtjHVbmNMz7fQ-qBE_4KVW8mEUvDvltzlJ3TSno_jtdrBfblNr37JzNl4tsZ5tb2E4C4teNzOLc5GkSKl2S1aZ5aV3yeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPACZaywg41I7qdV5c_coRTtAdzqzcKWhynfKHJ1ZTvui8QdbF3b7xSFeFQydejp18wPXPaIyjf6LmkFNUIGB7AOtPhnl6c0HqFfzfcmg9_TD7qhce8Amuw3VJg1YCUZ0iP0qNUuD1bMEvBfBlRN3kLY-m_O0O6rn6R8Mjg80c2R684vVOWnukDPsQR51ptC7JBGiw_8JaNU-k5SvihwKfX2Q8XPdE-kq6XRI5ZdYLOdwNp0wtdZWjXRmfAKr2PX8kxwzBAR4Kb_tJgCsptVw3t3sglS464RacsEmbgV1lHlUWKY-WYBWFlfyqzJuaRBMb-J5RK23KsXlFKIWhSsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rVC-oNC4e5V9viWA_53Z3sgm_ebk21oEpqJ4ZS0IbdXie_DpRmFBv9GfX1PV88w7sbF67C3a9R9U6zG80QUquqUGBM9UxJqoglCfO_nL0sOCCzwRMbe40FLOCe-jPAXullLMdb0kD8FwcGrkZGzRkZNvKFVnNaUOdfPv60AkoISSTZ5eZIOHPfKXuk1jrR6Nx7hQkRSnP_cQn3Dl22rD4m9LWlk2zp7gbdnv7pK4h1lDmxnRTYvt0RRPzctiBpQ_bciNgbJsmUJTVYFyxt1kP_2CYtYcXr9THro2vcjbXkfu50rgsnqLkwDeZQM-BATGYymqVzuacTU9-HEGMLl7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt6MVqDEgIczVpzbitjGtGablON96ehbWdnZp_uRq8foIOZK1CIcAA5VHmx6RHSIDp75ZrR-6GevcI952ROlWxiSlBr5BG7iQEmQ5Igx1mJ6NfaLjPgqQVCgNHZlgaph9QK3VjzIYGYeeLYK-pcfp1ir71IWWm6oWlFXN7Kcey-IqCVZHcu4joIfBzj0Fq9yUdQVSpURiyarfcLUkWnA4NvSD93bjoKxOQoDSJI66lhO6G0JT5ZbAFtO5liiOJ9YaXm9pfyzBH7RJDuiLP2a65NDh0RoPgnUbPE3pGCbWtCqeUl6Sno4xUCzUNoBqXkmXkJy5gmA1ZkNKuUKhfI3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5-4orRUxxKaKY9cznehPeMC8Fkyf0r9kI8OmIAhbA2DuyupQ5ojuczUslL4hGZO69x4YMpM4pEbLobqKxVLQk8Joi6SeuJm_xnRs1pWjiAfELVK7JKCoRPFESA1KmcA9VrWqhwaKUuqao-vsIiuFxCA7LmlWcm272uH0bsNdy1-H1v_5gCqUIXZeQgRGIXBs6GacVYept5YPPfe3ZP2gj2Ujf7khy2BMdtfL8U3HQaay78Dd-vWU7uKjMI18ukrFmYfInFxg0DKT9molDyFDIg3veBBoZbZj9tgxboMxfiB5x5UD3x21AR5kztImFbhpU8cfXA-wGVrCQDQ0vQBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=qGxJUrxs6kV3pW-SAfwe47Ur0KCDDa5gZpYmH3WMdPa5CpcajCRGqrpIVdNUJHFBMBbyaqPQ98Bbc93p_0KfJp1RYWGDnM_Nw6aGfO0OnjAYQ8B-oBOaCbCwhGYZbia0DmWMWvTwhRQAXt2D9OaUl1T7JoVff5Bwb-KXImfvhD5ifK2_k_7xiK93DwYbsKy15kThe7zEkf4wryt8aGcMOpROofAQ_IsLqnWND_IhmShJcBnhUVPiXr6BiyPjoFB2UgJhepTO1GljoTnVwhfWkpVUn7AlFp3UA3Kuj7uL6_6PUy89bM9j9uP7IGnrCbN75_s0u_FrRauQH0ZESQS-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=qGxJUrxs6kV3pW-SAfwe47Ur0KCDDa5gZpYmH3WMdPa5CpcajCRGqrpIVdNUJHFBMBbyaqPQ98Bbc93p_0KfJp1RYWGDnM_Nw6aGfO0OnjAYQ8B-oBOaCbCwhGYZbia0DmWMWvTwhRQAXt2D9OaUl1T7JoVff5Bwb-KXImfvhD5ifK2_k_7xiK93DwYbsKy15kThe7zEkf4wryt8aGcMOpROofAQ_IsLqnWND_IhmShJcBnhUVPiXr6BiyPjoFB2UgJhepTO1GljoTnVwhfWkpVUn7AlFp3UA3Kuj7uL6_6PUy89bM9j9uP7IGnrCbN75_s0u_FrRauQH0ZESQS-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyxr_grGrR1qR5C5EoDpAoUAOSiKdaK9Lk0dmbjrAKPVTeT2fTPkGIvX-CNcXKCQ-A9vuZiz3NSUzTkYxKiSDvGv8mPbox6pd3kpVD-M5BXDyNlwuGKkhYrLefh-xCtOOBVwhJB9ZRH7Oa8IBH-cNyo5h04lXigUnm1YB8cn9oHaTlb3q_4qtZ7nfi2FoSCZlhcDthSDuRAyQyL0KYWrQ2S82lpmL-Bf4lyLoS6T2MMlqzEmLowgc_ywlcFiWVv5lADpNmI_Rn4LL_WwoEVrU1Bu1AkqdsHMW-jkF1skHch9zrrp44pLv4OLULpvrsKRMVom_NuzMa8RO6HfRGph7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=NTd_3I6ydasQ-Ta0ltuIohaXWue8dYbNmG10N3IXxst3BebcBfY7qLjobH6AUpdP8PF9KvCLlL22y3A9oe4N7DiJPerYPdDjI_mZeWQW9yVBjZTYFmFG1K7nTPVgISxKBIjVcP00V-2VOKFBaJhkKNuEBI5MSNyPR10IbRNVTKfHYOxHnD-pqb47vGuHGuCap5oRcIxxtXzaTezn8MCF3U_gj9-4L4j1_GNpzgYlblxAXRFa3-xH65YukYj_BzQEEz8Qx9H6TcIQFrgFhnHqckOKXObtUulCnzAV8na1ePuGEdhY5bgbpU6a22z-jw1TRbdfzH-nyFiR2N1BbMQ-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=NTd_3I6ydasQ-Ta0ltuIohaXWue8dYbNmG10N3IXxst3BebcBfY7qLjobH6AUpdP8PF9KvCLlL22y3A9oe4N7DiJPerYPdDjI_mZeWQW9yVBjZTYFmFG1K7nTPVgISxKBIjVcP00V-2VOKFBaJhkKNuEBI5MSNyPR10IbRNVTKfHYOxHnD-pqb47vGuHGuCap5oRcIxxtXzaTezn8MCF3U_gj9-4L4j1_GNpzgYlblxAXRFa3-xH65YukYj_BzQEEz8Qx9H6TcIQFrgFhnHqckOKXObtUulCnzAV8na1ePuGEdhY5bgbpU6a22z-jw1TRbdfzH-nyFiR2N1BbMQ-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=UReSsdS9PqAPfYQ5fJvdQaxYrVebVDyOhijaCJm61YTYbWUTEvLkdQKrb1XV5727NlGW4ssuWR1La94P5z3ytvZMXR657rVB_eOMXjTKecAsGUySUiugZIbVSEaOhORXwMCBTHm9R0vErws-AjLYQqrh1FR86tiz6qVSyIV5MpI_6AMSb9dpdr5B4iHVZO8ucqnqXCkWG-Zv-suQaR4j18Sxu8uy_DCn1tKb9SQkqVLyorEsWhzcVacygqfl-9Q2WkeYB7C-5vlKO4CAxvbSSPsEl9rBO9vRYZiGSoZNquLDsUpKsHDN2hBHJteR_jUdUio1T88OL_4xSxtmrG8FhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=UReSsdS9PqAPfYQ5fJvdQaxYrVebVDyOhijaCJm61YTYbWUTEvLkdQKrb1XV5727NlGW4ssuWR1La94P5z3ytvZMXR657rVB_eOMXjTKecAsGUySUiugZIbVSEaOhORXwMCBTHm9R0vErws-AjLYQqrh1FR86tiz6qVSyIV5MpI_6AMSb9dpdr5B4iHVZO8ucqnqXCkWG-Zv-suQaR4j18Sxu8uy_DCn1tKb9SQkqVLyorEsWhzcVacygqfl-9Q2WkeYB7C-5vlKO4CAxvbSSPsEl9rBO9vRYZiGSoZNquLDsUpKsHDN2hBHJteR_jUdUio1T88OL_4xSxtmrG8FhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHy4AnHq1Cu63drzkb1fbUvtFyg58m6RxbM6H455F48n1xok3nF87hmXOYuziyPtL_0FmlnVDd7yRJZ9RGoNti7xOm07Gkm8zk6MQMx_sIzsSSc2IKu6dYf70_e8x293DVq-QR4pJUA3AoPCIYumkVcx4YUIttHq2ceWnD25UeqguDd1mLSAjqqZHjw6IRMa28UZk6IEfyH1_OOr31V7M5KvmwFE43wPQKs92T2XyWpT-Cga4-oA7VNOCCIDoDbDGUBuW2koxQjPwxO6Zxi7GA7rNzVQL1PvpB72b6igd6kLq1Fr3aheVSbux4qkqIgeY8r9HYGR8GzW9FCLwIM_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/emhLBwHozoh7MBDKG3SzBrMuRlb_LymVWt9mq0u1DfqpyJNhmE6FROFhf5Sh4gFILaUatgKPG90xQsRXXzMv-eeqAtg135J2khmeSHOkRucWXDaceQo6RIk1y-Mwht-UkfZoyU0NVXkSD6VJ7TqTmjelRsznrJ1IK_8eBV_ZZIl4lqjzoZOlbw9TUjVXEdoqFjhEFcTnnBIexZQHYCf9CiylJ4yJhBisHrzI0MVj96PX4t5nsFZrpVINz1-rGKd6C51p2dzfP3Ay6OyB3Ew8q6j9Z6WAYQfAjJcRlJu8-xTlVdMGlZcePlJMuWTZNTuyjY0GKZaA3sKs2wVAvv7q_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=PGGRLdEFzKWjulBBaniEdG-bKMp4SAfI9IFwnI_vQnFCsVdPSedC1zyDdVDlKpfnS69Q9_tPigpwC91jQXlqngA0ruzb3PMs4-oSBVSmSWUFN9WBwNqEowJWRZCKydYXWHG9g5_I63Ayddfo90tKnKyx2aLy9O-SzdJQkHGS1MnlmWHxTKclQ7R-oE-KQjGOH-xVOzYwiF8N25qfGYO7utfxRmgxtanHwPfBqI7xJUMCZUbD_imTA0EnsAOp3QP_keIXZMyslr1QH9EEVMHNjae_7gMwhZMRdz9cEhbbsT8y3Ku7d4-fyqSFMYz6cBaDOZSQqnwuKgA-D0hPokFlLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=PGGRLdEFzKWjulBBaniEdG-bKMp4SAfI9IFwnI_vQnFCsVdPSedC1zyDdVDlKpfnS69Q9_tPigpwC91jQXlqngA0ruzb3PMs4-oSBVSmSWUFN9WBwNqEowJWRZCKydYXWHG9g5_I63Ayddfo90tKnKyx2aLy9O-SzdJQkHGS1MnlmWHxTKclQ7R-oE-KQjGOH-xVOzYwiF8N25qfGYO7utfxRmgxtanHwPfBqI7xJUMCZUbD_imTA0EnsAOp3QP_keIXZMyslr1QH9EEVMHNjae_7gMwhZMRdz9cEhbbsT8y3Ku7d4-fyqSFMYz6cBaDOZSQqnwuKgA-D0hPokFlLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=oYGK82kHHZk373jVberZ0CbCZqPOZ-EAFe7gQTwMeF51FJrDV_uI1eZteUszodH76YL3IH6n9r_UN2HLFWPULVoCciAl92CJ0gMNhJ68Aj_1gZfWGPXCc_vD-4LWxvUwUaBHhNGgSQJ5u10Hu40ImUidc5EDSVca3vcdVZh7M44imLNjdgYuFRwYz5HRTtJ1LlGGZtmz4AxzbhtzsaMHW9WZB6EIq-bhWHYGQD8osWfEHSu2zJcpyxhk1INu0lri5Z3ctan_Abi60u3db2vxa4t47IV7phybCqPV-6UFBFnZ2CVqqTMyMHn_vzLUX2-sED2SMLJN-u5jFc5Diuh8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=oYGK82kHHZk373jVberZ0CbCZqPOZ-EAFe7gQTwMeF51FJrDV_uI1eZteUszodH76YL3IH6n9r_UN2HLFWPULVoCciAl92CJ0gMNhJ68Aj_1gZfWGPXCc_vD-4LWxvUwUaBHhNGgSQJ5u10Hu40ImUidc5EDSVca3vcdVZh7M44imLNjdgYuFRwYz5HRTtJ1LlGGZtmz4AxzbhtzsaMHW9WZB6EIq-bhWHYGQD8osWfEHSu2zJcpyxhk1INu0lri5Z3ctan_Abi60u3db2vxa4t47IV7phybCqPV-6UFBFnZ2CVqqTMyMHn_vzLUX2-sED2SMLJN-u5jFc5Diuh8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_TTu0SaMD9pChAzobqJKleNMT3TYcikkPAYjNhDipoZ6F4p8rDr8Z-ijNc_Piz3458fqLN1PPH19CjV99e1WjBckSFNtthKF7jwA8YYr5IhE6egQetFBC9Pivj334qT7gv_W_RxgExpIc45AJ79Ap4CM6RZ8FTkXFSttMMxRev96fSBSymkyEybtA8-PReHn09FGp_yi9Yk6pEFXekXS22nYn1g8kGh3Ca25RxM7K0OhdTz7S1RaiH7wzSeupdpR3QcltaGPIiR2X8WS4hILERexGl5kKUEJLAOj-kV1dtZ9tax29MEzYVBCmROtOPyjda6SXM4zBApxZMI2CGyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul-JiFcu8quUFacsZ18VAdenER7zjaR0iOAHXIxjCpZ08MxtKpV2Ef4zAveQwMQ0jhZRrH504ijUC4p_sq2u6BXOzgQ_yM4w9OovbKjEhxKKJVjqcNX2IC2d4E3eg3sE6nyEZC25ef4SVdzdvsMABRB7HM-zQzzaU3jZVLhjIpxGzvNzrxUvQlxtCKJHbug35ZwKiff2QhkZJ1oMA4m9WVlIAsNj3UJWxbhOKUU1iASVWFddZTqsCtqpccEIpFY344ilvFp6E-bNklIBfyQAVOsxDQtGO9JSajjtzRwh6d99q-wxCHwFKnyvrcMxz_Ody3-ZhqexLH_0BozWxyMjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8hPYBSSgulcpwx85djs33ju_K_o1jKmG09sPj0kuoI0SVaaBp9-SVETBA67D8DmwGjDN8mGRY8ZitTSX9CmarlbMSiLl08HYO_KVdcTQV-AnAzl5WupMQgpsi24jjF93x0spNenUAiguD1py8ezD_3CSsD5W0umKQbVID4RV5MjeFzIEqaFd2AjDNNMeuibawRGNE40M4o-4ppG2vb4hWvPpVBwB8rnYwsaudOu-cVQnHV5-B5NR7SmhVB4hJw-sPkgVPYVQ4VItsmsF5MWgS6qhbSWIVvjXIEbYWS5Asgjwlh84N2BIB-cE30krd2hL0_0rWLpmAbycFMkqFHGVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFHwYj2i3HwkTmU_2avdlyTjEUwhtOf_VEIZsQMsneVGnvMTBUlqGs2-3pwUiLu6ArccEKtOfVDc0SRBmuJh1MY7I2VUaU3rEknQjDdbdru2WridDiUFa7ciIDkFsns1ACUPGCauBQ8Fn4ARCSk5aCdKjG_eMQAuLw4pHVWBMWOuZxgR6MCMttRLp2kaf-L9oLgM7VLU4YkyWozL0qKdnQjmxEXBcgrIcN1weGayNglm81bytv3ay4awPz5-ebR7YWR_BgBRNzj_1n4vbEE_y7ISg0alTAThIloMqD9veHY-hlOCXWXEwVlK1oMwxfQQps0X2f-L_wz1_o_DuhwbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=g-G0zNIyl735zTkhWZT8N6O7iAUnn6Pl5vajnIdz2AoMTjdUXuMQky5ryMGKS91DrGGZ720ubhyDKuEnEK471mytVoWaCi-9rgae4aVfGMY12trT_V97KHLCMI40adLJvS0RduUn95Tx_XD6XeyeODgJ94DOkEvrdc-H1GdnXGNgZM-2pMynGfY6DT_MlLh5uOMgf1qPR363Upl8NO4sE5xIX3DNlDWwAIPiY7rcE4ww8HJ6OLMnMiQRckM_SxN9shvSUYcYrtBh_9liHR1qiBkUK3DBFU5i2hd187faj5VrBBWJOJSIf71Oj2QrX9jFoFDyjAZ1uSKp_YGfBBOjQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=g-G0zNIyl735zTkhWZT8N6O7iAUnn6Pl5vajnIdz2AoMTjdUXuMQky5ryMGKS91DrGGZ720ubhyDKuEnEK471mytVoWaCi-9rgae4aVfGMY12trT_V97KHLCMI40adLJvS0RduUn95Tx_XD6XeyeODgJ94DOkEvrdc-H1GdnXGNgZM-2pMynGfY6DT_MlLh5uOMgf1qPR363Upl8NO4sE5xIX3DNlDWwAIPiY7rcE4ww8HJ6OLMnMiQRckM_SxN9shvSUYcYrtBh_9liHR1qiBkUK3DBFU5i2hd187faj5VrBBWJOJSIf71Oj2QrX9jFoFDyjAZ1uSKp_YGfBBOjQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کشور عراق، تلگرام رو رفع فیلتر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64839" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏ترامپ: ۹ جنگ را به پایان بردم و در زیر دهمی زائیدم
@News_Hut
#Fun</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64838" target="_blank">📅 16:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64837">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adrR3yRs3wu12A8nkY6L7D6rhAoJ3vCC1zYehzXrFjeiVoTsMYx-N4YGlympzbBuLQ2RpkoLZ4X9Mm4USuTFjlCGdy3CayGIrlZKr-U7u8ciRun_VwUIhAELQIDzqfuc6oWSSgIloQETpA7q0o-NDnWBAEv0l80gAmypTEIdWgqmtlPApjb2vrtGnYUyEGuA4R3CozZKIhx0DS9KeRvBySLw9HXWCXZ1G0BfrA09EguTW0C2SCys_J1t8r4hsYeqbVQpr-5fVMtN72K6iiubgpNaAh630cxRFOurJMQW3RG-TUEz_Lt9dIK-G0gO8rRObK6QOocXJAnL5tskrk52eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=twyxWR7Xn0d1Wv53TWcxK_cuplBx_GsDQcYkj-Y6sPSCxzBu0RqdVrzb1oZRBCJmv_3BiLTSx__72AABqn3pvoe_yF3So1_JySM2yfAFr2mCvMUmFggHMSQdu1OI3kblhEFPbXlDk2lhKUp54GmBv_eASRCfOwSR_IcdaZS26tM7C-ulY5rkWZ3EgPAKRDIcum5Y33O3BbnVg3w0bvoND2Zav_FFVGLHr8KO_FZADZLITrOgdj1pSrNeZEiCPSwlbZggiADt13xM0oet_AjZyLQZA1kO7GwZCaft8yrvgKTvZREsQYpdZM3cewqJgvsSQMwCGpqjMGAZcENlFwfzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=twyxWR7Xn0d1Wv53TWcxK_cuplBx_GsDQcYkj-Y6sPSCxzBu0RqdVrzb1oZRBCJmv_3BiLTSx__72AABqn3pvoe_yF3So1_JySM2yfAFr2mCvMUmFggHMSQdu1OI3kblhEFPbXlDk2lhKUp54GmBv_eASRCfOwSR_IcdaZS26tM7C-ulY5rkWZ3EgPAKRDIcum5Y33O3BbnVg3w0bvoND2Zav_FFVGLHr8KO_FZADZLITrOgdj1pSrNeZEiCPSwlbZggiADt13xM0oet_AjZyLQZA1kO7GwZCaft8yrvgKTvZREsQYpdZM3cewqJgvsSQMwCGpqjMGAZcENlFwfzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64835">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
ترامپ: می‌خوام کل ماجرارو تموم کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64834">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
ترامپ: خواهیم دید چه می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64834" target="_blank">📅 03:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64833">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مارکو روبیو: متأسفانه، تندروهایی که دیدگاهی آخرالزمانی نسبت به آینده دارند، در ایران قدرت نهایی را در دست دارند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64833" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGDO0dYa93ZBESdm_pCPxsdkzha3RRHDtSunnurJXEl_S7dSK_4fi2ooxO5zVd_IBC0RvYb2gi3XyKBFdrztitAbbq-9n7Dwp-1-ar-OVSmp_I1hCQSovQKJoUI7cELDNIrR-8avpOHeUFQ3Mh21UD96-xwjrP47TkyAS4Oss2xAIXYivSCqBNixiqQvoOrMNonCPq9hy-70Wq6JgtpFPzavgsS-c_Hjz3676eQVgJaGNYu7kkJSeg9QJ7s54D9Oz17I6oN_u0m32M89BnXMMB8Ggl6Yb2sTYFZUzHI2WQm6Zb8LBu3x7AK7PA6NC1ZGhGAY-qJ6i-r7OA2FOFQPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFC7uQbdcoIHI_VRH9ddQDNr3JdjWGXUr6QQ02OVD6EkrsZuloOwLqOzYW6gHTT-5ABsXYZhVEfvBx5jicZh5z3ypwNgnkrevPGYZznrc79P6f6C-oOdKKbhFeJDBHhqkb4AhRdIgj0bQ02td1i1QEIHLSzN8lbL7Npf9NGAz7f2lzi72O0n2dqzY6hmqZX8uWQ-QdvrKbHowdYviGd9ey5zt7XdqshVd13hLLv9GUDA14U1ZAOs2uhx6Z4unpmAibG5b2vxYlUIjfHVMCB-w5p0wbzKbPFOzJj9g0vVI99mE1r3eD0JE_DmLWnB-y6LNHDN99JgsCFbdVv4ZV08Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cawyCS6RRAsF4Jd96YxeYTDU8U8e7EBrvawYpPf7J_VMRCVQtkA40wfrhsobO6QFLBn4h88rRoIeJNz8711lJtQFLe75MixiGJU4c4Yq0JjxOevbrtZjNVMrqjJo1BLBd9zlzZgMAhOg-n947LQO9a505sUGAChZYOTdw8Piq0esX04Zl48m9jDjQ1-I-vp-D1uHzAfwcN2PmCS59EidaJfam5tjP0mtuqE5d783gOFjSBNYvoQdXlzI2_cyg3GumJsjpymyO4ZYNWYa2zWoiJ6mbjZAlDhQgE7KvuCwBQHCeWVwdDtqwF75OmjxXKoiRIlIOhhiKLnq8x0I-_DeWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQDLoJypWtFKJ65jDM_F_wNxqGY13VinEVpzUhIy2krilkxFr_Iafg4lLvWqSQlKISu6M5ZEkggWuhUvJjmhJBRRBbc5_EplXQ1xEvcui2wIYjOURCBXvlXIL8blBp2a7GoN4w4KoT6qqEgOm91MFPu6sR8hydytrCX0kNK-UIwv0P0Grg8PwfQ90mHiKt1aC8mo43zwrAJ19exk_QgUFvaa5LwxITZgh-FPqkJFxuQYxBebqw6YXQP7qSLfzY53j-ezFmGCA1YAKxmbmMf_XoUcB8DSIa9NX3AUmf55679M2Pz1Yl9DkiAQK7uwLWV6HughQA26KBemR-pMKdOCdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فشار جنگ کم شه
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64828" target="_blank">📅 00:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64827">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=LvK22qcl2IhM79KCOCVdt4SEXSPyFNZVrT5ibv1V1xEk9632xFSfKuS7LP8tvL3RYJuGgJ3aOhKuRpNU0Ak0Lm2fTojd8Goidry0bJFyTaO-3zkGT2uMlXUK2wasbeEzpQOHpCdN39xEoSOcPLE9rKBYm68zLnHCuHIZvKhjlAmx04rvLAOscrL_83Am2QpIZkigYVY6eFmbQkvVmMxpDTxmCI5swbu6bSLPmzDkaIeYOtHC0940RFppwV7VlYrihVbJ9KdfpAWObl2W2hP7amvtwiqngk_8eNF-ufJqITjsglRntjoMagLbAbSxeLDZhhHaXM62XeioAi0lyLiJMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=LvK22qcl2IhM79KCOCVdt4SEXSPyFNZVrT5ibv1V1xEk9632xFSfKuS7LP8tvL3RYJuGgJ3aOhKuRpNU0Ak0Lm2fTojd8Goidry0bJFyTaO-3zkGT2uMlXUK2wasbeEzpQOHpCdN39xEoSOcPLE9rKBYm68zLnHCuHIZvKhjlAmx04rvLAOscrL_83Am2QpIZkigYVY6eFmbQkvVmMxpDTxmCI5swbu6bSLPmzDkaIeYOtHC0940RFppwV7VlYrihVbJ9KdfpAWObl2W2hP7amvtwiqngk_8eNF-ufJqITjsglRntjoMagLbAbSxeLDZhhHaXM62XeioAi0lyLiJMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی مسئول دفتر علی خامنه ایی درباره مجتبی خامنه‌ای:
خونه اقا مجتبی رو زدن ولی ایشون تو راه پله ها داشت میرفت طبقه بالا و فقط موج انفجار بهشون خورد و افتاد زمین.
فقط کشکک پاش و کمرش آسیب دیده که کمرش که خوب شده و یه خراشم پشت گوشش برداشته ولی الان خوب شده
مردم صبر کنید دشمن الان میخاد یه فیلم و عکس ازش بیرون بیاد که کارو تموم کنه به وقتش عاقا خودش میاد باهاتون حرف میزنه
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64827" target="_blank">📅 23:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoFu0YTcBKaKYG0zpSsGs8bBqwC-cV3Haia_1WVKValjmiRgkfdkVDStZ24qqe_Duqs1M87YnyqmhmZkRqHaVjnkkTPt5nLieoZnpYw-HYQEir-ngyYm2Dw-prfjLE5zhP0QpvL1KY_zTzkBf8quz0K6Tx1OViS-XOgYolroYppaDakhh1p30dfH1x0EafUuVOVA0spbdu4brw2nwuBAjmpy-5UctvQjRtT6a0QmHc4fLAG7EAQIPDNdvs-RN6rB91lH96C00VttF82O0mi_ERZLKie4t8gI-zfXb-EPzJlPOyvca_IgXMH9eiXodRQL2n8X5JURvQck8hAPwGxhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ ۳ روز آتش‌بس بین روسیه و اوکراین اعلام کرد:
خوشحالم اعلام کنم که آتش‌بس سه روزه‌ای (۹، ۱۰ و ۱۱ مه) در جنگ بین روسیه و اوکراین برقرار خواهد شد. جشن در روسیه به مناسبت روز پیروزی است اما به همین ترتیب در اوکراین نیز، زیرا آن‌ها نیز بخش بزرگی از جنگ جهانی دوم بودند.
این آتش‌بس شامل تعلیق تمام فعالیت‌های نظامی و همچنین تبادل ۱۰۰۰ زندانی از هر کشور خواهد بود. این درخواست مستقیماً توسط من مطرح شده و از موافقت رئیس‌جمهور ولادیمیر پوتین و رئیس‌جمهور ولودیمیر زلنسکی بسیار قدردانی می‌کنم.
امیدوارم این آغاز پایان جنگی بسیار طولانی، مرگبار و سخت باشد. مذاکرات برای پایان دادن به این درگیری بزرگ، بزرگ‌ترین از زمان جنگ جهانی دوم، ادامه دارد و هر روز به هم نزدیک‌تر می‌شویم. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64826" target="_blank">📅 23:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GperH77V-bJ8zN_clqXPzbgEsvsPKVMonKR2PhD5dq3gQkOPalwkJPlEy3Veh3GHvbjNvokHIJqZI1rR18kcSq_b2_0zmzVhUa1OSLQHM80cxsAl0f1dKGzggouLVoNnGsEpOpJr2TcrIAlu2NjxS0wbg0NL3xsZ9FAn23WDaCiu-Yf_qx1xblNZH7TKvh5fTm-1N-kdL9hr3Ci_2B9lLrvOKw2QPAwZmq26UUaQYvODoIpapDuzQ6-mNTWkj6o21wlLARYnQL7qDISSoMV0NxfGVH-IhCX4FFRdiDxItXhN4dzOVVEXl_icaQXxcNlqulMF_AyZcigfbUGHN3V25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
در مورد وعده من به شما، وزارت جنگ اولین دسته از پرونده‌های یوفو/یوآی پی را برای بررسی و مطالعه عمومی منتشر کرده است. در تلاش برای شفافیت کامل و حداکثری، افتخار داشتم که به دولت خود دستور دهم تا پرونده‌های دولتی مربوط به موجودات فضایی و حیات فرازمینی، پدیده‌های هوایی شناسایی‌نشده و اشیاء پروازی شناسایی‌نشده را شناسایی و ارائه دهد.
در حالی که دولت‌های قبلی در این موضوع و با این اسناد و ویدیوها شفاف نبوده‌اند، مردم می‌توانند خودشان تصمیم بگیرند که «دقیقاً چه خبر است؟» لذت ببرید و از آن لذت ببرید!
war.gov/UFO
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64825" target="_blank">📅 22:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
چندین تصویر افشا شده دولتی از اسناد بیگانه‌های فرازمینی، پدیده‌های هوایی ناشناس (UAP) و اشیاء پرنده‌ی ناشناس (UFO):</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64824" target="_blank">📅 22:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=Er6dvlTv1wB7VqTffag5IUdLm0zuzfDLPrfnEW76SUZj35GkBCNsmtR8G5lCosGNm6Ol7jmc8ZWPKd0XLGbJUj-Pz6B1e8SVsT2kMQz6NozmO_a6sYHCr2gzFASZJOAcoWEu4JF47Ajv0bAfKyHbAAtJZUPEO4KioGFZ-f4dUUbf_XVemKCKVjuWtq0u7r7bwrkDq5NSAQTMWtd5zLui32lofb0KSKuRhurqDMqT75CnDh93Nc_cE1xzSNIFQJtGVoy9hqbJxjccEGbjXBAgDrWKDC_b21nl1VZmmAAwUPSi43eGoB-lMsEezFefzjG5e7urc99MlLcm2tHhtNK-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=Er6dvlTv1wB7VqTffag5IUdLm0zuzfDLPrfnEW76SUZj35GkBCNsmtR8G5lCosGNm6Ol7jmc8ZWPKd0XLGbJUj-Pz6B1e8SVsT2kMQz6NozmO_a6sYHCr2gzFASZJOAcoWEu4JF47Ajv0bAfKyHbAAtJZUPEO4KioGFZ-f4dUUbf_XVemKCKVjuWtq0u7r7bwrkDq5NSAQTMWtd5zLui32lofb0KSKuRhurqDMqT75CnDh93Nc_cE1xzSNIFQJtGVoy9hqbJxjccEGbjXBAgDrWKDC_b21nl1VZmmAAwUPSi43eGoB-lMsEezFefzjG5e7urc99MlLcm2tHhtNK-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیو سنتکام از حمله نیرو دریایی آمریکا به دو نفتکش ایرانی M/T SEA STAR III و M/T Sevda که سعی داشتند از محاصره عبور کنند؛ این دو نفتکش پس ازحمله متوقف شدند.
این دو نفتکش تلاش می‌کردند در یک بندر ایرانی در خلیج عمان پهلو بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64822" target="_blank">📅 21:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
📰
فاکس نیوز به نقل از یک مسئول آمریکایی: ارتش آمریکا امروز به نفتکش‌های ایرانی که قصد شکستن محاصره را داشتند، حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: امروز پاسخ ایران را دریافت می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64820" target="_blank">📅 15:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcRAGzGbkxUzteP6h7Xhi2tXcyfDiqgNhZwRL1edcJG5VuhapkaJruhauLLbi16vFVDpsyTbe_9o35a-z4gE-8WG3cK5yuq3Y-HVSKBbm7waY1-6FtKiEzkSc4GHhTT0QeSInouR3HQo-B81XkC-KfllpvjQU6-LtamGwONwzW9hxn6CV7yD12Hoye9zHUrnwMO0rr5WaHm4o2o2_5QMu3UyMNYZbqErEsmiROjAEugQt_kOT_4DDQHrKYJu5Lg9l1IjD9CiH-KOZlQVHxGKmmOop8PZNkJQpI6WLwqSk0iOqJbnVU5DZVsBwKVIfLRRZmXoNUvLKq8epQnGUR3z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات که نه، حتی اسرائیلو هم بزنن ترامپِ کاکولدزاده وارد جنگ نمی‌شه، چون سفر و دیدارش با اون کیری‌خانِ چینی براش مهم‌تره #hjAly‌</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64819" target="_blank">📅 15:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده  @News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64818" target="_blank">📅 14:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64817" target="_blank">📅 14:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">باورکردنی نیست آخوند ۷۰ روزه که مردم ایران رو از داشتن اینترنت محروم کرده، چقد شما حرومزاده‌این که دارین رکورد می‌زنید
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64816" target="_blank">📅 14:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=dOAaBFRUsA8rIpGQetS1U9mSijpSL9YbvT7heZZERD_nfrKkcG8nGUUOia9SStI2-K_MWmwj95AhtzTYvIFwAQxkKMnNhAO77mGbaT58uDbj4AdP3Y1FxGA2IhefYcEQQiAmczSAK4gpxNoc_7Z2I1Io4JUsRILwtclGY2FMwtsNfW4k6ql4irnKE2EcYa7Iy5ML1LGXHwec1vNyt7C8zoZXBWhmkNidGR0PemLB2uLsxEkgW6Sp9zr7ZDuXMbvLcjbSJSwNKnX4YkYj6sbkCxsY6wFOpziUsC0-lzcbjSfrWZF55J4DNf44ixaV-5kTgM2al4PLf84iThaxYJBXkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=dOAaBFRUsA8rIpGQetS1U9mSijpSL9YbvT7heZZERD_nfrKkcG8nGUUOia9SStI2-K_MWmwj95AhtzTYvIFwAQxkKMnNhAO77mGbaT58uDbj4AdP3Y1FxGA2IhefYcEQQiAmczSAK4gpxNoc_7Z2I1Io4JUsRILwtclGY2FMwtsNfW4k6ql4irnKE2EcYa7Iy5ML1LGXHwec1vNyt7C8zoZXBWhmkNidGR0PemLB2uLsxEkgW6Sp9zr7ZDuXMbvLcjbSJSwNKnX4YkYj6sbkCxsY6wFOpziUsC0-lzcbjSfrWZF55J4DNf44ixaV-5kTgM2al4PLf84iThaxYJBXkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دلیل اینکه عملیات “پروژه آزادی” را متوقف کردم این بود که رهبری بسیار خوب پاکستان و رهبرانش و فرمانده فیلد مارشال و نخست‌وزیر در این موضوع خیلی عالی عمل کردند.
آن‌ها از ما خواستند که در زمان مذاکرات این کار را انجام ندهیم.
اما اگر لازم باشد، دوباره به آن برمی‌گردیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64815" target="_blank">📅 09:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64814" target="_blank">📅 05:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه  @News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64813" target="_blank">📅 04:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64812" target="_blank">📅 04:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چالم کنید جاکشا.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64811" target="_blank">📅 03:03 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBmmIvTs8kFc1HXYkiJofNWxpMSD-fEjwTvzp9VqYT8WLYR4l4evzIsRsWTHq9HA5WTqMKADZahRQirp56JMHIt7HojcyIap9tZA1qGRUwXzfxZjI0ulXlHG1-WMM9BjXJeYAOH64Tf7CUkdDjaRSZbj-gekqDTw_xcEGs6V7j5uSNG6If1VtGgyjz_MnGwjDYDoCtL6HXEX7--Ze363VPa3SZXUm-taMsT9KfjdjcfDdhjYijtsMhs0YufWy6ti-0REq1-bMEvqikHINljTHiq4NchK7KoQl8-AVlJr61lwoYRoYE6YnrI5vmk3tUBHdGslealm502HNZtZjbMauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
سه ناوشکن جهانی آمریکایی با موفقیت کامل از تنگه هرمز عبور کردند، در حالی که زیر آتش دشمن بودند. هیچ آسیبی به این سه ناوشکن وارد نشد، اما آسیب بزرگی به مهاجمان ایرانی زده شد.
آن‌ها کاملاً منهدم شدند، همراه با تعداد زیادی قایق کوچک که برای جایگزینی نیروی دریایی کاملاً از پای درآمده ایران استفاده می‌شوند. این قایق‌ها سریع و مؤثر به قعر دریا فرستاده شدند.
موشک‌هایی به سمت ناوشکن‌های ما شلیک شد که به‌راحتی سرنگون گشتند. همچنین پهپادهایی آمدند که در هوا سوختند. آن‌ها بسیار زیبا به سمت اقیانوس سقوط کردند، درست مانند پروانه‌ای که به سمت قبرش فرومی‌رود!
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند، اما ایران یک کشور عادی نیست. آن‌ها توسط دیوانگان رهبری می‌شوند، و اگر فرصت استفاده از سلاح هسته‌ای را داشته باشند، بدون تردید این کار را می‌کنند — اما هرگز آن فرصت را نخواهند یافت و همان‌طور که امروز دوباره آن‌ها را از پا درآوردیم، در آینده خیلی سخت‌تر و خیلی شدیدتر آن‌ها را از پا درخواهیم آورد، اگر قرارداد خود را سریع امضا نکنند! سه ناوشکن ما، با خدمه فوق‌العاده خود، اکنون به محاصره دریایی ما خواهند پیوست، که واقعاً یک «دیوار فولادی» است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64810" target="_blank">📅 02:28 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rb7HDIvXRVPMLqpge6JnepW-pac_EirxswmFhQvlbxK6KeMP628mdAvPktGle9sxHQMOG6F_paLnEcIWKdVjjAEZKbKKFTQMYv4KfUubYnX9f3x9AKHqMEMLMTPjFtav8dHgHosfKMY5aphlZipm9KYOhZ5xoG6oeo2wcPK3LfQnETXKFwKzsNhF8y6w4_q8rQp33LLWbGAvXGJSas8EojW1yaEhFzzqzFEM_GH-QiDOg-CFQxadvThheN4qEjnMc8fP0ssvqfILY2RUfCR6C10yg0W6xntCTMWWKiV37rASfUvboeCSqr306uaF6gZ-PzITyW2iSbXqcM9GwO0ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خلاصه: چند تا ناوی که تو عملیات آزادسازی از تنگه رد شده بودن؛ خواستن برگردن سمت موقعیت قبلیشون که سپاه بهشون شلیک کرده، بلافاصله نیرو های آمریکایی تاسیسات محلِ شلیک رو بمباران کرده و ناو ها هم بدون مشکل رد شدن و قضیه تموم شده!  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64809" target="_blank">📅 01:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64808" target="_blank">📅 01:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇺🇸
#فوری؛ سنتکام:  نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند. نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64807" target="_blank">📅 01:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64806">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64806" target="_blank">📅 01:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64805">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA7tte486o4Cs8pBtq8kzPuhzFwuC9ZQusPqJ0yVsF8OpWBKmaC-RgxDb6ugPwxoze7uzb28XG_rlS1rXQrSqBwtyt_-TKc31rV_bzNaFOErbdc_rD-St20_3zRNFb7uGpO8iyy9d1b6AQuaUwvP9lVFlCpl8R9Tb-BTcb8MnDOBPXgqOWqmHcGYTdJBb9fE0d_abLts-lfrq5dL_2IZEL42gA0ktxV74gJWsJ7VmNrA4AbbbtH6cDXg-a-UTSwPVOGom4ufplL77bucoxZacYsVVxQsK3Hp1ScvMYNKz2vdfEG2hyiL5GO6bBcmhqXQOobbGLgDUkmoCMBJ1iA8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگنده زیادی مدتی پیش از بریتانیا خارج شدند
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64805" target="_blank">📅 01:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64803">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64803" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64802">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQN0kILsx_8YHRaurr03e2m-sK1YJZxUlNC-ceUgo4Nfkw3zWx-y1RenNfm6i083YLNUFppIwlvZlbHBlyXSQZRqu6SryTp4bhuWisjxGzVvSWFAUIbIHOdLXBMy4dcBDCEllQhkJ0hgKPmL4Uyk-FF3l6KP3gku34Dvg6Cae3LZEPNsdsIEPfxl8_D1ELjE6IM5LhgbUKVE3FW-z0EVLhWjE4ucltKo4GvetZ3RA_9QFCa-Df5Hdef5offvFBXdIyP5rRRoVSbOmGIpIhZgW8AuOc1Gjg4tZnS6N3e2qVDEcLYHHpIl096DE2Gv2RLqh8t4SV5Si3JdDtNEISClnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ سنتکام:
نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند.
نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک را در حالی که ناوهای USS Truxtun (DDG 103)، USS Rafael Peralta (DDG 115) و USS Mason (DDG 87) از گذرگاه دریایی بین‌المللی عبور می‌کردند، شلیک کردند. هیچ یک از دارایی‌های ایالات متحده مورد اصابت قرار نگرفت.
فرماندهی مرکزی ایالات متحده (CENTCOM) تهدیدات ورودی را از بین برد و تأسیسات نظامی ایران را که مسئول حمله به نیروهای آمریکایی بودند، از جمله سایت‌های پرتاب موشک و پهپاد؛ مکان‌های فرماندهی و کنترل؛ و گره‌های اطلاعاتی، نظارتی و شناسایی، هدف قرار داد.
سنتکام به دنبال تشدید تنش نیست، اما همچنان در موقعیت خود مستقر و آماده محافظت از نیروهای آمریکایی است
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64802" target="_blank">📅 01:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
#فوری؛ کانال ۱۴ اسرائیل: ایران اعلام کرد آتش‌بس نقض شده است!  @HutNewsPlus</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64801" target="_blank">📅 01:06 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64800">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حوصلمون سر رفته، کاش وحیدی چن تا بالستیک سمت برج خلیفه هوا کنه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64800" target="_blank">📅 00:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64799" target="_blank">📅 00:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تسنیم: داریم می‌زنیم
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64798" target="_blank">📅 00:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64797">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این جفنگیات [
کصشرات
] رو باور نکنید توروخدا  #hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64797" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64796">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تسنیم: سه تا ناوشکن امریکایی زدیم که سریع فرار کردن به سمت دریای عمان
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64796" target="_blank">📅 00:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64795">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
هم‌اکنون گزارش صدای انفجار در بندرعباس و میناب
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64795" target="_blank">📅 00:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FruW55uPAa_0Udv8rdiBOcpcgsQ6KPhysnTLUwJ1QNpHcEoNv309XsAg9T6h_54IJmp5ojpP4LxvAvLl7kPm_jRGVw__Vf5_b2Z2GzFE4I54Ljhv1UczgM5DHnlvSPn_T_r-97TG-xhUukwzACewrItCW6Ut3FaDcQVXld4gwusU1nT4_eq6Eo3K5fhyJM7_-iz9pE1d5pZgIUUNQjEy7BANogFA4I5smNjnA8nR0qRccdONXjW7OmqILiyeHHspFf8chslmJfG01ltqbhNtPx085w6XLaJeP1raQ03tYYAaA0tySRaUxPwWrSvDx1wEfUJJdU0CfvFKVqciOrY2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جفنگیات [
کصشرات
] رو باور نکنید توروخدا
#hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64794" target="_blank">📅 00:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خسته شدیم انصافاً، آمریکایی ها یا زودتر توافق کنن یا طوری بزنن خزر به خلیج‌فارس وصل شه، این چص‌حمله ها مارو ارضا نمی‌کنه
🌂
#hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64793" target="_blank">📅 00:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1465e8fad2.mov?token=ngC5CtF85sThV5NnZpga8XVHnuKDZTxuQp1Ca6M7vCKt5c-75NG0i64ydtXTz2lWiMflyVTT8x3DGmog_pxJCz6veM8S-sqRO3FMI9pbY5uIHoj6hqkgsIvvAgSpk_2PxwZ7GSP9ZzP56gvkSSCTTbxqnWk2q8QfN2AGhDshSxAZoLoxF7IXZ2Z2HW9QKoBjOw54AwMD9nF5mP6JQ33P9b2JK-IK8gQivpf-spiczA5iqFWlDkpZ0K4_IFT8vhmdcsCvwEk4er8yuRJv9JSn3YasB0itW1vCIj6L_Qunl16W32FsbOTuoRSZiednCYfHSyd7770ssAtyiQUVb8W4CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1465e8fad2.mov?token=ngC5CtF85sThV5NnZpga8XVHnuKDZTxuQp1Ca6M7vCKt5c-75NG0i64ydtXTz2lWiMflyVTT8x3DGmog_pxJCz6veM8S-sqRO3FMI9pbY5uIHoj6hqkgsIvvAgSpk_2PxwZ7GSP9ZzP56gvkSSCTTbxqnWk2q8QfN2AGhDshSxAZoLoxF7IXZ2Z2HW9QKoBjOw54AwMD9nF5mP6JQ33P9b2JK-IK8gQivpf-spiczA5iqFWlDkpZ0K4_IFT8vhmdcsCvwEk4er8yuRJv9JSn3YasB0itW1vCIj6L_Qunl16W32FsbOTuoRSZiednCYfHSyd7770ssAtyiQUVb8W4CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافندی تو شمال غرب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64792" target="_blank">📅 00:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=R_GLD48dULJ8m-L_sE0mXiW506_u-zPb5TF7Fw2o5oHMZo-pRkW-il9gLLMxNkAwwEogDdugho_x2z5-MCaplX7cI3JblQvxnuabFlWVTnzHD_mRST-Ot9nWr0I4-yMR47G8yO6qiO8-splNFfhezuhmlYIvN1ZvOfiG3ogb57twnc1ybixGppSlfxVTt2gbFA4I19oevOxxv9RlwAoFR7fzGsc-dY0lVwX5HVBiZiPvB3oYd0f1qSugZNMM5_S2mms7Wiq-zpoQyyRwp0HjyAisIq0LbTJZ4ZKJyTAXYASm6c_Io22Wc4d-En91AXnyAvLji7e2SZNnQnZ1sLn27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=R_GLD48dULJ8m-L_sE0mXiW506_u-zPb5TF7Fw2o5oHMZo-pRkW-il9gLLMxNkAwwEogDdugho_x2z5-MCaplX7cI3JblQvxnuabFlWVTnzHD_mRST-Ot9nWr0I4-yMR47G8yO6qiO8-splNFfhezuhmlYIvN1ZvOfiG3ogb57twnc1ybixGppSlfxVTt2gbFA4I19oevOxxv9RlwAoFR7fzGsc-dY0lVwX5HVBiZiPvB3oYd0f1qSugZNMM5_S2mms7Wiq-zpoQyyRwp0HjyAisIq0LbTJZ4ZKJyTAXYASm6c_Io22Wc4d-En91AXnyAvLji7e2SZNnQnZ1sLn27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: آمریکا به یک نفت‌کش ایرانی حمله کرد که یگان‌های متعرض امریکایی در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت فرار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64791" target="_blank">📅 23:40 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امارات ایز دت یو؟
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64790" target="_blank">📅 23:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
📰
خبرگزاری فارس وابسته به سپاه: صدای انفجارهای دقایقی پیش مربوط به تبادل آتش میان نیروهای مسلح با دشمن بود که درجریان اون اسکله بهمن قشم هدف قرار گرفته شده  @HutNewsPlus</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64789" target="_blank">📅 22:57 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
تسنیم: صدای انفجار دوباره در اسکله بهمن قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64788" target="_blank">📅 22:46 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
گزارش صدای چندین انفجار در بندرعباس و سیریک تو جنوب ایران  @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64787" target="_blank">📅 22:29 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
