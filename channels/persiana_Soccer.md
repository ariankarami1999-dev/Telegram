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
<img src="https://cdn4.telesco.pe/file/Wa72znTc0EAiX1Q8iXwNxy3w_zHlndu3ObAUQKA4MG-C1kxsL0LOidTFuojE5rkx4eoK5p-4radGtz0bUugbut2t5ZPdac8MCaaEXdcrcscvfq5g6x12FMhYrMwru0mYBSbTqCH0GRK773fCkTAlOCeeZr8eSkgYa7zPUD0JbN8fJu-PJSEemJW0YuI45VJhEI6g8774upu0m_4n_AjoMxwmF2MzDBbnATW-2h0bFMv8gljjuT_G4ndRzirxT23jrijHlsyGsxfhaBpoKRjzKyV5MYg0bHvt6yz3AECC994SLXAam39sHucohv69tNOHkzqSK0Wo5oL2u5ziTEMm7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 520K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-29671">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گفته میشود قیمت پلی استیشن شش که درابتدای‌سال2027میلادی رونمایی خواهدشد یه چیزی بین 1400 الی 1600 هزار دلار خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/29671" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29670">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj5nrCvw74If24WdgY8P2FqiUH0nzTazRZZedD9R1zH72XP6VLIy7oONH9qwYWyh6rze4f58qpTpFnj1I0trEQP-f3821qN6mve4OmFc0bKh8a3QuCnNwDIbMy71Bbd38IcEkBZeeaNi9gxj28kmL1DlGCoo6CXcZDMoCsbQKKkjG3EA6FaYMEW9sKu72Des67Ha-0lvh2lzWieQ40hI-sWuWS4uhzuewnApsvrU_vbF-BvSoUj_wCXpK0vDXH-NwMFC2NMUaGJppxQygyPIRTZ5gvDtaS9pBhypJPuX6hGzIwSohoXGKFCuOKi4-Dfy1qL8BcfxWyVoEiu6_EC-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/29670" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29669">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7GnrkmbTVmZyRyukfsC1NcO9OePbo9IhUXv8M2UsSFp5NRq46Cr917wLEXiLP9Z9hB7W82JZeBmpTILkcJLXFjcrwuPRUoAsBlnfN-WUZBARrsJno3DqWBftMFlpbVGbs-Ls5qj2F4SIqOoQAOu81hJEaHPNg7myqx8nXwMfBpg6Anb5GzESUQXi350mg5YRBKaxp3Qu6-RB2GHiVdw5lPFfAjKYAsVeo1uiSHVQ4X6GLdGRInS4YCZDc9XbYPaidbKqC2x5yrrEgCZPq_1SyaKEZrhZYzfSCk7eRO_d3ehQhopfB3f2huPu6wYq9rtZuQ4duF_AHdL6jIF72AhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های منچستر یونایتد
🆚
منچستر سیتی درلیگ‌جزیره؛ شیاطین سرخ با اختلاف برترند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29669" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29668">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKT2DUY36eebBDQMFrKSdDLtbRTsJJyD2VFeeG_r2ohy8M_A97J_bTfA-P66jdP1hDEoyOE3G6KNYKODd32egFOUKBrMTcTa2CUCdJmGy6NnsbmR0xng9P6lukxBnREOUo8lORqE_SOop8BSkjpOMmP934CsHb4AMQx5mJkTT6PnhwgxrLFrywhOA1mXKuPx_-HTkNhPg55yR1_XWcmiHcCVKj8LnY15X1QWXA2hi7iieCpaz_U7AJOUsT_G3aglVy2yvuxw-27UOxKEgkPacg2P4-lcQNyaw7zpkWJ9Maj076eIXFW5sX_jdfyNXQixT6ipBwuIkDwV9j8HmM-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمتراز یساعت‌تاشروع دیدار فوق‌العاده حساس دو تیم ملی والیبال ایران و ژاپن در فینال جام‌ ملت های آسیا 2027؛ نتایج تقابل‌های دو تیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/29668" target="_blank">📅 15:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29667">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز کامنت‌های‌پرشماری‌که زیر پیج السد درباره غیرقانونی‌بودن یاسر آسانی در ترکیب استقلال زدند این باشگاه کامنت‌های اکثر پست‌هاش رو بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/29667" target="_blank">📅 15:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29665">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو با این حرکت که میبینید داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/29665" target="_blank">📅 14:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29664">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mupLnvTcGPwuDir8228zC9bqfjEQ7HpBp6fDZjFMSRwJ7rU147H9ATvCv2vL1R-KY8zF8gZxEOWLnobaBeM0mixMbqXDwXT2G4k1XjejxpYN9U5DmixMmvkXKDGqe8cNQzfjrXpaQ5ECDgIsMFzpIbVsnV6AKSNM876K09QDd-wBjB_BRSwvrm4wMYkwP1-gSKaqb0-2wV5xji3-vaqwghb8bI3s222Ix1qrnmp5x-sFGwe5l3MGgA7RCjUz0YEz-fCNE6gVYrIDynGnO7NxgDnnLShFWgR3WvW_Ve56vy_p8r9Oc9krbi9i2njRPhmMmPyMma8AUrGdn8XhiENWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/29664" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltXbbVS0Fp4Q8IEK0Tcubte5uoBdT-BodLu4Ov15dk5wem79YDhpzJUlaLc1psUHdx9Mf-68LDVAgyL7-KGxV3-QqTEIR-ulGt61n-mUMrn02FyZmgiS9fk2JLOeo6UM2ued4GdJoxk95ATrlzl_g1d7S5nIaf82_IR9jz0W-htWw_52lKW5ugCHLwmgYZe8F-vmJShf1uqIX0jOjPiImSSFWgB8BIUSUf7F1os0GVjI3vaIlh34ihH8xzqC4wuHSxcuRV4VzqyZm_VUURmSvd3Md3yMUrXUkFZc3eircfV5duwSl8zt_dFB4fQ4sPpvlkHwyx8f8hZ7bE9K2Xz2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای خرید آیفون 18 پرومکس در هر کشور چند ساعت کار لازمه؟! خودتون لیست‌رو میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/29663" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm50EgbCqreBxax3o2HlHkVX3T99xrzZKWzeZ4cPVm64Z431lRArKfkGiiASjqOByY4H3ZoERi8RTXD9zfUuAs1anNKABxfqTVQsQKIg8SU6S7y_B1MulxJE3cYBn6Ci8GHqma3EF2fq0xApvI3sD3YFT8T3cfCrVak7F6CbVMX0aSa8GflFNUQssJaDLY2T114Tg-WUG7bkgH5S0sQZo8x7tudPwsYMGZblNc0iPA7laqpnTBRqWNEc5sivHgkHHf-tBjpR5c4z_8wlFrpl99vOyhsgHHjxqx_kR4JDUL9esLSKjxdvIGeacVKKb-ZKHL2flu0EHlRuOo-NsrlC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/29662" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TizcT9Yen1h6mdaOvErsq2vf91gA4MYVUpxcMXQklVX1bL6SrEm22khapTJ-dDtcJVHiWd_s0AAOFY4sVuKaGZscGHienieu4wPWN78le5hoQllzYnC832GWXhmoyXczZDdJNyRLBv1kYv3Gns_fMH0qhXWnaIwuXwnXk2VGQllnJBgPZtEQQ18gtnIY-u1J9GP-y2Vlc6L1a_0UKM0F3PIIX-lXQLhOGsUPCB98RJkGZXHw_s4KZHzLfxqX7-5wG5tx-IAX_i2nfJD1dgUwCX_o23BUAk714Q2OjlqMO2PeWpJZkGVvg81qbal2RC31droZKbQTiux-WyCzar_GkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخورد ناخواسته و عجبب و غریب علی حاجی‌ پور بایکی‌از تماشاگران ژاپنی حاضر در سالن در بازی امروز ایران با استرالیا که بعدش‌ فدراسیون والیبال بیانیه داد و از هوادار ژاپنی عذر خواهی کرد.
🇯🇵
ضمن اینکه تیم‌ملی‌والیبال ژاپن دقایقی قبل سه بر صفر کره‌جنوبی رو شکست…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29661" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeWMmqHfHQcHiL2AJndUit_-kPF6bXFPStmoTw_CqG3imNgbtEaVAWduPR9Y07lvwf-jjVcLzrOW8Lpjq9O3ZcrTa4XR0BEImdWP8vU4ovdpJemzk_1VtGk7IgP2UuKTIS3UA_1kQssdO8I-Xgym4CosYiElJGSt2RezoFT_lH8GXn3ym9ipeh0_TWp5NZpPnctF2sJzEuesvy92T99QYi4p-P_55lRQcidJZtFqc-kggPWRnOi1vrJg6kGD5dhn96RP43IM1YDQ-u6VJmuCJ1mmn0CvBq3qBH1lERst2U6WIBJ8Ewu15J9flJRT4J_6WpXZUGD_yKshDLLN6CDJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29660" target="_blank">📅 13:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
هایلایتی‌از عملکرد درخشان عارف آقاسی مدافع 29 ساله استقلال در بازی هفته اخیر آبی‌ها با پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29659" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHLXi7UKAlQq955pLEKT1107jbIMSX2JCSGpQFU8PmIlHWL4KEM1e0Zgx8hTHssXjwK3VRaSEHcc5A3pxbLusyjNvxF91uoI8615efjaNbqiJpW7IqIsGrM1qluOne_lRNph0mgwhD2o8tUAbwnDKaY8cDnuAP1B5UUNy6E8KfYqlvT25ltzqA9X3snq7OXFU9TyMbAjja5t-tOHzGcAGjcfIloKjflnpGMAQ76Md6q29CTTFMaypZnAmeQBrvkxMQMPqlymA4fjj7aU91yYUsUT7zgV12PnFfcQ-HAkzCDSdyFg8lEOyFaLKVn5WvYhj5hdt-kzD2DwV-aGAA74tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29658" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2018 در چنین روزی؛
ممفیس دپای ستاره هلندی لیون این سوپرگل تماشایی رو به PSG زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29657" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAG8Kf6o5A5Wq1ewDjB6AaXdpnVfdSl-_pJdz8jOs99W8OS8ZVRbQiciaOncmHCo_LJo3r4IcWQ-cFf7w4EEI0T3YsNaWSL9_RAPWPA3cx_FTDo0EhHGysmIjf3-T4QzWiUSNNGfyAW6wHcnNYX57fKmdXQfDuZ7Z6WZtiLfcLUesMQrPovYKJ_olDB5i5fU9bD_hnpjkEkBc0ETeDf5K27nye59brFhB15DBaL5vS2_RCouFLSvLW81P-L47DMMq6KtJTs6t4qK0pvhUnOMM5mLsXCYv4sCTP0zshUd4-lzhz25sZ5GM8Q_4xsoIWdRlr3Kr4mdKeDCnIEUGgytKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
هفته چهارم لیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🆚
منچستر سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۱۹:۰۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29656" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw6dCRyN5VP8GgVzQaHO_0CRTbMeWTAqfnwHZy-uaqca35163K3YyvyhSrmZcqFlGfPjlPjiEiyI5XQ2zuSAvCR0izvnH2OtR-sAnJoHi94Qe1HyoF0vUdLpzptbGVMPIxq-jHDUGHO9_aDE5TeVtmVDBcDwylSQAC1JnsB7UJj0Qfei0D-wnOctQ4NYP2SOeiz43kCEv8-eLidv3o487HE7-Qb5--WdGPbjFV99qvXwYr6U2aBS5qgdgv-Jlq5wAIkYm5rPZ5rOrdx7W-Z6JJ2UOSugBUngmXzEr1H6dNRs3b-kjvL-m_BGhjAnmPs2kNR1xqJxrIPYlnJXBSR9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/29655" target="_blank">📅 12:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6HYrI1vxSeQkKwfkJaC2Pa3fJRgDT3CMyVUUtn82NgN-gqxlU5uw2tP-K0hBm706cnICX2zlNZK3YcAtpGf_vWQK-bgT2uSzevmg0zogLyftR-WkV8CNF4rjdJK1uB_gEzpRSLnmNW7ibc11POM3sroWBixnZg-9k_s6yWfVyxFJZdVjnP-uwQjHMr5osB7uE8EfbkESMikjggW5h0B-D9U9lTQ5rKAsODTh7i4Zm3pEB_lFmAecV-atj-lPeBfcHl-zRb94OLJ1AzgX8MvOJ0OYRxwRKjhdlxMbBrq3ZpU99LH0WUvl5HJepxV1lbW-ZfVs08nf1nh_M4Kfgl6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/29654" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29653">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFxDrCes9JP5OrK7P9ocBUNuuF_8sf9N0fHcbmo0KEXfcbAuDOG9iB9VLWOpDPpqiAL4W3VFZdmkL4AN_y1jD4sSMoI0hOW0kKsO6UiwX59FVyTY-CwGYAoWJNYiNCR5f63x0GXIPGYeWRHKv5jRpbhHpeVuBl2i-98Qlp5Kqbj7XRDUEq-qHPzNCr2GYjoSeDWbUOUNmb1-rRoNkakngSdWFejO8a24yNmVR4TV1XSyXnavZXWXu74BeVfrzWTPUSInyy_M42zLF1ZheGKCXXwVD1CRGEaLtiTkhtosPy_aNvgOvbCPk3gEhsPK0ZW055JrPQuhOvuTsfz-09a0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
#تقویم
؛ 138 سال پیش همچین روزایی اولین فصل لیگ فوتبال انگلیسی شروع شد که به عنوان اولین لیگ فوتبال در جهان شناخته می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29653" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29652" target="_blank">📅 10:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29651" target="_blank">📅 10:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5JGkW2507j5ep9vBAAUnbCvAr4c0AqSMdGqzw8RW2qFfjojuT61cGsDM8X5-uhW6XYWB0cLVPCRpclvjxOt3iSsVE6cHq5yCqOdr3k0tjidD6swT6eHZ4SqyTsRu03DsgBChzhFwq81VmJS0CukFxCK5CN1hQm68LL3Sporx_cNIp5EG34NtyU48dnX_Go_boYUqydscclL8-n8KBl8qTuBaieOyPsAYDb-SdZ-XAm628VU2km7VmV5nPh82Wy5_W1sI1yVPl_wrEaepNYZ6bX45M9FSFUp-I_NA6mDxLD-VNOwPk4LVfU_LdLwPSF3l-5BoexPW3YaZ4fzxlE0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌اسپورت:
یاسر زبیری مهاجم 21 ساله رن فرانسه‌ که‌این‌فصل‌قرضی سانتاندر بازی‌میکنه که در این 5 مسابقه پنج‌گل برای تیمش به ثمررسانده گفته رویایش پیوستن به بارسلونا درتابستان‌سال بعدست. بارسلونا از علاقه یاسرِ مراکشی به این تیم آگاه‌ست و به احتمال بسیار زیاد برای جذبش اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/29650" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29648">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
#تکمیلی؛ محمد قربانی، محمدجواد حسین نژاد و مهدی قایدی سه ستاره ملی پوش لژیونر هستن که در در حال حاضر در تیم هاشون شرایطی خوبی ندارند و باشگاه‌هاشون هم درنیم‌فصل علاقمند به فروش آن‌ها هستند. به احتمال زیاد هر سه به لیگ برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29648" target="_blank">📅 10:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29647">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e42f937.mp4?token=cB54zHjYSI3yGrz7NB2xvDR6mOyMXVOO1RnsiyXwMELGgD9IoMsA1cgZD4E02lb9y4CBVgagSQXOSZNzwYLR6gWrIoU3OBZHw9dhDcOyjyuxHZUtwQssGfQk6Ro5voOczyKfjM3PxM8y-HjtlA9iGtEOmJandNLeRvMeSrVMtZdsOghaSParUUKqZ54lKRIp6COp-wlZzl1v7ZFnlmskP1eIPohSDNr30bEcmMmfj3dQV7G7CR5o1p03hH63HWSxizwjDOS8K9-sZCOtB2wMqbfEd8dEL0PpfPavVCbaIXeUddInT7JI5kTCCw_33QpbGJGoA7d94iyqhIeghPLkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e42f937.mp4?token=cB54zHjYSI3yGrz7NB2xvDR6mOyMXVOO1RnsiyXwMELGgD9IoMsA1cgZD4E02lb9y4CBVgagSQXOSZNzwYLR6gWrIoU3OBZHw9dhDcOyjyuxHZUtwQssGfQk6Ro5voOczyKfjM3PxM8y-HjtlA9iGtEOmJandNLeRvMeSrVMtZdsOghaSParUUKqZ54lKRIp6COp-wlZzl1v7ZFnlmskP1eIPohSDNr30bEcmMmfj3dQV7G7CR5o1p03hH63HWSxizwjDOS8K9-sZCOtB2wMqbfEd8dEL0PpfPavVCbaIXeUddInT7JI5kTCCw_33QpbGJGoA7d94iyqhIeghPLkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار آپدیت‌شده‌از عملکرد کریس رونالدو و لیونل مسی در کل دوران حرفه‌ایشون در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29647" target="_blank">📅 09:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=gl8Mo90Vbeav-c8cHcwq3Pn_NyMijd-BLb20V9pH_njjYiH6U1_ofE9jxrde2MD8EjmvaI8k4rxFLUjcph111r11xZX3lGHc6U9R-scNsNPdT8F04EksJV9w7T8EFZ_vpK_9DxTpX5GHzQa1OpAPBKqnrqQOQFuTiNedulwfRjUjS_ApLBCtH3h2XwhkMqfCEmBby9llr8G2VDakOk_kLJBqzMe1EeyOhkMkhrbyQ-ECCTLaGMptJ5Z7irnK9ht9Z_tQMrzdWcmjVGI0gWbuvgxyH_-tCHBMXZf1br3Csy8tukc_blH0eazjBPbF75wpjIbMjZhwTMQxIF4HjDY8GIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=gl8Mo90Vbeav-c8cHcwq3Pn_NyMijd-BLb20V9pH_njjYiH6U1_ofE9jxrde2MD8EjmvaI8k4rxFLUjcph111r11xZX3lGHc6U9R-scNsNPdT8F04EksJV9w7T8EFZ_vpK_9DxTpX5GHzQa1OpAPBKqnrqQOQFuTiNedulwfRjUjS_ApLBCtH3h2XwhkMqfCEmBby9llr8G2VDakOk_kLJBqzMe1EeyOhkMkhrbyQ-ECCTLaGMptJ5Z7irnK9ht9Z_tQMrzdWcmjVGI0gWbuvgxyH_-tCHBMXZf1br3Csy8tukc_blH0eazjBPbF75wpjIbMjZhwTMQxIF4HjDY8GIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29646" target="_blank">📅 09:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLiqUl8e0VE7_meqnf-U0GO39UY8mmxe_n5o39gKyRkPUhCUO9fPfrLV-2HKgy92CeCxJQ49A22NaPOkRrP3LL_3RZ1xi5AZKPY6TK6eCPbbCXIdIvcUkWe2Ig5tN7zaBdy-i2TwQkm5K1r2kFexZ_mO10p_Sha-WmunAodeZUloH2Ru_eNJJ4ZTQ0DKwJdQlGeGdMP1ow2Y_FxGWk-hsvgKehIgki5Yi31XfaqRuVta9EHMcWZoPCkEwbeDvbVy4Vux-BjpPkp3LD2rlRMc6-iWPqFVdLOnpJmwSKy9HNyS5Gg8NyPUS9vnoQE3bWMTAWx14gtCMvSqSdPDRYATJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWR1ezl5azbA0IUEepBQbb5pc3OnilQYM6c0RS03QaOg73RwPGSUt04PJ4Hd7Rl23qVHWK2CMPR8hnQkzXM55qR_3MJ5Gt2Ac1X4Gqc76_uPIGQ21KRQMPNqJq7I5lMZvrS3j3l--GhycU0jPliMiX_6l4P8c8wtgi-4tJdEzGl5iZdWeLonHdP-MhP4Ifi-XmLpcl7jmislE-LfcNOVHVIzhxweoeCBR81lbRU0MiS5mHmvNArkY-XfiXfeys60k4onq4LrUznWXq2BuSFkVM_BXcn9EdCkga9urAlq2EqGOmub9CFDOCHu1w1CCS-5sVW6CghTrmWMjxkv2oFDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROyy_grIL_iwd-ylw80wB4_JG9pyqu911iALxzTC7a5OhXrQ_VXCOGUuiofN77zBnwIX0h22Iz5lI0IhmagbBDw5zKJWrNLWdY7dnPmKG-RNAPYr-Q7mdoSSEPJHkwMdbpslrMaHXloA64okVOSLjW_ZWzZUpm-9oz1BDpFvHbztj63zMNCvmLrM9-jBzzJIPf1hRUvdddoRztd-P-bvuTymTwFQkUmGmMxicJhCe5YU7Y5djBNMqj3EG-bNKYcX1XwKYKd_8lNAPeaYgMhrdNdXaM8uXviCxvVzbQOJkWSSnFCgHzsmMj0EBPEod74I-uBKvqZm8a2AqOIPXGhNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJKc20Lx7O5GCX1PGycQoHHc7V0w7irI8H8zb-I6OCSAjy7GqZnXFIm0yTzJApMkoGMxIsrOv_qqxlci-yJB-qtDL14jU2bLSVoBp4H4p2bu0rzOBouzTvOZvxIruYBVjr7TJxVbT6C1p-eLcP3dds38AxdgXyZTY-OYHl7IXly5DcVfg1g4nPd0BK71m1CDv5MxTEad0mqkjKk-75h-fce-X4T8Lcn_wPH1QvX2CclvHSW-IvAyapVH7Q9mjnCo-BfDAgmavGtZMrHj6L9n3VqdRk2-Mpu9eryvprwYh8BCdWyd_6Bn3Z6rrPDYDR_rXwkPCuxaUHCWTYZHaA0t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=YnnSDhRCydSfDv0QbA31wwyHgG-NKj2OZGSDl_AXDi5oV6-8Xn0v-Pc9OlLTykZKibbr0TTz3NhZUElFiXAKeM2QQK5k7-7nzjQbCamUrn5GDGWqolAzrmIsqAJYQ7sFPAFkaW_vSz7ZZo2Xb1Ft1t0ZaZvu7E12sQ2pHC-liNueu9nxMVMUZf1beeDmUYpiWq-Gnk53VV0DTWRUb5x2r1Z7izVf0eCAMxrp6UCgzgIhZ6WQP7mikSoi2WYmwI0UFJ2_eFdK0ZdsA736aNsA4VEl0X5y4K6Usly1SfSAY6k-ilHpKML3boALFwd6a9ftBUIs6CVDj7c7IPTEVvB-xLoTqTvl37svD3uR7VFAndKQuXCuGEptj3coXOoQ9xUhPkC76wc46lG28YyWMCZpa6eoPuZijZvJwlqA-brEBR3Hvny2vKydAAWLCV60UibQfDVl-wpDfPFrqvDG4ndDV5ZaydLvg6HzG-0mY70vpqVJNAAK136rQMIkEiYXrb3CEeSS89boTvwLh8Il3bzrp5xG7scvKEpCyL-Q8qafwOS2aUFTBc0bLr79lxBNJ4vhfST0AGm34hskPn5NrinhFNV_FknR1gTPMzVSda_RIvF9ZZB1aSDyoDrNsTCvILyUIJY9HYPmiLh1Ovr4SULdEc_wCGf9oHn9A2TE7zW4IxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=YnnSDhRCydSfDv0QbA31wwyHgG-NKj2OZGSDl_AXDi5oV6-8Xn0v-Pc9OlLTykZKibbr0TTz3NhZUElFiXAKeM2QQK5k7-7nzjQbCamUrn5GDGWqolAzrmIsqAJYQ7sFPAFkaW_vSz7ZZo2Xb1Ft1t0ZaZvu7E12sQ2pHC-liNueu9nxMVMUZf1beeDmUYpiWq-Gnk53VV0DTWRUb5x2r1Z7izVf0eCAMxrp6UCgzgIhZ6WQP7mikSoi2WYmwI0UFJ2_eFdK0ZdsA736aNsA4VEl0X5y4K6Usly1SfSAY6k-ilHpKML3boALFwd6a9ftBUIs6CVDj7c7IPTEVvB-xLoTqTvl37svD3uR7VFAndKQuXCuGEptj3coXOoQ9xUhPkC76wc46lG28YyWMCZpa6eoPuZijZvJwlqA-brEBR3Hvny2vKydAAWLCV60UibQfDVl-wpDfPFrqvDG4ndDV5ZaydLvg6HzG-0mY70vpqVJNAAK136rQMIkEiYXrb3CEeSS89boTvwLh8Il3bzrp5xG7scvKEpCyL-Q8qafwOS2aUFTBc0bLr79lxBNJ4vhfST0AGm34hskPn5NrinhFNV_FknR1gTPMzVSda_RIvF9ZZB1aSDyoDrNsTCvILyUIJY9HYPmiLh1Ovr4SULdEc_wCGf9oHn9A2TE7zW4IxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TswQVneMtTudrcKXM5N9OVvXUoarEKFK2xPp44_dD3iVWPdY8-dVYtNj2foprWDSCnncrBHizUN8R84KNDbGHCEINosLpN2rNMd8xRoOgfLvjMxec3DM-c6r4NvGdPJlrwJmuDvvZ7rxNGLHuLA2LUhia5x-2m86jtvCBpNyJriMq0GBpMOphkF-mwk-t8BuVl7iNu_6qAsOycdBrBWz85j-z0sPlleRVJok4gvyU9Wt6R0Btqxpbm9_FP-QNBw6Jr7gDz4Z8oVo8skz06rL9xI8rDUVcj4QHgO3wavqRqPW2wUinOD19v9lCN2l6eLY_ukFDkpqV2rKWVclCMn_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliCtPb4gwaQAmxBRED7SGgit58NBu_41NYR7ylauDVWJ7cnwI4YFP-qaGU4jHNrFh83JXAWPRZc-sfZszDeCX5ks2gXdVpPiVyRgmC6qE0E0eKAzsAarGTvA-miolKpT8HxsdID_vnUksyp_54BpVj_0F-fBp9_HRrhVnw5QZoj9ymZHYD9Z73uhHXSsBCPldbGPNbIRWM7SDp-PX5p3pSL9OmcAz1FyAQQgAIUlT8OkTOyHnJq796hjeiDvlbNnqaKH5a2U9iHnvziQZ1jwZcc_DRnT8-YQG6I3sbWEfDf9MsRQncfT0uUP7d1YBFSfEFkwtETqFsyksMGXaKPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGr8jKIpBx575rtHIvYT9YQ1pgesv-UTJJeHkPk9upxmAkRvCT49n5t9wo67tbEcRS4S_tPf4VzYm8fGwQzqoHiSZqhQ-zU-t-mYFY-tZb-dPgcHp0SLzZNDDRRzjlHR9gXOWmVc7EARxVTcYM-dgS-8eH5aBDTNJfPuOqE5Cwl4ZbGlzKmFaPo9cuLMsN8ADPh3duVzQ4drcwfTDYSrTIbInZsvIe2S6rcOsxZsYHNI465rLeO0M48DHk3d019DU3Ljwi5bdQY7a9h87M44SdySWLyzEt3EHbbm_-1-O5HGGPn9yrMU_XL0OrWvFw6aFUVYQxkU6xokLapDOsetQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjia5uq-MhhS4ftW87KkhZ74bMmfzDC_efNZtJ8U-NSodqyq7y3gVm2Wy-SCtdg3G0V9FJoDLJQjjDA38pdgpEp8XeFZZSBiW5n6zmX1jfNvXqKBg39anddg3UjKexgB5VslW-ANfxzmYT3JqRTjUFb18fk3X0-N_PCLXye7INkqvLCaLQ_nwBBGMmWEk63rNIxz7Yox5p8x1vXiHjagv_AmBsGz-cvMZ-PBfHeWin2ov0yQiMtPuB4VWq4IR91KSA4ovF3DhN8gDbt9Ccih_VFKUsOoHlHG6xuLGSZcoh56wffgZ96AAoQYvbEUzuFYE1huxUq8cnYvx4dgq6RxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛قیمت‌پلی‌استیشن 5 پرو دربازار به 310 میلیون تومان رسید. بهمن ماه 45 میلیون تومان بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29633" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdKM9QU9ZxmBA2W1dmAnFUwXYRlKK62vRPbZQH9y8zGG36_WYjvacURzJRJm-Kw-mhjgm9LRNo-UXIu8cQiXl6AIWECIqqcUPb4QuQuGv3aGloItjqx82TpHI4s6PvWNu0lmdboUaNuSXjOx-veyedDPWaWoRpvBnzn7VueU20oeL9ZuZgmAVCFiQBys_dylpirt_z3XPM2XzrMPtbfEiYXoeVBVuSwiukAsIqlnMz-HTUAAAftX2RCYWUXhD1KpUEZ67FsOOkpKOImyXNekkNvKaZFcbCilqYJrot7eaYDlDVnEkzJk3BGrY4lBe9cLWBe_B-m-IDxikdZRIeJaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بااعلام فابریزیو رومانو؛ مارسلو بروزویچ ستاره کروات سابق النصر با عقدقراردادی دو ساله به ارزش 12 میلیون‌یورو دستمزدخالص به السد قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29632" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKYotUMAuukXjsXYc0KcTIcodDMywiRbJ5DdsX9zgzf51v04vI8P4Xgb9PhI3N6Oiyrg40cJDcdLnTzKDibEc3AsvknNOyQ3ezyDj5l1WyOCAs23lkTQzhl-nfkRdIn8Gu05qZF5QnXPLaBNwgMOgYus5WPl0pwdzBknRHrJf5BzCYZVNdyTijv99rofZyj3s3aaGPiRHy-yNMU7AdBTZEplOmWhCAUbN4l7af9jZkU1otRS3ZYKiuksMyMmy0mW5s0CzB_uj4NOoUTEwWkDym6o1uyfIIpAs_GKA5FUkE1c_cIzcfvgrCvSDSWMvKi44_DY02jTVlEuAmUxLlWG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زگیل و تبخال تناسلی درمان شد
‼️
ویروس‌خطرناک‌‌که اگر درمان نشه تا آخر عمر داخل بدن ماندگاره و عوارضی مثل سرطان ایجاد میکنه این ویروس
❌
HPV یا زگیل نامیده شده.
⭕
درمان کامل زگیل و تبخال تناسلی :
1️⃣
زگیل تناسلی
2️⃣
تبخال تناسلی
☑️
زیر نظر سازمان غذا و دارو
☑️
بیش از صدها رضایت درمان و آزمایش منفی
⚕️ آیدی  :
🆔
@hpv_help7
⚕️ لینک کانال کلینیک
🩺
@hpv_hsv_clinic
📞
09212046421</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29631" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOe7GecJu46yKd0Uofh8kvtUuDRy7VerEZHYLdUq2yrbyYqbxJlqNnkcx2oRyn5aP_MFkk1OaGQ1095QXSnrEEDN2eDH8nbbd_HCjCQuT1CXoELyViPFx1eD1h8QsimZKnZ13zsiYkKXu_KOvF_-89P1y_4qkFEmLjMJHP3Ae-mtkH5T53MTbQXz3_iEPSY_km6WxUTXRziXvby3YEqXYYgT-feZD1ifl7UWAc9QcRdAJJi9uI5x6pQUfkKW9Js4giI_JyhKGff4xpxO7GqOu9KczmfqJ-z-ac4mzVlcdi8KQtBS4CSMYAeykFAG_ddtWfNEDBLYHkvFEiKqWgqsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29630" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC959Taa003IPFySKAz8BQRl0W3BZvvjrR_9R_-Oj0hBBtfTT9l8wp6MeyotBZBxcUzPCjUxM8B3OfMmP4Dz0IWnx_aVxQqYRtnU_F8gMqFCC0McW_e9qbSbV5QV2pGOg7s3fkVR1o7y4JDtMBwy-YweZ_Psoxv82T073sJW50ig7XhUy4q2h1tJWKRNX4kutgU9F9g3RanmUDB49ztSHcGVj3JlO5DvZs9CnKGDdvv_y6uNyWB102E8F7Xgvmu8oWCmGpGDGoD-XnLrALxArsgPnIGJcetEtLAO7u5XN8gSmj1KaVKyBvAVMALUJzU5N0CuFICALtHEVxc66nsv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌جدیدترین‌شنیده‌های پرشیانا؛ باشگاه‌پرسپولیس بامدیریت‌باشگاه فولاد برسر انتقال ابوالفضل‌رزاق‌پور به‌جمع شاگردان مهدی‌تارتار در نیم فصل به توافق رسیده‌اند و سرخ‌ها با پرداخت 150 میلیارد تومان رضایت نامه این بازیکن رو میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29629" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8G7Qq5EhO_k3HE4pzsYikulMUivk39sS0T51vC0leg8N8kd-wqWyzdz_VcBOt4XFbUDoUE7Ro6fYAv7gUGrpWByaa6i9tx9Q7SUSm2EZX1G8d4UD9L23EJKgWIDsbzkT4AUeH8U5XKIwfFaOBvnYFj7b1MhOgH_iKxBNDO2C26a0fxqKeamzkBIZZ8O2_B25Nr3kkBfNiAis3NzlI9iofE1J-9PF2NrbGbDXSQ5_fSop_VlybCWlzSFQ49UDLif_91k0WV65FZOWQ7K0EFuY9sm2A4EpQzizBXoSlSDNE3hV6VW_hQPhmMAOLPCcs0mZMDWbzYNkbwsodmwB-U3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ownGveQDic45xZKjX5sXRoLq_5slhIQZ02dcApUTwrtjzSOjzgUEYeYkL-ejUqo5phIoco7szlBZo6zB5MJRxkjc7FaUOhsWHbAdShijKf0E4RzwERF1R8BxyNGzaNAI0n59pkVaCZTcif8_zZkotKcrAQnPKMid6BOBI7XpwOmuLPQg2c3iT7dMejGprmZ0JIygK3aXquohNEiF79XcQGLVU_elWvhdd9G4Fu896vBfy0RlQPB_toO9WzziW6Bd9llW4NToSh5W4FJ6z7S8W_ywWsSfy6vHRMak5Oirm2FixrY0u5hs8yxU77bFmuio5bo3Nf1tayHC6zHAV25Epg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZpOdX51eVwFa5pIyZEQ5zNPVqqONHPil7qcRzXL7bENx4r7YE4cXADlrOIPUjjy5HZrhaXbGix0iijkX89FgOZda8JJYy5Qw0w84PVz_Fy5kTGBTMPdrgcZ-Td1nhi1P_9rVqc5tusDMcQsM9Ozw1ZyKPvW4ZxKj9rU2bVV4kaWyLg_lIrQO8uKDlYc9ogp1GmoTjKiZlh8S5dbtsghL2oqGfYeIAKAZzMCU4sXGWHgr6Ygm9lEsw282Kv-antcVb3CXRfCtpkCLObUzmmooNXcCUt6PxQAOkI_SVByhSbrRgaJaOLhBvXaS6Fx2ErnUHvCWzmjuEnnpbzUApMUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKn08gmiGcQ6LEN1bIgIkBt60YVa4j-qEIUkceWJcgq6nN8r53RsYbT4Q34lrRQ3SfG1frV3RcRknZGCMEo_GlkVIh3snj671a_z2tvM5e0jdPGy_wnuJHeJKaW74oeB_mXnK1bUyTnRKibxnVnICAEjnFiRKVrrauIsF23oykWWtQTVHaExuYLXaIuGUn6SvzlB-R3hfY13SlidaoA9afl8cUkQciarZmsdVYc7tCl-FrfMSx3D0n1iEkMG68pvjA1BwosXknMIFbbMzoJsPyBlVkPXlDaEQH8cNidWUiTXwAfQAefHbTrxKS41BYvD--FFw8dwoGTtAyxIenFuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRyOx2-SG3aCMBdt9mAr-9y0fud04g7cZgSJJgoU-NvjIdPESviSyXs47-WEhCaNau_dxnbhQnlTTKKQ-S9arEfNxsUDGHBGlOzrfPBwCu_iHIxqovBEMupSjDkCoS1KAas0eDX51FYx6uuNk-TgddnF-7rsWSP8wsT6B2t5gucxc-LfIXyTXCdejiLpEHUUHVcgYfl9QQK-muZC7s8XPKqaWVtntjsipMzMfGYOOXRwB3m62ZHklGpuznhkfXnhAK5cawH8JnarZLfHsc_3NqYIQk_3G3beEdEQ4OiSsCg-Jc_bEcZt4WCIXU6xRKuqb-XCbf7hAyDTSNsQHKEh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfLSkqqO6vMhemse6qGacwrN1bnEvXhXBt1RUkpCOs9KhImG1-_HXwF9C485yatBmxf-Ja5AsEoH5rhQxHlh5fAm1nCzT2oWzpYUAcTUGWlej3wnxoc4HEiwVUtCpleNk68lb8YN3PlZF9RI9RHJmCM9sdps0dzbBW6I-XFGgVuIAO3QlWuYmCeGFPb5RQYt9ialQvzh5D_21pwWAR9yVbW4CNoyHz1ej6835NagwpSyuPlLQiUmPwkxb8pgHDHYQsxOZJhWWmVFH52sNDMA_aTBCXBxz5A9uP5ijkJV35-gyIqObEJjK_4WtUzM8ijNta4q8RcCWCsB4FdORDwwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL-DnRkEooXNA4SGjrQE6Rc0mFx3jLGa3BF4IC8bymZ-1q8EvUQ67Y9OGemNZrA2fx1rOHT83-rnNfCjTYOejaA1HrIdI3FP4g0TqUh7l2oRP8dTBP9Dg5Oj7oaAmZfYLF75y3fEy9uIGIuofqKJC0ohRimfkXloG4X_m4alMaCGUFeEmr4i-OLMu2NaJG1D-sX_6A_jEQWN2wJ2_nGcPojAYNWuh7zl-narRiOUdNXpq-uuuSThVrz_mNkmACY5_qVc00cK8mg4vXWrHQ2IHpOMZRkSz4Lw_9-P4Lp2NVeDeh5_fdILS5AtZkfc89JpNeyFkaD6gc7_YiRe2Tbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHkN8c2jWx4QPEqtl-UBImkRRMmIScmEVq1GzB53WHzaSCKQ1wGpObfbsx2EnQDmEaX1m0IaCwa2C4T_g6aWdMgcTo0hXeqbTVEBIXD5OvO4fvgGrC5KNBRBjKLnjCTsKzG52VvgcXMek_nyaF_H473oOg8_VqrC4TeSgOwMTF580x2jL-S2natAeUznbQeOuwjKmBcLWdWH5L0xIcIAGk3U-yrCsxy6K4ydgPPiHEArG2ZEeztqkZZrug6sIj-rK8erqdD4YZjOCIruJkPmuy78l-ebHx7YGb3Fcv9zdJLKrOeW-nrkOWnDPxupYp_0AoMCni_QoIpuYS_zaSWJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWWmC_7JEIHb1Q1OWTG5ocfn7_RKOixI8ecIgGqb7wxE3D5xoZbuEqQcrltB605MnTJh_6TFbWUCjtjMW-yQonze0STQvN0Vzm1s_tmNoujzuLFhaFjbuwvkfDyyi4IKAKJ_g4avp5RGceqXSUv_ZCyWxiL84Sh2fIUU8dsZ0kcwMDn7qRgYPB4oD53HGFCf10Toeswo43F1cDgPNvCsA-l8C0ZEWeu6LlVPN8GLKGq-K7Jvj0-wWj8GM0nIk-cU7uqmUnaXOemeYiLbU9AdtX71NxqoD4xhvWThbeSozWcxymLxu20dcUQwhz5tLkg0a5RM7Q6smnB1xpTdD5y7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuT2acNcIzHPgniOyVV6LtFjbPTn5U4Q6aNcfj0sJeKnCK855bdE5JEuQkw2CebGAUxMKXCwkA2KuNLYnL5-fZIzi6u0oR1fRIaal3YVFFkgtv__BfQPZalVOXrARUlGBrevPJ5k8VfDzL5S1s5ObushPNQnya1zCrlhQWGTkbosMPJDhcYlMe67qOT-ln4kR2hNlr4e_JPgOXetvLNrFxWyld3scMa881seVXZQEmypUQasz4y78x32EZnoaoX4SWlJtEM1s8SxtYyHXgdxPG-njmwu-TwK0e7THsfcZvHvvU_6svtA8hXNinmEnhavAbJgPWl7eig6QuJzPajWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tT6havQfxjxr9tkuLTrmq2HtYjCAfSrHyPXYryhbDQqHmK9PENrI0QlEvkOTFgyJlDTXz_fqg0V8TMw0FnBe6Itq82EDrIY1FdKu6m57uW2kvR1lYqLZOEUmnloK591HPSCMyIgRQBeSiRr7XFyCnHhcIbF36TTwFSGRkpLemxPaGbWwnZQX59tJhj0lDoHNIvMU0Xe1E-82N2iuQNl2E9cWSbYvs5dwW_aWhz2AKvNUdJogGxO9tqhB6sZJo0bdLYanOIXRC6vOmMnk8uwXLNK-BEMKycyS0lMy58jxFSq-kxybaTuXX-WbcEoHvAR5uzbOoliy4_eqS41Rw96LKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLfdCT0u4dI8H738pjEK1jp17JpzB5Fb7L_e1PPmWLOxr28haozbwfJI2CIMCPqyn_QJxe6Eq1zOR1dTitu_HdyEIvc9jAOvYjNVfx0J60rvadLEl9HbD3TM8bLHpxuHgkHEik4wutc9yZ6AkSHNfKOm_LYsn9YyLU_BFFOOPbz5wvF69K9nGrlLA5qWy1V7ho6JewprsjllgfDoIMZClCOPxjm7a4caFyD6Hs-k2DPJzfQ9rix99nq8RlPVDHIdXaMz2m3CGiz9QMap5PvljX7qkeMaW6qbzrN4BNlvVe4u_tBP0z8kDPI_dWfr6tWzYiqqDFKoG9O7xQ0DDqNwtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzI6MhehLPJJ2pvuJKhn98-WUM-7zrK_Ogr1hzJP5q1cb_NuXcqZRxrmi1mjGW5JqoOpUXeikq0rcT2GnAvhvX4TACeJZA_8Ja_wOi79K8pRv_bXoW8aoeLj2B9X87u3SSCf0ccF_AQmdC_sohvxyUFN2SWS7lRqLenR71N1XtSmDlhFU9XloaFFsBxgFdPTA_R1tW1M5H9TB2gFYOWYm3vYcTlUTa88J028Vb257mrwsWvbUOZdv6HEM9GOssPXER6UzYuvNPH7TxkOBGjNe4sLxomL2Qlg0c9CULb8SrUrYZkv81uvSGZpGhy52gns8qOowJPh3sdVxTLbatnVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdC85qbWZMQG1pJhLaJKHfimzxGMNG6s5UR3GocSKiACeo0xoC3PLGyyj4VA5xTNP8jcHM33sFyzAL8-8KRpx724FxNOp7nM-9flZGpX9MEwKeMEAGDK0uAnkhTbU6d3AUvm5qKKtI5sZwjv1nW97OB7e5RUgYm-9h8mwxFm8-Ap-t41fqR4f8lQIWg1xtmeXhnTR6TmiT5FqjZFDjXhhsWBFOXiIlVE9iEyQaUXY-2tBOozMhFrx-TjLpcTFddrcXTDZiu89H_IbTUKeV73mTG3J8sKPMvP7xDugCvQuq2xpw6JEWgxhVOPGMJW5WbHWP93JLflD2b2OML1dnedug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFLD-2trte8EFScTgX6vWJaDfI2JBOEILWHIjpSCVZEfIDZ8YkSgBl03AqJqQjfxdY1mFfJ7z6UE9fpirC3L8paG2KpPOasyobA0kDtVbiva3ylcrLIbHV1bj9FT5U8q-qyFTNQkfcctLoXdG67ZT1PB4uaXH2V1FhiLKSeMdmbvqCey0Og4j1CNQJEWxiHoZTtkpF6PrLvLK0bA5iNTRrAH7YIn02mDdFSCow8eQJBD_6BkREpKl8-frXIoQYg2HTwHtBS41WuEmDljweQhNAlNsDpah14ZXoPLfaEyvUevx7IutY_HQI17DMqP6AfZ9dnfe58yKylK-tN3UVqreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Gbneqv_VbXrcwh9B4O0ax4MH628kR4JSOwRLyURks8FlcAFPfqIB4lKFd-cL9NElnQsk4e5wQKO7E1dhQTnGGnFg0RcQWIAfFwuSg_h84CTfiaSpy5_lIdOzuHKyYNHktMF_FEQ1XljwW3PmVYzzAq5zLBWIU8hh0UVtj8EFs8xgIHsdMYUf3PwyYU8WHX-9V7bzLxXrA8B-mBKm5JaWCznh5DUOY_CSybXHq3XkwnCD6E26rDxnJTFRN7loe2rilIB6hHqIqmPTNtGPGQkZ-rEHK0utd8g-lDq452Kpa3OW2k9ejEEHHP_-IgE6dqC2QklX-Y1Tm9LmBPcPOptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQ_i44Cseb8uHwThRoWRXsGhBJdzIPcb9YxRNqUxNTybxGKvLVFoiNsCwxpKXzEFW7cTMkfdo6aws4irdLqYMYOWBKynwn_vdUwTAOLpWDbFqU9kLQzaJTpbs3x6y_EglLm3_lRBFYRhrpmPgPA0al8zfhk5gl3DfgJVPrsld1qXmKKiCpnZZvCfZZi_rfENsXailOKxjsif0Iegd6rpNzhKmBIqygPEeiJRGgXA-4ehJLNmtCMAp07ovTZJwp04G3zu0MASZCIjuSU85CHYpk3UloYfgFKZwFCdGNc3vpGMb3zV5ghFKe6sVrEEdtchhDKWAzoRwx5bJFoDKFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVo4IL8SgWVSTvsjOnrIeN572edlHxkN5GmKGNT8gAuKSf3oI5tzjLmtUCCfqAUCjQAKWLnAmqhZ6fwuYLItIMc3Gp59Nv3SBeZjGKP8-ztLBbvhJqqV-jEi1Y2rbJW8oNRMRYA--UIZDRuaUnvMLQZcnZhOipoFB6VmlOP7uWSs75tWkkCCOcN6ubEsbv_wWESYQSUL3SJCj_-t8lcYYRPgKa07YF9aKfQom04RqzNtZfEXkbjEsYskjfB497JnlDjfASeWgJSQogbyOeZUWxzQWl3u_lpf86Jna07iJ9I6iPBdE162-kF9GHuo3rHhMc-teAsMdrbVgQaEzq2S8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmOCq6MJSlEI9g1VltUpqlgryNob0KQdzpeyywCGoKuRIYycLN1yDuaxW9QAeE_aRQ9_FX7cYejnjuGbGQaFDgtTeNvDD1EB16QC8A71LEsKW7JKg16aLubOO-FG3_YGQhCtm3-5sbwEtdqp7YYWitYRN0DprGLDWqgZKXaTv9LS-fl6U3PyFm8l4VjoQhgYToVbDyo1TYMdRqGtLjkY0HzLOX_p6HjTjdrSXbh_yBDdEJhLA33z-vYeTlzQzaw8oWNt8OJDyKRgSnCerLj_AhMLbz_D96eaRMGcVvJ0zuxgsM6ZJAiua91PcHfsTh84cpYtL_xv4SRsj68dCB62HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=rsr7wyzcsWc_6st6clssgM2dor2sF8CASWuqr_0lIhGoFBPzedurYOIS6dJHjUcYgxM6isB8w4Vwn0VGybpWPBh_CFUdyGZY0IBq1SZ0xCXVN7U7Swpk-4BAeBG1iuThkrGelbkjmCrc_lvLCTtlnoLGk2f-jrOuo7zg4Hsge0ypv6gng2AHTwj1TzFovY5H4TlczWqACsr0KzBTQOCYzsM_IY9QqGRcoFbKG5a0XwT1ewx6CKqvkFuO7XjQWk5h1sl_c3MOYUAhUg8Yc6gYPhpI87ORbZlN-P6_LLu7_9wQIpLQf4TYaYFKntHEwlVcPq1wo8o84XA8frpVeePiQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=rsr7wyzcsWc_6st6clssgM2dor2sF8CASWuqr_0lIhGoFBPzedurYOIS6dJHjUcYgxM6isB8w4Vwn0VGybpWPBh_CFUdyGZY0IBq1SZ0xCXVN7U7Swpk-4BAeBG1iuThkrGelbkjmCrc_lvLCTtlnoLGk2f-jrOuo7zg4Hsge0ypv6gng2AHTwj1TzFovY5H4TlczWqACsr0KzBTQOCYzsM_IY9QqGRcoFbKG5a0XwT1ewx6CKqvkFuO7XjQWk5h1sl_c3MOYUAhUg8Yc6gYPhpI87ORbZlN-P6_LLu7_9wQIpLQf4TYaYFKntHEwlVcPq1wo8o84XA8frpVeePiQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_k8c2tSGIwy3mD0GKPPALJ6s8LHb80k-jswfmxEe8BeGiyXYaGmg2Lj8XiKgjKZxrhMeA6ngrT_aQKoBJjkI9pYkapzm_uTw0a0x0weMxiLD2XrpmlAnqgznkUqdYFV-Hw6pIKyr9VJx_1FuVsJ32X7DfSfbwmrtGAo9662kOr2jgPtCAQfF-g9Et48TIacZeoMyzhR6Huo4Ps8XRgchPxuFYYlzDyFI1i2BBmQX-1cGNEw42ddAGHoED9AUXefIHQZx40Mah32iSVh54H88TLPh41_AQV9zfzDeRshzYQbWOKSZll_MLkOVKyCZivZ_m_5r3-AT2DW1Yu-LXVbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOBTlfctVXJP4DGKWbRaniuS41C_a-NIFeXnxsexEAUx9N95wCF9lHWS-qWsoDfvP7AECsQbV58d8tikIxW6pOsePtGO7DW4bpr3GEA_SLdsx7yWFq2x70YicIpEbze51BiX1TIah9Y3llSFaQmhwoAEH0CDycEgeV3dO9B7Xcu9N0F-0xfkhd2_-zJP-HnZjJyPKyLc_dqam0lEXF_pPThxSDrgoKFvoTCODVsN_Gp-S8YtEFBvYA2WrfF6gqOcz03z3H-KhJ3LwBm12MOfLpL72hSFR2huEY_6EmFulla3V92wJQTPdwvV3e0kzV2UKR_ngZFXClDB_AFiEU_Fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3QYEYxriTWFR4hyy2zDrm2kBTNqTknqHNJkIMmut671KJctcLVcZFxlHcrYLbERVIGRfWFL4NTGSmAnCt0q6SG6kpANh1nlRiU8R9eld0s_u8z_U7w4BZv-seeZFUe75Si9ghD2kYqMtCMtUZRWXsUujzAnYq8A2sHE3eU83Ee_vFeXIgDIoemXryY6KQdFRDB1VWELL0r0X1LQduGCLAiD_iRK_ANwmJ1pTCqribc5TvxszFE-gAby1NAacs09ZCt-quNJYD4DbpVodUUpDoIwfJj00PSpyPsFhajJ0JhMHyXKcqW5APppF4P8j849lNYg5XNyVOh7NT7Ex19jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=inUB8xf0gZ9LrvmwUWnRKGX08W17KFcXRCayh4CWbCR3Rc7PnvvgHgoI9QIIsKLvCyb25tQMOQcaiQtPgSLrAV41MmtxfhrdPBOMa6qR1tdb8iS2MyhBON79jTCNLuykgJP_2cNvXNFcbZE7VfSMcODuXLEn4cgOsEmI8aAQ6CPtynzMjErjnF0hPQFE7XoXHGXD0k8WLxqMKsEW8Oz2GwTAVYOja7QZlhQIcFv9zVjizHUi9Q8dFt5zU73JLVMqRjlBoQaVqCYEYx2p2HJbKpPkFWvDocbcBhwqCMAFo3FLjKZeQ_5rViKEbFUS8gIfgAl8h74M5oPOtq00-FcJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=inUB8xf0gZ9LrvmwUWnRKGX08W17KFcXRCayh4CWbCR3Rc7PnvvgHgoI9QIIsKLvCyb25tQMOQcaiQtPgSLrAV41MmtxfhrdPBOMa6qR1tdb8iS2MyhBON79jTCNLuykgJP_2cNvXNFcbZE7VfSMcODuXLEn4cgOsEmI8aAQ6CPtynzMjErjnF0hPQFE7XoXHGXD0k8WLxqMKsEW8Oz2GwTAVYOja7QZlhQIcFv9zVjizHUi9Q8dFt5zU73JLVMqRjlBoQaVqCYEYx2p2HJbKpPkFWvDocbcBhwqCMAFo3FLjKZeQ_5rViKEbFUS8gIfgAl8h74M5oPOtq00-FcJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4SNKCvl-aBajUZZCmqDZC5hVVCJVa-Gum_kCkx1Ksmgvlh09Q7JmGmWtvl3E34ckgPLWDboekp60fV1PRF-lYExi3hgcLT3j0v1lM1OeZ2ICAgInLxfMZoB2rg2An6B2eR1pkMvIe9I55eFBtIyFizv64OSWJCT5bN8bbxLn61sC580MD_hstYbkp24zTlUVL3iplHkLnQIm2shTXoh-IMbqxwd04SomxllGDa64BfHn_WbMDcQnfdd4L6G1jtduMGZCC7DEvzzm8tjY5jgIEe5AL69LN8Hm6j4lXlelDoc90zTSjpG2TmoPTP0yzBaMcg2y2YSgdrjFJM_0OmxNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl6T3MkDzIl_cAuG-GqVr6K4gYHObZ6fYkMOPmbo1wvtX9Sicg8oH3ulKuhRQnnFUAx4k9inrvbYi7zOLtK9rTRvLP7pwulrZ9Dc04QY0Obz7hx7fpHGE93m0KfrEzGomk84u0ewoUwQQC52RhqPS5sl--UKq-PqCmq5u5gBVaNoYJczwYZ0crh3lrkcOf5z00LhLBYajvrpu21Ub_eQebmQyQbJ_1Z52U6YH6BtzqMVTuBpb56d5KqlPGzLBhlO_8ltqy3cfzLXjKRmBZQYZAzAERAEe1rL9ENiKOcLaTXDsgvUZOGGDm2gBUixW8jlfLwPQIKcorBzcg7JC57xyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtwzgrbw7xZ23OLAPmbL0j-44otUponOaA5NAThgzwvPjN4lChrBumTfXkZkvQQrq12WiHsuhmIUxPQKvlr2RXIOcoNph3b7pK4UWJ3wfEqm5uk0a7M5ouw_e3tGLFCzc1PV91wYHE7tzBbnqp4hx6KLc1z9Tg1E43Iz1Md01LbgRgELlRjJ947lnHv_04skSmFdyShq00X6KYpRQ6paLHX0zjtXisuHE8uH5vG3_zdJ6OBZMmiQ8OLif2v0pHs540ewYztv3s1tRzI_ICQwgZqV3v6VXutXTgiH3-YEh4XV0i3ebUsmCoaXFQ7mQ5-JKVeoTPrINqKC2s11mYc2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbF16IBRJVMlWovM0H1kZ1h76AunLb5m0jk1aPXFgodY-RAkjtPueMk5CGhS9dzyXk3PvdXq641Y5wZdQeLQU1XC4YzQDo_7EDsQ2jebnAVMJYOOOUBHPrqn-cVe-nz7nXeWJ8OjOLgbZY0OAozh-GvIIrq-2BmF_yUXSk4jg_dN10rxxUWUPiWVtVadagV2fu6Q9-A-EVMRFMZ00DJI24cn-DrxWeJufXcy8QUeiQGjKz133KLN6dkmNs1WuN7zaFDT1rFoWKyhQsp3FmycT4CDNy27HgCWLArDc-sDlrnGxck8TMwHEwwwCRaclBNd-12x4zIX5AUyl5gLdYWMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImHYoLXOcrfOebSILHKrP4ZAMvOkWUh5dVNMolODWFpcnBRQGlTY3SFRJi9z5Ezci1rg4_lS7iwe-5925nbxCr32g8B6dmUoxBrljwDqdMs8uA3ZZQz6cSg0jCsizCocTSQyNuZNXPEfoUQ-g7NuZVlaAWabK8Sv2-_GSlevKyJFTEsFdO58ZODNeFys4nUnqrxi1b-SMCOC5TMW7YX0k48qZa2IU_OHilHuMAVw2MPRoqvMJVf4g_HKniZxeq1GzdTyOwXFulSecfsMigL4qP7wrROHAgT0MappXunL4yxXTa5MfV_HnmSOeIVboOX4WYDB9Y9PEXdTKFui42TZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOHsBTfBUN-wLSDTCLLrDnBNEw9nRahrIRS7n3jewd__QkOXwWl0OOwkV2c83thOWiDnGSZFcv-Zrjq9o-rVQIXhv-maukuGu3_cZz2ARxXTSg01Wk5dcmaHEk0O8qLysKBORxrVyEunILkpp2F5pDfo9DM4JvdTof6cJmryuUcKrctWY9-Tj5unqJxzIlYPgMDlQJWUJvyQZtvqBHBKok2yw_3LAGdo5LHVpoSq7bFKT05q4UJzMoUBqDyV40n9KXtl8oJuSgKeoBQYRqvRVoN_EwVwq6xHeDkGvQoMLm5sCZTVtTpt7RZyact9l8mj-MA7x8SmVoSTgg2pWvnTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNHg-UPSOL1EdIlT3YyPw-BODDM4Edzba11USrXCqnJ8yDhDqPjM4D2ruRHRfL3TqzYUuO2EEris720GkBdqVzsTIpj3UV3Ih0cp6rsDPXrWeameulo_vFc_xwUdK5VLZhO_6VtDuLpKiRtY9-4kaC8zuM3Lgtv6tT-HKq5-zUAh1Qmlkej64sNfWTO9xfrz2Oy8a4_vq7BMSUe0kgoi0iWeIaLQ2uy2OMvfLVWXBcqetTL9EmwVq4N0oGQEW1joLt_qjCYoKQzoxZf4XT3YeFkl4i7Q67qOugwJW1HDYN_c34YxH7Z4QZjLGxasJ1XtT_mx3ahwkWzyaFEEauqQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=Xr5dj3XF6kokBGpyA5bOqVYSI7BB_3_onKXtuMUhYj5TgsaHIxnXuiNb5N0YZT55ctXoUzi0yEPaiSUKMCu-IlN0Hgf-1ebT4ATIDIuHMejho51iaKlbIA2bKBHT5oGOQloMuP-m9zJiGpLbNMa9LL6hPCH-CZM4UgJifQeWFvi2Hqv7q42DVD0oM_7tcgzZ3_vL7i1ArZxVO0JFL_bciN0SDN9NZOd7Fpl3MzGtRPlmrZQduUXHnEzUbLO__W-r5b0Ef5b-R3kMNGMi38nFZ_okljJlUEZRpbID6WKxaL5eu2BaHn1n4QW1f25I0M4TnwpRHhxQB1_y0lE5ubvViQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=Xr5dj3XF6kokBGpyA5bOqVYSI7BB_3_onKXtuMUhYj5TgsaHIxnXuiNb5N0YZT55ctXoUzi0yEPaiSUKMCu-IlN0Hgf-1ebT4ATIDIuHMejho51iaKlbIA2bKBHT5oGOQloMuP-m9zJiGpLbNMa9LL6hPCH-CZM4UgJifQeWFvi2Hqv7q42DVD0oM_7tcgzZ3_vL7i1ArZxVO0JFL_bciN0SDN9NZOd7Fpl3MzGtRPlmrZQduUXHnEzUbLO__W-r5b0Ef5b-R3kMNGMi38nFZ_okljJlUEZRpbID6WKxaL5eu2BaHn1n4QW1f25I0M4TnwpRHhxQB1_y0lE5ubvViQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff4fVXXTLZ10eB2BuQHXs3CBgK_ofNg09cRqnHJ9Gln1Bx3sewwRI7ciwolLBsJZLe83M0ckYutf1uJhtyvRn6sPWloRJNujVbbO0VuOpGDwIyCO-Fca1JObLkNfCdNGVD4FL-S9gvCfqMDodSfyOS0Dmpr9QdwQc7RXiN1JiOI0R__oB8qHI2ors9rzfhuQLCUE3xaaOBTO8aDPhCcIc5qhUSHNnFR712S7LVtGcK9zfjigMQmw-W7v1_N-TCSXXFn3kWBFFa7naUtDKb5LebsGchROl5cZ3rHQ8jVYHErWf9nrfn7dJ4oQXnrftf6wpi859NNvG2lJsvG8zCjXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEWBEFu8vDH4nwFBFkfNdTpXh58Lhhv791lOybxbCSusk9MZpJUXhHear6Gh98K0Ifj8qbARy7k95DyuI8kIY8zCNrtN8U2S6i-x8WW3Du4UzOXFuC0W1e2Z42ogwqAPC_4WvoZMRoWCOaxF7toSdpokNBDpfA2NodjNgwVJKWCKslJYeffkh7nVTMKPFjE0Bw_XycPqLdEUamDK2BQpO3ibWeVnLHFujb-uRO3SV3-LunxKx70Ksp1QT19ZdenCFxnjXSGksaE-F4QueC9mkqtT-fckSH4BqZNBU6m58DFK7dEnDcWlmX41hnOstUeGDpVmRoSA_goHyl4huxbzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsbkR0hzjE96QI_78I9TN1GAAsg40gQKEwePzo8wAg2QzOYq46opKX61PvIMdoAfYtNd2iFr7nlQm7waBfzXnsW-CniPTli2K3lsuY-4ItYRsuf7mkT0KbawDfSitD8Vd4a1UgJwoGt-6ul33DX0tNQX5_x3s_KMBsQjLc6YcZ93J2SoogLNCZXjrsF44qbDUD7XUau75fK6WzqHSO4n341dznW-0zdB_5xVpokdZPSVYZioUjPxNSDsqo4Z8sa7KHk-yRe3-Y4m5wptBhK4A5ENNOQ5eiFhxR_xm7Lv79Gp4Mdw-9AkVHfRsNhP64NszFxml8THpX0CtuxskxTYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=DQOxCfn0rmB1m_jnGucVGOy0cQN_YsiC41wci7UDFwhMPodDbhaKY8ihnQOzmTtJd7vpuNaEU1cbW8Z6ptOIW1hNuTbWgagqhZDlZiaCEUvlZFCxZZa2VvLI6Ry3I8Xj8gNLvsFUhdipmVwo5KPhDK7HA2ipNgyYeklat6BJpJgMX4aPHc4nt4Us6sA1PmpnTviLtpl7R_w6NYdulJkjE1mepe9LEbgzqd9rjLvCxWM9HIYtLY3kDGzJh9rSTTtY7WOqY6KnjL2zuqum5JVizVHN22OAdcvuJh0_niXliGa5sEYneZLOiKH0yvEMkuLM_TmMS2rTVc5PihBQG7gipEUAHMwBsAN1A9qBgrup95GPHGJ5drg06LhDdsW69KJyo0Mx9qje2GH3HRJXgYC2GHSoRlWE0YGgHev_EK580Qi78EFbjYk9idL_5SaYwTKG20GKSNpRHgh47XgR45y3BofrJuEgXGIP5e7ExArKIsAPyE5mcIB2p3jeHC6DICn83upnhAvtQQrMjOjMD4j8VYOr6iK8ic8sMoe_7kM6-u8IwiQdvHj8BKifZBVKoS9R3bp-loQsqc70xiG85Dc1XhAKumMFJ1ietUx4_cvxTeK3lVMq1eWLQkxOyTKGECaYNM7agMkAyY-iWeEIxQnPq8BXGoIWsO83K63ygSzHbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=DQOxCfn0rmB1m_jnGucVGOy0cQN_YsiC41wci7UDFwhMPodDbhaKY8ihnQOzmTtJd7vpuNaEU1cbW8Z6ptOIW1hNuTbWgagqhZDlZiaCEUvlZFCxZZa2VvLI6Ry3I8Xj8gNLvsFUhdipmVwo5KPhDK7HA2ipNgyYeklat6BJpJgMX4aPHc4nt4Us6sA1PmpnTviLtpl7R_w6NYdulJkjE1mepe9LEbgzqd9rjLvCxWM9HIYtLY3kDGzJh9rSTTtY7WOqY6KnjL2zuqum5JVizVHN22OAdcvuJh0_niXliGa5sEYneZLOiKH0yvEMkuLM_TmMS2rTVc5PihBQG7gipEUAHMwBsAN1A9qBgrup95GPHGJ5drg06LhDdsW69KJyo0Mx9qje2GH3HRJXgYC2GHSoRlWE0YGgHev_EK580Qi78EFbjYk9idL_5SaYwTKG20GKSNpRHgh47XgR45y3BofrJuEgXGIP5e7ExArKIsAPyE5mcIB2p3jeHC6DICn83upnhAvtQQrMjOjMD4j8VYOr6iK8ic8sMoe_7kM6-u8IwiQdvHj8BKifZBVKoS9R3bp-loQsqc70xiG85Dc1XhAKumMFJ1ietUx4_cvxTeK3lVMq1eWLQkxOyTKGECaYNM7agMkAyY-iWeEIxQnPq8BXGoIWsO83K63ygSzHbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV62Rl5eGP5omYNywv4OC17KNP7kNmejbg-GqH5QBTCsdrjwEfPkKdez0eJLNN13JM-VgDvt_vQjRbdTac8CHdqvkQoFckU5095WG-Gmvn6cbkm_sAGIQe2b3D-S9Pkcgza6DXStXI3UCsOjW79aN-ij2nimpVQTusAqsKGZdJ-Zh_PHL17YP3iRAFJuyUQQwzolUIrmr3NHSbCz2EajSkk_QIewtlLwy70vmtQcVWxfvzEFC1eyd8DglLhOFhUYzSiciIEtYy4Z8VlhIo8AY6D4fwQB8azthJ58f5SKeVaNtuMs9zBul2RKncFnqfm5pjKlo8yp9nkgL9ONXAI25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4_WE-a-xJ1Yaqf6KfnfKldtRJN8YeusDW2m--EHA_fMJY6-274jZzaNOey6PPatBJSkIA7DNKGGU1JIYcXy67WM0EMbedOgdhZsOjBgjGo1ujdMUerJzxhjsrN3HK4owKUDiyqs8N2T4F3dr7vts7Bw4rTVAvcq39ZX6gkjJg8XWTbrPq7Z0EUCGi06srRbLiy_rSw0HiZndq3DkAyu4VKVYucXAVOPuCtD14B4scixvrJW2uD0-UrSwM8by8OgEv1U7JVaOfSS9oqwCMhTYWafeZx4K7jrozTb5tUiCsO3uD9MgUXEUKUV2yXoeD-VDSR51yKNm73DIF0II6EASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=JeYeiQhAxTcZFCzVGk-ej6zxQB9LRFBNiNva5JqKjRxk5vSrL1ouK8EAo5P9gXS8ensSWG1OK8nobxiSZG50CuzSxex2Uv4fViKgbX7c-ttwjreiD9p0LUSHZ08aR40ZKzMC12sjKeysnAc5fPmbBA3dJip2dTg2j3XbXMGsyy-BvIPD9UJYW3lAZrTKWDuZcaRUCwV7tBbMLOOKfrvfgClOHSrvO1cB2lwWApahbr7bgCgJWL-Y3O9xQ6P1eVQbRS4XOqU5IA7bXv6OWRUBFjg5dJtuBcwrNia-_YriumD0XBtfXACoV6k-DjYQs96ujbaLRRIGYASw45TMXd__3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=JeYeiQhAxTcZFCzVGk-ej6zxQB9LRFBNiNva5JqKjRxk5vSrL1ouK8EAo5P9gXS8ensSWG1OK8nobxiSZG50CuzSxex2Uv4fViKgbX7c-ttwjreiD9p0LUSHZ08aR40ZKzMC12sjKeysnAc5fPmbBA3dJip2dTg2j3XbXMGsyy-BvIPD9UJYW3lAZrTKWDuZcaRUCwV7tBbMLOOKfrvfgClOHSrvO1cB2lwWApahbr7bgCgJWL-Y3O9xQ6P1eVQbRS4XOqU5IA7bXv6OWRUBFjg5dJtuBcwrNia-_YriumD0XBtfXACoV6k-DjYQs96ujbaLRRIGYASw45TMXd__3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=qeII46mXpuSnrcPKeZwpBxzLTqLx--OnBJdKBTlwF6tobdIn99TG-QrTrbB7VWJlDLTxsjKJ0xykghRh7UCDexh04myqx4VgfOfJ6Qyf6q7doGAEu35dPTCUFKX1f1-vfRjlLgzGi8aXhbrckuEi82qbzVowaddAe-TIUswzybhUrOmDJEnAVypgiu1D7WGd-8ttyGXRCDq-fHUAIA8F5HySraZpfuQ_pLhN6riMyZ-hGMx-AO8R4QTsjzsh6emmupYBdcj0dKvROuE-E38Mrv-XqcZAexQ5N7Pn5Nut6mjHMD3oQvmYaniYgsVCJ8C3YnqOb8_QxyQ-s1xbtvQnIbxaMg-wCT2R5ooAvBenEuhnkIT-lfEvGR8xocpHGrCjsFqeSwHxao_gBZp7zP_G6hTiSrbLcNdP2cQxOEMJxpx0G8O7_aGJyNYBl4xXRP28-saxcVBbxY-WL0UE1bKBsUVVHiYfDSInks4lz4gf-kTjtowbKg9ckZwKl-V4UJGSvGHzqeSmSK2S70fKrIbXP0Z7d5nQDQVXQp7gjgC1WKAv8yGQeM8QF_wta9xCEkn37Qpqboz2L37uakl0Cdna77SJ-CB4UsRxjN5vy_dFhuajQ7gRAYcdy8FiTUG7SYhxNPMV79kUfflOnO_OSnrl4hwoq8llidW6p1ap9GPqxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=qeII46mXpuSnrcPKeZwpBxzLTqLx--OnBJdKBTlwF6tobdIn99TG-QrTrbB7VWJlDLTxsjKJ0xykghRh7UCDexh04myqx4VgfOfJ6Qyf6q7doGAEu35dPTCUFKX1f1-vfRjlLgzGi8aXhbrckuEi82qbzVowaddAe-TIUswzybhUrOmDJEnAVypgiu1D7WGd-8ttyGXRCDq-fHUAIA8F5HySraZpfuQ_pLhN6riMyZ-hGMx-AO8R4QTsjzsh6emmupYBdcj0dKvROuE-E38Mrv-XqcZAexQ5N7Pn5Nut6mjHMD3oQvmYaniYgsVCJ8C3YnqOb8_QxyQ-s1xbtvQnIbxaMg-wCT2R5ooAvBenEuhnkIT-lfEvGR8xocpHGrCjsFqeSwHxao_gBZp7zP_G6hTiSrbLcNdP2cQxOEMJxpx0G8O7_aGJyNYBl4xXRP28-saxcVBbxY-WL0UE1bKBsUVVHiYfDSInks4lz4gf-kTjtowbKg9ckZwKl-V4UJGSvGHzqeSmSK2S70fKrIbXP0Z7d5nQDQVXQp7gjgC1WKAv8yGQeM8QF_wta9xCEkn37Qpqboz2L37uakl0Cdna77SJ-CB4UsRxjN5vy_dFhuajQ7gRAYcdy8FiTUG7SYhxNPMV79kUfflOnO_OSnrl4hwoq8llidW6p1ap9GPqxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBs5Aa_Lnb9n2PMbnUZOLxL6tgNHNEhYwVfm7Y09fEJDRobomt5ynSGf8dGpNd4aMV40Jojd7LqWAAoV4Jsy98xRYXIqVTP75GQ757ACcN-uUyqeT36Ra6YcFLmTeFUbvSEGw0mviqTm-wutJx0lT5E2jpOIHJDMQbpqPTlDc1iJTLfhZycjnYhEHFZwwfn6g_ExYJMbEeUX7oyjtznxcSbscmOC7lz9VxbxKdDGX21jAJIxlx9E7-R6gGiRBMQgbZQTLeZJWYDfEaRas45KOBePOwGd1xWjnei8WdqhaafuHLW4SZX0syarvdDFs_ZCKcLeGLORHJvHRWET_rnvYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCzGAabBSX6B_stzns9U8gJtoKYdLycP0jFdkO7ExD6AnO_UzFFMWVyTzKURl5evd7sOlu96dlbpJmLRtpX9ZxneLyW8glqPXWyM0cNHlNmu9RbvS4TfC_YVjONc5gNKabLu9Mtd_BySS4jPIqnKDP84u18puRc52eNkbUllrcFwW5zedAbue1ecne7BkWKt8UZLPfg4z1mPbf9lVyQlT7vk2rXxTYvmZkS7_ZHIGGI1wp_6kqhxfjx28tkDDlRFBfxGzRKp6r-eGJu3OipUuY-4LqsyvsDCfZKkThiVPZ_ULs2daUkk_2qk9nZCMKCD5i8K7FoBoi9W6vR1IgC3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIK0rF4NhGEvkjFcxaa8vmNx9dl1rR9Zp3Nl0NcJfMz3mjaW_vXgkTGPPMBC34EjY0t6WlQUI25iWZT8Voyj14jOH7IFinH-d8klZ7uajKhk6Xnlks-Pwlhg1a3ekiyw0GQ2oQmfc4FxXLvogsZsbXuT7OTJAWx7c_CDzh1oWfbebxpeC_9fHuzYBBn7pX1HOy-bZiovt-Vot9VSGAzMw3_ZaWeGbdXfovPtCjNObTtcsFeusjd_7wJPyX7ujLFyKcnvKBtcpAE2J_9Vn5Np8v-zScw_0W1nVhMDr9MyB945vpEJ1SaOBy9oJx-66EAwiC2S8QOvXkzlXmahgBaTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geEQjWh3VEZgI08cN6MoVYuUM1EBAc1vxtCHLgvlbq7VI2WNV_WNfLPtJ1ptWD95X7e64-GVC83y3ocgK7hwQWOxoUaPTTncxJj9v0nHp21VRycUz4lh7uDx-mqsfyn1Iqj3zcQdLeYnvdcoS3kADXYk4Cf6XsDTwnbF5Rm50iCMt8hcphv3bRBerZu7goqxneRjCCUkdYThIVM7oZvKrtitxJ03xkYG0jRfEmnZeeyI8urpYcsLdbIWlymoIj9xE6yBNoDb2--tUiQwAjUNqct-rnNMuk7xLW9fP57kDhb79jquGehY7PixCDdYSaML8J0LEdWfc-zRCOXVcjImtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8bXbPahEHzS_xyd-PreBhcuSay4MAsFzaJiaiamtG7JmTNxdAmAHvzSvbfOOZP-prl-Zwp8SD6xGb2a9Y8VktUvf7QHCKgCJEiqOVKkzKKpdtlB03ZXDZek6gdQBPH3IeCrHU-KTWaSi7_bjNfuMWSZScLL-13_tAO8wLPp0lVqEdnxNesuPhKi3wNcgulsgN34rSgEaMUurm8304dGN5sX05AiI3HRkt-rE8KESX5xij7UmOpTpPXDxBc5NYTUI8NCvmO2p8zJjIdbTFZZYql0tY-K7gFvTX0hehyJd3TSbyVkxwJNWyomMYAKKlXjC3nLv17-9ONyWYUoEDZ0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=WKjtMt5lxEFrpWL4Pc5Kb4OHbKwZGzd34Z1drIV1Nfl3R0US8uRG8cG3D70cndFvIcKiSp3kWLVSRYCwA81nPD0zncLpL4KSRIguZeThXjUUh3mX87ZhTouolNRLrHkYeQttJ1lfQCAwIqRBJgdMFrAGb2qDUGNnoEZZ9al_tv0atEAXRiA3lp7ytE3a9iiTIKzeVlg4Wgv4eL5HEuyy3JLvqpBhscyQnsjvIRBoFDfDT0qDFaKIJ4V-8ycV08gW5A9iyJqMeTqdGB_-DMCH5TyegjG9HZGE64b0r9PDJd8Udsmeuvuq_Xy92vJ8d4CUbytCHNhfJ-vPhapRLve9u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=WKjtMt5lxEFrpWL4Pc5Kb4OHbKwZGzd34Z1drIV1Nfl3R0US8uRG8cG3D70cndFvIcKiSp3kWLVSRYCwA81nPD0zncLpL4KSRIguZeThXjUUh3mX87ZhTouolNRLrHkYeQttJ1lfQCAwIqRBJgdMFrAGb2qDUGNnoEZZ9al_tv0atEAXRiA3lp7ytE3a9iiTIKzeVlg4Wgv4eL5HEuyy3JLvqpBhscyQnsjvIRBoFDfDT0qDFaKIJ4V-8ycV08gW5A9iyJqMeTqdGB_-DMCH5TyegjG9HZGE64b0r9PDJd8Udsmeuvuq_Xy92vJ8d4CUbytCHNhfJ-vPhapRLve9u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzhUd4NApLWzMfD_T3H1t8Sy252Kd4vfxYYUiPEV1wpeg8ohyTiV8hpovi3SBm0mFuwl_qt3BiwZnr1vV8F1MYbOn_y0b7odi1V-Giw4Un5p2RBYqHg7CYZe0L5gcFHIx4nG_VSd1HYXw2dZ3eaxgBiafWNw28l-tDdcD_WoegA4pH93xsIpFrkqZNhO6P0rqijgYpjYFmTA3dD8-yYBburDPJ7CIbL_fGo8VpWxfT3QElQzAaKJ-mSL2V17b6avHQZiRTjnlfe9HT0WDtbGYQrolAf1ekxKXDpCMGhozDP_mHMzjJ7xlqVMya0moP8pkjku2j9hOsYCHj4TWUXZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2_1bA-hL-qJ1ni0YnWYHgAP9A-6TOj0w_8vex0RDV8mpqVNZdjc87elB3j87ZYaCr3zumvnbauI3W-VdlO4-I8B3Uv3AGNY7DWl_PyTULXZODUePK8hyr-CkzNC_kIrOzyuRo4jZSTdPU_SYCF0vmud4zWXnmR39E7qrUnKgXoZNaaM4TMrZ0XmhruMRnlPoB9xXSHu9-1b_wUct0Ojw7Y4Vo4EwuMywkiTaBEvTT5KZiODavLoUDaXbjjQmUTNVDQFD6Us1wbXjpw6810XXD0wkjbNFEHfeIuRMe9japzuthqnlQf_yns8W4BzFXUZsgkUZGtrbGx9ajqqawSdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARDUlHikEclLfFACe6Z9f4ZhFccSGlYC0ElgZ7uUGaUYUuKZ6ZFJIoa-DcUaulQszZxctfIJ1nque5qmWzIoDb_v6t2W28-rdrAlgVICOss-Yc75sbGmeArYm0poIWKoO6uY4SmrJtJRUf-CWUF2LohFTs9jD7bxbrsRHf-46xYOQjlBRuqlynfGu8o-Zy9Zhc_Prg2oNx8ryc5LOdhYrpqyJRU-H-H0J2QFQMJjODxheo-9-aZccL768iH3fqVLOogRR5Ru6F3O7UdNKXEuvcYXA-hnaX896Mtj3NZfTFLwLcpKywJutwXIe3wdM1fMB-heIZ6wJDDQQqna3yKgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoWx0QxUM6IrnQ1Bm6WhcCRahIncxqPZRfAKOBBMMqDW0X8qpINDUT35l5RuzzGiZ11gtKJJQIpFT-JPyIb4e4zPFJoIVQO0PbFCpFS5b0UY0utZnmb_SeivGqvhhTHLa13oRBeqtJ0RINtboXw5vayLQOzLbZucWe4qKW20G_z-bBFn8wf2bpkdMCOewWnqLL_AKTweBU38mk8ZB8Flf7kEmPA5qgDwOpGEI6phoP5bPAWk9OJnlElJsl2TqFHuUjJYuBuQ92ei6PMiGYZnqWOfnEHoPRJwLZK3KmN0o-xEO1As1hCXGV_HtGAD8LXyCr_P1d0DJL-fuFMGwtdlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkj0NIUDU1c0VfVC4TlssIl92co3xeKEJCcqPpx1Y65QH6GGO1K7ciY1CjIBQEXjRrqu31USGIDbEe5Cw7g4QTW3ZbEoktVf-UkBta8MQ1GRPQ_r7lso6XbdDHu-lmCoCvEQxuVDLEFb7zwSXxNqIFsMsgMi_UBxM1EfiXnrtlfRDPdRPFfaah1G-F24L48Pw7bkUDOI6ZVAuJrPEQFT7JyMKqEvLxrTrGBws2Q3X1fiuH0xr-XEqNfHrswH3tds1HCu58bmm1XaUNJhuVGeQHQVJ1K23rM2qcwqIfATSLvOHfSXHkAdZNgZ_uCPdvP_ptYFbz_nBmcFone7OL1PXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZOM8ODLoVEZs43g-Iq_dln0jF6Rp3gmVKO3kIsCL0IZRO7PSGnkyupRRJouz-IxCDOTPipasly5Y4AX4vLKxKISAoh0Itb9GEP6_QOjp-7JilzgI7l7xBOMQPPxWXgsAHLKvAYVOo2EAwRtK_6O07r24a6SxMnPsAIJtk9jK0n3YfXT3GjIRSCSolBkqY2-qPGPULLnL-XlJDHlwztzyvh_dkVuP-WGoGmxq39JECGWNUyZ3squlpr_hxuQ6KM42T-rPOejLrg9qTjSvYnl1i8TlgGp6JoVMZC1wiK-StNc_IsmOptRbtp2zB9Vd8lLc2qyf0BEltKWDLpwEFjWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoUFKW6-XhN9RQHEx6C-CEnt2EjOdSn50lPHkiyzUoSYjs_i6MEbrVpsCOYfSFeJAcG-cMBMa_pfiqlGHxBasn-5z-XKVH4hlUByGAV8Y_fzxLnV5WyPLa8NU7LU3apEe8UqgQdj94aGl4Sujv9A3zguC5qDSXq8uBD8sZKVM06rp8qQ4yMjw95yB8WkfZ8S4ZqM5oecC0dCd84uiaS3nIBkHPHGhoc3dOHdnj0_UVPo1xfA_kZGzUM-7rtuRFgUbOJBBc9oL8Vj8jSsvMg-i0-0FYpKd39YEepx8ryqzd8yepgph_bqSfBDx3uUNQdZfDxudcggZnciwALLEYrpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=hC051Qmp67zAC8k-FzR_Vo-SyWz_y51F54i-bnTjUB2fpqaVnz26taiaVPZByXE1_rSGcGQmGZludDlv_IlF7WMSywW7rPnJtC6LTojBpKyQtpXYC5Dbsxo_14X60a7RPmTReQpqDZel5Y0wVQFjW1NAxRpxX8AtKaFJ_MdjO4CswFehchDtUgOiW35MBJqsHnrn5ty5vM825oFQLYgQnsMKAaGrEtxMmofmFSGvfOumd6FHiE61QZ-hJzpdOMlDaEUNAbUgZtgLvexAC7cZvUriJlhVU3BlAyZOTsIlrR8JjMlo3mxdSKN_hCEd5ar2NGjVRnOu0-cyB68303LjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=hC051Qmp67zAC8k-FzR_Vo-SyWz_y51F54i-bnTjUB2fpqaVnz26taiaVPZByXE1_rSGcGQmGZludDlv_IlF7WMSywW7rPnJtC6LTojBpKyQtpXYC5Dbsxo_14X60a7RPmTReQpqDZel5Y0wVQFjW1NAxRpxX8AtKaFJ_MdjO4CswFehchDtUgOiW35MBJqsHnrn5ty5vM825oFQLYgQnsMKAaGrEtxMmofmFSGvfOumd6FHiE61QZ-hJzpdOMlDaEUNAbUgZtgLvexAC7cZvUriJlhVU3BlAyZOTsIlrR8JjMlo3mxdSKN_hCEd5ar2NGjVRnOu0-cyB68303LjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAhQ5gFFDsIxWSTRH2D78Sf_lj4HvJp4tlNjdlQpi8TSN7DGugBAPUOiUjRQ0b15tle8_HtX6zS62c-gJVWAGlBAm8jcji8UXhxIf93SuuG8uw_a6J2GCrOnFfI12bHBRgGGwNWZHgruZu-VrDZOhWr-y7rwtZkPIXiCrH66xptFPpeqatNx27ruLhgoqUaD9BwC4mUAtIwNGh_NwA_wLIIrGsj1uKEfuaIn5JCAbgKnKmAFso9aGY38f0IAQSpAFlEdufl2NIE_k0RR7IMRVsur9OB7u1KWeHQTxdF08k_jSM1sgQlvN4s2mxjrhxJg5jTINWBbLGMfepi1Z-PnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBaVYoD8mr0blp9QqLHNzy2WHqS-W-7HDgJHFcIx1x0atjjtSmTwAmUluzp12U9If6EGiX3qBHfzFi-_HqjJqYlfDQpduzwxZcvHehgBXLrc5cCPN9Pfw-ti89bOQaM9Z18E-UvZ9k5yO-hwcYeImznvTQ9q5YQOEsxnXlB0CyzIy6x4FFL1PBHiaqm5-2H2RZK1wKN3tcwPPUjN1Dc3CpEIa__uU21t5vx0OUEQVTRCli_TeV-mekOM-eJ4IeqetqM0kidVmmsYROUHbWWUv-_7lwPN7lScdZxelNlrEeGl8HCnsfWOboPfX0MBaVFhTr4OahVPBeuPGpObdIm4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
