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
<img src="https://cdn4.telesco.pe/file/BLNcqQmCNugwWGuhz8fm6pYR0TGtIy63oKNzmI9-CKvyKBCaxHeNZQqxzMczLXRFTO2tTz4PbtSi9fAFql4bseQG5v-I1uEn6nzL_Rc42rGlGYbLozTWhUnSUDVMyzRAryZWWEDe1Ewr_CIoJ6n3sh5S3tFbLgnwwsLOFDfSZtUxk7Xw64-OMr1I8w8FIncv0eWDs6qboVEMFFSUl_MD1sZmA1bTGA70l95uIJcMowtjFyno5xm3AQLo2oMd6EoYZ2K9ITVwXWUeq69z02nFs7Va8H9bINfpcJBtuosxoytxMPCLDO-zNVA-4wEDwsiUz8KWbFXYoE-Hxy3feg-Efg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/23029" target="_blank">📅 20:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMalekshahirad</strong></div>
<div class="tg-text">رویا چرا الکی می‌فروشی ب مردم مرد نامومن</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/withyashar/23027" target="_blank">📅 19:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فایننشال‌تایمز :
حمله پهپادی روسیه به قطار نزدیک مرز لهستان:
یک پهپاد روسی امروز به
قطار تخلیه‌شده کی‌یف–ورشو
در نزدیکی مرز لهستان اصابت کرد؛ این قطار تنها حدود یک ساعت پس از قطاری حرکت می‌کرد که
بوریس جانسون، نخست‌وزیر پیشین بریتانیا، کارل بیلت، نخست‌وزیر پیشین سوئد و شماری از دیپلمات‌ها و مقام‌های اروپایی
در آن حضور داشتند. قطار حامل مقام‌ها لحظاتی پیش‌تر از منطقه عبور کرده و وارد خاک لهستان شده بود. قطار هدف‌قرارگرفته ۲۰۶ مسافر داشت و پیش از حمله به دلیل هشدار پهپادی تخلیه شده بود؛
در این حمله کسی زخمی نشد
@WarRoom</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/23026" target="_blank">📅 19:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba17bf936a.mp4?token=XLz18P7oRmRCOlcdolhwK2gweRZgB70yQfnlSSGjSmy03JjsjzDNtezfNE4xICa7-WQz1uTZBHxihZ_x_YTpY66MeTj_O5DBvUmd1oLlUPW-23zlku-S7T7eyPdd0RTly4_YuA7Wo6GWSZNbIPEfhylDXXPn_lAEgCw6FUkzl1TV7XbUp_mMDRm6gSyVnrOpF6CZPkyVJTHp7XSfA8WlzQLl7--5ilawnAXctxiuIzYeOWwcJF1YePsQxDHSepEK4giaAqI0n8bIjJ-HzExUFSEMPulcF_7XsBIroKNoOzbpIICuAmKMz44dn_CA-ChGzvz99_yBAp6oVOP1ukMYWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba17bf936a.mp4?token=XLz18P7oRmRCOlcdolhwK2gweRZgB70yQfnlSSGjSmy03JjsjzDNtezfNE4xICa7-WQz1uTZBHxihZ_x_YTpY66MeTj_O5DBvUmd1oLlUPW-23zlku-S7T7eyPdd0RTly4_YuA7Wo6GWSZNbIPEfhylDXXPn_lAEgCw6FUkzl1TV7XbUp_mMDRm6gSyVnrOpF6CZPkyVJTHp7XSfA8WlzQLl7--5ilawnAXctxiuIzYeOWwcJF1YePsQxDHSepEK4giaAqI0n8bIjJ-HzExUFSEMPulcF_7XsBIroKNoOzbpIICuAmKMz44dn_CA-ChGzvz99_yBAp6oVOP1ukMYWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/23025" target="_blank">📅 19:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درصد ٪
@WarRoom</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/23024" target="_blank">📅 19:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=eAUPwn8Vzc2reETbixUBIGQUKNxQ43dxIsvEcogoEjvuVDgKcvX4eJBzT0NTuH7e0R2AHIfaV7Zp-l-wnawXYP4h6kmnpRtuhcNQWp5eHOr1TYaMgIxqCGzr86dakpfLtuOd25WCIuistgPB9FY56zAHn3S_OLXJJcYoa-sgc2VMsbmNb_AbFQbocloiCGIUGIXo4iRuWwRweVs6_bB8bl2D1hGI3Cfzl1Jq7Tkdvd1BrGf0tBew0xUWY7Szl-YoOYgfHkipCfyH8VnD5cyIPZpVDhotvjx5Mb76dMjq1LcdeSKZgcP0NRGylQaR-VN1lNV5E2oUIGASplnbBpLjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=eAUPwn8Vzc2reETbixUBIGQUKNxQ43dxIsvEcogoEjvuVDgKcvX4eJBzT0NTuH7e0R2AHIfaV7Zp-l-wnawXYP4h6kmnpRtuhcNQWp5eHOr1TYaMgIxqCGzr86dakpfLtuOd25WCIuistgPB9FY56zAHn3S_OLXJJcYoa-sgc2VMsbmNb_AbFQbocloiCGIUGIXo4iRuWwRweVs6_bB8bl2D1hGI3Cfzl1Jq7Tkdvd1BrGf0tBew0xUWY7Szl-YoOYgfHkipCfyH8VnD5cyIPZpVDhotvjx5Mb76dMjq1LcdeSKZgcP0NRGylQaR-VN1lNV5E2oUIGASplnbBpLjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/23023" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPo</strong></div>
<div class="tg-text">ما نخواهیم پول نفت مون نره لبنان و فلسطین و نفت مون رو آمریکا بر نداره چیکار کنیم ؟</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/23022" target="_blank">📅 18:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نیویورک‌تایمز: تندروهای جمهوری اسلامی در اوایل ژوئیه مخفیانه توافق با آمریکا را با دستور حمله به سه کشتی تجاری در تنگه هرمز در ۷ ژوئیه به شکست کشاندند:
مقام‌های ایرانی به نیویورک‌تایمز گفته‌اند
مسعود پزشکیان، احمد وحیدی و بخش بزرگی از رهبری ایران از این عملیات بی‌اطلاع بودند.
تحقیقات، تصمیم حمله را به جناح تندروی مرتبط با
حسین طائب، روحانی بانفوذ و رئیس سابق اطلاعات سپاه
نسبت داده است؛ این جناح از ابتدا مخالف توافق بود و به فرماندهان میدانی اختیار داده بود بدون تأیید مرکز به کشتی‌هایی که ناقض کنترل ایران بر تنگه می‌دانستند حمله کنند. پس از حملات، پزشکیان با وحیدی تماس گرفت و با لحنی تند خواستار توضیح شد. این اقدام مذاکرات را از مسیر خارج کرد و
حملات مجدد آمریکا در روز بعد
را به دنبال داشت و در ایران نیز کشمکش قدرت، اتهام خیانت و تهدید به استعفای برخی فرماندهان ارشد را رقم زد.
عباس عراقچی
برای کاهش تنش به عمان اعزام شد، اما موفق نشد. هم‌زمان،
نبود
مجتبی خامنه‌ای
بر بحران افزود و مقام‌هایی گفتند حتی پزشکیان درباره اصالت برخی دستورها و پیام‌های منتسب به او تردید کرده است.
طبق گزارش، هم اکنون
جناح تندرو دست بالا را پیدا کرده و به‌جای بازگشت به مذاکرات، خواهان تشدید حملات علیه نیروهای آمریکایی، شناورها و زیرساخت‌های انرژی منطقه شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/23021" target="_blank">📅 18:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/23020" target="_blank">📅 18:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ: با ایران به توافق رسیدیم، توافق خیلی خوبی بود، دیگه هیچ سلاح هسته‌ای در کار نخواهد بود. تقریباً همه‌چیز نهایی شده و ما به هر چیزی که می‌خواستیم رسیدیم. مهم‌ترین بخش ماجرا اینه که ایران هیچ سلاح هسته‌ای نه خودش می‌سازه و نه از جایی می‌خره.  ما امروز…</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/23019" target="_blank">📅 17:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/23018" target="_blank">📅 17:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
instagram.com/YasharMotors
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/23017" target="_blank">📅 17:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFatemeh</strong></div>
<div class="tg-text">ی تحلیل کن اقا یاشار</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/23016" target="_blank">📅 17:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMَ reza</strong></div>
<div class="tg-text">چرا موج مکزیکی تموم نمیشه</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/23015" target="_blank">📅 17:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976afe9552.mp4?token=PJWBVsnWwbbAmdcXcS2S8Hpb_3tpOPoyREYdkDK309TjVNudu6CesmDRMjaRoSHY2GSkwRqKnVY0j9seNS40ZJrQjS6Nf1Ie6MPLxD95PckbVls2cxnznvgYo_Pj-AIS6iapY0u4h3AD6w8WWcNzxethRtroElUmYNR8XYlW4AK9InNlYYjqmJGU8XN9F0YH27sEqwaCTGYms5YXEDwXOwUCe2gaJnm0qdVMGTrSWx6qhbYuyodC8LmAIwjCpQouN5iVWLexU-pzxt-kXzN9GCJ4nmd2gfjHTEZMJsze5HpAQkUvT1PdfbjGoqNkPYTAQ4pxB2hLqQZXTOv-GGCLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976afe9552.mp4?token=PJWBVsnWwbbAmdcXcS2S8Hpb_3tpOPoyREYdkDK309TjVNudu6CesmDRMjaRoSHY2GSkwRqKnVY0j9seNS40ZJrQjS6Nf1Ie6MPLxD95PckbVls2cxnznvgYo_Pj-AIS6iapY0u4h3AD6w8WWcNzxethRtroElUmYNR8XYlW4AK9InNlYYjqmJGU8XN9F0YH27sEqwaCTGYms5YXEDwXOwUCe2gaJnm0qdVMGTrSWx6qhbYuyodC8LmAIwjCpQouN5iVWLexU-pzxt-kXzN9GCJ4nmd2gfjHTEZMJsze5HpAQkUvT1PdfbjGoqNkPYTAQ4pxB2hLqQZXTOv-GGCLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ماجرای ایران درست پس از انتخابات میان‌دوره‌ای و شاید حتی پیش از آن به پایان خواهد رسید.
قیمت بنزین به‌شدت سقوط خواهد کرد. من می‌دانستم چه کار می‌کنم؛ چاره‌ای جز انجام آن نداشتم. ایران نباید سلاح هسته‌ای داشته باشد و هرگز هم به آن دست نخواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/23013" target="_blank">📅 17:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5a025761.mp4?token=QX2VJHfDuLXSgHkdvq3PCYdEiRi3Vgzs4kLlOZAck0Vs7JiTWLqFFMrKSNqW61KYkBGwLsVDfnWjRYw_VC-yMiRywAbx9Ghthd4sCD5IaMJp4ylHsaVNtoPzDEZpq3a2xKJhaDq12PG2wydxrof3Exh9r5FXbb7xY85x34xOvSGIBF6qRyDW2ylBUEjfDMBmL6DD8ZXjxn63jXvxybXh-7PRbXz9uW5x1UQ9QvkNCKYFPzY4yGk58u-ch1-lYisKP466W3A9jugbmAhFLEMqkx4ZWGhMwdFuJRqDXWKkJpc_ZE-wKuJdxtopfpzP9tGlvwH8D9CXC2RXR623auFR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5a025761.mp4?token=QX2VJHfDuLXSgHkdvq3PCYdEiRi3Vgzs4kLlOZAck0Vs7JiTWLqFFMrKSNqW61KYkBGwLsVDfnWjRYw_VC-yMiRywAbx9Ghthd4sCD5IaMJp4ylHsaVNtoPzDEZpq3a2xKJhaDq12PG2wydxrof3Exh9r5FXbb7xY85x34xOvSGIBF6qRyDW2ylBUEjfDMBmL6DD8ZXjxn63jXvxybXh-7PRbXz9uW5x1UQ9QvkNCKYFPzY4yGk58u-ch1-lYisKP466W3A9jugbmAhFLEMqkx4ZWGhMwdFuJRqDXWKkJpc_ZE-wKuJdxtopfpzP9tGlvwH8D9CXC2RXR623auFR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران به‌شدت خواهان دستیابی به توافق است. آن‌ها مدام تماس می‌گیرند.
ما باید توافق درستی انجام دهیم. من تن به توافقی که خوب نباشد، نخواهم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/23012" target="_blank">📅 17:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2125e8e92b.mp4?token=YWZjmGx8P1FmXxql6qVz1gdokxWIfbzL_k-eMJ844NFFIj6T-giGSaFXMqOBdY6gU5fHv1z1bqmyi47KoYQ1mDm84mRp98lTHx8d8FdNTgOmL187MEzi9-sQ9sEo3XWM66IZY4mCkeJ4i311rS7uqf5ZIS4zuEIogtj8vI2savKPvmX0Kndb2hfBVoW6x0p3gVhns__HJsw-LwUqKqTMk7YZdcuHhOaWBZK7U0tKfvHD_bopaQ5SOd1wKGg82ae9WnlwYa989YKiwQ3PDZ0ouBJtr-_fVzFnQBLnp6pBYXjzUFrWVG2sDx5-aAjotAAB7rQE9RsZSwAuRk9G6FtzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2125e8e92b.mp4?token=YWZjmGx8P1FmXxql6qVz1gdokxWIfbzL_k-eMJ844NFFIj6T-giGSaFXMqOBdY6gU5fHv1z1bqmyi47KoYQ1mDm84mRp98lTHx8d8FdNTgOmL187MEzi9-sQ9sEo3XWM66IZY4mCkeJ4i311rS7uqf5ZIS4zuEIogtj8vI2savKPvmX0Kndb2hfBVoW6x0p3gVhns__HJsw-LwUqKqTMk7YZdcuHhOaWBZK7U0tKfvHD_bopaQ5SOd1wKGg82ae9WnlwYa989YKiwQ3PDZ0ouBJtr-_fVzFnQBLnp6pBYXjzUFrWVG2sDx5-aAjotAAB7rQE9RsZSwAuRk9G6FtzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ترامپ به نشست دوشنبه ایران و کشورهای خلیج فارس: برایم اهمیتی ندارد
خبرنگار: نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
ترامپ: برایم اهمیتی ندارد. این به خودشان مربوط است. ما در نهایت از آنجا خارج خواهیم شد. مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/23011" target="_blank">📅 17:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab990d240.mp4?token=Qxi-Nj1s66enZELoj05xpvpxmeuhfs3zqcQH6mxoEsezlDityQEXn-U0Tw4oU4C-eJn0sSYjo7KoU0eHlJQAOSw7PtT5CE4e9eiGGtIZE41sYu3JGlIuSlZVBN7GQ_xwv1MGp6hLazHzBNxiZqOM4x_JJUlpWhYVgv2isXIFjwp4GeiawpzbZGYG1zWBxIVJq-5FtgakfVWrVqxqCUdBPT_q0jCai9-EOZKRCAQEDv-Qi4_KfSpoQ2958OYa2l1awz97jOF0bOBwNuzV8J6ku3dlDfQuWNUZEs8ry1rkmbAYMTYDlT0y3ntnKWVBFVkVYFXYlBckGE6TjfT7lqr0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab990d240.mp4?token=Qxi-Nj1s66enZELoj05xpvpxmeuhfs3zqcQH6mxoEsezlDityQEXn-U0Tw4oU4C-eJn0sSYjo7KoU0eHlJQAOSw7PtT5CE4e9eiGGtIZE41sYu3JGlIuSlZVBN7GQ_xwv1MGp6hLazHzBNxiZqOM4x_JJUlpWhYVgv2isXIFjwp4GeiawpzbZGYG1zWBxIVJq-5FtgakfVWrVqxqCUdBPT_q0jCai9-EOZKRCAQEDv-Qi4_KfSpoQ2958OYa2l1awz97jOF0bOBwNuzV8J6ku3dlDfQuWNUZEs8ry1rkmbAYMTYDlT0y3ntnKWVBFVkVYFXYlBckGE6TjfT7lqr0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات رئیس‌جمهور ترامپ درباره ایران:
ما در نهایت خارج خواهیم شد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/23010" target="_blank">📅 17:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش ۲ انفجار مهیب از تنگه هرمز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/23009" target="_blank">📅 17:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: جنگ با ايران قبل از انتخابات میان‌دوره‌ای یا بلافاصله بعد از آن به پایان خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/23008" target="_blank">📅 16:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23007">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: ایران می‌خواهد به هر قیمتی توافق کند، اما من توافقی را که بی‌نقص نباشد امضا نمی‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/23007" target="_blank">📅 16:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf4511f99.mp4?token=CgSGOfBw3sbvkap17PW_u4BL9dHQCgk333IJW2jgtGcwpiXUJOBlAzi0-BhV0oL25DdgmBBAzNvkxm4vIGQU9wa4VEFycVxONjN96vLxBvqDe1BCbggAJhmEEKyplriEStiZdRLWuIVeKU-0k2cZp8QeWzShn-xYLEU6pC8H1GERanTL-4A3IIzlK2a88jki1N6oXso1DLOHRDlkJOjmgS6X1bLngN0WqYE_QobVpE4m6etE70gkNqlN9b4LSoX9r8MBPIFRchRr7g0xv0UVGRfwoyDU0tnCvINDqzmK72FArc4Y_Wu2lVWwppJwehIS380CdgEKZOdSUpy7uR8RCjS6MWxK-bstOllkmtWinWwFqVfuTSnjfSaNNw-pEPTVVyNOD6zJEpwXqC7oBytA9SveZrmSOCT7OVsiG-XoxNMjajwpzPDgMNymTc7Fmc9xoHQT-V7obQeZuvNMmlr1ZCy8ndSEeTyFMZyzu2CP48v9RvK5dGHAYv1oLjHfCFba58XSCSLDh9CuKlzeFsT9pET8m1sK0HQ6FTnM6OZ0uvo6qidrcn7lBwJekkOXil8MvAaYhFCXBHPGGVCX7rdIil1Yt_kJmYePdWoaUdLqK-2ThLBXfn_l3I4fTEBhd_i3wJLE-6lboTTGSvMk22Uk0GN7FFj_vsuax88_4czXyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf4511f99.mp4?token=CgSGOfBw3sbvkap17PW_u4BL9dHQCgk333IJW2jgtGcwpiXUJOBlAzi0-BhV0oL25DdgmBBAzNvkxm4vIGQU9wa4VEFycVxONjN96vLxBvqDe1BCbggAJhmEEKyplriEStiZdRLWuIVeKU-0k2cZp8QeWzShn-xYLEU6pC8H1GERanTL-4A3IIzlK2a88jki1N6oXso1DLOHRDlkJOjmgS6X1bLngN0WqYE_QobVpE4m6etE70gkNqlN9b4LSoX9r8MBPIFRchRr7g0xv0UVGRfwoyDU0tnCvINDqzmK72FArc4Y_Wu2lVWwppJwehIS380CdgEKZOdSUpy7uR8RCjS6MWxK-bstOllkmtWinWwFqVfuTSnjfSaNNw-pEPTVVyNOD6zJEpwXqC7oBytA9SveZrmSOCT7OVsiG-XoxNMjajwpzPDgMNymTc7Fmc9xoHQT-V7obQeZuvNMmlr1ZCy8ndSEeTyFMZyzu2CP48v9RvK5dGHAYv1oLjHfCFba58XSCSLDh9CuKlzeFsT9pET8m1sK0HQ6FTnM6OZ0uvo6qidrcn7lBwJekkOXil8MvAaYhFCXBHPGGVCX7rdIil1Yt_kJmYePdWoaUdLqK-2ThLBXfn_l3I4fTEBhd_i3wJLE-6lboTTGSvMk22Uk0GN7FFj_vsuax88_4czXyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از کشتی کانتینربر ایرانی که امروز در نزدیکی جزیرۀ هنگام قشم مورد حمله قرار گرفت با یک کشته و ۳ زخمی
@WarRoom</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/23006" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز: احتمالاً عبدالرضا شهلایی، فرمانده ارشد نیروی قدس سپاه، عملیات حوثی‌ها برای تصرف شهر مخا در ساحل غربی یمن را هدایت کرده است:
منابع نظامی یمنی به رویترز گفته‌اند که بر اساس
شنود ارتباطات و اظهارات نیروهای حوثی اسیرشده
، شهلایی در هدایت عملیات تصرف مخا نقش داشته است. منابع دیپلماتیک نیز به رویترز گفته‌اند که
فرماندهان ارشد سپاه برای هدایت حملات حوثی‌ها علیه عربستان به یمن رفته‌اند
. عبدالرضا شهلایی از فرماندهان ارشد نیروی قدس است که سال‌ها در یمن فعالیت داشته و دولت آمریکا برای اطلاعات منجر به شناسایی شبکه و فعالیت‌های او
تا ۱۵ میلیون دلار جایزه
تعیین کرده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/23005" target="_blank">📅 15:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ازسالی : سلام یاشار جان من همسرم راننده ست الان سمت مرز ریمدان (مرز ایران و پاکستان)رفته.میگه اعلام کردن مرز بسته ست. اسمم  نباشه
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/23004" target="_blank">📅 14:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فایننشال‌تایمز: ایران از روسیه پهپادهای پیشرفته و گران‌قیمت درخواست کرده است:
به گزارش فایننشال‌تایمز، تهران امسال از مسکو خواسته است
پهپادهای پیشرفته روسی را برای استفاده در جنگ با اسرائیل و آمریکا
در اختیار ایران قرار دهد. به نقل از
مقام‌های امنیتی غربی و یک فرد نزدیک به کرملین
منتشر شده است. درخواست ایران در حالی مطرح شده که همکاری پهپادی دو کشور سال‌هاست در جریان است؛
ایران پس از آغاز جنگ اوکراین، پهپادهای شاهد از جمله شاهد-۱۳۶ را در اختیار روسیه قرار داد
و مسکو بعدها با استفاده از فناوری ایرانی، تولید این پهپادها را در داخل روسیه توسعه داد. حالا با ادامه جنگ، تهران به دنبال دریافت نسل‌های پیشرفته‌تر پهپادهای روسی است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23003" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e14331e2.mp4?token=na-gmsU3d1SO1C_oTfdzLw7vmTBIxG37sZmyRbL4Ktua5ZNU4PTlxxOhMmOwazFDbqlbaBlLSBzq03iJ-QDPIrnHVrndnLTbFRufDrOn-Gy-32Z44XrCN5xwGLE25tIO2u3WeBA691EhPgbIh9BkchccYwN3XiuTCLf4z4CIjUXEewXO3qky1BraE1jdl1906MQXi0QCErmirnvpIEf32n9sKK8TCCkeU3FbUX08dZFZSgJqbOSVaCbIFhi2nbJhJ0XXFZ9tVVXjv1xL1aCzCAg3GDPW4Qx91Ym_PLN-p3G1bJaBQnTFu-z1t3kUoIua5GTym3pTRLe1YIoTiZZs8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e14331e2.mp4?token=na-gmsU3d1SO1C_oTfdzLw7vmTBIxG37sZmyRbL4Ktua5ZNU4PTlxxOhMmOwazFDbqlbaBlLSBzq03iJ-QDPIrnHVrndnLTbFRufDrOn-Gy-32Z44XrCN5xwGLE25tIO2u3WeBA691EhPgbIh9BkchccYwN3XiuTCLf4z4CIjUXEewXO3qky1BraE1jdl1906MQXi0QCErmirnvpIEf32n9sKK8TCCkeU3FbUX08dZFZSgJqbOSVaCbIFhi2nbJhJ0XXFZ9tVVXjv1xL1aCzCAg3GDPW4Qx91Ym_PLN-p3G1bJaBQnTFu-z1t3kUoIua5GTym3pTRLe1YIoTiZZs8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام یاشار جون. ممنون از تمام تلاشی که برای آگاهیه ما می کنی. من همیشه آهنگ پرنده که تو کانال گذاشتی رو برای پسرم پلی می کنم. اونم که خیلی تو موسیقی استعداد داره، یاد گرفته و اجراش می کنه. پسرم ۳/۵ سالشه. این فیلم رو مربیه مهد کودکش ازش گرفته
😂
😂
😂
گفتم برات بفرستم که بدونی از کوچک و بزرگ، همگی دوست داریم
❤️
❤️
❤️
اگر تو کانال گذاشتی، صورتشو محو کن لطفا
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23002" target="_blank">📅 13:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جرد کوشنر، فرستاده ویژه آمریکا: اگر اوکراین تا خط موردنظر پوتین عقب‌نشینی کند، توافق صلح می‌تواند نهایی شود:
کوشنر گفت
موضوع سرزمینی همچنان سخت‌ترین مسئله مذاکرات صلح روسیه و اوکراین است
و ولادیمیر پوتین خطی را که می‌خواهد به آن برسد مشخص کرده است؛ اگر اوکراین با عقب‌نشینی تا آن خط موافقت کند، بخش عمده توافق از قبل آماده خواهد بود، اما
کی‌یف در حال حاضر حاضر به پذیرش این شرط نیست.
کوشنر افزود وضعیت میدانی نیز در تعیین سرنوشت مناطق مورد مناقشه نقش دارد و وظیفه میانجی‌ها یافتن راه‌حلی است که ضمن حفظ اهداف اوکراین، امکان پایان دادن به جنگ را فراهم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23001" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کمی پیش گزارش زنده فاکس نیوز از روی ناو جرج واشنگتن و پرواز جنگندهی F-15 و F-35 با دریافت کردن سیگنال تهدید از سوی ایران(پرتاب. موشک/پهپاد) به کشتیهای عبوری. همچنین در ویدیو میبینید که تماما پشت سر مجری موشکها و بمبها قرار دارد و این ناو بیش از اندازه تا دندان…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23000" target="_blank">📅 12:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxEVBLplBuc2umFY2JbbKkd-B7zyAt7Hjlzo_kpsHwFnJFYjPhn4gc1GVvnVDac3n3BYuct0fSATpwghfIKySn3Dfsr7UrLP2W9EmK-qhnnGdfgn9krmOXPmcnBcGLtyvVloqw3v-KwIewBZW0W91WqKinx0W6yVWRp41g-Ejr0_vtO5LzngyGovnQha8w5lGQLhnMTj-ZqxN3ylvfZDSoX1G6BYyEcPVU6AWmEikc1fD32sGVvJSey1EnTw62RbjstkR9t4iPGffinLXKpKt1L4D68eLjzs5WqVklPniEAWg2NRtxsQrXMcRRcI7QqfZo2DNjgskRpy3k3sAGdsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست:
سودا (مرضیه) ابراهیمی شمس‌آبادی
، بلاگر ۳۳ ساله اهل بندرعباس، به اتهام «افساد فی‌الارض»، توهین به خامنه‌ای و فعالیت‌های ضدحکومتی به اعدام محکوم شده است. نیویورک‌پست همچنین به
ترانه رحیمی
، ۲۰ ساله، اشاره کرده که به اعدام محکوم شده و خواهر دوقلویش
رومینا رحیمی
به ۲۵ سال زندان محکوم شده است. این رسانه همچنین به نقل از منابع حقوق‌بشری از اعدام دست‌کم
۲۹ معترض بازداشت‌شده از ماه مارس
خبر داده است,صدایشان باشیم
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22999" target="_blank">📅 12:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الجزیره: هم‌زمانی بحران در تنگه هرمز و باب‌المندب، خلیج فارس را در وضعیت «بین دو فک گازانبر» قرار داده است؛
با ادامه اختلال در هرمز و پیشروی حوثی‌های مورد حمایت ایران در مسیر باب‌المندب، دو مسیر حیاتی انرژی و تجارت هم‌زمان تحت فشار قرار گرفته‌اند. این وضعیت فشار قابل‌توجهی بر کشورهای خلیج فارس، به‌ویژه عربستان، وارد کرده و
واشنگتن در مدیریت درگیری با تهران، بیش از پیش با این چالش روبه‌روست که منافع و امنیت کشورهای خلیج فارس را نیز در نظر بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22998" target="_blank">📅 12:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فاکس‌نیوز: مقام ایرانی می‌گوید ایران تا پذیرش کامل شروطش از سوی آمریکا وارد مذاکره نمی‌شود.
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس ایران، در ایکس نوشت تا زمانی که آمریکا همه شروط ایران را نپذیرد، گفت‌وگو و مذاکره فایده‌ای ندارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22997" target="_blank">📅 11:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری رژیم ایرنا: دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22996" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3mA9HdmWt6h_NhGcatEloFRbziB3cowr2XOyQKI1lUSqpnpdt167lC9RdOGBLaihxOCS3oEQoSd0BinKy4oyJmx_miQl_9nJiOxA0ZboR5lUx6I_tEyjTLmY4qCkupA7eUa-PuvIHV3FaMJpDApJrEjhQDAsfnZTzdc6fG_jn9cjPqdxh0zkGTCCPfnDVDMJ60ucvFZYGfjrigNSm3Eg2bU82Mh5O0FcxxeHT6t47C6pxNTuy7AQijdwimMeQMmu5wFr04aWReyHLNFBwD5_1JOfRFarrzRDaE4x03K9K_JQLQaJupjxBM_kH735vvfnRzJsOoRLJvmzhW6Va1cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک کشتی هنگام عبور از تنگه هرمز مورد اصابت پرتابه‌ای ناشناس قرار گرفته است. در حال حاضر، اطلاعاتی درباره وضعیت خدمه، میزان خسارات وارده و پیامدهای زیست‌محیطی این حادثه در دست نیست.
در پی حمله گزارش‌شده، آتش‌سوزی در این کشتی رخ داده است. مقامات محلی در محل حادثه حضور دارند و در حال کمک به تخلیه خدمه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22995" target="_blank">📅 11:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdd8f1fc2.mp4?token=oxtDrmvd1ESz2BRX8k9_wmeO8X5WwNMPhz104GzhPj_mjhIOUNMxeLMQ4fyxbGSkn1ZL7L2P8ahquS-vm0KtMARZhn8nU5EfqRXzSIwXrzjWVHUNI6oAzGz94LOyD4Y1jD9HldkBJyzHe484mZSBujA8aNM3k2BSiSdTTYTua0d2XZeryobTJAq4frPgvQvZkmeEmhb_wIhx67P1ScORP4kZr8eYZTgUXsw1UuCd0_xUTNdgfHaKLg6WwBmweYYpnYBX-N2WkL_lL9qGa9LiXAl8zyIFqKidWGJewbbJKXgDW2aiaYa8Cq6IFM0k7k9qr3RupAqO_SWorrAjydjKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdd8f1fc2.mp4?token=oxtDrmvd1ESz2BRX8k9_wmeO8X5WwNMPhz104GzhPj_mjhIOUNMxeLMQ4fyxbGSkn1ZL7L2P8ahquS-vm0KtMARZhn8nU5EfqRXzSIwXrzjWVHUNI6oAzGz94LOyD4Y1jD9HldkBJyzHe484mZSBujA8aNM3k2BSiSdTTYTua0d2XZeryobTJAq4frPgvQvZkmeEmhb_wIhx67P1ScORP4kZr8eYZTgUXsw1UuCd0_xUTNdgfHaKLg6WwBmweYYpnYBX-N2WkL_lL9qGa9LiXAl8zyIFqKidWGJewbbJKXgDW2aiaYa8Cq6IFM0k7k9qr3RupAqO_SWorrAjydjKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمی پیش گزارش زنده فاکس نیوز از روی ناو جرج واشنگتن و پرواز جنگندهی F-15 و F-35 با دریافت کردن سیگنال تهدید از سوی ایران(پرتاب. موشک/پهپاد) به کشتیهای عبوری. همچنین در ویدیو میبینید که تماما پشت سر مجری موشکها و بمبها قرار دارد و این ناو بیش از اندازه تا دندان مسلح به منطقه عملیات آمده.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22994" target="_blank">📅 03:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارسالی : من امروز پهبادم رو بردم رو کلانتری شهر رستاق تمام کلانتری تخلیه کردن ، الان رفتن تو بانک کشاورزی موندن
😂
😂
😂
اسممو نذار
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22993" target="_blank">📅 02:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کانال ۱۳ اسرائیل گزارش داده ارتش این کشور در پی تحولات باب‌المندب، احتمال
شلیک موشک و پهپاد از یمن به سمت اسرائیل
را جدی گرفته و در حال آماده‌سازی برای چنین سناریویی است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22992" target="_blank">📅 02:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad.Rf</strong></div>
<div class="tg-text">سلام یاشار من از اینستا چند روز پیش پیام دادم ندیدی بغل پادگان 02 ارتش رو سه روز پیش زدن من رفیقم سربازه اونجاس گفت با پهپاد پادگان بغلی رو زدن ولی کسی صداشو درنیورد حتی میگف بازرس اومد فرداش ببینه چه خبره دوباره پدافندا شروع کردن کار کردن بازرس فرار کرد</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22991" target="_blank">📅 01:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22990" target="_blank">📅 01:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromممدم✌🏽</strong></div>
<div class="tg-text">یاشار تقریباً ده دقیقه پیش موشک از تو شهر بندرکنگ بلند شد به قدری نزدیک بود کل خیابونا صداش پیچید</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22989" target="_blank">📅 01:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش صدای انفجار بندرعباس
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22988" target="_blank">📅 01:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22987" target="_blank">📅 00:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سی ان ان: پیت هگست، وزیر دفاع آمریکا، برای حضور دو خدمه جنگنده F-15 سرنگون‌شده بر فراز ایران در برنامه«60 Minutes»تحت فشار قرارشان داده است.
به گفته چند منبع آگاه، هر دو نظامی درباره حضور در این مصاحبه نگرانی داشتند و هگست به‌صورت خصوصی با آنها دیدار کرد تا مشخص شود آیا داوطلبانه در برنامه شرکت می‌کنند یا باید با دستور به این کار وادار شوند. در نهایت، یکی از آنها با نام مستعار
«براوو»
با حضور در مصاحبه موافقت کرد، اما نفر دیگر با نام مستعار
«آلفا»
از شرکت در آن خودداری کرد. پنتاگون این گزارش را
«دروغ کامل»
خوانده و گفته تصمیم حضور در مصاحبه کاملاً بر عهده خود این دو نظامی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22986" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر خزانه‌داری و دارایی ترکیه به شرکت‌ها و مؤسسات مالی این کشور درباره معاملاتی که ممکن است مشمول تحریم شوند هشدار داده است؛ موضعی که چند روز پس از تحریم یک بانک ترکیه و دو شرکت زیرمجموعه آن به دلیل ارتباط مالی با ایران اعلام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22985" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22984" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارسالی : سلام داداش وقت بخیر
از بندرکنگ امشب با فاصله هر 30 دقیقه دارن یه پهپاد یا موشک میزنن به طرف خلیج فارس تا الان 4یا5 تا زدن
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22983" target="_blank">📅 23:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ارسالی : مرز باشماق هم بسته شد من اربیلم و همسرم رفته ایران الان لب مرز مونده نمیزارن بیان گفتن مرز فعلا بسته س و مونده تا ببینم تکلیف چه میشه
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22982" target="_blank">📅 22:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرنگار الجزیره: نیروهای اسرائیلی وارد منزل همکارمان، علی السمودی، در جنین شدند، خواستار تحویل او شدند و به پسرش حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22981" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک موشک بالستیک حوثی ها در منطقه "جازان" در جنوب غربی عربستان سعودی به یک مسجد اصابت کرد که منجر به زخمی شدن تعدادی از افراد و خسارات جدی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22980" target="_blank">📅 22:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22979" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22978" target="_blank">📅 22:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22977" target="_blank">📅 22:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وای نت عبری : حملات جدید اسرائیل به جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22976" target="_blank">📅 22:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22975" target="_blank">📅 21:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تصویر ۳ پاسدار کشته شده در سراوان @WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22974" target="_blank">📅 21:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری رژیم ایرنا:
دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد
منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22973" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پرتاب موشک به سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22972" target="_blank">📅 20:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آسوشیتدپرس: نفتکش آسیب‌دیده در خلیج عمان باعث گسترش لکه نفتی شده است.
بر اساس گزارش جدید، آلودگی نفتی ناشی از یک نفتکش که گفته می‌شود توسط نیروهای آمریکایی هدف قرار گرفته، در حال گسترش به مناطق حفاظت‌شده زیست‌محیطی در عمان و ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22971" target="_blank">📅 20:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmsNnrT7GCfhl6IlL1--ZHTmJkvsrWHfBIoLT3qA4cW5YvukftMQQ--t7HAJ1xXz-SHGXvOrQr-wtZTcRdN8RUpSaw4NoPPRdoSh_bbVHNTtu-5R3ybcNfcmolwh4BExuYBHsrPIl4vWgNtGk_j3EH6GDD-5AthuqKzvOT2w6pnh3Pz5N0s56STjDpf2-yKvwHDvSWRsJIeQOJ-0hqmA6f3m43dXJjgYxIecOUZH-w9LYMd2Vf6yUfw24CLjxpkAqG9vZuBZCQ4c7_NbfwYWxZZQkJSJOxgcP---IeGnPI74I_RWQn-iQVesHzy9k2sga-1LgiWPlfEs6WjvAHE2cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22970" target="_blank">📅 20:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22969">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دو مقام ارشد امنیتی عراق به رویترز:
ساعاتی پیش سکو های پرتاب پهپاد در چند نقطه از مرز ایران و عراق کشف شدند،
تا اطلاع ثانوی گذرگاه های مرزی با ایران بسته خواهند بود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22969" target="_blank">📅 19:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_8yqbEzeDtse5Sf9c6aLzd5LCWdq6GkiSQwIOWE2vfkcXpRqRC1VQXM6Tr4VaXkrqk8zrhCOn8ZQvR5-i_ZLUyjmwrHNw-ZCRSlUIphAdTIXmrmQ6GfV2vV08w9LTO2xm4X_-pcl238m-B7jKD2DuuExSRQHVq_boVhOI-XwH4f3gz_Z0d6cLVZRBzU9H-MYECVmkNcelv6eU1FEtox427TxeKbR1Z20xfP33INy0W4o3WdVV3v2YQy75TvhB1qpJWMCtpjG3mZC2UAs7p71NNmQ5Zu5F10yL6qOmMv08VCm31PClirtfG4rCyQ9YB28qWJ6NAO8FJSUZ-IJZemcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد  @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22968" target="_blank">📅 18:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد. @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22967" target="_blank">📅 18:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=CJafeoqdeHSf0RpCkpQKaeWZwTwBfVIxSQKjzjNWwMDknwOb-m9dCTke2RK7ezEGsGjxRxdo7iV6cE8oE2PPInpLAk6vxgiSOgk7O-lKApsYcQEOsGpvoXJQFYWBiP3AbHfe-A9XA8UpG0I4sLzQHhP_zKX4HmyP39oWgG0II0G1gLcCA_A07rlBsf7UPv2-MuCMbl_TcLTxYJIl7ebisah-txd46ZoHYEWvxelhotnKDmeZrWMH5_BljOlx9Vwe1wUyvgX8X5FRD1OIDbZ5Rs4x_9JQxFRDXOTYann1AD46Jqmo08a4-lrG8tZLmLpG0rObGGGGGon72DtYeE17n0e9Dhy5DpjQ8q3OAWt6RTcWnXBaBl8PZ8pKIy3jVjokoVIPo5S_jvblHuDuw8x_03x72twE0dNDnCv23aCSLkZ0m0h8XV1ts-otDbsyf2F19bo8T3lTC6hW9pRbtNNMzCz7SgD4aT_0gzeVep5O5eiudhyfPxpl6Azgh3DLjDTPxEnZDwGiNMXONA8GqTd2H5QufqFNVqtCuICxKV-1R8sV8jc5o5Woz21e0P8EbE35pFXpO8oIe_G4qaijRi75GyFbPDDE1ViialJGfGryFQUHXYSIMICv32rUmkNunrju-1ADp0YkiCQ6C1LK1yhIzc-EV7FU8vRvuO7uA7_ZtC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=CJafeoqdeHSf0RpCkpQKaeWZwTwBfVIxSQKjzjNWwMDknwOb-m9dCTke2RK7ezEGsGjxRxdo7iV6cE8oE2PPInpLAk6vxgiSOgk7O-lKApsYcQEOsGpvoXJQFYWBiP3AbHfe-A9XA8UpG0I4sLzQHhP_zKX4HmyP39oWgG0II0G1gLcCA_A07rlBsf7UPv2-MuCMbl_TcLTxYJIl7ebisah-txd46ZoHYEWvxelhotnKDmeZrWMH5_BljOlx9Vwe1wUyvgX8X5FRD1OIDbZ5Rs4x_9JQxFRDXOTYann1AD46Jqmo08a4-lrG8tZLmLpG0rObGGGGGon72DtYeE17n0e9Dhy5DpjQ8q3OAWt6RTcWnXBaBl8PZ8pKIy3jVjokoVIPo5S_jvblHuDuw8x_03x72twE0dNDnCv23aCSLkZ0m0h8XV1ts-otDbsyf2F19bo8T3lTC6hW9pRbtNNMzCz7SgD4aT_0gzeVep5O5eiudhyfPxpl6Azgh3DLjDTPxEnZDwGiNMXONA8GqTd2H5QufqFNVqtCuICxKV-1R8sV8jc5o5Woz21e0P8EbE35pFXpO8oIe_G4qaijRi75GyFbPDDE1ViialJGfGryFQUHXYSIMICv32rUmkNunrju-1ADp0YkiCQ6C1LK1yhIzc-EV7FU8vRvuO7uA7_ZtC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22966" target="_blank">📅 18:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvjo43mBgtYOLDzHU0vLZo-RlF55ZmIkvUUSgWF2mkyalVCNqdiXEjWZnGhmrGjnRbu4EkLOu1BL8dM1z25tW2PCFa_5IB2kJ9RLrBWFz27PGbNCzPk0rdUOyvd3AmDblRAE2JS9GahXXyOMvsnHt1ZmhjeWtdabM_yzYWgQeZkYNNyZqXyqo84ncVBXjOmHz3wV1zu4AJWRjH73ggpOd8RDbJcbUQAH6-5r7K-Qj4b0O6rRuiDwBD8ZVgfgqQjnaSj6z2rlZZn_9bBWotEljhrgjDBbJePTVclwe9Np-t8GHWcwTTSs9r_AiBFmW1v3IUadV-PegM6ayWSAmAG_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8Qmx8OmWgxNpXFRx1FI1QvQAghqnlQgVJv3UzF0VR4Ifae52WEO21lfNqfG3K9x5smjbJPPdE6JHTo-z5qrvBozbCau_NGLTXCFZnnYKPpo5MqE-VMtfVpzX86O3F76JgqQSof8d6dXZTsrZpzjMfU66Zguf4N1sDXpwE4Y2LqJAPz2B5H-MX7CUjNribyiYGbLVSQDT0tbjupiCHoRUj-0M1Fzc2McUL3fRuHAV3c6GT75ZksDl2os8CB83_5qCMfpySrf2rXiIRC1uGJ9DsaBcDLBGMB0zFvWnWBvEzmldxu2NCrfIay2yHQ632LeI27EHxLx2z8X1ScPCUS5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7efO9TFRycY8wCxnpws7UxM60kGOq1GBbZAJOgL-mFypXaUQg7INF5Sl8lynU0JsMqxeSu1VXhaHAm1sjxHrMFz9Pj3N8X2gV9hMnvuhYqLir8REsF3v-aejRjV4NK3DXX8T35-LnhSAg7txSJ-u4R4UgJDKdtzVlkDBNSvz1-RzP14xg4XP2CCUqigEv2aE0yX9xHH2WonNrtWo6ATc8PCy3QaMEn0pubiLEqrDTJHM9irCT5T1rOKuxwAkEziDl8N4QBv1GAh9UvKAt_YWGioUProwhiaosU6z5WXEbfW-mCKyHF7-_H2pP4keGEWRSb20MXX7DOj9HQhvDSafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhF0CCMBFf_8JNcSyt_IwcEvNShb3yUX_BkgAFmgVV8cOSpsCl_HIZtuMVRxN_04yM0J6ZcM3EOu12_z7dTVXt84TYAylGmJYP5qcS690WRDo9ESsLfJXu-f5eFsIc064jJivVb7sZV1xy5TnZoQPLxocCusVoU3jSDfxUBDtVggFTEB9FPMWBlWnwFxxRl4DUWGdR7TKFOk_t2Rh-IMpLd70EUUtRO-w4DHBfokjs00QZy4LJrevZeiriX10KTnnOa2rorOYOU7qbc9QvxymFdWKUBiHiaK_uPR9PfNLMBlAJSPlRodIqH3mRwmtJP61VPfXV-_fCro-BzZCuloJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آمادگی برای حمله زمینی احتمالی به ایران
سنتکام : تفنگداران دریایی ایالات متحده بر روی عرشه پروازی ناو
«یو‌اس‌اس پورتلند» (LPD 27)
در حالی که این کشتی در دریای عرب در حال حرکت است، برای عملیات احتمالی تمرین می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22962" target="_blank">📅 18:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی: نشست روز دوشنبه ایران و کشورهای خلیج فارس در عمان به درخواست و ابتکار عمان برگزار می‌شود، اما انتظار نمی‌رود در این نشست توافقی برای بازگشایی تنگه هرمز امضا شود. به گفته این مقام، ایران همچنان خواهان توافقی است که به تهران اجازه دهد از کشتی‌های عبوری از تنگه هرمز عوارض دریافت کند؛ موضوعی که عمان با آن مخالف است. این نشست قرار است علاوه بر هرمز، درباره مسائل منطقه‌ای نیز گفت‌وگو کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22961" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت خارجه بحرین اعلام کرد که این کشور در نشست وزارتی پیشنهادی درباره وضعیت تنگه هرمز شرکت نخواهد کرد و تا پیش از ازسرگیری روابط دیپلماتیک با ایران، در هیچ نشست جمعی که ایران در آن حضور داشته باشد، طرف نخواهد بود. بحرین همچنین تأکید کرد هرگونه توافق یا ترتیبی درباره کشتیرانی در تنگه هرمز باید بر اساس حقوق بین‌الملل باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22960" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آسوشیتدپرس: یک شهروند ایرانی-آمریکایی از زندان اوین آزاد شد، اما همچنان اجازه خروج از ایران را ندارد.
کامران حکمتی، جواهرفروش ۶۲ ساله نیویورکی، پس از گذراندن حدود نیمی از حکم دو ساله خود آزاد شده، اما مقام‌های ایران همچنان ممنوعیت خروج او از کشور را برقرار کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22959" target="_blank">📅 17:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتاق جنگ با یاشار:
اگر پرونده ایران در شورای امنیت به رأی‌گیری برسد، باید بین دو حالت فرق بگذاریم: اگر رأی‌گیری درباره
یک قطعنامه معمولی و الزام‌آور
باشد، روسیه یا چین می‌توانند با وتو جلوی تصویب آن را بگیرند. اما اگر رأی‌گیری از نوع
رویه‌ای
باشد، روسیه و چین حق وتو ندارند و نمی‌توانند جلوی ادامه روند را بگیرند. از طرف دیگر،
وتوی روسیه یا چین به معنی پیروزی ایران نیست
؛ اگر بیشتر کشورهای شورای امنیت علیه ایران رأی بدهند و فقط روسیه و چین مخالفت کنند، از نظر سیاسی نشان می‌دهد که اکثریت جامعه بین‌المللی با موضع ایران همراه نیستند و روسیه و چین در اقلیت قرار گرفته‌اند. حتی در برخی موارد روسیه و چین ترجیح داده‌اند
ممتنع
رأی بدهند و قطعنامه بدون وتو تصویب شود. بنابراین یکی از اهداف مهم آمریکا و کشورهای اروپایی می‌تواند این باشد که در صورت رأی‌گیری،
بیشترین تعداد کشورها را پشت موضع خود جمع کنند و روسیه و چین را در اقلیت و حامی یک رژیم تروریست نشان دهند
و آنها را
به اصطلاح در جمع خراب کنند
.؛ حتی اگر این دو کشور در نهایت یک قطعنامه ماهوی را وتو کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22958" target="_blank">📅 17:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPR06Zun3Fdkpw2LKV0gDwkZZ2VEaTWzINpbSn-ZS_AEjxYzry_jcWZvA_1ihjbV4LhYoRYIv34qt6GD64DOzww6XwK1uV_4v5__9BZ7YzVAwgSeam5oKucUqaaoOniEX_69-a_dSD9AwZtXV8b9kkJZ0aCgy5tO-pZ8jxSQ94dBsVYuZoyF0fV0arvQ4E3iOd1FD_msdKM2L4AzEb5UTksmHAc5NE2Qj5AzGxOAaTjw59HHB43fBIoX9MWln0gBzChko807Eufw3JLRrIRm-ulK8PcMn5fN-l5aybVnEk-6fv-mq-ZeAIHg7r3AFch-ibkpAEW0wtTn5oSQ7oxq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست:
ایران پیش از حمله موشکی ۱۷ ژوئیه ۲۰۲۶ (۲۶ تیر ۱۴۰۵) به پایگاه هوایی موفق السّلتی در اردن، تصاویر ماهواره‌ای با وضوح بالا از این پایگاه در اختیار داشته است.
این تصاویر که توسط
نهادهای چینی در اختیار ایران قرار گرفته بود، هم پیش از حمله و هم پس از آن برای بررسی وضعیت و خسارات پایگاه استفاده شده است.
مقام‌های آمریکایی نام شرکت‌های چینی را اعلام نکرده و دولت چین را مستقیماً به دخالت متهم نکرده‌اند. در این حمله که منطقه محل اسکان نیروها را هدف قرار داد،
۳ نظامی آمریکایی کشته و ۴ نفر دیگر زخمی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22957" target="_blank">📅 16:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ: اگر ایران سلاح هسته‌ای داشت، ما تماس می‌گرفتیم و می‌گفتیم: "قربان، آیا می‌توانیم با هم ملاقات کنیم؟" ما با آنها بسیار متفاوت برخورد می‌کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22956" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است
بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22955" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=Db5HWeDyDBAaJu4uyy6DhzaENKKFBan4mu6YgGoQVsqgz0nZ-P70WEErP0ZS-OCeBg2bcB_49xNlnL52JGhbu83asxlhIJ3RzZAqsrr1A3eplsw_kmw3bXrGskNApbzaPrmS3mpKpMfYHbF5f7HG0e2tB7S57K419kVev-KosneKEeMHnykUT_K4rs1pzNgnmE4hl4CZTplFLC97Y-oGL2y9dbVAf_m1TBg917zZ2x-oln-UsaIySNeE_bbFt1sm7gNWKfZzhLMzfV_H7FVXweaVqfw1FTBA32OV8Yh_eyvFo-ep1DQaKRcRmciN15dqWCuU8d-WBkRXo-19C8ZwKWXEQjYX4gz_mX5FKB0ajbQ4tU7iXxa8jEDRetzoiuP-9d2bQ9eo8ZzxCVOAUIaKGGV4PXSszWUgUK6PGju7isblWGFCqiJM70jRdk49yaf_xtvGPLN6KYlKbC01RkaMfRiIt3cg8NKpJvBlovd2DfoEWSSVUiTV5-1kuXYq2IrZQjaqAsL4mF1SmwapheEnFAuG2AejIwBEQcqis08XVPMEMuiaAzR2mqYoAmyDp_4aZLSe25YOxpXuMRnHbHpiueLo6C8bzDb6TGYMpO2VA-FDDBsEQ2WlwYYf2SohUjWKLEDMOQD8_xg05gCtwNCazAhYpekKFLvehKbb2gEa3gc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=Db5HWeDyDBAaJu4uyy6DhzaENKKFBan4mu6YgGoQVsqgz0nZ-P70WEErP0ZS-OCeBg2bcB_49xNlnL52JGhbu83asxlhIJ3RzZAqsrr1A3eplsw_kmw3bXrGskNApbzaPrmS3mpKpMfYHbF5f7HG0e2tB7S57K419kVev-KosneKEeMHnykUT_K4rs1pzNgnmE4hl4CZTplFLC97Y-oGL2y9dbVAf_m1TBg917zZ2x-oln-UsaIySNeE_bbFt1sm7gNWKfZzhLMzfV_H7FVXweaVqfw1FTBA32OV8Yh_eyvFo-ep1DQaKRcRmciN15dqWCuU8d-WBkRXo-19C8ZwKWXEQjYX4gz_mX5FKB0ajbQ4tU7iXxa8jEDRetzoiuP-9d2bQ9eo8ZzxCVOAUIaKGGV4PXSszWUgUK6PGju7isblWGFCqiJM70jRdk49yaf_xtvGPLN6KYlKbC01RkaMfRiIt3cg8NKpJvBlovd2DfoEWSSVUiTV5-1kuXYq2IrZQjaqAsL4mF1SmwapheEnFAuG2AejIwBEQcqis08XVPMEMuiaAzR2mqYoAmyDp_4aZLSe25YOxpXuMRnHbHpiueLo6C8bzDb6TGYMpO2VA-FDDBsEQ2WlwYYf2SohUjWKLEDMOQD8_xg05gCtwNCazAhYpekKFLvehKbb2gEa3gc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«ما
تنگه هرمز را در اختیار گرفتیم
. همه مین‌ها را پاکسازی کردیم. من گفتم: «پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟» گفتند: «قربان، این مین‌روب‌ها
زیر آب هستند
. آنها همیشه در زیر آب فعالیت می‌کنند.» گفتم: «چرا این کار را می‌کنید؟» گفتند: «به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه
خصومت و درگیری زیادی وجود دارد
.» به عبارت دیگر، اگر در یک آبراه مین وجود داشته باشد، یعنی افرادی هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
در آنجا دیگر هیچ مینی وجود ندارد، هیچ چیز دیگری هم نیست.
و اگر ببینیم آنها در حال حرکت هستند، خودتان می‌بینید چه اتفاقی می‌افتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22954" target="_blank">📅 15:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=Qr8qoo1KMozuWho6WY8v2acM7AkDEo7O9g1RzaVkvfUUhI4XcF0q916z_X7roLVAqnVwQnY4lE_Z2b3ZdZAALfvoWC5i9zP5SbohdNFKFnwxxIQ4wkEJe-Lgc0Bke7u10q-Dt4L_sFnPPXtqiY_GnSd3Ly2wrmzBrBcELF3URWpkhQ64cUcj5M9qGoWq2iXIQpQirpqwkHnpCsAHsR3e0iwBELxCHqyXB5wfjPrwE1EUov-_-yp9GIFBpaA94d7WrGUcdxcmTJSyCe5pgLfdKmYKBvWyq_qowpQyEOnlpU0FZhWqaC9SgJ8BwrvwTNUlfmn0-wgfCjFg2yi5CM5DgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=Qr8qoo1KMozuWho6WY8v2acM7AkDEo7O9g1RzaVkvfUUhI4XcF0q916z_X7roLVAqnVwQnY4lE_Z2b3ZdZAALfvoWC5i9zP5SbohdNFKFnwxxIQ4wkEJe-Lgc0Bke7u10q-Dt4L_sFnPPXtqiY_GnSd3Ly2wrmzBrBcELF3URWpkhQ64cUcj5M9qGoWq2iXIQpQirpqwkHnpCsAHsR3e0iwBELxCHqyXB5wfjPrwE1EUov-_-yp9GIFBpaA94d7WrGUcdxcmTJSyCe5pgLfdKmYKBvWyq_qowpQyEOnlpU0FZhWqaC9SgJ8BwrvwTNUlfmn0-wgfCjFg2yi5CM5DgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما یک درگیری نظامی کوتاه داشتیم. آن‌ها می‌گویند: «آیا ممکن است از کلمه «جنگ» استفاده نکنید؟ چون وقتی از کلمه «جنگ» استفاده می‌کنید، موضوع کمی متفاوت می‌شود.»
به نظر من، این یک درگیری نظامی است. ما آن‌ها را به شدت تحت فشار قرار داده‌ایم.
در مورد ونزوئلا، ما آنجا را تحت کنترل خود درآوردیم. ما در آن جنگ پیروز شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22953" target="_blank">📅 15:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وای نت
: کشورهای خاورمیانه، سقوط جمهوری اسلامی را به نفع منطقه می‌دانند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22952" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صداوسیما:  پس از بسته شدن دو پایانه مرزی شلمچه و چذابه به شکل یک طرفه از سوی عراق؛ از ساعاتی پیش مرز چذابه برای فقط خروج اتباع عراقی که قصد بازگشت دارند؛باز شد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22951" target="_blank">📅 14:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آسوشیتدپرس: رئیس‌جمهور لبنان به نباطیه در جنوب لبنان رفت.
جوزف عون در سفری
کم‌سابقه
به جنوب لبنان، در حالی که نگرانی‌ها از حملات مجدد اسرائیل افزایش یافته، از افزایش حضور ارتش لبنان و تلاش دولت برای حفظ ثبات منطقه سخن گفت. این سفر اکنون پس از عملیات اسرائیل در ارتفاعات علی‌الطاهر و ادامه تنش با حزب‌الله انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22950" target="_blank">📅 14:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز: کشورهای بریکس بر سر بیانیه مشترک به توافق رسیدند.
منابع می‌گویند اعضای بریکس در نشست دهلی‌نو بر سر بیانیه‌ای توافق کرده‌اند که
اقدام نظامی یک‌جانبه هر کشوری را محکوم می‌کند
، اما برای جلوگیری از اختلاف، نام هیچ کشوری در آن ذکر نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22949" target="_blank">📅 14:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=MCklo6wMe-SO1omOAuPH2HpmwiNtHZp_i7vtzhiFAmWgqIaIOWI84oDs9T8YxpZj5XZtCik0bqVdYtM1ttiOGkWSfGKV7cJa6KWFwlSwap2KDy5jh7FVm0ry4fVCe-ycjCBgfEzSlbr0ugAefbUYclhDXNHIW8hYGFgxwkzsHQcUghLgux7LxLnqxF9n6v4GRiSZu2B0yXj5hRIqMF1iRzQitWkYwWKvIVy4aoiqqgZ5GU9_wQZMNqAYbgPFgrFs50LE6vRH2iukFXjHQX-FTmqkM9blcemGH8N0hgzxc36TJjxv-4j0Ywj6aCfSx9So0J59PCcQFkZFVi4K6cBLLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=MCklo6wMe-SO1omOAuPH2HpmwiNtHZp_i7vtzhiFAmWgqIaIOWI84oDs9T8YxpZj5XZtCik0bqVdYtM1ttiOGkWSfGKV7cJa6KWFwlSwap2KDy5jh7FVm0ry4fVCe-ycjCBgfEzSlbr0ugAefbUYclhDXNHIW8hYGFgxwkzsHQcUghLgux7LxLnqxF9n6v4GRiSZu2B0yXj5hRIqMF1iRzQitWkYwWKvIVy4aoiqqgZ5GU9_wQZMNqAYbgPFgrFs50LE6vRH2iukFXjHQX-FTmqkM9blcemGH8N0hgzxc36TJjxv-4j0Ywj6aCfSx9So0J59PCcQFkZFVi4K6cBLLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران (ونک) ی غذاخوری افتتاح شده که عرزشی سوز ترین رستوان شده به اسم بی بی که تخصصش  کتلت درست کردنه، حالا ی عده عرزشی فشاری شدن و بهش گیر دادن، میگن تو عمدا اسم غذاخوریتو گذاشتی بی بی و فقط کتلت درست میکنی.
@WarRoom
😂
✌🏼</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22948" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22947" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22946" target="_blank">📅 13:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=TFLYW7Z2zV7W2Vb7bHWLyJYIr-D9UNyuQ67n8VYIFVEo7kp9VdOV3ammhzktpzQd0jkCksBEdhiIt3_u7NLr9ORBVkLSY95WPDfhEQKI-XMO2kczENMJJFWgE72iMHzAQ8v0nmoT_QZKZSSOIycRn0GNKlUEC5bvtxzYcmeB7KskPTJA7OoJI7Ra_WxGk2r7IvUbomA8qz4CMZS1fi_Omiuum5VbQGU_lcUF-y0YWy3b5ONzSQTX2pkzRn14cnvSd6nxwGo0LKPaYajY3WsAYsH-ue5QoqN1o7-5YPBqYL5R_08461adRac1eytff3ZgOu7BWwKnT60K7tmDZviq-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=TFLYW7Z2zV7W2Vb7bHWLyJYIr-D9UNyuQ67n8VYIFVEo7kp9VdOV3ammhzktpzQd0jkCksBEdhiIt3_u7NLr9ORBVkLSY95WPDfhEQKI-XMO2kczENMJJFWgE72iMHzAQ8v0nmoT_QZKZSSOIycRn0GNKlUEC5bvtxzYcmeB7KskPTJA7OoJI7Ra_WxGk2r7IvUbomA8qz4CMZS1fi_Omiuum5VbQGU_lcUF-y0YWy3b5ONzSQTX2pkzRn14cnvSd6nxwGo0LKPaYajY3WsAYsH-ue5QoqN1o7-5YPBqYL5R_08461adRac1eytff3ZgOu7BWwKnT60K7tmDZviq-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: ما با قدرت بسیار زیادی تنگه هرمز را کنترل می‌کنیم. هیچ‌کس انتظار نداشت چنین اتفاقی بیفتد.
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22945" target="_blank">📅 13:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=drc4ts_gue6sb2jemRtohKIq89M5miTaltk9MVLjNZBM6U3D8-1ZwevDGBvh51HWYp7XFjogz9ke2PeR7StwCrOWLgVIhOM1ro-ucUH4imBszHNDjU05QD9ZOHu1c9kCLc2RsA2fZMgxOkC6ldII-LKIV7bBqXjHs3kJH2DNmA2wWA3QH03eo3ugiHgfqydwX0iTjDi_-trV59uDjBvZnxSDAee7e_gpME1tkKa-GUgCt4QRG-PrLMZEjTdKXhTHfqnLSQn3J7wkIZnaK9yYccWjbRezPSyD6D-FpIS40DLy79_5a-uUNRSYe-rfQ91NCFdRaUdm5sNFEFiPg4SA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=drc4ts_gue6sb2jemRtohKIq89M5miTaltk9MVLjNZBM6U3D8-1ZwevDGBvh51HWYp7XFjogz9ke2PeR7StwCrOWLgVIhOM1ro-ucUH4imBszHNDjU05QD9ZOHu1c9kCLc2RsA2fZMgxOkC6ldII-LKIV7bBqXjHs3kJH2DNmA2wWA3QH03eo3ugiHgfqydwX0iTjDi_-trV59uDjBvZnxSDAee7e_gpME1tkKa-GUgCt4QRG-PrLMZEjTdKXhTHfqnLSQn3J7wkIZnaK9yYccWjbRezPSyD6D-FpIS40DLy79_5a-uUNRSYe-rfQ91NCFdRaUdm5sNFEFiPg4SA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جنگ در ایران چه زمانی پایان می‌یابد؟
ترامپ: فکر می‌کنم خیلی زود؛ احتمالاً درست پس از انتخابات میان‌دوره‌ای.
آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا انتخابات را پیچیده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22944" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=oZWNk4-HgjYR7MxcihppHir6xNRvkOScZB1VOWPZRNKWX6X6rxLTkUBYmhlHq16RfYiGqxR2d93HaHgVZeog8aTF3yN8nFX-RQlyphXkqaO1C2A83SstZlpTeFmk5_YOrwbc7gaFmzkSsg-OEreaoCgdRuoJmaUAKZQhISBPslwyrscPfMSIVAZHzzdBpK0WuzCEw6YDL93UpVkK5DZDxd4ClIbyHsYabKuAYnaF_DnyIYXFklfZlCykFuEDR-zZfgqn2Mg7UuA6EkW23PFXNyRh6dm8WwCRJtq93hCZ2r5UDlTjezaGwKQwrSlNC4UwJCkhY9DEqhBqNQZVCaX-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=oZWNk4-HgjYR7MxcihppHir6xNRvkOScZB1VOWPZRNKWX6X6rxLTkUBYmhlHq16RfYiGqxR2d93HaHgVZeog8aTF3yN8nFX-RQlyphXkqaO1C2A83SstZlpTeFmk5_YOrwbc7gaFmzkSsg-OEreaoCgdRuoJmaUAKZQhISBPslwyrscPfMSIVAZHzzdBpK0WuzCEw6YDL93UpVkK5DZDxd4ClIbyHsYabKuAYnaF_DnyIYXFklfZlCykFuEDR-zZfgqn2Mg7UuA6EkW23PFXNyRh6dm8WwCRJtq93hCZ2r5UDlTjezaGwKQwrSlNC4UwJCkhY9DEqhBqNQZVCaX-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
ایران
مسئول حمله به خط لوله نفتی شرق-غرب عربستان است؟
ترامپ: فکر می‌کنم آنها هستند، احتمالاً آنها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22943" target="_blank">📅 13:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ در مورد حمله به خط لوله نفت سعودی: حوثی‌ها نمی‌خواهند با ما وارد جنگ شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22942" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ: ما آتش را در غزه خاموش کردیم و روند صلح را در آنجا تسهیل خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22941" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دونالد ترامپ در مورد حمله به خط لوله انتقال نفت در عربستان سعودی: به احتمال زیاد، ایران مسئول این حمله است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22940" target="_blank">📅 13:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">.:
سلام یاشار جان من ساعت ۱۲ فردوسی بودم
دلار ۲۴۲ معامله میشد
اقتصاد مملکت داره منفجر میشه
خدا به مردم رحم کنه با این گرونی ها</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22939" target="_blank">📅 13:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ : اوضاع در ایران برایمان بسیار خوب است
همه چیز  به آرامی حل خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22938" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=aK4wS3kcujTzhqkMUagDcjUe3OcOn2RFCHoNM4hEP4QtpOGgNsT541sZgqtrOkTdIxWFvO1cNFf63CWAYPlTYwVZryH_UZZH8s8sKh3V34YzTYIIZpTP5P5qliExhLjkh1WAnZpQPFj8B0Rf-e8su0ZS6fEZodu382_FFvVssltImFIDUibboUukCbpSx8lGZ6G_t0QN1KDe7ks_PYtRkFYTEIE2MmJVdeu6h_GA1KYX7yUdhcGcHCc0VeId4jKSnJBlvdtDv01qY0TgcH30mKyfcjUzaQz4EFePJdHQQ3v6j6CzTtFL_cGMgIYoO_oBMHQfuePi6K8t3k1Ew3XdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=aK4wS3kcujTzhqkMUagDcjUe3OcOn2RFCHoNM4hEP4QtpOGgNsT541sZgqtrOkTdIxWFvO1cNFf63CWAYPlTYwVZryH_UZZH8s8sKh3V34YzTYIIZpTP5P5qliExhLjkh1WAnZpQPFj8B0Rf-e8su0ZS6fEZodu382_FFvVssltImFIDUibboUukCbpSx8lGZ6G_t0QN1KDe7ks_PYtRkFYTEIE2MmJVdeu6h_GA1KYX7yUdhcGcHCc0VeId4jKSnJBlvdtDv01qY0TgcH30mKyfcjUzaQz4EFePJdHQQ3v6j6CzTtFL_cGMgIYoO_oBMHQfuePi6K8t3k1Ew3XdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22937" target="_blank">📅 13:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnHbI6joR2W2fcvHZxnEiqy0izIFm3Pj_r26CMVchUoVXnK5S7AIaL7b4iIzlfcQpljIs3zH1TITNUPVv5sjv_bPYTKnLX2IpG6KRshomezJD5lTpJ8x7cXN5HNmBAPEl5YXwJMI6MiIAK7LYB9aMkczucwKUGOdXtLk2MgOZkCEB1sRWaPRlruyeVKAMogZQOTAiKrug0OyBjyQRgxGmxDaJ3jIprBSj_zD0OWZCu_g_fRp0yW4z5JstRMDxnH0erKottogSK7yQgidXucm5nCasrunNyyyZGATgFk0JFjVO6hHRt6Aoq6NL_JXFPmE3KSkBZZxFKPvCTenSlsJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIfb0ecVi9rGthi5YGKugjUT8f-jMEIAVfCDB2AzNM-2RjHbq3huCUxjdPlcEHL3KgK5iHCGeqz8brzaVyz8b8n7DvLN0BccFJZlcj8-o0ha0FTGubTqTwpGxA1bSuo1e-6gYnp0CRIunKZFK9rhippqpmYfK_SYOerBF5aTdYjEpvvIbRWPF_iBMXE-vlT1EMjcnKUmvMJsxuwTDsX_0tt3kse-vYKShvqttSRU1CfkNDoqt4vZ8WSCZ04SZEwUSdcrOUFtN9Lg8-wcAj_J64sEJXlrhtyTf0GbFLHEaQRlAgPRe-lrbxP-0iDaGUzKcPKttEGquoZw_3GE6JJ-1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22935" target="_blank">📅 12:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نرخ دلار ۲۳۵،۰۰۰ تومان
دلار کف بازار ۲۴۰،۰۰۰ هزار تومان
تتر ۲۳۴،۶۰۰ تومان
بیتکوین ۷۷،۳۰۹ $
انس جهانی طلا ۴،۳۴۷ $(آخرین قیمت)
نفت برنت  ۱۰۴،۶۱$(آخرین قیمت)
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22934" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=LQEOAg1cxVz5SpINb9cWEj-b6EYOHdgTg5fsxtmZGfNS2Tata077mHByhKFSbESx3wLz0KO5DACD0Uf6qXWjc15ieyLzetPyRbr7WOs2yjLshnIQRtSYbfJYMk7rcY_CqbJ6D36IW6oKKTgJuS0RuWJjuMAuQ3b1PsKWHOHoLSuqEDK6M16htQSfeyjSmdoS6ObawsWfE6vbsBcNUAHGKtc0qoHh7YQ5XLejCm7Sb-_ULVGF7PnsRxqxHBxwAVwMhevXMJC1brJjdHoHhTOhNzVVMuzb8PJ70pkD4xeK-1aLvxLgqdb2OP_I4GT1v9MA4_-ZGB7qBUTmPTSlxk6IOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=LQEOAg1cxVz5SpINb9cWEj-b6EYOHdgTg5fsxtmZGfNS2Tata077mHByhKFSbESx3wLz0KO5DACD0Uf6qXWjc15ieyLzetPyRbr7WOs2yjLshnIQRtSYbfJYMk7rcY_CqbJ6D36IW6oKKTgJuS0RuWJjuMAuQ3b1PsKWHOHoLSuqEDK6M16htQSfeyjSmdoS6ObawsWfE6vbsBcNUAHGKtc0qoHh7YQ5XLejCm7Sb-_ULVGF7PnsRxqxHBxwAVwMhevXMJC1brJjdHoHhTOhNzVVMuzb8PJ70pkD4xeK-1aLvxLgqdb2OP_I4GT1v9MA4_-ZGB7qBUTmPTSlxk6IOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بتسالل اسموتریچ، وزیر دارایی اسرائیل:
«اگر جنگ در همان خطوطی به پایان برسد که از آنجا آغاز شده بود،
دشمن چه هزینه‌ای پرداخته است؟
چه چیزی مانع از آن خواهد شد که دوباره وارد جنگ شود؟
کشته‌شدگان برای آنها اهمیتی ندارند. می‌توانید بگویید: «ما
۵۰ هزار تروریست را در غزه کشتیم
»؛ این برای آنها اهمیتی ندارد. آنها مثل ما نیستند که
حرمت و ارزش جان انسان
برایشان اهمیت داشته باشد. از نظر من، اصل اساسی این است:
اگر علیه من جنگی را آغاز کنی، اگر پیروز شوی، دستاوردی به دست می‌آوری؛ اما اگر شکست بخوری، سرزمین از دست می‌دهی.
»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22933" target="_blank">📅 11:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الجزیره: حوثی‌ها مدعی کنترل کامل ساحل دریای سرخ یمن شدند.
گزارش جدید می‌گوید نیروهای حوثی پس از پیشروی سریع در امتداد ساحل و تصرف شهر المخا و جزیره میون، اکنون مدعی
کنترل کامل ساحل دریای سرخ یمن
هستند؛ اقدامی که موقعیت آنها در اطراف باب‌المندب را به شکل قابل‌توجهی تقویت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22932" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه ۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده) همچنین فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22931" target="_blank">📅 11:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با یک رسانه هندی خبر داد که روز دوشنبه توافق عمان و ایران درباره مسیر مشترک تنگه هرمز در حضور وزرای کشورهای عربی حاشیه خلیج‌فارس امضا و به سازمان دریانوردی بین‌المللی اعلام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22930" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرگزرای AFP گزارش داده مذاکرات بعدی میان
اسرائیل و لبنان در رم به ماه اکتبر موکول شده است
. این مذاکرات قرار بود درباره ترتیبات امنیتی و وضعیت نیروهای اسرائیلی در جنوب لبنان انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22929" target="_blank">📅 11:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22928">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه
۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده)
همچنین
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22928" target="_blank">📅 10:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اخطار
⚠️
⚠️</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22927" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=YtgCCk-TMvIM33NfezbVNLe3GwplRttl2DCU7-za9MTioPvQn8Wg4BebmSUlzIQv8h5TiXHjOA_bvt1CdK-7qkw27m_zat7IQoTpeApNWiBRs72RrZNBdN3vSNwGW9oE9xelPCZiPYPP_6t3zYdn_mAkKvQp0qN9GkrSRU6h-ih3Zz-pg7bAiJ6RCVX1w9bLMfRWzav2j4HE8YewE88r2u11EwO8VzqgMeX5n18Vuy7oc5lL8S2XUSQzJ6_IKnVSBGpOTHJpDglZrGbrwyZ_IllDkPYgiMwOZ8JGuO1QyViunD1rdWXCGvmcRGEq1GFV69-jN9PTlvRsHxO4_vRVJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=YtgCCk-TMvIM33NfezbVNLe3GwplRttl2DCU7-za9MTioPvQn8Wg4BebmSUlzIQv8h5TiXHjOA_bvt1CdK-7qkw27m_zat7IQoTpeApNWiBRs72RrZNBdN3vSNwGW9oE9xelPCZiPYPP_6t3zYdn_mAkKvQp0qN9GkrSRU6h-ih3Zz-pg7bAiJ6RCVX1w9bLMfRWzav2j4HE8YewE88r2u11EwO8VzqgMeX5n18Vuy7oc5lL8S2XUSQzJ6_IKnVSBGpOTHJpDglZrGbrwyZ_IllDkPYgiMwOZ8JGuO1QyViunD1rdWXCGvmcRGEq1GFV69-jN9PTlvRsHxO4_vRVJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون درگیری میان
نیروهای نظامی و امنیتی و افراد مسلح ناشناس
در منطقه بخشان سراوان، پس از حدود ۶-۷ ساعت همچنان ادامه دارد. صدای
انفجارهای شدید و تیراندازی سنگین
از محل شنیده می‌شود و نیروهای امنیتی حضور گسترده‌ای در منطقه دارند و مسیرهای منتهی به محل درگیری را کنترل می‌کنند. گزارش‌ها از
انتقال مجروحان و کشته‌شدگان نیروهای نظامی و امنیتی
و استقرار چندین دستگاه آمبولانس در اطراف محل حکایت دارد، اما هنوز آمار دقیق تلفات مشخص نیست. به دلیل ادامه درگیری و محدودیت دسترسی، وضعیت غیرنظامیان و میزان خسارات نیز مشخص نشده و تاکنون مقام‌های نظامی و امنیتی
توضیح رسمی درباره درگیری و تلفات احتمالی
ارائه نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22925" target="_blank">📅 10:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=AX_zSVHLl7crzPFgvyN-lsu0CKZnnax77bMLULXHFza6W_c3jtgxOpFxj6BxrK1XHM47ERPnLncdHovKt8nHW3oWnAvojaZx-lOHmbLpEp_d--Kn6qSHFU_1phZUMxGMXn0K2KgP4C4cvJKy0yUZJWO27G3bsLlcAvJOwJWX5u_SuF-5tqI9UCGcUm6lL0q-tMEMEKzNQNwz6O_qPVdTUAfL-F4hxeJl8XhSTLOepFKMtDko7v3ruq9Yc3t538zWAzhp07IjT63chZ8esUGUCogsxlVDqDQ4hFrB4GWYzIEnW4h848FqovL4vfIhmpw0eZTY9O7wOyhRpISXwt99RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=AX_zSVHLl7crzPFgvyN-lsu0CKZnnax77bMLULXHFza6W_c3jtgxOpFxj6BxrK1XHM47ERPnLncdHovKt8nHW3oWnAvojaZx-lOHmbLpEp_d--Kn6qSHFU_1phZUMxGMXn0K2KgP4C4cvJKy0yUZJWO27G3bsLlcAvJOwJWX5u_SuF-5tqI9UCGcUm6lL0q-tMEMEKzNQNwz6O_qPVdTUAfL-F4hxeJl8XhSTLOepFKMtDko7v3ruq9Yc3t538zWAzhp07IjT63chZ8esUGUCogsxlVDqDQ4hFrB4GWYzIEnW4h848FqovL4vfIhmpw0eZTY9O7wOyhRpISXwt99RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌هایی در شهر سراوان در استان
سیستان و بلوچستان ایران
میان نیروهای امنیتی ایران و اعضای جبهه مبارزان خلق (PFF)، که پیش‌تر با نام جیش‌العدل شناخته می‌شد، رخ داد.
این درگیری‌ها پس از آن آغاز شد که نیروهای ایرانی به یکی از
مخفیگاه‌های این گروه
یورش بردند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22921" target="_blank">📅 10:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فایننشال‌تایمز: آمریکا حفاظت هوایی از نفتکش‌ها در تنگه هرمز را محدود کرده است.
سنتکام با به دستگرفتن کنترل غالب اکنون به نفتکش‌ها اعلام کرده پوشش پدافند هوایی آمریکا در هرمز دیگر به‌صورت شبانه‌روزی ارائه نمی‌شود و کشتی‌ها باید در بازه‌های زمانی مشخص، از جمله حوالی ساعت ۹ صبح، عبور کنند. این تصمیم پس از افزایش حملات شبانه ایران و برای کاهش هزینه و فشار عملیاتی نیروهای آمریکایی گرفته شده است
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22920" target="_blank">📅 10:16 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
