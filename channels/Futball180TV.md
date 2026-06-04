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
<img src="https://cdn5.telesco.pe/file/DXS4la6HD-4NjPxFR3uS_9x919RdS_T4AckDu0wBxXbpWodE89S1KxVBemTkNMEkXcea2iYxycwHiMQte_BKdUCzbae-qZnWvpF8aU_i2GMubgOudoorEX525is7kGc86tPJJC8jfO2VgY-hDA5Le2x5GYP8itWgQ24WNcjMFaQ_7fEe2U-sDNQZGEzP3po1m0cZQVDU1vRXFnv4fCdkvYhKyC_-VZ08eOZXbV7KLBBcYscDSctEgo-0UNpMkEN5slVt-v4YIM9Up7L6YtXkbCIWHaOU1xZkXIiItTZTXkKN6ZvIPp9bqY_hd9YEfu42-kRr7n3ttar3w5Yr1gqWNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 183K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 02:21:22</div>
<hr>

<div class="tg-post" id="msg-90984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/Futball180TV/90984" target="_blank">📅 02:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90983">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فووووووری
؛ رومانو: پس از جذب کوناته، رئال‌مادرید شدیدا بدنبال جذب یک مدافع دیگه رفته و حاضره رقمی نجومی پرداخت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/90983" target="_blank">📅 02:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90982">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/90982" target="_blank">📅 02:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90981">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXRAtXE26aUlymYS2nD570mDgZrRSxhzD9_-NaddAHMWPAkN5GQV_rFIfhyHqISCd48PRTQ0hlHchN7o_41BGVHAAkBz0NNFsP8pZIaRhafExqGb9D7pfqd9oS1b6sUkQWe9fpY8-H3UIkuhCXkINLEmcHS37pfTLqDM5c87oQiegrqRteOIB3MbNc0nuwj2MJ36-RTLhqvx1bvrQ65IOYKNyOPLgzNTfTf-7eN-Bnxwt-vxLnvdP6Lqh9mf5es0ILfSb61u5XA4Zda_Lx9mU7c34JcNM9T7yoIEJH1vNPpVi3DuCm-_3vsySJqZa9jvKCRVLbFaM5lYSXxfOi-J_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/90981" target="_blank">📅 02:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90980">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
فوری: خوزه فلیکس دیاز گفته گزینه‌های مدنظر پرز، اولیسه و نوس و ویتینیا ان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/90980" target="_blank">📅 02:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
وعده های انریکه ریکلمه قسمت n ام  : اگه رئیس بشم دلبوسکه یه پست مهم تو رئال‌مادرید خواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90979" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/90978" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90977">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تمام رئالی ها منتظرن رومانو زودتر از سه‌شنبه بازیکن مدنظر پرز رو معرفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/90977" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90976">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E_uHZ9-lv2tx9CzoMJVECYsj1PgSd4fofzZgAMoyx8niUvULtYQwqA8B8cOjIweP9lTX8f95xETq5hRrirRDmTfvO4-Qkg9I7lVbFGuPWNeibgq3xnpGXnWvcvmTYEUuVElLhu8RTOBNf7D66wfvtMkc6K3rwzMgSOmrir1QCQbf-hgj5r9LubwJ4SCxHl_mShHEsEjPDgDXqF1o2D7FT3nh3HHfUf1LRaTYjX-JXjIINWKk65z7gQLhnJTY6bbHffcI-y8GocIWT24LAN7Zt864JGGFYEWqrRQIVzEhonl0VZfzwhKpKFKqmhCfakG5X00UzHu44_etfTV3l-bLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/90976" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90975">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
⚪️
کوپه : این 150 میلیون یورویی که پرز اعلام کرده پیشنهاد اولیه اس و در صورت رد شدن قیمت بالاتری اعلام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/90975" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90974">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjTaQgy_BFzfRt_5kGw01-Aa7HL7VE6pFPez_iaXDGKdSsS9I0Nf-P2lgyz-XotQlrvgp7ibUIRUqbC5ZX8o18pQcMtuldt_9PBApKEqP-1Efv7IBpcsW643wmd5iTFuNHvTRFfHkjDlFeuThOt3dTm2zgZDaRZCfG0cz7q0qdRHK1UZGc34fNKvqmWZ6QKsA5oSEjNIpSpnZV_NikiY4yl15oWyi22TI3iDlfH6B7UaWoBAmhPwbxZPJRsohBlVZ9NNEJG7jpSlBS1VNG-SHkd7OO8PfjFtFVWCZhLBFpp5jrBKA5S6lpiIkTcnfC80X8sDba_zx16Wok_VPg6bFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/Futball180TV/90974" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90973">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5cGEVfmInDKckqmQAyOusBxkNpY0qvlmPZeG9eJm6YZeU51fcgCT6WkCWEQ5A-IEJ6arffdRSKaGn1_Q7hrJPb3KZzUqM6UBttOKCXNoVrQDKZWZSGZAdI48VZWCukf1agwPOoe-jK0AOYA3U7zFlIVDSbZXZ4PaAHXMIe4T88NFeSc0NOXNLsX6S27lLCm8XsIjx8GwTigGMHcD05_II6_NfFhCWa9sW9UuvL6oLEUGfKsgp3sO5uYtAHP3zJ9El79hxaEcs-mJBpYtxLzrnJyYb98tyFLHkgAK4RKIVpVds8wh9DJ7MA1uQLUS9Ti9tGgNePQq-zegnwqWoN38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت جدید اتاق جنگ اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/90973" target="_blank">📅 01:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90972">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WrQDzxMLhCBDcW011VDAHZCtR2LpXNZAi6Ywe3Xp960qUbTnmY1DP21869ZUaP0hbWzpvUJIi0ZsP_6DkR3DGBYXKB4IsfuLOfjbIH9hsFrngyzHuvIdAOS-4Pmf8zjDAPuc6GVlLmUEw6eZAT3y_FCXslCU1zIeubAAzv4AhDU5RsKN4HRudJDAAx7Hnisw4K2glNBB8J3PqbEKUpDy8pnIy1TyxOduB6tswxeqTxlSjA9NvmHMdwYz90DWBIGPXFe8jz2rHVl5jeFTnYexbMPnDN0KunonioNI1JlIPsH2wHVSn4vJpDGLy5EkF9PPp2z7YkLIoc93gX-WAKmrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/90972" target="_blank">📅 01:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90971">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu6vQgti-kN1nQXnH6o3MtydlokW3y6YOB8Zq7WdILs0ug-2mz3FUUFkvgKzqCu0UC6MHCtqV7jvtm_tcoWX46AgLnY8IZ3M1eBz9icMZ8tc4usPZhtIkBhIi6RTcEuJmo8ip4np2NAhYYTzX4nm60omUaSUD3_VfUpzNv5AhOrrsmcO0Zj406rf1rsd6YC6hRucVvvyAftOz4aiW-3pdrHRKaT7KeEg4WpREXgHzAp5TTLwMAakjMNSAchKzkiEKKfvCaZduLu7xZnW73_Ny1ynNmmaiStwcLMZpEuGJV1XVjLvKIrXLXsMBx8UWK6rYUvFnQQXmNs01rJzFAcWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
پرز نسل جدید کهکشانی‌هارو استارت زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/90971" target="_blank">📅 01:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90970">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ولی خودمونیم ها   پزشکیان هم موقع انتخابات ازین حرفا زیاد زده بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/90970" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90969">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/90969" target="_blank">📅 01:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90968">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3myYI4seBswK9XW-KcHWCVxNUBIMpaOey5g9JAU8fAnCQCCfvosEWQ_D4h_t1BHoeRLHpD4WQeHj-5js-vUuS7tWLjv6ccAuEjwCBawi9I0EY4OfgJtRtCMH_NIaKXArup5kj5LSDg0-BAa4nFw83xKmkjqa0WkwnqArPyH_0OLjLgQlAy7LJAvkqS0SIkTav2H6tRRq10Cb34DtAG1Q8Q6-wkrZSYCFK8SEU-3zBFkjaX2vWmtznvg6vGsMDE83utZ8csrYlBn-lPrQ-zBCzrp3pfIqDgv87ZSQfao4fHFKBHcVNHIGjcvsxguYNqXHdlTHLR-jhORILwfjxgOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/Futball180TV/90968" target="_blank">📅 01:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90967">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لاشی دنبال پدری نباشه یوقت
😐
😐
😐</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/Futball180TV/90967" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90966">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/90966" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90965">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری
پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/90965" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90964">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IMCLKyAH00VramnZH2lOUMTVKW9RyPR0ZFiZuLVO9d5yeZlahtPzamQ0N_kpIuCrNpw1gf2GYn8a6meIzBmFCjQbq85fL0D8-_yvK7KoKEim1fUaLRP9DPZuCYiEwZkyy8pY46LMk2Zro-S4mvlZlBZqZXgKodok4FIxAw-2uW6Ha2ZuI53tr7RS4g4KBkKZof8zBclvVecQCer-wspjLBdmfY9TOKZsbELSbuVnyM13QZH2CNDWUk-00MtoE3OjUQEVr8w-MNUn43jPvArNJ98zP_tNoaT9-lSCafZqcMkCvRNa0NoHbk06JN5q9nQbJk2zquvc8ufgFkk6FY4mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فووووورییییییی
بمب پرز لو رفت !!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/90964" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90963">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ6FCNa6gO46kg3LTuHxzM16uPY_Kj5jZqMWHjHX1sczOx7yOPNZTXxJTjhRFXxGm--luOS5On6cn6iIUA9H3y3nzLXIsesiNmofSBCgv7_Pi56FKvBzXXcIep4-LiQnxfjDvTzBBROo4c7B0L840pRU316HRAK99gOkb84UL0es1XXRG5R0t7SJsbM-A6aT-hDdL0871wQQVNTUlneJEmS3fd4RfNsqiTO2hTJV1-rRZR2sgEQHFk5iyWwYlwt2-jUni2dhSX18fzcY42az2ngaN7c671e9sX3pC87QrZ_Y1TRmeOwly5FR_jI0ZuKxN6Nh18_OwVjtUQJZMJAPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/90963" target="_blank">📅 00:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90962">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/Futball180TV/90962" target="_blank">📅 00:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90961">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/90961" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90960">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/90960" target="_blank">📅 00:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90959">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/90959" target="_blank">📅 00:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90958">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/90958" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90957">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇪🇸
فلورنتینو پرز: اسم آوردن از هالند یه حقه انتخاباتی هست. مورینیو حتی اگه ستاره‌هارو روی نیمکت بذاره کاملا تحت حمایته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/90957" target="_blank">📅 00:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90956">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
‼️
پرز: این فصل هیچ درگیری بین بازیکنان شکل نگرفته و هرکی هرچی گفته زر زده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/90956" target="_blank">📅 00:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90955">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruSQWIctaR6J10Q-kZ-VGUN-BbTS894U8gnnX2h3HYyOj80sk8FUOn8gQhEZWtZ9jC2HpELGF3Vf4gtUXwyXvlUek37iMpPQ_-mPs4-irjEmDwOJNWelvlJ79WtKu1t3Dodac5_EO4ulRuosdZ4_7ss1EZcqG7RfyFUoxDT2rZGLb9oI8kAAkMqoZeE_NefMBo1f2mkkGEz5pKccssKNWkPq701J4qC42SD_OTn-t7osXs1P1Nrkzr-GibBlwA1sxTTuk1BjbNm-3G6amBRjAFGbin1LKMMNKqA7fyT-c3XJkjID-eVpUJagcjKY8CIsioeLoTnYC5XZodB1RErbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه به ساحل‌عاج 2-1 باخت.
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/90955" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90954">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">▶️
🇪🇸
🇮🇶
خلاصه بازی امشب اسپانیا و‌ عراق با گزارش فارسی خدمت شما عزیزان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/Futball180TV/90954" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90953">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
پرز: همه ستارگان مطرح دنیا آرزوی پوشیدن پیراهن رئال‌مادرید رو دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/90953" target="_blank">📅 00:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90952">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff5287c9d.mp4?token=lVGcumfOEaJEB1CKRek5pwgYcbSoRTN8iouLqcmuLl4I1vf10gv1qsFRB5k7Kczlng1XT4zhsbxNPMvZZjBEKerxwGy4vJ8xSkSz3pFWC-t33obmXFNokRyQgn96xOPHNacY5WUMmVVmdbO9QpU-EPO52q9vw1R9SfohUN78VZ19opn6pf0Qh1GHyi9qCOuBpvs0KyuH-VVmc7xoLYt5wq7Ts-Ba_6IGkbYVcxDRDGcXCytMtE4QK8F_KJqEXtLOIhSIlmZwhS8OMbaJiOOWTs6UuToDrHc4cah79v6fVEzKX9nytTySXuPA-2nhdBuLP48p0zcJh5WVlKHLGMyL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff5287c9d.mp4?token=lVGcumfOEaJEB1CKRek5pwgYcbSoRTN8iouLqcmuLl4I1vf10gv1qsFRB5k7Kczlng1XT4zhsbxNPMvZZjBEKerxwGy4vJ8xSkSz3pFWC-t33obmXFNokRyQgn96xOPHNacY5WUMmVVmdbO9QpU-EPO52q9vw1R9SfohUN78VZ19opn6pf0Qh1GHyi9qCOuBpvs0KyuH-VVmc7xoLYt5wq7Ts-Ba_6IGkbYVcxDRDGcXCytMtE4QK8F_KJqEXtLOIhSIlmZwhS8OMbaJiOOWTs6UuToDrHc4cah79v6fVEzKX9nytTySXuPA-2nhdBuLP48p0zcJh5WVlKHLGMyL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇮
🇫🇷
گل‌دوم ساحل‌عاج به فرانسه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/90952" target="_blank">📅 00:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90951">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پرز: ژوزه مورینیو از اومدن به رئال داره ارضا میشه و بزودی میبینیمش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/90951" target="_blank">📅 00:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90950">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjwY-JXw9lQJgoINOdLsQ2sguJSUby9wFsWcEic1Ub57ASroDh8s18IXlIyw_nq8JUOk-U20a5W6FZtNucrW4Www1YKsx1iNmhYrhoZC2ndVzSuFGxi0htKcXJZ2z2tbmFQ3YblLPBMMKtTnW3h-7juSRG1jEh0ZfNICZGyWIVdU2TLXYk4JUgTWd78bAl337rmPDTkYmHgNDvsuWbdhAC-QMLjQoWmlo1jYU87vJ5Fj3Sdjkk2tzshphA0yH8q1QZaa_FhNHMsEiNyitI-ZkvS0iIh6QKRzTRdPztVplb9qfPX7tf_U7vnEfC2BH_KGV2bLonD2TFgAkhxlQLB_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پرز: ژوزه مورینیو از اومدن به رئال داره ارضا میشه و بزودی میبینیمش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/90950" target="_blank">📅 00:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90949">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
فلورنتینو پرز: مردم می‌گویند من ۸۰ ساله هستم و باید به جای رفتن به انتخابات استراحت کنم؟ پدرم رئال مادرید را در وجودم کاشت وقتی که پسر کوچکی بودم، و احساس می‌کنم باید به این باشگاه کمک کنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/90949" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90948">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut2wvRE9CKdEJkbb44Twvvf1yfznb8NXOSUb3tJhRhT8yn4GSFgV1M24_CCSEpmxqSnR2fw0PTvQU4RzNf0NBRV_hkewuGu2e8XSdLJtRfjtC_908RiYwC1xyGCNrEbszlPoxEAPH-MpSiXjwfqFj3xsutkKW2YPpbZxgjZ1nEtpvJwt5muSPfcK7qCMoa8wUhYr7BAQOZy404X8-KX2X2KXW_nCtfJeHGXPy_KdD-E2ROEVY6CQLM9xR61-1n7g6Qp1sJ0YGICgi3ZJE0wsyDHAJpRvl8JuKxH2hyuq5KW5cyvv7f5bw-ZhsH8ZqAj3qZxf2wkNCJk6h4zqM76KwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فلورنتینو پرز: مردم می‌گویند من ۸۰ ساله هستم و باید به جای رفتن به انتخابات استراحت کنم؟ پدرم رئال مادرید را در وجودم کاشت وقتی که پسر کوچکی بودم، و احساس می‌کنم باید به این باشگاه کمک کنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/90948" target="_blank">📅 00:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90947">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2wckD4d0VPZ4l0OqQ0bQLLxvDj8Rqf12Hc3GwjvKX8pBZX7b9kZMifbXEiW7JZBpT80j1oiK_Ziq35qE4pA5jDL9RMLR9UZh1x6hNtBJopq33KfgrnJWpYvNKwGpdX3ER9OIaRMbw8KOn9j77YRRK-QjuocWMgYzpgJlGKmXQnNDBhzLDpRh3Z7RpbLUjN2WCEpxs1kEEKMouZuTN4gB99iaHLj2LUL3HrG6n1zj9PuS2j5I0fNKTuIRPa2YhHETCZgzsAWrBfi7bzF0U06hfr4Mg1HA-E6WXNhj3vDFlMvpzzR2qFHNWeHztKLZXSCHHkK-znM_u74FykMb5PEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پرز اومده مصاحبه انتخاباتی؛ صحبت‌های مهمش پوشش میدیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/90947" target="_blank">📅 00:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90946">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW7llOM9LKK9ZLF4ULqF6mnA4uicvrYzy6agd2xr7lnWEGszuRqhvBfK7d7gisMcUEydTtXaxkMeKqfm4CNq1RtHrVhKKj_pW9YF41DdNtnup_51-MDcEoZ21A8VaM2JPq0_BWSs3RULgOmuMBk2F_YWD-X-RfWyP7bo2ab1hW7hmIKNyTWQWM52phMHS8_tUh4SfO3-lekRJ9k3nxGV83cbFlA70l-01lj6wNOIuyiFc5Hr2rig1zBHvy6w0Qp_3gfBsxF7F1VhLy6iz06PTqrAPooR2caMmI5MKXklO3mUM2LMeicbslwNFROQXxdMlnajROL0SAMxL47nCv4dwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇶
🇪🇸
تیم‌ملی عراق در بازی امشب مقابل اسپانیا به تساوی رسید! اسپانیا قرار بود با ایران بازی کنه اما بخاطر تحریم کشورهای مختلف، عراق رو جایگزین کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/90946" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90945">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
ایجنت منیر الحدادی:
ما هیچ نوتیسی به استقلال ندادیم. مونیر به قراردادش پایبنده و هیچ گونه مشکلی برای ادامه‌ همکاری دو طرفه وجود ندارد‌.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90945" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90944">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
😐
قیصر خواننده قدیمی آمریکایی‌نشین که امروز پس از چند دهه به ایران برگشته، در تجمعات بسیجی‌ها کنسرت گذاشته🫪🫪🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/90944" target="_blank">📅 00:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90943">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c7dad01d.mp4?token=Th9x66AMLnUUtwI7ZonsmuuPc1dV6U4mzQgxKTRwRmP3e8ThL1qMfEAITuo7iKB9Lp57A7xNN3tnVD-7rARkdd5f_LC0IqrYTxbsCia_IFQgaosgfYtVW1Zn-AqIgAGl24pkO5OogegmclEBNwJ9bv0yNYwB1n_6xIR2DS84GY4kMbXJKxZn8YaK0LcwEg0-uVyotK9Sx2ChjJy--tY9fHqAl_sKOo77fAFkLFIbDQcYtDijr_8ZRPSBMT6NAZLWwrbKYVaRkPO09bhxM14uIvMOj9Ka2BT7IF-fd-c5Y6SJ8YaYY-pGcLnCctvCeBcj15Lrbbk2dRfX7nEehtJpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c7dad01d.mp4?token=Th9x66AMLnUUtwI7ZonsmuuPc1dV6U4mzQgxKTRwRmP3e8ThL1qMfEAITuo7iKB9Lp57A7xNN3tnVD-7rARkdd5f_LC0IqrYTxbsCia_IFQgaosgfYtVW1Zn-AqIgAGl24pkO5OogegmclEBNwJ9bv0yNYwB1n_6xIR2DS84GY4kMbXJKxZn8YaK0LcwEg0-uVyotK9Sx2ChjJy--tY9fHqAl_sKOo77fAFkLFIbDQcYtDijr_8ZRPSBMT6NAZLWwrbKYVaRkPO09bhxM14uIvMOj9Ka2BT7IF-fd-c5Y6SJ8YaYY-pGcLnCctvCeBcj15Lrbbk2dRfX7nEehtJpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل‌تساوی ساحل‌عاج به فرانسه توسط دوئه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90943" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90942">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🙂
👀
#فکت
اگه ایران تو گروهش دوم بشه و آمریکا سوم تو یک شونزدهم میخورن بهم🫪🫪
☠
☠
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90942" target="_blank">📅 23:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90941">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de9f07d6e.mp4?token=VWZYz-5jsGKuXonMNNjTz7k2jAU8DXe7D0hHUn_CDTpfRh4tmArEBgBRTvMqDrL15R8562CfhzpRC67JBsV2jR_2e73ACsahy_N3Zm2AOxp_I4BHhli-bDaWLySf6fkVSUqYmQFkrBFvM90KuaPyaW06f5xilbXB4fEJiM4d-ZW_E8I_GpH2nO2CVj1Fg5rtV_qmnajYgJbqKSpQHtITYsE0Ps8FXHm4HkdC_1RwaiqywS0WPPn9MHCA0tO-jTm9BUX84mzSt8sSuZrNxbrZEdbCu_BLuFvfjNl6ZvDlhujAekCM3OMmT4sbd2O_BfurGqmOlrew47Sx7oXvqEgFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de9f07d6e.mp4?token=VWZYz-5jsGKuXonMNNjTz7k2jAU8DXe7D0hHUn_CDTpfRh4tmArEBgBRTvMqDrL15R8562CfhzpRC67JBsV2jR_2e73ACsahy_N3Zm2AOxp_I4BHhli-bDaWLySf6fkVSUqYmQFkrBFvM90KuaPyaW06f5xilbXB4fEJiM4d-ZW_E8I_GpH2nO2CVj1Fg5rtV_qmnajYgJbqKSpQHtITYsE0Ps8FXHm4HkdC_1RwaiqywS0WPPn9MHCA0tO-jTm9BUX84mzSt8sSuZrNxbrZEdbCu_BLuFvfjNl6ZvDlhujAekCM3OMmT4sbd2O_BfurGqmOlrew47Sx7oXvqEgFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
میکاپ جالب آرایشگر خانم خلاق ایرانی با تم جام‌جهانی ۲۰۲۶؛ حتما ببینید جالبههههه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90941" target="_blank">📅 23:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90940">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c687b5ca.mp4?token=X2a_DboLdbvgq8PNqnBwKDlbLGdFbhKF57phT7HnQej9TnDjik_yVXPLRUCGH3Y_In2dLp8y533XCvGMiWEb3JEVITnSxcs4gXCh9NBbM-vVBl5awskWl9XYxO82y0Jkgcl5LO6W4mwrpuuuKH-8gzyZ5XmTDCx5c-wIhcclY3BU6D_kRc6lt8e_HkiRaFpdB1K2TgwJ825NePJyPuoblfdj8cIhBne79K9zvgZSUBODDAiV-7nHIHlOi7j-MkbLL4CdlNyCGIL05DiklCXSSZJqOgjwVPDenEav3C0uifeIrf6HzwfikkA0D5GrrxSkLOHD3UmqpjE5bjmpjCFeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c687b5ca.mp4?token=X2a_DboLdbvgq8PNqnBwKDlbLGdFbhKF57phT7HnQej9TnDjik_yVXPLRUCGH3Y_In2dLp8y533XCvGMiWEb3JEVITnSxcs4gXCh9NBbM-vVBl5awskWl9XYxO82y0Jkgcl5LO6W4mwrpuuuKH-8gzyZ5XmTDCx5c-wIhcclY3BU6D_kRc6lt8e_HkiRaFpdB1K2TgwJ825NePJyPuoblfdj8cIhBne79K9zvgZSUBODDAiV-7nHIHlOi7j-MkbLL4CdlNyCGIL05DiklCXSSZJqOgjwVPDenEav3C0uifeIrf6HzwfikkA0D5GrrxSkLOHD3UmqpjE5bjmpjCFeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پشمامممممم از بازی امشب فرانسه؛ تنه عجیب فرانک کسیه به داور بازی باعث سرنگونی و مصدومیت قاضی این دیدار شد.
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90940" target="_blank">📅 23:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90939">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cff28a7c0.mp4?token=hoa_c1kKEKVWVGP57wgs0jC9Fg0ZMxq0swTAv3pERljQ4q_gmEsJXpqYVfGgFcfPduStPRchxwo5vyewojxCufVAnjwYokPvGfvmmPsu7SKApOImDgSSfXUK0ZZwDlGHxbTVd3Ja6jBYK6lHF6c2Y58i6yWpX8qoBDGrSw476eEeMjbe0Jp8P1-J_pnX5aJ_m4oHCd8WAc2uhksArviqdv705fBdnfjiy_bNKULRSvTpXayH9i7xtslfAtvovSrD58mcpD3JIGeW2fLtsfTnjbUVBNm_Nn5emeIPDpUE3L4eo8w51IugjjCl7aP9uizs6nfmuRgh-4H1-KIesXI4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cff28a7c0.mp4?token=hoa_c1kKEKVWVGP57wgs0jC9Fg0ZMxq0swTAv3pERljQ4q_gmEsJXpqYVfGgFcfPduStPRchxwo5vyewojxCufVAnjwYokPvGfvmmPsu7SKApOImDgSSfXUK0ZZwDlGHxbTVd3Ja6jBYK6lHF6c2Y58i6yWpX8qoBDGrSw476eEeMjbe0Jp8P1-J_pnX5aJ_m4oHCd8WAc2uhksArviqdv705fBdnfjiy_bNKULRSvTpXayH9i7xtslfAtvovSrD58mcpD3JIGeW2fLtsfTnjbUVBNm_Nn5emeIPDpUE3L4eo8w51IugjjCl7aP9uizs6nfmuRgh-4H1-KIesXI4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به ساحل‌عاج توسط چرکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90939" target="_blank">📅 23:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90938">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvC776bFqIVvHU4PvRDeXkOpiLGFsfH1-Y9G2VjOSiQrsBrttstKGZm1ehlPWQaW6i3ry_c9PO73atki8KHMn_p9N6rekA_mWiiuFzpKcmLqJELALON2jRhb0KFKWiLaAtHBxohU8dR0K9Dg1LwJYUa2A_Ta09Jt_2SSDKy5EoRSPYX5XQwKRgPs5Pybu63Ul18T-bwK-_pC4_rr0cZ2ypTdWR60MaydpTED0JhKnoeo_KOY33nEv3xRM6feNGGbzgeIy_5gEgwKyzGTKrFWoycKurPoByTBaSSR-P5lipBqH8mjtY751GWkoacjJrvzkrVEHVrNcNn6WJe6mzhxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#
فوووری
از ESPN: خولیان آلوارز شدیدا از رفتارهای اتلتیکومادرید در ایام اخیر عصبانی شده و برای خروج از این تیم دست به هرکاری میزنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90938" target="_blank">📅 23:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90937">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK6MlHudU8zGg62Hp-Ydo5N46kU_AhLXEaJlCINDr_ckvshyRE1KEJ-YoLsRkFh0e7q0xRV0K6OvU1YD88jvQXm2FiFfdjzqvmtcKwaPJ_pvKuxV_tWupoox-RlGIw6T_SYpPwmm33f-79P2zZNTzwkOPEhokXNyWInMSK61fDHIQ-b0PZ-hOJ-zeOxYJf9bZxWrVmJ8gM6gsCXhErEzzT0RpDB-TxYFPzWu3tOe5RM07NozC0atiIYgalQn57_ubGwTmQlSpjDEOjA40926M6owgmhTKhe0yJzZyZVUd59c2uv1YPpRPVBdCWRcD36TCb1oQTahZD-8Z_5w7VRecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90937" target="_blank">📅 23:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90936">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db661e26bc.mp4?token=f231xdP7XKlOSM1eTlh5VSi2HvEHQghtBDW0yTMriLieP6wagbWgVrNR-QruGD0s5KpMs6MRmAoC8EoNkqiF3qCgEXjmsHqHgNs2Q0NcOWUEs4Bxaa85enmQhg91nAPQaMv-_A0iAW-XrT9yzkpk4Kqnv8J2FVjbfaK7zEqCiMu3q_3wtJ1MXDsW4JxCQS1McRvubkiOMGDy0n35hXFaK0fpV9ND9O3xe-KeeH0N7ZfodTltvhszS7KwjYKsGRBpIILN38kQ22_ez9OUUa3IMrgo-bbXcsFi8vKed1qF-rYMxQ6BIiqR17V5_fZxLaHCv15lhjfp-Ti_-_nLedYAug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db661e26bc.mp4?token=f231xdP7XKlOSM1eTlh5VSi2HvEHQghtBDW0yTMriLieP6wagbWgVrNR-QruGD0s5KpMs6MRmAoC8EoNkqiF3qCgEXjmsHqHgNs2Q0NcOWUEs4Bxaa85enmQhg91nAPQaMv-_A0iAW-XrT9yzkpk4Kqnv8J2FVjbfaK7zEqCiMu3q_3wtJ1MXDsW4JxCQS1McRvubkiOMGDy0n35hXFaK0fpV9ND9O3xe-KeeH0N7ZfodTltvhszS7KwjYKsGRBpIILN38kQ22_ez9OUUa3IMrgo-bbXcsFi8vKed1qF-rYMxQ6BIiqR17V5_fZxLaHCv15lhjfp-Ti_-_nLedYAug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل تیم ملی عراق به اسپانیا
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90936" target="_blank">📅 23:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90935">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
فوری و رسمی |گل‌گهر با رأی انضباطی مقابل چادرملو برنده شد
🔹
کمیته‌ انضباطی فدراسیون فوتبال رای خود را در خصوص شکایت گل‌گهر سیرجان از چادرملو اردکان در خصوص استفاده از مائورو آندرس کابایرو آگوییلرا، مهاجم پاراگوئه‌ای چادرملو، صادر کرد و براساس این رای گل گهر سیرجان در این مسابقه ۳ بر صفر برنده اعلام شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/90935" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90934">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تاجرنیا:
فصل پیش هرچی اتفاق افتاد مقصرش ساپینتو بود نه رامین رضاییان و غیره
من میخواستم ساپینتو رو قبل از بازی با الحسین اخراج کنم میدونستم اگه بمونه حذف میشیم ولی تو جلسه ۳_۲ به نفع ساپینتو شد و موندگار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/90934" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90933">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqgMxz9sYUmxV5t2ZvnKLic_zHIKsm1M1nKVRVhBIJmS_hezcu1qBlDtHHImLiJn2X1Sj5nW7P5qGz1GuwSIYQyGVPRLQ5ITwjs4TNS_S9XJu2QzoR60Hbe3CUWsu16SLdKL1g3ahrWB6lAFvj4Cta4JJV9mbUd3FHvNRC8FEcCT14XjZietmxS-xHguvyhFS9VEbbTd2dwEn0LqY4THSafOrzuSzlm83rZBuiotIsyhEBSH2NO4A0qoG_QAv1btKXgrPq2PO9CLl2eSQKO6kcsxXI-vQjiVKDe8Ndh4SgIzbsP1PZeeyJ5UlGn3_VVzjayTvRZwWm9hLaoWF8zv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییی و رسمییی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آندونی ایرائولا سرمربی فصل گذشته بورنموث به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90933" target="_blank">📅 22:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90932">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6uX65m47YqbhMHLwSBGV1BsqyHqTYO4tFdbNXVpQex-tA5CEAg_eo_imKWL3ysjm7Y7-mQIXAFBT8L8ZcJ1uVpcX7vkQE5Se28Sv-HkLXJ7kIVsoxrQ_vDilCKpo_cuD19YafwXrcDZB-NIeQb9HR0WajSquuogNH5O9XzH30_jJN_VCd376mp56Mh-Z60SHihNNMwG3e-px913XTLDiAy0APkY-1GS_M0A1eoefumeEo0Tc-WZbFWtAladYk1VmqIQgaBvR7i1magWJ-RIH-do6KWFXhJ20aItUUa9svmcydAKLWhlTfea6OWpMi7NdY5RcqDJF9rSjqpo4IIOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با پیروزی ۲ بر صفر مقابل مالی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90932" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90931">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iht7En_TdpEXTCw5Cdq73AYHehDtHc3JpEOGLsXlSqOs__mpbrQyKyxsrYszYT17dpq5TZS08af7LPBAfX1YIEr27p3eRIu-szBy6kGoPQQh9br3-gRQ9S682LWex2NqUm7VwmtmXaTszap19sxztJ6AYKz4rEIOut4Bl0p76q8Of9RJYY24w5W3Hj9glYyGz4tlXXaL07RXMf6aBiQlV64lNNnjo3dhG8eXRx3U5j3Ke1zl5xHPUsyBOWZN9RMltSKcnKwndc1WxEjGY0jxgHDylsH2H8Ne7m3Ee2QPH9OOwInk3vtdfguuJEgxAk_kVobobLSukxIFTDmOGijMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب پرستاره فرانسه در بازی امشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/90931" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90930">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2312570c50.mp4?token=FCMdNC9UcCgjpv-NKj8sprn3djm_8548o8yHUzN8eI9xa77719PbiRy5t10QJa46uNPMxreNOM-JQ9L6jwipCNkOyDOFe1bxjQmWfUdvifzxBgC-ojzE36OsstIvPupKiw4yxWuLj_ABcAVDmMLM7BRWRDzT7QtCErndYVyciiL--eAqK_CWqw9zfl66__miTNe-ZrAfnrn9MqVp8NwTdMKALRXWoxmhE2515NnnAZi_YkbFGfPrSr2vAKvzTncApkx15USFrTidz7RD9tKEiDIcUdamwSmfngU4lxe7ubDeefdfpMN9-vfUtCpoyLW4kMa1rq98R6LJJfAm0cJGAnTyX7UQKgClcyXFZfzgNHkyDu8ZuTGvkY-jqJY1H7J64UDyF6-vwh7y0ExHEsP-6EvTxZrU9rt55H5H5jbhP6dpdbvZBR8H7I_sf3R2zflDtoZdT-Vw1EXuvD7mX3LzpyOkBToRAIChMhVrIe7dJHGxEPyk_nyQjbuOocMsrTiu0p8mboFRpltsjoLy1-A71AbjvTvv2WAY6VFl75lrSIdaLitQ4eZdyOFY34K1Q1WrvkaO8Kt91lHFvyFWovYSphWFUfAFEC2-j0u2bR5VmP1U67zob1DLrQMRdph-dxrUALOALjf-fseUe7OA0Lpg6H8sxHxB5W6uG6EGMndLddU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2312570c50.mp4?token=FCMdNC9UcCgjpv-NKj8sprn3djm_8548o8yHUzN8eI9xa77719PbiRy5t10QJa46uNPMxreNOM-JQ9L6jwipCNkOyDOFe1bxjQmWfUdvifzxBgC-ojzE36OsstIvPupKiw4yxWuLj_ABcAVDmMLM7BRWRDzT7QtCErndYVyciiL--eAqK_CWqw9zfl66__miTNe-ZrAfnrn9MqVp8NwTdMKALRXWoxmhE2515NnnAZi_YkbFGfPrSr2vAKvzTncApkx15USFrTidz7RD9tKEiDIcUdamwSmfngU4lxe7ubDeefdfpMN9-vfUtCpoyLW4kMa1rq98R6LJJfAm0cJGAnTyX7UQKgClcyXFZfzgNHkyDu8ZuTGvkY-jqJY1H7J64UDyF6-vwh7y0ExHEsP-6EvTxZrU9rt55H5H5jbhP6dpdbvZBR8H7I_sf3R2zflDtoZdT-Vw1EXuvD7mX3LzpyOkBToRAIChMhVrIe7dJHGxEPyk_nyQjbuOocMsrTiu0p8mboFRpltsjoLy1-A71AbjvTvv2WAY6VFl75lrSIdaLitQ4eZdyOFY34K1Q1WrvkaO8Kt91lHFvyFWovYSphWFUfAFEC2-j0u2bR5VmP1U67zob1DLrQMRdph-dxrUALOALjf-fseUe7OA0Lpg6H8sxHxB5W6uG6EGMndLddU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی دهات رفتنشونم با ما فرق داره ناموسا
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/90930" target="_blank">📅 21:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90929">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1wLPLrwgepWV1UaifFSCxu9jYzS4FgtMOTFbIKT2lOQ4TBmyGDDq7aE_PIpz6vfFEZAzmJ0PSUUAenFwMDMVNBe7BiYRWKQw9zValLrNOu0iBcuHn5cfQ_55fqYAYQXcv2xQ7j9VXp1n4S3PPR0saJNAhAvanttFtZaN1dLBgWpA2glk-vBEh2gOgC3Y-rifcHm9O5wl6h3_o4ZAJgcM_xrc5YStZEKFn5z0xcqMezZIJNHZfkTIQGE35fRDE6nq_d0rKROcEqGYAScfTjfaqcWkYLavDQmWZy3gqqXp0KKEMupDPUVZr4YzoWl6uK8XpyQtBvN3M2VjOQdREkb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/90929" target="_blank">📅 21:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90928">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=oVxbhll3HKFGmMtSMhY0_jXWQDZAwg0HVw3qojYpr0NDiMAYH6Jf3cXRiIbIPfAo-N3qc6m3EeyRbva0WV7wmilOvqgjv6ekmVe2I46QSvahHZ4aZhpw3snFKQUUtqvSki_jvlQW2NAReHXgs0hXdqW1PoJ3aPFDkMWRGaI-GMGBprjOwxZWiUB4n3ln8L4g_hrfIB9ndki7681cNve1NvL1jFEyweuyFOWrXuCMA48xzfP0sAAoiiOvPuuWy7n_FEzGOrhoXAZMayQ8h1S-MGc1sZS0geSxJH0W_11J-4i4nWg9_FsvkmwvxZW0k-yy9sUB3pi5-2U2ApMa6S80Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=oVxbhll3HKFGmMtSMhY0_jXWQDZAwg0HVw3qojYpr0NDiMAYH6Jf3cXRiIbIPfAo-N3qc6m3EeyRbva0WV7wmilOvqgjv6ekmVe2I46QSvahHZ4aZhpw3snFKQUUtqvSki_jvlQW2NAReHXgs0hXdqW1PoJ3aPFDkMWRGaI-GMGBprjOwxZWiUB4n3ln8L4g_hrfIB9ndki7681cNve1NvL1jFEyweuyFOWrXuCMA48xzfP0sAAoiiOvPuuWy7n_FEzGOrhoXAZMayQ8h1S-MGc1sZS0geSxJH0W_11J-4i4nWg9_FsvkmwvxZW0k-yy9sUB3pi5-2U2ApMa6S80Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فووووووری
؛ علیرضا نورمحمدی دستیار مهدی تارتار اعلام کرد که سرمربی فعلی گل‌گهر به احتمال فراوان فصل‌آینده جانشین اوسمار در پرسپولیس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/90928" target="_blank">📅 21:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90927">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=RfOULAz18U0uLEvl-etXroLl-KnAiwagHwAMRJbVQLTiorS4pInGe-_VRhIHk9nnHARdp77D57weE95izoFO1fjeHL2Psi4vZoK6eiajBUXci71ppMm6I-FTJGXqteCP0ScG2TadcXHPpOw6pVirTEhgCSQrfVggLP87Gl0CfTd0ajz2RPLYLu_Vb2MopJcpNKsYmJBe-fhyQ04jf_FRnDxc8Fznyx3_BZWAn5LGUTqEJQfn29Eqz6StAwzVTmdBDklaW3_RPru8GPJlh_apFf0559r9ORbgHD0RZSjqPKK94VQHzs-4eGN34ErwwnVndvCYlSwg9vmJ3a_LhoQqVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=RfOULAz18U0uLEvl-etXroLl-KnAiwagHwAMRJbVQLTiorS4pInGe-_VRhIHk9nnHARdp77D57weE95izoFO1fjeHL2Psi4vZoK6eiajBUXci71ppMm6I-FTJGXqteCP0ScG2TadcXHPpOw6pVirTEhgCSQrfVggLP87Gl0CfTd0ajz2RPLYLu_Vb2MopJcpNKsYmJBe-fhyQ04jf_FRnDxc8Fznyx3_BZWAn5LGUTqEJQfn29Eqz6StAwzVTmdBDklaW3_RPru8GPJlh_apFf0559r9ORbgHD0RZSjqPKK94VQHzs-4eGN34ErwwnVndvCYlSwg9vmJ3a_LhoQqVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال چالش رفته بعد پشماش ریخته که اسم خودشو نمیتونه درست بگه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/90927" target="_blank">📅 21:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90926">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4R3HeLINXonNknCaNpH0HAlUIEXYp6n6vUVzqZO05Wln24xbXxutRxqCHNcyRnfhHLPJ1GtaKgpVZRqgcfx7iLOoaFdDQfCMrt8bc8Zk5XyYQ2kWndggqgl12h5FdP0LOPnT8TCajSGIFuuogVaU-ne8mGwxP43SnbiEE9Vs6vvD_L9WHYBsOpCIXPndtNKw7dOrLVemGx-6ZyK2IwDHXRK5nk2Am8TX_JvzUK-yhcLTgfEees_DsLe-u4yabmo5JMVioaNFANtIHhfB_AFklgl0MNOBNayVVXU8nITv3nQBJ_fVt66dXlOHv398oqZGyNyXtmKiQMtRBbLpHMWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب اسپانیا در بازی امشب مقابل عراق
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/90926" target="_blank">📅 20:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90925">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVOY1Tt3TJdEfdYDuTpeIA3kaektSuc0lO93hDb4E882WojkuKEJFjUkfYIbpYJJH08yCAbzBEBctIKEVLao_QkFsDdGol5N2LU8q16tm6J8PrnNkiUrggt8vWOEHP-O7iumOVLqKg8JeeFmW6hpFHJDqixoIlbQvpwEsSXuRc49u9Y-qW_fBxdeXvWcwd27wEoKBRAA3PNEpFpCnuiBQNNetsD3nn8HkOA8v0YBf-1j_G9LNfZmtOJNsO2mWaxsFRmwZcqsrMNhpcgmKv0umU0nfQt71gBWU2IKJ5Ty4Lurc1wdGjo5Fxol9-fmHMqEG_hY-Z0Qrfp-3L7hBfVumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرخه زندگی اوچوا؛ قشنگ هر جام جهانی میاد میترکونه و میره تا جام جهانی بعدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/90925" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90924">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba0545774.mp4?token=J2YGyJ2cPsMqxBv5t5xiBIViBlDR2yMIpL1ttSy_UbepIs1l6JhFaPgKelofTfmL8jTF8yxiOiPUO2zyY4P3ALFmnd8K6g2dK932gzykQzBN872JNUTuCB-SvPCZ6g-PzcXTd173-Gki2KP_xsVhCIfaMZ06AoHn3yiXN7u7mNSZT7CsxZv8UyvTpEa5L1g7YIF_6zXcjdH9-xDs9eWQk9BErvZ37nPpiR68p6IfDkGA74BmyFEg47h1mHjMJSjI68PXZszXQfImHUyO_ySD9Hnwn-71-zYEU4AsMGcQGXg6-Nmu3EnIWWKPnDAvTCWp9rgiweU-4TDrfOs7C3t8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba0545774.mp4?token=J2YGyJ2cPsMqxBv5t5xiBIViBlDR2yMIpL1ttSy_UbepIs1l6JhFaPgKelofTfmL8jTF8yxiOiPUO2zyY4P3ALFmnd8K6g2dK932gzykQzBN872JNUTuCB-SvPCZ6g-PzcXTd173-Gki2KP_xsVhCIfaMZ06AoHn3yiXN7u7mNSZT7CsxZv8UyvTpEa5L1g7YIF_6zXcjdH9-xDs9eWQk9BErvZ37nPpiR68p6IfDkGA74BmyFEg47h1mHjMJSjI68PXZszXQfImHUyO_ySD9Hnwn-71-zYEU4AsMGcQGXg6-Nmu3EnIWWKPnDAvTCWp9rgiweU-4TDrfOs7C3t8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جام جهانی اینبار با دنیا جهانبخش
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/90924" target="_blank">📅 20:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-T70igYn5vwFNQ2PHfMGIdysXoP_ByQlyDnIJr4RaorWqAxysStKLYhZsUlSKuDccbnPdrgdYwt2vcpH-wFOrpI-wTCyrma8_BmavQcNdWHOR0eBCM791oSt0qFl9QG5td81kYQS-aI5Dfxpa_G7mgfJq04D48Lxz7d514RhgdcM9jVwSW9Vjp8qBP2rPD9u5HhyF8OpDr4IRGAWgP35hVUfIqrulspIVnLVWljiOfUr-DuH8PnQi-PO5J1knb2AwCGLSBVPg_nkPWYGyOcmiMpe1ja8wP09-BaXi6MdXK-MWC4Zx_p6_KWyu4hmIfO6bE7cMRMEl6baCysBhYwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ارزش ترین بازیکن مالی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/90923" target="_blank">📅 20:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90922">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ecwLDiiVVXe4b3BnEKXn2R0zqk17c0XtikQK7BZqqnORor4QV0JPhoe1zMh3FRxKB-iw6nP7Oq1SGQYHDhLavWlw7l2OEZ_WQof70tn121lHzhK4X1IiNaaLYbI5PeyIq40OrmvzeIVcwu93GHacyTjfXngffYjSy7Sf7jorYLVFpi6ZouJOPA_3MkwL3YERf7VCX7B8jkEipA1ypxq03uo8NBdKARxNqa-IPY9z_tggVXO8lZTHEHHon7CikQpw3qpsc1sQ2LlYRXi7Qb13jtHRHb-dTW_rbtYemFvhb335BCemTj_vSh9gsKYZk5sJwKr3nuZUeWvpDxPjarpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔟
بازیکن برتر زیر 21 سال دنیا در 5 لیگ معتبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/90922" target="_blank">📅 20:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90917">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9qIbISXkPJg03gu3aKR9pLEaDDx-1_WGfnopdO23ZooaIOA_WPB3pkW_ZCC_M5-_is_0u0JXvegjS5CytEh-hLP0BMDYD4O1VhFXQ20FJwRi6-K6_c03u16a-qKJnwvO0lfXSUpkXVJJwngP2nnDHZH_OuQySqJq3MiuJcUmWrmrk8bz_Gwd053-fHerH7RckX9DreSM3uMndYR3qD0ox4VY930CksZavULht_cfDDnB77nc2tE0Dew-n4iuhhocd3-rXeAUJMfLNu9ZnC_3qF4gm9yTd62H-52Id0YZPSjPM01x7hOoV0fyWZWftvMDzh19lnNo9EJrvZ43JnTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم فوتبال ایران مقابل مالی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/90917" target="_blank">📅 19:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90916">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=PjwnOlvtnVsR5y4lZmpfaUqu-T-I7CHyBOxPTp8K5m96wnNxf_e8AkepP2MYWobwqU3k5HFHbnuChGkw-L6VoKXuSNjOkHeocU_vixvl75LvhCVUuZdYO3mvJNsMeGFdjWyp3V3CbzMimZgPEYvAf9tOfelaHh-9tT_E6cVP7xqSQbpEM7s3jQVh5BwG4_fg4zBln5eOQU2pytS93clxKFQGrS_Rp3RQ1niM4f046aQ06WzXK4WFBhkOdCvUoDxSMLnc_OZEdpf-3TzHtj3H29uCzl4BBLdFOxEsKfzVT3oyU1uuamNNeaUkrwkldzKuggl1DrLaUSY0h321xdwP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=PjwnOlvtnVsR5y4lZmpfaUqu-T-I7CHyBOxPTp8K5m96wnNxf_e8AkepP2MYWobwqU3k5HFHbnuChGkw-L6VoKXuSNjOkHeocU_vixvl75LvhCVUuZdYO3mvJNsMeGFdjWyp3V3CbzMimZgPEYvAf9tOfelaHh-9tT_E6cVP7xqSQbpEM7s3jQVh5BwG4_fg4zBln5eOQU2pytS93clxKFQGrS_Rp3RQ1niM4f046aQ06WzXK4WFBhkOdCvUoDxSMLnc_OZEdpf-3TzHtj3H29uCzl4BBLdFOxEsKfzVT3oyU1uuamNNeaUkrwkldzKuggl1DrLaUSY0h321xdwP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های فرانسوی میگن دزیره دوئه و این خانومه که از قضا بازیکن تیم ملی بانوان فرانسه هست خیلی بهم میان
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/90916" target="_blank">📅 19:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90915">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🔵
✅
تایید خبر 3روز پیش فوتبال180: تاجرنیا رسما اعلام کرد که با هیچ شخصی برای سرمربیگری استقلال مذاکره نکرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/90915" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90914">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAqmtTJA2_bfZdBEQSAoZAKWdrJs74Q545UPaR6C01U7n1lZydnD7TauIwg7I_EIRsINhfgsCjJlI4cVciYiv4Tjrc90zJI1lOmJD87guEyyUtPA_h6KnJxVGDXK6MVDGoGYsPUPXIf7SyeXCjmep14fd97VRgeYcmW11p0aNROGlqQYTR0XHfl7OEymDYvkhucvzd15e9dmxXP8t8u0pJEz9FR4IkUSyJPbLnkvqbARdj_CfXIslXa7WlXBq6yxyfJgy4L9wfEXyC1pwpyfcncZsFtVfAs--_NzNWJT6B4PUYO6Eu7cbjJusFzkdHLrS-XNY-nUR1mrBZJ4mFYmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180؛ #فوری
🔵
با نظر کمیته فنی استقلال، سرمربی فصل بعدی آبی‌پوشان سهراب بختیاری‌زاده خواهد بود اما برای این مهم، یک پیش‌شرط مهم قرار گذاشته شده است. اعضای فنی استقلال به ریاست تاجرنیا از سهراب بختیاری‌زاده درخواست داشته‌اند که یک الی دو دستیار…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/90914" target="_blank">📅 19:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90913">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb2J46ij50h03bQuQeqkmL-IoqiIKlO7Owp9okIriw96qM6wGDOTUEzi4Pgw8fWNBEXhRhqi28e9dIrxdzqVUfEiDZ7Y40UOuYYt4F7wjqF-KjBe82oWbbq9Z8jveyiDPxfjRQKHQ1XVJcBfrF9RuWJbmIcVm_k1v_KDCwLwQ3MVnqTJIiZgunoO_iYETgtJB14Dbx_m05rGy3zi1HdCnhT7E7jmxPNFHUX7nxNL699g_el9reYHeUasvX3SC9p5XHAmqmEkFnylhlZPW01EhAwg0NFkt0Nys--xjBeppIbLa7lPwyGxUJAKNGwAQNJVG-Aj0hQppUUWrpjNFD2SHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری: بنفیکا رسما تایید کرد که رئال مادرید بند فسخ 15 میلیون یورویی ژوزه مورینیو را فعال کرده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90913" target="_blank">📅 19:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZlcz2jkBIvym6eQsC1XcYb4pntS16nK5HMiRGrSkhbJo0woG3v0vvOfFkPKnLhZ_ndNL3_B82iKV3I6VEkpJIHWAUaU5u2REzw7hbB86H4kxNYEy28sWtNfQX4gME7Nn6uinELzotnRvO9bBGlcZMOCKFHkgLdXUwflqfiiX0STSRS6VszkW-zKnWxgC_IAvz-PwspETUmsyK3V-Ik2BEIz3KPayMbCGvsghRQ4KBqo3PcT3jsMaLe5Lx4GDXMOsg0dewy23gftRnzA4gOjebVCx2rtFGRzcKFcK5aX5sRyXv8TyOAazu2V6hTsxLJ6jpl8qVoz5Zs09i_i3gAvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکلاسیکویی که فصل بعد قراره ببینیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/90912" target="_blank">📅 18:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjBeXBETa0dLzQ6yKPBokqxBx_RaXlQ0apAVzj77n7g6HQoLKSFB-LKn7ecgdiSJP3q8UZANAXOElUk7PjHiNM9Ou8jLw2Y0RtsnOauqbvgzPXNk1Yb8aOWnaSZmk-gyPuhnM0KHP8wU8C1m3VfF8mHybGJs4X-GTM7lYsmt0uKIVWpMV5w1S_pgQQWVXVC5gk5PRlHGQaccdDV7_rbz85MJCC174Nz2r4in_pzR5z70Jb2bjE6hczUdB_F4aUHY0vb6XTtp2I0qKt-6WN8IDR4wbik1S4Gu8XXigi2-IeBLPdcVuGGY8H28XyLku-xQdU3e1HfFQXg02Cadu1pzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
🥶
وزن عکسو تریلی نمیتونه بکشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90911" target="_blank">📅 18:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJRzL2fkmSKP36Gc6O3SMnkxTr8FukusCdjg0GTgUuQLXBPjmJoi7JfcxKimAX9wJewDkxcJIVfAVWy2ZSVOuCCqRf3Ep2qhelqFJsOTPOH2apCceRdmJ1fR_BZ_73UGnvavvN0HqsCna1opDFcD9Ck6PlS-Ew14sgA8yAa2nFhvAvOyaiJsgNUhsE4y4lJt2x7VAOy5JNntavdTy9wznuK-srxtaC81OZy0tHAf_1CdZc43yysmtTnonMMpgSnk85B27v4TTRUNTzRpWJMX4gxR6OAN1ea4gB_NWXkJPs4tWKFN8uohf8ov-iM7R1UfB6gmIWL80mjAdadouIQ1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
خوش چشم کارشناس اسطوره‌ای و حرفه‌ای صداوسیما: به نظرم جنگ تموم شده و دشمن دیگه تخم نميكنه به ما حمله كنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90910" target="_blank">📅 18:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90908">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=MWr5kcgfPp2kMBMx3Sh__dPHNA4dmb8iF6IyQ3Y3vKq1HG0GK9Ul5V_dV9KGiMCBYq86MaXPGdvS4Y0hg62TCh9qXt14ZEMwcoNKeVNXPpyvPI0vra9M7VFxXhzJpgqf17xvubyypbqy3I92l-wALS6vRm9vML1MFTMHuGa26GG2iJQfAZbxC15KT6sKdwPCYxBphsPlmRnL5XwUyrqYdgeyQH1fADrJATURAe0FQOPqjaIn890veiqHZH-8WPGZw0qVjtNB_UZDoSFpbA6KmJfwJKtxHgGeUpbF6aKHzwlYd3K1lZXURQ82NLUFmzgT9787gJt36fV9jQ8aLqqqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=MWr5kcgfPp2kMBMx3Sh__dPHNA4dmb8iF6IyQ3Y3vKq1HG0GK9Ul5V_dV9KGiMCBYq86MaXPGdvS4Y0hg62TCh9qXt14ZEMwcoNKeVNXPpyvPI0vra9M7VFxXhzJpgqf17xvubyypbqy3I92l-wALS6vRm9vML1MFTMHuGa26GG2iJQfAZbxC15KT6sKdwPCYxBphsPlmRnL5XwUyrqYdgeyQH1fADrJATURAe0FQOPqjaIn890veiqHZH-8WPGZw0qVjtNB_UZDoSFpbA6KmJfwJKtxHgGeUpbF6aKHzwlYd3K1lZXURQ82NLUFmzgT9787gJt36fV9jQ8aLqqqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو زیبای حمید سحری از اخرین جام جهانی دو گوت
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90908" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laUEZQW0mFK7rmKL7X68rHk96rL79o0aTD1cJRG_kQB1bHD6QPOI5uw3sNMqULR6cXmKFLEKO_ySJpNINbBsh8dexZDcskgzJ2U0dLzhcu3JmeeHcyZThYTKrmOcVXZmFgHxTjAkZlWZ8NFhaG4vn9C4lMEDpHUczjB1Rs613gRELVGf_RxKs7b5XPKiasyhPL950C7GGGo6SKbHaImQPONI2N4rsqUz8cKRblZT8AzGoQyp9qu-GXus9vPyJWVJl28UwEti3jkhGOcIHMhizi3W9di1aWt9booBYYt4blXZk9eJKN8_qagss6vaZmSdk_zik_0W3xFQeUr-uy-Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرائولا رسما قراردادش رو با لیورپول بست و بزودی توسط رسانه این باشگاه اعلام میشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90907" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90906">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXQ20yjmACcSkZxmEGvAzxwDUAGQfD5s_YgY3MyDW7qqx0w-R9gVChPYPXVtC8Bu4nw_RdjmkicmPwbe-1q1MejFHdaLP2rYiYbvZaLPqnolcIHycH_sx7tTZPkJFiU3ecna0e6DFhRBH0EZBnk0J3Mlp9F_Q4Os1X_ZDZoBT7sJQgbGighry1IIFKQWO5nn0bXxvYA758kRU1mpTR7BMVsq2YvN8X9XHEU2ZE4hWU_Y5JnivYxsuoh5MWt0Z7hGQTjeXdQO8OiRB5X0MqqyOLIWFMBfuiJIg_dR7VGwyBlAte0Q654mqkvBQmdzcwVhtMM_6DV5tAZzUM1gkWLMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/90906" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90905">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQeoov3KZ6R2cHkNwkrseMUmHQZ5rBqwcnr56KKot-N92SnEZhal6to40JOdXSTZUoW1oubWIiqMs5IGzOdf8mQ7WoeU4Md6TBPNqznmAfqZlxiwBuK5d8c0dASYb7RcUgrkwO6LiOsIQQN8K-TPn0ZpBuWMKXa1WpIQ2DVOI5SFp9BqJBPWIu-MgFJbTtpiGYPt_4MY8Uj1XyJFEu8cLFZiCOFLDU773CcmjHselU0Hs7zAOkSefzTUYNBVBm4ZtFp2i0RFhgI-JQmqLOiIkqfkIOmmP5_hQw3rA3YTaDfbEnuGCfJU3t-1NB2WDd5_PFOhwvIacTTOIbGgdsktAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90905" target="_blank">📅 17:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90904">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیکنای فرانسه وقتی تو جام جهانی به سنگال گل میزنن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90904" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90903">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاع های تیم حریف مقابل فرانسه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90903" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90902">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iaxgsg0BY5mlA38nEtMrXzJQIApCJVliwKZInjtKOaUTRLbMelMB4eFRY9md77BDBnPC75DA-8ghvt1IvQ4erflpqeyfIlVq6KzjdsawWgVl7-MMHmCog7s0GzAH4cbDW5oHSrE5cxF4EQ_uOtYp6MpUnQ1bo99ucUTXpykndw5H3bmQr4uKpYnrPjMmh8l8G1ehp4csgSBloFioRsJQe_bN_MaqVbI31r4rPyMQZH08NytUreIRWZ_BkC3jC2rj4Ac3bI6b3rMZZFT_WQ8KVmOuw-bQso4VPzIl6AJMRAIi2HINjQzIlhSnsI3iQ_Jiu4OvVDDjGompoTtc01tvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90902" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90901">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZnxL1njXk8RyJACnn8B-tG6Otcq0UWIa_Kp3zx6Gcr4y-ChJ7IRC05VibRE5Q2xbq9dPIAi90E_kAA4RshQe1xUr6R49CbLMb8axDzaKiQ5IQRBbSKQAEM4qntRBWZOY3ogwCwxpKt3FNGcLjt3pGIOOGzJqmWqL2ca8OG2aiO7WJqqGf1hIFr2x6UNXP0CTWUwM9oQTx6zJQVLvYCkSkZIU_MBNmbGMIQS65-MsN9GBQO6hfuHwrtZqtsIdT6kDlgl_9ojWmC9FezvhutC4vWskhUBRsMPkmKmCnmO0KHrqDig5h7oPukwc1K_j5ObS_GKO73aekAfHlN5r-4FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Out Of Context Football:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90901" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=gi4iPh530Pxmlyc10JenB5Qm6I9_9ESsKXSIgIp3A_4io-xYQzjdL5BrTjKRQ37DS-FPdTLYV2rXbNMTepDnSKRM-T5YIyVw-2qAEDmSU_xu4LCzDAPT1kv72jmmXdmHi28sRg7cxx63AHn27fHqaGi0mnstmPBcJjfZxIR0LZ6NI42TT02RNMDHwFCJKWL8igNpky2DWM1iKXpI79M2tZJRA7FBdk7ufb0EbpOLZOXnCHY8fbKuEw2wLZkw6Qa0wQ-Ort9WRIcuXZm4yn2Cyf3lpOGQwgjOswYKwh1GozDTYRYoJSQCQ2ZSS_fvzIAZFRqWCoVbYuPKDu_5o0B410044lNVMJezSr1K4wIt4VJN2Rt6IQspqrEDNgDCiW0OC1xy0v4pECSJkeg7teFa9r7oqyJeSu6tgYwNoj08DKLghUh7DZ_nqW2gGggmFro4-ulDMYc4Y4tV4RNSh-zKCXMCQOIDcGrPvFsGU3PJxs4nI7rYJongFckX96UrVxz4tMUEWV7xPzkic_R_HNwtLsxPCkek4hqaR3g-KYKYL8AuLMH3MQrL_rSnEr7133oa_LhpF_Cm24RzaoVvyRE-2r9Wx4POqxt8gvCVUYgv6yusLEXtRedlWzT2isj2jwxMLsOQsJXQbkobQa_QLCt4Ye1h_WhaWR8V30lH9Xn4YDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=gi4iPh530Pxmlyc10JenB5Qm6I9_9ESsKXSIgIp3A_4io-xYQzjdL5BrTjKRQ37DS-FPdTLYV2rXbNMTepDnSKRM-T5YIyVw-2qAEDmSU_xu4LCzDAPT1kv72jmmXdmHi28sRg7cxx63AHn27fHqaGi0mnstmPBcJjfZxIR0LZ6NI42TT02RNMDHwFCJKWL8igNpky2DWM1iKXpI79M2tZJRA7FBdk7ufb0EbpOLZOXnCHY8fbKuEw2wLZkw6Qa0wQ-Ort9WRIcuXZm4yn2Cyf3lpOGQwgjOswYKwh1GozDTYRYoJSQCQ2ZSS_fvzIAZFRqWCoVbYuPKDu_5o0B410044lNVMJezSr1K4wIt4VJN2Rt6IQspqrEDNgDCiW0OC1xy0v4pECSJkeg7teFa9r7oqyJeSu6tgYwNoj08DKLghUh7DZ_nqW2gGggmFro4-ulDMYc4Y4tV4RNSh-zKCXMCQOIDcGrPvFsGU3PJxs4nI7rYJongFckX96UrVxz4tMUEWV7xPzkic_R_HNwtLsxPCkek4hqaR3g-KYKYL8AuLMH3MQrL_rSnEr7133oa_LhpF_Cm24RzaoVvyRE-2r9Wx4POqxt8gvCVUYgv6yusLEXtRedlWzT2isj2jwxMLsOQsJXQbkobQa_QLCt4Ye1h_WhaWR8V30lH9Xn4YDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاراگوئه هم وارد چالش معروف شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90900" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvulhqin7OwujodyuJcq9vNd9ZCLUzqTfwylYvSKY7NCGfqUqlsUTHPRPKb1b2H6aRfO30-pFjwy0NoOYbh91P_2EzPaRDaVhMYhTSpcw-Cei1L-xd3xgrQteL7E9wnN62A3wUdaabW_7Jynq3k5w6bePk1iu7Vj7wEZ7X4DESh9yWM-bBIJO6agCh3SJ6anABz7Wituo2xgZDq7khxk6I5m5lNyxEqYTOugKR5VQF6NOXNaY2Q60ysfaD2raj6HqrAX7ldq_Rlbex6OGGOFfrznE_wnNCIKp1-dJzoDr8pTHBBF4gy5qeNM-yXr-VJOzlqpBac9fI_f_OOf_iZ7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
👀
#دانستنی‌های_جام‌جهانی
🇨🇻
فقط یک یادآوری که کیپ ورد برای اولین بار در تاریخ خود به جام جهانی فیفا راه یافته است و چیزی که این را حتی خاص‌تر می‌کند این است که آنها دومین کشور کوچک‌ترین در تاریخ هستند که به این دستاورد شگفت‌انگیز رسیده‌اند!
🤯
👏
🇨🇻
🌍
کیپ ورد کوچک‌ترین کشور از نظر مساحت زمین (۴۰۳۳ کیلومتر مربع) و دومین کوچک‌ترین از نظر جمعیت است، با تنها حدود ۵۲۵٬۰۰۰ نفر، پشت سر ایسلند، که به جام جهانی راه یافته‌اند!
👀
برای مقایسه، هر ایالت در چین، آمریکا، هند و اندونزی جمعیتی بزرگ‌تر از کل کشور آنها دارد… با این حال کوسه‌های آبی در راه بزرگ‌ترین جشن فوتبال هستند!
✔️
💥
و این اتفاق تصادفی نیست! کیپ ورد سال‌هاست که چیزی خاص ساخته است: دو بار به یک‌چهارم نهایی AFCON رسیده‌اند (۲۰۱۳ و ۲۰۲۴) پیروزی‌های معروفی برابر غنا، مصر و کامرون کسب کرده‌اند.  بازیکنان با استعدادی تولید کرده‌اند که در لیگ‌های برتر اروپا می‌درخشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90899" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90898">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
رضا شاهرودی: علی‌دایی به مادرم فوش داد منم باهاش دعوا کردم
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90898" target="_blank">📅 16:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90897">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=Ah0qwRruhfidLnUh7kVM4u0UdzwT12JbKCBg1YGTizdGKGBweAf33Dp2FjCDYzHhxL0SqyW4zkbjh-pz5UojjuebOloB07-nF5pt0Rz4g9bpu5TXUEcj_fBIzhDcKZsizERr--CCsc5eI3FjgSAxweTEkq7eCWUin7UnpRqpaF2LtF87fhEYqfx6syyZDjUFG5AX1djHycrbDxx1HstkFfBXKu3xl1gKHxU4L15jdzSkZhA7B7W-xATde_3pfZWkvhACSaW2oPCTRe8n43WJKYol4MuCmgraEk6Q_3fA-2GoUcn-KSKFKOMB40lLSkHQru7lE52iJ8y2sv794e3VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=Ah0qwRruhfidLnUh7kVM4u0UdzwT12JbKCBg1YGTizdGKGBweAf33Dp2FjCDYzHhxL0SqyW4zkbjh-pz5UojjuebOloB07-nF5pt0Rz4g9bpu5TXUEcj_fBIzhDcKZsizERr--CCsc5eI3FjgSAxweTEkq7eCWUin7UnpRqpaF2LtF87fhEYqfx6syyZDjUFG5AX1djHycrbDxx1HstkFfBXKu3xl1gKHxU4L15jdzSkZhA7B7W-xATde_3pfZWkvhACSaW2oPCTRe8n43WJKYol4MuCmgraEk6Q_3fA-2GoUcn-KSKFKOMB40lLSkHQru7lE52iJ8y2sv794e3VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
حرکات موزون و عجیب کی‌روش سرمربی غنا در تمرینات بعد ریدمان‌های اخیرش
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90897" target="_blank">📅 15:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90896">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkImg3gRLkAmazc5NLKNMSlnz7ycxj55E4b08yVpmGWx1TlrJ_ruHjl0KNtXTqUDhhGOPzbFz8wQCcdosH_rHt_NQ8IOFCY0ckYM73DHMsZDlV2mLfnMEULxspiW3EM5AgJ1-ykImskEwU2qelTQo5mZ7pTvlL6vp7_cdkMAveFOT-aJH_alwu2hAxLqO9ky4O8k0UpXjJNg9wTQowmJcspQ5xNTcqLuR9jYw6iJuwJ5pkGujF1Jip0wttLgq-JsH9wkk_VvZW1fK71lySrE5wdvR4zSTiZctq_crG-xaQ0xofM1jqmioqeiQZf0TNvwbQGgTqu8zxJJ22Sxfp00Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه ادوات بازیکنان نسل فعلی فوتبال و گذشته؛ واقعا نسل‌گذشته چه کله‌خرایی بودن
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/90896" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90895">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
شهروند لُنگ پوش اصفهانی امروز کف زاینده رود: بنده را به ریاست کل بانک مرکزی منصوب کنید تا مشکلات اقتصادی مملکت را در اسرع وقت حل کنم
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/90895" target="_blank">📅 15:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90894">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👍
از معدود خبرهای خوب ممکلت اینکه پس از ۱۱ ماه آب در سی و سه پل جاری شده و مردم اصفهان بسیار از این موضوع خوشحالن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/90894" target="_blank">📅 14:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90892">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش بامزه بادیگارد مسی و روبرتو کارلوس
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/90892" target="_blank">📅 14:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90891">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuPQjtIsORYffOqFAHqYsQv8S8rf2YPPP6toAIswEwAYwxKRnxFBNOjuRPg55F-csAaf34mxsZlNmXe4QnunY0v99B8ZHmguLUrM4TSghqNAW0NoHpBbDhqWZfSsFpRbp5scw680mAGfRtfE121zF6wzOe0up1KGa1E7PF0QxHTnYa1PXHTbDjJ3jNO22ktbGH_4qRvul1S917ZDndMumix0-Q8y5RCxp1t_vENi3AnDSjiMb7mKkotYLh0zASZ1Kt_je17u0vrK1PmEgIEIoOo3suR4R45g50RlCTa5rgUQ5aNfHw5NSwcksKIDMIXej8qoQBC6Sytkk6mMppaMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب در حالی ما با مالی بازی میکنیم دم گوشمون عراق با اسپانیا بازی دوستانه داره!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/90891" target="_blank">📅 14:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90890">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔥
🏆
فرآیند جالب ساخت کاپ‌قهرمانی جام‌جهانی در نسخه‌های کوچیکترش؛ خیلی دیدنیه از دست ندید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/90890" target="_blank">📅 14:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چالش جدید هوادار رئال‌ با موزیک ترند شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/90889" target="_blank">📅 13:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C31pbG1yvUtARG6ADVJ23Fr6G5IWEMPrvmzS_dgNaNZM-fk4rpxPMmivhcMrYs2_1ItNsH_uFJLzUanaDb_Vzo_Dfa8rOy9tOeGz-TvXXI8_R8YAiIpeXe1AgCypypw72ZihIvA0Wo6XqZutywuqsnyM_Z1qlSSv7DamfGCbqUp8_WLYAYKUuiAHHl_z-HcGJ2UeOdJYVA_3pE51OEg75UQuKzKKz9vNH2PlTkvZAK13YIlodX1Xary1Qt-TbbGPvU23APJUACfYxrTY4zSTMnb5sQ_ZJsw09sK8DCk1SBfa2S-MsOnF55kIYxJKStvG6EI2GtP8MOjsUX7havEwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📰
#فووووووری
از اسکای اسپورت:
🇪🇸
بارسلونا نخستین تماس‌های خود را برای جذب آندره‌آ کامبیاسو آغاز کرده است.  این مدافع چپ ایتالیایی در فهرست گزینه‌های باشگاه قرار دارد و مذاکرات اولیه برای بررسی شرایط این انتقال انجام شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/90888" target="_blank">📅 13:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام نیکولا شیرا خبرنگار سرشناس ایتالیایی، قرارداد ژائو کانسلو با بارسا دائمی و تا 2028 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90887" target="_blank">📅 13:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvCJQV0Eu5jhrTINrGJ8jR6oYulJ1W5hLSUgZA8Uo8szKt1N7l8AAIrn0AJA6XffMZTWIYhdpAP4nnuXv2lzADbBeyfDWsOIllcOPwtxhqYqZg7eXxh_kEzsBY1UiLDJtqVhFewICysGTm0fMSQ2YX8hOI1PCiXGV_AcpQjGQwowF34iNuzDstuFcaki8tzYODAEuBldQddvBbMybbS0eCSu2V2DJQNB4iiyomx9as-fABy57LpXn_8IBqK9UttIMmNwPgmJoIcQSIr5IXg0N3hj6s56ZluuejdgsZZaFT43i1AInK2s5R-1rGcGZZJs26kf4qETjYUzof33LCm_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جوانترین مربیان فعلی جام‌جهانی، نکته پشم‌ریزون اینکه سن نویر از ناگلزمن بیشتره :|
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/90886" target="_blank">📅 13:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
اسپاتیفای رفع فیلتر شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90885" target="_blank">📅 13:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOTn2tQg_whUJcSHLgjKZ0gloB5FRTWTwCgKXlihuJ4YRe-nFM-oK0z34nWZUGWEo6rQSHxMoR3KG1Zby_lteo12-1SwWoEuHsOJDmR5Fk5W7S6z0A9TxINi6NvO37IAcPDIkyCjWT_xSHdl_OQBVKoCgTEpjMIuWqvvSAJmHkDqwQtSZ5pyesB46VDXjkYENSDtLW6lnU63fnoG0-kYBaCfvBQrjYsGR8LWOF3EFCYO0EMio1e0DwYF8Zqsa8BwX5NCp9IawMun3rUz30aPCkbcWQCvEYvwmNGDhrRhzodEzG5T0h8Q7M-p-YaDNo6XW07RJLpjaELvyQqO_QHCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تاتنهام بدنبال جذب ساوینیو بازیکن منچسترسیتی رفته. گفته شده اولین پیشنهاد تاتنهام رقمی نزدیک به ۴۰ میلیون یورو هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/90884" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
چیچاریتو مکزیکی تولدش رو اینجوری به سبک چالش ترند شده فضای مجازی جشن گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90883" target="_blank">📅 13:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6tl-Jp4OvMFvZ7fAQztMCY8UVuoSUPfgtg-eRIApQ-xBvfzA8zQbtTvQNlM6720vfVAh33k3Yi5tfHcjM9GPoEzydlr1Nn3ZtKxajp6VIYNYzNBW4F4vDXDUBDzKZFA7uBIC3FD7Q19iRGuF-hLvoUA-yFTO2i3eXasNxX4npMICqLG5tg8fZ0S32nowQ12GY9kA8WcgF77NF-Og59fPPD5HPYo1AeHvwmZL_ICObaZeRy1D4_Ef5yQi_BXFmTGulHXky5EoRvtgnAD18-2nrsucOLrX66hIt7cg85nNrrxwIfZVXFM4o_jsFVxAPlOgJRPp7uLxwdsPC_fuCn-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رتبه اسپانیا تو ادوار مختلف جام جهانی‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90882" target="_blank">📅 12:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بی‌بی سریال متهم گریخت پس از ۲۱ سال
🥲
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/90881" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دهن سرویسا چی میسازن
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/90880" target="_blank">📅 12:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دوستان گشادی که به هر دلیلی باشگاه نمیرن و ورزش و سیکس‌پک در خونه میخوان
👆🏻
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/90879" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
