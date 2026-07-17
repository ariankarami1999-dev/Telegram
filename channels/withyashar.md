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
<img src="https://cdn4.telesco.pe/file/dL9sMLxqA4yDGGTsZhOrp9saIv2hCznBtK5sqbXZUHHLYRfW7Sa7-BvTY3nQz_tTNWeN52cYqShsiJjEPTlyXiDt0LLAoeItlT021Q9U5CYHb8E58HbvVcKiCD17jy-XDd0UbXrtTd8StZffNfVq2Y5rivJNvEdPPSEfNACBkhDVF10voTlYota7a-qR3UqpIzfHiTFPaXtxGP8xEckVMDXkhW5A98CqV0cj6_QRHIyovEwHA9VkTgGHjUbARCLMq1BHr4pLaHYgBPFMPP24cOeGnMAQsrOov_pbUxQOlstxQufGyoLGpKQTBxKP1Ovd9XFi3dV-FFrr_2CI0GYDAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 399K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 04:27:25</div>
<hr>

<div class="tg-post" id="msg-18500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بندر یدونه زد ملت نیم متر پریدن
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18500" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از سیریک موشک پرتاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18499" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حملات موشکی/پهپادی سپاه شروع شد و تمام پرواز ها رو هم کنسل کردند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18498" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18497">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام اعلام کرد تفنگداران دریایی آمریکا از یگان اعزامی یازدهم نیروی دریایی (11th MEU) در
۱۶ ژوئیه
عملیات بازرسی و راستی‌آزمایی (هلی برن)را روی نفتکش
M/T Wen Yao
در دریای عمان انجام دادند. به گفته سنتکام، تاکنون نیروهای آمریکایی در چارچوب اجرای محاصره دریایی علیه ایران،
۳ کشتی تجاری
را که قصد عبور از محاصره را داشتند تغییر مسیر داده‌اند،
۱ کشتی
را به دلیل عدم تبعیت از دستورات از کار انداخته‌اند و
۱ کشتی دیگر
را نیز برای اطمینان از اجرای کامل این محاصره بازرسی کرده‌اند. سنتکام همچنین مدعی شد
تنگه هرمز و آب‌های اطراف آن همچنان برای کشتیرانی آزاد و باز است، به‌جز برای شناورهایی که قصد نقض محاصره دریایی آمریکا علیه ایران را داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18497" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برق مناطقی از کیش قطع شد @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18496" target="_blank">📅 01:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۷-۸ انفجار رگباری بوشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18495" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شاهزاده رضا پهلوی در مصاحبه تصویری با شبکه آی24 فرانسه گفت، امروز پس از ۴۷ سال تجربه جمهوری اسلامی، بیش از هر زمان دیگر آشگار شده که بدون تغییر این رژیم، دستیابی به ثباتی پایدار در منطقه ممکن نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18494" target="_blank">📅 00:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پدافند تهران درگیر شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18493" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18492" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر 50 هزار نیرو در خاورمیانه داریم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18491" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فارس: حمله به پل خمیر ۶ کشته و زخمی داشته
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18490" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ حدود ۳ ساعت دیگه صحبت میکنه
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18489" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W831MBi7xOexlH3x5HmprsC1Ng2K3i-BeW-SxfKWwLHQQO6M5d82jJbbNGnwuLMZcJAvRRqRjL66ps0kGW346gUb0LSrvXN7mxU5BEWeWnD4D_ot6Y3mSB91XeIOULBTiQtYvGeU6dD5ssIZZiAhTgF64JcWEGuFlbxLKa7IkxjRMKiX-QvX7wMAwcAvwA4CJM-BYLgLkYPFdb643z3zCKfXJoUF48EmH1nZeogjlrtkrhfgfMXzg9-2FmaqYGlnPozkOAV6FO6VwJnilM0IxMfCPdMH2atf2UWb3BAYjASBplf8bAI1PRkJLoB22yderhWURQj4xowBNeQPwhH3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18488" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049770daef.mp4?token=rCfDH3x3FJeu5C6Tw76B1fWpzz-3pX0fZV_EesNTkVuy4Amc_9O6bYa7-IhvjPV2F_vpUAm2HXIHvkLZLS6-KeMiUfY81os92npM7YlY9FRmx4Hut0Ryge9StS2C8Gv-gss4czxzDQHiSInR9zgNx4NiosNXN7F2f3pcqi-GD6Z8azUSyX-E_r0-DkKgloCp3kjGcl50HGMXpHUewZJpZsGkYNue4xiTOKCLUbL1c26fl2Di7QcbloJmlC-iHoazek8gcCjPZs3jupshejlTg0Bp-Tw63Q8MsrZKSXAg2wv0FxXo-ZXGoPww5io5oPjlT0OTtpGEuenyzvlgepwReg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049770daef.mp4?token=rCfDH3x3FJeu5C6Tw76B1fWpzz-3pX0fZV_EesNTkVuy4Amc_9O6bYa7-IhvjPV2F_vpUAm2HXIHvkLZLS6-KeMiUfY81os92npM7YlY9FRmx4Hut0Ryge9StS2C8Gv-gss4czxzDQHiSInR9zgNx4NiosNXN7F2f3pcqi-GD6Z8azUSyX-E_r0-DkKgloCp3kjGcl50HGMXpHUewZJpZsGkYNue4xiTOKCLUbL1c26fl2Di7QcbloJmlC-iHoazek8gcCjPZs3jupshejlTg0Bp-Tw63Q8MsrZKSXAg2wv0FxXo-ZXGoPww5io5oPjlT0OTtpGEuenyzvlgepwReg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم زیاد از پهباد شناسایی در اندیمشک نزدیک پایگاه چهارم شکاری
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18487" target="_blank">📅 00:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حمله آمریکا به یک نقطه در اطراف شهر بستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18486" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برق مناطقی از کیش قطع شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18485" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاریCBS به نقل از مقام آمریکایی:
دستورالعمل‌های مربوط به حملات آمریکا به‌روزرسانی شده‌اند تا شامل پل‌ها و اهداف ارتباطی و تدارکاتی شود، با هدف افزایش فشار بر ‌رژیم ایران!
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18484" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWPz4NDqOZkyyNYzeyHoVxUy5ymLlUbcRs4XEX3gBD9oXEjYxhbILG71oSEBKMDCxqaE8-26uCgRJ_RjHs4QacjbBo3iPf4D4uR4VwhJdbIdoaZrKekxeS1AlVQYKg7oTVzbehzGZ1xMK_rzAro5FFuPK0PZJw7KTD8e939xoXoGQrGuG1FA9IB1bLQHjYaOkcqiwQ-2mCCJkBLkeDG20m-WDxkXz1Vl6Y-TyEP0dWmgmKDA9W_Kmof4PskCwF5tX3lQrBkkOKkMB192t9cx_x81tYO7HO6bB_1gU6FB7GN0rtQROMea_yrgzbOMkrVHK4UWUpHQd76Kv3o2dERjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه F35 رادارگریز آمریکا داره فرود اضطراری‌ میکنه
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18483" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">راه آهن بندر عباس رفت رو هوا
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18482" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قشم رو زدن ( گویا فرودگاه)
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18481" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شکارچی سخنگوی ارشد نیروهای مسلح : مدیریت تنگه هرمز به قبل از ۹ اسفند بازنخواهد گشت
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18480" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صداوسیما:تاکنون دو پل استراتژیک مواصلاتی بندر عباس، شیراز، لار و بندر خمیر بمباران شدند و تخریب شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18479" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجار سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18478" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یاشار همین الان صدای انفجار بندرعباس کنار پارک جنگلی
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18477" target="_blank">📅 00:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=fY309ajTybgjpg0N-Zm-zRjldb08n00wxpxClx2JfWHUbfQcnUjP3DVdLyuS9nguD9uV0sHJn4kHZZXReqX9eGtmHg69hku5eA6VrLcSFsWQNeik9o7Dw8TvIcSclTI1XOqKeC8Mnn7fvIS8uB28tckXj-JmMveniD7k0aApuJ1RLTYavhHdmTQTZ3t1L02hWnUIz4UOdNmumLfl6PUzfX18esKGIulrcyd4wgJkyta9X7n7beAISQkuhaoQcqdXufQnxBuqCfBfPCtIftx0KPE8gnRKGkdx31VPgNxXqDHZPhXQGr2my5DXDqzc8iqH7h6nkpiLLthPED6w48C03YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=fY309ajTybgjpg0N-Zm-zRjldb08n00wxpxClx2JfWHUbfQcnUjP3DVdLyuS9nguD9uV0sHJn4kHZZXReqX9eGtmHg69hku5eA6VrLcSFsWQNeik9o7Dw8TvIcSclTI1XOqKeC8Mnn7fvIS8uB28tckXj-JmMveniD7k0aApuJ1RLTYavhHdmTQTZ3t1L02hWnUIz4UOdNmumLfl6PUzfX18esKGIulrcyd4wgJkyta9X7n7beAISQkuhaoQcqdXufQnxBuqCfBfPCtIftx0KPE8gnRKGkdx31VPgNxXqDHZPhXQGr2my5DXDqzc8iqH7h6nkpiLLthPED6w48C03YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18476" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18475" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18474" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=nbtYMNNU9gaVpDss9voWQBzou-pI3BF6QI_bT1Ah_NOAzW9dopiZ6D4iHYqiXHWKKPuyl_92y7AKZdTmdCt0dWWOkM4fkqZ3bud37apaCeTHHoxSI2Mp3g7XQIG4NOAbnxlThlOdq4m7BTR7GN2kGHNpc4Q2r50F5lParIt9GN6JkTw5hhX-V9oCn2Uy1p8olAeg3Il1V4TIR-VPiOeoLjagdF0t3_0oN3EDmwb08qFJ6EBgsF4XlZjmwjVvFDLfs1sVb_D88lzm1t460QJEz3-KK_T9GbMKxgESHAOPssrJV2XhG5qneCh-5t_HmRp9qERHY9we7iK6xmsKlM3fCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=nbtYMNNU9gaVpDss9voWQBzou-pI3BF6QI_bT1Ah_NOAzW9dopiZ6D4iHYqiXHWKKPuyl_92y7AKZdTmdCt0dWWOkM4fkqZ3bud37apaCeTHHoxSI2Mp3g7XQIG4NOAbnxlThlOdq4m7BTR7GN2kGHNpc4Q2r50F5lParIt9GN6JkTw5hhX-V9oCn2Uy1p8olAeg3Il1V4TIR-VPiOeoLjagdF0t3_0oN3EDmwb08qFJ6EBgsF4XlZjmwjVvFDLfs1sVb_D88lzm1t460QJEz3-KK_T9GbMKxgESHAOPssrJV2XhG5qneCh-5t_HmRp9qERHY9we7iK6xmsKlM3fCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس ۳ تا پل رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18473" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9lc5WTj2so5AdkApBBnInjIQJvR86EJ1iRrnFaqUrsNu2r0xdnzdFkXGwHV0p75dA21PVv1HmyQ0Xe18JSj5VftoLT2yYVxqT4SeR4efnEew3njIohU5xxvylPuO0Ea7hrhR28XPjFe1U6jAor_k8tf5KuGruRYdmuQgIDUDrE3jaQJfNQAFoLFKYimz0P4IBCIfv16ovihL33-HszgfIOY2DE9JY-Mm6VHOW-z6AROCZjXUyESob-58Dh5y_kqh7BQ7UX0LBm7bGdeVSw7otiRxYilMzEclBMgW9trLOmMi_a-BNRheyay10nZ8FE-6KVeSVDEsMz8dsBDqBbKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه ایرانشهر
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18472" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مهر: دقایقی پیش، صدای حدود ۶ انفجار پیاپی در حوالی شهرستان حمیدیه شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18471" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=Ze3iTmgblj6kC53E6OyA6ekBjG6R3eWlwGJbI-IXs40ZYYoITAf2vGtI8x7jJWOD0WvcbL6vJXgZIkE3kIRaE3-u30PfJWTaXEYbzg-mTa3eUnGw7Jqd4mxYNkX3I4tW5MjT91YYffTeh01JKSyP41Fl7EDMGnPZ3Fb0WF56UYxXRB--7mxKE3O9v_i3TtYKGPXqm6T0ZpnuFqvlIgj6hHO4V18ohk_b2umhHiLV9fn00-F4D3mkZZ0m7ULusLK6zufqldiDN-qykqmM7M7WlpqxJZyEcifsaIdiCAwlkWGDDmrLRR3PxerqOCSxHEfCAY6ZsGKErcJiPrC4XHZEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=Ze3iTmgblj6kC53E6OyA6ekBjG6R3eWlwGJbI-IXs40ZYYoITAf2vGtI8x7jJWOD0WvcbL6vJXgZIkE3kIRaE3-u30PfJWTaXEYbzg-mTa3eUnGw7Jqd4mxYNkX3I4tW5MjT91YYffTeh01JKSyP41Fl7EDMGnPZ3Fb0WF56UYxXRB--7mxKE3O9v_i3TtYKGPXqm6T0ZpnuFqvlIgj6hHO4V18ohk_b2umhHiLV9fn00-F4D3mkZZ0m7ULusLK6zufqldiDN-qykqmM7M7WlpqxJZyEcifsaIdiCAwlkWGDDmrLRR3PxerqOCSxHEfCAY6ZsGKErcJiPrC4XHZEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18470" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18469" target="_blank">📅 23:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18468" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18467">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار اهوازززز بازم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18467" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18466">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b364528971.mp4?token=P992DsRfI0KccSa0GXyBDkF_rFKU8lFXekebEgvcdoIVRhIefDwrNvFy3_RR-wBJRRzbIuqZTiugGlHKrQ3RN8KqcV9wZMd9lLs6__7PXbbLDvLy5GNOVb25Sa0H_ONpd8IuQav88KvlAzNJpCBUy_qwLLdNnheUg65BioenUKCI2H6Gxh4Xw3oA-bXWuQrMTftU9RKQwi35VBPV0tYyqj-FCo-F1zkIAubBAbBrN_UcAELD-SwAF0r69pLlSuhLTQDls9m359tHYU46_TEkkFMT87wpiwrh-3kVpImpmpLf2dACT0-tytQisAT3046azbI7pciPGfDoYtYDHNTgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b364528971.mp4?token=P992DsRfI0KccSa0GXyBDkF_rFKU8lFXekebEgvcdoIVRhIefDwrNvFy3_RR-wBJRRzbIuqZTiugGlHKrQ3RN8KqcV9wZMd9lLs6__7PXbbLDvLy5GNOVb25Sa0H_ONpd8IuQav88KvlAzNJpCBUy_qwLLdNnheUg65BioenUKCI2H6Gxh4Xw3oA-bXWuQrMTftU9RKQwi35VBPV0tYyqj-FCo-F1zkIAubBAbBrN_UcAELD-SwAF0r69pLlSuhLTQDls9m359tHYU46_TEkkFMT87wpiwrh-3kVpImpmpLf2dACT0-tytQisAT3046azbI7pciPGfDoYtYDHNTgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس جهنم شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18466" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بوشهررررر سنگین
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18464" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قشم روستای مسن رو زذن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18463" target="_blank">📅 23:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همدان ، احتمالا نوژه رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18462" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فرودگاه ایرانشهر رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18461" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روابط عمومی دانشگاه علوم پزشکی هرمزگان:
در پی حمله دقایقی پیش به محله تپه الله‌اکبر شهر بندرعباس، تاکنون ۷ نفر از هموطنان مجروح شده‌اند.
بلافاصله پس از وقوع حادثه، تمامی نیروهای امدادی و درمانی دانشگاه علوم پزشکی هرمزگان در حالت آماده‌باش کامل قرار گرفته‌اند و اقدامات درمانی لازم برای رسیدگی به مصدومان در حال انجام است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18460" target="_blank">📅 23:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی سنتکام: ما در پاکسازی مین‌هایی که سپاه پاسداران در هرمز کار گذاشته است، به پیشرفت‌هایی دست یافته‌ایم و ادامه میدهیم
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18459" target="_blank">📅 23:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تسنیم: دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18458" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سلام یاشار پایگاه هوایی بندرو رگباری داره میزنه الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18457" target="_blank">📅 23:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قشممممم بد زددد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18456" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دارن گرم میکنین ۱ ساعت دیگه میان شهر های عمیقتر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18455" target="_blank">📅 23:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18454" target="_blank">📅 23:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بندر عباس میگن عباس هم رفت فقط خود بندر مونده
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18453" target="_blank">📅 22:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اهواز باز زد سه باررررررره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18452" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18451" target="_blank">📅 22:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش انفجار در جم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18450" target="_blank">📅 22:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18449" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کبودراهنگ همدانو کوبیدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18448" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=I7n-CT_iOvbwx6JmjPP6u0CXMiNZVP8fJl8-x-iSNgW4Ji6hwyJo1LY52jZwgiOShrRpG0kMz80RZsC9PSgTmuTew50GBHcKuWxni1jveX7gPUB2fQdAHsQZKE_8Nd4FgqxO5lVJVwYSYQ-0bGnJ3uNcyhFrSeP32S07Q1mDPlklynKZwp9tny74A6FcBMHgh41mChBLH22QgZuQp2Td1w-LQlDiuFYAg4ofKZnfXhy9gzlEo-srtjfCpuX76Vd9mwHImo78APGEJTqK659utv63copRzwIz9jHL_pSgGPbDA7jnR4L1iIIJ5RDt5sOBsdHjWU2ZYgqp0x7Df4Oq-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=I7n-CT_iOvbwx6JmjPP6u0CXMiNZVP8fJl8-x-iSNgW4Ji6hwyJo1LY52jZwgiOShrRpG0kMz80RZsC9PSgTmuTew50GBHcKuWxni1jveX7gPUB2fQdAHsQZKE_8Nd4FgqxO5lVJVwYSYQ-0bGnJ3uNcyhFrSeP32S07Q1mDPlklynKZwp9tny74A6FcBMHgh41mChBLH22QgZuQp2Td1w-LQlDiuFYAg4ofKZnfXhy9gzlEo-srtjfCpuX76Vd9mwHImo78APGEJTqK659utv63copRzwIz9jHL_pSgGPbDA7jnR4L1iIIJ5RDt5sOBsdHjWU2ZYgqp0x7Df4Oq-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله موشکی آمریکا از کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18447" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجار در قشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18446" target="_blank">📅 22:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجار دوباره بندر عباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18445" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار جزیره لارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18444" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اهواز ۷-۸ انفجار در مجموع
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18443" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اهواز رو بازم زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18442" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بهبهان رو زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18441" target="_blank">📅 22:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجار سنگین اهواز
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18440" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0125430a.mp4?token=TQqLxGIgmVsob4CIV3qLC5iab6hjkTJSixBfxMQ3sOJBfD98tg0Q3JJwXdWZKIG7EIKY8iXVQNCAk6xVI9c_ksEyTv67zGeQwdbMQKLHiZdhihsk5GLT3LaNl4fai0yCVtyyqOfYPoTT8xuwxlJa1gE_84hqbst_aAav5JjFBLjAhDckzSIgNKpHgOMXMJoOwUZMvS5szQ9J2SJvxEYnrTUbMG3I8wgL-OpfIxRfA3Lt8xxO6jjdOyKvbtoMx0w74OOKHWym7IP4td8t5cypCZgM1H2NUKkP1O6Oh3RBFXzruzvAZxgN3Wm49_RcPhjy6ARoUaaMwp7liKnBuOo6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0125430a.mp4?token=TQqLxGIgmVsob4CIV3qLC5iab6hjkTJSixBfxMQ3sOJBfD98tg0Q3JJwXdWZKIG7EIKY8iXVQNCAk6xVI9c_ksEyTv67zGeQwdbMQKLHiZdhihsk5GLT3LaNl4fai0yCVtyyqOfYPoTT8xuwxlJa1gE_84hqbst_aAav5JjFBLjAhDckzSIgNKpHgOMXMJoOwUZMvS5szQ9J2SJvxEYnrTUbMG3I8wgL-OpfIxRfA3Lt8xxO6jjdOyKvbtoMx0w74OOKHWym7IP4td8t5cypCZgM1H2NUKkP1O6Oh3RBFXzruzvAZxgN3Wm49_RcPhjy6ARoUaaMwp7liKnBuOo6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از بندرعباس؛ مجدد همون دکل رو با 4 تا موشک زد
اینبار واقعا شدید بود
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18439" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه های سعودی : شنیده شدن صداهای انفجارهایی در بندرعباس، بوشهر، چابهار و کنارک
@WarRoom
.
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18438" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش انفجار‌ در کیش
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18437" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Z8Yd_mObpHbtC7yChfT3TgpLhbkxsZr_se8ptr8gXIYZLPeDCQvw_9-pkunN62nfZ0LBY7aIRCVQEayRacs8DqLL7YLIxNDsh6QrAdZH5VZA09hUi_ljJqInRYKRJInb6G0U_vnRfwBiYxaePSCd_d2CaDgPH-sgPDitDnrTw-VNdq2fI_OdqOW8hOunpVeRTAY2ncXQ5FB-94DDm9WlWa5wRoHYsGdiii-WcLzWeVHVH-8ot3rXZUfeCi96F0eKoMczMEha4MQsbigQsT0Jj1YHg83rfPWDouvD3lvFqizy3keoeGH-tGlHub0oIxDN6fCQ19MH_e83sPL18VBwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Z8Yd_mObpHbtC7yChfT3TgpLhbkxsZr_se8ptr8gXIYZLPeDCQvw_9-pkunN62nfZ0LBY7aIRCVQEayRacs8DqLL7YLIxNDsh6QrAdZH5VZA09hUi_ljJqInRYKRJInb6G0U_vnRfwBiYxaePSCd_d2CaDgPH-sgPDitDnrTw-VNdq2fI_OdqOW8hOunpVeRTAY2ncXQ5FB-94DDm9WlWa5wRoHYsGdiii-WcLzWeVHVH-8ot3rXZUfeCi96F0eKoMczMEha4MQsbigQsT0Jj1YHg83rfPWDouvD3lvFqizy3keoeGH-tGlHub0oIxDN6fCQ19MH_e83sPL18VBwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس هم اکنون
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18436" target="_blank">📅 22:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18435" target="_blank">📅 22:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Ans5omMdf9ayrMQlOrzQCFyFQIH2G4JRV_EbObEC8-KpgKu3jWD2Ut92N60tUAtM83eVliOD_b7JiU9jUWKNXQTK3Yj0b5hdy7SBbCroXk9PJRjW9Rr1O_q69_rViIHgXmIxKwPItiKh7afmDqeIdCLnSovkm2qAVpzN8QwdnHab-dxxbsu0wVgJ2KdNiqc7l-AhUHadAo3SOh24tb_yGky1Mq-Nbse9SRZZCZETz5Only3X8ko5B4s-jbNzlTsTrEaK6ah_Mzs1B_dgfxe2ejh7rlYi_skhcaJKpKEfQKGtjBGlGoAQbu7KTS8CRshrSGUXSXY5N5LoamsdQiJscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Ans5omMdf9ayrMQlOrzQCFyFQIH2G4JRV_EbObEC8-KpgKu3jWD2Ut92N60tUAtM83eVliOD_b7JiU9jUWKNXQTK3Yj0b5hdy7SBbCroXk9PJRjW9Rr1O_q69_rViIHgXmIxKwPItiKh7afmDqeIdCLnSovkm2qAVpzN8QwdnHab-dxxbsu0wVgJ2KdNiqc7l-AhUHadAo3SOh24tb_yGky1Mq-Nbse9SRZZCZETz5Only3X8ko5B4s-jbNzlTsTrEaK6ah_Mzs1B_dgfxe2ejh7rlYi_skhcaJKpKEfQKGtjBGlGoAQbu7KTS8CRshrSGUXSXY5N5LoamsdQiJscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18434" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار چابهار
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18433" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بندرعباس چپ و راست آمبولانس و آتشینشان میره سمت شرق بندرعباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18432" target="_blank">📅 22:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">غروبه هرمز @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18431" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام : در ساعت
۲:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
امروز
(۲۱:۳۰ به وقت تهران)
، نیروهای ایالات متحده
موج جدیدی از حملات
علیه ایران را آغاز کردند.
این حملات برای
پنجمین شب متوالی
با هدف
تضعیف بیشتر توانمندی‌های نظامی ایران
در حال انجام است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18430" target="_blank">📅 22:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش انفجار بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18429" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لطفاً تا فردا صبح هیچگونه سؤال سیاسی اجتماعی و تحلیلی نپرسید. لطفاً در مورد اینترنت خبریی ندهید. لطفاً صدای جنگنده ها را نگید. لطفاً فقط گزارش صدای انفجار رو بدید و تصاویر و عکس. همچنین پیامها را فقط همیشه در یک متن بفرستید، نه ده پیام جداگانه.</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18428" target="_blank">📅 22:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vff7fqWUCnMZ6Uy04y7_PHhN7DwDWqG2n98emQz-jINEel7OdapTCcWqeo8_HQAEYoQwHtIrcl9KxtCx6iqEuWk06OyiTJCZOxX1HHHfmcDRVHvMWiyeCRq0-T5JpzzhKDGdw26I9SP5j_hzIZAf4rVxYZYVWlMmxaHQJrd5M4UNsHP2V0aylhj2Ku98B9_YjIDY2Nu_AzP1bJ6oMecR_s4JnhL3thIdFgZbZa2zXUnuPKctBihALg5U8xpn5BRWfUptzHROHYvloeTTzw7gtau7YK9NNqbVU3cDRgY53IpriqUpJ0kwOXZkr8NHXgHX7wIerL3IxWi65nwa2AyNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18427" target="_blank">📅 21:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18426" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادعای ترامپ مبنی بر آزادی یک زندانی آمریکایی از ایران تکذیب شد
ترامپ در حالی این ادعا را مطرح کرده است که با توجه به بررسی‌های صورت گرفته هیچ زندانی محکوم و یا جاسوس آمریکایی با مشخصاتی که ترامپ اعلام کرده و یا با هر مشخصات دیگری از زندان‌های ایران آزاد و یا تبادل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18425" target="_blank">📅 21:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بندر ادامه دارههههه ۵-۶ تا شد</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18424" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ولی باید ببینیم امشب به اصفهان میرسه یا نه الان مرکز هدف اصفهانه کوه کلنگ</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18423" target="_blank">📅 21:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار همدان
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18422" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تهران رو شاید بزنند ولی‌ نه به حالت زارتان زورتان به همون پارچین اینا بزنند فککنم</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18421" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۲ بار قشمممممم
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18420" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قشم رو زدنننننن
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18419" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بندر عباس زارتان زورتانهههههه
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18418" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
) @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18417" target="_blank">📅 21:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
حملات امشب شروع شد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18416" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شروع انفجارات بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18415" target="_blank">📅 21:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تناقضات میان ادعاهای ونس و ترامپ نشان‌دهنده این است که در یک جبهه هستند
خبرنگار:
درباره ایران: رئیس جمهور ترامپ اخیراً گفته است: «از نظر من، سروکله زدن با آنها فقط اتلاف وقت است. آنها دروغگو هستند. یک جای کارشان می‌لنگد. آنها عوضی هستند. آنها آشغال، بیمار، شرور و خشن هستند.»
سپس ونس، معاون رئیس جمهور، دیشب به جو روگان گفت: «من از آمریکایی‌ها - و صادقانه بگویم از مردم کشورهای دیگر - که می‌گویند نمی‌توانید با ایرانی‌ها مذاکره کنید، بسیار ناامید شده‌ام.»
خب، پاسخ شما به این تناقضات چیست؟ فکر می‌کنم با توجه به پیام‌های متناقض، می‌توانید درک کنید که این موضوع چقدر برای آمریکایی‌ها گیج‌کننده است.
کارولین لیویت:
رئیس جمهور و معاون رئیس جمهور دقیقاً در یک جبهه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18414" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18413" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
)
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18412" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۵ اسرائیلی: ایالات متحده در حال آماده‌سازی برای گسترش حملات خود علیه ایران از نظر دامنه و تعداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18411" target="_blank">📅 20:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGq6hpcIV9-Qt4BWtmnDDs40F9_LKhjsehha3obVvnMokQgDygUaPY_BXoQRM0mDis69PEBF8rL4b2dpunJ2h95XViDXtIU6Y7eiZD4ZyvBO2jkuWjyngGsvGQyWHtRy46rXYlBtas_mJPYX9Zpk_iRnPmcrH0LE96K00kd7d3BT88guCQ4QE006YzVwiirniahYmK_18uZHgDy9uJaipKoQtRp93WHwCistUEQ0idk6CF_ZzNhqibdF11ZxTLDMDyaGoC5No2A-m-sc1N8NLV8WRuDeuuFqvnJ6zoXeqX0Sp3TI1GCU9xyG7xRUodvFX6PgQpqnA_uTJb_1DcTbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : فرمانده اطلاعات نظامی حماس در تیپ خان یونس را با انفجار خودرو در جنوب غزه به هلاکت رساندیم
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18410" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اتوبوس …. ببوس
😂</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18409" target="_blank">📅 20:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18408">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز:حمله بزرگ علیه ایران نزدیک است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18408" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18407" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز رو تبر‌ زدن خبر دبی فیکه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18406" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق جنگ با یاشار : میزو بچینم برای امشب</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18405" target="_blank">📅 20:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری فارس:حملات هوایی دقایقی پیش چندین نقطه در اطراف بندر عباس را هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18404" target="_blank">📅 19:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شاهزاده
رضا پهلوی:
سرکرده‌های رژیم آخوندها در تهران و پناهگاه‌های امن پنهان شده‌اند، اما سربازان وظیفه را در پادگان‌های آسیب‌پذیر رها کرده‌اند. او با بیان اینکه حکومت جان نیروهای نیابتی خود را بر جان ایرانیان ترجیح می‌دهد، از سربازان خواست جانشان را برای این نظام به خطر نیندازند و از خانواده‌ها نیز خواست تا حد امکان مانع اعزام فرزندانشان به خدمت سربازی در شرایط کنونی شوند. شاهزادت همچنین از اقدام مردم زاهدان و مناطق اطراف در کمک‌رسانی و اهدای خون قدردانی کرد و تأکید کرد جوانان ایران نباید قربانی بقای رژیم شوند، زیرا آینده کشور به این نسل نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18403" target="_blank">📅 19:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حسن روحانی : قبل از آخرین جلسه ای که قرار بود تمام مسولین نظام خدمت رهبر برسند (رمضان ۱۴۰۴) احساس خطر کردم و پس از تلاش های فراوان و فرستادن پیغام های مختلف برای شخص رهبر و تیم دفتر ایشان، موفق شدم جلسه را لغو کنم
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18402" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان ، خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18401" target="_blank">📅 19:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صداوسیما: عصر امروز یک پرتابه دشمن به روستای مسن قشم اصابت کرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18400" target="_blank">📅 19:16 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
