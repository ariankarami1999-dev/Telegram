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
<p>@withyashar • 👥 294K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-13797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ به نیویورک پست: «اوضاع بسیار خوب پیش می‌رود.»
@withyashar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/13797" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال 12 اسرائیل:
با وجود مخالفت ترامپ، فشارهای داخلی بر نتانیاهو برای واکنش افزایش یافته و شماری از سیاستمداران اسرائیلی خواستار پاسخ شدید به حملات جمهوری اسلامی شدن.
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/13796" target="_blank">📅 00:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سخنگوی ارتش اسرائیل در یک کنفرانس مطبوعاتی ادعا کرد که رئیس ستاد ارتش، ایال زامیر، در حال ارزیابی وضعیت است و «طرح‌هایی را برای آینده تصویب می‌کند»
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/13795" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سخنگوی ارتش اسرائیل: ایران اشتباه بزرگی مرتکب شد
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/13794" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از‌ مهرآباد جنگنده بلند شد
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/13793" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13792">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رسانه های داخلی: تو تبریز پهپاد زدیم
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/13792" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13791">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/13791" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش انفجار در تبریز
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/13790" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ارتش اسرائیل تا دقایقی دیگر بیانیه ای صادر خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/13789" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ به خبرگزاری کان:
فکر می‌کنم اسرائیل به اندازه کافی واکنش نشان داده است. دیگر نیازی به واکنش بیشتر نیست.
ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/13788" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به N12:
در حمله موشکی کسی آسیب ندید. اگر نتانیاهو پاسخ دهد، این [حمله] ادامه خواهد یافت و ادامه خواهد یافت.
ما به توافقی برای پایان دادن به جنگ بسیار نزدیک هستیم و این توافق خوبی خواهد بود.
من نمی‌خواهم این [حمله] توافق را از مسیر خود خارج کند. هر دو طرف حمله کرده‌اند و من نمی‌خواهم شاهد حمله دیگری باشم.
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13787" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سوریه ، عراق و اردن حریم هوایی خودشونو بستن
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/13786" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبر تایید نشده:
یک هواپیمای مسافربری در صحرای کربلا سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/13785" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ :  الان دارم با نتانیاهو تماس می‌گیرم و به اون میگم که به ایران حمله تلافی‌جویانه نکنه
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/13784" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f212f792.mp4?token=uFC5rjQkawiaeUMtM6HWzI4hddNHgZC2cESvRSLNOODGiKfuGB3J38XltUgCr0EWeMzkQ8g2VNmSsVAO6bFQAwdMnvtDxy8zbTr0j5uTy6rT2bTA1LqH0w0mmLySOebIN0q7dw6fYGVjQRfrdQQibB5sNzI4vV3iWNvy1K2Lo7h3Don0tcnLoDRJ4YYVlRA2hzkuwSZpUV3dyDD7RgsROOfItFl5Fp0fmENn5-CWenTqbm2w71tktdFB2HGPwo6FYrtKr_rbv9_6H94zD22RMb8159qepgdzb1KKunpxiBVSd1hQAnxFgmH93-m3ILxAK0G_ofeuNBh9zhu-KT6isQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f212f792.mp4?token=uFC5rjQkawiaeUMtM6HWzI4hddNHgZC2cESvRSLNOODGiKfuGB3J38XltUgCr0EWeMzkQ8g2VNmSsVAO6bFQAwdMnvtDxy8zbTr0j5uTy6rT2bTA1LqH0w0mmLySOebIN0q7dw6fYGVjQRfrdQQibB5sNzI4vV3iWNvy1K2Lo7h3Don0tcnLoDRJ4YYVlRA2hzkuwSZpUV3dyDD7RgsROOfItFl5Fp0fmENn5-CWenTqbm2w71tktdFB2HGPwo6FYrtKr_rbv9_6H94zD22RMb8159qepgdzb1KKunpxiBVSd1hQAnxFgmH93-m3ILxAK0G_ofeuNBh9zhu-KT6isQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/13783" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش انفجار‌ در‌فرودگاه تبریز
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/13782" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13781">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جنگنده های اسرائیلی به پرواز در امدند
منابع اسرائیلی مدعی‌اند حملات فعلی به اهدافی در ایران توسط پهپادهای از پیش مستقرشده انجام می‌شود و جنگنده‌های اسرائیلی هنوز به منطقه عملیات نرسیده‌اند.
به گفته این منابع، حملات کنونی عمدتان مراکز پرتاب را هدف قرار داده و مرحله اصلی عملیات تلافی جویانه هوایی و بمباران توسط جنگنده‌ها همچنان در راه است.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13781" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس نیوز: مقامات ایرانی معتقدند که ترامپ تمایلی به ورود به یک درگیری گسترده‌تر ندارد و مصمم است جنگ را تقریباً به هر قیمتی به پایان برساند
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/13780" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سی‌ ان‌ ان به نقل از دو منبع اسرائیلی: ما به پرتاب موشک‌ های بالستیک ایران با قدرت پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/13779" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ به زودی تصمیم نهایی خود را خواهد گرفت
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/13778" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار/رعد برق در تهران گزارش شده
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/13777" target="_blank">📅 23:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به فاکس نیوز :
حمله ای که اسرائیل امروز کرد به بیروت کاملا بدون هماهنگی من بود و از این موضوع خوشحال نیستم
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/13776" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سازمان هواپیمایی کشوری ایران:
حریم هوایی غرب کشور تا اطلاع ثانوی بسته خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/13775" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: قرار بود دوشنبه یا سه‌شنبه توافق صلح را امضا کنیم
.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13774" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13773">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش اسرائیل : در مجموع 12 موشک بالستیک شلیک شد که تمام آن رهگیری یا به منطقه‌ای باز اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13773" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13772">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: توافق با ایران در دسترسه و بهش نزدیکیم.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13772" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13771">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حوثی ها منتظر دستور بستن تنگه باب المندب هستیم
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13771" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13770">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ به فاکس نیوز: آنچه به ایران توصیه می‌کنم: موشک‌هایتان را پرتاب کرده‌اید، همین کافی است
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13770" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13769">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سپاه: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13769" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13768">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فعالیت پدافند هوایی در کرماشاه و تبریز
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/13768" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13767">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدا و سیما : سد مجید موسوی، فرمانده نیروی هوایی سپاه: الوعده وفا
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/13767" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13766">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدای سیما شیپور جنگ را زد. آهنگ بزن که خوب میزنی در حال پخش است.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/13766" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13765">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آژیر در شمال اسرائیل و اردن به صدا درآمد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13765" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13764">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">موج پنجم حملات شروع شد
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/13764" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13763">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/13763" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13762">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اگه امکاناتشو دارید بهتره تهران رو ترک کنید</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/13762" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">منابع اسراییل: حملات سنگین به ایران نزدیک است
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/13761" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سوخترسان های آمریکایی از تلآویو بلند شدند
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/13760" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13758">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا : قبلا اخطار داده بودیم در صورت گسترش جنایت در ضاحیه بیروت، اهدافی را در سرزمین های اشغالی مورد هجوم قرار می دهیم!
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/13758" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13757">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رسانه عبری از منابع گزارش می‌دهد: ما به حمله ایرانی پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/13757" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13756">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">از ارومیه و اصفهان هم موشک شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/13756" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13755">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چند موشک از تبریز و کرمانشاه شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/13755" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13754">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">موج دوم حملات ۳پا آغاز شد
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/13754" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13753">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صدا سیما ما وارد یک مرحله زورآزمایی جدید شدیم چون ناتانیاهو خواست ما را محک بزند
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/13753" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13752">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدا و سیما حمله ایران به شمال اسرائیل در همبستگی با لبنان را تایید کرد
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/13752" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d65867a2.mp4?token=HBUrxXmIMf45FALM07vE_T6J2PJKTawkL-IB7X0L0d-GcXX0988d1yje1ikZBcq1jbyxTmmxVPwmR-JRUEXErWyk1SPzh8vSG11-ExyuYbkkGlcg-aS25LVAmvEEB0mVtST9715W_YGEA-LsuHE_UC0VeJL0dxHzzmdpDwUf0p6up4jruJUCZU6w2ynypvdo1MBNCvmu45jCQ1T_pF4Mcdvu1OCA5kwKSSM5Z8HCa_w8o7j6avsQ4ZZQ3cx7cuCaQUU3iU_10xgFfy_Jc6puSTburglh-2Xn6w5CvC3GjiPioZF952QIxHPRuFi96ehsgGCh6idDlTOeoHlRlBuPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d65867a2.mp4?token=HBUrxXmIMf45FALM07vE_T6J2PJKTawkL-IB7X0L0d-GcXX0988d1yje1ikZBcq1jbyxTmmxVPwmR-JRUEXErWyk1SPzh8vSG11-ExyuYbkkGlcg-aS25LVAmvEEB0mVtST9715W_YGEA-LsuHE_UC0VeJL0dxHzzmdpDwUf0p6up4jruJUCZU6w2ynypvdo1MBNCvmu45jCQ1T_pF4Mcdvu1OCA5kwKSSM5Z8HCa_w8o7j6avsQ4ZZQ3cx7cuCaQUU3iU_10xgFfy_Jc6puSTburglh-2Xn6w5CvC3GjiPioZF952QIxHPRuFi96ehsgGCh6idDlTOeoHlRlBuPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/13751" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfa1bc4a4.mp4?token=KVhcS_tgHVAtg8u6JjEJ4DJplfR_5fGXhZUFRHoBJE7PVk1ytsQqFB4Sr-q-zwFZnQBR2eO41jCudIxgsRoF42HBKCsRjWUbEhUKCognbJBm4end1K89JQv9oLT7qizo-riOeTQ6qlo275Q0Lkf7PwcScBgzzO6sDsChIMjcwe8spi2SIRIo6EzYuEd7SkmqpTix57KEoFLxv-NEeTQT7aNrKCHWUru5ObQr0XAKbDjx9AMqj3SnGD_1lczfD63MoZ0T-LXaySwpS5KmPNHuGFadQhvMEVSz7caL0iefgH5m-OQzvOPaY0ULgUuvkcXqBkhzHl7xM6irlQt1lB_RdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfa1bc4a4.mp4?token=KVhcS_tgHVAtg8u6JjEJ4DJplfR_5fGXhZUFRHoBJE7PVk1ytsQqFB4Sr-q-zwFZnQBR2eO41jCudIxgsRoF42HBKCsRjWUbEhUKCognbJBm4end1K89JQv9oLT7qizo-riOeTQ6qlo275Q0Lkf7PwcScBgzzO6sDsChIMjcwe8spi2SIRIo6EzYuEd7SkmqpTix57KEoFLxv-NEeTQT7aNrKCHWUru5ObQr0XAKbDjx9AMqj3SnGD_1lczfD63MoZ0T-LXaySwpS5KmPNHuGFadQhvMEVSz7caL0iefgH5m-OQzvOPaY0ULgUuvkcXqBkhzHl7xM6irlQt1lB_RdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب ۴ موشک به شمال اسرائیل شناسایی شده است
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13750" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13749">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایران از کرمانشاه موشک شلیک کرد
💥
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/13749" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13748">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13748" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13747">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیل هیوم:مدارس در سراسر اسرائیل تعطیل شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13747" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13746">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بوی عرق زیر بغل روبیکا میاد
🤢
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13746" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13745">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اینترنشنال: دفتر مجتبی خامنه ای دستور حمله رو امضا کرده و فقط دستور به یگان های موشکی مونده
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/13745" target="_blank">📅 22:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13743">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شبکه 14 اسرائیل : در این حمله مشخص خواهد شد آیا ایران می‌تواند صد موشک را همزمان شلیک کند یا خیر
🚨
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13743" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13742">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">العربیه: وزیر کشور پاکستان که هم‌اکنون در تهران حضور دارد، هشدارهایی را به ایران درباره تشدید تنش‌ها در مسیرهای کشتیرانی دریایی منتقل کرده است
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13742" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13741">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هواپیماهای مسافربری در حال ترک حریم هوایی عراق می‌باشند.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13741" target="_blank">📅 22:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوست بیلیونرم : Regime will send rockets on Israel tonight.
رژیم امشب موشک‌هایی به سمت اسرائیل پرتاب خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13739" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دایرکت داره منفجررررررر میشه نمیخوام ببندم خواهش میکنم پیغام احساساتی  ندید فقط گزارشی ها دایرکت بدند
🙌🏾</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13738" target="_blank">📅 21:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروهای مسلح کویت در حالت آماده‌باش کامل قرار گرفته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13737" target="_blank">📅 21:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسرائیل هیوم: احتمال حملات موشکی ایران تا ساعاتی دیگر وجود داره.
براوردهای امنیتی حاکی از آن است که اگر ایران امشب با هدف قرار دادن شمال اسرائیل پاسخ بده، ممکنه مواضع شبه‌نظامیان (نیروهای مسلح وابسته به اسرائیل) داخل خط زرد (مناطق تحت کنترل تشکیلات خودگردان یا مناطق حائل) در غزه رو هم هدف قرار بده.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13736" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13735">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0895ae3f23.mp4?token=YCoATewVbMeVtg704XXXTF3TJ3RvNPkYULCdI1I6PtDeaTc8TUYEc53zoOlpcNIde41X_W5kzXZ5jjk0STF2hny1IrRQrziXc1Iyru_Ak9b1FBQvqAZyYfcSb0ASnNrjFg6jzuOxlvGlat8rzpvVvotUIhzaoanILPfrYPNeiKvhdW1pPJPuOK7g24r3nZNMNnTXZFZunImIOuKgBH-cYqT61dr611IUGHlCU1hlRGTBeCNYPjHlXsmTDAM5NuBmwRFd8atDTbY_bMPemB5WoWUf7gd8Nykq-3pbFFq4bE6zl-LS4AdngZywJY0dACUu9hbNKk1xCmL6LA1Sjd00Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0895ae3f23.mp4?token=YCoATewVbMeVtg704XXXTF3TJ3RvNPkYULCdI1I6PtDeaTc8TUYEc53zoOlpcNIde41X_W5kzXZ5jjk0STF2hny1IrRQrziXc1Iyru_Ak9b1FBQvqAZyYfcSb0ASnNrjFg6jzuOxlvGlat8rzpvVvotUIhzaoanILPfrYPNeiKvhdW1pPJPuOK7g24r3nZNMNnTXZFZunImIOuKgBH-cYqT61dr611IUGHlCU1hlRGTBeCNYPjHlXsmTDAM5NuBmwRFd8atDTbY_bMPemB5WoWUf7gd8Nykq-3pbFFq4bE6zl-LS4AdngZywJY0dACUu9hbNKk1xCmL6LA1Sjd00Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بریم برای اتاق جنگ
💥</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13735" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
به هواپیماهای که از تهران بلند شده اند دستور داده شده به باند فرود برگردند
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13734" target="_blank">📅 21:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایران ایر، ایرباس A300B4-605R به جای پرواز به جده، عربستان سعودی، به فرودگاه ایران تغییر مسیر داد
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/13733" target="_blank">📅 21:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هواپیمای بویینگ ۷۳۷-۵۲۴ کاسپین ایرلاینز به جای پرواز به استانبول، ترکیه، به تهران بازگشت.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13732" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش شلیک موشک از گرمدره و بیدگنه مقصد نامشخص !
🚨
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13731" target="_blank">📅 21:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13730">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش ها از پرواز گسترده جت های جنگی ‌ناشناس بر فراز اقلیم کردستان، عراق.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13730" target="_blank">📅 21:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13729">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش از صدای جنگنده در تهران و کرج
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13729" target="_blank">📅 21:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13728">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صداوسیما:  جمعیت مردم در تجمعات شبانه نصف شده.
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/13728" target="_blank">📅 21:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13727">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۴ اسرائیل: نخست‌وزیر بنیامین نتانیاهو با هیاتی از مشاوران حقوقی دولت ترامپ دیدار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/13727" target="_blank">📅 21:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13726">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">محمد مخبر: اسرائیل میز مذاکره را به آتش کشید، به زودی پاسخ دردناکی به تل‌آویو خواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/13726" target="_blank">📅 21:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13725">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ایران با صدور هشدار نوتام آسمان خود را  بست
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13725" target="_blank">📅 21:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13724">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پس از ارزیابی وضعیت امنیتی، ارتش اسرائیل تصمیم گرفته فعلاً تغییری در سطح هشدار یا سایر دستورالعمل‌های دفاع غیرنظامی ایجاد نکند و همان مقررات وضعیت فوق‌العاد فعلی را تا ساعت ۸ شب فردا تمدید کند
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/13724" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13723">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fba499bc1.mp4?token=CaA5065a7F7ojf6ikPCmlansdlPigqXI2ibUgJ5mORg8iVas0mKCz8MGdWeQ4SaL3CLbP_SaA63L3p1QxNNiFWWaExdD_KkaPBJnJv0Cs-pZS_3oh5wWbawKjCTq4ZUvl2hLVRFmK-rPPjATS9FwicGgDOlKnv-qVT8-uN4AvXIpeuXwmWVabY-mJz_tUm3qkLkouHAsnBpxOwJhUSzWCg-bz6zPgpXlAD1fsshQr3eHosJHxlPGED3FyCcvnkFlOqjkbD2xlxO_rapXjCugK9H7Vge3xskk9fDcRZl8qFRXYMsda6KuOo05kXwvPK-6wFI-FeP0nDAt9tQxqeyMog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fba499bc1.mp4?token=CaA5065a7F7ojf6ikPCmlansdlPigqXI2ibUgJ5mORg8iVas0mKCz8MGdWeQ4SaL3CLbP_SaA63L3p1QxNNiFWWaExdD_KkaPBJnJv0Cs-pZS_3oh5wWbawKjCTq4ZUvl2hLVRFmK-rPPjATS9FwicGgDOlKnv-qVT8-uN4AvXIpeuXwmWVabY-mJz_tUm3qkLkouHAsnBpxOwJhUSzWCg-bz6zPgpXlAD1fsshQr3eHosJHxlPGED3FyCcvnkFlOqjkbD2xlxO_rapXjCugK9H7Vge3xskk9fDcRZl8qFRXYMsda6KuOo05kXwvPK-6wFI-FeP0nDAt9tQxqeyMog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو حمله به ضاحیه بیروت
«یک مقام بلندپایه اسرائیلی:اگر ایران به ما حمله کند، واکنشی صورت خواهد گرفت که شعله‌های جنگ را دوباره برافروخته خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/13723" target="_blank">📅 20:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13722">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پرواز جنگنده های ارتش و گشت زنی بر فراز تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/13722" target="_blank">📅 20:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13721">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شرکت هواپیمای هلندی "KLM" لغو پروازهارو به اسرائیل، تا ۲۷ جولای تمدید کرد
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/13721" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13720">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فاکس نیوز: یکی از نمایندگان ارشد مجلس ایران اعلام کرد که ایران امشب در پاسخ به حملات ارتش اسرائیل در بیروت به سمت اسرائیل شلیک خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/13720" target="_blank">📅 20:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13719">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/13719" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13718">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خالیباف :  نه به اتش بس پایبندن نه به گفتگو باور دارن و با محاصره دریایی و نقض توافق ها درباره لبنان نشون دادن فقط زبون قدرت میفهمن
محاصره دریایی علیه ملت ما و چراغ سبز امروز امریکا به رژیم صهیونیستی ، پایگاه ها و دارایی های امریکا و اسرائیل تو منطقه رو هدف مشروع کرد
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/13718" target="_blank">📅 19:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13717">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27f5183ea.mp4?token=lU228tRi1__Fbu8cerb4mSFGl1BvyUeHOEUGCBBN5NtZme7Xdq9ABVWvuEQt4zQio9hJupWoWj06AbEcekBx8lvpT6BNGAcKFktES880j7NY7doHywRFFLm3itO2-SrNlQq18hfzj2BeUkDVqSqNrnM4qpJaRJl0mPkr_xYV9ag5NrFcl8GcpFrVw5X-ze1hcx7aRDZYgURWhRZhq6Z0m2MN-GbnFfazT5UUhIdrWsd4rsfbB3HSm_v7xjNVE03S2CRrN5vwszhLv_NvNxqx0sS6xv2zFLeLaHRHNAomRPrpte8pzgOb5m2rjnLYwWb_ykD2F38oybSGvrWvPkmrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27f5183ea.mp4?token=lU228tRi1__Fbu8cerb4mSFGl1BvyUeHOEUGCBBN5NtZme7Xdq9ABVWvuEQt4zQio9hJupWoWj06AbEcekBx8lvpT6BNGAcKFktES880j7NY7doHywRFFLm3itO2-SrNlQq18hfzj2BeUkDVqSqNrnM4qpJaRJl0mPkr_xYV9ag5NrFcl8GcpFrVw5X-ze1hcx7aRDZYgURWhRZhq6Z0m2MN-GbnFfazT5UUhIdrWsd4rsfbB3HSm_v7xjNVE03S2CRrN5vwszhLv_NvNxqx0sS6xv2zFLeLaHRHNAomRPrpte8pzgOb5m2rjnLYwWb_ykD2F38oybSGvrWvPkmrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگزت، وزیر جنگ آمریکا، می‌گوید پرزیدنت ترامپ به دستیابی به توافقی که تضمین کند ایران هرگز به سلاح هسته‌ای دست نخواهد یافت، متعهد است و افزود که ایالات متحده آماده است در صورت شکست مذاکرات، اقدام نظامی کند.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/13717" target="_blank">📅 19:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13716">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آی۲۴ نیوز عبری:
در پی تحولات در لبنان و تهدیدات از سوی ایران: نخست‌وزیر نتانیاهو قرار است در ادامه امشب جلسه‌ای با وزیر دفاع کاتز و رؤسای دستگاه‌های امنیتی برگزار می کند
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/13716" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13715">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قطر با صدور اطلاعیه‌ای، مسیر پروازها از طریق حریم هوایی خود را تغییر داده و مسیرهای جایگزین برای هواپیماهایی که از دوحه و فرودگاه‌های عربستان سعودی حرکت می‌کنند، فراهم کرده است.
این اطلاعیه از امروز ۷ ژوئن تا ۱۴ ژوئن معتبر است.
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/13715" target="_blank">📅 19:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13714">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک منبع اسرائیلی به i24NEWS:
تفاهمات آتش‌بس (بیانیه مشترک اسرائیل-لبنان-آمریکا) از روز پنج‌شنبه این است که اگر حزب‌الله به داخل خاک اسرائیل شلیک کند، ما به فرماندهی‌های آن‌ها در ضاحیه شلیک خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/13714" target="_blank">📅 19:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13713">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تسنیم: اسرائیل از ترس پاسخ ایران در آماده باش صد در صدی هستش
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13713" target="_blank">📅 19:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13712">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تا ۷۲ ساعت دیگه احتمالا لش خامنه ای خاک بکنن از کل دنیا سران کشورها رو مخفیانه دعوت کردن ایران @withyashar از منابع خودم جویا شدم گفتن اره مراسم چهارشنبه تا دوشنبه هست</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/13712" target="_blank">📅 18:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13711">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صابرین نیوز به نقل از منابع آگاه
ایران قاطعانه به نقض آتش بس پاسخ خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/13711" target="_blank">📅 18:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13710">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تا ۷۲ ساعت دیگه احتمالا لش خامنه ای خاک بکنن از کل دنیا سران کشورها رو مخفیانه دعوت کردن ایران
@withyashar
از منابع خودم جویا شدم گفتن اره مراسم چهارشنبه تا دوشنبه هست</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/13710" target="_blank">📅 18:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13709">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رادیو ارتش اسرائیل : اسراییل در اماده باش کامل قرار گرفته
مردم در نزدیکی پناهگاه ها بمونن
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13709" target="_blank">📅 18:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13708">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مرندی عضو تیم مذاکره‌کننده:
صهیونیست‌ها مجازات خواهند شد.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13708" target="_blank">📅 18:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13707">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جلسه اضطراری شورای عالی امنیت ملی ایران حدود نیم ساعت پیش به پایان رسید و
«تصمیمی گرفته شده است»،
اما منتشر نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/13707" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13706">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بعد از تهدید سخنگوی کمیته امنیت ملی جمهوری اسلامی، اسرائیل حملات را شدیدتر کرد و با جنگندههای خود جنوب لبنان را به موشک بست.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/13706" target="_blank">📅 18:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13705">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری اسراییل :احتمال دارد در ساعات آینده حملات موشکی هماهنگ شده ای از،چند جبهه به ما شود
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13705" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13704">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگوی کمیته امنیت ملی در مجلس ایران، ابراهیم رضایی:
ما به حمله رژیم صهیونیستی به ضاحیه پاسخ قاطع و دردناکی خواهیم داد. باید این سگ دیوانه تنبیه شده و به جای خود بازگردانده شود.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/13704" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13703">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13703" target="_blank">📅 17:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع عربی: تحرکات گسترده و انبوه موشکی در ایران مشاهده شده
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13702" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13701">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شبکه خبر: ساعات مهمی در پیش داریم
@withyashar
🚨</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/13701" target="_blank">📅 17:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13700">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العربیه: حزب‌الله پس از بمباران حومه جنوبی بیروت شوکه شده زیرا مقامات ایران به رهبران حزب اطمینان داده بودند که اسرائیل این منطقه را بمباران نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13700" target="_blank">📅 17:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13699">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e9d489ab.mp4?token=sbEpE2sL57sWRBOThndd3_dFUWo-gplmxt1-JW7z9Ls7IG0w2I6rZkmhF6xC2y8DyZLYZyupnV1AQN2t4exZbxhLutrNH3ydRu7BwIbtxHRxCCLJ3UxEWcOdPCS_ApU4RP6rEqfzwdfq1gof9FC7gwlFNR8ZYwkAtbpFYzb7ndwvedxsPP81Yvvscq8hmVacTlQ7UjK22UGJtAN6m5Tkcj6_L4QDp9vxLYM8YLCrhcvOJJmuPinD_Ofx9Zr3tY7io_TpQxRMQ3RsIRDnxYaXK4DsA7XwBLY_lH7plMlAjVneYTFKp_HZcDoGnFry9KL-PCxC7GNHijbGXhLik2VYXwJfoyqQFbH8OJOgpFJPdZOXMDoIfUuesaVDG1DX3nCXW4qsVI-or3wWbJtPhr9lZ1bWINSqH0k1tpIZu5EFIad6MB0k8vVm6Km3F8EcJzrxzxyC-kS64D_BwJ70rmnCsKa5intX4fjIcl_mTnQ-JpDvY6SMwKqwVke9XN5yQTgNdoaTXypxi34329JbyWpM1qSFozxDAQwutz7u4EB-yXSRU55PuCBDS4iAe1Pd32EcxVfeoHX0kWsDlI97HTF2ff5Qk__HrDfT2evqo9z8WWS20Xag-bbkog98QjPuWKNVvSSjn4AY-J9Y_-dBkSOOhBRMfevpOZUpEGveDNO1JYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e9d489ab.mp4?token=sbEpE2sL57sWRBOThndd3_dFUWo-gplmxt1-JW7z9Ls7IG0w2I6rZkmhF6xC2y8DyZLYZyupnV1AQN2t4exZbxhLutrNH3ydRu7BwIbtxHRxCCLJ3UxEWcOdPCS_ApU4RP6rEqfzwdfq1gof9FC7gwlFNR8ZYwkAtbpFYzb7ndwvedxsPP81Yvvscq8hmVacTlQ7UjK22UGJtAN6m5Tkcj6_L4QDp9vxLYM8YLCrhcvOJJmuPinD_Ofx9Zr3tY7io_TpQxRMQ3RsIRDnxYaXK4DsA7XwBLY_lH7plMlAjVneYTFKp_HZcDoGnFry9KL-PCxC7GNHijbGXhLik2VYXwJfoyqQFbH8OJOgpFJPdZOXMDoIfUuesaVDG1DX3nCXW4qsVI-or3wWbJtPhr9lZ1bWINSqH0k1tpIZu5EFIad6MB0k8vVm6Km3F8EcJzrxzxyC-kS64D_BwJ70rmnCsKa5intX4fjIcl_mTnQ-JpDvY6SMwKqwVke9XN5yQTgNdoaTXypxi34329JbyWpM1qSFozxDAQwutz7u4EB-yXSRU55PuCBDS4iAe1Pd32EcxVfeoHX0kWsDlI97HTF2ff5Qk__HrDfT2evqo9z8WWS20Xag-bbkog98QjPuWKNVvSSjn4AY-J9Y_-dBkSOOhBRMfevpOZUpEGveDNO1JYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه پیاده‌شدن تیم ناملی از هواپیما؛
این کاروان با نام میناب ۱۶۸ کمی پیش وارد تیخوانا مکزیک شد
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13699" target="_blank">📅 17:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13698">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، در گفت‌وگو با CNN گفت:
مشکل اصلی در مذاکرات با آمریکا اینه که اونا مدام موضع خودشون و خطوط قرمز رو تغییر میدن و حرف هاشون متناقضه.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/13698" target="_blank">📅 17:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ در رابطه با مجتبی:
ولی اون به شدت زخمیه، دوست ندارم که بگم داخل ایرانه یا نه.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13697" target="_blank">📅 17:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ : مجتبی خامنه‌ای به شدت زخمی شده اما بسیار شجاعه
چون که خیلیا اگه جاش بودن عمرا تو این وضعیت به فکر اینکه با آمریکا چه مذاکره و توافقی داشته باشن اصلا فکر نمیکردن ولی اون براش مهمه پس شجاعه!
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/13696" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b1d2798a.mp4?token=QgSW3Qt2En8hMfJCM1TK6erbhXsxPtiU9ibCBdyGaRde4vvtvB9IBMYH_jAmiLEstp8H8CEPnCfW7Mr8j_XOc0VcSG4fUxT-AXshFcZNYcwdt2Z9dUJcxnJlRSyHOXXsExmBWOL8N_FOvqes0XSMX66BvTTa5UHXz-DZZ8X-Hdij-fnFH0Xj6emweYDHdN1NNFGhjnHlYBIbsgEmz8XTPs-ECFg6VdZswYJKpscphgfCTXpeNcttDDNIFh2Fb9gIpk2O80m7FFFIFiEX7wTo68POpgBRsQlT86lc7bNA86L3eQEdAE8tccb6Mmpksg-k3gfdtbwA4X2EeAt2_CXIv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b1d2798a.mp4?token=QgSW3Qt2En8hMfJCM1TK6erbhXsxPtiU9ibCBdyGaRde4vvtvB9IBMYH_jAmiLEstp8H8CEPnCfW7Mr8j_XOc0VcSG4fUxT-AXshFcZNYcwdt2Z9dUJcxnJlRSyHOXXsExmBWOL8N_FOvqes0XSMX66BvTTa5UHXz-DZZ8X-Hdij-fnFH0Xj6emweYDHdN1NNFGhjnHlYBIbsgEmz8XTPs-ECFg6VdZswYJKpscphgfCTXpeNcttDDNIFh2Fb9gIpk2O80m7FFFIFiEX7wTo68POpgBRsQlT86lc7bNA86L3eQEdAE8tccb6Mmpksg-k3gfdtbwA4X2EeAt2_CXIv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما یک محاصره داریم. این بسیار مؤثر بوده است. و دلیل اینکه ما این محاصره را داریم این است که آنها تلاش کردند محاصره کنند، و حالا ما آنها را محاصره کرده‌ایم.
آنها محاصره‌ای ایجاد کردند، پس ما آنها را محاصره کردیم. ما محاصره نهایی را داریم.
من این را جنگ نمی‌دانم، اما اگر بخواهید آن را اینگونه تعریف کنید، فکر می‌کنم می‌توانید
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13695" target="_blank">📅 17:07 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
