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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
<hr>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=XhvxPJEmhgn-76YWVC-XEYzi62ECdFEhGWsdiKAMiQGpKiZCY2lBBce1b7dIjtHfSE-X9XFsw7zwFhdIoQUXgc4faE_l-LwmyX-7fwS6CKYF_TzG9eDpshwsoQ_K88dcOyQbmE-28fYY2-7ieHG4xpPvpP_Xz6516i--8LqsXXpJ-ppab7zLBlxlp1Kriyje5EakWFKduzEFgE4pBlyq5_Eg_dmqmeiRf_PPM6QGD5CXLSzEwynKfWmKBszdgSNv5F0onDl7oosMnjo5XX6oZaJVv7dI_JWF4islQPaZkBFhQFXgQe0T5XT01Y0oGk3cBF_UjWeNYpQDr0MIfeG5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=XhvxPJEmhgn-76YWVC-XEYzi62ECdFEhGWsdiKAMiQGpKiZCY2lBBce1b7dIjtHfSE-X9XFsw7zwFhdIoQUXgc4faE_l-LwmyX-7fwS6CKYF_TzG9eDpshwsoQ_K88dcOyQbmE-28fYY2-7ieHG4xpPvpP_Xz6516i--8LqsXXpJ-ppab7zLBlxlp1Kriyje5EakWFKduzEFgE4pBlyq5_Eg_dmqmeiRf_PPM6QGD5CXLSzEwynKfWmKBszdgSNv5F0onDl7oosMnjo5XX6oZaJVv7dI_JWF4islQPaZkBFhQFXgQe0T5XT01Y0oGk3cBF_UjWeNYpQDr0MIfeG5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=NxDv2qsU88Uht_eMdoupW-SKbUj4Ut1TasWu0b_Adhtjicd6CDZi2K80c7T7UF7MEEFxMfCkGQEt9Tqn2fQ7sfnBKM2OPrjumx94MBHqtLycjmGV5hbNfeZfajmCqkLhtromXXjyXFjjWOcm8gQmkIwMHQmZyXNan5tYlaqp3Bgai2yAzpKQjUkfHRy2DHAJz72E0e8WrJ_fPj3PJeXqCND4gZPwhu6SAsKf413wTAwr6LW0E3GsIQlYyXsUnMp30N21JXLynW9BkFFs0Ohb_VZtAhDh1ylp3NH1cUQx8JRVqN8LA58ysvU1Po0XEiUIvdTk1A4VafRVDcJJtoeHDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=NxDv2qsU88Uht_eMdoupW-SKbUj4Ut1TasWu0b_Adhtjicd6CDZi2K80c7T7UF7MEEFxMfCkGQEt9Tqn2fQ7sfnBKM2OPrjumx94MBHqtLycjmGV5hbNfeZfajmCqkLhtromXXjyXFjjWOcm8gQmkIwMHQmZyXNan5tYlaqp3Bgai2yAzpKQjUkfHRy2DHAJz72E0e8WrJ_fPj3PJeXqCND4gZPwhu6SAsKf413wTAwr6LW0E3GsIQlYyXsUnMp30N21JXLynW9BkFFs0Ohb_VZtAhDh1ylp3NH1cUQx8JRVqN8LA58ysvU1Po0XEiUIvdTk1A4VafRVDcJJtoeHDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrO7cSrShcbA7oEVSGy5OWRjzxGLCxF-edMDWKn1RPt9HA9KJVM3fXvMWYGyOQsPlN68UOuZ0g8AHCZgyZ7L3BWLKZtMlLzsQSY1x0O0QdGP7qSCPQLv0GaI9GUDiVk0GA1dmY-QquKn3M2ufhxBj6mgV7dTo_P12UOu8c6qVOv6_vBlLp0jPzhbm7XZCQh1DPPQ7kSRx7BqnELKKgbLNgcJHjiavAahFoarTXpMkfnAlxY3UENbDS0V1bja6AbgWFiYB539GxTZ0SpjFhldfLt2L2yEb19ChY_es5VRk8i1QiKevT7Ghc24Xg_jMvOSAxlKKD6nFUghENAHiByVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=ZlsvbDClqvN_jrciemggC96xQ3ivTs219Hanke4olGno-WXNGEkHYv4kGcFMr-Y04ucP8cSGTr-_s1eIEIVSg7G-INKl2Ss1HOy3JK4vXV6VsUT2yHdO_m3eh46aadH9Eycdlr_GMcrzgJaES9LJM67OGOl99BEcmy5MKwkbA3dW_4TgnCrtSTle54p-gSDd0TLT6pCnsjd2DKl6IElc0BWoKmRhgAXgFMArPpb1-EM5sETpFjxmLBXFhXIuxgfsKP7rFgFF-gEiuBgn8BwD75q3Jr0M1mJ5fsrsm8yPt0lqopGw98CLG83C-2ZEXKOVS9CHjUPXl9kcGbu-Yyyxaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=ZlsvbDClqvN_jrciemggC96xQ3ivTs219Hanke4olGno-WXNGEkHYv4kGcFMr-Y04ucP8cSGTr-_s1eIEIVSg7G-INKl2Ss1HOy3JK4vXV6VsUT2yHdO_m3eh46aadH9Eycdlr_GMcrzgJaES9LJM67OGOl99BEcmy5MKwkbA3dW_4TgnCrtSTle54p-gSDd0TLT6pCnsjd2DKl6IElc0BWoKmRhgAXgFMArPpb1-EM5sETpFjxmLBXFhXIuxgfsKP7rFgFF-gEiuBgn8BwD75q3Jr0M1mJ5fsrsm8yPt0lqopGw98CLG83C-2ZEXKOVS9CHjUPXl9kcGbu-Yyyxaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6bycQ0H_-bQHyYXuerZVIJXGJPtf5k8WsGXCSgJHv49PhG4nmXW-iQu-VJCQd7kWV55iEoHQ0ZOChaxQNIVrTDcT--J8rDU55g_m26OMG_NMnIZpPd0f6iFRIYFHk1nhbD4p8gvzjIjALxeOz3IOea9vWUXvSrv6ZeDqWRxgCcmcWD1rM8_Iz5Vsla0ptPnx77bdiM0EkQ-flrpXVVYi0HCEmtenVkLCLPkeQxFy3QSW0F96Jw7YioerOXieHpnIekFPoqu2AwO902ThPjSxMerVsP40LwQyS5TY0Q2LN_-f6eQZJKXTU804dKwVekKZ_IwRG4Ibo8HGvTu62LO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=j_anMZe4xYmoKy7QSkaAWb0ci3chYBWUunVSY3erLkX4CzoeQJ0WbZUqUFQ924StGLxuwyCqjIRaSNFqusy1Uds445x0kxq-Fcm-v6HHkM3Bx7xU6ZphtjRMPNbRzAUMlN9jylmaP4-Lppymkqa2evQ3n3hTnODPlJ_q7sRCOcxXNaMhDTt-GfgPGawMRhcTYBUIqQC6V_jk80jOzadCv0HcE8DuUNRevjK2hsicPSMx0mIoku_S9dwAyGKwVS4CbwnvWK6PI602QqfcEzkno5RZa5YjA44BTzxTT0as0sJQJXh1dh6KB93IgtSR55-hm5Ojo9PKmlBjj0HmX1F-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=j_anMZe4xYmoKy7QSkaAWb0ci3chYBWUunVSY3erLkX4CzoeQJ0WbZUqUFQ924StGLxuwyCqjIRaSNFqusy1Uds445x0kxq-Fcm-v6HHkM3Bx7xU6ZphtjRMPNbRzAUMlN9jylmaP4-Lppymkqa2evQ3n3hTnODPlJ_q7sRCOcxXNaMhDTt-GfgPGawMRhcTYBUIqQC6V_jk80jOzadCv0HcE8DuUNRevjK2hsicPSMx0mIoku_S9dwAyGKwVS4CbwnvWK6PI602QqfcEzkno5RZa5YjA44BTzxTT0as0sJQJXh1dh6KB93IgtSR55-hm5Ojo9PKmlBjj0HmX1F-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=vwVEsuMDWl_TBj2XDd5a1luIc2BlpDxic1z206h5DEucN9kgK3XqenJAEAZUpcKOkq4yZRcpyGriIAxZGLjOQzSIhtqoZBn7GMEIUN0w_wJfQrlYlPHwzZBLJ0wZdeQB_34lAyYEjZhWmzEA6UNvdpLDHJOq5x-0lvzmlPU1IRET4eGeA8-E-gYgVSVBwnvPBNxs6lGT2ef7V2av-Z9bohovNJ79wbcPFU831wf15baGRSoq0tIT7f1C71xKOlUIQiJX-inZcMkFxTQjAwV3xiafXtvIxKXfnnSZW81xy1WhGBnfQsth0bTH4OOiST_IUaVYPwoqBy0OmI_72mYkTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=vwVEsuMDWl_TBj2XDd5a1luIc2BlpDxic1z206h5DEucN9kgK3XqenJAEAZUpcKOkq4yZRcpyGriIAxZGLjOQzSIhtqoZBn7GMEIUN0w_wJfQrlYlPHwzZBLJ0wZdeQB_34lAyYEjZhWmzEA6UNvdpLDHJOq5x-0lvzmlPU1IRET4eGeA8-E-gYgVSVBwnvPBNxs6lGT2ef7V2av-Z9bohovNJ79wbcPFU831wf15baGRSoq0tIT7f1C71xKOlUIQiJX-inZcMkFxTQjAwV3xiafXtvIxKXfnnSZW81xy1WhGBnfQsth0bTH4OOiST_IUaVYPwoqBy0OmI_72mYkTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=DaEZlypaPVr5zaVOzbZ_Cw8CB7pe38pICsGHou1xVTRm4IHagHLNhMH5Zh0_v4x010uEEEKCbGDAHKpwBG0MVCdL6U5_qOB5Gyk4J3Ke8979r25sFnzhlAbR9j8cifEaLkwkJHAUQKAglOp_d8Ya0WVEwHkry_eZ48t-l9G2EebTiv-5WfkZp3EtniUkueZ6OYdz85FWSEj-5sHq9cuVyC417OoHeFfbmYF6QLdVW9nUzX3MzXSX4XgNfWyYIOSr3RAcD18UHHmG94Qmwa78vl0kuo8r_J01gEKbxixu3Pg1P8dq4dwdI8MI5-T5-LrcxvlxFZRp1vNztBINiAl3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=DaEZlypaPVr5zaVOzbZ_Cw8CB7pe38pICsGHou1xVTRm4IHagHLNhMH5Zh0_v4x010uEEEKCbGDAHKpwBG0MVCdL6U5_qOB5Gyk4J3Ke8979r25sFnzhlAbR9j8cifEaLkwkJHAUQKAglOp_d8Ya0WVEwHkry_eZ48t-l9G2EebTiv-5WfkZp3EtniUkueZ6OYdz85FWSEj-5sHq9cuVyC417OoHeFfbmYF6QLdVW9nUzX3MzXSX4XgNfWyYIOSr3RAcD18UHHmG94Qmwa78vl0kuo8r_J01gEKbxixu3Pg1P8dq4dwdI8MI5-T5-LrcxvlxFZRp1vNztBINiAl3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Uc-UD93Eyf8x3S8Yzj46Ohk46_61VT2VLQF2oVCw6RsDtPRYqhBxeg6pbpx_e9hjb0ps_Zts8OCL2UZwt-x1xcZ3zZNfiz7MPqIGCjONmBi_Qq_n5dWvST8NM3yzxH0S7ReD9R2CU_oAihZQVm6gwxgyzsdd14vuqnIRouuWkGwUX23ZGcXsKbdH9SopxbI3GiAWPUaKwJ4hWeiV1K5ChhRehnsTzFTpL5ryLQdMRgpGoEXaOdbACqoM3kxs_HwYpO3cHSGJWmAo8UCXDekWDCsgjSJq_wOQ_ZjX3kjomusAF9SeIJVfF5UrL-pbsKo-8l88DMjHBNLrFFIN8Fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=UbhHhM8lYtnHNbCzwKzK6uCsxDhHb7NVeC4Yeuq7zoDWCUMLuBYr9N7r_EkrNKKAQJWZ5F_zYYl4KeWxRFf6muYo-pIz0e8tU_rhBF42OV5bXQKCqx6J2FCfzkob55jZn5VZu-OrxzTuv9EJdhSW3_Ny0LaMwHW5ae_mGw-VDioW9RMPVryc8Ytnobq-l1C6T4Aid5uZR-KKsqBp8ZsKk2LQtBJohDxhltXLQ2bFOuaqk72KGVshpXxFKtAZBN2mEwfeK7NGdA8NUoSl-nP7oFQgB1s30yf4ViodKfHHKw0PQjdfXKIEfewy2sf9udKzXXeFIiKumN07jcsesZVt9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=UbhHhM8lYtnHNbCzwKzK6uCsxDhHb7NVeC4Yeuq7zoDWCUMLuBYr9N7r_EkrNKKAQJWZ5F_zYYl4KeWxRFf6muYo-pIz0e8tU_rhBF42OV5bXQKCqx6J2FCfzkob55jZn5VZu-OrxzTuv9EJdhSW3_Ny0LaMwHW5ae_mGw-VDioW9RMPVryc8Ytnobq-l1C6T4Aid5uZR-KKsqBp8ZsKk2LQtBJohDxhltXLQ2bFOuaqk72KGVshpXxFKtAZBN2mEwfeK7NGdA8NUoSl-nP7oFQgB1s30yf4ViodKfHHKw0PQjdfXKIEfewy2sf9udKzXXeFIiKumN07jcsesZVt9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU1RBzQTBUbidDg2yMXAf_nMJck74b_xjwLmAP8MihLGmDwuJfXa7DeC9FybPRzttvU_7STN7_lKrj5HfP5B2ut2PHL2fi47qQL9Bq8BmqLSB8MX0LQZt1rqCYjh6dEbbyKkYBPbKBbRqbAOCKGOsF4XrMNi4JdXW76mTM3PNUM20VWI6MgNsgI_lhFyPLnkDdTCDYSMk7iQZijCKA0Zd8cIMzK2fQya-iEAg4Qu9u3cxZ3xQD38i6Suci1_7nKVMA3ix9wnB0JeZ_me7-5dmEqKulYDu493hkjAKheWG6tbEYm8XU0c87XXrQb6qz43Wf2_xhuzHYx1wPjFpNIQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMbU3vzuDXvf5urw_4PfR-LOW4cQqHFWwCuZF9DCCxbpU9uFC-19MFjn7lTK8XXK0-UtHaxdXD-4XfLc79o_aQQkIaL-UyyTJefeWXqmxD1EyK56G6tZGJkPfKRHkIetetVbrmRv2DfMLKaPZVtJoDcr0tjIa1iA85bYscSauDcZ_gVIQ_0CcVIJkVuwnJmdcdPa00Nt_chS2CVYX-yFnATzbgGgRbWS35QlpoO1-szE8V8NkmIbyT4maIlveTtn-DySgNj7Lcbzjr80znWwNpFN6rZ7Z9rnZ8cuziX3y2nHkmIzm1pg8APYAT1ND673c8qBUYURMUMQAcY4gr6ChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG-5sqZX1xQBmZW5c3NWWez7I749Bp0nnvfe30Prm4GleJehkcM6oPeUHhoLeM27sHa4g9pNOrDKt4CyjG0Ft5SvdJcnpUKSWQtgb63mcEDYGnrsd6RjFvY2U8iIK3SUTD-BQELaY4-cHq8wnvoRCZ9etkYCTF0eDnEy-kRIowWOWav_UkeJNCfU7Sm5PN6GYAvjSV4sUfLC6Zx1lBhpsiEml_gyIk8QFddUOKIyzbXMVz4AF4XL048NSe3MueZbL5zVBM2keDLXhO-jybmwJrEZ86eoGcG5S23zLeTt0UpxqnVJ0jRKgtgSxfJlaSaI7ESe5hV6T6lj0EfSa8TeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsHKqb_La8m_yyO26AyQT6qASjMDPTr8_5eT-qtWr5WpFsdyE87azjqgXTAyZwsHgjpP4jIzN1SHCFCEvs1LUU2hpmZ5Wf18j03q-Y-MFtjl8n4cCyZ-CStrGXZs-Epacj7bd6eQpr0ar8-7023tYYx5S6TbacozT0jn2_uF5pOvw7Mj6_3KEl5KLQhwVOqKVOBusi2rkEND4gGbF8Qrko8RNZPVclWolU0BNkiCst9sxoP5BT0177BsivmWF8ThHlTc81Px6yxMCaqqsM70gjbww8o_Fb4wv1NZV62tsIjTwklc31zH3SVFSCiD88l9qij8S3gNVm9XkCy8RWtUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC5ZRQdOHVYFW6-raQ7qbkHYmgLrtVsDhur_vZGBjpii03a74u84a7BDTwyST3nLpqBEanB-AhUmMOj8AG6OXw58UttWDLsm3sDErD_l57t0SkOAlHXj8mk3XiTeLTaM18ZGSqfYLlde6yBDZVCdZ7F-QBJ3UwXk8a8d2gNZQltqHPy_EJ_3O20IG62TfX7HEtdr1AKMz90l5DyIqMSveEbhaQ6-UxYCb-iq5mm3f-3djA6x0BR4SvTmx81Xer5ElWwH3nApZijhVhTHc9enQVKSvGJ0plXHYghFf-qmUo_b6BRkLsF8CSvgQxUouKpAIvp7FtIvlBRJMeSvU3faiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jisNc-GuII3jgAhWpUFfEh8_DkmhJpAbVbNipvktTQPIMAGqKrsWTuoQpMX5cpxdAtQHguCkHWDcBXeZ3PdY9xI1DsafwKSvpzUBCNnAMP7kk4t6fHFBuw47VPVOw9D0ezIawTbIzlwT0vFBHBBKHxYLjS0uGDxp-l--z5zNuP9-U4-bIBg7WMX0f6mUvNNsH6pPCH5XCIEkUuqQGo-fHNDzsaEUnY3gnb8-86aAuMjhPPNjUkR6TGZT5qR4QIHo7ADouJUDoyG5eBn9G6jxFPqFzfN-CBYPXXsqScvd8kifQe5lgZVOzA2SCrIBVx8G1Z9bF0j1Bxxvbaj_d8ca9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1yqSKDWR0Bv6ahAGlnWbRraAdHbTvkN_2842ibZPmSPE-06xgLfhpSxPY8hLHSFYnQYbzIxONNs5dsTmIrQ5esuEwNVycaLKgouKI9A6IpmNEPFzCLe2MW1XnVYY69kceI3B0I6aWNbNHS5tXnDRTQfFEBPHUYudvbqderK7WaRE0kkPrBSXQbid4MyTZihOwaK6SnnVxmvQmK-PY2hVEQ621bJ4CJwcDfqEr8d9SiqzXTcI20JgfqMSS7i885qe0DHyEfN8OM3dwtyBARgxWWHEpvJ67F1W57__8LKNi7Eb3CdvF58MN0cx2LVI1RIKzqOoS8PS2ODKoy4GWcX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYBRVtc_ofzWPFR4BTiR-rJwZcjIuU-eBXaVTO5I1cFhFZM49PNXO0UG9izG2sZpLZaQCOaZSNiXF4LB7NzOSW7DIG130sq_DPELtbsRyy_pQBnlkC7GESPJcBGwog0S0vJG5jvC8pwo-SAxaWsFGvAbvmc0ebJ3HGWjDAuw_gFUI072PTqNPArs0Q1ISRkkjasZhJEtpci9XebvHM858yMkatiqSpzafWbNZ5TIcSTln-o3uxa79mN935l80WF6wxj27giVqJO61FGtvHkeM7DXGgH3rE7IhjeL1Pz1cvYfgVtsdt9H6UIJXUg243q4e9yUHBal00NRUr7pMtEdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1OWhfM8N0SaZAh-Y5yeieVZjEdV3q65BCJIFksxXudlwziIFfTtAtfTRCh4c7U3BiXrPUYr8sfnuBNBaq2T5OeMeqDSLXM0vTbbshy93x_IKDiPJHfGFVMrxfOv2CnKJZYcd8S5aI3WbnBy1wjdC2XhuLO2WWwEjDz1qJ2IybUjrZNX7VZ6YjRc5Ae0TpRUxg5Yn7YV4EymSVg-se2SXlM9I5ymBW2w0bmmgxQ9iUZtJHD54VxXYOpljofOI04_BVoannKeyHgqtdBAJ9hMkzXjtjnOL91nhgV3sdx-Yfq2CU-nE7qR17k0Rk46slMBD7r9EQGZ3tRV2NR3nsofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5BhspcJvWsUHX1l_ZSYx4BLbOVS6NIKr1ZiUlW-0WrO697-hC_lJ-kpoKxfLSTVwjNOb0ik0kv_Ww3wN34HHUpC-OQ4KchX8LX8UzRbc-22AiW6Bh0BpXI1c0d25PVLjd8ObxX5aZoFyHsQc9aog595GIsCCEdzn7dGlbKrPxgI0L-6DS5AK8qI8X7RXR1-RGPHT5obwGalHPNNN-noqKQ5EvRTnFIhPxAgqR0PrTdjwXVcXht2R5JK-simj_R_EDkVafF6GOYIjgAyeBOIKkNG7jAdJynwVR4dH9tGMo_sWQLxWw6DQfwx__NyknA5UnevSAj0A4mU_MINzdII7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3zO2oKfXJ-fEiVMpWDXugkY72dmBbcNReNvbG79Y4uyc6RMPDeUviPVQaFJQBfa9hmfL52Hj7ea_vbMs6ozTzO_dzfdzci5UR1fWJK4ETDvvJ0npnusiZ1L0PjrZpidZH92rKkebdgpuK98N1OJujIvo1rCEROUSxEFFdIXuDoNMgJOYI3uNWuKSC1Fes1l56Di7W-aZSeOLM-6D_1FrqgISi_0lZpMBgFJnNB8rB0PmNsPXlHw0yQz7YsjWMSLgTRZc3hMzcTNIYeicskdwXP8mP3L5eVD1mNlWgE1IOUN4AMygwkCZQzgSI004U5iUuYNrh90QFeXDBd9GdrPug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=SkKEvnqzppPGYocJopTE1efTmVJfAR_OOx0ZhgKXPOlr3nFhuQ3MBOHaPKnNdz9KVKy4QiKD_KJEwfwQ4p9QzdsAgwK1slcp5Fpu8_UlTb2Mf6_a068uqGudflNOir9hBdZm5acb5G7EKEL0hmUcEeNNgQi91zjJ1EPKEgDhV_SuU6Ty7Ih5g8t3rbDpipIZef1WrxE8Rw5gS93MUqkxDvK8E4Fm02L_-Gn80ZDW-c5JZ4AOXFkD45GhgBgGdI31HrbS30QVtXwYkD28MiGJ13W5w0728_H9WKEuRWzEk9_tVLEWJ2XmunjYtSeAXU3m7jIYEscdBBtWP755SvqaGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=SkKEvnqzppPGYocJopTE1efTmVJfAR_OOx0ZhgKXPOlr3nFhuQ3MBOHaPKnNdz9KVKy4QiKD_KJEwfwQ4p9QzdsAgwK1slcp5Fpu8_UlTb2Mf6_a068uqGudflNOir9hBdZm5acb5G7EKEL0hmUcEeNNgQi91zjJ1EPKEgDhV_SuU6Ty7Ih5g8t3rbDpipIZef1WrxE8Rw5gS93MUqkxDvK8E4Fm02L_-Gn80ZDW-c5JZ4AOXFkD45GhgBgGdI31HrbS30QVtXwYkD28MiGJ13W5w0728_H9WKEuRWzEk9_tVLEWJ2XmunjYtSeAXU3m7jIYEscdBBtWP755SvqaGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzAlNAuqqwSgXqo8NvmErGWn7enByHW8GRYhiXiKN-CS_a7OpbXtNvNyWBELH_und9x2t9cokX2yvYW7Yvkem9F2vconDE--oCR3eWK6u8CfR2AkJVXmmZGvL2910oOL-bQO0WEhjFP_KqDxrygyUN6KwWDDsdYcBO2LDWFXM33Aurf1u7vuvnVtWfADO1if9bj4GyKRatj3e87rxpFyk9UIQZJKONf4A3THfNahMwuCuQHCLck3lmPVyKjHceAcGjzCxAD8d3GpX7krns8nKSJhA6jH7ltD3PqVi0imRp4QDYbfYuKoUw3mMm8T5pC2CEgVGT1Qlib04rvIJwEe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=cNKEheWC1JXtaqv6DMgn_WIQfHCOVMj9fXlQ0Po1hsMK7EcsFy7G7iGhf1Xtsyo0i4nJffKy-0W9WUQ1nMUB3iarp5cq3ehNCjcYmzn2iDSzysX2pmEZVMv1ycWDVvWns69hSQCuMmThQusfzUsu6O6DS6JBikqqyuSPJfmYUav6ibOKT8rqQcA-c1lOklvcIZtIXJoqfSHTe5Jv03NmlbPoW_P5GCnaZb7rgsKMHx7fgHYQVFyR2sCbZKzgnLqSq5QMujNTyWm-yzCDe7haeoSS5-liDdJPpiJcrOWvdSDh7Sn3VAUTz4wtC-4OgvW2ItBbUzYkDp1xP_2yfGeMXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=cNKEheWC1JXtaqv6DMgn_WIQfHCOVMj9fXlQ0Po1hsMK7EcsFy7G7iGhf1Xtsyo0i4nJffKy-0W9WUQ1nMUB3iarp5cq3ehNCjcYmzn2iDSzysX2pmEZVMv1ycWDVvWns69hSQCuMmThQusfzUsu6O6DS6JBikqqyuSPJfmYUav6ibOKT8rqQcA-c1lOklvcIZtIXJoqfSHTe5Jv03NmlbPoW_P5GCnaZb7rgsKMHx7fgHYQVFyR2sCbZKzgnLqSq5QMujNTyWm-yzCDe7haeoSS5-liDdJPpiJcrOWvdSDh7Sn3VAUTz4wtC-4OgvW2ItBbUzYkDp1xP_2yfGeMXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqzjh3iRalDNqtjRvY4lvG1ggwHWsOQFGCHDmno9PVRSc7nA4QDXYFosDZ1LJfzZrOPWOrsGWYmZ1dKUxXqVQM_gcg28W2ZwnDT7OtzVzx4J4oAOh-rLns22ZSHlEyxpGcUNc5piRMxYK2iwQlBqBXfZ-8999-5DqwsC8BZJ9Vn2kkSm-h7UjhXClfBg4UG1YicYN17fhHZHn1bXEjVg_zeZMwtMgKIPI49f7bWiNHoSwa28qCY9hDsGP5XVQtiI8z9dGEckKfhXvM8qqd7Gh9MMPEV3SxI2SM5Ad7XNbd1G_ZMfiGOfrctsrC64XNR2dJ4Unu8MsQ09vouWiRXmXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlYKvXcpx9Utnvx0hq3ftMymGIWxO_v6KNic31lK-A2YvERf4M8WjXGH1CXRZw5xdBZObA5ZKsPeAeRNz7cQIHQSRYyvjU-Z9weld-LEOfHQbDEg0aA3_fsMplpJ_9RUEuKfsUNDPDh9_sZP6xgelN-EPAioyivNbKaq_SNiNfS0E0o3ZE07Vk9h4mdTBa2NrlsDeSDyYVQzFe1V64amlnVfX1rqDzF9emghd55rEs0CWJteaiyEbOiEEciEEF0gWOC7m4AjNd5uMS0yIRW-ygeX470nPR_JuMYpLY9cH8CNXycI4Vp-ehFrj1I3K1A1Ti9jPCkiUeimMEJ-8WsR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqtWFRuh4BTN0Z-Wqr3pU-QPrUISnzI5PhA3AQH9NmeP9VbZTnJSEIfzw36tlS51FeJ8UQ-q230RFlkxnp7tIG6IhmYz0sJimycPlppZUqGs4c2-cChWIyNqIhWi0wnM93eC5eP9J5608kSYE0YZh1Gs7G-tHKoELJlxCMrY3L2N85odxLqzsC4eI2_aQ0fIHoq0He7EXAcVXNNvx7NR1i7QvKhuIBdU5B_StF7Ppu7Am9OT8EW67E8nOgjccUHyIcYJ0iOz4oeL-TQBaWlj1oalcsQQLndhbzsxwlgUHn_4PvQAUWt5bfc_E0GPls9Rwdl69ghsODDlPwEww5WHGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPsZWjTS16XcuHedRJbXBdTxVeAr1cKlE2wCbQQwnT4F7rkEV_ItdUuoSoSr0CFSZ9KBNQmpFuEJtKmy8yGuQFWi-hLjsV-I6UPJfZNrJfoIY4Kt3_1EawYalZpRp2XF4t2IEOX6XZ5LzZtKIryX1R8eN5ah-IZPtGP-BghSlALntCk13SI3hA3rzM3FI4ap9IGssrKfCzXAxL0IYP_A7RRpPtArbH2yChCdEOk-Rnsj0M9RhadL4CNoPkh9oiUAHUue0YiiA3qBZ3Ddf-ndqXF2Ec1gMTlbQni-VZ67w6r3RAKNi5TniOhhuXFxdXtBJEK_MPshmITPQ7pAOPvE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=L049S-45q5Ov5cuS330g3qXmIn-6KKhKrABf6t84_SlBPHfU5iQrJOM6WZA3XS-UhBCZjbRS73SXlI1-K517hYOOu4kTNg9v5qeZqEZxTvsgqEiwh31gnd34D1x6LHmApRE3idD0RrdYpDUaVljLONv_346_9D-tEIurkIyGRz4Hp6W8NyN1t4q_QCI5luVsIObt-WEA0b6Ouin1v9W11HniAuenEUj9QgJGifHCdBT0AEi0KVUibyVHvdwzbnO-AQQt9JFTO4kSMiQ_7pmySR24er9eC6Wd1FzrzK4Dqwfl8OE5AAghHud0MXpQEDWxuZGFhrqA0sP1RiaO8VK3Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=L049S-45q5Ov5cuS330g3qXmIn-6KKhKrABf6t84_SlBPHfU5iQrJOM6WZA3XS-UhBCZjbRS73SXlI1-K517hYOOu4kTNg9v5qeZqEZxTvsgqEiwh31gnd34D1x6LHmApRE3idD0RrdYpDUaVljLONv_346_9D-tEIurkIyGRz4Hp6W8NyN1t4q_QCI5luVsIObt-WEA0b6Ouin1v9W11HniAuenEUj9QgJGifHCdBT0AEi0KVUibyVHvdwzbnO-AQQt9JFTO4kSMiQ_7pmySR24er9eC6Wd1FzrzK4Dqwfl8OE5AAghHud0MXpQEDWxuZGFhrqA0sP1RiaO8VK3Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=dPNBQ9oLuOi7CswlrEYEsh8-B2zIsiAheUVx7us0C1S-pZoXwssdWcRGfTENFmA2yJZ8Dc_-rcCnOGSZsbx6HhLDbQMm07UHTVisw0kDQdEK1-7cywGhXQbEkjFWwaw9PlVZVJtYdVR09054cEi-CrS8nJu1a-V9047PxhpvQc7p9J5BrS0vBWXwmlbNxbKUmkj4b9y88twDYbMM67Ay5zcoPLsGSpVy95xHWLz9QyKNSoq1c_wLeZneQUa-h-K0qDwHgWgAinRLPDXHe0PQUxLl4YRTAPRq1-Hyoyq7zqFWD2yNqGHUe_nDZk1jkuOPCQvhAg4g0HJrf4Q4l69dNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=dPNBQ9oLuOi7CswlrEYEsh8-B2zIsiAheUVx7us0C1S-pZoXwssdWcRGfTENFmA2yJZ8Dc_-rcCnOGSZsbx6HhLDbQMm07UHTVisw0kDQdEK1-7cywGhXQbEkjFWwaw9PlVZVJtYdVR09054cEi-CrS8nJu1a-V9047PxhpvQc7p9J5BrS0vBWXwmlbNxbKUmkj4b9y88twDYbMM67Ay5zcoPLsGSpVy95xHWLz9QyKNSoq1c_wLeZneQUa-h-K0qDwHgWgAinRLPDXHe0PQUxLl4YRTAPRq1-Hyoyq7zqFWD2yNqGHUe_nDZk1jkuOPCQvhAg4g0HJrf4Q4l69dNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPQUC0SIln-GBvTVmri-YP94KUOkabvqvb0Z3-Skzj6gWt_tCbYWMeobfqOVnZHS0SCd0Pu9VeltPDouQv_p6uBHRTrBeHg7rZys-7mGW77Zu7m88QMmDDbGJSp7Ey4Qoj87Yoi7LfXI1fkQQElC1E5Aj2hDizMnABaTukk19rVYC_6vdMBmgPbcJy9FIPeUa4tdnB68LlB1gwuJgPPiPcdUvGqGC0P-uvxscH8YJQFE2fbt5JSoKYHfOZuXUqJAdPmSjpibTzvvF0vSM4Qw6nOWzZkYT_xlz1HWS4KybqAtVpAHLxl6b8d3F2xKYE3i7rcdM4zgWqLFF7srFYQq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OErZ6O-Dl70n6b8KG9lEu-DQLIyjsafbwZrOJBYYykNUOcD32G06c_bSsuJfz2ZCoeOpLkuUnuy37yxlFO4utc6bhxiElp31H_j2KBF1zXxGZ1_EFfaKcrUZ6rDT5FmSL-Uz_TBScrvLNBj1nPDKSCaq8v-5-h-bVEOdTdKUQ_lfB2CyqrXPoiuep0BiJ7kWlqORBo1m8XScHdSurM9OsqpSLL94L8E0q-FLfwipt56zg9GEno8xky42mlFjxb2vIp2lLF9oNWYu_24tTwWOBCJttKfRI2rkQi9gNRUZ8hjNa8Q5ISOhpxQyOmYim55gb8d5w1MT4YVWMFoiWsPPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwCNUYBmB4puuyDZ5eSVpDojEb3Y9vIr1Nf-R-4xIoix18o4wCtF0bD0X-4nUv2UqVOT3bUgP-1YDVJh8XufWaAarzUNboUBcay0r0htogJiMtQMEoNF2_ocJ1R4NbN0O1lS_KenomVdArrcBdf4XNqX3bwVaiOV8TZkEMmpQrQtL1V_F17MpRhKatVvI1S9ctq4vXPI5tm6xPzUn9XcYMncl374thL0U96QvpUYeEWUGY9UkGOAt_TkUwaNCpSYpANQM1_wq6JjpZXlVSDTQTo6n7a25Vag78Eyds4VkJxE-M1hBvRU5n3Wa38-IciWSBVkh1IkXhGzICZ1EbutfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMfe6NXa7Uk3YICrvNWZgwOCZLtV3iRtoAPRJn0S1QAR_gIC9AeAq-851tn6hNr2rbXMvVvFHhcdeNbVhHTcqjnGp7i5h3Z3tQN8pX67d2jEnO4LeQQyoS8vpJmQLf4_j6eEqvutjLjT35iaMOS4CUzrj8dWWDWBdSJNO7TPbJQLCHczfXWoZfdPGF1OHAzxXQCY0Yw_EHyAphJdg3kbtb-1ddsjLTUaopM8gRnYTrvFS5c2psYTPvvAyFxGmzguL9aVMcq9_CZ26RdUKxv_04lEr683rFmoslPucwIoe0BdnUrl2m1XU50GkqMKFIX-p9lw2MAUGsx2oYkrkF9SyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=ubacU8RmFCERVPAaVC9YiorjaR0Fr3km2VErD7pFOOfxhBM6SQdiVsMKJE6VHfXzCkwZh6sAzaBThjkrDAhwVjxBUdgDHuyPEzpu8wJM_okJHmXhzfjyWxKdmx-M-FcZwJ-ZV0d8-q1JVLXCDvFgI3OQ-0rgrZHJLfek5yzDWrI1Up2eRU99NasMdeHfYbTxFmWP2W0UmFKR5eUnoZJdL9bDPgwLWu0MziWAmEgpZLQdqg0ev06VwcVkwVWuoEdU7DC7SXycgyfNJcAImUTTYfPDi4nkr1QSfLfgsKYg_GHz6C4OkAFBO2Sltt0Um_yi645BuP07s4jLetE6h4XMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=ubacU8RmFCERVPAaVC9YiorjaR0Fr3km2VErD7pFOOfxhBM6SQdiVsMKJE6VHfXzCkwZh6sAzaBThjkrDAhwVjxBUdgDHuyPEzpu8wJM_okJHmXhzfjyWxKdmx-M-FcZwJ-ZV0d8-q1JVLXCDvFgI3OQ-0rgrZHJLfek5yzDWrI1Up2eRU99NasMdeHfYbTxFmWP2W0UmFKR5eUnoZJdL9bDPgwLWu0MziWAmEgpZLQdqg0ev06VwcVkwVWuoEdU7DC7SXycgyfNJcAImUTTYfPDi4nkr1QSfLfgsKYg_GHz6C4OkAFBO2Sltt0Um_yi645BuP07s4jLetE6h4XMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=Xb_eXd9i9xK2R6Il8WDbb9FFifa_lSDu7CB8poC6VYleWkEmb9f5xBAVnyD8ESFFTyBF0g0F0weHfyPPXzZwCfLFUXxTp-BsdEfcl9YkKvfw8SsjP_J7h4D_p2WUvt1WoEyrVWCcBcteKMKXlvjjfQiDhyb5BqZPKLdi0SE8mTH1z1t9QjZt6R2JfUCO2J85OoC1Pm2aMoKjM2iBsNsMruqtb9I8443Wk8I11WKvuzX-MQpFVraXGkWJ6OMJQnfFGX0sdVnjmpFKJWqaFT82h8Oo0oPhr9G4HdSYo5FiSRPUxKcvag0sMAo07j4ZEJINQTQvYk-BlB4pXQ3L9OTSjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=Xb_eXd9i9xK2R6Il8WDbb9FFifa_lSDu7CB8poC6VYleWkEmb9f5xBAVnyD8ESFFTyBF0g0F0weHfyPPXzZwCfLFUXxTp-BsdEfcl9YkKvfw8SsjP_J7h4D_p2WUvt1WoEyrVWCcBcteKMKXlvjjfQiDhyb5BqZPKLdi0SE8mTH1z1t9QjZt6R2JfUCO2J85OoC1Pm2aMoKjM2iBsNsMruqtb9I8443Wk8I11WKvuzX-MQpFVraXGkWJ6OMJQnfFGX0sdVnjmpFKJWqaFT82h8Oo0oPhr9G4HdSYo5FiSRPUxKcvag0sMAo07j4ZEJINQTQvYk-BlB4pXQ3L9OTSjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5Rs1bcjokMDRDj6MRUK2lQjOzsgtaoq5ikcx8JFByozojN1susoYwps8n46xZ6lrt-t2traX3vrtAb2BWH_k9xw2eqeLz6X75qEyH8g4gxW6zf7kWnODxDsOV2Xnszu4_XzobTah2AQ7SzrREYhVsNW_KtVULXFa0dcgsQuHxc8_LziLhx9aO9m55DC4jUVTrhG_n4CUFHgGTzPvR2M4Bi9_7p8imLSspg2xCG2DnHJfpyTEzblAgRARi4D71TsaSj6-1F7bvTQnhZWStQt_ewrLDiyfUYty9jRDADzTkD1pRs2kfJRWgbgWcz9XwqXuwueELHQcfi2DahZ2cmWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=mwA3yr-1s998Gzz_BVP7y-5rDayea_-4fCiEFA1J6Xs-Jl516KCD0Y6zbFv2qbhf1Ot2GsEcEmYls5FLA7LIu1AlHFEUZ-Fcf1f4dKZSBhwR49rq_rfd8Q_N981I8W1ehMA0Pf5mKPrtQ7F6DcB-RyZWlMiHGSWkkr1TbI3KIabkv1aqH0puLb9y9uD50ScP3kS6ypJ5xUToRzf1b6f2RHR61RNpZAw9f6Tc6RU7V_GXpL1Lnak9z_JS3QlyZhnd1xjXlQXRbDtZ_F7HaipgtYo9sjyuUpKKbu8r7TRnO6RBY3CU1u9tgH-0YgLA7tYHQoouT_cr1xgzemNlQDhogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=mwA3yr-1s998Gzz_BVP7y-5rDayea_-4fCiEFA1J6Xs-Jl516KCD0Y6zbFv2qbhf1Ot2GsEcEmYls5FLA7LIu1AlHFEUZ-Fcf1f4dKZSBhwR49rq_rfd8Q_N981I8W1ehMA0Pf5mKPrtQ7F6DcB-RyZWlMiHGSWkkr1TbI3KIabkv1aqH0puLb9y9uD50ScP3kS6ypJ5xUToRzf1b6f2RHR61RNpZAw9f6Tc6RU7V_GXpL1Lnak9z_JS3QlyZhnd1xjXlQXRbDtZ_F7HaipgtYo9sjyuUpKKbu8r7TRnO6RBY3CU1u9tgH-0YgLA7tYHQoouT_cr1xgzemNlQDhogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=dVUWqW4ghKHKA-jv1UeFv1AuZQPhwJEX00JH1Bv-z-ifAb5CJNX5xH09A22AHGSxD4ls1AekFf54WoMpqTeqstO3x60FDFh6JM6Hbn5S73S5AJCWOmzb09-lIhSkPiALC7pnjZf1qCeFiZTraqOanKRVswubRS2F8eUZ4B7hbYjs-mFk8GDUpBwIzG48cTMmRTb9BwAzCOM-N5icnXxzG8mhKJyFOtSYf5Ll40gOcKaVNqZ_cYD23EWU-dg8pauPyBFR3XAjQ5l4GE_dUsRJ9DMaqmoxdb_cW_yC6DycRzGTogaMiWcMkXSrQUN_o8TPVfnPHNNcvKSAvJT0z19Sjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=dVUWqW4ghKHKA-jv1UeFv1AuZQPhwJEX00JH1Bv-z-ifAb5CJNX5xH09A22AHGSxD4ls1AekFf54WoMpqTeqstO3x60FDFh6JM6Hbn5S73S5AJCWOmzb09-lIhSkPiALC7pnjZf1qCeFiZTraqOanKRVswubRS2F8eUZ4B7hbYjs-mFk8GDUpBwIzG48cTMmRTb9BwAzCOM-N5icnXxzG8mhKJyFOtSYf5Ll40gOcKaVNqZ_cYD23EWU-dg8pauPyBFR3XAjQ5l4GE_dUsRJ9DMaqmoxdb_cW_yC6DycRzGTogaMiWcMkXSrQUN_o8TPVfnPHNNcvKSAvJT0z19Sjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWvnmfFdwnvvEuGzU3aMb7svSeXiQ_WdU4ZfY2RLfZZngXkp2gMGzIyEPygk2LMjN8-qNGc-jAXXH3s13sEtswyLzaJfqX-u7bSzfHkn3W6K5ktQJ_DqKzh-T3VruVU7uP-7A04hdJuSvlYPVQ0i2uPXwPM-KHGFBnYfenDW6Kb9XTZbICarf1lxitWxZdweQMaY8HGPgSciM58F-vK_j8AUoPFifUt6MLv-_nRNRcX1tNXjx2P0-wklRqFM4eYVc6tnHHRpO_XEEHTk6i1UwolbSscH_gX9vPBj86KPr5BPtTyumwNQ7uC9GRmfbxlVeO7IRhXWK9kdIO_vmWGbLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=mDrprqhv9WWOctxuuC9RImn2LaqcrVQgQAkHPQqQwgvCxSCpCSW2KbTX89kxKcN5y9kX4L5zvN3KRUQNnX0zkfKQAU0i12BEAwvrLcSD62UqjA_j8twM-t5yaChblVfv4JX2W0IXm-2Fy_UMR7QWY_757d6nzXbsHSu547Hgqqf9O5JmGTBrhSV3s8ffxCgtB1LZrSp7f4iJcWC6tO8bS9qK40LuL5_WRPgILX_mHRBTYneq4yABo9Jz_qqOuYuW51vbFH3qNCuXkaIla49NohddYuqTmYPEV9uGUcyRdCIgNZ_jrGqWyGzWCKNcmBMBpJb3nXT7auPPAROX8sHptQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=mDrprqhv9WWOctxuuC9RImn2LaqcrVQgQAkHPQqQwgvCxSCpCSW2KbTX89kxKcN5y9kX4L5zvN3KRUQNnX0zkfKQAU0i12BEAwvrLcSD62UqjA_j8twM-t5yaChblVfv4JX2W0IXm-2Fy_UMR7QWY_757d6nzXbsHSu547Hgqqf9O5JmGTBrhSV3s8ffxCgtB1LZrSp7f4iJcWC6tO8bS9qK40LuL5_WRPgILX_mHRBTYneq4yABo9Jz_qqOuYuW51vbFH3qNCuXkaIla49NohddYuqTmYPEV9uGUcyRdCIgNZ_jrGqWyGzWCKNcmBMBpJb3nXT7auPPAROX8sHptQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3fe0UcVcD9sfJFnHPdgcxh-vfHUxLam2Def_OOT5NF0lfzwMD2licBM1qf5LmbYgWtp0q5kcDR0PywEuJ6Nd_3BxCQUJKSJbCxD6_A4lTiKC7zbG8QPdc4tDt9z32v9zxLJeCNNPn7hbkJswATY4GoZ-IBkkh9SAltby1KuVHjpqmGoSgvXw7xVajwXoaNnPbKTUFDkkVBu1_7hPj27UQu-St7RQCTEHZbARsrBYibQsXAMg4waBUa3WCTqDhYhYCnR6yiSUU58_WvApaYBrdqAlFGYCE_tvhQj1qa2Qf6FlYeBmK-jHK6H1EPsPq07gKo3UndgW6kpY2yzY3ltEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf-mRr9Q-QCLX16jfA18xsZosTU3-taDEU_CqMFFHTkJO7iBTtxoM0-am9Au1YCIBQVpJSjxVod-P2gFsU_mSq9ouxFGJkp2lL1MWfeF7iFQsMnt_1eeykpXrTAo8lQUSxpw9Opd43lh2VGxZMaKtthJ7I-4qPOZCrShrhf1n35GQCbn4HWTLpQ5RHW_wDbuRrUzTA59fDjUqyps6maVisucukokXWCd2Gf0F5Mt7L4cOIMgIRzDKLzknc6MZHAZFxoPuGMwED91k7hoAOu8LhDYvPOQt5M4JIN6PD1pSUy-n-33yLkBDRQjRYOLekiNOV1fch5fUfOywqah8tUXsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=lYArhL286VtXPFzN6eAsFJyfHCutbmOf_eb8FJ_QLf3yrY1eAnG0NJ_lSQ82fiRAiuUwxypSw2E58h21ibqJlfq1GMq3B1swc8UQzi_wZEz2-DFmOvd24G-o9fdXCRNKMzDDKWPHDsLkHGjt7VqVuhWX73JcUOZYkWEKMGqSYAKCo8JK_x9AHgm8RX0x9T_-dqjxprJcqXWFYBqYV6rdP0hpsJK8JmgcBHVB20c6ezMqOyRM5e3nIVGN3IPA5A8DN2BpuF0O_2ClZTQwd_DTKpLm8Lmf5DX5wqqbvLMc2450Fmx6umjF2en6T2Rpv5nwzPUg7loBu6QKIKE_SOj_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=lYArhL286VtXPFzN6eAsFJyfHCutbmOf_eb8FJ_QLf3yrY1eAnG0NJ_lSQ82fiRAiuUwxypSw2E58h21ibqJlfq1GMq3B1swc8UQzi_wZEz2-DFmOvd24G-o9fdXCRNKMzDDKWPHDsLkHGjt7VqVuhWX73JcUOZYkWEKMGqSYAKCo8JK_x9AHgm8RX0x9T_-dqjxprJcqXWFYBqYV6rdP0hpsJK8JmgcBHVB20c6ezMqOyRM5e3nIVGN3IPA5A8DN2BpuF0O_2ClZTQwd_DTKpLm8Lmf5DX5wqqbvLMc2450Fmx6umjF2en6T2Rpv5nwzPUg7loBu6QKIKE_SOj_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=oJCF1zcriVb_KuQRiCS3HU9bzC8etDVCiryQy1kOYUo7F20DHYL6LT4oh_YLNHuW6GFs-jhV9zF5VmBFP5Krc-hb8r4BIpxk5eCQLF5K6gCZd-d3iWj113GtiD78RV3_e7oq_gD2wlC-ghRrcqi8a5O2rG8gMV33O9foNVivNMCSHDtP4MYHfGNHJ0qCpryjoEu7wN7gjHnBeGbQrLfPGc-Iy1oF709FXZP5n3D3AiveQQZjOhaLfg-3bvWk4dqGDI_qRi6b2twffpeAwb2a4lrpjd1XexZW_0QjX0qIHwzDQ_Gfqppdh1dYTOBbzbyhmkU40ivbijQ4JFlyf6Tdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=oJCF1zcriVb_KuQRiCS3HU9bzC8etDVCiryQy1kOYUo7F20DHYL6LT4oh_YLNHuW6GFs-jhV9zF5VmBFP5Krc-hb8r4BIpxk5eCQLF5K6gCZd-d3iWj113GtiD78RV3_e7oq_gD2wlC-ghRrcqi8a5O2rG8gMV33O9foNVivNMCSHDtP4MYHfGNHJ0qCpryjoEu7wN7gjHnBeGbQrLfPGc-Iy1oF709FXZP5n3D3AiveQQZjOhaLfg-3bvWk4dqGDI_qRi6b2twffpeAwb2a4lrpjd1XexZW_0QjX0qIHwzDQ_Gfqppdh1dYTOBbzbyhmkU40ivbijQ4JFlyf6Tdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrGwV6ir7PDc-sbFg0XBoFij2KhDy6xVGqweC9GNnwPYwMkHxE8Y_Szcm7dYaTSp_XZ2NhpYOHT_M7JAIdHckyl0RVvBMGF5uMrI8ClaV_IwEYoITqbj01bok4zsrEGcA2Mnc8_w4zuoIw2igMwvfS6Xu-Lii1CDtFH6kx2J-lZ2dysef0w3zFgENdGRenqy3mhOrbbvMLUllU0wz5EH6GDp6HdrSKQ2rARJWtDY0mdJkPAY3SITKQJ83qjZb3evpS9h6xE_87iDvTDpk6YYRjEg6ZzN1UOmTipSZPDjnH7SAM7ej9_s8JPwCUM7lFeYhfTKPjENb0m29bYLxN1evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJtm4qkcapYO5kM3Bf38IX2dfZbidfyQ3EobNhKmiAwPpRJkERPec08MZW-n2uzW6LX-gKFR_dlpROmktYn1UJGyEthHxZ2_RONm1C1eb65qQqL3v_nNnjCk4X5QPEgA-6r0rpV_RPTl_CZqAGAHr2Cf_7MI8YRzj_uxsmlM5ru2WZbpDJG-AD2LANWADONfsPc2TkQhiNG6KPlawiKElJUkFzWzfJbeQzcime2ObKKL7JOOOhQXwKtHGCtkM-Fe4pyrB69vnA6P0cJnfr2XauyEG5NS7aFtwor5O8zdqrIxWXpjY7Lt41auP3w2Aj42veyDnI3Vd5iNxNDcX8yDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=LD_c_bvqLlRvdtZvPhcEzfdbVy-Yp08f8lVkMgxk1RodEm4FNQYxq8CW01zwjVeBOJUZbJlXMsfqJ9t0FbbwdBgvadgxUi3UNB1-coBmaf9CmHcydIQNMsTIEdw0eg8Gbba7ademBFVG3pH_6FjNv-lor6hvQ-ObX7OGkKI4-IFtkA5kWgz9hUi_6HmqpA8GjtH3eSBRww0KZhlPXhwS45530LZa53EVQOzzlmRi6k4PSLWopAa17Cd3iUYvyxdHfZVFQ6OL7P6pg776XRJtDnijfUKhwhrhakbvNykYw7y008rTYiEb0rG48QNuf1Vr-VgGL7jWR8VGhWlDrkznNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=LD_c_bvqLlRvdtZvPhcEzfdbVy-Yp08f8lVkMgxk1RodEm4FNQYxq8CW01zwjVeBOJUZbJlXMsfqJ9t0FbbwdBgvadgxUi3UNB1-coBmaf9CmHcydIQNMsTIEdw0eg8Gbba7ademBFVG3pH_6FjNv-lor6hvQ-ObX7OGkKI4-IFtkA5kWgz9hUi_6HmqpA8GjtH3eSBRww0KZhlPXhwS45530LZa53EVQOzzlmRi6k4PSLWopAa17Cd3iUYvyxdHfZVFQ6OL7P6pg776XRJtDnijfUKhwhrhakbvNykYw7y008rTYiEb0rG48QNuf1Vr-VgGL7jWR8VGhWlDrkznNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=tk4HpbgFRxtaGD1QAh1qWZXu1SMiwGZ0ufbMti2riDn_MhfR5lffVJ3XQ8dK8fLfM99pFbfSqOCqjxA9eEDaMIdEPEQWL51K5Ri4rU1KV3GIbp-O-ag9VFNGBL8jpsFe2gGvXi5RxinwRzy7kNnH9o-JaR81UdiVwrZYR-uUnv0gb50lrXlRwMadfQ6ZUl6v43S8DJWA8WnaNz8-W4mRlsqafLFalK8ak8k2t2DueHFhfy19AMFPKLDjsv_C02pADzvAPVRlQpNcJgsG4UmWbEz9wDP98URjTcVAa1q4aOaSLa9RjfL8QOMmVyxz_WtyVxvj1wkIyZSU44KpPdF_aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=tk4HpbgFRxtaGD1QAh1qWZXu1SMiwGZ0ufbMti2riDn_MhfR5lffVJ3XQ8dK8fLfM99pFbfSqOCqjxA9eEDaMIdEPEQWL51K5Ri4rU1KV3GIbp-O-ag9VFNGBL8jpsFe2gGvXi5RxinwRzy7kNnH9o-JaR81UdiVwrZYR-uUnv0gb50lrXlRwMadfQ6ZUl6v43S8DJWA8WnaNz8-W4mRlsqafLFalK8ak8k2t2DueHFhfy19AMFPKLDjsv_C02pADzvAPVRlQpNcJgsG4UmWbEz9wDP98URjTcVAa1q4aOaSLa9RjfL8QOMmVyxz_WtyVxvj1wkIyZSU44KpPdF_aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=VI4cc3NSik3yI_CNCNSSU7JzHpntNSHKqRXJG9DeQ6bgSwvzUl_WaEmbuvXlXyg4OMngmN_iwjzHMFIv_4msvxhfXNyhMM9KKCvg9g1ABxIl3krrjsTfF-YDnF6SqH6y-fqSW6-77_b74QhllEGLfSdlNtObQ0L77s_BMgAuZdd5ytXglN78KOrjEA3xpN3ZS6wigxobHgxZS5ytqcmiVT8dQ_WLzZx1U22Cl0YyA304FQ1NgOZxi3s2lctdqHuRYq8NLuL9B582THJTbKVwrJOZsXmbbl2Ez-Jgr9Coego_clnLL7xpRK6W_x5hI5f1Q9eegVsv1Xp7T2lg_tGadA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=VI4cc3NSik3yI_CNCNSSU7JzHpntNSHKqRXJG9DeQ6bgSwvzUl_WaEmbuvXlXyg4OMngmN_iwjzHMFIv_4msvxhfXNyhMM9KKCvg9g1ABxIl3krrjsTfF-YDnF6SqH6y-fqSW6-77_b74QhllEGLfSdlNtObQ0L77s_BMgAuZdd5ytXglN78KOrjEA3xpN3ZS6wigxobHgxZS5ytqcmiVT8dQ_WLzZx1U22Cl0YyA304FQ1NgOZxi3s2lctdqHuRYq8NLuL9B582THJTbKVwrJOZsXmbbl2Ez-Jgr9Coego_clnLL7xpRK6W_x5hI5f1Q9eegVsv1Xp7T2lg_tGadA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=sAbV6xT_tmyDBjOE65lnfQm4H4Wc9doalHqsmFBBvW9fEr0tiQ-5yfPd7jtk0q187tJ-zoLZ31bVTZ1QAvQH9UaZ9fNc1UD23dCy7m5UHsUVt0id6kh8xJH-CPE0foEfrPEuWoFn-7wlOCqD2cVzIQl20gR5jS8HlG3KakD69oFbc4OrvupFDq1Aly2F5nO0ye5o2bqqbaGDwrvDTRIedTxpS2DzxMs4OUel0A0ylm6hGQxtnd4ONcNEdZXKnS5tsHjFTHLJOH6zeIBY7uoHQKfmwqZ6nKAvlykbPVfFvk8zvI_AR1_FaTaSUVyCJ6DX2xksoqHu36mhWVslP_NFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=sAbV6xT_tmyDBjOE65lnfQm4H4Wc9doalHqsmFBBvW9fEr0tiQ-5yfPd7jtk0q187tJ-zoLZ31bVTZ1QAvQH9UaZ9fNc1UD23dCy7m5UHsUVt0id6kh8xJH-CPE0foEfrPEuWoFn-7wlOCqD2cVzIQl20gR5jS8HlG3KakD69oFbc4OrvupFDq1Aly2F5nO0ye5o2bqqbaGDwrvDTRIedTxpS2DzxMs4OUel0A0ylm6hGQxtnd4ONcNEdZXKnS5tsHjFTHLJOH6zeIBY7uoHQKfmwqZ6nKAvlykbPVfFvk8zvI_AR1_FaTaSUVyCJ6DX2xksoqHu36mhWVslP_NFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY3au0sQEx-6KD5It5X5M4tnfGP_oOSv4JMdFA-Mny8qPgC3R-Szi3MTbL6b4upZHM1FRGEJplnPlI1gjDdKnpdKKYvJoNHtVQXbm5WEudJ7Q2iWk8mtoLDey2g6IwOEdFg3NERP_Q2i9_2TTWBUKfG_gMhe5iX6kXSDqg7tYTerXcPLtCELDy5yncGgFpCPv_3VTpOO0v_j6JtwO_DhU3_Z57d-yVTBAGrHT6EgI1Zu1JYaZIryR5eti6Zgrd3CDkXt633on9poN64XcLsRQnP111hEeO3fPXXMJBbJ4hvZHuB0rbOduKzb36zcsHwqjbgjecrvnKphWinrmHL-og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=kBozWwRp8E7qczbwwCIiRK6fad-A6Q_H8cYPN01vLk5etiepKeZhd7w3voHFvm-IWXJwo1HgdN5twFr2uLDHhNAtIfddGPKWYcbei75gyxHIxJgQct6WktkekOI_3VlBT03oFF3QxH4zOTTpS_6cw0Xg2HCbNYLuoYtcLtPeqRj2X4LWUJIBRdp7JL8os7NNzrAxEVCA_VEHENtrooNnfA-sBJRyssFaXcO6_1atyuy6cYmKJZ2euolRdhQ7kalSpG6umQMaPoVlTKR-uzF7zpr9SoTmwmJgPmjyJ-9489u2fGHkphJE0QjyxEg5I59gH6aCyTREZb5NVkdscA4x0TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=kBozWwRp8E7qczbwwCIiRK6fad-A6Q_H8cYPN01vLk5etiepKeZhd7w3voHFvm-IWXJwo1HgdN5twFr2uLDHhNAtIfddGPKWYcbei75gyxHIxJgQct6WktkekOI_3VlBT03oFF3QxH4zOTTpS_6cw0Xg2HCbNYLuoYtcLtPeqRj2X4LWUJIBRdp7JL8os7NNzrAxEVCA_VEHENtrooNnfA-sBJRyssFaXcO6_1atyuy6cYmKJZ2euolRdhQ7kalSpG6umQMaPoVlTKR-uzF7zpr9SoTmwmJgPmjyJ-9489u2fGHkphJE0QjyxEg5I59gH6aCyTREZb5NVkdscA4x0TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiW8nCpekEInci3KUmo4ajDyU9xycuFu05lrebO5ewpsg0O5O-NbmhkAt-jxh3u-5AI_bdLaKEv3YUqu68UMkGjhQmT4F-YJwjX9cxQT58GHZs3kUhQQOhQA1cE3C6slkE1SQAapqFQ9ianxmqzuNx5rTs1eDVbEHx59GG97ZnsziLCwtcoxNnSSSerj-ocCoVsJH0Ba3OUKb6LBgKBSkdbbQD74Og7xctI7sBTK5dvsr1aAoMMEJU2Hspuhbm4Pp75I_Te4O0fhJbyriaZqpAlNmb8BcfICVEJnCQN2YGORJHEbyrpzbrL6NaWJrqPFHLu0bxTQKtTw8w77NqPbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=CawozJjeLTDHZVXZnItfJtgWxYiouZ4Otb0tI9mY44NaMnUsuITIOuqfF1Fta6_eas-d6Nn8t9NJm6XJihfFiIwT2fMROnBZvX0jnDijdILSN7HGug_ViROIOZJzPDFXK0WbxKaWPjAqHyQQXub7wyo2g_J5CPKE9YhNWnRtfk7ND0jxQPfqLzWbQzmu0hLJ6ruCiFNR5ou2CS1wwSThL9AOKDD4FWp0FnsLO3eoM0ZrqemkqosLFz8_KkfOaBAKdlyMmwEc7p9-IfSGzrI6TjMdaro798A1ajRvgB_ZwF2y8bYeEBQpy9R5nxXDrRxpuOqsB9-ZxFLMxCH_2LZysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=CawozJjeLTDHZVXZnItfJtgWxYiouZ4Otb0tI9mY44NaMnUsuITIOuqfF1Fta6_eas-d6Nn8t9NJm6XJihfFiIwT2fMROnBZvX0jnDijdILSN7HGug_ViROIOZJzPDFXK0WbxKaWPjAqHyQQXub7wyo2g_J5CPKE9YhNWnRtfk7ND0jxQPfqLzWbQzmu0hLJ6ruCiFNR5ou2CS1wwSThL9AOKDD4FWp0FnsLO3eoM0ZrqemkqosLFz8_KkfOaBAKdlyMmwEc7p9-IfSGzrI6TjMdaro798A1ajRvgB_ZwF2y8bYeEBQpy9R5nxXDrRxpuOqsB9-ZxFLMxCH_2LZysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfzKHmWb2LGlmC9KZKFPV9HuJ6xhRFbj9kPyUXK8k7JW7L8ggw4x54ylk_BYMYjs_-HM4IwL66oJdHuWgp0etl7gmhaSgUOpV-y70O_5ipFJxgEUqQTQoWVNX17qr2jwGfYLZgJfS5txANgYflFkONgeCrQtZz1F80oy6RKdPxFNeYeOX3oNs8jFK-hkP7V6zCyh6bi37xe2dmmwQwGdyKyEYYDml78kDm1PKlXWf9mek7ZFPMPNRBIeDiIUfZeePWm-tOdJoyl2vYCfPbiMXcNlxDvjPuRlMCxl5tuLBYldwYlyWWzq4riBguyTHYwOzajRJWz2R2uYkOTSLaWp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=qeiw1xljoL0TPfG6YcDqvGQfK185hyP7KWiqdXUlc-Vr6TXJKvaXfj0zlci3YiQ3kb0XdfnaRBCXFNVEq31Noljm5_lz-9dEU3VftickPQimn5kiFFWJ8Fba7pKGjSFO1qDGZdffQjR62Q0aTYUoQw1SUK8zuNDf4jmY3eu2tVhGDYZuU7f5bpp-RQwhLHd223ltaYv-1K8bjWVShaPxDTvH5jPKMht6pox3dSDhquEYTfFrGFeJi45OhgVd1orRxb7RX68DseUTqtc9TKeHLTnhiBbMHTCvLxNiecCZyh3aG91o7GJ99gpg1rb7Ac2-VSaWzRgtG-RpGlBdeRtRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=qeiw1xljoL0TPfG6YcDqvGQfK185hyP7KWiqdXUlc-Vr6TXJKvaXfj0zlci3YiQ3kb0XdfnaRBCXFNVEq31Noljm5_lz-9dEU3VftickPQimn5kiFFWJ8Fba7pKGjSFO1qDGZdffQjR62Q0aTYUoQw1SUK8zuNDf4jmY3eu2tVhGDYZuU7f5bpp-RQwhLHd223ltaYv-1K8bjWVShaPxDTvH5jPKMht6pox3dSDhquEYTfFrGFeJi45OhgVd1orRxb7RX68DseUTqtc9TKeHLTnhiBbMHTCvLxNiecCZyh3aG91o7GJ99gpg1rb7Ac2-VSaWzRgtG-RpGlBdeRtRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vshntyQQ0woOOeTxp9htL6HE0Bp2aqfQIEnXTfr8-crd3yCZj_8G4mia0LdOMSxXy0EV1ZzEPZC-1hAxGHmhILf7v0_SXN5L7pTHmZ6JcZSoCvutFkBnHqQ9gS9YwhJobLrVZNIE-GYRvBnr78ZHyP8C0N5yNbMYzLLFkHhofpFoktTiflW5s-us-x-rfqnrQMEDUGthYdxtmYtgD3jdWb_5N26XTx6QXaY4wPPcfnEUL1S-lP5ifYGo4I19ArgQCrIKxnyFJpzPLK1fxVYC3DVAY3az-YF4WIcd-NrEW8bxsQE9jv5Rj3AsdiYm4r23FZI4L5TnwPOmdfEnec7URQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=dTPcjgKd4KNMLXhuQMlrweBa-9DWNnBW2q15Qqn6WJH_QsHWAPbBZTU9DBhjYLTXQztOmJfjGl_ijqJdeSk5YrUMl5SS7AWRK1Vq9uKg4CNGgGgL5o2ST_xNFqG_BrO7QEC9KXz-HCxgrUzX79WyB1PWyLBlk-_7bvZMR-rp2WhHVM3OwM6dQlSmyLL3r5o7Y33DhOZyqhT_bHIEe5SafyoHogbGXWQZ7eIWbOg-LIzepiAl0KgHFSQY6BBwLC04ksWVuzGNhR7qxJaEBJWI7Dvvnd9LnhWrzBoUGF8qL62f_pC30GVzz0dMabGMx_fG7aSoH6mlgMB42b1IsKNFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=dTPcjgKd4KNMLXhuQMlrweBa-9DWNnBW2q15Qqn6WJH_QsHWAPbBZTU9DBhjYLTXQztOmJfjGl_ijqJdeSk5YrUMl5SS7AWRK1Vq9uKg4CNGgGgL5o2ST_xNFqG_BrO7QEC9KXz-HCxgrUzX79WyB1PWyLBlk-_7bvZMR-rp2WhHVM3OwM6dQlSmyLL3r5o7Y33DhOZyqhT_bHIEe5SafyoHogbGXWQZ7eIWbOg-LIzepiAl0KgHFSQY6BBwLC04ksWVuzGNhR7qxJaEBJWI7Dvvnd9LnhWrzBoUGF8qL62f_pC30GVzz0dMabGMx_fG7aSoH6mlgMB42b1IsKNFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=MsXNJaWQic1bA8XWbnm3tKPu50afr6XcrxR8p52o0alOU5T9444CmD9B70p3eRGzfwgQrjZw4KpPtHnXdLANhZpq74BbEnTyT_3HxQljQaBqnnfWyTgbNButzwjKhPfx3R31HsCgTu22ierADLRoHgyLZxLwm34hxKLz7sC0-uha98vl40HH5H9YVGrYQYITj5RrxWG0QHpK22cz_P-cZgLAg_weDHS_E7NmECMCfgeQg7Wf482C4EygOuauvfW1HK0nc2gRwEWzKCddHZXx-PavfmVS9HH5k6kSM9ixv0uHPs8jsfUeiDJWTRYKIU5LUYJMB2dyLncG9b0IbS-6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=MsXNJaWQic1bA8XWbnm3tKPu50afr6XcrxR8p52o0alOU5T9444CmD9B70p3eRGzfwgQrjZw4KpPtHnXdLANhZpq74BbEnTyT_3HxQljQaBqnnfWyTgbNButzwjKhPfx3R31HsCgTu22ierADLRoHgyLZxLwm34hxKLz7sC0-uha98vl40HH5H9YVGrYQYITj5RrxWG0QHpK22cz_P-cZgLAg_weDHS_E7NmECMCfgeQg7Wf482C4EygOuauvfW1HK0nc2gRwEWzKCddHZXx-PavfmVS9HH5k6kSM9ixv0uHPs8jsfUeiDJWTRYKIU5LUYJMB2dyLncG9b0IbS-6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl4i7Yg95mWDX-sJhoeieIldWPWI3lnNaBUluhhO-UTMWi1lQV2IptsW7olcLE7uC4eKhGWIoc2ZiDxcE3V08zi4jxgU6rDJJEipIN7gs3qobnAUHDq3cpACJi9hBGMXnAiLKCWZvraV6_DxdaCJRjDVKQ1mdrpu-qVvekdZNdjPxjrmXvfejRbtTAqB-cVQbuvHS88q0IEQjPW7dH3aw8Pd2N6-QPXWv45mbsVU8VocOXQf5cKwqQpDdcdH43ASjOnqmmLZqUBVq0mTCXQqXKj75aJVQgTG_N4I4ekQLaLzzDa20mg3Vr6hGI64_jbKPsWV0GhV3wegydtB7M6smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=QBvnoO_3sOd_P-b1MRSfg4-mo_2STjlR0gY9F19rGt0hsLzvfZMdtZQvPqfDkx4pGaQlNNkpGPZFgpDtnj7M12Vz-3RrC7XVNDUBynpux1Rr0DSLeacQi88YBFKgwiZb32Hesja4lJl-in5RjlDOiDxn6fCljK_zekfQBbXb5yb2tMZjzX_lC0lkORcSzu4KGWnDwvSmZp2M4JFuXjHQopUZPDzTitefx0rR6YI5LQiLpPkrN-WHormT3Icpg6tbC3uZJmUjPLYy75lU6BuqlbLu9h-6WCQ0YOZFwrybCNCT2ooYnA4gclBNgbZR3jEIyr1_Xw8ZIBE_WJnqYsPJBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=QBvnoO_3sOd_P-b1MRSfg4-mo_2STjlR0gY9F19rGt0hsLzvfZMdtZQvPqfDkx4pGaQlNNkpGPZFgpDtnj7M12Vz-3RrC7XVNDUBynpux1Rr0DSLeacQi88YBFKgwiZb32Hesja4lJl-in5RjlDOiDxn6fCljK_zekfQBbXb5yb2tMZjzX_lC0lkORcSzu4KGWnDwvSmZp2M4JFuXjHQopUZPDzTitefx0rR6YI5LQiLpPkrN-WHormT3Icpg6tbC3uZJmUjPLYy75lU6BuqlbLu9h-6WCQ0YOZFwrybCNCT2ooYnA4gclBNgbZR3jEIyr1_Xw8ZIBE_WJnqYsPJBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=H1WF63kzFXMH7Zuch4R6tET6PXpvmuphmqTtteqyhg8VLMfdKaU8b4_0dVJ3Ilbn7_yp83TWmyg36dY9HoLI4UTZcJs8_gpbBp-rcZMp6JqrsRn6o_DCWujg66cIIFx_lwi8yvzJOUJW_f-np6WnewIGz678wK2E51j56Fq7i1NfkSZDCg-DiC7zR2lhPsw_QdOJwol9GEsEHjkj5OVJNlsKmsIaQAcScojD-lcUkJqtGt-AXaDFjrc7T5H_StUuWZ0znLdsM62IWMBsXBV6UOF5RI2E6gwlVaK3yjfuO0A1S2g18GsKLhntTWEKZGI13a_6JzqHoQgquqcJpY9DDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=H1WF63kzFXMH7Zuch4R6tET6PXpvmuphmqTtteqyhg8VLMfdKaU8b4_0dVJ3Ilbn7_yp83TWmyg36dY9HoLI4UTZcJs8_gpbBp-rcZMp6JqrsRn6o_DCWujg66cIIFx_lwi8yvzJOUJW_f-np6WnewIGz678wK2E51j56Fq7i1NfkSZDCg-DiC7zR2lhPsw_QdOJwol9GEsEHjkj5OVJNlsKmsIaQAcScojD-lcUkJqtGt-AXaDFjrc7T5H_StUuWZ0znLdsM62IWMBsXBV6UOF5RI2E6gwlVaK3yjfuO0A1S2g18GsKLhntTWEKZGI13a_6JzqHoQgquqcJpY9DDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=VSsEXlPNlJjh_PFaTdwCRH1_ahcN0hiesrJcH2d3t0fV5cJY8ivKsaoqoUI_S4YHxW2KK9zNZur3-HuTmL9D0nqeaJdhWQ8PU3333BzmBQo7ZtX7GNcidB6qGp9ONGdwTCntLhTN45mfi0-RnC-94uG5eneZKTXiP13Mn5Fj9-Rq16jECokZXJbZ-vcEtEiV-DjeHHazpfbAJggcrdM--GlcFkveirzqs-kcdvjOgF6ZH-I1Adu6xDtWJ4CvJOgnpRuZ75LqMM4sQsvpueR1UD5xr90Oqct5KuQvMy8jafH0Hr0ZK8Pr0XHTOQUD19u44NK7S-NqEc-q2dWO2UDhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=VSsEXlPNlJjh_PFaTdwCRH1_ahcN0hiesrJcH2d3t0fV5cJY8ivKsaoqoUI_S4YHxW2KK9zNZur3-HuTmL9D0nqeaJdhWQ8PU3333BzmBQo7ZtX7GNcidB6qGp9ONGdwTCntLhTN45mfi0-RnC-94uG5eneZKTXiP13Mn5Fj9-Rq16jECokZXJbZ-vcEtEiV-DjeHHazpfbAJggcrdM--GlcFkveirzqs-kcdvjOgF6ZH-I1Adu6xDtWJ4CvJOgnpRuZ75LqMM4sQsvpueR1UD5xr90Oqct5KuQvMy8jafH0Hr0ZK8Pr0XHTOQUD19u44NK7S-NqEc-q2dWO2UDhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=jfbw3YzJD1dPPH9bcZjb2J7RxiF2oPTp897XNi5Qc_BJ79WN1tNuXd-tlY0N3F1DX39rNtP-B5iQy0Dco6bgg8A6rBR88BfHN4bFnYo7CUslVSJ_McDDroGvY0_sa5La20e2rz2WEJ27UUnniNEaI7n5ZefrVscte4049CYTQXEzCltkc4rJiBCUFej1lnAuQ_IeP8KbW0zohSbtWxm2dJ-tSflj57KPrMbkFhefgmzTxIr2Txr74z3YyVQYTaXrHUsGDxaFFM-blw919ai56nt8rG_jh89vTM8cN6QlEWHYZPhkJ-oY3IaajN1mQkDHNMuv2BzMGBouRkyN_oVcGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=jfbw3YzJD1dPPH9bcZjb2J7RxiF2oPTp897XNi5Qc_BJ79WN1tNuXd-tlY0N3F1DX39rNtP-B5iQy0Dco6bgg8A6rBR88BfHN4bFnYo7CUslVSJ_McDDroGvY0_sa5La20e2rz2WEJ27UUnniNEaI7n5ZefrVscte4049CYTQXEzCltkc4rJiBCUFej1lnAuQ_IeP8KbW0zohSbtWxm2dJ-tSflj57KPrMbkFhefgmzTxIr2Txr74z3YyVQYTaXrHUsGDxaFFM-blw919ai56nt8rG_jh89vTM8cN6QlEWHYZPhkJ-oY3IaajN1mQkDHNMuv2BzMGBouRkyN_oVcGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=jktdt67ttJeJg2ZQ5PQo_-2kG_IGhC8mcJX4BiRAdb3e_JbIixpbO0KHdksRDn2JOewW5C3Qo2By_HMH7nRTmeoB4PTtVhdYzIzf4lCUiwszx0wRhOMOjq8iNmGm6sBpdFuF8P3TJzc-9ar0h5T3THLZI_VFLHyAMTh9ciYVWTQ1g1aKtJrewuX3b_nAiw8gTRBGFun5ZWlVwS73R1tTQjNc1P1yPfedGXMkzgDAghmFbaE4-TIPjHjvz0QSm0LXMXCm9eXWH-Y1C-0Z3SqL3sSqdBr2RJ6I6m-PBjHYlaPajgfxfTBg8ZbcretqL2i1_DpE7YAlGmHSBi-tCuOb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=jktdt67ttJeJg2ZQ5PQo_-2kG_IGhC8mcJX4BiRAdb3e_JbIixpbO0KHdksRDn2JOewW5C3Qo2By_HMH7nRTmeoB4PTtVhdYzIzf4lCUiwszx0wRhOMOjq8iNmGm6sBpdFuF8P3TJzc-9ar0h5T3THLZI_VFLHyAMTh9ciYVWTQ1g1aKtJrewuX3b_nAiw8gTRBGFun5ZWlVwS73R1tTQjNc1P1yPfedGXMkzgDAghmFbaE4-TIPjHjvz0QSm0LXMXCm9eXWH-Y1C-0Z3SqL3sSqdBr2RJ6I6m-PBjHYlaPajgfxfTBg8ZbcretqL2i1_DpE7YAlGmHSBi-tCuOb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=Pfgnx23akPsIFeI6O4IwfwYhtBBGEPozZJ-6-VP9HI7VOuAia-8Q3u6AD6MBlEZz8dtx1sKwhp-vKIOBTTaCSOBus53LYyGTLhUdkHQTOITLs4dJSwc97AVUdbniVzdJm_oTyRLm4LV99-xV-cMkEQPTE7YJq9OgZpmEn3IQYYL8WqDLb_mGFlIE1dZUWmsa7omwTmk1qE9O_0PV3si9Drf8K-kHe2-wqJr6JBoIJcq9sN12xnjhQ9q4JIVWAprhY0GwOOTkuc1gkUApqt0X7bgsvAJvtgjTh1I7_o_O6IfFeRMgR3I3rO1eOHrvb7IDj--CAMvESEvyXyu6KCgBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=Pfgnx23akPsIFeI6O4IwfwYhtBBGEPozZJ-6-VP9HI7VOuAia-8Q3u6AD6MBlEZz8dtx1sKwhp-vKIOBTTaCSOBus53LYyGTLhUdkHQTOITLs4dJSwc97AVUdbniVzdJm_oTyRLm4LV99-xV-cMkEQPTE7YJq9OgZpmEn3IQYYL8WqDLb_mGFlIE1dZUWmsa7omwTmk1qE9O_0PV3si9Drf8K-kHe2-wqJr6JBoIJcq9sN12xnjhQ9q4JIVWAprhY0GwOOTkuc1gkUApqt0X7bgsvAJvtgjTh1I7_o_O6IfFeRMgR3I3rO1eOHrvb7IDj--CAMvESEvyXyu6KCgBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghortZLHgvdtB2RWPLb6eq0TOeGgybPnbazV4uBBRgiVVcpNXX51zAptRP-R0TirauPD8Dn9MATkqnRsvEVWsfTq1bZFptUAe4u0svxyL5vHq5TDZOPNJAmA94Oix47fHsRtV0EymJlmzZQ0RQ7UVhp_dybxhi9t8mgSMo6Y4TcYMi-cmmp31UX9_i4QNjzj2ETn5sWpBxNp93Y0fg_rcE5j5iEqsLXp0DaXOwOvjvH6doclxscDB6frmKp_cjgJN4bgvOjBzjXDzzY3-Ysplyot6MbHkRhTWQNictPE3zf2Z133dW2X_NOClFMgk7VgLJT5PEyibuLv_RKsqmjI3zdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghortZLHgvdtB2RWPLb6eq0TOeGgybPnbazV4uBBRgiVVcpNXX51zAptRP-R0TirauPD8Dn9MATkqnRsvEVWsfTq1bZFptUAe4u0svxyL5vHq5TDZOPNJAmA94Oix47fHsRtV0EymJlmzZQ0RQ7UVhp_dybxhi9t8mgSMo6Y4TcYMi-cmmp31UX9_i4QNjzj2ETn5sWpBxNp93Y0fg_rcE5j5iEqsLXp0DaXOwOvjvH6doclxscDB6frmKp_cjgJN4bgvOjBzjXDzzY3-Ysplyot6MbHkRhTWQNictPE3zf2Z133dW2X_NOClFMgk7VgLJT5PEyibuLv_RKsqmjI3zdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=bQFk0H5f79nca9qKDcshhSkWeN1GYzXA4yRBpJvFE1dXwKT8UPhVwE4DhRb_aBsGslF_LUi9EHdu06k8aFJMHCo1M1-NZLcAuifN4X1-a7ggfNtowGg0xU8XQE2UMmTxE1OIaibE1JWMVp0Re8jfzcXvl_8rLLEUl6a631BRDmRpXwuC4APhr6Y8U4jCvzhYoWckWTBxwsX_ZPdf-3Fe02O6b8bNrkE1sLvw9hk-yZA_yLpoed9qyP8pd5GsSkA9zRF60_yQUytJz9JUVB4C70s0-uKNeMBLrXlH7UxwmmaAb5kI7ywc0llhSKdHzx_3ojz_aq58M1aYMgxrxzUS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=bQFk0H5f79nca9qKDcshhSkWeN1GYzXA4yRBpJvFE1dXwKT8UPhVwE4DhRb_aBsGslF_LUi9EHdu06k8aFJMHCo1M1-NZLcAuifN4X1-a7ggfNtowGg0xU8XQE2UMmTxE1OIaibE1JWMVp0Re8jfzcXvl_8rLLEUl6a631BRDmRpXwuC4APhr6Y8U4jCvzhYoWckWTBxwsX_ZPdf-3Fe02O6b8bNrkE1sLvw9hk-yZA_yLpoed9qyP8pd5GsSkA9zRF60_yQUytJz9JUVB4C70s0-uKNeMBLrXlH7UxwmmaAb5kI7ywc0llhSKdHzx_3ojz_aq58M1aYMgxrxzUS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCNg6lomeJjhsbyBk4A__fAZRI__UT3wbs44A9JnwmAC2W1WVm94v7wyeENZa4hHekaOt13BDYEL0qMFW95cmZiKGFSvY0hPOVugqmcU9926eT5-L9nxh2ZyXBsPOet2d_oyjyp2n2ujpPQ1iEKo40pWQWRD8czDir1u14kY3zGGTyz3fwCFSV6Q-DlfsYndJf0l1avfFjEHdp7wJ3hsR8CWfhNPVewbaxmBDu51oZ2j910cSyu9-CMGQEKXEPcDL9mY95fADl-cV8GQn-N9NFcN1007UdfoFUSDk0mpSUhYh19XR-_P9l2Kxrd4HxXCwt-Ub8VSIxxYD30ki2sxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
