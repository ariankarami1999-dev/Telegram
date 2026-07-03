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
<img src="https://cdn4.telesco.pe/file/AHGVQRwjnDu03HUwWlU4xv9qrO4mqXSA4GbV7LdAWpu_K6-zmu0mf7aJZC2_g1a5smW7j10hAuG8WGeG3lGx2Thza6BncWJgD09iAEby4D7qXKp6lKlqd8ksVVRX4Iu65Alfv9hW_xGqf0zNixFO3glg_cBDXj2YWIS4NEDVeraOCxhVpein-Ti4wSjrKGYzK4XPT-JblbLR8vPR-pLox_zAEJDE-JEnZsvdpElwXOd-cE0JAfDSVKenK7NMYNtctEfs0Cy3zV_y9cRSmcV1NpAEMeoEYdGpoMD1-IkB5BjFeTMwA8DnbWMNvR7BNybUt6HVidqZx1WXaWSKqc1zBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-665918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aum9xQ1h9lHKLFEw0x4cWXlfu8rZ-xyBTJtEGY-4plAid3b-Ey0nsLoD8X5mbtmdr2l58iVoMr9bIO-Ml98PZ1RWbNIqZw1A5P8wb_emK-E8OcedbvBrNYfHxTfkRrBkgxhFfBETX9Yx9W7xQ-BjnDy9oZELZyrRgcVFD0r7WVSqoU2aGY8rhDf_CVWmT1EurKFMve3eufE55VLc_URWfZBI1CuFiuAfjWfFA_b28vEuIbckDugPhePiA_3n5witENVxjyfYYiYIfkhgiDv48i8F76BThqKDY5bc__S1C_L0_czfcgMeEK2S3n7nB21NCMfjSD0T_2k4kbBs_z_Jpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صف‌ احترام
🔹
مصلای امام خمینی (ره) امروز شاهد صف احترام بود، جایی که هیأت های رسمی رهبران دینی شخصیت های سیاسی و نمایندگان جریان های مردمی از نزدیک به ۱۰۰ کشور در کنار مقامات داخلی با ملاقات با پیکر رهبر شهید انقلاب اسلامی حضرت آیت الله العظمی سید علی حسپنی خامنه ای رضوان الله علیه آخرین ادای احترام خود را به جا آوردند. از خانواده شهید نصر الله و نمایندگان جبهه مقاومت تا رهبران ادیان علما و فعالان فرهنگی از کشورهای مختلف همگی در آیینی آمیخته با اندوه و احترام گردهم آمدند؛ حضوری که فراتر از مرزهای جغرافیایی بازتابی از گستره تأثیر و جایگاه بین المللی رهبر شهید را به نمایش گذاشت
🔹
هفتصدونودمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/665918" target="_blank">📅 15:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cd8516d3.mp4?token=jJ0-mbnWwyBim9jZsQpebamDKBlU8lIgkCBRXERN3fY7_wipPxIYKZQcPuKkQI_lc70YK05f9Po3cIRsqNaIbJVo0d1vxiRQey0ES_9LPWGEEbeXQpc_VmVY9v03LdN1RC1zmtC_Iq42nLj4DogIskhXhO9HdlB7lFqQX3rnrNo7MGUu3vLJHES8dWKakIaChxVqFLVoGWZcgM5_Vy0lMQIHD9LPc1dKSaRjKNfwldtYH35WG-1pEX78HST0-Fogd_LQi_GLrAJBzdQzPhr7IREiH_YcVwNUYRBVrD7llJ6PweHKgDc2-X6cYeBAY1dm1dwaAXufVi0xTIwE4O0w1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cd8516d3.mp4?token=jJ0-mbnWwyBim9jZsQpebamDKBlU8lIgkCBRXERN3fY7_wipPxIYKZQcPuKkQI_lc70YK05f9Po3cIRsqNaIbJVo0d1vxiRQey0ES_9LPWGEEbeXQpc_VmVY9v03LdN1RC1zmtC_Iq42nLj4DogIskhXhO9HdlB7lFqQX3rnrNo7MGUu3vLJHES8dWKakIaChxVqFLVoGWZcgM5_Vy0lMQIHD9LPc1dKSaRjKNfwldtYH35WG-1pEX78HST0-Fogd_LQi_GLrAJBzdQzPhr7IREiH_YcVwNUYRBVrD7llJ6PweHKgDc2-X6cYeBAY1dm1dwaAXufVi0xTIwE4O0w1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد مسعود: فکر می‌کنم زیباتر از این توصیف برای ایشان پیدا نمی‌کنم؛ اینکه بهشتی زندگی کردند و بهشتی شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/665917" target="_blank">📅 15:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0138be663.mp4?token=MKAZ4EDn3H9aT3qOXs30wV_ZfUmBP189etBQokY5L5SXiPVkqm2GVNyRMTstmFctj4mAGRqU445mkmHXGnsL5gsARDpXPuRXCGQ37bgAYeJ35zwl9uKFMLzB7Xlea4Os00zbSpD-Pc0GiQecJSHwgTcTBkpvJNZsxs2cSAy2ZgRobG8f7mSUgCZ6_WExJuP7bfhAQGp0eIy1emlTBu7qBiPKYQ8r5YSTch__lODUPlujOhiYS-d3qOG1yIi5gg0i0iscIITrmMkMVZ8k6-PMlIGn3i4DtABDZRhSkxQq5qol5tGw0GoO_ruI2ltM1Ic-IOSXhkVZ9q8HIUms6qjkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0138be663.mp4?token=MKAZ4EDn3H9aT3qOXs30wV_ZfUmBP189etBQokY5L5SXiPVkqm2GVNyRMTstmFctj4mAGRqU445mkmHXGnsL5gsARDpXPuRXCGQ37bgAYeJ35zwl9uKFMLzB7Xlea4Os00zbSpD-Pc0GiQecJSHwgTcTBkpvJNZsxs2cSAy2ZgRobG8f7mSUgCZ6_WExJuP7bfhAQGp0eIy1emlTBu7qBiPKYQ8r5YSTch__lODUPlujOhiYS-d3qOG1yIi5gg0i0iscIITrmMkMVZ8k6-PMlIGn3i4DtABDZRhSkxQq5qol5tGw0GoO_ruI2ltM1Ic-IOSXhkVZ9q8HIUms6qjkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنوز هم فکر می‌کنید آیفون بهترین دوربین رو داره؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/665916" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf4154ba.mp4?token=Ah72pgSG9TzMhNMGbqQre11Ri4oegbFmI-cHG-1U3Ny3YaMqelqpBur-X4gBKzj5O6HTBaPVj2Rjswi3hseAw1e23US3Hz5T5JaPYa9NqMl5qF9dN3bUlicgpIW9vb4a_rhNui4XGX9reIt_ibv5JwlwGStHzHt-96C40djHUEhQO4HAIBm_Gv2Pb_2BmEhXWFjxvlCS7Xrn_q7IBw2TLgIq4hj4beCrOl9skw7rpfiVCk8zqT103c0E24RP434CQcAh6clvZNE_4Z5hx_A-fuYayI8hHGlE8uQYkv44q51m3QCNq1wo36Frbq3K8jTMnXzA8wX2Nz8G75cLb1MHKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf4154ba.mp4?token=Ah72pgSG9TzMhNMGbqQre11Ri4oegbFmI-cHG-1U3Ny3YaMqelqpBur-X4gBKzj5O6HTBaPVj2Rjswi3hseAw1e23US3Hz5T5JaPYa9NqMl5qF9dN3bUlicgpIW9vb4a_rhNui4XGX9reIt_ibv5JwlwGStHzHt-96C40djHUEhQO4HAIBm_Gv2Pb_2BmEhXWFjxvlCS7Xrn_q7IBw2TLgIq4hj4beCrOl9skw7rpfiVCk8zqT103c0E24RP434CQcAh6clvZNE_4Z5hx_A-fuYayI8hHGlE8uQYkv44q51m3QCNq1wo36Frbq3K8jTMnXzA8wX2Nz8G75cLb1MHKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس منطقۀ کردستان عراق به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/665915" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f1a33e6c.mp4?token=VW-ad_0qLwDzTgI2sh2wwG7AiXjw_oxxevMnuQZCI3FTazOdY831qbRU_LInTHBLYcaA_1WPxfCuHEsR1nSLwOF8u4PLB0G3ba7BuPpZC_Y257AEICzV7-0lbUfy9Nf8VFFi-hSBDmnw518mV52WMUWF1RFyPanjd05iNPZ0R_EMIxqRlbvvWhslBhCXvU-x5Ikv-MGfjUxXVr2RDyDYeGcTkPWZFoLTOtQVoKySfxjP7fbAVuzft9Zg-Vp-XjU-HMKqw1pllRfg2pj4tdlLbOUQ5XtR5RDDe9BgX4SOCAfOOvq42hANJ6DUFJvrJcemsKNiOIntUxhmSa2XbiEi7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f1a33e6c.mp4?token=VW-ad_0qLwDzTgI2sh2wwG7AiXjw_oxxevMnuQZCI3FTazOdY831qbRU_LInTHBLYcaA_1WPxfCuHEsR1nSLwOF8u4PLB0G3ba7BuPpZC_Y257AEICzV7-0lbUfy9Nf8VFFi-hSBDmnw518mV52WMUWF1RFyPanjd05iNPZ0R_EMIxqRlbvvWhslBhCXvU-x5Ikv-MGfjUxXVr2RDyDYeGcTkPWZFoLTOtQVoKySfxjP7fbAVuzft9Zg-Vp-XjU-HMKqw1pllRfg2pj4tdlLbOUQ5XtR5RDDe9BgX4SOCAfOOvq42hANJ6DUFJvrJcemsKNiOIntUxhmSa2XbiEi7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلپایگانی، رئیس دفتر رهبر شهید انقلاب:
تدفین در مشهد وصیت رهبر شهید انقلاب است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/665914" target="_blank">📅 15:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY7GEucKGTCm4YYqzjZeW9COfbePH4RAzEM9JQC1PXn1KJ1LGg4QNnqIEYxo4XGO6mIlPlGRpy1EbXA6v0GQHFx562l6iwiNsu6FwJS2jzF_f7MMhdHoEM1i97sWNo6kq_Hgocgi94qX2F3_1s9195P-6f0PH6unXIzuaVd3k9eQ6JAHKg_R3_Dc5RKCcW2DsbgYRI9HKzvu7IEsNELpXQAp0fUsAhl2lUNi-IhdhQw5yt0UhiM_T8FNfjZY-OURV7QVRYJh7QZJ0J6ThWX8h_JB9TMleHRFKgeoHq7QJT3CQepXJEo1hWmOd09mWZX_07k3Dzz15VLzoTkQUKRKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحویل پنج فروند هواپیمای بوئینگ ۷۷۷ سعودی به ایران
ادعای کلش ریپورت:
🔹
پنج فروند هواپیمای مسافربری پهن‌پیکر بوئینگ 777-268ER که پیش‌تر متعلق به شرکت هواپیمایی عربستان سعودی بود، علی‌رغم تحریم‌ها، به یک شرکت ایرانی تحویل داده شد.
🔹
بر اساس گزارش‌های موجود، ورود دو فروند از این هواپیماها به فرودگاه مهرآباد تهران تأیید شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/665913" target="_blank">📅 15:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=LKZBTpPgpVtoEoow0PL-xggiqIcwp-KR3JJk7NHBxMM8XLDtVgunrAAQ9mOSSz3lLf53senJiA1ydVGFJWuXRvn9YL4Uhab83pk8aOYb5VPHoOdT20Y4E_HL9Bi3v3Pi-iMgEn3aZRSr8cp7aLyiXuMVdeU3gODw0K8vVCg10y0sCDY2Bk14aLyXn9BU17-b92Z3mYay6BB6evf86PaTPRME8ugaufvAmDlINWcOi7vXzxHdUQ29L7838CSHlH1qsrJ9-u5yaqlAis2PL36FO7KGKKS3ty7I6K50yjnPnNUpF-JS-8gOwS6XaSFfhltEDu1FeG5jvzEszjWwDZsSPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=LKZBTpPgpVtoEoow0PL-xggiqIcwp-KR3JJk7NHBxMM8XLDtVgunrAAQ9mOSSz3lLf53senJiA1ydVGFJWuXRvn9YL4Uhab83pk8aOYb5VPHoOdT20Y4E_HL9Bi3v3Pi-iMgEn3aZRSr8cp7aLyiXuMVdeU3gODw0K8vVCg10y0sCDY2Bk14aLyXn9BU17-b92Z3mYay6BB6evf86PaTPRME8ugaufvAmDlINWcOi7vXzxHdUQ29L7838CSHlH1qsrJ9-u5yaqlAis2PL36FO7KGKKS3ty7I6K50yjnPnNUpF-JS-8gOwS6XaSFfhltEDu1FeG5jvzEszjWwDZsSPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدهادی خامنه‌ای برادر رهبر شهید انقلاب: شهادت مناسب‌ترین دستمزد ایشان بود
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/665912" target="_blank">📅 15:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81852e3307.mp4?token=dr8eKdkozHzbjmFnDi1P8QhRdgUqFowXX72jMRlXu5WFQkN7oIlXFXjJfsbBIR5iptoo77087KqEBdMZv01wubJDJPSPvq4soQJEyPIWSpcDngYWM6GwvzVWQB87X_IkleHxWD6C9pYmNB0GZxPhmmPqjwN9ZUXbqkr58Q13wztSsr2e5zhM9apTML-dBKvZQVja9RYoZ_PPOlIbypd0BFVuldSotX5bvlkkPMohMxBM6qeFQsY5jKtKZvPbPh98dB5KIXdcHyboCTuUseorRpVgJcgnFw9Z3_gZ7WSm8YTxfVFZZK923d4081g89dL78CBb2wN8B9V27Ceb6w7XwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81852e3307.mp4?token=dr8eKdkozHzbjmFnDi1P8QhRdgUqFowXX72jMRlXu5WFQkN7oIlXFXjJfsbBIR5iptoo77087KqEBdMZv01wubJDJPSPvq4soQJEyPIWSpcDngYWM6GwvzVWQB87X_IkleHxWD6C9pYmNB0GZxPhmmPqjwN9ZUXbqkr58Q13wztSsr2e5zhM9apTML-dBKvZQVja9RYoZ_PPOlIbypd0BFVuldSotX5bvlkkPMohMxBM6qeFQsY5jKtKZvPbPh98dB5KIXdcHyboCTuUseorRpVgJcgnFw9Z3_gZ7WSm8YTxfVFZZK923d4081g89dL78CBb2wN8B9V27Ceb6w7XwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نخست‌وزیر و فرمانده ارتش پاکستان به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/665911" target="_blank">📅 15:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665910">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW8w4KIZzlMi9QTyXCmgcBUM6uYbNHJFYtP-NAVIAWCXBA0DlWNRaNkN9GlT_kF6bq1XfTG8VhxosEZB9VCeOF6TiuRfGT4bqAvysUJH5tYgPOi7BVWJAgAucvVcxxCtWmb_Dl5E2yvrLFl9HtfuPxEV_NZ9x3hyl-JRWi7jQOwOwjy9Sgl0kpTNViHkTnkfCn6UE3SI4e-9EeO1lsFYMe6sPvzZscjnoGRPlR5nQjvsg169QiB7N0Bg_i1KBEND3LUpH5ksNCWjWbwWIxbrqMyz9nLpHrBmqTEwAp7wjSSBHOJhiytmWGqgzmIQcwLVvy8gdUzb9bVWVw4dm0Xd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضائیه خطاب به رهبران غرب: تاریخ در حال رقم خوردن است
🔹
رئیس قوه قضائیه با خطاب قرار دادن رهبران سیاسی غرب، تأکید کرد که روزهای پیش رو صرفاً یک مراسم تشییع نیست، بلکه لحظه رقم خوردن تاریخ است.
🔹
وی افزود با توجه به حضور گسترده ایرانیان در خیابان‌ها برای گرامی‌داشت رهبر شهید خود، هیچ چارچوبی نمی‌تواند میزان دلبستگی و وفاداری مردم به رهبر انقلاب اسلامی را توصیف کند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/665910" target="_blank">📅 15:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMfeqb6oEsx0wHqwJLU6UKWFdfxR5tY9eMN9GR9Q1VCaS8odlKC1_EYR_JzUJ_RSKiz0NhQu010tYULukoGmujgbEpl5J8hrcmZbKnChzErLD7sqeIsCul1OxmTniMMzPgYl71NLMemU5CCTq7G_148F-ZjVv7BH2Ajovi4wVXOgfzZzdUd9Zn9MI54dpjlB7R-DZGuUtPDJI49rwPQFd8nkHpLQIe7TKDX7PTd8I3PSEyk9OxnEFb0xDsGzrXJpY9zq_inW_Jk7nSkNHvEDcr0RFuJmfjOhWumGgNQZreimgA02PsDr2AFhYpmQZ58FCRot0JxsvdlVBgvBdfh-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Czyc2WLWDmH8oYoONuwN2zp8WSaVxkClQ-1bE8n3i6JEQtQdSOJnn6vaE_gQfhyj5C9mO0ePV6VQHdRMkfwbdD7uFQt64fXyka-5X12f3GVYP_AmkZTQUP8EgLaBIWe0IOfunGxN3ruOrzJb9gWLerhwJ1Z5q99mKqIu269RoN2ijpkXEdORbBzjBOOyuL4e95YDKJo2QzZ0vLx2fW2lAfPB8jao7msH0zhMNpKYntUAzjXdMeZt7xli3nmLG0BDy6ficmr4TCoU3HeutfnW2msOow0U-Aq9-W6lVRha2zS4oC3GuPDlRdxVtg6MQctrHKWWn8LwrD8SOwjPdeQUPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور علمای اهل سنت برای مراسم وداع با رهبری شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/665908" target="_blank">📅 15:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981c29129d.mp4?token=sewIuWgrU7wSrMEi-DUJpo3-ZYIzj5JcSC4p3escbDNJkm5Xlm75IcXjf2Tsttt6wFGB94FHRikW4mrgfQONK-uu_3V5QgAeu6fkafbpkg1l-FDQtbQZEv1maJl0PNTtG4i12xvty9MF0iLmmmf-9FMzofEkexblXoSv2TOvdhNW45MBg9qsWJSXBV9FfAL6Hmfr0bj8UKXxtgrZfzPADXhcV_BnQtuYBzIRLEp_4XRBBfIllJl3BDbgQbA_r31VQM_Nl11XlHqP0-IgGSvz0W6X5_47xhjUJBr7hNT82pFLhU9TELjaR5BDhCek8PUzsCHMb8diIH__8M_knWvMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981c29129d.mp4?token=sewIuWgrU7wSrMEi-DUJpo3-ZYIzj5JcSC4p3escbDNJkm5Xlm75IcXjf2Tsttt6wFGB94FHRikW4mrgfQONK-uu_3V5QgAeu6fkafbpkg1l-FDQtbQZEv1maJl0PNTtG4i12xvty9MF0iLmmmf-9FMzofEkexblXoSv2TOvdhNW45MBg9qsWJSXBV9FfAL6Hmfr0bj8UKXxtgrZfzPADXhcV_BnQtuYBzIRLEp_4XRBBfIllJl3BDbgQbA_r31VQM_Nl11XlHqP0-IgGSvz0W6X5_47xhjUJBr7hNT82pFLhU9TELjaR5BDhCek8PUzsCHMb8diIH__8M_knWvMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام «امامعلی رحمان» رئیس‌جمهور تاجیکستان و هیئت همراه به پیکر مطهر امام شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/665907" target="_blank">📅 14:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">باید برخاست</div>
  <div class="tg-doc-extra">KHAMENEI.IR</div>
</div>
<a href="https://t.me/akhbarefori/665906" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
انتشار موسیقی ویژه «باید برخاست» برای مراسم بدرقه رهبر شهید
🔹
رسانه KHAMENEI.IR، قطعه موسیقی با عنوان «باید برخاست» را به عنوان موسیقی ویژه آئین بدرقه حضرت آیت‌الله العظمی شهید خامنه‌ای منتشر کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/665906" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMvjab-bwsMypIrnIQInXhOpLXzFA8xuf9PHCKmmSUjyHMf2OgcsFmSKvyHquJvov54XKuTzCJdt6oTCQW-DNdAHNVxy9QvhD9-YG7zAjoRzsZWSkGoDduUvxDgiWcF-ibRjXf7YWAq0jN54i3DHZbUutbYMiyIUD0pxkkDI33vNqHWz5SAk19qdRSOt03b5XUVIVLVw_rgvSer_xyK_2YxDJfg7zV4ak6hHXlx11ggShNjh20Mx79lBgGEFVVIbi-Em1G7OEUDKxaARa14vwH-7TP0sHfkf1uRMxjkGb7uHOSd-25DprC9Bxn4Ll58bTzz-gQuo4c3rOw52_DeBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادبود بچه‌های مظلوم میناب در ورودی سالن ادای احترام مقامات کشورهای خارجی به پیکر مطهر رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/665905" target="_blank">📅 14:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57009bf7e4.mp4?token=ME5XUN5Cgn0B1LHXRiPa5LES04UW1ilk3SAaQVooYLsSXNaxGHhE9gp6D8ew-3GS_tUvSyx9B73jkZmdC-Vsyi5OhuTqJcFF3npzOhIIyZjsd-Pmt71JJgiQXxiabt4CSyM3lXhXfaLIInIm0MByrgTvvYSR6nFHOUs8w5RxPp7Hyzc2qlKvB0a9DDgU3RdOXbYUazCr3DPVbSfpxKV03yGWP7dDdWZdl6TIWn8tuT-5dtIk9EA-ZbT4DSs0YpGtooh_xg6xPXA2WsVcYfhopTKMM_t-HLF3vfPQ4xisZ1cDUPK1kXoKdz0XVM2an9TLkmOm-kcSIJF4esfH_ygTIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57009bf7e4.mp4?token=ME5XUN5Cgn0B1LHXRiPa5LES04UW1ilk3SAaQVooYLsSXNaxGHhE9gp6D8ew-3GS_tUvSyx9B73jkZmdC-Vsyi5OhuTqJcFF3npzOhIIyZjsd-Pmt71JJgiQXxiabt4CSyM3lXhXfaLIInIm0MByrgTvvYSR6nFHOUs8w5RxPp7Hyzc2qlKvB0a9DDgU3RdOXbYUazCr3DPVbSfpxKV03yGWP7dDdWZdl6TIWn8tuT-5dtIk9EA-ZbT4DSs0YpGtooh_xg6xPXA2WsVcYfhopTKMM_t-HLF3vfPQ4xisZ1cDUPK1kXoKdz0XVM2an9TLkmOm-kcSIJF4esfH_ygTIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفری حیرت‌انگیز از آغاز زندگی؛شگفت‌انگیزترین مراحل شکل‌گیری جنین را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/665904" target="_blank">📅 14:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
قالیباف: ایران بر اجرای کامل تمامی بندهای تفاهم تأکید دارد
🔹
محمدباقر قالیباف، رئیس مجلس، بر پایبندی ایران به ۱۴ بند تفاهم انجام‌شده تأکید کرد و هشدار داد که ایران در برابر هرگونه رفتار ناعادلانه از سوی طرف مقابل، با قدرت خواهد ایستاد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/665903" target="_blank">📅 14:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0b770706.mp4?token=XsZXZQ2Gu9IOkpmutnXH52w6JgS-G2WtKrCUCfjjVKhbPMa2JBnOhX4lGAUDyUrT27fKtQMEm8EwxMxK_hgvMF0Zyk86-BJnFY5Dzvsrho9jtSqkRqJvUEL8v9s2iPoLyrU0HqFJrz5FTFjOOrnMDI4u66Oj75jfPWnJfcgl2vKewm2j0rufcbWGA4xWHwTUpRWCNPbAG1voOn2GXvGgf2pih4GEkG3CsxPKE0FNrfimfBREnGQj2LTm3RbWsv7xGCtudM3LyK_KGdjox-HI2qeJfip3Da2UpiJhoD2WMMUIZFb0VBDOkTiMRSayAhVba8BcW9b7ET7SLrbnns1YQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0b770706.mp4?token=XsZXZQ2Gu9IOkpmutnXH52w6JgS-G2WtKrCUCfjjVKhbPMa2JBnOhX4lGAUDyUrT27fKtQMEm8EwxMxK_hgvMF0Zyk86-BJnFY5Dzvsrho9jtSqkRqJvUEL8v9s2iPoLyrU0HqFJrz5FTFjOOrnMDI4u66Oj75jfPWnJfcgl2vKewm2j0rufcbWGA4xWHwTUpRWCNPbAG1voOn2GXvGgf2pih4GEkG3CsxPKE0FNrfimfBREnGQj2LTm3RbWsv7xGCtudM3LyK_KGdjox-HI2qeJfip3Da2UpiJhoD2WMMUIZFb0VBDOkTiMRSayAhVba8BcW9b7ET7SLrbnns1YQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نخست‌وزیر ارمنستان و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/665902" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی ستاد تشییع و وداع با رهبر شهید انقلاب: درهای مصلای تهران فردا از ساعت ۶ صبح به روی مردم باز خواهد شد
🔹
در صورت فراهم‌شدن امکان بازگشایی درهای مصلی از امشب، اطلاع‌رسانی لازم در این مورد انجام خواهد شد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665901" target="_blank">📅 14:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادای احترام هیبت الحلبوسی، رئیس مجلس عراق به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/665900" target="_blank">📅 14:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75987c4611.mp4?token=lYtX8ypU7bfQraORmNg3koQwGtwGUo1qwN1cg3oQF7NskN6dZpns36OgMIq9rWvNuHCkKVHe2jLMrpMFIagBgXFsilEBkVsl5CGTrPh-eQlpV0uzZx3ecaLuYzwV_jxWNB1Pxp_hPA90nYce6Yj42L048wO7l7vvBZdrOcHt4QXoQev9ApEWF636T4Ws7LdbKK7xA-CKN6cHO3uKv7qzMomc9dxmh5HDpy7VvPprrQBjWZbAqNXStdXac6B62x8-Bxx28nF0i3UtYb2fDQEIx7PnJZVz8JlK7jMoY0q1OCv5WIzXtMwVlpBMCI5YH4oukug6brWbe8V3dKuwZSxoSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75987c4611.mp4?token=lYtX8ypU7bfQraORmNg3koQwGtwGUo1qwN1cg3oQF7NskN6dZpns36OgMIq9rWvNuHCkKVHe2jLMrpMFIagBgXFsilEBkVsl5CGTrPh-eQlpV0uzZx3ecaLuYzwV_jxWNB1Pxp_hPA90nYce6Yj42L048wO7l7vvBZdrOcHt4QXoQev9ApEWF636T4Ws7LdbKK7xA-CKN6cHO3uKv7qzMomc9dxmh5HDpy7VvPprrQBjWZbAqNXStdXac6B62x8-Bxx28nF0i3UtYb2fDQEIx7PnJZVz8JlK7jMoY0q1OCv5WIzXtMwVlpBMCI5YH4oukug6brWbe8V3dKuwZSxoSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفتگوی قالیباف با حدادعادل و اژه‌ای با عراقچی در حاشیه مراسم ادای احترام مقامات خارجی به پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/665899" target="_blank">📅 14:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6837ecae4.mp4?token=dbqHAFzyOw-pXViqpUuuy7bcrW1q0PiXEdwIW9jkGz7IwlhSX9GYeA9KgMy6CfR8yKrrFu-fYDcVOOuYntDQDPUJakwxY8QJpAPIITBB3uv25OM60PCrB67Ao09SIQB6B9hQTJTz8agOxhfaaAUh4qpaZAALHmWu6D3rcbeGkI2LbwhQJCadnKCLzwZChfMOXnYH1b8SHCP9WrKXxZJRYN2W310fi46lEapJJ3zo0T1HL2Kig8Og6sB38zuvGDjJ0HgOHlj2MUHPp7Cu5MSNBqLoXH8DForut62nBVapuJsWC4u8eb5tLzHbERDifqbkERg50yQ7__WFjH26dvP7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6837ecae4.mp4?token=dbqHAFzyOw-pXViqpUuuy7bcrW1q0PiXEdwIW9jkGz7IwlhSX9GYeA9KgMy6CfR8yKrrFu-fYDcVOOuYntDQDPUJakwxY8QJpAPIITBB3uv25OM60PCrB67Ao09SIQB6B9hQTJTz8agOxhfaaAUh4qpaZAALHmWu6D3rcbeGkI2LbwhQJCadnKCLzwZChfMOXnYH1b8SHCP9WrKXxZJRYN2W310fi46lEapJJ3zo0T1HL2Kig8Og6sB38zuvGDjJ0HgOHlj2MUHPp7Cu5MSNBqLoXH8DForut62nBVapuJsWC4u8eb5tLzHbERDifqbkERg50yQ7__WFjH26dvP7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های قالیباف و اژه‌ای در وداع با رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/665898" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKFGFEt4xmyxf2mIdCmgqu8QsxszWUE4WpmQ23zpdo6n_jMkOcHn3Ltb5avuo0eIGsTLpwSgXBlztcaao1mEBmFFU57wkMGoZl-9Y4fI7q6FMmPTeQ4QlZXJ2J68snGn608-iw9WGh3Q2SAmNCzL_oYzC1UQZWIie9dBtm3KHLzE-i4e-tLAixAoVGMHVfRh-el03h7urnfCXAjHWYSh0X0DDu_ThyiTls48nwEQaLlPJZg0VWmyBFaGJ4CUwEvGMBBYFPes4OIB5eDIzOV8wAZtUutmJHgsteMmDWWKzkXpkA1rmRWxT7mzeRLNNWoMfOVxgIcN-81vNTZ1RPBWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان برگزاری مراسم تشییع رهبر شهید در کربلا و نجف
🔹
مراسم تشییع پیکر مطهر قائد شهید امت اسلام، شهید آیت الله العظمی خامنه‌ای، ساعت ۶ صبح (به وقت عراق) چهارشنبه آتی در نجف اشرف و ساعت ۱۶ همان روز در کربلای معلی برگزار خواهد شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/665897" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad577cb8b7.mp4?token=oiGhuFSzG-1z05AFRbsuvgkIZBGSbgDgipBza2bRp-tLdOe2mEvFnF_QfEPrbSiY6wDwSIhBnk0EYaWtmVVmkQJ_CUi-1AdbKDtQLS4kXG7fdu1OFc62s2tkC5znNnHKB92IE8vJCYzvq1mxAc12K9nBuJIoq3zJKWVgeQS6-YR2ANm1ziJGTAcOP9brg-IQUSupki8ZoNPQin5lSGny7odgQ0uxxQzJK16JQ9PF2KXo7m-R9KbBysjCI8sxWqB93z-SqdphTcyUMWm3Z_mfG8VhoaftqCOjhc9HivBckqCr5VO4xTE6_c5vD4WF6Dvg0yBKyptTqClGK123TDFuAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad577cb8b7.mp4?token=oiGhuFSzG-1z05AFRbsuvgkIZBGSbgDgipBza2bRp-tLdOe2mEvFnF_QfEPrbSiY6wDwSIhBnk0EYaWtmVVmkQJ_CUi-1AdbKDtQLS4kXG7fdu1OFc62s2tkC5znNnHKB92IE8vJCYzvq1mxAc12K9nBuJIoq3zJKWVgeQS6-YR2ANm1ziJGTAcOP9brg-IQUSupki8ZoNPQin5lSGny7odgQ0uxxQzJK16JQ9PF2KXo7m-R9KbBysjCI8sxWqB93z-SqdphTcyUMWm3Z_mfG8VhoaftqCOjhc9HivBckqCr5VO4xTE6_c5vD4WF6Dvg0yBKyptTqClGK123TDFuAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید: با حاج قاسم رفیق دنیا بودیم، انشاءالله رفیق آخرت هم باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/665896" target="_blank">📅 14:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebH1YvGTUqmtJY4ff3ZMQOx_JwTa7NOK516jA_HEFduSntQKfYwele7o_Hn53oNhWNLjXRxePUEBJONXABYa89aXEfdI5Mdtmduq0ehgVBqp7lPYUQAwcihoEaG6WhRrSetmBAnraGAqP4-RBAlT0IOYqxnuDnn0fJJDJQSGW6CznafB-psPQwtXprPyoPkuug_2LGjRQIEnUt9EDALptHK86oyFHv2hPVPhrA75mufjC65cXvew3YyNxFu-zz2ZIQE-OOFFJFMIcbhkjxbIemR4ONkduwRatxa_TUYsSkRTo7DTkUeHty5eklfi3RUefsV7scd2hfAR6k9EeuevzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع پیچ‌ها و اسم‌هاشون بشناس
🔩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/665895" target="_blank">📅 14:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آماده‌سازی برای نشست‌های امنیتی ایران و کشورهای خلیج فارس
فاطمه الصمادی، پژوهشگر ارشد مرکز مطالعات الجزیره:
🔹
مقدمات نشست‌های سطح بالا میان ایران، عراق و تعدادی از کشورهای شورای همکاری خلیج فارس برای ایجاد سازوکارهای امنیتی و نظامی در حال انجام است.
🔹
بر اساس منابع او در تهران، این گفتگوها که به‌ویژه بر محور روابط ایران و عربستان متمرکز است، طی چند هفته آینده آغاز خواهد شد و ایالات متحده نقشی در این نشست‌ها نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665894" target="_blank">📅 14:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12142587d1.mp4?token=cQKzOxY8NNjgz8p0sd2gsuwL8UHDmsjXek9CPa87T-wfCQy0n0Lg5J5r4iuR4CfdOY8wXGR-Znc0_uriVNsdaCJ0iFi3O2xGvemD3Boy-tK1DJIhtT4shGbgGiK7nkyuZP8Eu10qzz9ltxaEiOnE8-n1rBL5tK4Kmfhs56j36NuyRrdQ6mdLuTzbH4uGf5MhEkg5ipjPTK4JT7g-J0KEbp_w7Yts8giUHsysMimSd6bnv7XHEFrMlIZ30QVrn7I2yR6yCXPDkY8y86V2XJ4-6ms3pLTlScjCmVbalp41fZbLa4m0Qc0XXqa23fplFD2pYaofvIeldJTSJ9sddaHLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12142587d1.mp4?token=cQKzOxY8NNjgz8p0sd2gsuwL8UHDmsjXek9CPa87T-wfCQy0n0Lg5J5r4iuR4CfdOY8wXGR-Znc0_uriVNsdaCJ0iFi3O2xGvemD3Boy-tK1DJIhtT4shGbgGiK7nkyuZP8Eu10qzz9ltxaEiOnE8-n1rBL5tK4Kmfhs56j36NuyRrdQ6mdLuTzbH4uGf5MhEkg5ipjPTK4JT7g-J0KEbp_w7Yts8giUHsysMimSd6bnv7XHEFrMlIZ30QVrn7I2yR6yCXPDkY8y86V2XJ4-6ms3pLTlScjCmVbalp41fZbLa4m0Qc0XXqa23fplFD2pYaofvIeldJTSJ9sddaHLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار وحیدی: دشمن تسلیم شدن ایران را به گور می برد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665893" target="_blank">📅 14:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6906509da4.mp4?token=PNzlyTPUl-u_A4sNypTOvDVi8sDpeD4njg50G0pYtP_Xm94h5VFLK8mGLnJylC_iRE8FsQfQOzcEUMs2ErrJ82nk0jFOBd_k9QcloxbJ6sTTT6Lbp1UTWI0R9KM5ZgjGFH6CdRg0d519GiVfW5T4IGKxqGEZ0mF3iHxVBD3Ouo8A5oYEhz05D5sutSVp-VdvD4gfIuIBC09psE_G3a0WqBb9XaHo9tFsnMfsBs5-B0dy3cibR9BiJoHYN3dTsQ1by6gXbo8tTBy0cVRn7Cd6q-yKSU6wd7DhoU_MRMowXsdDT7KJESEO1qpzMDRUHSit-sOT5zPt1fWHUTV3gq1lcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6906509da4.mp4?token=PNzlyTPUl-u_A4sNypTOvDVi8sDpeD4njg50G0pYtP_Xm94h5VFLK8mGLnJylC_iRE8FsQfQOzcEUMs2ErrJ82nk0jFOBd_k9QcloxbJ6sTTT6Lbp1UTWI0R9KM5ZgjGFH6CdRg0d519GiVfW5T4IGKxqGEZ0mF3iHxVBD3Ouo8A5oYEhz05D5sutSVp-VdvD4gfIuIBC09psE_G3a0WqBb9XaHo9tFsnMfsBs5-B0dy3cibR9BiJoHYN3dTsQ1by6gXbo8tTBy0cVRn7Cd6q-yKSU6wd7DhoU_MRMowXsdDT7KJESEO1qpzMDRUHSit-sOT5zPt1fWHUTV3gq1lcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام حداد عادل به پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665892" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc36adf0d3.mp4?token=arm-pj53KbncWPRW-mKZAKhtPofs-VHnsEPxL3wFgbr1Cg6_DcOQacZZ5zl98Rhp0QfqbYCyGFp6-brGuUagV1t1NsG7tLyj7_IW4kjm7vLcjs6n0-VEs5I8p-qnvhMLA1FICo1-pxVjrLLUYdAnaDPl8XUTDZThG8xoQ59EDMb332ZlP300idNmRHbRi0g6MBITy62GuMasjYi1qa8cKorlSSoXKAUih30Z11AS2Lnv_eJjJkNwgejC1Let49OK_G8om-jHrmJkPdwWgyAixh10Wc7o8SmPvMMHfTqbjQlHsBD7xWRnWmGvD234zwXq_Gj0bFcLJM5tn3KU1S5k4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc36adf0d3.mp4?token=arm-pj53KbncWPRW-mKZAKhtPofs-VHnsEPxL3wFgbr1Cg6_DcOQacZZ5zl98Rhp0QfqbYCyGFp6-brGuUagV1t1NsG7tLyj7_IW4kjm7vLcjs6n0-VEs5I8p-qnvhMLA1FICo1-pxVjrLLUYdAnaDPl8XUTDZThG8xoQ59EDMb332ZlP300idNmRHbRi0g6MBITy62GuMasjYi1qa8cKorlSSoXKAUih30Z11AS2Lnv_eJjJkNwgejC1Let49OK_G8om-jHrmJkPdwWgyAixh10Wc7o8SmPvMMHfTqbjQlHsBD7xWRnWmGvD234zwXq_Gj0bFcLJM5tn3KU1S5k4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان وارد تهران شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/665891" target="_blank">📅 14:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bbf502005.mp4?token=l9VjOxFZiibsapJx1B51sk7ajbOkBKJqByeeOEiND08kA39T2q9Ch9WJJSW5JCadlKM-SM5I6I3T8qKKVwcVwkoLJ8PM-AjAqS0wVk7Rx02LGOZ5-3gsgiJbAyqfyJ9NOnPtjYyYGpRoRF0p878HnPFq7FjfHYqmC4vGQBys7kEBYHS9WYxRdGyO78wXl9Oj0avpnhi7kkpSZ3s-HP0PJh7UKTxskgi8WndM-4EK3LnRoQlWOXUeC6R_bNRXgo6QidtE7erJ3gGoU67TfZ_Nwv8p2xyWKP6YNKnMKSurFAEVv_xWmJYx9ctISf9l3hmzXdTwiD1O7rJfPvhd9Zf44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bbf502005.mp4?token=l9VjOxFZiibsapJx1B51sk7ajbOkBKJqByeeOEiND08kA39T2q9Ch9WJJSW5JCadlKM-SM5I6I3T8qKKVwcVwkoLJ8PM-AjAqS0wVk7Rx02LGOZ5-3gsgiJbAyqfyJ9NOnPtjYyYGpRoRF0p878HnPFq7FjfHYqmC4vGQBys7kEBYHS9WYxRdGyO78wXl9Oj0avpnhi7kkpSZ3s-HP0PJh7UKTxskgi8WndM-4EK3LnRoQlWOXUeC6R_bNRXgo6QidtE7erJ3gGoU67TfZ_Nwv8p2xyWKP6YNKnMKSurFAEVv_xWmJYx9ctISf9l3hmzXdTwiD1O7rJfPvhd9Zf44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه با گوشی، روایت بدرقه کنیم؟
وارد رسانه شویم تا احساس میلیون‌ها دلداده به رهبر شهید را ماندگار کنیم
🔹
لحظات ناب و تکرار نشدنی را برای آینده ثبت کن
🔹
هر گوشی، یک سپر دربرابر تحریف روایت
🔹
خبرنگار حماسه بدرقه باش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665890" target="_blank">📅 14:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b419c1671.mp4?token=TrNDJVmm42cKWCXojGghLUUeDrNihKe-HdXMrxgjA4SbXrH57t7rFXIUq8RC-ZwL1RfZu6PKyQKOUHEVEC775QTvm5-r4KWILOOIusAAxQBMGrfwKhT-0XHW3bOfe_oH-85BYCtnEK4zYZxPvsN-yq6lh7F__5GTtUXEAoQnZ7xNs9bQCbcHYqSxNedhqZ4LjbLb0ZAh1dF6reDwK7zJf3RilMJhBL78ymKMxWMaqZnP3tvKLSrgo7FXUottVLWmhyWyMd_JcGkbxI-sV6cste8xOWP-Gqyy-ovqcSMVK2osMjcuztMlpquIuiZVsZKLk0ezSlTUo7Mj2u1E24lEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b419c1671.mp4?token=TrNDJVmm42cKWCXojGghLUUeDrNihKe-HdXMrxgjA4SbXrH57t7rFXIUq8RC-ZwL1RfZu6PKyQKOUHEVEC775QTvm5-r4KWILOOIusAAxQBMGrfwKhT-0XHW3bOfe_oH-85BYCtnEK4zYZxPvsN-yq6lh7F__5GTtUXEAoQnZ7xNs9bQCbcHYqSxNedhqZ4LjbLb0ZAh1dF6reDwK7zJf3RilMJhBL78ymKMxWMaqZnP3tvKLSrgo7FXUottVLWmhyWyMd_JcGkbxI-sV6cste8xOWP-Gqyy-ovqcSMVK2osMjcuztMlpquIuiZVsZKLk0ezSlTUo7Mj2u1E24lEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام خانواده امام خمینی (ره) به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665889" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbGlPehdMKKM-JKtGNYZePTD8ZvzJcGZB07AedYNTt3lHKb7TbQ__6cYCxvA7GR3hA7EyIlxzhtBfOYNfnp6eYrcClI8NP18y_HbkAPbueoW_PpDYCg9Tbx9L_Y3YOHR53jIHkqxr24ygzPuCS0wy4MuQ0tbCnoPoFgZZS_3YqIM6OFjkRqshWzb4lBcH33fiFFtSzjjSsf2mwn1cluXrD6pi565tg5OHR1dWySwEVHK89epB9tcVWsZOMTx9QZEoOirlIG9zE8r85RjA-PGOcqEodaN59TwBLNWoFa4vovDDbRCOvh7mRhPRnygtKabjCouE2fLW5GlbqbegMoGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کت چرمی «جنسن هوانگ» به حراج می‌رود؛ ارزش‌گذاری تا ۶۰ هزار دلار
🔹
کت چرمی مشکی و امضاشده‌ی برند «تام فورد» متعلق به جنسن هوانگ، مدیرعامل انویدیا، در حراجی Sotheby's عرضه می‌شود. قیمت تخمینی برای این یادگار، بین ۴۰ تا ۶۰ هزار دلار برآورد شده که با قیمت تراشه‌های پیشرفته‌ی Blackwell انویدیا برابری می‌کند. این حراج از ۱۶ تیرماه آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665888" target="_blank">📅 13:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zsob_WRr4fBFLdS3kZODWrEHwd401cpfQ4e50nm9HrqqrM6HirVp8EgOKZE2XrRsk2UxVKufvefxu-V3R7c4t5xOZloUdiK6QkIgW1pwUwY1Y4KY9BM1x9dWP0mOOpE8ByTgOQmhx1hGiXmokANIc7G5R-5WBsSt1g18GGPfXAekOmRHVxjU6k_SPp3v-HtNxiOvxV-hZtbTkwSSFLYnnztgHj8mjvIcyjez6Plhh-IuyDNnGSIWOJgwkWEZrFUyQRxd-Td73_05LMnZx4xgrSEfI41i_S64fXE-heCcaTfgOTITRbdND9XYbJxtGaBDxwoxWVIrLYtMZJ2U3mmF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر متفاوت ورود یکی از نمایندگان پاکستان
🔹
مصطفی تهرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/665887" target="_blank">📅 13:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284edbc04f.mp4?token=aHXPpVW0h7XLQHyeKDY45GHPEn3HXjHzy9dc1M9vHEl3yohL7xUGB2O_f8Pjc1vtfZluVZ06gvzv5DjfbZuuCdpsHKXgW-vY9jY2CI9f03Z-q6n_LIL3GaVgMnw1TgaprgAYrw5ISht6SWahsL4XI3BiT-TF-2qVFXKoAIwzNQvF8o28voCrNSByFbDQ-q6sCrM_h3ITHVGxiPzne_AAf84szJH9IcKzW3u0XXy6p6o7xmjEkmzBcwCm0He0BNlDUgykpqe3sJTEc4ev6EF5mE9mIjokO539eT--YJAAxTGdwfpQEyEIiGNy881xFErXx4Gqb7bHm-aUkAshaKwWPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284edbc04f.mp4?token=aHXPpVW0h7XLQHyeKDY45GHPEn3HXjHzy9dc1M9vHEl3yohL7xUGB2O_f8Pjc1vtfZluVZ06gvzv5DjfbZuuCdpsHKXgW-vY9jY2CI9f03Z-q6n_LIL3GaVgMnw1TgaprgAYrw5ISht6SWahsL4XI3BiT-TF-2qVFXKoAIwzNQvF8o28voCrNSByFbDQ-q6sCrM_h3ITHVGxiPzne_AAf84szJH9IcKzW3u0XXy6p6o7xmjEkmzBcwCm0He0BNlDUgykpqe3sJTEc4ev6EF5mE9mIjokO539eT--YJAAxTGdwfpQEyEIiGNy881xFErXx4Gqb7bHm-aUkAshaKwWPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های سران قوا در مراسم وداع با رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/665886" target="_blank">📅 13:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1453b1794.mp4?token=JM8pY9jirbH9xWzBfU4ETdmPdOpTSrxyGaRtRI46dxB8HpNR8Yb2Uq0ly82vROlXjq218hgHMCtSXDd5ZHWzlue8iDO2oeMIXClV5lrjCqsqedsucWPdkTNuXiOLejdA7JrscSGdg-ogTbdJsxado0HgZEjNMBNYJ9MLq-TlWc5ViFOtJQiUqJuMLGqbv1nPCCy5Heodhapw4GZImLfpjkrUtaT6rj7O3KyEEYziAglKJA_eS_kPgvfz9TyisdsnvpOg9HSEusKfOC7CCCEIuMifQN_5ppn47uS4eYhtGzOo5RYpXgeu5Igdk927Q6X_giX5TMfCzzJeIIHm9ihvDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1453b1794.mp4?token=JM8pY9jirbH9xWzBfU4ETdmPdOpTSrxyGaRtRI46dxB8HpNR8Yb2Uq0ly82vROlXjq218hgHMCtSXDd5ZHWzlue8iDO2oeMIXClV5lrjCqsqedsucWPdkTNuXiOLejdA7JrscSGdg-ogTbdJsxado0HgZEjNMBNYJ9MLq-TlWc5ViFOtJQiUqJuMLGqbv1nPCCy5Heodhapw4GZImLfpjkrUtaT6rj7O3KyEEYziAglKJA_eS_kPgvfz9TyisdsnvpOg9HSEusKfOC7CCCEIuMifQN_5ppn47uS4eYhtGzOo5RYpXgeu5Igdk927Q6X_giX5TMfCzzJeIIHm9ihvDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام روسای قوا و رئیس مجمع تشخیص مصلحت نظام به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/665885" target="_blank">📅 13:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhzzmYOVMdlcrbx94Y4Vwd0V6967UkyZz_xTaq_ZqUDzEE9x2kVl0gygQvZC89e_Y2OcN9oTm7NiV3hFsNsWYO_azdOFwUr_tRKPAPK25h8rEFndLQK9E-zI8yEUHju2Q2uBQRjpG6bVpamaDl7tEIAoZIBf0nCkcknjGcOGlxfzfJWw7FkxdPfBA52_4fFDGzxwajZ8_l8QmK5P5QNAMvX7A2W8WkknBE1efMPyHfV2_WuKBy2CO-O8K5ZCQCK6-kardVYBn5GJMSR8A3GdPVzw3vII5P9FrT06Ok5d1B9dfxrM8sYpyKZnjYE0M-qHYg2nnPSdChwBh_-3EhTDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله سایبری به سیستم بانکی امارات
🔹
خبرگزاری دولتی امارات (وام)، اعلام کرد که این کشور مجموعه‌ای از حملات سایبری علیه بخش مالی خود را خنثی کرده است. مقامات گزارش می‌دهند که سیستم‌ها همچنان ایمن هستند./ الجزیره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/665884" target="_blank">📅 13:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMALaXCXjRIPpF5WwrC0TB9Kw2jFYKTtGPnHkm_lYd-P58E6hfb8fm5KequkfCa075OnaKmCadB6-EBy9xeTsnW5WBVSH5HGGOav9e4joakPd5hXmp6vKxM3qvfgH6OyAbwRP0F09OXuAU_RSGLvrk_mtfHYMplTvBPnMZYMfVhrLnEoneAAFqxz48OC1e7SAnwGaO-97KnntaPQg9HQuYwPy0BPgEWl_toW042eCCR9Bc4Oy16e4ZLVDl83Yrmz6UZesduVztd-vQgl2VkRBotvlDb5rPp9u7_AfHjFGeFjkDdcdrIq8bjXgYlTZQCJrED13TrazVfPjyshP6VpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن پست: اختلافات آمریکا و اسرائیل از ترور لاریجانی شروع شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/665883" target="_blank">📅 13:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
در چین، در یک شهرک مسکونی، روی پشت‌بوم‌ها سیستم باران مصنوعی درست کردن که می‌تونه در چند دقیقه، دمای محیط رو ۵ تا ۸ درجه خنک‌تر کنه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/665882" target="_blank">📅 13:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عاصم منیر فرمانده ارتش پاکستان با استقبال وزیر کشور وارد تهران شد
🔹
رئیس مجلس قطر وارد تهران شد و مورد استقبال نایب رئیس مجلس قرار گرفت
🔹
شهادت مامور پلیس کرمانشاه با تیراندازی افراد مسلح؛ هویت فرد ضارب شناسایی شد
🔹
هیئت‌های ویژهٔ افغانستان، چین و نامیبیا با پزشکیان دیوار و گفتگو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/665881" target="_blank">📅 13:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/717f98956a.mp4?token=Se0VRtqO_Bg71ytc3I_-yTNdE_p2mLpNgZI0a1tkTR-KeVxBi7NAdID8sMvmAq4I5anKujUbkfGayfrf-C9it7X4hXojOjkyMwB7JOnINdIojmfDdX1zq3G3BPf6iQbxen41YFgLSNQx1cYEExVupsT9aG5qHNl8v4hzHJbzC5OcnVOjfRHUScWfbqsfHs08XTD75Gw2EXK9Y0nbvQFVYPqub6zn-vg43U25AbLbDFD1Xo6Hbzqn0-mrGAup05Swf49tp8NLT6C7meIrmGqKxBG-yl9nleV1eapYQGX0OIMRY4X1GFEgjozX8x12ZdTjl-7CNitW0Y2DlVr9l0TS9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/717f98956a.mp4?token=Se0VRtqO_Bg71ytc3I_-yTNdE_p2mLpNgZI0a1tkTR-KeVxBi7NAdID8sMvmAq4I5anKujUbkfGayfrf-C9it7X4hXojOjkyMwB7JOnINdIojmfDdX1zq3G3BPf6iQbxen41YFgLSNQx1cYEExVupsT9aG5qHNl8v4hzHJbzC5OcnVOjfRHUScWfbqsfHs08XTD75Gw2EXK9Y0nbvQFVYPqub6zn-vg43U25AbLbDFD1Xo6Hbzqn0-mrGAup05Swf49tp8NLT6C7meIrmGqKxBG-yl9nleV1eapYQGX0OIMRY4X1GFEgjozX8x12ZdTjl-7CNitW0Y2DlVr9l0TS9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار ابن‌الرضا: اگر در حین مذاکرات نقض عهدی ببینیم در میدان پاسخ می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/665880" target="_blank">📅 13:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxQsykXo7-SrLf_FBlTrXcecPzNmnJgTgg_7MNQQ1HysMLGesXjaoNo04SZJRpZzurkZ57tIYXeKQWEuHSVcMA3FkJMGTu6jTU4B0qdTUGwgLfp-xKzUNSc9oBjlu5NEvp5hLZu85F5Zn5t-XMWpIYfdNnycFGtuL8FQerqbMI1fB2yJPpC4hUPOChlhM7I5il2aq_OFjGHJ9TwcqYQ2BxLRjEsC7vrDhCZ2wEVpTyLmj1bkctMJ4wMzeKyPxp7-2UFFAjigDVaaw3f4Ox5BD9UUTjYwuuuEZ6m19-c1yR_yUEEdd9_U_VhNXtHakFFI64AXCa9Fz7Z06vvAJka5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار نخستین‌بار؛ دست‌ نوشته‌ شهید مصباح‌الهدی باقری برای رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/665879" target="_blank">📅 13:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH7yKTp98tShOuWNmYaQU14j4BmygtL35x8TIhmY3g92rFunninBYtW0qMWOvs4ncjBd3_jB-KjH8WGPD-vLR9ZEdM048fdY060FA3sJlB0V_sthIDPXqAADLz36DmHSj3ElxSVAMhVXEyMgK7KoAnkKYjgzHoIm5DZTSk9DPB3KeXO6Gfr5JszbNz4LDwnhkd2IV-57tXz_urpS3gLIE7_5KVztLnf7THm4sA7_nnyLWBuwPPHhbThlBHb-7dOaAkpdQcPFeTh1eyYl1g6Q4xU15wptcScmOXuiyhhA67FqEhYSFJFSpCNzNM3yICuViP3-3ofVOSuOU4wkCA11aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه کفش و کوله‌ای برای مراسم وداع و تشییع مناسب است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/665878" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86a8bc2e2.mp4?token=UMm7rXgh0HhC86IEgBM4NHOH0HP3syDblmF63z7QntbndqAVTEzT1afCXfFboazCZxyswfRf8yFr0YzIDlsmmJFT4Gc1iInAl4Be4Ki1Rtsk8WEe6l6dhS7dAuv-6iGyEPeyaUi_HwuEHjrLqpUQNAWoyXILOndnYyL7wReTIsiAeO4H8VqPLHkWdIAzSfCCdljxRaMggu0n0sg6VTS8wTKlYv5fek3QGBQ-l_NULhYFIGQxxcyqm48e3_B17ay3A7AIM1nt81EI67pX_1jSHdY2Oh8SD7KKjh21SoM6uesGDkTe8a89wnURhaL2UW-e05eoptWfAE5hFAC-zXo4SiHvHq27HGOPZujHefvN1WMRPiVzi7XCs3wUDJVgoMLKI7pl8EWpOyzrM6gKLvQ51UspWJoUbtNqqbqe4uHPvp1FT48W4flxmB6-Bc90tHQk8_GUv6JiGc3m2WIP7VqYSTkHY22Io8BlPxFlITZNQkWALrv0RcAkZYt0dcE_tOFr8vHjjDFBb6r-QRDBoGkXakAuTFOMU9nOuKVitz4e-HfcUhLlFXLMAa5sJ89JhEtgBZOMp_rhdjwsim665YPp5AjkkvVmptHEyzAnTiu6lScLgNJLX99W2zAxSQXMNzGYVVh2TO0d6y5LUC3X2XM_GDIvEv11flfpJ-RyR-B_2JI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86a8bc2e2.mp4?token=UMm7rXgh0HhC86IEgBM4NHOH0HP3syDblmF63z7QntbndqAVTEzT1afCXfFboazCZxyswfRf8yFr0YzIDlsmmJFT4Gc1iInAl4Be4Ki1Rtsk8WEe6l6dhS7dAuv-6iGyEPeyaUi_HwuEHjrLqpUQNAWoyXILOndnYyL7wReTIsiAeO4H8VqPLHkWdIAzSfCCdljxRaMggu0n0sg6VTS8wTKlYv5fek3QGBQ-l_NULhYFIGQxxcyqm48e3_B17ay3A7AIM1nt81EI67pX_1jSHdY2Oh8SD7KKjh21SoM6uesGDkTe8a89wnURhaL2UW-e05eoptWfAE5hFAC-zXo4SiHvHq27HGOPZujHefvN1WMRPiVzi7XCs3wUDJVgoMLKI7pl8EWpOyzrM6gKLvQ51UspWJoUbtNqqbqe4uHPvp1FT48W4flxmB6-Bc90tHQk8_GUv6JiGc3m2WIP7VqYSTkHY22Io8BlPxFlITZNQkWALrv0RcAkZYt0dcE_tOFr8vHjjDFBb6r-QRDBoGkXakAuTFOMU9nOuKVitz4e-HfcUhLlFXLMAa5sJ89JhEtgBZOMp_rhdjwsim665YPp5AjkkvVmptHEyzAnTiu6lScLgNJLX99W2zAxSQXMNzGYVVh2TO0d6y5LUC3X2XM_GDIvEv11flfpJ-RyR-B_2JI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احساسی‌ترین صحنه جام جهانی بعد از بازی آمریکا و
بوسنی
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/665877" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0edb585c.mp4?token=pw8bf0E5yEWR9QpmxKCvV8x1TZki_4FaP3Plic3961GS-rgm8C8Z4aYqpT2Lto-TVcS4qa70NOOzRYQyc_QrjXSxP5uT3tqpCXHX6aWCco2fgZguwBTGB-J8rE3Q8HoWPumW_TQ1xaGaLEdNkI6QSQqkCkldpITxPNC5WULzTj-TXAoywdwDs_ClXsMiEBNQGOa4kRPzqE8tMT84evwEHwNfFsxdihMJ7cbyUbc7GPdEbkvHhcp5_YcIdAqsp1ga4AA6MdmKSMX2Lv6VarQEL6j0NbvSKThkpv5-AKSdREGAEqxQgLrCB39kvKzzFGm9YLVFbYzHy3nqcn4_piel6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0edb585c.mp4?token=pw8bf0E5yEWR9QpmxKCvV8x1TZki_4FaP3Plic3961GS-rgm8C8Z4aYqpT2Lto-TVcS4qa70NOOzRYQyc_QrjXSxP5uT3tqpCXHX6aWCco2fgZguwBTGB-J8rE3Q8HoWPumW_TQ1xaGaLEdNkI6QSQqkCkldpITxPNC5WULzTj-TXAoywdwDs_ClXsMiEBNQGOa4kRPzqE8tMT84evwEHwNfFsxdihMJ7cbyUbc7GPdEbkvHhcp5_YcIdAqsp1ga4AA6MdmKSMX2Lv6VarQEL6j0NbvSKThkpv5-AKSdREGAEqxQgLrCB39kvKzzFGm9YLVFbYzHy3nqcn4_piel6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده‌کل ارتش: با اراده‌ای محکم‌تر به دشمنان ملت ایران اعلام می‌کنیم تقاص خون امام شهید و شهدا را خواهیم گرفت
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665876" target="_blank">📅 12:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJMACxyzaBFE7MZr98BHJHNH7baHiW-5lNqPl9hjo8dnv_KGL9OUhFfj6UY1ndNLgWaKzXLMeWDfERxw3Xisu1XQQj1bjiH4H5KlTCCfFHoOxT6wTL0j6uyt0RLELsE-vFnYO8e5LzClekYU8N5oApERzZ035A2VkE6V3yvXQi3vNFiohvgvXtcK-hhzg9J2m6rw84EPuouAcJrKxbqBK1zaaEnsYfYK9kGo0ftAWXfm4QcaQP3wYDFuO2mVpuASTt7CDqFRA-w6Jn2s0DgB7vq1QAZKw5EgcKC_4V5mo3wMzg2JjJI8Yu5u2walsFTIf46UjbtC0czADcu1_KPrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار رادان هیچ صفحهٔ رسمی در توئیتر ندارد و هرگونه اکانت منتسب به ایشان و همچنین ادعای بمب‌‌گذاری، کاملاً بی‌اساس و کذب محض است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/665875" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665873">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206ec001f2.mp4?token=u_HawngVF0F5RKq7X8uwc83UMIomHHgUSkljfgiU5UCBwJ7HClFLOebnWzbGnDPAlSsQ3AVii4ZSP3q294TFDykTjUiPbFUBIcrSUZQHN7k8u-LrGd_qRmUspq6vFynlCBcJR07zhUcQWds0rJCiNYhR47tCFz3oucOvac3036RwJ4msNbLoCS7ZNVnwAdXpXZFerH0Csm4TvcrPtArr78c7UaUGkaOen1fBZZp-OYSqR8EJuSYBxgiMwCFjTNlj_QLPQECpmXuDQ4MzRFFyme-qpOP5lKrukWXm107DxBGybgLv6O8lqj2mBYqzaAJJEIxR1zLHO3ZH4WkTZ2nHHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206ec001f2.mp4?token=u_HawngVF0F5RKq7X8uwc83UMIomHHgUSkljfgiU5UCBwJ7HClFLOebnWzbGnDPAlSsQ3AVii4ZSP3q294TFDykTjUiPbFUBIcrSUZQHN7k8u-LrGd_qRmUspq6vFynlCBcJR07zhUcQWds0rJCiNYhR47tCFz3oucOvac3036RwJ4msNbLoCS7ZNVnwAdXpXZFerH0Csm4TvcrPtArr78c7UaUGkaOen1fBZZp-OYSqR8EJuSYBxgiMwCFjTNlj_QLPQECpmXuDQ4MzRFFyme-qpOP5lKrukWXm107DxBGybgLv6O8lqj2mBYqzaAJJEIxR1zLHO3ZH4WkTZ2nHHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک توریست آمریکایی که به تایلند رفته بوده، پشتِ صحنۀ عکس یادگاری با ببرها را به اشتراک گذاشته است
🐅
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/665873" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665872">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd9198640.mp4?token=tSc-LPypei3Vz93rrEKeKbExUfEI-E4Wl7MUK3iO_7pKMFM0FR2F4V4JweoEFA1TULrggQp61gUppjd8fL-9ZI_ocyicqrPNgSFcfRHLSB7OcWD4In2K9HXY2dHv9BaAbJYqYZRa02ZN8kBQVj7NpapUzlLz4Vv_CODx7w8GJapFUi2ncV7BcvJEYoL8KVu0KEHDiHcBfg2h9wOk6t3k91MuDRh_oY9hj3Ygw47xToe9mPEaNQ_x-B6UKzquinfOp4i-j3yDtJZpytFQUCYPENT-V9LKSV4UNTREyP7XKr0kBR8tiBpB-lFa7f4BtTDn_IN_2xCvksKyLCwv6HbysA8wDnzkCfIi_tUi5LKozuepHMaELTwhQ3Kp4JS3WDmfiZ_op4i5ZkB6cVzksRtIpUeCMqtZtAW8VnQ280EMRazD_4tyV2kul79JeoNqXcti-rBA0qLHUVEKUX4B1tXl0Cs4lBjGWMNqCWKN6xoXBDArBc-X-IxzjFNTw79rClcT6gPA0nsTbvgDN0SD1iUAVL3ALLq5cDELuLlvqGWwoQwa83wPIYRrRKgRoa_2wyfk_cSP0Yu9s4soSe-YmYSekfVYr2JW0OqdXKZaMFHfeNZdQ9X1wuPL8twmmRKKWQCG5mbmJTsi4yvuruiieJRVViJSYVUOSldMAehpqDH5q1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd9198640.mp4?token=tSc-LPypei3Vz93rrEKeKbExUfEI-E4Wl7MUK3iO_7pKMFM0FR2F4V4JweoEFA1TULrggQp61gUppjd8fL-9ZI_ocyicqrPNgSFcfRHLSB7OcWD4In2K9HXY2dHv9BaAbJYqYZRa02ZN8kBQVj7NpapUzlLz4Vv_CODx7w8GJapFUi2ncV7BcvJEYoL8KVu0KEHDiHcBfg2h9wOk6t3k91MuDRh_oY9hj3Ygw47xToe9mPEaNQ_x-B6UKzquinfOp4i-j3yDtJZpytFQUCYPENT-V9LKSV4UNTREyP7XKr0kBR8tiBpB-lFa7f4BtTDn_IN_2xCvksKyLCwv6HbysA8wDnzkCfIi_tUi5LKozuepHMaELTwhQ3Kp4JS3WDmfiZ_op4i5ZkB6cVzksRtIpUeCMqtZtAW8VnQ280EMRazD_4tyV2kul79JeoNqXcti-rBA0qLHUVEKUX4B1tXl0Cs4lBjGWMNqCWKN6xoXBDArBc-X-IxzjFNTw79rClcT6gPA0nsTbvgDN0SD1iUAVL3ALLq5cDELuLlvqGWwoQwa83wPIYRrRKgRoa_2wyfk_cSP0Yu9s4soSe-YmYSekfVYr2JW0OqdXKZaMFHfeNZdQ9X1wuPL8twmmRKKWQCG5mbmJTsi4yvuruiieJRVViJSYVUOSldMAehpqDH5q1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشه‌‌هایی از سفر رهبر شهید انقلاب به کرمان با لباس مبدل پس از زلزله دی ماه ۱۳۸۲ شهر بم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/665872" target="_blank">📅 12:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665871">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZZ8d1urVysIeg1KyLvEp0jDEp56mcYyTy_sAVAS2mw6205eBl4hp5qOHw5r7rFcOxDKyV85_h7_Kn-Mmhnu59biEtPQknJHY3FEJ60HEEb_LO4_MUPiwKaPzESynPynMLDA6nBNmcEf0eXyJa6kA31ekJBX7Ypq1dJSTHadH4RJ3bPYYQaeoQb7D4sR0nXRzuWILtjcQPuoVJYriTPwJ5OBeZuXOweWseXML6CoYTOEQwIPIvwPf8vFPAZI_JJei9SfF0r3r9diHhRmGNP8-hoxJUIWCmS2uAYKiplHQ5GiPbtzsrcbpqCCbcr6abV610Sc1JGeysfh2QNhF6ILug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | حضور به نیابت از جاماندگان
🔹
اگر در مراسم تشییع رهبر شهید حضور خواهید داشت و مایل هستید به نیابت از افرادی که امکان حضور ندارند شرکت کنید، آمادگی خود را به خبرفوری اعلام کنید.
🔹
در صورت هماهنگی، اطلاعات لازم برای ادامه فرایند در اختیار شما قرار خواهد گرفت.
🔸
برای اعلام آمادگی و حضور به نیابت از کسانی که امکان حضور ندارند پیام دهید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/665871" target="_blank">📅 12:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=UoiooKzpYiLUFH-FX6POb8v2GC9cuSUhTg-6GPr91xaP7HDMWKpqRF4qcIRFy9MGSsSjctPhsCEY1jxZcz5D_1q3v7eReKIbK64pXFndmRIj_YgtxhTHHY6FCvgAOZ_YdqNd1hUlbwpclE0gHuZu4WxRWvJJeRf3c4ISj9pZUqOXPhEp1q0PnAlC3TNVvLia8_8ENmWTfM78rZgk1FT1VZvS6bYxGt1xbZfw-0-lyKSmiw3C0jD-s8uNa5DeclzFUcZe63yI4K4BCFBC82-zAxqq0FKDU9hPYkU8zH_rNDvHSw-7J5kRnMygLu7ordeNWat29lf_M_7DiFtHQTYnzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=UoiooKzpYiLUFH-FX6POb8v2GC9cuSUhTg-6GPr91xaP7HDMWKpqRF4qcIRFy9MGSsSjctPhsCEY1jxZcz5D_1q3v7eReKIbK64pXFndmRIj_YgtxhTHHY6FCvgAOZ_YdqNd1hUlbwpclE0gHuZu4WxRWvJJeRf3c4ISj9pZUqOXPhEp1q0PnAlC3TNVvLia8_8ENmWTfM78rZgk1FT1VZvS6bYxGt1xbZfw-0-lyKSmiw3C0jD-s8uNa5DeclzFUcZe63yI4K4BCFBC82-zAxqq0FKDU9hPYkU8zH_rNDvHSw-7J5kRnMygLu7ordeNWat29lf_M_7DiFtHQTYnzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع فرماندهان ارشد نیروهای مسلح با فرمانده شهید کل قوا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/665870" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665869">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
نیکزاد، نایب رییس مجلس: هیچ تردیدی در خون‌خواهی رهبر شهید و شهدای جنگ تحمیلی وجود ندارد
علی نیکزاد، نایب رییس مجلس در
#گفتگو
با خبرفوری:
🔹
اول باید تاکید کنم درباره خونخواهی رهبر شهید و تمام شهدای جنگ‌های تحمیلی اخیر بر کشور، هیچ تردیدی در میان مردم و مسئولان وجود ندارد.
🔹
آقای شهید ما، تمام مجاهدت و تلاش خود را در طول عمر با برکت و زندگی سیاسی و دینیشان بر حفظ استقلال و عزت ایران اسلامی گذاشتند، لذا ما بر حفظ استقلال، عزت، اقتدار و تمامیت ارضی خود تاکید داریم.
🔹
اینکه دشمن به اهداف خود نرسد و هژمونی ساختگی‌اش برهم بریزد، برای ما از مصادیق حرکت در مسیر راهبردهای جدی رهبر شهید و رهبر حکیم فعلیمان است.
🔹
باید تاکید کنیم که خونخواهی زمان، موقعیت و وضعیتی است که مسئولان کشور و در رأس آن رهبر فرزانه انقلاب اسلامی، به خوبی در آن اقدام کرده و همگان حصول نتیجه را مشاهده خواهیم کرد.
🔹
قطعا در این راستا دشمن‌شناسی همه‌جانبه، حفظ وحدت و انسجام ملی، پرهیز قطعی و جدی از دو قطبی‌سازی که رهبر شهید انقلاب بر آن تاکید داشتند، از الزامات است و در این راستا تقویت بیش از پیش نیروهای نظامی نیز از واجبات است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/665869" target="_blank">📅 12:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdA9lzoF_0HqjqCyCsSDvk3Ps7q5Hh4cgrawg8nLbewZQssTj3jgIPeO4kjumGnjmyrKyNMYupGR096SPE5r2Eg2Z1X1bjx2c7LT_03v5IxGkIIElrFgWHQDhpi8VAZTUXsU8WxYRL7K7ilcDNwsjLuW0JMJkRZA3jsqfpaiqECl3KJhfpHLpPXOWlokaR0Jsjc4Z4aQ22UG0SZKlVbxiQL2vz6HLVZ0FKeRQBfkZwGuYYcP8SL4VN6mAQb-5WvPZzb__9d-5AsO-irGM4bJOUf30U1oWCfusIPHRIQgL6RvUORcf03TLFqZdO_7VcI7CaUxB22cxDuJATczUprSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت دیوار سکوت بانک سپه چه گذشت؟
🔹
یک سال، سه ضربه: نشت احتمالی ۱۲ ترابایت داده‌ی مشتریان در فروردین ۱۴۰۴، فلج‌ شدن خدمات بانکی در روزهای جنگ ۱۲‌ روزه، و بحرانی سوم که هم‌زمان با جنگ ۴۰‌ روزه شکل گرفت. در هر سه مورد، واکنش رسمی تغییر نکرد: انکار در ابتدا، سکوت طولانی در ادامه، اطلاعاتی ناقص در پایان.
🔹
حقیقت اما جایی رو شد که کسی منتظرش نبود. در گفت‌وگویی آنلاین درباره‌ «بانکداری در شرایط جنگ»، مدیرعامل توسن، بی‌آنکه چنین قصدی داشته باشد، از نفوذی به شبکه‌ی بانک سپه پرده برداشت؛ نفوذی که درست از دل امن‌ترین لایه‌ی این شبکه سر برآورده بود.
🔹
این اعتراف، بی‌آنکه نام «هک» را بر زبان بیاورد، همان روایتی را تأیید کرد که کاربران شبکه‌های اجتماعی هفته‌ها پیش‌تر درباره‌ی هک بانک سپه در جنگ ۴۰‌روزه مطرح کرده بودند.
🔗
گزارش کامل را اینجا بخوانید:
khabarfoori.com/fa/tiny/news-3227401
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/665868" target="_blank">📅 12:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665867">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaqUC7eWIyqudwMm0AtyG7BT3GYQzWaXfKqFhcXk6AbZXgWDcFq0KeRw40nsDe0ZvWa0kKtbGiMaMNa0taXzgyw5n5XMHlIOAsWNWrHw-pzv1uUJxFf-S9d7umhP2MiCccFsJD9X8wldxRMV7Pv6QHzmUi2dXFcaWgNxZW0mnyghe-QPUPlxqdQuH0iTvCuezJ6AKXa49K0L8cFHw_-mr0BOy7SGrQngCu4IIkjZfznfiTYe6caZr8_ijn-ENVy_ytlcsb1CqCOeN9OHtLUq6YoYPX0DRrJ_pcvE9vMkOCzbk9wUdeUmK6xtIHc_lsnYJakEUKtxasCnjryP7ujweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین آسیب را از خروج سرمایه انسانی دارند؟
🔹
شاخص خروج سرمایه انسانی، میزان آسیب‌پذیری کشورها از خروج نیروی متخصص را در مقیاس ۰ تا ۱۰ نشان می‌دهد.
🔹
این شاخص صرفاً تعداد مهاجران را نمی‌سنجد بلکه، عواملی مثل مهاجرت نخبگان، بی‌ثباتی اقتصادی و  اثر خروج نیروهای متخصص بر کشور را هم در نظر می‌گیرد.
🔹
در این رتبه‌بندی، ساموآ با ۱۰ در صدر است و ایران نیز با حدود ۴.۶، در رتبه ۱۰۴ بین ۱۷۶ کشور قرار دارد.
@amarfact</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/665867" target="_blank">📅 12:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665866">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic6Il-fJwq0ntlbaczuDbchWJYkcVECkWti0khchVaztQUGkn6UyiiJJDbaoGyr-j0kh4LEfkFOyoOk9-UzfA3Xqpx2h5dx1ndUFugtypocL1U683UwZWhZgG1ZiT5Pv13ir1aUy722aRgVyc3EaByeIqTca4w9hwzA9DFthEOz9oUhmd7hpJ0TM7XV3inXpYyrs1LYcQvkqZsR462Wz1lzRQlqiyHKGzvs54_E9PH6-YPI2nQSlsixfilzuYDW3ADMJW5b-yGZcxyhF96LTFzgHWKEg8NpxNh4veSAohX42txXtG0z0QKDJWvvdadO85OwenLdCa-7JNFdRdRzL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای روسی: به شما اطمینان می‌دهیم که مراسم تشییع هیچ رهبر غربی هرگز تا این اندازه پرجمعیت نخواهد بود؛ زیرا آن‌ها انسان نیستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/665866" target="_blank">📅 12:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
گروسی: درخواست دسترسی به تأسیسات هسته‌ای ایران را ارائه داده‌ایم
گروسی:
🔹
برای دسترسی به تأسیسات درخواستی ارائه شده است اما آژانس تاکنون نتوانسته است به آنها دسترسی پیدا کند. آژانس معتقد است که ذخایر اورانیوم غنی‌شده ایران همچنان در تأسیسات هسته‌ای این کشور قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/665865" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665863">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f05d6012.mp4?token=uL5Wf8AJgo-rZBJqnZZwfbnsD1JzkQ96fz7WHQDC3JcA4DX1h6bw54AMPa45Rjh-NOWGvlu36vKZjsgdw2vx2dMFtr3AhnaLeBN5RSkoTLgaX6CTYmVYRx8ZlbY_TWJ0LHGjHzbTRQX92x-AUkkLSJfNRjMUQeHD04Sg0aOC_JjX60dPOquIwS7LiaZUGLM3wzBPCiD4K-yqBG7E9Gz5jOpeP-raqUMhqTyvQRvsz3H1ybP4DJcsN-t_V9GCZm9K6DeOuEDgStqYkZySUXOC5RKZivNi0sgaqoHxV9TMqIv9bgiFbyUV85g3s0fLCknro1RrYbavdWIRrq1tnIP1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f05d6012.mp4?token=uL5Wf8AJgo-rZBJqnZZwfbnsD1JzkQ96fz7WHQDC3JcA4DX1h6bw54AMPa45Rjh-NOWGvlu36vKZjsgdw2vx2dMFtr3AhnaLeBN5RSkoTLgaX6CTYmVYRx8ZlbY_TWJ0LHGjHzbTRQX92x-AUkkLSJfNRjMUQeHD04Sg0aOC_JjX60dPOquIwS7LiaZUGLM3wzBPCiD4K-yqBG7E9Gz5jOpeP-raqUMhqTyvQRvsz3H1ybP4DJcsN-t_V9GCZm9K6DeOuEDgStqYkZySUXOC5RKZivNi0sgaqoHxV9TMqIv9bgiFbyUV85g3s0fLCknro1RrYbavdWIRrq1tnIP1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینستاگرام ویژگی زیرنویس دو زبانه و قالب‌های پیشرفته را به اپ Edits اضافه کرد
🔹
این قابلیت درحال‌حاضر از ۱۵ زبان مختلف دنیا از جمله انگلیسی، اندونزیایی، روسی، پرتغالی، اسپانیایی و هندی پشتیبانی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/665863" target="_blank">📅 12:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665862">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
قالیباف: اجرای کامل تفاهمات به‌دست‌آمده را با قدرت مطالبه می‌کنیم
رئیس مجلس:
🔹
اگر آمریکا و رژیم صهیونیستی به تعهدات خود عمل نکنند، جمهوری اسلامی ایران اقدامات متناسب خود را از سر خواهد گرفت.
🔹
آمریکایی‌ها در این جنگ به‌طور کامل دریافتند که امکان مقابله نظامی با ایران را ندارند و ادعاهای رژیم صهیونیستی، چیزی جز تبلیغات بی‌اساس نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/665862" target="_blank">📅 12:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665861">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اطلاعیه شماره دو آستان قدس رضوی ویژهٔ مراسم بدرقه، تشییع و تدفین رهبر شهید انقلاب اسلامی
🔹
جریان زیارت و تردد زائران در صحن‌های پیرامونی حرم مطهر به‌صورت مستمر و بدون وقفه تداوم می‌یابد و محدودیت‌های تشرف و تردد، صرفاً در صحن‌ها و رواق‌های مرکزی حرم مطهر رضوی، از ظهر چهارشنبه ۱۷ تیرماه ۱۴۰۵ به‌صورت تدریجی اعمال می‌شود و تا پایان مراسم تدفین ادامه خواهد داشت.
🔹
از زائران حضرت شمس‌الشّموس (علیه‌السلام) خواهشمندیم این مهم را در برنامه‌ریزی سفر به مشهد مقدس مد نظر قرار دهند و با خادمان خود در اجرای هرچه شایسته‌تر این مراسم همکاری نمایند. یقین داریم همراهی و صبر شما، همچون همیشه، پشتوانه برگزاری آیینی در شأن حرم مطهر رضوی و رهبر شهید انقلاب اسلامی خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/665861" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665860">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شهباز شریف برای شرکت در مراسم تشییع رهبر شهید انقلاب راهی تهران شد
🔹
روزنامه یدیعوت آحارونوت: بازداشت جوان ۲۱ ساله در اسرائیل به اتهام جاسوسی برای ایران
🔹
مشاور امنیت ملی اسبق آمریکا: آمریکا در حال به شکست کشاندن خود مقابل ایران است
🔹
بارزانی و عراقچی تقویت روابط ایران و اقلیم کُردستان عراق را بررسی کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665860" target="_blank">📅 11:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665859">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC515MTWN0xU19XRXrwDyNPlUbWS9_ZsiPqSTFFN15W9OdqGVdZzFmBB1wrCYpaSJKCBimv3mLOer4W1f6pEzqtGEB-tvi5vZaWkKLxjJdsMdoDNz8t6-w4-kbTgoPPzcIxNVbgL8L-raqhgwAmJ3kBFdZSIU6O-zfA6_IsRuYr1vc2lExWGD7Sh7lAXj_Wt5hBUhed7xp74pnuFd4_NpxtpATHq3z2AbGKk17hMSKnMDkn6OAyXOtwewMxvfzeKDR8m6Yp-gdNnUahsmcjWhq1WCkZtwlJYeYNmuRcu4XCIg1QyPWDrX6obLoorkR7pM1nSFSoUJC0ubke_Xx51HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زبان مخفی جراحان؛ علائم دستی که سرعت عمل را بالا می‌برد
👨‍⚕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665859" target="_blank">📅 11:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
خونخواهی؛ مسیری برای عدالت روشن
🔹
در نگاه بسیاری از ایرانیان، اقدام آمریکا در ترور رهبر و فرماندهان ایرانی، نمونه‌ای آشکار از یک جنایت بزرگ و ناعادلانه است
🔹
اقدامی که مطالبه عدالت درباره آن نباید به فراموشی سپرده شود. خون قربانیان چنین حوادثی، صرفاً یک پرونده سیاسی نیست، بلکه مطالبه‌ای برای اجرای عدالت و مقابله با مصونیت از مجازات است.
🔹
خون‌خواهی، در این معنا، نه دعوت به انتقام‌جویی کور، بلکه اصرار بر مسئولیت‌پذیری، پیگیری حقوقی، حفظ حافظه تاریخی و مطالبه پاسخگویی از کسانی است که در برابر افکار عمومی و قوانین بین‌المللی باید پاسخگو باشند.
🔹
ملت‌ها زمانی به عدالت نزدیک‌تر می‌شوند که جنایت، فارغ از جایگاه و قدرت عامل آن، بی‌پاسخ نماند. مطالبه عدالت، اگر استمرار یابد، اجازه نخواهد داد تاریخ با سکوت نوشته شود.
🔹
بنابراین آنچه که مردم این روزها از مرجعیت داخل کشور انتظار دارند احقاق حقی است که در تمام جهان به عنوان یک مبنا شناخته میشود ...
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665858" target="_blank">📅 11:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcRbIox9jEsGLrNcGRs0A5tVpIdZJ7ZBvx-Em7743R9oPbkxVTU5YxRaPAwjcclslFRBzlAfv91JL6zYL508-Ozl4QLSraRrABoFe-oVMcsOfso7PCFVBltV5e9R-uoU5K8SF17rIR55EnzzjnU3yniVdCXL1WsN1dXg7bRKuaEiiMr1UhCwjIyuiDEepkLogFV5Sh0z3rJGefH7HlvllDWBqeHS_0-VwlZ7yU8MPDO6HDoaIIcQEhbk3xW0wPUi430aJRljzEGKSJ4FBd7sGQcwQ72lP5qpqKiLMhAMw_VgmDllnoBD62HBPIHS-af0AbqV78WA9UIP5H4NARpd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: یاد شهدای هواپیمای مسافربری ایرانی را گرامی می‌داریم و جنایت نابخشودنی هیأت حاکمه وقت آمریکا را هیچ‌گاه فراموش نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/665857" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
آسمان تهران دوشنبه به طور کامل بسته خواهد شد
رئیس سازمان هواپیمایی کشوری:
🔹
روز دوشنبه، همزمان با تشییع پیکر رهبر شهید انقلاب، فضای تهران به طور کامل بسته خواهد شد و هیچ پروازی انجام نمی شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665856" target="_blank">📅 11:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665855">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ef817bd9.mp4?token=TtRKO2cnfcR9aB8TfMiRbamkatBaRMvl8XAvweFu5VR62e0uxWGjYuP7_FAGwwpVxfAUMr36x-ERTO5upnmZhq5z-N34MMoeq8kk8Cb8bj68C9ZNRDqK3ZX76GdoXQQPErtXHgTGohYg5TxXfkROVgs9Cw0p9gU6KKIPNvcVqVgDDXx2B-a9VSafTaOAwIJj3X2EhIbZFaQfu5Sjd8EWla1utlH_36Usna4m2q5Jf1rkNekLIMzC46yx8ix-NGha84n7iRLQWZD5CugfNhf6xoLXJlzU8lz4ZX0j9LYp_e4rRbAu4K5c1GGqsPWtdnACC_K1L9AVvehI-2kQjmAXThBIH5-eeOZhymJnZLs_EpivsNuJajUziZt4Wiuua19Mut28cb9QT4gGdfwW2wbq9-k8ZUl5aGzd2B0BkSesEsvfYl3TgVlD3diwqvR_D8qjTAQdcroLzVTN3HM-YLy8SFgHzXdhu-VmnOXzmIJUQl5jmB86TqHcIq1ICKyh4kKuV5T2TvXNhrqAWpxcb6Zmq_75RKoXRqCUibuBQABsjK8_xCigOWt868Bu3oKKRFmMvwreva2o-5Pa_zqii1jxexc8MyTqyr9wT52SA-xtmQtJ8osfj2j25YSNNbU8giO5uj_l4gmZylbx-cAF7OnCt9cio4OqpphNGIOXT6Le_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ef817bd9.mp4?token=TtRKO2cnfcR9aB8TfMiRbamkatBaRMvl8XAvweFu5VR62e0uxWGjYuP7_FAGwwpVxfAUMr36x-ERTO5upnmZhq5z-N34MMoeq8kk8Cb8bj68C9ZNRDqK3ZX76GdoXQQPErtXHgTGohYg5TxXfkROVgs9Cw0p9gU6KKIPNvcVqVgDDXx2B-a9VSafTaOAwIJj3X2EhIbZFaQfu5Sjd8EWla1utlH_36Usna4m2q5Jf1rkNekLIMzC46yx8ix-NGha84n7iRLQWZD5CugfNhf6xoLXJlzU8lz4ZX0j9LYp_e4rRbAu4K5c1GGqsPWtdnACC_K1L9AVvehI-2kQjmAXThBIH5-eeOZhymJnZLs_EpivsNuJajUziZt4Wiuua19Mut28cb9QT4gGdfwW2wbq9-k8ZUl5aGzd2B0BkSesEsvfYl3TgVlD3diwqvR_D8qjTAQdcroLzVTN3HM-YLy8SFgHzXdhu-VmnOXzmIJUQl5jmB86TqHcIq1ICKyh4kKuV5T2TvXNhrqAWpxcb6Zmq_75RKoXRqCUibuBQABsjK8_xCigOWt868Bu3oKKRFmMvwreva2o-5Pa_zqii1jxexc8MyTqyr9wT52SA-xtmQtJ8osfj2j25YSNNbU8giO5uj_l4gmZylbx-cAF7OnCt9cio4OqpphNGIOXT6Le_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسم‌الله گفتن رونالدو قبل از زدن پنالتی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/665855" target="_blank">📅 11:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665854">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecfa437d02.mp4?token=pP-pqIkwjJokgCBRVDU-CijxkZqAPkOxCPT5JvLmEVxYB9y6qeowfECrT5nQpNP_bmOjsXH7dUKycvm-SwtzSgHN189xQCN1NmGxKiezkYHlbWK9V9bAVu_fyPoZQKTWxYo676sHeBDapZbACgS_YFvsjta52xniJqcwbbsFaxPIU4oCSVWKHTesBpyEaXWBisAfNppnlc_XzSa6Steg1GOSABP-4RAkVfBSATT0X5gl1S4mNqo-g_RLG4CJVpQovvYmbZ7usRsjVLTYhJ7cJb3KEokugLFF9KAaUIhR_wG36VtfaTCNwMC8-dj8f74MzCu3lKUzjwKr7E2NKHEFBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecfa437d02.mp4?token=pP-pqIkwjJokgCBRVDU-CijxkZqAPkOxCPT5JvLmEVxYB9y6qeowfECrT5nQpNP_bmOjsXH7dUKycvm-SwtzSgHN189xQCN1NmGxKiezkYHlbWK9V9bAVu_fyPoZQKTWxYo676sHeBDapZbACgS_YFvsjta52xniJqcwbbsFaxPIU4oCSVWKHTesBpyEaXWBisAfNppnlc_XzSa6Steg1GOSABP-4RAkVfBSATT0X5gl1S4mNqo-g_RLG4CJVpQovvYmbZ7usRsjVLTYhJ7cJb3KEokugLFF9KAaUIhR_wG36VtfaTCNwMC8-dj8f74MzCu3lKUzjwKr7E2NKHEFBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از علمای فلسطین به پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665854" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665853">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0saZ7tSxDIKZdAnfXrM3evZOtgihdP4hMAsrID5eN_01VZpGT8LuykvTDD-pEhPngxCja860ix9Pb06Wxl4Ft_yny_Nfn6opnNa3twcye8tjQM5t3QI3cdre52WZwA7y7DQZ7tsbOJwc3l_qRKStfcFV7TNH_j3VoAVpBM39vm8kO6SHKZAx_906UFnTGG1ufSOt2DyYSTzAsInLoaFJ0r6mLTjI0fFEFb59wgg85nQN5hIzYaQxEnYLNj89-Ku0GY-sOX3DXZaosMzIxobDLIMTUUeKqyGrVnA3Tie4V-vaqzRoKY_RX_JyUGY5iXe89zkE1Iyt8xaUKXk6RkmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالعمل افراد کم‌بینا در مراسم تشییع و وداع
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/665853" target="_blank">📅 11:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665852">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
حزب‌الله برای رهبر شهید، مراسم یادبود برگزار می‌کند
🔹
جنبش حزب‌الله از مردم لبنان خواست در مراسم یادبودی که به خاطر رهبر شهید انقلاب برگزار خواهد شد، شرکت کنند. این مراسم قرار است شامگاه چهارشنبه آینده در ضاحیه بیروت برگزار شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665852" target="_blank">📅 11:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665849">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hs8I1K_Rv47payWbK5n6ktxIsoaO3DoaI7_zKRVaIDjDJayDkFWb7fUG3qoi0ZGSrg1S-TkJ97DD9b6b1urdxFZn935eaP1XVCh8UUtP8nRLeaa6zw3iEG5P2zxR9Ez6Fnzd0lE141D5gE3RabQh-5SuFObp4mG3yq9MGU9aIeLM4mrp7cLKjRsJDbq25StXvdTG51YHSxfw1HYVedkxUCXLy27seSEi-ivrUcydCv4o61NYUyt2qcHwsxDcn9qD7hYjSssbKSgs0XKheYTCDlpXRnulqt8mTwtLrZoNDN_jQwBFsHnK1-MoFmtMFLdaZqneoLPBaOxSrca6bQIbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZ7WY_YN3lsSCAENUvh9yOPfKB-zOaACSAuYRBWi6yWn4AtLPTTxlMzr_Mxs1alkhX6ajaoI6ZaJdsaKQnlA-L175qM3NtN_VtWCddVTHnp5HeYZi-adeFd0kIFsOG3Jps7tbOnO_Uexqq6lnSX6jNovgEETgAU9HtwVdK79hxaB8mofxKmdwOOth3iDpIW0w8X-8rYvk2UV8QYpCmCjZPON17YoQmPVMfl-UMlZJrj2ph0LEJGKCg919lQ8ulCoa5I4j9fyXG_byFUW4sMiRaWzBOwi0RDE8FpKF1AfFQ5B1TfXxefPQuB1tOJmxx-9YwzXgKMi6GuMVHxovQxJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHMBGpzG3Oz8-lcgI9sNwKErKGN0nX-NzksHFq_3w4FIrWNPa97fknVMQEpro3_HJQe8FUTCEDVTK9WAK-vAm--p0h8vnhF5w6ma2RaarPjSVGHiQGvHdNSuwvzymZpBfeC-zF0hkkY_-KqR4mHujwoyWYEez5ybUyiLmAh4CNLwxb00z3j_dl2LzPPiZtX76hLNjb0p86kA9Z6Wca6JP2YLtnpuDtUyWVhTH8_YT66ULytex3inr8HqyiAIH2ni2k0RZt8p5qCN6QsbUFCRgYlC5vsvrhXvzgcq9aVSkCn9-pL2zShFbdRxV7d3iF3j31IGg2BvH2NePlKs1RC8lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار نخست‌وزیر ارمنستان و رهبر ملی ترکمنستان با پزشکیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/665849" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665848">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063a3452e3.mp4?token=b7ABpdwnJ_HyDY5dWB8iz_CmN8LjaFGYN-1gOSb-f_YVXjnad36YxnqipSd9FK2kQpDSYlmnsFWGppeye7bGOH0OT6R8_iELCeQSs8cHAtRZw_eDDT0ZOxo7N5WclE_T4vNtDeMLA-_KbO7N9arFvGZpxoaupP6tuXwWt9eyE4givA47ud719CYK0-JGcgueGsZFXX6DZr2tp1q1hi5aXCpXX8pP-rEdNXRDf1OJOizLMKrqfxTKXX1lM-WOiwX3Lvkf-5XifKAGkC9e9L7796_IusWpaw3NbjRC8h0IrxeCVdVkhlQDdqHbe2nyZ4_WFvx42YVGyfoQHzLO5OXQ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063a3452e3.mp4?token=b7ABpdwnJ_HyDY5dWB8iz_CmN8LjaFGYN-1gOSb-f_YVXjnad36YxnqipSd9FK2kQpDSYlmnsFWGppeye7bGOH0OT6R8_iELCeQSs8cHAtRZw_eDDT0ZOxo7N5WclE_T4vNtDeMLA-_KbO7N9arFvGZpxoaupP6tuXwWt9eyE4givA47ud719CYK0-JGcgueGsZFXX6DZr2tp1q1hi5aXCpXX8pP-rEdNXRDf1OJOizLMKrqfxTKXX1lM-WOiwX3Lvkf-5XifKAGkC9e9L7796_IusWpaw3NbjRC8h0IrxeCVdVkhlQDdqHbe2nyZ4_WFvx42YVGyfoQHzLO5OXQ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منطقه «البراری» دبی
🔹
﻿وقتی توسعه با برنامه‌ریزی همراه می‌شود تنها در ۲۰ سال، بیابانی خشک و سوزان به یکی از سرسبزترین و چشم‌نوازترین مناطق این شهر تبدیل شد؛ پروژه‌ای که امروز از آن به‌عنوان نمادی از توسعه شهری و احیای محیط‌زیست یاد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/665848" target="_blank">📅 11:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665847">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5621a5736a.mp4?token=noOBqewJr1n97Ng0nqJI4-IVT5p4RmdwOU2y5-uLXVuAM9yBa08_c_OTt_NEQ8QAm22-6bK0Ba-_CbQqdn32ukTltesrecBsUBspn17Sszl4K5CwaH9YgnZNpXA9r9fuYGHb2Z0bD8Y2st659xmUYGovyj0N8WlKe4ASJxXEawajGfwys6vQ0d4VvC_XXzWjBGx99E-jcSFs-e-fVnSCz1Uuma6sybBLswgcsyMfrUMx8_I_dO2EXgQLHSPv6vHhBBnhoyHh07anOwJO_Z1Uhz0NmfqnCSEBALOfeXyuEsTGUyLGJa9f-eN5Ol5t0cvuXVqo5IUEOJtyqag0BBrw1Cu1dVd3IYgBugw3s0ysmHqdxJBgIbdCyLB8w3eh7Odz4ECBvaY36Pu_-S383vZCi_DNf9mAE5j4fu9O5wXCRb-7VIA4RO4-eIuySBUx1-ntDO5x3HkA1u-jdNfKgI8OgJU4Z96Kb-ppUQmwb5Wl3xP6F1aT5EW7kQY4BWpcJb0G3ReMZPKJDGAFz8L64kX0BHBktTiBMWjohxddS0zzth7Ac-S6fIwQz5_vdDjsj3r9xznghOZLdgFvJf2gAIcgPiNSsJDxYU0exyKvmxicWKy7HQzyraEDh6i7ox6kzEB6Oj9qA0hbUhTmDqsMwdW0VHv9KId9_ezf4LJtVdJgVV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5621a5736a.mp4?token=noOBqewJr1n97Ng0nqJI4-IVT5p4RmdwOU2y5-uLXVuAM9yBa08_c_OTt_NEQ8QAm22-6bK0Ba-_CbQqdn32ukTltesrecBsUBspn17Sszl4K5CwaH9YgnZNpXA9r9fuYGHb2Z0bD8Y2st659xmUYGovyj0N8WlKe4ASJxXEawajGfwys6vQ0d4VvC_XXzWjBGx99E-jcSFs-e-fVnSCz1Uuma6sybBLswgcsyMfrUMx8_I_dO2EXgQLHSPv6vHhBBnhoyHh07anOwJO_Z1Uhz0NmfqnCSEBALOfeXyuEsTGUyLGJa9f-eN5Ol5t0cvuXVqo5IUEOJtyqag0BBrw1Cu1dVd3IYgBugw3s0ysmHqdxJBgIbdCyLB8w3eh7Odz4ECBvaY36Pu_-S383vZCi_DNf9mAE5j4fu9O5wXCRb-7VIA4RO4-eIuySBUx1-ntDO5x3HkA1u-jdNfKgI8OgJU4Z96Kb-ppUQmwb5Wl3xP6F1aT5EW7kQY4BWpcJb0G3ReMZPKJDGAFz8L64kX0BHBktTiBMWjohxddS0zzth7Ac-S6fIwQz5_vdDjsj3r9xznghOZLdgFvJf2gAIcgPiNSsJDxYU0exyKvmxicWKy7HQzyraEDh6i7ox6kzEB6Oj9qA0hbUhTmDqsMwdW0VHv9KId9_ezf4LJtVdJgVV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرتغال به کرواسی توسط گونچالو راموس
؛
پرتغال با کامبک صعود کرد تا امیدهای رونالدو زنده بماند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/665847" target="_blank">📅 11:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665846">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مقامات سیاسی رسمی کشورهای مختلف به منظور ادای احترام به پیکر رهبر شهید انقلاب، ساعت ۱۳ در محل مصلی تهران حاضر می‌شوند
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665846" target="_blank">📅 11:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIiMVpzYGmkcr0CIM3c34AlhObl86DhxY4FLc6Y1daQmN3KOlbUzaWdeRJZc0MMXWtrYe1Dfin6HCDrRChk3ruspepaoOywgIEXYBsmkpTAE3KYihI1YauUq2tWRJLMovaXlcuQz7Ivs0FbRtWf7pEde7KgAhxTLImsQJq3zMfijvT730Vax4xA8PVs82iFYgHo34yAfT4J0lipCQW37h1lhUZV7f69aXfJRDtIeQi7Fwhu5K6z83E5QJ41kK5W2WGJzbB4jNFxBCyl5M0TKA1z23ql8VDVeG-fgxCnlZW1Gac_VkQFPiNgt3ZLP4Da3yJTQdPJqarEWfiCtVj6PMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط اتوبوس به دره در پاکستان ۴۰ کشته برجای گذاشت
سخنگوی دولت ایالت بلوچستان پاکستان:
🔹
امروز که درپی خروج اتوبوس از جاده و سقوط آن به دره ۴۰ نفر از سرنشینان آن کشته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/665845" target="_blank">📅 11:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665844">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=aM76VlrmLrwjSzvQ9f5rGnqHL5f7lqcRIC5ltNzFU0IdBo3AsDhiJM1Sr4bLfe03k7NqepBBZ07vv73-NbvSTIRUSJUCgC5vbq9LxJS7nl7yDxlA-b3xnuN9rdRMQvPjaXd4DCK_-H3ZYJEkhgNEGMlDdxp0LUFe5boa7GcHrx4OlOWWJ2M5RGVmZtjqTE3hQ7D-PHO_rp5yY2Pj-hiToq-Uui0wEi9pQZj9P7y_T8AaBfy7ZKTbvKdY9sWBagrwPgp0InTkJSAONRSg4hiKOVSDa5zotE9iFA2LQ6YoUS-hOLIY6I9w6d9fRKHAHP_vZePUjxDS1fBSFVwDDQ7aTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=aM76VlrmLrwjSzvQ9f5rGnqHL5f7lqcRIC5ltNzFU0IdBo3AsDhiJM1Sr4bLfe03k7NqepBBZ07vv73-NbvSTIRUSJUCgC5vbq9LxJS7nl7yDxlA-b3xnuN9rdRMQvPjaXd4DCK_-H3ZYJEkhgNEGMlDdxp0LUFe5boa7GcHrx4OlOWWJ2M5RGVmZtjqTE3hQ7D-PHO_rp5yY2Pj-hiToq-Uui0wEi9pQZj9P7y_T8AaBfy7ZKTbvKdY9sWBagrwPgp0InTkJSAONRSg4hiKOVSDa5zotE9iFA2LQ6YoUS-hOLIY6I9w6d9fRKHAHP_vZePUjxDS1fBSFVwDDQ7aTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از ارمنستان به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/665844" target="_blank">📅 11:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665843">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01d988089.mp4?token=CuhSg7E0lHB1nUaEIbw6XGmG4CEDQ07FJz7nCk9eudgcijigy339uWV2BsooJWDwcsDd4Su9DGreD47uAsS0vDVH-hIwflfV_s5r1Xr1PQxocLmR3wg6zMmf143WnJguyFjUYXUHYGph_j_EbLlwbG_4vKuOzF7G2oSD4QKM4oa-TOGWIEpeE9TTeF6Wj3UnY_M15lHmzke880ZMyLEI6k_1cm0EM5oU-BPrtz14R_7rzWzh0D9c0brSNlKrOeHh5RSH9uFbb60cmjjVJh6E_qChrIuQ7BNBAUvTH-Iv-5hyIkWfHfWhB-BCMglGYrMLwrwwjxm8l7nXgjVBNK9m8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01d988089.mp4?token=CuhSg7E0lHB1nUaEIbw6XGmG4CEDQ07FJz7nCk9eudgcijigy339uWV2BsooJWDwcsDd4Su9DGreD47uAsS0vDVH-hIwflfV_s5r1Xr1PQxocLmR3wg6zMmf143WnJguyFjUYXUHYGph_j_EbLlwbG_4vKuOzF7G2oSD4QKM4oa-TOGWIEpeE9TTeF6Wj3UnY_M15lHmzke880ZMyLEI6k_1cm0EM5oU-BPrtz14R_7rzWzh0D9c0brSNlKrOeHh5RSH9uFbb60cmjjVJh6E_qChrIuQ7BNBAUvTH-Iv-5hyIkWfHfWhB-BCMglGYrMLwrwwjxm8l7nXgjVBNK9m8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از بانوان ‌طلاب و فعالان عرصهٔ بین‌الملل به پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/665843" target="_blank">📅 11:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d78a6625.mp4?token=OX6YeqcWSRVWykIk_fIWemAlOYYQC2fYspxJqVdNhYvH4G51zuab2x2WBEvaW-mQxOrg1neKvkzCQgYNm-5tAFk1fOtgFm_m5b53NWQDlVvEC8nLHD8U3vCGOCBTNBNkUCtcEfpTuefDoLebrzSCkNByZM3YyRr3Jh0litEAC-pC8xDvHV-P-qCZkqrLRN7GQALv8In4SUqyZYYujnVLmqeJ7iw-gYmLJh-uRQFYTa1NQWDax7MjH-uBEUJ-hXFoGbPQVA_g2IR0dcBfjVjN4oY8cO2QxermT14TPHcA_znqsApkPLQ9bH_QreVpymFb0oNFEwggjWPnyH1qgS0vAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d78a6625.mp4?token=OX6YeqcWSRVWykIk_fIWemAlOYYQC2fYspxJqVdNhYvH4G51zuab2x2WBEvaW-mQxOrg1neKvkzCQgYNm-5tAFk1fOtgFm_m5b53NWQDlVvEC8nLHD8U3vCGOCBTNBNkUCtcEfpTuefDoLebrzSCkNByZM3YyRr3Jh0litEAC-pC8xDvHV-P-qCZkqrLRN7GQALv8In4SUqyZYYujnVLmqeJ7iw-gYmLJh-uRQFYTa1NQWDax7MjH-uBEUJ-hXFoGbPQVA_g2IR0dcBfjVjN4oY8cO2QxermT14TPHcA_znqsApkPLQ9bH_QreVpymFb0oNFEwggjWPnyH1qgS0vAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیاتی از بیت معظم رهبر شهید انقلاب به پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665842" target="_blank">📅 11:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادای احترام هیئتی از شیوخ، عشایر، احزاب کرد اقلیم کردستان و اعضای پارلمان کشور عراق به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665841" target="_blank">📅 10:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665840">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728761776c.mp4?token=mHh0htJ6O_8_WC9xPqM4HP126Y7uNiyixYgyq4CtlZFtXl-Gsr_hhA9bK13Iz77Z9BR0v9fzhm_NItAC_Gxbf5Ew1DKBEIgJCkU-7pxL1MqWQ9zWhmXCE5jWrTpJCeWMT79mkd4Lnp6hGVhHk074T8AIX3B8u_KWgvlCj-t-DBvbP3ePF4BghWC_YW0hC3Bn2hqWb15ytVQkpZqeSjKVUcdkzhrq1lJuhRjgxpgl_pcj0xcZmIobdVvC0jqy3qQ0qikcpT16Soxnx49Su_TAAsjHcFhri2Rv5wLrQjhOOtvkoGXIBk6FbdviLerf-qfiIZIIOu6z-BIMTBMI9nmYUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728761776c.mp4?token=mHh0htJ6O_8_WC9xPqM4HP126Y7uNiyixYgyq4CtlZFtXl-Gsr_hhA9bK13Iz77Z9BR0v9fzhm_NItAC_Gxbf5Ew1DKBEIgJCkU-7pxL1MqWQ9zWhmXCE5jWrTpJCeWMT79mkd4Lnp6hGVhHk074T8AIX3B8u_KWgvlCj-t-DBvbP3ePF4BghWC_YW0hC3Bn2hqWb15ytVQkpZqeSjKVUcdkzhrq1lJuhRjgxpgl_pcj0xcZmIobdVvC0jqy3qQ0qikcpT16Soxnx49Su_TAAsjHcFhri2Rv5wLrQjhOOtvkoGXIBk6FbdviLerf-qfiIZIIOu6z-BIMTBMI9nmYUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرتغال به کرواسی توسط رونالدو
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665840" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665839">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF0qHGstQo9lV9u-LRARYa9-LUsN51d3VkbAMTofGqGwEvRFikemovU5i9hNG4JA2RjK3Be-fL7XVUBKQkfUBMw2KXYfCwCENtU8j45mNQBBuYi3LVekE_IZgDc8TlyyBDlIc7DTGAAEHwJqP40IA5GR2LkhBVWJjizBScMPf2uphDwQai7XIF9IB2RUdqxeWPeLCiNEKytNCSJvndN2KWWCOA5cnnYpw6cKTkHfDGFRmsIe0OLd2xC69reQFYKyRbItphWZK71L8dxT1AbluAbYrXBhANbsloC71EsYzPPofkkT5Znyl8G_Esaa_ZhWSL06Lf70oFSfT5_D2Q2nHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل نرم‌افزار Signatures را برای امضای اسناد دیجیتال روی اندروید منتشر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665839" target="_blank">📅 10:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665838">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6aaecdb68.mp4?token=UIKpNfYxL43ukK6CTa3jwU8qW20LCowXYk6kMujqAblCN17kcEGrQYmkvs2AJLh63pA9zxQb1f-RIpEB5Utl5rxnujztXGN444M1NEtVyGFQeK_dL-zXpHtVwTwkrczDIl1DcWBs3CwJpRiv5Q_knNNTM16lPlMTbTP-LIgEXRRzE49tE2O7rI5XXB97hMdQ1kUwjYL4T11U3wQ7B8SsfZAd95PWipgLQIfyaH6Dfud6eIrLqwqCtQzvdvAGe34QlyTqZ0a1FJUpJwSZNepryjgpaBYIR-TIkYmHockmIUdJHirTvF6v_u5ZnVKpQ50VLVZhJKahKJytgNMKXqhhtQI_-bcngNt4SL49Zi50CLcq8GVdt1yGTF43mSjpKz_O24vXZgRFYUGHAI3d1zRQdQ76IiHqlhByDUhqiXaSC6JZV42IbSeIhjbPrCiqPrhf0OBKtzZxYa9hyAZxNrSf67tm29XufxCi_Vp82l7IHbV6aiJ_rSDLl2ZUxP5xUs7O1BJatfwtpumJ8olhE6ABfwDU9rob0qA5LRUvN4M246QfElTp8q2TnmENWvqNjdrT3HuDZQfrPlCJnzZJqkFgfDsLBPD0PlC3u7Bk1nc5ceWmSc-wtd4qoFpHI5DblTwJTfRko9RPYDgmwEAY8sB36gkSef65NKkvJFBhNpHXLGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6aaecdb68.mp4?token=UIKpNfYxL43ukK6CTa3jwU8qW20LCowXYk6kMujqAblCN17kcEGrQYmkvs2AJLh63pA9zxQb1f-RIpEB5Utl5rxnujztXGN444M1NEtVyGFQeK_dL-zXpHtVwTwkrczDIl1DcWBs3CwJpRiv5Q_knNNTM16lPlMTbTP-LIgEXRRzE49tE2O7rI5XXB97hMdQ1kUwjYL4T11U3wQ7B8SsfZAd95PWipgLQIfyaH6Dfud6eIrLqwqCtQzvdvAGe34QlyTqZ0a1FJUpJwSZNepryjgpaBYIR-TIkYmHockmIUdJHirTvF6v_u5ZnVKpQ50VLVZhJKahKJytgNMKXqhhtQI_-bcngNt4SL49Zi50CLcq8GVdt1yGTF43mSjpKz_O24vXZgRFYUGHAI3d1zRQdQ76IiHqlhByDUhqiXaSC6JZV42IbSeIhjbPrCiqPrhf0OBKtzZxYa9hyAZxNrSf67tm29XufxCi_Vp82l7IHbV6aiJ_rSDLl2ZUxP5xUs7O1BJatfwtpumJ8olhE6ABfwDU9rob0qA5LRUvN4M246QfElTp8q2TnmENWvqNjdrT3HuDZQfrPlCJnzZJqkFgfDsLBPD0PlC3u7Bk1nc5ceWmSc-wtd4qoFpHI5DblTwJTfRko9RPYDgmwEAY8sB36gkSef65NKkvJFBhNpHXLGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کرواسی به پرتغال توسط پریشیچ
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665838" target="_blank">📅 10:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665837">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fe7546a3.mp4?token=fvE27ODT6viU78pYJ3GFVVdmrx0NIbE9qY-sNIHobaTg37dUK3Ycoe0VSRgKLlyHCsj-XvoUBNz2HgXzilcQDpOihBriBCQf5Ic-1u1em7bQHxLp6BX9YFo_3GWGlWA2YMo_GrZQGrcEWN6YJt6KZ4vaOVcwOo25ynMh3oCVCRKsFxhX4KzZml6WOXxYxEn1giz5Y3IUgFGZGWhl7VPx8ApDQn4arcxl042s3pJndvjJuYLJ_2yzvALXqCXelxQEpEwki_zbhJbeUu8J2LYFdJ3CdLKbNi1oEhMlOS7jy_JpIV4ag01eYKO6WqaiG093-Y70gR8J1vSd5MezLltJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fe7546a3.mp4?token=fvE27ODT6viU78pYJ3GFVVdmrx0NIbE9qY-sNIHobaTg37dUK3Ycoe0VSRgKLlyHCsj-XvoUBNz2HgXzilcQDpOihBriBCQf5Ic-1u1em7bQHxLp6BX9YFo_3GWGlWA2YMo_GrZQGrcEWN6YJt6KZ4vaOVcwOo25ynMh3oCVCRKsFxhX4KzZml6WOXxYxEn1giz5Y3IUgFGZGWhl7VPx8ApDQn4arcxl042s3pJndvjJuYLJ_2yzvALXqCXelxQEpEwki_zbhJbeUu8J2LYFdJ3CdLKbNi1oEhMlOS7jy_JpIV4ag01eYKO6WqaiG093-Y70gR8J1vSd5MezLltJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان ۱۲ سال حبس؛ نجات زن فرانسوی و پنج فرزندش در پاکستان
🔹
یک زن فرانسوی به نام سیلوی یاسمینا که سال‌ها پیش با مردی پاکستانی ازدواج کرده و به پاکستان رفته بود، به همراه پنج فرزندش پس از حدود ۱۲ سال حبس خانگی و تحمل آزار جسمی و روحی، با فرار یکی از پسرانش نجات یافت. پلیس شوهر او را بازداشت کرده و این زن قصد دارد به فرانسه بازگردد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665837" target="_blank">📅 10:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665836">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
حمل‌ونقل عمومی قم در ایام بدرقۀ رهبر شهید رایگان شد
شهردار قم:
🔹
همزمان با برگزاری آیین بدرقۀ رهبر شهید، استفاده از ناوگان اتوبوسرانی شهری در روزهای ۱۵، ۱۶ و ۱۷ تیرماه رایگان خواهد بود.
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665836" target="_blank">📅 10:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665835">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcVA-kB2OpcoJ4xaT7fzeN2oGhnebJKCLsdPkrXkqQuWzQ4l_zMCfsnLmsdI8AjXXOcK6ml-Gu6qFxUQD-3e_-5YTteA2b89gnNfBPYeNO4hw0jKWCAU1_yk-SMtE4mNbNT74eunxUYMGQSEpA_Yiogl69JPuQ6py9IOcr5nRvAoiGSIjUCTFnOIZwrvfE-o7AFeWYyZUYj3hMeoYhvz6Lg-HiISnYVPXV5NjagFuyTp5ypL0TvFF89Xgadp_a4DGQdxOKxuhRQqgvAM43Tor4DklB6c0derd7Tirhfz3bsD0j0jZ7rXf2f_Kza555Ktn_gn5Rt8E9IIDqsmkFp2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ظریف: «دوران بزن‌ دررو تمام شده است»؛ ایران دیگر فقط تماشاگر نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665835" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665834">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=horEuOIdvOMj-tLsL2HEQSrzob68ZCVJ18iNKeMVjTDMecTvNa42wawpsM84_BJruu3w4e_bENPyE_oN7s3FFk-i3Of2LC7zqMl065THN93Asag3cEvjmy-zJv1eAo4HAnoKXVrbBuH6RTGiLMe8mDJS7tYrEsKa684m3d_IwdNMPZ8W8xi4YE8badC7H9Qo2rZpZ5v8GimYQ_P5ZlJLZAcooUTiSrQckrOctJ9IdWp68ias9Xq8yc3wkvYhzWhM_qut2i7k1zwUfCjriufs26fzKzLJJVqPQGEiPz91VU5aQeXRvEkzQjH6mxbv9gpwu99GDQgzyGjga6p9Zyndig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=horEuOIdvOMj-tLsL2HEQSrzob68ZCVJ18iNKeMVjTDMecTvNa42wawpsM84_BJruu3w4e_bENPyE_oN7s3FFk-i3Of2LC7zqMl065THN93Asag3cEvjmy-zJv1eAo4HAnoKXVrbBuH6RTGiLMe8mDJS7tYrEsKa684m3d_IwdNMPZ8W8xi4YE8badC7H9Qo2rZpZ5v8GimYQ_P5ZlJLZAcooUTiSrQckrOctJ9IdWp68ias9Xq8yc3wkvYhzWhM_qut2i7k1zwUfCjriufs26fzKzLJJVqPQGEiPz91VU5aQeXRvEkzQjH6mxbv9gpwu99GDQgzyGjga6p9Zyndig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع جمعی از اعضای حزب‌الله لبنان و خانوادهٔ سیدحسن نصرالله و عماد مغنیه و فرماندهان شهید حزب‌الله با رهبر شهید انقلاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665834" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665833">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t41sHOHj9x1elri5GbT-RYHBL1qqCRLErPi48AIOaPX_2Sre7B6nfHCjZDQmO3UH-pP2h0RQsAdNREtf0WIiGpqImJxE5-HVe2lp3TMoKiNjPqx6-vvwPWjjyGnfgIovLdmSbSUwIAE1DjP5LCPSaitrxcLzvMvs-6vrNbUYkjV2eYDaXppuThpWp2ZTMTnXDzSGXUPcfJQyqEuh1wUXA_eJNnxeJ4g7ZDBv5e_xkkDvxSUTixDM8ywfL5WkmofaEaJmWNh5ok-DQdEOyTHva67e3Xm3Z1n77Gt8_zLq82nb17sT_Vl2brOQkSQyZEznyzgg7ORf9GyFtaIYjb3yfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی کوچیکتر از اونی بود که فکرشو می‌کردم...</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/665833" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665832">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs-BhKHn-Jy70V_T7tg2xbEPRiM0kE-lX9JJeWcpwndzE0KJAT90dfQJvZaoJ0DjixvNi3Y_GfhptF6-RXTk38KVVju0UQrlVTaM8y9uMBHhmDiF3rw0RMgwWoF3271zP2tbop0XZNIvidQA3Lek7ZaXkHSMum5mR3d18b1PAaTvdwMQHv6chGRxLPmDTLGM6L08qELnDvjrCs1GZ_bpYU7eXPuAsKrowLBwL8jIX-zXXdqTZcoh2rCJ7mv4IPp9xw9aIx2xEpw_2OffBxK9nsCf6dH_7cTBuIJPxmDu0ms1HUFK9iBDayuItF3FAe3UFQW8nnxr4WILAnqVee2e4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشیدن منظم قهوه تا ۶ سال مغز را جوانتر می‌کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/665832" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665829">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=Ypd7nx7-Te5r0U6cXMUWLKhtjd0aU02tuf9-Bf8Jjmdg-iT8NSRtyHorg98WiUb_wwnSGoLW6tRo-oLOJNjFOqAc6E8mp1b2zzhhJ3hLRAvDR6miyq6Ldil6zC__GKU1_aiguiUaG_GhisbabWtfdj_X1phQnzL7kZW4JvpRYgiUV1voeKaVHPN4hfRcLuKkRJQSsxn1JBBMVxWKv7MguX9pwGiABRk6VQR08wnf7clveH0osPRiXGt9h-l15AdoLm5H_8HTRO3NOKQA67Dg73L0QmpnfypkezrmU3_BfLhLMifoYvynuEqioL4vZpKvu3Ek1SWHlpu_iYPYl6yJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=Ypd7nx7-Te5r0U6cXMUWLKhtjd0aU02tuf9-Bf8Jjmdg-iT8NSRtyHorg98WiUb_wwnSGoLW6tRo-oLOJNjFOqAc6E8mp1b2zzhhJ3hLRAvDR6miyq6Ldil6zC__GKU1_aiguiUaG_GhisbabWtfdj_X1phQnzL7kZW4JvpRYgiUV1voeKaVHPN4hfRcLuKkRJQSsxn1JBBMVxWKv7MguX9pwGiABRk6VQR08wnf7clveH0osPRiXGt9h-l15AdoLm5H_8HTRO3NOKQA67Dg73L0QmpnfypkezrmU3_BfLhLMifoYvynuEqioL4vZpKvu3Ek1SWHlpu_iYPYl6yJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعی از رهبران هندو، شیعیان تایلند و شیعیان آلمان به رهبر شهید انقلاب ادای احترام کردند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/665829" target="_blank">📅 10:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665828">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
محدودیت‌های کارت سوخت حذف شد
شرکت پخش فرآورده‌های نفتی:
🔹
محدودیت‌های سوخت‌گیری با کارت هوشمند سوخت در ایام تشییع رهبر شهید انقلاب برداشته شد.
🔹
صدور کارت المثنی سوخت نیز یک‌روزه انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/665828" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665827">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351721101b.mp4?token=tBSg2QY1aW1MES4mAIV6oOyGohz0nt7c6qj9DvZrWbTAi5Js5PERnB5xoUCMBgtYPu47MwaXwPBhtkbUun10I_y-LEnyX4kTdoMT7c3ZYqVnObEBFluk9eBnstMIxJDdrQfCx4LX9wTqJEryw2ZBC1isF_DRnnnFw0uWHwQKBWp21prs6NmCGkwqFoD_Kpzad7Rg7XacZs91YOZJYvK4e97XLfCJlnsA91X5iFAtzW_YxED9Cm0nlQmoDY_TytUY4xFwh_MCSfe2VpFK-wbjg8Pr0RjyUlSDXlfwxL1fH9K7Ajq_uFAvMbCPjoGY1RZxPCrm2KXDuLuW6slFIlzAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351721101b.mp4?token=tBSg2QY1aW1MES4mAIV6oOyGohz0nt7c6qj9DvZrWbTAi5Js5PERnB5xoUCMBgtYPu47MwaXwPBhtkbUun10I_y-LEnyX4kTdoMT7c3ZYqVnObEBFluk9eBnstMIxJDdrQfCx4LX9wTqJEryw2ZBC1isF_DRnnnFw0uWHwQKBWp21prs6NmCGkwqFoD_Kpzad7Rg7XacZs91YOZJYvK4e97XLfCJlnsA91X5iFAtzW_YxED9Cm0nlQmoDY_TytUY4xFwh_MCSfe2VpFK-wbjg8Pr0RjyUlSDXlfwxL1fH9K7Ajq_uFAvMbCPjoGY1RZxPCrm2KXDuLuW6slFIlzAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت علمای روسیه به پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/665827" target="_blank">📅 10:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909be738a9.mp4?token=L5hP6qYOMs525xzVlIUf-NwDNZSYhGO9e6BhWpBRtQDcWgIPzBBLTvev2a0Ord-F8MX7ZGBJSn75uPgjw_zp7RaPvsyCZJYkI0fbqOJ1wCVgM90eVhjoXDIpap2reh2YtS7-I8asW5dCDTSl7TlTckX0YpoM2aubWbDvxqrtIobZRFoPbiPBpE2V8yMHJdXDD0x1cPfYacZgDUjBxgB7GVMxyzRGOl4eCFN-dOdzwOvXo9pCmWllqoCqn23cfd6nCBzIX4PIry8r1VIoo9hrEcRE80dijQfcdNfYTHLgvoyg9lVWzjkUyHQHRIhdYVVO5e31nGyYJ3gLDKTcvrBFTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909be738a9.mp4?token=L5hP6qYOMs525xzVlIUf-NwDNZSYhGO9e6BhWpBRtQDcWgIPzBBLTvev2a0Ord-F8MX7ZGBJSn75uPgjw_zp7RaPvsyCZJYkI0fbqOJ1wCVgM90eVhjoXDIpap2reh2YtS7-I8asW5dCDTSl7TlTckX0YpoM2aubWbDvxqrtIobZRFoPbiPBpE2V8yMHJdXDD0x1cPfYacZgDUjBxgB7GVMxyzRGOl4eCFN-dOdzwOvXo9pCmWllqoCqn23cfd6nCBzIX4PIry8r1VIoo9hrEcRE80dijQfcdNfYTHLgvoyg9lVWzjkUyHQHRIhdYVVO5e31nGyYJ3gLDKTcvrBFTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه‌های بی‌امان فاطمیون در فراغ رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/665824" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665822">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab42ac3b54.mp4?token=Lh-8SP3iOj3I6eZ8rx0HQRd_QXHeGg4lVAnV2t9DcR059iZrdCfPCJYFLw2YK-67pjVYd8g0T0-dYTumNz8raMZNvD9iK6I37uRm61WGo_5zMPvuak_HQMyGvtchNknUO69vViZYdDnKByABm6IQ10A_jjahOb8x7wgmGy7lsMS2sQtMubSbYwCbUN_Cr4TOMu0fJ9Rv32Rb9EgngVu-PJXeSonh9JZXFpYy0T3hpaf1-cZnh9zSVoU2JbEhBaHmumkuWsGtjSXG5IOUm89azARHxmjyqVF5sJzVEC9hYW-W0ajTOUMHJhcxwnz_Mqi7jM8iCJ5haaJp47rVxIXbQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab42ac3b54.mp4?token=Lh-8SP3iOj3I6eZ8rx0HQRd_QXHeGg4lVAnV2t9DcR059iZrdCfPCJYFLw2YK-67pjVYd8g0T0-dYTumNz8raMZNvD9iK6I37uRm61WGo_5zMPvuak_HQMyGvtchNknUO69vViZYdDnKByABm6IQ10A_jjahOb8x7wgmGy7lsMS2sQtMubSbYwCbUN_Cr4TOMu0fJ9Rv32Rb9EgngVu-PJXeSonh9JZXFpYy0T3hpaf1-cZnh9zSVoU2JbEhBaHmumkuWsGtjSXG5IOUm89azARHxmjyqVF5sJzVEC9hYW-W0ajTOUMHJhcxwnz_Mqi7jM8iCJ5haaJp47rVxIXbQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندگان پارلمان و حزب جمهوری بلغارستان به پیکر امام شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/665822" target="_blank">📅 10:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_ANcvfD_HZTS9Uq0dZEXq33FUkmezKSUH9nvFph9XhmJ88HDAeRpjDaBgQdYeKmMeAGs79JXHSI8c1YYnzQxgvAwg4ZLS7jx3xGmXk32jFwnNygBpj7I4U1xQEhtUPNisvK9dojY6lsfV3AiO60tpxzfe9YdBfzrfpODoJ_v60L5VdhzjNKl58Ay7rzR0FKjkijf4y93W204Lai2mZ7djW6qWw6AkXCUzDM3SnsrjSjQnj4kj2oJIsejuTdN65iLOvanp1hGyNZnHIFWSX1YRk3EEbL6dED3Gkx4EKVHb5-S_TcMZ2ge2tlTKVEpKzGHkyIrcVckhRI8m0tudsOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنده بیرون کشیدن یک مرد ۴۳ ساله از زیر آوار،  ۸ روز پس از
زلزله ونزوئلا
🔹
تیم‌هایی از هفت کشور - ونزوئلا، شیلی، آمریکا، پرتغال، کاستاریکا، السالوادور و مکزیک - به مدت سه روز به صورت شبانه‌روزی برای رسیدن به این مرد تلاش کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665819" target="_blank">📅 09:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f860cc7e0.mp4?token=F-yxY6Vq4xvityomyf0FumJU2q-oELjVHgfLv6y0rgbjyhdw4gNmSZUhsZNo3kLDAbSd-jiKiRIenuBmon6NG003vupV3YdkfAncPvzVZgxnoloXwXVJXjhvn7xN1De76IymM_7c_jZrmbNPtLG5h4g3tG_WZ1rPf4v9bOJPC8AKjgApHoPVjcl2sTNHeDjX61rstHU0JP8wfjQLOS2j8cuYDOq0yAVijyO8cUetW0ThMIm1Z4jMRpNEycbwaky9A6qoOiqhsJti4bodkG_CoUpY3eE1ytcBO2ibmUrTfnx_O5wETEk44XyOcyyrnmVTjDBJW97QhCOEbNgDONmTIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f860cc7e0.mp4?token=F-yxY6Vq4xvityomyf0FumJU2q-oELjVHgfLv6y0rgbjyhdw4gNmSZUhsZNo3kLDAbSd-jiKiRIenuBmon6NG003vupV3YdkfAncPvzVZgxnoloXwXVJXjhvn7xN1De76IymM_7c_jZrmbNPtLG5h4g3tG_WZ1rPf4v9bOJPC8AKjgApHoPVjcl2sTNHeDjX61rstHU0JP8wfjQLOS2j8cuYDOq0yAVijyO8cUetW0ThMIm1Z4jMRpNEycbwaky9A6qoOiqhsJti4bodkG_CoUpY3eE1ytcBO2ibmUrTfnx_O5wETEk44XyOcyyrnmVTjDBJW97QhCOEbNgDONmTIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد خشن پلیس آمریکا با هوادار تیم ملی مصر که در حال گرفتن سلفی با یکی از بازیکنان این تیم بود
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/665817" target="_blank">📅 09:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXD72h4laj8ENZU7uoMVWzVtosfRi2kT5COoOvWc3TFrFZvIPJRDYoTqLZGHFCXpNPQueyZ1Nn5ZrvVMgE2PHqGE1QWantaivErZ8VEzSM9oBC_jswv_EDIzDVy6DtFFGHoXcAqMkwYRfgsYePHLkEh9v8gzR8oZ5kNgAvYdi0Jxdzgc9laemqoskp5ClWKDHcWqdHCNvYPzUpzD0UqXyZHOIoZEkg-1rAecqrRRCw56g3xOslNuWCen3rmjD3qGAXftUSDH6mjGx0txHbseJ89WGZFgPQzICxNGYALBCGhVnhveD_UdbA9zmHYwgU92NLL8hfO7qzSqNGZHlYdN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ادای احترام احمد مسعود فرمانده مقاومت افغانستان بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/665816" target="_blank">📅 09:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665815">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYzqb8VwBhFQY765sUqkrYsJm_OxBysyhKzYZPpVKg_sbLtRvpL0_azKoCr1BqncoeffWA1z7No8dMgnaFEjzqhl6S5yBiWIHg9Lp8lZ-IG5YgBdZgCLXFHgCRx0aFinXTg9cazZj-sdodsEQQEcb_3q_HkV_CzaJk5UptjeEAPMOWy1ZBDmQ6nXGusPJKHE7A2h2fA6T64KPRDaqPjldjGpwJ3GDImfgm1H6QcF8wGaPcyB3GCBG6DwKHreuFeF7Cu6GIYN_Viz0FzRhJDV0wvycmoJOe0_BQeuVcY4DX2yV3Dpn4uW-cwry8-WAiMjErpXqLt69NJPxIi5ms761Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشیدن منظم قهوه تا ۶ سال مغز را جوانتر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/665815" target="_blank">📅 09:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665813">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCSRPvfr_IuzPrFdvy0IEu49EDDkjUtMvM3RhozO-WU6ScB063D0BZoZ_GpqACnsFyV3aHv7P7HQbmTOoaOyzL5bKAx3fY4cca3F6cIsGo6Hz8JyShEJtXE7YGBVWPqVGJ6mMmMolY0IzSb56ygTWA04DlWZXuwNNIDx-5qafAOzSN22SIPx2Znjog_bsuiFWZhIA098SbZKn7gksLIIjZVBlpB-c4DuJ1TXiz6i3oSkZhD4y5E0erQ-rvUcWi8Ne8EagaPrNT5-BUo9AO6naZB1z6sfDJngDILQjPHjG6DwXlx-PvhVPkyqcnMZJ2W-nA5haMSCOVGkzLu2gY-pKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود پیکر مطهر شهیده «زهرا محمدی گلپایگانی» نوه ۱۶ ماهه رهبر شهید انقلاب به مصلی تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/665813" target="_blank">📅 09:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f5f27434.mp4?token=oPljT9eykgWA17H7WzWZyY1C373zwzU5FKnl8s_b1QHcHCH00i0egiD7aHVoaS0XXVjwZK9Id4Rd2t2iaeogLaf4n5B8Iv3BKrMGi8yoKiY2ey_XsiXcNgJUhVoRNjKiZvwtSVJlSccgLBsRPmYHbl3R8sxFDZ-3TyWOzi0-TodQQSGvL8IxQnOTw3bjx5h3SATazdD7IMLQ5EeQiC9u1WzSbYwQmAjtpqewfcnUNz6ZLfWqMlt8_qFMyXrd-ee4QOLf9VipxnCIrtbDXUOFor_QDxkPAWiKzMtlXl7ZBMvI-toEGCpIRkFly8sGFSC4h0603k5dndwdG67L0UL1q0dBIIzmJwpqWH4TEJ3vwlkXl_b6fLcJ1Y12wiLqPQC_TL2W3AwST4kfh63lDcODnhZmCGaIn5N0Ed4kKWAPmHW4ISXfhC6y77mPTTsUygGulHQOZ4C0s74rdAzpXGNbWVWDbnrrGU8VWvcO4ZJ5kyGzoc-_Pi8nkJ8joXuHL8xHCd3lfqv7dLunZYBlSs9ySbd8p7aRr8GkG-kOG_2eBych6jetK2tmLTZRFpk1YYMpFAyPzJ99gN4lSVELRgVH0hnlYV7RWaE2FJIUCawRJaVF5W5zBicSMN7CVeQnqNJdBrmL9Ca4_Y3wfxl2Mh-RjkaFRcEMTkF2rV5ASU7O2OY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f5f27434.mp4?token=oPljT9eykgWA17H7WzWZyY1C373zwzU5FKnl8s_b1QHcHCH00i0egiD7aHVoaS0XXVjwZK9Id4Rd2t2iaeogLaf4n5B8Iv3BKrMGi8yoKiY2ey_XsiXcNgJUhVoRNjKiZvwtSVJlSccgLBsRPmYHbl3R8sxFDZ-3TyWOzi0-TodQQSGvL8IxQnOTw3bjx5h3SATazdD7IMLQ5EeQiC9u1WzSbYwQmAjtpqewfcnUNz6ZLfWqMlt8_qFMyXrd-ee4QOLf9VipxnCIrtbDXUOFor_QDxkPAWiKzMtlXl7ZBMvI-toEGCpIRkFly8sGFSC4h0603k5dndwdG67L0UL1q0dBIIzmJwpqWH4TEJ3vwlkXl_b6fLcJ1Y12wiLqPQC_TL2W3AwST4kfh63lDcODnhZmCGaIn5N0Ed4kKWAPmHW4ISXfhC6y77mPTTsUygGulHQOZ4C0s74rdAzpXGNbWVWDbnrrGU8VWvcO4ZJ5kyGzoc-_Pi8nkJ8joXuHL8xHCd3lfqv7dLunZYBlSs9ySbd8p7aRr8GkG-kOG_2eBych6jetK2tmLTZRFpk1YYMpFAyPzJ99gN4lSVELRgVH0hnlYV7RWaE2FJIUCawRJaVF5W5zBicSMN7CVeQnqNJdBrmL9Ca4_Y3wfxl2Mh-RjkaFRcEMTkF2rV5ASU7O2OY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام مقامات یمن به پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/665812" target="_blank">📅 09:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=hLc8TpQDZFhs2h1bMQTHcXdL2LgKOLwCt9pvqzaf8ixJgxk1KTXfO2vJB5e3oguhHS_w-YUa6y2QWg-TAZjs3RK37ub3S2E1I92KP2NU_LLVVNgGRKrmfmQMKADmWx0Kso9h1E9BlQSTKG-uk5uCFfo3I_DceiZlqRTuoT9Cjfh0k8soLGKtk8V5Vp3bQrsiPM5v4spXG_zS7HYI9gPkDklfw5LRRZ5IU0JCD1pGIKX1U1WXvSvFAUEromHKmmA0r1kqcKq_PhRFy8l-9VG0WMYaBJOHA8FI2O2Bqe8b5uyrBqkvf1N5mfj9GbWNKBVeky8RsgtKIaK1XEWyd8TzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=hLc8TpQDZFhs2h1bMQTHcXdL2LgKOLwCt9pvqzaf8ixJgxk1KTXfO2vJB5e3oguhHS_w-YUa6y2QWg-TAZjs3RK37ub3S2E1I92KP2NU_LLVVNgGRKrmfmQMKADmWx0Kso9h1E9BlQSTKG-uk5uCFfo3I_DceiZlqRTuoT9Cjfh0k8soLGKtk8V5Vp3bQrsiPM5v4spXG_zS7HYI9gPkDklfw5LRRZ5IU0JCD1pGIKX1U1WXvSvFAUEromHKmmA0r1kqcKq_PhRFy8l-9VG0WMYaBJOHA8FI2O2Bqe8b5uyrBqkvf1N5mfj9GbWNKBVeky8RsgtKIaK1XEWyd8TzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سال‌ها آرزوی شهادت؛ سرانجام اجابت شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/665811" target="_blank">📅 09:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9688fa726.mp4?token=ZnjS5hhC6HXQaaF2uLqTj-rD5nx28Jhn69AevMgRmd4gOw4eATp5BQ8l2horA8mbTCvRnbvN407KxBVlR_4EUqVhV9q7XJMlzgz3qYWxg8_iaTn5qdKCF9YDY2Bct3K4ybrS8vomr3yBVYJCEVcTwyVNlnCQygcZ9ecLSx2yrIVn3a2aoYdCo7VShyF6Ja8vlN28JL-t-HVeRSx1j5t1rn6-XxJpWp6jBXNQAq0_jXT_OGQ-lBohKJ6Rh00JVf2B3qJaqSIPiWMJtFCm6MbzGCwASBAEYHppaPbx63CeGm8n1_AbiioyTNZ6iFTS6qg71JCLeS3ZhXt4HyY92zd4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9688fa726.mp4?token=ZnjS5hhC6HXQaaF2uLqTj-rD5nx28Jhn69AevMgRmd4gOw4eATp5BQ8l2horA8mbTCvRnbvN407KxBVlR_4EUqVhV9q7XJMlzgz3qYWxg8_iaTn5qdKCF9YDY2Bct3K4ybrS8vomr3yBVYJCEVcTwyVNlnCQygcZ9ecLSx2yrIVn3a2aoYdCo7VShyF6Ja8vlN28JL-t-HVeRSx1j5t1rn6-XxJpWp6jBXNQAq0_jXT_OGQ-lBohKJ6Rh00JVf2B3qJaqSIPiWMJtFCm6MbzGCwASBAEYHppaPbx63CeGm8n1_AbiioyTNZ6iFTS6qg71JCLeS3ZhXt4HyY92zd4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام شخصیت‌های مجاهد حشدالشعبی عراق به پیکر قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/665810" target="_blank">📅 09:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7188c59e7c.mp4?token=WfDE7FV7_dyxPZxnx3ZnV0vCXN3n_gAKa2wyL1VfJsXcbPoWu94E7WwKBMJwpxDYHUkeohbBSeZ6B0c6pQawbjJ_CHIksg92F0GXXBAU6cJSTIGUI0swIMJkPkdkkgirniIbwOm4NYSINQRiPzy3i2JEOv135WKG21MZdR0ViMTk1cQjC7RL_8x_kpOKDMFIVxxy290aLUW2Sh96kUZEoXRpCrNTmyPhcT7p5QdBCEipzjCfYscE8HAgec3dQhtIwhK2SQedBH7EOaSD7LZbCRVqZlnTsVrvxBXMLrbkboOWc9m6EhubdYuOh39Qyt0zIRm6eUI6wKqm4XW6KN738w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7188c59e7c.mp4?token=WfDE7FV7_dyxPZxnx3ZnV0vCXN3n_gAKa2wyL1VfJsXcbPoWu94E7WwKBMJwpxDYHUkeohbBSeZ6B0c6pQawbjJ_CHIksg92F0GXXBAU6cJSTIGUI0swIMJkPkdkkgirniIbwOm4NYSINQRiPzy3i2JEOv135WKG21MZdR0ViMTk1cQjC7RL_8x_kpOKDMFIVxxy290aLUW2Sh96kUZEoXRpCrNTmyPhcT7p5QdBCEipzjCfYscE8HAgec3dQhtIwhK2SQedBH7EOaSD7LZbCRVqZlnTsVrvxBXMLrbkboOWc9m6EhubdYuOh39Qyt0zIRm6eUI6wKqm4XW6KN738w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از مجاهدان و شخصیت‌های کتائب حزب‌الله عراق به رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/665806" target="_blank">📅 08:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665802">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsKgTaqwTo1wTqpvBd_XGETgcJpSdM-FkETWfX7dBKV8YmNQsFxqu8Q7qCDuoi_sYVpJl3682vEJYxxHkeZlzzbDoxO_TPZ_XPAF3J7fvkBGF9cKdu8Lv4aKnklLsWMm-U5p7n4rwoC-4H0VTHOu8aSOBfznHMeiAtklG0-1vYfu0Sxp8YuXCgVyQQ2JpVVXG6YT_T1K9QkhyU2cJrs5dRxlHLojrRnuNjGf2okSPt-DM_cfyohogQ1Q_fwcLrZmyr7M8p8nfqQiyqLxN82oS03_tB-eH2X3tOyYrmesBa6J_BJDal97snldiLMFZ8nPJnMcyCqq4SASK0_oN1zJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار جام جهانی بعد از پایان بازی‌های دیشب و بامداد امروز
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/665802" target="_blank">📅 08:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665797">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNZWiLR3BtFDBiKU6LRIzHGjN7WWksDtXBbLy5cMZz3qV4CxgaT0GLW2bdRpKkCDeRiAjbK1VCRHgUTO0faD_XpciXTd7aONfIWANh4GshIUuJ8Te0qetG8qYknfOz-bIwa8AA1BiletqWDkdyBtYyeLd7CHKxpMbf9CVux2Yh9h6C35gzJMeiZaGEittcv96tM2ntJGJrH5CgHYhmBujcNE5HA2qnG-7014UD1PZXuSCKVLSfJHfYWsCIJUfnA5VXuImZ9XHVOhlxHnJbfOu4DBTZdXe1t-oz2yDiTeTZnDnkJYdI0cLRTuJJtehXCGJbFs91xg9QZJhpknlDCR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epX9HGenDRM_y_K8b29g9AQRtqwsXqwGCl3gFZ8HADbS0660hO8w7IcCJ3VdFH4m3KRTGGRVoCpZ0CJwVqA_NQqCqsQouf2dvjsq8boXNfjKLgHf-dW0O3tFrVsIN-X_6lroysTdkiLB9fYVaJULI994uGV99wUduCFhtn6U8PdN57CUbKC-VG3sAFaBqcOAddZveY3z7ltQxzCPU2sRJpwJiCGxZU9X3iFolLOWCVkKDm4tRvxShk3Hc8IPLxoAvwdc_KPnMZm-Ha4PU1z6Wh_-WGUnc7ShtZ6N0E1P4hUkxSAHwcHCu2PFEOMiAcagNogktt-rXYHsiZ1bXHiB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFhArc6_cXXl4vr77KR1g_P7nukpEzoNGbWuo8GVZgwABXyQI9a6OBTIWu7YSPK9Q5L5YNPMtQoIUUlFA66-tuTlH9vtNq8gAVwZQqHulYYsGKvTHgTdL6aw-7PZsFMQSDPbi_Dn6X7FZREo4U2RcUEOVwA72Hr19GpnvRbsrizmujPfQWPKq9z-U0B4lpZNrsDQtlWWa2ZgDKBgAXRhgXjm8PB4kvX_C7ZuUfzK3LuL1QXjH7z2narIxipfG8Pvf5ZtfGV8Uy6W72PQ6FpN8HskUx_tcmIlnJ9picAB6rd4URaZF6FPGB4CVOYLuOEd9r6fdWjkF0MQKUFsKiG2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVIWWNBilQdDSmhi6Ymo2JfHk6H9iLPR24J1WMKEI7QlzO4UYwsoA695uQWduBWbNtw_wGkr01I9FSyNjc9T3qgAwQhHAPu-JXhCkkHrRl2rLr3QnBH2_lN9hKGTZwnPGTEGPzdB45xX4tYWzTjgmitUh5mZZKM0lMwtYKk8flvINyiZFD-vkAxihmSdz0kA8a-DozVkGRrBclcoiLiH5MdbAuY80zwpNIVo95O3H69Bc8RTyAX6ThziL1V45K7uTIDT0vLLrJE_YlmJwXyd580Eul1Pfdgh3VZOpiCs5ILG8amoMWsaqtnUASotyJz38LoZVa1ThNTYLCu85HHe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Co2DkgYASiF1lBOiay2HHN6sDOLKU2wuseLC53b5X7Rsm8WE_chjmD0mrgBHQVMl_p2RpRt58Q_gdbwZxAvq013wDOam7P5FRTxAbtrVgL19YSHXMFhmrGXcbco6_HbsABjL72XMPyFUcU_VnpuDJfMaznyGS1Vv2g-4IAJV_7yPHVmXFtm-R7IL1hApfZj2fkStMNuP3cregEL06Sbwi9crsQXzi4b5Hiiseouw6IsDTjF-kiqzRwmwgsh_9EyRa5Zpc_PSH-8nkHgRb5ws07IcPKIl3JuItCXVJcD-gGJMid6Jcyt3QB-IH3B-n2l1C6JNKRyZHXahWBbw5WLHGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حلقه‌های اعمال محدودیت ترافیکی برای مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/665797" target="_blank">📅 08:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ddf75733e.mp4?token=DU_Kg9qOEzLmSfNgmM8imjbjLhh7sVAa4vWHwWEqL1B1sVzRzR9XJsCUfa-YfTpx-goHqFklLmJkmMbAeCx0CamxDtTz44zIcSdwlXWcL9PBF1ZhdTEm67orkLlMlCN8U4mjLRPezLJZ-5ZVBoeh7xqKHcMMETRTeenNiWceFT0Jm6EO_dJZ-xzG7dg6wZ4s2i46X35b6fmsFkHf84L1itzgF8NCvuVoxrweNmNiGJ-KYQKS1Fm50DcyK1MDeefdYhjx_OvllZFmdbriN5_QOO4yTriUR9cTxJIocOdG5Vq0pYNR1rMX0ZLOgnonApFc7fO4DAy7_oSEUz8X6qd5QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ddf75733e.mp4?token=DU_Kg9qOEzLmSfNgmM8imjbjLhh7sVAa4vWHwWEqL1B1sVzRzR9XJsCUfa-YfTpx-goHqFklLmJkmMbAeCx0CamxDtTz44zIcSdwlXWcL9PBF1ZhdTEm67orkLlMlCN8U4mjLRPezLJZ-5ZVBoeh7xqKHcMMETRTeenNiWceFT0Jm6EO_dJZ-xzG7dg6wZ4s2i46X35b6fmsFkHf84L1itzgF8NCvuVoxrweNmNiGJ-KYQKS1Fm50DcyK1MDeefdYhjx_OvllZFmdbriN5_QOO4yTriUR9cTxJIocOdG5Vq0pYNR1rMX0ZLOgnonApFc7fO4DAy7_oSEUz8X6qd5QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت‌هایی از روسیه و چین به قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/665796" target="_blank">📅 08:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/702696af3d.mp4?token=rPjTw8ctNAuB0NdZc0Yh5klj46bohr-ERGc1O41uldstEETgbcOaiEvWkUz_Wjx566LBULix6g8Cj3rqQ0zEh2jNns13YAUC_ddWjcAnDLXSidsp84Bqy8mKSpOBj9P3Sf8II72j4o1SNfEAVaNB993sy3KoMFuseJ4JYqm_D8F8_km1LcLhrZDOCuNMbWZfqVohBarhf9kzXs2CNFz6ROaaryRZHpO46m28fmuM2e8pbDWif9pHrgCHGn0P5wywkf2Z8fWyNBuoQVLja8TmC1waz-pHPrKGULyNGrjjK7RJIYgUdP-sVLggyDGVoSpGZa4V1YPX2zyFI0dwAZWmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/702696af3d.mp4?token=rPjTw8ctNAuB0NdZc0Yh5klj46bohr-ERGc1O41uldstEETgbcOaiEvWkUz_Wjx566LBULix6g8Cj3rqQ0zEh2jNns13YAUC_ddWjcAnDLXSidsp84Bqy8mKSpOBj9P3Sf8II72j4o1SNfEAVaNB993sy3KoMFuseJ4JYqm_D8F8_km1LcLhrZDOCuNMbWZfqVohBarhf9kzXs2CNFz6ROaaryRZHpO46m28fmuM2e8pbDWif9pHrgCHGn0P5wywkf2Z8fWyNBuoQVLja8TmC1waz-pHPrKGULyNGrjjK7RJIYgUdP-sVLggyDGVoSpGZa4V1YPX2zyFI0dwAZWmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از پیکر مطهر رهبر شهید انقلاب در مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/665795" target="_blank">📅 08:09 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
