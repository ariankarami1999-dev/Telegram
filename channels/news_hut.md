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
<img src="https://cdn4.telesco.pe/file/o4bLWi1ynTFG6MP485nQhDfl6LyZBkKmNVQg24VmVRPLvzpmcy1VELVVw3fq1-B03ywU8Y8gllbWetlUlAWgTNGyZAQzzxJE9YoKDtzYEdMCUUBKssz1z0DZTTafEdA4ZdUxz_G1msnl8vr3q3H3dOvRZMqPZnrqjLdzrjAr9DB3r3sDrUcx1-cxp3ZQ-HnCMVXeN4Aqn97geqv2tLVgCWagXeLJw4w67mVd0M9n3uqtG3whyXGeHsyhPYF_JwSvcO4RPwnyqSgkCw3TW_vqCn-6okjheCFwLc6-dTDLQP5St4p56I9bqSKHs5J5tcKGcfeI3bqQwu_uKMD6HgwGwg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 138K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 22:26:03</div>
<hr>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL1s92kvkA5Ptg-lylyZx5__Mo7O17Irqtw4F6yl3sYC4-4itjPzYzkzm_f9qgtD8vphPSL1qjbwVRw2w78h1gU9kQeJPnh55m_-cqjzrNJs4FWuVZJouhR0XsBRlJLk9TCVoAHyzcjZPpG-kAwlWSse21szA5h5cFOuNj8E4pknqDTbBrV3eJp03RsJnbVEe7uEyCDnmM6Dve4QIlDkNfObLStiF3FrtAMbhDUv6GTT9f1eixWnPtwQ0tBH5Cp5E1t2K9aALWOt4aWE0q9ddIWqF5K_c_AwoVsvueuqKS3X17hfma2O9vlSbQEhEl8y8KhBij02v7jh-YJyEdm1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBBG_1qdu4hhrIBRNVCQnJTRjZEjl8F5O5p6_XQrCz1KHkgPCORrFPRlogjcgNG26571ZISY1G-Z4Uzxnhp-tmqHL9lqat4tH23g3-D1gfI_hp6U74IGthxTYDMFBNgB1kbwSFbs4u037gjYAav3ymLUa1TXQc7Kvl0rWFmt5VslC2_PBCxCxlxoBsIBeS1nlP4Ii0EbvR8IPj6yT7pFFqcXtg1mFBKqQ67QcUzOyNSZIaS5C7cYuXL0pCDNFeK7-OiT18pyidzY_9KIw1iXGnWJJdOtL4JfDGIUS_YQufrtxO_glvzd0Fyyvg-kinUjBdk1n82v3CIa1ihA_fDFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iP0Aa7lfHfh0mFUo_MGLEjZ6T4hzHIksQTI-g_XVrB-V4mmKZYHO5K6UyBjovAt7zkvVLPgs2y4QApzfRaf30jY3usRIc6gbSccWs6Pxtl_MfPJw4PTD9TjAhjP9FvHk7RrRNBensqGYaqgcoP3T2CNB0QWBnyUtM_CNiLiqduG_CCHIAis-DDUvtJnvyt9QwismU2u42z9w_BPnBXTw9QfgUgHRVi0RIQZwaPqZFPSzS2BVKHi-UMV3UdbJmMnqhmwKLt4pjo7ek_r6N1UhcgOozDHbaENP9OzxzvnwBwgwYcSZClRvgJfOWVG_GFkQxFh27VulQljkLUiH6YFdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQcLTr4IY-wbLnRXz2_hrXQNgXq2n3BHrOCHgaj3eVVBcr9v-TLvnjj1pvgMQWyfpq-7LZ3lM5kJXrfYcYfzkE0RfAR3pVONgyUKMMZN8cVXMPqfHJ-qvLsgw3l0BhS9M_QPqIN4c3-0GMXNqlk9oi2jpkRIOzOIVkwbWpDYCbCrX5sJTF-PhtLejDQkmvi6wOQMTFW_dwdDHETz_-OIxoIvQgXJIP3zqTvFovngyfg0YQdnHBMVewyHDaTaBwUylr9hvev7STj0gMb18Ir5u4A_CZ8elSFAvFwHbgaXm8EmOGhnn9FoJsXIjZX4eGjtlVsglt62RFkP1J1GUzWu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MR_aTOIOg2pBNpZ94ARLKL-5qCGW4iYBU8Hflza1sp4UO8gYk1cSSEbIUDRpFRmK_pfGiyvOxB3BQ4jdMBbcZK_f4MvlNrVqAF6xcftwzfZn7XDputhXCdsNkK1UBDdILNctsBlTAmQwRP2Qbu_wBJkWbIwrZqI1vqcxmWA6eSw_24VYSJYX0kf5B5Ct4KtgYwnjMvoWHCyyewqMBtmc-amWMyDN8qotExyRGbrLKKnxo2oohC-XY0AQoIDXSiU6ZIZSDTzTJvnPbqutECE4iPTyHX-8Umo9I7yopTM08xzr4fUkoOcRu8n6vnCQqFbQr0pyXMdpNUTaRyi_BoKv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7otGrCrbcsOxhQXEY-yoWBHhVl-Oo5pjxzGYP0aCvsMsXigRo_3Uba4gh29ohBIX30hxIzHM74q5CmBB5Yhc9XXKql1TX1NCbvyQRwKybxxZ-_GaSFlSG2lE1fnboGCc5-zwNBOSH_QnJK6T6zeFDquPsWSy0KTOi7k4TwApiEU8WxM8fqt8Ut02U_jARXsOKfiQi_59QRJTJlfKrer4Hfl8RUuPbwQNm8aclg5x6hVxyK7xYJfoaz6RZRmeKYR0d3ZAm-VG4LGxrpxktMdoH-JPUzrwTHFk701SLL0duRG3VKnNefWYzqOImiEMkihsyDYtMCgYMnXlvAi7If2Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJM17yeNfuzPfEYWxUDhjbIE8J7UYie4CvB7XX4lSQEd07TOz0apHJtAq0JexZWe7wPrCulq5V4TTutSe60zyz4Ia6OzgZfCcrofAZHH4jCiZCtee40LMKAc_vIvZxq-T27iPLYREG98B_aKOvY_H9BL-p2_4gRYd-ImWk8oz9-H8G1W7WXkizXfQEwIhmlCjmDwgvMnuc-SGalEdujEjEptu6HJ4VkJb8LhZMZVkTYmBQQx3YVwcPWzBhQTlLfi2Ce-ClxLZYLoPsIZ03A3sDjx0KPKARJ_xzgm7nWATiEk8fKrdHUdGYbZ8-uHQVPC61wMmN2aOqACyz99QE5JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRrOuXpU1bwhvctyNWSCxmbU4h1rVkuw1j6Zwm4PvD9LuvtbUBvSX5Z4hRxhwvpjJMoczksfuKNIVcwrz5imunB3T4OExdUCh2ZdOVOXEaOk9YmmoUPA8Y21xpuLegX_F_4RnjDF1BUU03cljF7Gs4V9rVJcJ7fETteTBNSWD_f1rvA8hG7TsjLBEXI8ym6hPK48f-7PYPLIPYDFqEp-tkN6QtJOHhq1DQs0X7PyfME1z6CTaBSUCsZ3zijkOyCegdbPvXzsqymH9afE5gijAfdkDZ5xCAskfmZz-HYBnLezBUCJQmPet51enicbpsr7cYCeAW5_4TUuqtrAzVgzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy1abK5BHuol529D_5xf1Q2iHD2NIjRgHITPtc0q6B1a1-sHniVOwJ5ld6vyvGRE5N2WZEHzKMGJmP-szoIqz155IcCHvcRK9N3XCCT6dCw8pGDIRozMlVyqq4pQfhjXidG0yuEUMVp5Ao8snP6fsY8cvtQEZu_T6lJsWd9i5iEH7XL4CF9mKmgo4v78bpdgDEWBVK-5h95JKx1uX3zU0cNI5WxleTGe4vCM6JdGgi5OXi2lL2ZsPRoHWvXwNArt9X555D-7PCCv3uv0I_buZAgaz3bg95FvvhTaYZXrxYZ74lb5wz2EP4p6Ip1r9rxRwGQ-TeelyxjNbpzYcUoOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=Zyoa9hxNrjUe8ItAajFf707Z52KxKmKgFSJ7ZbC4ouyowVlD6kPmzgA5RksMZwhsxYSXoX8tToWpC5uYNerWk0Py0MMuhOS141x7De-FLFfHRdr6j4Z4YV5GoHpOGLqp0EDGn1-7Q5O3k7i8FQbfGUuokkHsGMX3exdeFlP5w1qzRqPeA4pJZYb6lnNiQhyTyeyn-3CJMpcVbE3I-1L9ypSZeG0CVR_OX5DTCMe0D4tFlWvYbwYUnhzZvjuCGI-QBr2Ic2NogO2i_kVdbz8Sm7-gVmEwzra6qwzuppA1mC0CZBDrcZTM3cEyLYYpB3GWQbWb9E-WmJOhC_YB2wse3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=Zyoa9hxNrjUe8ItAajFf707Z52KxKmKgFSJ7ZbC4ouyowVlD6kPmzgA5RksMZwhsxYSXoX8tToWpC5uYNerWk0Py0MMuhOS141x7De-FLFfHRdr6j4Z4YV5GoHpOGLqp0EDGn1-7Q5O3k7i8FQbfGUuokkHsGMX3exdeFlP5w1qzRqPeA4pJZYb6lnNiQhyTyeyn-3CJMpcVbE3I-1L9ypSZeG0CVR_OX5DTCMe0D4tFlWvYbwYUnhzZvjuCGI-QBr2Ic2NogO2i_kVdbz8Sm7-gVmEwzra6qwzuppA1mC0CZBDrcZTM3cEyLYYpB3GWQbWb9E-WmJOhC_YB2wse3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=UmvxfA22w3eb_CUmsoMoP-AKyxUWG5hnfDRvjcB5YrFU88jxNarOQ_m5nQn9UgPXs64TY1EJOSa6XxE7O-8F7lrb9lG410qSY3GAdl8TSxYD1n-QRwNDX_Qj0DEE2-3DN4f5DaKPFivuPcQXi1g1RD3fRAiaQiXvYYuqPBNdzhag9smf3mO8lk9y-PgeAt5QBVnkWHdWn8maYN03C0GO1sWFnjsUVUIa9M2SVz-pTQZJQxSn3n0Q7MUXeFMD6aPZKLAVSU-tc_lH_Gylxmzy8OIYlRBNvVdTdJGTMnq-phOzf94wmWPlokhqp5gKbZPCp84Rlgv9FIlUFy2PzjHxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=UmvxfA22w3eb_CUmsoMoP-AKyxUWG5hnfDRvjcB5YrFU88jxNarOQ_m5nQn9UgPXs64TY1EJOSa6XxE7O-8F7lrb9lG410qSY3GAdl8TSxYD1n-QRwNDX_Qj0DEE2-3DN4f5DaKPFivuPcQXi1g1RD3fRAiaQiXvYYuqPBNdzhag9smf3mO8lk9y-PgeAt5QBVnkWHdWn8maYN03C0GO1sWFnjsUVUIa9M2SVz-pTQZJQxSn3n0Q7MUXeFMD6aPZKLAVSU-tc_lH_Gylxmzy8OIYlRBNvVdTdJGTMnq-phOzf94wmWPlokhqp5gKbZPCp84Rlgv9FIlUFy2PzjHxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=MvDpeqHii2NwLnb3Ht9QocotGOmUfYY38kR-B4wH8A7eTVqz4ZzI5DgioFR2weNusZaijt--LWEzzg9gLGOL2TioDHPQO3AD0aHvUQrAj41ZXv4FRubyGClBCf8FNouVofITrG_l8pMQB9Ev-JlhmlgdZVXbtSCXF6_1Gb8-ivAvMgs3dm-8ymD_dd0ujyBKMx5by2pDjuFBHx7YptyWVm-DKojx4_CKTn_PfCWn8Yvd9C4niufTHgrTSs_OHoTQTXbittlFk4seFG3RBx-9wEpjqt0gvBQbmE2Bd5Hgwq5sEce_OhqgKo7wjpv_M0suqbtB1bwBR-n4Wk7MfF2TPFUcK76grc3NZ845ZSgzMFyIG1S7Z7anahFDZwTdROHyxLmbJiIirPhCbYe_vvhvFUuK88ro4xf6psJ09A1nsVAfGGlQ6YuobjoyyKYsFv-lW9j1nGbKToZmIaXIg-8GoLiI6wrxe39k2khoY8sJ6xdhWS6u-m3f0kOI523lr16Z05VoXp_uyTVgYe0FUyYsIzy6piyMuT6SCbOYOEf1n4qna8F19UJc85WOjmEexAbGwfxqt5Eh9Acq6ORNNE2aTKPjYD1Ni7tbqi-uFS_tSuOj25e5gQ32umXqwF5tTCBVOasXrtCnqpIr5yPtG0JQY8jAMM_l9fp-2RK_OpKQyQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=MvDpeqHii2NwLnb3Ht9QocotGOmUfYY38kR-B4wH8A7eTVqz4ZzI5DgioFR2weNusZaijt--LWEzzg9gLGOL2TioDHPQO3AD0aHvUQrAj41ZXv4FRubyGClBCf8FNouVofITrG_l8pMQB9Ev-JlhmlgdZVXbtSCXF6_1Gb8-ivAvMgs3dm-8ymD_dd0ujyBKMx5by2pDjuFBHx7YptyWVm-DKojx4_CKTn_PfCWn8Yvd9C4niufTHgrTSs_OHoTQTXbittlFk4seFG3RBx-9wEpjqt0gvBQbmE2Bd5Hgwq5sEce_OhqgKo7wjpv_M0suqbtB1bwBR-n4Wk7MfF2TPFUcK76grc3NZ845ZSgzMFyIG1S7Z7anahFDZwTdROHyxLmbJiIirPhCbYe_vvhvFUuK88ro4xf6psJ09A1nsVAfGGlQ6YuobjoyyKYsFv-lW9j1nGbKToZmIaXIg-8GoLiI6wrxe39k2khoY8sJ6xdhWS6u-m3f0kOI523lr16Z05VoXp_uyTVgYe0FUyYsIzy6piyMuT6SCbOYOEf1n4qna8F19UJc85WOjmEexAbGwfxqt5Eh9Acq6ORNNE2aTKPjYD1Ni7tbqi-uFS_tSuOj25e5gQ32umXqwF5tTCBVOasXrtCnqpIr5yPtG0JQY8jAMM_l9fp-2RK_OpKQyQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=mcC25WNjfPpe3mFYw0muWlLVsSB0vrKpW-YRQPiZ5QQbbQqNzhf7jPx-xrI-ZBCBDrqzBfxZmTHbpdGNyRhz-M6uuWl8R9cG5fb4jR2mEc1t2Hx2v2iTJdcBBC3XbbPVblnmHegpjQ_R8e7FGRLDRUy7A99i7o3abFXj2uZKqcHnTalpI_fGKk8zdchHUPeiaEutMU3ENc_epEPndef9VR2iNt7LKWq8bpSKkY66F4e5X86RQ2Ta-_CdTPd0o_yUJ4YaN2Lm-jnM7wHMXvvOmozGzKSq6t1-9pt_s9A8MgpMezmOezyr1YuJutrPzoZd37z4oqCzlMg5BJm_wAdLIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=mcC25WNjfPpe3mFYw0muWlLVsSB0vrKpW-YRQPiZ5QQbbQqNzhf7jPx-xrI-ZBCBDrqzBfxZmTHbpdGNyRhz-M6uuWl8R9cG5fb4jR2mEc1t2Hx2v2iTJdcBBC3XbbPVblnmHegpjQ_R8e7FGRLDRUy7A99i7o3abFXj2uZKqcHnTalpI_fGKk8zdchHUPeiaEutMU3ENc_epEPndef9VR2iNt7LKWq8bpSKkY66F4e5X86RQ2Ta-_CdTPd0o_yUJ4YaN2Lm-jnM7wHMXvvOmozGzKSq6t1-9pt_s9A8MgpMezmOezyr1YuJutrPzoZd37z4oqCzlMg5BJm_wAdLIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=ssT2f86cldWalfTpnlFTm4jcsOzg5RYsgxm1DgNsGRNWFk2qWXlhnkBULskYPPRei1Msb-WTnDMgFNudTJUVpXwAlj5m0SYWXvSiBM1MCbAsaHTMUoOur5HCJ-vkZsvMdJ-DuzmCHO1wtDXRIBxxTb3OUvAx8oQWX4R3_Tk7DwfuFYEQjJ0vd-metaFaJvPgLz2ABqvOFzbelEPRQUFCoPYanE0BH882zJFg71M-WjdnxNaBPkJYlCHFFqi_AUEZrrONWFVdwQdYj3NaWv3vQtsPunKt6Ha6_srRQ0bTVkgwKINoLint3Rf3OHRRF5q588Anq-AwaVg8Jgufqyslgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=ssT2f86cldWalfTpnlFTm4jcsOzg5RYsgxm1DgNsGRNWFk2qWXlhnkBULskYPPRei1Msb-WTnDMgFNudTJUVpXwAlj5m0SYWXvSiBM1MCbAsaHTMUoOur5HCJ-vkZsvMdJ-DuzmCHO1wtDXRIBxxTb3OUvAx8oQWX4R3_Tk7DwfuFYEQjJ0vd-metaFaJvPgLz2ABqvOFzbelEPRQUFCoPYanE0BH882zJFg71M-WjdnxNaBPkJYlCHFFqi_AUEZrrONWFVdwQdYj3NaWv3vQtsPunKt6Ha6_srRQ0bTVkgwKINoLint3Rf3OHRRF5q588Anq-AwaVg8Jgufqyslgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=THLCWQM79ZxNrfw7RzWz96Y4rwNzr8EpZSTFPhJPWrRfJC9maZYQ8MmN7vPZMDBgjoD-9If6U5izPKSgHEeceUgQZfQDERzeq2ZsUvFpanNceZpznoI93yIH7FetrLikmcwtew-PxT8fBlHyeBE1fLRRte-jhjcutUQ2ZAqWGLjUdYnL0EZ2mVBUizqV-osEMkyvA7BefaOwOjQZkYqL23iGl6tIBPVHFcnCP8QK34lYCoTm8oY3W5GN1YuVJXwrUQY2HZkdliaXWCVfAemcU2H1K5LqhpTNgmNpHEflp2bXt01esHz5ubjuurIML-D6J2FyOBNC0EoZrtyCM4auzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9fLWH6pOFQDtAWaRrlGBSZHeflZZk9HVBfdCAbeoMNCA_hEe_mdk8qPJHRWjAbTJ8vpNSxDKD47MPHHSYvBxB_rm6kSaZ4nWGlLy35_g8U1kXkBurxq5yNDCHl87VZ-00lA7WBgyffGYYb2xmopWLPcqNE_11r3kjdTJLqRn5TSbQZowJKf5R5uf3beCl7xbXEAPBgDnnGlW9qyJYgR2pSjP1-cOlm57o2S36hgeJwdip_DO_HV-hU8dNnZ3Yng5NL3AWtKAZ8YjYtqm-S8DK_oPghQRoh5oeEgQqWmrKiTai7jBEprtKH2vOzigB0SyGluDkVNMhrovR8fi1UpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=I0WVpleK8FhuxlwBYV3jnDSbd3zr6pAhciMpRuLs8dJCHjJT-hdPSrPJTOaWCVIAH1AWOTkuo1d4-_uf1aHCisCiptLRmOoiOrQ6UAutglBeX1Rl5RhVCIY8AyWb_Vkp1mGudCMGa3lqX4aCmlvHHJ5rw1EG2sOD7vSFaL8FLRBx3L4l9JBoIp-UzMPuqQeNVFgLX5hBEU7lBhrcyXXqEFrSSbE_j-okh65N0gSMY2zz9ZUtP9tSHKfVMq3YlsMjREXeHwqGYlf6LAsqEJAKuQhXiOWcTFyw04iIchKff_GE9cKMAYvCmdIu3gcqagM4ogSOe7_sss1L5pHR29Ioxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh3fX4vDRDMJLy6yTLWL-2smCQh__1TilPtaFOYeHh9rEcPOh6E9YD6A_5pcLwe6WsKRxx85VTZ2muu3M53ecf_zhbahSIxDlWPjDeUU3kZAMDgfSJPjIFezAsTYSBCURHgB7eJCkZJkar2YTpIkVh4yQQHCOHPMmQr0A0UxXfQH6EKbwjLFLgSH_B3hjfGahvWDi-1isXdHD6IlcCr2KJlhqbhGXrUAV-BjWJlXpGuPyw2XtRUEotx6GRNgY6U1_XqQrbxbL1ox2p9IQY2-Uejq1zgFlBp7SfhAKORO4-cEF1XhuHVwK4cZx2eFNRf2uxZpl-T2IakeaTsL2QjQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBQR8FinZQPg_rF83P-491OUCBhjH4gWDgSw0nxtVCLy336gvZ8vmcb4Bl5l3TofbdIicjwxwuTUsgf6Ho8hwF-PwVxPm5Tp7eqqHS_hU8AlCVLyPyGZ4g5RTi8iRRiItLB5ke5q1SBdKxQ1kxzqgDsKIs31LIyZLL_VK0Ellc7jkTSqxKOcZ930ie_3jk97U_EKQFelsatVsY7Z1TJpulDOlu4ui44wAGYvv5J2O5agnazyYUMCfT1FtZcEFOrxHvMWYXVNVo3AqYQ76V8FfZgB4zWNiDbnubyE9ymRtoM42ZDAAGtL0o75WWoj_VQK1V3NiFVL4z8eoZoRpKsxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzPDK1d78ZZrNveDda3ibRqfh7XAgfgc4SHhHbyw3iwYn5diBasuWFCqOzlmT-NzWOLFZMu7YgqueKGGKTfKp5u9Z113lCUsTw5h6NvjsFUsNjLzy5eM3niN60frbq4zXaL4EB8SdCZJBMQJXzbdqvUMhU49CUIzCzcyP2XGW6P8UCwQh0YSO246C6flJ44Dw5h1xvxV3zwdZSMpyHi6P6F0sKpj6dp7MKflBeLqNIBGvGej9OvmgtkxWXb172G71DGIe_-M2CNR-I-kyfNPdXxWkZJ-7xJTEpt3ye2z9XFl1HeNthcswPd6CoThmLeYB7kfGEaxVfVoh9MShysgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdyGZEQu2mAS4NnT3tL_aBrONKD8G3ZGd67v5Je3jTQ0lz4DQ9iNyq6UGTnEVU2F__dVUgdjfVL6V0bPFhiKoa9PVBfi3_A2pa2CEMV5PCUKq5Tc7XPMJfoHQL-0K-PrOIyt3rCEG67_J-zdOZQe-gOGluziWzkMvfGzMPBlNJhCu0p9kZukAHJZoEtm-HcNtn514ZKd__xLwqxNATn77Uprzbwl4OUf3bI04JG30jG-k_E3LvWy4zg2kVxnn-Eyg5_-pk30jakyPx4xFGp1rUz8oNnvnk0-JE6iDFYCU-12dEF5ldRsZf57jwwhFl4BP4kQWp0lZxpMMtwmBzRqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2Qr-t9v5KPtgHn63Lbn21DoaFI0jeMST9-f6SIhVguyRbl-ShzxF_5AUIjMS314AiEUV4S1xj7pku7Y5H1-ZkwYFeIwqSzBqs10YZihMRHS9-DeIUecELIrsEZHcpiCtIfG2AmqoaTKpZHQ0Sp8Lxj0Fh53U-WmX6WW1YV74E7UOVJCO84EvkHHAK4PGwciH8y6wDeIcJVV0MOjYDwA646DwAveXVO6s9_ZQDYvrbJSkLyM-hhXxt7O-DRSunfVuEu2CY48auz1js-3HEljPofKbLUnwk5sgz43ClzIhREKAn7qqdTv2QQpcGvYKWPgcXUbU-7h0l4GkqXYOhDuJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=J0z7sLuSHzZ23TFekn92ykk3ENt6J-X9e1SvMyYoSL-HXpW-U-bf9mLNyg1Decxfz9ZCE11wRaIBT6UwOKzXUFYOo-DiSWWda0Y-C0eun8tUor9XdsXuseZhvzFL7tI8hdQHsktNrBarQtI7Pt_KJVDtzWLsuU2ku7xE5-AZD5eP_MoT06t1XGJXuViJ6f6bxCH5KO9i2uqAUDWTpDohRzb9A9ogW5OetxYpWA4rkX6ZjOE5n6feHVy2G1ygP6UFN_ezYSlrl2B-sisGynewIOe0pt497B7l2qBAdKY1X6r49fMpX0ywYd9rpyUsWzX8KpDrNy9N7lE-ZXl_ihQRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=J0z7sLuSHzZ23TFekn92ykk3ENt6J-X9e1SvMyYoSL-HXpW-U-bf9mLNyg1Decxfz9ZCE11wRaIBT6UwOKzXUFYOo-DiSWWda0Y-C0eun8tUor9XdsXuseZhvzFL7tI8hdQHsktNrBarQtI7Pt_KJVDtzWLsuU2ku7xE5-AZD5eP_MoT06t1XGJXuViJ6f6bxCH5KO9i2uqAUDWTpDohRzb9A9ogW5OetxYpWA4rkX6ZjOE5n6feHVy2G1ygP6UFN_ezYSlrl2B-sisGynewIOe0pt497B7l2qBAdKY1X6r49fMpX0ywYd9rpyUsWzX8KpDrNy9N7lE-ZXl_ihQRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWJO4DRi4-GC-kqKNQY0Coo-BTxvIO901woFHd6ADdpWA9TjDlkedNCcZRoC0LQ6nTfk6KY6SxsWmffSNtGM67kdpwd0EROUM0KdmViSQ6q_thkXYYY_mzjy9HSV9xH-qLj63bb5lQsbcUe0t5UVtGHg6wIhzOu4ejcxldz3upOZX3IMtVvKRElbPeen4plhQM3xyIpTGEP8N6VjW8_7eURWDgXtoHzAQ4raFNQpgl41RAIzwS1Zrax49-O1FO1s3dxurE0ZRykhRziJnt-huq081FYvkvb8T-6AQjY48f_vK5pSYOePj4C0Pvq_AsBruOe2o_5ZRuxeusLZ70lIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_dyHqVFbzlAhCW9qC6bLeHjS_1dIPa4DH_BaaTYBGsqNKrcBWipWFWz7lDHK1uREA84ElSyN4EHmQ9scU9s4C5iaJs_Zu0G02Ja_moEAwEeRFJ--ePMO7NPAhniL1RE2Z-vLznvERf6r8HGEFnqWNx5x34zD4bd8hG6MEm4u-lyVzXxvi3ZzCHL8qsajtVIGVmL9hg1VNFHxCTENVPmSAgIgTVFV7BJP8lBbdP6kFl6wMBkWXv7z56rP7Oft8_38ShP2hNJXiPYgRrOONwS7XocW8Vj8BfG_KqojCRofNYwMVVLlN--A7lVKpWB8zpj6DmNsv-ou9IPAvH1toKIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz4SiBeuFip66tG-OMYnXwo44le9Vwu22SxgprTP-et7LAUIGMR9kIir3J25MvRZyqJdfzzN5Qi0psPkRoniGE1RBBguqrAqaq_WBMRktVOGbNUcW_az-BaYfN2mu7eTthunjhdzRQyn9EfzGIaRmoV_uyFBXADFgaOFFS5jkEkG6iJ-B3gycrow3mvvR3uO0juIZwNyQqn4i6TQtw5wfnks_22t3wzcyY66OgZ7nkbFWerkLGaJ2tAyza7Ucfwgr3wp8HZfO69PlCXpTe2UESYNuoWRXRhEhe-5GkvkiMCtmk3GedwkjrnAlCXlLxjDQG4c1FTcafoHsjJS7aLAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=uDuk4HziZ4Tz6cdkJJITPLRSZR0_y-0Xlhi7JuRICD7xoKvxKMKIuJkbZCkyLBmN6agttQfaV2LdHm6-A8gH_bw1hzKyFGs6qewheKs6ZivwXF2Wkijc-Nn67TweErcsBSw-juhqcPcIOYKItIQhwfqxdL80ufT_HuT8qfghxzoPzop67gZU-JJIvxZzasmrjHqxn26HdlPtCqjz40DMNOtiBwEbf5Ajjri0v7jlkJthA_YixAd8MjnuQkFcG83yb7-yxR52UkNxCZcfKGxRl4EM_05L8o9QSNY_-3ZSNqv9hdHCamuNpjDzLMn0tfsb8GpSEWRDgoYcXqiA6y8olw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=uDuk4HziZ4Tz6cdkJJITPLRSZR0_y-0Xlhi7JuRICD7xoKvxKMKIuJkbZCkyLBmN6agttQfaV2LdHm6-A8gH_bw1hzKyFGs6qewheKs6ZivwXF2Wkijc-Nn67TweErcsBSw-juhqcPcIOYKItIQhwfqxdL80ufT_HuT8qfghxzoPzop67gZU-JJIvxZzasmrjHqxn26HdlPtCqjz40DMNOtiBwEbf5Ajjri0v7jlkJthA_YixAd8MjnuQkFcG83yb7-yxR52UkNxCZcfKGxRl4EM_05L8o9QSNY_-3ZSNqv9hdHCamuNpjDzLMn0tfsb8GpSEWRDgoYcXqiA6y8olw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oLuazcMUsmaLdQ1rQ_MF56NbBdAVM8_f31kAU24qs7AD-bsCtrMlwzfOqfU2eJ0ZYzMPNzrJAlcVInBFMMws1QvOFJaR1cT_VaoOGF5Sw2ZTz8bWHY2qvSUJQMReJ_W4MxW4Uqx6GpHv2JKGtLkwoSE9OGktXgqHFPXKHhVwkR7B5H4c7Q5mOgzwPOpMHvrpQ5_9mYgjl86fsOh_21FUpGuhpvmmtXIDsMSidJz3-6z6xLdFmzMRZWuwrC-P6TG336NGAjzkdRTaUI11dJK_sjCmQrr_1LE4Z29m0WZAjCg1xhYb3Zf6RKH6LgB0gu1EeSmiZerLW1IC--JN6buB5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oLuazcMUsmaLdQ1rQ_MF56NbBdAVM8_f31kAU24qs7AD-bsCtrMlwzfOqfU2eJ0ZYzMPNzrJAlcVInBFMMws1QvOFJaR1cT_VaoOGF5Sw2ZTz8bWHY2qvSUJQMReJ_W4MxW4Uqx6GpHv2JKGtLkwoSE9OGktXgqHFPXKHhVwkR7B5H4c7Q5mOgzwPOpMHvrpQ5_9mYgjl86fsOh_21FUpGuhpvmmtXIDsMSidJz3-6z6xLdFmzMRZWuwrC-P6TG336NGAjzkdRTaUI11dJK_sjCmQrr_1LE4Z29m0WZAjCg1xhYb3Zf6RKH6LgB0gu1EeSmiZerLW1IC--JN6buB5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=BNe1uKx6bCyWZ4ar9S3OjP6zKZZUBM7MpoiiYYm6LzYqIPyQq68Vaoj_DwaTyV2iPY05BwHmRcf7IcNnPVJDoXY_asKPfeawpSdjxbLo-o4I6EBCaF3GcE3rkBtldsMpmvzYKmL05JuNu-TS1i3ls-X7CIAlXLXA7HMD1blhlY7HIILFAW7rDDftbWCTAoz6FfaLt6DLxGasp7xHa3-7huoyam_C1GhszJnveZQlEo2c-pWreMQ9J_ZeSaQrXDLM0uSspY0AiphnWLOx3Z7ujUGe9ze2oZdDCkN9aZlP3vtjCQgJjiIxG_U0tuXAPvTzSD6uhOXE3ZdvAFXP1cIOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=BNe1uKx6bCyWZ4ar9S3OjP6zKZZUBM7MpoiiYYm6LzYqIPyQq68Vaoj_DwaTyV2iPY05BwHmRcf7IcNnPVJDoXY_asKPfeawpSdjxbLo-o4I6EBCaF3GcE3rkBtldsMpmvzYKmL05JuNu-TS1i3ls-X7CIAlXLXA7HMD1blhlY7HIILFAW7rDDftbWCTAoz6FfaLt6DLxGasp7xHa3-7huoyam_C1GhszJnveZQlEo2c-pWreMQ9J_ZeSaQrXDLM0uSspY0AiphnWLOx3Z7ujUGe9ze2oZdDCkN9aZlP3vtjCQgJjiIxG_U0tuXAPvTzSD6uhOXE3ZdvAFXP1cIOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=MLFApZ-L60952wCu-4eXfV-V6OCoq3pqSAQ75ZHT07KL-GUhxfSldcMzPO1HFJ39ybZ3yBRTJ6wqfPexTZ90aHXyjRFN8pJhghYAhhUdcxmcAYLfTIJovGwpsUD4mjOvq81oFFhEmyjRHTmDeEBpUW-nX4yz65F4wuCBZKukZwz7_M1WvhVScOHTi26VhFQJixyLDFmtemt478XrZq5wTMYcY6DwlCb72XMtEyaP0WOdySzos9JMRdXF64OVS2LHZ2WUTsMjDZ16GKcW9fdwT-8Mh14lQt3QrugF4QoMpN8GyH2DI0NymY6SejSD-btpoB1xz9R7HkPZIk-2ZHjG8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=MLFApZ-L60952wCu-4eXfV-V6OCoq3pqSAQ75ZHT07KL-GUhxfSldcMzPO1HFJ39ybZ3yBRTJ6wqfPexTZ90aHXyjRFN8pJhghYAhhUdcxmcAYLfTIJovGwpsUD4mjOvq81oFFhEmyjRHTmDeEBpUW-nX4yz65F4wuCBZKukZwz7_M1WvhVScOHTi26VhFQJixyLDFmtemt478XrZq5wTMYcY6DwlCb72XMtEyaP0WOdySzos9JMRdXF64OVS2LHZ2WUTsMjDZ16GKcW9fdwT-8Mh14lQt3QrugF4QoMpN8GyH2DI0NymY6SejSD-btpoB1xz9R7HkPZIk-2ZHjG8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=d4x8oB1GNsfqsmTRGHs-cDkcsXkgS666U4-nv4bGgo1V0We-h7dke5LFh3ZEcq1CJmdQ4eu29S1FcAy2khdeaS1vVjydNFzBT3NCD1BXVvjQ2qQt4Ncn2-qJYF28IVupAj1CwgJ-4W-zQWjPaod_HBsfbSh-CrMzbOqfF072gdKu8MZEbVLIOdg0s5vWlBJA4P_-bg-2SwM7rYlA5WDex4ohS9vzMr-w_pTgHBw2W1juZCDY3dO7XnuQrLEErknYeedYUM7EOf_AMFiA5H6nrHjUO3pRnOF1BDMUd42kDdE-45mw3o06sFfnXMNba1aKxp4zjpSSqKzhKR9YdrpMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=d4x8oB1GNsfqsmTRGHs-cDkcsXkgS666U4-nv4bGgo1V0We-h7dke5LFh3ZEcq1CJmdQ4eu29S1FcAy2khdeaS1vVjydNFzBT3NCD1BXVvjQ2qQt4Ncn2-qJYF28IVupAj1CwgJ-4W-zQWjPaod_HBsfbSh-CrMzbOqfF072gdKu8MZEbVLIOdg0s5vWlBJA4P_-bg-2SwM7rYlA5WDex4ohS9vzMr-w_pTgHBw2W1juZCDY3dO7XnuQrLEErknYeedYUM7EOf_AMFiA5H6nrHjUO3pRnOF1BDMUd42kDdE-45mw3o06sFfnXMNba1aKxp4zjpSSqKzhKR9YdrpMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruV1XNtft5MxRVys6gWCf-_-mDJYagp3XCRk-qCyl8IwUGa1rLdSCVWY1zUTxuC8zrnL_77kk1OJDCZa0k_Kl20cAYDsPDOGHfvEH34Jr4weQUSbp651L_P9vPct3IEJQsclDeoIvGDJE4FwNwJA9P7PT3cR-TuUsn7w6_4fFrtVCXsrB8ywJTA-MiawdYa7sGFQtzWVDNb45nmSdyvfe06Xw02fvnT3Lktrq4FohXLLKo83wfagiuwOqBIcXzqwNoM-VJgCr11DICmJmfdtMBMttxhApVwcEEFgjWu9T_IswMIgs9H1xyWEt-hl9YezJHUfgfAn6nstJzDYMFIbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=UF0Ks1yl7qf4eAs__FRpSs85WvLn79oU61w8Gn39chXugy2h1a87DbgTtaOHTL_2VDtObxEPH21Sc_2fL4pI4pyT2I7xMdN1QNzEQ4FKApNIPMqz3GDo0N9UvfD6GW_cKpqQLSe1c8cIG1zwPMRr_w-YXeQDQkgUUWy_8s996o06X2cZXX5xrYV6jdom_vqkrWjG9eQdgpGjvTk5189zUpKHTK5_VDy0rXpSXpQDnYZ3G-gQWlv4chLoi30oBzoOzYPmWWP64SKp6UJbtutgkQHjTpj4b6eGpNOl2GNOqrT2dnpqQA-rXqFh2PrNLq00T0QBvxTSuC5sdgVUD0AhVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=UF0Ks1yl7qf4eAs__FRpSs85WvLn79oU61w8Gn39chXugy2h1a87DbgTtaOHTL_2VDtObxEPH21Sc_2fL4pI4pyT2I7xMdN1QNzEQ4FKApNIPMqz3GDo0N9UvfD6GW_cKpqQLSe1c8cIG1zwPMRr_w-YXeQDQkgUUWy_8s996o06X2cZXX5xrYV6jdom_vqkrWjG9eQdgpGjvTk5189zUpKHTK5_VDy0rXpSXpQDnYZ3G-gQWlv4chLoi30oBzoOzYPmWWP64SKp6UJbtutgkQHjTpj4b6eGpNOl2GNOqrT2dnpqQA-rXqFh2PrNLq00T0QBvxTSuC5sdgVUD0AhVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=JolGq-8ytr0C6mPmrV4KRi76ydNyRHbrf3Dy_CZLfTJQFO0b39t4IMqqFMz9frFEdLKTUh25vBnc18pjTsGltnVLG71ftaM8O_h-vKZhnL4XPj9pd0f6S2r8m-WOSgfPVNRr1HPazVjNrX1ySJindUSlc8OSI-6ZGc6cJGA5y0EFN5U2W8wdzacnP3ehnZzRRYM_toBcdhHAutaHl8ETMquF7RO3FnIkrYcgokjjx53cLeQt_8d4f0jB_CUKPb66KT2n4ILJmY7-Y8POJOstNxKN71YgVBTDZoPsKpltmP569OKEVQSLTMuQMhcoKTYnmPv8QCz_PNaI4aNyGkGGdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=JolGq-8ytr0C6mPmrV4KRi76ydNyRHbrf3Dy_CZLfTJQFO0b39t4IMqqFMz9frFEdLKTUh25vBnc18pjTsGltnVLG71ftaM8O_h-vKZhnL4XPj9pd0f6S2r8m-WOSgfPVNRr1HPazVjNrX1ySJindUSlc8OSI-6ZGc6cJGA5y0EFN5U2W8wdzacnP3ehnZzRRYM_toBcdhHAutaHl8ETMquF7RO3FnIkrYcgokjjx53cLeQt_8d4f0jB_CUKPb66KT2n4ILJmY7-Y8POJOstNxKN71YgVBTDZoPsKpltmP569OKEVQSLTMuQMhcoKTYnmPv8QCz_PNaI4aNyGkGGdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=IpNdKsbFCVakW5lkUGrk-35kE3EgbM72fSK1FrY7-zh8iPHCMrjaJBO89bVRPe-ub7bGL5erjS12AYsGvRLE2z8lyPEwLZvMe6cxai8l4JkFvUen1hRVN63HWvA2a2JXCHVjBSZp-BZYlrshDyG3VoZv2Mk6yc-0EOtAktA9qxF7QN_s_b-VT8wq61mlRlUazdC8tbt9-lHgTakyHH2I7n4NTU9WlNrihXhRRplZldixryv2rhY-ySoIdqnA2DeUYHXLiCSuxkp1b-5E1aH-Iuo9iCpVLeHQw_wPP_ofKMkOosLFQq0zTPkkdWgLEo_1H2emdFsb-o4_OmiFgBNUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=IpNdKsbFCVakW5lkUGrk-35kE3EgbM72fSK1FrY7-zh8iPHCMrjaJBO89bVRPe-ub7bGL5erjS12AYsGvRLE2z8lyPEwLZvMe6cxai8l4JkFvUen1hRVN63HWvA2a2JXCHVjBSZp-BZYlrshDyG3VoZv2Mk6yc-0EOtAktA9qxF7QN_s_b-VT8wq61mlRlUazdC8tbt9-lHgTakyHH2I7n4NTU9WlNrihXhRRplZldixryv2rhY-ySoIdqnA2DeUYHXLiCSuxkp1b-5E1aH-Iuo9iCpVLeHQw_wPP_ofKMkOosLFQq0zTPkkdWgLEo_1H2emdFsb-o4_OmiFgBNUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=g9XEITkPaQoOXBbVSV2C6cjg52g5WnTImL2lw0RbuqhQESzRldLcl2dt03BeiVAAoVqaO8aFYv_vnAIwy0JTj2WGQ8UTGVsFAKegzVy4WE1KPVeHNM0YYDFwjPLc7BT8_Dc2EzzdDuJjsoA2t93bmOkE3YmH3M6amJNSsUPA1hfUIzOqc73asmuyMRvsfTMR0NGbjvaIobSztM5BHPvUa1bQ9WSxbE53a9G1jPe4YNa6ZmMhzK3WP8PBywkPOdTZo3UyUz8ZNiW8dop7P1nnhDnQh38xuAN1ttxTxGrSktIBNkd2oBQAhrjQz90C2NW2_IVm-uSczjMf1zM2udzMqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=g9XEITkPaQoOXBbVSV2C6cjg52g5WnTImL2lw0RbuqhQESzRldLcl2dt03BeiVAAoVqaO8aFYv_vnAIwy0JTj2WGQ8UTGVsFAKegzVy4WE1KPVeHNM0YYDFwjPLc7BT8_Dc2EzzdDuJjsoA2t93bmOkE3YmH3M6amJNSsUPA1hfUIzOqc73asmuyMRvsfTMR0NGbjvaIobSztM5BHPvUa1bQ9WSxbE53a9G1jPe4YNa6ZmMhzK3WP8PBywkPOdTZo3UyUz8ZNiW8dop7P1nnhDnQh38xuAN1ttxTxGrSktIBNkd2oBQAhrjQz90C2NW2_IVm-uSczjMf1zM2udzMqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L48-Po4pf4hBhAMP1L4yys7LfB6uxvyCd1jF5GqRB6773T6ZwCQVVkyfwV4l73cunIJbT943CT8hkgSUvNHqGdxua3MnrLgFYcpsp-5yGb76UQR-WJ3u4mZOUcLXo43oI3wVVLPbiDeRVYIC3tPB4W2b7JBqvtw7w0s3DwheCVrtvikRdT4IR6UdhReGHY12n8sU8TFfOTFTw8ulWdbLQ_G9QGeDKNPoopCzY0-8TPEV8yOeAKzRWJJrZRUaNye9_3zttApkF-FGs0LYcgTH7PLZ4uR4VPMG6bM9WExJDg1od3bUToe3Ss7eK1NNcyDjFVONYKw-g6UPar1b6b3NYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIbuiSC-wOEqKgMfniEcqCbvPARZfGG29FcGlsDmxY7i0oDl4rF7-UcFE23LIX5tRIUcoK5U943G8cbQ_2jESg_u_lPPCfdYKgADD7XQ155t5LvRVF1ykZAm_sz7A6qGrAg0tYz_2h8w0NyzAq1fOrXsvkB08S4XgraFA3RheyAhEJX1r8jvtWwFdr1bdbUv787fIjzgrMaDWSNUTuVYi9ThHTDeHdfChj8hE3AUqQzmP5WsdKMVlZsmCVtTflbFZcG_EQ5e-BuVaf5NHPZsYj0hjOuqw1ju9jHKFo-A8qujoPJg4tVMuOf5E4lr4VBxrmcuJnFQlFoO59RhhGtzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tztbVaiHDYU_DO9qDmTmwviDuFrVnDhkHPiDhVYaiuP5U4F3U77OaP8fkxZvz7SHQI_QBDLttiQ9HXi59ot3k1SNS_LrUfsBevCANGp-0WjzhMX4MdawqD--0e95Ikryze7_sGHxasS4eHCl9OZM1S2-QV3i0axzO2bqRNqXOu1Ak-GUEXc_hn8iTOf7CE8E078gLMW9AsIirwXxqIHPte7159wOsP64vuc1mLm1iP0OAHOAIYUW0mFmlRq58Tucpulw_gQ8MSfN4tySu76MBTi5o-JWCsWBG0TUigoYxqzA70dkWqpj6vKhuFYFu_OcdnrarQKaiXnDpXroYDiuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFRVAkgdD31FYiThgnD3alvymhni0sGILNQ2tAJSXytGGW_-UmxdiJ0vIiXT7l1WmgdG8rypz5785oupiGrri2-n000kobK1d7tOOSa8tgemxKmfgvkUzeI65LR1bDISQRYczTdM-1C-sYm3LK1A9DexdePHk9MbO2G0amOyeXufVFdp28g5LgkFYYTJdqqh5ZQLOHblL2ljKWoyr3b_kgBSAJC8L-hYjFlXSbYnTynpprBDqL4DK-GlvRcye42V2dUIc3vNHurOiQ2GHhQtDZZDht-YQ09PpEAOknRevgp37UV8z54rPeQiDORGzjs8XVr4oV2_dEphP_8OVNoIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=m74oMBGtcYlaMgJP9hUKLjNnG4wLW5IuvtkQf6UmM78VxwASukLoQFlez1aUUhA_Hi45uXKfq6tqUq7eMptk-Jqd6k1DqUmytfLZg0s_Ab1wXy3gu16JDJFRayoDHoMvsSP_XIB-AjtxEVDBquqqRwkupYPeYAR_V90_u2bMI7lMpStgcNM-8el4DcMWKNIw3EHXepc9R5quSgvrAMMRrsArmdbGr4t5h27IcbKIIqMOF3ZLNMjShjqmWfUtGv1XOW2qjug-va97y_k7avvsFQ3-z63PHcnnfotBjuJ3NTDmaxshBLCfk65oSFmfoLQPZuVKZGX62-e2knqHtBJx26Hop4imHpRYls4aJwD8gN8okZnLeoDgUuLTzuPhV6fcFGxrwNGNSkXJmUyGWzVnTvSaR7qklxWtPbDZeZDR0AJYolU4fUw1L2M4TNKaLPsUikoN5PI7422IdiuF20Zl0ArkY-cVfz-4flGVOcgGNoVoEP3WlTCual0bBA2RBqT5cZRlQZ9VZ3ckH7iXc8bOxkU5Q1I5mKGsWD-qxHTXDTiYexoZyy_Nyr0EV9fw7kjXaY8csUVoq_zAIhdi2Xp3J2E2fHun2g63zGkJ7EoZO3vIkC6IvWrG8StIL64gIJ9A4_kbLt79PzuvKUECOje0hbr4cA3aAYx0Ms4AIn8ICmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=m74oMBGtcYlaMgJP9hUKLjNnG4wLW5IuvtkQf6UmM78VxwASukLoQFlez1aUUhA_Hi45uXKfq6tqUq7eMptk-Jqd6k1DqUmytfLZg0s_Ab1wXy3gu16JDJFRayoDHoMvsSP_XIB-AjtxEVDBquqqRwkupYPeYAR_V90_u2bMI7lMpStgcNM-8el4DcMWKNIw3EHXepc9R5quSgvrAMMRrsArmdbGr4t5h27IcbKIIqMOF3ZLNMjShjqmWfUtGv1XOW2qjug-va97y_k7avvsFQ3-z63PHcnnfotBjuJ3NTDmaxshBLCfk65oSFmfoLQPZuVKZGX62-e2knqHtBJx26Hop4imHpRYls4aJwD8gN8okZnLeoDgUuLTzuPhV6fcFGxrwNGNSkXJmUyGWzVnTvSaR7qklxWtPbDZeZDR0AJYolU4fUw1L2M4TNKaLPsUikoN5PI7422IdiuF20Zl0ArkY-cVfz-4flGVOcgGNoVoEP3WlTCual0bBA2RBqT5cZRlQZ9VZ3ckH7iXc8bOxkU5Q1I5mKGsWD-qxHTXDTiYexoZyy_Nyr0EV9fw7kjXaY8csUVoq_zAIhdi2Xp3J2E2fHun2g63zGkJ7EoZO3vIkC6IvWrG8StIL64gIJ9A4_kbLt79PzuvKUECOje0hbr4cA3aAYx0Ms4AIn8ICmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=blJtAvC_XRtTEvPEETcuVrQLN42LdRPhqveBU8arXnxQ7pyQXWv_cQC6GynemOaplyNhLjKtt3KnwuoSQLwBpZA1hs1XDpJlEBl44OiI9O0S1C4fP_yyASx1sj-9B9nyPC2idkuqa_QCBP3JlM6OshFXM_ebq43va1v5Z_jXeEHVUxf5goc1hGiUtknMPtCIHOTS5j4D1OKZE7BkCeqdVrX6FefHyJukl0A1zu1AbBSHO7xbYbCb1z3oV7uwp2gHIpOiA1nRtffeJTOFb3cMFd8kzysGhTrC0h2E3MfjzO8EcSc67wbqml-rdUbi2AsvlGwL8AFDWN6CdL1qTAw8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=blJtAvC_XRtTEvPEETcuVrQLN42LdRPhqveBU8arXnxQ7pyQXWv_cQC6GynemOaplyNhLjKtt3KnwuoSQLwBpZA1hs1XDpJlEBl44OiI9O0S1C4fP_yyASx1sj-9B9nyPC2idkuqa_QCBP3JlM6OshFXM_ebq43va1v5Z_jXeEHVUxf5goc1hGiUtknMPtCIHOTS5j4D1OKZE7BkCeqdVrX6FefHyJukl0A1zu1AbBSHO7xbYbCb1z3oV7uwp2gHIpOiA1nRtffeJTOFb3cMFd8kzysGhTrC0h2E3MfjzO8EcSc67wbqml-rdUbi2AsvlGwL8AFDWN6CdL1qTAw8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YobqDl3wKZ85Yt5v2DndDjK0gIJPf6KobH2EPx0FTNMbdKlnUEUWxaLjwVKjh3m7AUG6tIRvERm-6C_z5C5qFU42jUgNubAyDbjRxX8LThZYUB6IuSJ6BqtAksrg7FLgqBQIviEacadEGyT3N1i1Vi195Bckp0qLOUz-o4oeasOpBlpn1RoVa2Ujc4wY9EErU90zsQPDvEHK3zI6a_hBUAySOoQAdiONu49hYlXDdsFnRVWEB_qZVj3VPys3dkWk53m7m6KqMCXRkN5ZNXXR8KcKBt9tiRxzbw_Wyc0pA7X8JGm-clXANskU-VJyGRZ-7Qll0whWdt73tFNPTYx7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=h90afPXSU7KFhIvUuVYVT8e_w_5RtrgkABEW8BkyXoMb5hOG3G9v-4-6gO7FhbPklGWVHmOFheaezu1roYR9PBXu9aPXcx36oGuXHkpobLwuX7vlzbiW7u7AiH2sBBz4JDXfmRh7UBUr_ekwTp4tJyETopGb0P1XzlPNxcpOe7b4bqOGd3JQaNg2Fi3Cl7gR937yz8KNrjt_c43a6cBfHaqZtwE6O42b46F7XGvJFfBvpt220Dg-rDwrz-HAX4Ca6GKyGi9NwRbk0deXZ2D_jLxQtxOtLEMKhRjU5vU7aHLa9TTXUCc15125s1PsYqDbX_TyhHKL3DOPxLPr_MTqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=h90afPXSU7KFhIvUuVYVT8e_w_5RtrgkABEW8BkyXoMb5hOG3G9v-4-6gO7FhbPklGWVHmOFheaezu1roYR9PBXu9aPXcx36oGuXHkpobLwuX7vlzbiW7u7AiH2sBBz4JDXfmRh7UBUr_ekwTp4tJyETopGb0P1XzlPNxcpOe7b4bqOGd3JQaNg2Fi3Cl7gR937yz8KNrjt_c43a6cBfHaqZtwE6O42b46F7XGvJFfBvpt220Dg-rDwrz-HAX4Ca6GKyGi9NwRbk0deXZ2D_jLxQtxOtLEMKhRjU5vU7aHLa9TTXUCc15125s1PsYqDbX_TyhHKL3DOPxLPr_MTqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=CCxJKtYm0YaTFpuEQqcVr2s1Ws0w7FFGOcUVNHaKGTZ75Le4F4WDuEy8XEMtJ7FgCfDD9rPKXJsmeV1bbRgYkA2aki8B8HPcCWJXDBj9zH4QmZQfjs88Tb79o7-g-cPNwk7LJBPMuL0wkjrhuYCi8EqAQWmJp2_ITZDftipuBx_SPe9WDzPmPYtITtc1oJ27QAchGfyw4jodUrkWuwgzgpalM_z39gqMIgqNPvrFqJB5rDpJb4TrAioHRhciIFNKHbOX93l6-JJHB6rB7ctUErtmOmcAanKWmVEoq0gu3EzULQgm7LEdzWhWqJ3UIUYdIeNLWEPNko1ka_37MOUZ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=CCxJKtYm0YaTFpuEQqcVr2s1Ws0w7FFGOcUVNHaKGTZ75Le4F4WDuEy8XEMtJ7FgCfDD9rPKXJsmeV1bbRgYkA2aki8B8HPcCWJXDBj9zH4QmZQfjs88Tb79o7-g-cPNwk7LJBPMuL0wkjrhuYCi8EqAQWmJp2_ITZDftipuBx_SPe9WDzPmPYtITtc1oJ27QAchGfyw4jodUrkWuwgzgpalM_z39gqMIgqNPvrFqJB5rDpJb4TrAioHRhciIFNKHbOX93l6-JJHB6rB7ctUErtmOmcAanKWmVEoq0gu3EzULQgm7LEdzWhWqJ3UIUYdIeNLWEPNko1ka_37MOUZ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=MXahXVBqsvRITsXHz-1OmxjPT6BecoDK9aPjI9hXi5fnyjXJgRqz9KwNORCQLqruojK2-bO8IorBgKukEzwS9UTljg4cpsX0_k0TdU-GnLZ9Tba9KpuDt0Ey2q0bV66xEkJm6QwEpPVYXYn2aSr9mkyAxcYQwC6sRrt31fXnUYpcpzfZA4yrGVzmuK2ey_S_oI-WQHBZlL9gEqMg9dDRPiPko_ZwKrGVOG0pLlzitEe8HhHs__-5wnRO9u3ojN9DedcIv0hjHiQinYgL3qfWs5c1j6KpLKUsLy8gvRA0SX24BVvGIdy_FkGZ73FNCrkE3BdBTxtMOreBnQNqUoSsgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=MXahXVBqsvRITsXHz-1OmxjPT6BecoDK9aPjI9hXi5fnyjXJgRqz9KwNORCQLqruojK2-bO8IorBgKukEzwS9UTljg4cpsX0_k0TdU-GnLZ9Tba9KpuDt0Ey2q0bV66xEkJm6QwEpPVYXYn2aSr9mkyAxcYQwC6sRrt31fXnUYpcpzfZA4yrGVzmuK2ey_S_oI-WQHBZlL9gEqMg9dDRPiPko_ZwKrGVOG0pLlzitEe8HhHs__-5wnRO9u3ojN9DedcIv0hjHiQinYgL3qfWs5c1j6KpLKUsLy8gvRA0SX24BVvGIdy_FkGZ73FNCrkE3BdBTxtMOreBnQNqUoSsgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=glZCWxsBg04CjoutBFAUhnB4rafQs3TFKbSEoVIxspdKwbuTLLHNGd3Q0GuFSGqzVFb7p7OcStIF-sg8EIZHnTl4T0wOTwz69yUWsoOPh0R_d8E9k2-F8ARYJyrQG3bJ6jvwCK6LsB_WrGRucxKWCnUqtBKdKd3MuWHc7JT0mk4WY2UeMSy93g0ky4GSe-jaFADhCFwnP0BlTtwzlf4I8KuxKWbFyhDiS92wjZNynhds5n1jHm-L7FjKL6lum8k6E7Dg7tD90fUsbuSQTYkyODhbxz9lsDR5e8GN2m5PEiAl6zBJJcdkyhdudJSSbHYuaVucjIWUEMr3Demsy5XX1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=glZCWxsBg04CjoutBFAUhnB4rafQs3TFKbSEoVIxspdKwbuTLLHNGd3Q0GuFSGqzVFb7p7OcStIF-sg8EIZHnTl4T0wOTwz69yUWsoOPh0R_d8E9k2-F8ARYJyrQG3bJ6jvwCK6LsB_WrGRucxKWCnUqtBKdKd3MuWHc7JT0mk4WY2UeMSy93g0ky4GSe-jaFADhCFwnP0BlTtwzlf4I8KuxKWbFyhDiS92wjZNynhds5n1jHm-L7FjKL6lum8k6E7Dg7tD90fUsbuSQTYkyODhbxz9lsDR5e8GN2m5PEiAl6zBJJcdkyhdudJSSbHYuaVucjIWUEMr3Demsy5XX1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=TmFepIH9bc83sFKBTe19z3XIHbb-niPulmzonATGeNxQ_RBhPEOAEPRvyf_4D9NYbl5aNNx0uxr2T61pT3EcxzqEJBZpgr439BCWw10mteDGcrpvuKjYeMr-7hlP4vN0JX3skyWFBVswuujvK9DtL7kxrluiYbf5beFTcjVcq6yWmxKrzNrnYpWaEa48IuGDZo55S-6D_83_ISk0s-ajENMUyf9vklf5E4YIoNl3xmak_bthvC8qjz0CSK7xcfXJiLuYgIlgUYWpxSOxWUMJ1jXcAwC-MBAjpAE3JWoRdbDqi2HqdFitTtDcnVCfNClx9iX1nKRWRHoEwh8jCGTlOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=TmFepIH9bc83sFKBTe19z3XIHbb-niPulmzonATGeNxQ_RBhPEOAEPRvyf_4D9NYbl5aNNx0uxr2T61pT3EcxzqEJBZpgr439BCWw10mteDGcrpvuKjYeMr-7hlP4vN0JX3skyWFBVswuujvK9DtL7kxrluiYbf5beFTcjVcq6yWmxKrzNrnYpWaEa48IuGDZo55S-6D_83_ISk0s-ajENMUyf9vklf5E4YIoNl3xmak_bthvC8qjz0CSK7xcfXJiLuYgIlgUYWpxSOxWUMJ1jXcAwC-MBAjpAE3JWoRdbDqi2HqdFitTtDcnVCfNClx9iX1nKRWRHoEwh8jCGTlOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=cxMMKzVDxq9UmXBxjzCG-mOtTQ6OkqphFrAQJrLVjFw7DemJ7OgCuQ-WYLzNt2vAq4Zs0P9drQ2x74UCg9O6TaO1G-6hbHcisL4uqoTLmYjV_8bkxnJqlCm8JEz-kWtqc7JvDnHJgclqxBdmKK6G-yCW23dBXPiXuH7QhSaLP4_if0-B3NndgO1pq_Y7qvDIsyPtRJVOVzJ9JNjYNJkMakCyEcbSMoTXWXKf8f-rWUD-pwR7uKY0i0u2FEC67I6iC6x0GP0lmfy6UCiPjGdZiNFOoIsh7ehuQPv5ZlpWAmQx34wpqVDmE4r8LmdKXn2Mko-bo8R62jP0maSBExzgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=cxMMKzVDxq9UmXBxjzCG-mOtTQ6OkqphFrAQJrLVjFw7DemJ7OgCuQ-WYLzNt2vAq4Zs0P9drQ2x74UCg9O6TaO1G-6hbHcisL4uqoTLmYjV_8bkxnJqlCm8JEz-kWtqc7JvDnHJgclqxBdmKK6G-yCW23dBXPiXuH7QhSaLP4_if0-B3NndgO1pq_Y7qvDIsyPtRJVOVzJ9JNjYNJkMakCyEcbSMoTXWXKf8f-rWUD-pwR7uKY0i0u2FEC67I6iC6x0GP0lmfy6UCiPjGdZiNFOoIsh7ehuQPv5ZlpWAmQx34wpqVDmE4r8LmdKXn2Mko-bo8R62jP0maSBExzgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=iq2ol1Efas3d5JgzvrHy3CRQLYIjonqHR_J9sO-RMkztUaCXusekZjzUajsi4Ou_cvhdsFK9rgfq_twxL-hIOkvOf4YJTMif70OTunSAUtKnmOxB5aohT6id1TQ6CB8kwOjqYtRvamT7aq0iSWjT7IDaitDQRZOxzozSz4C1-LY_G450VjzPNc2xhf0O6mQjVkjr14MDA0yWlgrmJJ3oGfx1bQ-13qUSxAXiqNQ7Xvr3Czpi8kSDqPfvKljBkqGXzXSNW_c4vvGH1h5gkxxdKJPag9V7qZXDcptrSRD7NbLnVS9tgAwPNdqeJ_8bFnzrgfHUVfw-9u26pGs_laMmOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=iq2ol1Efas3d5JgzvrHy3CRQLYIjonqHR_J9sO-RMkztUaCXusekZjzUajsi4Ou_cvhdsFK9rgfq_twxL-hIOkvOf4YJTMif70OTunSAUtKnmOxB5aohT6id1TQ6CB8kwOjqYtRvamT7aq0iSWjT7IDaitDQRZOxzozSz4C1-LY_G450VjzPNc2xhf0O6mQjVkjr14MDA0yWlgrmJJ3oGfx1bQ-13qUSxAXiqNQ7Xvr3Czpi8kSDqPfvKljBkqGXzXSNW_c4vvGH1h5gkxxdKJPag9V7qZXDcptrSRD7NbLnVS9tgAwPNdqeJ_8bFnzrgfHUVfw-9u26pGs_laMmOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=p0grGGmrrEYKWPDRnL7TzBkCYd6-7N25XYa0dJVHmw2F7N3hGsbfGbfjVQGl2aPI9PeSe2uHMEmpL9ix5PgJBC6ZDqxHy5MLJi1I5NG48feAY_Msw1m14mTpc7gDNPOSkDdx-iBqEH0WUu220XVsnOqLl3RCEhfXNu0CirQ0cFcNson3unwnczODlbYUr9LtLpAdcKA1Uwt7vIX_vJVMQWktiSxdBV8SUf9WRGao4d8x52mDLFIL92fls4yg9ItVwE4BfYbtx0L7o7MsMTm55Y0EyHVh9U916D419AJQGupjmwRefQxvanfoRxbJ65HWvg0snRX-pczoRp4ZG2oGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=p0grGGmrrEYKWPDRnL7TzBkCYd6-7N25XYa0dJVHmw2F7N3hGsbfGbfjVQGl2aPI9PeSe2uHMEmpL9ix5PgJBC6ZDqxHy5MLJi1I5NG48feAY_Msw1m14mTpc7gDNPOSkDdx-iBqEH0WUu220XVsnOqLl3RCEhfXNu0CirQ0cFcNson3unwnczODlbYUr9LtLpAdcKA1Uwt7vIX_vJVMQWktiSxdBV8SUf9WRGao4d8x52mDLFIL92fls4yg9ItVwE4BfYbtx0L7o7MsMTm55Y0EyHVh9U916D419AJQGupjmwRefQxvanfoRxbJ65HWvg0snRX-pczoRp4ZG2oGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=md_Jc6WNX7NnH6dhfGfL9CfrbkkfN0cbqHKeBLGpUYHziY9tRFkkifNdLo50AeeK0cDjgyswVNR_zd8mGQZwFA3HfcwjVDwtsmYHAYjVpj9qEMIr_jJt42sqiA364uwusNxNkNYg5uNCZam-4gCBi8olnJwub8SY8igdHrpHXXZNUxoqiJOjA2pugrYix90GrXV3xfBi-7izRTYGUgPyKWQrKEGAa_WeP_YZAu02po6IWgqHLmDtAud_KKVB8cqqEbrBswA40kL4ej6-ZC2p4IHcSwLL0pQoXg-xrOijR56Hawdbjcmm4ge_H9qgbrnIsQoQjpaZOfF687xWqOWwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=md_Jc6WNX7NnH6dhfGfL9CfrbkkfN0cbqHKeBLGpUYHziY9tRFkkifNdLo50AeeK0cDjgyswVNR_zd8mGQZwFA3HfcwjVDwtsmYHAYjVpj9qEMIr_jJt42sqiA364uwusNxNkNYg5uNCZam-4gCBi8olnJwub8SY8igdHrpHXXZNUxoqiJOjA2pugrYix90GrXV3xfBi-7izRTYGUgPyKWQrKEGAa_WeP_YZAu02po6IWgqHLmDtAud_KKVB8cqqEbrBswA40kL4ej6-ZC2p4IHcSwLL0pQoXg-xrOijR56Hawdbjcmm4ge_H9qgbrnIsQoQjpaZOfF687xWqOWwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2yUCUYNqbVVYzztx0cLZXtpHzCHkW-1UkANewCtNmSWGMHsI1nH5L8MbwaXX4b9vVFBP7kJN2CZut-ErohaivIZK0EHauvOBUbtx0enGXBgDpDl3JnBe-5U22ulcYqBAGZuwBTYqxuRVpfRSKtSWQUagFO8ocbg2Uk9nJtushnCSpzPO2v8gvNcQFosdtLznhrFE8qyWqdaVmPRaXwJaja2c8koFRTWyd9ZX1S4qkbH0jhlM3Cd4YFt7YagAdoyOcPfjvHTTMpZjTzaoZNddPeURsjgWEQzSpMRj8GoZ_PZlK5omXRgEfS3l_6VRoWQ9tU8_6JUXp0LwuCLQy7QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=h_Ayh96N3B6vOpP5b15hRaYG63LI57vJvewsLaMTpYWZukxAC_0jV1t_8cpbW-Ws_6Kb_jjd95rGeC2Ww8ggx3ilewz1tHR8rzKMLhZm9myI9RgjlE26ogO4KUFZ1wbogCGGiEzFTbYvvtLvfBO-6C51itMk2e17t5UtoZhkZyUb_F9KYKZnAkNHTqgKcrq1pCnXMwoPuAAweOeIiBwNfk2bR7vz6tCNUdMskCMYclgWNqw-ZmHaKtJZFJ2sYAUVHowksRq6klimK2_w1dRyxPJHGC-1EgmLdS9LelhB3rQfsQYVgoXLedEsBXswmqJMcCnp_7iuq2X5v-JM3mgCAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=h_Ayh96N3B6vOpP5b15hRaYG63LI57vJvewsLaMTpYWZukxAC_0jV1t_8cpbW-Ws_6Kb_jjd95rGeC2Ww8ggx3ilewz1tHR8rzKMLhZm9myI9RgjlE26ogO4KUFZ1wbogCGGiEzFTbYvvtLvfBO-6C51itMk2e17t5UtoZhkZyUb_F9KYKZnAkNHTqgKcrq1pCnXMwoPuAAweOeIiBwNfk2bR7vz6tCNUdMskCMYclgWNqw-ZmHaKtJZFJ2sYAUVHowksRq6klimK2_w1dRyxPJHGC-1EgmLdS9LelhB3rQfsQYVgoXLedEsBXswmqJMcCnp_7iuq2X5v-JM3mgCAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnbeVnscdGVr4i784ovGOyzulfkVCjfMUKOxEyES4eUyunyjtRRjloA4xEk4xItt2YwZJjjAT9O9gWIuLUf16CO1BHw1aOpajPIVuL550gk4TaHaFaxTOJ2TCol48b5fpyhlECjLn0CffFYSmoOZqYvyfOGOn0OavO6kLfvxyBHSMwYVVosjNCBNY2g-emtFAVii8Y-c7_O75w3h6PFjwIqwakiMbMY48ssC4k_XyDPGQDwbsGxyhSDczOgQlPfOZsrnkz8MgdGxAdd9KoRvFQdAlq5H7M2IMZ7gPbVpUo1MtuETv_l-d5Jeah5HuJHsL1oRBcXyo89ejd3B8ymGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=fLC_r_ERXcvHkQatcSx4yRtgDIzyiSrndeiPyTNkl9QM8CnZYReLQSMceb7C529lfE4TfC8fT2CkwSh1P_9XBDlCcBUKcgDDxifIDkKTN4CDKh4bpfTHbEQ9YgX8-50bJfcZI_i-AgpsoIAHnriX4ZhMut2QsXUJ-VsOSB3-_9l2fNanV8dKCK1YNZpQRp89wNldrtY8vLAP4_DXLjoYNnKY6vZ1HXhr3Gn-Te_3YDPUlUlpRPrllcRkCTTctsGeMEMd1Jm6vHx0rbkVXOVRA0JFw2PMJgoH7v64F_2AD2ukf6w72ga32ydSluzmhH8YrVbn5H_CjpTrljPy3yxzCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=fLC_r_ERXcvHkQatcSx4yRtgDIzyiSrndeiPyTNkl9QM8CnZYReLQSMceb7C529lfE4TfC8fT2CkwSh1P_9XBDlCcBUKcgDDxifIDkKTN4CDKh4bpfTHbEQ9YgX8-50bJfcZI_i-AgpsoIAHnriX4ZhMut2QsXUJ-VsOSB3-_9l2fNanV8dKCK1YNZpQRp89wNldrtY8vLAP4_DXLjoYNnKY6vZ1HXhr3Gn-Te_3YDPUlUlpRPrllcRkCTTctsGeMEMd1Jm6vHx0rbkVXOVRA0JFw2PMJgoH7v64F_2AD2ukf6w72ga32ydSluzmhH8YrVbn5H_CjpTrljPy3yxzCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfU8z8ZZ--XTpo-fX0qRmU-4ZXVNGC5jBadIAWvu6UU7RL1fb8TeKvSyhrSHGBIGyi7kGPCY1IkbtIKo1NTmbN70eJooPOr0alkBvwkX1jvVDP7xBPbwiDT6-UEgfnqnvV0pNbaJ8upaM4Dmh9oIYvQLX-ipeiMYLoikBPvLjDqfc3PirF-nc2l12QHXSB6k5P06dxBAt4Hx2RM8J8iujg97CotRNpL2bU27fiZiVY9l9W0z71tT01t3w6mJGkAOevsTeQ1RjYbV0aKpmb8Fddoz0VPNxnrHUrNlx9T7Z2zGuM5KvyLgmSk8JdFZp2B5y7Qz1ikA3FYcSEOOKbQaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWrXATqQUWbsNBqMdYZt9sRk7vNrviwiCYF-htK6DBf7qreZeq4AqoDFGUb3Oe_OaLwl4CCDWxqy01zX7PL7kUnKGyvUFLTzLNGMN4ZUnda2McfsJHnp_rB38b4_yBBIH2diEhLmnRHPgQO7AHooINSjCpYMdfw6Gc0Tz0Hr8XmH7T6UrzCGcKWa_8W-xeTJSPCeLZSLjSMQnUb6PToutA79OFg_cbLmyTBG8FC0kMWl6OzYT8Dshvy-vRvzHEg7AspTialsYRRKwR48HveQTwoa-aa7i_ZGhg0I7Ln9_2DuDfHQiHTy-ORgGnU_uPIvxGEFTiHIRg4M00gx7QbAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z91Lp2iSaBIY-1NBeesGcMjIL3iFjsPO_qYD_z25C4JRPtbZTshbyIbgYBH0g0KTclm7M6hyrGR6KHywpydqwzNFmmt4sT49265ef3tK3iH18lb2OK6000G3S0xUcN9sU5XlEaNMKoXyMe9v99QVzKxaefKlRljDlF-c5unBK3bn4qtwrZw-Z-2vs2NVdrsyEfJuvlQXtqa4Y2fPp7NS6Z_UUopVsGnc2p475GzzEEy5ikXaCNT5KSZ27q4aPdPi4hmN2_QKoHB4lfn0T0nzkSHiTpjEp5LRi_6p3uTNQnL6NPa21xsVPqXVDROypHiVSisAP5f14stePUjMyfE-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dKnanYsIliwTK4AbaNrDUcqUQKeGIha3DFrYecIcZhC-JCcFa5_IiVYf9uXemGMbBiQYH_QwO6sic_USl6loG-yc_ocFYGaHWsmX2cydFCjZ6wLJpoHtdZJIzQHeVdpzaWNZ03ceFqxhww9yO_v37XfgzY9NDcJjiBVfi9akSiCPNmW9eHM8WL3mQUfISKKxFtjIvsLFfbUkFlehAJ2RvCuVcX0I9sBRBbRV4VXImW3I75XobzjOrJa85e5-f51W_-0MScXZSKkYq4S5_VzLAgcs3fEzJcRJsRpi0I2H_kNtcCs_AkLcXtd4c1bqcFm36ml_bjS0ScUY-dKi4nzasA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dKnanYsIliwTK4AbaNrDUcqUQKeGIha3DFrYecIcZhC-JCcFa5_IiVYf9uXemGMbBiQYH_QwO6sic_USl6loG-yc_ocFYGaHWsmX2cydFCjZ6wLJpoHtdZJIzQHeVdpzaWNZ03ceFqxhww9yO_v37XfgzY9NDcJjiBVfi9akSiCPNmW9eHM8WL3mQUfISKKxFtjIvsLFfbUkFlehAJ2RvCuVcX0I9sBRBbRV4VXImW3I75XobzjOrJa85e5-f51W_-0MScXZSKkYq4S5_VzLAgcs3fEzJcRJsRpi0I2H_kNtcCs_AkLcXtd4c1bqcFm36ml_bjS0ScUY-dKi4nzasA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=KFoVWkTBCh6-pUN3ck2yZ_N5KWoLOrXH5LiV56PePAtj_5HFF3oivifxgnVTTEFlFllOC9qIMRqQkdtmmm093twZYLuPTmyEnuL4csufbBIAD3MAahuRjtCaRJztgcAC1-2j3D0-SBJU3XpzupsB83StHIZbV1OfRcjOWQe0bEBTv-zoT5lA-H3oLuCYPdhjYukaCNdtZhvYSs-EenkK9SMLdaITqwHEpCht2yBqJa-sjTybH5_ANcu0Ja9KCLNDt2AegcTHw89qkUmgQZAHzzMmALUe8CgS8G8KS1VecySa0Siy_gYyWEE3UdPbZeT7Cwddh7JyzKA6MgB-Cj1mxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=KFoVWkTBCh6-pUN3ck2yZ_N5KWoLOrXH5LiV56PePAtj_5HFF3oivifxgnVTTEFlFllOC9qIMRqQkdtmmm093twZYLuPTmyEnuL4csufbBIAD3MAahuRjtCaRJztgcAC1-2j3D0-SBJU3XpzupsB83StHIZbV1OfRcjOWQe0bEBTv-zoT5lA-H3oLuCYPdhjYukaCNdtZhvYSs-EenkK9SMLdaITqwHEpCht2yBqJa-sjTybH5_ANcu0Ja9KCLNDt2AegcTHw89qkUmgQZAHzzMmALUe8CgS8G8KS1VecySa0Siy_gYyWEE3UdPbZeT7Cwddh7JyzKA6MgB-Cj1mxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=PRU8qdrj-FkjD76mdb4dsGESvdY_rEr1Dq707IZU7rRWSKcPz9D18c4YTO9NpT3HWMZv6LcxGroqTnMKKU_7FcdVvdPaH8ThhNZjZBYZO3GIjrsi_OYp4Ki7s-WAUOg6A7IxL6h0gBKyfMLfv6R5rXLbPCxNldVxgamzFwRu48IKqevv8ykW6k0qtLxSGGTDrZ9cfbPGBDTWxU1sk6cdDskeKQYZrkib28M9JSGuWXejWLkOx6-W88jgzZiZN4-s6A4H7Qmv38xXaY4qSGe5o5-CD50kdDjQ2ale0z5mjwur9jmaOemnJ03qAyNFplchxF8MCQnl9poYJhGI5ZOVyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=PRU8qdrj-FkjD76mdb4dsGESvdY_rEr1Dq707IZU7rRWSKcPz9D18c4YTO9NpT3HWMZv6LcxGroqTnMKKU_7FcdVvdPaH8ThhNZjZBYZO3GIjrsi_OYp4Ki7s-WAUOg6A7IxL6h0gBKyfMLfv6R5rXLbPCxNldVxgamzFwRu48IKqevv8ykW6k0qtLxSGGTDrZ9cfbPGBDTWxU1sk6cdDskeKQYZrkib28M9JSGuWXejWLkOx6-W88jgzZiZN4-s6A4H7Qmv38xXaY4qSGe5o5-CD50kdDjQ2ale0z5mjwur9jmaOemnJ03qAyNFplchxF8MCQnl9poYJhGI5ZOVyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HSF6CY3URQeGsFZKQhs5qArqshgUzbFbFz9mUmCsgP_Fp6H1VUhzJyu7MMqZsa8WgBdXKPXc9CuEklJOsp-aYSa4PaQgK34fwfj3uVBLtajN-txQokMgKUDj0r93TYfgnlaGbAgmF_D8HzlyXNV2dwLWKezT_8fVJPl6IatLIfHU_O62C_D82heXDGvNZwNx9UgM2tZvlSVoDuK2kwcJPRYvijc1dfo5Jt_lZniWL-frzY-WG5hLbo_G1F-fSGDoLLTlbycO1vQTA1sTIFPOOO3asRk5dnj4OQC_r0Q39PMIrKJPKXeg1eAKlKbEBWUj1D8VbZh8bcBoM3OV8HGSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=WlcwE_N7FpeMsPgXyC-DU1TPJTJzJVyvt-KfOR83tm6ahEh8OBxBT2KzqaMXf6CwytAcol8DDXih2uXgrquQyGJOMtXdzQ-migO2ojyQ2jLD8bFrSbE05QH-pGxY2vSNvBy_tyF0d21T_t7QpaK5TPCTQ-vscUfln6CrBec1eAhoroniNCzuja56-moEeRsChLqoMOQmT5hn-rSoRmdoYD6oCXnZbjrWg4JNKrt_HJXKy1dYinvL-Q-q_Dy8wYh2KtBkw6LryZTzjPeLRNm2olPpsubM0co2SUw-uxNFdDecamZkHeiGY7TAy6nNWOY_Jb3N43ug5y5Fzb_SoSIlfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=WlcwE_N7FpeMsPgXyC-DU1TPJTJzJVyvt-KfOR83tm6ahEh8OBxBT2KzqaMXf6CwytAcol8DDXih2uXgrquQyGJOMtXdzQ-migO2ojyQ2jLD8bFrSbE05QH-pGxY2vSNvBy_tyF0d21T_t7QpaK5TPCTQ-vscUfln6CrBec1eAhoroniNCzuja56-moEeRsChLqoMOQmT5hn-rSoRmdoYD6oCXnZbjrWg4JNKrt_HJXKy1dYinvL-Q-q_Dy8wYh2KtBkw6LryZTzjPeLRNm2olPpsubM0co2SUw-uxNFdDecamZkHeiGY7TAy6nNWOY_Jb3N43ug5y5Fzb_SoSIlfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep2dEaMQlkj9ENCAWw3gpaTIFii5puK5hi5SJaoXxFMaPzblV9PTMjgPnv-lS-MszqITiRL_MW1o-CruvZBvmcT1n1Feynvp-lL-CIDfWSUw0OgoN8UDDu5OISUZhbAGl3R0qpOMb_VeZOsUPiqRWeOkYwmr3205V9H2uAs1gSSIU5NxuLjJSgCmNWxluRoIM3BaEbyCI8vBgd--hVa75rOwjcAVOp5C7TT0UbKECkS7NahoVeP9MENTpkNODq299Qn3JNwiVwO-prLUOc90iJZTZnR-9rZyE9RCeaVTODqn5I2mbQ5txXirH-hg3Yij4-bWRjixwXBR-ZIXaoo0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgXeXLWdH35utEcYUon1hBwDJeZ8H-3KEStrcjUc0ocRUH-GWuvQc4zN2rMGCWDIYSrSwd6YfGltkVH58csLcrCdg4ifrjiZR3g6_EZAIS42RxsqA74TOkwKwwycTJuxqZrVLax9O58cU9aWHplzpoDBvJScFf4_UGM0x4CzR-xVzhnwI369WqKYeEazjAhk5-DVdVdHZxkN1HiCUj57fIDveyHe3u-qBFeD9L53qs0iWMHTbSySZEBO3untZWZVgoeN6TMaevv_QLNByPNTphr9VnPjTLtStgfUymuqIKiw3-JaF2EL_pkAVWmrvfH3zpSC8F9RF2ESp_0LMAVwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=mcP9hhLqZXuPL0ae5qSz--K4V_rlQD4BpmsdM1gpwOwLFJv1sXKAK7Je6DXBuK6hwpTxTJTbKZOg-D8aLBLQyb9YHwGo1g4-G1tnYuKcncySZfRGrVPFr-OnW8muEixZF05ZKd2yXPVPZgtKcGLe9jWQo0mmgYgPhIyN_Q2sC7Rqp54Xo_YMO6_7ygW2goXYhRrunGflHPvQB3ZSfxeXggHwNS-Nky1785k6GNNqc5zeEdwQ-MNxFoJ02T1bAEhgW1iY1M3c35EqeTzFhxao-ysFONpVPn32p5SoURHlDN382r0wRsF7J4TFeYOe6dtIArY4e4d4tjpnmCNxXI8kpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=mcP9hhLqZXuPL0ae5qSz--K4V_rlQD4BpmsdM1gpwOwLFJv1sXKAK7Je6DXBuK6hwpTxTJTbKZOg-D8aLBLQyb9YHwGo1g4-G1tnYuKcncySZfRGrVPFr-OnW8muEixZF05ZKd2yXPVPZgtKcGLe9jWQo0mmgYgPhIyN_Q2sC7Rqp54Xo_YMO6_7ygW2goXYhRrunGflHPvQB3ZSfxeXggHwNS-Nky1785k6GNNqc5zeEdwQ-MNxFoJ02T1bAEhgW1iY1M3c35EqeTzFhxao-ysFONpVPn32p5SoURHlDN382r0wRsF7J4TFeYOe6dtIArY4e4d4tjpnmCNxXI8kpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTq_mXqcp4IArWlOhVuQsfMGyNmeVHiEPwLD8p49yvfZW5ftrMnLl4jJDhA6SXZWx7m826n6x6S7iEMTxzyJB__GAIhAUEK5kc0Uis1iDlFrzShxwdKQxqDW9joxBwwcL_oCdmYpoLC-M-JUh-XqIUcHWUk_bGmE9svesnfCPvWs6w7fw79T6R6g1QIleW8zA-wW5YfTws3JVGi2sQ7D3VUSulcsFsHb0Uyjk5PqVVnGBsTcsaXWvtQUof785YuIsj_GyO-1L0jBXM1poRVOKLn9_UuYCqWf2cAKtw9o83W8kMnJpxyZLv04qm54fRNb7hb4gxwLwtvkO8YlnpKSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=L9zIdYLjuiPWWfUOmhM1Wo5HrDZ5YGHxSChpFuWxXj7lmME2Bo_P-RYWkdSHLye5hbKwVoToD2okFKwgPLFpf503ij1u-qGpFag0Zv4E8nMUSzKy3A0o6nXL2kLzFJtFCpteIk7OxEKb5E3oIzXSjXZHsKmKKz9y_9ogE2AA8eDXf1EnbfgE05aNXJts9yhGPHjUQEcfL0DvoIuXNBY1cGsSnunJa1oVQNGM8nutvKxZj6H24jA54Fx_4iCpcbsvaOan6V_atydXId3TtVyPQ6AyOegzlMpJu_5W_s6LxlhO9W-0BEGNJqwB_f6bi6ZEkDmqeIQBWYxa07f8MVK8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=L9zIdYLjuiPWWfUOmhM1Wo5HrDZ5YGHxSChpFuWxXj7lmME2Bo_P-RYWkdSHLye5hbKwVoToD2okFKwgPLFpf503ij1u-qGpFag0Zv4E8nMUSzKy3A0o6nXL2kLzFJtFCpteIk7OxEKb5E3oIzXSjXZHsKmKKz9y_9ogE2AA8eDXf1EnbfgE05aNXJts9yhGPHjUQEcfL0DvoIuXNBY1cGsSnunJa1oVQNGM8nutvKxZj6H24jA54Fx_4iCpcbsvaOan6V_atydXId3TtVyPQ6AyOegzlMpJu_5W_s6LxlhO9W-0BEGNJqwB_f6bi6ZEkDmqeIQBWYxa07f8MVK8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=QeSGl9hWni4iG4kvfRWg83ooOcAfagcGYK-z-HE104fvfCS73F8BDa-CkgKqIpE-Q4BoPTna3wnpZnLOKFBQTHe91xuNeSFJ8wqfAMy02iByn0XLd8DRgsRnxUUGlcWgbR37DuFRhPWO-q9ysrCkIXf7xzuKQVl3gMls0RufyvICJroqGDwHCPN8u26Ku8CXbXzUJV_MGlRdAo2wryAWPU_RKGjnfKP_xRCimXPX-kaVIRtyKXB3wS19CCrLFoesCSXjJOjt32m9GOi9On6A7HXdebbMPJz5H4LDKQwZmJV0YzINMve-H4lASXBtTgnVy4adeBbxBObGLlPPv6YtWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=QeSGl9hWni4iG4kvfRWg83ooOcAfagcGYK-z-HE104fvfCS73F8BDa-CkgKqIpE-Q4BoPTna3wnpZnLOKFBQTHe91xuNeSFJ8wqfAMy02iByn0XLd8DRgsRnxUUGlcWgbR37DuFRhPWO-q9ysrCkIXf7xzuKQVl3gMls0RufyvICJroqGDwHCPN8u26Ku8CXbXzUJV_MGlRdAo2wryAWPU_RKGjnfKP_xRCimXPX-kaVIRtyKXB3wS19CCrLFoesCSXjJOjt32m9GOi9On6A7HXdebbMPJz5H4LDKQwZmJV0YzINMve-H4lASXBtTgnVy4adeBbxBObGLlPPv6YtWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi7dXnAPJjqpOWSicO8v3gdKhtLKaxVkCj04Y7vT5IX2jWnqqSMhpRdjxwJjcmqu0BmIUhwLeIDEDsLCzQlRnWF6A1EIegPOWYAmK5XS1vM5PUUssdSNKuN0D0ZuYLswK8oU3M0nVpvVq_q5Wi21BDBxGi7b4xkCGag2rpR_kfcZwQhmQ2Gr4RMhOXMdA4f5tV2imifUbK9PSBVqhnyOddCFoDDWpcyiiTOJNmJvhxwkgGYVSRxfAgrjZkEblUCDG3tsPtFqTH2gWMT6DfZneySNShQMelUb5B56klugvxH3XnQFCxd4atHEcjJWGHS1CnA2Xp6tyB2ijhNdv_NBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocaopJAHQfFVm7eI4ETP91pdIia-ITi0cmHS68Kc9znFauih2rOn5PkuPPSCKDJadVpqIcBcXjcnkLJzlZB-9TxDj9y6-eqwfY1z6w2scuHetV8OCdl4VA2LXqre9_2PH0ETp3KwKvBFuHVFL68WUMDaIChcfqHLnUtBUpDEt2bXfv1ux9kwII-QKfMNNEfzZX2MvinYg65RDMAh5QhfqNJq-jSI344fv5NX5EyM8YXcg0JiM3HtaM09B-eFa7_pUD2iZ5ovP9EJttzOQ64eLNuTQm9SizzJ-pjoKrQmwybb2ssGMJt6O3wCJJbab9yDNTH8YJ9HBMRYXi23iMoC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=D_7iLcy8fLg04YhMwKydboUPyJNyCPIJnyHp2H8vJXpehbBvhk3Br-NyLHB9grBy2pD3s2yuIgrPpRyRAcYvbUNNrxR_VtzT_3AU3oJBI9h6qWhgMa-29guj1WlVjEimUm3mbAuakRN8Ox0mw3UNiM6YZ8d1_KEltJznkrgShlgPcKCgP7pgsvV5ZMqILL541-s-O_oNNgO4e-TzalQbnEFZ1OpV-Hy-3ZzTIMjIQgGBfIhYE6dVBDra-YHe4bX_1_1IotRh5RNH7Juk3wlCKxDpvJnqDW-VlpI7eDQir3U5GdTDX7MwJbQI4uhTRPUXA12Q1ShAxfi7tArv-1mDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=D_7iLcy8fLg04YhMwKydboUPyJNyCPIJnyHp2H8vJXpehbBvhk3Br-NyLHB9grBy2pD3s2yuIgrPpRyRAcYvbUNNrxR_VtzT_3AU3oJBI9h6qWhgMa-29guj1WlVjEimUm3mbAuakRN8Ox0mw3UNiM6YZ8d1_KEltJznkrgShlgPcKCgP7pgsvV5ZMqILL541-s-O_oNNgO4e-TzalQbnEFZ1OpV-Hy-3ZzTIMjIQgGBfIhYE6dVBDra-YHe4bX_1_1IotRh5RNH7Juk3wlCKxDpvJnqDW-VlpI7eDQir3U5GdTDX7MwJbQI4uhTRPUXA12Q1ShAxfi7tArv-1mDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6nYKxSQhQiEMtIEiA_ZyNAy7hmhQeqDy1qtOv28JwIK86QMCcV8cBZM_GSWuowEVQrOT3zQLvedGM5acYgnnHJuL6cT7DFimeozf_yTOacS3Lz8BS7mZj-hdJVoLxqV-I2zW3Xa6pOkoQayYHC_WfL9lN2nQmkbhdNtxBE0CpdwFUEUhxviqQ8c127PoptKf4t6zjIdkDI3fsTljhkHcSqKES3PWhDE80uzE7pbdSEdjxwEAf_mgHazpV9UpVj3qYoSaRhDgbm5sCh570Jjo5Yb_M_IjhtwKGjmWkdUX9jyRl4eZ_DI7DMdZ8JAIrMMrYEMfxEit0ztboxoTHemJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=l8y6YXEKW566Ci0RWrVe_MWjpVjOFeXj70uGTfkgnMN-amBqtsoyRhI2_9-8PGl-H98Y7V-NtIyKMzMEgFysKwLeT4K9QsCXp8wekqQa5E8oFwNzs3FJI2fGXwt21UCx79GjQfwg_12VexJnnJ5n4A6bWl1nyeujsqxnD96l5ptY49JE8bP04jN9Ozf4AtpAo8E0vMuyIwp__fQodRXb8gusNNlaYNI-hPyG5eNpPorWOpXxw0w6n-hHM0IJB4I__-w3af23b9UcStdfrR2qm1ABVyJsp1K9qptGJPV-QAl1aaIpFrMIntgoboPMZKYIDB4AY4uftdx6V9jnrPiQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=l8y6YXEKW566Ci0RWrVe_MWjpVjOFeXj70uGTfkgnMN-amBqtsoyRhI2_9-8PGl-H98Y7V-NtIyKMzMEgFysKwLeT4K9QsCXp8wekqQa5E8oFwNzs3FJI2fGXwt21UCx79GjQfwg_12VexJnnJ5n4A6bWl1nyeujsqxnD96l5ptY49JE8bP04jN9Ozf4AtpAo8E0vMuyIwp__fQodRXb8gusNNlaYNI-hPyG5eNpPorWOpXxw0w6n-hHM0IJB4I__-w3af23b9UcStdfrR2qm1ABVyJsp1K9qptGJPV-QAl1aaIpFrMIntgoboPMZKYIDB4AY4uftdx6V9jnrPiQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH9lW7VqpezoteWx0_6xrUi4mkSTePT8BDcCzZER9jgzg3YGHb3GMG6MuyCemF-ITzz461Ts888Ppycmocr8fYsOBMxS-dm3rhe6CnxC_o--4-32u3znemvKFufn7ySAKivbDPU2aJnsz-g8q9Bi_l3ueMtopj8-H3eF5aMkq5VNnCcn-jwkppYlnKFZZThPe9HBwU2xkjpQLZiW9-t6OfIaaUIieXLRy8chfLhXogtPwXvdkhpD9xfOJcTwZU0sXkQPHrXp7T6_h2mdPzNy6xCZrM69W605r1-VuAHeWjGHeyj1b-0RPCTWYVZLnSLgfLJ5N8KLukylJbul6n6gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=EijEsTunDLZiK-R7rId71wI--mawIOnf2rMktLT5TaYcLLqIcb56XLOcWvKIK7yN_kMZw_ssSmfTgz53aDkgO58jam6kgRwbkEu16bW61zZQi3seigs1J5Z4jFgMvRP8WQ1Q0UEFq-GDUIQ4-gqzGqzHQyTjDoTB2hqp3LzxZ0Vd-Hy80gcgAZIV8zzFyRsgHx3TmjvG79gfuDJqE314dzoP2lktodcA2dLqgVxLrKUXyCt1dhDygEpRxko2zFq_N12Rnb_knMAhgUB8trW47D4ZQZk7mSXVfPBUqCHDaDebH1x4l89N0jNHZQzTIm8xMkG55tYe7v4IbH9QxvQCGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=EijEsTunDLZiK-R7rId71wI--mawIOnf2rMktLT5TaYcLLqIcb56XLOcWvKIK7yN_kMZw_ssSmfTgz53aDkgO58jam6kgRwbkEu16bW61zZQi3seigs1J5Z4jFgMvRP8WQ1Q0UEFq-GDUIQ4-gqzGqzHQyTjDoTB2hqp3LzxZ0Vd-Hy80gcgAZIV8zzFyRsgHx3TmjvG79gfuDJqE314dzoP2lktodcA2dLqgVxLrKUXyCt1dhDygEpRxko2zFq_N12Rnb_knMAhgUB8trW47D4ZQZk7mSXVfPBUqCHDaDebH1x4l89N0jNHZQzTIm8xMkG55tYe7v4IbH9QxvQCGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=FoJyKqECYqiLfQVwgJdKB8T7-qwJZe7NleO9Yhvt13uwpVp_XnpuwLClu2vV6U5OAT2LLm621kAHxcIGMP1EYoTFxir54HKcWuNVb6PFdonrZiH52E9e6ZY9EC2VcYJ0EA4s795JFpPlBUOK_B8M8O4gxJBQgQfOk8BZXsKntxMTgFZwSXNhmfCjkaKV6wETgXtxZKFJVVL6IEEAIQWahj9zhwS-Lw7MXWtVwwGhMXGxll4thDHvhugbTMaqO-XllvXI3xRGjWtPhBsn0VCVvSxeC2KY6unSL5hSLuGPrrHXdzD62JNmGmTD3xttuE7_O61K2z8T2EWEu4qkfDsQxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=FoJyKqECYqiLfQVwgJdKB8T7-qwJZe7NleO9Yhvt13uwpVp_XnpuwLClu2vV6U5OAT2LLm621kAHxcIGMP1EYoTFxir54HKcWuNVb6PFdonrZiH52E9e6ZY9EC2VcYJ0EA4s795JFpPlBUOK_B8M8O4gxJBQgQfOk8BZXsKntxMTgFZwSXNhmfCjkaKV6wETgXtxZKFJVVL6IEEAIQWahj9zhwS-Lw7MXWtVwwGhMXGxll4thDHvhugbTMaqO-XllvXI3xRGjWtPhBsn0VCVvSxeC2KY6unSL5hSLuGPrrHXdzD62JNmGmTD3xttuE7_O61K2z8T2EWEu4qkfDsQxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuRDkgFdp-535RCghCW3mJMWrv2bvumaOK_bJo1pSlqv99bjiLfdTyWG8NFcGIGyJDpkxhuqmD7Kh7qAB7kD4ttSe2w6nBolm6UoMoyPNdYXdqlyoETAh6FC5pLVUpf2wegRBxJW9aUvK9BHt9kRi7WQCsv1eRkWR1pj6TK-W2mDXL75sH5Fj8P8m3JDwRceD24V5ADSpZL4NdHOza6gldx-gnbaN_SdDOKxzDNQL3WdSp7Wh1NC4wV6jQKl9Xwe0Hu10KT6kM05cAAVOVtGgvqjzVvjqJbqAKzbP4UUw-mPZpaqdA3M36G3EMiwrrBJdqM-7tunyy-qtikKU2DcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhlIs85fNs6_GGQETwgZlAiQ42Be4BgyaTXtZge-nRkOHkuc0A7dVxYO78A1Ew93Frx1c5stc8osSj3BW7QJGFtBa4d1A-lrh-3WDamUqD3yvF5vFmVXkrG3mmiUNHQ89XKL1TV5x5Luffl_opUAU0HbYTsUpSnuy4WMCmX6l7mB7EteGcOm3g1XTbTcNO81klk7jtkwWGvkcpp_iEfc12fMX_YGb2AZLSDzXoN0NyFwz-GEOBxXg5ob74bcpq6CxTPXmqKdQrjnv16Y35aCyRGiU-ag2AhrVEk-Ybcfl656b3mL_CRma_4UMkwtyEpkqLz3VgNbjGjD6t8ul_quiuzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhlIs85fNs6_GGQETwgZlAiQ42Be4BgyaTXtZge-nRkOHkuc0A7dVxYO78A1Ew93Frx1c5stc8osSj3BW7QJGFtBa4d1A-lrh-3WDamUqD3yvF5vFmVXkrG3mmiUNHQ89XKL1TV5x5Luffl_opUAU0HbYTsUpSnuy4WMCmX6l7mB7EteGcOm3g1XTbTcNO81klk7jtkwWGvkcpp_iEfc12fMX_YGb2AZLSDzXoN0NyFwz-GEOBxXg5ob74bcpq6CxTPXmqKdQrjnv16Y35aCyRGiU-ag2AhrVEk-Ybcfl656b3mL_CRma_4UMkwtyEpkqLz3VgNbjGjD6t8ul_quiuzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN0edO6I5DX171rnNRfSEdZshiP3oPlnPmd1Hw5B4cJETDotcpDMNVBEKhXwBFJs2B1zv9yUOz0304MCe0uzr-9gvJMAkZcvs1alZA0TTOJeGMlDSO7ot-BFf334NpbS5ek3YVJ8nOvzTIBQ42MzLyj-AkULQPQ3qSvhIPzdAlqtISBSJ8CzVTM4lqiQKmr1MbhcedrEaxJBEguECYd2HANZ_0ILJiuUU3EsYs8n6E_0-eWULVRSv_X0v2Sj4AgSeshjEBydfrimWPHJN41L_5OAVpy9lgH6cPTxZjZuDBg-oJSmX6qDEmY0PU8ri1ncNGuqFWZ193GytSygzjfVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
