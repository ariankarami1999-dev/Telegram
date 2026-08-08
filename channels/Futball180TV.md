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
<img src="https://cdn5.telesco.pe/file/tqoMP-1cN6sKFKE8UDgwcbpSOXklCWtoCaa1nzb2dcMx2BoGSfOmZGWQmVj_Hd7TBB6YIjNPF1cwY9r1R2pz_TMEMLbPl_gtBqJJsZrU7sGBHHfubZonRmizFbs4JIhptf-YtztRxci_lEfRGFfLJWYNshxZvjc3f9MetYRYBXrBBiD5FguQqtuXxDinCneC6lLHqt22hkxeUQ336Q60MgcZVNO3JCVLMtYK1GIUgKHJY-pk6Zbn2Kmhlv8N9goHOqTbPeuCzxEQiRQBTMoaDUZwe2DO3t7VuPUavAlyb3QYjhQ940CQMK046GKhH3e5ccdzgPgwY3E6kBrRZ3-fUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 484K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 19:51:41</div>
<hr>

<div class="tg-post" id="msg-103097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=fysqqQ3VwXiDnFIU9pSSbIaz7YQyAGlkn8JMwKfhoTMKcE7jRr8oDVi2he8G2qM6Nvk-qqP4uVnTslOd5twvv5EDDH2Mwta5AZEoaBh3SOTfZFBQMBDZDs0JerhbYuVNht-__NXJO0Y1Wj3M42HIA10cdzImiMhQZnLtLpvsj9Gr0OcYwLWzV4ck745pL2l5oOT-yqJN50eMy6xZhDmGTiMLdLodUmROYOzKigiKgTS3hihzj9V5fHjFkv-umitkDeI40HlnmtRza-F9K6dIxvz0es3fXp5twkA7_r9mPny6FZ9z19bA879vsPiQvQYnB1gm01mu34Fw-h3jWNGGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=fysqqQ3VwXiDnFIU9pSSbIaz7YQyAGlkn8JMwKfhoTMKcE7jRr8oDVi2he8G2qM6Nvk-qqP4uVnTslOd5twvv5EDDH2Mwta5AZEoaBh3SOTfZFBQMBDZDs0JerhbYuVNht-__NXJO0Y1Wj3M42HIA10cdzImiMhQZnLtLpvsj9Gr0OcYwLWzV4ck745pL2l5oOT-yqJN50eMy6xZhDmGTiMLdLodUmROYOzKigiKgTS3hihzj9V5fHjFkv-umitkDeI40HlnmtRza-F9K6dIxvz0es3fXp5twkA7_r9mPny6FZ9z19bA879vsPiQvQYnB1gm01mu34Fw-h3jWNGGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول دوست دختر سابق یامال:
یامال ازم سو استفاده کرد با اینکه من دوسش داشتم بهم تکست داد و گفت هیچ وقت واقعا دوسم نداشته و فقط دنبال سرگرمی بوده، من کل شب رو بخاطر این پیام گریه کردم. اون خیلی دل منو شکوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 306 · <a href="https://t.me/Futball180TV/103097" target="_blank">📅 19:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103096">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKqfVj4ANBaqfUKqinrXxWQLssw8T0mTGHIAcm7EnUy7GqnKS1Pv5daHurKODAfGCdXvRb_2BIF_-tSGK73A80mjGgN7zauOX-XaLUqkAu4kBMtJwfB1JzBhuxBoj2kC7oYy9TUJgeKyX6IIiMurv5B2XWDjTFb6I8Zxc87xtyoRS6fcMg0CkDTGITBSzDwJfQJir2YHE_j6iDjExiVgBOvEDvUcGx-V2mVqtVPR2S_Et7paCvKyGJJa8BWa_ONwuzDKVz0OHPc2Y-hAKNOgNwcCx3_PI4H0vp89uH_z2nmuGdgavr8J4WIGNTdHZ81aEDCTw5g2hlw0V4EXw8qtiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی جدی از اون نسل طلایی آژاکس که نیمه‌نهایی به تاتنهام باخت هیچ کدومشون بازیکن درست حسابی نشدن تقریباً
دلیخت، ون‌د‌بیک، زیاش، نرس، تادیچ و اونانا
دی یونگ یکم توشون خوب بود که همیشه مصدومه؛ جالبه همشون هم سود مالی خوبی دادن به آژاکس...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/103096" target="_blank">📅 19:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=P8ILGAJlFC4hivnl5o2dCWNDj2kRTl2WOdrGEwChhcHUHt8fz04aWEoWS9CRTmiRKIxkSTVyOfMwi2Lorf8R0nRrMrwUsZE6Nd_3sFikzf06HEqhpR_RTqRC5aIxuhMYQnPcrUQK9D7dL6iP9-lfDfvxl45vWLySCvHwa0O9F9EguOrcXWmbR9U_DD2C4FW3qaTOzEg_nkl8ayUTVq4SDtdQmG3zSnBEIRnI7vp7Y181Q0ZmCF9khgDy2UAKu_Ftb_ZItGF-Bi89VuBlTojdeiQDiOlMNIHiBOSy6CPLzbhhf8Yy1rpkRX4B1GW6HJt76rRj7L-wdrhwTPBl6dupXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=P8ILGAJlFC4hivnl5o2dCWNDj2kRTl2WOdrGEwChhcHUHt8fz04aWEoWS9CRTmiRKIxkSTVyOfMwi2Lorf8R0nRrMrwUsZE6Nd_3sFikzf06HEqhpR_RTqRC5aIxuhMYQnPcrUQK9D7dL6iP9-lfDfvxl45vWLySCvHwa0O9F9EguOrcXWmbR9U_DD2C4FW3qaTOzEg_nkl8ayUTVq4SDtdQmG3zSnBEIRnI7vp7Y181Q0ZmCF9khgDy2UAKu_Ftb_ZItGF-Bi89VuBlTojdeiQDiOlMNIHiBOSy6CPLzbhhf8Yy1rpkRX4B1GW6HJt76rRj7L-wdrhwTPBl6dupXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از عروسی رونالدو و خانمی
😃
😃
😃
😃
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/103095" target="_blank">📅 19:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbzQxgEdB6TNZEOSspf51l86zSTDwnrM_PafFkGUOe4P9JneXXmmg-Gr4bZ8Yp4oxqYv4vttP9oC-VA12tw7NzewJVGpjAttoZ9qA3uf57nj_ttByj4v6Dw3dgBMqp3jBClU5uJe8ZJbZYcuNoGq5yyFVt-fR2WXfSC8_9GqoNm0NP0spZjahR5sX8VmMd_IheIkUHRKejbybNv5RcI9QuhX6U85FKzQpXFE8uQ3-lrnwyLXENZyUUO2mj8q109BlRIK1ON-deixPPtWkJUeoNt39rUHkpQigcm-sGlsCrJhWrMJHdmHiVzZBeRv40q2vOOcwWMymNBb22ZjKRZhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQ4PYnNuuLJoIbm-5eL9QQN5MDi1Xzepvt6Rc-jnQZ76-ls6nM2cQT2KBQefe9GVHp2OLT9Lc3AaMs9toXydNmtc55ERdaDNxjVCsahXVtlGsByn7xR9175zppHIF417eL3VA-niQXG54H8LXuW7gI6cbhvPuzMT09KIf0B4hghYnEDxbC-iLdwhk_2LAfcwXcg6hde1rVUnT8KIu8E1NIvNPNBg3p5-TUcivXxJAH2nlXywhXPn8ogz5nNreFteRqYEDQM7KfcYBqWwPAEAarai3YLnRV7Hu3duBic4AnztXUOmD1bDYm-LtGC-a4b5osEHFpsBiAEV9pMGZUd5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_rlLTYsGLxuo73QtKBahFs41JkAG8ncLhssULu_8UdSPS6LvkVIV3qzwaGj3pDDDpbI_J31WexiLrQwxM5SdHNDZ94pAde1LqqpWFMSB78w670J3oVxdhYTA-ioiX8997J9kq7nzMyXNxEIRaLC-0zllKfnBj2U-Lpy_TPyeae3PSfiE1aG2Ns2nhec-LqK20lX2WkXFXUK5f3HGyuyMXEI2NG_qmNNWyL5qlegHaF40ZR-ojv3x2lB3Xqoyjaoq8gjyabO57uJZ_eQDENdBxQJkHVx4r4p2ynlwCRgKDuZx7_bTBnlgN3jXPYGVdgVLU4A8yjxHS2HXj55Rr9iXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
✅
👕
کیت سوم فصل جدید بارسلونا که قراره ۱۲ اگوست رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/103092" target="_blank">📅 19:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwo0f2i0hlVjf-JxMNMTL-JFhDeJFgFcl6lTome4wmuOBExRB4jzD7p1Qb26E1irrXKGBgf-C41nk4msTYL1e244Foqyxd0v1aQN021RtnddTM-qDb8GhKxNbHMOY47CqjWmkT9NM55enwhS8-tS_YuEG_41HUubqbFFEoWOx2CjDdzzj-7-Mf528euCLI-0aRWQsQfoS-43oUfbEPCugNDzwyeqh2aEoF697EHmVdXmbtGlmr-m9nIUVpIkj8mFOSBtDu4PJ1M67Hue8Ujh_a0Gb7ZeRVyvOTFxlOmoYnu7bAgceEiXk5N7e9WJx9N8CIZz7pfm7wZ16t6RsBJPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🟩
پرسپولیس در دیداری تدارکاتی برابر آلومینیوم اراک به تساوی یک بر یک رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/103091" target="_blank">📅 19:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUDQ2T_6W1jFY_9QR6KFwNwkefKwEmO4zcu1WLFB6yD-nG4yfzsOoKO2CDW0D5gm0oyOa6pQyrOFmlLcQEE0Vm-fjv41cPkC0uH0luwLUP7BONN08p7mMgFuddi1HhT8WUuG8wVf5Pp8sTEatwRT-Ji-OCPZrW5-cEkYbIXajzbwU9aVoSryun1rnWK8wAX6_NErWuGb6rOezBRS_v_4TRMouVh6sGsQCzvWXnVmk6xJJUOMZvDFkme5tcYKqAjGfJFBjPatn3FQNldEQIALSuTWLOBHJv1p54nbFzZQ7CUiN-YnLys_4pC9jYuOG1aa8qKIqoruuHwSkk5QkVxUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل واروش‌مجارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/103090" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103089">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/103089" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103088">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3KI4oUhX_76qvd4L2ILFGJ5lukPfjI2TKMdlqfO730iy2rAQX4wYJxLLztw1JPmBUjupdr7NE_Ufi0e4abtxzIFfZg8cH9H0FuViRaydP-4ME-H4Dlct2Yhp9stNV3_-2ReKEmM47OgyUmd-JiCmz0htE6PJOlsSQ9mJSV9KwWU8BxyxGRVvtR0AzjtvDnzujLxG2YnHeFoPWICe3dx8tXRrHyS2RohsaiA3FPEl0B1_F5hYvHCD9J4mHLcp3iDNxsbmoGKX4Z-E_lxSfWWTvTuNvEWZqo_WswFhlcZ2L_7iO_cyfMn3D5xT_vqZg1XpYiZOaWuwEW2s73iHSumGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/103088" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUsEusdQpWm5QZi1INYneSRcTuT6V5Ck-55Fx6Uk_AE83oxwLu5nbNTx-LKJctpH7efYib-8dBDebpUEfx38vlElBy2guAbvubGHF4zpatLDm7zHmTXvHQyxyJQjJ82ryrlU8dgO-ioL9noi-d_9ZklvGwWAN7Jwa1iiDwQoMRwCaAeg048rsirRh6KxRkmP2cTZpvrS0SGD8RMpU3A9h_R6pBuUF5cNmBwdJg4CCDvAju8sZiTvgPyenNbX6xMEtC4nf2ZatoYuxg6Wrs2RzYs9eZvA8-GQmIYHQs9abtzzqxaYYiKqTm9b8ATRAA_Pb1iPgfksqH_JtcX0S2rBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نتایج چلسی با ژابی آلونسو تو‌ پیش فصل:
- برد جلوی میلان
- باخت جلوی یوونتوس
- باخت جلوی تاتنهام
- برد جلوی سیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/103087" target="_blank">📅 19:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47158534d6.mp4?token=l3uA4oTKrCpnM9Op3Dmn1FHgot7iapUKUdN-ZHtoYcOT597pZXC-GpcxYsxuDoso_Zhr9Cu6dm_aeke57Y87ynrQ3KoxjX6-9g3ZAFcsp_MSB-6syVecL8W0TjlY2lGNFpVzZ2uC2GZ9jatbFhqhuslzfUmmzMXR0zj-pzRArqkhY4h28z4SC-1AH0xAbJQGVxBk6Y7oazf7S34dpUoVDGhwq3RjCznqPGp7wzUShRM-gwcfgkhwQh1e3_bz5XtSmYloFxIKGDuVL9XTBKTjD8sYWFKdkL9enGBNhRCgxUXv6_Lxzg8OGPSbLtrmc9sAVaUeVCOl6HKH_SctY5JtNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47158534d6.mp4?token=l3uA4oTKrCpnM9Op3Dmn1FHgot7iapUKUdN-ZHtoYcOT597pZXC-GpcxYsxuDoso_Zhr9Cu6dm_aeke57Y87ynrQ3KoxjX6-9g3ZAFcsp_MSB-6syVecL8W0TjlY2lGNFpVzZ2uC2GZ9jatbFhqhuslzfUmmzMXR0zj-pzRArqkhY4h28z4SC-1AH0xAbJQGVxBk6Y7oazf7S34dpUoVDGhwq3RjCznqPGp7wzUShRM-gwcfgkhwQh1e3_bz5XtSmYloFxIKGDuVL9XTBKTjD8sYWFKdkL9enGBNhRCgxUXv6_Lxzg8OGPSbLtrmc9sAVaUeVCOl6HKH_SctY5JtNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام به مسعود ذات پرور تو مسابقات اورال کاسپین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/103086" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpIZpGVITsZWTnCd_t_WxUHAZEl38ddjO0c-SXPjXxHZ-qCw2OHVEobMxDBNXU965cZW5rvC2DW9XaYYSfPHyGfchCkcvE86rf1g0TtrIauKO7ZwkCcDMBKF06E-JGQNxMjEi4kDoFWvg5DNy4TbVPk_kx0kVwKCFRUrUA9D2QxjokaOgwvGJWKmYdgt-0y4NGDdcDdMTUD2Hv1RMt9DtS49Qnnt_uct3WV7Y1LWlRA_TemEIf1uNJerzdeSWpwhPPODATQlDYiW8fPuPHR3WpXtgPMdbeY-bF05WPD5ZSMtyoKhcRdl15shi94PrW_Q1EKMedBH_0xbHSM7lRKLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/103085" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5956080028.mp4?token=I9V2O7naV7Z3IcFdYiFoysitsVqtKgsv2eEulG0m-q2J1jWzxTBAlEKUuhdA_hTikt_4obn9SvEg7Y7Q5KoZHNa88hWXXVkuk7CQ8B4QFrLVk03MrgeYg89rORezGzkcBVaz4B_0YOmvj9sB6TTNPsmsE_NkHGMoe7Y5A_fgXcbMU3vqvMpQwNX7z8AeYUNLjB5wa7-qvrm1-ub0_wLBf8Ugtjdey-UFYi9B38KAi7-p_yhnMT6CFU3Wspq0StqUJieCxsiR7Cui9r6JcVrtMeKatZt2q9HiR0VitVJS07QFQmxWBaXOQsig4GFJLAHubm9sRoF1DaZzzc1_uLcMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5956080028.mp4?token=I9V2O7naV7Z3IcFdYiFoysitsVqtKgsv2eEulG0m-q2J1jWzxTBAlEKUuhdA_hTikt_4obn9SvEg7Y7Q5KoZHNa88hWXXVkuk7CQ8B4QFrLVk03MrgeYg89rORezGzkcBVaz4B_0YOmvj9sB6TTNPsmsE_NkHGMoe7Y5A_fgXcbMU3vqvMpQwNX7z8AeYUNLjB5wa7-qvrm1-ub0_wLBf8Ugtjdey-UFYi9B38KAi7-p_yhnMT6CFU3Wspq0StqUJieCxsiR7Cui9r6JcVrtMeKatZt2q9HiR0VitVJS07QFQmxWBaXOQsig4GFJLAHubm9sRoF1DaZzzc1_uLcMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رونالدو وقتی از سماور خودشو میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/Futball180TV/103084" target="_blank">📅 19:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">▶️
داستان عجیب و غم انگیز از ناصر حجازی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/Futball180TV/103083" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_avQYh7CjdN9cnEMWZaDdimXTGLtFQebIBrLwJYG2iDyYXMOtugGeeWnH9xdPSsFVtsswWPRZsCXxRMs_Rqz7MOr41camV2AjCYGr1HBuw-Q88SEFv0izNcMeHvm1gRjTIklzaLbMiM9UUNdPAwG3xyPKlZsX_naBmlVof07ntY-_Dmwsr-c96FlHh-tmRANFo_iee4YqIPoURwr0h5hD9NOv_MLzQOvrqvCtpwEXYAYQrAVP-_tbTxsXeGHpzxK0sFsiAt2RbC1G28n9Dmic13kvkBRCu5onbdH9iLWoci_foEpzHUnR-vod5WCRY0EmeA13xN_BUHjTQsxs_MrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بالاخره موتور چلسی روشن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/103082" target="_blank">📅 18:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Kv5iWBUJzDzuYxetbndrgpDBpR8YAxH2wJtZafHwDozaumzHAOk_7mZExJO8Xyn5YE8JDgxXtX3eAPPDbuafESEGwRbSnnGbBymE8HO4eDI1wkpLbYTXqq5nXCHGIsQ9P1Do6g6G-NgY2tVXO2RWdAxoXQz-1K7nFhqGFpRjjQ5wBBBZyh4TCOEkuVeb6Q0sDE3tZnLO9Q0eME7jarfpHPzGWvJnetkshcjC8ky_92JejiO6Ct4EXRyuNkgVwROi4BL-VPIYuEkidDG6h8vLTakPFPXuNE5GiGY_QAA8Gsr5TrWrw5Z6DeHjxNxd00TboKpNi02ne7Q8xl5D_CdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ایشون برایان ماجو مهاجم ۱۹۳ سانتی‌متری جدید استون‌ویلاست که لوکزامبورگیه و متولد لندن.
‏پشماتون بریزه که متولد ۱۲ ژانویه ۲۰۰۹ هستش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/103081" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jG3F3QTHvITPuj3jT0m01CohNki6jArYywoE1_Qr8DrBdoGfjKmsNkGVaIQvrmbvThr1z925YbSHoUepenQURIZVhYhw1yRgfYErYIUw4ddBaGQv6QftYXRIiJwfymKwsoGcYPsU821A_ZeDZ7HTs4eLYd7l-fbt5RMRJX_3iuUjtZsq2mVrug4IJzo3IEIX_cRiz9bsAe1bUsl6BAcPoADNDAdwepVbKjEBbhy11zlzQGXHD0m4lFlEe1QZj9lp7UIgZT-dSR1PncPx4umUL5FvCVbBvAhAWAasJ48xepTCfjVjykQ_7jv5JYDr64P8IpT4Ee7ygAxZh4GULvEoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4sYYZhivTHo775TlxKXq9mHhJCIJXaRUAQxPchukGUsX10r6uvrhm4X06oHzHYZKUwyKDsvOwAc4Se7a3S48TqsUBmY8_dQSM4M0lLq8zSLC0wpDtKp7K4aP4I_yhKBsVcaleqgyMGcu54OmO6EHNN-f2GPLnL5l6xTiypM14F1_xTn_MB2zJAUArlwBuJG6ozNlFZhf4lz73bf1fPkY_PGpWyufKcMh5GVf7fD6MI-VzV3xQZ_hEKObqG9OamOro2CvGu4iIekqeHXw4JuwGampDt34yPbUvwx5U1IowCVBVpSxEA_L5ihYO03g7jwFTXpoOcae4doZ2AlJihA-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 آگوست تلخ ترین روز تقویمی لیونل مسی بوده..
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/103079" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از ال‌موندو: زوبیمندی ستاره آرسنال یکی از گزینه‌های پیشنهاد شده به رئال‌مادرید پس از عدم‌موفقیت در جذب رودری است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/103078" target="_blank">📅 18:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44f31c73c.mp4?token=JqltQz-_Hbdc3gNNsXdSiPURqDccbOSGcwl3Y05I5IfmEuIU5RCVcMJDN3-wH89VZzJWMBk4kvC_lRwz3YLDPtTEou1PB2-QqYiZ6Ha45eYNXkjcBS0wE_YXZtcHHZPFtqjuZYGvzmy5ePuwKXJ4X4L92Pyzgt1vEPRE8WgKLQ-yDugyrPOpE9XPO-CQiTbvthS9xeAJKyhf5la0XXfQR8qfW2QNkhaIbikilGa--aj9XKn_UI2DsNJTsIuUQwf_KTjzrcbBcJ0XjSeoC8MyipZHP_EshDok_nqwml390lXCQl1C2-UeLyaPN8OXnNSWRRAbyC_OP8Re-AoszLxOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44f31c73c.mp4?token=JqltQz-_Hbdc3gNNsXdSiPURqDccbOSGcwl3Y05I5IfmEuIU5RCVcMJDN3-wH89VZzJWMBk4kvC_lRwz3YLDPtTEou1PB2-QqYiZ6Ha45eYNXkjcBS0wE_YXZtcHHZPFtqjuZYGvzmy5ePuwKXJ4X4L92Pyzgt1vEPRE8WgKLQ-yDugyrPOpE9XPO-CQiTbvthS9xeAJKyhf5la0XXfQR8qfW2QNkhaIbikilGa--aj9XKn_UI2DsNJTsIuUQwf_KTjzrcbBcJ0XjSeoC8MyipZHP_EshDok_nqwml390lXCQl1C2-UeLyaPN8OXnNSWRRAbyC_OP8Re-AoszLxOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده از مصاحبه چهار سال پیش رامین رضاییان در برنامه فوتبال‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/103077" target="_blank">📅 17:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b851903a5.mp4?token=vGaDj2Zi8Kpqfb14xmohK9dM9bPt3vEwoLNXLViefUJCDRSI0r1mWF4KIJYVOzySgQSc3nNLgTgYDF_qZbe_Q1F_CzJfA9HeUOEJMeVLzTywLzR-hSqdxxl6yRQH6tyGNXFLscg341oZpXPtve2TDMs4DtoOiyMvYwbLAM3qA5ixs0n5x5oYNwJ8-5eA6LJ3vqiyeGFRfGSAR1OXXXjXKlztAswy6UxdCoDYhASk41LbJ-kiWpmfECNG5aR0C48T3CdQs2XnN6zRDw9kg6Xk_eCZw-5HZw95CmWYy0UT7IX1Qmd7OSEYUFusjZtPxlndlLYv6J-paTr9e9d8377DTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b851903a5.mp4?token=vGaDj2Zi8Kpqfb14xmohK9dM9bPt3vEwoLNXLViefUJCDRSI0r1mWF4KIJYVOzySgQSc3nNLgTgYDF_qZbe_Q1F_CzJfA9HeUOEJMeVLzTywLzR-hSqdxxl6yRQH6tyGNXFLscg341oZpXPtve2TDMs4DtoOiyMvYwbLAM3qA5ixs0n5x5oYNwJ8-5eA6LJ3vqiyeGFRfGSAR1OXXXjXKlztAswy6UxdCoDYhASk41LbJ-kiWpmfECNG5aR0C48T3CdQs2XnN6zRDw9kg6Xk_eCZw-5HZw95CmWYy0UT7IX1Qmd7OSEYUFusjZtPxlndlLYv6J-paTr9e9d8377DTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
🔥
آهنگ خاطره انگیز:
Savoir Adore - Dreamers / PES 2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103076" target="_blank">📅 17:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsuj25SzA-uSfBwdVcSAe0rfp1g-hJSS-ckQbQvRxXdIsGbLE4zW402Vvwl_vpQeUPW0S-ZFG6gcLNNwIIHkLkzXGo1XQzPg8DTqwqQBIoe9YgHXaojai-eMcPNLKDLNJQaDsamH3qv7SeVv4e4mT3-I1QcDIz7pg1Za_YCMyUxV_0oH2cIT670ujWME0bzKye1nIJzaYUxhIXgLAQtgkllnuqfx2PkEWpmC_zNydtxxE0egg-BMG9vED66qNynGBRuyz7XmPPrnXHYsd_MoRaZyZENe4QFgxF_MygqfM0P4dUs2kj1-aYdlNwdjgW4Ns5c48nAM2zb7qqdYBH0Ihga1tc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsuj25SzA-uSfBwdVcSAe0rfp1g-hJSS-ckQbQvRxXdIsGbLE4zW402Vvwl_vpQeUPW0S-ZFG6gcLNNwIIHkLkzXGo1XQzPg8DTqwqQBIoe9YgHXaojai-eMcPNLKDLNJQaDsamH3qv7SeVv4e4mT3-I1QcDIz7pg1Za_YCMyUxV_0oH2cIT670ujWME0bzKye1nIJzaYUxhIXgLAQtgkllnuqfx2PkEWpmC_zNydtxxE0egg-BMG9vED66qNynGBRuyz7XmPPrnXHYsd_MoRaZyZENe4QFgxF_MygqfM0P4dUs2kj1-aYdlNwdjgW4Ns5c48nAM2zb7qqdYBH0Ihga1tc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تمرینات میلان 2002/03
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103075" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5i7t0fjUxPE9LtIi-fP_EObH1Z12caCKFAaI1xY1FHObBh7BS9s610el7AGrjvvkdU1xHBC66usqxf1iJPPG8ggsi4MQE3FhY8XQS2vNBl8dT7jLdV3OxSH8FXt6I45CmTy90Gwt-bsqPmJGWThHWXQ5GZ91wfgF3C4-e6jg0HZLQ5UPbz2RT4A5l-ulJCsLaqlx5LfZWV1_iJmSzNlXih2z_dlE7a69MSPVlrbGisFNFCB82Ca4N44Xo5bJn5os1_6fPCMW5CTNxpvcA7kUNo2MYBOs1Vm22Wz1jhpXyd5bQCQ8buC3pu2QaeOBVOhgqntGCKVPYzbjksmO1Fs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از ویکتور ناوارو: بارسلونا در حال بررسی شرایط جذب لاپورت به جای آرائوخو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103074" target="_blank">📅 16:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103073">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=MdoZCPuFxWcuN7iU62ctahZTQhAotkVtuLyGrJI9bcP5SPipwMeegni4VbOXY80S8MsQEJZqcNKCfQFd5f1fHwpTT4yaf29xTjovhf8FO28IMqpa2VDUdr_wtprM7AvqYy7FkTqyQ7OfiseoTFC0ifZSHdsGMwtovlGOfMbaWNIC_7M8dRHFb0a4CkDa5Ne3W5OtdDZvE1iYjbD933fnYhJ-qpTd5bXyNwEEshGw_XPqh10WUiNPn4RICVwiV3upyWReI-a6kQ0yn2SSuD8ox8D0kHW9HyM5hcz9zm8dY4t4Vpxe7GN-Psvkru_HvXijwoKNA9RoCMsfjTZK05lcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=MdoZCPuFxWcuN7iU62ctahZTQhAotkVtuLyGrJI9bcP5SPipwMeegni4VbOXY80S8MsQEJZqcNKCfQFd5f1fHwpTT4yaf29xTjovhf8FO28IMqpa2VDUdr_wtprM7AvqYy7FkTqyQ7OfiseoTFC0ifZSHdsGMwtovlGOfMbaWNIC_7M8dRHFb0a4CkDa5Ne3W5OtdDZvE1iYjbD933fnYhJ-qpTd5bXyNwEEshGw_XPqh10WUiNPn4RICVwiV3upyWReI-a6kQ0yn2SSuD8ox8D0kHW9HyM5hcz9zm8dY4t4Vpxe7GN-Psvkru_HvXijwoKNA9RoCMsfjTZK05lcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب بهروز رهبری‌فرد از قمه‌کشی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103073" target="_blank">📅 16:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103072">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=ExwFDH2G1eg4o2IbQ8eE0V96T6mD2BCWUFaEOgjodrd2VLomrVfdZX8-12v6JBrzVqRwNoS4Swfnknk6skucUpqlMUJJUYdR7XLpG0mJ4NIhYGCQlXq5Fxi2Z3zEQj-9BODWp_uV16g2AF88_6OO1KXyKJFHJL1_8BhN6Gg1esxX-FDytNPVWHFCc7k_gnaolQ1VJg-zrb78NvDzr9ltUcn6_XAwMEuVQ9u4dB_z0L75WXL6o8KpBW5d194-HVyLDDQsp1OK-0GMYIhwYR9qtmFE61pPYDSL_AsSaB5fbOQtvBphyQhAk-Liq1wD6hLY8dIg2hX_UkM32ZC3Sm8nSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=ExwFDH2G1eg4o2IbQ8eE0V96T6mD2BCWUFaEOgjodrd2VLomrVfdZX8-12v6JBrzVqRwNoS4Swfnknk6skucUpqlMUJJUYdR7XLpG0mJ4NIhYGCQlXq5Fxi2Z3zEQj-9BODWp_uV16g2AF88_6OO1KXyKJFHJL1_8BhN6Gg1esxX-FDytNPVWHFCc7k_gnaolQ1VJg-zrb78NvDzr9ltUcn6_XAwMEuVQ9u4dB_z0L75WXL6o8KpBW5d194-HVyLDDQsp1OK-0GMYIhwYR9qtmFE61pPYDSL_AsSaB5fbOQtvBphyQhAk-Liq1wD6hLY8dIg2hX_UkM32ZC3Sm8nSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
این کلیپ رو چندبار ببینید و برای آدمایی که تو طبیعت همه چیز رو می‌کَنن و میخورن بفرستید تا بدونن یه قارچ چقدر راحت می‌تونه آدم بکشه! اونم مرگ با درد زیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103072" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103071">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=Sr1-A0_RCzzQdTRwaYtA0BvheH0H06lRwhAoV1MV5bTaxDVUx7xgxyXk8JApnWWBW5gP0i0PAu2MU6M0Hf3Eja0Qqzj8jM3pxwxqG3o4tN4FqEgkbXaq__f5D1LgAZjXSHW33tanQZDR78_4hGHShh4uAIe6nt1pxf-RKEnDtq9lMcVj2FFDoNU-g5F79mn5dB38aEuQpyfIoA71tbtJdqH0f6PQwSl8xOziny6gZdVU2tgSlRa5JzqLFnpw1ar7cywquVt_fGedFjPZF8lb1L8RL_BWHlInJsmgAfuVJatbrsJF18f_jccLjqRxFl19sW-o-pOA2LvfbqFmp77bBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=Sr1-A0_RCzzQdTRwaYtA0BvheH0H06lRwhAoV1MV5bTaxDVUx7xgxyXk8JApnWWBW5gP0i0PAu2MU6M0Hf3Eja0Qqzj8jM3pxwxqG3o4tN4FqEgkbXaq__f5D1LgAZjXSHW33tanQZDR78_4hGHShh4uAIe6nt1pxf-RKEnDtq9lMcVj2FFDoNU-g5F79mn5dB38aEuQpyfIoA71tbtJdqH0f6PQwSl8xOziny6gZdVU2tgSlRa5JzqLFnpw1ar7cywquVt_fGedFjPZF8lb1L8RL_BWHlInJsmgAfuVJatbrsJF18f_jccLjqRxFl19sW-o-pOA2LvfbqFmp77bBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
روایت‌جالب‌پپ‌از معرفی نیمار به بازیکنان بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103071" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103070">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be22201896.mp4?token=t2I2jOIsvAva-Bvr65iDtmyh12j743Mf8nm3GJTRlMyqUO2WcZOLZNtnzqbK8fjPxhelobz2YO7RMxuepham7j2qafvALnVnpjjbP2rOwCGxbb5pwFG5aKqkPqychJh0ZlgbcEKieVU-cn92sZ0TDk8EIjTY2P0XInsNja_UWQyi-K82WvXqd1v7lMuCEPcgTelaS1yr4GQC5GwOcokWzrB98qlWWANyuygRBF8qYIqLJyQndvctrevqHpDwecoR0tIEtzGTwXCJFQRLvwqY2UWQuTgKUDq-Ro--Kc3RZYOSZLvQDnG1cmGyvZYpVBbRE8fHdhKhH4P2TiOx4lMCJDAgNOcCVKXL_DtvHptczIyxrxxhnxgqz1AxJzrB_t-6WHaa-_9jGIiOTtvxjSUGi2E_0-GuoHASLqOy99HXs_JxXlzHC8xho0nkrSOHEl8w8j6C1Cc4sj8T_9kBxpadWN23JvCu5wrJ1HBRvktTjs9QvuTUd5shqYzIgkVWg0OF5TbuZZtVHsqJt_FLBLhKOq5CKNKx59tuznPSvV4kBU8QGqe3DofvEGjljIGp_pMfGo6dNk6ZsDhjzZKVvd2YQlMEku93srq8PZ4WaJjBCJjjvobR5kSDF5OdsVOU2v0fAHp4cIBZxbHHaln5-J6ClW3cqllFYDQo36ZEcB0IuFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be22201896.mp4?token=t2I2jOIsvAva-Bvr65iDtmyh12j743Mf8nm3GJTRlMyqUO2WcZOLZNtnzqbK8fjPxhelobz2YO7RMxuepham7j2qafvALnVnpjjbP2rOwCGxbb5pwFG5aKqkPqychJh0ZlgbcEKieVU-cn92sZ0TDk8EIjTY2P0XInsNja_UWQyi-K82WvXqd1v7lMuCEPcgTelaS1yr4GQC5GwOcokWzrB98qlWWANyuygRBF8qYIqLJyQndvctrevqHpDwecoR0tIEtzGTwXCJFQRLvwqY2UWQuTgKUDq-Ro--Kc3RZYOSZLvQDnG1cmGyvZYpVBbRE8fHdhKhH4P2TiOx4lMCJDAgNOcCVKXL_DtvHptczIyxrxxhnxgqz1AxJzrB_t-6WHaa-_9jGIiOTtvxjSUGi2E_0-GuoHASLqOy99HXs_JxXlzHC8xho0nkrSOHEl8w8j6C1Cc4sj8T_9kBxpadWN23JvCu5wrJ1HBRvktTjs9QvuTUd5shqYzIgkVWg0OF5TbuZZtVHsqJt_FLBLhKOq5CKNKx59tuznPSvV4kBU8QGqe3DofvEGjljIGp_pMfGo6dNk6ZsDhjzZKVvd2YQlMEku93srq8PZ4WaJjBCJjjvobR5kSDF5OdsVOU2v0fAHp4cIBZxbHHaln5-J6ClW3cqllFYDQo36ZEcB0IuFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
روایت احساسی خوزه از ساعات پس از فینال UCL و قهرمانی با اینتر و تصمیم برای سرمربیگری رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103070" target="_blank">📅 15:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103069">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=fOt1LAzhtzKYWoK5vkS-Rw3jiRbcNQYqW0mAzSI_s_XZlJVUqfDPkolH60Z89bkn6XHV1nbhumE8fuY7fBy2eUGU8juGjKILrOJ6tT9hhn94lNfSEDbcyLhczij30dEE9OwMi_MOfNSR8iOTuxUU5fujVOEq0QDKC7Ri65OVFkJSyZH4IJs5i9p0VV_zkCz7A6zMKArpSF4TssjEQHCvLcRTP3viExziIcyq9L_2bYffAr0-4ZBEfxdIIf-2d9uHf1qdFs88Haw3pIEyYvp-9BUrThN0GGluAJRfWpfh8uLtkBkCaJ9-knle2V9zpks4VAfJQn_hr9r10d8qFJVymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=fOt1LAzhtzKYWoK5vkS-Rw3jiRbcNQYqW0mAzSI_s_XZlJVUqfDPkolH60Z89bkn6XHV1nbhumE8fuY7fBy2eUGU8juGjKILrOJ6tT9hhn94lNfSEDbcyLhczij30dEE9OwMi_MOfNSR8iOTuxUU5fujVOEq0QDKC7Ri65OVFkJSyZH4IJs5i9p0VV_zkCz7A6zMKArpSF4TssjEQHCvLcRTP3viExziIcyq9L_2bYffAr0-4ZBEfxdIIf-2d9uHf1qdFs88Haw3pIEyYvp-9BUrThN0GGluAJRfWpfh8uLtkBkCaJ9-knle2V9zpks4VAfJQn_hr9r10d8qFJVymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید چقدرضربه محکم بود که یارو با این هیکل پهن شد کف زمین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103069" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103068">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmXQL6se3NEukU3Fb7st_GDBLR86_zsNqod_x8mVKRmuxglCMZF2n8C1pZaOX6V2TFjPh2DGu8Qd4Nrg00sG_kMrdUXcFbReiQg8rbbW9nlM29D94oX_2L9lxknJmLXiPeXEOwDsAfBHzq8XCYM4ItPpI3MrXXwSX_rVjwvWH1NZ9HXecg1A8GIZ15bWGPrbQTXf-KJ1h8cMq_ZCH9XtwHgaUvpPmdHzevVSIy6ZUdwRVw_SWx0I7q1tACc0_4x5vo-0EWU0KPqbmKfyThsH3ByL12aw1WRM13DQU3D1-rQROV1T8L_YUXeKSjg0e_u0VH3U-lWUebJZp1NYWGEyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
نگاهی به آمار گلزنی لئو مسی در بارسا به مناسبت پنجمین سالروز خداحافظی او از جمع کاتالان‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103068" target="_blank">📅 14:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103067">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcCIJbIgW4KmPtu3ojVGK96r_8wwqMEEbyiaHkwnAVwnjZoNGKdDyX0ovArZHdHebMjDG9HmAtZNmePhiqfMG9NROXb33bvTI_kC3UAb5CJ_JkH9I4LGtADvOcWvA7GFKd_4hKGYYdnzLBvAUhQYQNW2QtNE2TUux3nAXMytuaNtApayhTN-i8ff_ktQqG_gJc6t3WctIGb459xbdGPX4VSEOcuL-pySV1qnqbp9qWEAuiXiGp4CFjDqUJtw5jDIHiSmXQueVhdFQdN0OXk7UweGetyOPXd4SHw5234TKI1vsp2wkE7TV2eiTfkY12BbLnxEyRDPVjC6CUy2QltTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خورخه مسی، پدر لیونل مسی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103067" target="_blank">📅 14:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103066">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=l--T2GIfXSPCZfcizOIJH9JRvg7sQixRza0Ees5Q_b65yPIZcLUIiG2vvFdutafgl9OXMUNQJyJoNaoJ4DF_ML-ijTw1ZvQrnhIl-hWYYfBXI4SWv99PEumkPcfuMLmcibxANC6CdrOTN31PIo6CofNs9MB7LlPTRnJ6xLOty5U9vz1G6uCs90VuAuOTjOy2sMiDVHIm-cy3iDNTWlhyy_q8CJ1mJ-lSg0HjSCtsqesFdX2FTw3Nod4x-XzHtSgKxZxUVL1bsEvEkfS1uUju0i21RGzL5pXTgV6IJVNVydSR_ZT3W6RTr31K6NF8xSqpwBxu8V4CdV8uwQ8gl5aESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=l--T2GIfXSPCZfcizOIJH9JRvg7sQixRza0Ees5Q_b65yPIZcLUIiG2vvFdutafgl9OXMUNQJyJoNaoJ4DF_ML-ijTw1ZvQrnhIl-hWYYfBXI4SWv99PEumkPcfuMLmcibxANC6CdrOTN31PIo6CofNs9MB7LlPTRnJ6xLOty5U9vz1G6uCs90VuAuOTjOy2sMiDVHIm-cy3iDNTWlhyy_q8CJ1mJ-lSg0HjSCtsqesFdX2FTw3Nod4x-XzHtSgKxZxUVL1bsEvEkfS1uUju0i21RGzL5pXTgV6IJVNVydSR_ZT3W6RTr31K6NF8xSqpwBxu8V4CdV8uwQ8gl5aESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
سطح‌تمرینات تیم‌های باشگاهی آفریقا رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103066" target="_blank">📅 14:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103065">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhP_SA-6wZvR6M1otmOBzueWHbP8cHKtvAr8gePhWc1iR08rh-myDLETh8bTjLjrvcVv62XxOg9CqdYBR7k525QmqtBQ1eEJcvD-_oM5BzUyy4Q1mL1Y25Tt9iJd7qz-kJH96WLbyfSlOPF4wIIyariCjHsTMkwlemmRMUL83KwHyzOfLvYEopjwJXf-woxZjjlb7WcR2xoegKPohRrVNG7FQvn__zCKo4ak7ED61ouz00qkVpaTPeDyM89mzJU7gvJzQwgA_2PhzMulRfspjtFvTcfEOGbKVXJFq6IvA6BqWaW-gNiyMj2sgnd1MoQVC2FWFaWbOq1pTPGH531CBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
🇹🇷
علی‌ناجی خبرنگار ترکیه‌ای: پیشنهاد ۱۲۰ میلیون یورویی اتلتیکومادرید برای جذب ویکتور اوسیمن توسط گالاتاسرای رد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103065" target="_blank">📅 13:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103064">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103064" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103063">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=Rxjri4SIfz0h1EMLz1pwuyO5pbaFAkxdYZDPvRhcsG7N9xxOz_eEcg43lNvCtu2E_9S_mTA970PULXRnc6NCz4k6e-fwq0rPr5N5xPAk53raU8vMTyNpx5sF6PbcwnI0m9BHCgb9T0pSD6hYEY4AdYzPnqE0uy8VBblYFf8jg1U3rDNxUSaOyEDg_smfwFchZVfXY1MIKVwwWVPHFOiWy66FxaM79gmWZTB2In80T5BNx6UqeJib-qtFl-GxguO42xPYvlP2lgT47OnRK4dgmKxStLwE_4RRXf8nZGKhmNGkwkfmUxCNzt2ZvcsTv5Y53lhrhxMtFVhgEEicWylP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=Rxjri4SIfz0h1EMLz1pwuyO5pbaFAkxdYZDPvRhcsG7N9xxOz_eEcg43lNvCtu2E_9S_mTA970PULXRnc6NCz4k6e-fwq0rPr5N5xPAk53raU8vMTyNpx5sF6PbcwnI0m9BHCgb9T0pSD6hYEY4AdYzPnqE0uy8VBblYFf8jg1U3rDNxUSaOyEDg_smfwFchZVfXY1MIKVwwWVPHFOiWy66FxaM79gmWZTB2In80T5BNx6UqeJib-qtFl-GxguO42xPYvlP2lgT47OnRK4dgmKxStLwE_4RRXf8nZGKhmNGkwkfmUxCNzt2ZvcsTv5Y53lhrhxMtFVhgEEicWylP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
یامال این‌روزها تو کلمبیا نقش دیجی‌ بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103063" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103062">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDKmJFAIHqReYH6iMdRFvmp5VtmsVcLplRk9jFxCJprW4a1IzyoLNdIPiOp8IbLNefQzJiB773tvDc4Yw1DBjbrYl41c28cPtkquiw8px7UW1rhzJIqmzk6XnsB1DBH_KLqf4H47rIKN_irUQhb5nJLw0PWj56SYpuOApgZ-Nk6BLtOy-qiMJ9Rz6Ao5AUuWsKUNI_9QdyW1WyLUGnSeTSNPcD7D5rBvjl1znrI9p4S_c3qQbIHAktNb6pOm4p0CoR3ESkBa5VlTEkk3GXct4fPHcCZsIDsBd2Xq9Y_7HdHZCQRqAzH8EskyZspXR6NyEyjEbmJ9pfiOAAfLFLdZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📰
افشاگری‌عجیب فرهیختگان: موسی جنپو فصل‌گذشته به ازای هرماه حدود ۱۴۰ هزار یورو از استقلال دستمزد می‌گرفته که در تیم جدیدش در یونان این رقم به ۲۰ هزار یورو در ماه میرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103062" target="_blank">📅 13:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103061">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPmSS-iK1q41szkhuA0ODsDd8_uJTLwe5M0XQDqz0qZd1gZjJz1_RWsxTZEOEuB_3YMZlz1rAy-8aPZLVH9eQzu2YVnvxdqoUhHMWysMMH65s_aigCGNvn1xJ9YwYDMUvi56sBwfF9hekmYm19gFULdfPFGrb1Zc9QC4SFrqZHMvta6emhUC1GH67-pLB7Ae-5XVRwFUw37QGy9XCDy30qX2SG9yCgCka__qlZ31HmHuWn1fc77NEfQlPU9OjBJHUeCIFDKdMw9v2BXnBk77W7X0kHLpGR0d4SoWyENq0ec_BzpySo9EJ2E8NnE4ztIKStDkXiekelcDAjJ1H3Bkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🤯
#فوووووری
و پشم‌ریزون از مارکا: توطئه‌ای برای ترور لیونل مسی در جریان جام جهانی فاش شده
😐
🇺🇸
طبق گزارش پلیس آمریکا، لیونل مسی بازیکنی بوده که در طول جام جهانی ۲۰۲۶ بیشترین تهدیدها علیه او مطرح شده؛ از جمله یک تهدید ادعایی درباره حمله انتحاری.
❗️
پیش از دیدار آرژانتین مقابل اردن در مرحله گروهی، ظاهرا فردی با فرودگاه دالاس تماس گرفته و تهدید کرده که به همراه دو نفر دیگر، با سلاح و مواد منفجره دست‌ساز وارد ورزشگاه خواهد شد و مشخصا مسی را هدف قرار خواهد داد.
⚠️
تهدیدهای مشابهی پیش از دیدار آرژانتین مقابل مصر در مرحله یک‌هشتم نهایی نیز مطرح شد. پلیس همچنین یک تهدید بمب‌گذاری جداگانه دریافت کرد که در آن ادعا شده بود مواد منفجره داخل سطل‌های زباله ورزشگاه کار گذاشته شده است. نیروهای امنیتی با کمک سگ‌های مواد منفجره ورزشگاه را جست‌وجو کردند، اما هیچ بمبی پیدا نشد و مشخص شد این تهدید نیز کاذب بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103061" target="_blank">📅 12:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103059">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNSRvwjAHxKcShsDUApb3DZF03GaFYSNumSIrkJHHty01Fb2gbZ1ZWY__naBSMg7SJXL59HNUEy3mW1kXCCmOyYUnzxiBieAsr4VeIbk4Gk5NXB6ueV4gj--aitsK7RM7gOdFx0GwpwF7mMS2O3tHzzKd9esSM64qwJoLpn5o6-3DuKVWjlFFwqZE_XHVnDOB87-vanCTDcQrKc-2vThRhkkvY8ZdBoeJUqIUak26rCc6LCRsjR0LvTg_uepdsBuZ4rLFa_spPFoR5EBK5wF8C9Gi-1Nnl8fjLgaMPjC4hMCKm4_qZGL0OraxpVAtprzGOb1xjHEX5zwZ6BAs_rsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از لوئیس روخو :
✅
فران تورس پاریس سن‌ژرمن را انتخاب کرد
🔼
مدیر برنامه‌های او این تصمیم را به اطلاع باشگاه بارسلونا رسانده
🤝
هم‌اکنون مذاکرات میان دو باشگاه در جریان بوده و تا نهایی شدن توافق فاصله‌ای باقی نمانده
💸
پاریس سن‌ژرمن مبلغی در حدود ۵۰ میلیون یورو پرداخت خواهد کرد
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103059" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103058">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU_aoUenKQAp-koAq7CZhshJknqWmh1K53fnlZ7zXgTTYH6RcmksHWwowNc4X6W-5O6T9ZxWILlzZtph8DKzxfCQE3zwFvdaDE9Df3jA0c4sJT8ZNCn_gi7hHn5zNFAB9XiKKsvUgkx4H6cCGDdP4Kx9W7XB0HIJWllp-DbgorIpRynJHhAyk9LLKIncWq04Sy4H0kKoAlOyNYBmHSccCbHdIckMyi6dj7GONpJwNVF_I1YWEjYOBcEd9HXjOGHqLlJgSkWRy8lgySCR2mPv2OhNoaFj-Mw0zKll6Y2avs0lBRF4tNOiu8wRG--rSScfJEu-wf9tvRAoBYwq5QQobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری
دیه‌گو سیمئونه :
🔻
وضعیت کاملاً روشنه. باشگاه تصمیمی گرفته که میگل آنخل اون رو خیلی خوب توضیح داده. از نظر ورزشی ما از داشتن بازیکنی مثل جولیان بسیار خرسندیم و بهش کمک می‌کنیم تا به رشد و پیشرفت خودش ادامه بده.
🔻
قبلاً هم شرایط مشابهی رو تجربه کردیم و دیدیم که چه اتفاقی برای گریزمان افتاد. از نظر ورزشی هیچ راه دیگه‌ای جز ادامه کار نمی‌بینم؛ این وظیفه‌ایه که نقشمون به ما دیکته می‌کنه و تمام تلاشمون رو می‌کنیم تا مثل دو سال گذشته بهش کمک کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103058" target="_blank">📅 12:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103057">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCIFRoxnjyRycF4DHGmn90YIliMBx3hGpylHuTOVygQJB2MMn7VLhjmIN5fHVyrigINYhDUKKF3EAx-ulEFsTVDc5rSB6765-fX2CUyvz_ZCvCNsLlTNvJ2igKGl_o1807MF-_X-gl71nrSyITWy0W1QTgpoXziEBSEJ-7IxKsXbeZPcJqTyc8xUNUooxdF7c4MR6e6u1ZA5sJjURVNInQCYl1YVhCNcCLos8rsfxOQP2IaKW-ReT2wmas7clnzzbN-LmE4LQdzORfbGUI1TMCqFCr__1oqcsqH8fnGjtzuvyu0Q6bd4oKt5avsW2BsVMwJMVIRG0QdYXpGLzsKRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو:
الهلال برای جذب کاسادو با بارسلونا تماس گرفت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103057" target="_blank">📅 12:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103056">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trbSM0LsKvQVygQuU8D5uv6sksdN5uOINwwwbexb84vSH8TD4R0XVjX6WG7qqW9sPjl4pIwzePwAEHe7DHZsY8PWgIInRFQnJBGWWJDtZhduiUbu35jLE4j6-j_T2mp2DFd1lkgDH1BGdiBBS9jfVu75Tj17mJ6Wn34oPwn6k0yTllBQdjXPfTi_XgeC2Np0jP3LIt94TdmCd_dsO4GxBjz2Uld05JnfTzIfjp215dcrVEzEn3-geICgvjXTbFv5miatCGxgkfvpTQ0PpORY-Jw9GYvrwO7SVvs5reHK-I2ZQVBivXltUDye-ET_1APaa1jCXd9Ls7rZvv-cy7cVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست PSG برای بازی با منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103056" target="_blank">📅 11:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103055">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgV5gkUHy7b2-aRgUY7O1WHxtuzBLy5bBqbPESGwYx4jS0farjQxitBWa_2yw_8KJayjnwYVXiVwKIN8kczpLKEiWQnj2AADcF1-V_q9y9x8_s4Nzl1ebkA4cAmMvf8WtDTOWXEfJsspbHZCRdLv1xdci9RddB0ZwMMH_KsmhpC4UO84STTcFf8-7b8v53mOLghAXhdSKpD219gZ5WUqJeWB6ecn696eTAlE2QGvBVDabRIuGpYVfmERHVnk-FUQnP7h-N_8hrUp37BwXwpJZydvXDyTBwGWiFWsj9Izh1M6XRayM89u5h4Gc3aPSKRJSxhe4mTVezVdw9YwEIhG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
بارسلونا روز ۱۶ آگوست در سومین بازی دوستانه پیش‌فصل به مصاف بازل سوئیس میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103055" target="_blank">📅 11:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103054">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff922b433.mp4?token=viJh8LbH-kxGbfGJ8-OHBNsuIfZjqISzAb7gdED9EYwnAO4nOZEKiB5-DTFf3uEcrKk3RhK9ByYAj0FcGmSAOf3r0_yfXDyoIgaAVjO0_bdNs9jW-cRZ4Dk-Q6WJ-Cue3q0itJjJ8qvMYbCduuxjwBUCadLK1Y6IsnwE5366fOcwO26eqWJwW6nCkDcKFCQR44kzvia6Xs9msHlcbm7WMJksv1TP_Xaw_d7ErFWWF8X7jXcRE1bZ88Pj5vysSu9GKYoPJNplg5qWTdc5iRtftO1wox4gJjKPEduEOTY7hGZQxTYkYcm8wxnB_gpcLlHKVBvhRZy1ZpBoYo7CBker2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff922b433.mp4?token=viJh8LbH-kxGbfGJ8-OHBNsuIfZjqISzAb7gdED9EYwnAO4nOZEKiB5-DTFf3uEcrKk3RhK9ByYAj0FcGmSAOf3r0_yfXDyoIgaAVjO0_bdNs9jW-cRZ4Dk-Q6WJ-Cue3q0itJjJ8qvMYbCduuxjwBUCadLK1Y6IsnwE5366fOcwO26eqWJwW6nCkDcKFCQR44kzvia6Xs9msHlcbm7WMJksv1TP_Xaw_d7ErFWWF8X7jXcRE1bZ88Pj5vysSu9GKYoPJNplg5qWTdc5iRtftO1wox4gJjKPEduEOTY7hGZQxTYkYcm8wxnB_gpcLlHKVBvhRZy1ZpBoYo7CBker2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترابوزان‌اسپور ترکیه درحال یادگیری زبان عربی بعد حضور محمد صلاح در تیمشون
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103054" target="_blank">📅 11:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103053">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d7174722.mp4?token=fWKbCIU7d0vTpKKQjP5WirpHBeVexBN3g7lD5np78VWcDeQGltiLfhbzTLB0yvDAhex8iBLvncmsrIyjJekLJnDtlJFI0o-WpdZFl6HEX88hozL-1hWDy-1xe7O5EEc6SKxVmlGuf2SgjDA3sVeoDNrrJEziMkZh5CDrcVeOSUgE2gpnTl6sDd7OOEsZgdOm4geDf_Ki3kPcbdEHSYYI22mrNPa28jDJpeKl7QJ_jaR5ZUk97UwBdLq0fX5sHsyQdsD8RGr_rGKa_7jUkp_AAuSD05g5WhJjGZZWDa6flKFH_c9zCPF8NtZRss22343aBjoxSbdmRkkp2LoQgumiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d7174722.mp4?token=fWKbCIU7d0vTpKKQjP5WirpHBeVexBN3g7lD5np78VWcDeQGltiLfhbzTLB0yvDAhex8iBLvncmsrIyjJekLJnDtlJFI0o-WpdZFl6HEX88hozL-1hWDy-1xe7O5EEc6SKxVmlGuf2SgjDA3sVeoDNrrJEziMkZh5CDrcVeOSUgE2gpnTl6sDd7OOEsZgdOm4geDf_Ki3kPcbdEHSYYI22mrNPa28jDJpeKl7QJ_jaR5ZUk97UwBdLq0fX5sHsyQdsD8RGr_rGKa_7jUkp_AAuSD05g5WhJjGZZWDa6flKFH_c9zCPF8NtZRss22343aBjoxSbdmRkkp2LoQgumiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
از عجایب مملکت؛ امام جمعه ماکو رو بردن که سالن آرایش زنونه رو افتتاح کنه
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103053" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103052">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103052" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103052" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103051">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=E95VDFrHxQI3Z9pZCriAtqOgn86sTmc9M3laec1Ml_6UJkFqxwb5ZDMNftRucd2uNksWEO4Td9JlNfIJlhMP9saRJjtyJ8Jjo6Rwhte2pHD-s0uB69lNZaYSNGTHiK6T9yf2GOM5b7MKvbqP3_THbpO7c5mmN8LKIDJ0_HgdinqEepS7JSTOBl6qM1uDbjOGcpZkNSjXgkZMmSkypN9KsxOD3Csf_iB59xHV_ZlivlIo8VEk3JlTwBwednRtKf7wauq9gDQcxz3C-OOmbC3voKSdyxaV1rgD-1NuzoFgTOHG69WdYtV5ARC5AHBmWa38DcbngrqUJ5KZOI_AjlMheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=E95VDFrHxQI3Z9pZCriAtqOgn86sTmc9M3laec1Ml_6UJkFqxwb5ZDMNftRucd2uNksWEO4Td9JlNfIJlhMP9saRJjtyJ8Jjo6Rwhte2pHD-s0uB69lNZaYSNGTHiK6T9yf2GOM5b7MKvbqP3_THbpO7c5mmN8LKIDJ0_HgdinqEepS7JSTOBl6qM1uDbjOGcpZkNSjXgkZMmSkypN9KsxOD3Csf_iB59xHV_ZlivlIo8VEk3JlTwBwednRtKf7wauq9gDQcxz3C-OOmbC3voKSdyxaV1rgD-1NuzoFgTOHG69WdYtV5ARC5AHBmWa38DcbngrqUJ5KZOI_AjlMheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r17
@betinjabet</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103051" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103050">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f294785d1.mp4?token=O7nLSf_VFZLgyYCQFV4iCpHirDnWUNs-8cX-_qSMGHe8KfiTwUYFs1-OnJYZtb7EBQqy5AvGZjFR2FawXJ22wTtVZ48AxkaxJvZfo4RW3tJnm75hj-re0yy_nyPllH51KwbZ9ku1nD-O8GsPfywbiR1E3RgK3Q7TRJbl1oHPpKFgou-Vls9OY5sZ-w4Jbbue6m2r8c4DJN6CAZ3IhZfNAcGCP7_lulJ4rVsbUPOY789fUNKJr8sbEaRlvAve6NxCc-6XLh1Xrg5FG3T-VR7gqjtqDN7Mb_B5NTOEnxS2e-0_NGfr2YSDdzvimu0OLgGwVU7HiXshWcKx4_eox0otP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f294785d1.mp4?token=O7nLSf_VFZLgyYCQFV4iCpHirDnWUNs-8cX-_qSMGHe8KfiTwUYFs1-OnJYZtb7EBQqy5AvGZjFR2FawXJ22wTtVZ48AxkaxJvZfo4RW3tJnm75hj-re0yy_nyPllH51KwbZ9ku1nD-O8GsPfywbiR1E3RgK3Q7TRJbl1oHPpKFgou-Vls9OY5sZ-w4Jbbue6m2r8c4DJN6CAZ3IhZfNAcGCP7_lulJ4rVsbUPOY789fUNKJr8sbEaRlvAve6NxCc-6XLh1Xrg5FG3T-VR7gqjtqDN7Mb_B5NTOEnxS2e-0_NGfr2YSDdzvimu0OLgGwVU7HiXshWcKx4_eox0otP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚽️
مثلث‌رویایی کریستال‌پالاس با حضور ازه، اولیسه و ماتتا که شکار تیم‌های بزرگ شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103050" target="_blank">📅 11:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103049">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsB5b_fsz5ZdGgMfopNmEzNX426bDOFQ3ch3MJXR4OB-CKeXe1YCP6FKFS_coyeO2FHH8l-C0t7wNVXZouD5sKteQKu0vdRU5tq7HkNBI1VRCe6nnZWne1DQcmTB5_hcndoOrGX3Cm1OajN9fS2D_wTsPlGaDKfdozW_s4j2pcMCVuDweXGmPSxchZUnvnF1SvhDspNN5SIjsI9xX34Q_Zuyg6TVczxQP4y12RFu0stIudFQUIWECflVRQUTLJAyphBByMaVwT7mqMiy_-aWKk27qQytdOxpLJ6Iif79ZkF4OE4UdiNZ7uj-jSBVy-kEoSoYQxFPtgvM7Cri0a6j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تلگراف:
اینفانتینو که متاهله و 4 تا بچه هم داره در زمان تصدی پست دبیرکلی اتحادیه یوفا با یه زن کارمند یوفا ریختن رو هم و باهم رابطه داشتن! اینفانتینو هزینه‌های زندگی این زن رو پرداخت میکرده و کلی پول خرجش کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103049" target="_blank">📅 10:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103048">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3239f9b4b3.mp4?token=XZttmbKz32nPTBzBpm8ZhKQRSi1zy2mX1X1OV6uZAFqNE4qJ_pRE8MzN0tISX_8CvTp7WnGk5txpMauOxez2s4BQx_Vn_pzyIaFYQnI7ipW_ca82EAYYttI7o7FltI33mEzIMOYydj58LGpdu7_a10CV8hprHWVNY83_hcLslbOhlVKPXLB7CW5DgqrDDaVWKo20UWtk7fkcIw19dNO5Yw7hCnstEaciUbkfRsXMQmPQVFdN15msNb9ZCeZG3bnhOFzYclOWMkOiAlTDoiI3T0Bk_nOlPN37yaL2f7dPXiSuzcIe-wz2rp405ICvrcxB1LzZidJcJVg9btLVU5Y4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3239f9b4b3.mp4?token=XZttmbKz32nPTBzBpm8ZhKQRSi1zy2mX1X1OV6uZAFqNE4qJ_pRE8MzN0tISX_8CvTp7WnGk5txpMauOxez2s4BQx_Vn_pzyIaFYQnI7ipW_ca82EAYYttI7o7FltI33mEzIMOYydj58LGpdu7_a10CV8hprHWVNY83_hcLslbOhlVKPXLB7CW5DgqrDDaVWKo20UWtk7fkcIw19dNO5Yw7hCnstEaciUbkfRsXMQmPQVFdN15msNb9ZCeZG3bnhOFzYclOWMkOiAlTDoiI3T0Bk_nOlPN37yaL2f7dPXiSuzcIe-wz2rp405ICvrcxB1LzZidJcJVg9btLVU5Y4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تعطیلی باشگاه و واکنش صاحب باشگاه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103048" target="_blank">📅 10:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103047">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🙂
👀
واکنش جالب پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابوزان اسپور
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103047" target="_blank">📅 10:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103046">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563a2467b.mp4?token=jC5yQHFNDV-ma51WmvknATxESXBut7KjkjogngyFoZqbB4cpoTxIeNepmPulwxP_hFqZ3Zr1ObViNNVGAJhjlcj5u-dEJ-hroRj80pQtkI5048PxKd1pmhe_IQhkmwBoIgnBcwtZT0LulT_bvPTO0IiRm8Yj9-QrrKxxSFNGtQwHhhzg7n72bgHKY39sk-IpuMQvqs6sN9K7Zm5t7gahTrS4VQ2deHW9ZviSUTpQKt6XVP30wpiIIVUhH9Ls_Gl3wnYy3e3bTmsR2kZ8qTRBrE7JphNk8Zab-wV5FMKonARgbZ2AKV7IKX8U5BKINnimZjLWUpjmFa3UZsIkCZaopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563a2467b.mp4?token=jC5yQHFNDV-ma51WmvknATxESXBut7KjkjogngyFoZqbB4cpoTxIeNepmPulwxP_hFqZ3Zr1ObViNNVGAJhjlcj5u-dEJ-hroRj80pQtkI5048PxKd1pmhe_IQhkmwBoIgnBcwtZT0LulT_bvPTO0IiRm8Yj9-QrrKxxSFNGtQwHhhzg7n72bgHKY39sk-IpuMQvqs6sN9K7Zm5t7gahTrS4VQ2deHW9ZviSUTpQKt6XVP30wpiIIVUhH9Ls_Gl3wnYy3e3bTmsR2kZ8qTRBrE7JphNk8Zab-wV5FMKonARgbZ2AKV7IKX8U5BKINnimZjLWUpjmFa3UZsIkCZaopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
هنوز فصل‌شروع نشده لوئیز دیاز گلای سکسی خودشو برا بایرن‌مونیخ شروع کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103046" target="_blank">📅 09:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103045">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114a435ca1.mp4?token=D9WWrFEeNTttweeGIKa8WPESzw1Uih3I3Om1fIR-8Yhs1kql7hjNpbJvLIm4xzlEdfycy5X42fkNHZVIQUVX5xWza15UhVeRuZAB51PBsqQ0ZY7QS9TQE8sEbLmGSsqvlyboaX12yA21Acffjw4GlTsQ__wJ8lfubF0yacAWgJI8YCXvXfEneteN2somMyDIohqZxjuLJHk1qV41JgegMgAiVhxVs_G6Js9AhcD-diXbPIaoIS5JdcvNMkY_Q0Lli5PCyvwa9mEGaubNNNZeSXO0ATZgM6fSMKNT8Qo-9cNsGWc2Z8neFsch-CSqUwYWTp3-FB3kAsktKD4dM_z4MpcwLqTERP2UwyELkarXKshCKSEwyTua6YbmAz8vAREpjpfGc_kBjKCohIA44xGGOrtIFn6pKSHVAt1z1jrRwg68250tROc59qLyjHuUIvqUzEzgYMWoErwGBo7iDxpaIyokZ8D783aiM8ftXou6W-FS6g5jxv6_tMGgTtDtKgUAHPyBQ_27LDmkbeu0go4dNuPPV3ArWE_YH9XI3fmx5qCh5Q7yBB2UzXCr2evUNskvABbuKWbWpsE0tpkFvbJ0lsx3_FWaO565acQnVTJLUEcOUfSDThe9HhlY1kgmWmm7odpNN1ChIUuFgRJIncpHwrL3fHfV1vDo3nVzqGBYYss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114a435ca1.mp4?token=D9WWrFEeNTttweeGIKa8WPESzw1Uih3I3Om1fIR-8Yhs1kql7hjNpbJvLIm4xzlEdfycy5X42fkNHZVIQUVX5xWza15UhVeRuZAB51PBsqQ0ZY7QS9TQE8sEbLmGSsqvlyboaX12yA21Acffjw4GlTsQ__wJ8lfubF0yacAWgJI8YCXvXfEneteN2somMyDIohqZxjuLJHk1qV41JgegMgAiVhxVs_G6Js9AhcD-diXbPIaoIS5JdcvNMkY_Q0Lli5PCyvwa9mEGaubNNNZeSXO0ATZgM6fSMKNT8Qo-9cNsGWc2Z8neFsch-CSqUwYWTp3-FB3kAsktKD4dM_z4MpcwLqTERP2UwyELkarXKshCKSEwyTua6YbmAz8vAREpjpfGc_kBjKCohIA44xGGOrtIFn6pKSHVAt1z1jrRwg68250tROc59qLyjHuUIvqUzEzgYMWoErwGBo7iDxpaIyokZ8D783aiM8ftXou6W-FS6g5jxv6_tMGgTtDtKgUAHPyBQ_27LDmkbeu0go4dNuPPV3ArWE_YH9XI3fmx5qCh5Q7yBB2UzXCr2evUNskvABbuKWbWpsE0tpkFvbJ0lsx3_FWaO565acQnVTJLUEcOUfSDThe9HhlY1kgmWmm7odpNN1ChIUuFgRJIncpHwrL3fHfV1vDo3nVzqGBYYss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
✅
استوری وریا غفوری: تقدیم به همه جان های عزیزی که برایِ ایران فدا شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103045" target="_blank">📅 09:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103044">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbaa91a27.mp4?token=erseHJIKJl2AmJpOGZim-HlAmnCvVixC2fcNRyopaJRnJNVJbNq6WltFA7PtZlOf4xorYNbq14f-TjQnBowKJtqIqLf-U-dJLwmfjD8I_7PKkWWrZvWnhLuS4e1onGPm6EXVLfUXIKMsS_SGkLZRN88teFyldhJicq2QgrYot6EJA4oYrrbHNYW9n5mRJsVEuBZ7OFjCoZYBr5OPv5-7VDy0PX2xr7ZWihV5ilaE3ovWdxUaNz17kMy6iwSR1zTi9o1w1zxtrNeh5JoISLCrtKyx1QgvyImOnDwqV-zKh17p0wsJJlv_zarDCaqp2sPDtMRyoCE8humr89TKtHvkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbaa91a27.mp4?token=erseHJIKJl2AmJpOGZim-HlAmnCvVixC2fcNRyopaJRnJNVJbNq6WltFA7PtZlOf4xorYNbq14f-TjQnBowKJtqIqLf-U-dJLwmfjD8I_7PKkWWrZvWnhLuS4e1onGPm6EXVLfUXIKMsS_SGkLZRN88teFyldhJicq2QgrYot6EJA4oYrrbHNYW9n5mRJsVEuBZ7OFjCoZYBr5OPv5-7VDy0PX2xr7ZWihV5ilaE3ovWdxUaNz17kMy6iwSR1zTi9o1w1zxtrNeh5JoISLCrtKyx1QgvyImOnDwqV-zKh17p0wsJJlv_zarDCaqp2sPDtMRyoCE8humr89TKtHvkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✅
رودری که بارها مقابل مسی و کریستیانو بازی کرده، بدون تردید لئو را بهترین بازیکن تاریخ می‌داند.
🔺
او می‌گوید تفاوت اصلی این بود که کریستیانو در محوطه جریمه مرگبار بود، اما مسی در هر نقطه‌ای از زمین می‌توانست بازی را تغییر دهد؛ تا جایی که فقط با رسیدن توپ به او، حس خطر به همه منتقل می‌شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103044" target="_blank">📅 09:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103043">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/103043" target="_blank">📅 02:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103042">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=ETGWnZn63DZ0a0AbK6RPywqK1KiRxSYt4Tqna6ZSxOnw6trNvZBAkXQ4Wnbjgut7kpoY-BtiKWGx06muo9KKhgg4_8zwJWbERqkfdZhyeKN8RtUSQPAfqP_Hklcmv3hAv0H5redQ76xr4o8HH3pu8c8Rywe1Fb77NG5MGXzwFD-PjO9iby_BsbVcjHLzMBu415e9tE8rruv2v4XvzUru3MJUQAXjAuI0vGeImD2KbMN8g-iW3vsAR3I_PjcSTC87kddHG8cbMK0tJNhsDSgdlPrvjm4crHSM5o_K29XdayPltBDjowBGkncVXPp-JSqNg8ca7fbruhgId9H1QQEMZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=ETGWnZn63DZ0a0AbK6RPywqK1KiRxSYt4Tqna6ZSxOnw6trNvZBAkXQ4Wnbjgut7kpoY-BtiKWGx06muo9KKhgg4_8zwJWbERqkfdZhyeKN8RtUSQPAfqP_Hklcmv3hAv0H5redQ76xr4o8HH3pu8c8Rywe1Fb77NG5MGXzwFD-PjO9iby_BsbVcjHLzMBu415e9tE8rruv2v4XvzUru3MJUQAXjAuI0vGeImD2KbMN8g-iW3vsAR3I_PjcSTC87kddHG8cbMK0tJNhsDSgdlPrvjm4crHSM5o_K29XdayPltBDjowBGkncVXPp-JSqNg8ca7fbruhgId9H1QQEMZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❗️
ریدم حاجی اینجارو داشته باشید
🔻
حسین کلهر مجری سابق صداوسیما مصاحبه کرده گفته که یه شب تو خونه حشری شده بعد زنگ زده وزارت اطلاعات که براش یه پرستو بفرستن تا چنتا اعتراف داشته باشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/103042" target="_blank">📅 01:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103041">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9yqnQbmCjLC8AfdXFuboSp-kEJwMVnCSz9IcDturHUERKcQIT03nw2HEkHvOgYXdYWmbcE0YL88jCgec2zutSwkyeRhFJrwsiCNcoYW1K4KT6HQAZf-DMuMzXg8Xsg8YOY4vJ8k4FmrB6pycqHkfm78oJDpeAkxlYhiK3H-p9GzSwC_VKHV4Gw-MOzEbGn1k7mSJXWO5VOYNKtMlzmSWctcSUKaw239aT6XdblPzMAuizdPGpSROBp_cPNjo2JBhFytwvfvTdkdxVkGExNAks9OWz4IW5hc1mceHy9GeviFVoSJW8YmtNhi1Han99Q8K8H5FENc8S6IuiTQrpVolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
🇪🇸
بنظر فصل‌آینده عقب زمین بارسا قراره حسابی تیمشونو شوهر بده؛ مگه اینکه دکو کنار این سه نفر یه مدافع باتجربه اضافه کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/103041" target="_blank">📅 01:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103040">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geO7JYq7pbYufsHvHOLhXM4hdnQFdzyQUFJPF74hPjM-4fU6I_yrkvpvYVUNkDGTOkoYfUIfh_WZUn2R4mV06sSz1MLINYl48ecVJTkAjezi6MxoxR5VW1zcX-Ktzzxx88m6_eI4WLfZBbRYa_X-I3VcG03iBcbYYat83-8nmdKWR5L0J3K-tY3tvNz49ouviuA2T4q2uibSCTTRDMvW-V2XSeuGb2O2jEoQhgDov0k_Tz5wJrH6Jfwl_BjslgaoiljRWQ9IV80mCpzYyrg2lTuOTrtxTOMuIaO5gmg-OYl8Qk_aQCf9GOFSadeAxaQnrRxrbS1zIpia8h8OruZRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
لیورپول تمام حقوق آرائوخو رو پرداخت میکنه. همچنین بند خرید اختیاری داره و با پایان فصل‌آینده در صورت نیاز قابلیت فعال‌سازی داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/103040" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103039">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/103039" target="_blank">📅 01:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0fpaHTeIvoiAXfI9wBm7KoJrI5cf9kKCztjZrcFNEwggbL2cUbI8zJuFWTqtTYSxTTxTCrg-Oty8gSu1EB93up90zKoFQZ2D90z_R-O7nyqbKH0oIK55nSxOzjUr3v1Tr73Lu2X9hvDNv-ya9q4_OVOpkhmwLzR7N5iGesR9oyC4U6qWVTgCG4hmmzEHVvRAZP4bj7EFB60CmO8XsXFVaIr8B3mE_lEIyxct7tf9g1M-37DEGhA6Qd1jO01LKoSDn7upaeKgrNEKR8uU2g8pWz4iiT-Mno0u9OZD5MOoP-ofijHUX88bCznyuQyY4K3oHwbwqj9JHcTbVIwSvWB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🇪🇸
بگایی‌هایی که اسطوره آرائوخو در سالیان اخیر برای بارسلونا به همراه خودش داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/103038" target="_blank">📅 01:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103037">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU3Ii9bGbpMwrAM_-JoJj2GO6EedoZMdLJb60FSjuIEFZwxTwP-ubf8GtBPNd_y5OW94PidfJcJ_Rew0pxnCJjTOxHJ8-NFOTszVhCyScaIzr8Wgnl4hG-mEKrtl0S2ohW4NpVXY5xPP0S0sRX8nhPZiNNBeuRWtnOvtcd1IIWAJacfSV1Ya1oeBRjYMUzgcTnozaOQkprD8HyWYD9t6T-4eTR_2XwFCUSCzGHvMDTZImCrlc67jqavSqIp7VVyibqBcC00Eh8P-ZyGt-dmxmYrpAqyHMB0gwlZvbq_ZWxA3H7YDcEgpbi_TuhQJzkGFL2r3xugsfk0clSuPtZUlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/103037" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103034">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoeVft7QeZfJ966c2p0gHdk8nEHWBI4OkinOIEgxr9zZ-7Ah55EuqDYJkj-Gy53i8WbLyZ8gJNSCgmPw4SjMWSHu2gcC2nzZmqG5161qrybRagYWMYF_lcStpYvGq65aoxHucfj47B_C9a1-gORwf_OmRzPKf4fedFVDLubdrlMWIHAMzIujAuSW9JAovn7huOZATmoCSKaWj-y7qMxvHZciryhaqRTuUm4Pc4TzC8HXQCdozjItTTa7_pI9kIx65N_XRwaS7-lrpikvXXXbOFRSlqOcAro4XJDn3n7PVGjeIlnEOBkXzUIYDIoeD0NFqq9AQ6BmoevmVZS9EboL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🤯
مهاجمای پریمیرلیگ خایه کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103034" target="_blank">📅 01:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103033">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G83-X4zbP6OqAjXx_ADnjZB23jKY0vPp2hAOHIaFtdjvQlNsULB_Y2BKx9h_w7JfSFxMgDz5OByYLGcYjqvjoW_HQ41D9WxQMpCT3tEvTlwx-N8AkOaglSdHdkOAUIxRe9CboLpVeVb0YaL0oVjM9A6o02fc9muS42Ic5hBHyXKTF2whGv8OX5APKJZtNeEww8PcCHYo6RKW6dhXoHdHRuJ7ttZBFJEOswcs7jimFBliI6LTgoIIzCOpp-oiDydg-3MIxu08cASlpEgJbKyfCawGAmgWf2Mbbw3o6x97ggpcxqeSpwQPMdgx3zOsykUE7y4kgvH4hKWHOT2q7WVMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤣
🤣
🤣
دکووووووو بیشرف داره چیکار میکنه تو نقل‌وانتقالات امسال با بارسااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103033" target="_blank">📅 01:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103032">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/103032" target="_blank">📅 01:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103031">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejSsc8GdZB9p_JX2rQPFnSiJS4twBRexiryLK8D2G67NDXJ2gV03BbmwavGGINq_x7zf4HfgGk7q0BhX6dArPcs-IQgxn6wZuvn1mVdjacKHZXT-xQpOfzSXTLJfJ260pdIfmO0euRueRnexyVzHUOcrhjvs84mNfr4IJmPA6cOjjEJStJApVxkC44VpirZOl88gxgTWJiC49BkXO4pC3BKJdEykYL7Ety_qJ2AYfKueSLNgoB0OIPP4hLrdyi5U7cQGlBAtbHzHmRn4ORH27kE9qUhaBOgbDP2QUJ8K2cC-phO2esiGIVIfcMJwjF4giQFFSq6CHfgXU2iFzjErWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری
و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/103031" target="_blank">📅 00:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103030">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/103030" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103029">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k04J5wiQWbe-OdHLgrJREUuHijHqJw_KDIJBXUZl9mM_zBBlaO5wyYE7CeGiOxqa7MidRSKVH4bf11VRogG4RYAiWz9bLbMW6-S65ndPlYUDKDxWvkdr8uvTfOsvLjsYI69t58CVQm8rizCAJ8xc6Tmg4s3YLMYZax1UAvBMIq_YJf4mW7NrSxumxiRIvzHLpEn3MW68iNOePZcXY50sy-m-YcYev-lNvjvIlMsPTS-iHR6J9ojQHdsngdiGop12ChN4ND6REx8wqj7Zjc_bZt4EmC38yewEgadTpKqjTl6DY1G8lJ53wGbGeJeT0lHHZo5KTcQZ4rO5tViuExk0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشتون راموس عجب بدن حقی ساخته
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/103029" target="_blank">📅 00:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103028">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZiXv2pwHbFl1tjm0IOOxLCPx4q0bNR5sKs59aoNpRXAZZR0FqKZMgDOcOvmm7xZSV49UJZYkf-oiYqvVF7fZF1mUbUWsGrNy0UXD__LebvvqA7A0xZaOZuczj_Xm4D-7EnDUVoAa5OBQCVSw0qUGiE5aJkoLUE3UPU2jM8I95ojN5ZEHyBZPhpfjUHLc1XQS70f1nWVzMGGXPMOlwRvdsdYh1ze3Lwk9LM45wRg5aFSn9C0F-Gbe_imRahJYJ6AvMctOa3kvniav7dEBVfeDFFC7AItXkgtee1zGKQCSUJPgkpkYYPlcrhIT-KxUy_XPF2M-8S_llvjK4GT2tQ_YfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
آاس
: برخلاف شایعات، درحال حاضر شهر میامی آمریکا شانس‌اصلی میزبانی از سوپرجام اسپانیا در سال ۲۰۲۷ است. شانس استانبول و ریاض کم است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103028" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103026">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRdFqo9DrDFkuET0QawFzkBTxxe9FNrw_4s-YUfvnLn8WDqRKJ7KPlrfcWpCcq_x4Eqrd-d8ZzCYoPv8JFASOmbu6caMg4sb7xd1JlA3cb6SnGVg1iUl-KYbPJPvdAIjJlqUqsiravu7mIz-JVSZX4oT40rAc2Z7u11spygW3-37pdSISW38D-Jsx1uAhCAX6AqilZK2C6YHDufa0C7yd6PLZ2AOGaxK3Gds48osdUe5KoHKXZFMOIe4d0zbZyhGoPSGAubVlqx0LLxqryG0VC0HQTCo5Wmb9q41lUOuD4AxJHZDExKi1Xkzji6U2IXD36GpfpCYc-zZssPkVLsWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APuAL5r_a6kjv6jZbZ0lPJ4Z3stJZL6CaW8e8HwHWZOAmYcJdtpzK36IWmn0Gf1Y66hDe1vVY4sFBM4DbYnD6VvIfarF17Nw1LF-bGZcS5aKqgg3YALYs6tPYxytNbIYWIyt0GnRcEey6VMuxyAZZHTptjp2v8A4JD7lAyQiImobwxZ19ntnSrWEE6yDXKNa4fpy8DgmJB2EhImArE-bzQCPif4XEUxAlXVnAHWjhi4QNiXsQ_uLFeY3r5qs29S-P8M9xc5QtIN-vwS9xO4cWtiUAS3o9LfUc_IciYODdQCNzNbUaOtlEQuMzTNig63Utl9wEvSnZR1D4h6fHjJsVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔵
ادعا شده کول پالمر هنگام جلسه تاکتیکی مشغول تماشای ویدیوهای سوفی رین روی گوشیش بوده و ژابی آلونسو هم بعد از دیدن این موضوع، اونو از تمرین اخراج کرده و گفته فعلا برو چشمم بهت نیوفته تا ببینیم چی میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103026" target="_blank">📅 23:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103024">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnlkZ10BJ9pH2fcv3xghaDQradFVWkAqDrkSy7cL4wh5YTvkrfwa7STTV7IMoI6T1qnWtIPwRrlOvVI76Dy0Cpm7c_f5EuGaRQE7Jh0ZCxEQmrLGRo3g5LFMfq2l0mr3c2hAQOUjRBRK95SCzAagoSwgRNRztnSWkjhJsNCRhj_ACrx3v_DT9nq5HWrnL8BzbV2ivtxMP2CG0zlranHk1kATUK-w91Mt2uO6o06ahLH8_BYo6WC8eC8FXfGJtB_iQl-Twu_9crA1Bqpzm0-pW8LzBdzZrGYOelOOrvSdY4LZOM_ZbTovw1-n5hyellu1Vr8c2_WOdsQABqp6Z5RWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vl0gM2MA29GKWc8ODjpWS9RzZ4lRoBlMow6e56UIIJQTnNqUIm32_tZlnMfvmfIiTi-xsG0Iq2fYbJmI87Tl3_qEAjcndPToHjmanBPIjlx_JV14JC1WdY19k661beBmMvQDa0mR1uOaokOxipoJp85qKRPV-1-y7QwhQF1u5lum8Zmpy4Q6CcDKPf_Z_7YRndYW6BCNfThsWUZC7jxSuKkCKnc0OXOjSG_zKMOg8zIH9Ckfm1QnZ4X43szFpj5FCIYlhxsFkG1V30ut3fuG94Lpzd5ufaVX-0OfsWeD3LjpJFstdpe7flE8CEdkGXt_aVw2rVSf-GpaNAC_H1TTng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بازیکن مورد علاقه‌م تو رئال مادرید؟
🎙
یان دیومانده:
قطعا کریستیانو رونالدو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103024" target="_blank">📅 23:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103023">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmaXMFGfXyZgZ_8fTFpwBKBBUhtUT52AWn3MAw6WYopxH84gpJZm3ikGA_EPmWOe8ISBwbUWJXAAUh7YLEme6KKuSlGautRXCGB8UFYU9XZuoT3hjKKnvSFVAcIVZrjR6bbbNu6hXt4ueTLl-7v9_GBRXwGG_33tNeOuh1n_f1PNadVlGneiQuscgyiAg7secLOeeX3Q7BRNypvseG8Fp8yfDdYtqEWxbJIDt9g0W04ghI2OeCZwnmuCo5sLDp0LL2la9S_U5TCs9RMv7VprlecE1NU45wpRqEe_60QU1zmiXDc4DORzbsNzoSEZDlY4IcnveHG1kswk28O3sBb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شات خوشگل از مسی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103023" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103022">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdg9_HXIf9pgkXSh0kABCrtzlzH3S3pVXUsw1cJmqrFe65w7lMoYpco_IQB_73wa-C1dRKh_bbrsFL_wPGlcdm-Oj6yorqTpa-NWqUxADNUELJALXOJhiKXy3mC5mqkB849X323Q1oQixeICLUzRwaRd2B_DUeA1Z0Q9LkE-HfWKK086gWixqdwjUoq6VUAm_jgQgdsSsL7bKppTzRhTENDosKuFdkP4dy2hb6z4y3V_IalZwEqDV0c9PEpMyhtwzCXSBB93jdYoQN6cjDv_8alXRGVI7MtIdw1R58_UC-0OnU-abukqv_JXpCwkucCHdIanpwemhpSqx4oRO6PQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جیدون سانچو تو انتقالی عجیب به الریان قطر پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103022" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103021">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ea6e382f.mp4?token=BYKPFLKzgdOLWDD8wPAs7JZoyRL2G3dZ1iklXnV7UooxkvywJuNSnhksYaJ81RbrJCydbmA4euGVlSt614-UR1k_MmAoyX0tNkFrXLYi2_wxXsLEy1U0PT7-0jou9Ov-ktE42T7MpUakfWIAhpNVr-Ahkr0Atabg_aaLPsotr-k08ZO-4xEYCBxFwXTwgWy41tcw1LoxK3kqoybuoeX2xiXCYXLDCz1J6TSjZj1C2tTflpQN4-Ygvi6dLY0-cDKYXFjL5_4EeKlrHMsUnDi7357p-emMYqGk-eBklC1pX2ZpuvrFHUDjeH-4Gma_J7aOc-hkk0KGeiLYZ_XJmW0AJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ea6e382f.mp4?token=BYKPFLKzgdOLWDD8wPAs7JZoyRL2G3dZ1iklXnV7UooxkvywJuNSnhksYaJ81RbrJCydbmA4euGVlSt614-UR1k_MmAoyX0tNkFrXLYi2_wxXsLEy1U0PT7-0jou9Ov-ktE42T7MpUakfWIAhpNVr-Ahkr0Atabg_aaLPsotr-k08ZO-4xEYCBxFwXTwgWy41tcw1LoxK3kqoybuoeX2xiXCYXLDCz1J6TSjZj1C2tTflpQN4-Ygvi6dLY0-cDKYXFjL5_4EeKlrHMsUnDi7357p-emMYqGk-eBklC1pX2ZpuvrFHUDjeH-4Gma_J7aOc-hkk0KGeiLYZ_XJmW0AJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چیچاریتو: من کریستیانو رونالدو رو آدم مغروری نمی‌بینم. اون فقط روحیه رقابت‌طلبی داره و همیشه تلاش می‌کنه بهترین باشه. وقتی هم به موفقیتی می‌رسه و ازش درباره اون موفقیت می‌پرسن، میگه: «آره، من به این موفقیت رسیدم.» اما جامعه تحمل اینکه یه نفر از خودش خوب بگه رو نداره و اینو غرور می‌دونه. ولی از نظر من، غرور وقتیه که چیزی رو بگی که حقیقت نداره؛ یعنی بگی بهترینم، در حالی که هنوز نتونستی ثابتش کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103021" target="_blank">📅 23:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103020">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRM7LSLrRvUMbL9el3mhrRXmLrE_bIp4QuGQ4j8La61HGs5QQjzYmTAA5GfvMRZxDLkE5z3KYlgByxhI1P-G_mcZ9BKPayyw4V6QAcvKHitDBKpMTLIhuT8KlQbo7edX6ko3Hc_ajjpu4r-DWEBVbfZdDYe91QBYvjWAFJtniBl4TxIYoWCbPn93DfmhYRt_bDjiXUEezQGUZAFYgPyY3j671FAOkPesoAc2NarHHmrQ41mVBWpK8Jhduergad2xVbcBHTlZ3qVg1zLjbTxkoYaa0_VUhqT3URNcdFHv_xIkEUbzf4VIwM5Vj97rxdE2o9McJfjbY171817g9y2gbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
بازگشت تیبو کورتوا به تمرینات رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103020" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103019">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
جلل‌الخالق؛ اختراع جالب دهه نودی رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103019" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0EqRYZqqwzOoqPr5Ci6lW-otxcneqF7oU-u3jwh9sIJxO6y7IJvUmlUZiYCKCBBN_2sXtYFQTBUHhLP07nRDCxFpGnW2Ov9RO8BNTdPcFX2QlJQuAZLeX-__fRFyFFpbyjzePlMnuF3kscof4JJkBsKnIfZ9bnQj2hwByw4Z-A4HOHOsi-dYPkAWuVpXy6mXQBrk5MYpFvNpA3RaCgJxFIBSKYLv5AFH6kq6KlGoU8eW8yTOfYW29iz8zFfDe9-twZeRcypP-cvXTxL7z7V6Tg1zR4FyMB6Ne6lQakrwWe1GTEuzh415PNo_D4WSSmWETAkLY6dQZ1z-xGfYRP5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوپینگ با ما چه کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103016" target="_blank">📅 22:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nndNR2eOhx610itFlYMZXkHreP46eHIGRSyx0U7pwQ6ZJH4l_uXxqXdO7yUC9xcs5-eIa_13UGZ60S9zGzYv8ksLfG_kL5kacfxgrk1Nb-5CS2CtKndO_84Y1a-y4SqctFav7Jy69-ukdz8ifBtd5IFvHUwmnb2L0vWOlJ0AoabY9PBkHGZrPeBDc3hzZ9CTjFusjKAodsUSHF3ddUsk3VZHGiWfrc80TBzMRDC6FGl4oiqqrm-GydWU4veGawWmXxTQHe-kxawKkeo5KK15DRNvYuTC0-7QcK_z0du6_dh1hF5CtHZLxXH4v4aTKap_pFNTaVeX9Mk8wl64pn8b7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utMP8LXUuHuKi1T5Tp58JOMet8Bz8nLHRI-hsW5pHbY8M0WxBe3BQJXV1eDkiS-r3pyww2E9_NSgK2hfqQx3dBl3QwTgdgxtdqBJh6gOItQqWQ6wDzwpPCo-MP7B4yyzaPtXo6O1zADuP1HGbeJa_E9rH0sZzYDNNBRJwoybBSfQ5kCA_c3Ld5YkdQIqc6_qYH1ST1oyoNIOr0KN3XtEBAaWAmLgfBqc0j8z4IMXfBHBWDSZv5-Hi2fRpeZZ592SdeuwoytG5QA5vGs2ocXiq_sJaGDUPDAzZJFmSUBQmp3inVP4EQAYzBUN4l9SddpqCpqmelxmAsgGtlF1MXCBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzF-NA8ynDHNJ3nKSh98tatDT57mvgI1njE64JabyJnpjZBE7id3Wc48eQnAgD0SIPjaTuEMxs4qKzk58rfQ6yC89B9lvxwPS6kXyI1AAGLdgHlnxCAn5Rfgm22XG5WSN7IoIrXiMjiU628T-ASx3nmZ-GauxissE7OLhxm-OIxQAoKL2Op9WD-UOk5byrzQuxkxKaF6Q5YPPEHT-_2NgJcFu2RbT1-os16cpulCbRp0qu6_0PN26AHxdhcgV34gl-do63pua9mUMaAbP53pw3VO9lBn-bJUc3Casuw6L-_5-dHcSisO6nyqG6Y3xrze_C9ticUCU8InG2HGS9ZPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
اولین حضور دیومانده تو تمرینات رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103013" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcuxpmzIfjOp6lvbP7ARaPV0ZLvrpXaxzKVK7O7QeIw7oVXgFI_3OdhhN2KAFLKqfsIGN3dhIS1J0Kc79eF3mLwCDcqml0gYJBkRT-6b9efCQjDpGUay1doc1sNE67E2GcLuHJuQO8b7lYHWLLqKiA9TO07_sioOyk7SuwMtqDy7d6dIyIWpVF-lj2KJEHeBAvr2pYR9UNMoPqbEbBkSzYoXf7lmcbScC59m2sF8uSyPBEEumkXForzDdbdZiDPEtNULNurhYK8IB7T7JrcoozIb9NBW5Gy-j6NXMwNfGsn3YDILzooMLiqvXkzRb1KMATCjWC_g0q8bjNGOt_kqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: رولی گلر مارسی با عقد قراردادی دو ساله به سیتی‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/103012" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQoIpY9ThSgFgkv4v5rNjIP1jP3OM28mmiZGEYIO0dB5nOEZlfcFgFQ5RH5i_VCYrjEvN-U0UWIXeMpb-pTDoXaDA-LNDhqikeIjRiRIVcHOwsq0O7SIqKqIVKAITZNLA0VPsiEPXnmmlb1z8VYPnckkgKQwIaha-9RRcBi9WhNIKyu67dhPqk8gxzyKB2zRiovJnfnTIKdXUGoVGSYFPuuArKFte9InUOHA0fYpCTMr1AqMjDS-zoGJK0YMlUQKMKpQfsZ55Vwil5b1RnsHn_JOgg1rLrQUwTn7MWHUmsyKJVNBkQUt9_Tls6NSFAgyIxvRYjWCtDesyZltb13_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
ژائو کانسلو در تمرینات الهلال؛ مذاکرات با بارسا جهت انتقال دائمی به کاتالان‌ها ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103011" target="_blank">📅 20:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103010">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVx_E5uaAOpbMPfzQegfvt-cgC4_GA8LZH61amkvPRliG2atGD-uhzTmckXLZW-iOw8B743oMPJUxOVFdQuUzqrOBK-Fa74KhOhEfwIa4xO4-ktbLTsdwWAyMpXdeYYhgA1hfxiqQoUbi6m08xLlPXZvUC425t20vj_0KvwxEXMwTrU1-kQ6fXEBvmn9y2DnOo0hFIqltUC2v9HYpQYqcgHORNLS2ESVzITEgh-i5_8If7mazXxFqGOBeKkosX9LsnqWeODmUFQ6tx1Vani3FCcej7xnd5wZgGokWoBlGnmA2U4UPfDoVVz8I2pBdDIzx6ruLw-6v5zNe6Z7O_BEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جناب مالدینی بهتره یه تست DNA از پسرت بگیری:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103010" target="_blank">📅 20:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103009">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwQ32IpzeT6ta27DDOMe1ijUYjJicRA5hoptJ5SE44cLZcsP9Crcs-D01eYDru58aMe-REoxUeMUpO08nLc7j1jKGsbx1mEtnXZpd524cfijg-z_sFQZ_2EUaetFy6xD3sK5e4Cs3rsRRHy_7cMJSYInfIQXAbvJa2dfedqOCvcOKadGgAYcrHxCPgdTegazyM-dLzuePE7q-42rLzmHDD5FhSk4Pp2BRQYtRWTl3-gpqn1VrNAyJaHnbTazrHn1S16I7gIrtRWTSbhw2_fjIaOeR37HAGSznSZw4r_niHC-Zjfap1mDcEYKTh-tdnUIYI9f853Nx6wBUosFu-WJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🔵
سهراب بختیاری‌زاده فاز گواردیولا گرفته و تو شرایط کمبود بازیکنی که داره، گفته که اندونگ رو هیچ‌جوره نمیخوام چون جو تیم رو بهم میریزه! از طرفی گفته آدان ۴۰ ساله رو برای نیمکت‌نشینی میخوام و تا نیم‌فصل که پنجره نقل‌وانتقالات بسته‌هست، باید برگرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103009" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103008">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=LMBvVSbNBO9HnKRS9mSww8rWxbtw1V8oa2W7Izi3qTSD8JxsgGcLzHDn-SVwXjYObV8g94i-1Nk9hGz6c62j7DMF7-sGah0ZT4NSMndcgMdfBrLcXjKjC9aQUFtZGQ3_w6qQCVkmBYrzpqbIv3WB0uuOYuj9g5nPg2_2i1A6FvwnP8ywp6Nef5CXDANhGcA4f--eiLHvATfXkFauZgimLyyIwyrIBD4B7OA9bauImQ6wNt9KBJBq65dBGKdYW-YvsA50K0qlYyyiA1jObvlJb-0vKAypa8ms-I1tXBEyHxIiuCViPleCA79B45zi3T-Od3Fw9r5muxLqei0oHakLHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=LMBvVSbNBO9HnKRS9mSww8rWxbtw1V8oa2W7Izi3qTSD8JxsgGcLzHDn-SVwXjYObV8g94i-1Nk9hGz6c62j7DMF7-sGah0ZT4NSMndcgMdfBrLcXjKjC9aQUFtZGQ3_w6qQCVkmBYrzpqbIv3WB0uuOYuj9g5nPg2_2i1A6FvwnP8ywp6Nef5CXDANhGcA4f--eiLHvATfXkFauZgimLyyIwyrIBD4B7OA9bauImQ6wNt9KBJBq65dBGKdYW-YvsA50K0qlYyyiA1jObvlJb-0vKAypa8ms-I1tXBEyHxIiuCViPleCA79B45zi3T-Od3Fw9r5muxLqei0oHakLHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پیشنهاد اولیه بارسا برای خرید رودری بسیار پایین از حد انتظار بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103008" target="_blank">📅 19:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103007">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=GAcjJN-4v2wwh_77lYyPQV7FOx9eOoH2CJBHmc_xIA0cDjcZqkhOuiLONp8RsSDpl1_bIXu3UOKTPubSWxePb91L07AjpiXDiWuuV8aHRFMT7DCRC0k_b6H4gwMCUpbQjMJBZK2HN4pj71lD7A_O9kGRN5tz_HilOKbixwmC7bbSRQAmteKjgmSBawkRnGrrfoPwncMlNGKcYopf1avRjTdaRFPc87PhHUzgRJy4rhLd9vG2_72wkiSclhkebVZJuXJVm1nD1ssMMI0YGMXwYVZBrtKNyOoGH68yEz5Bn40xfufJzY40YAVQiZo_UmMh2EGVYet0WCWYaGvwPZHS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=GAcjJN-4v2wwh_77lYyPQV7FOx9eOoH2CJBHmc_xIA0cDjcZqkhOuiLONp8RsSDpl1_bIXu3UOKTPubSWxePb91L07AjpiXDiWuuV8aHRFMT7DCRC0k_b6H4gwMCUpbQjMJBZK2HN4pj71lD7A_O9kGRN5tz_HilOKbixwmC7bbSRQAmteKjgmSBawkRnGrrfoPwncMlNGKcYopf1avRjTdaRFPc87PhHUzgRJy4rhLd9vG2_72wkiSclhkebVZJuXJVm1nD1ssMMI0YGMXwYVZBrtKNyOoGH68yEz5Bn40xfufJzY40YAVQiZo_UmMh2EGVYet0WCWYaGvwPZHS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق‌و‌نوش لامین‌یامال در ایام تعطیلات در کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103007" target="_blank">📅 19:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103006">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRVod5xCsyrO3BnzusfRKUaeCQpYyYBTwU7AxC2Tuf5hbhBFNtqStx-Ndi_PQmTbXn0GIcCawTXTz59mET0AT0QQFxFCId_otr9AIu5CCr2McOzfmbqZHKcBbV2G6NCJInfkyeEVcNLSmp5Mz5jpB31q8p66LLHW_a-un7d-q6I2P07IwOeLT15IhWZbvQiyQ0H_JrxhRijfh1o7KiJS0GrWyXJhVS9gEBUzm6hRB1jAt3F88ZWVL8jgJR7i1pvsO6LUkGSv2_69ZOmD4Cvljjm0SIV9dDCQrl1HVZitudURFs7z-J_rR1pr21Tp9ZezxC5R--q9SHP4VgvooQVcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
دقایقی‌پیش سه‌کشور عربستان، پاکستان و ترکیه پیمان دفاعی سه‌جانبه امضا کردند که شکلی که هر کشوری مورد حمله قرار بگیرد، دو کشور دیگر حق دخالت و حمایت مستقیم را دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103006" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103005">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-ZFGxbWc03Qqu9vEt8sbIhyjEiXNT_qz_uMGpuCRj0AoArMtFTk_4ZBKGwOoDJztkqdHHgp3-GhlIEhaQzNsh27q8d6adDTEp31Bn-iKf8Z9ofuyYow74gyVBnbwJZ3UroUgCtz5z_hAQa9OrOZOUs-emznFT-5Lury5JrwIOaMz7fuvVzPaiA1oWXW4aGhueP43pzltvrbIjYtqRifZU-4R7AL3hrm6c8dWq9c9AKw2A3O2sKQqz6uEKWvhdtFBscTmg8ufOpHyCXeDWrDD7Q0qHjaaOnqofHtsV4qvVfTwyEgaZTPiRSs-_UCRsD8ZToJLAuxlUo1z7LFhUor8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین دریبل ثبت‌شده در فصل‌گذشته اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103005" target="_blank">📅 19:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103004">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVW7AzsUmu8NRwF1mL1DHABV6rFei_CV7R82JrAFxlWFpsTAkS3hrJaF4KjOsvYuqo6o9WArrAfoaXxEMEtrGJ3aSStLLTrys50XgSNViNkTAp_CXo6QmCMu3qiJ-tXyXE2HHEAFS3TPkV5ZuJVCfQo67phefj9sCXFxBhhJjrD2LfxePOc9vdSvnjaBrJns141mJ7tJVssYULFBD3oZrn1SzZ40WVeNURNF10_E47Ld8--DboTU_rwRLvqSTsxC49v2o1DHyCAGuFN7lf3A-C1ux8bv3Mi7bX7YX7ecN9CFRs2RT8nwh9qxgFATo3jY0UYHX1QjBl6mKKvEgrI4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
خوشحالی بعد از اولین گلت چجوریه ؟
🎙
دیومانده:
به این شکل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103004" target="_blank">📅 19:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103003">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=YMIQQzyZ6PbbqFQlgFrkOCvM6Ro7x_wrRDgjuVMb0yklJNd65yjLEuqiHPJI6aJiOqjbkTAcEFMpWEXsfMtpsY6kcqSBtm7sIEXJXmRybvEvettmf2dW6ShIPF00kdX8IO-qBOhOIlDgrTdvFahSudQOk8YKPp5yC_ttHlI990XfaB_Kbiltz5_xyYuLcwuwTXj-O3jkDbXLq5vkjQbmQZ05f6NRY0rHZM0eLDkDpD6ewDloq1XYKYpxTWWPpQlJm_GmbT50zUwTqdWV8XvpiChYAQYQ-d9gEu3W8Ilm5WBRphtknxVkBlqPKT141kxVB5SPRhJcrkMpeFAAVOa_q7XedL90KPQdarwbHiB1_5WeGqPCAU9hNx_7hTTuzo4onrjjLNUUCJRouhlp2a6CS3r548iU6_pZZB3-ttxUfOKE-IfWa1x7a2-H-mRhxMnx3g2dIGQn0coRhFKygBaPf4rsfizo4MAz-YDYFiiJ7I6X6XkS3DoJ6LEeMbEVL3r3gviWVu20LthIMbjCEgk0K-LgPuIWWb0edMWhi_wLUZvmHrpe0UreD6SbpnUwBbwnv8Xyxi1aQGPiQaA0vW5eoXjo5P3sDQgBddaq8s31SPX98HB4iRA_oDEeSH9nX020_XbZVtVkFA06Jw82eE69XbGwp8CVqSoKqZ9ZlLU0MKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=YMIQQzyZ6PbbqFQlgFrkOCvM6Ro7x_wrRDgjuVMb0yklJNd65yjLEuqiHPJI6aJiOqjbkTAcEFMpWEXsfMtpsY6kcqSBtm7sIEXJXmRybvEvettmf2dW6ShIPF00kdX8IO-qBOhOIlDgrTdvFahSudQOk8YKPp5yC_ttHlI990XfaB_Kbiltz5_xyYuLcwuwTXj-O3jkDbXLq5vkjQbmQZ05f6NRY0rHZM0eLDkDpD6ewDloq1XYKYpxTWWPpQlJm_GmbT50zUwTqdWV8XvpiChYAQYQ-d9gEu3W8Ilm5WBRphtknxVkBlqPKT141kxVB5SPRhJcrkMpeFAAVOa_q7XedL90KPQdarwbHiB1_5WeGqPCAU9hNx_7hTTuzo4onrjjLNUUCJRouhlp2a6CS3r548iU6_pZZB3-ttxUfOKE-IfWa1x7a2-H-mRhxMnx3g2dIGQn0coRhFKygBaPf4rsfizo4MAz-YDYFiiJ7I6X6XkS3DoJ6LEeMbEVL3r3gviWVu20LthIMbjCEgk0K-LgPuIWWb0edMWhi_wLUZvmHrpe0UreD6SbpnUwBbwnv8Xyxi1aQGPiQaA0vW5eoXjo5P3sDQgBddaq8s31SPX98HB4iRA_oDEeSH9nX020_XbZVtVkFA06Jw82eE69XbGwp8CVqSoKqZ9ZlLU0MKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
صحبت‌های روز گذشته پدر زنده‌یاد مسعود ذات‌پرور بر سر مزار این قهرمان و اسطوره ملی و میهنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103003" target="_blank">📅 18:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103002">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=u45HMZLCmxo3JZq32v4xL6du7TPMj3GFmqiPWYbYbjhaojv2SBK5IcHe07uTjrgqVO2ZjjoedI69opxRJBsQ_WfWXc3ElnMPB35oFF9UPGO6mUyG4W-mH1S-PQKMWqgr-Mgdr87rLAZvdw-mlRo1PwSNLnMjLph5Ywp1W9-yT-qRC_lXQEXfT2PgxSkq1OnFGxSBqfXLd9sFZnshzCb7gvaF_340ClbbMUz_J0-chk3qcGNZvIbX6A7vtpn5KDl2f_HrYH2VGMdfCq6YPbPmfbYftE8T-c6qUOtbCgvXsb6AC3hYGxF9VExZubVxS-J5f2Ih1D4V0EyQUmYkKUPFWoCWbCHipw6XOR12tbAftWo8qds8Sxyg08TqRkaYRjcfMO0583ceTI_q1lfefxFbomepsgKfKlh-MXUALs2J0hJ5Ft0_V3lPcLC_89a73Oqa2AwDY7VDUmEo_dGBznL-BClYvVgSS3U2CZpf1ZWobsoUK74RJqd_Ys7So5ly-bTYonGETbBbl1jSRw15_BpRUxs5Af5nGVAWqzGGptyUV6wRWUql5kvIagjsjBqITyOd62lHQ9q4erII6jOl2jZ71iRA_etgyeIuK8jMtV7qMpR3oq3HE8RjqtI0m5lrXiYOMtTRQmbN0iIn9kCq9-K8cHk5Fdiycz7SH69b3SzfW50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=u45HMZLCmxo3JZq32v4xL6du7TPMj3GFmqiPWYbYbjhaojv2SBK5IcHe07uTjrgqVO2ZjjoedI69opxRJBsQ_WfWXc3ElnMPB35oFF9UPGO6mUyG4W-mH1S-PQKMWqgr-Mgdr87rLAZvdw-mlRo1PwSNLnMjLph5Ywp1W9-yT-qRC_lXQEXfT2PgxSkq1OnFGxSBqfXLd9sFZnshzCb7gvaF_340ClbbMUz_J0-chk3qcGNZvIbX6A7vtpn5KDl2f_HrYH2VGMdfCq6YPbPmfbYftE8T-c6qUOtbCgvXsb6AC3hYGxF9VExZubVxS-J5f2Ih1D4V0EyQUmYkKUPFWoCWbCHipw6XOR12tbAftWo8qds8Sxyg08TqRkaYRjcfMO0583ceTI_q1lfefxFbomepsgKfKlh-MXUALs2J0hJ5Ft0_V3lPcLC_89a73Oqa2AwDY7VDUmEo_dGBznL-BClYvVgSS3U2CZpf1ZWobsoUK74RJqd_Ys7So5ly-bTYonGETbBbl1jSRw15_BpRUxs5Af5nGVAWqzGGptyUV6wRWUql5kvIagjsjBqITyOd62lHQ9q4erII6jOl2jZ71iRA_etgyeIuK8jMtV7qMpR3oq3HE8RjqtI0m5lrXiYOMtTRQmbN0iIn9kCq9-K8cHk5Fdiycz7SH69b3SzfW50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تو مسابقه مردان آهنین دیشب نزدیک بود دوتا بازیکن با همدیگه سر یه چیز کسشر دعواشون بشه که بخیر گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103002" target="_blank">📅 18:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102999">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IN4_4UvzG2GRAkymOncF6U7rA-ixCQ1_S6rU3a3T97jzTWpIn3vo5id8AyjPigHlFkI2pCeVe9LTs25oIU-YdOVdeegwSFEQtd45xdxFQBww-vrMguyvnCG736s8wxg4IWd1I5kNiKFXq7BOLAhXg3taFLpi4wd8SyUw1lJmDYtRjj7vdiPqdfsHXlLSbqMTYOBQz8VzgeIjLM_KAx6xs0FyDZnUuo0v01SPsvBmA48LyyTbQ6QjAGfeYb2AI5jTTj_gg4xw0I72tR5KU-WwY748w2QwSq3kSLZhaMEFlHIQJvei4JfMKZh1R6a_2Uj3xpLcbnMwh1HBPUhyyPMXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaorvnXw-769zW6h_uiwhNMe3ubbAUUqiz4G_XWoMpFphbD-bAeqCpwGFqGLKXMI2oW6dK9CWonfNxSrfEB1osDdct1mHrkv_-NitEmYZzgUJGJ8OaYrMXUpXKxnpbVlc8XFiNl4Er25gFdZqCPL-d_qbHJhrZ7hLUgzDRkbGcYtYEikQp-Ey2lUlhcjr7mYtqqXlFS1mhqZfuW-4ZXtqYiRmflnkA-stodC1qSv1aL1ZBrwCy6R9_LM6C7a7bbm8nRMThc5TvakFd2ZDOMoKSqjNtiE2tXP_6TJMmrJl55l-1eftqOlNXuAq22ku0EtEwApsb-92fPM1qcRxS-pnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kF9_CUCWDPnpNHD6vMJJ1NxWEmZYrXsYQXu_xU87leQIvXs8SaA2xN8XOE7rYVKSH_ZIyzG9JKKYrCDe64AMBNqF8FFPx8eoi9lk7brcfTCt47x5UwpwihBXc-QGlWfcXVy4j6HsCUbx1icXQR0FWMF3llalEOwLe_q8MfGumpi9MYPu71SJSl3cwVX1B3Zsoezz4EL9yBJP4xu-dag49b_kEtZRBz_f_84UjXYhHTqmL8iZAiiRnLg46Lsona1bY2JS5jfX21uXeMpnGi0RnqrDkihu-6Co8cmcW-C0uVt-Ucj6VmX2jeolfzZa9R6O_CHZTo2zgTcMI6VjedF36A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102999" target="_blank">📅 18:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyXyolOtNBvGiQhBG7X2Z29vOz2TxDaGU9tVshpnLDO95zNR_5L_4tdlr6oGD_jjTVBtYO5SyXqGb4glECMnBInvkKQR6ZVkTlnkUomQBgQlgrLP_QQc26TpsH9B7Mqz-F8uc72ZRrPRUrKJZLZJICn-XQtbXufnP0sXWd8wxxobMCP11b85jmgig-T5bgPK6mzbzdTiYTOvVrxzJ_pyDC_fTueIsL9YptLD-IzX9z1m1D9T-fq6cSOAPsouLusftxnEEHWjHtkaSS5QeEDyQdBz7dUm-xmV7W8wRKn_xD5U3aBAsZ148X4KDIHdr75qHJ_N59iBgFN3_xkfhpgEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rFhOqNyrQ1Mm2NrFsrz6bDyM6rIUxbOyWP7I3okigeNLNZlbrcki7Yxzz_gpjbUA6dwBpeoRmRruYD8sbLhrJFBht-ikyhPFJ8IadGRm13lyMI-lyL7xbJGEwrqecb1h3EY_XWOKdKzVz_8uep2nrsviji3p2FRU_NcjYroM8iW50lpQaeEIrEJH2Blc1O7e7Zdo8KPMCUfkx0mgoi2WiN3w51yzuaGfZ66rGZ08gWjwtjlmcPDQ03SUD0sziFnysVnQTiQTrcp0SiGKgMzKpPED09XJmA3RJ1lD9BVALnQVm5Qg0kSFhUBFBp7AMILsj36I2Xgggnw16M4uaP1q6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sK6EPMgIJWT24XNZPOKhVfzY7nPH0LaLU_K2oOG-z95jrxcu3xvvBdJJe8cA6-E5aHFwwNrGC2XnG9-d2r3T5TpGaeZlU6h-Rj13ka31Ahz61jNvZ7DbiUBb1rPUwSMmWCVSDT5sT1qUI4j-LltZjZn-O4qzuq7_hVS1_csjDggS-DGZr6eCwJv1t1ziFCrf-CXJ0nZ4dB7Zuo0N9Ctv8Od4-4kiTUqXHB1O1n5FP8r2yfJjtvGbdaWhB9rud-Kle3yh9PwxD9r1V1rVxTd0WT2stKd0FrFBZmnDaPbSE7gEu_Af3l3_2Hpbz00V5QbhxBYgTG9x0NQf-Hjdgpdqzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102996" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tumo2v7gkTTzZdPSvUKdrVOvySFZtugbhU9VIIK5vrJoupBXLdU65-gHm_scCvXX5S9OF8uA-NV8nJ_5ZjPf2Vz9XVbjnDD3IgCi3Qh4JNOMRgsgUOOdCHynWyuhAmtW2Rb-OiAbDMR_wSXLNqyRiq8V6KV_Jp5Io1C4ro8sIiSqGAfKUfCaROy5en8zPzesubTEysl-m9QrfK3R_Nhvhj3sfTZqqay8Bqj4fhOXJx1qMGP04RcI7EbidQsSiQlAJvDAO8u7kdWPXmafcIM-zQO8PH0mV8DyCkvbPrCEYtW2Yol9zpEih6anQcv9xMjg2exGVOO3z9-fVk240awLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیومانده در تست های پزشکی رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102995" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
❌
#فوووووری
از رومانو: رونی باردغجی‌ بازیکن جوان بارسلونا که در فصل‌گذشته معمولا ذخیره لامین‌یامال بود، به صورت قرضی از کاتالان‌ها جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102994" target="_blank">📅 17:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuslY1JR1lsXSir4tZ9jvu_EKATecLv_EUqY03DES7eD_q4koEPR1Rq7V_1Rwbt7uV2jhr4UTGbHh8SdstluQ6p7h50kiChuiIPcDLLYO_nCgTO944K52RfFwxOM65cN9wzuch0JVrEDeOnzexey3MC4EbkohHfLmX67X-9RWv8YMxON_OlwzlGpI7soCy48wMl1t5iNBpC1BJSvhaJQugfcJ9YEzmztOFe4RZ9POkS5LLsQefiJL4h0p_TbX9zfd4yf3VWt0TDY3q77WvsaHTaNqfOwkZPivBTujVHElZ3tuwPMyYueSg8gqDjjI_ssd4l2gZw462DNJOr9oDU80A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
🔥
🔥
✅
بنظر باید تا اواخر امشب شاهد خبر HERE WE GO رودری باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102993" target="_blank">📅 17:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn7IYNyqRENzxlQIf_zSNMXbq4Ex24cl8FCIomIgpNztUnBLly10DGSl4E1a9OBkAIZW0TU5v4ea2GgMHgY7lnWK2XH92tJufR9uRrVinOlBwyQu5j5efuKd1ruG3fZjEoPmyx1-5PesPHEwPWpyg8YgreYO0Dccmi9-FJltyRDd-5BSndH3m1DocKJuw2T0NkjSDat-WddsAitItnLAPsv3gCeOdyYWY-J7n1zrIwwgGeFgnXozhKR5lD00ZcmwgerzZcOLBqVzKqUHyU4AYCvgK_OA5vGBoerHA8LXimV3GGS3_RWXNWTA2z1OcDPoaCMldqc09go-mDyzsv1XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
#فوووووری
#تکمیلی
از RAC1:
🔻
رودری روز ۱۲ آگوست(چهارشنبه) زیر نظر هانسی‌فلیک تمرین خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102992" target="_blank">📅 17:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از RAC1: رودری با مبلغ ۵۰ میلیون یورو به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102991" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=Uh76GdQe68-ywrJKOnSq409xUMk8B9sKdo3Mb5_PUw4oLveENf9RzhOBgm-8QXia6ycIja2PVnkbPXvW1t4sqaSsXeEIn12AAgZ21VTcBF62OvN0OU10k11p6WnAIS1RY5qNjiGR7WaB-OU0bSqLKsgDOQWC_tkFHoaE_vQDopHDYmZdkSe6Qu8QtafIIZ_CeSfjwLTO9oD-ZFJOU_PC_gbDwJXdnLP-XRdEEMtb_RmboFc2vxKvUHgy0RFr2BufGR8D2XcpIWjGlrDDVkQ22Ui_VsNiXoQTFiaHjcZgC_Fm7cTBSWiU5e2bU6i-TYSxtWJPyGhKlBpm1Qqf8_-Itw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=Uh76GdQe68-ywrJKOnSq409xUMk8B9sKdo3Mb5_PUw4oLveENf9RzhOBgm-8QXia6ycIja2PVnkbPXvW1t4sqaSsXeEIn12AAgZ21VTcBF62OvN0OU10k11p6WnAIS1RY5qNjiGR7WaB-OU0bSqLKsgDOQWC_tkFHoaE_vQDopHDYmZdkSe6Qu8QtafIIZ_CeSfjwLTO9oD-ZFJOU_PC_gbDwJXdnLP-XRdEEMtb_RmboFc2vxKvUHgy0RFr2BufGR8D2XcpIWjGlrDDVkQ22Ui_VsNiXoQTFiaHjcZgC_Fm7cTBSWiU5e2bU6i-TYSxtWJPyGhKlBpm1Qqf8_-Itw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای رئال: اون دو هفته ای که ما با رودری به توافق رسیده بودیم و وینی هم تو راه آرسنال بود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102990" target="_blank">📅 17:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=U8pITE0J5bcjfwvQ69UUkHInZiRT-oyHmsAhM22ub9QUtxhfqSgpDd9FEI_q2dTIH8bze0k6nZ00uwr3XBB-f9-SuaVeYW9XT1mZ4mC1Oad7DG48TsnJp0PLlzw8xzB3hDXTf6AwAGNBHdyTliqhnJGVFi-advwKz1-jrSpYaexP5vzX7AjePV5wnkUVvXUnqzSswICeD6VO_Z1uHZMpnlRMNShECMS9m6NIP-fKHVm-eEBRAuRXdBiwumWQ6iOWFzGEbZhu415S4INFWaUAufYrlOi1XPj8KD-HkDRC3Wywcrsidb26lHjGYZWjOv08wOGq27hopnnsz6f9rA17sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=U8pITE0J5bcjfwvQ69UUkHInZiRT-oyHmsAhM22ub9QUtxhfqSgpDd9FEI_q2dTIH8bze0k6nZ00uwr3XBB-f9-SuaVeYW9XT1mZ4mC1Oad7DG48TsnJp0PLlzw8xzB3hDXTf6AwAGNBHdyTliqhnJGVFi-advwKz1-jrSpYaexP5vzX7AjePV5wnkUVvXUnqzSswICeD6VO_Z1uHZMpnlRMNShECMS9m6NIP-fKHVm-eEBRAuRXdBiwumWQ6iOWFzGEbZhu415S4INFWaUAufYrlOi1XPj8KD-HkDRC3Wywcrsidb26lHjGYZWjOv08wOGq27hopnnsz6f9rA17sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مسابقه مردان آهنین و فرامرز خودنگاه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102989" target="_blank">📅 17:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQy6QBThB5Dt94-xM3GYGr6gYJicdxAqsHuYEX4pJCzlfvks_T799nvmu7A63B9DlAaKgVayd0PYVAlLiVCbp6Q5mKrceMcTCFAK2Z4PKLdBRJbZ7_WmlHwVbf_FMuwFAtYovIkANr0R-JSlnxn64FLYwamShfNKeZpbAHuAnnHGfWMtaRToz7Jt451VL5RJ6_2adK7wCdVPIDrODz2h86P9A3b-eV1kH0e4149e0Fn2JnF-i-Thx2TKrwB51V-0GnsqqPixH-tlW_xZ7Bbgyf55R4qNUbKHsYmIjZb9Czd0QZYoXtFFCMDCU784xbyfZ7oUKqz4n-92LnJw56A5eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
اورنشتین: بارسا پیشنهاد ۴۵ میلیون یورویی برای خرید رودری ارائه داده؛ درخواست سیتی برای رودری ۸۰ میلیون یوروئه.
📰
رومانو: بارسا حاضر به بیشتر کردن مبلغ پیشنهادی خودشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102988" target="_blank">📅 16:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=SMbVjTIHmkT6bbwLLvKzP3zx1UCMRa6VVzHtX4VBCDjMSl1SDqIfV83EZLwLZh_LcImL7qWFbv38qQnFpymQ8Mzprdly81H61os3nP360KiNuILdI8pGl_rAwhk_Gu-sNEHyWU3ao0OmksuUUwpqFevrfrKaH6tNT4efJR-5jgPpUO4qnBsw1htFHtaApt9_O38PNShpum_osH67aLxTnYuOT-LMmdZ-YAU8dtlNvSilTVf4HXoQVG2OA6z3wUmnNLsAUmu2JJ67XYP9I_C6pscqSBQqM-jHqBxzfV1syKpnY6YapqBP48ZvB9Rya_RiYOepsfO2I62gmv4_uR6jxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=SMbVjTIHmkT6bbwLLvKzP3zx1UCMRa6VVzHtX4VBCDjMSl1SDqIfV83EZLwLZh_LcImL7qWFbv38qQnFpymQ8Mzprdly81H61os3nP360KiNuILdI8pGl_rAwhk_Gu-sNEHyWU3ao0OmksuUUwpqFevrfrKaH6tNT4efJR-5jgPpUO4qnBsw1htFHtaApt9_O38PNShpum_osH67aLxTnYuOT-LMmdZ-YAU8dtlNvSilTVf4HXoQVG2OA6z3wUmnNLsAUmu2JJ67XYP9I_C6pscqSBQqM-jHqBxzfV1syKpnY6YapqBP48ZvB9Rya_RiYOepsfO2I62gmv4_uR6jxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات گرما روی رفتار مردم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102987" target="_blank">📅 16:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=Use_ISepckCJY5uxwUv_9cVSvMjgFAWSTU1-k0ksgV5tIE_WSg7PYITvlNh39sarXpD73z7YXYuidfUaoSOVspbyWmNXnLxUpi9NRKeZTAtFVqjpsiDi_wyJGe3eey5fMw5QALNkHPOYc5g1l07jYbdYYCmL-2Tn2pQFo3jWdfwcUKCmiJ7fu3YnPZt-ontu6A-CX0S3b4nVXqp_OTNjx7PLq6VLX9iJasyP1sm3Rorz1XZzAyebZymkglGipWfV_Lnu6QJwNY0L2rHpDnm2rAxvjAVD7ESXt1VjCcJmDpVZrdhlAgEwsyw16ZCi4tBBghfkthsvIJWMztPp3nNJpyk0GXicaCr1gqu5ScJ-vDEikObJpwAGJ8y8GcH0VXiEZ15-fb-o15exQ8tNtmnXU9yvKF-eHpnG9uEplERRV4yoVA3QAhgp04EqJb6vXDPmaYr3FLU1gKEEdHKml7Z2E_v6U1is-dwTed0tymGQk_Smxhugky0s1Df-BQvJMFPq1FPaCDLnHLDDWtIudoVR56-11HmeX4cvseJZdBH6SDtWhBvq6bJoFxRKcRbrgoCQD3-srB_HvEW3DZVmnwU40MXuvNyH-nXw7E2g4nCqcbWJWvfsqrzrurD8Rj0y-n2kfTKitEl0SgAFiszSgIoSDQkwavXQQbpBCsQJdYFsxo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=Use_ISepckCJY5uxwUv_9cVSvMjgFAWSTU1-k0ksgV5tIE_WSg7PYITvlNh39sarXpD73z7YXYuidfUaoSOVspbyWmNXnLxUpi9NRKeZTAtFVqjpsiDi_wyJGe3eey5fMw5QALNkHPOYc5g1l07jYbdYYCmL-2Tn2pQFo3jWdfwcUKCmiJ7fu3YnPZt-ontu6A-CX0S3b4nVXqp_OTNjx7PLq6VLX9iJasyP1sm3Rorz1XZzAyebZymkglGipWfV_Lnu6QJwNY0L2rHpDnm2rAxvjAVD7ESXt1VjCcJmDpVZrdhlAgEwsyw16ZCi4tBBghfkthsvIJWMztPp3nNJpyk0GXicaCr1gqu5ScJ-vDEikObJpwAGJ8y8GcH0VXiEZ15-fb-o15exQ8tNtmnXU9yvKF-eHpnG9uEplERRV4yoVA3QAhgp04EqJb6vXDPmaYr3FLU1gKEEdHKml7Z2E_v6U1is-dwTed0tymGQk_Smxhugky0s1Df-BQvJMFPq1FPaCDLnHLDDWtIudoVR56-11HmeX4cvseJZdBH6SDtWhBvq6bJoFxRKcRbrgoCQD3-srB_HvEW3DZVmnwU40MXuvNyH-nXw7E2g4nCqcbWJWvfsqrzrurD8Rj0y-n2kfTKitEl0SgAFiszSgIoSDQkwavXQQbpBCsQJdYFsxo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وقتی صحبت از خایه میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102986" target="_blank">📅 16:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=nCOeQqvJX0EK2Mxn106NjF6g3orc8BFX_eXiSWJybjQG3usWqOD8LPsDqOxUqAj7NhYwPhzEONt_qlHeW2ufZ5BD8S2KU5w0W21EpYzfsb4gDD_y2WC8VxaDUNGJ7QLZEMu2QGIs7o-m0Y8BJVT_ipoJ8o8_DIa1YJYWUWKypliPULEChWlBqT-99q2FSpMIdHC06HCQcH4x49LRBFOZr1HhU4ZEgGFXrfsG6nG6SBfG7YjUAmUA4IRID7IyhQucdMpYs9tdbiKvGoD9HZEEftf3l3Yvnis75dhRmziJu2oMFXD_cUzUTIJx2nK1nEoA7UGYrMTSdDw-W9yZCV5Aag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=nCOeQqvJX0EK2Mxn106NjF6g3orc8BFX_eXiSWJybjQG3usWqOD8LPsDqOxUqAj7NhYwPhzEONt_qlHeW2ufZ5BD8S2KU5w0W21EpYzfsb4gDD_y2WC8VxaDUNGJ7QLZEMu2QGIs7o-m0Y8BJVT_ipoJ8o8_DIa1YJYWUWKypliPULEChWlBqT-99q2FSpMIdHC06HCQcH4x49LRBFOZr1HhU4ZEgGFXrfsG6nG6SBfG7YjUAmUA4IRID7IyhQucdMpYs9tdbiKvGoD9HZEEftf3l3Yvnis75dhRmziJu2oMFXD_cUzUTIJx2nK1nEoA7UGYrMTSdDw-W9yZCV5Aag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گذاشت همه چیو رونالدو انتخاب کنه
#احترام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102985" target="_blank">📅 16:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi1o7c7UOd4wESqNhDwFfdCkZO-rRh7yOdcWIEFnGdZj7_SzzEW-lJpu7gkMe3_upf5anJvoS0y4xdFRkHwkmuOUYYSnjfeHNrPVMyX8460vRqRzW_Ab5qLGLKxcPaVcgdLJtgwUK8Djg9_SGtCejjCg8csieveZuM2GGteGblbdc6C22gXWCSIkMz__IraapX5y-0_5iELd6YoRX0PcZ7wg5BbdeaYMrkU2rTm1eYBuBsQQ6RILOYeej0jCGKfwlzCLIfd_UJ20NZNdJhB3ido9EIQOlJj5KYcU3OfNpxN_v0vo23vj2Oo8oy_2Y-vRKVq3F2Ls19NeeWATAS856w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
منچسترسیتی به توافق با لیل بر سر ایوب بوعدی نزدیک شده است.
این معامله در حال نهایی شدن است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102984" target="_blank">📅 15:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=hUMJ7MF5uMnAw8GTfewduWjbBMyZH0oR0ir0poDSEoc6O89J3uBZBe9J3YyN3j3D10EPiolLrU-EB3B_Y7QCmCXYY2V4_P0Nxi69x7OlJknCuAmSi5q-HSY_cJkYmsr45DD_vJ_aOGx6TFq2lRdLHVPBdVFas2t-mAoP2-4oNT5Ov7m3LvU7SFKm-_XFClXv0HTTribkb9dBBjF1OZ6QICo9vw21Gm-fvUGohkJaGgbLRqSg16IPrGD_v_WShm_fjHi26nxtVTrhaXWL1mggJAhrhMZBrLZk9CeVKxs0BLOjMvvycZGR7KDNug6QhJgpi2TkreiasBjJN6C1rwJqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=hUMJ7MF5uMnAw8GTfewduWjbBMyZH0oR0ir0poDSEoc6O89J3uBZBe9J3YyN3j3D10EPiolLrU-EB3B_Y7QCmCXYY2V4_P0Nxi69x7OlJknCuAmSi5q-HSY_cJkYmsr45DD_vJ_aOGx6TFq2lRdLHVPBdVFas2t-mAoP2-4oNT5Ov7m3LvU7SFKm-_XFClXv0HTTribkb9dBBjF1OZ6QICo9vw21Gm-fvUGohkJaGgbLRqSg16IPrGD_v_WShm_fjHi26nxtVTrhaXWL1mggJAhrhMZBrLZk9CeVKxs0BLOjMvvycZGR7KDNug6QhJgpi2TkreiasBjJN6C1rwJqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسابقات جذاب دو امدادی المپیک ۲۰۱۲ با قهرمانی کشور جامائیکا و رهبری اوسین‌بولت افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102983" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=LTPq7Y49bz8YrHYW9HDXatcE8jbVD27YQzs96cy0FUrtCzmRuW2T-3RvhYxS2Ys0V4e-jYuPEdfUomsfjQv379pVTrtPPQmBdoDl6SWDgT6jAgiigyb2cqby3Cs7-VqQbHmh98a1Q2k2YP344AAOEr9ZlEV-p6h3kAg7R39quFeWx7VaVoKV7phPvtD651FQ6cU3YgnGC9Ha9TVKkzjwe-GxJgImuCwCtkxXbqh8iVYK2_OhUMafBke98wD4jkdwJ3xaM_u8qu1J3eFfCha4DGCaCI53E7UNAVbf0y-StkLUcj3nHDdhqbezGDsqD5o_e8T-7CLI_uOuut5LoIgPbrBtGev4_Yo7_ieeShvjx2fPDb9FLTfJo0XAPIxPhqxLpRtni-fL-u5X3fHv_se7XHOpvRKhjLMRP78hjYlo5VWh19EeGdrBwxRg_r0RuBhRYRgcB2FjYt1VpInSa9rWqoj9SfdXhgIWYJTpoNEq7Zm5jj2KvPDlNKhbKaa383FNzgTn0T01eE7l8FknawBZPnu0owiXfO8pdSpKEiyYorytZr7yo39ZzZwjwg51a1CdSp3JSgx6LUpxnA8x7bRKrP5OBy8pOT04N9_x2KViAMXwPgfrbeE0f4xdCKaMhHT3Sca_AZywa8BkrrPWeCKbjl3VdF-PChZaBvNuG161Pjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=LTPq7Y49bz8YrHYW9HDXatcE8jbVD27YQzs96cy0FUrtCzmRuW2T-3RvhYxS2Ys0V4e-jYuPEdfUomsfjQv379pVTrtPPQmBdoDl6SWDgT6jAgiigyb2cqby3Cs7-VqQbHmh98a1Q2k2YP344AAOEr9ZlEV-p6h3kAg7R39quFeWx7VaVoKV7phPvtD651FQ6cU3YgnGC9Ha9TVKkzjwe-GxJgImuCwCtkxXbqh8iVYK2_OhUMafBke98wD4jkdwJ3xaM_u8qu1J3eFfCha4DGCaCI53E7UNAVbf0y-StkLUcj3nHDdhqbezGDsqD5o_e8T-7CLI_uOuut5LoIgPbrBtGev4_Yo7_ieeShvjx2fPDb9FLTfJo0XAPIxPhqxLpRtni-fL-u5X3fHv_se7XHOpvRKhjLMRP78hjYlo5VWh19EeGdrBwxRg_r0RuBhRYRgcB2FjYt1VpInSa9rWqoj9SfdXhgIWYJTpoNEq7Zm5jj2KvPDlNKhbKaa383FNzgTn0T01eE7l8FknawBZPnu0owiXfO8pdSpKEiyYorytZr7yo39ZzZwjwg51a1CdSp3JSgx6LUpxnA8x7bRKrP5OBy8pOT04N9_x2KViAMXwPgfrbeE0f4xdCKaMhHT3Sca_AZywa8BkrrPWeCKbjl3VdF-PChZaBvNuG161Pjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
روایت سبزی‌فروش اوکراینی از حمله پهپاد روسی که جون سالم به در برده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102982" target="_blank">📅 15:10 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
