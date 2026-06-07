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
<img src="https://cdn4.telesco.pe/file/LPcUEakLM79Uzdvf1TOP76-d1FQAtjWtGae-boeEeNEnkuZOEnLmuhanKFhMgV5RtE7_Yn89b-01BEn-SuseRP395NoS2SjhFom1AqTW6OKl_L7tTYdAongDL4QHg5TeXdieUMtBbBB9mPCda6LuUViJxBksHlc_UDi1zUsTZN3LS7gPm7ulCusY7k_x65XheQGlof47A_6vLGxKsjzxF5-lFdidBrPaUtpRJ2SG7m2BasUYnRFONH75URv1rkZ_yzBLce0_WKlgXT2rI0vAidDkkW5PWka-vJBGKjxvY0Mw9rU_UwHiXFbwpuLVYKBOXiTObn9m4L2eE3P-7LaL8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 295K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 01:28:15</div>
<hr>

<div class="tg-post" id="msg-13837">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شبکه کان اسرائیل:
نتانیاهو هم‌اکنون پس از تماس تلفنی با ترامپ در حال برگزاری مشورت‌های امنیتیه.
@withyashar</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/withyashar/13837" target="_blank">📅 01:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13836">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتاق جنگ با شما: سمت تهرانپارس صدای خیلی خیلی وحشتناک
از تمام صداهای تو این مدت بدتر
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/13836" target="_blank">📅 01:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">منابع العربیه: عراقچی به پاکستان اطلاع داد که لبنان بخش جدایی‌ناپذیری از پرونده مذاکره است
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/13835" target="_blank">📅 01:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/withyashar/13834" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جمهوری اسلامی شدیداً در حال جابهجایی های استراتژیک هست تا در برابر حمله احتمالی اسرائیل کمترین آسیب را ببیند.
@withyashar</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/13833" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13832">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/13832" target="_blank">📅 01:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع عبری : نیروی هوایی اسرائیل آماده پرواز میشود  @withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/13831" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9v5DuiPNaKtEGMyfiXZ-NoxEXtsO8qijHRNo0xi5eK8GpUbSMqKjoy4XvnlNCBbLAqNtFg1Dah08GTJUTWThNFgOjb8I-lYMdaDM3kLEeUH3BEiEQXn2fjgQmY88ZOBhSzum99da_UQG1WgPhmjfL-AGw3-4PU40Esq1eZcgoC5Xgb9kptq_N9gpaoSossiho8GNWsKzVLS59a0NuphbAKazf9AqiK5f7UHKltazvtmHl8_UAdk_S2kj4Zxd8IG7PUC9o5JbYRVqQ3KNXmWzOaBJ0jSg5YVKi-OAPx82t8YKqxCV_kchId6eldoKCnKvVgClTZnsWUlUIL52Y_8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۷ میلیون ویو چنل تازه تا این لحظه … و زدن رکورد بازدید… مرسی از شما
🙌🏾</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/13830" target="_blank">📅 01:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایران به سمت گروه های کرد مخالف ایرانی در سلیمانیه عراق پهپاد شلیک کرده است
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/13829" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/13828" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13827">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/13827" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13826">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/13826" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13825">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/13825" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یدیعوت آحارونوت: بر اساس گزارش‌های دریافتی، در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که قصد حمله‌ای قدرتمند به ایران را دارد. رئیس‌جمهور آمریکا روشن کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/13824" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13823">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اتاق جنگ با شما : همین جوری هواپیما داره میاد بجنورد میشینه
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/13823" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کانال ۱۲ اسرائیل: تاکنون آمریکا برای اجرای حمله علیه ایران موافقت نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/13822" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">والا به نقل از یک مقام ارشد اسرائیلی: پاسخ مورد انتظار به ایران سخت و گسترده خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/13821" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صداوسیما : امشب از موشکهای سوخت مایع و جامد استفاده کردیم و معروفترین آنها موشک خیبر شکن بود.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/13820" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رسانه های‌داخلی : «معادله ۲ در برابر ۴» وارد فاز عملیاتی شده است
آنچه که از مرکز فرماندهی و کنترل سپاه به گوش می رسد
معادله دو در برابر چهار
، عملیاتی شده است.
فرماندهان ایرانی تصمیم خود را گرفته اند اول زدن اسرائیل، دوم انسداد باب المندب، سوم حفظ هرمز و چهارم رفع حصر با ناامن سازی کشتی های تجاری آمریکا و متحدانش.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/13819" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13818">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه های داخلی : پروازهای فرودگاه امام(ره) تا اطلاع ثانوی متوقف شد
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/13818" target="_blank">📅 00:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو :
تصمیم گرفته شد حمله امشب انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13817" target="_blank">📅 00:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13816">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">منابع عبری : نیروی هوایی اسرائیل آماده پرواز میشود
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/13816" target="_blank">📅 00:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس: ما بخشی از این عملیات نیستیم.
اما هنوز مشخص نیست که آیا دونالد ترامپ به ارتش آمریکا دستور خواهد داد که در صورت حمله احتمالی اسرائیل به ایران، هیچ کمکی به اسرائیل نکند یا نه؛ به‌ویژه در زمینه‌هایی مانند سوخت‌رسانی هوایی و سایر هماهنگی‌های نظامی.
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/13815" target="_blank">📅 00:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13814">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منابع عبری : تماس تلفنی ترامپ ‌و نتانیاهو تموم شد
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/13814" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13813">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">«رئیس ستاد ارتش اسرائیل می‌گوید ارتش به محض صدور دستور، با قاطعیت «دشمن» را هدف قرار خواهد داد.»
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/13813" target="_blank">📅 00:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13812">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانال ۱۵ اسرائیل:
پس از پایان گفتگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/13812" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13811">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/13811" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13810">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرگزاری وای نت اسرائیل: آمریکا پیامی به اسرائیل فرستاده و گفته چند روز صبر کنه تا ببینه آیا میشه به توافقی دست یافت یا نه.
اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد و ارزش نداره که این فرصت رو با درگیر شدن در تبادل ضربات محدود هدر بدیم.
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13810" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13809">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ به باراک راوید خبرنگار آکسیوس : هر کدام از آنها خوش گذراندند. اسرائیل حمله خود را داشت و ایران هم حمله خود را.
مابه حمله دیگری نیازنداریم
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13809" target="_blank">📅 00:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13808">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانال ۱۴ اسرائیل :«نتانیاهو باید حتی به قیمت رویارویی با ترامپ به بمباران ایرانی پاسخ دهد.»
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13808" target="_blank">📅 00:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13807">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فاکس نیوز: با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/13807" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13806">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فاکس نیوز: با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/13806" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13805">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-u9_-W2WcOasC5ktXtkQ0kkm4ZwRLT9lE44_l4gNMlrpQs7JFecGHvdr-_ZAyuTEJRKQLDASBTkTrL-pHPZH-MYeY_mvQ3QjLHlFHJ4CkstMRO4PhBaXczwR39JUy64ZFEpWmUZOevKMRZErZkGs3WWGS1EpyPt-KRzplYYLsP8yIJknOywnVNsBb2dr7d-Zkm5SyF_A-j7tSbDcw8FEiLNegSAnCq9OXKuanwiKDPaxIN3N3seZM-fWOv6002FMjOmxVUJMd6e94FlPihSwFu_BdFFyM9Z_vqMJhXdZDMDLOABuzKHu4A5fi_i06uDmRB5SNx6zEPvb5C94rSebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم
اطلاعیه NOTAM صادر کرده است که بخش غربی فضای هوایی تهران را تا ۸ ژوئن به روی تمام ترافیک هوایی غیرنظامی می‌بندد.
تنها هواپیماهای نظامی، دولتی، تخلیه پزشکی و جست‌وجو و نجات مجاز به فعالیت در این منطقه محدود شده هستند.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13805" target="_blank">📅 00:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13804">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">طبق گزارش ها،هم مقامات نظامی و هم مقامات غیرنظامی ایران هم من از اتاق جنگ کاملاً بر این فرض عمل می‌کنند که حمله‌ای به ایران در راه است و بر اساس آن اقدامات لازم را انجام می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13804" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13803">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39c27664b.mp4?token=UffvnynecEXVU_2kFRfOnBZDtGryWxUBxJkqJCJvgzwMw0WIVDuWSwfiUeuIkZqT8K3XGLZ8RvD3cpfqu1fxwzw2dVTExA5nxw1m4GXt2W7uknjlb25Am2GObKlbDn5KhKiCEyi3QaYUmRcfIq4NxAv5NVCkMXtd9MGDX3xQuRp7kzPrd7kpcslxQHntntFvyuk05pIx5fFPuZol9MiYSjYpi_cxt3wA6Q2K-QKiCtMGzc_jtUBvC7np7CPDmUDGUX5CQCEleEOKDa9NArQFXmg8_jO9xlCmAjue4NR6MrW9KKIUR1NWkfiZ_uXRG4oU3FQj66u8VXsSKn5OjDj6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39c27664b.mp4?token=UffvnynecEXVU_2kFRfOnBZDtGryWxUBxJkqJCJvgzwMw0WIVDuWSwfiUeuIkZqT8K3XGLZ8RvD3cpfqu1fxwzw2dVTExA5nxw1m4GXt2W7uknjlb25Am2GObKlbDn5KhKiCEyi3QaYUmRcfIq4NxAv5NVCkMXtd9MGDX3xQuRp7kzPrd7kpcslxQHntntFvyuk05pIx5fFPuZol9MiYSjYpi_cxt3wA6Q2K-QKiCtMGzc_jtUBvC7np7CPDmUDGUX5CQCEleEOKDa9NArQFXmg8_jO9xlCmAjue4NR6MrW9KKIUR1NWkfiZ_uXRG4oU3FQj66u8VXsSKn5OjDj6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر تایید نشده: یک هواپیمای مسافربری در صحرای کربلا سقوط کرد @withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/13803" target="_blank">📅 00:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13802">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از‌ مهرآباد جنگنده بلند شد @withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/13802" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13801">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fba84ca98.mp4?token=b7muqvIZ5qC9WIU6TzOHK5WpVjnykvrK45JXt38Nw87SZPpGm80sP-KR3Dxo8Wjz7S3WxM4bhOnfnyG7qKbeCUGgFCTCxJ_WXGHhUoHE5RIqQ1GPn1PpVfOwKwUSxgTGDpL9wwiE_zQq0n0BknPflA1wyoyEZtl_jShJfzG_CWwMT-U-FxwN2OoXmGocYB2KNIZblsdZLi_mqvIYK2Q-UkdqqX451wND92X0GB0yVbqQzs3sMKcJr512gTVwIMwHo5x35NGa2Mccb2Klq3IvMF7IOYvkBK6zK06qN0FS2WZK-94uQP0iX26lmJAZArpba_9U3lDvPSTJ8PiX0WgCp7pSTa4zvuYwN2_biWQla97CSe7Ypf_rvnUhmKFyJhHiAAjYiu5htdt-eJEra2zcNvzPzqqaCvBh3XHj22st3-N6uxd_8LEv0hFyEmGbb1sIXlEaegEG1rEsiWKAhBFKien5nFXTOh7i8X_YseKMOYCM1_uPdltMSA_KD88GxYnzZEiyuJUot1jVOjj4Yu1NzooQFooHm6Y4_kwgzWg00NYhRgF0QwZrMKILgwWBtb1VCI7LWY4u6jZhnGlBuaAMFVXcYvraTmQJWM-RurXda8NhMGbsyu9UXzjbhW0G6PHauUmd5BE3a0aajX_7Xg-170zvFnsiAfEUHsKsjxtgjdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fba84ca98.mp4?token=b7muqvIZ5qC9WIU6TzOHK5WpVjnykvrK45JXt38Nw87SZPpGm80sP-KR3Dxo8Wjz7S3WxM4bhOnfnyG7qKbeCUGgFCTCxJ_WXGHhUoHE5RIqQ1GPn1PpVfOwKwUSxgTGDpL9wwiE_zQq0n0BknPflA1wyoyEZtl_jShJfzG_CWwMT-U-FxwN2OoXmGocYB2KNIZblsdZLi_mqvIYK2Q-UkdqqX451wND92X0GB0yVbqQzs3sMKcJr512gTVwIMwHo5x35NGa2Mccb2Klq3IvMF7IOYvkBK6zK06qN0FS2WZK-94uQP0iX26lmJAZArpba_9U3lDvPSTJ8PiX0WgCp7pSTa4zvuYwN2_biWQla97CSe7Ypf_rvnUhmKFyJhHiAAjYiu5htdt-eJEra2zcNvzPzqqaCvBh3XHj22st3-N6uxd_8LEv0hFyEmGbb1sIXlEaegEG1rEsiWKAhBFKien5nFXTOh7i8X_YseKMOYCM1_uPdltMSA_KD88GxYnzZEiyuJUot1jVOjj4Yu1NzooQFooHm6Y4_kwgzWg00NYhRgF0QwZrMKILgwWBtb1VCI7LWY4u6jZhnGlBuaAMFVXcYvraTmQJWM-RurXda8NhMGbsyu9UXzjbhW0G6PHauUmd5BE3a0aajX_7Xg-170zvFnsiAfEUHsKsjxtgjdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ردبول
🪽
😈
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/13801" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13800">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">منابع عبری:ترامپ و نتانیاهو در حال حاضر در حال گفتگو هستن
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13800" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13799">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بریم اتاق جنگ</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/13799" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13798">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال 12 اسرائیل:با وجود مخالفت ترامپ، فشارهای داخلی بر نتانیاهو برای واکنش افزایش یافته و شماری از سیاستمداران اسرائیلی خواستار پاسخ شدید به حملات جمهوری اسلامی شدند.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/13798" target="_blank">📅 00:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13797">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ به نیویورک پست: «اوضاع بسیار خوب پیش می‌رود.»
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13797" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13796">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانال 12 اسرائیل:
با وجود مخالفت ترامپ، فشارهای داخلی بر نتانیاهو برای واکنش افزایش یافته و شماری از سیاستمداران اسرائیلی خواستار پاسخ شدید به حملات جمهوری اسلامی شدن.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13796" target="_blank">📅 00:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13795">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سخنگوی ارتش اسرائیل در یک کنفرانس مطبوعاتی ادعا کرد که رئیس ستاد ارتش، ایال زامیر، در حال ارزیابی وضعیت است و «طرح‌هایی را برای آینده تصویب می‌کند»
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13795" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13794">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی ارتش اسرائیل: ایران اشتباه بزرگی مرتکب شد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13794" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13793">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از‌ مهرآباد جنگنده بلند شد
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13793" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13792">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه های داخلی: تو تبریز پهپاد زدیم
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13792" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13791" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش انفجار در تبریز
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13790" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتش اسرائیل تا دقایقی دیگر بیانیه ای صادر خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13789" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ به خبرگزاری کان:
فکر می‌کنم اسرائیل به اندازه کافی واکنش نشان داده است. دیگر نیازی به واکنش بیشتر نیست.
ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/13788" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به N12:
در حمله موشکی کسی آسیب ندید. اگر نتانیاهو پاسخ دهد، این [حمله] ادامه خواهد یافت و ادامه خواهد یافت.
ما به توافقی برای پایان دادن به جنگ بسیار نزدیک هستیم و این توافق خوبی خواهد بود.
من نمی‌خواهم این [حمله] توافق را از مسیر خود خارج کند. هر دو طرف حمله کرده‌اند و من نمی‌خواهم شاهد حمله دیگری باشم.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/13787" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوریه ، عراق و اردن حریم هوایی خودشونو بستن
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13786" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبر تایید نشده:
یک هواپیمای مسافربری در صحرای کربلا سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13785" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ :  الان دارم با نتانیاهو تماس می‌گیرم و به اون میگم که به ایران حمله تلافی‌جویانه نکنه
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/13784" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f212f792.mp4?token=uFC5rjQkawiaeUMtM6HWzI4hddNHgZC2cESvRSLNOODGiKfuGB3J38XltUgCr0EWeMzkQ8g2VNmSsVAO6bFQAwdMnvtDxy8zbTr0j5uTy6rT2bTA1LqH0w0mmLySOebIN0q7dw6fYGVjQRfrdQQibB5sNzI4vV3iWNvy1K2Lo7h3Don0tcnLoDRJ4YYVlRA2hzkuwSZpUV3dyDD7RgsROOfItFl5Fp0fmENn5-CWenTqbm2w71tktdFB2HGPwo6FYrtKr_rbv9_6H94zD22RMb8159qepgdzb1KKunpxiBVSd1hQAnxFgmH93-m3ILxAK0G_ofeuNBh9zhu-KT6isQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f212f792.mp4?token=uFC5rjQkawiaeUMtM6HWzI4hddNHgZC2cESvRSLNOODGiKfuGB3J38XltUgCr0EWeMzkQ8g2VNmSsVAO6bFQAwdMnvtDxy8zbTr0j5uTy6rT2bTA1LqH0w0mmLySOebIN0q7dw6fYGVjQRfrdQQibB5sNzI4vV3iWNvy1K2Lo7h3Don0tcnLoDRJ4YYVlRA2hzkuwSZpUV3dyDD7RgsROOfItFl5Fp0fmENn5-CWenTqbm2w71tktdFB2HGPwo6FYrtKr_rbv9_6H94zD22RMb8159qepgdzb1KKunpxiBVSd1hQAnxFgmH93-m3ILxAK0G_ofeuNBh9zhu-KT6isQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13783" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش انفجار‌ در‌فرودگاه تبریز
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13782" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13781">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جنگنده های اسرائیلی به پرواز در امدند
منابع اسرائیلی مدعی‌اند حملات فعلی به اهدافی در ایران توسط پهپادهای از پیش مستقرشده انجام می‌شود و جنگنده‌های اسرائیلی هنوز به منطقه عملیات نرسیده‌اند.
به گفته این منابع، حملات کنونی عمدتان مراکز پرتاب را هدف قرار داده و مرحله اصلی عملیات تلافی جویانه هوایی و بمباران توسط جنگنده‌ها همچنان در راه است.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13781" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فاکس نیوز: مقامات ایرانی معتقدند که ترامپ تمایلی به ورود به یک درگیری گسترده‌تر ندارد و مصمم است جنگ را تقریباً به هر قیمتی به پایان برساند
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13780" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سی‌ ان‌ ان به نقل از دو منبع اسرائیلی: ما به پرتاب موشک‌ های بالستیک ایران با قدرت پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13779" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ به زودی تصمیم نهایی خود را خواهد گرفت
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13778" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجار/رعد برق در تهران گزارش شده
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13777" target="_blank">📅 23:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ به فاکس نیوز :
حمله ای که اسرائیل امروز کرد به بیروت کاملا بدون هماهنگی من بود و از این موضوع خوشحال نیستم
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/13776" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سازمان هواپیمایی کشوری ایران:
حریم هوایی غرب کشور تا اطلاع ثانوی بسته خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13775" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ: قرار بود دوشنبه یا سه‌شنبه توافق صلح را امضا کنیم
.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13774" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ارتش اسرائیل : در مجموع 12 موشک بالستیک شلیک شد که تمام آن رهگیری یا به منطقه‌ای باز اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/13773" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: توافق با ایران در دسترسه و بهش نزدیکیم.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/13772" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حوثی ها منتظر دستور بستن تنگه باب المندب هستیم
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13771" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ به فاکس نیوز: آنچه به ایران توصیه می‌کنم: موشک‌هایتان را پرتاب کرده‌اید، همین کافی است
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/13770" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سپاه: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/13769" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فعالیت پدافند هوایی در کرماشاه و تبریز
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/13768" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدا و سیما : سد مجید موسوی، فرمانده نیروی هوایی سپاه: الوعده وفا
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/13767" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدای سیما شیپور جنگ را زد. آهنگ بزن که خوب میزنی در حال پخش است.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/13766" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آژیر در شمال اسرائیل و اردن به صدا درآمد.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/13765" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">موج پنجم حملات شروع شد
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/13764" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13763">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/13763" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اگه امکاناتشو دارید بهتره تهران رو ترک کنید</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/13762" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منابع اسراییل: حملات سنگین به ایران نزدیک است
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/13761" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13760">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سوخترسان های آمریکایی از تلآویو بلند شدند
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/13760" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا : قبلا اخطار داده بودیم در صورت گسترش جنایت در ضاحیه بیروت، اهدافی را در سرزمین های اشغالی مورد هجوم قرار می دهیم!
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/13758" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رسانه عبری از منابع گزارش می‌دهد: ما به حمله ایرانی پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/13757" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">از ارومیه و اصفهان هم موشک شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/13756" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چند موشک از تبریز و کرمانشاه شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/13755" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13754">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">موج دوم حملات ۳پا آغاز شد
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/13754" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13753">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدا سیما ما وارد یک مرحله زورآزمایی جدید شدیم چون ناتانیاهو خواست ما را محک بزند
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/13753" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13752">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صدا و سیما حمله ایران به شمال اسرائیل در همبستگی با لبنان را تایید کرد
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/13752" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13751">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d65867a2.mp4?token=HBUrxXmIMf45FALM07vE_T6J2PJKTawkL-IB7X0L0d-GcXX0988d1yje1ikZBcq1jbyxTmmxVPwmR-JRUEXErWyk1SPzh8vSG11-ExyuYbkkGlcg-aS25LVAmvEEB0mVtST9715W_YGEA-LsuHE_UC0VeJL0dxHzzmdpDwUf0p6up4jruJUCZU6w2ynypvdo1MBNCvmu45jCQ1T_pF4Mcdvu1OCA5kwKSSM5Z8HCa_w8o7j6avsQ4ZZQ3cx7cuCaQUU3iU_10xgFfy_Jc6puSTburglh-2Xn6w5CvC3GjiPioZF952QIxHPRuFi96ehsgGCh6idDlTOeoHlRlBuPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d65867a2.mp4?token=HBUrxXmIMf45FALM07vE_T6J2PJKTawkL-IB7X0L0d-GcXX0988d1yje1ikZBcq1jbyxTmmxVPwmR-JRUEXErWyk1SPzh8vSG11-ExyuYbkkGlcg-aS25LVAmvEEB0mVtST9715W_YGEA-LsuHE_UC0VeJL0dxHzzmdpDwUf0p6up4jruJUCZU6w2ynypvdo1MBNCvmu45jCQ1T_pF4Mcdvu1OCA5kwKSSM5Z8HCa_w8o7j6avsQ4ZZQ3cx7cuCaQUU3iU_10xgFfy_Jc6puSTburglh-2Xn6w5CvC3GjiPioZF952QIxHPRuFi96ehsgGCh6idDlTOeoHlRlBuPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/13751" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13750">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfa1bc4a4.mp4?token=KVhcS_tgHVAtg8u6JjEJ4DJplfR_5fGXhZUFRHoBJE7PVk1ytsQqFB4Sr-q-zwFZnQBR2eO41jCudIxgsRoF42HBKCsRjWUbEhUKCognbJBm4end1K89JQv9oLT7qizo-riOeTQ6qlo275Q0Lkf7PwcScBgzzO6sDsChIMjcwe8spi2SIRIo6EzYuEd7SkmqpTix57KEoFLxv-NEeTQT7aNrKCHWUru5ObQr0XAKbDjx9AMqj3SnGD_1lczfD63MoZ0T-LXaySwpS5KmPNHuGFadQhvMEVSz7caL0iefgH5m-OQzvOPaY0ULgUuvkcXqBkhzHl7xM6irlQt1lB_RdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfa1bc4a4.mp4?token=KVhcS_tgHVAtg8u6JjEJ4DJplfR_5fGXhZUFRHoBJE7PVk1ytsQqFB4Sr-q-zwFZnQBR2eO41jCudIxgsRoF42HBKCsRjWUbEhUKCognbJBm4end1K89JQv9oLT7qizo-riOeTQ6qlo275Q0Lkf7PwcScBgzzO6sDsChIMjcwe8spi2SIRIo6EzYuEd7SkmqpTix57KEoFLxv-NEeTQT7aNrKCHWUru5ObQr0XAKbDjx9AMqj3SnGD_1lczfD63MoZ0T-LXaySwpS5KmPNHuGFadQhvMEVSz7caL0iefgH5m-OQzvOPaY0ULgUuvkcXqBkhzHl7xM6irlQt1lB_RdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب ۴ موشک به شمال اسرائیل شناسایی شده است
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/13750" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13749">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایران از کرمانشاه موشک شلیک کرد
💥
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/13749" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13748" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13747">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسرائیل هیوم:مدارس در سراسر اسرائیل تعطیل شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/13747" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13746">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بوی عرق زیر بغل روبیکا میاد
🤢
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13746" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13745">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اینترنشنال: دفتر مجتبی خامنه ای دستور حمله رو امضا کرده و فقط دستور به یگان های موشکی مونده
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/13745" target="_blank">📅 22:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شبکه 14 اسرائیل : در این حمله مشخص خواهد شد آیا ایران می‌تواند صد موشک را همزمان شلیک کند یا خیر
🚨
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13743" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العربیه: وزیر کشور پاکستان که هم‌اکنون در تهران حضور دارد، هشدارهایی را به ایران درباره تشدید تنش‌ها در مسیرهای کشتیرانی دریایی منتقل کرده است
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/13742" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هواپیماهای مسافربری در حال ترک حریم هوایی عراق می‌باشند.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13741" target="_blank">📅 22:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوست بیلیونرم : Regime will send rockets on Israel tonight.
رژیم امشب موشک‌هایی به سمت اسرائیل پرتاب خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13739" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دایرکت داره منفجررررررر میشه نمیخوام ببندم خواهش میکنم پیغام احساساتی  ندید فقط گزارشی ها دایرکت بدند
🙌🏾</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13738" target="_blank">📅 21:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیروهای مسلح کویت در حالت آماده‌باش کامل قرار گرفته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13737" target="_blank">📅 21:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسرائیل هیوم: احتمال حملات موشکی ایران تا ساعاتی دیگر وجود داره.
براوردهای امنیتی حاکی از آن است که اگر ایران امشب با هدف قرار دادن شمال اسرائیل پاسخ بده، ممکنه مواضع شبه‌نظامیان (نیروهای مسلح وابسته به اسرائیل) داخل خط زرد (مناطق تحت کنترل تشکیلات خودگردان یا مناطق حائل) در غزه رو هم هدف قرار بده.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13736" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0895ae3f23.mp4?token=YCoATewVbMeVtg704XXXTF3TJ3RvNPkYULCdI1I6PtDeaTc8TUYEc53zoOlpcNIde41X_W5kzXZ5jjk0STF2hny1IrRQrziXc1Iyru_Ak9b1FBQvqAZyYfcSb0ASnNrjFg6jzuOxlvGlat8rzpvVvotUIhzaoanILPfrYPNeiKvhdW1pPJPuOK7g24r3nZNMNnTXZFZunImIOuKgBH-cYqT61dr611IUGHlCU1hlRGTBeCNYPjHlXsmTDAM5NuBmwRFd8atDTbY_bMPemB5WoWUf7gd8Nykq-3pbFFq4bE6zl-LS4AdngZywJY0dACUu9hbNKk1xCmL6LA1Sjd00Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0895ae3f23.mp4?token=YCoATewVbMeVtg704XXXTF3TJ3RvNPkYULCdI1I6PtDeaTc8TUYEc53zoOlpcNIde41X_W5kzXZ5jjk0STF2hny1IrRQrziXc1Iyru_Ak9b1FBQvqAZyYfcSb0ASnNrjFg6jzuOxlvGlat8rzpvVvotUIhzaoanILPfrYPNeiKvhdW1pPJPuOK7g24r3nZNMNnTXZFZunImIOuKgBH-cYqT61dr611IUGHlCU1hlRGTBeCNYPjHlXsmTDAM5NuBmwRFd8atDTbY_bMPemB5WoWUf7gd8Nykq-3pbFFq4bE6zl-LS4AdngZywJY0dACUu9hbNKk1xCmL6LA1Sjd00Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بریم برای اتاق جنگ
💥</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13735" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
