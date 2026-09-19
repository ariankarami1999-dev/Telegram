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
<img src="https://cdn4.telesco.pe/file/QVXn3d0oSKEdI4e-U-s8biouUjj9p-uqeX4bnbJeDT3t_d-sOkfNgihB2j2qSg6cTe0z7jnqlHGvtB1u1lW2wKJrJxPRplcHoxTVMIjypRJG062sOsFHKOTk4S-nwHMJ9yv22l4anleSmjKf0rg5UwUu_0G8fAtmWyzn533B6kLukAyEENSdx7UAZrdLO4fREmCvPB8AHGk2JXDxEhpzWlINwTiWGyiPsAAczVxupWCBgltZAVUEjeSPrjG3P4JBkJURzOBIA1KvAwb6YqD7A7qCipizHf1Ozg5VFOLBqJlYkSr2amwqijFnrMAZsUayqCLjifnJg4Z1H6a-5CwupQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 05:53:03</div>
<hr>

<div class="tg-post" id="msg-691064">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=HCiq8oWlBN1D5NDWepVxE8095w1bU8Uu3tFdmFxF5HNawr_r39t40MFJadfcYdCucq0V410fTwxJ5uzcEwMxCDJlbrzm383JT65yX9yLIUj5q3WCBOI4EVoj1Qnf2Z9O1RS8iq_J-HRhpgdJjwRRQv4EDZi5_BdvCVatnvQDsLzK_n-sHoSsTTAcRwWjldcQZQcLKpitbjLg3scfV4L9Kpy7-zlrl6F7Drc5U1h8upWjx9jZxmr2XffFQArDPVC-Cl01HTbyE89yp1UrZrJdM0iWICkrRttyNle7kO0nlzh559pwiePiSWiKliWshL4hNycIK6W2Hz_iP5cGuSBw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=HCiq8oWlBN1D5NDWepVxE8095w1bU8Uu3tFdmFxF5HNawr_r39t40MFJadfcYdCucq0V410fTwxJ5uzcEwMxCDJlbrzm383JT65yX9yLIUj5q3WCBOI4EVoj1Qnf2Z9O1RS8iq_J-HRhpgdJjwRRQv4EDZi5_BdvCVatnvQDsLzK_n-sHoSsTTAcRwWjldcQZQcLKpitbjLg3scfV4L9Kpy7-zlrl6F7Drc5U1h8upWjx9jZxmr2XffFQArDPVC-Cl01HTbyE89yp1UrZrJdM0iWICkrRttyNle7kO0nlzh559pwiePiSWiKliWshL4hNycIK6W2Hz_iP5cGuSBw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فشارسنج خون درجه 1 برند Arm Style
قیمت ویژه و فوق اقتصادی
📌
استفاده راحت فقط با یک دکمه
📌
کیفیت عالی
📌
دقیق و بدون خطا
تخفیف تا 28 شهریور
🏠
پرداخت درب منزل + ضمانت بازگشت وجه
خرید سریع از اینجا :
👇
https://memarket24.ir/product/fast/37863/180124</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/691064" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691063">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
المانیتور به نقل از یکی از منابع ارشد اطلاعاتی اسرائیل: نهاد‌های امنیتی اسرائیل با هرگونه حمله پیش‌دستانه علیه حوثی‌ها مخالف هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/691063" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691062">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
منابع خبری گزارش دادند که ارتش عربستان مناطقی از استان صعده در شمال یمن را با توپخانه هدف قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/691062" target="_blank">📅 00:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691061">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/691061" target="_blank">📅 00:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691060">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجار در جازان، ابها، خمیس، مشیط و العلا عربستان خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/691060" target="_blank">📅 00:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691059">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dcc95981b.mp4?token=Or1DKSRi-s3_6FqE6vNNYs_pRhfsdEEZLwGW9HPmT9UlQWFcStr3pMpihyVAKD7CVnxazn4xz9x4D9tCFP1KlxjdoMhpumYNsmZgKXu10L5Lm0tH_xV2a2bAE5e7ye7HEFM4kT2uu9OqSdSV-oFyUomTI-hF9Q1WOkVPqNc_IpIHWarm1O2Je5FiQCzNtQWPLS0_Xbq-ecHK6e8myHxASWLpDCV6zVomCQU8ps_VR4yki_QfoDW5cQBcPR6DRjFOpJ9gyxClm3WTKXnMCXe-GEMxpEmgt-FaW_XNKGh88X6_cPHPoRQZVAU5Yjs4RLdey8YTTQ-Viwcwk7jVo9-GRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dcc95981b.mp4?token=Or1DKSRi-s3_6FqE6vNNYs_pRhfsdEEZLwGW9HPmT9UlQWFcStr3pMpihyVAKD7CVnxazn4xz9x4D9tCFP1KlxjdoMhpumYNsmZgKXu10L5Lm0tH_xV2a2bAE5e7ye7HEFM4kT2uu9OqSdSV-oFyUomTI-hF9Q1WOkVPqNc_IpIHWarm1O2Je5FiQCzNtQWPLS0_Xbq-ecHK6e8myHxASWLpDCV6zVomCQU8ps_VR4yki_QfoDW5cQBcPR6DRjFOpJ9gyxClm3WTKXnMCXe-GEMxpEmgt-FaW_XNKGh88X6_cPHPoRQZVAU5Yjs4RLdey8YTTQ-Viwcwk7jVo9-GRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاد استتار اقیانوس؛ ماهی مرکب صخره‌ای باله‌بلند که در کسری از ثانیه تغییر رنگ می‌دهد!
🐠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/691059" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691058">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=C6l8RWpuout59tsxiFwuQWTgYkRHaDTEo_qaHy7IravfHibJ5xwlTxXMCOeHGoBVraeiNuxdrg-FYrPcogDCM_oAUKGFQ5R9XwZ-2ewmw3a-WctWHdES17SOPO8wsCuKltSUmCGsKeLSpXkNab0RN5lJmZzY1RkShdMWFrXRVv5NOyrcploAbpe5u6jKRnmwHuP7OkO6Bg4-i50lfChLDlXCOeeSlWyOmgzbVEvo9CMCzEeHcHmBBoUEJY_N3gND3iupLeveDITwDDLHt2Oc5jFfJoFZWZHCt9JjdLzGeZZSutPcyk9yLyo0u85Fkpe9-dVYjNTl1hX28c3hl9Wf3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=C6l8RWpuout59tsxiFwuQWTgYkRHaDTEo_qaHy7IravfHibJ5xwlTxXMCOeHGoBVraeiNuxdrg-FYrPcogDCM_oAUKGFQ5R9XwZ-2ewmw3a-WctWHdES17SOPO8wsCuKltSUmCGsKeLSpXkNab0RN5lJmZzY1RkShdMWFrXRVv5NOyrcploAbpe5u6jKRnmwHuP7OkO6Bg4-i50lfChLDlXCOeeSlWyOmgzbVEvo9CMCzEeHcHmBBoUEJY_N3gND3iupLeveDITwDDLHt2Oc5jFfJoFZWZHCt9JjdLzGeZZSutPcyk9yLyo0u85Fkpe9-dVYjNTl1hX28c3hl9Wf3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه
؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی/ مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با
۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
🔥
قیمت قبل:
۲,۲۹۸,۰۰۰ تومان
💥
قیمت ویژه: ۱,۸۹۸,۰۰۰ تومان
💳
پرداخت درب منزل
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/brief/35160/180124/</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/691058" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
به‌ صدا درآمدن آژیرهای خطر در عربستان
🔹
سازمان دفاع مدنی عربستان سعودی از فعال‌سازی سامانه هشدار زودهنگام در برخی مناطق این کشور خبر داد. این هشدارها در استان‌های جده و طائف فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691057" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFqV2z63DmMCj8LNgip9FEUSJ28ai-KBfBVZ9MORuNWXYYxBwNUnjTY-KL_hewdiOUCRrXflxJqHaFKVmprpLZrc51cWcFQfatE1nygG5pxc9ydciSo6gt8WgdET8WTfhi0ZpjscV7N6Ykh1A0GMF00hWJvJxptApRam_3lLmUiSKNg3lubLr0t7Td9syx_tMxO2bb9MkXUgSXdMzFlMD1jP0Q86W0JrpzH-vxcDIh5oozuM3Q3b57DrU9BcXQkYVLnUZil55jEO9D-0T8wEWA0cdmBsUr5ug6w4TI1idSmsGzgPv3G14KyBnQ5sgaPOR6ZuiCW19ItFrj_YTs98OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/691056" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
در لابلای خبرها، پربازدیدترین‌ها را از دست ندهید
🔹
🔹
تصمیم جدید درباره بنزین
👇
khabarfoori.com/fa/tiny/news-3246091
🔹
ترامپ دوباره ایران را تهدبد به نابودی کرد | نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3246176
🔹
آیا شی جینگ‌پینک سکته کرد؟ | شایعه سلامتی او را در اجلاس بریکس چه کسی راه انداخت؟
👇
khabarfoori.com/fa/tiny/news-3246067
🔹
افشاگری درباره پرونده اختلاس فدراسیون فوتبال
👇
khabarfoori.com/fa/tiny/news-3245981
🔹
هدیه سنگین ترامپ به اسرائیل | آمریکا ۴۰ هزار بمب یک‌تنی به اسرائیل می‌فروشد | این ماجرا چه ارتباطی به ایران
👇
khabarfoori.com/fa/tiny/news-3246085
🔹
خبرها را هر لحظه اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/691055" target="_blank">📅 23:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
به‌ صدا درآمدن آژیرهای خطر در عربستان
🔹
سازمان دفاع مدنی عربستان سعودی از فعال‌سازی سامانه هشدار زودهنگام در برخی مناطق این کشور خبر داد. این هشدارها در استان‌های جده و طائف فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/691054" target="_blank">📅 23:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxnSMqu6TQVvCJzSDjR8qR00rwEODOKwcZR6i-uQoTKgyLPSeIKLc5xXrrbcRc2LEP8m78tnDFDheJfbjv3IlLWAsozo1WuHdwD-sen-uScBeKY6ZhTmTRYvfwAeLSkZu-1Z4KqXWfNbAsgM4bPJeO9R5MEtvAubsreJjTfkvM6-VEA_QQqmHhUH7OY4DQjjtJVryV_ZqRTC8181fQo3q0CwvzooTLmr2Dg_G3QSShr8HVrGnxgxhGkVkPS1qvkeZtVwNYjCcpEyegyHuIPylhfj37gjad6XPalN7PJ6s8ye6VDlO8g_vXD_1w4zqDs-4ObzY_jPZYUAJF_mv918tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مکرون: قیمت سوخت غیرقابل تحمل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/691053" target="_blank">📅 23:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c21eca87a.mp4?token=M5-dt_waIbnxl3c7UtmKEUlJC6hfokW3emv_1AOjux4G6od4qFc0I4JYrA24Mt1NOKyES8UFS3GF6OWRDtEqMre3mrayjUPAMVw0k4-K1tV0JKjXXDro1Y0Q-elVembUI6AAgXs6tF_c92U_hIKDKMzX6JZgPuUe8NmkvLgq1ufyGwhe-7FBOhU8YG_EUXaKRVuvvzW73lZzeEV7M5JWWiYk8PG5EAKE-sykFNLrQA0BUMqVmoeadfWmfkDBexhmbpusXQ9esYIGbs2WqVSgqAo9u4CpUzSjllJIi-Fuv5mYZNfT8cmt_LS8rip2SDamf1M7kRKmFpWkAKJ0QIG4Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c21eca87a.mp4?token=M5-dt_waIbnxl3c7UtmKEUlJC6hfokW3emv_1AOjux4G6od4qFc0I4JYrA24Mt1NOKyES8UFS3GF6OWRDtEqMre3mrayjUPAMVw0k4-K1tV0JKjXXDro1Y0Q-elVembUI6AAgXs6tF_c92U_hIKDKMzX6JZgPuUe8NmkvLgq1ufyGwhe-7FBOhU8YG_EUXaKRVuvvzW73lZzeEV7M5JWWiYk8PG5EAKE-sykFNLrQA0BUMqVmoeadfWmfkDBexhmbpusXQ9esYIGbs2WqVSgqAo9u4CpUzSjllJIi-Fuv5mYZNfT8cmt_LS8rip2SDamf1M7kRKmFpWkAKJ0QIG4Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ایران سلاح هسته‌ای نخواهد داشت؛ البته برای تحقق این امر، مردم باید هزینه بیشتری برای بنزین بپردازند
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/691052" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908b5c30e6.mp4?token=oxz_4SyFWs98aPcVzWyMJ_Dj66gq1jqY4USckI46nt79FXgTN30uBFJpSGjvQDtlMj6g9uImGAVkDIAXoOK42XSGU7uwf5NOowUoEFAYz0VSsnNcQYQXhWWWqHhCRxt6GDxfrRtX14jyle9jMcwB9GbeCdRvzfzC6hLj5iIgeydfdgs7z8PcBqxhzFU3-FIoCwpR3e__Bf06QJrUsvDE_SN-5GsD1Ap54CzpnJrUu3PFRwELm0LXz08JK7mN0GBJsYe5JY3rfRrWBRl4Vu01Qjax0Dgr6Xt7jR7fQoG3KpMrXCy_2dzrFsUpkRvHSHOvCknRcIgKEGhYIOKxH1UGyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908b5c30e6.mp4?token=oxz_4SyFWs98aPcVzWyMJ_Dj66gq1jqY4USckI46nt79FXgTN30uBFJpSGjvQDtlMj6g9uImGAVkDIAXoOK42XSGU7uwf5NOowUoEFAYz0VSsnNcQYQXhWWWqHhCRxt6GDxfrRtX14jyle9jMcwB9GbeCdRvzfzC6hLj5iIgeydfdgs7z8PcBqxhzFU3-FIoCwpR3e__Bf06QJrUsvDE_SN-5GsD1Ap54CzpnJrUu3PFRwELm0LXz08JK7mN0GBJsYe5JY3rfRrWBRl4Vu01Qjax0Dgr6Xt7jR7fQoG3KpMrXCy_2dzrFsUpkRvHSHOvCknRcIgKEGhYIOKxH1UGyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران: ما در جنگ با ایران به‌ طور قابل‌توجهی پیروز هستیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/691051" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6ab4aabd.mp4?token=lYB-GYT32I7W4aGJY3w5AT6bC-gdTKHKjy_YP0a7FKLk90z-xizV_ihua39U3-hOn3xB6qteWg9EkQyom9km8rbu8v6pYrND6kCGjtobJmUEGhogbwc5JDcAQ2nXLBJ_G9R7Q7J_3DtYeP7u_DRmABzoUUvMW3t0IBa-4tg-Tnix23NXm_rU6E14_Net0TDOosmDCFWVkL-ZjLzcx8ciZlB2YnDG8xAFyjF0gNlbBdhW9j8FPCVGFkwDxXbJqTHcy8jD3sLpk1MMlePBbOohTi8UvyforHUMKOXgIxcc1NNs8vTTdCB6XaLaaUOicm1TAUH5EA9zoFhx9I56LML6uSBDsTDbybsZPZV2_yBQQFHmG48tGdH57WhQIhbeKlSMVuLvXq6w5TO3QxQ0RnYDgawWd0Xzj4YKxYAzlwHCa_iooOTEsqVlSphrtVmuPZHNtafRHBe7EPM6rGEzi6JtTfnAsSfGYf7UPhZmM9MmVI71nJyk22q37WeqYRect3etE50Pr0RKib6APNnUqHybutUfX2QGpeVh8J901KzjvFks356dAVaoPMxg1b1qOA9R2KDcrb1IIbSSZmD9veiSJY29cEHKdhSMAdDEuCydaAlaEKQMJXvbcL-YqkKzo0AX8PbdMzUSNtkrIZjguHEkxyJbLNHhSjv9Ls62K07SoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6ab4aabd.mp4?token=lYB-GYT32I7W4aGJY3w5AT6bC-gdTKHKjy_YP0a7FKLk90z-xizV_ihua39U3-hOn3xB6qteWg9EkQyom9km8rbu8v6pYrND6kCGjtobJmUEGhogbwc5JDcAQ2nXLBJ_G9R7Q7J_3DtYeP7u_DRmABzoUUvMW3t0IBa-4tg-Tnix23NXm_rU6E14_Net0TDOosmDCFWVkL-ZjLzcx8ciZlB2YnDG8xAFyjF0gNlbBdhW9j8FPCVGFkwDxXbJqTHcy8jD3sLpk1MMlePBbOohTi8UvyforHUMKOXgIxcc1NNs8vTTdCB6XaLaaUOicm1TAUH5EA9zoFhx9I56LML6uSBDsTDbybsZPZV2_yBQQFHmG48tGdH57WhQIhbeKlSMVuLvXq6w5TO3QxQ0RnYDgawWd0Xzj4YKxYAzlwHCa_iooOTEsqVlSphrtVmuPZHNtafRHBe7EPM6rGEzi6JtTfnAsSfGYf7UPhZmM9MmVI71nJyk22q37WeqYRect3etE50Pr0RKib6APNnUqHybutUfX2QGpeVh8J901KzjvFks356dAVaoPMxg1b1qOA9R2KDcrb1IIbSSZmD9veiSJY29cEHKdhSMAdDEuCydaAlaEKQMJXvbcL-YqkKzo0AX8PbdMzUSNtkrIZjguHEkxyJbLNHhSjv9Ls62K07SoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات دردناک از پیدا شدن پیکر مادر مفقود شده تهرانی از میان آوار منزل مسکونی در نزدیکی اتوبان شهید باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/691050" target="_blank">📅 23:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSejnC_DP1JZh5HsNFnEWOv3eNrdZ0daOJlTsU9Mf2QMPdT6swrQwVjUccyQzVkFtEC5Hwn8BW9slPWe6OfgrbY3yfSYU02m7ItHCEXkiDecWrn3QMGWODIiOUBsKvh1_IpGIV0-eOX10BKAFIvMOecaKijS7Wip-KB0H9fi06LXfongPQ5Ez2G_DjeYX0IHdCCkfAf8T3mj32KNOuxf01U8959BytO3JIxCKw-DUh6t_jNQbrgMpzL5HC57l1eqdbv0LOSzklLLRbzMxBhq8TJVEgP3ipMRrc8vpWebRk0GJUdJnKfHxvoRQmw1JxrMf09gukThwmixQhKHKnF0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه بلومبرگ: هشدار پنتاگون به متحدان: کمبود موشک رهگیر تا ۵ سال ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/691049" target="_blank">📅 23:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691041">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
اولین و آخرین آثار هنرمندان مشهو
🎨
🔹
دالی: از منظره‌های آرام کودکی تا «دم پرستو» (۱۹۸۳)
🔹
ون گوگ: از «طبیعت بی‌جان با کلم» (۱۸۸۱) تا «ریشه‌های درخت» (۱۸۹۰)، احتمالاً آخرین اثرش، نه گندمزار با کلاغ‌ها!
🔹
کاندینسکی: از بندر مه‌گرفته اودسا تا «شور معتدل» (۱۹۴۴)
🔹
پیکاسو: «پیکادور» را در ۸ سالگی کشید، و در ۱۹۷۲ خودنگاره‌ای کشید که مستقیم به مرگ خیره شده است
🔹
موندریان: منظره‌ای از جنگل لاهه در ۱۵ سالگی، تا «پیروزی بوگی ووگی» که ناتمام ماند
🔹
ماتیس: اولین تابلویش یک طبیعت بی‌جان بود (۱۸۹۰)، و در آخرین سال‌ها با قیچی و کاغذ رنگی «نقاشی» می‌کرد
🔹
مونه: «منظره‌ای از روئل» در ۱۷ سالگی، تا نیلوفرهای آبی که تا لحظه مرگ رهایشان نکرد
🔹
فریدا: «خودنگاره با لباس مخملی» (۱۹۲۶) پس از تصادف، تا «زنده باد زندگی»، هشت روز پیش از مرگش
🔹
کلیمت: طراحی زغال یک دختر در ۱۷ سالگی، تا «عروس» که ناتمام روی سه‌ پایه‌اش ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/691041" target="_blank">📅 23:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691039">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رویترز: داده‌ها نشان می‌دهند که حجم حمل‌ونقل از طریق تنگه هرمز همچنان کمتر از میانگین ۱۰ روز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691039" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691038">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سخنگوی دولت عراق: ۸ مهر آغاز مرحله جدید روابط بغداد با ائتلاف بین‌المللی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691038" target="_blank">📅 23:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691037">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d124f0d6.mp4?token=G1i74il6LPiLgjIAEVD8_usNdCkNRWoF3Def8ZNPkAkRDFx_IB4CKIkeKPlaaFBbdJCMKb9craNYYVfjlNGfk4gbNp2RYlL7z06XcrhPSQXd8oj-SftrD71ce5M7gkpRyW5g7YNHVQH8SB0_EMLKSrVm-zkhlJOX3bKeqtPgMFyem7YjgBIB7Slfvc4HdpMVcQNEZGDfJySM3Rn5755S-B3MRfeWelxW8yd3Zmk_TdQ9_CY70cKlnuQTi_1ndiHepFarip-DrQe9p9HneartDcOspSdiKk7TXYuQSQKmbG3D_VXfjRZFjPY7t5jZoEpu7A8ciPUskQzpK_2OEi4xCKpHinCjDcg0ZNhLTGuLxY-b62mMnxxhwpkfDT7p8G1DsyOCc80tH2aN2dm3tG77KhIgno-rOIRVu3t4TpOCya3efY4RPUz7xN4U1Gt-I7wpUv_ZpvT378kpydtq-uQJXP8H7TmGDpiTdjk2jXHeWfakp_1WYOkyeHkxGGysGGE_FgECjCcoesj5ugBYLOM54U59l16EVkNGvxfVeo-djzlSEC_x7-XHGGLysGsTmY6MYHgxHQ_L0wjbPAe3sPzuPIRfV4et_PMAc3-emvAc85S5xdGIPx8sxUZhMfWPUF_pcVIgeAJTkIYP0vclY4Wlgu7HRq73tRzH0NAEZh_nKPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d124f0d6.mp4?token=G1i74il6LPiLgjIAEVD8_usNdCkNRWoF3Def8ZNPkAkRDFx_IB4CKIkeKPlaaFBbdJCMKb9craNYYVfjlNGfk4gbNp2RYlL7z06XcrhPSQXd8oj-SftrD71ce5M7gkpRyW5g7YNHVQH8SB0_EMLKSrVm-zkhlJOX3bKeqtPgMFyem7YjgBIB7Slfvc4HdpMVcQNEZGDfJySM3Rn5755S-B3MRfeWelxW8yd3Zmk_TdQ9_CY70cKlnuQTi_1ndiHepFarip-DrQe9p9HneartDcOspSdiKk7TXYuQSQKmbG3D_VXfjRZFjPY7t5jZoEpu7A8ciPUskQzpK_2OEi4xCKpHinCjDcg0ZNhLTGuLxY-b62mMnxxhwpkfDT7p8G1DsyOCc80tH2aN2dm3tG77KhIgno-rOIRVu3t4TpOCya3efY4RPUz7xN4U1Gt-I7wpUv_ZpvT378kpydtq-uQJXP8H7TmGDpiTdjk2jXHeWfakp_1WYOkyeHkxGGysGGE_FgECjCcoesj5ugBYLOM54U59l16EVkNGvxfVeo-djzlSEC_x7-XHGGLysGsTmY6MYHgxHQ_L0wjbPAe3sPzuPIRfV4et_PMAc3-emvAc85S5xdGIPx8sxUZhMfWPUF_pcVIgeAJTkIYP0vclY4Wlgu7HRq73tRzH0NAEZh_nKPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت شگفت‌انگیز رقص موج؛ چند ثانیه که به ۴۰ ثانیه تماشایی تبدیل شد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/691037" target="_blank">📅 22:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691036">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985f734a23.mp4?token=lC06lAckgBZQJl2gecHUa500M27XnznLEudtADchqHEhY8PB46jQm_b_Q9M_KN9rjBm-rH43-vsr7HUdUTvllhfx0dFZ0yawHaXckzarrs4--WC8Q1OE0Ag0A5jo4XBKsInLSsIvEtfw8kutbaT2gBKM6zP_-vJs2_23DmZRnxihD7dMzafULx5MUaUc6RaUbE5Ell4i5OM1fzMA3PIUgO31wzwgLlYp8ZJrekCMH28noWopu9sBKgCbMPI9As-sbk8vBvfoZIb0PqdagArAOuz9ye96N-MmXVy3qMAKCUR5LPiB_ubu8Y0AbyTbCy9u4j9bvTxS38HmHX1BHPDEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985f734a23.mp4?token=lC06lAckgBZQJl2gecHUa500M27XnznLEudtADchqHEhY8PB46jQm_b_Q9M_KN9rjBm-rH43-vsr7HUdUTvllhfx0dFZ0yawHaXckzarrs4--WC8Q1OE0Ag0A5jo4XBKsInLSsIvEtfw8kutbaT2gBKM6zP_-vJs2_23DmZRnxihD7dMzafULx5MUaUc6RaUbE5Ell4i5OM1fzMA3PIUgO31wzwgLlYp8ZJrekCMH28noWopu9sBKgCbMPI9As-sbk8vBvfoZIb0PqdagArAOuz9ye96N-MmXVy3qMAKCUR5LPiB_ubu8Y0AbyTbCy9u4j9bvTxS38HmHX1BHPDEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشکر آقای شهید ایران از جانفدایان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691036" target="_blank">📅 22:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691035">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
عضو ارشد انصارالله: عربستان خواستار میانجی‌گری ایران شده است
🔹
پیش از این سخنگوی وزارت خارجهٔ ایران تأکید کرده بود: «انصارالله بازیگری مستقل است که خود تصمیم می‌گیرد؛ نه از کسی دستور می‌پذیرد و نه نیابتی دیگران است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/691035" target="_blank">📅 22:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691034">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری
سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو
به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691034" target="_blank">📅 22:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691033">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0510776e2.mp4?token=TYML69b1P0eubrf6Yy1HRWMS8PrUYI0W3ZCE4nAhAP0W6sSCioOvoW4tKKsaA_ZRmcNEygm7rvOcGjr8SMkgMCI9IN8K_Lw0LIvZP1gh541f6odFGsJJpgAx0DOevs4XiA3a36iv1I6aBsoQ5Voj2rmWeCXHUC5pkSPcD0iYV0iHPSeX_7Vqa2UrQ-7WBKR_x1RCjnbSxTmqJzXjLXCO4RxVVa258Mf9CRO09lAKebEuTJuGKhFav3JUPbGqq0pRUft60gCyXIcR1i9sdaOeCSGwmKTE6lxxLNL2eoka0i_o4Y_1u1qnmLGEmV8C7_8flHAr2c2QwiZtWeFTwzsU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0510776e2.mp4?token=TYML69b1P0eubrf6Yy1HRWMS8PrUYI0W3ZCE4nAhAP0W6sSCioOvoW4tKKsaA_ZRmcNEygm7rvOcGjr8SMkgMCI9IN8K_Lw0LIvZP1gh541f6odFGsJJpgAx0DOevs4XiA3a36iv1I6aBsoQ5Voj2rmWeCXHUC5pkSPcD0iYV0iHPSeX_7Vqa2UrQ-7WBKR_x1RCjnbSxTmqJzXjLXCO4RxVVa258Mf9CRO09lAKebEuTJuGKhFav3JUPbGqq0pRUft60gCyXIcR1i9sdaOeCSGwmKTE6lxxLNL2eoka0i_o4Y_1u1qnmLGEmV8C7_8flHAr2c2QwiZtWeFTwzsU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معطلی رانندگان بدون امکانات پشت مرزها/ اینجا منطقه آزاد نیست، منطقه آزار است!
🔹
نبود امکانات اولیه رفاهی و معطلی‌های چند ساعته در صف‌های کیلومتری ترانزیت، روند عبور از مرز را برای رانندگان خودروهای سنگین به کلافی سردرگم تبدیل کرده است./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/qJni4yP2kbU
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691033" target="_blank">📅 22:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4168e38cac.mp4?token=m99kE59F_Avhdf3SoczCY4lTJaXZWvG4gE4BamF3F_a59MDnW9GBU13SKXBl7S4RFm0PiHPtavit9Zv14Tsuji3WBY655823siDbYaED261UdtBRNgTJHJNiyZ0DR1VdToUTZ2JZagDlwyTaSMABN6nPOtf-BVJ5jpz7cCjQIR9AqdnF_caRPaGdTbyJATmKc0XtVV1BdY2ujlPm7FQzfXIHuy4M1evVIaS5jlYsKZgeYa7xgcyca8H3t96xCnnoskzS14Fi8gvt16_ZC1xz52es9a_MIgI6daxorGXWBWXv3Fjjh-p3OzOYK5WzR9J9gGyZUu7VUai6F4Q_IsAR4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4168e38cac.mp4?token=m99kE59F_Avhdf3SoczCY4lTJaXZWvG4gE4BamF3F_a59MDnW9GBU13SKXBl7S4RFm0PiHPtavit9Zv14Tsuji3WBY655823siDbYaED261UdtBRNgTJHJNiyZ0DR1VdToUTZ2JZagDlwyTaSMABN6nPOtf-BVJ5jpz7cCjQIR9AqdnF_caRPaGdTbyJATmKc0XtVV1BdY2ujlPm7FQzfXIHuy4M1evVIaS5jlYsKZgeYa7xgcyca8H3t96xCnnoskzS14Fi8gvt16_ZC1xz52es9a_MIgI6daxorGXWBWXv3Fjjh-p3OzOYK5WzR9J9gGyZUu7VUai6F4Q_IsAR4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درد دارو
🔹
صدای شما از چالش‌های درمان؛ بازتاب مشکلات و سرگردانی بیماران در تامین داروهای حیاتی.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/691032" target="_blank">📅 22:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691031">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای واشنگتن‌پست: تعداد بیشتری از نیروهای نظامی آمریکا در جریان جنگ با ایران کشته شده‌اند، اما پنتاگون این تلفات را به‌طور عمومی اعلام نکرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691031" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691030">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmFI_i8AVuOz-lco_HUObAGuPdCB2ATa_OFBr_0XhjCSbLckchbjGHiI_y9ccanIwcJGdVPugyfOogJLhVt-bbs2jX5pWYobmJUrriPCyvNwhsIu5J1_XV77KbRnVa2PcZRIM7TxpCtWr_oEFoVvUSwKunG0gxiRh9VBjRIytxqR70AeEQZzIGIoy-M1C0Ggdlaka9TMWUWgw7Wvk4zdUw1FscPtuOXFqc1P077GzshR-3ZuwryuRwYis9mo6VtpSkHp_Mc5vl33XV3IMN68u0vgnE3ShHf8-zsDB4OO8Udc7Cql81CRVieLjgrbMZxem8dxYVcYlBDxhHLhKRFPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار اجاره جنوب تهران هم دیگر ارزان نیست؛ بررسی ۱۰ فایل منتخب نشان می‌دهد حتی برای واحدهای میان ‌متراژ هم مستأجر باید با ودیعه‌های چند صد میلیونی و اجاره‌های سنگین دست و پنجه نرم کند
/ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691030" target="_blank">📅 22:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691029">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dd4c53c0.mp4?token=ls9ch3fIkyNmR6_TWSOLG-pBETU20n5l7xQrwj1Qk0h2x9booFKrtd9ybhHGV-g04lznUnNknixTQXkDo6QsWRtU5QocrPOOFreiAnWWoZXsa0pk8Plwkvhca0xBRmpZPbBLjjTxL_gCl9ujm4efpn60p89fsmW_Yl5TyjHFk0bTL74J5_y6UucrXih8Fz-kX5i8GzpqNWu3HlVMWX9tBNB4XYQHfFW5C86vPuCXPdcEFx9WvWCMjule4MBsqf2JZ3CvhuJ1Wfa-eyZAaAcOHrKraZJqqpYQGxumt1yVX1jsCw6NU3Orh0wN-bo1ACpIZIm32_2ZjPsTehsqFl1rBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dd4c53c0.mp4?token=ls9ch3fIkyNmR6_TWSOLG-pBETU20n5l7xQrwj1Qk0h2x9booFKrtd9ybhHGV-g04lznUnNknixTQXkDo6QsWRtU5QocrPOOFreiAnWWoZXsa0pk8Plwkvhca0xBRmpZPbBLjjTxL_gCl9ujm4efpn60p89fsmW_Yl5TyjHFk0bTL74J5_y6UucrXih8Fz-kX5i8GzpqNWu3HlVMWX9tBNB4XYQHfFW5C86vPuCXPdcEFx9WvWCMjule4MBsqf2JZ3CvhuJ1Wfa-eyZAaAcOHrKraZJqqpYQGxumt1yVX1jsCw6NU3Orh0wN-bo1ACpIZIm32_2ZjPsTehsqFl1rBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش شجاعت جان‌برکفان در رزمایش هزاران نفری جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/691029" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oi62KwyDVzPpbilyshTSrDcnH9HKLuCWzz9RMHUw6EWInV8Lx91bMTrw1muVV4VJ4xxhlPiBYlma0uoA-apjbytvsldv1W4R8Zr9dwmh3zlNidOdpUsK-4QfhYHP4NY4Xbb8XJISpV8RCZkzqc9CcCEgESEHfUl5vWJ5rAvysXwTSBymTrE3UcaRS0LGV8yo1w1CUhRq9llCpUI-JAj8xsFSJ9T3T3wM_d858m1GO2iWMSXmrSf8Nw-By-LBbofy_hh-r85h4GxtCAIqhr4uF-ePqAM8rF2CfZ9J4O-eAwOxtf7KCBpvACEtCThaWxY_ivaFuHe9GnMhZ3f5a9sL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQX3aXswWaNE2i7euBDWOtX_s8m-KXVEcfxBjj6JYuG0s_79X2o-VAjwRGqQ8bH4D0ZqaIun6ZcbEeHjqkhP8GD1EejeDd0N9P9Hx-51dJd3g8HlL6SMtTVwcgJNcLnqTVsujdL2K69D9GcXHkzDYmY_l0hxpUUnHxvqMhatJLmJI-VL-2mOKoZRq1E_-V13cU7GLrhk2wjTPhL_APJF-xFoBJeaCw7GKoMXcE-EJcTp9oCpw-n29LAIodi-hR0TcmU10YtkESBS9C1gDKhqLceSY81zlAVQlMUcERf0x5zGEzN4JPcyRsaMqDMkD1-DeBKDIIjwIlrD8scMjbL0uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان خرده‌فروشی آنلاین و کالاهای تندمصرف در سال ۱۴۰۳
🔹
آمار انجمن تجارت الکترونیک تهران نشان می‌دهد «زیورآلات، طلا و مسکوکات» با ۴۵۰.۷ هزار میلیارد تومان، بیشترین سهم را از میزان مصرف خرده‌فروشی آنلاین در سال ۱۴۰۳ داشته است.
🔹
پس از آن «لوازم خانگی برقی» با ۲۸۹.۶ و «مد و پوشاک» با ۲۳۸.۴ هزار میلیارد تومان قرار دارند.
🔹
در بخش کالاهای تندمصرف (FMCG)، «خوراکی‌ها» با ۹۰.۸ درصد سهم مطلق بازار آنلاین را در دست دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691027" target="_blank">📅 22:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691026">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پوتین: روسیه هیچ برنامه تهاجمی علیه اروپا ندارد و آماده همکاری و احیای روابط با همسایگان اروپایی خود است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/691026" target="_blank">📅 22:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7R9oqY-FcLTZ4Fe5S9vOmC0kFtMuD7KqFal1ttSTn9aAYVXqioc8PjgJi4fpP587Z20lvtF8GLBBat22ZTlwjsRWiB7SwkmCDOnNZ3FLsTr8V_hcN9ZpCnaLCCNnp_p6nFNbEX_evGFZkpRDue9bXDA3LREijz8r9Fbl5rSOc4rJnKBCerW3ygZkDAJFuraKfLzVO6IsMV5tp__DKa3_0mGnO6WVkvMVIKMImD1LAftYOLT7NerIbAvhPgpcAHyE1CwIuOatnXPDG8_0yqk2lW0MQRKRmzkQiLwNndUKNNqxSoKv_ylWa85_mrbbs6evL5T26dnebzNUdDw89NcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بوریس جانسون: عمران خان در زندان کوچکی در پاکستان در حال مرگ تدریجی است
🔹
بوریس جانسون، نخست‌وزیر پیشین بریتانیا، با اشاره به وضعیت عمران خان، نخست‌وزیر سابق پاکستان، خواستار استفاده بریتانیا از نفوذ خود برای کمک به آزادی او شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/691025" target="_blank">📅 22:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac7470020.mp4?token=kN68K7qcT02f1VZRbWbP-h8FSOEeAFhqRYiZxVEyWH-JBnvu7YLGnwb_7ULHLwM1T33XHV7OwS6B4lAzvDQPMdGeOaFeepykKkT4uqKnhj-0KhBYcJqwO9aV9dpKRlHEovAoBCpcXm_mZSUIs1SuRLnudcmQB513AvZDKprSOX2OXwugJwhIjKcikBaz5ZzD4S21zKrGG4VPE-5ebTMCdbAlsCbZPQhxpTiU80XrxtL1_VPuyxouHBMz9s0Ny5szaIuloYXD75IX6akdBeE2cyGHih-WLeS4vu3BKWLqh_pkiZY2sYqHDpq2KhYucyWX6GpIvwnC_WA5Idg7cQ066g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac7470020.mp4?token=kN68K7qcT02f1VZRbWbP-h8FSOEeAFhqRYiZxVEyWH-JBnvu7YLGnwb_7ULHLwM1T33XHV7OwS6B4lAzvDQPMdGeOaFeepykKkT4uqKnhj-0KhBYcJqwO9aV9dpKRlHEovAoBCpcXm_mZSUIs1SuRLnudcmQB513AvZDKprSOX2OXwugJwhIjKcikBaz5ZzD4S21zKrGG4VPE-5ebTMCdbAlsCbZPQhxpTiU80XrxtL1_VPuyxouHBMz9s0Ny5szaIuloYXD75IX6akdBeE2cyGHih-WLeS4vu3BKWLqh_pkiZY2sYqHDpq2KhYucyWX6GpIvwnC_WA5Idg7cQ066g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیرترین موجود زنده جهان؛ کوسه گرینلندی که ۳۹۰ سال از عمرش می‌گذرد/ متولد شده قبل از نیوتون، موتسارت و داروین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691024" target="_blank">📅 22:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4994b7f7.mp4?token=TNgK5O_DscgLJKgwMqb3qtpPb-qKeZb4Mh2Q6Ibm9tgUaVFWmHiqSl_eelsjODINWFbfDrL3BEY69xVxDy2OJGUSCJGg8TcMLaobRocYlbqi6UxHNNcGeMmxZcc2vpSAromUYVc2IIRpZMVLsmhWcH6aZLQJ0U4Pq-5sqK-NeU_EContiWXLtapVz3kERXEN28pFcvnTJ9TuC7T3rMTpAjjq1-yPW0OLHtWvtXpMFZCztyw4p-_aYTnPXxhY9ZCee0ZiDn2pjhiFb2K5gOFaNYNmim_TYQh3bhoq6QxSpOH26XHI2r7ZX4otFjjsrf5Vp0Jk3Twp-SmTdXVbty0fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4994b7f7.mp4?token=TNgK5O_DscgLJKgwMqb3qtpPb-qKeZb4Mh2Q6Ibm9tgUaVFWmHiqSl_eelsjODINWFbfDrL3BEY69xVxDy2OJGUSCJGg8TcMLaobRocYlbqi6UxHNNcGeMmxZcc2vpSAromUYVc2IIRpZMVLsmhWcH6aZLQJ0U4Pq-5sqK-NeU_EContiWXLtapVz3kERXEN28pFcvnTJ9TuC7T3rMTpAjjq1-yPW0OLHtWvtXpMFZCztyw4p-_aYTnPXxhY9ZCee0ZiDn2pjhiFb2K5gOFaNYNmim_TYQh3bhoq6QxSpOH26XHI2r7ZX4otFjjsrf5Vp0Jk3Twp-SmTdXVbty0fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لبیک یا خامنه‌ای
🔹
اوج همبستگی و وحدت مردم در رزمایش بزرگ جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/691023" target="_blank">📅 22:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691022">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1-v3wbGYG-trDD2BF2Q_stJy2AQLGhYDtFIJpe2mfmqmiczkZQv-6-UFbrgUuVfLsjD2t1ebg_26y9wi6jo-Bm43CMr-qvfJqHHz9LcKA0DR4fFN1A0kM6k9pO2gq0WZwv_ocedjdm288zaa18ARwHfx3uRmviuq9rJlk2IpDQ1FuRX2Y0nNVFNoR8Ubk22xVOLDjiyf-0S1JOdXLPlQb3JI25bBeYBTCwibDHcZcPcTWlI-tok5Rs5QXY2wjHSWeWPELCsKIbb5IpqGTVP1Ef0sPRZQWZNa3vf91aN5idRBNz2c1oOjrSlwxqchiu-M_Wc1mTKv0cHXqxgulDDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: محبوبیتم در جمهوری‌خواهان ۹۵ درصد است!
رئیس‌جمهور تروریست آمریکا:
🔹
میزان محبوبیت ترامپ در حزب جمهوری‌خواه اکنون ۹۵ درصد است که یک رکورد محسوب می‌شود. رونالد ریگان با ۸۶ درصد در جایگاه دوم قرار دارد. متشکرم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/691022" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تهدید به «فرستادن به استخر»؛ زیدآبادی درباره مرگ هاشمی رفسنجانی: فرزندان هاشمی مدعی مرگ عمدی پدرشان هستند
🔹
زیدآبادی: اگر مدرک دارند شکایت کنند، وگرنه تکرار نکنند، حالا تندروها هم همین را می‌گویند. یک طلبه روحانی را به «فرستادن به استخر» تهدید کرده. قبلاً هم در زمان ریاست‌جمهوری روحانی، طلابی پلاکارد داشتند: «ای آنکه مذاکره شعارت، استخر فرح در انتظارت!»
🔹
یعنی مرگ عمدی را قبول دارند و دیگران را هم تهدید می‌کنند؛ اگر قوه قضائیه قصد بررسی این موضوع را دارد، این افراد را احضار کند: اگر مدرک دارند، پرونده تشکیل شود؛ اگر ندارند، باید بگویند چرا چنین ادعاهایی می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/691020" target="_blank">📅 21:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691019">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل از یک منبع آگاه آمریکایی‌: ۶۰ میلیون بشکه نفت ایران یا نفتی که احتمالاً ایرانی است، در نفتکش‌های تحت تحریم بلاتکلیف مانده است
🔹
واردات نفت ایران یا نفتی که احتمالا متعلق به ایران است توسط چین، به ۴۴۰ هزار بشکه در روز کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/691019" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691018">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6ec2409e.mp4?token=kNa41A0aZhWPPz8bXRfg1cKSN74XdnOf9IZMQQh1v0ApY0tNc9ISOe1otPfAk_oJqiLVgumIgms6886FLkTupfU_uUmki1hLKoSvcFU6q6sigXMjdK272D60oNZIyrLSD20bkV-nZyvESKkMPEMqXqDPd5uC8e3-x4rk-5eNnq7odDOsfjePPwO57Hp95-1ukVvaCn6bdCyTjfve50g3EnaaK6OfPJvPEEKl7pvJBi-Tby4NK2R78vuF8tEuMF_igyd8LDEvqL2nhfEYYnwAAFGynYLWeNOl7AvEBMd2dMDg4HUQCuIxj6TfcuqZFwDp_faTY68kLtT8dhHYtV9m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6ec2409e.mp4?token=kNa41A0aZhWPPz8bXRfg1cKSN74XdnOf9IZMQQh1v0ApY0tNc9ISOe1otPfAk_oJqiLVgumIgms6886FLkTupfU_uUmki1hLKoSvcFU6q6sigXMjdK272D60oNZIyrLSD20bkV-nZyvESKkMPEMqXqDPd5uC8e3-x4rk-5eNnq7odDOsfjePPwO57Hp95-1ukVvaCn6bdCyTjfve50g3EnaaK6OfPJvPEEKl7pvJBi-Tby4NK2R78vuF8tEuMF_igyd8LDEvqL2nhfEYYnwAAFGynYLWeNOl7AvEBMd2dMDg4HUQCuIxj6TfcuqZFwDp_faTY68kLtT8dhHYtV9m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر
شایان
:
بانک
صنعت
و
معدن
طرح
توسعه
واحد
داروسازی
فریمان
را
به‌تنهایی
تأمین
مالی
می‌کند
🔹
مدیرعامل بانک صنعت و معدن در جریان سفر به استان خراسان رضوی از تأمین مالی کامل و یکپارچه طرح توسعه واحد داروسازی دانش‌بنیان فریمان توسط این بانک خبر داد و اعلام کرد: طرح توسعه این پروژه تا پایان سال به بهره‌برداری می‌رسد.
▫️
در راستای حمایت از تولید، بانک صنعت و معدن متناسب با سرمایه‌گذاری مجری طرح، مسئولیت کامل تأمین مالی طرح توسعه این واحد داروسازی را بر عهده گرفته تا بر اساس برنامه تا پایان سال افتتاح شود.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/691018" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7586235fd.mp4?token=Gf9fjwTkbNCf8yNzcWwNDUdQrks-Syi73HoyN0ZKZixJiG3tgQofqZbFhbaHOFjYyCNEbpG3v-Gu6GWxEKeo8gy-hmG0czkypxdgRhG8mfRFsGHogAVrWHhQZX1Ru7fMhNK6eeKUF1BUyZHYKCKTZhWin1SLFV4VsDod0DymcYkFf-e2NSVS_DM9EY8NZzARtwe0gZNwqyamtT6_g4dvLBn2SXUNCUBaOyhH2UUnvGOr2-mnIDUs2qDo2LH5dr2wY8-NgIBaRII14A551-49ny7UXhVrtJLXj8iKlqi8OCPzCrjGDEnA9fjtU6mLQgowcDn86Qkp0ZBTlfyVi79J6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7586235fd.mp4?token=Gf9fjwTkbNCf8yNzcWwNDUdQrks-Syi73HoyN0ZKZixJiG3tgQofqZbFhbaHOFjYyCNEbpG3v-Gu6GWxEKeo8gy-hmG0czkypxdgRhG8mfRFsGHogAVrWHhQZX1Ru7fMhNK6eeKUF1BUyZHYKCKTZhWin1SLFV4VsDod0DymcYkFf-e2NSVS_DM9EY8NZzARtwe0gZNwqyamtT6_g4dvLBn2SXUNCUBaOyhH2UUnvGOr2-mnIDUs2qDo2LH5dr2wY8-NgIBaRII14A551-49ny7UXhVrtJLXj8iKlqi8OCPzCrjGDEnA9fjtU6mLQgowcDn86Qkp0ZBTlfyVi79J6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تنظیمات رو یاد بگیر چون باعث میشه با گوشی سامسونگ عکس‌های خلاقانه بگیری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691017" target="_blank">📅 21:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d741aca11e.mp4?token=lPlEHrMs2OU0jt1k8S_jBlsVqzXDjrNNSI0yLyVLjc2LcMFYar2eebxsOJdW3mwAYfQ-ZKHbyI3m-c3ShJZGdX8S-2PAmFolmcyUMEZaGF1GIATfGQKxCep1URJp-iOF1xrGnP-2ALMkTFJuLPAeM8T5pRFGNmoL8CbBzjJ7OooYSPYX9znIcPz2cvvaooceZSzj6d3g7Z7Z_8foIBYNe6PR_Ol1BeL-HafLziWSqXeeE4Q9BSEdpnj0CPzz58DwduB8KThKBMRK9XWT-29HkJ-GmYZXoCW68hQaBEEGpKnFtOFY-7w8xDUfLVJfpMGvQ7cuADP-fTDrMM9T8Bxo9oeI-BzFvs0inmd9ZWD8_rhDSK2tukK9QDXTLhvny3Iz_DMb9i3fslBe6zWwu7ZvxQGn3XautWDIlJJZUpAQDtrnpLth8U7PQLj_b0swsAaLi-pRd_KcLl4nZDPoU0Z3m3GPi9K2FjCv20AE3XtLmQweS3jO4JIbqPjzK0VE5Luvhyj3zI-B4SqCALclTiCgKgt0h-N5aA7HyQH3q80dPpeDWvUClt6k7pnKkrxXmkrIXu-UfOrfD-K8oLkpiJ1LlbQ5LG5kduvg2ACIjQjz62u71W7Z5yGYeBu4x6gycxbjffpOnB63rrh2aMkkuQOI3pdS-nyDa7yfuQd247EbRJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d741aca11e.mp4?token=lPlEHrMs2OU0jt1k8S_jBlsVqzXDjrNNSI0yLyVLjc2LcMFYar2eebxsOJdW3mwAYfQ-ZKHbyI3m-c3ShJZGdX8S-2PAmFolmcyUMEZaGF1GIATfGQKxCep1URJp-iOF1xrGnP-2ALMkTFJuLPAeM8T5pRFGNmoL8CbBzjJ7OooYSPYX9znIcPz2cvvaooceZSzj6d3g7Z7Z_8foIBYNe6PR_Ol1BeL-HafLziWSqXeeE4Q9BSEdpnj0CPzz58DwduB8KThKBMRK9XWT-29HkJ-GmYZXoCW68hQaBEEGpKnFtOFY-7w8xDUfLVJfpMGvQ7cuADP-fTDrMM9T8Bxo9oeI-BzFvs0inmd9ZWD8_rhDSK2tukK9QDXTLhvny3Iz_DMb9i3fslBe6zWwu7ZvxQGn3XautWDIlJJZUpAQDtrnpLth8U7PQLj_b0swsAaLi-pRd_KcLl4nZDPoU0Z3m3GPi9K2FjCv20AE3XtLmQweS3jO4JIbqPjzK0VE5Luvhyj3zI-B4SqCALclTiCgKgt0h-N5aA7HyQH3q80dPpeDWvUClt6k7pnKkrxXmkrIXu-UfOrfD-K8oLkpiJ1LlbQ5LG5kduvg2ACIjQjz62u71W7Z5yGYeBu4x6gycxbjffpOnB63rrh2aMkkuQOI3pdS-nyDa7yfuQd247EbRJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهریار را همه با شعرهایش می‌شناسند؛اما پشت این نام، زندگی‌ای بود پر از انتخاب‌ها، دلتنگی‌ها و اتفاق‌هایی که مسیرش را برای همیشه عوض کردند
🔹
از تبریز تا جایی که نام «شهریار» ماندگار شد، قصه‌ای هست که خیلی‌ها فقط بخش کوچکی از آن را شنیده‌اند.
🔹
این ویدیو، روایت کوتاهی از زندگی مردی‌ست که شعر، فقط بخشی از داستانش بود.
۲۷ شهریور،روز بزرگداشت استاد شهریار
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691016" target="_blank">📅 21:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691014">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDbfJmGoY3LmlCzF5RwKjcDpMY_L2iGL8BKgOoyItdPJi9lahZ-P6EEJMQTObWmWp3i100UQN3J3yswAlpNO3YxOb87Ddt6kgdTx6-ci_FR5wIspos1W4kU6uZnAFU1xnGBJ2XGCCYyLpJdQVytKZ5ij4-8go7_B9KsV4DzHwqM_Hxp6125UtWWCz5e4IoLKps83erToEITad4O6VxZuVeBQukohLe5iS83Xpi9bYp7YLAMDN8D6QTqEd_WRAh7_DSM8bRXGH6oHP_6zQcc1JWxCAsVz1QSPqntZNdAAwvRjj2JlL6aXIXn9S0udbeG4cFHHCHZBtSZy8SOH5REyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAO7c7AIlWKzq4xJvoc4Wuk1FK3ujtQMq5cC0cMys465Koo5elpNbYVZsxUX7zSPQ3IZ_v73gn8hmLHxzrLXjkf0lQRW0f23MN135JWJ7ahoB92engN4Q42h6jcgmOmGF09Z9eQtEvstq_Pm-2a9oVnDQNYb4ac2Xjvhc4iTr029cgndVkKEJ8vIh8tPnZN4r6AiFHMGBtU4dfjBQkDR-YRVIKfjiLw_DFSqXzT2j9xdfJ5gGxN1Xpe2orYvC4bxPmlfbsC8P5bFOwmkxBcqT9JN5c2MnSjp4hpFxRI6zU1sn_aMWCT133Kd9YBjJe8tEddil6arWeVyS0s5obSSiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشارکت بانوان هلال احمر در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/691014" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691013">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
فاکس بیزنس: فرستاده آمریکا برای افزایش فشار بر ایران عازم امارات، ترکیه، عمان و بریتانیا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/691013" target="_blank">📅 21:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691012">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e624bbe2.mp4?token=H4pOFIrzkZnSGnMhkPgOoXLpZytKWLQBHbNdTT27Wsq2WEEr225mwHQUMGiUELv4OWFufI2LRFJg_tVtfiThF6WW6JaAD4WYZ1HhnrC4z4tPp1Td98MuDCLvUUpr8PsXk-teRgSPG71X_258l84W_TtdooZXPlTxbHHwMYMYh0Nv2RO9-MObKs7qvZ2Tq9nldGuSoeMn1KGaOMMTah7tcYdV5jt9o_RGmX0Cmg-YOzdLbVaw2YCtzCkWjz7CoBjq4Ohb6agVUAbFjhFNnaknIpZ4sI30mhms0O4mwfol0zoTwKY0c3ZhU2acfAiV-UUS5UVOIXVO2MgVUX5P-FekGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e624bbe2.mp4?token=H4pOFIrzkZnSGnMhkPgOoXLpZytKWLQBHbNdTT27Wsq2WEEr225mwHQUMGiUELv4OWFufI2LRFJg_tVtfiThF6WW6JaAD4WYZ1HhnrC4z4tPp1Td98MuDCLvUUpr8PsXk-teRgSPG71X_258l84W_TtdooZXPlTxbHHwMYMYh0Nv2RO9-MObKs7qvZ2Tq9nldGuSoeMn1KGaOMMTah7tcYdV5jt9o_RGmX0Cmg-YOzdLbVaw2YCtzCkWjz7CoBjq4Ohb6agVUAbFjhFNnaknIpZ4sI30mhms0O4mwfol0zoTwKY0c3ZhU2acfAiV-UUS5UVOIXVO2MgVUX5P-FekGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از نوزاد تازه متولد شده که حالت خاص اون مورد توجه کاربران قرار گرفته است
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/691012" target="_blank">📅 21:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691011">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
العربیه به نقل از منبع آگاه: وزیر کشور پاکستان طی ساعات آینده به ایران سفر خواهد کرد
🔹
او در تهران درباره تشدید اقدامات انصارالله در یمن گفتگو خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/691011" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691010">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
جنگ در کمین انگلیس؟
بی‌بی‌سی:
🔹
دولت انگلیس از شهروندان خود خواسته است که مواد غذایی کنسرو شده و آب آشامیدنی ذخیره را برای جنگ احتمالی با روسیه آماده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/691010" target="_blank">📅 21:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691009">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA2Yb45UJ_C3PN_Rg97KMSNxf0Qs5gbHKRbcQheX8STc3-MQRjbHUkJShS2nCCoxxTEzJgwaZIUgIgKJT7IMYDgqgqk2VEyhNlaG5qT4kwVdCedMKyYsbu2_dnF1GUzf7rY7q6CUyAlgcmsneemGqhrbkte585ETj3q1-yxFCy9NQpGu9fTIxdXXeF92yufU1meYcEiXqKn1akZmxf5XQ4w5TJtVpwpZerVorHfGpm-uzP4_W6hH7LVSQ9-a-M9lHp_5OQ4ExKC544xZAynJDG9j87ZuiHePLB2kSA_k2FKBm6bTMY3w9Xf8ZK1NvJ1SwcPNwZd_0_1RStQ21u6-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام های درد بدن رو بدونیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/691009" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ar24WWoHkI2SFkF7xjyXTJpzQ5-IKjozJTuVzT4kVMHkPjmWhn9UJqsdVy156PBEdDrnge3D0txoM3ZPz2j8-twfvPt6m0giQ8wIQckkCbccvKtKrC-ALQ6MazyzJ6wK3jvMLRJUi1rwa5FurqS9xwVWp7FvnSpilWnfgZvl3CsxneDi8ol6RVdKbwJsni743NCcjstf3BJwKaB2mKSwBSmefj2EiX5onQh2ioH4bebVXf3junoFhQigDzyca5GrI8zS38r0JW4x-z9kmpPK9UYSmdc7l-SLluaMYy6_drmAje7PybdH3Zi5zwqkN3GGe6hnquDLX8MYQM4DKGNhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZCnnQlmrhJed9z9CTu9Wg_MCKxKp9GWR_FzmmHb8bFBxk5DkK14dKB01VfS_h_nAvDGVyq8ORyQh8LNVvnT1Bk_RQHjPNxes22cQo2Dhq_b2nmFikYvjInK7P3DGEnumUtBM7I0E4vOOXkNMDTIUAKTRdZqb-kLWnX5_NQqocfUrtfWb9FDUG4PUQ8-EVEDHaTe6nVDDPw--t7qNGwM8HSrEJH5TFB0BGSdchM2qmsIS-dPGfqVIMjkSjJabqDZ5OW3RBZ-nf_Xwrs9dAkmO-RaEPo73O1Lw8ivIlJ8PbXjDu_3cGuXoAnftV70sU7gnwr6M4EMmRZNAjmbOGfR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5wTr8ut2bIjVTtE4h5yEmdJC_0qqEXWn_RQORSF0lsu5UwsX0uEQ-54uGVwZkL2ZQDw55nwVKFV5XSqo2ijkdwMO6jTFI7KQhVLKucMec5_u1WgEHivXSnIJ_NJSJsv5lZJdnNGh4bYrFbSp4d7RhZ9VHF6DZjHOHz4QUc79ky8_mloze6G08G0Y7Nfm-JAr63lTKTcWwWpCpsvXr4n8TeH9W8yLWzTI8hueBFfqT8DAwgEkqm0rZtHuV25tM3DGdX93DadvalXNPcovmJE2xzVg0ItJ5qwwSu0FlnsHvcizTi-2jjuu9eStXTMt08eTDn0L6eAl6u32tEsAzSuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPqHf5dWXZZw9MirsRb5l5tdG5ZptHXatO1qmP8DzLbqV0MDC1lFWcL1JMpZLTpjEIQynLQHXBjRJ2P2rGTORWaCDwH2DgXolGrqHLLDJKmHFEbUZeIpy8F-t_JI2yAgnib7dzBm_RMcU4ZYV6FpW5VA4Tb9vRrYj-vBX_XouEsIhU62wLWA3MOZEcC5z4mDsStI0Do0d2oLUNzCkYAJaXusy4ZHtLy4KWqzdv4Lz7oIl1I8K8iBx19zZoF7qGthAG4Eb_BfN95627uJDDo3o3i1Kjk2icsBRzHwME3KwlbGn1xaP7qq-mS4QUD4PrMOz31yL-S140MtnHPZZKxH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHiq2hg3mbuU2OQaUSMk_e8S6cYh_Udq2ytiwImRpKXAtfuT4n7aziK2XbUuOn2IPnC_MVIEQJPyjvduQ9BIabXe9VH5MwV8ACGzEC1o_gs_IUBbrmxGIWPlfPIt6aN7xmAqPJIDdVQn7eJrwz5JaowPvIROQeUQ740GIIv0rONx4i_PsX8NRFFWDQEpmuM3A7gSYgU9zKRm4bc1zDfAaf72XOCSo0bxQfNU7QrC17tQ61quSHLK7GQzy1ycuMXBKytYS_kF6Vqsv4nS1SN9J2bK3Vva0h-dwGZCRZ1j4zYLQRM4KrcYGE6XAwFo1Xja-J-PZLfIxoLds0pgilZLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ok4YJzCpIujoAEpAOJwEndTu2Lb3L6S38-ZyFnjG0B-49hY1vyZIcsuUEudXPpDsRfbAMDGBgC3a4wTyQ6xDW-55evHVSyhweLi7ezHYa9fSJycbzgRehaM4vGtWwVRy6HcqZDUCqj7D8zei3gOcFuz2V8XqZJM18qKT9kRoyZubQRYYoSKFp3bQTa6_HqsgfXC-CmY-CUE-9GvK4B6BMKXLsWPXt_4anTrWvcatw3PoashjO0Xw004Fg4UtLajhLCwjL_ks4j1zaXGAZh6VEF-pUwsSC3VAn8RZYdduhv9wvaM1uvXOETIHIYdZkpjxO2k5ZFUxeZq2Rzcqz8I9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1lg_I6V_YIMX57wje62pjNzBgrWQ2PCD527j7wlkiAD393992KHlvmW0Dop4F4a8g-7SG0RYmEVN6Qye_9UB8c5xJ8P2li8W1LoB6PtI1uU94ykWrtLxgc4LtgaJ8VHNBbZ0fcdhgi4KJcQlf3VRWF2tEP0ADxtBBsZBUQnDnSpkmlUklcua5GPSFniH8ygcYTesfcwVtmat0H5EtS0OBbctpNeMlPgRGC2a5cZLb4imInAlk9YBMyRkBu-p-5BbWpFp0_KH2W0t6VMXyC_h1Q8KCLTtT7VI3gdM70EG3FtPjhJqn4GY3J2_XKpC9Z_ljzPqGEatCwyfUiaBtBpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH-npPI6B9raBRc_Gmsbt2FE0KP1tfyFraorbUbbU6K_jaEzVDmCyww0WSVJyf_XdodjqpKu2ERXDL6vwAail44Shb5g7LVfPNch9f72okAH7WFYdnU0WBIneB_Bweh5bB0nVYz2_sRCAMA8owaKPxhOouLvjXTcOfoRUECMIFMw3nOZ9ivz12mgpJ07ejgKEiVTfaKZ2ZV63aIAYELRtKB6zLEz4sPos__8fMTq3G3z8Hdl_JJwiqioNvnJs2GtI0j8nYWJdlVqvPSoW4jG9SIJKJyyzFqvNRISILG9kofmkXE_NnZjuU1tBpOg2jg9Iirb3bwDp0zVpD17hlAiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTM7eruR1WzPlD3ojnyftmJcuWmPozfGd_PRCE3yMG2sf6jOdqBP0xXCb5j2pIBaKePBSMqyLuFda11yris5B7xK2EKkKWk02sWwoKe4PcjNw1kAlYUBlTcsN87DEuQK8T89C9sncE55mUP2BwMmtyyChhxFv1HI_0MxYDf9MQSqI55rMS4MQVDjw3DBgt4Y2soqj3OwcX_eqYid-IdXF_H4bZXo6pTAzu-jMEiGZUnMug9trFX48gwzAa9d7dcNdqOOyinaVtBFHuVCM_mL2YxAzjGak0nFWDvWhMqzrmaWA7S7s4ob5kUTAf_fzJdXXJSf9Wfc07SD0XX9l4qNZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرچم ایران امانت دستان کوچک؛ جانفدا میزبان کودکانِ و نوزادان ایران زمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/691000" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKI7aVXwWW3BIHBfk-sV1U9h7idHM4G3ShdOmd7zmUSt9CZ0E4WIJSm9JX3dcCpz9n94UOpkF7fN-n_N_bX3OnX2tx7rLUplC2ryFCPjsW8w7vGIA-SsE1h-VvhOl461OpngpUzFkogCGc5ztokZruJaaqhmhG6yGRiHnwbTBozhbDnVqW6VmzwGh9flYYYMbBIG6Vltg4H4I3UmKxK4U2_6ADs-QQFf1xz1VvlQFRlj_quRAwTdJ0xJBopgbMKD5zQLtKNB7kgACWrIaRg20iwz27tr6vOrjuFcRMHgJ-iSFwzmGGE5j1fCDCjzDxMpUJm2tjajpW5t6z1adRfvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: دوره‌ای آغاز شده است که در آن هواپیماهای شما، از نوع F-35 و F-15، مورد هدف قرار می‌گیرند و شما مجبور می‌شوید گزارش دهید که به آنها آسیب رسیده است
🔹
آنچه که روزی یک کابوس وحشتناک بود، اکنون به یک واقعیت روزمره تبدیل شده است؛ شما باید با این موضوع کنار بیایید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690999" target="_blank">📅 21:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e616241d65.mp4?token=EZjkt34QwpsSo5N_9njdf8BcKJGaw4RrQmBBmDd6ZjgwoSPtbGwb98pcaBLwviLgvb-AYPLgPlvKoKmswHZUoonkrMWC2c8RuL06xHsxK6srTmfg0nTJLVVU9AlRn0vwF57Ld7bpK6c_6iMZVf2Lrt_G7-rMLvOKPzzYjDLomCJaiyhflY6pD6t1TPKXg6W7oaU4I4pzqscLtJ9BTdA1byabOs51jF8WUbi37119qheNhO2eZgrZZn66piH_PutN0FYcpuHYytW_FvHtOdfeZHKPMreeZ7UgobMJHr9fyTMSL8zzKhbH51E-xwTdcC0UhNBQPbxEUP5vyBmoxZ_mNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e616241d65.mp4?token=EZjkt34QwpsSo5N_9njdf8BcKJGaw4RrQmBBmDd6ZjgwoSPtbGwb98pcaBLwviLgvb-AYPLgPlvKoKmswHZUoonkrMWC2c8RuL06xHsxK6srTmfg0nTJLVVU9AlRn0vwF57Ld7bpK6c_6iMZVf2Lrt_G7-rMLvOKPzzYjDLomCJaiyhflY6pD6t1TPKXg6W7oaU4I4pzqscLtJ9BTdA1byabOs51jF8WUbi37119qheNhO2eZgrZZn66piH_PutN0FYcpuHYytW_FvHtOdfeZHKPMreeZ7UgobMJHr9fyTMSL8zzKhbH51E-xwTdcC0UhNBQPbxEUP5vyBmoxZ_mNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای سینمای دهه ۶۰
🎬
🔹
صداها، دیالوگ‌ها و ملودی‌های فیلم‌های آن دوران برای خیلی‌ها حال‌وهوای خاص و نوستالژیکی داشت؛ «خط پایان» محصول سال ۱۳۶۴ نیز از فیلم‌های پرفروش آن دوره بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/690998" target="_blank">📅 21:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
یک گزارش جعلی هوش مصنوعی؛ آمریکا نزدیک بود به کشتی چینی حمله کند!
سی‌ان‌ان مدعی شد:
🔹
یک گزارش اطلاعاتی تولیدشده با کمک هوش مصنوعی، نیروهای آمریکایی را به اشتباه انداخت؛ آنها تصور کردند یک کشتی چینی حامل قطعات مورد استفاده در تسلیحات هسته‌ای است و نزدیک بود علیه آن عملیات انجام دهند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/690997" target="_blank">📅 20:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJdGeQBYQ1Jex--_-M-t_EcUh7KAMlVvGhqeDmyE_wNSHpMCNJMNEJY0RKQu-YULMDsTm3Gmtttw3rP9Jh35Z2HJHefcKRoxnd3-XL0EfsHygABZ9QhThIhjmfJKLkzNu7SNHO0zANyLcBCWgTbhGbtP9dOgij6otfdy2DBTE2gUe8ctN4vI7XMBuYCtXB05naAwMK6edSU4qc6ZcEwhRq4xQWMBBJ_kuR_blKuX1wPjxGUWiMghtXbKIM5BhxNDrg05RW2g-hT4GtN9qQaKDN2Yt07NL8lNAhbY9Z4DcVWHrX1AMIMP2YtnVfWMFSMzu_loMKuAovU87wvbLIIyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpZ4UR7D7DwgKpSTxNz0IFHSFkhoD-snqkxKMqHkOnjOrRE0ZHu6woNh_QHfux5bTgTMzn3YREiihPud2VnCIZyZC_ftXU22pskiVho-dwuP3H7WcWP2T3VyzSaVBij3u9ucjBRm1dbu3tfREMXkbSrRbZCzpUMSspfKILIT5T09m1h0j-pPzOrTB_aBwOIxXrjUgMvhrGWG0oUr1DCVN4fjW4cusaDdDxk-e7qPScZY8ZHN3KhNsZ8WSXLYuMmqMFQEjJs046YJXbTaE-V_cfGpkKITkL4PVRLblVEXHsd3JR6bttMuX8h6QVM_7HNZiuvAtBaO0LlJ7HqrC0xP4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4179a1b0f0.mp4?token=CiLbjJ25cBxzu4pGQKhUB2MgYadtThZHwIwvis7SXy0sDqJP_HUXm6-Mp5NDHC7sydSoqcv5q25VxDRjOFkQQqWzj8bgP7F9R4CR_MWPaqipeSBSwvdsO1_o4mixZB8F7dRBfejv2MNK-YyxEuzMrVwiV0wnoPoBZjxIORCjLhCimAbiv-3BUEAMm2632dierwS0aVKSkIQYwXMCHE8i-KeF5hYHD5zKBHSSmljxV10aPmYzJ8NdzCRNt1v85bU99ctm9HWuLvgaxHRtaZk-qEfIWR-J_s4Dt5OqcKy9nsXcXtdECYLEmf96hA1V3LOBN-v7BlIGXvML3vue-9dTMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4179a1b0f0.mp4?token=CiLbjJ25cBxzu4pGQKhUB2MgYadtThZHwIwvis7SXy0sDqJP_HUXm6-Mp5NDHC7sydSoqcv5q25VxDRjOFkQQqWzj8bgP7F9R4CR_MWPaqipeSBSwvdsO1_o4mixZB8F7dRBfejv2MNK-YyxEuzMrVwiV0wnoPoBZjxIORCjLhCimAbiv-3BUEAMm2632dierwS0aVKSkIQYwXMCHE8i-KeF5hYHD5zKBHSSmljxV10aPmYzJ8NdzCRNt1v85bU99ctm9HWuLvgaxHRtaZk-qEfIWR-J_s4Dt5OqcKy9nsXcXtdECYLEmf96hA1V3LOBN-v7BlIGXvML3vue-9dTMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد کودکان شهید میناب در رزمایش جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/690994" target="_blank">📅 20:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سیستان و بلوچستان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d58954e4.mp4?token=mewuTf0-qaY94WNXKpG5dBhFUUvJFxiY4u8_Q2PulBxprmw0c0gTdd_-OknaBKpNqyPUkb2uD491o8GpwmTpTrsxIhTzBH5nKL2uTiTN6ofSW7WWAmaOyW28_1nhacoYv374skdDsAMf_LmqRD2BRsLmyLVbbWdxTJQV7XN2lUdmx5ThQXTIfamKSjds4JWGb5ngr0x3Whtvqd7z0Y8GIMNkn0IKBlxaWG-FjmNNZjlJC1y_2y9n5udANliXsNhtbsuF_oFLbAQwqphjnoUOZ8KSKb-GL-oyQWgcM4K78fHvCyx3eyOlyjT-WghbrR_jpoaoG9I53ArCh10egdc31o3dyilBvETps-7af4y3Z9Kbl62uca6FVqWSUUAl4qSOBoos0Rf3eblKfY_HYHErjebRcxGc07WS1cnjdf4DLvGgyLkzb3Yxxe1RF7nSbA6ZsY9ZL1ckfwDLkdgItybDjcQGEL0ERYZUIkK0eqwVY9Rncd0KwgQOg8tcBogpc5Gtp8ME0u80VPkxS9WNTDFWEsItwiG7hR4uz9C_Fxv7p-yp--JuRHnH7MGiC_pjjwXL3fs0aN9M9NwrL7QQQe0OnhMKwWJbmkqlWPc51EdCEgkReJB4PAC8RqKDM9sqpd7VUbotb5Z4kwhZUbtVpaagpF2GbGCrmaejg1u7Ggbmzoo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d58954e4.mp4?token=mewuTf0-qaY94WNXKpG5dBhFUUvJFxiY4u8_Q2PulBxprmw0c0gTdd_-OknaBKpNqyPUkb2uD491o8GpwmTpTrsxIhTzBH5nKL2uTiTN6ofSW7WWAmaOyW28_1nhacoYv374skdDsAMf_LmqRD2BRsLmyLVbbWdxTJQV7XN2lUdmx5ThQXTIfamKSjds4JWGb5ngr0x3Whtvqd7z0Y8GIMNkn0IKBlxaWG-FjmNNZjlJC1y_2y9n5udANliXsNhtbsuF_oFLbAQwqphjnoUOZ8KSKb-GL-oyQWgcM4K78fHvCyx3eyOlyjT-WghbrR_jpoaoG9I53ArCh10egdc31o3dyilBvETps-7af4y3Z9Kbl62uca6FVqWSUUAl4qSOBoos0Rf3eblKfY_HYHErjebRcxGc07WS1cnjdf4DLvGgyLkzb3Yxxe1RF7nSbA6ZsY9ZL1ckfwDLkdgItybDjcQGEL0ERYZUIkK0eqwVY9Rncd0KwgQOg8tcBogpc5Gtp8ME0u80VPkxS9WNTDFWEsItwiG7hR4uz9C_Fxv7p-yp--JuRHnH7MGiC_pjjwXL3fs0aN9M9NwrL7QQQe0OnhMKwWJbmkqlWPc51EdCEgkReJB4PAC8RqKDM9sqpd7VUbotb5Z4kwhZUbtVpaagpF2GbGCrmaejg1u7Ggbmzoo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنگاه که افراسیاب با سپاه توران به مرزهای ایران تاخت، سیاوش، شاهزاده جوان ایران، داوطلب شد تا در برابر او بایستد
🔹
نبرد آغاز شد؛ اما آنچه پس از میدان جنگ رخ داد، بیش از یک پیروزی یا شکست ساده بود. تصمیمی گرفته شد که سیاوش را در برابر خواست پدرش قرار داد و راه زندگی او را برای همیشه تغییر داد.
🔹
این نخستین گام از سرگذشتی است که به یکی از تلخ‌ترین و ماندگارترین روایت‌های شاهنامه می‌رسد.
📖
روایتی از شاهنامه فردوسی
این داستان ادامه دارد...
@akhbar_sob</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/690993" target="_blank">📅 20:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfFQ1ga9Uq7IHlHlw-vjI29AUq3L2cast31NBZqtoTRVDlhwL_nitfeph4LMxJn8iVbVuek_oOywa6fqvIjznQCc0KZDxUbu3W-6a6gcCdYdU9ggeB4faq58YJ0fwGwbwK7oXw_L8O5BYVGIJYcvQ2bTXuJ9qoThgnJfQfc5kQ0oqlJDTxWGEDpicXTulkxOTopjofQKlDLVYUlSQ_grtUOXVzn0CwS9GncFi94bVNhPisBtFENqLTAAyT3FSm7P2k-5MBn8pK54IRMHAKN2IvqbXUaT4JaKqXccEcat4V5r3yqiDSRE0GkIF97yLfCuGVCrdm9gK66kiGascKuAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادداشت کمتردیده‌شده‌ی رهبر شهید انقلاب خطاب به جانبازان جنایت وحشیانه پیجری
بسم الله الرّحمن الرّحیم
عزیزان من!
از امتحان الهی سربلند بیرون آمدید.
صبر و استقامت شما یکی از برترین جهادهاست.
شفا و عافیت و عاقبت‌بخیری شما را از خداوند متعال مسألت میکنم.
سیّدعلی خامنه‌ای
۹ مهر ۱۴۰۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/690992" target="_blank">📅 20:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: کارزارهای نفوذ با هوش مصنوعی در ایران، چین و اسرائیل
🔹
شرکت‌هایی در ایران، چین و اسرائیل از مدل‌های هوش مصنوعی منبع‌باز چینی مانند DeepSeek برای ایجاد شبکه‌های حساب جعلی و انتشار هماهنگ محتوای سیاسی در شبکه‌های اجتماعی استفاده کرده‌اند؛ طبق این گزارش، کارزار منتسب به ایران با حدود ۸۰ هزار دنبال‌کننده در نیمه نخست ۲۰۲۶، نگران‌کننده‌ترین مورد توصیف شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/690991" target="_blank">📅 20:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63097770d9.mp4?token=AMJ-0OtwHrBC-sTyUf53_kaBZVunezfs6JNpbyhKPnlwuSuQzTW5FkhNyaEjNU49IUkg6BCshTJzGZQiS31054zI5X0FsVi8DyqsOfLhOBPn8rjubBI0_X9om2wgoRzZckxk27SUJONdIdMjQZh1chZPMglJzQx2RxzhMi2q8kMza3o7q-o3Ct765ss352tJgx9q6E0MKL0YcH8DBGiGGvpnG1tIFMgSRKagI3S8xa_u-y3CULuXPQ9GUnRo0BAOr7VUbcE9ov1aACpcV_nAyHI3sppVBafQPeWj1TFBq4_e1p8wG21Nd7IWU4T8dOJxxwTXykh1vXqrWaETDtCJww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63097770d9.mp4?token=AMJ-0OtwHrBC-sTyUf53_kaBZVunezfs6JNpbyhKPnlwuSuQzTW5FkhNyaEjNU49IUkg6BCshTJzGZQiS31054zI5X0FsVi8DyqsOfLhOBPn8rjubBI0_X9om2wgoRzZckxk27SUJONdIdMjQZh1chZPMglJzQx2RxzhMi2q8kMza3o7q-o3Ct765ss352tJgx9q6E0MKL0YcH8DBGiGGvpnG1tIFMgSRKagI3S8xa_u-y3CULuXPQ9GUnRo0BAOr7VUbcE9ov1aACpcV_nAyHI3sppVBafQPeWj1TFBq4_e1p8wG21Nd7IWU4T8dOJxxwTXykh1vXqrWaETDtCJww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از شکوه حضور مردم در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/690990" target="_blank">📅 20:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: از زمان از سرگیری محاصره دریایی ایران، مسیر ۱۰۵ کشتی تجاری را تغییر داده‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/690989" target="_blank">📅 20:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e096ac356d.mp4?token=tckhzq45rkHRhd3hxCsqvof_xyXLdX45YgqXq52hko-_L6IAA_qWG4RJ2wZ5FVINEJXz1BISe96c3SIhJI-LC8VXn1spBJVYPM5nk5hD_ZWm7ct510csbJEXjBzvs-XUJ3ipCFh-p9-CxxGfftQvfSfffd-Uz9pOBYbj1CoztpL2RqXc26lirnFZqxVUjWPjIb8HIQvw_trwJ2T2mzxMDRj0aR9X8ZkoZEWEzF8ec7C1EPBT997tvWXnEigm2BlxFu-esIY6AlhoaP3jwSx2xz2IXA6LcFmtBnb_bFJ7WGaf1V4nUuUv4wa8r-SpzMZuCPZ5QnSuxUBY_TuvDAB4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e096ac356d.mp4?token=tckhzq45rkHRhd3hxCsqvof_xyXLdX45YgqXq52hko-_L6IAA_qWG4RJ2wZ5FVINEJXz1BISe96c3SIhJI-LC8VXn1spBJVYPM5nk5hD_ZWm7ct510csbJEXjBzvs-XUJ3ipCFh-p9-CxxGfftQvfSfffd-Uz9pOBYbj1CoztpL2RqXc26lirnFZqxVUjWPjIb8HIQvw_trwJ2T2mzxMDRj0aR9X8ZkoZEWEzF8ec7C1EPBT997tvWXnEigm2BlxFu-esIY6AlhoaP3jwSx2xz2IXA6LcFmtBnb_bFJ7WGaf1V4nUuUv4wa8r-SpzMZuCPZ5QnSuxUBY_TuvDAB4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: ایران شرورترین کشور جهان است، خیلی سال است، ۴۷ سال نه، ۵۲ سال!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/690988" target="_blank">📅 20:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اسامی شرکت‌های هواپیمایی ایرانی که امروز در فهرست تحریم وزارت خزانه‌داری آمریکا قرار گرفتند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690987" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ty347jXroadQGFQB2b1MpCpfI2jvfhuwaYLTEM6tEsH0zV6AV_xfqiZVUQrV2uc-lxPr7TNk81JMtxhX0Q04spYZ11usHviX5umFZCvNTgPM3l-hssgf8KnkUMuG72Xrc2ze9QlWEOij_V4cxxziorMpK_d3agKbTuzHEz7aJC15GUAPGZ0ZmpHu7W9T5MBhwzL8VeyWZa-7z9fRoa2BNLQziC3nvH6fMb0tUnPu5SYfJe9HEaWyX1IXZYKkfJs_499O5Zu9yz7g0advPWgaNRnwWDnXP6pGhESs7VY3Gv5qw1wOoXTEjVBrj_V3j47QwZZ9g4pupNt2oXFyKIrQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkWNvmcfl8hzaH1ukYV0_6Lkei3lAJ5j76a0pA_F60cJM_O8WDRPzv2HE2kEsvQ40pSrqzIeHvHTmaopeG2otHD0xp4hVeRURLpYBdc-PdXPouyDS7pl6S__KFF4ao7bE3VAR0MxaHkwAnafd_diBjcXIPvBOchpTU5pT4imig5ITrLzVAJhE6ctAaLmR-NBVoOAPkNXlCUGCH8CjeVkFm8VNCqltdpYHUyZWFMzZCPUwAtn3W--5hUbnXwLlRiv0V9vbCXozsMLZIqcKfFgoGwaCrvacFTtSE0ZiE9ZpfKVR2fmpHiwkdVU_Q8SpKtB6rpVKAE3w8alrZvtmI_Zqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNzZ0ESgDrqqYw_mnV38AE4xhvVdtmbwYGhubAw04Qw3zt5dIw60IGi8m1qg2m--ck4mfMAiI5Cu6V_42DKxG0-SbM2O-433Kz5dSlRr0jKsNMj1A5f46zUtDkGJjZgVKU3T94beOjkKKZPuBnXNsNoa1FFmZwUCGCXm5JMTqCgF3ZcBQZ4Yf8_LfzePzOBOwqDy5DLVcOFnWfjhlZnyxEsdtmLc-JFlOrp1NvlrIwSe8SmGNGvmKziPm-ND_7UkXMjMYYkpWQW8D2srlpJypzywxOz3N3J6Ud2lowMgQhfT_2y8M6JUABeqzPA1FKYBHm8Y6cf0su_gar99cwyUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6mT6vSnCuyBJANNdSgV8zb6JPDUwrl_4fOGiZOzAOK_HdrayM8BY0abrL_d1J1Cez_nv53PvvfhAEls9eCN5600BJMCokOdH69f2GefOp8GdtUyPpH611Q3AXTOGK5m0Q1t2hmsgu9ogU88FF8UuJKjhptczPsnX29z8UPL8rxBL2wcgo_AD4nYhcX4lEDHU-4lQVqqShb9Qo7_F3mMl0mf43aV3OraHzA5mqZWsXuBhTq2mgCGnazjvbwStAfpFa4kLR2bq-1Em-9Fe3A0y3EhhPXfsUUNcne9jWF9ZNc9DGadrixtkDCE1w2DwudbbdfvdTAj6755xTT5dK8v_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja9jP1Mt9YWHn--9-8mmnrRJRjuEGf4qaIvxchu3Lc4rndAQ21Vq-2jGLohT9mPz-nxMmSiuppgKQG5Y7gfNWfhHsnJRtZaM57C7V4oQRFwi4Ci6TN4kKj0wAMA4stFUiAMRhMS2FRgN0wRWsji84Iy-Vp5PhnK73lZkwxVdjwZ5uptoK0hQlu5p_wdYNHWsK9gqj5D957lDJWkAg0GdWxb0l93fCuQFaOX5699FlfCw4bT39C_8NqxoENtSp0_-4gWEpOOGt-5NnAQvhtjejyD7K-0Ct1Y12CdH7xHRDnyW6D6Mqx7CYYeEpvELFUy8jhBujOYW_JBasSp3axwpVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیگه خرما رو ساده جلوی مهمون نزار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/690981" target="_blank">📅 20:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdw7DCuWa-EIu2ijSypHDgEMpQwyWfTcT9bn_5VIUVlf1vfdHJf6QbotaplvPIuYitdOiYjOHkNB1JnVLZD1hMWNYeEaeWZTMZ2sFLWEBxxAl7dJMg5a0ySqe8uZH14Iivrc2mB7CDLk_KbBzuoAGjI7VnDtXwoESXg7q2su1BCBIJVziq6G5awn-3h6vqG1rkS4fuLqH06BrKvsVUkRnl3JvmSS9QqCzUsRUIZGpz1c7haXbym-PNZrPOJ9cEnMBPsk0LtnPqm7ewVcnJ6-5lDii0rtDdZJxodNgZUwXGzDsdfabLG_DPs5otpfQSUfKvc6udnchltZv23YZmmLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد الشرع،رئيس جمهور سوریه درخواست عربستان سعودی برای اعزام جنگجویان سوری به یمن برای جنگ علیه انصارالله را رد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/690980" target="_blank">📅 20:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690978">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUMiOx93j5VQ42-6zgZEJnmtuXJAUmoHqfsGlotkMZoqTzWdybaiEJkjppQ6DcNX0WwzHAI_bDXpJXv_yWihpXW_bwhdZaav4f1Wxbj0swLfxhtx6AjslFXzMzJpYD5xMv3Xe1dAPSWbO912zBI5LCAQN2SYdFg5QAKT2TSZ0trRH41rHw0YuT6eIA2vulX2MKSezDKAOkG8j8H6qpEcnGxcCw2kDZq48wvSGFTVDAclgxV64SVlRfZbMuVr8y2LXrbz5VIQAjHpe5IjeF9Ld9XZNMxMPMcTecJzCz6MVTMdeFr9Ugm5ESqiSzJEZaHgMYrV85CQp3quDzPYQoNSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iquFqaLPjy2yCa7f8WIG7cea9Q2VnpWfsIDKr0JJhqEECxgUNwznL0IpIIKjMdq32acBmkcFOkx_DW3znWyuuSjw0k0j77SsBjMgCn_N91k_1_O5idLH4hVfIrll5c6Fie_5kY4dSoq4wJpjDNIVJMG7M0hBpRs7KZGrWHZIjmNx84FNViK9yPrFnKISnYNOntPZ9X5b5cdHSuJnyxaI76kHUlCNqWTIplzdagkI6C0Ye-Hvf5xUfGcakFmBqW8A01rpHYhpJJAQFDqJhYs6xWVBQccjfHxfol0Ch_J5AnrwYXzS6gG7jA92huB_THdHQuaEIdY03BajHM4zazWXrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم دو ماراتون در بوستان ولایت با تایید مجوز استانداری تهران برگزار شد
🔹
درحالی‌که از ظهر امروز تصاویری از همایش دوومیدانی در بوستان ولایت در فضای مجازی منتشر شد، پیگیری‌ها حاکی از آن است که این مجوز یک ماه قبل به درخواست اداره کل ورزش و جوانان استان تهران و با تایید استانداری تهران صادر شده است.
🔹
در سایت رسمی این رویداد نیز، «تهران کلاب» و «هیات دوومیدانی استان تهران» به عنوان برگزارکنندگان معرفی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/690978" target="_blank">📅 20:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690977">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
هانتر بایدن، پسر جو بایدن: اسرائیل از حمله ۷ اکتبر اطلاع داشت، اما برای جلوگیری از آن اقدامی نکرد؛ جنگ غزه شبیه «نسل‌کشی» است
🔹
۷اکتبر ۲۰۲۳ روز آغاز عملیات طوفان الاقصی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/690977" target="_blank">📅 20:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690976">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDYJZTCsVJS6XRZzAAfyWoGP2U0SBWPq-b2NJi2SnqEHkOsX3A75vRJihLk8s1SvruhyIMZ2rnEB2bjlKzaCM2FUuOzCMBYkvY0x88_lMbplB8ozBk1aVLZaEMVCNQoSWufWsdHQzUye92_0NVmrugxd0bVH8kRq5E1r1hs461TTo0uEEaEpI4QEDqynCFxEZAKr9NjgTWUiRexzFzKVT72HIGcEYyUOOV4Fb_-5WTrzXBz57x7mJq8PmwCIbE-94vPclr40MCrcz0i6iDaUufzulRMtqYDL8v3m-CBMOqQ4oBbEZ05JDrioLqex114bn4_EbBMlsp3j0DmME3iMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ کشور به‌عنوان اعضای جدید در شورای حکام آژانس بین‌المللی انرژی اتمی انتخاب شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/690976" target="_blank">📅 20:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690975">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای ترامپ: با حوثی‌ها در حال گفتگو هستیم؛ حوثی‌ها نیز تمایل دارند به توافقی برسند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690975" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای ترامپ: با حوثی‌ها در حال گفتگو هستیم؛ حوثی‌ها نیز تمایل دارند به توافقی برسند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/690974" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690973">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c989965e.mp4?token=qizsSyo5NCElKBkGySsH49CP6DQTKP_3c-aU_wcbZPw9EkjMq5fe_ElGqLbVD-tTKT7i728el7Doz2hvws_ct1tUR3tXsveTMxkbOpKTcFBimkDAUyidq0zZmabfK2NlGZ8dX2JldG8uwR60rTYdvJ9E_6dE-xwrLvt8Q3k1wxwyk_bbxgXQtbDCxQ2b3nFPHYowcGfTz7OgFbhbWIREgu0oGx5YFNuERkio3DrrT_xvaU718CiXOmxRcjz2T1KPEU4WR1UGqjyrsbd_AmmITZIKUzxirFjnpyCC78WjsCwtVez1DEBAEdtxyTsK5LiOzVil9OwE-tElOxzt0hHm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c989965e.mp4?token=qizsSyo5NCElKBkGySsH49CP6DQTKP_3c-aU_wcbZPw9EkjMq5fe_ElGqLbVD-tTKT7i728el7Doz2hvws_ct1tUR3tXsveTMxkbOpKTcFBimkDAUyidq0zZmabfK2NlGZ8dX2JldG8uwR60rTYdvJ9E_6dE-xwrLvt8Q3k1wxwyk_bbxgXQtbDCxQ2b3nFPHYowcGfTz7OgFbhbWIREgu0oGx5YFNuERkio3DrrT_xvaU718CiXOmxRcjz2T1KPEU4WR1UGqjyrsbd_AmmITZIKUzxirFjnpyCC78WjsCwtVez1DEBAEdtxyTsK5LiOzVil9OwE-tElOxzt0hHm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانکرها چطور کار می‌کنند؟ چگونه هزاران لیتر مایع بدون واژگونی حمل می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/690973" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyzPLkxyVN0cjSU7f1RRWRxi4IUJ4HFttkzhp1hxZwIH-qGbEu0IxghTM5A3d2GC5tuhyvGQ-bgAmL99V1Js-sCxd7EWLEILJYRotF-IOvSDyolmZ1GXq5YdrU7WGT4IHck2kMMc5b0y1UufE0Ee66Qf9A6XHx_pPOHhnKiaVoQhz2GD75U1i_RbUSl1zdAXG2ImQAQ5MrRdwaQsuM_KsjLTOtJk7wQknylqMogO12ijwDVe-g_t_E-fYG9JgVZHu1iVmD5Kq9zUVLJAXb716lcTnOD4FX-n9QD-MXcw8dpvv-VNkPhh5KNGOhHIXU_toSF4nMz8oCVEyD_feWqNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q77HhC3RGXvkCfy91D0znN9OIAI64xmNWszAVy3gzVxz8qLeQWvd26ZzEYS5R5AHlarZ177IheaI-Q2asZL63bNOKsIeaSPk9wqTTQFnJvr8QezNyO4kbZo2iUnHdat8FmBj8nM0S1rT3I74s2Ko3qq6CKS54TUYlEKJubTzywiVv8LD-QYxD3zXY4fXfROfZvLszW4sazz96DQgFPPERy0Ns7KtQM9pJghHMwrCx60f6psRjrzlf531555vNCE1mVJt8ETLKpHpriv9a6FhgOFHcqEYFv-Euu_Vmod6lNgs0Al7XfHTtt1bXhtJlyYWdO6jee-DDztlrxfSewqtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oha1pRyOwlEzwMIuPMBjPUbNPLwmzWeuXh54MP0Pd9iYQAbQCjT9_NPP6AIoLWoV9xj8b1v92pMFHS6qAQeKJ7rDe6vY8ZqPrxjQPPGyXQbEbcRNmA9XNDegsMxjCyYNkU0LW5ozfs2XtIBYSll78WnEbg90wnZTyv1ZLZvU6p9YImnU9A3RVTr2QCVl0fEdbUJN_lhvs7uqF4i9tEs50vQqy0CSfCtZQJnpOFsFzjgEqvtxxYGTNPS8ZtFUHu1LxcVRGeZ-chjP1Mc9fGIVevMxuSIZ3IoL1XcnvkQV8JmBJmJZKsce1b4QdtEN2k3eWh7G9Ty-kg95hzZI9S9BLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQNZB6EQ3DgX6Oz2eFa0MtIIXl5Ci5gJUMskMQyBRKlCB9YJSEyWb0acXeYHl2Q--lB7zu5EbjyIbt_984Wsgxu80MPKaH-Tvc_tYm800WJ6I7SCNt5aSYQb7eukNVBOmendIR2KynuF9dL9aILqdd_PPBoa15ue1R69hxye69K_OhyrQc4zgrFee9hYkES8CkJj_PGWTwJ90_qqkwS-A3ydp8oiNHlDsKvC9zRvsiC9s1C-TXWWVJzlvbCLpiu_ygUB4ZX2fIioodFhy0gcefPJzmRBDqHxID1UbdcSNxHerzKe4glQ12Y8n9xVENe3Tu1R0j8WU4m1aN82KdWOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVtEWlyPO3FC5A3JQ2uPWG4vdma9UILPllXoYSNiARmtKywXbEJS6xz53OHm_a0zn4FL6w5--YXUra5_cHtUPCsr_xcRN8r7pSvvyCXQAKalviOKjGcr5fdEoE0kCG-OsLBhP8qXOycV3uJfFlF5-5JWf_s8ASmOiTxsH7AtUTxQBS2bsL4wxRXESnnK3RCaG7blJrUgFnsvoo5NtALAgMxLia9UsSXKMFtwWHOqfonFqETj2C_Cv9fK5RZlFqcY2kksFpjbvHEYTknLKBD_bHkrjlFyYIVyOJort1YWPdS93HjsakfqPlhxeolxUWKodgMUFCKbpV7FpRyyeQXv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjAc7FKDI_pcC6ArL_KZ3gcm0lr01e8NVULj86wJKB3Z6KRl5I9Hwsz6kd37LemgiHmSjsHba6Fyyhvg6kNWvdgH2rr_VDYMz4E_yCiEIqDRqHjAyAOvkhcd-jfrNb11peDccWNiGVQy0-xjCSrkgD8uxbilu0Gf2fNeRvlw29UDswCkm9swcwHHm4r9XNqhNKcz3AEzj8e6VBZeSAltn1-w3hpgtnJxbPgiW2T1dcsqd_alE7w9tHggLApF3PAND7dVDQF4FZKryMMgu8Pvy-8yZ-_vhLf7ppJDAratv_4qeDzA_xdya48xjwL43E20vSNDlExlOfb5ot_M9H_hRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNg3GKRSHUJIMeqVU9ZDIVcMmWrY6TBMUZ0UF9o5sNdTPkSv-tzmG-Z8-bGp1Zj75HA5Dbnn0Rldoqo5cPkAPjYbxwCr2l7sbT5uwsgkuE-nw518hrU2qE55QXzF5OLarYYHHeIpFj5-i6VaQ2Obo9WmwpWmNA3AKAuhKV3AQz29g653pbuv3oZFs3Yd6F4Adp1gqo5ODH8BiOFgHROZnUWLBHya0wjfyJuIiexZoQx1rNQR-1BfUrIDQc7m0L0QVYQgaRGOPNQQvT86lWGyLJflNjNVUMcVa6VP43Q-A5N5ux-HDkolFsDle8un8w_dmbFykjM7LLsjvm-XwCBW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSmFCdg8Qv3fH_4vsR1Oj-EEwdEwqrpBaMFXeBnX5ipvv9gFEDj_-bltrXJWan8b704K5wD62Pi6nml91rste_MoyBqVVnEIV3m4xRye7NwN85mH2ZOLbjd-zi5P7GIfjbRdzo8NCL_6fZAmHZR1bXkLolr9qp2zoOOLrf-LQqRrXV584ARVE2v7Ga4PvOobBVXosa4sCBP2cV8BVv7wQg3kH19zXDbz9K3W5Mf9RvMl7Zi2qNdOdTMAUTTJINcutzgsgY4ZTvT3sXd0Gf1HnlQ4i107YcZMhJhA-GQXsIUzZA74RXSrXCPqizjje0mXGeNpFMha4CAHOsM9wujBsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور خانوادگی اقشار مختلف مردم در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/690965" target="_blank">📅 20:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ-7a3_jUNRQ8ecfjgGIazmmyfZ-JkDkB4cAOegrG5mwgkdEDZpmQxTWJo--s11MZTVDCaWCFtO0Ydpt_pANVoRFgWyW7j7m1_5IHEU-6OFtRGqmgsptQByQ1XV6MSmc1W1RitLg1e4XHnnaHqJ9cfCAU2KzWp6rLh4YV8dNA4hmG61sw_1LHv9kg61uooAm9TpYmyjfn-i-7e7ChCmIn4jpn9SXSCNxe25EKvvhHBr-8FMnhgwa6C9PDtQ7PedmNwBZI9S7aMJFivC-9tkGQ5oSIQf8SF5XJOUYUA_1MrnMPRJ0ePhA_J4VUo0Zos01NqMDPZIQqwF0UzOXbG7KAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعات حساس F-35 سر از هنگ‌کنگ درآوردند
پولیتیکو:
🔹
قطعات حساس جنگنده F-35 که از استرالیا به آمریکا منتقل می‌شدند، به‌اشتباه به هنگ‌کنگ رسیدند و این موضوع به بررسی کنگره آمریکا منجر شده است.
🔹
گفته می‌شود محموله شامل کانوپی مجهز به فناوری پنهان‌کاری بوده و پنتاگون و لاکهید مارتین در تلاش برای بازیابی آن هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/690963" target="_blank">📅 19:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe19ff3eb5.mp4?token=qpHK8kgIifzMdWdXgYbh8YDPfH9V2qoj8Ja2TCFoCxmpV_l1b0tG9I9BTQEUD8Gp0cMOmRRNDRnqVAQDl1CbsTik9_aujC74IZlWBBstmfELEog8A29GRdEAYk9fI7TOJnYO79BRAj-AJHo-Rvkb7mODbeOFh1E3ASc21Jw1YUgn7ttjZu8XOdbeo5H3CncM1fJL98x4yfamzJd2OK7EWesPgz_ykm45f14ozHv25DmvJSDy5-55sS2UnizJrRt7SorhpGOBr3UZAvjDgQb4JTZlCi0pnWiQyJmyxbBZ9-UKL6TGz5-GdOG82VktbqUdtmc8LnNQf3SJ9Bv3GVxxyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe19ff3eb5.mp4?token=qpHK8kgIifzMdWdXgYbh8YDPfH9V2qoj8Ja2TCFoCxmpV_l1b0tG9I9BTQEUD8Gp0cMOmRRNDRnqVAQDl1CbsTik9_aujC74IZlWBBstmfELEog8A29GRdEAYk9fI7TOJnYO79BRAj-AJHo-Rvkb7mODbeOFh1E3ASc21Jw1YUgn7ttjZu8XOdbeo5H3CncM1fJL98x4yfamzJd2OK7EWesPgz_ykm45f14ozHv25DmvJSDy5-55sS2UnizJrRt7SorhpGOBr3UZAvjDgQb4JTZlCi0pnWiQyJmyxbBZ9-UKL6TGz5-GdOG82VktbqUdtmc8LnNQf3SJ9Bv3GVxxyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماده‌ای کمیاب از نهنگ عنبر که ارزشش به ده‌ها هزار دلار می‌رسد؛ چیزی شبیه مدفوع و استفراغ که در ساخت عطرهای لوکس استفاده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690962" target="_blank">📅 19:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
یحیی سریع از ناکامی توطئه سعودی‌ها در صنعا خبر داد
سخنگوی نیروهای مسلح یمن:
🔹
تلاش‌های جنایتکارانه دشمن سعودی در صنعا (پایتخت یمن) که با رنگ‌وبوی داعشی انجام شد، ناکام ماند و بدون پاسخ نخواهد ماند.
🔹
هنوز مشخص نیست که منظور یحیی سریع از طرح داعشی عربستان سعودی در صنعاء چیست، هرچند برخی کاربران عربی از کشف و خنثی سازی یک عامل انتحاری در تجمع امروز میدان السبعین در صنعاء خبر می‌دهند که این موضوع هنوز هیچ قطعیتی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/690961" target="_blank">📅 19:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690952">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvMoEHFCSqkaaRL6iYBvcIAFSpov7_yb5P6uJdgz5dq_Bko4lIAAOqSu9PZiP2TwaVSLAWqBEz7E3BrfW4VrtcRaLf30egka92KYv-LAX91HC8xDCvB-dYTG3me3BvM2lhgHPVnXL5ZP73-iS3kvewzfLmgnSrlOfrb_7AC5MbnfWE0gIdaX0B0s_EcmbZ43JFaY0KsIssYSct18F0av17fwpG7EoXdBfSFsaUyKi8wY0NsuUAGxE6eWQfg2dFQDb6v2ZGZdAOblzaVXKjlHoSu_2EC8huesUofsm9bI6W7Qa0QL7hQOAifaPpMHTCrBILXdd_dYwkZvKQ7UfJgKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ztb1CdKhacWljUUBPhc6bBk92A_D8w4Jby1CQP_WzRyQGzQ5RPtczshaa56gT-CfsYnxTsbAu45yFzmI0bw0RS6VMz8Ex7rbEDJfybFOR6lqDc-DsOAEhXRy-vpKEbk1M3yYvIku0WAps_MA65GtDkkSN7BZKK_o0szAX0lBslNgMCUDNhywifYgMkWAOV2VEmHqO8ZgzIephskYgKTjv6hvuogMJ0ZBHXERJ5zv7kDJ4yLLJb-BvI-UOW3w5V03bI_v63QvqchndGmLrlF3WxlPhHHSN1k3GHeXbuhrFBfnMwTglzY3tdJ8oMJBPOh8Q_zN077XESKr6e6fczRbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJeIagX-BhuSbIO3ixABZTWrAjz_X0CAoD2hQVxPVW_nTyPDsRd--Zp6Ojn8uhY9LnWq9Ae4ufIdIOYM7AYbFLTYewxK50msBPkcWSxGSpcB3qGPASg-2xU2fi2PnfLlO8jdWs9tlz99XLVNrC8DRPO_vu8K-QiA7lOIvimjtpazQlD-jpwrQ7vQ1tvVPuRVGuW4M6QxTeu53s8aDxPA53OejfYvxXqFONlJ7eWQvXRk365vWYeexQq1HNlEZ1NZpt893mwLR0iiCveVuI6SV_fw2wxZBnW2VeLmb7I8Jd8X1zDWKNOvDvd_nqcD1W3dz0ipMc-v5G4YkCeDXXZu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFNVsGZkND6brNTAWsfKAm1SsMZyXagZn0-VfmU9SpkefcPRxWVQsPQN1JbsJu-j9w_u_wyxKwcqdzEkmcWvz4l1jjCak6hY2qGro1JMkOjecsDrmsgZDQVL63ZF0isSuhFBh_7E6kfNxIgmXuePLL-VVZ6uvLri93cbixOWRSwuuCu9FxTr6gt_QLngFwqhffq6uH5hQnhjja47k0yAab-xSTgVGWQ82W6b2FJSNZp2ZuFVRferhGkCsD_XoQRmoTprfaUVaDtdAd2qhxA7hlDBTv0T0MwaLQ22SyvpWDPNWP2oQQ1uvHo0QBUTZ1yYmx7BJGr4uTxHdv86zQ1_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XExpUCRxEhLaBk19EYkUCm4NnEHE11Usq0zmnTCyaTFxhnLWT_PbmskjsasqWD7eeCWyAe8h-FbnXu7v6E4hLTm4Je4qvNvkmUeBaaz3lO7Qjcv_nHA3TP6gPjrVvNY_cCK_HIXrNrJMQmwaYGxO-fy2Lsmf99wMgTEauzRjIioNCkKA2v59WGB9SsHjobUBdvzdkWOr5nGALSAqY5LqwV5GfSMpcD0EVsnUswBVYP_EhNnrkdPjd7EyHlolHO8yZrfRHqwRxt-YFpDvDIvKuW8_rWtvMHXfO2tsk_QhGZiHU_DWYIbwzUCxPSL-cVllm2_hgzbV3DLxb1zoUIAmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GH6oi7liP_5ASP0mhLYsX7dr6Eow0QndsAbMKlEA7PaOvVELBhwnqMxNPL9lPexmvIIrvM4a94bXZVFH7A6Vwuh43coVAAUnpp9dfnK4CW1el8kAxZ3oGbj-7x3jSGCEQk8WZCuoeBow0EP6Ng6X4E7lUAMu_56w1LBk4NmBGQDU-maEcLPAhw048Y033Uc-3u1BHI9Q2JjdwGTzC4b4cHtytjwaokh046zoXZA81HMlqLZJD4rnRlMO3Z2xfREWWgZbrUgtlhFBEZJz6a8Bzst2P5PFx8zsht1vdwkpfe0SYsq8Fleq0Jrp1b3b6JDdULeZvffnsGEmvSgfAaOrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYyY4gquvwEOlkGFhjd1XcOPp3TO-ry4y2WOhR-yFnYK9Vfo53XOmUefCV3ge7bp1xmugd1af5BqPac-7YkzO_8nr3MaYqhC3paEjt3XgrXbIrY0nooshGLPS_GcR5pNAGrohySC6ad9aGAizQwTOyU7YIzxIyEqObHWLyq49_hzLS3ScwZanwsBYd6z0zv8ZPtmrjI6lk88gj08VBcqWNa4K3UuH_82PKo6joOKQlX6C9oRsKP6NFa3UC1hKlmLCWbttQ23IzC6n2Yv7DBFcbLcbRox8qKKtpVlyOGuA2N8A2YusfEyHGNrwKj-nM_aRzpPxQ7uYGBkgCx-Zpa12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4vCLCpV_Mud1n_1C6srJDsGjqTSzceuQD8B9Wo84b_wBv7v7Abpq9uiiiuOoelhn9uBSkhV0OpYjYs_4sXV-jjhKWJtBVrXPQFb27w_ZOt_oCtCX4Ky3nVZNH4QBG3dqG-ee-agJzXIalKBdhYCvKD5LAKCDmURzTgwrw5He_FA393yGA-srYWmjWW6hKGHoVuN3ADDTIAZm3kBWpAJ_ESWfxACBxaAGs59xgLiaMEKBPNhJyNzsprnWUcpOdp2hZKB4pmRJuUAA05WsLg4dtoGYXUn-qAa9YfmuYnxP4ki2S_D6JuTT_sNnE3Y25iQvgn0LtUcyY0qxH3RCZgIuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07146f6366.mp4?token=iEzLA0_iq0Vz-Q2D1Phv3xSJfFLSJ_UFJRhkO8YJKT7k0pi-zdFxzS8JdBbZZcjL5cF55VFw8l2e8uVnYPY8guXstwZAu6diG5HnT_6RA4PKtH5FAMVunR--olWB3zWSfCCa1GmwTtBqTvGKjsmN5evLZuogM-d3vieLyPOZopI51h-3OFCkqf38NHrDDBMjiy-ijlHKOupG-NuuwTr2Yxnpo2aiYOW_T4cwrZNb6Cg9kmTQ0mDLk-0VZphC3NJJWVcu9CMEZlYTHc04k1gAcAars6nRw7JClf3LrJqgLke-o076VFxTfpRLjL3YtaGclmgg2XYP41-OlJtYNNnzog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07146f6366.mp4?token=iEzLA0_iq0Vz-Q2D1Phv3xSJfFLSJ_UFJRhkO8YJKT7k0pi-zdFxzS8JdBbZZcjL5cF55VFw8l2e8uVnYPY8guXstwZAu6diG5HnT_6RA4PKtH5FAMVunR--olWB3zWSfCCa1GmwTtBqTvGKjsmN5evLZuogM-d3vieLyPOZopI51h-3OFCkqf38NHrDDBMjiy-ijlHKOupG-NuuwTr2Yxnpo2aiYOW_T4cwrZNb6Cg9kmTQ0mDLk-0VZphC3NJJWVcu9CMEZlYTHc04k1gAcAars6nRw7JClf3LrJqgLke-o076VFxTfpRLjL3YtaGclmgg2XYP41-OlJtYNNnzog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم، سربند و دوش انداز جانفدای ایران بر روی شانه و سر و در دستان زنان با غیرت ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/690952" target="_blank">📅 19:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690951">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
هزار دلار پول یه باک گازوییل در ایالت فلوریدا!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/690951" target="_blank">📅 19:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690950">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پرواز استاد دانشگاه با جت‌پک در چین
🚀
🔹
یکی از استادان دانشگاه ژجیانگ چین در جریان روز بازدید عمومی، با استفاده از جت‌پک به پرواز درآمد و توانایی این فناوری را به نمایش گذاشت؛ صحنه‌ای شبیه فیلم‌های علمی‌تخیلی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/690950" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690949">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
هشدار تب کریمه کنگو/ رئیس مرکز بهداشت یزد : با شناسایی ۷ مورد قطعی ابتلا به تب کریمه کنگو و فوت یک بیمار بر اثر این بیماری، شهروندان گوشت مورد نیاز خود را از مراکز مجاز تهیه کنند و از کشتار خارج از کشتارگاه خودداری کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/690949" target="_blank">📅 19:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690948">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caae7d32e1.mp4?token=FyZUZFqTvqDl4wH6FX23cLIpPmbaFPpHpKV5FgfNj0SUlbW8Zpvtf-2qmnWmCZcLvdN1yDvq6bCv_Ts2aAE_sI__fksNOCmcfZ-OZGS79wvvuAoLFyty7T_6PM8bthwW319oSaqqLgx99zMMYV8yr9R8qIriyvGyjeVzgAjCUspGb6pm0uawi2DYYprUMxke9nVJ8e9f3-yPEsMcwCHHhSNww8CT7H_He6PlqmITIKMvHUSGXLQoJrKy0MM6ixTTU9_8rqN2eqtI0-K6yAHn4ADWxG2WsB6an7SkO61FAl8EFuZ2OngCMIFQHzotrgHdDpvZCOQn31Xlez24gRU97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caae7d32e1.mp4?token=FyZUZFqTvqDl4wH6FX23cLIpPmbaFPpHpKV5FgfNj0SUlbW8Zpvtf-2qmnWmCZcLvdN1yDvq6bCv_Ts2aAE_sI__fksNOCmcfZ-OZGS79wvvuAoLFyty7T_6PM8bthwW319oSaqqLgx99zMMYV8yr9R8qIriyvGyjeVzgAjCUspGb6pm0uawi2DYYprUMxke9nVJ8e9f3-yPEsMcwCHHhSNww8CT7H_He6PlqmITIKMvHUSGXLQoJrKy0MM6ixTTU9_8rqN2eqtI0-K6yAHn4ADWxG2WsB6an7SkO61FAl8EFuZ2OngCMIFQHzotrgHdDpvZCOQn31Xlez24gRU97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخم‌مرغ خام چقدر وزن تحمل می‌کند؟
🥚
🔹
در این آزمایش، میزان تحمل وزن حلقه‌ای از تخم‌مرغ‌های خام پیش از شکستن بررسی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/690948" target="_blank">📅 19:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690947">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پرچم ایران روی سرهای جانفدایان ایران در رزمایش ۳۱۳ هزارنفری جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/690947" target="_blank">📅 19:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690944">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa588871d.mp4?token=pcF-aFGnPCJyRpA2fVhtjKvcy6Ii_ILJtbu7GDn_kw5E-1VUy-wGT7mgaQYSWQca1im-cY1R9a1BtfmR8Lev-bOFgOikHpyRoKnb1lZuW5y6LgCvnwhHS49xMrVzJD9qU73iZnfC9o8pe9uaqPQf0HmZ9XqnQUpxoX9498zEOU_2HRoHOH3GchmGo7TqVquHOB2OBvYsNJ2VZfXP_TI233mZU4jrHPHOCr2ZT2Aablhv32JNWnIw0K5PYzXzwKzpNYE9kySYAElSs2IMs5xZVBLmqCJXZ9Jhfn5shgos7Ay3I3pzHUMNwIBln_gRQqgM4FSupk6onMLOAc57of_jyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa588871d.mp4?token=pcF-aFGnPCJyRpA2fVhtjKvcy6Ii_ILJtbu7GDn_kw5E-1VUy-wGT7mgaQYSWQca1im-cY1R9a1BtfmR8Lev-bOFgOikHpyRoKnb1lZuW5y6LgCvnwhHS49xMrVzJD9qU73iZnfC9o8pe9uaqPQf0HmZ9XqnQUpxoX9498zEOU_2HRoHOH3GchmGo7TqVquHOB2OBvYsNJ2VZfXP_TI233mZU4jrHPHOCr2ZT2Aablhv32JNWnIw0K5PYzXzwKzpNYE9kySYAElSs2IMs5xZVBLmqCJXZ9Jhfn5shgos7Ay3I3pzHUMNwIBln_gRQqgM4FSupk6onMLOAc57of_jyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد "مهدیس نظری" فرشته مینابی...
🥀
💔
به مناسبت بازگشایی مدارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/690944" target="_blank">📅 19:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690943">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3b7367f3.mp4?token=b_lCgFkc7Xe5JQEJIkukclEMKmDWr9grvlJTJ-FxHmHsFDgksSJrKXt02DlkrABCVbEpotwwKatUwcfLQfr_NmAw0DW-ID0q0KVjJdksn2AXXeYW3hRGtjRsQnhVJg96lSqLzBcCNWI55Z1QAXE5F2z9eQQFLajasW9Hj00w-McgTUHujd2a03Kc4Pvw1TupEKBgp7Pbzp8om4C3Iwzm9C6-A0zDDu0zH_BRyU7H1oiPXOK5cp0hkI2ctPnqbHiAXyUIxghM3qrAUaVZ-0hbhQx4gI_QaS8UFKKSj5YbAPAPNIlpghrer4SPzMrMictK1oospho6MyZcLRsUhDK_-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3b7367f3.mp4?token=b_lCgFkc7Xe5JQEJIkukclEMKmDWr9grvlJTJ-FxHmHsFDgksSJrKXt02DlkrABCVbEpotwwKatUwcfLQfr_NmAw0DW-ID0q0KVjJdksn2AXXeYW3hRGtjRsQnhVJg96lSqLzBcCNWI55Z1QAXE5F2z9eQQFLajasW9Hj00w-McgTUHujd2a03Kc4Pvw1TupEKBgp7Pbzp8om4C3Iwzm9C6-A0zDDu0zH_BRyU7H1oiPXOK5cp0hkI2ctPnqbHiAXyUIxghM3qrAUaVZ-0hbhQx4gI_QaS8UFKKSj5YbAPAPNIlpghrer4SPzMrMictK1oospho6MyZcLRsUhDK_-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاشار سلطانی، خبرنگار: هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
🔹
یه عده خودسرانه موشک زدن؛ کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/690943" target="_blank">📅 19:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/081e9989db.mp4?token=OxVLJks-DActSNHwkLJJwjRupRcrjqpl8AjIVef4dKxpKzM5HJVPOfPl2TIxqjZg4zmTluEvzGuptqofCLHBgk1Ms-8IBozwGkqGmOLDopRWwWEq3BV7D2HNdGbgKvdWgNyNySc57EfsHOXRvd5nAIl9LwABbsGMWbxOt00rbF6in_BpIaUlY0fpXaGGdRl5-T7N2C3KmvoJDL_JcMSKdfFXH1xNSCLE1iy4Wk_J_03maXtgTLa3dwlWreJzjgBfcSRl41x8V0u6yFUVORKjvJNX2kclioNjJA_mUn4rx_RmAkmwslOQVshd3JbAbw3x95WZL12bXzl-I_vL69r4nFYQVZhfiDyR4hzWGeW0yZoGyTQ30hDzBiqL9qsMzme7OHRvIxa4gVXFkHkSuTyK5Dxz_xYlYaN5m9G3mV1vRUxhklhZaY1Yh03yMPZ-vL5YZld9PmY_tjkDZ-Hfgmsziu3DHHKnqJS1sxTJEST7AC925no0Fgd4GmWabI7U2GKp18r69r9iNxbASvgBAVbzoB3_6Te_jmFsguXnTF_gGfuzxc430CY6LZBMXJlLjOCGzvqyBDC8zoRZ4wP1SX3LgWL2BloaiCWJzZzzBcSa94BA4HNmoZhNuSkdDvgTcLIwo_r24edR_OsX4mWNnFPBNJUV-NPTjARjSPOgTZUXOvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/081e9989db.mp4?token=OxVLJks-DActSNHwkLJJwjRupRcrjqpl8AjIVef4dKxpKzM5HJVPOfPl2TIxqjZg4zmTluEvzGuptqofCLHBgk1Ms-8IBozwGkqGmOLDopRWwWEq3BV7D2HNdGbgKvdWgNyNySc57EfsHOXRvd5nAIl9LwABbsGMWbxOt00rbF6in_BpIaUlY0fpXaGGdRl5-T7N2C3KmvoJDL_JcMSKdfFXH1xNSCLE1iy4Wk_J_03maXtgTLa3dwlWreJzjgBfcSRl41x8V0u6yFUVORKjvJNX2kclioNjJA_mUn4rx_RmAkmwslOQVshd3JbAbw3x95WZL12bXzl-I_vL69r4nFYQVZhfiDyR4hzWGeW0yZoGyTQ30hDzBiqL9qsMzme7OHRvIxa4gVXFkHkSuTyK5Dxz_xYlYaN5m9G3mV1vRUxhklhZaY1Yh03yMPZ-vL5YZld9PmY_tjkDZ-Hfgmsziu3DHHKnqJS1sxTJEST7AC925no0Fgd4GmWabI7U2GKp18r69r9iNxbASvgBAVbzoB3_6Te_jmFsguXnTF_gGfuzxc430CY6LZBMXJlLjOCGzvqyBDC8zoRZ4wP1SX3LgWL2BloaiCWJzZzzBcSa94BA4HNmoZhNuSkdDvgTcLIwo_r24edR_OsX4mWNnFPBNJUV-NPTjARjSPOgTZUXOvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران سوخت به ترکیه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/690942" target="_blank">📅 19:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نوسان قیمت نفت برنت در ساعات اخیر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/690941" target="_blank">📅 18:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای مشاور ترامپ در امور کشورهای عربی و خاورمیانه: رئیس‌جمهور آمریکا برای پایان دادن به درگیری با ایران در نزدیک‌ترین زمان ممکن تلاش می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/690940" target="_blank">📅 18:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc98ee2c9.mp4?token=Qnr0N0jhaEsiytTNUm3HgyFmwooT5wroGJkuVDq_g9xEoSOD_KVHmu0qrRxPAY0P8D-PXSjONjcy52039pdA597JVLsGOff7BgKESNprXvN6G46kypM-V6H8n3TVZstS9W0aB8V9S9L1pBt9NUX49ibrAUnrUvowrbQDOWTLbwc0Fcj_Y6d1GAvM22pT5RQIljrjNnBuDnkBiLSqIfN_qfImMewojc2Ncr5ow6nkpiYze0oWvjhnc2tSGE6Vnio4iGniWG5RnAOrS2zX_H9V2SYFRwlc5VEOKEMwYbIDaiaTBOC8kM02gaxNyiBGgHY7kqECLeNz6kvUT2V9YkmDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc98ee2c9.mp4?token=Qnr0N0jhaEsiytTNUm3HgyFmwooT5wroGJkuVDq_g9xEoSOD_KVHmu0qrRxPAY0P8D-PXSjONjcy52039pdA597JVLsGOff7BgKESNprXvN6G46kypM-V6H8n3TVZstS9W0aB8V9S9L1pBt9NUX49ibrAUnrUvowrbQDOWTLbwc0Fcj_Y6d1GAvM22pT5RQIljrjNnBuDnkBiLSqIfN_qfImMewojc2Ncr5ow6nkpiYze0oWvjhnc2tSGE6Vnio4iGniWG5RnAOrS2zX_H9V2SYFRwlc5VEOKEMwYbIDaiaTBOC8kM02gaxNyiBGgHY7kqECLeNz6kvUT2V9YkmDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در رزمایش بزرگ و مردمی جانفدا در تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/690939" target="_blank">📅 18:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای یک مقام دولت تروریست آمریکا: عملیات عقب نشینی نظامیان آمریکایی از عراق ۳۰ سپتامبر(چهارشنبه هشتم مهر ۱۴۰۵) تکمیل خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/690938" target="_blank">📅 18:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690937">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رسانه‌های رژیم صهیونسیتی: پرونده‌ای جدی مربوط به جاسوسی برای ایران از درون ارتش اسرائیل، هم‌اکنون تحت بررسی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/690937" target="_blank">📅 18:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8531e9c2a5.mp4?token=RZ1PMrE52K7IS635Dkya-VGh4jE7KVTTOagouUxXaKG0AkH_uzMqTMTDJ6-lRdSGdrPUUUIIFq8TJSviHMwBkPq63ygVUgpmAAOOmP3u23uZkQGNQYbZK5YivjZS0VSpMngbrju98KQoeyXDJUY9y_o0USrHlo5C_aflW9gP3fKrGSXysBAXbwz6NUp6M2cPn2q_y1tN7cI6LByDSi1t7xwoh3NkMdcZBIdeYaJ_6Yh55jzVRTu-VjhtFW1yKoHh5qqI6oxaSVV_OydzqbSjgQMiw229JFsnAg8VxKr-_TNBx_3-WchtuHzzxm-mOC7gXzVwVZxo1uVgcHknEQbvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8531e9c2a5.mp4?token=RZ1PMrE52K7IS635Dkya-VGh4jE7KVTTOagouUxXaKG0AkH_uzMqTMTDJ6-lRdSGdrPUUUIIFq8TJSviHMwBkPq63ygVUgpmAAOOmP3u23uZkQGNQYbZK5YivjZS0VSpMngbrju98KQoeyXDJUY9y_o0USrHlo5C_aflW9gP3fKrGSXysBAXbwz6NUp6M2cPn2q_y1tN7cI6LByDSi1t7xwoh3NkMdcZBIdeYaJ_6Yh55jzVRTu-VjhtFW1yKoHh5qqI6oxaSVV_OydzqbSjgQMiw229JFsnAg8VxKr-_TNBx_3-WchtuHzzxm-mOC7gXzVwVZxo1uVgcHknEQbvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا مار تازه‌ به‌ دنیا اومده دیدین؟
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/690936" target="_blank">📅 18:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtkcUU63b2IePNfdMi1Y6bBSlWWNsCDZcNoCxHG2zG8GF8RCRVgNJ55I3Eemn_lMO7jUvdhHpZE9C3_DV5dyrynEKUDX37KOxHl4nmoWBfS1Ea3OymxGDghgwZ4w5blJ8fvsJBWZX2BQA-Qq6EAGuUip26FFNjmqIpZfJnqHo0jCHNogBoRxlRk0XqhAXRU7doCuW8lgBMmvyZxNgnHtGSU-rJPH3xB7IPSFBduJXstZrF-HFdYr27tb7yjrdJeg03aEugGfsSsnPN8S1CGPiYbQaIvalHxNj5XJuT1BRZz3jLbSl9f-jBTuQtym4NwQ-s6TKyo5Vf1ksbvCyzcNEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین از ۸۰,۰۰۰ دلار عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/690935" target="_blank">📅 18:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
از گذشته تا آینده…
🗞️
➡️
💡
🔹
دکه‌های مطبوعاتی قدیمی، با چهره‌ای نو و هوشمند، دوباره به قلب شهر بازمی‌گردند.
🔹
این‌بار نه فقط برای خبر، بلکه برای ارتباط، راهنمایی و زندگی شهری هوشمند.
🌐
🏙️
✨
طراحی زیبا و هماهنگ با مبلمان شهری
📍
راهنمای زائران و گردشگران
💳
خدمات شهروندی در چند ثانیه
📺
بستر نوین تبلیغات شهری و محتوای دیجیتال
ما گذشته را حفظ کرده‌ایم، اما آن را با آینده پیوند زدیم.
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/690934" target="_blank">📅 18:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
طرز تهیه رشته و ماکارونی در هند
🇮🇳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/690933" target="_blank">📅 18:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
العربیه به نقل از منبع آگاه: وزیر کشور پاکستان طی ساعات آینده به ایران سفر خواهد کرد
🔹
او در تهران درباره تشدید اقدامات انصارالله در یمن گفتگو خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/690932" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690931">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974fee3d52.mp4?token=fOrjyBTmgoeWdxchsl98oZ7OmEh4grvDUJqktr8IzE9yq34FfkpFeADD43TsWxzXtNcrqr1tN2d0C2VZIihwngaV8AQH2vuo90Rta375E2pAoMd2zN8iWa3Z7EIgxvEI9NcLekQDP-FI_NtO51NiIbSD8H5wFMRl0shlL_VEcrPRLKtZh5w_dr64-1TjHlJyhMN1ZkFlmnXLhORL6X6rZmtcn8j3HspXsaWuKxVhDQ12bGUBpXWsii6Nm8U7NloiSdGBmc_IBDrss08aKSay67aySWjQlvhCD5XnhLwUXdjHs2xjJcVsVIZ_zf-S8kt5kAaGP4775QHztFnaq0qslw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974fee3d52.mp4?token=fOrjyBTmgoeWdxchsl98oZ7OmEh4grvDUJqktr8IzE9yq34FfkpFeADD43TsWxzXtNcrqr1tN2d0C2VZIihwngaV8AQH2vuo90Rta375E2pAoMd2zN8iWa3Z7EIgxvEI9NcLekQDP-FI_NtO51NiIbSD8H5wFMRl0shlL_VEcrPRLKtZh5w_dr64-1TjHlJyhMN1ZkFlmnXLhORL6X6rZmtcn8j3HspXsaWuKxVhDQ12bGUBpXWsii6Nm8U7NloiSdGBmc_IBDrss08aKSay67aySWjQlvhCD5XnhLwUXdjHs2xjJcVsVIZ_zf-S8kt5kAaGP4775QHztFnaq0qslw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشتن پرچم خونخواهی و انتقام در مراسم رژه جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/690931" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d717437bb3.mp4?token=szyKb-TNd9j9h_M7gUk2qpCmFVeLjNDdqZcwCQW8SGVJTT7ftu9GfOfVbweKtJYqR0bX_RR4-MhgRcT7QNbIBdRHZFV-3omw4mDcRA9syuFOqMzYRe0x1im5xH4QTa_wNeT-QjEMibssNorkV8yVpN8ZeoNi-_yGQ0HHpQa1feKT15H56z8EAZWYxrvdP8S0LBSNxGFlavZG-YsP7uV0T9gxpiYvL4SHsvtQvfR-SnlFEOzAPK3e7qwb4DptvR8CcOmAJSiad4GOeh_Qnl3EqFZnc9EPHT7_4IZDEktbdkBXwgfyW6fkL-3_X3t09x2zmQm1QPL0J-xLh-CzluhbMUCNOoX3O9fh0f0x0wWCGlilgYh7BUWAPsJ59LxjwYLQ4zkosjmFf1dswvV2UrcZlcQDVg9DPizljQPTriTmU7x9oEpzBHYuMbY7K1oOu7rklNcqH2rdlnW7mPeljzy7I3hPEmddDJ4c-_UifeGqvIfraokFhvB4Vp9ztV2ut5H28FdllTomIG_l5-8GWHbrD63kTvXx2JlaILhAAHWNINbEhOxCVUrCqmfBDCh0Z8w1-UARZ6QWKsS8ZH8Cz1iNISqYnNY6rLVuczHwz6-bsRiH5pDvZ9w_7b5gJ33BOekndptVlc6mzr7cUTwL9yeSY0x4HO3wiCHQ9jz7wvwPARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d717437bb3.mp4?token=szyKb-TNd9j9h_M7gUk2qpCmFVeLjNDdqZcwCQW8SGVJTT7ftu9GfOfVbweKtJYqR0bX_RR4-MhgRcT7QNbIBdRHZFV-3omw4mDcRA9syuFOqMzYRe0x1im5xH4QTa_wNeT-QjEMibssNorkV8yVpN8ZeoNi-_yGQ0HHpQa1feKT15H56z8EAZWYxrvdP8S0LBSNxGFlavZG-YsP7uV0T9gxpiYvL4SHsvtQvfR-SnlFEOzAPK3e7qwb4DptvR8CcOmAJSiad4GOeh_Qnl3EqFZnc9EPHT7_4IZDEktbdkBXwgfyW6fkL-3_X3t09x2zmQm1QPL0J-xLh-CzluhbMUCNOoX3O9fh0f0x0wWCGlilgYh7BUWAPsJ59LxjwYLQ4zkosjmFf1dswvV2UrcZlcQDVg9DPizljQPTriTmU7x9oEpzBHYuMbY7K1oOu7rklNcqH2rdlnW7mPeljzy7I3hPEmddDJ4c-_UifeGqvIfraokFhvB4Vp9ztV2ut5H28FdllTomIG_l5-8GWHbrD63kTvXx2JlaILhAAHWNINbEhOxCVUrCqmfBDCh0Z8w1-UARZ6QWKsS8ZH8Cz1iNISqYnNY6rLVuczHwz6-bsRiH5pDvZ9w_7b5gJ33BOekndptVlc6mzr7cUTwL9yeSY0x4HO3wiCHQ9jz7wvwPARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آکسیوس: جنگ در ایران باعث افزایش تقریبی ۱٠٠ میلیارد دلار هزینه برای مصرف‌کنندگان آمریکایی از طریق افزایش قیمت سوخت، از تاریخ ۲۸ فوریه تاکنون شده است
🔹
ایالت تگزاس بیشترین میزان خسارت را متحمل شده است پس از آن ایالت‌های کالیفرنیا و فلوریدا
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/690930" target="_blank">📅 18:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/690929" target="_blank">📅 18:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzQx-lTpDQRdmLYg3xejZIG3F_Ls9AoS82K6XOT9hftDXxd6_vXC96977terrCimFFVcjQpuXimxodApqhTZh8qV4mB9RWcMZVTwG5haAo-JjXMgfT3X5qxqX7Ng1rdyvVs6RU7KuQGKXCMaG1bAEx-TSdUggKeTGM5AnXZJRuvHgYtxDENQ8BRVwYIBoOfLtL3GxvS9iSpK1yUnjCpuUymezafMaTBROY8necGfrrnIplnRUVlGnyMFxBESrjTxL-6BQ1KR8nCgaz5Qr9QUgbfgx98mrCKELyYjDx8j0mPCSBQcBwE95wX3GGmp40du1LvbhNa-T6TRxTlDi_E75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زبان و ادب فارسی یکی از بزرگترین ظرفیت‌ها برای ترویج فرهنگ و تمدّن غنی ایرانِ اسلامی در گستره‌‌ی جهانی است
🔹
برگرفته از پیام رهبر معظّم انقلاب به مناسبت روز پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی  ۲۵/اردیبهشت/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/690928" target="_blank">📅 18:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690926">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd5ZRLcbFLfJyqaIz5x2euLRrNyzXDeYJYckwrly7bi7pc5UUDBbxU7DBdsJDrFK2y3aaSrwJz8uSneX2La3afaGVmaGOWt-sbNq5QIk4E6TKb1R_3xH79I0nI8muKfDu7kHq-M7XSxSknL7bAxjH-xOaYxF2Culu4DZs8s60fkA4ORVN-hSsKf7CuHXc-GPkXl4O_ZlLQ53QGqMaCMIuOvshrMRNXWFSiLL7-kZL8vM_uxSEemyWLUTkmGV5vpx2xvLgP9E_AaGVZgynA8dcNd67XSadVWfiFqRhvY84ij3AXsfVatYNUu2qnO3H6k0ZxIhgjNQBrzs-Nblv7A7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd18f3e035.mp4?token=tW5z4snSi1fUB-2kQH7cWpAZxpFTIsMsq3jbT5Iwex5geH1dLsLpAcmrDsWOqKt09hpA0whTAh39UMiGZj2lNFCC4s4bIA02282UZUXhfG3Ad5Gz2yHKvXSdFX-F-p0F911BI5PwXXIeEzvkBdzPQbJu-P06LwhmDAKT5uhJriVLRvaisoIWy4XSUJdrN2mWVuY0rP93IDBHWzbOpoNGyGtFGl1eBrbqqJ1VKPm3epCeo68JbtfX53V1IVI7VR6YfLHvJhULVnQFkDS2PhVMRsbURq7kDk6kIL3IwnBEZzv6w3IHFWJ2b8ZsHiqjctbTjz7yJBWYG6bXuU-qDYg-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd18f3e035.mp4?token=tW5z4snSi1fUB-2kQH7cWpAZxpFTIsMsq3jbT5Iwex5geH1dLsLpAcmrDsWOqKt09hpA0whTAh39UMiGZj2lNFCC4s4bIA02282UZUXhfG3Ad5Gz2yHKvXSdFX-F-p0F911BI5PwXXIeEzvkBdzPQbJu-P06LwhmDAKT5uhJriVLRvaisoIWy4XSUJdrN2mWVuY0rP93IDBHWzbOpoNGyGtFGl1eBrbqqJ1VKPm3epCeo68JbtfX53V1IVI7VR6YfLHvJhULVnQFkDS2PhVMRsbURq7kDk6kIL3IwnBEZzv6w3IHFWJ2b8ZsHiqjctbTjz7yJBWYG6bXuU-qDYg-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مقتدرانه بانوان کلاه‌کج‌ در رزمایش جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/690926" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKWhy270Sbfv6up2H0uJerCqLwzdVKyTFiUXhWegYkBf-OSK5rAc5Dlu8LFppEJyNiKazoe9Xmyto2IK7K3YqW3XC1tMBVpQ8crMvDHQlGgdRKJ7xujCQbCnaKxL2705SwKrnUD2GKiTwspFh3FpS8a70DmDjn-TSEj0VRXooaYubOirzTcyubSH7Tv0HrhNteTfNSbctsPAXCicynZTGyrVDql6Vj6sEvHLDXDNXGwGyAc8ZGQprFieRINguXDH_K1euOCAAHQHyYYRVSAe2CMgzLoS1xjHpm0S9dP5NHuvYAFhE9iCru444D219UL4S8aLviGHb2sSdJTQzRsT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه جنگ ایران و آمریکا؛ ۴۳.۶ میلیارد دلار
بن فیری‌من، عضو ارشد مؤسسه کوئینسی، به نقل از برآورد سنتکام:
🔹
هزینه جنگ جاری با ایران حدود ۴۳.۶ میلیارد دلار بوده که معادل حدود ۵ میلیارد دلار در ماه برآورد می‌شود؛ رقمی بیشتر از برآورد قبلی بازرس کل وزارت دفاع آمریکا./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/690925" target="_blank">📅 17:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690924">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f327cc1ca.mp4?token=rMFleqE6pq_Z_ctIihPqEBLJYfvf_ac2q_VpKH8wU47rUxMM2IfVnlwvWBBCRgH3J2MTjm1TW3VkRAGERJnhUzqVqwxxxuKBIzycp4mH0yRYRVoiKwuQJU0d60JXWnSAHL0GUB63W8gEaVVhOBfuf0M6ajr9UjdCdaSr3Uk2avwS-jytRfNeFpXJRcj3gpG4f_H8mOa2KrKbXgmMOZvZvXtmOwEG9LuelOHaTI28HEAT4STUdztKVVI7lj1_SgumUZCMEvbMXXSqmqAthaFkazCnBL1RRS1wEARJWgAopuZqZzQcaTVDpX5-v7szsmfo4H65pm3DrRrg85l9y29qOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f327cc1ca.mp4?token=rMFleqE6pq_Z_ctIihPqEBLJYfvf_ac2q_VpKH8wU47rUxMM2IfVnlwvWBBCRgH3J2MTjm1TW3VkRAGERJnhUzqVqwxxxuKBIzycp4mH0yRYRVoiKwuQJU0d60JXWnSAHL0GUB63W8gEaVVhOBfuf0M6ajr9UjdCdaSr3Uk2avwS-jytRfNeFpXJRcj3gpG4f_H8mOa2KrKbXgmMOZvZvXtmOwEG9LuelOHaTI28HEAT4STUdztKVVI7lj1_SgumUZCMEvbMXXSqmqAthaFkazCnBL1RRS1wEARJWgAopuZqZzQcaTVDpX5-v7szsmfo4H65pm3DrRrg85l9y29qOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال‌ شده از صحنه وحشتناک یک تصادف
🔹
هشدار: دیدن این ویدئو برای همه توصیه نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/690924" target="_blank">📅 17:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پیشروی بیشتر انصارالله به سمت غرب یمن
🔹
نیروهای مسلح یمن وابسته به جنبش انصارالله، رشته کوه‌های «الأغبرة» در منطقه «المضاربة» واقع در استان «لحج» مشرف به تنگه راهبردی باب المندب در دریای سرخ را از اشغال نیروهای وابسته به عربستان آزاد کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/690923" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
بحران سوخت در پاکستان و روش‌های عجیب مقابله با آن!
🔹
پاکستان برای صرفه‌جویی در مصرف سوخت، ساعت فعالیت بازارها و مراکز خرید را تا ۹ شب و رستوران‌ها را تا ۱۱ شب محدود کرد.
🔹
دولت همچنین مصرف بنزین خودروهای دولتی را ۵۰ درصد کاهش داده و هزینه‌های غیرحقوقی و سفرهای خارجی دولتی را محدود می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/690922" target="_blank">📅 17:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aad723577.mp4?token=p6-jzAiCDblgEywWIR4sbRZO4yYgWGT9L3gGagOrfq3uKUR93k3xsPJamiLX6fclGnUY1vMDFns6YmaET6Rmxwi3a-WRns5XP1oqZccu6kbidPkUv_AceVud-Ho-OVL4QCXOo3ATFIU2al5fuFEc5OrCK6Sk9uCHaQzswdzdwCEseutTuUk7lsion8E-4Oy_TM4sQ61aceQjbXoxSgDBo8ym466DqBWtDctbVUqfc9IFL3lHbzn9Wv8S8wLMs2OVpz7VrsYyS0oUwPODB_rSzWhcf4K-4y8hpGDFQqsn-HHSYy0bRWGDEocTKGZ2gMxNGs0wpHwjwXlSw0CsrsH2H1r-ecHzkcesaxdlrZ_wUIwyJHjKJ-yKGBvqgxUlwLJ1o6cqc0SH4u9KkdMKHmUetp0aDdfZy4yfIedXSg1H-qbaZ9I-cPjkNVsc82fb_s0_RSYvru6oqfeRqnRlp6QrSAbDMX3GLpHlP9TB-yJqpm_vCEtlLVsXHlcymWqV5H8IcDhIsyumyLyq0lOwYF3lKWcl5rfva34uVG1fL8iPc4t6dWEutPjsdFfqqkrliYAMj1-fvES_BaRbNmCnEOH2RwqeovmlKPn4YliW2LRvKN0Z8hwx9-PFFoUTD1JG6zSMQ5elrUPO9RgYZcsA7yMW-jg2-usj4A3-NOxN0LRpCWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aad723577.mp4?token=p6-jzAiCDblgEywWIR4sbRZO4yYgWGT9L3gGagOrfq3uKUR93k3xsPJamiLX6fclGnUY1vMDFns6YmaET6Rmxwi3a-WRns5XP1oqZccu6kbidPkUv_AceVud-Ho-OVL4QCXOo3ATFIU2al5fuFEc5OrCK6Sk9uCHaQzswdzdwCEseutTuUk7lsion8E-4Oy_TM4sQ61aceQjbXoxSgDBo8ym466DqBWtDctbVUqfc9IFL3lHbzn9Wv8S8wLMs2OVpz7VrsYyS0oUwPODB_rSzWhcf4K-4y8hpGDFQqsn-HHSYy0bRWGDEocTKGZ2gMxNGs0wpHwjwXlSw0CsrsH2H1r-ecHzkcesaxdlrZ_wUIwyJHjKJ-yKGBvqgxUlwLJ1o6cqc0SH4u9KkdMKHmUetp0aDdfZy4yfIedXSg1H-qbaZ9I-cPjkNVsc82fb_s0_RSYvru6oqfeRqnRlp6QrSAbDMX3GLpHlP9TB-yJqpm_vCEtlLVsXHlcymWqV5H8IcDhIsyumyLyq0lOwYF3lKWcl5rfva34uVG1fL8iPc4t6dWEutPjsdFfqqkrliYAMj1-fvES_BaRbNmCnEOH2RwqeovmlKPn4YliW2LRvKN0Z8hwx9-PFFoUTD1JG6zSMQ5elrUPO9RgYZcsA7yMW-jg2-usj4A3-NOxN0LRpCWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف دریایی
🚤
🔹
برخورد کشتی گارد ساحلی چین با شناور فیلیپین.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/690921" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81627115.mp4?token=lIp9auQzh6qwu0wHG65KAbP2wY38vDbOggxo6h-37PwRQesTFt5FzMybTZuOaMWl9WIGv2c4jDSb9p8aXa1Ptd1LeOhxmeE6Vwwi-05E2Iy24G3leYjsMxkPYnHosot79_uErvRWXvS443Yg26CS9UBtMKdW__nyoS10egF_7p5hgotmqFDLms0-gXy5XIU63NaPgxmN-uE2JHOWMOlq7czt_Rh5mmcPIH_HCiOj6G_kzEQZ4c8CdnKeqjpehOhBzByfaeZzZNmO9F1c8LUMKhNCwXYt8q4NzCKnNyv3E84pCHnxXVvqNah7mikWkBADNzaqUfHGhfGddJ76CnQIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81627115.mp4?token=lIp9auQzh6qwu0wHG65KAbP2wY38vDbOggxo6h-37PwRQesTFt5FzMybTZuOaMWl9WIGv2c4jDSb9p8aXa1Ptd1LeOhxmeE6Vwwi-05E2Iy24G3leYjsMxkPYnHosot79_uErvRWXvS443Yg26CS9UBtMKdW__nyoS10egF_7p5hgotmqFDLms0-gXy5XIU63NaPgxmN-uE2JHOWMOlq7czt_Rh5mmcPIH_HCiOj6G_kzEQZ4c8CdnKeqjpehOhBzByfaeZzZNmO9F1c8LUMKhNCwXYt8q4NzCKnNyv3E84pCHnxXVvqNah7mikWkBADNzaqUfHGhfGddJ76CnQIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابتکار جالب سوپر‌مارکتی‌ها برای مقابله با رسید جعلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/690920" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
جزئیات جدید از موشک قاسم بصیر، کابوس ناوهای آمریکایی
/
روایت کارشناس نظامی از موشک «قاسم بصیر»؛ ارتقای دقت موشک حاج قاسم با جستجوگر اپتیکی و قابلیت درگیری با اهداف متحرک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/690919" target="_blank">📅 17:30 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
