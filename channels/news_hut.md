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
<img src="https://cdn4.telesco.pe/file/QUWrsBeVcezt6XZnOhlTFVmucaUn_uuqX9SOtZjfU0d2nV4T63JPkL6rIBdEZhcPoo1sgEOEcumFFtCxW_8FnHJ592LHjvefFUog-1ealBabOiyovNxaNCrlUZmek6_LWiAE5LKLfWEUq-tPSwpZiANcXbC2gTX7l6WerGDtrjwYWn0nRU2E02wp5deYHfLqJQorwORxiQDic5Sm1syQLuz_LX_RY1yI_-CqLTG4SXGaWYYIUME0xQxaBCUqp3maLeddz63AurkRTfcYXa4lLkJb-kYs1UjHWbk139AGEoeMGGRyNkqxOvE4SX5RKWrL_6KmWVyiBk9-oBijSxN1WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 221K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7FPsnAyuwmKYwqqXDz8SKsHHJ10yxr4viSDJkdy7BT3HvExAtkVh5K-zRBuk7q_47qzdlXWulFEkb3UmDbnM4IPUbo1_BsfmcFfaAjK_n_dEaJmE8Qhi8pCN5bkrePy7SSs0X0lvJxDWNbQZfxcyVsIvUkb-E7gYMsx3VjLmtD7ZMkg6hQ_xpa4Hu79mnT0JHmtprXy8bwpaD7S7LaadUemQ01luV9Zfu5HxaxQ8lJXgOmNjAoVSm7wJ94YNac2teplGm6rP20x54enuV4QrndpaB4Ccgs645pqRdTKuHFIxlbxIszadS_pYSpeg58acL-YnnY1fbWiKqeGmSK02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 522 · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5LTuhy8xIJ5vuoEp9jJ4NTt9zI1ll4Y3m2vLMzv08SW0TJF4Kftp5O1YGTkhZhVhp2c-_w9B_ktw63d8xi6utxWoEDqbS6T0twbxDfXQesGDCKsaokO32uW_b7bYZ6IF33jDmB3zsOT7gUOHPusEKMRWRhiXcFy3-TOVIV2zIbedCTpq0KxlGJuCBen_b-IdY881KBJxRehyfYDSjZUeXLv-7_wZ9keteDMXsnclq1dEsvvO8FtUsIsc1Wx7W6Unx-NIcYlklIOWs6fhJslBzXy8ePkwIplw2hEFQQfrDQ-1SGdjU8bipK48yncGP9G2wFuwVsPyfkF3DUbgvXu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Dqu6rmzFtUgsmzumGdT311Uhm_6l728QTlo2dARcW7TSVhhEp2mtnnOsrVNQt74rJPmtlqxbcI9w4A98VO9kBloCiKo2IWRCz-hWPy_vBN5hfwdV9diGKwktVbFhnTzUz8yGtEjItF7r09r0dLLG3iuKTzYqbnxdIzDhLRBsbvLHdr0fUakKrcSNrxkP0lLU95IkVcmrnE7bH6Rn_TnTgtDYEL_lKZA7rg7smGXso2rLUuQ2IkaGAUvPZPvso2Fh20LlxJ7T-4_RAMZPKclcJRSvJLjKQTlnaVptZv-dYsVS7StZ83q2sY6nYD8WqvEkW-XtVKj1i9vTBxJ0S62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gor1Vh9vu5RrJ-gAr4gQIaXwJXzbv2VyFUtzhxxP4Mw7WRzt2XosKqNSa2LTIYjpysv2Qp4uRpeByktiFM0ouzWjpOKK_v_gV0fsxiPK1FuYVb3OLcJYWN8Cm4z5wqK5l9aRsZV506pdATZh4_PN60zV_WUfq7GtvHddkNPCnbgOCipFUO02gkC3-otP6HfhBt7YzkA50DbTiuaiytR89yYaYr2FRjxunkh_3f4YSip2Quw9NSaJWjGp2Ndc2I0FfWww414zRuf9u0GKYf4cWX3F1HYTIMmeP_wqPWTt6z3ZwWd7gWTnSa-qmy-QOzxSXX8Oz_CY-H0bEQKk4WK-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VauJLf2UYjW6NoVVBHie_-FOVMcjUF6e2SRRjUwOBCgmtNJvLAos1vcCf6lkMIP-dmFwU9x2ykLXDq5_Kjt0S5QWjad1AjtmsWfppNRpqCjMN2Z5WjgrbAO74Rl92hZfUjVXzJyA3g55wVlp8poTtrYw8a6hZmNB3cz0vJqCEVl0BHMMj1drlYnTe4fTchPlibMf9TbE0DSUT5VVzG1VzXcbfxSQl0n9Zaa5nviD3M3vdvNt9Pe5OE_inOBXVP9PDEPIFDPqm4YV7oAESDiEB5NWejGG7GDvbLJRP-UdUMORuSo0Ww6qJMXuyKPSvfRzegHG67m4KcwYRO6o2s_voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxume8HH2NNDee5-mJYJRAFdz5U4f8Y6oguPqhqwKZvxbzrJK4NSY8oGBVTxSMgiv2ToE1GYUnIH3bW-uScpfWB1vaz28lXMdKvYncDjrmvMRPEdiNJR7b1Fc1-tfsSpI3MIp0eVVCP8R8OBPI5H4ES6-aorSIKdDP8SsQzLfoEVPa10-3f5bQP2PLgL1JJ7nv6W4bee-8YOXB2TMwA2TlAzySAqL3dNV2Ipref9zDvpLtYf_U6je_W0evaDbJsyKrKqccig-1JWaPCFhJ_-hwYjfvXsmud2U4iqQ9Y3fSp6n-HNrJBSAgwSV43jroyJikCzunMm2nKZFnk3QzSgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q3oZaR4IoC_eTCmLJQ8eL4COrulmtxfhhkrSt-ue9dHhipCxJguObXCt-p9jgNyseTV-Nx4Hr8AgLEHfwqhWpjoqDttWpE3JWfDxh7-y56dWuUX2FP6i8hMZT-dufDc58BBYRvHHdS2X0HwHEtg3LcHgsPDEvyQQWHYzeSE4LpcmyKst184e8yruE2KLSS5ZIsNKs1pZ9OQ8jJdScnz5IacJycbD6_UEdnmYGqNtqT6ohCV1HCzISVK1iTacf2oEq9QVR8JfpVNRYLy9V5C8nN11mN_mMQ6iesECwRldOsCb3ahaCJz2wFFMshnRKx1TJuZX0EBHtCApYarG0DVrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K22jwwDldbwtS0slQbKl3JK7R-HKhOMBITUppR8GIb4N6FjPq6LA0QrvL2PwsBthKouqgjfC0bV1v8h0jNzux4d2wjpMFl-4bkrIA5lW94QegcCYcexfzRrEGnQbZHVzX0JpkT-5nQs9H3VHvRhBEVXAURgdFctnJzqthIW2e0p4brXBaUA2gtit8x9xJmBCzbbAzxtwgp1VkgkkDCfBpRvEY1fNnl3TFYgF3TINY8N5wdauP1QcHl-8R55M-d5c4GZ0ianioa3EQZ_fyDxi2M5LA3aUex6UM7A9r4-iZ4m9lDhjyaah0CBdymJNNtBbHjpz4GKOe_wS7wONcJHXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDvExEj6VyEL5MQn1yCKVV6x1fr744oWSmzzRmKISzQWR25outQK05LGQKSsmt06C8LtvzJQVNY321hlCZvss6NicRHTlF7H9TiS2znZ_v_MFWuT7J9oZZn2YNhqyRgLaFkHiZzJaDLi25tJLC82uwiC-jUqOaIwBHtqRnQ8oAo5JsLIkUXWJNW9nCKrh5sA2EUMjTlYTt8wNqQEW8mdmUJ5YoRmXGSBi27PwBhnzpg5cEPijD8QacO1zQIGq8OhLZP8BBi-fgUMlVuZLcQcGb6sVc3FEkARxqx4M-6ZTEIx7QiBahuWvWdcJ5RqQImmOilyQsmEBK1qC-Bzm5Z9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAlqS6TVlzidGu31QOSJ4Ef151VC2lwZHfyHM6ueoraJ0bdQD2jXTIW7Zo9W8d442JEWmSm6yagfgZ2begJmQgQG5qbJQOpwD5S-8QrVATWBJNV_N5_eXWELLKbmqkHzqpzgQgVwGsoma_7MQzIVj03jIF2nUHEYstEseYVP27t1hll66aBH6rAQfVzad6tF-kyoXQ_xuQOB_b-19590ef-OpB20DJwzkUinkDwi05QRNvvJ9AVZSyZkMaKJEyEXKtHEi3hJjUJoG9P4YseFQoBJfr1h-JZtaQ1glnCxb2o4klYkSP5XpU_wjF2BTcqSGV5_5opWaaELQKQMNkGE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy42qJ0DmWjONP1OqEcJ3nq_e7A_2Iz5ccP24BhetHLHiZ-yQaKkSo31q7n4htGlTAr8OA6eIHuLAmnCPSwRvpt7_xljfLwAg2CdX9honVhvVwULvBoCsFPOVuZl8BW14nPhkYDqeDwlceqfpTrYs2kdf5F04uoqH7RlLf_8L80OIzlFCzB7TT87Kn2uVq9RY4lR-NIXrsWzh6UZWfSj7acqpDDcOSqMYZFOlzN5-o8QFpmFHN0myIAn3AAzY4yuuELRv0_SeD2AKX8ipop-Oh_t_F2w_qmhzi1EQBGZVTgUMPyLSv50jsS8CI1_LVhtKtgVaCVD1xX6FbRnaSWGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBwQeke6WcUGJDk-3I6ozpJCYTW8lp8xwx5TT5zSfKvEKPEqQD8P_dzt8nXkzk072fCItvlqCGcEDE-f6zst52qtzvot_8aRTn6mKWPxjsh__go_vw3-IJiYuIwrMxxA_H7SZtqXXCVrq0GX3vZ9jaa_nG3pY3GjZiU1qxcM0okoukvyfpdx-FLFPApfmIfRKq7l7DdqmaWJuU2ncxBxaq9h335HcHMBkj5-5MY7e9NHoDnYca-StczzlgAIyWOZtc_megsOvTQXEvB3QLewIWa-zt4UpM3PceqbfEwg2nf_jRHlXEZPow8dDQ3y8MgqiDZLDEGKS1rOSk-z9xMptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmUg4D_b8jfdyILYtmqnoYQrDDI5ou7cbGF86Cj3OR3bU3m3bw-oLwqeXX-KrmadbWcv9IY0Wncf9SgmYEyZXgeXOSfNXMAYRnibA0i5-OqtAjLEt_KQB5fkOWYzaR0KvxCWQUZcFGSmHzq5htJoN6h7YzeOWaiL20hfibGFGqTCgFmDLG-pwMZXF2UxUnXSiMzrA0ec3mvWTn_CBG-eW_oFhYihOPijF6CfU8uS7Ox8KgSNHh-V3v0gm21nWQKZuNhGMnB-LApxJlELy9P-QxLjfQ9FjJkokwvciIxmf8zVLi1fAXRXL_xMzSZhCwq7PQwX2HcKLLrZ3qVHBV0l1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=S7m73mfCwPps0UOHiTb_QDvAwPn6PiB7oYukvd-gUyMa7dZnJH2PVDAfhHJRjeEwIUXP0fGBKL3jqw-tmt09Roib9C6QXp0xPUxGEg77PbNs-jFc2mMQ347BdPpGFNwThxu1CtXfEaPs2bNFzjIa-EzW-I0MO9xO0ST8HqhmkffuFzMPfXOMpJ5Hse_eaxeCYhSiJWn9es3YklHrKqRTbv0R0gGY9QkXUiIi2Or9O_ZnUzL80RFrZ5FslxafqQ2VqnPr2trYJLUWaT2T0hP8QZ6qj0h7LHPuuSYubZAbmfXmx1YpTR2JVNcsg_rEjiH3XOQhbpk0ikbHmwydpGPEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=S7m73mfCwPps0UOHiTb_QDvAwPn6PiB7oYukvd-gUyMa7dZnJH2PVDAfhHJRjeEwIUXP0fGBKL3jqw-tmt09Roib9C6QXp0xPUxGEg77PbNs-jFc2mMQ347BdPpGFNwThxu1CtXfEaPs2bNFzjIa-EzW-I0MO9xO0ST8HqhmkffuFzMPfXOMpJ5Hse_eaxeCYhSiJWn9es3YklHrKqRTbv0R0gGY9QkXUiIi2Or9O_ZnUzL80RFrZ5FslxafqQ2VqnPr2trYJLUWaT2T0hP8QZ6qj0h7LHPuuSYubZAbmfXmx1YpTR2JVNcsg_rEjiH3XOQhbpk0ikbHmwydpGPEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhJd55tlqNxuZ7fdyyjH6CZjhuo7nh6DAbq4pTdoWAgzJ3Q3Yjpx1lBlfjs08Qe1S7YC91Ler5HBMwoEWcKep4l-THrlPVni1-jT8F_ifRf16WwFnG10DvbAu5uRz7-vrWxRSVSY6ReChQLnZ0LmqHQ-rvM4fAaY17-RN0k5dp8fDsJAu_EATCB7Km24qgZO2QASdsoeN0-hF2GHvZno_kcWT2MrmjHYy1ILeRdAA2IOjpD1pQKfqX7zP9wxq0RyQemeifgJXN0Z2aKb5bEFtVYVvf_o4Nrq63SXndh69M7t8kjy1sBL0ugta18Qp5QeSttc28LMBsC4P9H9WrJpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUGVl9CLfy37So5sqBBMYbxXLuD9sCzFw6LinaXl-7w3ouprur9EyLxezhCtXSUdbfg2oUjplZ_X0oHAvAtz1UzvIPu9WAmjRLpr3If-1vgdT3-E_4zWN36eSe3jfMstchkkL8s9XV7U0cjWFdnAAM1UhsnFRJ6zPfF6Shy97y5dznAhdujuoQ8Lu3WgE5-8sFyI-JwjQ4CirCk1_OhiMJbEHRmYUIaZ0DDT-qs2V-W7zMeZ8HPlQF0FM8xPoRQnyHYw7q6qwa3qMmYFe_drpJ4nP7UnMvqFvfzHsXY_jRqLs7N2JS1gEdv6msV0803FjUb91Q_PZx-eJJCM9k9lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBcm8SPMk6yZLjfsypx_jOBo_-wxLLUP7FK9vbQcUQQsSkpA7XL8j2a9l1IFPnwPizpKgX7rdYUqRvnYgh4baEI7KDT06ZtlzSh_Mf8lR7vs1Q3NZexZuB_BfAhqmhcm7li4IX66loHg2_5jtFdInq7zLWPq8JXipyp2Bcyc-K_488TD27FVvDRzEqYMkYDl9pOnevPzl9HzXGsBwqT_r5hzeIP_u1Jfc31NWU0LEMwKyc0YSigR3_dVl8MnrWdktStcqJrhqP7aQtg8NYvBOt2-gzXBK0xklJiL36gh_97koSM_LC-DdOeKElrtSR_ORiFt6h60HDHDVa_E_pO_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=liA5TZoGDz04Hq-vy6rpoNJIiuXVIZ2lCwGWbSkPIatWvaLuRDl1zLEl8OgypInRtDbxIbTclsTZt7cUbnqW0bTlVIa8He5C132DJxNyA9R_kz74EvU-07VthQzhD6KsNIv2pXu4b_U-lRweahPqFY2W4ZUmOLT-fn74_MbNwyNfXVgT5uSr-BMYGS2oeZfM1C1rqBwdKTV9zH-j7pVm5jZJ4mjCDQapc6U7vguC18ao4hF_Yaun8MPWeNdg5SKBJOfERmzItIPEvYh1Hq37Dye_6RTqokJbzplxsCrEBPQn87q2GiBmRK9RMVwqkO5Zhu4u-0rnoFW3Ze2AqOSkPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=liA5TZoGDz04Hq-vy6rpoNJIiuXVIZ2lCwGWbSkPIatWvaLuRDl1zLEl8OgypInRtDbxIbTclsTZt7cUbnqW0bTlVIa8He5C132DJxNyA9R_kz74EvU-07VthQzhD6KsNIv2pXu4b_U-lRweahPqFY2W4ZUmOLT-fn74_MbNwyNfXVgT5uSr-BMYGS2oeZfM1C1rqBwdKTV9zH-j7pVm5jZJ4mjCDQapc6U7vguC18ao4hF_Yaun8MPWeNdg5SKBJOfERmzItIPEvYh1Hq37Dye_6RTqokJbzplxsCrEBPQn87q2GiBmRK9RMVwqkO5Zhu4u-0rnoFW3Ze2AqOSkPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=fcJBweLXMzNubf-3bDC6liVZ7WXFKWPeQco2FrzOvfPBRUd66NEvzXdBU2JyyAN7saLr3Gubba0_twpMEDjtXPKEvxA203qAhjYRozcijjb1RY28YmWqh7AF-801bOMna4_d-fmlTzBBvoTC67n2X5yS-dHLbPVGrsZLyNkenhaOwdWXB-0Ph6DXaZQ3efU0OWawfuWny7PQPah2tn5Laf2DdJDVWR3ATObrt7ZEzX8BW0X8ljF5dsuyLuY2uMWimtEDdyGyesakncbNbBhBrpO8fvB5V1flB9296lFk0_ytP7tU8kLXwqr11KZVSqMxZejfzjb4oyh1GT-MmeDqEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=fcJBweLXMzNubf-3bDC6liVZ7WXFKWPeQco2FrzOvfPBRUd66NEvzXdBU2JyyAN7saLr3Gubba0_twpMEDjtXPKEvxA203qAhjYRozcijjb1RY28YmWqh7AF-801bOMna4_d-fmlTzBBvoTC67n2X5yS-dHLbPVGrsZLyNkenhaOwdWXB-0Ph6DXaZQ3efU0OWawfuWny7PQPah2tn5Laf2DdJDVWR3ATObrt7ZEzX8BW0X8ljF5dsuyLuY2uMWimtEDdyGyesakncbNbBhBrpO8fvB5V1flB9296lFk0_ytP7tU8kLXwqr11KZVSqMxZejfzjb4oyh1GT-MmeDqEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=uorIE-wPyDDGG--GFdEYsDN_n__AzsEjshHzzlLcbQ8SLmYptFI-I5BFSp2iJlXT_Dh5YU7Tq7PoGx1E6hWpZ1g-AqxmSFK11nftp8rwNJJ-uKYnQg10WJ1OYD_PrgIDO-DiLiFolfyRff4CpgxdvNPTODNKLlBKCnd7q5xnD6yTwkabuV3qaqiHlq0OPQrS8NvMz9kps1CdFGRkRPLNta2DdSxjv8IO898iraA32jkjcZzr8jZKK2EWqZ3ebBuKzkcr7oVQIXqqp0wDLbbF4mPZHOJwZRbpLK8xaRqzF5lE92M_Lgt_d8P48t6miJsviCHh4KUAoqwgRbQxHIGreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=uorIE-wPyDDGG--GFdEYsDN_n__AzsEjshHzzlLcbQ8SLmYptFI-I5BFSp2iJlXT_Dh5YU7Tq7PoGx1E6hWpZ1g-AqxmSFK11nftp8rwNJJ-uKYnQg10WJ1OYD_PrgIDO-DiLiFolfyRff4CpgxdvNPTODNKLlBKCnd7q5xnD6yTwkabuV3qaqiHlq0OPQrS8NvMz9kps1CdFGRkRPLNta2DdSxjv8IO898iraA32jkjcZzr8jZKK2EWqZ3ebBuKzkcr7oVQIXqqp0wDLbbF4mPZHOJwZRbpLK8xaRqzF5lE92M_Lgt_d8P48t6miJsviCHh4KUAoqwgRbQxHIGreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGe3GF-KHksU9YBppThzYmFMDV2olM3Rj8M831AbpLOcL5A6mPmhp6WrvMVphZTd5EpOWuyudyYuv-ac0qLsaeSGHjbhowcx349StpAjo9lIR_DhO4D2siDaCKOcJas0ZMCYx7KHWlwUmW4UcAFcnfOtuyPzSLQS76n9oOZbvSEb0A9TLenfqwkSptTc7O5xGNoK-33swKSMkrnAn1VrZkgXWtNzikukNhjCIjS5ViguBDn1FTTbhEh4B8kIvrjRr2CvMkWm9TDhb8VtD_GSEQT_frciP9NCehA-iqwuCbYUrxKTivR6wZxHwICGsfea4wKkJVnvJd4zt1ACGwByhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4LTsJM5_fmFLF969cO7SBDtjIqeZ83l2-_KJEfRdxy34VUQq_JcDnlGB2Yh37FGq_lxCWAbJcvaHGP5HmjtZXNg6-A9_BWCGPUgweSt0N7R9fDgfl9OyZBbRsNC1DsSjPgw7JJiVlnW31Kt8Pn2xrh-CfHLtH9bTji67tUixQ1vo-soiZC2n0ZQZDNptJ-QZx_Wf8TBvNVMcJEF5_RKWggkEVMZZuy-X_HpmnSGywSbdpMlqQU5rvCgBrCl-bwY9M9MFaL7clJqizY6iFKdF0Yv2wYFwM-LOFFrKQYEJZL7giFO_R1V5AOfvTR1ECb10Ew7FBPz_G7KkRJZuR627A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4X_3U4-F3fHjMVef9-2LsiuKffgz-bUQfgd_B3CszvBp1he0PVcQSk4OZCWvcNWrViTh9CbcYFhp8lfRcPFRgGkNSOhf1b5gdtN4_91c7zTKVFsBtStKTD9bGpv0gZQshscsfJi684dPJ-H-l4ABcRMjTPlFnDpVyPKn3QUbzsomHfRqBUR4DjwQ0EB1lTiyYNaKIAo5L2cLKvC4rjc2D4vMKr8APV-fFlS3EvwPKOkAW-jo-bTz1zSKaimEhV7NecqK3c-WIeLCoBq-iCsrjpNss70nQqKsL1WdTaQ_lo5thyXW4hRYcXKGaVYclmtaxflcYTpAMVbspk1OMGeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4x1i7gZUPSJ5rIiFyHl9cJZ4O8zq-hwBe-r6Miulc2EkxFH0Iyq7URZXiG44puHCgVuvO3lOMNTbtuMflCSWoeQwmff_rK_W2XFJffuILwJ-bv2uUeioSiT5pp_xp2o9sS8E33sr_lxcEydhxgn6DNn_X8f3R9wCUiqBZ4aTn7nfu11eJb80ung-lLrqV0WCltWweqZdQxCI2DAZaFDi_P94Spe_WlRII3WJktzGYEFRVp9WHCmIwAcuqSPzG4JmNeUw2TXvYJOlJ07A8Be05kiCZJTxOAK3fqNR6o4QFONORM34yrDCfhRwnFlrEh034japQmmSdPM2u9j6YqX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuBJ1hMKhGAhr-WNeSD4QizIF3XMFppFMy7GaomnSQDoOdAQ6-8QtId6ISI5t5wWlpTTeW1rAgS6JVF20WHIZxeI2pED4IvrQa5Ijm8TobIn-Re1KrydEJ9fq2mNEID5pg2hC2Tq251bXG1fKFfuvpyGNgk_yJ3dR9Wsj5SlDDg51HDOgv7Vt09esKBjtv0Zl8n-1QM6qo8NJUZPLFHpf0IOFxD4yVRI1n2TE1vm37kTVNkpSdrbp5fDgrBEtFlcBL--bHLooC0P6z7JpFPlPbHNVAVStDBZtE0mh_AjK9k9uNQVoA2ulo4CVs5El2bghgw5YfHHmbl3sGe3GJksgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5jicy-VVbvO3sVYMVCTdnR0jQ5Otuawf0_1AHGuEuz4oTEP6DTDNKP_FW07i9L06AGMV4UAinJwNCUXOniRXwzqVVlx46L0c_0g_uQo6TlnrVDgUVazEcLvqvhFQVia_ha7jIXPpZRbJfMwCWHAtnZuxCZKitwzCgJHS35_H7zygKjekjHA5jxSEUPaan8_zjwScfU_9Bn6WiIfxzkNEMSNPuOqrIqX-MXmKG1LpwmK7Ud927FUMww9y-GBMS7cG-YQhHBqlXqvTw8A7x8OcFGro_QmU-M6BD8GMW-xiRH2SEsLYtm07Y2GZv0bGBCFQdY158d_c1wBD5b-ZibV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njnMMbi-_2r7Kt4nbZmC0Ad7opLb0xIz6btJJY6-pTb0fQIeokgkTwFrwVmygFq0TgtX1dfQDA__QT4w0B9iHKekp9VCRNX2TD9YtE4yYFzz6wsqlcdA9wzZvbvA66pAMRVheW7h5jFuAVoH-x_BOl2d4ztLHf7uKqXlAtlkU_yBlwr5zqw5eVmt0_o_Uc3gyl4R3NJqv82a7XJvpli2BadxOd7AmvXolTa75VyGaMCHM_KXR6u6wjAglLF1c52Y20vSZNRdZAoWXG3GwllFSbV3zxhQmotRsSmzqx9sjR3R0-jNlw1kl9VvH-3V41ucR6KY4-2uuSADNwBIRVO7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=Q5-0oJrwjvVveIarfGBvHN377TdY52uRnnff9neFBKZyFy72YX4kdTSEnndBZduyU3bYRp43abJILh_iquAXFuBugMH0KyxWYNcNBliygY_N9Qz2isK3SkQ8PDFvdgA4arpWlj8Twn2jp_y-z2alk-zHuoMlp7Cii4e8tpZaK7R2WjXlaRFGWzUtAkVSbrWV93CD7GNJVs9yeiE32bVgsc4EyqCKU8xteP7S-z1dXwohD9DxFxxfrrKlWHoKAdN1ACE1EL7jE6Z-FnWPXaStYcy8nrwUDBSu9eLUfc_va0bQIKL1VVm_rYrNlTr5IpuQEeHhFl88eIrmJl0vIJIj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=Q5-0oJrwjvVveIarfGBvHN377TdY52uRnnff9neFBKZyFy72YX4kdTSEnndBZduyU3bYRp43abJILh_iquAXFuBugMH0KyxWYNcNBliygY_N9Qz2isK3SkQ8PDFvdgA4arpWlj8Twn2jp_y-z2alk-zHuoMlp7Cii4e8tpZaK7R2WjXlaRFGWzUtAkVSbrWV93CD7GNJVs9yeiE32bVgsc4EyqCKU8xteP7S-z1dXwohD9DxFxxfrrKlWHoKAdN1ACE1EL7jE6Z-FnWPXaStYcy8nrwUDBSu9eLUfc_va0bQIKL1VVm_rYrNlTr5IpuQEeHhFl88eIrmJl0vIJIj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=jgcA-hcXbo4gRjkCBb-76Ggy8r4HySU1mISJ3eXCV6EL9zcHS-KkO6RTGnNY4tlll4vqN4h5W0lRkAzh9H2t-OUMkD5TBFTvuqptaHK1tnVQ_RWrXunXbLyOqoXW-rB2aLb4TxMPPRI_n1XSXzdCeehEMZQZ0WlpZeRJhCnEyOp6GqZa7r1_WV0yyDNw50_cFYkgCDYb3vaDKwDutlxxeDks3A8kHN0v4CPelwy3ioji1lNGlTYYrpkZ9dSzpK5ssUM1PpZHLyreKcizZtmcDXURoTzgsKKVm4fZ7dAbm8LNesh3H-VWPrMoLhg5RqMEmbMdzmxT0AdZLlFXPfFySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=jgcA-hcXbo4gRjkCBb-76Ggy8r4HySU1mISJ3eXCV6EL9zcHS-KkO6RTGnNY4tlll4vqN4h5W0lRkAzh9H2t-OUMkD5TBFTvuqptaHK1tnVQ_RWrXunXbLyOqoXW-rB2aLb4TxMPPRI_n1XSXzdCeehEMZQZ0WlpZeRJhCnEyOp6GqZa7r1_WV0yyDNw50_cFYkgCDYb3vaDKwDutlxxeDks3A8kHN0v4CPelwy3ioji1lNGlTYYrpkZ9dSzpK5ssUM1PpZHLyreKcizZtmcDXURoTzgsKKVm4fZ7dAbm8LNesh3H-VWPrMoLhg5RqMEmbMdzmxT0AdZLlFXPfFySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=FkzaIlnE49CSiDg1Ao7DNGmxguRU6pL3oifUb3IVBEgdNOPNvrUqFHGT5lxkUTmXDhxn7mxKqfPJtYuKJfvAGqHi-SHjJtRovsJKMjVMnF2hjDawTMPZ1W0aZbR7eNIgxtpkL0OBvfiQk27RYd-pKgznoL6m_o96vLSgojDI9epcleOx17v4RU1ZK24tCOC_xsPScxdsQIMpxWxj_LJlYpbOlWgbwVbgM0-8Lt-1efU457JhuBGLy6P9D8AYI4TP91EaBeJOG4MAG0DcAPBq8-gcB44IIaqb89Q2LIrmr0xbqKX-oGROXkRQxpOoOnFpZ9wyovvUaGbEz9Dt7_HBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=FkzaIlnE49CSiDg1Ao7DNGmxguRU6pL3oifUb3IVBEgdNOPNvrUqFHGT5lxkUTmXDhxn7mxKqfPJtYuKJfvAGqHi-SHjJtRovsJKMjVMnF2hjDawTMPZ1W0aZbR7eNIgxtpkL0OBvfiQk27RYd-pKgznoL6m_o96vLSgojDI9epcleOx17v4RU1ZK24tCOC_xsPScxdsQIMpxWxj_LJlYpbOlWgbwVbgM0-8Lt-1efU457JhuBGLy6P9D8AYI4TP91EaBeJOG4MAG0DcAPBq8-gcB44IIaqb89Q2LIrmr0xbqKX-oGROXkRQxpOoOnFpZ9wyovvUaGbEz9Dt7_HBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=QiSFoZ9WjZQggzvJMlvdBynrYwOGWjvMiy4pMc89iBI0lq7fLcyBpENAdZJqF2XCWo8aPgER9p-dlcSCsqgSQnhNbHzMACNb4_C2njNyivx3g5fxm1XDtegyC9vso1pQ2l9BX8nSVBjPxl6ucK1cRsD_G0Dmg3t3eOXZAKOFzMXTBdtF4SwhWmX9jutt2pd2FTSpJ42qIZbuzKfj0Si306Az-UF4qY8luNATUNtkoW4XuSYjv61NChchU4teZKV1q1z4UP_reEmJiUUg8aYW9k3RzVgQ_UDYlWlRJK8-GbfIHiI4bd1Y1P2lIUHEeVEnFYpS6Ow4w9_dmRRrkVbQMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=QiSFoZ9WjZQggzvJMlvdBynrYwOGWjvMiy4pMc89iBI0lq7fLcyBpENAdZJqF2XCWo8aPgER9p-dlcSCsqgSQnhNbHzMACNb4_C2njNyivx3g5fxm1XDtegyC9vso1pQ2l9BX8nSVBjPxl6ucK1cRsD_G0Dmg3t3eOXZAKOFzMXTBdtF4SwhWmX9jutt2pd2FTSpJ42qIZbuzKfj0Si306Az-UF4qY8luNATUNtkoW4XuSYjv61NChchU4teZKV1q1z4UP_reEmJiUUg8aYW9k3RzVgQ_UDYlWlRJK8-GbfIHiI4bd1Y1P2lIUHEeVEnFYpS6Ow4w9_dmRRrkVbQMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=DCfkH-vBguWQ70EXzceEFBomuaWfMOOfFs2zocCCkd0gF959KwqQuKZQkboQimWri0tkE2UqJ4xWEdVQgVA0wGZeAwMRWP64bs9QcFwOtLKdBSr6gLzxL7ov-o3aa77F3snTlbHR8rw_UJZm3KJOCu6nI-BxMF1ed5lYdiix4nJnzaqASMRGp0nftan9j1dmDntr63LB1itkMCSYbVv3AeC06wGWnidIjF3DoFH1gGuY0HiUSay29p_6JS92YSY5MTnrhCHVPBMCpCBoY3BBBODd0Zs0IweDDT7xzu993jLU8CuC7UPSpr6zMXM59d6iKB5NCb9hYtHGJdUnVpV_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=DCfkH-vBguWQ70EXzceEFBomuaWfMOOfFs2zocCCkd0gF959KwqQuKZQkboQimWri0tkE2UqJ4xWEdVQgVA0wGZeAwMRWP64bs9QcFwOtLKdBSr6gLzxL7ov-o3aa77F3snTlbHR8rw_UJZm3KJOCu6nI-BxMF1ed5lYdiix4nJnzaqASMRGp0nftan9j1dmDntr63LB1itkMCSYbVv3AeC06wGWnidIjF3DoFH1gGuY0HiUSay29p_6JS92YSY5MTnrhCHVPBMCpCBoY3BBBODd0Zs0IweDDT7xzu993jLU8CuC7UPSpr6zMXM59d6iKB5NCb9hYtHGJdUnVpV_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=VEEOcOYX9BNkYUYHAClpiLqeL7ydN1DTrMBBHTlBuW8mNzfjJhFyiGu6MWC8j2Cgi798GtPT_iLwLm6y7QanjC7PFYJuZLBqMRUPuIcZYkkzNTKl0iASMUvAwJUzqAwmMbhawIzhTGSNsweLy4yxV95IqtRRBNR626ucPl5SK9bSTMwzcb34CtaotVc9MoAeBzb5Pa0SkJwuUdGO79IK9SE9nx7jrUUUF9F8xdH9Fruq5GjB2ybduoAvCzFiVf6rl8jrI1cx7RNLkIRhtgdosEdwBbF5t1twyxYCqZgVD1LbcPLWpx7ICLy9EAr8_tXiA8lb42XLqapDlnAl_iERYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=VEEOcOYX9BNkYUYHAClpiLqeL7ydN1DTrMBBHTlBuW8mNzfjJhFyiGu6MWC8j2Cgi798GtPT_iLwLm6y7QanjC7PFYJuZLBqMRUPuIcZYkkzNTKl0iASMUvAwJUzqAwmMbhawIzhTGSNsweLy4yxV95IqtRRBNR626ucPl5SK9bSTMwzcb34CtaotVc9MoAeBzb5Pa0SkJwuUdGO79IK9SE9nx7jrUUUF9F8xdH9Fruq5GjB2ybduoAvCzFiVf6rl8jrI1cx7RNLkIRhtgdosEdwBbF5t1twyxYCqZgVD1LbcPLWpx7ICLy9EAr8_tXiA8lb42XLqapDlnAl_iERYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=HRdENQ7abOU7OarBHYyZHmkiIi-l1zSRJOOdzKjDsFViSiY1cNgnWlDiF6v6IXtffPjV4vjLJsnJEWDmePvyAzeQ94nv81mcTelezQsiN_PeO7bN93HCFpaiHpOdEgmbuGuJjQwbB8JDGpsIXyQ_7NgMaPFS0HlAKonFh1_hxMnpq42kXWzyQNXB71VWh_DIksrqUHde2JzewDKfUPGBkx7VPyYnBEeHpKB5lnDSq4g6qWyS9ZqJMilKKUGcRfbeuUiBH0IEM_6vks8nLTXKOqStyf2Ggk9lqw2jvr4EC0PM_bAm5ZB1aDXma0ozjBS0aVJdKFy-yd1BbrSdempLew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=HRdENQ7abOU7OarBHYyZHmkiIi-l1zSRJOOdzKjDsFViSiY1cNgnWlDiF6v6IXtffPjV4vjLJsnJEWDmePvyAzeQ94nv81mcTelezQsiN_PeO7bN93HCFpaiHpOdEgmbuGuJjQwbB8JDGpsIXyQ_7NgMaPFS0HlAKonFh1_hxMnpq42kXWzyQNXB71VWh_DIksrqUHde2JzewDKfUPGBkx7VPyYnBEeHpKB5lnDSq4g6qWyS9ZqJMilKKUGcRfbeuUiBH0IEM_6vks8nLTXKOqStyf2Ggk9lqw2jvr4EC0PM_bAm5ZB1aDXma0ozjBS0aVJdKFy-yd1BbrSdempLew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8xdXaUfTadxyA_wweBUzLW1-KiCNl4EjdZd35J4gf2TBlw4UdmDjnGctTNPDH_5HcI1o1W87L_eFxUZTOIIAWOskMbxeCDyQkeF3HhueopOnhsEWVMpkCz884UPjX3-tiy_KDkRpuEYbRUiqzC3BJH-k4Fgy-4RPs9WwrxMrTdRP5YYqq7kEI9MOIV2JeccvVdP4q5pUUBQKXQsTGM6iPUPwBc8stjMGbfnyMP0OtccaITlvEDvPuJtc-How6pTHJxvG4mClCrIOvJ4BVaDRv1Mj0eQDlPEdeGUnHy0ITgsmw8ynoItp77ZvWSy10I6R9YefTtX7YZJPlXEjGVHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=lz_f0qS7jkbnxSe1KIIQ-I6_yxbygQIAJ1PfyNxoWuGdAj2uzGokgxai-JlMudAxbN2RDGoaxbc1lwV_exp5rfiIHHax6-k1Ek71DWpdTUQPFSx6MSKNtbJ6ngC9zF3Dva8NTV_TE2Y6AEwTVHoBoxtv-cIRfY4w3zDMhnvAzjpcyGIylf0PgMun28xNiji1p0wSqf0OCMR6jSjZKEuIjzU9OyxGAYHcxjT69In1uKhLh9njLadZ0BhI2wP74lNxHUuQQ_p5JIS6JJMonJP4Cu6pXfG1vQ4tcWMMNQAJLbtHBtebbm3UZMecDg9ZLdD2I_yEJWFPMr8S5mkcbL2mwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=lz_f0qS7jkbnxSe1KIIQ-I6_yxbygQIAJ1PfyNxoWuGdAj2uzGokgxai-JlMudAxbN2RDGoaxbc1lwV_exp5rfiIHHax6-k1Ek71DWpdTUQPFSx6MSKNtbJ6ngC9zF3Dva8NTV_TE2Y6AEwTVHoBoxtv-cIRfY4w3zDMhnvAzjpcyGIylf0PgMun28xNiji1p0wSqf0OCMR6jSjZKEuIjzU9OyxGAYHcxjT69In1uKhLh9njLadZ0BhI2wP74lNxHUuQQ_p5JIS6JJMonJP4Cu6pXfG1vQ4tcWMMNQAJLbtHBtebbm3UZMecDg9ZLdD2I_yEJWFPMr8S5mkcbL2mwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=aD9QxbAeJWfxljduiARX6uio2VtaXR9PLWZNoRvWc-RmzRIGxMcdZa-w4UeDx9l-xbMS3BnTnpeg7EGPXcQ7WQfNqCcL5IM5C6yHmBOSAfi7fOrPaasffx1nJS77wSn4Qq1D6ICkJae5QuYTP0GI8o9sJqCijGy57f-ivbZBIYFqhod2alnNW33Vb5KOIqAx9C5v-8_okZfGs9HCV7gBtA9e-YaY-43NvmGyAFDVYZEtSHDroHwYPFk15yXKKvHb5s_Lt7newFPB8i6ET95-vVG9OTOy106Eniy89GwK5wdwPUzVudHOYT59bJeR1Cy-J2pogb8GDIcE0w94DdDydg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=aD9QxbAeJWfxljduiARX6uio2VtaXR9PLWZNoRvWc-RmzRIGxMcdZa-w4UeDx9l-xbMS3BnTnpeg7EGPXcQ7WQfNqCcL5IM5C6yHmBOSAfi7fOrPaasffx1nJS77wSn4Qq1D6ICkJae5QuYTP0GI8o9sJqCijGy57f-ivbZBIYFqhod2alnNW33Vb5KOIqAx9C5v-8_okZfGs9HCV7gBtA9e-YaY-43NvmGyAFDVYZEtSHDroHwYPFk15yXKKvHb5s_Lt7newFPB8i6ET95-vVG9OTOy106Eniy89GwK5wdwPUzVudHOYT59bJeR1Cy-J2pogb8GDIcE0w94DdDydg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=adZAb9nLuA92zjgfOi_DPyUbxxkac9sw4VJAdGlsdNa41f3_3awOWJ93qJU0aPgG4jJMoSJujpU7vef0raCO0b6mBVSM4hBUY7JzU185A7S1upXvG4W3hrv3ugflz76zBvapxsDn0Jmo8kAIIpHaoe_0Sx_VCkrO3dNtSgz4WSmf9oKPxmvbXBi7ZLnsU-9Pt63yiQexeO20xTIWtvSclb7Rc1QuTVKdIW-yFb4K5tW1SBBVTxXyhAmgxooQqvefXfREhKdDXKXE2OPWkVOomtdcvxdu5yShPqHJazXxUJJNjEZAvAOszVcHrGTblyAURlNETop0RnUERW0j3W6fsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=adZAb9nLuA92zjgfOi_DPyUbxxkac9sw4VJAdGlsdNa41f3_3awOWJ93qJU0aPgG4jJMoSJujpU7vef0raCO0b6mBVSM4hBUY7JzU185A7S1upXvG4W3hrv3ugflz76zBvapxsDn0Jmo8kAIIpHaoe_0Sx_VCkrO3dNtSgz4WSmf9oKPxmvbXBi7ZLnsU-9Pt63yiQexeO20xTIWtvSclb7Rc1QuTVKdIW-yFb4K5tW1SBBVTxXyhAmgxooQqvefXfREhKdDXKXE2OPWkVOomtdcvxdu5yShPqHJazXxUJJNjEZAvAOszVcHrGTblyAURlNETop0RnUERW0j3W6fsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=byribveG401hDaKI6M88rP1r_kJARdEWmkypNPtGNuGSgbKIet1-j2Qy7l_Eiw-yEgVzwB7nkEPppZMdlQERbN-uISARO7PpybXQPC22X06Q_pYmHhzQnEvZDubyzevxIGvOfwwVVqqHiwnOucC5hulEX00eosdijtu0k_yyQX3qCNiQFmK1ThtKOXCH-oYlfATjvUYO3N1gZAcgHwE7bBDuek_V_Rxrrgt4zcsaP-DBhquf3gjDv0TX6TuKFQKukRijpOPpdEXjWqmisJn5JNhSDdpeusHZepHjvAONTP8r2ss9R5ftU3ctLX-8gg4iMFi96VbIXO-Ue4BUKMC0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=byribveG401hDaKI6M88rP1r_kJARdEWmkypNPtGNuGSgbKIet1-j2Qy7l_Eiw-yEgVzwB7nkEPppZMdlQERbN-uISARO7PpybXQPC22X06Q_pYmHhzQnEvZDubyzevxIGvOfwwVVqqHiwnOucC5hulEX00eosdijtu0k_yyQX3qCNiQFmK1ThtKOXCH-oYlfATjvUYO3N1gZAcgHwE7bBDuek_V_Rxrrgt4zcsaP-DBhquf3gjDv0TX6TuKFQKukRijpOPpdEXjWqmisJn5JNhSDdpeusHZepHjvAONTP8r2ss9R5ftU3ctLX-8gg4iMFi96VbIXO-Ue4BUKMC0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=lfpwq6D8x8QBLoMqfOQ72B98vIK9-ql6StAKE9eh8pnCydy0rayimPCXAlH59CTYsJYYAlNZWBgLGQzDPM1UdpoKFrw_aXCL6bXJCi9eJ-TrJRcBAFqvXt5IrJ4n5LCgGMbPlJGy1oBxqMh7LDl-dX-O1qVtnUQ6G5ooUllEYxLo_Eix1sVNeztIHVVxs9TbyhmndeYe_F_LFF5PyNOH6Jph7phdsbN5tHlR7obCbQ7g05ObaA8LODa5N7YDPj2qlEjCVcfOBNnNNbjS17wZBd1ABEdmtN0rR-mi46VLbFiHRHVEy5j7KQWuqb3WjziY1laEjyLGAVRsDMy9pLjyoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=lfpwq6D8x8QBLoMqfOQ72B98vIK9-ql6StAKE9eh8pnCydy0rayimPCXAlH59CTYsJYYAlNZWBgLGQzDPM1UdpoKFrw_aXCL6bXJCi9eJ-TrJRcBAFqvXt5IrJ4n5LCgGMbPlJGy1oBxqMh7LDl-dX-O1qVtnUQ6G5ooUllEYxLo_Eix1sVNeztIHVVxs9TbyhmndeYe_F_LFF5PyNOH6Jph7phdsbN5tHlR7obCbQ7g05ObaA8LODa5N7YDPj2qlEjCVcfOBNnNNbjS17wZBd1ABEdmtN0rR-mi46VLbFiHRHVEy5j7KQWuqb3WjziY1laEjyLGAVRsDMy9pLjyoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=KTzHXpEQ98n9XsOiDxyTKkdygh7uYw3X3YSr3jZLmBIJzIHUh6K6k5-NkQaSQDWRtn5b7kYmLIDnxnRKGBFyRnetC3g7tW-GB1AWTddRUXjag9C73ifKbCQ0EyhkSKCLky5KsFpmWJU82M6w35zgehwgOkLmhCPye1IjF5a027Z7kzfo4gQrhttap8JBewqGvamahfdjCbtBkI-wEVtWH6ypPRuj0FcdbEyADr-c6zyraNGwpS7kmDk1nHDWb3JrAMGq1hSwL-6uJCLYbgAf07wi4w7oc5PQhhFNqdcF8eLZU9OHk0vSV2fUHja1nTy30tadFN-M4HQUT9BRkp1PAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=KTzHXpEQ98n9XsOiDxyTKkdygh7uYw3X3YSr3jZLmBIJzIHUh6K6k5-NkQaSQDWRtn5b7kYmLIDnxnRKGBFyRnetC3g7tW-GB1AWTddRUXjag9C73ifKbCQ0EyhkSKCLky5KsFpmWJU82M6w35zgehwgOkLmhCPye1IjF5a027Z7kzfo4gQrhttap8JBewqGvamahfdjCbtBkI-wEVtWH6ypPRuj0FcdbEyADr-c6zyraNGwpS7kmDk1nHDWb3JrAMGq1hSwL-6uJCLYbgAf07wi4w7oc5PQhhFNqdcF8eLZU9OHk0vSV2fUHja1nTy30tadFN-M4HQUT9BRkp1PAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=dIjuEhsC6yGJezvUpVNobjG2b4GB1pNmqw4hc06ifIU8OeBr25mGQKBWqqoYClNXoTKkLSbcHhWyZKxL9bV6jpJENHgQ8Nth2oejH_lPj_zmb7dN2tmXrXahT4EBYyEX0a1K9-nsrcbPCfv1XgL96nUh6S6aRqTMod9ZMRKrKa-UU5jmWfrwsdOfq-3mYsO8dywEdZOr0Y-GkKPbxmUdguFol2itDKo19ZpjYv_KJSdUYCmE303Vfu6qCFkue8Rx3f4Fe36L6YY0YfsMSBVtR8JdNNlWCw3rysf3rqTPIhEa4dwrlrW5_oI_yGiQHfnCg-BNxmGh-rH-k7df3fpZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=dIjuEhsC6yGJezvUpVNobjG2b4GB1pNmqw4hc06ifIU8OeBr25mGQKBWqqoYClNXoTKkLSbcHhWyZKxL9bV6jpJENHgQ8Nth2oejH_lPj_zmb7dN2tmXrXahT4EBYyEX0a1K9-nsrcbPCfv1XgL96nUh6S6aRqTMod9ZMRKrKa-UU5jmWfrwsdOfq-3mYsO8dywEdZOr0Y-GkKPbxmUdguFol2itDKo19ZpjYv_KJSdUYCmE303Vfu6qCFkue8Rx3f4Fe36L6YY0YfsMSBVtR8JdNNlWCw3rysf3rqTPIhEa4dwrlrW5_oI_yGiQHfnCg-BNxmGh-rH-k7df3fpZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=HtmI-nifJijP88j-h7kN-475Gb46mwYS6c_76cOAJpl6LvyXbVIIY-kQVtK771yVHCjKVLHdoAVkwKCrSU9MVVYUZ4qDbKaUustln03PNhQQIUbqlCmGX1AA8IgN3CLp5gcvdFSycXckcpjdO72yrrb73lQWMTeEJJr6no4B06wAh8WJYLSmuGQ9-8V_vN3oKSdEWjylTUAT4c9-u9UxGx7t62qdBq2P3V9HPHtb5kylcey0rhDsMzvG-shF7YgX7Bpwz6cwlrHVEv6U6D7bzqA2AkZ4oppNfQ6S2ckr6bU6VoljT_zxeuQwVuupQXkY0iyOj1KGlMuYqHMp9_4pa65vN2ISztIdSHHFimKfdWF24R1A4Wogd5ewx0sARWqHrofYyQ2nTWrgmvvjAMwZcTo5zaG_GrTuVAYcNgwOrUtPvGpRgojH3nf4otyEgQUhTETbhymxczmERHfsgOydOnD8RdHZnvv0Zghd91flwdxERN-Hcp3tk6IMblPgG7QpmeUg02cDnLG7nQ061o3cJ4uAn8V9Ui7k4q2dwzuNFP9QmGL5tz3IF2aWAG2-gN4qJvldcZqA-11MYuJBP5V8NiZk86aGNb9GBxwFXCXWaI3EsCUa3ihC2eSPBLCnppUFuh2Vzg4oG7pBCRV4uiFEuFjkiDAjxKFdE93eWlOBE6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=HtmI-nifJijP88j-h7kN-475Gb46mwYS6c_76cOAJpl6LvyXbVIIY-kQVtK771yVHCjKVLHdoAVkwKCrSU9MVVYUZ4qDbKaUustln03PNhQQIUbqlCmGX1AA8IgN3CLp5gcvdFSycXckcpjdO72yrrb73lQWMTeEJJr6no4B06wAh8WJYLSmuGQ9-8V_vN3oKSdEWjylTUAT4c9-u9UxGx7t62qdBq2P3V9HPHtb5kylcey0rhDsMzvG-shF7YgX7Bpwz6cwlrHVEv6U6D7bzqA2AkZ4oppNfQ6S2ckr6bU6VoljT_zxeuQwVuupQXkY0iyOj1KGlMuYqHMp9_4pa65vN2ISztIdSHHFimKfdWF24R1A4Wogd5ewx0sARWqHrofYyQ2nTWrgmvvjAMwZcTo5zaG_GrTuVAYcNgwOrUtPvGpRgojH3nf4otyEgQUhTETbhymxczmERHfsgOydOnD8RdHZnvv0Zghd91flwdxERN-Hcp3tk6IMblPgG7QpmeUg02cDnLG7nQ061o3cJ4uAn8V9Ui7k4q2dwzuNFP9QmGL5tz3IF2aWAG2-gN4qJvldcZqA-11MYuJBP5V8NiZk86aGNb9GBxwFXCXWaI3EsCUa3ihC2eSPBLCnppUFuh2Vzg4oG7pBCRV4uiFEuFjkiDAjxKFdE93eWlOBE6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=jd9F9dTQtr3laxJxvCvAHL-l_w8DEfgn8MRxdudKtCZswzJ3aMvAqRnpPwBx5zMwlQPT4YZb4uAAPCH6jsyAN_0PYFk_vX2pkaL-MBYCFC1ALkSWRAB95nwS5T64IuuRsCMi-3gxuiFhLlxilrEaL0APwWRer8iDELYJgzVR5Srdxt4W8-mmhPVpvSsA-kR9WTwImZE2h492TBI006uKpCyqmOt5EjAWC1h8o8ayclLBWL2OX8Emqa-7J8DCnpnTLgXtor8hcoF6TGUHShIvTOAy3U1cEFj-mkf1eBG2C9J8tjsLURG0Dc9O9ZzTxF8lFRUn3oWDA0ytOp6H0tKhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=jd9F9dTQtr3laxJxvCvAHL-l_w8DEfgn8MRxdudKtCZswzJ3aMvAqRnpPwBx5zMwlQPT4YZb4uAAPCH6jsyAN_0PYFk_vX2pkaL-MBYCFC1ALkSWRAB95nwS5T64IuuRsCMi-3gxuiFhLlxilrEaL0APwWRer8iDELYJgzVR5Srdxt4W8-mmhPVpvSsA-kR9WTwImZE2h492TBI006uKpCyqmOt5EjAWC1h8o8ayclLBWL2OX8Emqa-7J8DCnpnTLgXtor8hcoF6TGUHShIvTOAy3U1cEFj-mkf1eBG2C9J8tjsLURG0Dc9O9ZzTxF8lFRUn3oWDA0ytOp6H0tKhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=LuZ5DS3idRLtpOWimBhQ99forUd8WUFZ3sXPIps7_meUbxoPGlFP6zjxLmKONPyPL3UjSw2oUPgP0D4-0YgJVSAPGQ196pd4FeE9Bkg2RfWqNVQSKniz2RxJHTtLy32wC5UeEdQjIBMJaUse8u47rDlZIjrTyLBQaWqeG4sfeulgQ7Yfibcg5B5BckNRR_l_gVdbSXvtk5AypgkjTlyJUPO4b7ardSa7ZnNq65r9s3Dc8njTh7CGE_YxF0muOLE8iHszLdL0ruUTZdXrpvfOVPnwlKyPfAe5DTY08QIaYsdJkcsC0mylU1d8rly82HF6eYH3Uc8k6SMhDj_E8PiCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=LuZ5DS3idRLtpOWimBhQ99forUd8WUFZ3sXPIps7_meUbxoPGlFP6zjxLmKONPyPL3UjSw2oUPgP0D4-0YgJVSAPGQ196pd4FeE9Bkg2RfWqNVQSKniz2RxJHTtLy32wC5UeEdQjIBMJaUse8u47rDlZIjrTyLBQaWqeG4sfeulgQ7Yfibcg5B5BckNRR_l_gVdbSXvtk5AypgkjTlyJUPO4b7ardSa7ZnNq65r9s3Dc8njTh7CGE_YxF0muOLE8iHszLdL0ruUTZdXrpvfOVPnwlKyPfAe5DTY08QIaYsdJkcsC0mylU1d8rly82HF6eYH3Uc8k6SMhDj_E8PiCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rsNZg2bUmpKobhXjmU0XlkxkJL-BsAi3A-v0irto_HTywCb2DZQ82u46i4w7LvkYEhn9YsSO40gXx-Z6YDEb4Xzz9gKD2ZiDZwsxiyck2v1TUJNYnhcu8CMR4xkJNegnXOb1669XMxu0gxmwORxBmXUnNnXI_NktoTW_NcOEGtnt7wQCzqB4MacARpmt75j4oBTa35m5uVy_jUV3bta5kVZVu0pVdguh1CyKDUSLGYDlwNuRTtH-rpuNaFjkSTQO12qCybQEUCvwIvqfWwVKgLw3lZamVgxE6VtMIA2e0ZL9h8kNcDXwaVoWm9lCHmu_-R_3P7lhsvgR3BFnPGN0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rsNZg2bUmpKobhXjmU0XlkxkJL-BsAi3A-v0irto_HTywCb2DZQ82u46i4w7LvkYEhn9YsSO40gXx-Z6YDEb4Xzz9gKD2ZiDZwsxiyck2v1TUJNYnhcu8CMR4xkJNegnXOb1669XMxu0gxmwORxBmXUnNnXI_NktoTW_NcOEGtnt7wQCzqB4MacARpmt75j4oBTa35m5uVy_jUV3bta5kVZVu0pVdguh1CyKDUSLGYDlwNuRTtH-rpuNaFjkSTQO12qCybQEUCvwIvqfWwVKgLw3lZamVgxE6VtMIA2e0ZL9h8kNcDXwaVoWm9lCHmu_-R_3P7lhsvgR3BFnPGN0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=vXh2UBCogTgF9j4DzSAIlIoDQCoqQefQgYRvVgNHFBKV7feDQidLsxcwJK876Ia9NTJmL_Fzn1dLuB1djj_Nk94rGM-we8rZLEeHO1Ik1BU4augwo-BLrNE7Mjavg2odOxBsjvDHKKy3_sssPfAI3bwdZrfIA5h2aC9c7wExn5OAxO95cOUzWz6mxnjBFTZu6oOL-8hP8dRYVuV504FAfIBh3B8LImK94zgmWrOOOs4vEY8tdioiv3OHGcA3PjFS66L4yqhMDy6wWLqjDwFiu3IxswHOeJbnLyILGY1ieElV27a_wMwnfrSbh6YZzrtQOvg40VHj5581ct2vjMDOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=vXh2UBCogTgF9j4DzSAIlIoDQCoqQefQgYRvVgNHFBKV7feDQidLsxcwJK876Ia9NTJmL_Fzn1dLuB1djj_Nk94rGM-we8rZLEeHO1Ik1BU4augwo-BLrNE7Mjavg2odOxBsjvDHKKy3_sssPfAI3bwdZrfIA5h2aC9c7wExn5OAxO95cOUzWz6mxnjBFTZu6oOL-8hP8dRYVuV504FAfIBh3B8LImK94zgmWrOOOs4vEY8tdioiv3OHGcA3PjFS66L4yqhMDy6wWLqjDwFiu3IxswHOeJbnLyILGY1ieElV27a_wMwnfrSbh6YZzrtQOvg40VHj5581ct2vjMDOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=jbjrxtwJofk5jh2tldwPzE2FR5Ze0wYb45gmdrylZm9oseOTX5iBuNB5h0crbvpSy6-vo-f4uBb3c8G38Kn6_U2fhukSL5HexsRNU6btpdY5yXNbawd2V0PvkPc0tAMKYo6GBnpeEkqDFQ9zYdnjKJKLkI2SRFiUNte2UHn-WqvjYfI4BVSM7tIalPUGe6zEh3HHYUom-rpaP4_5q_XRz6__dSBhDYY8hHD1yVfrEmVl47vnCxlIGhOy4qhqrnpkDa79jJRHfhlzUM1NgXczOaUbwaQvx3Md-B3mIPa6UHBPWqzQX-HdvpC5FbnGg8-fREQkWjlgE2ulAqSZwgIwXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=jbjrxtwJofk5jh2tldwPzE2FR5Ze0wYb45gmdrylZm9oseOTX5iBuNB5h0crbvpSy6-vo-f4uBb3c8G38Kn6_U2fhukSL5HexsRNU6btpdY5yXNbawd2V0PvkPc0tAMKYo6GBnpeEkqDFQ9zYdnjKJKLkI2SRFiUNte2UHn-WqvjYfI4BVSM7tIalPUGe6zEh3HHYUom-rpaP4_5q_XRz6__dSBhDYY8hHD1yVfrEmVl47vnCxlIGhOy4qhqrnpkDa79jJRHfhlzUM1NgXczOaUbwaQvx3Md-B3mIPa6UHBPWqzQX-HdvpC5FbnGg8-fREQkWjlgE2ulAqSZwgIwXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2U4vrLJOk9q3zmt0JeXLRzhSpW6mS7HBq5L2WygYmB6yU4qpEnagRIiRSIjV5ths21OxlJMBoZbaS1NMLI4PP2Ss-cmQ8uMIbS30ZB0UfeI61pJiA2JN690hRaLlNvK8-YGYdE7F7hmRZwBbbUK0JLdHbXr0G3S2MgfyOhj4FuZ5rPxE3YqvcNk84gu33A4jpc0iYnku1Zo7J_q7K5jjZyNi-JL8lcfyfzMctmSQlJX_PDG2doT5Q4kzo6V-3njE4jjiu6qfjOYTSV3SffLdmYVe0LEOMqkUWjuW93gxoZOY7is19eLlRH1QL-NJWCanfGzjG9tPK9874IlHdweqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc-sVvzZAoxn2t1ufRwgKFBy_7jd7mtTsantKSooSRa9f3_OWqvtic260fe6kriabDKO-9YVd4Oi8szHfQ3cK4c7i8TF6dcoMI_efDumCoQ6hzU7PxQTnzaAgos4bvXTMfhgt9w6pLuo2R1yvMk8xvW6AoRqikIhnHJYCfxOp9HjFaWeSItV6ubRhzsSei35IGZKhJ_jWaHIA_ucd22V0INwwckkWI4Mqmde2hqgCDcVp9-zJk9__KwskuvXZkSvVFsLHMRQCSZTjhZil9d_fn4YVm4ZgD8y_GgfDBi_LeYZQTttuQeC-Zwmn-n4NAw4QiVRZrWX-HBHi-RUs_7SMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvalqrFyqppavsaQHobC2aQ8DWkgMHJEiang7a75Pishw1QJ_KNwcV015LG8L7HvZr8-wXP6Q7s60S3eQTVMJHj_61nUGaV5iLF-u0PpmfgjVsaH4oSMNMhwwwr13DB_D_LR9d09mOtA7C-gxOAT5DVwqpzAkHwTq1amJrPMv_R0r08EcFrD3F2kfUwL9cXMcvT6E-Qgu6oknyhz7Gwum6f46bDh3w-6Y8HswzdHlLeVp0yehmuP0ZCnp7fh1xT3q7UKiV89WIQrA7_Xm_bG_vZHDsPfdAGX2Uz1Pd2MLr2gKGhdR3cM2ErjgWAaDOpRKWuU7w1SEg-enFO0Cpz3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=ivZ6xTBxOUKu-qQ-4O3nw0Bg6zdZ9ktlyKOUZpyoVWOVBSqXIAARt5PLHobrkkW7KelJvyRd8vzObfLf9zcjY-D43VlvDuhxDsIJXLiaAeKpzOm5nm1SQ8IGSHI9EnqNaDIiHbYhJmWlUUO_qqNc2OA60brvTkpgtBXsiBoWdRfLQDNNdaiJPOpayw7r5R0DNV69Yj3_7angm74NfExrKObH_nZFERBvZwBnOR2AzPkNxH6bFSMlyhouPx_na1XNBM_U_gvxFfAV3eFb4jZeqLAJJBdHuGrH8widt606fhmjLOVl7dnXzf8Vd6kaNKUOaZSD5oYVPnsMeJ7Y_m6aeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=ivZ6xTBxOUKu-qQ-4O3nw0Bg6zdZ9ktlyKOUZpyoVWOVBSqXIAARt5PLHobrkkW7KelJvyRd8vzObfLf9zcjY-D43VlvDuhxDsIJXLiaAeKpzOm5nm1SQ8IGSHI9EnqNaDIiHbYhJmWlUUO_qqNc2OA60brvTkpgtBXsiBoWdRfLQDNNdaiJPOpayw7r5R0DNV69Yj3_7angm74NfExrKObH_nZFERBvZwBnOR2AzPkNxH6bFSMlyhouPx_na1XNBM_U_gvxFfAV3eFb4jZeqLAJJBdHuGrH8widt606fhmjLOVl7dnXzf8Vd6kaNKUOaZSD5oYVPnsMeJ7Y_m6aeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=ZQuiA1uI_-XnVokhDtaJERCfhEnEkytLEHRKPK9itXee3LMqeiHsbsxcWOYIArlOHZWovDTNe0HaM6rm1l2w3zDMWq948TIidbfQDw2cwCdCuCn8tDK3vJh02CjRx70Qn_rI7_yKhTP0mqwbFjgGlR22st6NN5B0OeF5FpP4CEo0L529GoWYoaf_-Eg2VoQd8PKB45ykI37GZospnU73SZqs-bmJnwjlijJreZydjvkDWF6-DNvgjsp-Rp01vNLUGgufs-So_8jp6DUkr_LndZWQtPyCnTWLpst_z3M4-wAz52P1vNIdgD00PSLJNSdFfMC1--CBSPo6P8Sm0kRdSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=ZQuiA1uI_-XnVokhDtaJERCfhEnEkytLEHRKPK9itXee3LMqeiHsbsxcWOYIArlOHZWovDTNe0HaM6rm1l2w3zDMWq948TIidbfQDw2cwCdCuCn8tDK3vJh02CjRx70Qn_rI7_yKhTP0mqwbFjgGlR22st6NN5B0OeF5FpP4CEo0L529GoWYoaf_-Eg2VoQd8PKB45ykI37GZospnU73SZqs-bmJnwjlijJreZydjvkDWF6-DNvgjsp-Rp01vNLUGgufs-So_8jp6DUkr_LndZWQtPyCnTWLpst_z3M4-wAz52P1vNIdgD00PSLJNSdFfMC1--CBSPo6P8Sm0kRdSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnGP2rTylmQ6BHKHR0fUsCg03O8MktNEvE8yzivdRCf9SoEgPcYxYAh8AsUlG4czpiUeTYqSzdiz1UUroLrQ2cCqLjIi5mUnt---JoENESzovsGvpkrzivOavInQigQiT3IOStrkswONLeYs8HEt14tHnaByvNYB_yUZACyQkKENZBFhN6ncpIFC3cFNgyc0AzZHEUAoovdqEkNOOpP6yaXlhrHqhQJhJcAIZYvfD9gJ3nJyMgllhKEWOf-SNZ2GiaPeyKQLw7QojINkLvIqJp0FNrTPZ-YKIY2Ajx6R7788DeDu-1nWITSpXTwLcNvrshIzbr4fRFGwUb7823gmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=ggqXPwxojSCc7iyDeJAUNfbxie-hloT_cqoqsaNLVl3N2dAJAXXLd1s-3L9hl86j2j-8LWZneE0i864xG5x40uEW6bphFyPU_Zg_9UQeP3g50vBdfzykxS5oI_qAPCGcpKxDO2E4q8Nt1qQdpkLwGzkK_Qp50EsX1XdyBa5KW1GcxU89al6OuhNi1G3rvHJcy-0TRT8yfiLAW5ijWDuwxZIxFET432zHxz1cUTcZJPrQhjLDHcGODULSk2gArK1Fr0x66nUKN7usUiVHPSZDCgi3p7Jnc8wY1MQdRP3j48MZcWLrpJtjDh8gAl-ugGRmhY6n8BWNRdpiEtEmQj4osw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=ggqXPwxojSCc7iyDeJAUNfbxie-hloT_cqoqsaNLVl3N2dAJAXXLd1s-3L9hl86j2j-8LWZneE0i864xG5x40uEW6bphFyPU_Zg_9UQeP3g50vBdfzykxS5oI_qAPCGcpKxDO2E4q8Nt1qQdpkLwGzkK_Qp50EsX1XdyBa5KW1GcxU89al6OuhNi1G3rvHJcy-0TRT8yfiLAW5ijWDuwxZIxFET432zHxz1cUTcZJPrQhjLDHcGODULSk2gArK1Fr0x66nUKN7usUiVHPSZDCgi3p7Jnc8wY1MQdRP3j48MZcWLrpJtjDh8gAl-ugGRmhY6n8BWNRdpiEtEmQj4osw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj1EpX9rATgkloBntZWoSsk4m7yIF1sbQ-s7QAoU1RFKPKROzBywEmJqpHKsSxTFzM8s1a99it2xvgZXgvY7mx6Evk2qDAUW0jAPjsYLbxAbClWum11_fv29klhRn_NnXIgqdqmbw_EeA9Hpf9Xbn0C0XP8Sw5Y2eBNldtRDZ77zSZnbbLk9_QOeD61GdNzeL-W392rKtR9qVsWmlgVY5TmQ5QTZey28L88QMarv7ONnNrJJnfFBHi9_OqI41iO6TJ5l6yIYrKjfQg3LFB-nZ5fS-gLJIDgqCUeAGoXxI9RGMvoobG8saeR5hEJMjVOUihTVtPZk7QcWyAN9wDkbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=WSJ70_58iRgVxbxxlP6ansRvvTzXNVCvBOlG3-sR-pWMcXZS5T2mX4_P8uQE5J7EFX_MbOF4VeGHcaFxjM1lDfV6OSUoBoVCbUaMIry8NwvCA4M0uuds3hUbpzG3Hkivu3J8byQP7FnO4g_I_70zCAAUQ8hgcCPLtW_EA90l1MhVa-TziqMB-vEtG_2O6pRQlsLVoF00ku5Nij6H7HAt9X1p7IluBZ0HOsiXxDCetKi6ZGoe_nF25cztg-alhCXTneVDrq7gNPDouf2zACloEVYaX7O6rYauuQs4X8uP68Faf93RDC3ifBFzPz33vM2Xp2VYKxlW2pyPkdXb1KWSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=WSJ70_58iRgVxbxxlP6ansRvvTzXNVCvBOlG3-sR-pWMcXZS5T2mX4_P8uQE5J7EFX_MbOF4VeGHcaFxjM1lDfV6OSUoBoVCbUaMIry8NwvCA4M0uuds3hUbpzG3Hkivu3J8byQP7FnO4g_I_70zCAAUQ8hgcCPLtW_EA90l1MhVa-TziqMB-vEtG_2O6pRQlsLVoF00ku5Nij6H7HAt9X1p7IluBZ0HOsiXxDCetKi6ZGoe_nF25cztg-alhCXTneVDrq7gNPDouf2zACloEVYaX7O6rYauuQs4X8uP68Faf93RDC3ifBFzPz33vM2Xp2VYKxlW2pyPkdXb1KWSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=ADm8F9x4UdjKuIMdd0zDo1Kc87CVs-ngD02ZoTviKC336Mv3FiIvZ4Y_InzPNMxrVxNryFCkS5-VVpe_skgKcXZqNO2MeKLaIZni6FlacKncz_pFyABJGW1oIq_8iqcABC3lOoCf5irgyK0QF5snokrvynnp1LVmXOIFfCl16qf3cKhH5uZO3LwajOnGLV5coYWez2UZ0Lyh6TqL0l7E74pEYOVX20BprF3ctUZOPp7JolyoXzamH5zK1zJJADB7aFOqiNUcoldK0N0CVCRYfmiCAnEz7e4yQDDYW209SGCAIQyJ4MeSaCzhQOgU8pVF5eCiSsalCnetz9XzSe7jpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=ADm8F9x4UdjKuIMdd0zDo1Kc87CVs-ngD02ZoTviKC336Mv3FiIvZ4Y_InzPNMxrVxNryFCkS5-VVpe_skgKcXZqNO2MeKLaIZni6FlacKncz_pFyABJGW1oIq_8iqcABC3lOoCf5irgyK0QF5snokrvynnp1LVmXOIFfCl16qf3cKhH5uZO3LwajOnGLV5coYWez2UZ0Lyh6TqL0l7E74pEYOVX20BprF3ctUZOPp7JolyoXzamH5zK1zJJADB7aFOqiNUcoldK0N0CVCRYfmiCAnEz7e4yQDDYW209SGCAIQyJ4MeSaCzhQOgU8pVF5eCiSsalCnetz9XzSe7jpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=esfy8hXVkuZMOOCEtxO82KvDPJcT6phj0GSVMmxnUxM1Sb6sbgMiB07_gbPTMoziRuwcqMK6P5le_tVVcpgVs9GfqABTi2MMDB7lwrUYwMOkVEvv7zOksxFG_NIoP336SL_qDQ7yH2MPbW0yMduJVXnRfzF7KRs1wUzaKlo6FQCYSZ-6Zrn3QEcptSFHxaLnkYgEwGstXVVl679wBSO-m60N_i-W4QFnSI_M3qOj1FOOwXxaF3uN9mGU_7gAhOe0aVFJs6nd6h_sukWHZxekgW-eyab-cLi_pmMxuMob5vzTaKzhM5Y3HSHgWsTnLsSN29HWskUDodWdzHCeX-7TJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=esfy8hXVkuZMOOCEtxO82KvDPJcT6phj0GSVMmxnUxM1Sb6sbgMiB07_gbPTMoziRuwcqMK6P5le_tVVcpgVs9GfqABTi2MMDB7lwrUYwMOkVEvv7zOksxFG_NIoP336SL_qDQ7yH2MPbW0yMduJVXnRfzF7KRs1wUzaKlo6FQCYSZ-6Zrn3QEcptSFHxaLnkYgEwGstXVVl679wBSO-m60N_i-W4QFnSI_M3qOj1FOOwXxaF3uN9mGU_7gAhOe0aVFJs6nd6h_sukWHZxekgW-eyab-cLi_pmMxuMob5vzTaKzhM5Y3HSHgWsTnLsSN29HWskUDodWdzHCeX-7TJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=nUIrQNnzlQGJ4MrsOALaicxFwr1me--KrkY79CoML-yAYp77lUdf3oHlnOwLSbJ8N4umTXiyv0-R2n4aFjpl2y2l7JXm0fM0ktsm1HcPBPGwOVyz_BHEdJ51FgiHD8cFoHvWEQccBr0esan4-rF9IYRKDc57WNyJjtIT1iFOnxdOjv99IhqUu96myHNjYXkvzO0N3ACJ6nAqCslzCyM3T46XeTZY-3tkQlu7fUK2FgVu7txhME8LlPvFgVZwTXo2E5TYwTRciUuyc3hFhY8pkwlWESb1SkL75AvT8kBQuopxGZIJUrgRgyXLVFWu68J9Fkjxe1cA8CM-mKb9mYEXOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=nUIrQNnzlQGJ4MrsOALaicxFwr1me--KrkY79CoML-yAYp77lUdf3oHlnOwLSbJ8N4umTXiyv0-R2n4aFjpl2y2l7JXm0fM0ktsm1HcPBPGwOVyz_BHEdJ51FgiHD8cFoHvWEQccBr0esan4-rF9IYRKDc57WNyJjtIT1iFOnxdOjv99IhqUu96myHNjYXkvzO0N3ACJ6nAqCslzCyM3T46XeTZY-3tkQlu7fUK2FgVu7txhME8LlPvFgVZwTXo2E5TYwTRciUuyc3hFhY8pkwlWESb1SkL75AvT8kBQuopxGZIJUrgRgyXLVFWu68J9Fkjxe1cA8CM-mKb9mYEXOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
