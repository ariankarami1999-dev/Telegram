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
<img src="https://cdn4.telesco.pe/file/Mqp4b6MVJutlKUoaHv3Sd5VFu9uSE30R2iJsqVub6gWTOZ42nClqmjnCKG-ohFdRxFLL75yY2PEIhHyVtGAugG9fBrP3id2j-i2libHd3TWahGb5uJKacBODhbAgcl0NM0PyT8_UEgmR_jva7nw8_-4HxcaO1R9U2mlJaFEDdXeeZ8H2Fc0BKE3pNEuPhZD7LlcFvtDz9_qDJX2T0_-8JYfHY6dBcrR9oGW-ia9t4oL1hzOfsTiLlZBF4__POWilEeGmvxXhCGIFMLgFM4JutPqX5NW5WwVRtiRX2z_PM49yxhY5ucBD0O8MGPPAnaU5GhoEU5RN1dQHySaR8FyHzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 954K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 21:50:26</div>
<hr>

<div class="tg-post" id="msg-129615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سی‌بی‌اس:
دولت ترامپ خواستار عقب‌نشینی جزئی اسرائیل از جنوب لبنان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/129615" target="_blank">📅 21:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 دوست دارید کی ببره؟</h4>
<ul>
<li>✓ ایران</li>
<li>✓ بلژیک</li>
</ul>
</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/129614" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بیرانوند: دروازه رو مثل تنگه میبندم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/129613" target="_blank">📅 21:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1jtOcOvKoj_u7IBc2iZSVIdXWJ2erzySo9MOybeXWqIdEZck11Lw13_nl-IG7K2Oy--MA3vLtY0MakfW-hrUN50CS5Cas2R3wLTgvA7saBEL1nKL7VhUZy43ZN0abZJLIEjfA2YkYkLcjsyzlSKKDEsWK8CEOrEDlMUM8DXvn_KdxntMhPT-08PXMeH7YKhJf7nR3x_omZfHuiS9QWm-8yIpeiXfedVCRyl0VUND8Bqk6_QQ77OsksEf7nkTCCjq5Bfd4fV5wHauVvVAXOXXm6X5_Mre4pKn1S4qDz_7vCP5ZBHGqszOf0mPH-6F9ruQtVQb9hF8V0j1yifzMeeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از نکات فنی قلعه نویی به تیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/129612" target="_blank">📅 21:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129611">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی کند، به مذاکرات باز نمی گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129611" target="_blank">📅 21:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129610">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2b50d32cb.mp4?token=p1fEKBU8OqB38aYAg2mIkCBYZPOJ4syAr7ZYFjoLBlZDtbm21LyNmc0EjwzA451uiNjdR-PEsUOQgoBIfsWjhwZkUmvkavnhfSn6-yuE9oz5QDjnu8eRYWfoj4HHOJaf68vEyAbbrlXFDc5VKt5fheXY3-0X5ZSwDAeYAERCDiCuQDxqBwhFk_zGFIaGCvNtsk16a-LBihbd5ZSCVQ7buj0yGK2TszpG_o4Ru-GoGhNJq8vE71R5IgRjzUw8rl8aD7AZw9MwYFztSJlICSg1xej8Ah1Lo5qDfyANFuq9JCXHi2orjyHeXiFHK7jgrrcY3DyfjRwFRlpgI9rgL_MIdUYdreY37WbnyFWjS9-LhodXBmMPWt6oQghjaemimo92MXQsNEh2tQu9OGF_FwU4WgJaPgqJdrGNjBc9006YVPxJLVT-lonnIB2fUnV_OxjKXFlG9dTg4_P3dfeM3q5KPcLFC8oq9acJm3nBfxmOuQNn_r2_hlFzswGdQ9P4vlIZnHCZQ3U-Xvp1514wS9G28wXkykrj3mp5hV8qmpazHkQH3NBWX2qXqS8haKOdXDg5TZDmO6TlPwj6oEn6OCLmwrtf6LNv8tIm2oEWlGrxJaaW2WoDjmEBFvNEp04lMWkidwVGTjUjqb7ZFPORDBATsLsc6meb3ANIKXcTi9NYlZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2b50d32cb.mp4?token=p1fEKBU8OqB38aYAg2mIkCBYZPOJ4syAr7ZYFjoLBlZDtbm21LyNmc0EjwzA451uiNjdR-PEsUOQgoBIfsWjhwZkUmvkavnhfSn6-yuE9oz5QDjnu8eRYWfoj4HHOJaf68vEyAbbrlXFDc5VKt5fheXY3-0X5ZSwDAeYAERCDiCuQDxqBwhFk_zGFIaGCvNtsk16a-LBihbd5ZSCVQ7buj0yGK2TszpG_o4Ru-GoGhNJq8vE71R5IgRjzUw8rl8aD7AZw9MwYFztSJlICSg1xej8Ah1Lo5qDfyANFuq9JCXHi2orjyHeXiFHK7jgrrcY3DyfjRwFRlpgI9rgL_MIdUYdreY37WbnyFWjS9-LhodXBmMPWt6oQghjaemimo92MXQsNEh2tQu9OGF_FwU4WgJaPgqJdrGNjBc9006YVPxJLVT-lonnIB2fUnV_OxjKXFlG9dTg4_P3dfeM3q5KPcLFC8oq9acJm3nBfxmOuQNn_r2_hlFzswGdQ9P4vlIZnHCZQ3U-Xvp1514wS9G28wXkykrj3mp5hV8qmpazHkQH3NBWX2qXqS8haKOdXDg5TZDmO6TlPwj6oEn6OCLmwrtf6LNv8tIm2oEWlGrxJaaW2WoDjmEBFvNEp04lMWkidwVGTjUjqb7ZFPORDBATsLsc6meb3ANIKXcTi9NYlZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ضرغامی در مصاحبه جدیدش علنا به حکومت دوره آقای آیت الله خامنه‌ای انتقادات سخت وارد و اعلام نیاز به رفراندوم کرده است
🔴
ضرغامی گفت مردم باید تصمیم بگیرند که چه سرنوشتی داشته باشند و خودکامگی کار فرعون بود.
#تغییر_پارادایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129610" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129609">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی‌برای کاهش تنش تنظیم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129609" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129608">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خطاب به اونایی که ۲شبه علی الاصول راه انداختن
🔴
اصول خدمت به مردم و راحتی زندگی مردمه که سما درکی ازش ندارید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129608" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129607">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: اسرائیل در حال بررسی «عقب‌نشینی‌های محدود» در لبنان است که شامل خروج از قلعهٔ بوفور (شقیف) نیز می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/129607" target="_blank">📅 20:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129606">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HHAdkMbekAhk-f_oSvc34TZF8vH9YNvkrWv5XslU0cimNupZ1wUFoD2YsMpMf-imA3ttl6ZqCjzULzbClO718vxZWAmD-_EphEizt8Is96eeCpBHGtdzMF7bx0fsHQLDAPMVMWE9Hfs83KBOecf0qdVlMAmxsEZ72WPZDXS4jN4CPWnhk2zQKTwg9_8VaRQQHvvUW-qsYuyRxBIglfDSr4UrJctfO9mAAAAKrNLEtn8ovcnDeH6wM3hXpQUJj_zWCOINMVhyGIq_Nn0P45O13NgR8jD7TGA59hNAnCc6l-fYMxaOMQGqFtHAcMvcDlkfUkAGumGYSMEgQP84uAoJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
ترکیب ایران مقابل بلژیک
@AloSport</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/129606" target="_blank">📅 20:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129605">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی به محل مذاکره برگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/129605" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129604">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfJcfjbZILjczlNrriq6vIFW0tkhqJsHriz6DlRptzvnT9ImYpYPZhiXKmFEXt755QvmE8Fv6S4FB401vywvl1a_LaOhuYYzJpVgHEHCAigSeh-Bb9_-M_qNenuKiBByiIooc-AddLokkpq89aubXHX60P-cTZjJKmQD2cIPayfgz2_DIU74AnIE-mMotVf_yo-I7ryF7kUV5wI9WVzKN8wIh9dFWdYWIPUmmGliaO8tacGvys_t8PeSm_Bp45sMDyITV3jKGUeU8XzUSISaUzPqGKkA_Nk14M4VokoSTRtzlxko-qv1Dk3Vc2oNF2kIBhQgSks6jIjfXPBQbpT8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:
مقامات ایرانی هنوز نرفتن و مذاکرات همچنان ادامه داره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129604" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129603">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ایرنا: هیأت ایران پس از دیدار با هیأت قطری به‌عنوان یکی از طرف‌های میانجی، ساختمان محل مذاکرات را ترک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129603" target="_blank">📅 20:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129602">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده:
ایران مصمم است روند اجرایی شدن تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند.
🔴
نشست امروز در سوئیس، برای پیگیری اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵ است.
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
🔴
بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
🔴
گفت وگوهای امروز، متمرکز بر اجرای بندهای مزبور، به‌ویژه بند ۱، و نیز مرور تدابیری است که برای اجرایی کردن بندهای ۱۰ (موضوع صادرات نفت ایران) و ۱۱ (آزادسازی دارائی‌های مسدودشده ایران) پیش‌بینی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129602" target="_blank">📅 20:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
منابع ایرانی به العربیه:  تهدید ترامپ باعث توقف مذاکرات شد و امکان ادامه آن را زیر سوال برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129601" target="_blank">📅 20:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
عضو هئیت ایرانی در سوئیس به صداوسیما: اگر جنگ در لبنان پایان نیابد، مذاکرات ادامه نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129600" target="_blank">📅 20:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129599">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
المنار: هیئت مذاکره‌کننده ایرانی در اعتراض به تهدیدات ترامپ محل مذاکره را ترک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129599" target="_blank">📅 20:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / فارس: مذاکرات متوقف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/129598" target="_blank">📅 19:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/تسنیم:
مذاکرات آمریکا و ایران در سوئیس زودتر از موعد با خروج ایران از جلسه پایان یافت، به دلیل پست ها و تهدید های امروز ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129596" target="_blank">📅 19:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
جی‌دی ونس: من شوخی کرده‌ام که دو نفر بسیار، بسیار مهم در زندگی من وجود دارند: یک هندی و یک پاکستانی.
🔴
هندی همسر من است و پاکستانی فیلد مارشال منیر است. احتمالاً در سه ماه گذشته بیشتر از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
🔴
بدون دیپلماسی او اینجا نبودیم. او یک رهبر نظامی است، اما فکر می‌کنم نشان داده است که یک دیپلمات بزرگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129595" target="_blank">📅 19:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwBZ3WBzffWF1Z7ouZg2xZrKW3hbS1DH0xxfc__58Bh1afH6LWuIWNnxPGPQf_QKW-t13RsML25RQ77n7MEE3A7_FR_KYM8vh2VExS6Nj17kQzWVtrIhoW5E1RckBT406gg8h_P43Zq8e8wuRT7tqjCZGDncuI9uvx7rs-KcWNVoV-v0YzCLd5WqNBLUhnP7usSXcO6JJysmJWQ_AIlGuBrmbbYtYPTC7TJ75e832gymSHwDdPgwq6txPolrMPM3FJBzKB8hSoquaBZh2P1ymfRQ4zEHft4inuzGfKwXYrD8lb6a6IUczGmiYLb1vyoQNuGEUCSJ2_TPVUrYhgO7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید قالیباف در واکنش به تهدیدای ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129594" target="_blank">📅 19:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129593">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جی دی ونس: گشایش تنگه هرمز، پایان دادن به برنامه هسته ای ایران - این چیزها قبلاً انجام شده است.
🔴
اکنون سؤال این است که چقدر بیشتر می توانیم با هم انجام دهیم.
🔴
آیا می‌توانیم روابط در خاورمیانه را برای همیشه تغییر دهیم یا به انجام کارها به روش قدیمی بازگردیم، که ترجیح ما نیست، اما مطمئناً ممکن است اتفاق بیفتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129593" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129592">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مدیر عامل شرکت ملی نفت: از دوشنبه هفته گذشته، کشتی هایمان از خط فرضی محاصره، با ۲۵ میلیون بشکه نفت عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129592" target="_blank">📅 19:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129591">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: چیزی به نام «آتش‌بس به همراه آزادی عمل برای اسرائیل» وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129591" target="_blank">📅 19:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129590">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: می‌خواهیم برنامه هسته‌ای ایران را به طور دائمی از بین ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129590" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129589">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
العربیه:جلسهٔ دوم مذاکرات اندکی بعد آغاز می‌شود.
🔴
هیئت ایرانی به سالن مذاکره بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129589" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129588">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اکسیوس: یک مقام آمریکایی می‌گوید که هیئت اعزامی برای نشست چهارجانبه شامل افراد زیر بوده است:
🔴
جی‌دی ونس، معاون رئیس‌جمهور آمریکا
🔴
استیو ویتکاف، فرستاده ویژه کاخ سفید
🔴
جرد کوشنر
🔴
جیکوب رِسس، رئیس دفتر معاون رئیس‌جمهور آمریکا
🔴
دکتر اندی بیکر، معاون مشاور امنیت ملی و مشاور امنیت ملی معاون رئیس‌جمهور آمریکا
🔴
کلیف سیمز، مشاور امنیت ملی معاون رئیس‌جمهور آمریکا
🔴
نیک استوارت، مشاور ارشد ویتکاف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129588" target="_blank">📅 19:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129587">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرنگار صداوسیما در محل مذاکرات:  گفتگوی دوجانبه هیئت های ایران و قطر، بعد از مذاکرات چهارجانبه آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129587" target="_blank">📅 19:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پرس تی وی:
هیئت ایرانی اعتراض خود را به طرف آمریکایی اعلام کرده و اکنون در حال بررسی گزینه‌های پاسخ مناسب به تهدیدات لفظی اخیر دونالد ترامپ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129586" target="_blank">📅 19:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
لیندزی گراهام: من روز جمعه ۴ ساعت و نیم پیش ترامپ بودم و چیزی که فهمیدم این بود که اگر توافق صورت نگیرد، او بلافاصله حمله سنگینی به ایران انجام میدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129585" target="_blank">📅 19:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727d10eda8.mp4?token=gQGsqrWYXUK_lBe4nvMwyfqLa-LOp6-gK35RWuECbbAEJCnW4W4vJQV0vFjg-OyI_7A6FQ0sLmkgU364SiO_UilWrV4umzE4mnhYvoAEaO0c6ETp2f1tYkfuaYdCARbx4aJgZJaVa9JH2qNhvKJ4adEE2nnI_pSa_hF2vfRB5rMZMl0AIYyjPP1ECmE0lihLb_ItvHqEjJ_xJCQ_J9LMk9GPZzJTrgHyshYA4exOxoWPbGZegXd2OgSpZDmMYUR9pB89ywRXRKH-ZMMfXtf81l7kVjLrYeQMyOudCyIJx8oBh3Rkx0cFc7VnyFWPT5MShfiuZcZNJbAdaaDN6mC3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727d10eda8.mp4?token=gQGsqrWYXUK_lBe4nvMwyfqLa-LOp6-gK35RWuECbbAEJCnW4W4vJQV0vFjg-OyI_7A6FQ0sLmkgU364SiO_UilWrV4umzE4mnhYvoAEaO0c6ETp2f1tYkfuaYdCARbx4aJgZJaVa9JH2qNhvKJ4adEE2nnI_pSa_hF2vfRB5rMZMl0AIYyjPP1ECmE0lihLb_ItvHqEjJ_xJCQ_J9LMk9GPZzJTrgHyshYA4exOxoWPbGZegXd2OgSpZDmMYUR9pB89ywRXRKH-ZMMfXtf81l7kVjLrYeQMyOudCyIJx8oBh3Rkx0cFc7VnyFWPT5MShfiuZcZNJbAdaaDN6mC3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نظر سیدعلی خامنه ای در باب مذاکرات همراه با تهدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129584" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtBIGPHi4HNrNurY2j_R2aMaN_Bwvj7Wj0pRaVil-eSWWUYkGUNJB9OfO6n4SOy-w6o_a7uEOZO5xDNlCmhKdDNZEmSZ7lRgk4yq0ACjd-OG93hEqLQzSyEHbVbyVPf0jYSng5UWPmrnRK9voBr7RO--2hIwkYMToNHW_8VNwRNlabeUJ7OZMRa1QVCm9VZyf3lTdU5MHA3hejbrp10BP2ZBlFAlklTYj_wSikaD7flkxK6njYWxFNbZbpU47E8UCenBCRO6Fi0pDELx5nGPVnnllzCxPDvpp9lrlu3bFLGr1K25Bdhozp3sD9MHfyTZiWvxiUq1Cum07l4pq0RAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : شرطای آقا رو زیر پا گذاشتید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129583" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
درحالیکه منابع رسمی داخلی می‌گویند مذاکرات فعلی متمرکز بر لبنان و اجرای مفاد تفاهمنامه ایران و امریکاست و منابع غربی نیز اذعان کرده‌اند که بحث لبنان و ایجاد سازوکار حفظ آتش‌بس در لبنان در اولویت نخست مذاکرات امروز است، جریان رادیکال در ایران از صبح امروز به صورت پیوسته در حال پخش این شایعه است که گفتگوها وارد حوزه هسته‌ای شده است
🔴
لازم به ذکر است که به گفته تلویزیون المنار حزب الله، با پافشاری مذاکره کنندگان ایران، در ۲۰ ساعت گذشته دیگر شلیکی از سوی اسرائیل به لبنان صورت نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129582" target="_blank">📅 19:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFREdqM9rJHQeknUIWVA5PHPkPrZgDFiQprGhuT040Ie0KRB1dmU4RLzhb9dLri05Nj6xcSEyYaol05nv6CwNa38L1ww13jYGq6EI0LEPM1onsyijK2moZEbtfI89-g-4_TVrgQb6RhFLOSwFtSY4YQzw91hJ32Pxvw_19ffRfiky5oyChsvlNaEA_eXqs7OWP1ioNCbCvbRI54uGXao-sseFcQiPQrKEe5WkYqftAMFnOiy1JsPpLKNBGhKlvWBqvJ82yuSyuIPFO3zxaStqlzamd0qflkxMNTK-g-tBGYvvG08VPeKGDgseiA8VIjPZkHfC95qbIwklLDuyYZ0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: گروسی را به مذاکرات راه ندهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129581" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نتانیاهو: تا زمانی که لازم باشد  در جنوب لبنان باقی خواهیم ماند
🔴
و در مورد ایران، هرچند تحولات سیاسی باشد، اجازه نخواهم داد ایران به سلاح‌های هسته‌ای مجهز شود
🔴
تا زمانی که من نخست‌وزیر اسرائیل هستم، این اتفاق نخواهد افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129580" target="_blank">📅 18:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک دیپلمات: مذاکرات جاری در سوئیس به جنگ در لبنان، تنگه هرمز و ذخایر هسته‌ای ایران می‌پردازد.
🔴
جلسات سوئیس به عنوان یک گفتگوی آزاد با صراحت فراوان آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129579" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نشست چهارجانبۀ سوئیس پس از ۸۰ دقیقه گفت‌وگو جهت مشورت های داخلی متوقف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129578" target="_blank">📅 18:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
جر و بحث مجری و کارشناس صداوسیما با هم بر سر نقض تفاهمنامه ایران-آمریکا
🔴
کارشناس صداوسیما: شما وکیل مدافع تیم مذاکره کننده هستی! پس من سوال می‌پرسم و شما پاسخ بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129577" target="_blank">📅 18:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed9884f2.mp4?token=U3JDUoR-vIoHaLDwfJG26hydY2ytEBOMCmEvhhCWl63Y1_VKEo6X8YsUrNRUK1HhP-_JXmyg0-A-A6a3YK-YyDJtfhKPBMMIXD9G-pWJYfgibhibmq5xg_SxF7zSWAxQMzU0wN_99oV8AIf8fi_K1nfdbXJuxrsgo8jcIGchhPxs_bSSwYussPaYd0umHYZCabmxWWmha2kiURjdjqgQ9BCGFnEMi3oSgmZ55X4PUAkZvYQ-KAJpSGQ1fRhPbXUFd2J_pjo52X8M21RyTHsbEHxyd_8kQUz_chDrZ8m_IthNgLtQaKq7i8cCq26jQHOepP2eZjIKdt7bw_h46OWbgaBDDGyANddcxvDdaRNDM9hyEL_I49d_ttkjgc7tRowKBTSjDvvzb_uWqQAgtO9X4WJavS7sDj_WvASQE7Kk-JPajKoynJH40-FpeRe4CcFIJo0HS85iSWOT94CdLZDhD13o4oDT7fZjB_y9TKu-v_uFOA8x9EBBOYohoLhlR7ZGewUXfHxJveqFq-7nREo8dFV6cpR2-3VUkje-NoV_Up8SUqQbiRGxYLhmYWyc5B91m9oTULucQYY4vHocL9QkdEJXhR5yyJKP--oesgrMhwar0gfN4n7ugqg_4LAvxf1uytmHNA6PAkLG5SLmtb4hXPo6WBA2fYajUJ0HRA0bxpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed9884f2.mp4?token=U3JDUoR-vIoHaLDwfJG26hydY2ytEBOMCmEvhhCWl63Y1_VKEo6X8YsUrNRUK1HhP-_JXmyg0-A-A6a3YK-YyDJtfhKPBMMIXD9G-pWJYfgibhibmq5xg_SxF7zSWAxQMzU0wN_99oV8AIf8fi_K1nfdbXJuxrsgo8jcIGchhPxs_bSSwYussPaYd0umHYZCabmxWWmha2kiURjdjqgQ9BCGFnEMi3oSgmZ55X4PUAkZvYQ-KAJpSGQ1fRhPbXUFd2J_pjo52X8M21RyTHsbEHxyd_8kQUz_chDrZ8m_IthNgLtQaKq7i8cCq26jQHOepP2eZjIKdt7bw_h46OWbgaBDDGyANddcxvDdaRNDM9hyEL_I49d_ttkjgc7tRowKBTSjDvvzb_uWqQAgtO9X4WJavS7sDj_WvASQE7Kk-JPajKoynJH40-FpeRe4CcFIJo0HS85iSWOT94CdLZDhD13o4oDT7fZjB_y9TKu-v_uFOA8x9EBBOYohoLhlR7ZGewUXfHxJveqFq-7nREo8dFV6cpR2-3VUkje-NoV_Up8SUqQbiRGxYLhmYWyc5B91m9oTULucQYY4vHocL9QkdEJXhR5yyJKP--oesgrMhwar0gfN4n7ugqg_4LAvxf1uytmHNA6PAkLG5SLmtb4hXPo6WBA2fYajUJ0HRA0bxpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از مانور مشترک نیروی هوایی ترکیه و مصر که در مصر برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129576" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات دو ساعت دیگر به اتمام می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129575" target="_blank">📅 18:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر انرژی آمریکا به ای‌بی‌سی:
۶۷ کشتی دیروز از تنگه هرمز عبور کردند و حجم نفت در حال عبور، نزدیک به میزان پیش از جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129574" target="_blank">📅 18:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل:
آمریکایی‌ها، چه درک کنند و چه نه، باید به خاطر مردم یهودی به خدا سپاسگزار باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129573" target="_blank">📅 18:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاکبی
:
آمریکایی‌ها، چه درک کنند و چه نه، باید به خاطر مردم یهودی به خدا سپاسگزار باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129572" target="_blank">📅 18:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / ترامپ: نزدیک است که مسئله حزب‌الله را به سوریه بسپرم
🔴
آمریکا ممکن است در آینده در صورت لزوم تنگه هرمز را تصاحب کرده و عوارض دریافت کند
🔴
این به معنای حضور آمریکا به عنوان «فرشته نگهبان» تنگه هرمز و خاورمیانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129571" target="_blank">📅 18:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBgyHKWegjXuCO_-GCW8JDRAji9FVBCFqdhmF7l4JMJTHAea3oWLFkhHbjiR3GSUArsJ3ZVRJLCOCyKkm9i4vPC-wkFENX_IL9ouQk0Qyi4ETQMlyVrVbsnh_rO7cDShIfB1eV15yhDcCQA7KPUgUuiH8r1S22_pLTm7rhR0BgOkun2cvZz1EXPhzzkZwk0Vz0ZNITMJjQbGFFsheWUAW9OtIEGqbtQR5PV9rMMRLcKAxOz8Wr-FNLAA9f5D33ojni-sTfM4paAdOUmPJFgXSSwbtrtfYkFnfnYVQ6D6mz1ONyef29-3RBRz4sbgJcWhTvolFWtfoY103G8yxvNFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بند اول تفاهم‌نامه اسلام‌آباد: جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129570" target="_blank">📅 18:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMSpA1YUnc4i47AqprSvDj2tvlj9lmmXpDv3GpJK6NvdAjz6uihya4NT-81Nac5RU9yF_CKKIgDpKW61hyUSxc25_pgRK6Sj6b9jGh3Dx9iDtfLyhHLPpjluSPAoxe3Xzg-oL3cxLDMlb3lkW5-9Pti7n0h6cCOq8TpwYyoF16eZ6PMYOi-TZzJzRI5sa2sBPbaJkmVA7EAlhJ_cW2DdaHUhqdWMBRezGbOAdZU2pix_irfT2niLQYcVsm3EuArmQuEB4ISj52eBTCgxH6F7KEjtPuJGTUCP6ThtMz2D5KrHkylm5T8IS31OhL4SXMRNp0OIkMr181ZP7oyTRMR_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل به
اردوگاه
البریج تو لُبنان، حملهِ کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129569" target="_blank">📅 17:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef202698d.mp4?token=dNPB6p4HjeZu2nh7eNhu9UgGE9ksQWbMRr5UNFfHgqwbEtemkwTjSKKpUuLYKmfZPSjqC-8KjXt7VvREOxsVZaf80fWBbT28MWpDIN9GRPcoKYrllGl_9wRRYLQAkvW9uYIFJIcA87oZ4jadidrUB-wPaia4ViQpxdfat2yWUhNPg76FgcJNX-C_Ekll1Xbv37_ryTYlmmUYZEhUntTRbjfnrCyEJ-l-d-4MrVZX7IZ6tww8jQ8y78XYyYvNFl2UVnM6sxF4O7dMjppj2yorysYTc0h4yGgdbewX6bGDs8PcGPoBLlO-yb7CpGNX3d2gYzooX-DC5jMTw86-Lbuvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef202698d.mp4?token=dNPB6p4HjeZu2nh7eNhu9UgGE9ksQWbMRr5UNFfHgqwbEtemkwTjSKKpUuLYKmfZPSjqC-8KjXt7VvREOxsVZaf80fWBbT28MWpDIN9GRPcoKYrllGl_9wRRYLQAkvW9uYIFJIcA87oZ4jadidrUB-wPaia4ViQpxdfat2yWUhNPg76FgcJNX-C_Ekll1Xbv37_ryTYlmmUYZEhUntTRbjfnrCyEJ-l-d-4MrVZX7IZ6tww8jQ8y78XYyYvNFl2UVnM6sxF4O7dMjppj2yorysYTc0h4yGgdbewX6bGDs8PcGPoBLlO-yb7CpGNX3d2gYzooX-DC5jMTw86-Lbuvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیبر امنیت داخلی آمریکا، مولین : شاهد افزایش غیرعادی شهروندان ایرانی هستیم
🔴
اونا سعی می‌کنن از مرز شمالی آمریکا، نه مرز جنوبی، مخفیانه وارد کشور بشن
🔴
این موضوع نگران‌کنند‌ست برای ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129568" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا: گزارشی از حادثه‌ای در ۵۰ مایل دریایی سواحل یمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129567" target="_blank">📅 17:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل: آتش‌بس اعلام شده در لبنان شکننده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129566" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKTk1evUmfsTUJyJ_GS3UVCWPqRuEBl92uOKb5rSZcndS-6PkFXZ3wmvo-93K0O2p5qasvCG9J8VpGrgLrVdLlN1CUzgo2ReXvVBCC_4_Gez0jpOi5I7kOYYhrOf8-3x0QvlvYdxr4dDUnTkjULwYIC1XLFlnvjHwNZ2ffUAg7hNnpY8Rh2UEK0e0hUFeeWKR-NC8i-YiEarZsSU5WIv1DXwSB3DY9qMyT5lyMQyZ0UyDEucyctpRcmAQ9VcldGKCnYCl1qx9FKb1qLcB3mdWX0w7KiGP21il0AH2U4ktnvCPYJrdOy1yXGeE6jz1aZCYqNBBFV5Sd5XNy7gnFjtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کیر استارمر از سمت نخست‌وزیری بریتانیا استعفا خواهد داد.
🔴
او در دو موضوع خیلی مهم به‌طور بدی شکست خورد — مهاجرت و انرژی (باز کردن استخراج نفت دریای شمال!). برایش آرزوی موفقیت می‌کنم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129565" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129564">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IILiHMq4cfg5UNYRxz62AVtw1ycAjpktMmeAsgQA2hywgCHz-tQIIBwHgmz2UjnvbjymnQON3nlM2s_9lV6R13Jshm1zQo0f_hW-bbwc6IGRyzGrU_sLUGkFa3ZsQXkMBpsjP-9i0zR-Y8-ljCS1Ri4KOB5YpeokYUZKyo9dKPHZ-jSfLZ22drBWD4HkTOAxPFRz3AKwi5g277sLxVHrO6aq98I9mjdKxDlszbZybcU5bTR2ecHmQgSQDBoi1x_iywu_Dl7xSBTYOBZIZR8J3Ondlfyzt2w9iaVxBMqgzwBUpl3o5gyJMe8_Kbn_PW89yQTGYLJd2pP6sT2Jvp7W-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو سابق تیم مذاکره‌کننده در واکنش به توییت ترامپ در مورد عوارض تنگه هرمز: هزینه‌ای دریافت خواهد شد، این قطعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129564" target="_blank">📅 17:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129563">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/ترامپ: یادداشت تفاهم صرفاً تمدید آتش‌بس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129563" target="_blank">📅 17:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129562">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkdx1k82izHoNLAWondv4XPkhMZwXFJSx-6oJCrtitLDA8-8Za7cWWMWEfBtbcYNA5KTNRPwY2Iv7uw2hKsmV5-RlXNzHHSxY4f2zFYdV1tEMRVMSNuMCNtftBsfbrDJYsZqyjFKUlbzhzFUe99DZQozucWOcr25xSzqwlBQegqfFHVht3IQLPxXfgfgsKIYpsF2_xCBzfXhsLV8_RiXkVC5YvC5cTPhTeR4qV9n9DxZE-fMM7KNO09PBxDy87AQtjNzxs5rxv_eR4Rk5BotuXpslGziVW0szBBUxvGGkeVa3bxRubJ8Fh7qXQFhK4izAgo6QVk2oaBQKh-ATDKtBR6Sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkdx1k82izHoNLAWondv4XPkhMZwXFJSx-6oJCrtitLDA8-8Za7cWWMWEfBtbcYNA5KTNRPwY2Iv7uw2hKsmV5-RlXNzHHSxY4f2zFYdV1tEMRVMSNuMCNtftBsfbrDJYsZqyjFKUlbzhzFUe99DZQozucWOcr25xSzqwlBQegqfFHVht3IQLPxXfgfgsKIYpsF2_xCBzfXhsLV8_RiXkVC5YvC5cTPhTeR4qV9n9DxZE-fMM7KNO09PBxDy87AQtjNzxs5rxv_eR4Rk5BotuXpslGziVW0szBBUxvGGkeVa3bxRubJ8Fh7qXQFhK4izAgo6QVk2oaBQKh-ATDKtBR6Sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129562" target="_blank">📅 17:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=RRXNXEaz_SYlKywufn-EVwIVDpVF7Jvq-fkL8Wofi4Lb8X4lJFVeCUrKtV0GlzOaGHraNplAvt8OVTURTrrdaAvTCYky8W0-DUTpcZe7lYBLaxGnemyFM_GZp7YPB4BCODXbgj6IiZRGqsNBQqtGMjDyvR0MTcrPX7wPNpTGRP-GCpxLDlY3-HF_DNh98tZJ4Uzy3c9K_n6Rvmvkmyz5AY5B50R-nNqm9vEcGT-jE6aptbxkgmdFd4cskqmir3kscu1S6B5PS0SBdGhpdIRsnWnHjIm9UUks9v7bT8WSJdnYmusc6VJ9DHlliHG-pY-osYlXdv4IK7tVPmJB5LrxB74EBNlluYwP5SRFe4RLyfdIvJ677P_94Gwl7C54X1139x35ZBp3UbDksA2Dl8L3WZ0o4YD_9IDKI4IAGxc9O53xcaUABshrSadX1CGF03rBjzhgKT1W_vYEdVsMZQEzXhx9hvViSxwst_B2eyY3wRiivPmmTwJyaXcXYW4S02Dx4DxEn4JmyKwKV7edg4rcbSPh1pFFVHj1VdPiJJII1kZo7ScuDmH06nZJW_UF3ExSQlkPF-eUCn-cQMVsQI1a3M99p8OlHam1bTuzmcoGlAiM1XKmjPPDzdPvlJLw6E8JMSgfQQUl3Xd-SJlQlMgiHg54l5c-glXJAFqODGvbgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=RRXNXEaz_SYlKywufn-EVwIVDpVF7Jvq-fkL8Wofi4Lb8X4lJFVeCUrKtV0GlzOaGHraNplAvt8OVTURTrrdaAvTCYky8W0-DUTpcZe7lYBLaxGnemyFM_GZp7YPB4BCODXbgj6IiZRGqsNBQqtGMjDyvR0MTcrPX7wPNpTGRP-GCpxLDlY3-HF_DNh98tZJ4Uzy3c9K_n6Rvmvkmyz5AY5B50R-nNqm9vEcGT-jE6aptbxkgmdFd4cskqmir3kscu1S6B5PS0SBdGhpdIRsnWnHjIm9UUks9v7bT8WSJdnYmusc6VJ9DHlliHG-pY-osYlXdv4IK7tVPmJB5LrxB74EBNlluYwP5SRFe4RLyfdIvJ677P_94Gwl7C54X1139x35ZBp3UbDksA2Dl8L3WZ0o4YD_9IDKI4IAGxc9O53xcaUABshrSadX1CGF03rBjzhgKT1W_vYEdVsMZQEzXhx9hvViSxwst_B2eyY3wRiivPmmTwJyaXcXYW4S02Dx4DxEn4JmyKwKV7edg4rcbSPh1pFFVHj1VdPiJJII1kZo7ScuDmH06nZJW_UF3ExSQlkPF-eUCn-cQMVsQI1a3M99p8OlHam1bTuzmcoGlAiM1XKmjPPDzdPvlJLw6E8JMSgfQQUl3Xd-SJlQlMgiHg54l5c-glXJAFqODGvbgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت: بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129561" target="_blank">📅 17:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129560">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نخست‌وزیر قطر: ما شاهد فداکاری و تلاش‌های بزرگی از سوی ونس، نخست‌وزیر پاکستان و وزیر امور خارجه ایران بودیم.
🔴
آنچه امروز در این نشست رخ می‌دهد برای امنیت منطقه و جهان اهمیت دارد.
🔴
نشست امروز تنها آغاز راه برای تحقق اهداف است.
🔴
این فقط آغاز است و ما برای آینده‌ای بهتر برای منطقه‌مان تلاش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129560" target="_blank">📅 17:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129559">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA51k04LquzDbroSFR8cIQtCei-Nqyy7Pjw48rtmKnZgmX4mreH4bAxRSUwYeYvuLndoHk3acVuheyd8H-HzbopCLYLKUNmSRJH0mcaD-aPcj3ZKq7geVQLGZ4vgp4n9iGXsktBcoqKTrlSk8lY5zwjbVctCow1c0MuCl1KrjZ7fbf8HBpgas2geA_RUqJ81aWQtqSGdCuoBmUuww0hwFrLwhbDYLcnvU8fVub4PDXYus6sohI4YlUux0sLtGL0v0gBEFyP_Gt7MKKM8geFNAvG8VmtsGL7YdC-NYZtFw0gd53jV1F8Qfip0FXpzSBmPMFCxwZwn-kQAjN_LBsFKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :  ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129559" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129558">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b4fe6074.mp4?token=RqRKLJXOgBYx-e-PnmE_0zpKWy9BVfKeGFAckNYYHPc59vMN0BrpZfv-3vbCpW07wRT4QYm3BYUDBZe8eZbFdSUWajpL5O7r5TMKkjb6P1b63Ob3aTYuFOwqoEYgfxtgSse21oTDiHYsmnD-PF968iWG7h6bIexy-hyt3FmmgiJgP7Ksvmo6UHoBM0qcmN6BsarKeHFOtwAaqjYfVzXKTUkh3bVDwD4y6UHmbA6x_uslN875I8MlvMTJbPM5ntdX-iNiAgYx7_oiXODaFqjrT8D-RxsUaUu0W6IwWZQN5hPV_HBmmRr6mpiQxvv9bHdvHFBlW8Y4W3Ddph_tEdcIVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b4fe6074.mp4?token=RqRKLJXOgBYx-e-PnmE_0zpKWy9BVfKeGFAckNYYHPc59vMN0BrpZfv-3vbCpW07wRT4QYm3BYUDBZe8eZbFdSUWajpL5O7r5TMKkjb6P1b63Ob3aTYuFOwqoEYgfxtgSse21oTDiHYsmnD-PF968iWG7h6bIexy-hyt3FmmgiJgP7Ksvmo6UHoBM0qcmN6BsarKeHFOtwAaqjYfVzXKTUkh3bVDwD4y6UHmbA6x_uslN875I8MlvMTJbPM5ntdX-iNiAgYx7_oiXODaFqjrT8D-RxsUaUu0W6IwWZQN5hPV_HBmmRr6mpiQxvv9bHdvHFBlW8Y4W3Ddph_tEdcIVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: دیروز ۱۹ میلیون بشکه نفت خام به دلیل این تفاهم‌نامه با ایرانی‌ها از خلیج فارس خارج شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129558" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129557">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: دیروز با مقامات ایرانی صحبت کردم و به آنها در مورد بستن تنگه هرمز هشدار دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129557" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129556">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: من یک گزینه ۶۰ روزه دارم؛ بعد از آن می‌توانم هر کاری که بخواهم انجام دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129556" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
تسنیم: هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129555" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
صدا و سیما: خروج خبرنگاران در پی شرط قالیباف برای عدم حضور رسانه‌ها در این نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129554" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
جی‌دی ونس: باز شدن تنگه هرمز و متوقف کردن برنامه هسته‌ای ایران، کارهایی است که همین حالا به سرانجام رسیده. حالا سؤال اصلی این است که چقدر می‌توانیم جلوتر برویم و دستاوردهای بیشتری داشته باشیم. آیا می‌توانیم روابط منطقه را برای همیشه متحول کنیم، یا دوباره برمی‌گردیم به همان روش‌های قدیمی؟ روش‌هایی که دوست نداریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129553" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: اگر ایرانی‌ها تنگه هرمز را ببندند، کشورشان نابود خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129552" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف: از رئیس‌جمهور ترامپ به‌خاطر رهبری دوراندیش و بسیار پویا تشکر می‌کنم که منجر به برگزاری این جلسه امروز شده است.
🔴
فکر می‌کنم اینجا قرار است بحث‌های فوق‌العاده‌ای داشته باشیم که امیدوارم در آینده به نتایج بسیار مثمر ثمری منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129551" target="_blank">📅 16:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دقایقی پیش نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129550" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ونس: هدف ما تغییر شکل خاورمیانه از طریق دیپلماسی مشترک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129549" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
جی دی ونس، معاون ترامپ: پیشرفت قابل توجهی در ساعات اخیر حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129548" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ونس : همه رهبران بزرگ دنیا اینجان
چون ایشون به ما قدرت داده که راه‌حل دیپلماتیک برای کلی از مسائل مهمی پیدا کنیم که برای مردم آمریکا مهمه
🔴
ولی فکر می‌کنم برای کل دنیا هم مهمه دولت باز ما حرکت می‌کنه و برنامه هسته‌ای ایران رو ادامه می‌ده
🔴
همه این کارها از قبل انجام شده
🔴
سؤال الان اینه که چقدر بیشتر می‌تونیم با هم انجام بدیم؟
🔴
می‌تونیم ورق رو برگردونیم؟ می‌تونیم تغییر کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129547" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQWr_yjCB096OYvr6txnVKsQwlBfAM0dJ8-mRGaxnM-8OTX37h46TnTs2-SO0ZXJ0wE-w-_mY_QfgYJkOZhPW3ob8SnE9aNDMiXB8YfoJdOgJzukYUtDdAp9fTp6WG_jhmp7U3JCZ4jxMpdaiJDzbPnezFojPX6XKwT4_26mZn-uXm4p1ohiNZJJXTLFpPlsCNK74icD-plpzqi6NT93fBYOEQlj7OjgnZKxLyTNAkccUNk9t-go007yFiBv8G2-0GeDbvY2XjAHR7kdNy-Lsl2PzlM4sQtE9FWYI0PoQjX2nXB5u-dX_rZZJE2aBFhDlCCPqCPJyVqcmuciAIqy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت تتر همزمان با شروع مذاکرات مستقیم ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129546" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ایلان ماسک : هوش مصنوعی داره جای و شغل آدما رو میگیره، واسه همین دولت باید مستقیم به حساب مردم پول بریزه تا اقتصاد فرو نپاشه و تبعات هوش مصنوعی جبران شه. حالا با تولید ارزون و انبوه توسط هوش مصنوعی و رباتیک، تورم کاهش پیدا میکنه و حتی ممکنه دچار تورم منفی بشیم، پس دولت هم چاره‌ای نداره جز اینکه بین مردم پول پخش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129545" target="_blank">📅 16:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از دیپلمات آگاه از مذاکرات: میانجی‌گران ابتدا درباره سازوکاری برای نظارت بر نقض‌ها و حفظ صلح در لبنان بحث می‌کنند
🔴
در مورد اعزام هیئت ایرانی به سوئیس، مقامات قطری به ایران گفتند که اگر هیئتی اعزام نکند، عملاً به نتانیاهو «حق وتو بر جنگ» را داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129544" target="_blank">📅 16:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گزارش تازه دیلی میل به بررسی احتمال تغییر رویکرد روسیه در جنگ اوکراین و بحث‌های مرتبط با استفاده احتمالی از سلاح‌های هسته‌ای توسط مسکو می‌پردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129543" target="_blank">📅 16:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مصر، ترکیه، عربستان سعودی و پاکستان بیانیه‌ای مشترک صادر کردند.
🔴
در بیانیه مشترک وزیران امور خارجه مصر، ترکیه، عربستان سعودی و پاکستان آمده است: بر اهمیت دستیابی سریع به پایان مرحله بعدی مذاکرات تأکید می‌کنیم.
🔴
تأکید می‌کنیم که تلاش‌ها باید نگرانی‌ها و ملاحظات کشورهای منطقه را در نظر بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129542" target="_blank">📅 15:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وب‌سایت «زتیو» به نقل از منابع آگاه: ترامپ به شدت از نتانیاهو عصبانی است؛ او گفته که دولت اسرائیل سعی دارد او را فریب دهد تا دوباره جنگی تمام عیار با ایران راه بیندازد
🔴
رئیس‌جمهور آمریکا به شدت در این باره فحش می‌دهد.
🔴
در حال حاضر، او قطعاً از اسرائیلی‌ها بیشتر از ایرانی‌ها عصبانی است
🔴
حملات مداوم اخیر به لبنان، ترامپ را بیش از پیش به سمت مخالف فشارهای تل‌آویو سوق داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129541" target="_blank">📅 15:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emQtrb9-JwCnuYW_qqIp5YY_F4pCOKd_gqdKROQKFBlYwTODh4HzVTYXCztVTbE7do_ZvthA1u7OSZs5D3APhwLE5ORjNnlIJhm5waGzenEkVTMZ1rm8oKwVaRO8EjZFukYN8EH9oMpv0eV3NhuGLeaZ_YD8dQo57Ls-YeStWcfy9yXbX9TUozu9mAJcSPZtPOakZsgyBnMI-oxfZ_0n7sONyllnFzvjX3eusSpTQXsk5w20MvL2hJcrklDJUSLPr7cGzJLUzQ1xk9uNHbnMPqJO5J3XOI4wrzgE6S3Wh76L1Rk7MQbv0rhhByqqfr1TfI2pwiO_x6zDjpQYi7FvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ روز پدر را با تبلیغ دولت خود تبریک گفت: روز پدر مبارک! کشور ما عالی عمل می‌کند. تعداد مشاغل و بازار سهام رکورد زده، بهترین اقتصاد تاریخ! بزرگترین ارتش جهان، تا به امروز. ما در همه جبهه‌ها پیروز می‌شویم، پیروزی‌ای که هرگز سابقه نداشته است. خدا همه شما را حفظ کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129540" target="_blank">📅 15:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
امارات به عنوان اولین کشور عربی، استفاده از شبکه‌های اجتماعی رو برای افراد زیر 15 سال ممنوع کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129539" target="_blank">📅 15:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129537">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=h5Mk7o3qluMmrIWNK2ND_TOcOYk0kiOPa05ybAf2YAH1WH_30yoBgn33wQUG7LVJiR1w6nfYyRjw8d3o-DzIDUE2RUZFvhEpdo3k8KRmJwmtnIWIt5jK-2DascvR7dkEQ_-P8wl7htArv-XApBLM4hDYgHuYXxcPQTezXwffO0bWWLGlzANwgbgDWz4ftSj-6mhlWvAd0YhCu_81402HsSVfeyTOO6nq0Qj_uuPSdvB5NFxTRUMj_lYTSgvIY5EDv-VbcNSG8oZnUhCK6Am-vzo-gB4WNPXH_tO1BoWpEHUwtG6CUZFICEo1-RS3pCp8R5wkyywqlNmSsE9iSsmjTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=h5Mk7o3qluMmrIWNK2ND_TOcOYk0kiOPa05ybAf2YAH1WH_30yoBgn33wQUG7LVJiR1w6nfYyRjw8d3o-DzIDUE2RUZFvhEpdo3k8KRmJwmtnIWIt5jK-2DascvR7dkEQ_-P8wl7htArv-XApBLM4hDYgHuYXxcPQTezXwffO0bWWLGlzANwgbgDWz4ftSj-6mhlWvAd0YhCu_81402HsSVfeyTOO6nq0Qj_uuPSdvB5NFxTRUMj_lYTSgvIY5EDv-VbcNSG8oZnUhCK6Am-vzo-gB4WNPXH_tO1BoWpEHUwtG6CUZFICEo1-RS3pCp8R5wkyywqlNmSsE9iSsmjTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت فعلی در سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129537" target="_blank">📅 15:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129536">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2df66b5d.mp4?token=JQRfsbKWlfoIpzOYhh1I3ffF-fxjCLsIYH24OjSuFhgBO1nTKloQlVh8i15Nutskcb2Ist_VUsiB7kWa_ccv_ioMVRlIMgLJF-EEamBJUiVLHcCwsf_xRUJT3z3u2VFJl_4NRKM22z1m0vFmcqG2vonFkd5jgmk7_BHnMUBlJz7remN4G7TKHMi1A0SG4E1EKIGcpwGVkBU5ipjhEBAcE96V-Di94YGm0d8hxrhBQl5FuqD7ukIObQcjvOVmx3gLrOADB0s8S9l_L2c-Ddf8Vw4aQQ7Auz_ktN1xZOSJQdm7ta2ixLgelg6x1I7trErM8-VX-kobdMIOpJzpVhN3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2df66b5d.mp4?token=JQRfsbKWlfoIpzOYhh1I3ffF-fxjCLsIYH24OjSuFhgBO1nTKloQlVh8i15Nutskcb2Ist_VUsiB7kWa_ccv_ioMVRlIMgLJF-EEamBJUiVLHcCwsf_xRUJT3z3u2VFJl_4NRKM22z1m0vFmcqG2vonFkd5jgmk7_BHnMUBlJz7remN4G7TKHMi1A0SG4E1EKIGcpwGVkBU5ipjhEBAcE96V-Di94YGm0d8hxrhBQl5FuqD7ukIObQcjvOVmx3gLrOADB0s8S9l_L2c-Ddf8Vw4aQQ7Auz_ktN1xZOSJQdm7ta2ixLgelg6x1I7trErM8-VX-kobdMIOpJzpVhN3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شوک در حزب‌الله
گزارش‌ها حاکی از آن است که محاصره ستاد کل حزب‌الله در جنوب لبنان و در ارتفاعات «تپه علی طاهر» در حومه نبطیه، باعث بهت و سردرگمی در میان نیروهای این گروه شده است.
بر اساس این ادعاها، نیروهای ارتش اسرائیل موفق شده‌اند به یک مرکز فرماندهی زیرزمینی و ستاد اصلی حزب‌الله در جنوب لبنان، که گفته می‌شود با حمایت جمهوری اسلامی ساخته شده، نفوذ کرده و آن را تحت کنترل بگیرند.
این محل پیش‌تر در دوران حیات سید حسن نصرالله به‌عنوان یکی از پایگاه‌های مهم معرفی شده بود و در همان زمان نیز موضوع رونمایی از موشک «عماد ۴» مطرح شده بود.
در ادامه این گزارش‌ها ادعا می‌شود احتمال گرفتار شدن صدها نیروی حزب‌الله در این مقر وجود دارد و گفته شده ممکن است تعدادی کشته یا بازداشت شده باشند. همچنین اخبار تاییدنشده‌ای از بازداشت حدود ۳۰ نفر و انتقال آن‌ها برای بازجویی منتشر شده است.
حزب‌الله در تاریخ ۱۸ آگوست ۲۰۲۴ از شهر موشکی «عماد ۴» رونمایی کرده بود؛ اقدامی که در آن زمان به‌عنوان نمایش قدرت و پیام بازدارنده علیه اسرائیل مطرح شد.
در حال حاضر نیروهای اسرائیلی در حال پیشروی زمینی در این منطقه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129536" target="_blank">📅 15:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129535">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
گویا علی الاصول راجع به مسائل هسته‌ای هم مذاکره خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129535" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129534">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: آمریکا درخواست انتقال ذخایر هسته‌ای ایران را مطرح کرد و ما به راه‌حلی با عنوان «کاهش سطح غنی‌سازی» رسیدیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/129534" target="_blank">📅 15:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129533">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtg-0jfbL9xdh_w-V4ngVrrnNy5ml_DLjlm4UW8n9Wa9s14EMFsN_qY9mHbIG1YvHiUq-3IpI340O_xPeRVyNt2n7nDN1jmu5N5lJUKdGBAxbJEICRumO2roxC6OLk7NoXXQd_046vzNaRDhTE17AWerNIBQZq3_NzS68C1uBCcfSd-C5F_1N16jo3wSNzXM9kc2RywJf1-ZdRbbrMenrfGJE_71_1l6vH01L2B1U7IObha1pebsoN_RQ6aAXx6preJLN192iRNHkjns-s4T_6p5Y9qB9lhzTjwVEXqcfw6oTmZz3cTsSzf135IDwIVSEpep1dyxyeUBVWvcGiChXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون سوئیس، جمع پایدار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129533" target="_blank">📅 15:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129532">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW_tw_LAnWZ88mAXBnJV1KhEFx_1XOmoxO1lVNAp0FJnaqn3sH9Jmo716EF4ep55d3DKdm6uSupDgaGjtmagIk7-n9jx3icd2hnaO7Rx1NToobuJp9CmyTlT4f1mGTOXCsQqhu3i-GKhzYau-k7zuAQm3oonWmn4F-wnuCqUIgA3-Pb4EiERmuVRovPyWgT3F8KN3g_qxb5AwKXk1jMxNNlPaMNxKh3Tehbxv8UTWpCGqMN2qvmgLfH6TTQesgSPbzNXFkxH8ltTV7fI8OM_deEyDpgKhFww92Dj_5NI8ctggexJ0l-0oT6ZgSn4jCLxWiwmAH1HBikZOAzggP3TUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت عالی سد کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129532" target="_blank">📅 15:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129531">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر خارجه پاکستان به الحدث:
🔴
ما موفق شدیم آمریکا و ایران را به گفت‌وگو ترغیب کنیم و به آتش‌بس دست یابیم.
🔴
ما توانستیم آمریکا و ایران را برای نخستین بار پس از ۴۷ سال پای میز مذاکره بنشانیم.
🔴
ما در هماهنگی با شرکا و متحدان خود این میانجی‌گری را به نتیجه رساندیم.
🔴
جنگ میان آمریکا و ایران فاجعه‌بار بود و تأثیرات منفی شدیدی بر اقتصاد (منطقه و جهان) داشته است.
🔴
سه تیم فنی در مذاکرات بین آمریکا و ایران مشارکت دارند.
🔴
کمیته‌های فنی در حال بحث دربارهٔ پرونده هسته‌ای، دارایی‌های مسدودشده ایران و موضوع لبنان هستند.
🔴
در طول دورهٔ ۶۰ روزه، هیچ گونه عوارض عبوری در تنگه هرمز اعمال نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/129531" target="_blank">📅 15:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129530">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
برگزاری نشست سه جانبه ایران، امریکا و قطر با موضوع لبنان و اموال بلوکه شده
🔴
نشست سه جانبه ایران، امریکا و قطر با موضوع آتش بس فراگیر در لبنان و اموال بلوکه شده ایران هم اکنون در محل مذاکرات در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/129530" target="_blank">📅 14:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129529">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار صداو سیما: یک دور رفت و برگشت پیام با واسطه پاکستان بین دو‌طرف انجام شده یک دیدار هم با هیئت قطری برگزار شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129529" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129528">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد که ارتش اسرائیل (IDF) همچنان برای مقابله با تهدیدات در لبنان آزادی عمل کامل دارد؛ این اظهارات پس از پاسخ گسترده اسرائیل به آخرین حمله حزب‌الله مطرح شد.
🔴
او تأکید کرد که نیروهای اسرائیلی در منطقه امنیتی واقع در امتداد مرز باقی خواهند ماند و اسرائیل از جنوب لبنان عقب‌نشینی نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129528" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129527">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBInMfR6k1-1n_UrEehJtTDjJNUfkUdow6ZjHsZE8EH2WP-qARJygd_skIYESpYnC8dDzaVhWvK5dNcv9YWG6hKXhiSMFiPSomso-FHY7Vyvak7xLCEMqivQgCEhfimNxscMt-YMZQkB40JGQdaG0b2uVf2tB-2HOBv8fTmgcXMaDk0_Xtbe9weHxgih_IuQEoRscxPqR3y9LSq4IiH1mP0zmkvlOBSOJVtRh-vkImiAm3adAZZsW98WDyJIfLgxCsTmJbzSKGrtPKQn3CrL-CCW1HQasvPpDl-swIbVDWNwscctDMAbZNfXKNCqm9d8nuMIMfwNtDODtJPXLnZVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی:ایران مصمم است روند اجرای تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129527" target="_blank">📅 14:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129526">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پزشکیان: ادامه جنگ به نفع هیچ فرد یا گروهی نیست
رئیس جمهور:
🔴
ادامه جنگ به نفع هیچ فرد یا گروهی نیست. بر اساس همه تحقیقاتی که در جهان انجام شده است، هر جنگی موجب اختلال در رشد، توسعه اقتصادی و اجتماعی و افزایش فقر و بیکاری می‌شود.
🔴
این سخن به معنای ترس از جنگ نیست. ارتش، سپاه، نیروهای هوافضا و مردم ما نشان دادند که با قدرت در برابر تجاوز ایستادگی می‌کنند و اگر جنگ ادامه پیدا می‌کرد، با قدرت می‌ماندند و مقاومت می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129526" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129525">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl6vtQGmoBfRoL7aFF3iHSUfKEq0KMwZ5LvNI-keOpM2CN-MfzMhLRaMWIymtvqbDJiFQ-dUhNng02-KzsHoMihcilon1HfYZQQMwOdzKnmT8stcFwdKQijlyqQY9Ha5_zp_7a32b3l0KRJRYLYZd0Jo1TQUkuhGSPv5kXOwEnFIr3kZQg8HjUNl0rcGoKc5VsMoAtv7SbHyM1ilM16aGsIKH6U8frgOF3QkaUYBnBbKCJ0jKLjZjoHv1K5VecSEOVCq60YZRvozGrQEAVmH4oiE4ZGMnWc7mGlMeyRp8RLIYW9J6qy1u0i-19bs4ApCZ-mLyzIZeUldepNyDPKhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام ایگنازیو کاسیس وزیر امور خارجه سوئیس پس از دیدار با عراقچی
🔴
جناب عراقچی به سوئیس خوش آمدید.
🔴
در نشست دریاچه لوسرن، ما چارچوبی برای گفت‌وگو و تبادل نظر فراهم می‌کنیم.
🔴
در شرایطی دشوار و پیچیده، رابطه مبتنی بر اعتماد میان سوئیس و ایران، که در مأموریت ما به عنوان حافظ منافع نیز بازتاب یافته است، همچنان در خدمت دیپلماسی و در راستای صلح و امنیت در خاورمیانه قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129525" target="_blank">📅 14:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129524">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پزشکیان: در شورای‌عالی امنیت ملی تقریباً همه اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد
🔴
مقام معظم رهبری به دولت اختیار داده‌اند تا این مسیر را دنبال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129524" target="_blank">📅 14:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129523">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=E70JLhK7rJdzmgSEoijXmKNLRRehC7kYpw_8IhobUYFbtBKR47GhqWk5WSiDReTAqbz8S_ymwzSL8qqioZOGFedbt9iNnmamw0lijex2ANkcBO_lQnvBtSphfgBwJHYWDqCA6_uKCYeLAsulS1k9ucAG7UzQNLO89ZtRm5F4EIHWsvsqjVx0T_GDx-qTezZyWxfgs2df0SrD3TRC9De9AgjMaxL8VapWtjS077nFXvO8wnHLG-PuAFznYjZfH6we5n5wFwYFZBlhM0_HSjCYPxnRIFQoTspWFy7jYZPV4IGj94oxGO7O9x-mE_1YXR0AO28go1l1qyKeiCe372enhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=E70JLhK7rJdzmgSEoijXmKNLRRehC7kYpw_8IhobUYFbtBKR47GhqWk5WSiDReTAqbz8S_ymwzSL8qqioZOGFedbt9iNnmamw0lijex2ANkcBO_lQnvBtSphfgBwJHYWDqCA6_uKCYeLAsulS1k9ucAG7UzQNLO89ZtRm5F4EIHWsvsqjVx0T_GDx-qTezZyWxfgs2df0SrD3TRC9De9AgjMaxL8VapWtjS077nFXvO8wnHLG-PuAFznYjZfH6we5n5wFwYFZBlhM0_HSjCYPxnRIFQoTspWFy7jYZPV4IGj94oxGO7O9x-mE_1YXR0AO28go1l1qyKeiCe372enhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار تیم مذاکره کننده آمریکا با شهباز شریف
🔴
تیم مذاکره کننده آمریکایی به ریاست ونس امروز در جریان مذاکرات چهارجانبه ایران و آمریکا با مشارکت کشورهای میانجی، با شهباز شریف، نخست وزیر پاکستان دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129523" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129522">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otl5JswHk4D8M1Xj0wVu1YfbjLEM1Ls8GNc-dYzDdsK5eGtlYuf7o8a6j4zsjPp8_-b2xNrghO2AGwmi7lL4dFHsfQIkbQ1FHtaMHIbOuI4NNgQxnSCamDQWogfb4HzxwITAsDm4K8o1PfcPCybpoiNhfDV03KF3jWy6Ea8v1A3Tuhrkf0QZkpkejVnV2fKbSsrZOipg9rB3-TXI3rWYErCV6ef5a5yUj9UXJkwrDY4VailWSiDYh7kYXw5IyhhHbYLySHD3PRsd-6-TE9GjPCF1aq_8pWZT0eBXeYu1_RU1Q80s_14dGX90rTugl-hPEpN3uGbWJrwArWkACZVH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر کل آژانس بین‌المللی انرژی اتمی گروسی گفت که با وزیر امور خارجه سوئیس کاسیس در بویگن‌اشتوک دیدار کرد.
🔴
«در این لحظه حساس، مهم است که به دیپلماسی هر فرصتی برای موفقیت داده شود.»
🔴
گروسی همچنین از حمایت طولانی‌مدت سوئیس از آژانس بین‌المللی انرژی اتمی و تعهد آن به دیپلماسی تشکر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129522" target="_blank">📅 13:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129521">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پزشکیان: دوران محاصره دریایی یک بشکه نفت هم صادر نکردیم البته طی دو روز گذشته ۱۶ میلیون بشکه نفت صادر کرده ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129521" target="_blank">📅 13:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129520" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=NWJkUecMA2zW5TYMvfiTqfDpdBmItZ0zoUc5uRIZayVSRbKHuEUpr76sjNqWZ9uxQCwPhvapDfN5H4iq1lNYt_N8rl_bJFYxBH64WPAenOefAIFUEE7dLe3-JMjE9XSSURlXKalfctXmzsd1FqscgcsWUdLMDXkbiPcrLfBrqgPcgxKmpFTHgxk75egaMjvoIGhnDPrdF1iuhv6Iz1irFpOv3st8Kb4vtdysJMjXlqxBYICr-9mCuIgfUATRKyeZW2d_RJjBcddj9-56gA42rywd5hnArptkqx3tw39KgOyoRXZY1DD-W32qzyheelu0kPlnGj8tbaOAo22xVhngUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=NWJkUecMA2zW5TYMvfiTqfDpdBmItZ0zoUc5uRIZayVSRbKHuEUpr76sjNqWZ9uxQCwPhvapDfN5H4iq1lNYt_N8rl_bJFYxBH64WPAenOefAIFUEE7dLe3-JMjE9XSSURlXKalfctXmzsd1FqscgcsWUdLMDXkbiPcrLfBrqgPcgxKmpFTHgxk75egaMjvoIGhnDPrdF1iuhv6Iz1irFpOv3st8Kb4vtdysJMjXlqxBYICr-9mCuIgfUATRKyeZW2d_RJjBcddj9-56gA42rywd5hnArptkqx3tw39KgOyoRXZY1DD-W32qzyheelu0kPlnGj8tbaOAo22xVhngUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف، معاون پزشکیان : دنبال جنگ نیستیم
🔴
ولی اگه کسی بخواد شاخ بشه و جنگ رو تحمیل کنه، جوابش رو جوری می‌دیم که یادش نره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129519" target="_blank">📅 13:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZe-4TiOQ2e-TxMsUWMiIGqD6EVfabbBmLti_IDgJGsojgG_hjqMq5g8f6_zQN_ANCwC7eTuupoiWQ4NeWxgFikQ9j-uO-HLLRapFxVo5LC-jjK9noXsSiseUqY4M6conSTg3YDtPExXl7xKSMeDC-qXynovMPUVQP6NlGLzkkgOJsfDzf4Rj6ZTWwtXnQ2QObyxc1M-bpSmOyXmpiI7cWXEPmJHUHzfM5zvTfzftJ--qwOqGVL90cIB_43Oj9xTSjStNHbGYQgM1T8ZMRYcldcCUbFX6u2W360ubvYGLuwT3jpqLTpGjhNBE7lwMU4yxCpU8syV-T25Ui9QrnYPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود اعلام توقف گران‌فروشی اپراتورها در طرح اینترنت پرو، ایرانسل همچنان هر گیگ اینترنت پرو را با قیمت ۴۰ هزار تومان عرضه می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129518" target="_blank">📅 12:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ6qCkQRm3aPEg7OmWcyFl7UTlzkea3xjv3BNjZ9IXqBxLvCkTvL-O2U8eth2UvninpiC8CCfQ_Q5pf7caBTOjKKmmPyuwt0VDfSDSWmZNtR7zrr5y6MH2AYOiAJ-gDoZNp44hqR53lqqple-uN5glVlz4vas7mPmdfMCF_7PrLWPo2UdfU78OB88vJhQBLYudqInEeHY3ypSW9qqRsaFsVd2_Af8uoXsp_eGisnPaUfhti-vzmf3RmgS7SM5c8falZYRaww_PpcHa5JhWbDcPAEFB7T_XgHdrRFs44kyl6-Ncnq5anxh6Z34xDAw0SMW4ExZNKcs__KJTRU_dnwgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار رسمی اعلام شده از وضعیت پتروشیمی‌های کشور که پس از حمله اسرائیل شاهد حدودا ۸۷ درصد کاهش تولید نسبت به سال گذشته بوده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/129517" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxkiKKJNSeIDFirXv8RoeX5Of8kDdzuJR3xW_73OR9QBaMuBZXlp-sHi7DFsGC7f2RtqxgPuP-UlpHiMzfBwYu6Xkd9RFDY-Fw4j42nIcpLRhIEeWlbM5lN0TKaqPC0DPZ0M3hDCUWkHsPdnKuGCrNu63MO-u4KOqXLqjGfIvNBtLTMaSAx0RhusmGuHrj6RndYQlzjBl1WCTMqmC1TUIh1ThIsE5Q4bGoObh_2eDjvvFRSX9xT8T5chFU5NMyVbXl6cPgNuxfUt69tCR2WR5EE1uF_Q67u1t6XOTwpcHZe_cYTkA-06QjMLa32OPqOwXSSN-kPSDUmHbPQpPTvvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : قراره ۶ میلیارد دلار از پول‌های بلوکه‌ شده ایران برگرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/129516" target="_blank">📅 12:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیات جمهوری اسلامی عازم ساختمان محل مذاکرات شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/129515" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129514">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9coQP7zW351teL8LngZrtBfxuWVA0xo3lILp4h2nU_tXs90sxT9Ft77ZvpfzG-NiJALX6Nc7U0l_Vrnpm-9vTIKeLIal8N9oyuGDpBoe8qhIJPgoI2a5-Dz9C2RtJ0pejnPV8u1X-P5pv8wtR17BzO9MbqAYK8eHsFJUV6YsRIV4GoLmXoG2NgDa6ijnC7BFiPU9W52aIa9y7HPDPSmAzZBrbyNZ3BMO4A0uhJkoMvwdv6MUOuBqSL2k9eVwg4JYsoX0KahWa3Z7rdwAc210UEX7K2Tk5lW4ilRLLIujKLDF2FFv9B4copwufV3uco3F_gCxOngk7bU6usq-KxrHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمایی از محل مذاکرات در بورگن‌اشتوک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/129514" target="_blank">📅 12:07 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
