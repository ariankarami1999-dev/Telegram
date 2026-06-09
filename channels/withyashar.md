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
<img src="https://cdn4.telesco.pe/file/fHPZHJZtUXiINapr0PgZLJZIbrSzzD-MoaifJm43THw8FArR_M5Qyl_ud3JLhGyoGRnJEEZqnYuYcjomCESd-HE8MlE_gz_F_LupMoq2exmF85qflGwbIyBGKlDVM3GF7Jt9PRthbiMs_V-tWA_AZcz0w9iabsvPmKs1TX6KaY4dcSFYn8lZJCBC9B3Fp8YocUP_HfpOMsshc4GDmu2KPunbNsXXJCeAgsWz_--tEhOiRHpupkenLXoJXIxf_VpZGM2GUuXObAXtQS4nVHRHiSxgJq4h4Sy4XYPs1VlBmc6ulghQ8K0ba0C-UGotMfVRM_T-Fp9I5AEUBE4LdqtvwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 308K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 01:35:45</div>
<hr>

<div class="tg-post" id="msg-14227">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اتاق جنگ با یاشار : خدای من و شما شاهد است که هیچ ردبولی رو بیهوده حروم نکردم
🤣
✌🏾
@withyashar</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/14227" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14226">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مقام ارشد آمریکایی به باراک راوید خبرنگار آکسیوس: عملیات ادامه داره و آماده‌ایم برای چندین حمله دیگه.
@withyashar</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/withyashar/14226" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14225">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش
انفجار در اهواز
.
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/14225" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14224">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/14224" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14223">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سید مجید موسی : ‏و ما النصر الا من عند الله العزیز الحکیم
@withyashar
🤣</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/withyashar/14223" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14222">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/14222" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14221">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هم اکنون بمباران مواضع حکومت طالبان افغانستان توسط F16 های ارتش پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/14221" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14220">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ به ای‌بی‌سی نیوز:
من به پاسخ قوی اعتقاد دارم و این رویکرد من است. ما توافق بسیار خوبی با ایران داریم و فکر می‌کنم همینطور هم خواهد ماند.
@withyashar
یاشار : زبانم قاسمه کتلته</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/14220" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14219">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک مقام آمریکایی به فاکس نیوز گفت: حملات هوایی علیه ایران «ادامه دارد» و اهداف شامل پدافند هوایی و تأسیسات راداری است.
@withyashar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/14219" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14218">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش ها از شلیک موشک‌های سپاه از کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/14218" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14217">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق جنگ با یاشار : امریکا و اسراییل به طور هماهنگ و گازانبری به ایران و لبنان حمله کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/14217" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14216">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۳پا :
حملات سنگین علیه امریکا در راه است..
@withyashar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/14216" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14215">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کشورهای حوزه خلیج فارس در حال بستن حریم هوایی خود میباشند.
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/14215" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14214">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار در ضاحیه بیروت  @withyashar
🇮🇱</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/14214" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14213">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری تسنیم:
آغاز حملات ایران
جمهوری اسلامی: همانطور که چند ساعت پیش هشدار داده بود، پاسخ قاطعی به تجاوز آمریکا خواهد داد که تحت پوشش سقوط هلیکوپتر آپاچی انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/14213" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14212">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">از خوزستان موشک زدن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/14212" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14211">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجار در ضاحیه بیروت
@withyashar
🇮🇱</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/14211" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14210">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤣
🤣
🤣
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/14210" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14209">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سامانه‌های دفاع هوایی دوباره در بندرعباس، قشم و سیریک فعال شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/14209" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14208">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فهرست اولیه اهداف:
– پایگاه دریایی سیریک
– پایگاه دریایی جاسک
– موقعیت پدافند هوایی بندرعباس
– باتری موشکی ساحلی میناب
– باتری موشکی ساحلی قشم
– بندر قشم
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/14208" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14207">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مقام آمریکایی: نیروهای ما به حملات خود علیه ایران برای دفاع از خود ادامه می دهند و عملیات همچنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/14207" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14206">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صداوسیما : پایگاه های آمریکایی رو هدف قرار میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/14206" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدا و سیما می گوید دست کم صدای 6 انفجار در جزیره قشم شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/14205" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">روابط عمومی نیروی هوافضای سپاه اعلام کرد تا لحظات آینده پاسخ سنگین به اقدامات خصمانه دشمن داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/14204" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/14203" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14202">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش‌ها از هدف قرار گرفتن دکل‌های مخابراتی درقشم
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/14202" target="_blank">📅 01:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
هم اکنون ترامپ به ABC درباره حملات ایران:فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم،
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند،من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/14201" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارها در قشم، بندرعباس، سیریک و جاسک
@withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/14200" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال 14 اسرائیل: ترامپ نتانیاهو رو قبل از آغاز حمله در جریان قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/14199" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14198">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۹ انفجار بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/14198" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14197">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjIfOz_vtLhQyr51awFJtE2LNdslkSugSgWHhOeRigWMXXYJyiEM_DCg2xOWOyMOIEqyUwZxczVnH843VuHOox2FTGl3hcj2OJ6I0rublrrrD6bSB54d96PEbrSeOp5Kww5WVDj3tHtqZgVLi2GSaUAqdkAUCFVnkLCZkVgU9TW-uoTV06U_s2jDeDPjOBlxp0IvcN1COjpl101KenvSoKb88Y8T-I-f-MYUxnq5sCLb8pxXE40HjhFvoEzYhpehmA8x_hvrzAln3SfqF3Vjy7hVvOPvpAQ-6HbkPI-1Ih4V5Q_sEQKxLWt2fMHtGczKM1meGHNekkODbdDG-tAgUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@withyashar
شکار‌ لحظه کردم</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/14197" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14196">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">طبق گزارش ها تاکنون حملات در جنوب ایران متمرکز بوده است.
هم‌اکنون پدافند در جنوب ایران مشغول دفع حمله است
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/14196" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14195">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ارتش آمریکا از شلیک گسترده موشک های کروز به سمت ایران خبر می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/14195" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14194">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مسیج های زیاد از انفجار‌ در ‌سیریک @withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/14194" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14193">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOBas6mCMu1yRIXMiuaNcKa9Yy0pLAsX7vJr0s6GpBuGFHVTUyIo5mJuwNoJvHvRnNvoQx6q4wjGuBE8BFLwuiUpzdhqahfNBGOJfcdT3ziiaJNMQ-F6JuvEsuHhO2R48JD-XR17amj-IMARq8QmQGKDZw8v2y0nvqYBDdje8khkZ2G5MCchisBXZBdHIo0Z_6EgcnSJL_8B1MDCdIpjssb67Vy8S5qZeaxGo2Sxbkj5oBONFY1pUzSDr1IuWXL-NQMcP0tFnCL1pncgjGcSkdvGiztk7CfB-b8i2BYGldF1E2TlWdgu9_u21mNXur8wvBVM3zvM-fPrdI0t-zvuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری : نیروهای سنتکام به دستور فرمانده کل، از ساعت ۵ عصر به وقت آمریکا، در پاسخ به ساقط شدن بالگرد آپاچی ارتش «حملات دفاعی» علیه ایران شروع کردن و این یه واکنش متقابل و متناسب به حمله ایران بوده.
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/14193" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14192">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/14192" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش‌های غیر رسمی از هدف قرار گرفتن پایگاه شهید راهبر در میناب
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/14191" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرنگار کانال 14 اسرائیل:
هرچند امیدوارم اشتباه کنم ولی پیش‌بینی‌ من اینه که ترامپ در پاسخ به سرنگونی بالگرد آمریکایی، یه حمله‌ جزئی و نمادین انجام میده؛ مثلا یک ایستگاه راداری و چند سکوی پرتاب ضدموشکی در منطقهٔ تنگه‌ هرمز رو میزنه.
یعنی حملاتی از جنس همان حملاتی که قبلاً هم چند بار در جریان آتش‌بس دیدیم، نه چیزی که جنگی رو با ایران شعله‌ور کنه.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14190" target="_blank">📅 00:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش های زیاد انفجار هم اکنون از قشم و بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14189" target="_blank">📅 00:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14188">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIXv7hPsm6TTGawszdfxUXX2EuNU5ikRDq2_j5LYvGZp6_FywzctG6JwlaMvaduNHqKADgz-cMqZg2IqBfk6iPtaPwNCeiXQhjNrIfn4EM-GivNDFaPX6OrVtgW45JlYxUBMnsKjp4qWDt1hH8ezRr36w5yVjtiYjIKswCH490mtieyXn2AHsDdwKjdzMCHeFqkUjKuAj8cDDdQr3M4mheIryao_gHnYxPVuBOFN2cNGoOMDFuL8sBoiL1e7RSvjkVdc-4G16RBNfcg45l-bW8TnAynhuNI_xjxkD_9T-TMh5zLJKwBX8Hn7RD151w5XLZpAqNEUWku9hc1ks8Wkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون انبوه هواپیما های آمریکایی در جنوب ايران
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14188" target="_blank">📅 00:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14187">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مسیج های زیاد از انفجار‌ در ‌سیریک
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14187" target="_blank">📅 00:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/14186" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ان بی سی : فرمانده سنتکام کلی اطلاعات به اعضای دو حزب ارائه داده که همه قانع شدن حمله ایران به هلیکوپتر اپاچی کاملا عمدی بوده و باید تلافی کنن
@withyashar
این اولین باره که دموکرات ها تایید میکنن حمله به ایرانو</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/14185" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14184">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ با شما : صداهای مشکوک اطراف اصفهان
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14184" target="_blank">📅 00:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدا و سیما : به جون مادرمون ما هلیکوپتر نزدیم اصلا امروز کلا نبودیم
🤣
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/14183" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14181">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aca1a7b7a.mp4?token=Vg8UKoOCluMwEqCnzfKpGldM7V1NIESP1E-az7p8jjNO9v3RsWapZZ710fh9sxA2Rb-VjnEgYZGMdYWm_-YbZZVmSnEUogzCcVADoqdeZp1cltnDRgHQikR7jRPpsZQjIkgEAppufVps03wfXLO0PgNOX9WgCPQVA9fIn_XyTv92b2Dtc8hVDPRVzXG_WSXJCTF30ZyWwEM9CwcG4YfCKQBQfLC_voFrN9HGQOzuzF7ployD-XB89VNpdeQQ-m-buzaMbRjQwmAnFLJcG9CcS7La-E1DPhw0FNulab5F0_q7Bh0-qmVdA4GBXQHY5BjBL3ELS3pzkz5FfPY3hwUWAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aca1a7b7a.mp4?token=Vg8UKoOCluMwEqCnzfKpGldM7V1NIESP1E-az7p8jjNO9v3RsWapZZ710fh9sxA2Rb-VjnEgYZGMdYWm_-YbZZVmSnEUogzCcVADoqdeZp1cltnDRgHQikR7jRPpsZQjIkgEAppufVps03wfXLO0PgNOX9WgCPQVA9fIn_XyTv92b2Dtc8hVDPRVzXG_WSXJCTF30ZyWwEM9CwcG4YfCKQBQfLC_voFrN9HGQOzuzF7ployD-XB89VNpdeQQ-m-buzaMbRjQwmAnFLJcG9CcS7La-E1DPhw0FNulab5F0_q7Bh0-qmVdA4GBXQHY5BjBL3ELS3pzkz5FfPY3hwUWAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/14181" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14180">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/14180" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14179">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/14179" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14178">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس :
محاصره دریایی یک عملیات نظامی است و ما به آن پاسخ داده و باز هم خواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/14178" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14177">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الجزیره به نقل از یک مقام ایرانی :
بالگرد آپاچی که منهدم شد به علت پرواز در آسمان سرزمینی ایران منهدم شد و برخلاف ادعا ها بر فراز آب های بین المللی پرواز نمی‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/14177" target="_blank">📅 00:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14176">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9cb2f588.mp4?token=B5VQ0bGdrcXpdmO33cMrp_yXHqdSankyzVRfEwT_a8y-KodMMeqxEICvjauYJ3Z6pbYeoub6MgXunh0UP8wIJ01SOGZG-QSVuQow2y0Y1gGZzYp9lh4chzlmI1OAvQVH7FjngvZfX5dz309zzrJbKyfFmWupGwokKkHnxrMjKtlKRi4veFURhY0FYoEVPpj1nP3BdH8ZLH8UCBG57lNsSeXWd23P4ImqOuavsD3kY89entxoafa9yDt94D1a8XppsiHAe5i9j24jekO03csG-9sMZrXdfi0uIiwzvWXkCDZvldjwWYqKLl2n2VnOYLBWN3eheybew4QL7HKjqt69fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9cb2f588.mp4?token=B5VQ0bGdrcXpdmO33cMrp_yXHqdSankyzVRfEwT_a8y-KodMMeqxEICvjauYJ3Z6pbYeoub6MgXunh0UP8wIJ01SOGZG-QSVuQow2y0Y1gGZzYp9lh4chzlmI1OAvQVH7FjngvZfX5dz309zzrJbKyfFmWupGwokKkHnxrMjKtlKRi4veFURhY0FYoEVPpj1nP3BdH8ZLH8UCBG57lNsSeXWd23P4ImqOuavsD3kY89entxoafa9yDt94D1a8XppsiHAe5i9j24jekO03csG-9sMZrXdfi0uIiwzvWXkCDZvldjwWYqKLl2n2VnOYLBWN3eheybew4QL7HKjqt69fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/14176" target="_blank">📅 00:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc82e1504.mp4?token=H5efP7NjDe5KjnwKaGtPxJlWclvcXIAvjiifznXs2UNHLLgz_WGwNEBN1B7citUPbXHY4hJmHqo0PxqzWHmVbXMfriUAgDboPo8Su78kzCqdCvEccRWt--sAmbTZd-9QRmaB8ufysyb8o3YmtN3AOVpK8LDzBziFhmf8MVHua80IK6GsieJ-ykQl0U7RKYKI-oUyIHPuerrQVqGUzzDrTzcaZpU_pDT8Rq3hhaXsCPen9qFs8VEOLT3FV_6rMrILynu-YKsHTVth4CTpsIPYsPMLv9pSR8ulW4XmOtgXi6xbF7CLCalHI1FqrBmrwyg_zh0WvBx8qTHq4u4CyK-HCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc82e1504.mp4?token=H5efP7NjDe5KjnwKaGtPxJlWclvcXIAvjiifznXs2UNHLLgz_WGwNEBN1B7citUPbXHY4hJmHqo0PxqzWHmVbXMfriUAgDboPo8Su78kzCqdCvEccRWt--sAmbTZd-9QRmaB8ufysyb8o3YmtN3AOVpK8LDzBziFhmf8MVHua80IK6GsieJ-ykQl0U7RKYKI-oUyIHPuerrQVqGUzzDrTzcaZpU_pDT8Rq3hhaXsCPen9qFs8VEOLT3FV_6rMrILynu-YKsHTVth4CTpsIPYsPMLv9pSR8ulW4XmOtgXi6xbF7CLCalHI1FqrBmrwyg_zh0WvBx8qTHq4u4CyK-HCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/14175" target="_blank">📅 23:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14174">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس تروریستی ج.ا :
دست آن رزمنده‌ای که در تنگه هرمز با سرنگونی هلیکوپتر آمریکایی (همچون شهید نادر مهدوی) سیلی دیگری به شیطان زد را می‌بوسیم، از او به عنوان یک قهرمان تجلیل خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/14174" target="_blank">📅 23:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14173">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1747743dd.mp4?token=GKOj7x4evP5xoOTd5L04mYGJnv3RcdJdnURUkmbGd49PO8PBWuDV-xChg-bqqvRq140B39UumbUPJC8nsDrWIUEuQiUZ29EC0nCb4Z7tDVWRuIKzXrazfM5ezK2na2SM8s2yGqLrqEEc8wm7ksI6qDPUFgXPVB3YBZwydNOKJIdOlQENwyXIvlcW9KhwHkRsE0VwfMCAL66lRtAej8hcb61ngxrVt_IZYPYvjl2Qkx5A8mwwF2btEMMRd7RsgqDEKKm07r4SmslhXCmOcy_smbfnwcrljvz1YUEHnYSDg4cEpE9a48FBuitlkXjvxzW_iKuKslbSP-MAH4dWVtpz8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1747743dd.mp4?token=GKOj7x4evP5xoOTd5L04mYGJnv3RcdJdnURUkmbGd49PO8PBWuDV-xChg-bqqvRq140B39UumbUPJC8nsDrWIUEuQiUZ29EC0nCb4Z7tDVWRuIKzXrazfM5ezK2na2SM8s2yGqLrqEEc8wm7ksI6qDPUFgXPVB3YBZwydNOKJIdOlQENwyXIvlcW9KhwHkRsE0VwfMCAL66lRtAej8hcb61ngxrVt_IZYPYvjl2Qkx5A8mwwF2btEMMRd7RsgqDEKKm07r4SmslhXCmOcy_smbfnwcrljvz1YUEHnYSDg4cEpE9a48FBuitlkXjvxzW_iKuKslbSP-MAH4dWVtpz8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد واشنگتن به دستیابی به توافق با ایران نزدیک شده است.
ونس گفت:
«ممکن است این توافق هفته آینده حاصل شود، یا شاید چند ماه دیگر.»
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/14173" target="_blank">📅 23:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14172">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ به وال استریت ژورنال: حادثه هلیکوپتر آپاچی موضوع جدی نیست و خلبان حالش خوب است!
ترامپ: به زودی پایان جنگ و پیروزی آمریکا بر ایران را اعلام میکنم امسال جام جهانی خوبی خواهیم داشت.
ترامپ: محاصره ایران رو به شدت فقیر میکنه و تا زمانی که نیاز باشه ادامه داره.
@withyashar
🚨
«این خبر ‌وال استریت ژورنال مال قبل از پست  تهدید ترامپ در تروث است»</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/14172" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14171">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرنگار: شما گفتید آمریکا باید به سرنگونی آپاچی پاسخ دهد، آیا هنوز هم این نظر را دارید؟
ترامپ: من مجبور نیستم کاری انجام دهم، ما همه کارت‌ها را در دست داریم. مجبور نیستم این کار را بکنم اما ببینید، احتمالاً این کار را خواهیم کرد، باشه؟
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/14171" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14170">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ درباره ایران به ABC:
یک نفر باید همه آن زیرساخت‌ها را بسازد، پل‌های جدید، فلان چیز جدید، نیروگاه‌های جدید... آنها از یک تریلیون دلار صحبت می‌کنند، احتمالاً بیشتر...
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/14170" target="_blank">📅 23:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14169">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">منابع آمریکایی و اسرائیلی ادعا می‌کنند که اقدام نظامی قریب‌الوقوع آمریکا علیه ایران ظرف چند ساعت آینده انجام خواهد شد و آن را حرکتی بزرگ با دامنه نامحدود می‌نامند.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14169" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14168">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14168" target="_blank">📅 23:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14167">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">معاون وزیر امور خارجه رژیم جمهوری اسلامی با ترس به الجزیره گفت: ایران پشت حمله به یک هلیکوپتر آپاچی آمریکایی در تنگه هرمز نیست.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/14167" target="_blank">📅 23:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14166">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پست جدید از آخرین وضعیت و اتفاقات پیش رو کارهای اداریش را انجام بدید. کلیک کنید.
💥
💥
😁
https://www.instagram.com/reel/DZYFeVJS_V2/?igsh=MWNobm81Z282cWtmZQ==</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/14166" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14165">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b5cbaa3c.mp4?token=PlqMqEiXu_hXud2qK29QxbSsYyIzO0GjSllVVYTQUqtvejk3HatwkmUMkzG1wNt6cPMpJIBL4R7pcZKzrRy9BEGDB6eb-H4bmHG4fumTWhkD-EvOsf-LOnQ-Ax3eVDkXskMmv-BrZfjBkHIwDysAEFINWJ_jEMpRCkx83Y1ojq4WL7TfY1MGkIVX5oMVios-Z_PYrWkwMB0BzebqonQgCionC4I-GJy4VWMeG0-hfonRK5nbikPoZ4SHjHCyaIUFNipvG9eAzPSfOPagGAKwY4wg65Ue_1zBDP8uX_8lq0hJnV0OY3YbVSzlE1On4gD2-rbwe1dsNl2o9a7xji3LblNHRDFhTCLJymT6sKbARysKJRSnVy6PMoFMMGH1o7X7n_Xki1mKKoZCllda3RGpSmkYCygT1Znx2Yt0ZoUCLfbxESvc5LkKD9VzMQYaEjoyLRzrCqsC9qRES6ojvZ_AO13l3DYpfAXgOopLxasU6K9hwkhwzGqWmPQ2E9-hJyvOsk97lDZSgCj5aUYjCCif3_86yhrOii--wbTOvWLxea7Ag8CsKIjvQZFdbv06HuT_KX8VMTjJaqxCPsgyH6RKTkit9aCQZiuCukxZlDwUphVKBpzKADM0Q7A2nhtKB01Tx5A1e2coI5makn-pCEvHcrhYaYCwhbCBASDHf_bJIm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b5cbaa3c.mp4?token=PlqMqEiXu_hXud2qK29QxbSsYyIzO0GjSllVVYTQUqtvejk3HatwkmUMkzG1wNt6cPMpJIBL4R7pcZKzrRy9BEGDB6eb-H4bmHG4fumTWhkD-EvOsf-LOnQ-Ax3eVDkXskMmv-BrZfjBkHIwDysAEFINWJ_jEMpRCkx83Y1ojq4WL7TfY1MGkIVX5oMVios-Z_PYrWkwMB0BzebqonQgCionC4I-GJy4VWMeG0-hfonRK5nbikPoZ4SHjHCyaIUFNipvG9eAzPSfOPagGAKwY4wg65Ue_1zBDP8uX_8lq0hJnV0OY3YbVSzlE1On4gD2-rbwe1dsNl2o9a7xji3LblNHRDFhTCLJymT6sKbARysKJRSnVy6PMoFMMGH1o7X7n_Xki1mKKoZCllda3RGpSmkYCygT1Znx2Yt0ZoUCLfbxESvc5LkKD9VzMQYaEjoyLRzrCqsC9qRES6ojvZ_AO13l3DYpfAXgOopLxasU6K9hwkhwzGqWmPQ2E9-hJyvOsk97lDZSgCj5aUYjCCif3_86yhrOii--wbTOvWLxea7Ag8CsKIjvQZFdbv06HuT_KX8VMTjJaqxCPsgyH6RKTkit9aCQZiuCukxZlDwUphVKBpzKADM0Q7A2nhtKB01Tx5A1e2coI5makn-pCEvHcrhYaYCwhbCBASDHf_bJIm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : اختلال GPS
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14165" target="_blank">📅 23:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14164">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شورای امنیت رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ها علیه جمهوری اسلامی ایران را تصویب کرد.
بریتانیا از فعال شدن تمام تحریم علیه  ایران استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14164" target="_blank">📅 23:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14163">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پست جدید از آخرین وضعیت و اتفاقات پیش رو کارهای اداریش را انجام بدید. کلیک کنید.
💥
💥
😁
https://www.instagram.com/reel/DZYFeVJS_V2/?igsh=MWNobm81Z282cWtmZQ==</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14163" target="_blank">📅 23:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14162">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرنگار یدیعوت آحارونوت: حملات آمریکا جوری خواهد بود هیچکس حتی فکرشو نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/14162" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14161">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/14161" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14160">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/14160" target="_blank">📅 22:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14159">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/14159" target="_blank">📅 22:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14158">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پست جدید از آخرین وضعیت و اتفاقات پیش رو کارهای اداریش را انجام بدید. کلیک کنید.
💥
💥
😁
https://www.instagram.com/reel/DZYFeVJS_V2/?igsh=MWNobm81Z282cWtmZQ==</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/14158" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14157">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرودگاه های تهران رو دارن تخلیه می کنند.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14157" target="_blank">📅 22:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14156">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAN6MsfjlUENaJV__npoQ61BFnx0wEjkjaJxEwicZItA1FFmItkP4eDr0usx4HeZNffrphUR_RSXIY93XiSBrLiCTZddimnpDc_n7gBcg6he1kRvPK0l-0Lo8eivK33QxQHCW0eXQzYrx-7smhjh-PQUThjXBQIrA0EW2Ce5JZ7oy8FUFqtdFq4ACqXkSuFObNMiS2lsaVm3e5n4UJMVqg31JKlbY1mzYZQoP6iKuhT4OLp07SInS-qupxrzYRyzPhHOFBWSfT9oMAejMphlVVbVIybC7Nln5EDrya8N_hLyl0yvSugs0lCqUAlPzrXJT_91_gkpm_tWSROQlVug5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14156" target="_blank">📅 22:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14155">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/14155" target="_blank">📅 22:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14154">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آمادگی نیروهای مسلح برای پاسخ به هرگونه شرارت و تجاوزی
سخنگوی کمیسیون امنیت ملی:
نیروهای مسلح در اوج آمادگی‌های رزمی و دفاعی قرار دارند و الحمدالله آسیب‌ها رفع شده است.
نیروهای مسلح آماده‌اند تا در بالاترین سطح به هرگونه شرارت و تجاوزی پاسخ دهند.
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14154" target="_blank">📅 22:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14153">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ‌با کت باز گفت :  در واقع خیلی ساده است. برنده کسی است که قدرت دارد. ما تمام قدرت را داریم. @withyashar
😁</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14153" target="_blank">📅 22:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14152">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با شما :صدای مهیب اومد بعدم آمبولانس  پشت بندشم پدافند کار میکنه منطقه۶
@withyashar
یاشار : امشب هوای تهران طوفانی‌هم هست</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14152" target="_blank">📅 22:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14151">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ‌با کت باز گفت :  در واقع خیلی ساده است. برنده کسی است که قدرت دارد. ما تمام قدرت را داریم.
@withyashar
😁</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14151" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14150">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش پرواز جنگنده های نیروی هوایی ارتش در جنوب غرب کشور
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14150" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14149">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرنگار العربیه: اسرائیل با انجام 4 حمله هوایی مناطقی را در جنوب لبنان بمباران کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14149" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14148">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال ۱۴ اسرائیل: گزارش‌هایی از چندین انفجار در منطقه امیرآباد تهران منتشر شده است. این منطقه محل استقرار ستاد سازمان انرژی اتمی ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14148" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس:
نتانیاهو گزارش من درمورد احتمال از سرگیری جنگ توسط اسرائیل بدون آمریکا رو تایید کرد
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14147" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14146">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار اسرائیلی:
من گیج شدم. دو روز پیش ایران به اسرائیل حمله کرد و ترامپ خواست ما جواب ندیم ولی الان خودش میگه باید بخاطر شلیک به هلیکوتر آمریکایی جواب بدیم.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14146" target="_blank">📅 21:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14145">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14145" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14144">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نجات ۲ خلبان بالگرد آپاچی ۶۴ توسط قایق بدون سرنشین آمریکایی
سخنگوی فرماندهی مرکزی ایالات متحده(سنتکام) به رادیو ارتش اسرائیل تأیید کرده است که کشتی‌ای که دیشب خدمه هلیکوپتر آپاچی را در سواحل عمان نجات داد، یک کشتی بدون سرنشین نیروی دریایی ایالات متحده بوده است.
نیروهای عملیاتی از اواخر مارس شروع به استقرار چنین کشتی‌های بدون سرنشین در این منطقه کرده‌اند.
لشکر ۸۲ هوابرد معروف به شیطان نیز در این عملیات نجات مشارکت داشتند
.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14144" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14143">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : خبر ۳ میلیارد دلار خبر فیک با منبع رسانه داخلیه
خودش هم گفته باز به نقل از یک مقام سپاهی!!!!
@withyashar
اون پرواز هم چک کردم رفته پرسنل رو تخلیه کنه !</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/14143" target="_blank">📅 21:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14142">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار فاکس‌نیوز در کاخ سفید:
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
«رئیس جمهور ترامپ احتمالاً در شرف دستور دادن به یک انفجار بزرگ در ایران است...
هیچ سرباز آمریکایی در اینجا کشته نشد، اما به نظر می‌رسد که ایران واقعاً، واقعاً سخت تلاش می‌کرد تا سربازان آمریکایی را بکشد، زیرا آنها یک هلیکوپتر آپاچی را سرنگون کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14142" target="_blank">📅 21:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14141">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سی ان ان :  یک پهپاد شاهد ایران  یک بالگرد آپاچی ۶۴ آمریکا را سرنگون کرده است.
قیمت پهپاد شاهد بدون رنگ : ۲۰،۰۰۰دلار
قیمت هلیکوپتر آپاچی ای اچ -۶۴ مدل سال : ۳۱ میلیون دلار
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/14141" target="_blank">📅 20:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14140">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منبع عراقی  : یک موشک روسی اوگلا-اس به یک هدف هوایی که قصد عبور از تنگه هرمز را داشت، اصابت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/14140" target="_blank">📅 20:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14139">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیویورک تایمز: ترامپ از اینکه نمی‌تونه مستقیم با آیت‌الله خامنه‌ای صحبت کنه خیلی ناراحته و حسابی ناامید شده
این خبر فیکه  داره پخش میشه !حتی ترجمه عنوان هم چیز دیگست
خبر اصلی :
https://www.nytimes.com/2026/06/09/world/middleeast/us-iran-talks-war.html?utm_source=perplexity
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/14139" target="_blank">📅 20:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14138">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی مدعی شد:
تحقیقات به این نتیجه رسید که یک پهپاد ایرانی با یک بالگرد آمریکایی برخورد کرده و موجب سقوط آن شده است.
این مقام آمریکایی مدعی شد هنوز مشخص نشده است که این ساقط کردن هلیکوپتر با پهپاد، تعمدی بوده یا خیر.
@withyashar
با این حال، کمی پیش ترامپ در شبکه تروث اعلام کرد که انتقام این کار ایران را میگیرد.</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/14138" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14137">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قالیباف: ما زبان دیپلماسی را ترجیح می‌دهیم، ولی زبان‌ غیردیپلماسی را روان‌تر صحبت می‌کنیم / شما سوار همان اسبی می‌شوید که زین کرده‌اید
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگر را بسیار روان‌تر صحبت می‌کنیم.
اگر تعهدات خود را بشکنید، ما به همان زبان که خودمان بهتر بلدیم، روی می‌آوریم. شما سوار همان اسبی می‌شوید که زین کرده‌اید!
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/14137" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/14136" target="_blank">📅 20:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14135">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694d9db426.mp4?token=t0K0ZlE8XtwBVL4dNkNo6mzH1MAO-DR7iffdS8l1vAYXTFMveGIdkncQ8vb-YtO5gHmxV_wBZRXnHBR8X8-9hGeIzAFBU7hfKecE08IEWsivZmVm06MWJbC6fcp2UELCtmUvN73kfCoD70GvKskK_6n9pSVJzC0EPKvOfOiKd4LrSlZxD6_x7qSLzcugugrdR9xh6B_EW68ImGolbTilaUBuAvuLrqslazbhEo9DvWpxpoI_PCY30x6iHmf-blcyTWMFaN5KrNHFK7bGih2fZARTpyHHM0Y7me764EnCHS6sHTT0omAX9NL8y3dS2Gs5iYPZ3H1DGtqQQn1r4IP5kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694d9db426.mp4?token=t0K0ZlE8XtwBVL4dNkNo6mzH1MAO-DR7iffdS8l1vAYXTFMveGIdkncQ8vb-YtO5gHmxV_wBZRXnHBR8X8-9hGeIzAFBU7hfKecE08IEWsivZmVm06MWJbC6fcp2UELCtmUvN73kfCoD70GvKskK_6n9pSVJzC0EPKvOfOiKd4LrSlZxD6_x7qSLzcugugrdR9xh6B_EW68ImGolbTilaUBuAvuLrqslazbhEo9DvWpxpoI_PCY30x6iHmf-blcyTWMFaN5KrNHFK7bGih2fZARTpyHHM0Y7me764EnCHS6sHTT0omAX9NL8y3dS2Gs5iYPZ3H1DGtqQQn1r4IP5kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/14135" target="_blank">📅 20:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14134">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ در تروث : «به من همین حالا توسط ارتش بزرگ‌مان اطلاع داده شده است که دیشب ایرانی‌ها یکی از بالگردهای بسیار پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان در این حادثه حضور داشتند و هر دو سالم و بدون جراحت هستند. با این حال،…</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/14134" target="_blank">📅 20:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLqaZnCBB_KZ_a1IguAC4Igbrp1gJHjVHnRILgi-3kWBqn1a9sVwN5_Lwds_3Q8C30Iq0Wlsyg7xsNqljC_9ee3rpFvyUm6eZbNgJtxIjF5C2NWZ6KNSAI-5zB_VAXJ0zxQGsNZ1uTAmPaOcV38FfcGL4Kt2GhX3aRd7nm-ThmMK9IxLraFvDw__km5h-YAYW0i-_SejAZR3IvsUcZoDASinpefSRL3d9DWhaHqgqsk4MYtv4rPFbbrV1wUuZBv6IEaPMGSNu8RpcgXBIn_8qRy8tkSQzwu4s_clNuVJIavJieiho534Ha3vsW3PDapvFyWc4LsHMgX_XZmnDptUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «به من همین حالا توسط ارتش بزرگ‌مان اطلاع داده شده است که دیشب ایرانی‌ها یکی از بالگردهای بسیار پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان در این حادثه حضور داشتند و هر دو سالم و بدون جراحت هستند. با این حال، ایالات متحده ناگزیر است به این حمله پاسخ دهد. از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14133" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/14132" target="_blank">📅 20:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزیر انرژی آمریکا: بازگشت جریان انرژی به حالت عادی ماه‌ها طول خواهد کشید
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/14130" target="_blank">📅 20:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQkNBxiF_YMDdGgO3QdIUhP6wjvgb4QE62OTEj7LubLLE1r2qHCyyylvIG041EptpOMcWNO2JWKgQ2WfY0iE6UvQOOCNTiODMpoal55TK9GkBHkqZiUUiSFvyYLY8ahhJa3NKZxX3wVOEWaHyuTPOq2LKkIPslZRRUW0hOnqc8yvb1VoHFIJxJZAJQwg1gS4eNQ7o3PO_LwiNRXJZXi1iVxsmXy5_El3cFKYSQMVbH_6HLS92qk_mJyTGe_SuNkQb1vHxCYcrCunFXjCZ_cuLBetrHos71bB0XANhtk8o5TLbm3mR6EQq2ZbZ4XT9qC_82WIHP32gFgcD0ou9DgE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود همین الان تهران محدوده ولنجک @withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/14129" target="_blank">📅 19:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آغاز حملات جدید اسرائیل به صور در‌جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/14128" target="_blank">📅 19:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9WdoCnCQxDfpbLgtKfpp6Id-6muez1rNe02JcUy4TiMIt5Kss6Kz9-BQMj2-xj-hnCvo0u-8TDsAZ_8xiriSXRnIbti2hVVrKTtqb54FXs4GIuD5h0xp_yCA8Qr6ligNZh9w4LaOSq5iyj99cO_IXKaxPrsanCsLefC8ea1Y5MoxOFCynkhcO34CUI5qe46QxvEKI6A-jiz-V2nGQNZkYhLTkZIQnDj97zr-enLqR7yp_AgLTWzcj_Duo8lr-Qx5w0PzJ1fJoDVJKVDsLifvNz48ZNYESdP7OJS3Pw_E9nXecOZs11FGI3VbqtWGphVax2jteb7wZl5DFxFiuZHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیراز  یک ربع پیش
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/14127" target="_blank">📅 19:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">برنامه حضور تیم‌ملی در آمریکا مشخص شد
سخنگوی فدراسیون فوتبال:
کاروان تیم براساس برنامه فیفا، با پرواز چارتر به آمریکا می‌رود؛ یک روز قبل بازی مقابل نیوزیلند تیم به محل می‌رود و در دو بازی بعد، دو روز قبل مسابقه در محل میزبانی حضور پیدا خواهیم کرد.
بجای بازی با گرنادا، مسئولان فدراسیون در تلاش هستند تا یک دیدار هماهنگ کنند که این بازی پشت درهای بسته برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/14126" target="_blank">📅 19:08 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
