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
<p>@news_hut • 👥 176K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 01:00:29</div>
<hr>

<div class="tg-post" id="msg-65202">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/news_hut/65202" target="_blank">📅 00:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65201">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/news_hut/65201" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65200">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/news_hut/65200" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65198">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/news_hut/65198" target="_blank">📅 23:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmkPjX4rJ_XOZHYxysSPUn8udhU_MHZd8d1ZOWTV4CjueZQZwisT6aTSILSACk_Vl4pN2T1HiBukcgbrVmB6aqoSTdbLk6A8IdkJXVlqjmeTFR1Qoa9hrnbm-4J60KfU0CXFLrWGDZ78GRGC4PmvrboGRGFy_HZRUdCgwWUEPs1yyhWjV2_rza809oVSfmXzMK1JEiqnTyqIjUqWV42lCmD1qZyGgZKlYrEiq0XZUkCtN3QQR2pOgOgNmfYf5yO8T2TIVYg_IRuY9DdZGMdfZk3oI9BTAoRB8AhBo66vqSPExj2iRGwcnOhjyYIpHP4ulSvarmSH-G27nWEBr25HFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">با کانفیگ v2ray پینگ ۱۰۰ هم نیم ساعته یک تصویر در حال آپلود شدنه، این چه وضعشه؟
من تو دوره‌ی جنگ بهتر وصل بودم، شماها چطوری میاین تلگرام دایرکت بگید
#hjAly‌</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/65196" target="_blank">📅 22:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65193">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65193" target="_blank">📅 22:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65192">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65192" target="_blank">📅 22:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYl1AiOuKPkLjuT2Ct1yzcaBbp7dDRIU3s_ZeLwgAMCFaCDIFrnRTa3uF4fil6cg_VQogvq2KvZHOgDgcPGniVtlobUe1seNzvucI273xwlvPOSzbacCrNnKiLxdygy_oktqA_TU14BFueUh1bnfRsNtZGFH1-JN8DSYcMfgdAxbZrIvoNepbwfSWXsmIDp_yfvfHsiF5sKqDVHtxobF0-t-3FuKe_cTE1RFTetmqSzDYbtJq8l3kAhN64Cet0DzSifQq9ne3hln4pyv0nTwQ6ibAHOGL4NbrHZ8bZko27LuUwLPZTxUNou5VJ8qg6YDyCcIpXVBeGvJdgVYzq2xCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCOcvO6SkgTuc9SBCTgnaEQ6DZwPRhByj8FypXonErLklhsWI_HGlkUVWcLHPiSHkJ3yaWV89fUymC1P8XerB66UbigKDZCcnO7JP1ZFxZVXRcGd0vVs6Zhk3AW-Lj2q6xHjtn_aOgPthA0cM-LBM2xAaysHijE1x8qK77tQkTaVAdWsea3_CApseawfiiyCGl_olw39h6-a7Y2v7QA0yzCrMH15EbARiEHrcg6Xc9kkmAcMNG6LDruJQ297I4TiMrh8bycwI6ovjeRyvAaedTifzd7kw8UtDd4FBunsjon6JeYw6hN6Sr5FqdCVznzuSJ7hLwRjR_xH_jPNDzIC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke-y9qVTSEgTdMHJxHMSXpyJqlvgpxGIwFzp68VfgGeH3tbpe07GE9g0Z5ZXDN3ezJ-Zsevzsm6FNhEYQoHtFGkrHRLfy5OKQx5_FPW6oxUGjroiazr6kY4ll5f5tS9_Qx-fCthjHA-GmiWbsF2uUQ5Xe1PW5VglL79Jsi9mfgG_sHZCgqVG7Zvgowd4WoBhzGfhTwNyLUi3wyTT_oDZ5RcKNwTs9b0PpattdaNRKChMqZxPsJnGiihCAqP_UyeAmr-H-H7dtZn8LfIRvmX89mTeuiK7D1s--XBmtilhRyvMZ7l5wb44ZsZrZ7NK51lg6Vx07LBP1J2yRrLbeMjiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65181">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65181" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqwbYiA2lRuAswD9vHc68Zf29qDzvUKiS6_SSnUkYtUULWVz_rDacch2OQAT3ISX62Go6fSqjjPa-bYr61-pqGdA5Q1Oh-RO_A37R2CkyrRaBQJRfqh2FB5GmFxjS2yoQK6m8IR9iOrITwAjwvroLfzJAY2EytEPBzClwFWXbaav4wlM0nHt8Zg7RkXx0OdhvJXwziWtBbzAgh5XTdddbd6ho24yRZ_NKeM6rAvSPfIBAaL4hS90Ts0dKUsGIE5H2R_aBr9gFxjQbsVKB4_zzVfU5fSMclACMokr-yAvAPA-qOeN9LNvN4a-pee8HFwjeZXXkSykciZKMIejMTpVTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65180" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=tli5eaqN6nwXw5WFK8zBJB3ziooR77-d4pCt1PK9FJzwvxsBO0-0BHvOx60gn41cAiRl7u0vFNMFns5ytD3wEHwM5IY07IWwsGK74Po5Mk1lMgbvfvVK3sqQ41RidFXWYMRY60LR4825RYGV6ZX238zpFff5GbesKYtljskAI9YO5DHwf2fqrxQ5TD3tV9VCVm_PWljp12pyBBUAwrhQaAyppA7vVTEajRz0BLuBHkHoDSRR_v-qw803k_djPP7aeqT_ZjT5P6tGbQdiNRM6Cg7Du22v2l1nGNtYAxU4aFnXSzboCaqggzlD8dr6gkCjIdrVCRi95ypqawFEWFL7eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=tli5eaqN6nwXw5WFK8zBJB3ziooR77-d4pCt1PK9FJzwvxsBO0-0BHvOx60gn41cAiRl7u0vFNMFns5ytD3wEHwM5IY07IWwsGK74Po5Mk1lMgbvfvVK3sqQ41RidFXWYMRY60LR4825RYGV6ZX238zpFff5GbesKYtljskAI9YO5DHwf2fqrxQ5TD3tV9VCVm_PWljp12pyBBUAwrhQaAyppA7vVTEajRz0BLuBHkHoDSRR_v-qw803k_djPP7aeqT_ZjT5P6tGbQdiNRM6Cg7Du22v2l1nGNtYAxU4aFnXSzboCaqggzlD8dr6gkCjIdrVCRi95ypqawFEWFL7eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=dQcdVT_JQzjcbUILSm52Iw-ZDs9kaU7Yh85LGxu4158f792PCTeE5iHXN2enBkLgEsC4IwlWZgJ3QQwvM9DBrLsJD6zJpzkqMT5qRLfhCvJAIPpr7XDTIvb3QzEZ3YcSsNk9y1fxOfc-k8t5P9xZ2G5x12Cq3CtjaPpH0DERlM_0yCZfU_DCWtJjSzzaTG6kVL5B4iEi5vmnqBuBdW1BU1MDq7VQ0Q4VMVFo2ITEf8LME7CG5CFuF228kHjDFIqXeFG2ZYdnQrenXIW6XxOpb-hYgx8LRyc8Hci-ldtlI1j9GoV0-17CRDxbKqN467qFkwQgm_5xocDOKXghYx2uOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=dQcdVT_JQzjcbUILSm52Iw-ZDs9kaU7Yh85LGxu4158f792PCTeE5iHXN2enBkLgEsC4IwlWZgJ3QQwvM9DBrLsJD6zJpzkqMT5qRLfhCvJAIPpr7XDTIvb3QzEZ3YcSsNk9y1fxOfc-k8t5P9xZ2G5x12Cq3CtjaPpH0DERlM_0yCZfU_DCWtJjSzzaTG6kVL5B4iEi5vmnqBuBdW1BU1MDq7VQ0Q4VMVFo2ITEf8LME7CG5CFuF228kHjDFIqXeFG2ZYdnQrenXIW6XxOpb-hYgx8LRyc8Hci-ldtlI1j9GoV0-17CRDxbKqN467qFkwQgm_5xocDOKXghYx2uOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=GhXLsWIlgrY4YThf9mLSxZuS6ZNKfh4MOzRZcuYVczpeAS6pnuOTR5KvXPEmjgTxcWzRv0GpfXJp7ze-u3kM_1Ym-yPZjKL-dq_H0mLQVINdz_CubJuJxam1glY2jspNQk8srLWZmsiWD8N0dQsiS5GsnfhQ79JJ4KdZMiMbcybEoQxh4ZR3jeMqf8wl_JK5nQtlsBdNRdZN-YIArTBBBIdiWNwbP8mp9eg7pWjMOUsTxgWi3KDLInhigzS3lY2A1CJk1x_jFoMZEDB_6wrM9nKa18Wmd3ktcyV5kWYi6dEf0_YdEzJCHX8jA37Mbn4Fns0d0sG2l9--n8vIQQRHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=GhXLsWIlgrY4YThf9mLSxZuS6ZNKfh4MOzRZcuYVczpeAS6pnuOTR5KvXPEmjgTxcWzRv0GpfXJp7ze-u3kM_1Ym-yPZjKL-dq_H0mLQVINdz_CubJuJxam1glY2jspNQk8srLWZmsiWD8N0dQsiS5GsnfhQ79JJ4KdZMiMbcybEoQxh4ZR3jeMqf8wl_JK5nQtlsBdNRdZN-YIArTBBBIdiWNwbP8mp9eg7pWjMOUsTxgWi3KDLInhigzS3lY2A1CJk1x_jFoMZEDB_6wrM9nKa18Wmd3ktcyV5kWYi6dEf0_YdEzJCHX8jA37Mbn4Fns0d0sG2l9--n8vIQQRHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP یونی بت شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9: https:/…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65176" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9FrwEdbCrUdtuGQCcdy4YyZoiQ5ORmVbglAQTrXZCi6Lyik3xmtMWMJHccsfqDWai-plh5QdfBoyCkp8Uk8T-WJppWB7kxcMUQMMU1Q2DukpBX5OZVqpods22Xnk4si21U1Z3J7NhG5Va7_ePgBVlrJQlliRrYupwwgd8Fz0vXMj6T9sa4OXm0s5HzFFUGJC8yjDZZ6y2RpoaoDIh9hGSKhsJlXYDBq7vCjAH_Ya47PiupvjKMdn-hcqh0qTMXXdK_a5owfO_aSMqsQObUQHXafblkbCTEJZDOJ5oJ7VIiXNjdtOvPJZmNfxUHTDtcgbYh5ebg5Rdp8bb7F1AHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP
یونی بت
شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9:
https://t.me/+YwYFluMQ5-kyNmY8
https://t.me/+YwYFluMQ5-kyNmY8</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65175" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OlrL9mKlgSJAV75JLOw51IRitPOe9OHqLO2mEJUZRaTjRFUoTwA-rou1rHKLTQds-_nPS8YWUwN0HL1_Bt5iJ1vk5kUUO8CA1bYOLCYCATNZ1EPMSHd8Ujw7wrlofTSeX8zBj4bpwfNYvfbQsRdSHY9K89t4pum0d5ekJswO2zm66l2pNhrGF3YhORRR1U5FG5KsFOQ4apCmmYRBbeeNOUdrnZEjB-IRrwqSOu0EvIwDMTp-bOkWdyxgL0oLBZ_Q8yi-_Y4zcKKOJGQSGyCjf8X0CI3_LkNQuCjJHDGgBf4zcKupls4QjPZrzktOTVItgAW5RPHGU_hUf8VULwhGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LX-XdtQE7SBEWHCWLSDHUHoxBPSFCuXeaybA_QtVOXms7oobOUUFc8yk7firoCLaBfcQP7llM9FFkfiqIM37SDMcGV13yvue0xR4ScTTRmGzielMiMltLGmEBYkoAcR9H2dossk6m02kN_Q1laZbhQr6ZVDWK9I73pLnkzgqXbWDogbk8qDRmMqnZySuP0yAshu9TRasKlzr9UWVY8RCTpx6jRWCLitE3lFUqzQPWTiuOtWFUvre7TZ19UGDi1EfEsPHqnKJs9IsmquqTN-t4f4Yc3id00bRF5EHvwrHfcbZygY4_ARWllW1i0L_TGZjswRbUJcs874K5CaTdU08JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65171">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmyRr5Y0Bhi1nDljhljOuhPdxmWnLE0HdOrDd89a9yZtsIfKy-Wqohee1pMdRJtFMycRQkvqgNwZZsQFmGIRecfJOP9OY_m4-qvNiZgR_CWLNFipbQAfME_l0Shk7Vgr8Htu2OGG824nRIreU8GQRa7kONXzdcS4Aph3BIeR-VWkKcm-RBbTN6LKtzcDcG-XjbM55ak3R3nWEmiV_QlwFQhw52T2jFe3qR5x82Yt9JxsrmyBkBbkbw0N5YzTn7sWUKuBAdqLTYopExWn2BgjnpJDkqvxVK9QkXIvONnlgs9WGN3KXCZtHFqX6Hr4DytQ9dGAEmFpyRjwZ0p7Y3Od8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آلمان
🇩🇪
-
🇫🇮
فنلاند
🏆
رقابت‌های دوستانه بین المللی
🌍
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه میوا آرنا
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آلمان در
۱۰
دیدار اخیر خود،
هفت
بازی را برده و در
سه
دیدار شکست خورده است.
✅
فنلاند در
۱۰
دیدار اخیر خود،
چهار
برد و
یک
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آلمان
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر فنلاند
۲.۶
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۳۰
🧠
قبل از ورود، بدترین سناریو را مرور کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65171" target="_blank">📅 23:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65168">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65168" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65167">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSHRC96yRxF6IMThkGXXIqxAB7vEFFShQmcHg271LLQAkoFYhNLzhB6-DA7V0ggImEclsekGeJ0UlklRxOhD-lLmzPav_YHtSfXAFFmi9kBwGoqdsuSI14dxqgQVrDPNIABHOOZAyMTgHPtTmmu49NU_tHP51zhMK0if8pcYqOwoVFZ0ikaAIE4uU2i1PZqfUdbPNFpAWogstVYBuLs9853_XdIIaa-jAcJcn0BugkUO2PWtpVYTkc2D1hVFJNLclIzHbe6N5NIpbdxJ5DFy79q2_TEMgjGDrI1GNnG2ODUYyTrPdOVT4n6VYRynWjtzBzUOmtAMiDspoWANUzBKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت G9:
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65167" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65164">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65164" target="_blank">📅 22:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqiMMP1dBoRKK_dHqcYoXZ8QvJyL8QkH-Msev5_NybaekQSRtKTluVwpM8ik3a2HE2IDR0Ppnb5R7aTZbnLV4Ss1j8XPBsIXDbVaTq13EyDfrF0q1vE8gGGXFFDfojKR6hLx2TiuxOpbuEJ5q6JlcFZYVAozSzxsxGKTO9uxH2yfiDTrXDy_7URCivbowUlTtEJnjWOH75Wfolbs6wV2cZOWuti44NV5co5WreJs-S5WkUmM7Djfaar9lTfREyeHdj7su_LsI3rYZOg7gICmBPdpPKPuejxSIB-RJbXCgScC8wJzU9-1A-tsD0Nq-DYmfxigW2gdxX4ROsY3Vt0z9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3vmDA-6Cto6bRNkYPDXS2VqSiQuT4BMLjY-SJeCi00pJYJ0FVH7gc_y_mq3JvnToWDXSsrUCVNOJug9g7M43jBZQOVyNy_rHhfRBMbd80ao4UVxlRXTnAeSXVwAAwjJkvrUCB_Z1fchxzE4doRrzgghzCg0eqiLstU2I-eN6YvoNl6JtHmNOifn3VFcuOks1tCqXLjjGRMwKbhdYMwPAuBl9zJmG1n6wTTU4K3pOPT9oGBeDAYi4PiuNPZ24Hx6Q0WdqQAXCeef_2mFfj0bJYGiqX4k7e1i5y6yf5jln948sECjwPOD7UaFvbM0ZEeFBvlbHcM1xywy7ZKMmd1MRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65160">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65160" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65159">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65159" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fD-A3YDOLOtQMjXtGo0nG0TuFyg2YGY0pvfG-u_77w9GmU0sxDhO37FlZUGYEvVEpvk57o-ftrYp5_3-t8CjJBowpdWS8wAr68Iq1lHhUlQ4S3VvmeEMl_9tTQHwG2QxqnkQs4avvPgX_ivoIqT_GQhlrpbR9mELJRc0LmpyqBf_rAxSZyFzDTA0FQPUYWv4Gqlelt5M3Ctv4DPWhnDosXbNhYvwrVWpgJshefONtn0y6GAHevMKqcduEBjusVmYj6ayu86LD01Z6EkVeaa2Kz1ui7LoPiGKgw7p40sCMwW7pQtsJRIQQRCEN8OXZEtiyqtKxa4pjPSdbnVkaSBy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvTGHXsq6EWvntWw0wFJX5nzKMmF3x7DE-z6WZS7J915-H73cXFpLcFHvxUeLpLil9jH7f7TYmBW5PheBbSAeh33P3-UGf5V_77Lkm3N3aJRGboB4zPfThD3tgJocmg5qUFntVhSwOvVoz2QogBNDFDTJpGP2lpVBI2YFhmoL8kgLZVo0_88bQSE5LkX79UcIC7Kb-4yHNowdkJ8OXaSvrHLxB1t-4kj_Q2eFwLD6-q3SCDHKg6nbjb6VonTZLltKF4m9HUrbRM_Wc8RKVUvl1RPPye2xwRzbc9efpZ3lzvGm0MV1_mw6-EobB249iN9WszHkWuNmelGmi4Y_nSy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgvUJ3PH_qUY97SFwe97GmplZSiOA2jj07i0_FLUidCk0GsXfkfoV45cZxF6b8O1C2ToldWZmh1ZY8dbzGufBV8_LsseKjw1uGFYtkmJtCZ1WSn1CtLelh5OYfn_ZBSI79Dz9T1wNuYU2r_QFDZSIWnQ45Sa4DpqN-kpoDNwfrHA9vhYHglVXqkhE2qnuHilsiUNS9aqVsOmO1iNiYiFBPt0kHpamoo9d_H6zn552AhwZe_ZySdBsEK26RHQPxJpxEtBgNbbrGovCQ4aFYNFwZhmUSPXdq_0hTs_VZd28FpNV4J7fVKKyZLG1dBLAZvaOqx_qaNhv8w1pe3gjYsILA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSUbmuDa0VTc3ABYmv3-eWyMM4YBR9F989j_r9kIFXoAiXIeiF_QYkAW9JY42BNx5iC5X8Z5sysejvbq_2QA83ArkcK0TFUOLaHZRvK6tbZ--GjsheMCHBj1GT5a4lQI766oCYlrRP9lXHXYMNjKmrVL0EoMbo0_v3StR7NTM179FWFYDS1bnkDI5MGYcLzvI7zt85yx4Ybo-9W_gUDt6FVfZiQXZ6Eita6J2j4TLIMb6cAkZnWsmFcPX8LPF6fijCpDC7eUbb8UwRontPrDASlhQ0-pRxQYyxKNSwnj5fP3AJ0DI2SzdCtjr7MJFGhVU3GS_CGmNeD0zhNTmDlTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65153">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65153" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65152">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqO80j4S-YH0dDjeVRgMWD1yJDBtp6l5yviHhpNowefAhXvhrgnLCPcWodP1if6zgUx7ZuVA92vplWYost6I-6qdJR7K3ZphUU12UghGJv_m6sA37UVn7CNfD1Gy8DePgKaZbxckT-OBo5f4vbR6TROR17tSeSx9PpchVYb85ajYsWDRiY5GXy-UG3Db-4vhVcCqo1XJJUF75dGXCBNM1Z_stwka1pq8KqL317aE-kdmj_Nykk9wF0C1VrDiL6IWEiZ681ef1-cH9tjp1CQn6Iq1pxMBzaTt_lTniXGZY2evFpRYRPo9YJdtJe1bUNkAxwueP6G1q48l3tHIem6mIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65152" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=j4l6n25YtrK7_BuwfBejW549LgRlFboCh7pmHmwwJ3eMCQDoDz6vxw3K5s_oAM2_2pv-0ucVWO5c0H7iuX6beWxOxuD11ZxQxlk2NO8ZJjaLM1adswD9qyrOZGNUJT9Lv01dwiMbczXJ67-0ocTHm3Si4RpN6Yu3WR3Qt8js3Io5SO7cZ64lCcWD28gxBDBEOOApHzLzZVen4ihQ_A-ExDmo40ygIpMBMYEy62Xd1COdKUrLxHbX77bIQ7N1pwIi5E9a98lulYRqW7k8BIH2eK-0WASLUXaKj88lNaEnuScuoRnd6XQueDKR5m8jSxQ6r3C0I5vo0ZIAton6jbbDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=j4l6n25YtrK7_BuwfBejW549LgRlFboCh7pmHmwwJ3eMCQDoDz6vxw3K5s_oAM2_2pv-0ucVWO5c0H7iuX6beWxOxuD11ZxQxlk2NO8ZJjaLM1adswD9qyrOZGNUJT9Lv01dwiMbczXJ67-0ocTHm3Si4RpN6Yu3WR3Qt8js3Io5SO7cZ64lCcWD28gxBDBEOOApHzLzZVen4ihQ_A-ExDmo40ygIpMBMYEy62Xd1COdKUrLxHbX77bIQ7N1pwIi5E9a98lulYRqW7k8BIH2eK-0WASLUXaKj88lNaEnuScuoRnd6XQueDKR5m8jSxQ6r3C0I5vo0ZIAton6jbbDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDmvBfmozUPHWiHspLmzH7SrUds-IZ3YIHzTB5QzWcv3U8sIyqdgHjAmObYb5C47-9we6zTBYqDUaW6r3dhzbQoxGxsdUy_i__Q-GyBs4n9GnokwoACXWOLJyPAMyPqPzLdTZOr5xEHLQhCrwe_2yChv3tTsRfgPGl_RevZexWrh0CU1Wii0Fu3Ytl7II-CIIgzYv1chOxphvgFjaccTYCrLCy8mhUajNeWn38iCjM0s5HupbV2_CSsBRdC2ycyBvaHA4nGBOtMyRFy8LAbxIRjJOAAnOGikWmq3rrZxO4RtV1gA7QqU3gcyrZoZZhCfAVGQCmdq4EwbGjlNaWLQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDThNq6HjBsCAzQRxaYb0bcCunzuRr5dbdjV8CD-DemB5XoOket-3HoMOkBsh3cneQeiZFoXbtfFJz9O0LzC3gR7n5KjgnTlU11IiIC5lJkwtg6leJkBYkCx2Q-bOsYEwqhTZFYcnZOzLE7-_VMzKFuudRr1Y3RimOs4MH9WfLJblLzNiT5gML5KeFpymzXqM80ozHmzB5Y_M9qlh-DinFnlp5DUVHw35O44KSGKeGuODaWsD6GqYhzEGQKNbZdTKfJjKDb0FIbiUy7Yt2tcsVljN9zWSz7McvtcEYi8UCzGSysbVFB8I-7BmiReejXPwoxtBgBSg1W7fd_-fEDqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65148">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq2dFCXFurra36U7neCXotkrsQO0VDXUOgMECpWxg6POdgoMAm1GGrJf23qMlBGIcC_rKbGDBCB_Dm8XLtiVKw67VHGkvcpVSQlf6tPiI0UvHzy2x8Ai05e5MI3ur0m41KzMmk66Q4rwjx3_EeVCe2d1bPHNOPyPrJYDgATQ5jk6__2G8QyN38i-1aiQMLbo6D96hJzI-rV3oy36L0Zj2VU-OHm4J_tSQDZOba63Pl3JNTE4q9XztsN2FLk-qAK2qTeboMB50On6lHj-432HC8tilCiWfYJkhhwaEwSdhjx4hPFxsgJ4b3hpw8x3Zuj3Z2CRp9pMzc3jov8ZO5YTYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65148" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65144">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65144" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65143">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXXxYDg9p8iqrfg6ufSHY3gywaNCWQsKR-duDa30FVMSDxH4mPa3idRTR4QS0pw8hTj4hbvjjTqcr1CVcS50ym4TbPTLZ9hEZHdtVWt3sDdisB2Gni65tHaZ92_5ceBnp-nwyCmIhpog59Ee-TkOId0IJC_jMZK_B4HLlN9nJYGvXSYjbvHFoEt1mYDV86Q9K65b9-A1c8LdKilX-LK0Aw3MVLHQd9c0NrxoFTTq_uy7S8y0nJfohwgOJgZP4snJdh6yk64vLS7dZhnagSC8ahSeaN9QWY166u7gTfEeRtjiL5edUI8flHuYuuj84gaTIChuCovxo2cqq3NKD7kdkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65143" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXoJyF9MTZk5CEPhEwQf7Xs0KDxNWQbNQYiCvO6FK8JnfKuJiIuVw4Dp5e5R4ZsHxc5FkAnLs20Xx6DA5HAlg80xgb-A81d1Lkr6GSidP5adA20eqPIB6UUw3_bv0Ub7TK3qnbmAu6THsU4Gh89_1fJ3CRvJ8z6q-7A_YXNbuYhruZo0gOW6RN5dRfA72QtMKuwQvohVekIVWU0k8VzdsdmoyJHEXCQ4A65t3JpqdQqGK_PZuO1HfsnKe9-t_S7erThfRVIj_jj4FR2S3LzlrDBcnsJguyUXaKJa_1FR29iYCtkMw11UKJxgGONvykVLQy9rypFVJA6IG8_DHPBFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Xids2ukPA18gyaRzYylva2_oiSCnw6b-6VyP9SkTmo8YQH5KjIX8-X-D4qaCxl8n2nKHQozNGgzbxJK_0lsymO2zg4OujXx9l2o5R1PxHQiSWvA7ZDUsDmG6hH2s0sDbnfTQM0UNTwYVzktZlIOiOvH-Lz9-6o8oBVaTxEywEl_cLlQfMKWqNB98O-dybkyXRzP2dLKUJXXcrToOtXYrbKyC-K5lk0ym8HbP6toY_zS_2wFU9HVsHhLA_imP26dEZkwcE260-W93dVOECkFNRrSk2n9UVkpOHuBczBO21vhUsvXhidkW5hmRq-0MqdHwNcpK8ozRFkBKaWkuNW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65139" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65138">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65138" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HZ9VjI-1LbfrtYoTtzgJtFZZcnyH47SIYkjvRYEBSablQ88MniOb2FPVD2tE3qhY8T12yOs22kY2hRmdcAvHTbMZ-akzWKx6OS8job1Iz4qhey-s1T4wbiRL4ldu63MfT-ndS1AiJFFgu0M4GR71xhEVhL95epGcaomCgms8lU0BOKSPrZFjEQB-qjyqiD9Lp9OnRX5lqI0RAC55K5Ka3PIXgV6fExY_niCU16TkBFwEfGlK2P2O9nVhv__bo54COWzhNeuU8IXxxWYI6xZpAtul_4Y0-ksxZ7eN1__NQ49EcK0Kw-4wT7HA-OZcjriwTpJf2-R7kK17V7weXSVe0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBzDmeBxGxnSRY6SrSxh6QfHCp5ZWQG9TQEB97Afk0-IjPsrqDD95lt1kt0XmsY4Jiar6wIQ3t6ds0uC9ZPLPzhNG8g0UD3ZdDbjOxhiQxyKnvifV5ytp952dBmSxEXlCKR6VpvrnMML55q_wGIHBtE0wMemT899u4sENHi19Bj2y6Hnr-LTBl2LIFZTGbE8KpVncGOMhN_4bs6FunrlXIqi3ZrwayCuUc5qgc2YHwl-3BDBeHvCn2wmpG2HdNomo_zSMiqDhvozRRe8e066_kuZct4cFubh4lKaM3jwbqz7MytLOTPjIE3lVoMpWFZtb7Enfq5kPtFwPhdXtzhRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=PpUKop3eEWhiz9Ina2b2-9NFbIe7RiI4RbHMdIgmgLm7JLSMjbUcskm8vJ11OgmCPEFMWSlt50qXxYqEHdYVYWTFLD84XGeWStW5i5Pfz_12Eve5Pw99OdVcnIsWG9EnAEdUpoXrjQeMzroufiyA7nIV8Tx-1NAHmdx5lLVNNnpBlrTAQ-Fe9P7SZZ0bsIBcQ1XI_roTYql18mQMvshDfy-WQxsYljJ1pQ7aQmzsmSaC7z5eimNqfXroEBO_GlqBc0mEanwrZgBaA_O-LfMksOo8UbHeZmSqAcvh7DRJ-h5gh45rBle4R8gcHZeDpdr9LnqkSQDFzwDiTL4Vd-6j0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=PpUKop3eEWhiz9Ina2b2-9NFbIe7RiI4RbHMdIgmgLm7JLSMjbUcskm8vJ11OgmCPEFMWSlt50qXxYqEHdYVYWTFLD84XGeWStW5i5Pfz_12Eve5Pw99OdVcnIsWG9EnAEdUpoXrjQeMzroufiyA7nIV8Tx-1NAHmdx5lLVNNnpBlrTAQ-Fe9P7SZZ0bsIBcQ1XI_roTYql18mQMvshDfy-WQxsYljJ1pQ7aQmzsmSaC7z5eimNqfXroEBO_GlqBc0mEanwrZgBaA_O-LfMksOo8UbHeZmSqAcvh7DRJ-h5gh45rBle4R8gcHZeDpdr9LnqkSQDFzwDiTL4Vd-6j0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65134">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65134" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65133">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXGBNtumHkOe63s5zyNOjdz2W3xG7warVTLkG-kn9tLAvDCzncwhoIGg17Byu2pJRxKr1LSCqjRkXlr4_yIaVOP3zyBqQcENoIufPLjXb5ZqwGeQnYhz6RAq0LN4vB8KSw-FjWCeh6a-jpq5ryq2G_ZfuC9tnsWVq3w7qVBdR9Dc4665MJACFrZ8VgYxVYeSt_NoQtK1xE9jCwSH8S9ugWeSx90owVnTezpwMP7ZbyFxWcwg2jVUuTeZiQEUrGKENtqJL8pCrHF4wHDhvp25W-H4_L3CeM5S_xiW798dvBEFloAqwYnLJzqcEnL5JNpAhHJWhz93LhFaoVrUnvNaJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65133" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGmB5iAmYnM6ZHntdT2qSDvYsa_nl64ShztmHwcApu8tBmrYxOdEpUuij0mHHexL4qKQ40EG92RqEjkRUvKiFdfs5SMHKi6grKgNbgcsnutWenyjEYji03nvBH8-vRVY-DWF-hqRmI4LN7o4o7NdoVvFrED57aucYjX1rSTFAbKguagjkEjk8l9CE7K8SyjHzqOJ8ZKhGOj3ukMdmqLwVspNFEbGqpe8ZdidQfNnIXjhfsUDMbKaMyv8Tm3YO_ln8VCm8bw7TMCugrMH0kmtknEVGhNWkWtxsKuGsXD0bhhALMUH7t0e3jj-36rDj1uQ2hRaAS0uGhUY3zNADrqxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=UTpcelOhB12xpzfuxPE5f_oORJKJuUy_c04xnCfqZ2-1crN7g5-B-LIW4GPK1uSOI9v5VOPb5LklmgptNUDDZ_LgwBW9ECJVwDMors4yajGedAl0rjKNx9ZsjRx4zuMvd0E1xZBlOj7IjQd9uUISLxQgm6Q5VOFrgxmQ4Lg-OtbVt0GtiKuvAqrLZ3IVf-tzV5zWmnJvkLbWmEN8bsWYsAKsIoddqINsgF6MQpgMPUr-6eELSZjeQhLQkYSW3pmyQMSaAevgSImiXFCvljNCzSX8nU1gboRzFIYp768Q3gjjDAOO1ozd31FehHzgV6izQDNVuJuhIneCh-3XuXvCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=UTpcelOhB12xpzfuxPE5f_oORJKJuUy_c04xnCfqZ2-1crN7g5-B-LIW4GPK1uSOI9v5VOPb5LklmgptNUDDZ_LgwBW9ECJVwDMors4yajGedAl0rjKNx9ZsjRx4zuMvd0E1xZBlOj7IjQd9uUISLxQgm6Q5VOFrgxmQ4Lg-OtbVt0GtiKuvAqrLZ3IVf-tzV5zWmnJvkLbWmEN8bsWYsAKsIoddqINsgF6MQpgMPUr-6eELSZjeQhLQkYSW3pmyQMSaAevgSImiXFCvljNCzSX8nU1gboRzFIYp768Q3gjjDAOO1ozd31FehHzgV6izQDNVuJuhIneCh-3XuXvCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isv8I2euxs_h8QwwKamZprKBPfbcKy7xGNP9cnIyR6vh3jtUvRqqTmN00HbcOSw5wrAPcjO7-a8bV-yTPmTrToIq2i86smTeaAl7tRjiHyDegI-o0K7Vv_A8Ro2lGWitYRBbsAFSs73upnmu3ZSPqFYAzlwuYpaTt45-9xmyXFpY3oeEMJr0KEza6tbFdYl50HKrlciZawCe21XCl8D7rUkzFkRFumicSGDbKViPQ1hj2DLE_qv199Wgnsp2idtFdA9oA3HEemIdYzg8zNsbmxs34G8ZBZD6An_WCBlqZdC0wMQKiT0eSNZyaO1dNPM5tbFM4BZUH_aV0-Fcqt7oSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65129">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65129" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65128">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VudeLFNKRPYPvZTQefarj7pnYfgJLyQbBiVXRPu4tvBZVI8-lOD8qM2Y5_AeGc0o_5cjtRSDkNwN64datPVPwc1KYkrHBNV10Z0oAe-Bp5_sng2GZ5IqaJ4fO83oTS9mA9HfOYWos32u6qfvgLN8rLDD-U0EPuFbidTeah0gNUjvFemWqjvON2RTy7seg88n-m3pTFkkhkWju2y_nP1Lr5G04EXopJ-o69qf5jJtp_CXcJmvspN62gOk1TzA0O7mBLBgKv3bSNjHcYV7s59AxznpF3pkEnltZBe5gY3EC0m0XFKycGulC3tpj3ivY7XcwkBtjd2CBQnuwOm_y4dZlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65128" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=h3mDLcLb-KEDg_MIYRfD_rRbWKlT6qccQSuIhSwN4UM-y1wBTd2kcXc3S7ODD-pJ6qjC4l1-Yx_CesGwH_-2EDs39IZ6RUeJQA8n8h_LMD-I4Rn06IkQwB7TGQpl-_JcODLF8PTR18629MEWLbSfXLEJSsz-zgn42nDAO4sSG2Jay5YSrbpu29a4T41u2gNFJWXZLANg87icc5hgKkDwndjfBroQHOVWd5piTYvPaekFPn2bWGr4jP9KMbb8x2i8tCj7ZtehoEy-36bQwXTQFfHSMTsiRhxpRXB9V8jPlt45J-E3he3QYMfdbu1ksJEU-g52KsVlQH81mDjTSSjNeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=h3mDLcLb-KEDg_MIYRfD_rRbWKlT6qccQSuIhSwN4UM-y1wBTd2kcXc3S7ODD-pJ6qjC4l1-Yx_CesGwH_-2EDs39IZ6RUeJQA8n8h_LMD-I4Rn06IkQwB7TGQpl-_JcODLF8PTR18629MEWLbSfXLEJSsz-zgn42nDAO4sSG2Jay5YSrbpu29a4T41u2gNFJWXZLANg87icc5hgKkDwndjfBroQHOVWd5piTYvPaekFPn2bWGr4jP9KMbb8x2i8tCj7ZtehoEy-36bQwXTQFfHSMTsiRhxpRXB9V8jPlt45J-E3he3QYMfdbu1ksJEU-g52KsVlQH81mDjTSSjNeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65125">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7DHC66BuioFiYqvYPloNcoiid4RxvqSgKtmq6A5kw0-CC6kX0iFW7_He6LUx4v8UD3M6DVAt_4GajftMg0CuP2sWqSJjK1cwOWDu1HUC3Con9FMHssoJBpJQc1F03vE1ihYE5shgJbHwnRL8oY_83kUVPluwXUUdGoJLme2NFVBl4n5eS3k2jeGWKufOAJI7d4DfOc3sU9GeFb15-KdaK9iDqN-H2oCHV5AgDmHeknsVgHroXiLz3CLngpZISb3FV6h0oYHu0IeBoQVHUv-8mDOVmjOrKP16ZOaK2_lUocqmyvnZUpTka3QoEGgth9Qy6Q3glsqMYeFeCVuJYRptg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65125" target="_blank">📅 23:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=oYcUrLaKiJx-pt4BVpC4onesdmzoNFVT2P8lAJKwHlf4NtvGG3l_s6GVo1qBOpyflB-Z0Gc98ScSfZOBtWYciCxo1r7lpnGwQRsH0JtcI_YMo3wH57R-QgeOdVzGtP1bccQJ65-y2rqeF26mRD5Z3X3xIoA2Jo3cAYplenjwTMJtnIyy2KcMipliIus_EtAWANf0rmVgwGYGHqckfvRVIOizCwXt3lXdsdI8Qw9vVIyM3UyrUFWrWSNO6YnNOAzmWMtt2rLTUwEj7xthsyqxJmkFw-EYWp895bQo_LMO3hKA9slMCX0iow2ytQVJDw-HobwkkMz6yHdWRvs3_Vmrrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=oYcUrLaKiJx-pt4BVpC4onesdmzoNFVT2P8lAJKwHlf4NtvGG3l_s6GVo1qBOpyflB-Z0Gc98ScSfZOBtWYciCxo1r7lpnGwQRsH0JtcI_YMo3wH57R-QgeOdVzGtP1bccQJ65-y2rqeF26mRD5Z3X3xIoA2Jo3cAYplenjwTMJtnIyy2KcMipliIus_EtAWANf0rmVgwGYGHqckfvRVIOizCwXt3lXdsdI8Qw9vVIyM3UyrUFWrWSNO6YnNOAzmWMtt2rLTUwEj7xthsyqxJmkFw-EYWp895bQo_LMO3hKA9slMCX0iow2ytQVJDw-HobwkkMz6yHdWRvs3_Vmrrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65118">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65118" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0cvWLZytt2Oepl7RS3Jg8DJQtYpr5QXV2HP-X299mauCnRw8kfhkX299lJYvJKgu6QoWwTCg5EAchzGWbmCAgz7l0cDZu33Xqo0VlFZNm41p4oDLfeBEFXJnXdpzpKUEC8Je0JsTAOKaBO852mpT2ekotO-uittAlLUCK4bN4TqAJT5Qx-by0g-QaFmCaJfGOae-lEZbVa2SZvbd5x4LD8mvH_dupvZr-HpWmN0okN5sHmnMGyAdnH5u9_lbFP4G1WcGohLqRNSiQK7EC5TS9lZ16fJwmXg_aKdrs3f19pu5HDK-7VzglojwgWdZ9JnWl8HWTOKL7Jq_DhSVY-Cng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65117" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o33-zyt3kRwj53BRRfOr72YqfNMsMwryaA6sg7C9r0BctQFYKtP7MG93IBQIiX7yOyVMSd1GZZVozQdXIso35Z2bci7iSQk9UP431Y0f_bDQv4qrQCGW6iyL-hliY6G27lRFdaeunb-Ix_Sonn7u6q0PtCuclo8NutVh3rWAyRXMfJZgrbLP0wJkrWEHEKJq1CqbnHlAL6JbLmJ0Kgmp5Gk0na1cB7jMQX1vNGydEJ3OHncHaeKeI_oc0iaP8Xfq61yJMtWbkd8mdMg6V6rSb57GILhehpAZmmTdU9nj7WRZPkUIbKBLw3EYkkSgZUAZeN3SLLyPoF1pyfE9E92Fqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvesAN512judbly5W13W31qFYOey3jt75G_SEcuWhErZEvltVgFRGw7KC8DkQUs7Apk_KuOSxef_O9D9iC3dD42wFlKvqLW85j6P4AmNyTQ9nd4WUlsRaNWvdLNtDOX24XoAXfmToN-YVoe1ix5UeA-FKIAw49BuT8AdsIDEqNamCT6nDxgLINxcGjT_uCqlNdPop4m5KO_I7RNh8I_SCuNr7zrH3AD9AlQe_egXRDYpuymLKh56ljMHZV3jEKj5HnDUgMmdvCeaPCdqeMIv3vHTjTxWUiiuE0oEc8B6DRbJ4x0Prb3BP_Xkr7hudboVm1-KaT67JbLzwmnSUtB-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Zo1lUcMSJIZfVnPBnX7H7CtoGb8Voka_Tgpwg65KEDQvjXeVahMv7o_RLe2GHp0wqMVaw53zKWmaNg5-nc9DdFI25QwX9YdoE61Gd7H813GD6ZpEHPEd0JCHaKOovZhme136rBgDigQAakbWYcpUbuCBbheaNE7Uk3WImIUJ_bF9EdaOYWlckeHwgM8VeZAQeuYE2dq-eqHO14bH9e_09Xle5cYRXjDFL3_nFYeob-_PsXcKiWj7NycBvSKe7VWjR_If8YJmLvD5PZVyI8dHadW26IGPRYAj-JihtVKAF46KvDOBm8U1haDe93mMRe4_vXU4bXKBsTKXcDC_RTt0aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzAsuR4EXsao_-LE-S5wB0EPPedGvyRWHjv3GmrlQLiSvKX2OWMvTuUx2BhLY1hU6fsZNDqzTBS_j8MZ44lv18qbxNp3wlSn14qYDvKJkSWA3WVdcYYz9pqeMU0TBx3ovrXkFy160T2tDtiIXQ1Cq0EGEFzk6S7-F0Gj_F8w7r5JWBvN-zGPINMQx4KI4UbuypMYUniM58tCqr7riB6iG82iUiPsMHdaekB4PxUNLCSmsmo3WTwnKueFBTYMRVQBTyUY4h0p9TonwhsJcc6Iq86zmTJSwQ1NJqG32_d7k1qdYG14GWUWJ11lqREE5xR5nDbfrZprPa43wUQundhpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYTphJnji1THFyQaySKiCIbLt-crM7WkLMmRdS0P8Au40Vc1ZUTS_o_2ycryZfGHZAWWfrTSooMvHLkSWvSKbEfIctDGQZaXmQfYiV03xu_dTNCX9lcNrr6srsxzbDaq7Iebk-_YBNfC0eqIySg-nsAx8-kZYdRvj_FoTbkKqUjRcTmQd2eumrfUAARQ_cXmEKFX1WFmoaiy1niHflMAjI8ddGWkkRBqBOP16wLOlcKyikieC1eUrLquJvbouH4W2WzVN0NLMlzA_CqISzPT_NfJJoEpLNgbBF4LhXNnsBDu-gXfx9m-AIuC5bYAChCldR8qY3QmptlQMrT63RdWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idpijJb11rvZChsXTVOQqiZMMsF708z_9OyHZppntnsnm8xQ0XP0YPZWgWUHclKyl7x_JeSj_l-IN_zQ8MOLbFhgVb-eOG19wJM4jh-J8vbRM2-VXBu43DA5xjS20FRD4u4pQzm7hv5DYOQj0i64Gf5_p0zHVU-MQothjTjFuzXyYIOyhoIZqdMI4Je16h1NpryjEiyOHIMK5qVrl-dwBs4qz-Sotq483g_0KXqAg1rONMhoOGOBQ19khnYpa9wsxW_nIoGsI8lb4UpAdO05vzx5UYF4YBmxSX1vN-0ZnmxO9F-2_pY0ZbIEJD2R-dEAJLi-IoPibyL5iJbzPSAgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MMdgbH_MpjCeW4YWCbQLaEMS6Bno4fPx88ciZgmQJiZ0UskF3NxNGntMVkpxoaxyHfmZpGhCOLEGsBGmkJLAT84BS_0D1rAiBAj_p5rNtxZ2vOvKS5UTLK2f3uDTDYUsBgMa3RJJSYuv3WbzfVhx95Wq_SgnKQA2EZFUGioqkXbjGhcWcOepQo2uMiKsukpAwu3rBUqFWJdmqzwGLiFJMJq-_mr17bFUwzKVDHVG8jm3KmIVR7cddhGNnolLzH6EBaUFNBCsTVadvGkf0vfpZNUczCwNwputb_1XdfGZP0lt6H1m6NuZa53LgsCQRu0hU2612cubfbKs3PmRYTth9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFUQcbmGDLVY_nq9M7oFClelhQxk3ouqE5jXNZodXsEGgmmAf1XPYE2Gk4yhSQ5Jf694sUKsaqd_y3tPSEIOp1MdQO_oa0sm7ufIEsUXVVbQ0tAxG9ASoQTb8JfOjekh0OQl2R_Gm7iv1erDu_TDeWTAu8a6BErLYyxTPOZI1fWAU58J0XzOoons2fzXkiRdQ1szq69TDVRmwM25RxY9TGul74GaW8KeGChA2nxQAxmXAGwIC3leeYX0uB3MbBBwDkmXpWGr6RS_DIwGZaw4x5zvBTgb89nZ0uPDgVnOLGqAAXcMGlxy0jrpKLUfkS1Vgx3KJrAeDeYdvlc4HM4Llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
