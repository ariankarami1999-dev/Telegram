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
<img src="https://cdn4.telesco.pe/file/oBfpaES4Axe1wKKIuW-qD39uKRjJoMVBkG0crslmv7S20c83jdKWBETEnIWK2w3JTU4ZXWte0Z0YbV5nDvmT8lEBHhN_xfEZQoYey4fXK4Kis3n4iQSF9LOEzpAIL47xoKfY3Wo1_EUAcCMyV7hbJst0bD7S5XU3LftORxUW707zWrnEGXR7Xt4iRrU5q7gq0S6UcHGGDCNO8iFA4osiU9aOPvs-1cNwYe7o3eZOJTmfpJ9jbeeY7VnUmgLSGum4lrF5kwkx_OgQaqSx58FotRqSebp__Hqkj99zxQqoz-Mom4UPgHFQcJcLe6hv38QDRvXOblbjRnl9Moy7OUI2Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 06:03:55</div>
<hr>

<div class="tg-post" id="msg-15816">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=mIkr-vGckFqYZyxxDc0AENku4fJp-mIwdLLxRW62zc7W16S7O5bvXOVyyw8n3oTOIecDqVoGnbD_FUBYmOB7Cwr0fnDGjKq2mq15z_Xjvz2zCGzYB6gtf4AWMMS_uQbFNBa1ZN8Gml2NfteF-wLWT_oecM1dUkXZh9WwZR6ry9T5ueVDjJQCHg15Q7J6NYtqpUEzcz_MA3lUHEVNnEFls1hvlyAuRQYd2yQ9dVWXFyF58p8SX6laydmBJQYqYpll9MMG2CWHRaCO2wY9kXb8Sj_9HCiMXziluJjCCnxN0JI28WPXsui7jiZFFi3iK5lEiAeZcf5xI6b0dXEoTTn_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=mIkr-vGckFqYZyxxDc0AENku4fJp-mIwdLLxRW62zc7W16S7O5bvXOVyyw8n3oTOIecDqVoGnbD_FUBYmOB7Cwr0fnDGjKq2mq15z_Xjvz2zCGzYB6gtf4AWMMS_uQbFNBa1ZN8Gml2NfteF-wLWT_oecM1dUkXZh9WwZR6ry9T5ueVDjJQCHg15Q7J6NYtqpUEzcz_MA3lUHEVNnEFls1hvlyAuRQYd2yQ9dVWXFyF58p8SX6laydmBJQYqYpll9MMG2CWHRaCO2wY9kXb8Sj_9HCiMXziluJjCCnxN0JI28WPXsui7jiZFFi3iK5lEiAeZcf5xI6b0dXEoTTn_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسی
🧕🏻
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/15816" target="_blank">📅 00:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15815">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شبکه المنار : توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/15815" target="_blank">📅 23:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15814">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جنگنده های اسرائیل بر فراز جنوب لبنان به پرواز درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/15814" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15813">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/15813" target="_blank">📅 22:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسرائیل و لبنان، عقب‌نشینی نیروهای اسرائیلی از جنوب لبنان را تکذیب کردند
یک مقام ارشد ارتش اسرائیل گفت که این کشور از منطقه حائل عقب‌نشینی نخواهد کرد. یک مقام نظامی لبنان نیز گفت که تحولات میدانی روزهای اخیر «خلاف عقب‌نشینی را نشان می‌دهد.»
ارتش اسرائیل هم در بیانیه‌ای اعلام کرد که تغییری در محل استقرار نیروهایش در جنوب لبنان ایجاد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/15812" target="_blank">📅 22:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15811">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هشدار نهاد مدیریت آبراهه خلیج فارس(PGSA) در‌مورد تبعات
تردد شناورها خارج از مسیر اعلام شده ایران
نهاد مدیریت آبراهه خلیج فارس‏ در پاسخ به استعلام‌های مکرر اعلام میکند:
هرگونه تردد از مسیرهای خارج از چارچوب تعیین‌شده PGSA، مشمول تضمین عبور ایمن نبوده و از پوشش بیمه و مسئولیت‌های مرتبط برخوردار نخواهد بود.
تبعات ناشی از تردد از مسیرهای غیرمجاز، برعهده مالک، بهره‌بردار و فرمانده شناور خواهدبود.
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/15811" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15810">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9xWb3_US6h8KPfzsm1QdXBCn7uq9XftCseHRxuhqd11v4Iy7NfFmnGfAwjUnpEKQd7WoTLKhjFQvtc82kXAmeyyMAKXfy7fC2eKjQv-Ul0ieEv1W__5OMfa4flYLyQ3KDEwYYThbsUPHp4xMinN6Gn6kTKU9-UsyhSpTOpxBC4IiEOTCO9gtGDPQUT4rPdmzb3-KXUwF3VetSNoO62B7UQa8ICvbtVImgvByIMC318Ve6blwQ9nY8i-GjV5XMG0IQbO7OgARV4DNTyuNU9QXk_HHV7j8kq0oMrXG3q_bwUN6-Xvjsm0ArPFpIxMb2nEmfOX_COspWR1jTv1PTL1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتشسوزی منطقه ویژه بوشهر الان
دوران جنگ دوبار زده بودن اینجارو
@withyashar
🚨</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/15810" target="_blank">📅 22:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15809">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ورود نیروهای اسرائیل به خاک سوریه
یک گشتی نظامی ارتش اسرائیل با عبور از خط مرزی، به حومه غربی شهرک «الرفید» در ریف جنوبی قنیطره حمله کردند.
نیروهای اسرائیل در جریان این حمله، تعدادی را بازداشت و آن‌ها را مورد بازجویی قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/15809" target="_blank">📅 21:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15808">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نهاد دریایی بریتانیا :  خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند @withyashar
🚨</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15808" target="_blank">📅 21:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15807">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نهاد دریایی بریتانیا :  خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند @withyashar
🚨</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15807" target="_blank">📅 21:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15806">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر انرژی آمریکا به سی‌ان‌ان:
لغو تحریم‌ها بر نفت ایران، امکان فروش آن در بازارهای دیگر و دریافت وجه آن به دلار را فراهم می‌کند.
دارایی‌های ایران که مسدود شده بودند آزاد خواهد شد و تحت نظارت شدید در مورد نحوه هزینه‌کرد قرار خواهند گرفت
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/15806" target="_blank">📅 21:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15805">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/15805" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15804">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moamelegari-trump(@withyashar).pdf</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/withyashar/15804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کتابی از دونالد ترامپ یکی از بحث برانگیز ترین شخصیت های سیاسی جهان.
رئیس جمهور آمریکا دونالد جی ترامپ ، جهان بینی حرفه ای و شخصی خود را در این کتاب جذاب و خواندنی بیان می کند، روایتی دست اول از ظهور مهمترین معامله گر آمریکا.
دونالد ترامپ : هنر معامله گری
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/15804" target="_blank">📅 20:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15803">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینم کتاب ترامپ دوباره</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/15803" target="_blank">📅 20:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15802">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش شبکه کان اسرائیل : آمریکایی‌ها در حال ترک فرودگاه بن‌گوریون هستند   ایالات متحده ۲۸ فروند هواپیمای سوخت‌رسان را تخلیه کرده و اسرائیل نیز به‌دلیل نگرانی از اختلال در پروازهای غیرنظامی در طول تابستان، اسرائیل خواستار تخلیه حدود ۲۰ هواپیمای دیگر شده است.…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/15802" target="_blank">📅 20:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15801">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بالگرد نظامی (بلک هاوک) نیروی هوایی ارتش اسرائیل که حامل «اسحاق هرتزوگ» رئیس جمهور این کشور بود، به دلیل نقص فنی ناشی از برخورد با پرنده در آسمان، مجبور به فرود اضطراری شد.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/15801" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15800">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شکست شاگردان پیاتزا مقابل آمریکا
🏐
جمهوری اسلامی ۰ - ۳
آمریکا
🇮🇷
۲۳|۲۰|۲۹
🇺🇸
۲۵|۲۵|۳۱
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/15800" target="_blank">📅 20:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15799">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یدیعوت آحارانوت:نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/15799" target="_blank">📅 20:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15798">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پایان ست دوم , لیگ ملت های والیبال
آمریکا
2️⃣
- جمهوری اسلامی
0️⃣
🇺🇸
25 | 25
🇮🇷
23 | 20
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15798" target="_blank">📅 19:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال 12 ، نتانیاهو :
هنوز ماموریت‌هایی برای انجام دادن وجود دارد، هنوز کارهایی علیه ایران و حماس باید انجام شود. ما تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/15797" target="_blank">📅 19:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نهاد دریایی بریتانیا :
خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/15796" target="_blank">📅 18:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/15795" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15794">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/15794" target="_blank">📅 18:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15793">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی :هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد. تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/15793" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15792">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/15792" target="_blank">📅 17:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15791">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=IHKZuhSO5L6qHAM4HRy2wZOPtwgZ9X7HV45-qDgr8we2_o8U6N0DIsX3t4PDioQLjSCRdwQMT0ir4n6iC82Ura8oC4BWxK2KCsiaqtsUY1N8djaKTm4onCAHoU3MFETHf5d1IIRzrWMqfWayokUjEPAyqa_4p6CXFdTJSESzRvMAW9WZ9mRY9cSNYhaN1DmKudSNcmMWFtsA_vTMrzlOUrmXyGTsbbEDAObpgnA8LDys2wdg1xo8HDxJtGCoE7M0Z0J-pFAk_L80iqV0Pw5eGyqg_2-FIO5X7CXxyu9mo_TD2vxcZk5s0GYadvFlL9CLY3Ov4_G4-olLX09MGsIjzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=IHKZuhSO5L6qHAM4HRy2wZOPtwgZ9X7HV45-qDgr8we2_o8U6N0DIsX3t4PDioQLjSCRdwQMT0ir4n6iC82Ura8oC4BWxK2KCsiaqtsUY1N8djaKTm4onCAHoU3MFETHf5d1IIRzrWMqfWayokUjEPAyqa_4p6CXFdTJSESzRvMAW9WZ9mRY9cSNYhaN1DmKudSNcmMWFtsA_vTMrzlOUrmXyGTsbbEDAObpgnA8LDys2wdg1xo8HDxJtGCoE7M0Z0J-pFAk_L80iqV0Pw5eGyqg_2-FIO5X7CXxyu9mo_TD2vxcZk5s0GYadvFlL9CLY3Ov4_G4-olLX09MGsIjzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۶ VHF نیروی دریایی سپاه:«عبور و مرور در تنگه هرمز فقط با اجازه نیروی دریایی سپاه و در مسیرهای تعیین شده امکان‌پذیر است.
اگر هر کشتی‌ای بدون اجازه ما، با سیستم شناسایی خودکار خاموش یا خارج از مسیر تعیین شده اقدام به عبور کند، مسئولیت هرگونه عواقبی بر عهده آن کشتی خواهد بود.»
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15791" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15790">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قالیباف: آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما صرف خرید محصولات کشاورزی آن‌ها خواهد شد. جالب است؛ تنها محصولی که ما در حال برداشت آن هستیم، همان چیزی است که شما کاشته‌اید: دهه‌ها بی‌اعتمادی. این محصول، ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا تنها سویاهای تراریخته، وعده‌های شکسته شده و یاوه‌گویی صادر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/15790" target="_blank">📅 15:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15789">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=jhySbyzGCWcx_lryJVR3jX0r0xz0ZD9cFs5SX7qcrQ7B6L84K1NTa4sbbtxMMY8xOWOwA94Bg5UilYPwbgGUbcCrJ8BG--Fc0C0_WHl3JmKJXHmvpWvmi9fuS3hoFNqtE7OEVd2QCE4EMGMEGckVMQOGzGd4Bb7idNdVIkQjlWLggQEtFIqVD8mae3uEttmpIBIbJmfcNClynaphtPBk3qVJejgPQQDokMPvaWZ2NMJP2jIojzRT18hXK2mclMOVi4FGq1RhxyUtjHhjNmUIe70YcrHBrcbHlz7W2U7AsQI7vyG_KF-r-Js2G2U3tY_TJHp0DCkcLzOb26fxRaDMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=jhySbyzGCWcx_lryJVR3jX0r0xz0ZD9cFs5SX7qcrQ7B6L84K1NTa4sbbtxMMY8xOWOwA94Bg5UilYPwbgGUbcCrJ8BG--Fc0C0_WHl3JmKJXHmvpWvmi9fuS3hoFNqtE7OEVd2QCE4EMGMEGckVMQOGzGd4Bb7idNdVIkQjlWLggQEtFIqVD8mae3uEttmpIBIbJmfcNClynaphtPBk3qVJejgPQQDokMPvaWZ2NMJP2jIojzRT18hXK2mclMOVi4FGq1RhxyUtjHhjNmUIe70YcrHBrcbHlz7W2U7AsQI7vyG_KF-r-Js2G2U3tY_TJHp0DCkcLzOb26fxRaDMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: هنوز مطمئن نیستم همه‌چیز تموم شده باشه، چون هر چند ساعت یه توییت جدید از ترامپ منتشر می‌شه و با هر توییت، تیتر خبرها عوض میشه؛
واسه همین فعلاً روی هیچ‌کدوم از حرف‌هایی که ترامپ زده حساب باز نمیکنم.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15789" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15788">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اختلال بانک‌ها بعد از چندین روز همچنان ادامه دارد
رصد گزارش‌های مردمی در شبکه‌های اجتماعی، کانال‌های اطلاع‌رسانی و بازخورد کاربران نشان می‌دهد شبکه بانکی ایران از فاز اختلال شدید عبور کرده و بخش عمده خدمات به وضعیت عملیاتی بازگشته است.
در میان بانک‌های بزرگ، بانک ملی همچنان بیشترین حجم شکایت کاربران را به خود اختصاص داده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15788" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15787">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">روبیو: آمریکا خواهان توافق با ایران است، اما توافق به هر قیمتی را نمی‌پذیرد
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15787" target="_blank">📅 14:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15786">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فرمانده نیروی قدس خطاب به اسرائیل:
اگر امروز با اختیار خود عقب‌نشینی نکنید، فردا با خواری و شکست ناگزیر به فرار خواهید شد
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15786" target="_blank">📅 14:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15785">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=eh3Yq5A1vXY0aCwQKMKX3YF8oB81Ts6dgrJg0m5bK06nUFPosL-k8vvxuva_moj3hdqaG9qisTJLhDui-OOJbVbUe-Fh7SdgKfycjeILu7TUnFyDmOpkO4hwSOFcsjGfbhIdu0_2LrtDxD8N4gTjskpY0VI2c-V_4em2yRvTdjpYHYAq9UDrnDb202kWxe2lVjhZTHCU9zujudYbFGN1sBJaeAdhip3FcKxSh596xKdk6ezhAFDVUhlECQJ0ukYoRqVC7KmW3gqCUKz_R7lIdOYl1r_ryyMmFv8KU1U49uEaeYE8XzJXIwp8W0gC0MO3pCt3SUU1E_Lo4YPKJHm7xn1BLj44Gjd1hBBCT_yq_UMggrvWWKZKFIvRg40MxS7_1Piw5yPmn2BD96eA068Qpa826GiXNQ-wh-DX5d6IcsHnktCNCutEJIrFKl1IZtcfSe4rXczzyqeWWyPURCTP6iiBX1pcW_QsG1mnsaCTIksG7knWIa2q5lp0IzRM0xQ9pBl_n3_4kCQ4zXXy9U0KBabz--mDM0U9pYS3eAsj1ehBn9jB2f74CJgNkhkKB0zF8RaGHyEDHb-wEo5rE-OABzVX6iRESuckWngqweu8cTPrvqsvPzaxQnIfDM_XI3LkNlZzMHFJbJRCMjI4PlNbTCV1qj5FPO7qZDQtoPfoZg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=eh3Yq5A1vXY0aCwQKMKX3YF8oB81Ts6dgrJg0m5bK06nUFPosL-k8vvxuva_moj3hdqaG9qisTJLhDui-OOJbVbUe-Fh7SdgKfycjeILu7TUnFyDmOpkO4hwSOFcsjGfbhIdu0_2LrtDxD8N4gTjskpY0VI2c-V_4em2yRvTdjpYHYAq9UDrnDb202kWxe2lVjhZTHCU9zujudYbFGN1sBJaeAdhip3FcKxSh596xKdk6ezhAFDVUhlECQJ0ukYoRqVC7KmW3gqCUKz_R7lIdOYl1r_ryyMmFv8KU1U49uEaeYE8XzJXIwp8W0gC0MO3pCt3SUU1E_Lo4YPKJHm7xn1BLj44Gjd1hBBCT_yq_UMggrvWWKZKFIvRg40MxS7_1Piw5yPmn2BD96eA068Qpa826GiXNQ-wh-DX5d6IcsHnktCNCutEJIrFKl1IZtcfSe4rXczzyqeWWyPURCTP6iiBX1pcW_QsG1mnsaCTIksG7knWIa2q5lp0IzRM0xQ9pBl_n3_4kCQ4zXXy9U0KBabz--mDM0U9pYS3eAsj1ehBn9jB2f74CJgNkhkKB0zF8RaGHyEDHb-wEo5rE-OABzVX6iRESuckWngqweu8cTPrvqsvPzaxQnIfDM_XI3LkNlZzMHFJbJRCMjI4PlNbTCV1qj5FPO7qZDQtoPfoZg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/15785" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15784">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15784" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15783">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مخالفت شدید چین با اقدامات آمریکا علیه کوبا
وزارت خارجه چین بیان کرد: چین همواره با تحریم‌های یکجانبه غیرقانونی که هیچ پایه و اساسی در قوانین بین‌المللی ندارند، مخالفت کرده است.
پکن از واشنگتن می خواهد تا فوراً به تحریم کوبا و هر نوع اجبار یا فشار پایان دهد. ما حمایت بی‌دریغ خود را از کوبا در جستجوی مسیر توسعه سوسیالیستی متناسب با شرایط ملی آن مجدداً تأیید می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15783" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15782">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">moamelegari-trump(@withyashar).pdf</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15782" target="_blank">📅 13:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15781">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز
:
اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/15781" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15780">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15780" target="_blank">📅 12:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15779">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده…</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15779" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15778">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است. برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت. @withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/15778" target="_blank">📅 12:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15777">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=BVe5_4lT3-E75HRXtTL-vWggoDIjZQ5IlWJs_9OpbHHycwjWHE4h_8AkSWxWLjaa1ssXpXJnMJNV8Cwa7r4KYb0rSEDaVej9SrdzMfOfT23qiSNdfSf4T8M5qtMb-hEE4g9pafuGNzaGBPdnfTQIfn98MT2vVJnPSdprW3_vvsv_TxZhmKifCDzPHvJ96JZOzFFvDfJ96i-QxZfWSmglx4PllfXO-OQx4dJi461uQMSxoVvegPGBSPucZ_z6ANFt2q2_ghcEHg69T6VdXmYhtP1HWtuDufr0yLKq6jsIDTN1RUlLTH5bSil9txeAsfYhTNeQBH-d900Sv0UqUSmKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=BVe5_4lT3-E75HRXtTL-vWggoDIjZQ5IlWJs_9OpbHHycwjWHE4h_8AkSWxWLjaa1ssXpXJnMJNV8Cwa7r4KYb0rSEDaVej9SrdzMfOfT23qiSNdfSf4T8M5qtMb-hEE4g9pafuGNzaGBPdnfTQIfn98MT2vVJnPSdprW3_vvsv_TxZhmKifCDzPHvJ96JZOzFFvDfJ96i-QxZfWSmglx4PllfXO-OQx4dJi461uQMSxoVvegPGBSPucZ_z6ANFt2q2_ghcEHg69T6VdXmYhtP1HWtuDufr0yLKq6jsIDTN1RUlLTH5bSil9txeAsfYhTNeQBH-d900Sv0UqUSmKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است.
برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/15777" target="_blank">📅 12:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15776">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15776" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15775">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وال استریت ژورنال:
ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/15775" target="_blank">📅 11:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15774">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/15774" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15773">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avmnqIaBfE25rR7j5CUklK0eRBLRe6mPBgaNlfhAEjjVg1XBLvcmXoh-a9s9Pitzqbq3QdudvNsIYZsCS99oYvbFb4vyunFQV3nCT2ff3bJoBKL9worsmZzjibsh9wOQXA3Yd6ELiXwS7wGBAMNCNi46-sAT9p1dD7l6OIlpwtAEL1drrd3WGxbIHZMYc7pQPkbw_Tc-oBrDkOodUFexpzkHEFwR_1Cir-4hFm-Dizl2ydmwJ3Bj71R0tdkGEKbTR_2XZQZ7VzO3bijJ2ZRYBFCs2HzFVasQSlmlc-lO-BU4m8tzgw93m2e1L2EykKU1Ff71JRAv7zWUldmRiQ6KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/15773" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15772">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=fA8O7E-jqbkdJTzmeLWlSf3JPRHm8n46nikD2O5Lr6HT5Uirpw7eZuukjTNQwXcyS9LEpPYgbT_bI7RQZ_dg6nmMOewTVNyARBVJhrI8gP-qce3aAQ2H3OyUQF80DDb9l4twAwp_IFWHeJQ0eqE9ON_yThHiXx4TkeeGLL513_d4frXKxnJ4vMYc7aEU60hGKq-IHlqsuwsr_ZTBiyH8dcXJG7rrtpq0F9mHsz6KGhsBMnrNTl5Ogyd-w3B0cOB7HWUs_NFwpr0byzrgR-8-3P8xlRrQkkT6wa55OF15urFWW0IW9zgCtNhxWMf6CTmvC-gyIaQaH9gHWFQK0JNcHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=fA8O7E-jqbkdJTzmeLWlSf3JPRHm8n46nikD2O5Lr6HT5Uirpw7eZuukjTNQwXcyS9LEpPYgbT_bI7RQZ_dg6nmMOewTVNyARBVJhrI8gP-qce3aAQ2H3OyUQF80DDb9l4twAwp_IFWHeJQ0eqE9ON_yThHiXx4TkeeGLL513_d4frXKxnJ4vMYc7aEU60hGKq-IHlqsuwsr_ZTBiyH8dcXJG7rrtpq0F9mHsz6KGhsBMnrNTl5Ogyd-w3B0cOB7HWUs_NFwpr0byzrgR-8-3P8xlRrQkkT6wa55OF15urFWW0IW9zgCtNhxWMf6CTmvC-gyIaQaH9gHWFQK0JNcHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
ما باید دوباره این کار را انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15772" target="_blank">📅 11:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15771">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">«قطعنامه اختیارات جنگی ایران» متوقف شد
‏ سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
‏ جمهوری‌خواهان و ترامپ استدلال کرده بودند، تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
‎
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15771" target="_blank">📅 10:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15770">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درباره ایران: هفته گذشته، ما یک توافق تاریخی برای پایان دادن به درگیری با ایران امضا کردیم، تنگه هرمز را کاملاً باز کردیم و کاری را انجام دادیم که هیچ رئیس‌جمهوری قبلاً نتوانسته بود انجام دهد.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15770" target="_blank">📅 10:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15769">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amUdHMYe8sgOhia2HMiBR4_u_RCLUv4Up2M7pRc90OfFv5C5ncnae32B7d8o39ADSE3xRmeq4KK6nwfLxrJs6GhO7WzgGshM6C11lgqRcujg3N2Vd-NniDKprfX4yKLZsMn6pEoktQ64lK1xgDAL7kKs8JoXh3uTaAdCKWor5VK46v6eq52AjzTIcT7ubBZA5L-E79QbMm_4lDz9hS6pfj0FK9pNbvllxob2qt8pM2O4bBqLEmJUENltobRcc9wH94_-OXC_A-M4CGDvlxXofVuDolYizxZd1Jh4ipKR1Al1SOsZOzaYrfiZOF-Q0U8HhSkHFrs4VvD4tqfacAmg_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌ تروث : دو زلزله بزرگ که به تازگی مردم بزرگ ونزوئلا را لرزاندند، هر دو در مقیاس وسیع بوده و تعداد زیادی کشته به جا گذاشته‌اند. ایالات متحده آماده، مایل و قادر به کمک است! من به تمام نهادهای دولتی دستور داده‌ام که برای اقدام سریع آماده باشند. ما در کنار دوستان جدید و بزرگ خود خواهیم بود. گزارش‌های اولیه خوب نیستند.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15769" target="_blank">📅 09:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15768">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد. @withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15768" target="_blank">📅 02:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15767">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=B4o_m4EWWddcPoTeL06rbOaphZJr8Z4b7boG8f-WkxMyMY-glSB8Zreir2cAyPlmTPFJ2kZcqmmJgaocOwULc3j2oDchLv_HmWw6coojsmMugqja32H54ZkT-C_m_DyMtNi_0mOFtJnDRbtA2mu4qvdiRk3KrGTU1EkKXOEmdhXfPbOim5Jeq1-IARIZFVVI9cXMvuSX9PKt70oi-Y6WHKoDDw9LHAPtgIQ-MxERv59k7N9Lnsdz-5jHgNak_8VgDlnqJwfEcwXJtpJ9sd6pSgST7iK3fR6XrF47vLLXPIlE0DrNwxJz_GelePjRNKzS2uxqJwaYOkvd5CN4BcnHvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=B4o_m4EWWddcPoTeL06rbOaphZJr8Z4b7boG8f-WkxMyMY-glSB8Zreir2cAyPlmTPFJ2kZcqmmJgaocOwULc3j2oDchLv_HmWw6coojsmMugqja32H54ZkT-C_m_DyMtNi_0mOFtJnDRbtA2mu4qvdiRk3KrGTU1EkKXOEmdhXfPbOim5Jeq1-IARIZFVVI9cXMvuSX9PKt70oi-Y6WHKoDDw9LHAPtgIQ-MxERv59k7N9Lnsdz-5jHgNak_8VgDlnqJwfEcwXJtpJ9sd6pSgST7iK3fR6XrF47vLLXPIlE0DrNwxJz_GelePjRNKzS2uxqJwaYOkvd5CN4BcnHvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15767" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15766">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده شدن مردم منتشر کرده است.
‏گفته می‌شود بابا وانگا، پیشگوی مشهور بلغاری هم، وقوع یک تهاجم فضایی در جریان یک رویداد بزرگ ورزشی را پیش‌بینی کرده بود.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15766" target="_blank">📅 01:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15765">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طارمی و الهویی دوباره در مرز آمریکا «معطل شدند»
ایرنا از معطلی کاروان تیم ملی پس از ورود به خاک آمریکا از مرز مکزیک خبر داده و نوشته مانند دو سفر قبلی، روند عبور مهدی طارمی و سعید الهویی، توسط ماموران مرزبانی طول کشیده است.
دیدار با مصر در سیاتل (ایالت واشنگتن) که مرز شمال غربی آمریکا با کانادا است برگزار می‌شود.
تیم ملی برای صعود مستقیم به دور حذفی باید مصر را شکست دهد اما با تساوی مقابل این تیم هم می‌تواند به صعود به عنوان تیم دوم یا سوم باقی امیدوار بماند.
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15765" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15764">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKzHf4NA5pxh9rs0RV2AcU9H7dosMEuf3xaVNE3EwManpu28wFvjE0TKorQDJwis1pPZAh8YNitUO-RPoCbirk7flsUgM81GhAUufFJX_V6G5pvjf3EEwCiuj455yn6tX6aadsvwLF1EnF2HLnSCRMS4IAdPhzQql7vDcMUla7btgtIajGJvT_sLRbjQTyJ5jxmI_dfzEhlsQf1nNwy6_anfZO46Ycq7SzcTpg81MfvlQPMUGA5pMhV9kq8bH00Iw-fhkFCiTCFK5NcDplyrLLGFJdw4xwq0nf1ZrtpVD-waD1p1mJ_drYon9iKfUorIPFJXBhIawwAvnL1xQAERag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن (CVN-72)» نیروی دریایی آمریکا در تصاویر ماهواره‌ای در فاصله ۱۴۰+ کیلومتری بندر چابهار ایران مشاهده شد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15764" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15763">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فاکس‌نیوز : ترامپ به دنبال تأمین ۶۷۲ میلیون دلار برای حذف مواد هسته‌ای ایرانی است
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15763" target="_blank">📅 23:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15762">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزارت امور خارجه ایران: واشینگتن باید از تفسیرهای متناقض با مفاد یادداشت تفاهم بپرهیزد.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/15762" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15761">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارشهای زیاددددد از صدای انفجار دوباره  در بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15761" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15760">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15760" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15759">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.  گوئیدو کروستو گفت: تنها…</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15759" target="_blank">📅 22:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15758">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران
پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.
گوئیدو کروستو گفت: تنها پروازهای مطابق با معاهدات مجاز بوده‌اند؛ پیام روته کاملا اشتباه است.
احزاب مخالف در ایتالیا از این توضیحات قانع نشدند. آنجلو بونلی، نماینده سبزها گفت: ملونی به ایتالیایی‌ها و پارلمان دروغ گفت. ملونی باید فورا روشن کند چه اتفاقی افتاده و به پارلمان گزارش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15758" target="_blank">📅 22:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15757">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فردا فرمانده ستاد فرماندهی مرکزی ایالات متحده(سنتکام( به اسرائیل خواهد رسید
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15757" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15756">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نعیم قاسم ، رهبر حزب الله ، اعتراف کرد که یک گروهک تروریستی نمی تواند ارتش اسرائیل را در رویارویی مستقیم نظامی شکست دهد
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15756" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15755">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15755" target="_blank">📅 22:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15754">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتَهمتَن</strong></div>
<div class="tg-text">داش تو ویست گفتی بوست کنیم؟</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15754" target="_blank">📅 22:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15753">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15753" target="_blank">📅 22:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15752">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15752" target="_blank">📅 22:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdam Fazaei</strong></div>
<div class="tg-text">یاشار جان ایموجی فقط جاوید شاه دیگه نیست ؟</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15751" target="_blank">📅 22:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromf</strong></div>
<div class="tg-text">سلام
داداش
بجز اخبار یه چیزی هم خودت بگو
مرسی
دلتنگ صدات شدیم
😂</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15750" target="_blank">📅 22:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بندر عباس صدای ذرت مکزیکی‌ میاد
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15749" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15748">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وال‌استریت ژورنال؛ ترامپ اقدامات جسورانه علیه ایران انجام داد که هیچ رئیس‌جمهوری پیش از او جرأت انجامشان را نداشت، اما در نهایت به همان نقطه‌ای رسید که دیگران هم در آن قرار داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/15748" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15747">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانال 14 اسرائیل:اسرائیل در حال آماده‌سازی برای احتمال حمله دوباره به حوثی‌های یمن است
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15747" target="_blank">📅 22:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15746">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78282e8e68.mp4?token=lnevf41dqfiuG6bfdCaSutV4mA66dZPaT-WthTrcltmL2CfVKtWgeavTSojGaeSZlKh-LegaB-WWKWOPLUcGGgyldyYSE6XzqDUTTPIf2Ijsgp9CBRl32UYdcOebeerwMOa56dey1TmQnEA8VOe2mOV9r3I5mQJ6cu8sb1P-92ZYzfAGtKJ8djxd6-iUriaqQFkMd8N9jkN1kUfo_SN6It1nmyoeSA9LfhajMH7N81pxKsbEZh5ABDR1e_tk8X2mmmc9iPD7bc6hasaHIeZQdj79kdi5-cCG4MG65yWVH6QRPbD_uO9gMfEWa4mviFtJ8LIwI6Z5ZLZVbN7fv3AWEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78282e8e68.mp4?token=lnevf41dqfiuG6bfdCaSutV4mA66dZPaT-WthTrcltmL2CfVKtWgeavTSojGaeSZlKh-LegaB-WWKWOPLUcGGgyldyYSE6XzqDUTTPIf2Ijsgp9CBRl32UYdcOebeerwMOa56dey1TmQnEA8VOe2mOV9r3I5mQJ6cu8sb1P-92ZYzfAGtKJ8djxd6-iUriaqQFkMd8N9jkN1kUfo_SN6It1nmyoeSA9LfhajMH7N81pxKsbEZh5ABDR1e_tk8X2mmmc9iPD7bc6hasaHIeZQdj79kdi5-cCG4MG65yWVH6QRPbD_uO9gMfEWa4mviFtJ8LIwI6Z5ZLZVbN7fv3AWEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه کان اسرائیل : آمریکایی‌ها در حال ترک فرودگاه بن‌گوریون هستند
ایالات متحده ۲۸ فروند هواپیمای سوخت‌رسان را تخلیه کرده و اسرائیل نیز به‌دلیل نگرانی از اختلال در پروازهای غیرنظامی در طول تابستان، اسرائیل خواستار تخلیه حدود ۲۰ هواپیمای دیگر شده است.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/15746" target="_blank">📅 21:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15745">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام ندهید. در غیر این صورت مسئولیت با شماست و توسط حرص و طمع خود شما انجام گرفته. به این مسئله دقت کنید و
فقط از تحلیلها و مطالب آموزشی افراد استفاده کنید
. هیچ پکج یا هیچ پرداختی به هیچ بی ناموسی انجام ندهید.
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
از توجه شما به این مطلب سپاسگزارم، یاشار</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/withyashar/15745" target="_blank">📅 21:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15744">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">1$ / Tether = 167,000 Toman
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15744" target="_blank">📅 21:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15743">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر انرژی آمریکا مدعی شد: بازگشت جریان نفت به حالت عادی به دلیل مین‌های ایران به تأخیر افتاده است
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/15743" target="_blank">📅 21:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15742">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یدیعوت آحارونوت: فرمانده سنتکام به زودی وارد اسرائیل می‌شود و با وزیر جنگ و رئیس ستاد ارتش دیدار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/15742" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15741">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c79bdeee0.mp4?token=OAikw-YfGm4VJpwInG5w4fh4zeCB-L2E5KZaQx-9p9eSNnObOlTX7j-T0WIpuc6U2JpLgDXcL2R3GQtor3_M9avdEQJ0uXlQQlTbrikzLRBTXQJWn1MlYpEC-LOAnq_cRBTBLZ0WsDO-rJUvCoBQt8IRHPREStlwaJhTtPiiLSlujSdLN2cSFkni3jkLscxEhPyjF6jnUzMzLzGpt8NgZpG9xUYaXvluagBL6C2PjCTi1Dt2B5xRg6Gc9XoiH0vzRM_aCsMXsRbagZ336WI9hyJVTpefCd7Gfc_qCcEMV8TETLqZ1RQzD81cL9Eq7I6LLX_ula006did4sq8lZtdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c79bdeee0.mp4?token=OAikw-YfGm4VJpwInG5w4fh4zeCB-L2E5KZaQx-9p9eSNnObOlTX7j-T0WIpuc6U2JpLgDXcL2R3GQtor3_M9avdEQJ0uXlQQlTbrikzLRBTXQJWn1MlYpEC-LOAnq_cRBTBLZ0WsDO-rJUvCoBQt8IRHPREStlwaJhTtPiiLSlujSdLN2cSFkni3jkLscxEhPyjF6jnUzMzLzGpt8NgZpG9xUYaXvluagBL6C2PjCTi1Dt2B5xRg6Gc9XoiH0vzRM_aCsMXsRbagZ336WI9hyJVTpefCd7Gfc_qCcEMV8TETLqZ1RQzD81cL9Eq7I6LLX_ula006did4sq8lZtdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگ داره خیلی خوب پیش میره. همون‌طور که می‌دونید، ما داریم با اختلاف زیاد می‌بریم. ایرانم داره امتیازهای خیلی بزرگی میده. ببینیم آخرش چی میشه، ولی واقعاً اوضاع خیلی، خیلی، خیلی قدرتمند پیش رفته.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/15741" target="_blank">📅 21:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15740">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روزنامه تلگراف به‌نقل از منابع نزدیک به ترامپ مدعی شد که رئیس‌جمهور آمریکا احتمالاً
پس از انتخابات میان‌دوره‌ای کنگره، توافق فعلی با ایران را کنار می‌گذارد و به‌دنبال توافقی جدید خواهد رفت.
به‌گفته این منابع، ترامپ برای مهار فشارهای اقتصادی و حفظ موقعیت جمهوری‌خواهان در انتخابات، به توافق کنونی با ایران نیاز داشته است , بازگشایی تنگه هرمز و دستیابی به تفاهم با تهران، نگرانی بخشی از جمهوری‌خواهان را کاهش داده است.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/15740" target="_blank">📅 21:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15739">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آکسیوس: اولین دور مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه پایان یافت و گفت‌وگوها در فضایی به شدت پرتنش برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15739" target="_blank">📅 20:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15738">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ:ایران تاکنون 500 میلیون دلار مواد غذایی آمریکایی خریداری کرده است.   @withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15738" target="_blank">📅 20:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15737">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ:ایران تاکنون 500 میلیون دلار مواد غذایی آمریکایی خریداری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15737" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15736">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYrNNneCauEPMa9Y67qOwi9BTTfWmxWgGywOhS88briilVmhSsR9LSnEtqrHwu5SL6pqNPtdsxp_VhymUnYNo7pRx9k7k2NDieDfLdz7ug04OS6lLCsW8cQruyEzOju4t0AIURJfGhiDzxg-MkUV_Az04OslRTl2LkBvyhrDlawXZMBkQzPQJifVz9IkL-vkJNxCCX70M0Lpoy_rO5MhorB_4LpNcOC0zimaLCRCUN0Jb1z8GhFnqKtQlXex1z_JzrJD82xcGjg94m4Tew-fjqmDa9QQ_TevCfvq0O8YX0CRw3gTrlWUdeTyDgHl4FJG7jr68wPd5FvvRzxK4SfVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیت‌کوین به زیر ۶۰٬۰۰۰ دلار سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/15736" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15735">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مرحله دوم مذاکرات فنی ایران و آمریکا ۸ تیر برگزار می‌شود
وزیر خارجه آمریکا دقایقی پیش در اظهاراتی گفت که مذاکرات فنی ایران و آمریکا، روز ۲۹ ژوئن / ۸ تیر در سوئیس برگزار می‌شود. پیش از این نیز وزارت خارجه پاکستان اعلام کرد که مذاکرات ایران و آمریکا هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/15735" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15734">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=MU6qHXRpmqi_gD1xNiiPDI06-J2VYhhW8w1CNiG7ABe7jqpvGrliJ1eVJI1C-SODwHKUnKAeoIFLkqoZOGuxniC6Sf58kKhuJoBftyOlw0Q2FdK4QyrViV2PO0p_1v6ody_FhxQ7aqMn68u-iOCu-l90JjCqRYHJ8JVIjMArJzUoKBXYgAEIDU7_7Iu6GFdy7sRZQI5QofLDxmmglPoSOegN1WmxY1jcQ5CmDpiph5owYWc7Xn8gi1MI1piFSWEzfKpPQMcAvTNvoNEw7VEZJooRuJGqZtdJ498NQTN3hoASKwNTBnk7Ah_0rrU8Uou-CeWxYlIBGbmHHpEaAM_vnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=MU6qHXRpmqi_gD1xNiiPDI06-J2VYhhW8w1CNiG7ABe7jqpvGrliJ1eVJI1C-SODwHKUnKAeoIFLkqoZOGuxniC6Sf58kKhuJoBftyOlw0Q2FdK4QyrViV2PO0p_1v6ody_FhxQ7aqMn68u-iOCu-l90JjCqRYHJ8JVIjMArJzUoKBXYgAEIDU7_7Iu6GFdy7sRZQI5QofLDxmmglPoSOegN1WmxY1jcQ5CmDpiph5owYWc7Xn8gi1MI1piFSWEzfKpPQMcAvTNvoNEw7VEZJooRuJGqZtdJ498NQTN3hoASKwNTBnk7Ah_0rrU8Uou-CeWxYlIBGbmHHpEaAM_vnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : من بیشتر دوران بزرگسالی‌ام را به جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای اختصاص دادم.
آماده نبودم اجازه دهم زنجیره‌ای از هزاران سال تاریخ یهودی به خاطر دستیابی این آیات‌الله‌ها به سلاح‌های هسته‌ای شکسته شود.
به همین دلیل بیشتر دوران بزرگسالی‌ام را به این هدف اختصاص دادم همچنین به عنوان نخست‌وزیر
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15734" target="_blank">📅 19:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15733">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ارتش اسرائیل: یکی دیگر از تروریست‌های حماس که در قتل عام ۷ اکتبر به اسرائیل نفوذ کرده بود، از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/15733" target="_blank">📅 19:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال 13 اسرائیل:
نتانیاهو امشب یک جلسه امنیتی درباره لبنان و سوریه برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/15732" target="_blank">📅 19:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15731">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو: از ترامپ اجازه‌ای برای حمله به ایران درخواست نکرده‌ام بلکه تنها آن را به او ابلاغ کردم.
ماموریت ما در لبنان هنوز پایان نیافته است.
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15731" target="_blank">📅 18:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15730">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832f75f201.mp4?token=oQIJl6v-0H0F8NDd8AZQRETTWUg2FyCob-izd22kEs87JJAKZPwqFqdkKAk3q7nwuN5JhsnSxKY7h2go-Yss83V8dze9NA152OtknbBGHyG6uA7QHfBwVjeH2WXUszGn0Wn_LkvKal8nc8bOYA845qS6FpS2WhCE63fX1axRa5Jz_xPlrAJIw4tzRztGL5EPPOt3Jd8TFiXZE8fizykJgUty3ADpyRGQ4yEjSyTvpumq6d2HYylmJNvYO-Yei39Am7dPA8W2CeQvkWQutDduVZ6lD_DBEIX34aN4_IRU9_U4b-k8gKBZ2z11ECkcC3t-Xw-782zCzq9iZ3zm9Cx-6TQfSQuQtc6vQs1fRPVA_xuzO4XwyFUikAo8ig4JoNggYNT3KXGbYeP1Pk_fJD0aZres53KPDCiaDRgz_-FfKVH4dSO3bDUxv9cYJpVc3BHlkMtT_JUmNS9jb41hgSp0ymkwEXZp3sVi5f589okHL-qKni8hTmdfTdbKOngXfxDuL4bZ3_oUzFv5bXZlfnSkiEvaemjhN7wXdtYQjt8QKRJBjgjrTB5fjW1jLfqgf-A25lQP0q--9NIiwpiw2nX1WMmuyxzrGmufaGyOVcKAAyONR2pcTDk19B6YYUkR0mN5KbR9fgt8BjvpK7ZyqOhaQ7jDVN7PqPIHDFoYwKXao9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832f75f201.mp4?token=oQIJl6v-0H0F8NDd8AZQRETTWUg2FyCob-izd22kEs87JJAKZPwqFqdkKAk3q7nwuN5JhsnSxKY7h2go-Yss83V8dze9NA152OtknbBGHyG6uA7QHfBwVjeH2WXUszGn0Wn_LkvKal8nc8bOYA845qS6FpS2WhCE63fX1axRa5Jz_xPlrAJIw4tzRztGL5EPPOt3Jd8TFiXZE8fizykJgUty3ADpyRGQ4yEjSyTvpumq6d2HYylmJNvYO-Yei39Am7dPA8W2CeQvkWQutDduVZ6lD_DBEIX34aN4_IRU9_U4b-k8gKBZ2z11ECkcC3t-Xw-782zCzq9iZ3zm9Cx-6TQfSQuQtc6vQs1fRPVA_xuzO4XwyFUikAo8ig4JoNggYNT3KXGbYeP1Pk_fJD0aZres53KPDCiaDRgz_-FfKVH4dSO3bDUxv9cYJpVc3BHlkMtT_JUmNS9jb41hgSp0ymkwEXZp3sVi5f589okHL-qKni8hTmdfTdbKOngXfxDuL4bZ3_oUzFv5bXZlfnSkiEvaemjhN7wXdtYQjt8QKRJBjgjrTB5fjW1jLfqgf-A25lQP0q--9NIiwpiw2nX1WMmuyxzrGmufaGyOVcKAAyONR2pcTDk19B6YYUkR0mN5KbR9fgt8BjvpK7ZyqOhaQ7jDVN7PqPIHDFoYwKXao9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، بسنت : سلطه دلار خیلی مهمه
همه کارهایی که ترامپ داره انجام می‌ده، دلار رو دوباره محور تجارت جهانی می‌کنه
تو ونزوئلا و حتی مذاکرات با ایران هم می‌بینیم که معاملات قراره با دلار انجام بشه
درکل، همه این اقدامات جایگاه دلار رو دوباره تقویت می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15730" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15729">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ به فاکس‌نیوز اعلام کرد که قرار است به بازرسان اجازه داده شود تا مکان‌هایی که اورانیوم ایران در آنجا نگهداری می‌شود، بازدید کنند. از سوی دیگر، ایران قصد دارد در اولویت اول، کالاهای آمریکایی به ارزش حدود ۵۰۰ میلیون دلار خریداری نماید. هیچ عجله‌ای برای ورود بازرسان وجود ندارد و تیم آمریکایی قرار است همراه با بازرسان آژانس برای یافتن اورانیوم غنی‌شده اعزام شوند.
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/15729" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15728">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
ترامپ: هیچ عجله‌ای برای دسترسی به این مواد وجود ندارد، زیرا پس از عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/15728" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15727">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ در تروث : شهردار ممدانی با حمایت سه کمونیست تمام‌عیار به پیروزی رسید و رسانه‌های جعلی هم با سروصدای زیاد و به‌صورت یکپارچه برایش کف زدند. تبریک آقای شهردار!
من دیشب ۱۶ برد از ۱۶ داشتم و به انتخاب میهن‌پرستان فوق‌العاده آمریکایی کمک کردم، اما رسانه‌ها حتی یک کلمه هم درباره‌اش نمی‌گویند.
در دو سال گذشته، حمایت و تأیید من باعث ۲۵۹ پیروزی در انتخابات مقدماتی شده و تقریباً هیچ شکستی نداشته است، با این حال هیچ توجهی از سوی رسانه‌ها دریافت نکرده‌ام!
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15727" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15726">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=S98lbwgU7PouW9dEKA2NvtpMRIvYYJnQt9lhIcz6NiMy2NZBv2BqOZbT7esE0yVV2fQm5pJtrf9tMOcCOq4201Wzs3jA-G3i8D_AKxA88lDjjTTstXl-NmsqWBoTTTaW3iLb9IKkjaUCt3Om4599tXq4nPX_Q86HNsVtkQ2X03R6o4Y5l7XVsspJmzV2-CzrWkohQj3-BQ93JwkiTLAdIbvvBMjx9AS_ZdXcR2UcTrY27er__fUCABY5qrVkzlH5h5eYbNaRXgeH0iCGY_t-rOdUCzCTeHSfr0k7KaHWOQG4diW_ljZ6A-ZcMQHJkn10P9EWdyGPIVzLkUGkzw3PNoeye0U_XDK8uI4DZL3j5R2k3ttmt0cOEFvGwYImKviX--gtyFSSVT3T7pTXAoWlXSJ3pGexeSr9dGG0mtzYXaQXyFTuMG2CQWzMpow9kAe6AAlYKhiGQ1rMgxZdlkkjenWo_ZCAi0CfEkiAFw5cQeaViYUe7AXb8PZD0JOBwMiGj56F7Fjtlv3xnFKQp9v2_2E1N4oPKRSVB1vYiE40_Geprung1pWxCv-Vlq3rnoD4nlPcRltqwL1RqCBGEJnh0928YuE0xw7P8bvK-8hwMa_Nu9JYKSwJkv_oe-FYgwytZbkaJIPGV-t3bAoJ3ZKb3vFc6NfQda-TREgQ9GMOWk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=S98lbwgU7PouW9dEKA2NvtpMRIvYYJnQt9lhIcz6NiMy2NZBv2BqOZbT7esE0yVV2fQm5pJtrf9tMOcCOq4201Wzs3jA-G3i8D_AKxA88lDjjTTstXl-NmsqWBoTTTaW3iLb9IKkjaUCt3Om4599tXq4nPX_Q86HNsVtkQ2X03R6o4Y5l7XVsspJmzV2-CzrWkohQj3-BQ93JwkiTLAdIbvvBMjx9AS_ZdXcR2UcTrY27er__fUCABY5qrVkzlH5h5eYbNaRXgeH0iCGY_t-rOdUCzCTeHSfr0k7KaHWOQG4diW_ljZ6A-ZcMQHJkn10P9EWdyGPIVzLkUGkzw3PNoeye0U_XDK8uI4DZL3j5R2k3ttmt0cOEFvGwYImKviX--gtyFSSVT3T7pTXAoWlXSJ3pGexeSr9dGG0mtzYXaQXyFTuMG2CQWzMpow9kAe6AAlYKhiGQ1rMgxZdlkkjenWo_ZCAi0CfEkiAFw5cQeaViYUe7AXb8PZD0JOBwMiGj56F7Fjtlv3xnFKQp9v2_2E1N4oPKRSVB1vYiE40_Geprung1pWxCv-Vlq3rnoD4nlPcRltqwL1RqCBGEJnh0928YuE0xw7P8bvK-8hwMa_Nu9JYKSwJkv_oe-FYgwytZbkaJIPGV-t3bAoJ3ZKb3vFc6NfQda-TREgQ9GMOWk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشد دارایی ونس و هگس در طی سالها
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15726" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15725">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=N39njRCsLanUwo8ut8boVMJACAjUUSKoVHorDnOgccWhTtHv5yDHaHhpl3ngClD9GJUdstIXSURF4Iu4XeYarG68CRiM6zLw-XaBUCXcpK_phDigp3LaRHNt5C_fvxHkVd0S3i1YoBymmlfrzVptldyVIToRkb8qFrJVPTPCKX-C3sQEeXI3ya2x40lX8K5kz-OSXTxZL6xYMVOGqcRuMkzM7RW8mF6nciAG2OWs7aInsCOWs8xwBrAbNsNMAQNaYCFOQriDBNmZdwpqnfFJAHAefYRpBMcIgFCT0YrhR-aLG4cd4mt8sOzSSbNtVe9gQYzM11eBecpLaXTNNEk6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=N39njRCsLanUwo8ut8boVMJACAjUUSKoVHorDnOgccWhTtHv5yDHaHhpl3ngClD9GJUdstIXSURF4Iu4XeYarG68CRiM6zLw-XaBUCXcpK_phDigp3LaRHNt5C_fvxHkVd0S3i1YoBymmlfrzVptldyVIToRkb8qFrJVPTPCKX-C3sQEeXI3ya2x40lX8K5kz-OSXTxZL6xYMVOGqcRuMkzM7RW8mF6nciAG2OWs7aInsCOWs8xwBrAbNsNMAQNaYCFOQriDBNmZdwpqnfFJAHAefYRpBMcIgFCT0YrhR-aLG4cd4mt8sOzSSbNtVe9gQYzM11eBecpLaXTNNEk6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری دولتی لبنان گزارش داد:
یک پهپاد اسرائیلی خودرویی را در نزدیکی شهرک کفررمان در جنوب لبنان هدف قرار داد و دو نفر کشته شدند.
پیش‌تر نیز سخنگوی ارتش اسرائیل اعلام کرد نیروهای ارتش دو عضو مسلح حزب‌الله را که تهدیدی برای نیروهای اسرائیلی در منطقه علی‌الطاهر در جنوب لبنان بودند، هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/15725" target="_blank">📅 17:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15724">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قیمت اونس طلا به زیر ۴ هزار دلار رسید؛ آیا سقوط ۱۵۰۰ دلاری از اوج تاریخی ادامه خواهد داشت؟
قیمت نقدی طلا روز چهارشنبه ۲۴ ژوئن (سوم تیر ۱۴۰۵) تحت تاثیر رشد ارزش دلار آمریکا و افزایش انتظارات مبنی بر تداوم بالا ماندن نرخ‌های بهره در این کشور، برای نخستین بار از ماه نوامبر ۲۰۲۵ میلادی، از مرز روانی ۴ هزار دلار در هر اونس پایین‌تر آمد.
تقویت ارزش دلار آمریکا باعث شد تا خرید شمش طلا که بر مبنای دلار قیمت‌گذاری می‌شود، برای دارندگان سایر ارزها گران‌تر تمام شود.
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/15724" target="_blank">📅 17:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=I00M6vZ3bC6Zl3LSrH9SM7QM_5XOEH0pdH4kQz9JmPOmVawUCMkCLKekQczQKL2H5isAoxRgMzU-XC1GeoDHlDBDkqgiNFBngT5qqV1fAecH_6AUhJm1niQfvThXjXDunYZoxZ7Cy7CX12sYwMHtTqPRkWQea9I56Q1CgFgcZFHg-QnYUGTe3BmQG3yP2tpN5yil16FNi7G9isH_GPa46YEgfIIsCte_V6XHW1Aj9m6b_OoZGO-GilT5QxMtNl3hiUJc9rKUNjEUSntBUNVTPzbCiHvnAVUrwBMi9_DBEysOE5PZFCu-OSRH_msObYWR551JP_GGYIbWdBEMp-uAgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=I00M6vZ3bC6Zl3LSrH9SM7QM_5XOEH0pdH4kQz9JmPOmVawUCMkCLKekQczQKL2H5isAoxRgMzU-XC1GeoDHlDBDkqgiNFBngT5qqV1fAecH_6AUhJm1niQfvThXjXDunYZoxZ7Cy7CX12sYwMHtTqPRkWQea9I56Q1CgFgcZFHg-QnYUGTe3BmQG3yP2tpN5yil16FNi7G9isH_GPa46YEgfIIsCte_V6XHW1Aj9m6b_OoZGO-GilT5QxMtNl3hiUJc9rKUNjEUSntBUNVTPzbCiHvnAVUrwBMi9_DBEysOE5PZFCu-OSRH_msObYWR551JP_GGYIbWdBEMp-uAgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، برای دومین مرحله از تور خاورمیانه خود به کویت رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/15723" target="_blank">📅 17:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15722">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سنتکام: «نیروهای فرماندهی مرکزی ایالات متحده در تاریخ ۱۹ ژوئن یک حمله هوایی در شمال‌غرب سوریه انجام دادند که به کشته شدن یکی از رهبران ارشد داعش منجر شد.
در این حمله دقیق، علی حسین العلوی کشته شد. این عملیات بخشی از تلاش‌های مستمر آمریکا برای مختل کردن و از بین بردن عناصر تروریستی است که در پی حمله به شهروندان آمریکایی در خارج از کشور یا خاک ایالات متحده هستند.
نیروهای سنتکام همچنان در همکاری با شرکای منطقه‌ای به عملیات خود ادامه می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15722" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا به سی‌ان‌بی‌سی:
هر پولی که رژیم تهران دریافت کند، متعلق به ایرانی‌هاست.
نسبت بسیار زیادی از پول برای خرید غذا و داروی آمریکایی استفاده خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15721" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فاکس‌نیوز گزارش میدهد : پرزیدنت ترامپ روز شلوغی را در واشنگتن دی سی آغاز می‌کند و آماده می‌شود تا به کنگره برود، جایی که طبق گزارش‌ها قرار است با جمهوری‌خواهان سنا در مورد قانون متوقف شده «نجات آمریکا» ملاقات کند.
در طول اقامتش در کنگره، قرار است قانون «جاده قرن بیست و یکم به سوی مسکن» را نیز امضا کند.
همه این اتفاقات پیش از جلسه کاخ سفید بین ترامپ و مارک روته، دبیرکل ناتو، در اواخر امروز رخ می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/15720" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl1OO0C-Ze3dERjISr4dZGOr33icjtY-p7pRedASHx4b0n05GYFTzdN1eGhshIFDXe6RnxXEiW0Sygnex2KpHMNY3Sn2deoKTANBHYpNcRJ7jzo7rXjOxIidsXQyANCQM-zRV6OIeZuXMFICjTxbdh2s-TW88egax-nTUPo32pkas8OUnKm6MTiVoE6nfom_SLpEpNOjslw9bhsC9biV07pH2IbUiT5C18cNDRe_On-xK9AzJL0Xl8oxSqIoBitBn_uoXAFf96MMcqucUJz25NwG3o4mfC5uEx0eGB12dUmGyTWUzT-e9nmWN89AbrEgaoNXU__Fgc3Ju5WxsckLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث : «ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دردسرساز رسانه‌های جعلی، هیچ‌گونه عوارض، هزینه بیمه یا هیچ نوع هزینه دیگری از کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌کند. اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت.
همچنین، هیچ پولی از سوی آمریکا به ایران پرداخت نشده و هیچ بخشی از دارایی‌های ایران نیز مستقیماً در اختیار این کشور قرار نگرفته است. ما بخشی از دارایی‌های ایران را که همچنان کاملاً تحت کنترل ماست، برای پرداخت به کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا از آن برای خرید ذرت، گندم، سویا و سایر محصولات استفاده شود.
ایران به‌شدت به مواد غذایی نیاز دارد و ما این اقلام را منحصراً از ایالات متحده برای آن‌ها تأمین خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم.»
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15719" target="_blank">📅 15:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15718">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGH0Ome0PuUDO4o6C-0ALLLLMGWrdVhbBGRZ2JUmUZGxD6j_4YT4Au3k5WymsYfrbPUrdOhkqowVMbhduW5gT6XRMdZzf53t912YcxffPd2FgEaurOlIUMVVygCZ_DMciLPLWzIYyf2gC1yrZHxNsv9KEI7U_Z140FNwLteuDa6AZLtPylRo9UX1jFXJUJ8SwW6N353ZIdLqcQwkDzbXoxxn1460fq2ZAuFTV7WyQ7ualhGGIP2otJcvdov40fBRolEEEf5Z1YhA4qrIYZuR0ZsW8jkZhvsDJGsVernJG688rjWrrMRKL_P1XhmgIqRGhLgIF5tXXvORZt13HDeOgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن پالیسی:
توافق ایران زمینه درگیری‌های بیشتری را فراهم می‌کند
!
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15718" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15717">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با اعلام راکستار،قیمت بازی GTA6 مشخص شد.
نسخه Standard:
80 دلار، معادل 12 میلیون تومن.
نسخه Ultimate Edition:
100 دلار، معادل 16 میلیون تومن.
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15717" target="_blank">📅 14:18 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
