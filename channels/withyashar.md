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
<img src="https://cdn4.telesco.pe/file/un6TNAbWI5MzWD1nf511yrkNGLxTULc1XXLbtUhaeLl5eDD5wxYwEz64CBcO9hR1AusC-niWIYeESjMc9FZw_NsNPmLKxfNDt0TAsBhOuF3F_TSfJE_phpDneo6EFr_6y_Nznnh_Awu4SsEWiTgEySbEmmDk6T1AAv6dVQlUW4XfhH6lOnyD-pzcCAuk91QezI3oA_3xmoi6inOBQpc3mOoDK4KxNZRfDOXtKOCEC8ozjVfuiYimOp5BnNsPikB73_-xkvXC1YMb-R-HT7Q68OIvEDHrrTjTrhSNR4up1GlkXP694QKdx74IAVBcwEu2m4IEocjwAde9ymetcMHOgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 277K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 03:12:00</div>
<hr>

<div class="tg-post" id="msg-12763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/withyashar/12763" target="_blank">📅 03:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/12762" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8116492af1.mp4?token=nsT8ZUP7c-sO-Yi6ztsSWN4wMQvpDYoyv3Qb76GXvJDDghxff1QybMkSHJlBVaEoPrKIZzEsw7cbUM0ivHkf7s8sXaR1hUpI-KozZCc61ra5rP7Y3gY6YCoe3xalBobbYIG-NZQNjhKa4vP76SIfcvA-SCDA6x2Ptx01orj0P00xB_G77IoPa9NfzMCdp4DyfuwmYcAmpCK-ujTXsP8ivT192EbIIIr6DT3spr9tJUpz1YL3RAQ4uwjSWWUk6UkXJRY38XbZ4XsAFDTWvKTHvsxut3u-D9cvGczqJGRm3N8Tg_ErRqXtrD9wJ4t5I071yeJ2F3hOd-RWZgQO-QNXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8116492af1.mp4?token=nsT8ZUP7c-sO-Yi6ztsSWN4wMQvpDYoyv3Qb76GXvJDDghxff1QybMkSHJlBVaEoPrKIZzEsw7cbUM0ivHkf7s8sXaR1hUpI-KozZCc61ra5rP7Y3gY6YCoe3xalBobbYIG-NZQNjhKa4vP76SIfcvA-SCDA6x2Ptx01orj0P00xB_G77IoPa9NfzMCdp4DyfuwmYcAmpCK-ujTXsP8ivT192EbIIIr6DT3spr9tJUpz1YL3RAQ4uwjSWWUk6UkXJRY38XbZ4XsAFDTWvKTHvsxut3u-D9cvGczqJGRm3N8Tg_ErRqXtrD9wJ4t5I071yeJ2F3hOd-RWZgQO-QNXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی همکنون در آسمان اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/withyashar/12761" target="_blank">📅 02:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:
ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد
@withyashar</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/withyashar/12760" target="_blank">📅 02:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه.
@withyashar</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/withyashar/12759" target="_blank">📅 02:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/12758" target="_blank">📅 02:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/withyashar/12757" target="_blank">📅 02:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/withyashar/12756" target="_blank">📅 02:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یا موسی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/withyashar/12755" target="_blank">📅 02:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پدافند اصفهان فعال شد !
@withyashar</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/12754" target="_blank">📅 02:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فارس : شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقه هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
@withyashar</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/withyashar/12753" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبر گزاری فارس‌ انفجار رو تایید کرد !!!
@withyashar</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/12752" target="_blank">📅 02:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تایید نشده ۳ نفر‌گفتن ماشین این کاربر‌ با آدرس گفته :
بولوار‌خلیج فارس یه ماشین رو با پهپاد زدنن رفت رو هوا و بعد پدافند با تاخییر شروع کرد فعالیت
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/12751" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">داداش من بندرم ۳ تا انفجار ۳۰ مین پیش بود و تا ۱۰ مین پیشم صدای پدافند می اومد میگن گویا یه ماشینو زدن و ترور بوده
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/12750" target="_blank">📅 02:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/12749" target="_blank">📅 01:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12748">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چیزی ‌نیست بی بی اومده یه قلیه ماهی ‌بزنه بره
🐟
شلوغش نکنید</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/withyashar/12748" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سلام همین الان پدافند بندر عباس درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/12747" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارشها شما اکثرن به پایگاه هوایی/فرودگاه اشاره میکنه</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/12746" target="_blank">📅 01:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صدای سه انفجار در بندرعباس دوباره
@withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/12745" target="_blank">📅 01:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارشهای ززززیاد از انفجار در بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/12744" target="_blank">📅 01:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کره شمالی تشکیل ائتلاف چهارگانه شامل آمریکا، استرالیا، هند و ژاپن را محکوم کرد. پیونگ یانگ همچنین تاکید کرد که هرگز از برنامه هسته‌ای خود چشم‌پوشی نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/12743" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=DouNo95Cg_wJESW8TAq4sUrYQKyiMqQVYpr0_FMGp-oDkN4TqenfEBVEM9rvJRC7kLQO8G43Y44aE6OmJUTXxjgA8u7zYWkSW_kyu9EJaCQ2CW2rJ6QSZXIODbO7H0vR8Am-Ro3sVx6mrtgNKWC2bHkdFUudyhSd3yerN-cO_my2nDIhLMMYEzsPLPoP1IRv8CQkShWEoYXR1oJZp-vy3U-_aCxG0Iwe0zAW_Zqn01mfEDI7g8_WbFAXyRlq8eyM0uqUyC3pCAgSGgAG79nkT80EpB1RJ4xX0Ai-gmqFyFoMgKtBSawR5QPMaSxj9vYYatRY89RUBwk5C_qSyCzp1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=DouNo95Cg_wJESW8TAq4sUrYQKyiMqQVYpr0_FMGp-oDkN4TqenfEBVEM9rvJRC7kLQO8G43Y44aE6OmJUTXxjgA8u7zYWkSW_kyu9EJaCQ2CW2rJ6QSZXIODbO7H0vR8Am-Ro3sVx6mrtgNKWC2bHkdFUudyhSd3yerN-cO_my2nDIhLMMYEzsPLPoP1IRv8CQkShWEoYXR1oJZp-vy3U-_aCxG0Iwe0zAW_Zqn01mfEDI7g8_WbFAXyRlq8eyM0uqUyC3pCAgSGgAG79nkT80EpB1RJ4xX0Ai-gmqFyFoMgKtBSawR5QPMaSxj9vYYatRY89RUBwk5C_qSyCzp1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حتما با پوشک بسته نگاه کنید
⚠️
میگن سیلوستر استالونه بعد از دیدن این ویدیو فروش آنلاین تمام فیلمهای رامبو رو متوقف کرد.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12742" target="_blank">📅 00:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">علیرضا فیروزجا با پرچم فرانسه نفر اول شطرنج جهانو شکست داد
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/12741" target="_blank">📅 00:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/12740" target="_blank">📅 00:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عضو تیم رسانه‌ای هیئت مذاکراتی ایران: سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود!
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12739" target="_blank">📅 23:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یاشار جان  احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12738" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromE R F A N</strong></div>
<div class="tg-text">یاشار جان
احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12737" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم! و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/12736" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKnow</strong></div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم!
و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12735" target="_blank">📅 23:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شاهزاده رضا پهلوی جمعه پیش در نشستی با شماری از فعالان رسانه ای  که ویدیو آن الان پخش شده گفت :  تیشرت های سیاه یا ساواک به خصوص و هر چیزی غیر از تم اصلی شیر و خورشید نپوشید این جریان در کمترین حالت ایجاد جنجال میکند و انحرافی است  من واقعاً درک نمی‌کنم این موضوع از کجا آب میخورد و این مسئله نگران‌کننده است.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12734" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12733" target="_blank">📅 23:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12732" target="_blank">📅 23:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2ksulAz5C5DgXKE4YxLdhK5BaA0LtmqA_aA4b5L6dtAK9yQNks11zZvYFU9baBzSuPbSZr4kWMxsT6UC87VyglrYa5H5l2USl45bYelhhd0SbtflxseqYXdg2HAo72GWJDEq0eiyO0hgtDmAIWyKy65Tn6L5aH9QfZgLBaM-8qTpa2mROiQYEtMNs8B0vkjLCyAsJOoH2dFfLxy8kLPAQHvKMFmUZ5q1ej3Var_S4sBDTyIqgE1Hip8yP3cPUl2HYfcLFZccWz6cM-iQgNnSja181kwYl-diNf8cwh0eg_eBy56ukga3mX2MAzYRmO2OmbPArxEcg18b7jcRB4Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : داداش این ایده ایی که دادی رو یه مقدارخلاقیت دادم بهش که بفهمن دقیقا چطورمیشه رفت بدون پرچم
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/12731" target="_blank">📅 23:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/12730" target="_blank">📅 23:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هم اکنون گزارش ها از دو ترور بزرگ در شمال غزه.
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12729" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12728">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اتاق جنگ با یاشار : کاری‌ نداره اگه همه با هم متحد باشن میتونن ، فقط با پوشیدن لباس های سبز سفید ، قرمز و زرد یه ابر پرچم قول آسای انسانی‌ پیکسلی درست کنند
🧠
😍
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12728" target="_blank">📅 22:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12727">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12727" target="_blank">📅 22:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12726">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12726" target="_blank">📅 22:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12725">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58450dfb0.mp4?token=mJElCDyEkU953tqp7U1jMzw5YEum-q37qDSxDbtfu-q0DVLTgpIes41Csf8TIJSbx04NSotShiPejoWA1gUdriye5NJ14c6P7YAWhzQLfUn8dktPTxKbPBoC6hByfm0_vyCGZM2XbwZtMhc_nKWvBUMB8F9oWEtzDC-d3YS5E1EGw9sKOx_Ik4G93gptAhSFY7NidLIcrNhxuPSc65duBwx79MAVC1TXML68jtlQCBEUM8STkXuuvss3CywCQJ4Co610P2Ccx_Dc2tacpLU_GEsC67pRkwMjwojhN17MzO7z02JjgaJu_jRiDoV8tgUcfb_oVmpKs7zoiKIkaZosaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58450dfb0.mp4?token=mJElCDyEkU953tqp7U1jMzw5YEum-q37qDSxDbtfu-q0DVLTgpIes41Csf8TIJSbx04NSotShiPejoWA1gUdriye5NJ14c6P7YAWhzQLfUn8dktPTxKbPBoC6hByfm0_vyCGZM2XbwZtMhc_nKWvBUMB8F9oWEtzDC-d3YS5E1EGw9sKOx_Ik4G93gptAhSFY7NidLIcrNhxuPSc65duBwx79MAVC1TXML68jtlQCBEUM8STkXuuvss3CywCQJ4Co610P2Ccx_Dc2tacpLU_GEsC67pRkwMjwojhN17MzO7z02JjgaJu_jRiDoV8tgUcfb_oVmpKs7zoiKIkaZosaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما شرط جدید ایران برای توافق با آمریکا را اعلام کرد: پرداخت غرامت ۳۰۰ میلیارد دلاری از آمریکا به ایران
!
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/12725" target="_blank">📅 22:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12724">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در اسرائیل پرونده‌ای جنجالی به نام «پرونده بیلد» فاش شده است. طبق این گزارش‌ها، یک سند محرمانه منتسب به حماس عمداً به رسانه‌ها درز داده شد تا خشم افکار عمومی از دولت بنیامین ناتانیاهو کمتر شود.
گفته می‌شود «آری روزنفلد» و پدرزنش یک مسیر غیرقانونی برای انتقال اسناد محرمانه از سازمان اطلاعات نظامی اسرائیل به دفتر نتانیاهو ایجاد کرده بودند. سپس تلاش کردند پیام‌ها و روایت‌های سیاسی خاصی را وارد سخنرانی‌های نخست‌وزیر ناتانیاهو کنند تا بر افکار عمومی از او تأثیر مثبت بگذارند.
این پرونده «بیلد» نام گرفته چون بخشی از اسناد ابتدا به روزنامه آلمانی
Bild
رسیده بود. مخالفان دولت می‌گویند از اطلاعات امنیتی برای اهداف سیاسی استفاده شده، اما حامیان نتانیاهو این اتهامات را اغراق‌آمیز و سیاسی می‌دانند.
@withyashar
اسرائیلی ها هم دنیایی دارن خوب‌ مردی بی بی برا خودتون اسن کارو کرده ! ولی مخالفاش داستان کردن !</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/12724" target="_blank">📅 21:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12723">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12723" target="_blank">📅 21:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12722">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سلام یاشار جان خسته نباشی، ممنونم بابت زحمات
میگم یه سوال تو خبر دارین که میگن جلسه کابینه کمپ دیوید یه تله بوده که کی اطلاعات رو لو می‌داده و فهمیدن که جی دی ونس بوده؟!</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/12722" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش اتاق جنگ اعلام حضور کنید. مانور امشب شروع شد. این کامنت زیر پست بی بی را لایک کنید، ریپلای کنید و اگر میتوانید اد تو استوری هم بکنید و به دوستان خود هم بگویید این کار را انجام دهند. آماده میشیم برای مانور نهایی در دوشنبه. توجه کنید فقط همین کامنت را لایک کنید، حتی پست را هم لایک نکنید که کاملا دیده بشه
❤️‍🩹
🙌🏾
https://www.instagram.com/p/DY2dIhsM-VK/?igsh=MXFhaGU4NzliZzVmaw==
ترجمه:
تبریک می‌گویم بی بی جون، فرزند راستین کوروش کبیر.
دیگر زمان آن رسیده که مقدمات حمله به ایران آغاز شود.
مردم ایران در نهایت ناامیدی فرو رفته‌اند.
لطفاً این لحظهٔ تاریخ‌ساز را هرچه زودتر رقم بزنید.
هر روز در ایران، روح جوانان ما را از جسمشان جدا می‌کنند.
تمام چشم امید ما به شما دوخته شده</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12721" target="_blank">📅 21:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12720">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12720" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12719" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSG</strong></div>
<div class="tg-text">ماجرا ری اکشن پر قرمز چیه دیگه ؟؟همه دارن میزنن
😂</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/12718" target="_blank">📅 21:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1s8mjW1WX-4Dc8OrLnxRJNAloAo3Plk88AN6raRLSKDk30rWliCl8hTTr3bUwo-rJGgS-m20MyiJ7TPu9tish135FPP4a0-ecf-j23IWfz7APGN4tOwzqz7U2VU3rO6rDsYK2PfHJvrgBHghncb33XFnYVag1jkwoyVg3RBVqfmfQ1_yI7HW7mME1FN0eocPpTudztHQPRm5zr5ITjXan8MqQseWjumqCf3pUslYsJbRIv0LOd9rvGXrwMmDySxsZq7Ux70be8pKA3xN5ttJDMjT_17x6mrkV-_Eei7oxWrdF5z079pnpBx22BemjBZNNWkQz_RmP6KNgLBUTX-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی رد لغو تحریم‌های ایران از سوی دونالد ترامپ، بازار سهام ایالات متحده در عرض تنها ۲۰ دقیقه، ۲۳۰ میلیارد دلار از ارزش خود را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12717" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: اوباما کشور اشتباهی را انتخاب کرد. او باید کشور دیگری را انتخاب می‌کرد. به شما نمی‌گویم که آن چه بود. او وقتی ایران را انتخاب کرد، کشور اشتباهی را انتخاب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/12716" target="_blank">📅 21:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار : هیچوقت انقدر مشتاق نبودم حجاج هر چه سریعتر سلامت برگردن خونه هاشون
😅</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/12715" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12714">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12714" target="_blank">📅 20:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/12713" target="_blank">📅 20:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: دارن کم‌کم شروع می‌کنن چیزهایی رو که باید بهمون بدن، تحویل بدن. اگه این کار رو بکنن، خیلی خوبه.
اگه نکنن، هگست کارشون رو تموم می‌کنه.
ما درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول صحبت نمی‌کنیم.
وقتی اونا درست رفتار کنن و کار درستو بکنن بهشون جازه می‌دیم به پولشون برسن
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12712" target="_blank">📅 20:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار: آیا با این موضوع راحت خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ: نه(زیر دلم درد میگیره)
@withyashar
🤣</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/12711" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ :
ما کنترل پولی را که آنها ادعا می‌کنند مال خودشان است، در دست داریم. ما کنترل آن پول را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12710" target="_blank">📅 20:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/12709" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhesam | امیرحسام</strong></div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/12708" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیت هگست درباره ایران:
آنها ممکن است موشک داشته باشند، اما در حال حاضر نمی‌توانند موشک‌های بیشتری بسازند. نمی‌توانند پهپادهای بیشتری بسازند. نمی‌توانند کشتی‌های بیشتری بسازند.
آنها آمدند و التماس کردند تا صحبت کنند.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12707" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHQy9giUvB_vxmaGBvnO0IIR0XWPQdKsvu7w-qyQLrZYB3VOaYkPlNiVVGE7UsWDBle8I2mS6y9kmAh1RTuvDzm6zZsFmFkrJuuDa1HUYVnez44JI9h5sMTwiQ8cF1-WiuoU_LvTzOgwYNBRG26oseEDUr4W6ZL-WXrXz0tg8mjY2NhNkUWxeLYWFkm_qd_WOjwkPXIhoZedScuVK21_dA9d5rG2WXFsKvstgRNkmwBjj6tXbdOS9wHIomFNkBZSm2Y-tc90maGVpk_ndAedudkb7WJ9x7CQSAPaA90qySunFmkYiwDN2feGlwLn-1GRz7y9vVSpJmg9b40d5ligvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️رئیس روس اتم می‌گوید روسیه تصمیم  گرفته است بازگشت کارکنان خود به نیروگاه هسته‌ای بوشهر در ایران را به تعویق بیندازد!
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12706" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مارکو روبیو :اگر ایران توافق قابل قبولی مارو امضا نکند جنگ را شروع خواهیم کرد این‌خواسته ترامپ است
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/12705" target="_blank">📅 20:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من به خاطر جهان جلوی آن را می‌گیرم.
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12704" target="_blank">📅 20:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره مذاکرات ایران:
آقای رئیس‌جمهور، اگر این کار جواب نداد، گزینه‌های دیگری در اختیار دارید.
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12703" target="_blank">📅 20:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">روبیو : ما با جمهوری اسلامی پیشرفت‌هایی داشتیم اما در روزهای آینده میزان اون رو خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12702" target="_blank">📅 20:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12701" target="_blank">📅 19:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=KXbXfIkSbl0lpkIZmVAAlj9pMzwvL4K5_KtyUs7uKw-3t8RtelJRUsc7ppLsQ9hiaZohiZF_T-p8PfYI7iM79loDJXFNmcN_A3WN13GNcAiQ4NAl573SnEd2WGtBIohY6Bh7rzkQNZfZjkGUbIrFX22dYfeEKiCyGJ3SDmjubQxzfflKeit45i98dzuH6GpKK2OAQXsYEGMPqDf1nawA-muaXIT8iQkt_ndOieTLKbYu3rysaLDMUeww3pQqqpR9XzhQbWT-sYM0EFmgqmJsL_fWBak4jRs__zOeUagwwAPH1BtXNSLDfk5Y9gz0qsklOGHVd1ngbFrcePgqP1aBcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=KXbXfIkSbl0lpkIZmVAAlj9pMzwvL4K5_KtyUs7uKw-3t8RtelJRUsc7ppLsQ9hiaZohiZF_T-p8PfYI7iM79loDJXFNmcN_A3WN13GNcAiQ4NAl573SnEd2WGtBIohY6Bh7rzkQNZfZjkGUbIrFX22dYfeEKiCyGJ3SDmjubQxzfflKeit45i98dzuH6GpKK2OAQXsYEGMPqDf1nawA-muaXIT8iQkt_ndOieTLKbYu3rysaLDMUeww3pQqqpR9XzhQbWT-sYM0EFmgqmJsL_fWBak4jRs__zOeUagwwAPH1BtXNSLDfk5Y9gz0qsklOGHVd1ngbFrcePgqP1aBcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران :
ایران خیلی دنبال توافقه. هنوز به نتیجه نرسیدیم و راضی نیستیم، ولی یا توافق میشه یا مجبور میشیم کار رو تموم کنیم.
اونا دارن از روی استیصال مذاکره می‌کنن.
اونا دیگه نیروی دریایی و هوایی ندارن و رهبرانشونم هم رفتن.
ایران فکر می‌کرد میتونه صبر کنه تا منو خسته کنه
به انتخابات میان دوره اهمیتی نمیدهم اونا گزینه دیگه ایی جز توافق ندارن
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12700" target="_blank">📅 19:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اینترنشنال باز خل شده ؟ چرا ترامپ رو انقدر میکوبه ؟!</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/12699" target="_blank">📅 19:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم @withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/12698" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx66A-tzAe8khLKKDri2XmqGGe46mwT1grZvLGqo_dHgIMkvohWNwB4fmWJ4DVZ9Z51pOaVnmeVEKY-5Ay1Yfp2k-Dxd9rKDIIIY5d_YwBQ9NanQS56XgMdPbw4u20d0DwAssdVogKVyp6P7cNa91JesWoTq52cN_E0K9MmEYxrkfyorbLIYuzOUjVlPzHJ-YRBMKjk5QSV92XO0CDqZLjfvHJf4rU14OyQyWP0WeQ-YSc-l_9OFEqigJdHJdO8xv0rc88MnjrecvyvHD3_JcLIrft-qeniJKRzsvYchZVpfedJcw35a0Bllvpi2joFVM_39yRKQGfnAVOFotEX4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/12697" target="_blank">📅 19:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q71IlAWWn07iSBQjVcjdBTRidHSV1nQ4OM2NA63fjsc_0WNRLRseRTyBZSI55zbkjq6X-ylTpbjcBHh8DlxN_BZTIq9Bx5ImtB6XvVVcxhfWN0cQudn1xSGZImOWGVeRdG0-htsgXsSnHFyUVD4EiNHvqgpY7qFZN9IC4ALRtw4wwqSNL12u88P2N5wYeeHL9GmKPiDwoVVDTz912e6ijO3OdPZbraJn6dDsK_IZ0RqxM1dq8Xbp1P7kJPGMYU8l8DtRU40zcw_PT_AYx9vfITmLesrzmdd_9k-PifIl8T9Itn961VCiOm_elZrMBD9YfP3fy4jhf8h9sqVJfD7ctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها می‌باشد.
میزان اختلالات در شبکه از دیروز بسیار بیشتر شده است، بسیاری از سرویس‌های گوگل و کلودفلر بسته شده اند و حتی قابلیت استفاده از گوگل پلی و اپ استور نیز وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/12696" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12695">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">یاشار جان من دندونپزشکم، دو سال سرباز بودم، صبح‌ها تو کلینیک ارتش یه شهرستان دورافتاده کار می‌کردم، بعدظهر هم تا شب تو کلینیک خیریه کار می‌کردم، از نظر مالی هیچ سودی برام نداشت فقط دلم می‌خواست دوران سربازی یه کار مفیدی هم برا اقشار ضعیف انجام بدم واقعاً از دلو جون مایه میذاشتم
اما اون دو سال، از آدمای قدرنشناس  و پر توقع رفتارای زیادی دیدم که باعث شد بفهمم خیلی از هم‌وطنا وقتی برا خدمتت هزینه‌ای پرداخت نمی‌کنن قدر خودت و کارتو نمی‌دونن انگار وظیفت بوده بشون خدمت کنی
همین تجربه‌ باعث شد دیگه سمت خیریه نرم
خیلی از مردم ما واقعا قدرنشناسن
وقت و انرژیتو بدون سود و فقط از روی عشق به کشورت صرف کاری می‌کنی بعد یه عده‌ پیدا میشن که  برن رو مخت و پشیمونت کنن</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/12695" target="_blank">📅 19:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB40eFNTVf-ufV3AUcZYz7CL_RRooEJAEn-pCwHL-ew3CDrsaMJ4c5EmEp7k0cowueagiaf_mvUSR6KgUYI1mdtRfjuK-xElR2GIIalijkES6GgdzDymqxp6Y98Q2WIn0441kCJWHUnbRDvTxVIIfqbMagZ30l3ekYE2rbFnCSk3WZjxVtJvjrE6b24laQq1gVzZmRowG8ZHpI-rkjirA4ybBhTlsgcdTfJhvrDzN-BLwepGGS4J2nayYC_wSCi5zCqGDcaR0kxk4qCW9qEXIIbqYEVmkNxnngKokAsKksXptodiq3QRLJRkZmJb7OD0oFHIesD8kPiBYV5Q5fM8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به PBS گفت که ایران در ازای کنار گذاشتن اورانیوم بسیار غنی‌ شده خود، از تحریم‌ها معاف نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/12694" target="_blank">📅 19:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlXs3XZW84RWdxe5SN1NBmIzWthl-9T2OlDeBOnD6nslak-6nQxhDGUfSLhDcnVKwnfUhHC_WE_nNNGZhYk8hAQ1w_boloVdgNzIp0zj1fmD78Cdo200iqpf4TM9l1mEWyyz1jGGgexyr4mPrHkYFr4QNL-CGuYKIq7uuHmBslquZFi_6MllkAyOK1QBp_3Mdyy82bD5SX6J4mCe9WFwe6yDwN6oSTuUhuQdxF8SpS4CXkVJ3kUZcIJkAhQ_Rx-P3OaYhCDkMXnwDNuuAloxnuDBuLgXT7QzQLjrb_1CjjWq0XAwHctOqoRiVmPVjwDjyBzhbDJ0uIvXnrwuEqFAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار برج چیتگر پامچال چهار از طبقه ۸ به بالا آتیش گرفته
این دقیقاً روبروی همون برجیه که تو جنگ دوازده روزه طبقه ۱۵ رو زدن بعد گفتن نشت گاز
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12693" target="_blank">📅 19:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری فارس: به عقیده ما احتمال دارد ترامپ در ساعات آینده به صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است
@withyashar
یاشار : عقایدتون رو …
🤣</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/12692" target="_blank">📅 19:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzqXjBDSTZ13RDLbhgilXULI7EEbj4ey_oBdYNuvL_1ASaosXcG0X-Nu_i8_ht7DoLFVga4ursM8n0IMz42n_EQAPFMy9nlSJeaHvSbTUXkYoGPUPN71VlLqFdQtU704G09HAbP0nuSqP0YhV37jzDoqs58_CcSzHvUbIs84qXjueKVikCzIB3BTXqtIb3uU31UFatt5sJE1-Lc2K-mLphAtydCFwN7OZE1I4XClyMtrviFgL8lV4sUDJCm3hk8P810-JtlN-245DdZIm5J9TYgm-KZERYfDgSRX0WRsJU12urFEnLIcoX3m2_fjrcBIVaSCVAFz4HoDuxMP1W97Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
عوامل موساد باعث بازگشایی اینترنت شدن.
@withyashar
یاشار : شاید باورتون نشه ولی درست میگه اینبار
🤣</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/12691" target="_blank">📅 18:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12690">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR8l6koMScmFUHEFLVlDAxQNTe5H0QV3lfpiENU5w2ZgTcOY-_tMw-uwMiYRmCNFUpKwxEtNYsr_wz2aSnDaJGCGRiztnNQPK0WCU7FUxvgFzFaztcJ1S5-MzIdLyg_9heDlOUZUpfrftujqVv8pILCZo7I_JXrlLNqYLHf950iC1uUviIT_Z-j0Dw6uyVgroXMbJ68dXfEZSTGtV8eYNmSMJglUrmSSDx_vrdX0SOmINmBJORbTDmFiitZD65Q82hUFEBc4Igok5Ykx0pC1QGhQq-3EUkCp1DdtW9iTbK4Z133G6po_FYY7zfmuzDIXlDCJNHQVIIGxB2qxXBAWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای از پایگاه هوایی رامشتاین در آلمان، ده‌ها فروند هواپیمای ترابری C-17A و C-5M نیروی هوایی ایالات متحده، چندین فروند هواپیمای ترابری C-130 و حداقل 10 فروند تانکر KC-135R را نشان می‌دهد که در آنجا مستقر شده‌اند.
در اتاق جنگ گفتم که رامشتاین مهم‌ترین پایگاه ایالات متحده در اروپا برای جنگ ایران است و به عنوان یک قطب لجستیکی کلیدی عمل می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/12690" target="_blank">📅 18:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12689">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/12689" target="_blank">📅 18:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12688">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کاخ سفید گزارش‌های مربوط به تفاهم‌نامه ایران را کاملاً ساختگی خواند.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12688" target="_blank">📅 18:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12687">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پست جدید
یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12687" target="_blank">📅 18:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12686">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش اسرائیل در اقدامی فوری دستور تخلیه کامل شهر بندری صور، بزرگ ترین شهر جنوب لبنان به همراه تمام روستاهای اطراففش رو صادر کرد
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12686" target="_blank">📅 17:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12685">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زلنسکی در پیامی به ترامپ:
اوکراین برای رهگیری موشک‌های بالستیک روسیه تقریباً به طور انحصاری به ایالات متحده متکی است.
سرعت فعلی تحویل موشک‌ها به اوکراین دیگر با تحولات هماهنگ نیست.
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12685" target="_blank">📅 17:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12684">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر دفاع ترکیه
یاشار گولر
:
ترکیه حقوقش در دریای اژه، مدیترانه شرقی و قبرس بر اساس قانون و تاریخ است و با هر اقدامی که بخواهد وضعیت موجود را به نفع برخی کشورها تغییر دهد یا جزایر غیرنظامی را نظامی کند مخالف است.
همچنین هشدار می‌دهد که نسبت به تهدید علیه منافع و امنیتش در دریاها بی‌تفاوت نخواهد بود و ارتش ترکیه توان مقابله با هر تهدیدی را دارد.
در مورد قبرس هم تأکید می‌کند که از ترک‌های قبرس حمایت می‌کند و به‌عنوان کشور ضامن از حقوق و امنیت آن‌ها دفاع خواهد کرد.
@withyashar
ترکیه با یونان و قبرس بر سر , مرزهای دریایی , منابع گاز طبیعی در مدیترانه شرقی و حق حفاری در آب‌های مورد مناقشه اختلاف جدی دارد.</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12684" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12683">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به گزارش فارس نیوز، آواربرداری، تعمیرات و بازسازی تمام واحدهای پتروشیمی آسیب‌دیده تنها در ۵۰ روز به پایان رسیده است و اکنون تمام تأسیسات قادر به تولید با ظرفیت قبل از جنگ هستند.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/12683" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مهر:
یک ساختمان اداری در فرودگاه امام خمینی آتش گرفت
دقایقی قبل یک ساختمان اداری در شهر فرودگاهی دچار حریق شده است.
این حریق در یک ساختمان اداری گمرک شهر فرودگاهی به وقوع پیوسته است.
تاکنون از علت دقیق حادثه و میزان خسارت و تلفات احتمالی اطلاعاتی در دست نیست.
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/12682" target="_blank">📅 17:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12681">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ امروز ساعت ۱۱ به وقت محلی (حوالی ساعت ۱۹ به وقت تهران) برای بررسی مذاکرات با ایران، جلسه‌ای با اعضای کابینه و دستیاران ارشد خود خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/12681" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین</strong></div>
<div class="tg-text">واقعا این ملت باید به دیکتاتور وطن پرست بالا سرشون باشه . ملتی که جمهوری اسلامی پرورش داده جز دزدی بی فکری پاچه خوار تو اوج بیسوادی ولی ادعای دانشمند بودن میکنن آدم فروشی ...... اینا با دموکراسی درست نمیشن فقط باید یه دیکتاتور بالا سرشون باشه مثل رضا خان بزرگ . این جماعت تو هر لحظه رنگ عوض میکنن در این حد احمق حالا یه عده میگن توهین میکنی با کلمه احمق ولی توهین نیس واقعیته یه واقعیت تلخ . حکومت هر کشوری طبق لیاقت مردمش اداره و اجرا میشه واقعا متاسفم پاسوز یه عده جوگیر احمق شدیم</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/12680" target="_blank">📅 16:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">درووود بهت یاشار عزیز،همین که توی حاشیه اصلا حرکت نمیکنی یعنی کارت درسته.فقط(( هدف ))مهمه تمام.</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/12679" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilad Farahmand 🐾</strong></div>
<div class="tg-text">درووود بهت یاشار عزیز،همین که توی حاشیه اصلا حرکت نمیکنی یعنی کارت درسته.فقط(( هدف ))مهمه تمام.</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12678" target="_blank">📅 16:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12677">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لیندسی گراهام:«مدت‌هاست برایم روشن شده که پاکستان به‌عنوان یک میانجی، فراتر از حدِ مشکل‌ساز است. دشمنی آن‌ها با اسرائیل، ریشه‌دار و دیرینه است.
این حقیقت را نمی‌توان انکار کرد که هواپیماهای نظامی ایران در پایگاه‌های هوایی پاکستان نگهداری می‌شوند؛ و همچنین مواضع و سخنان گذشتهٔ بلندپایه‌ترین مقام‌های پاکستانی علیه اسرائیل نیز نگران‌کننده است.»
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/12677" target="_blank">📅 16:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12676">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/12676" target="_blank">📅 15:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12675">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOzGP5ig1KTQzc0EsI-q0MFUmeyAfDhkC765UgB4vfjI2Qob0n8IBOwJI5qeQur7Bb20xrN6A2SGLWPGJJ-obCikzEp7sSFU0cBgg0xkjPiTcLqDuJmNoMTee822JwCGbTqH9TEQGn1Edv5x2En0TfQtnpgmF7UWa7eMAXQ-j_Qew1jB_WJs2mRctqYfI2xhjaHQkHAVmnEr3EGMCzkZtZRzNMXi8TiFV5j1GiqN6CJN8x-aQv7JsEXc2tREMiVenCqFoA3x1iGQUr7KMkjHSlWkOSfXgLlCkMADJKL7tP0qJV1XEVBdt_RZSyC6fw3EZ3aOuIhyXoF4Zl8yb12FNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث از جروزالم پست :
آزار و اذیت جنسی در زندان‌های ایران در دوران آتش‌بس به‌شدت افزایش یافته است
جروزالم پست
آزار و اذیت جنسی در زندان‌های ایران در دوره آتش‌بس به‌طور چشمگیری افزایش پیدا کرده است.
یکی از معترضان به مدیا لاین گفته که هنگام بازجویی با باتوم به او تجاوز شده است.
مرد دیگری پس از آن‌که مأموران ادعا کردند به پیکر همسرش بی‌حرمتی کرده‌اند، اقدام به خودکشی کرده است.
گروه‌های حقوق بشری می‌گویند از زمان شروع جنگ، دست‌کم ۳۶۴۶ ایرانی بازداشت شده‌اند و قطع اینترنت باعث شده ابعاد واقعی ماجرا پنهان بماند.
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/12675" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12674">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK3jSkJh9OEscCnLLYD2cz1g-cXafNbwtlO6CCmNLmuxS7e6TRAllvXBVWEd3Tm9WnX6AEUC_v0i3Nj-lWUJmtpFEW6M3DjFFrnIstHeAOiab_qWx7X9HCUzGI679Vy68iHRmLuvLlT4B2sPaXExjmxgOIzbsSxKc_YJ7MA4BzZlUAcW_Ntm2uQvniJ7niBqtF2yUEvImK6N7g7xbwC3-CakQM9znX6f4exmqYrm1DDngQ-Ju8j6XeyPRGBrCskURrtSNg3iKvmq5RBMQliFwV6ld0M0oVitjAlNhZWyTMpl9YK6LnCzvnNqzdKqi1_uQxS2rdRiRuSATUywQ7oebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای سوخت‌رسانی جدید نیروی هوایی اسرائیل، KC-46A Pegasus "Gideon" (301)، اندکی پیش در اسرائیل فرود آمد و ایال زمیر، رئیس ستاد کل ارتش اسرائیل، در مراسم استقبال حضور داشت. این هواپیما اولین فروند از شش فروند سفارش داده شده است و امکان سفارش دو فروند دیگر نیز وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/12674" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12673">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8b7f9a5a.mp4?token=Exj7AVmap0mmdB_KbTQRycieL8DXNgKJkVBjluEmTqcRJnNKqP0CjsbUXkgjKnsv5-YYqQZmmLZh_4rtEPOtADDQLNgSNHXY1z1NvNZD1DT3O9gENoCwFGD2nfCCTUoCJH2QpK82wW9pX-qhyucjeFjC6hvnJiucVYfaY6YQcWuSgOyTgYlWEkLgb41nqde3AKX9SN-ulw7wvnlJxbetQC8vIZpYGcnCmPh07CNutdb9S5QFfbSnAKGTCRqVG8brIEqihpbaOBU4j2kL_HboGvK4hn1x07Va-N3i_CT-7XQVPAidliuIP1GeR_FcACGw1k1Lf35i1JmD_nTjzIsHow8UVdcbPw0O1sXJ-bMCeDMN_jgI2Ntn_lPlnhS5CzLA7J4ftW1b2_yI_ZUic_nMjjiMB8VrU-VYkkKTFANQ3N465UCOPlCLXt3EJlUrVechFLxQ_dXCiFTFV14WboeV4m9_kXDFTrdSRybdX5dlfjWVGvOfWlEOY0gE3mml62G7YiXHV6XNsW0ZZ0owZetxcO2C17CipKJd-aNaah_kXvSn1Ew9H9THC_aK9LmK5e9axnl7dAK2Qdyaft1RRmKDP23ncUnJZCipQEzDu9BxbJ7tfmwcIPHt4fN94eDVgIT6VkOSonOb_fgBXMJe6Sd_9ttec7S0jhyeSXZuJOzo1uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8b7f9a5a.mp4?token=Exj7AVmap0mmdB_KbTQRycieL8DXNgKJkVBjluEmTqcRJnNKqP0CjsbUXkgjKnsv5-YYqQZmmLZh_4rtEPOtADDQLNgSNHXY1z1NvNZD1DT3O9gENoCwFGD2nfCCTUoCJH2QpK82wW9pX-qhyucjeFjC6hvnJiucVYfaY6YQcWuSgOyTgYlWEkLgb41nqde3AKX9SN-ulw7wvnlJxbetQC8vIZpYGcnCmPh07CNutdb9S5QFfbSnAKGTCRqVG8brIEqihpbaOBU4j2kL_HboGvK4hn1x07Va-N3i_CT-7XQVPAidliuIP1GeR_FcACGw1k1Lf35i1JmD_nTjzIsHow8UVdcbPw0O1sXJ-bMCeDMN_jgI2Ntn_lPlnhS5CzLA7J4ftW1b2_yI_ZUic_nMjjiMB8VrU-VYkkKTFANQ3N465UCOPlCLXt3EJlUrVechFLxQ_dXCiFTFV14WboeV4m9_kXDFTrdSRybdX5dlfjWVGvOfWlEOY0gE3mml62G7YiXHV6XNsW0ZZ0owZetxcO2C17CipKJd-aNaah_kXvSn1Ew9H9THC_aK9LmK5e9axnl7dAK2Qdyaft1RRmKDP23ncUnJZCipQEzDu9BxbJ7tfmwcIPHt4fN94eDVgIT6VkOSonOb_fgBXMJe6Sd_9ttec7S0jhyeSXZuJOzo1uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیمان بستم و شب و روز بیدارم
👑
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/12673" target="_blank">📅 15:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12672">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/12672" target="_blank">📅 15:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c0f02fec.mp4?token=eJ-qUtz3NKHuCtCVKcBge5oneNjpFF8JRQIq1R257G9ZArSaX4yv8OWOVEHUk2psgF4TOp7XW7ipLam-2DYMKeFUXXsntFv2HUYAti-KsoIbKTkayTMQP3SgnnyYU28ehhJjI9zhW6h9euvZ1RF63wLWMCuEDHIl8p4hr5ZbwZUzX4_0J2G888_iXtWrIKufQCen7bv55pwgmsrpsikg2vP-GeVjXr2gx2nRdzq1Ap1aIyxMmNCiiigEyhIxq2S9M-BGmERzZm-0q4Gl2sD4bcU58In7sW4CJI3GlgJpxUqiZXWPI_wP6jGGgHAkZwMbhzF8WgZpOfQEVmSQAXC8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c0f02fec.mp4?token=eJ-qUtz3NKHuCtCVKcBge5oneNjpFF8JRQIq1R257G9ZArSaX4yv8OWOVEHUk2psgF4TOp7XW7ipLam-2DYMKeFUXXsntFv2HUYAti-KsoIbKTkayTMQP3SgnnyYU28ehhJjI9zhW6h9euvZ1RF63wLWMCuEDHIl8p4hr5ZbwZUzX4_0J2G888_iXtWrIKufQCen7bv55pwgmsrpsikg2vP-GeVjXr2gx2nRdzq1Ap1aIyxMmNCiiigEyhIxq2S9M-BGmERzZm-0q4Gl2sD4bcU58In7sW4CJI3GlgJpxUqiZXWPI_wP6jGGgHAkZwMbhzF8WgZpOfQEVmSQAXC8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امنیت داخلی اسرائیل:
توافق ترامپ و ایران یک توافق بد است که می‌تواند به اسرائیل آسیب برساند. ما اجازه نخواهیم داد این اتفاق بیفتد!
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/12669" target="_blank">📅 14:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شبکه 12 اسرائیل:ناوگان هوایی آمریکا ظرف 72 ساعت به پایگاه‌های خود در اروپا منتقل خواهد شد و در صورت از سرگیری درگیری با ایران، هواپیماها در حالت آماده‌باش برای بازگشت به فرودگاه بن گوریون قرار خواهند گرفت
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12668" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/12667" target="_blank">📅 14:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بگو یادتون رفته پزشکیان همونی بود که ۳ ماه پیش جز شورایی بود که دستور کشتن ۵۰ هزار تا از بچه هامون رو داد واسه یه اینترنت شد ادم خوبه کاش وصل نمیشد همون
😡
😡
😔
😔</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/12666" target="_blank">📅 14:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommet</strong></div>
<div class="tg-text">بگو یادتون رفته پزشکیان همونی بود که ۳ ماه پیش جز شورایی بود که دستور کشتن ۵۰ هزار تا از بچه هامون رو داد واسه یه اینترنت شد ادم خوبه کاش وصل نمیشد همون
😡
😡
😔
😔</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/12665" target="_blank">📅 14:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حالا بدیش اینه که این کند ذهن این مدت نت هم داشته و پیگیر کانال هم بوده و همش پیغام میداده زر زر
😡
اخطار هم داده بودم و گفته بودم دیگه دایرکت نده کلا ، دیشب گفتم بعضی ها میخوان مغذشوت پلمپ باشه ! مگه یه معجزه اتفاق بیوفته
🪄</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/12664" target="_blank">📅 14:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">واقعا فک نمیکنی تو شرایط فعلی درست نیست فعلا پزشکتان خراب کنی ؟ این همه ادم دیوث هست تو اینا یکی ک داره جلو سپاه وایمیسه رو چت نزن روش</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/12663" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr_ACE</strong></div>
<div class="tg-text">واقعا فک نمیکنی تو شرایط فعلی درست نیست فعلا پزشکتان خراب کنی ؟ این همه ادم دیوث هست تو اینا یکی ک داره جلو سپاه وایمیسه رو چت نزن روش</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/12662" target="_blank">📅 14:19 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
