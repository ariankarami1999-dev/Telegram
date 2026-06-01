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
<img src="https://cdn4.telesco.pe/file/TpWO_3R1vur3Yz5hUGcKB9A6Jojr64b5B7XB9vE5X7A1xqLOxCRlj3fd8Jnvk1YdWwjKIuSVLndlctfbCVSn4ZZ82072sUvzqHvZ18q36aZ12qgG05QvD84pK2wNZBIK2GeRThArbIbyPDwznQ93MRW9696ElbdVQklxdHZm1zQMZG8Af_E5Q2t71aChRAxtEMqX_4Poj94zxaTRkWdtHahdqirKC51lH3-e6NSUPs8enyy5HDm-DJ6f1rytDq9Xp3R3rHTaupjXxa6gQX60ZvhaVzbrYkBp9TN7Ec9wx0SoHem5LjhjQZUSGWdNxBLfbiq-VHXqJyMB1qinlayY8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 186K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=e5dJbSl1KkjR7ir3WAJGc0Gk7VfFI-MMzF2gcU6wH1RULCYF_qA4Kj2CkPY-xSIjlkJiHFlmKj43NTDcZLhoeXGw0VhRsYjtOr8xQF_Eaf1yHpk_R6WzB2k7Gs_mfUkfh02H0ts_cjCOs1iR7kBziwDe89TL_jkLfJrL4oeqwcTdTJtO4rN-CUOdYHssldfWy6OaH4kcm69VCvLA_BnuVHXqQgu6e_k5wKWo0u3JFB_w-jcWsRZwxLPjWhDZmgXvOyRLm6mdSqoFRsVdFh8Uz9rSdHIcCA0D42pSZf5-x7wPgINSSYHNZvvI8x9EaAwryWsxtESbZInBCf57YmO2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=e5dJbSl1KkjR7ir3WAJGc0Gk7VfFI-MMzF2gcU6wH1RULCYF_qA4Kj2CkPY-xSIjlkJiHFlmKj43NTDcZLhoeXGw0VhRsYjtOr8xQF_Eaf1yHpk_R6WzB2k7Gs_mfUkfh02H0ts_cjCOs1iR7kBziwDe89TL_jkLfJrL4oeqwcTdTJtO4rN-CUOdYHssldfWy6OaH4kcm69VCvLA_BnuVHXqQgu6e_k5wKWo0u3JFB_w-jcWsRZwxLPjWhDZmgXvOyRLm6mdSqoFRsVdFh8Uz9rSdHIcCA0D42pSZf5-x7wPgINSSYHNZvvI8x9EaAwryWsxtESbZInBCf57YmO2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65202">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGVDvD-sVnL4fn4RYHvMQBPEPLlJSCqs-p-owebelbKRgst02BREaGtBrYriZjxUjiPvj8uSi2Sd82i6Nf2yQeheKmkK1qz-XfHsv1RsC_EymWspEAAZrkv2oQt-jkm8DdaGEwsTr07J2ORWlMzrR-ixz-zU7q8u-0o1F6h3cNqBvlM3w9QWrt-ko3CkuiDb2NvC_Mj3S5jn2Lj6UaQyMS_H2chiQIuxQaask2CXfbAsKn528we3PSeyT4IqHKrq8ukSfG76v3QdVAxgs0IY3sCmZFyvUpdlgX_PFk9AmzMmbEH9CZ4FANvJ3Tq_f1LXl5aMn2vxLKlyXk8GDGGBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🔥
ورود به ربات و مشاهده :
👉
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65202" target="_blank">📅 00:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65201">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65201" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJarfRrDXgd7zdcXk_ktMsNoD8zQXlcqrfhKW_Sk5U-zjB3GfSWdUVMa_nl8xLyoKeLp66JR6qmnDGDlvE9KyxpBwQcEew6w8jW9x7wmuk98rIpeo0Ww01ZHuRG_19K5qeTranG63Ae5sPiQ9D1edhy6nlgJYGpO27a2-FF94UN3bqV98-sd8ZZ9oI49Sq7j1HMPt8l6ji0xDgzs_amjH-iv1Qjrsg1jRxqffo9rn-hpFNqknM62zVStp63PlquFNskHLyNYIbXWNkoGsc74YFkzx9xgH_XJemCo4Tu293XKRdwJC2goiZGF0BQmgZo6H5UEqjC1EcAXFSu2e6Q19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65200" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4BfbA7K_sqZsJgYdEHMcb0wEcm_Oqx4mVnM10iLnd2WH2KXiNa4fkXgyOPn8AV2cxqkXTBJ2Y2kYf1uoAGFThx3XmWKjc5Q2l03tD83spksmVMEu4HYJ_9BIpWvdTJyye_IQyaGtXqsNJnQd1sS7veuTXn8gQqMbz8HDByjWQDrKFGk96GcQm3AHmUB5vSoPqFotzVoGf6kTpxzWH8dmJsyLouQm4XAb9KZFyxGaBZxLXVVjLB8YB-ueeJcU1FWICI19E8L1BoMVgR5HfyNeZyKcUo_JNUAvViDDzorj3rdryGuqz-LEWNod2HkoW5MJH6xRl1J6kwYWH8_uY9Y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نروژ
🇳🇴
-
🇸🇪
سوئد
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
دوشنبه ساعت ۲۰:۳۰
🏟
ورزشگاه اولوال
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
سوئد در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳.۷
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر سوئد
۳.۴
گل در هر بازی بوده است.
🚨
نکاتی در مورد بازی‌های رودررو:
در ده تقابل اخیر دو تیم، نروژ موفق به کسب پیروزی در
چهار
دیدار شده‌ است،
پنج
بازی نیز با نتیجه تساوی به پایان رسیده و سوئد در
یک
دیدار پیروز شده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۲۷
🧠
تغییرِ مکررِ سقف روزانه، نشانه وضعیت ناسالم است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65198" target="_blank">📅 23:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmkPjX4rJ_XOZHYxysSPUn8udhU_MHZd8d1ZOWTV4CjueZQZwisT6aTSILSACk_Vl4pN2T1HiBukcgbrVmB6aqoSTdbLk6A8IdkJXVlqjmeTFR1Qoa9hrnbm-4J60KfU0CXFLrWGDZ78GRGC4PmvrboGRGFy_HZRUdCgwWUEPs1yyhWjV2_rza809oVSfmXzMK1JEiqnTyqIjUqWV42lCmD1qZyGgZKlYrEiq0XZUkCtN3QQR2pOgOgNmfYf5yO8T2TIVYg_IRuY9DdZGMdfZk3oI9BTAoRB8AhBo66vqSPExj2iRGwcnOhjyYIpHP4ulSvarmSH-G27nWEBr25HFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💩
⚠️
دیگه #فریب بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی #وینرو و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io  کانال بونوس…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65193" target="_blank">📅 22:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFCFm8BDS_i9SrOoFh-V4aKp4rHs77SmKqj5fn_n513V1cWMLAq7hsjFFpCYUn1k71A_rE5kpSEEYiZ51q8qRgBSq7oj4VI5vIqAnualfH3MNTau7TxmXR2QulFiZsQdngzPnEF_YURu6oaQD1S-brGBe1xdlbOu-GANOE7sYVk8DImr-R9-g5fEIEWrdVcUXhAbGiz4t10K-8ITgFPUCDoMlzC_SGcP_4EB7r-zDoutZYY7euCgD5QwO_FJRWfkrk0XAQ6OsuiOS0PAqfRxEVgQ1kDLYFxT0L1-ujeAwt007OMARGmAYfAszhBrjkhg4Fl5i1GzQ3HxLF3zrWtuSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65192" target="_blank">📅 22:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYl1AiOuKPkLjuT2Ct1yzcaBbp7dDRIU3s_ZeLwgAMCFaCDIFrnRTa3uF4fil6cg_VQogvq2KvZHOgDgcPGniVtlobUe1seNzvucI273xwlvPOSzbacCrNnKiLxdygy_oktqA_TU14BFueUh1bnfRsNtZGFH1-JN8DSYcMfgdAxbZrIvoNepbwfSWXsmIDp_yfvfHsiF5sKqDVHtxobF0-t-3FuKe_cTE1RFTetmqSzDYbtJq8l3kAhN64Cet0DzSifQq9ne3hln4pyv0nTwQ6ibAHOGL4NbrHZ8bZko27LuUwLPZTxUNou5VJ8qg6YDyCcIpXVBeGvJdgVYzq2xCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7lD6WIDyoWTn0WEtGfWnOu9gjUmyusdb69lUtXuOkSlN1K4TgwStn11baW8rX_bCy5UDDP1JSNPDJH0FDEovMj4zGJbQgC2ME0KVvgs2rYo-pGAm-Fs6xdfZbxM33I7-XzGbC7-wLtJdFgpq92zHumWoWWNMoPedv1g8hvpLAc_-3pWmbxXdjkqdqXSV7jTvTpp_EsY19neCQO4I0VJh6Eh-_QLyLow84x574dJ04pr0p1fmetnKolZhHvkb_20OPQPRgRIyBk03ILb5UPYiEFlREzsx4r-vvivaGvs1A1d5_R5SRcxMwjc8nzS7q-rURXt3ZtsAb5PKziAcdE9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFqlKL_Li7SXLF4fAMSSlKEpLi64-8EHB85sr8eDXhjxgqIwF-gaIcXkav1YNe95QLPE-tOWNdk7SF_wDwS7ULN37i4K70-wzXtIlBCPjGtsdzDpc0a7-goNmr32XLNXL-vGe6f508gRJXijdsUOAat1eJ_WzDEjXzlvIVsxwgI8IEpvIAIN3G4yFi5odgedNpEe4cBQydVKqTGyuWMaJXwEVzCfrKHTrt_Tn0S1mo0MQWbeaCULD1PcMNFPIAndYWCYJCNIhMOVAGgEIiNGmHugjTZF4zb8nf2RT-RDhEvSfVcsjyW8f2gjL6jOXF5rIUxLoN8i-4lPCIqfkD0Efw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=W_O7I53-XGRs3_tG-1zBOrd2pMobtniHE2wcgIm3tD0ZqdBxqA9f2voFYnnofvHHeenKtuIpVGZ_Yx2nbJgDVMQsc_mB0APHQEjD839dHwQz1kuaiTVq-Me1RXGJxlqTZ-PTdPsOetHqudZBRd5exiKOyYsurCeEQ2TfCa7Lis6sdTwvaPsu3HTCHApZlhoxa3BY9UajpeYzS_2OE57JTzUmjoWzz4dnpunoqwmDC4fk1R-ncTt-RfuEHdaOwGFpzn8L716LRzzREHLmn40ZEV5NvW1jmTrl8FlczZNhxqRmGYnYByltLW7KNJ-HkgkgP3U9CZAOWASrYPJZddKbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=W_O7I53-XGRs3_tG-1zBOrd2pMobtniHE2wcgIm3tD0ZqdBxqA9f2voFYnnofvHHeenKtuIpVGZ_Yx2nbJgDVMQsc_mB0APHQEjD839dHwQz1kuaiTVq-Me1RXGJxlqTZ-PTdPsOetHqudZBRd5exiKOyYsurCeEQ2TfCa7Lis6sdTwvaPsu3HTCHApZlhoxa3BY9UajpeYzS_2OE57JTzUmjoWzz4dnpunoqwmDC4fk1R-ncTt-RfuEHdaOwGFpzn8L716LRzzREHLmn40ZEV5NvW1jmTrl8FlczZNhxqRmGYnYByltLW7KNJ-HkgkgP3U9CZAOWASrYPJZddKbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCOcvO6SkgTuc9SBCTgnaEQ6DZwPRhByj8FypXonErLklhsWI_HGlkUVWcLHPiSHkJ3yaWV89fUymC1P8XerB66UbigKDZCcnO7JP1ZFxZVXRcGd0vVs6Zhk3AW-Lj2q6xHjtn_aOgPthA0cM-LBM2xAaysHijE1x8qK77tQkTaVAdWsea3_CApseawfiiyCGl_olw39h6-a7Y2v7QA0yzCrMH15EbARiEHrcg6Xc9kkmAcMNG6LDruJQ297I4TiMrh8bycwI6ovjeRyvAaedTifzd7kw8UtDd4FBunsjon6JeYw6hN6Sr5FqdCVznzuSJ7hLwRjR_xH_jPNDzIC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=Ep4qVcvPr8O_sN8LxMhzFDbtzD1G-ZAzAkoc6KCIjhiLLNYHJdYxPl49QMk6DoCEbgDydUXWyuGSjbLMwPEePhCN89uIX137iWf2lgXwYtMgvSc2UUI0zkwb65B15w6RkdPbZmXvPg_bOJ78EmqoRcLEI2QV5vdPusXUFBgV0Vbxe2243qf7xqt9RAtHduo6oz85yEL-nc_CktPlsnvz3i3vFKrFXIZXhA2REfoLuoA8KHzsbW7RYKxIcW1AupvkrMCAFVXgqjSVqDhhkD-qBezIxve8Ll8Yy38E1_d-VnxolM99uCYwwxaLs-lc2TDIC0TxoTKis2M1rqaWeGckAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=Ep4qVcvPr8O_sN8LxMhzFDbtzD1G-ZAzAkoc6KCIjhiLLNYHJdYxPl49QMk6DoCEbgDydUXWyuGSjbLMwPEePhCN89uIX137iWf2lgXwYtMgvSc2UUI0zkwb65B15w6RkdPbZmXvPg_bOJ78EmqoRcLEI2QV5vdPusXUFBgV0Vbxe2243qf7xqt9RAtHduo6oz85yEL-nc_CktPlsnvz3i3vFKrFXIZXhA2REfoLuoA8KHzsbW7RYKxIcW1AupvkrMCAFVXgqjSVqDhhkD-qBezIxve8Ll8Yy38E1_d-VnxolM99uCYwwxaLs-lc2TDIC0TxoTKis2M1rqaWeGckAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbSXryWc17jleYj2Ce7vSfIP6s5pDnEe95mDJuijHizLIF0v1POTcUeNpmcQzLW7QJP224PTd7Qd-pkc99WToaQtkpsAaP20QfvT_o8UObE2HyJwhly60LhlDnHIyP5plZma7qLGtn1fHHZwY8R8PrutAttcY7_oPeMYb4BqMHuzY_mNY3tKT1NaIPJvrJRx2XjJ0_kwwAUPI1ZetjXdC3E-z5on0PWE46NPsmQ6SiGjfEghvsFi4WxdmiWX5emS74OO2ZfrSPxjhqfPDfbQexrE9d985zhrC1F2q9ygRJXbAAD1jWbFApdqbjADskCzkIwXT_V4fT0E0AzUBKykNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65181">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65181" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65180">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTO1jFsUN-TdHSCnvY80jM9JsIIAB6hEJMvqArw263AKFQviRIaaI8kd1V-vIsfD1YMKPKrh5jL4GewSfnipUatovyDY4CPR4yaGiJqFUJ9SP1qKjBErDgIwllIBmgnEuO5OezPP3ziwV49wnAIdUu_Ez2TSOC9iZdKvpOpUkpwbEL96edO4cXYJ_2ld9hF1VSYy15Xc48Fe1lAm2cXcHUkC87l-3CQsXYBsrDWO6pJ9PSViDk3FQHVVc9oK_s95cKJ-hUHql7sDRPxhz7SqqD5ALO6NtlAyeuuTK5Xnr7MlYVpX1kj8WB1djTt3ijEEb00Mo2RiCRpFmNT5jfAIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65180" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=CGzgWjcFQiTxmdmn8s0jBlMiDkkfmBPue_sjBTkIlyoxfJTAZ6UNHE6Odbjz8Thd1Rahd120Zdd-oNLnYNqZDa8PG0fKJKmzt2-ShXwXirRI-FzCsIPtcZjTSQxCDNmmxjRHWCyGX1-Jr5gRjhWnPY9UHyyqWcK6TzSgD-gT_TtHbiZKzeTUqTbcGdJqmBtgcH-VS_mcjdEfAabsRFbyXwEoRo1NPhkc-9ttNuKzknWAox6SfZOjJkeDMYASj92OrogEK_O4WKVxk7PD_CqE0z6zvBa1FeaUrq-itsTpV5LPO7OTMRKfFjnSGxZUTyxgqr8SaSnfNKnI9BdWa9mqlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=CGzgWjcFQiTxmdmn8s0jBlMiDkkfmBPue_sjBTkIlyoxfJTAZ6UNHE6Odbjz8Thd1Rahd120Zdd-oNLnYNqZDa8PG0fKJKmzt2-ShXwXirRI-FzCsIPtcZjTSQxCDNmmxjRHWCyGX1-Jr5gRjhWnPY9UHyyqWcK6TzSgD-gT_TtHbiZKzeTUqTbcGdJqmBtgcH-VS_mcjdEfAabsRFbyXwEoRo1NPhkc-9ttNuKzknWAox6SfZOjJkeDMYASj92OrogEK_O4WKVxk7PD_CqE0z6zvBa1FeaUrq-itsTpV5LPO7OTMRKfFjnSGxZUTyxgqr8SaSnfNKnI9BdWa9mqlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=HOPUGG3WitunxVFj5v4u22nmFl9uiDUQkQYKICJma096YsWAltmyydRAJkUrZ-0rixosxnPOiaCX7PzZx7qC84_cZRu3z57TpQUmV634tExkm00phVsazjlgBNXZKzddf7FaBu8fI2pnq6_emOr7SIOL-EyyL5I6WwmgxkN-xBRHKOpvQYHIHZfk8D-sYZ8WPLrf0WMLJH6ls65QJFhsAb0onPMM8GD9-IG4uh0sBzY565rnDCoWNBIrMlCkHGijLk7yIr2DQfocemjvvXfXJ9Q_muvE5FYBSN39p4Kl58GDkHL5aWJrmOneom-t9RMx6BaWb8azYYht-5H0nEzs4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=HOPUGG3WitunxVFj5v4u22nmFl9uiDUQkQYKICJma096YsWAltmyydRAJkUrZ-0rixosxnPOiaCX7PzZx7qC84_cZRu3z57TpQUmV634tExkm00phVsazjlgBNXZKzddf7FaBu8fI2pnq6_emOr7SIOL-EyyL5I6WwmgxkN-xBRHKOpvQYHIHZfk8D-sYZ8WPLrf0WMLJH6ls65QJFhsAb0onPMM8GD9-IG4uh0sBzY565rnDCoWNBIrMlCkHGijLk7yIr2DQfocemjvvXfXJ9Q_muvE5FYBSN39p4Kl58GDkHL5aWJrmOneom-t9RMx6BaWb8azYYht-5H0nEzs4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=nNJJdxaWIWrDxWggfk1UZCf8L0Znsl_qQKKMWC5GuMFWveonfH0EKvMu3ZFD3dPzURyVFc9f7gii9vpl1qe8sDW0iVnhwGezN0m8kLDI0vtwJvsirqWytXzqJALG1MoYqZiUeGohTtyTiHy2SZU-b1aDNfFNBvcFm-8ITid8j3gi3Nsv1P4NUST5dLFT_COqpKHULcesVgXJgw4LS0VHD6uU4XXTGCdE40pdCTg7rGb3IzZjwimzSs-U1vq972IhvnJd1k32PiAcK2nuMoM_62ZBUYIIHeK-Igb6BCVZDjje7tdsPVa267yDRMuqQ91TyEoNTi_lkjt8pSsckDSBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=nNJJdxaWIWrDxWggfk1UZCf8L0Znsl_qQKKMWC5GuMFWveonfH0EKvMu3ZFD3dPzURyVFc9f7gii9vpl1qe8sDW0iVnhwGezN0m8kLDI0vtwJvsirqWytXzqJALG1MoYqZiUeGohTtyTiHy2SZU-b1aDNfFNBvcFm-8ITid8j3gi3Nsv1P4NUST5dLFT_COqpKHULcesVgXJgw4LS0VHD6uU4XXTGCdE40pdCTg7rGb3IzZjwimzSs-U1vq972IhvnJd1k32PiAcK2nuMoM_62ZBUYIIHeK-Igb6BCVZDjje7tdsPVa267yDRMuqQ91TyEoNTi_lkjt8pSsckDSBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OlrL9mKlgSJAV75JLOw51IRitPOe9OHqLO2mEJUZRaTjRFUoTwA-rou1rHKLTQds-_nPS8YWUwN0HL1_Bt5iJ1vk5kUUO8CA1bYOLCYCATNZ1EPMSHd8Ujw7wrlofTSeX8zBj4bpwfNYvfbQsRdSHY9K89t4pum0d5ekJswO2zm66l2pNhrGF3YhORRR1U5FG5KsFOQ4apCmmYRBbeeNOUdrnZEjB-IRrwqSOu0EvIwDMTp-bOkWdyxgL0oLBZ_Q8yi-_Y4zcKKOJGQSGyCjf8X0CI3_LkNQuCjJHDGgBf4zcKupls4QjPZrzktOTVItgAW5RPHGU_hUf8VULwhGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LX-XdtQE7SBEWHCWLSDHUHoxBPSFCuXeaybA_QtVOXms7oobOUUFc8yk7firoCLaBfcQP7llM9FFkfiqIM37SDMcGV13yvue0xR4ScTTRmGzielMiMltLGmEBYkoAcR9H2dossk6m02kN_Q1laZbhQr6ZVDWK9I73pLnkzgqXbWDogbk8qDRmMqnZySuP0yAshu9TRasKlzr9UWVY8RCTpx6jRWCLitE3lFUqzQPWTiuOtWFUvre7TZ19UGDi1EfEsPHqnKJs9IsmquqTN-t4f4Yc3id00bRF5EHvwrHfcbZygY4_ARWllW1i0L_TGZjswRbUJcs874K5CaTdU08JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=spvsJ8QSCuzSA_t6uZw4IsAnftpxpODaFjTupY8uUKWVGQLLHxD5W1C6olaRQm9yix_GLFVgny9cofCrJ75puq-57mN3rfVN4REGw7sVMDtdkaSAOddIv56J7SnyKaepFXl7QCoW26lAXt08h85ZgrQ4vQH8PJoxToSgKefkQiqfkt2Kg1mZp7YBo1iQefsHwxhcA1Epd1nxVubn41Oeqgoc_EuEfEGUUgap82rTfLno4ExM1jRYqlqm-vTWmdxaLXASJCfBqD3gGvWuy1vnmbgfVovF4GW7RWPeVQWF1rjPMCte6roreheUJ-LekXS5sdnYINM0d0FYlVDnCKcQ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=spvsJ8QSCuzSA_t6uZw4IsAnftpxpODaFjTupY8uUKWVGQLLHxD5W1C6olaRQm9yix_GLFVgny9cofCrJ75puq-57mN3rfVN4REGw7sVMDtdkaSAOddIv56J7SnyKaepFXl7QCoW26lAXt08h85ZgrQ4vQH8PJoxToSgKefkQiqfkt2Kg1mZp7YBo1iQefsHwxhcA1Epd1nxVubn41Oeqgoc_EuEfEGUUgap82rTfLno4ExM1jRYqlqm-vTWmdxaLXASJCfBqD3gGvWuy1vnmbgfVovF4GW7RWPeVQWF1rjPMCte6roreheUJ-LekXS5sdnYINM0d0FYlVDnCKcQ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=Cpm_oiceQmtJhiUQQqDeT3hM8D0xvXBrviiweesgaJZslJ_6MlrMSx6LF2TBqUf-IbTs7JFxlMKQYZAEsDbUIckT5450PaMlJ87ylZnd68LIoTfbqwSE8TGqeDlH-YoFMZmMa2ymHVOCB_Q38NNearTp8dIbmBZjALXepl6Bmx9mUV-wJMQe6veto5Ana3WZdq05K6E5F0IHsEBCnn1kBlG5eiXjPyHI8jLTpJDhIgY8TscGJBDoGUh1o2PXMmLlhzTnkjV-DAoZ_pYhh8s95DQ1TuxJp7rJGxOwjAq8-6liD5wic07EEU004BEbKpCr05fe0CYXVz6bB_F5wgVy9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=Cpm_oiceQmtJhiUQQqDeT3hM8D0xvXBrviiweesgaJZslJ_6MlrMSx6LF2TBqUf-IbTs7JFxlMKQYZAEsDbUIckT5450PaMlJ87ylZnd68LIoTfbqwSE8TGqeDlH-YoFMZmMa2ymHVOCB_Q38NNearTp8dIbmBZjALXepl6Bmx9mUV-wJMQe6veto5Ana3WZdq05K6E5F0IHsEBCnn1kBlG5eiXjPyHI8jLTpJDhIgY8TscGJBDoGUh1o2PXMmLlhzTnkjV-DAoZ_pYhh8s95DQ1TuxJp7rJGxOwjAq8-6liD5wic07EEU004BEbKpCr05fe0CYXVz6bB_F5wgVy9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
⚽️
⚽️
⚽️
اخبار داغ حواشی فوتبالی و تحلیل‌های لحظه‌ای جام جهانی را از این کانال دنبال کنید
👀
اگه می‌خوای جا نمونی، همین الان بیا داخل�،
👇
👇
👇
👇
👇
👇
👇
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
✨
اخبار داغ  و کانال معتبر
👌
👆
👆</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65164" target="_blank">📅 22:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqiMMP1dBoRKK_dHqcYoXZ8QvJyL8QkH-Msev5_NybaekQSRtKTluVwpM8ik3a2HE2IDR0Ppnb5R7aTZbnLV4Ss1j8XPBsIXDbVaTq13EyDfrF0q1vE8gGGXFFDfojKR6hLx2TiuxOpbuEJ5q6JlcFZYVAozSzxsxGKTO9uxH2yfiDTrXDy_7URCivbowUlTtEJnjWOH75Wfolbs6wV2cZOWuti44NV5co5WreJs-S5WkUmM7Djfaar9lTfREyeHdj7su_LsI3rYZOg7gICmBPdpPKPuejxSIB-RJbXCgScC8wJzU9-1A-tsD0Nq-DYmfxigW2gdxX4ROsY3Vt0z9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3vmDA-6Cto6bRNkYPDXS2VqSiQuT4BMLjY-SJeCi00pJYJ0FVH7gc_y_mq3JvnToWDXSsrUCVNOJug9g7M43jBZQOVyNy_rHhfRBMbd80ao4UVxlRXTnAeSXVwAAwjJkvrUCB_Z1fchxzE4doRrzgghzCg0eqiLstU2I-eN6YvoNl6JtHmNOifn3VFcuOks1tCqXLjjGRMwKbhdYMwPAuBl9zJmG1n6wTTU4K3pOPT9oGBeDAYi4PiuNPZ24Hx6Q0WdqQAXCeef_2mFfj0bJYGiqX4k7e1i5y6yf5jln948sECjwPOD7UaFvbM0ZEeFBvlbHcM1xywy7ZKMmd1MRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65160" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65160" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U8rpKqA_jGyuJLnKZpj4pEe2rpg84JJCwaE43_2V9P5v2w-LHWS13_nx9miZPUWiAUKTOUIavZAYAAdomx0O_A73GB4aJzPQt6NcLwaaNcnlPRCa7iABIFS0eb3_w8hG5YPZb_0CEMzVZh7aFj3SPXmLRbKEmAmF4tef3zH8xpRyi8VVdhndRAlP7YaxeI5wnUGocFTb8C5FF3ze__F_v1wix93RzXblELxt8dlg_ycM9gkYEYa5pzjNwxgCMRN4w80JdkLU4JNMF-UDpV83_1_s6R1R5aa7khqip7rqbLL4nsU8xu-VSVzV2meKhiOlN9CO2It8gnB-FQpaw7LMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65159" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X3X-UK4YqE12APcmVWpFZzDB8dxyqSUfRZxuSoQJ4F50_JxhLB8i9bN65HE19VhMxySkcjAcSxAW6y6CTrYjWcEy5iGmpHlDDXBNIo2V6RRzkLKqqGdN12fKZXe5_OJBeDfbFR8FumniCbIZpqJz2yrrUvkTvifdValC1xSuR_SH_eX6h58F-0PcAkQxF8nl_STR_kaH_BOME7VmfcjCqKz6LHjpBdDAnGdxcSOwqiwkEOjXnDaD0IADWuYrFZU4f5qleGFrZuIYIoEAmwAVmYoVCOmUNG71Bj8AAk9KdwbGgf9oMqZA4Rgldy1GDJGpwIRLqdzWNvDflpmq1q51NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJEBqcOdh7k1qdDBYbKzhe0JLtRXhQcDYCmh0s9JflkYXijJXpLGivO2QXxXmCcNZUKM3DOdzxFhCRZsgupkeldQeGb4eOD4_68QR9WdSffEo6LgPvYOngniuYPBPvS1HHxzLYxu3TD2RNylQH6RttG_xOACvSlfmwEBY8jdwabZ1CdH10Un6KcfwpffLTSY8bt94l7KugqnUrPT90FaGSTO-c1pP_amJJFhe7_Dyisc-PBt3-L6QpFRRtnpifupZZhUPax0omxxbDco9iovdHqZeXhqEel-z8nsn6Xc0cJBNzGssm-DbI_khvltfN4KKx_lcXAKzjdiL03RNEKLPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-UzqQ3_UABBCnEfPSliJkATQ2gsC1-PJKdDAY_xq7VwhwuuQ_jB7dw_06QNFOEZ-u0iEv8aGmjlPMYJbA3SS48G7i4RGz1OmuJ_Zum-coTal3j6BsyZRVQM-qSc-JkIEXalJu6jFXnflepVKXu4vrz-VGJOp7lZguy6Ra3c4GHGLdYIRU8_8GFa5lRH1qanKqL7oDSBsdkPdGvF_oVwgBAW_ub52Nikl7XhJ4v3hVG_r04m-EEJTMdxp4_iHpBEPyE2-51IJJzSkFNI_fX2NmkvK_4k5-KUCa6jfrR684GApWvkW9dDIwN-nEpglG6RZ7VG271uTuwuO19Qpv2GCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bA6SJpnZvi6Nc1zkgQInmrUfFeve9HvoSE8eTJWc7pEqWzXlHwjRrsjR7FUHquuxHcyvyCg7-LGpbXe_bQKt3mJL-fT5tebFJQJQ2RRkKxIcWFc2-dpwXzBEKGyNLbdno16oI0xK8B-pnL6kE8v8pjNE-9JoYfYbDonrCezlHladzyN7SnRo_fu5Nad2Zp3ktWz4ZgrqdMllMR1iRHbxZ_n8Uo0Rb4QfjOtZvioQPtST04TiSceJWp9wJe142mjh5cCgXVsv-76Vwz4rh5fYktmKYnM0N0cCy-JUKatPnNZD8tcmaGLlIJ71J2Um4C7tfcU_MLHMsTZ794JAZ3GLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65153">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65153" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaQZlULcVz78OX4887apeaxs3eE-v36XBhQealb3Va1XNi5jJPubRHCVBUNWt8a0H2GJ1NA3tEwi-sd44L2hKEzbdnj8SuV_IiwYoGfSwgN3CgYGds5IrwRgy_av8ol-qMjD6hiuhEj9HmKw-HYCpJ6dFr0BDpHe-4XnWlYxKXUT4_mrEL2gXi1ybvnADD4p-fPV_rzfx4pCBF9rVbn5m_pRGNTJikKxPIy_qk9DyzQI72sqRgpqxOfiBpBePch9vjMD1Rik7dlUfkjJih60Pjc7tebACb2OpWKgS3G69ZXfIpmonA4gzspwEm6tSUhIdxFptzHuqYVijneC4itjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65152" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=rrReCBYJImGG8MlEf2PcwWCiMBhW5c-b13k0gCRmGzJ-lmZm_VWOCk8abwhrJ-_XaTds8D91mHIfdh4KsFx_MOMagiVS3zA8mbhVzXLu81RRDXfI59AZHNq8xDBFWUxYdpXRdjqMk4mfvoCu0JgAZ-cxpiNWQW2eiyOkovv5ovndhlmRYL0hVLo645KlPFv8_I51-q-QjgxmpXtD8hGxLCWkn_t_YN_wpgu8rIodKNsPmuRD2CqKbGZVH_xVfaBIkizF5Y1oTFxIySzOuDAlP1WscKW8BoxIJKhE2FHBvEeguhG_oueeCLc-UioY_2V3UNKcIhxFMYsAU2xk4EWMKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=rrReCBYJImGG8MlEf2PcwWCiMBhW5c-b13k0gCRmGzJ-lmZm_VWOCk8abwhrJ-_XaTds8D91mHIfdh4KsFx_MOMagiVS3zA8mbhVzXLu81RRDXfI59AZHNq8xDBFWUxYdpXRdjqMk4mfvoCu0JgAZ-cxpiNWQW2eiyOkovv5ovndhlmRYL0hVLo645KlPFv8_I51-q-QjgxmpXtD8hGxLCWkn_t_YN_wpgu8rIodKNsPmuRD2CqKbGZVH_xVfaBIkizF5Y1oTFxIySzOuDAlP1WscKW8BoxIJKhE2FHBvEeguhG_oueeCLc-UioY_2V3UNKcIhxFMYsAU2xk4EWMKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbMEoRHYR_KugWxvu2npIesSrmpFHqzEip2oNgTI0zDZOk97M-g2SRvogsnrYspdow72-iMS4vjpgjM4H8pmS_dzmIcy2vuR0WLn6S3yz486psbUt9_D8_4vDidCEY53-ROJO8XPMvpAw-nQwmDuvNnMdTJV0vtac7P6RxitSH0XBpoR4vHA-wNn4wBycgaAXbPbi8R3uSqAOq6MTzRrsGVWOEKJI6vKw1qtf2brz_0zibJWmEii4I3EvAOl59y_ggCrg1Pu94g_9S0dxkaHhDT-hLxN3bbvO2K-DS10MkTDpsd99IbiX7qsug6-XXmaVcBlPlNxnnU7nHZS3GUbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_dx1tbkql2--TdmLn1Wsn3cBd_Cm5Q73EVNAfAHR3yvcRu9CCxm5sm7_33jcuAqnGo7bXST_SPzN02BPqjlSOMJ-48D17po6j86msnGPl0KWB82MpVg7OGGApNvjRb9gZeanAchyFqf26Ckh3Z7i8052YqBTS6OOwLr-pF6Lo9_ujj8ghkl7JRMqr8DmHr_GNi_XphHiYHmNhyPwXDdZMrMM6cHFv7idTgPRZMKKx3sQMXQJmJ-C0KeEOfvcE906vXf3egnjpBBwl8QnjADoTDTxe549Z_z6S9aysioMEoFXxXTgynx4tcsA9wHZ2LW21bjaIznSj5C4JugkSOljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCMs6p50kUg8L_AzdPapP5MsLS7zy4Mio-y7uqjwW838DdapLQNSfnQuRUi0-cYgBcmLp-q_RhgmEqa_E7ZI0VVgE_ZRHIvpFOCWZ9uEkKSblv9aTQwSIxvMKBaPr5AM8OfUpumWOE110SCuzP8hruUpdGmKzJN4bovcamgO4EFD5oeVq1pgMiVworQd5qxhgFbFExDU3Pp9fMh_4XnaBnPlqwWUrKDbD2Sy269uJweTcjHqm0iptVpANJI1e9KyBlT1-MZ8e9VOElNmHyZntXAJLWwyXVnue69qhAiT8aYSCR3KHhcLgNYv3W-47vwKjGwCk_LGpLqoGltN3NcwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و
بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در
۹
بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در
۱۴
بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پاری سن ژرمن در لیگ قهرمانان
۲.۹
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرسنال در لیگ قهرمانان
۲.۴
گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65148" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65144" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY4qEnncQQEN3KA6NTmAKCjCW7UR0ylOirXgxqkzMVHqaGwkJJ1w9OHFLoFwCxbFKNmJG0HcGlJS0NoPmLyJHrIHJg_pkU49d3mfcU7T3jDCS-RfrscpH_JDvkOfE10Ptv58jMsgAFT9xCLci44VtXvgMpPPTurB4IrPv8fJWqg3B4Rpwip4HiwXRw96pWvBDgSreYACzbuhYZX5oodSZ0iLN2mp6Iop9ZAZl0y3b6tI8I76BWAVPYbZF8h5tU5-N4NAPurtQX-urDVpoOYSrGLvgKjIZNn2SC6TguQDhJuRsH131ZZdVHTQ9ntBafITLt9PizF2fcujQtJuEGMILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65143" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2Q-NqE-WKg6jjAP5or5eSEcSk8wXgdRGQ7YI2JSzI0aWjbSmGtmEAq0GnC4L8a1v4r1D8REtjvzWt94mMG5CoaptgJkVADo4ybVooSjYX7LH-5U2gTPe0Pd8RaA_ChV2mVbtMZmqiTSXLdU4l5r2N_qu9WFjK9xEhpezVu5n37Q9BrN20AfMzJjBAMKDyRmiFpdQO41WODKbvEbnm0lMRojSTVtW4G6btH03B9MXCp3KUjj-5UOGVuYILEcD74mHg0Om3pdOzdyI-e13tNSTwP7PXCKWgjcwrUJVKKyphkS9VKfA57RpEzhRGqABh24pFmi4vjXDtN9pkDiKU8TOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGPOOebt6ippT42GXSvf0Qc6TlIowNE1ugXyhUqBrcTb52Am1OCvOQDQXYKUvihes6tuZJ3xwzx380MNwpbA35Ka0Cjhq7Pdb0UVUCTHGdbDoJfaS8UPYv3jeQN7e0FMFsDtuu_--PbZiQlRIjtEpzdKxfEiEu3RpqL6mkoqqoOzmPtTq5yl4HjrD-d-8PGbKZ_licl4eNJoRcoFJmqTalaCCY93cAzvu1uruXXlamDHJqqg4CCMVy3-P7BAdXj-bPDVUNu-XIcpXFzDXcf0x8XRbh70vMTL6qLqblKPIBb4q8dX871FOpXjMDJ5kO-IRlJrA6QrwRTjgha8PP4RwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65139" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65138" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65138" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZGNtQnn7rRx1qYsm2IS3BNVptCD1lUPbUvQIAfnR2TRK_DzTT_TACnu5L_Yy1_j3ImDU6vOTKHpM8zyzqw6pSfHRBLmrYv4hWQDinvy0BhPd2bwGZUUOXJ5Qi17fxRUY0QUgVhXpGy5TPhmTohQhTDCrLDgU1XmsqHNoRMLcv4eC30UbPnY_WEFeRbaUaORwmLpApcQtnfQgn5GmtzRXbILJUQEr7HNLp5BuIzm8b-6dXLbMX1haS_TJiaFv22K-MuQjkfMhlHyg2Cdx1Ls6qWJfwVlSfipRtDCqTjtsEMTb_r4k6iBWB93YMCYlBWInqgfmBVM-HkBgGZbv6otjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEvTtYvLAhAAc4O0Wup_Xns8FbCmO8UnPgTdAWZGYcUyfrm1lyJcqvK3v2Wb8DzER4v7NHEPCD9M3MWzwCEwGCKrUDvqclE6NzOCLDAzj1KJ5emPFKCkwEOBXMIsXksqDM61_DR1IePc8hHai_3pMcyJk6Mad4vcqwjVxGEMl3zcf_kpFJbm3ycvkLFh2FYpeRgkJc_1TKeolN9zSnZcK6sI2Km9qumwLj6q3WaPC9amXxxhHakh25vCvkFkI385188Q_3hwTW_rKQnzl_Xr4ErkAcQthXovJZq1ZA7V9UHJujXdZZymTqACGHb3hYH-jTNUaE0a_vLr6g3xSvnyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=KP36-Ct5iIiCLWS7OeOUHN8JOuHW37gq9mR2VmaQbDrd8R7eEsUZtQWU0MZlGS26ZrQPmrUodbkz6meQH7qMTUYZ6plObZyS9N2XcuiEOuuk6b3H_tRO0Apjs5ksWScltiG-addEggJxn5vKjRNlpQzMbo_HKt8gXsmoZM7W1FAr8xiZ0ztcE8cDHNG73Eaay2up9ekhAHFC0wjYA2FxhAsnpEHGEoTfhSmFsN75dKDKs0ICV_DcsRCkjIgC4G2s_5RTJOzCdoUW16RIUnQz0kKG59eIA_fgrfN9H4QcTInbWu6MGqpBAKzSxACaCYqAtAJgl87JsykaQOsPWkhggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=KP36-Ct5iIiCLWS7OeOUHN8JOuHW37gq9mR2VmaQbDrd8R7eEsUZtQWU0MZlGS26ZrQPmrUodbkz6meQH7qMTUYZ6plObZyS9N2XcuiEOuuk6b3H_tRO0Apjs5ksWScltiG-addEggJxn5vKjRNlpQzMbo_HKt8gXsmoZM7W1FAr8xiZ0ztcE8cDHNG73Eaay2up9ekhAHFC0wjYA2FxhAsnpEHGEoTfhSmFsN75dKDKs0ICV_DcsRCkjIgC4G2s_5RTJOzCdoUW16RIUnQz0kKG59eIA_fgrfN9H4QcTInbWu6MGqpBAKzSxACaCYqAtAJgl87JsykaQOsPWkhggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65134">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65134" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65133">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8k1PlxM3tL0789Zdm8yF1K6v1it3-sEL7u4SOTnVQxOfbTz0j1y8recqn74Ir1CWPFzTHedl_KD2iS99Srg_0rdHOXk0e9xX4QiLyRklLJtHmt5abjgGQAKgEPXvJZAiGM7pWEteh4PiuYn1vD8FHxHb41e4gLht9egLuWx0hxaT7iUrAN2UuQUeaPVDtZT8zkoa9QAT94SkikSP8pFb0JcgksDZu7wvL4fam3F-gJFt7VUYtA21l0NiTc5MLkkevtM9jmlTLkj-ft19220qXn6XdHUydBJQBArB9z4dEByJl4EUOmoYEVtttRuoMecECgpSJ2VlDcWGBCYbE_8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65133" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqW7RpfAk6heLr-FHzxMLQGbK4X6dSDWf6aSWvxv7eOK0rsYAZvQXHkMfRD5zs6JU_IMze2H_4cQpN5XqV145lFAR6rgerTHnL3dmAxbqjAK_90bl1pYZtVksFdukOhzTD984sSt_pqc5WDX4SyQDQYjilYSamZdh6fO21NLnEZjlngZpED0p2obNazjVlpQBGa370E_BgXNHDHxL8Y3ksyLj1Vx4ERmuVGiTtypCKA-ed1S7NjmMv1xIozyYjrcRuTAchwVnAtyaOPjjKss7kVXkKctNZF6UD5r7UapqUGmL5n_5s_cn3VYx8-H1cURId3UxPiwYnqGHbthlfpIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=dX46vWGx6gzatSfZeKVYhnhTjr_e2IdlbovnM4xfbDvIEPwSEK1ssxIXAH0_Nx7RKJFYIPBQPSxMyK0X9EOcfdRUJ96chMdZ81FItVn7l7lFVuuTy8wYEeZiJY8qNAkYmAGR-WazWtaPkCOshVHML8cXLWl3tqXGz98ULtWZ_qLxa3z_E3On9GbSGxU9FKBRPDeB4cRqvUSyyK0EAw7JjYMoHQtvY4XIY6u1ImbfsVN-KAlXMwsKM6dSppxfg4f5tSWDAt6_j_RD-JuDeqGImu3cGpKgDNFTfmsk65CDJ2vD36bBdFHDbVcXjFLD1RBrZjth2JPtDjPgK7oV1-sbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=dX46vWGx6gzatSfZeKVYhnhTjr_e2IdlbovnM4xfbDvIEPwSEK1ssxIXAH0_Nx7RKJFYIPBQPSxMyK0X9EOcfdRUJ96chMdZ81FItVn7l7lFVuuTy8wYEeZiJY8qNAkYmAGR-WazWtaPkCOshVHML8cXLWl3tqXGz98ULtWZ_qLxa3z_E3On9GbSGxU9FKBRPDeB4cRqvUSyyK0EAw7JjYMoHQtvY4XIY6u1ImbfsVN-KAlXMwsKM6dSppxfg4f5tSWDAt6_j_RD-JuDeqGImu3cGpKgDNFTfmsk65CDJ2vD36bBdFHDbVcXjFLD1RBrZjth2JPtDjPgK7oV1-sbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL82-DB7K7Z5OGayTGpqIb7YnpSJKUQuPJsJAM4l0YDRioZRIWBlUDo-tPmPKu5RmH3yuCl06Hj-7Z-odaRe89S15-tN_TmcyhwwdE4NyP0ni8_uFVPdIqyDGQxjbfH3-oErhHd-V8VcCe1LS0EUfWevY9B-KO3fekt02oyzsLin-NShvUGbCQz74RcY3RcC0wfh8R26sHWORAflpFbHjK2A9wcHm3qEil1Zd6bUVl_5vwsE_arayI5A5fcO8uONqgdVaerKtQRMG1ZsvAuAwj-FvVyPq8AR5GubplTNHNZL8xC-qx13tqZFHe2B2OR_o1TncJJXTVbjDf08xLaKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65129" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzpI4mBROv34BF1c23GZ2Q_DRrpvjvneOuaCPboaJP400jIMsclL6C4bUKaHGzshd6XhSaxohsc1QQ5eYgCW34bzUErJNikSKLV1KC_wjogLUx2OgX42gvHV7d060MXP5HUKxQjJ-tsOYyfYLKLdkvIaYG4JQnt98A5GBXrPDUf2jxcxrCbW4QH2c919CI9n0rcSc2hcA5C4jN3p8lEyAKTg1E8nu_pPKQ4_qfVLHHRxkuO3sZNzUdFZLuAgx1AYQjwjLaMwdMr4DuCroK75qR5GW5qyzv1lDtvhQuqVh7WXP1gRCBXDetYH8TILVNLQM3uimxPB6E97x3oWLnIOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65128" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=sb1WBNUg7MU9mlqGkb94jSzizfdIZODRTOh5tA30HMTOh9lZhuKhoK6ay2IBtkq6tKxU5rEvND6CW6f5d145AWo3SJRJ0aRcrXWkF2ATDJ_b6sNID-O67OuSmunnejZQlOaU-UWlUDdpwRnhP5SB-DiyXo_nte353OKeA8x3kIHqUGU97IYVWJ462wOgHxTZ0QKMjHdLVkQ3cqo1uLSNk3vHh3lHPxh6j2IduGkC92N8PRj3hoxQ2gVKkrGxZrVoI0W6nxo_b4loKagUGWc48g5EsOr3YHBvkUK3x6WTgaLA1TQtOeV4KUR5beqvCQufTWIWGq4nxzcUFGovIsbo6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=sb1WBNUg7MU9mlqGkb94jSzizfdIZODRTOh5tA30HMTOh9lZhuKhoK6ay2IBtkq6tKxU5rEvND6CW6f5d145AWo3SJRJ0aRcrXWkF2ATDJ_b6sNID-O67OuSmunnejZQlOaU-UWlUDdpwRnhP5SB-DiyXo_nte353OKeA8x3kIHqUGU97IYVWJ462wOgHxTZ0QKMjHdLVkQ3cqo1uLSNk3vHh3lHPxh6j2IduGkC92N8PRj3hoxQ2gVKkrGxZrVoI0W6nxo_b4loKagUGWc48g5EsOr3YHBvkUK3x6WTgaLA1TQtOeV4KUR5beqvCQufTWIWGq4nxzcUFGovIsbo6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4cDarAg8M8uSI-RoBdorLqGC_JYC2_YBT27OmyCuUIduyMmDtXGoySTh6igciLA3_7750G9pmt8t9Lml6HFTeJK5L34cSLfeaJ9f0nVbcVvD_UDJGx88T1BKuZ4A1izFc74y-8IaH2zt8IashTnoP68Uj0KL7VmGGuU_cCe1J6UpuYGUM6-HiR9MxPUJtA1C47DZ6VwsFKL94kOOt5UeCFm7LiJKrtqVeg-WUk9ZT3dPy3bnwF1ED_awxkJ-pvJe4Br3MdwKu96ZI3dAV1Exrg-eLAGrwdIYRhmqxv8LHvRq105ir5hqlovgDEQbbwEjmxpGHq4HN3qJIUsEf-Y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65125" target="_blank">📅 23:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=I83kjdkbAtfcN2_EzJqPD8sStm4rLf3ulmNrGinTPmo4Jui69dUE_0T9AFrFavYUt4HkceQGLEfNnMlzgAC6x2XDXBnpAF3myjXmLS0suh0pw7pJFd0giNJyKPa3AWUssaaiT1hYWtYHDokMN8Cca-ofGCHjlWsk4SoBr7FXYFyURNitfSs93Qc3qPRtK-eI-ka0L2152InP9EA8WodGZWFiLf3TjFvWzOaleJQTufpsk7xRB1LLblha6NI1tJiNjUTj7tT6719wUDuZs8SRA7XTY07rqZfJG0HAvYjtK2Upo6FYE7ZZQUVVCrwh2_kwsRrfIEkrv73C0GnPoHtPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=I83kjdkbAtfcN2_EzJqPD8sStm4rLf3ulmNrGinTPmo4Jui69dUE_0T9AFrFavYUt4HkceQGLEfNnMlzgAC6x2XDXBnpAF3myjXmLS0suh0pw7pJFd0giNJyKPa3AWUssaaiT1hYWtYHDokMN8Cca-ofGCHjlWsk4SoBr7FXYFyURNitfSs93Qc3qPRtK-eI-ka0L2152InP9EA8WodGZWFiLf3TjFvWzOaleJQTufpsk7xRB1LLblha6NI1tJiNjUTj7tT6719wUDuZs8SRA7XTY07rqZfJG0HAvYjtK2Upo6FYE7ZZQUVVCrwh2_kwsRrfIEkrv73C0GnPoHtPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65118">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65118" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65117">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hsu9bkn9H_Yyg1UxZ7E5Vag6I6Z_viU3uGmjXZGxFfst5LMXkntTafQsYegQt0hb8x3tSqaSDiaVVDRqNwfIqL4cpLE6Y7hRf1oVaHAfcynw27mhfznAAos8QKplr_qUZoSQyFTB6MnrjBHiSLOXXtL1kVEyUE3VhwKxjD9Y262vAvjNmHuMKgZZONCN073rzSAIo39QTYKuGgysuoxoCedPePVTRb_bBsREzthYcJlGb59pyIQFCSQ1z-wDvw8NID0SM4IVr6_RM1Hiqo9xhYjNrhz8p8HH-N1u_8illPPfEbr3OTyBe1DciaszEPEfuUSbvlMCgr_rXF1Co-9gXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65117" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC4ui8uBKNd34U-SSAIiM3pLgOhE6Ls3rXbvgWzNH8GYLrkREqICFiM44u-gIGyrfNVCKF3GzO_XuTo44ms1-z1EfAe-5lzuUxwEqD_Uos36CzurB873_Nj20Q-2jQlBi8PCRbR93P15mvuI7Jxb2nyt1crsFAw1QrBUWw21FyVW0xduCSb9qonrSe_kBoolzUAsDgrGXyZY7P6VfanuL1kH4cvTJUJtt4JHFUP0EQEmlAGDML8LH4W0h8lYm9XcTGYM3Efkd4mmlRF0lr9G_lKpFvvDDQi2iq6nGpZSiXJQamy97ujSyp9HR4gpDxg5l9CCwQcux1SoG2M44wT2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sfh9Cf0qudqXyPhoArXnp0FTr6NRjBjo-SWhThfC7JhPVNAJHjOjpWZOvIn-V1tpRN3hC3x_mXLNHsnN-tMbSRxwCi5BIN1LaDIsdTHu0xwz8X12gYw_DA6QmPi-gcQ-1W8aCeFLtJ8fWoudXUfZ6ko1_eUFErQljEXCZHoYW5pZ_oklqcrGwJaBLeI6RZdJ9zY0ySOcEiqiCJVwxStIOXEAdumhcNpPF5ObOlDYc-HO2IUAGA60jF6c5rDXJEAstUDFroY08a9fHVerBZa6u6HTp5-miTOz8ZiRIar0Nrrd_uH5biIYzmthR535hIQK_I7ao5LuWvKrNJOBAKT_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65114">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kq9s1cCYgOCzdgoqaIi27FsE4amfh2lhf3HFqY_nbeAmg006JrziQbc7xZNttHJ90HmR5D1CL6wA6g0WWCtg4O3RkUk7OnYGXFxxf8zvHbZ_E4hhYaCo1iecY6FukYKHMlM3fvTaiYUJPzDiHb5EOR74gsIzAb90z59DXJzjgUQiiYBk0X1oVC9PuUxvGBwkWk43MzV05nE-q1t0fxKjKvUDPTbtQehOrTMcD-1RMn6iBO5M3TdpxH7OSfz6Szj0546KMe15K1hTWDVR_6-PVfizavxcD39RXX2QRDSjLc9nlm82mlCpEfzRfy5hfLI92s_FyhlYb1lEAXOFde3uNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا پشمامم حقیقتا ریخت
✔️
➡️
تبانی نتیجه دقیق ضریب 15.00 رایگان
😳
10 میلیون ببند 150 میلیون ببر تضمینی
💸
فرمای تضمینی و صدرصد رایگان
⚜️
🌟
https://t.me/+BDjkK6j2gcQ3MGFk</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65114" target="_blank">📅 16:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgbjvFxsyZ919iRByqo1ao31Zm3Ey3QUw-fTdJDdTfsQAD5VxWr2bgmrzXjcHyGFmpFu4gbQgh4hux32FsXyzaAZIqGGanY6blxTOMFhbDTWKQDsVigQp1zKEIxhPX0TYBlY_NWKQYKX3klaQy9ypCj63-dHSVHG8xfkHX4Lb9BACVc_BAn4zI4ZZzacIkI1yyDMo7rDtyzHlIIAAuBKW6ESzQQkZquYwwmOIioMAmgijOHfojWZX32j8131PCciqxVv1zS5s2SEXa1EE_ZB-3eAkxAe_0Glre0PeQ7T01GphY1g90sXoRuWvyPXjSCAOcDfnCTbLS_gewP2pIFZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuaH0yMUCipKnqMD-QUlWyc7rR-3x2DAH8Pos3bF85sQTB-Nib4sh7oPlRwdKDT3Pqe6rSn_03D9aTlBGCFzRoVE7MMFY5oydg73o9ru5rY-GlD2NfcJeu92kc7kpJf2Mt-5D9ctW_Lq8LH38sZEQ2UahdqhXVVFGGcuPAmhMvtVk18Qvu5ptXYZoWVsp8E1gwerenspefoC5o4cZrHTM-GBo9OaYCzAqfIgwyYoPDrLB1KPsfgSoBWg_ZeSr6kq4ezB-yjnTipFMIHb3OZePm_VVsVTWzUrwGQr8TSS08WX5o5Dd1G6o0TJeO_muGgndAIvkIBm9d6fGX6oUy09iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XswG-S7Y5U8dgqY2z4xjL43QyZPSWMH4WdeJ_f3BwyIluWegVY-505iYFKqYvM4f1Zx--RKMUi3EWJleXgyBVoIz-_4LmntHownqj9o4DvJaseglSwSkWRAwJky45LrDJEH5FFFCMbagOaqcXmbe0o9tAYDvX4Ux29G0uy_sJYcbr9Bu4of0WE_rA7CnV_S4Rv4lKEiZwi5xt5-RgvPEvNyKWd7MdQXvSQTF0SE_xZ9GY92DCUfR7UJbselt9kRuqYB1t-QPYrSy5FpsHzZj6pr_0K_aFcSNEWyD7Z5LuXTfRGdXQBVhtsaelOHGX5c6TpgQriA0eMltlQJU1spReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mt_dZ6vCZahsNyXcuGbi-rycBKzA9DSkw7ZErRsnDzy4fh5XoZNOkdoevUfDyqccdcXE1dOu3NruvaenAvbYs_36VyfycwrvMG7Zy9lIARSGLs0pIIVjf4XNuldTTXHRZ6l1CG503-3pGcmZTDOkvS9ZVTYM23g-lGGf2wT9cpEMZCfwg3vlRlxQiEu122W2_kf4z8jSDSLM_yCzRGcJ4nLmJL3DXbOBgzGiFORN5wB9jCFD8BCrultz5lM6TOXg6j2HS60YHC87DIxAbzfKaZUEiSG2oZu0eP5o-o1FMO3lOdSrcH-S8w6sh-jfFKnEn0jMml4dWoJtEbRkjaUyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjHKcFeiyl3swgMv1t6l71PbXpKlvKziWupHEn_lwnEn24gaUdz2Mi3qMHldqjben-fsmVLA3ckz5SXyyrgMqwn9jE_uaUn5JN8ut-reWCHHX_qkatxkrXP47rWUPWQMpqQQ10lga83Junsghqn9MuGvbi_yhp2ZRyX5itcGp8InD-T6tFVXS1Khvl2PTZ7wzVeaHkmJY2h9pKonouAKaUwVC67wZw1oyc_8JG_S19VhAZ8wZRXoW6bhjvQrc7dEdm751YTngtd2nJRf_jlFyEPm2J44aYvdIm6FqDXPXYlDENPm7A2jiMU6WSTJUhovcfqAQfMajLoQG55UIm9JGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8E2y1HlLpPE8dYc9fXcfXF6BVqrpAeoUfn6rHIE1LWF23gohzT_Nqah7uOUiVLQUa_4s8WOnaASlbk0J-60J71JYjUjNpaxJ_1xagSIBllTMdl5uXhXEZwWG1qOjnA66lNa-5oAD38iOSln1g0EfGmIugmnRZe7dYl9AZWMs4LIqJxbfR9bzupyE7R9USXtU5bkQBs0FRuezKIYEYY9gdaqpd0-_Rm0dSKCZnCuDATc18px5pJYg_arLEsPPDGThfa8iv0wHuh1g4b37EHnawlvH3LlPs3KU-X1a3mwzXMciQV08OQJYLft34w3QT1qr_0FOno-uSnUyACwKCBIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
