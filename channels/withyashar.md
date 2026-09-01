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
<img src="https://cdn4.telesco.pe/file/vkr3Ud69VSP6xKDWzuSF8BHYM030NUsP3JES7G0OSEqP_Sp0JhE2YN1j_iApSkEgKn03aeoTRLowdy6S0bysCLXHJDHfeYaIHa4E86lATTKZm85cOh4vQO3uw2dfAkouGeMa8D2qJ5vrgAQN39zMjOl3eJq38YNfCje7HR4Gm6RFoiHXVPpklLJv4I9BNy7omAvIKCsOZfWRna_5NsUmCZTGqzPIu9s9PyjvJ6UyCZDwh0yb6f3z_b_qCJFdh6XbQ2SNaMYxR1So7pfAx5cF8qs8Kz-CDHSkV4cI1lJq8Ub4ZLlSW94B9ZPjUVr8JP-s9KJiecwa7f0nOXAyILtroQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-21925">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مرکز فرماندهی مرکزی آمریکا(سنتکام) اعلام کرد که ۸۴ کشتی تجاری را به مسیر دیگری هدایت کرده، سه کشتی را غیرفعال کرده و دو کشتی را بازرسی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/withyashar/21925" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21924">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بسنت گفت : «احتمالاً این هفته در چارچوب کارزار اقتصادی خود علیه ایران تحریم یک بانک را اعلام خواهیم کرد و هفته بعد نیز یک مورد دیگر را اعلام می‌کنیم. ما در حال گفت‌وگو با متحدان خود هستیم؛ همه آنها جلو آمده‌اند و حمایت بسیار خوبی از ما نشان داده‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/withyashar/21924" target="_blank">📅 18:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21923">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که با انجام عملیاتی فریب در غزه، معین محمد عرابید، رئیس دستگاه امنیت عمومی حماس در غزه که مدت زیادی به دنبالیش بودند را زنده گیری و  بازداشت کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/21923" target="_blank">📅 18:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نائب‌رئیس مجلس: باید محاصره آمریکا رو محاصره کنیم
@WarRoom
🥴</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/21922" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbQpaDSpa2oZk3hHUQoE_yWxG7xaS79zu3TPOsidqKSTnCz-eDkpA3FpcVKWNJ7vzQGHvDKVyKxtyyuX10Uukoccp4a6bMG74m7UMB24VS8rHfPfwiRWuknxx3bqCtQ4SxDteoBhXHzf-VO89nH98y3Wn2SWoUAG7V6g1at85tuVFddbYIjFE-Kq9Cp0-CR4Y8kR7LTlB7VW09xDt0Z-u1k4R03C9v3PXZ6u3PF8KHSEUBNjsD9e1igoXKqEw3W4tZIndNcdjjL9HI1r2t2UWWnzkxeNzHRGPXQS8iDxEIEUkqWjkwDNFoQ3u83ql8AKWLmoDBQ94N-oriqtbt0Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط ببین کار این حکومت به کجا رسیده؛ به هوادار خودش هم رحم نمی‌کنه! از بس زیر فشار و تحریم به خاک سیاه نشسته، با اسم رهبر مرده‌شون هم از جیب همین عرزشی‌ها پول درمیارن. طرف هنوز نفهمیده چی شده، اینا دارن جیب خودش رو می‌زنن
@WarRoom</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/21921" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتانیاهو: راهبران ایرانی می‌خواهند من در انتخابات شکست بخورم؛ و حزب‌الله و حماس نیز همین را می‌خواهند؛ و ترکیه، البته، همینطور. آن‌ها این را صریحاً می‌گویند. از خودتان صادقانه بپرسید: چه کسانی می‌خواهند در این انتخابات پیروز شوند؟ من می‌توانم به شما بگویم، آن‌ها نمی‌خواهند من پیروز شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/21920" target="_blank">📅 17:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/21919" target="_blank">📅 17:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک هم میهن زد نامجو رو تا شیشه جمع کرد @WarRoom</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/21918" target="_blank">📅 17:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba29001cd.mp4?token=qBVAVOaeoLGjnpeNbxUcg5O9wJrXVEZLsPLsA3x7iqIjwygR_swS5mK4xLz4LNNIzkweXneEt05oUz9uMSrw9aLfvHpgcj9CTjzZxXBkxDt5yoUlXEeTR-8H1zUUscn3AYfCSgSQVFbxI7ktJBCttx84V8raHi0nZFaMvYpv79bnxjtXbkdFERmmveMtZSJaPkm5xSEkWo93WrVxuV9mP9OX9uDaDKmsfTsWrTmaOb4emVwJONx3aGh_ehLmiy-SYVo4ZjfMpq2DZl0_wUCRt5UMpL9r64Y_A-t2J7PbgBxCusrleq6lwxCNQSx0OsFprV0tZanHa2U4HXIx0iARPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba29001cd.mp4?token=qBVAVOaeoLGjnpeNbxUcg5O9wJrXVEZLsPLsA3x7iqIjwygR_swS5mK4xLz4LNNIzkweXneEt05oUz9uMSrw9aLfvHpgcj9CTjzZxXBkxDt5yoUlXEeTR-8H1zUUscn3AYfCSgSQVFbxI7ktJBCttx84V8raHi0nZFaMvYpv79bnxjtXbkdFERmmveMtZSJaPkm5xSEkWo93WrVxuV9mP9OX9uDaDKmsfTsWrTmaOb4emVwJONx3aGh_ehLmiy-SYVo4ZjfMpq2DZl0_wUCRt5UMpL9r64Y_A-t2J7PbgBxCusrleq6lwxCNQSx0OsFprV0tZanHa2U4HXIx0iARPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هم میهن زد نامجو رو تا شیشه جمع کرد
@WarRoom</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/21917" target="_blank">📅 17:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نرخ دلار ۲۱۴،۴۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۹-۲۱۶ هزار تومان
تتر ۲۱۱،۶۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۸۳۹ $
انس جهانی طلا ۴،۳۵۲ $(آخرین قیمت)
نفت برنت  ۹۲.۷۲$
@WarRoom
۵ عصر تهران</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/21916" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skgVsUSdLjAwjxjjKihOS5e4HPBd4zmqCuYnF_wxM8e2bY58gzjsDMVv4EEqE8wAvQJ0buSflPIBY5Oi_8LYZLRjb3dUUqatp_pbdlsj8i80hjZFZ2cueJnQZx1FNkrm2-mf1rI6ijkWeXh8OsxJHRiTdUzncbgynhYM-ZLTZ6PrZyr3tqNAsZey7yRPvGwFyClc67Qz2yDtWLlyVcRZUxklevFWJqDSfivlBuxi1LugEBB4u-RyDojahHJzixLd0urlXkyKXeOMJeSfLScp0H5hyNqhKPLFveLGiqI9QCq3vSD8J9HmF3nNrXDUIdOT4kwOa3DDWmWSgpA61tfVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون منطقه دقیقا مانند قبل جنگ ۴۰ روزه شلوغ شده پهپاد و سوخترسان زیاد!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/21915" target="_blank">📅 16:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21913">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4002634599.mp4?token=H57setBkaT1SlNb8twkgeZm3Y822OX0PKV21PKtM77wXtwEDecXs8t7TwbdJ9zZyPqDFzfbKbE-_5WWmPA0-b0uwvF1dRtN4m232UDwj32_Qv1Bf_6FK27uZMoVs4P6qJdowt_8G1cOpLvMUz0qutWn3grNRsvxEOkewfm1CLkqTc_o3hSCT7RR4x4lvvwkXNt4q8FtcEloFC2R70TmTMao53w6rDmny97ttPmr_hN1TYyJuH3JrvBiivgkROgiJnmKujBPc9zne-t3tzxEyZLdP0ITZYjs1p8gnVIp3_PKL3sob0akZ74LZE6nsbDRiX8RyRB7kjcKPPaO7NAKNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4002634599.mp4?token=H57setBkaT1SlNb8twkgeZm3Y822OX0PKV21PKtM77wXtwEDecXs8t7TwbdJ9zZyPqDFzfbKbE-_5WWmPA0-b0uwvF1dRtN4m232UDwj32_Qv1Bf_6FK27uZMoVs4P6qJdowt_8G1cOpLvMUz0qutWn3grNRsvxEOkewfm1CLkqTc_o3hSCT7RR4x4lvvwkXNt4q8FtcEloFC2R70TmTMao53w6rDmny97ttPmr_hN1TYyJuH3JrvBiivgkROgiJnmKujBPc9zne-t3tzxEyZLdP0ITZYjs1p8gnVIp3_PKL3sob0akZ74LZE6nsbDRiX8RyRB7kjcKPPaO7NAKNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال دست‌کم ۱۵ دستگاه تانک و خودروی زرهی با استفاده از کشنده‌های تریلی در شهرستان بمپور , بر اساس مشاهدات موجود، این تجهیزات زرهی در مسیر ایرانشهر به سمت چابهار در حال انتقال بوده‌اند.
‏این انتقال در حالی صورت گرفته که پیشتر نیز گزارش‌هایی از انتقال تجهیزات زرهی به سمت چابهار منتشر شده بود. بر اساس تصاویر و گزارش‌های پیشین، دست‌کم هشت دستگاه تانک و خودروی زرهی نیز در مقطعی از زاهدان به سمت چابهار منتقل شده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/21913" target="_blank">📅 16:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21912">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حتما. اگه از طریق تلگرام با من آشنا شدید حتما پیج اینستاگرام رو هم فالو داشته باشید. یک سری مطالب فقط مخصوص اینستاگرام است و یک سری مطالب فقط اینجا مخصوص تلگرام.
instagram.com/Yashar
(پیج اصلی)
instagram.com/YasharMotors
(پیج پشتیبان)</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/21912" target="_blank">📅 15:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21911">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXmsU7pi3fiSpX3jjmAVlf1lph8llo980xuKdDc_-uHNYJ2fY-GzoFebv1xYA-j6YLjedFQpScL1S6hM4wR3dhu1pGveAgGrrsgWaJTlfGGkyf4FdCv6kce8lKOEESharNhF6kKpEdvGyi36oo-OFPMI1DGzpW-DPhP1-OwiFrPJZJISJPSdLupyYec7G3oibjW68pAhdKiFt-Am41Rafq4eC4vVoGdXNnbeMe4mKiNeBGBEj366dvhS1bTX216V01-R22N2x7Y3gtuhMjSDMrJfNynlCuF1XVeinsvOPDCF5AE020gTBiz3uDfcMLKevn6acZOxy4lrn87X-wa2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان و  پوتین در حاشیه اجلاس سازمان همکاری شانگهای
@WarRoom</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/21911" target="_blank">📅 15:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21910">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501b5e7e6b.mp4?token=GbCsw1EMbZ8qbNjWvjq6wSaHwhM0eTTMEiWuuUKWbn-ehM82qREKhHknJRXWH44nWohrcjOrwvYu8jh8Lx0yKmk2CN0FGCewtVlNvUL4tOgqoZyv3Z2MOPIBrjVsm_gniEPoW7tBvboUg32P7SLMNCyWmbe5fok4a_KKqyNTw2klUWNJRlaTdBVNsiwc258yCutcelIC5VYQqRIPVAkZUvqYC-Qu1jHwO4gXJIxnJf8d-SBx1azPYQ2nhAC0uN2kOlrj-rFhJQzoF6bC6LDtd75Za4sVAWklXs9ya2NgQD4OKO-m_1tbpooaHNXRRmiv3w7RTQA0dL2bapFKa8OXUqCxJBioCiYxzRJ3ZtNsoVQ5OO2zVlU6EPsxYg0wb-BCmn9U_MBBUBgYKqXvOwlbddHPJAv80YRSitoYcqzaxCEuTghuBFQe8yEUYR4uGobQkVDT_RISsDchSdmvsaZl5pkFQSGHqv6Y7L5pJ6M2k_F04RKnlEHrX4xqSQOGreEnuz8MTKxnyvx3XEanRHzhxGGUpvnrXnTsIeLTR_vOnj7gPXACOQml2n5T9G5sXw4vpuyJr97F6VBYCE8TOXzMMGzq7vNz17qRTgHpTNK6zhPge83M9BzEFBvv2_KJhPXdjiHM8xR8TjDgi5-KV3ANSbhV4jpcXsg695we-TMh-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501b5e7e6b.mp4?token=GbCsw1EMbZ8qbNjWvjq6wSaHwhM0eTTMEiWuuUKWbn-ehM82qREKhHknJRXWH44nWohrcjOrwvYu8jh8Lx0yKmk2CN0FGCewtVlNvUL4tOgqoZyv3Z2MOPIBrjVsm_gniEPoW7tBvboUg32P7SLMNCyWmbe5fok4a_KKqyNTw2klUWNJRlaTdBVNsiwc258yCutcelIC5VYQqRIPVAkZUvqYC-Qu1jHwO4gXJIxnJf8d-SBx1azPYQ2nhAC0uN2kOlrj-rFhJQzoF6bC6LDtd75Za4sVAWklXs9ya2NgQD4OKO-m_1tbpooaHNXRRmiv3w7RTQA0dL2bapFKa8OXUqCxJBioCiYxzRJ3ZtNsoVQ5OO2zVlU6EPsxYg0wb-BCmn9U_MBBUBgYKqXvOwlbddHPJAv80YRSitoYcqzaxCEuTghuBFQe8yEUYR4uGobQkVDT_RISsDchSdmvsaZl5pkFQSGHqv6Y7L5pJ6M2k_F04RKnlEHrX4xqSQOGreEnuz8MTKxnyvx3XEanRHzhxGGUpvnrXnTsIeLTR_vOnj7gPXACOQml2n5T9G5sXw4vpuyJr97F6VBYCE8TOXzMMGzq7vNz17qRTgHpTNK6zhPge83M9BzEFBvv2_KJhPXdjiHM8xR8TjDgi5-KV3ANSbhV4jpcXsg695we-TMh-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زندگی ملانیا و آشنایی با ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/21910" target="_blank">📅 15:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21909">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دیدبان اتاق جنگ : هم اکنون پرتاب موشک از محدوده شیراز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/21909" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21908">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/21908" target="_blank">📅 15:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21907">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الجزیره: حکومت ایران می‌گوید به مقاومت در برابر حملات و فشارهای آمریکا ادامه خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/21907" target="_blank">📅 14:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21906">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">«دادن استخوانی به سگی ، نیکوکاری نیست؛ نیکوکاری، تقسیم غذایت با اوست، وقتی تو نیز چون او گرسنه باشی.»
جک لندن
یاشار :
کمک واقعی زمانی ارزش اخلاقی دارد که برای کمک‌کننده هم هزینه داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/21906" target="_blank">📅 14:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21905">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سعید لیلاز، روزنامه‌نگار و تحلیلگر اقتصادی و از چهره‌های جریان اصلاح‌طلب :  «مردم می‌دانند  خر ما اگر از پل گذشت ؛  برمیگردیم به تنظیمات کارخانه»
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/21905" target="_blank">📅 14:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21904">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0mV1j03mcMezdLFLiyiVIKBbmWlGHWmqMe4Z7G2rPPK5lgXR0w6UrfyWJUFwdnQnf5xCSC8i3f4BSIS6bDGHI08Q28xqw4U20jzgMt6T4wTxqc4eYPFUnphYMgUYgPd3pNtUNM4mLNOXT3ilJDuvk6vgZFVwulbUzLq1gD20PpI2ZAVateKTUWWFsXVT5vjXG3uefp6pbpNR8hKO60mqMOc-5BjiCxY7056vCJF5PMOTlaxHgi2_KNjMaQlF84oCRnMqpYVVcmrcNs1_TXhVkhfMafknIhFLBnqZcmwOZ1F_lwocEdvkOJBm968FwOYy7cAU2dBffyj-2c3Di5Qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث بازنشر خبر : ترامپ قصد داره بعد از اولین درگیری و تبادل آتش با ایران توی چند هفته اخیر، قراره یه ضربه «سخت» به ایران بزنه
@WarRoom</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/21904" target="_blank">📅 14:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21903">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فاکس نیوز از قول ترامپ : هرمز در «وضعیت بسیار خوبی» قرار دارد. پول ایران در حال فروپاشی است. تورم ۶۶٪ است.
«این بدان معنا نیست که ما آنها را نخواهیم زد.»
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/21903" target="_blank">📅 14:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21902">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسرائیل غزه رو داره شخمی میکوبه و چپ و راست هم زده گویا یه سمت و زده برای فریب و تروریستا به سمت دیگه رفتن که تله اصلی بوده و پوکوندتشون @WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/21902" target="_blank">📅 13:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21901">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نبویان: اکنون بهترین زمان برای حمله پیش‌دستانه به منافع آمریکا است
با توجه به کمبود ذخایر جنگی دشمن، افزایش قیمت سوخت و نزدیکی انتخابات کنگره آمریکا، دشمن به دنبال کاهش تنش است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/21901" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو
:
نزدیک به ۴۰ سال است که با مسئله ایران درگیر بوده‌ام. زمان زیادی طول کشید تا نهادهای امنیتی اسرائیل را متقاعد کنم که مستقیماً با خودِ ایران مقابله کنند. همچنین زمان زیادی طول کشید تا ایالات متحده را به این درک برسانم. توانستم این کار را انجام دهم، چون نزدیک به هزار ساعت در شبکه‌های تلویزیونی آمریکا حضور پیدا کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/21900" target="_blank">📅 13:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seU7axR5Vwtb6PrwQwFVvLUT6w1uohnVHbGb9PCJPLXHtNgjK7CgnYXng3Yk5r_ouzK2UtKWwtIAYUjlHAKp2cDOWvrtdJ_U4yfV3iVeWA88pREcFtEVynXOYO8b1TazQ97jhx2k0TQwAWky7Ji9opR8OwU6g4nOlJBawNY6L3JYr-umhJDN8xD44-37op2SIL10wiPezL8HE8TnQPvzMyf8BhS9xvQ0cLKl7AnkFOSot6yftVIlxH9OnVtQcKvBo4mPlZs4Xj-tMQGrUDqH9w7KanZDcqjq447LPRnaxKyAuZu8oaYo2l7xRwMjUl0Z-ylbhL5iFUsIo72ag9ZKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج دوم شاهزاده (دفتر شاهزاده) از دسترس خارج شد
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/21899" target="_blank">📅 13:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUUFyUby_Xh7afWUei9yWcss8J0j8YPfauRj8dgNNd_Zvtj7fiaBO3q4pB0Ir-HfTkjhKedAnboQftt_3V4IiwU3HJrSA34JrpDwskkyhB6vPugrlKhe6BHZGNn8xVuRjM5NBbkp6JQAC-mCC4-eAG3rf3cWi7-kyZz9uwHQWsOT0CAFBkAdy_chdSuat9WXv9Z3LsVKUGsvdcHQ-lQbP0pJPAkA8kPfKtkx7jvB9xEdTsxIk3dDAJ6lf0QFjWWguFxAXQ1KT57O9JM6AqW0QflC0PiWdwC6gzwNOSVOjTQcLUcrsZchpVB-ZnW4AzzBVcHlOgqvWo-Q3KvwOJi1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن مخوف B-1 ارتش ایالات متحده در نزدیکی سنت ایوز، بریتانیا، در حال پرواز ناگهان مشاهده شد که احتمالاً در حال انجام مأموریتی مانند بازدارندگی استراتژیک، حمله دوربرد یا آموزش است، ثبت و علامت تماس این هواپیما نشان دهنده یک عملیات رسمی نیروی هوایی ایالات متحده است که بر آمادگی استراتژیک یا عملیاتی در یک منطقه حساس تأکید دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21898" target="_blank">📅 12:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5xg8UOMvwJVU_WGE6DFJCkWTTx1wfavey1IHcgu8BSbkWSM92pbWEzdfvDAZ3kcaJi_wKWJUcXDIxsNqkVw9FA8WFXBjUPDzaljvVJWgu1YBihyIokuSUYn-0h1FWp6F3ox4yiWrvHlsPzi-n5og0Nuox6HN0a2VHNIvh-0BzHy4lTXE1ZPIKucV_o9AIftWcb97MjFEvWwlkuLenuDZnHYmnKM3jSz2Z3SEjhBH8r5mUzcyorgg75z9MLUdVpbWmAt1m2nkB7bAXURG-qJNRT-Wst_7e7ZltGnH5iyXYRsTKNcMx9EhSpFG0ciwuM2X2_-zbnlCuLTA9fxDqTeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
یک هواپیمای باری روسی Il-76TD که از نووسیبیرسک پرواز کرده بود، لحظاتی پیش در بوشهر ایران فرود آمد. (RA-76834، با توقف در یکاترینبورگ برای سوخت‌گیری)
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/21897" target="_blank">📅 12:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21896">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتاق جنگ با یاشار : امروز یکم سپتامبر مصادف با دهم شهریور اکثر دانش‌آموزان جهان سال تحصیلی جدید را آغاز کرده‌اند ولی در ایران
وزیر علوم اعلام کرد آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود
، در نتیجه اول مهر هم حتی نیست ، این در صورتی است که گزارشهای بسیاری از انبار کردن مهمات و تجهیزات نظامی در مدارس حاکی است ، در نتیجه جابهجایی آنها برای رژیم در این شرایط جنگی نه ممکن است و نه صلاح، چون جایی بهتر هم برای پنهان کردن آنها ندارند که
سپر انسانی
هم باشد ! حتی کلانتریهایی هم که در جنگ هدف قرار گرفتند اکثراً یک دکه در کنارش زده‌اند و در آن کار اربابرجو را انجام میدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/21896" target="_blank">📅 12:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21895">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArmin N</strong></div>
<div class="tg-text">سلام یاشار جان لطفا از کلمه زارتان زورتان استفاده کن برکت برمیگرده به جنگ</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/21895" target="_blank">📅 12:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21894">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نرخ دلار ۲۱۲،۵۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۴-۲۱۷ هزار تومان
تتر ۲۰۹،۴۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۹۱۶ $
انس جهانی طلا ۴،۳۷۸ $(آخرین قیمت)
نفت برنت  ۹۲،۱۴$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/21894" target="_blank">📅 12:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اسرائیل غزه رو داره شخمی میکوبه و چپ و راست هم زده گویا یه سمت و زده برای فریب و تروریستا به سمت دیگه رفتن که تله اصلی بوده و پوکوندتشون
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/21892" target="_blank">📅 11:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYOqONWtbFXeaST3D8L2RoMgPJr822mF83qqMxW2_pPXabPPgQZ5NiiWyM4GhEVQdTO9OG-uoK-Fo2Yum5MkAn3IWAcZe764S8zfvcTOjxXg4hADQWNgFMXMxF28tbW2Rj8d_G54nysV2KclnmhwNEuF0ovOrL3TED_N2I4OP1sy2bNJeFD09cTVI7FqXsxapFkE5sC3nKylFNeEeQAIUspgm6vF8fbX1bktBcGDjkLYN_WWuzX8IU-0k4QjHrfwqKg2uX0UVGZPLqLHYHjCkE7qFJVN_MNJAMy4SwgYKhpiDJ24Z87UIrhNOpvfrmnupc3tumjg7qrfAgzRBEoXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار از شنیده شدن صدای انفجار شدید در اصفهان،در این عکس ارسالی دیدبان اتاق جنگ ستون دود قابل مشاهده است، علت:نامشحص
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21891" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21888">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOqoJ58zOemMsoLd3blZ1toBj_W5dKrjb9rYxSOrJSBOB3xHZXSOmX3t2e3al9lSfgI4F57_BePfatrW1IrI7_GbYgJo-KD6fNBYivGpynuMQhWH3NcBukXlZXJW6uaDGUanndgf3cc7ahChFeyec7R5BnyCrhNs9PB2geh_0ECQ1un_fs0JdANoiH8O1PzSEt1swoL-YJwlf4SgaX9QrZ6aEwz5sNj1oaVecfZps_ZWLOa-KoGCNVPmWSIBOrYttllag9o0AHhwbi75DfXb9pEu0Xm0MPk-Xkf0Iirc5TDOpfwQBLqiw1pe9-oxHEixzrDBQP8Td1xVW-c_S6HBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSVQpkc8lJm0u-WPa5DRBupeYmOtXOF6FB7c6NocxAXmUkHFbisagQph3gprgiOPWlliSA2d0e8haslQGRit9P2QW2eCz5uU4DNpgP0prphH1b4FvAZqG5lRayWFy5Qmx5FH4FS_7bLuFZY1yk0lFRG3nOgjWfrwkOilAan00x8-_pS6W4gC7ocDM7LGFuJfizaZ6hO0ptm2VwWdTcp89LawKA-1uJBV9F7lk6zrmH2D6SN4ahLwip1ljZIQoRtm2sIU7kKKfqbu17A60vkOzmupaN72uj_p6NaJID-mC6HsZE426szWWTb_nE_PWwNjdwDCgm5Kl2Wf1HfDKEjz9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک پهپاد MQ-4C Triton برای جاسوسی، نظارت و شناسایی (ISR) متعلق به نیروی دریایی ایالات متحده در حال انجام ماموریت‌های خود بر فراز خلیج فارس است.
ابتدا از شمال غرب عربستان سعودی به پرواز در آمد روی اردن رفت و بعد به خلیج فارس آمد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21888" target="_blank">📅 10:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c9e33af0.mp4?token=OYqwsgiokX3ySsVWsbM-L0yoWWtptMDDXeFLg1aUXN0AKTaZPi1gD6jho-8GUXY-JO131q-5qfdMNvGC826DSBLoW89oX5jfu0iGC-bFPjAbzw1buDLpxRca_BLsbp3rq9udkimptSNQSANswsli_C_KodMv4CMGAaAapionMqhZKvC92XT7qpjKhPey3LZ5EwDTddnUw4It32JRmL9gscBo7vFFPoQuFcYVm12_qh98tgrAFTYRs796arBQ1rQZtmmaipesqG2pl--emiOhWA-8OOtk14a_sranPuNgKQWqoTVQ164Owy4i3MYQEReHff7OtNQ6o1FUeYXfMT2Chw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c9e33af0.mp4?token=OYqwsgiokX3ySsVWsbM-L0yoWWtptMDDXeFLg1aUXN0AKTaZPi1gD6jho-8GUXY-JO131q-5qfdMNvGC826DSBLoW89oX5jfu0iGC-bFPjAbzw1buDLpxRca_BLsbp3rq9udkimptSNQSANswsli_C_KodMv4CMGAaAapionMqhZKvC92XT7qpjKhPey3LZ5EwDTddnUw4It32JRmL9gscBo7vFFPoQuFcYVm12_qh98tgrAFTYRs796arBQ1rQZtmmaipesqG2pl--emiOhWA-8OOtk14a_sranPuNgKQWqoTVQ164Owy4i3MYQEReHff7OtNQ6o1FUeYXfMT2Chw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : ناو جورج واشنگتن در خاورمیانه در حال عملیات است
صدها ملوان نیروی دریایی ایالات متحده برای اجرای روان عملیات پروازی بر روی ناو هواپیمابر یواس‌اس جورج واشنگتن (CVN 73) لازم است. از تعمیرکاران گرفته تا مرکز کنترل ترافیک هوایی، هر ملوان نقش حیاتی ایفا می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21887" target="_blank">📅 09:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W14tokBv5wL3FsZIg0M7CVsgHUS8OW8gMpktd272AHw3e8UgRN9JOstHHYXzbPbDBJ3NS5KvZfThw4JnpceGMWCEiS1EyFgD2x8sr6uinxgTsw-RrEePnDu4flrIn50kunWm-wvXETJ88tE9VtelpBHws9HQ58B1PCFS81h5LAFHhIs3AzJvhVB0I_CkxGSgRkZlM8DDNI1gN28l3LCBDeJOdPwne77Y30C2d47yn5ocfeHs4Zz1fVkQ6BkfYyDUKqmZxKcosRVA08WAzYIS342AO-SzmjeoiUrFGlMfzzYUeR-ky5fSa6PR6UfQJvXfmnA-U4_pm_wSwPUpOo9iXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21886" target="_blank">📅 08:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی کاخ سفید، در پاسخ به پیگیری سی‌بی‌اس نیوز، گزارش‌ها درباره استعفای دن دریسکول، وزیر ارتش آمریکا (چهره بسیار نزدیک به جی‌دی‌ونس)، از سمت خود را تایید کرد. این استعفا پس از ماه‌ها درگیری وی با پیت هگست، وزیر جنگ آمریکا، صورت می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21885" target="_blank">📅 02:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd32f538c.mp4?token=OcfaFrTsGWl9iv6397BTcytC1EquyWdVr9_-_TgH5dkeYvn_dErZXQA1KYVVHN_1OAAq5K4v4hB7lYR9S0o5ji-IxHqHj8XtjDkJ6smI9YK-UYGRJgu8RS3NiBenZOFkuvFtxcOs1AynMNbnFCFvTkRAFjZhrohxEws-lRfarsTR-CbaxWM6l6sGIs6Fq_672fJ9qngBVxoPYJtC6L2MnqV97s3Y0Fmw2C4lfIr7OpXZxIpaZqAONbqtcUO5OFmKNz08N_QsxU5-YO7Xx44meBmUla4JXhQEvg1ZTVgatj3KrlqirUk2dv8sieEoRXaLsOy8cgXgcauX05TBa4UHRYQCQJEcpi66nusRYAHraMl3s7hPZAkCE0N_fb8QZLR4l2sJiTPSJlvqZEpy_AsCmv-r8IVDSepiTNHbKjwbb5yvVivCpsYpjf7qfTtLhrvv5Vf4os3NIi9R4oAEQXFnQH6R-oi5XG6i3-Z6JRfmuYr1yPbGsPLCT7XAaw754h7VrKrDKDf4tEfcSeg_UAhK4LSGVo8jZgPWieeJCXP1Ym0sNtFrg5N3STZL2vVd3qHSn9xb7WDQbTjw-qBLNGG_znizuCuXX71X1Ved8R9ShphlP9aJwY5OJsQr7aVbeshuBz1djrlExBBfbIUnfiQxu-tQZHJBNl0LuH-gvg5OxUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd32f538c.mp4?token=OcfaFrTsGWl9iv6397BTcytC1EquyWdVr9_-_TgH5dkeYvn_dErZXQA1KYVVHN_1OAAq5K4v4hB7lYR9S0o5ji-IxHqHj8XtjDkJ6smI9YK-UYGRJgu8RS3NiBenZOFkuvFtxcOs1AynMNbnFCFvTkRAFjZhrohxEws-lRfarsTR-CbaxWM6l6sGIs6Fq_672fJ9qngBVxoPYJtC6L2MnqV97s3Y0Fmw2C4lfIr7OpXZxIpaZqAONbqtcUO5OFmKNz08N_QsxU5-YO7Xx44meBmUla4JXhQEvg1ZTVgatj3KrlqirUk2dv8sieEoRXaLsOy8cgXgcauX05TBa4UHRYQCQJEcpi66nusRYAHraMl3s7hPZAkCE0N_fb8QZLR4l2sJiTPSJlvqZEpy_AsCmv-r8IVDSepiTNHbKjwbb5yvVivCpsYpjf7qfTtLhrvv5Vf4os3NIi9R4oAEQXFnQH6R-oi5XG6i3-Z6JRfmuYr1yPbGsPLCT7XAaw754h7VrKrDKDf4tEfcSeg_UAhK4LSGVo8jZgPWieeJCXP1Ym0sNtFrg5N3STZL2vVd3qHSn9xb7WDQbTjw-qBLNGG_znizuCuXX71X1Ved8R9ShphlP9aJwY5OJsQr7aVbeshuBz1djrlExBBfbIUnfiQxu-tQZHJBNl0LuH-gvg5OxUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳ قانون پیروزی ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21884" target="_blank">📅 01:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش انفجار/پرتاب ‌جدید از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21883" target="_blank">📅 01:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خیلی گزارش اومده صدای انفجار سیریک ، فک نکنم اینبار شلیک باشه فک کنم زدن…
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/21882" target="_blank">📅 01:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/21881" target="_blank">📅 00:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مایک جانسون، رئیس مجلس نمایندگان آمریکا، درباره ایران: نمی‌توانیم بدون اینکه این موضوع به طور کامل حل شود، آنجا را ترک کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/21880" target="_blank">📅 00:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21879">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه‌های اسرائیلی: قالیباف و عراقچی با ایالات متحده تماس گرفتند تا سطح تنش‌ها کاهش یابد
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/21879" target="_blank">📅 00:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21878">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ادعای خبرگزاری نیوزویک : ایالات متحده قصد دارد یک کارزار رزمی ۱۰روزه محدود علیه ایران در جهت استهلاک هرچه بیشتر اقتصاد این کشور انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/21878" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21877">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">العربیه: شبه‌نظامیان حوثی با دو موشک بالستیک به شمال بندر المخا حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/21877" target="_blank">📅 00:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21876">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق جنگ با یاشار : کاوری که با عنوان «اکونومیست ۲۰۲۷» در شبکه‌های اجتماعی منتشر شده، فیک است. این تصویر تاکنون به‌عنوان جلد رسمی از سوی اکونومیست منتشر نشده است. مراسم معرفی
The World Ahead 2027
قرار است پنج‌شنبه ۳ دسامبر ۲۰۲۶، برابر با ۱۲ آذر ۱۴۰۵، با حضور تام استندج، ویراستار این مجموعه، برگزار شود. بنابراین تصویر منتشرشده پیش از رونمایی رسمی، اعتبار ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/21876" target="_blank">📅 00:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21874" target="_blank">📅 00:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کل یزد دایرکت دادن که از یزد موشک زدن الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/21873" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار شرق بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/21872" target="_blank">📅 00:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4261e93c.mp4?token=sES4dFdlDlWELR7X6BRRZG8vNn9OendF4pfw5Ls26u7noCjklR3ArJnbwD-k-zzOxTjC-Nqd5fOiLjd4OtzU7vrPDSHuoMdVrZy99jEBr6cgGyn9NXJp1WHiS1qxJBBqMyh2ewJgNeGCRzd8bywg_Z5fS1KCHs3Mqr7tNto5UZG74wK1Kfh9qoGnenuUmSvamUzVQe-GiF-4v4KMQQ-qNGU9VbV7aXfJbfXCuc-0NybZMhXI3NB9OEe0elw949wey7yAibphrbEgfplL85yvckD5hpVmAaWA3Ou6oFVBADk4nsXWpiNMP-l6n3GWL-3Z308_e_rgeqPVuenlMv9k4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4261e93c.mp4?token=sES4dFdlDlWELR7X6BRRZG8vNn9OendF4pfw5Ls26u7noCjklR3ArJnbwD-k-zzOxTjC-Nqd5fOiLjd4OtzU7vrPDSHuoMdVrZy99jEBr6cgGyn9NXJp1WHiS1qxJBBqMyh2ewJgNeGCRzd8bywg_Z5fS1KCHs3Mqr7tNto5UZG74wK1Kfh9qoGnenuUmSvamUzVQe-GiF-4v4KMQQ-qNGU9VbV7aXfJbfXCuc-0NybZMhXI3NB9OEe0elw949wey7yAibphrbEgfplL85yvckD5hpVmAaWA3Ou6oFVBADk4nsXWpiNMP-l6n3GWL-3Z308_e_rgeqPVuenlMv9k4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گزارش شده است که چندین فرمانده ارشد نظامی به وزیر دفاع، هگست، گفته‌اند ادامه یک عملیات گسترده و طولانی‌مدت در ایران، توانایی ما برای مقابله با تهدیدها در نقاط دیگر، از جمله در داخل خاک آمریکا، را تضعیف می‌کند…
ترامپ: ما هیچ هدف دیگری در ذهن نداریم. هیچ‌کس دیگری آن‌قدر دیوانه نیست که چنین کاری انجام دهد. ما در سراسر جهان مهمات بسیار زیادی داریم و اگر بخواهیم، همیشه می‌توانیم از آنها استفاده کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/21871" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ : همه گفتن نهههه ولی من کردممم
@WarRoom
😂</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21870" target="_blank">📅 23:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9uzJNdmTIll8e9ylqE46WrcLu2j6zZFHeOrBJfg37Z-GvMLiB94X4XDcFVGyrwE90My-U1Rf7bTtdWJSX8dNB5sTUcvOIbqN1UQ4Hf9kywj1FKAB1mIMMYO7uROjqCYGgN7C7SusDMR-twznofUC7GODZ3KX0Q7JguH7FNaSTfxXGlKZs0a9xaKg24fEmFuVDMBFKccGd3nmsnpXXUZfX1GUuzZBeBkkmfdFNsoqJTg5amDVpNOKnhF2ud7gDXdJBMQXFSSvLp9zWHZ-QCLKrm-ybFFbuLBU7aRklfoHRheThahC1G-Aoc7ZoFVFG36nI6jQD4GIwTjr2zBzKqJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا : اعلام می‌کند که گزارشی از «حادثه‌ای شامل یک نفتکش و نیروهای نظامی» در اقیانوس هند، شرق عمان دریافت کرده است.
یاشار : اطلاعات و مکان بیشتر با ورود نیروی دریایی ایالات متحده به یک کشتی مطابقت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21869" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253924d72.mp4?token=asRbvfw8DkAyAlz6c5VRzPTUKkb1_XwbXV7MHQ06zaeMiQAibMjEOlKoovOOmH3fH_eaJMKS1r7AHe7gakIF-W8iWp5VBll3itrB2p8ydAKy8Yf1I6lrLCtJYyPrj3EsqFmlcUQvLB9CUyi9q-m36rzQbK1TBXINYiBW54tcoce_j2NT8ev0LiJn-7KQmK_RfCg4ICWsTAN5GhYtZ2CoKUdIvuhfo4jbLE6W5k3tE3DlF8ilGqZ2SAFDx5owpeObHKdu9u6EiixzE09W8whrvZNtP2GkkD5FMYopuid7oF0pGYzYpnh17U11n9_YOOt7s33oybaNNVpi7au4xDOILw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253924d72.mp4?token=asRbvfw8DkAyAlz6c5VRzPTUKkb1_XwbXV7MHQ06zaeMiQAibMjEOlKoovOOmH3fH_eaJMKS1r7AHe7gakIF-W8iWp5VBll3itrB2p8ydAKy8Yf1I6lrLCtJYyPrj3EsqFmlcUQvLB9CUyi9q-m36rzQbK1TBXINYiBW54tcoce_j2NT8ev0LiJn-7KQmK_RfCg4ICWsTAN5GhYtZ2CoKUdIvuhfo4jbLE6W5k3tE3DlF8ilGqZ2SAFDx5owpeObHKdu9u6EiixzE09W8whrvZNtP2GkkD5FMYopuid7oF0pGYzYpnh17U11n9_YOOt7s33oybaNNVpi7au4xDOILw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی کرده‌اید؟
ترامپ: من هیچ‌وقت چنین چیزی را نمی‌گویم، اما پاسخ بله است.
دلیلی برای این کار وجود ندارد. چه سؤال احمقانه‌ای. آنها کاملاً شکست خورده‌اند.
من آنها را شکست داده‌ام، بعد باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سؤال احمقانه‌ای.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21868" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ae0a3f9f.mp4?token=fQgDhRtl_CtSeWxrf1IQLi-QG6zPbJ_h09gpFsA2sVvu9sc3d1os7PMeaQqevH8PfdE1Bz_SViuWwoxX3rcnceYBjVzf50J-qwnnQMUGtLWlX6mDPGaXPnog4Re5m8A7MQ4ZFvrK2Rc1Y-4zvPRi5zCQ-48GCWH2JTO-prrMM7e9hYXovKRLMb2w7ln1ReSvC3SminwfYI36vU1uAhI4NAwPmnM2NNiJfzvPchYCHtuYrYdZKyhdH-H2CNxHfT2qwYCeHgUw4LJ50dSDysg7icSQjoCmEXq_I3GcDmgkMwZ2yTfyJYfqyGQgx4K4xluReVc1qnJBvvp3bYFrDhFSxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ae0a3f9f.mp4?token=fQgDhRtl_CtSeWxrf1IQLi-QG6zPbJ_h09gpFsA2sVvu9sc3d1os7PMeaQqevH8PfdE1Bz_SViuWwoxX3rcnceYBjVzf50J-qwnnQMUGtLWlX6mDPGaXPnog4Re5m8A7MQ4ZFvrK2Rc1Y-4zvPRi5zCQ-48GCWH2JTO-prrMM7e9hYXovKRLMb2w7ln1ReSvC3SminwfYI36vU1uAhI4NAwPmnM2NNiJfzvPchYCHtuYrYdZKyhdH-H2CNxHfT2qwYCeHgUw4LJ50dSDysg7icSQjoCmEXq_I3GcDmgkMwZ2yTfyJYfqyGQgx4K4xluReVc1qnJBvvp3bYFrDhFSxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
ازسرگیری حملات به ایران، یک عملیات محدود است یا یک جنگ تمام‌عیار؟
ترامپ
:
آن‌ها یک کشور شکست‌خورده‌اند... این به آن معنا نیست که به آن‌ها ضربه نخواهیم زد. خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21867" target="_blank">📅 23:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e3f0dc763.mp4?token=BPnLFvvJ_-sTckxsCUKTqWZSh2XC46F9-IC6u5M-0-XKYydq7UbdnlPdKACbOG1Hb6_pS-Qfz3HvtSSR2E78q18V5GKn6exIMS9N1fBMS851dBxnqTQipDaqmS202rNahSoOnpp8DMR70FOvrypfNYG-cjX5MrBIrwF3CUvgT_Q4BHXTTg_LKdPZQIprBZv3hZSntN8Cynf8CZU-fBBafjXUXLPI1C-OJFBOFycNiC8GGEoej_wnptYaaCClp9v6-qAMrwUjGJl1NLh5pmxt6cXzwvDNqXkzhLax2OEO1sBUoPx_fNvd0OMuVuRxS1RDah9MvRA01ZKbLB9MPWnTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e3f0dc763.mp4?token=BPnLFvvJ_-sTckxsCUKTqWZSh2XC46F9-IC6u5M-0-XKYydq7UbdnlPdKACbOG1Hb6_pS-Qfz3HvtSSR2E78q18V5GKn6exIMS9N1fBMS851dBxnqTQipDaqmS202rNahSoOnpp8DMR70FOvrypfNYG-cjX5MrBIrwF3CUvgT_Q4BHXTTg_LKdPZQIprBZv3hZSntN8Cynf8CZU-fBBafjXUXLPI1C-OJFBOFycNiC8GGEoej_wnptYaaCClp9v6-qAMrwUjGJl1NLh5pmxt6cXzwvDNqXkzhLax2OEO1sBUoPx_fNvd0OMuVuRxS1RDah9MvRA01ZKbLB9MPWnTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما وارد ایران شدیم و داریم حسابی آنها را درهم می‌کوبیم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21866" target="_blank">📅 23:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4906f15f1.mp4?token=XTiuZDaYT_XNH7s2JQw0MT0f8Hu8AUPBJW1w9Eb0hKXa4p_VTwz5EInXgVdBwKwoNcsWC9uX696hJZtUe492AOP__CqHhC84mJGqm3dR5Hb4HRo48prxuPtGnIVYFm4H-wBOszASUvYScnLFOKT3zqRUSsQjvFRreZZ5eL2Kh8Vple3Q2pk0avL4m_sywCVNaiqn-voRMldc35O0s2bez6VvrVoiZa9HRD7uD_teONm0X6xLZ3Ms4XsFtV66pmKtZ0qShaXuitfEhqErTbCKBt3iwY29ozCtaq-wId6MmrVheBbYS0PWC3CZJPtEsJA-g1Ub7S1J2LewDwvG0go63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4906f15f1.mp4?token=XTiuZDaYT_XNH7s2JQw0MT0f8Hu8AUPBJW1w9Eb0hKXa4p_VTwz5EInXgVdBwKwoNcsWC9uX696hJZtUe492AOP__CqHhC84mJGqm3dR5Hb4HRo48prxuPtGnIVYFm4H-wBOszASUvYScnLFOKT3zqRUSsQjvFRreZZ5eL2Kh8Vple3Q2pk0avL4m_sywCVNaiqn-voRMldc35O0s2bez6VvrVoiZa9HRD7uD_teONm0X6xLZ3Ms4XsFtV66pmKtZ0qShaXuitfEhqErTbCKBt3iwY29ozCtaq-wId6MmrVheBbYS0PWC3CZJPtEsJA-g1Ub7S1J2LewDwvG0go63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها واقعاً نمی‌دانند رهبرشان کیست.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21865" target="_blank">📅 23:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4bfc4cdc.mp4?token=K3HiHkynWuh5H9Ua1zVx2ADt8NuWCrQgWsu03wr0Z-F1mL9JTmQT9Ow9ct3wWC1ty_LdCdfFewozNAJu0IXKawAAo1PIkY95Vvtgf5ilFUaX10IJbdwG90CJUXNmHo29ocr71jxdud8W47BtyqAVhpRCEUDujGcP7OVTzDZut0SOXYAyQj7zR6DffdTBXcTrMXsDITKSrDSTW5pj5nK4HAVgIG5uOIS4tHKrVBwcdQbY8dKmr7zdT3nk0y92EYvUNbOxMXqVoQtqYh5o73LZpEkMSFUcEFEg_Uu14vZW-8zV5OiGZSqC0A_AFxTpcZ45-OcMYEOsvCxwOngbQLaPK4WkVwAez8QQeN2m6QmTthK7h1j5l0A_lTg6JXBQiMab2WiqSzYmzbqN-1DDM8OcckX30BlcLzJj_TdM80ik_7ShosL4WbHsg5zWIk6cboKAfWH_awyDW3b4cn0LViJ796yYcZ3HUlnSu8ezZq7jbb08KGSspqpeabZXe9e0e1W8OVigNJLp4je4Bj_ShKemDIsJK5cq97phMkMK8JGx3Zc2A9zpjtuHYuPVSQ1_e8N-RtrbWaJdQ5gwy3Y8x4mkSzXYzfCzstZ5AYNCaBcOhSDc2GibID0pHVrbmrV006Y9o5QUQ4JJeZhMah81DowUuB73pg8Adk5Zb1lY_31vFqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4bfc4cdc.mp4?token=K3HiHkynWuh5H9Ua1zVx2ADt8NuWCrQgWsu03wr0Z-F1mL9JTmQT9Ow9ct3wWC1ty_LdCdfFewozNAJu0IXKawAAo1PIkY95Vvtgf5ilFUaX10IJbdwG90CJUXNmHo29ocr71jxdud8W47BtyqAVhpRCEUDujGcP7OVTzDZut0SOXYAyQj7zR6DffdTBXcTrMXsDITKSrDSTW5pj5nK4HAVgIG5uOIS4tHKrVBwcdQbY8dKmr7zdT3nk0y92EYvUNbOxMXqVoQtqYh5o73LZpEkMSFUcEFEg_Uu14vZW-8zV5OiGZSqC0A_AFxTpcZ45-OcMYEOsvCxwOngbQLaPK4WkVwAez8QQeN2m6QmTthK7h1j5l0A_lTg6JXBQiMab2WiqSzYmzbqN-1DDM8OcckX30BlcLzJj_TdM80ik_7ShosL4WbHsg5zWIk6cboKAfWH_awyDW3b4cn0LViJ796yYcZ3HUlnSu8ezZq7jbb08KGSspqpeabZXe9e0e1W8OVigNJLp4je4Bj_ShKemDIsJK5cq97phMkMK8JGx3Zc2A9zpjtuHYuPVSQ1_e8N-RtrbWaJdQ5gwy3Y8x4mkSzXYzfCzstZ5AYNCaBcOhSDc2GibID0pHVrbmrV006Y9o5QUQ4JJeZhMah81DowUuB73pg8Adk5Zb1lY_31vFqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها یک کشور شکست‌خورده هستند. نرخ تورم آنها به 350 درصد رسیده است. آنها هیچ ارز معتبری ندارند. به سربازان خود حقوق نمی‌دهند. بیشتر رهبرانشان فوت کرده‌اند.
نیروی دریایی آنها نابود شده است. نیروی هوایی آنها از بین رفته است. تجهیزات نظارتی آنها تقریباً به طور کامل از بین رفته است.
این به این معنی نیست که ما به آنها حمله نخواهیم کرد. ببینید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21864" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18b0e8cad.mp4?token=v4YpHyGc4AU0dDyQC4CUVwrULWCygPKm--a9ZtcO5FGzIftmTE5eJPKLx5yZph5wlX2n1yaKFmIh4AmxRETLelTYzKnNetldLWSvoJBBA4qEIvECkEO_OQZX6rpbDiJ429Fb4ml5doog4oCj7k9AQXNYDVVJ2_OD6JWBiBC36PmNxYsWTAjykLL9kayzPiZLocJgYld8XSVa9KH0cy19pbtuYsbztRe6uKpB9IF5EF0LGEwPrHprGVGYpjJht7iFSMSRsU7FELpr0xKiSLz4C67lFS8twzd5Z33PeREJv5fwB0xTSHL5gg5NSeT-YG_GQtULn5sCECqTr5TnhhtAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18b0e8cad.mp4?token=v4YpHyGc4AU0dDyQC4CUVwrULWCygPKm--a9ZtcO5FGzIftmTE5eJPKLx5yZph5wlX2n1yaKFmIh4AmxRETLelTYzKnNetldLWSvoJBBA4qEIvECkEO_OQZX6rpbDiJ429Fb4ml5doog4oCj7k9AQXNYDVVJ2_OD6JWBiBC36PmNxYsWTAjykLL9kayzPiZLocJgYld8XSVa9KH0cy19pbtuYsbztRe6uKpB9IF5EF0LGEwPrHprGVGYpjJht7iFSMSRsU7FELpr0xKiSLz4C67lFS8twzd5Z33PeREJv5fwB0xTSHL5gg5NSeT-YG_GQtULn5sCECqTr5TnhhtAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : در صورت بروز وضعیت اضطراری یا جنگ، ما کاملاً آماده‌ایم تا با آن مقابله کنیم
هیچ‌کس به ما حمله نخواهد کرد. می‌دانید دلیلش چیست؟
چون آن‌ها عاقل هستند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21863" target="_blank">📅 23:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال ۱۲ اسرائیل: چند مقام ایرانی امشب به‌صورت مستقیم و همچنین از طریق واسطه‌های منطقه‌ای با دولت ترامپ تماس گرفته‌اند تا از حملات تلافی‌جویانه گسترده آمریکا که گفته می‌شود برای امشب برنامه‌ریزی شده، جلوگیری کنند. این گزارش پس از ۲۴ ساعت پرتنش و در پی تبادل اقدامات نظامی میان ایران و آمریکا منتشر شده و تاکنون از سوی تهران یا واشنگتن تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21862" target="_blank">📅 22:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همکنون یک F-35 از سمت خلیج فارس به سمت عربستان سعودی سیگنال 7700 روشن کرده ودر حال فرود اضطراری است @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21861" target="_blank">📅 21:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اکسیوس : به گفته سه مقام آمریکایی، رئیس جمهور ترامپ در حال بررسی طرحی از سوی سنتکام برای انجام حملات محدود در تنگه هرمز بوده است تا از بازسازی قابلیت‌های راداری و موشکی ایران برای حمله به کشتی‌ها جلوگیری کند
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21860" target="_blank">📅 21:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خوب رسیدیم به ساعات ملکوتی صدای انفجار به وقت سیریک لطفا گوش هاتونو تیز کنید
😁
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21859" target="_blank">📅 21:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آکسیوس:شرکت‌های رمزارزی به‌دنبال ورود مستقیم به نظام بانکی آمریکا
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد تعداد درخواست‌ها برای تأسیس بانک‌های جدید در دوره دوم ریاست‌جمهوری ترامپ افزایش یافته و بخش قابل‌توجهی از این درخواست‌ها از سوی شرکت‌های فین‌تک و رمزارزی مانند
Coinbase و Ripple
است. این شرکت‌ها می‌خواهند با گرفتن مجوز بانکی، خودشان مستقیماً خدمات مالی و بانکی ارائه کنند و کمتر به بانک‌های سنتی به‌عنوان واسطه وابسته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21858" target="_blank">📅 21:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پنتاگون قراردادهای هفت‌ساله‌ای با لاکهید مارتین و سیستم‌های مهمات و تاکتیکی جنرال داینامیکس امضا کرده است تا تولید موشک‌ها را گسترش دهد.
این توافق‌ها با هدف افزایش تولید و تسریع در تحویل اجزای حیاتی برای برنامه‌های موشک‌های ضد موشک تهاد (THAAD) و پاتریوت PAC-3 MSE انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21857" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امروز
کنگره آمریکا بعد از تعطیلات تابستانی دوباره شروع به کار کرده، تمرکز اصلی مجلس نمایندگان روی
لایحه تأمین مالی موقت دولت
برای جلوگیری از تعطیلی دولت است
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21856" target="_blank">📅 20:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTarazi</strong></div>
<div class="tg-text">به تمامی دوستانم معروفیت کردم حتی به راننده های اسنپ گفتم بهشون صریح ترین و سریع ترین و درست ترین اخبار رو فقط از یاشار دنبال کنید خودم گوشی رو میگیرم براشون میزنم پیجت رو</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21855" target="_blank">📅 20:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8089942cc.mp4?token=hrjALNK83XIyXvtx3hWeIDOK2I74ipDLPAaJqtBocMwxfZMruGKAlMC0ToG-CxU6VkNyr1rFMFoRq8Vv0Q6fc4bexRBSHIueL_DJDmzHRY9E4zH7tBHV3qFaTfcYyFR0c5wUiqtnLepzIE9AGbopaZs3HSc032-sA2Ps3uLb_ILrEpngk6ggLKz40aRIefnutgM-HoToUtj0Eye5Jf22J4MduN4gxrxbDHlSWQofM7hQPMond96WSAEcc8vRyQCPwlQVW9pz55LH0Ho4LpOhCNprrsPWrZARfNt3uKabGZygwn-0tcdrEnQKt8hcR8Mynpg9DWzvvP2RRAvmMHf5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8089942cc.mp4?token=hrjALNK83XIyXvtx3hWeIDOK2I74ipDLPAaJqtBocMwxfZMruGKAlMC0ToG-CxU6VkNyr1rFMFoRq8Vv0Q6fc4bexRBSHIueL_DJDmzHRY9E4zH7tBHV3qFaTfcYyFR0c5wUiqtnLepzIE9AGbopaZs3HSc032-sA2Ps3uLb_ILrEpngk6ggLKz40aRIefnutgM-HoToUtj0Eye5Jf22J4MduN4gxrxbDHlSWQofM7hQPMond96WSAEcc8vRyQCPwlQVW9pz55LH0Ho4LpOhCNprrsPWrZARfNt3uKabGZygwn-0tcdrEnQKt8hcR8Mynpg9DWzvvP2RRAvmMHf5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبران ایران مهمه اینه که سرشون به گردنشون وصل باشه ( نکشیمشون )
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21854" target="_blank">📅 20:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سه پا : سامانه‌های پدافند هوایی ما یک پهپاد از نوع MQ-9 را در شرق تنگه هرمز سرنگون کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21853" target="_blank">📅 20:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الجزیره
:
پوتین اعلام کرد روسیه در مسیر پایان دادن به مناقشه اوکراین است
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21852" target="_blank">📅 19:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a8c19c57.mp4?token=v1ivWfu-XH-6Qn0PDnuSu8OFKuCzOoxuaREaCE6gm7aBCU1Iz6ujK6SiZMYiJTb4oP2Sud4I9swP_KCJqBKnuMRrWN2r794PgG045rvQRI3GhD0TcRzr7KHDv-Fbr5THGSz3hjpGEdD41zAqKuuDbGFGrjVrBDS120_F70gXpHJlgJvwCmHAjkQTvRB5LHW7uFkcj-Z-g96E9deoIN5acevJ_YVOOkU2m9CLSXeBagkeLYp16-94i3qWH7YZwOSRL1E2BfBrlL1UdzR5p9eiX0NIImC5CGWVUxvXfacEZacxEfdIK5T8fXfMSTQFAGo07IBtOhZNEpQCIS5Ov3cMZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a8c19c57.mp4?token=v1ivWfu-XH-6Qn0PDnuSu8OFKuCzOoxuaREaCE6gm7aBCU1Iz6ujK6SiZMYiJTb4oP2Sud4I9swP_KCJqBKnuMRrWN2r794PgG045rvQRI3GhD0TcRzr7KHDv-Fbr5THGSz3hjpGEdD41zAqKuuDbGFGrjVrBDS120_F70gXpHJlgJvwCmHAjkQTvRB5LHW7uFkcj-Z-g96E9deoIN5acevJ_YVOOkU2m9CLSXeBagkeLYp16-94i3qWH7YZwOSRL1E2BfBrlL1UdzR5p9eiX0NIImC5CGWVUxvXfacEZacxEfdIK5T8fXfMSTQFAGo07IBtOhZNEpQCIS5Ov3cMZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور آمریکا، ونس : اینگونه فکر کنید که ترامپ با پست جزیره خارک به ایران پیام خودش را داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21851" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21850">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrwykDBCixnjl-vb714tD1IbemT9N-ctv6gQbvgCl6BOksvgXEK0e3lp4iAyWYWwGLlcqvm9jO37dkDUvj9ObBfIQbHTNALW3rDqGAJS5gTH0H8_M9z4cvgHyEuvWz0x0o_dLleDdgn0LRUywo65LJDH-C4JYzAy6u-JVxumniOYr6YDXa5424KL4rolfrRivqHyH21WyGTR9Ess6X_jM5RC7sO2jaAxmi3jqGZInKqjDT9ZRbgcIuI3En9CgK032T__14Y00hzDB3NVKTXWPE9XRGUUh1GBAzl-7j2O4q6XtTPMcxE-clkdjbr-9Q1X6Dr79lmsto8o0DiwGAXf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث ، بازنشر خبر بلومبرگ :
ایران با توقف تجارت با امارات، در معرض خطر از دست دادن شریان حیاتی اقتصادی خود قرار دارد…
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21850" target="_blank">📅 19:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ در تروث  : جزیره خارک دارد به‌طور کامل به تکه‌پاره تبدیل (با خاک یکسان) می‌شود!!! @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21849" target="_blank">📅 18:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرماندار قشم : دو کشته و تعدادی مجروح در حمله آمریکایی به جزیره لارک در شب گذشته. @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21848" target="_blank">📅 18:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">منبع اسرائیلی: پس از تشدید اوضاع در خاورمیانه که شب گذشته رخ داد، فرماندهی جبهه داخلی آماده است تا این بار شاهد تشدید اوضاع در
نیز اسرائیل باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21847" target="_blank">📅 18:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نرخ دلار ۲۱۲،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۴-۲۱۷ هزار تومان(سقف تاریخی)
تتر ۲۰۹،۵۰۰ تومان(سقف تاریخی)
بیتکوین ۷۷،۹۰۸ $
انس جهانی طلا ۴،۴۲۴ $
نفت برنت ۹۰،۷۹$
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨
۶ عصر تهران</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21846" target="_blank">📅 18:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnE34ejhR-JjNUwS9ptgo3vA9yXXBLs1As8KhWwelmUOIrZTLEa4g6CjjmAgbiNAzs-CLu-k_PR7VxDzxyFvVvEoe3Yv0oJTNSvf9yal7l2o3zxWj_BLVCo3q9MZ5L6cj8WD8UBzj8fs4OzW14Gxj7G7rJLlz813_ozXaUUmg5QpdVtzcovXGe8npOL3YPZeqFSr_KP1sqvWOXGESkwCh-gXEvph9brVJQWN3j17ZtC5gYBsI_CELi0F9McTLinQ599CIiQiKj6ddrKPWxfvrf50OdcIy0cB5MyuaVw_ejIX1CZfg4m1kLkWBoRG2TrhzjbT0l5AR0szMITmg4hhcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سوخترسان و جنگنده های پنهانکار در حال عملیات در تنگه هرمز - خلیج فارس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21845" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۳ اسرائیل گزارش داد موساد پیش از آغاز جنگ، طرحی مخفی برای سرنگونی جمهوری اسلامی با استفاده از نیروهای کرد آماده کرده بود. بر اساس این طرح، هزاران نیروی کرد برای آموزش به اسرائیل منتقل شده بودند تا پس از آغاز جنگ از مسیر عراق وارد مناطق کردنشین ایران شوند. قرار بود نیروی هوایی اسرائیل با حملات گسترده، مسیر ورود نیروهای کرد را باز کند. طراحان امیدوار بودند یک شکست نظامی اولیه برای جمهوری اسلامی، اعتراضات میلیونی در ایران را به دنبال داشته باشد و به فروپاشی رژیم منجر شود. اما سه روز پس از آغاز جنگ، این بخش از عملیات متوقف شد. یک مقام اسرائیلی به کانال ۱۳ گفت: «سه روز پس از آغاز عملیات، دستور رسید: انجام ندهید.» طبق این گزارش، مخالفت رجب طیب اردوغان و فشارهای جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در توقف این طرح نقش داشت و دستور نهایی از سوی کاخ سفید صادر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21844" target="_blank">📅 17:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرگزاری CBS : ترامپ به شدت عصبانی است و می خواهد امشب به ایران حمله کند!
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21843" target="_blank">📅 17:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ea412ab5.mp4?token=XidSD-qZ4EsLgknqqryz6H8fb1xr5HPRqvWYUbLZNiN2k6XY74ct6vEljxOOYWFEKCHXOuvA3i6sgn1yiq9i2BMLAkDV0mAn_STwhVbdbBsxCKfuI-Sx3QVZIJf1VuaoMFI5EG3NNK_IBV3JL2GLU0V1lzZW4b_sar3EU6Grw_SGokDeVRCyz__z8Yg4GpuQC-zDgBq7kH_kVasxnJ_ntBdgG-UVHMxiSODfr2pch5V5mKR0syT68D0_rzxYc7jQ-hUpjbboZJo7IVsgoz8ISAY-BnIoks2KdLCHTru8I0_68YQPHWHUNfFd-O5sDfU5XQ-1kIFwGr9kyyVqIXfOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ea412ab5.mp4?token=XidSD-qZ4EsLgknqqryz6H8fb1xr5HPRqvWYUbLZNiN2k6XY74ct6vEljxOOYWFEKCHXOuvA3i6sgn1yiq9i2BMLAkDV0mAn_STwhVbdbBsxCKfuI-Sx3QVZIJf1VuaoMFI5EG3NNK_IBV3JL2GLU0V1lzZW4b_sar3EU6Grw_SGokDeVRCyz__z8Yg4GpuQC-zDgBq7kH_kVasxnJ_ntBdgG-UVHMxiSODfr2pch5V5mKR0syT68D0_rzxYc7jQ-hUpjbboZJo7IVsgoz8ISAY-BnIoks2KdLCHTru8I0_68YQPHWHUNfFd-O5sDfU5XQ-1kIFwGr9kyyVqIXfOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت: می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا بابت بیانیه قوی حمایت از عملیات‌های اقتصادی ما علیه رژیم ایران تشکر کنم.
با همدیگر
در این گروه حکومت وحشتناک ۴۷ ساله آن‌ها را به پایان خواهیم رساند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21842" target="_blank">📅 17:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21841">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFfc6ekDc6-FMRaoo47IC0HLkfRghG4UwBQj6gbvVU1uf6Kx3mQMR8NNwKB4r3qXUb6zglDXDGWFJxnRxNwccdWSy8LhGTOj6x8MigbhGrp1dyY83Zv2KRv4Catw62gIjnAFlN2iiARvofgKwrbQ6PFcNhqHRoTivQtLYMbef37RP4CRDHLHsW4-QsLf_bds6JdOA39lQ1vxn71oo2KE6UxL7ryq44yIwU1Z-ZRCfLUZMfDXBHdfJ_SozTYpypwKWI8MWHLdidWFxHHTDY7BDF5iHskiZ1irQaavXmAjZiOnP3cZ5K9N-XOZCBOTVo1SpCgJXmxYe5Ii7FlhpG1Q7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب سنتکام در پاسخبه خبر فیک پرس تی وی : هیچ کشتی در تنگه هرمز به مین برخورد نکرده است. این یکی دیگر از تلاش‌های سپاه پاسداران برای ارعاب کشتیرانی تجاری منطقه‌ای از طریق انتشار اطلاعات نادرست است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21841" target="_blank">📅 17:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد. @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21840" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">@WarRoom
roo be jolo</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21839" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21838">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21838" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21837" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7129ba04fe.mp4?token=CULOTG76GeWuWsjafkdeZaEPn3ZbIwvZsPDFXzv3Las7fNmPYvX11eiIAM8Lm8eyEvnCsceKriT0hIfFLv7WZN9B3DOsPS_5CwE8gmuvKjKKYOwlqy7DbLeftCAS4ZZrfannr_ICoKhLczDx2hgjBncvXusnYyNMlrneUap8m24sb2YDsK_7t7t5Y8Ne1aQJ-ZCpDfLhfaPqA39FdC3S6RNZ2zfxpqZbJ3K72iWq6aEy5G_vXfkagFh_qVUeHO0RyZtXhPg3NO3v-nF2SvyCRXABMWenmCOaqP7kWQpjupF0mBCz4v0ulcgENGi9CxcoGUvDPaA0YgFT-fsltvqxmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7129ba04fe.mp4?token=CULOTG76GeWuWsjafkdeZaEPn3ZbIwvZsPDFXzv3Las7fNmPYvX11eiIAM8Lm8eyEvnCsceKriT0hIfFLv7WZN9B3DOsPS_5CwE8gmuvKjKKYOwlqy7DbLeftCAS4ZZrfannr_ICoKhLczDx2hgjBncvXusnYyNMlrneUap8m24sb2YDsK_7t7t5Y8Ne1aQJ-ZCpDfLhfaPqA39FdC3S6RNZ2zfxpqZbJ3K72iWq6aEy5G_vXfkagFh_qVUeHO0RyZtXhPg3NO3v-nF2SvyCRXABMWenmCOaqP7kWQpjupF0mBCz4v0ulcgENGi9CxcoGUvDPaA0YgFT-fsltvqxmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت : «ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوکه شده‌اند.
ما شاهد صف‌های بنزین ۳ تا ۴ ساعته در ایران هستیم.»
ایران به دلیل اینکه از نظر اقتصادی در حال از دست دادن توان خود است، به اقدامات نظامی و خشونت‌آمیز روی آورده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21836" target="_blank">📅 16:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
فروپاشی کامل اقتصاد ایران ممکن است نهایت چند ماه طول بکشد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21835" target="_blank">📅 16:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد. @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21834" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21833" target="_blank">📅 16:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیانیه جدید EASA : هشدار پروازی اروپا برای آسمان خلیج فارس؛
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) با انتشار یک بولتن امنیتی جدید، توصیه پرهیز از پرواز در حریم هوایی کشورهای امارات، قطر، بحرین، کویت و بخش‌هایی از دریای عمان را تمدید کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21832" target="_blank">📅 16:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45560d441c.mp4?token=C4SaOh6qDMRoZsvfjMB-MkCnIIdr8xXMmPon2vWBqLCsIi7Pz5lUTwX0_pAXYKVBA_AGj1VxUmnZBgDkVMdqoL4agfgc2I0qmReQMEVcnf36iieQudK7VA6CIfiu8cbaEvG02HH7KbtKAdxS-PIEv6KVgk6kQmAPsOZA5jMnIw9nHr88zgbFwXjLWLvM91vRmy2sSyjw0bQ6z3oU76W7bZbRFYFizSRY62ui7h_i7ZS82UUIondxZCqb1RvLHcLZPIZN21-Z21aqEW4rO_wPl2QYOv58lDDq0zSk9KGW0TKGFTxHVvQSvhehZGnEg8RLPMqrAnBMqYLZjbBSO1UiyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45560d441c.mp4?token=C4SaOh6qDMRoZsvfjMB-MkCnIIdr8xXMmPon2vWBqLCsIi7Pz5lUTwX0_pAXYKVBA_AGj1VxUmnZBgDkVMdqoL4agfgc2I0qmReQMEVcnf36iieQudK7VA6CIfiu8cbaEvG02HH7KbtKAdxS-PIEv6KVgk6kQmAPsOZA5jMnIw9nHr88zgbFwXjLWLvM91vRmy2sSyjw0bQ6z3oU76W7bZbRFYFizSRY62ui7h_i7ZS82UUIondxZCqb1RvLHcLZPIZN21-Z21aqEW4rO_wPl2QYOv58lDDq0zSk9KGW0TKGFTxHVvQSvhehZGnEg8RLPMqrAnBMqYLZjbBSO1UiyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21831" target="_blank">📅 16:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21830" target="_blank">📅 16:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD8e9hH_sXSdbpzkgckSMBWmM8wgWnZzsb-lRWWvurRWd97DXKnriEAuqPSnQHaj1pYf6Y8s5uxYt0hlaFrMBgSUTNbWImFsNq3IGOGWqxuB6IN6ovhY6zliygzSGmzV6MoIMeUx1T6SutjefdPB0dn_J48dV6-G3l3-cQKC3UB_6aQRdeKdgs76gT6TETKQCUnTk-a4w8SxI8HeKum7OJr8tY_BA6aKt4Vl1SwL_1ar7wYoEeIqa8ICvKf9MBO8zPM8Hub5V-Djjgo_PEG3tq267DkCPdFjxqOfqMqtSb-7bwVuFGiWdtUiq2iXmK4ASYxly8NF0hxpfhtRtA6K6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «ایران رسماً یک
کشور شکست‌خورده
است.
ایران مُرده است!
آنها نیروی دریایی ندارند، نیروی هوایی ندارند، پول و ارز ندارند، حقوق سربازان و نیروهای پلیس خود را پرداخت نمی‌کنند، تورم به
۳۰۰ درصد
رسیده است و رهبری کشور کاملاً دچار آشفتگی و سردرگمی است و توانایی نمایندگی درست و شایسته کشور را ندارد.
تنها چیزی که دارند،
اخبار جعلی از آمریکا
، آمادگی برای کشتن معترضان خودشان است (اکنون بیش از
۱۰۰ هزار نفر کشته شده‌اند
. آنها باید به دلیل
جنایات جنگی و جنایت علیه بشریت
محاکمه شوند!) و البته یک خط خوب از
«چرندیات»
است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21829" target="_blank">📅 15:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فرماندار قشم : دو کشته و تعدادی مجروح در حمله آمریکایی به جزیره لارک در شب گذشته.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21828" target="_blank">📅 15:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ در تروث  : جزیره خارک دارد به‌طور کامل به تکه‌پاره تبدیل (با خاک یکسان) می‌شود!!! @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21827" target="_blank">📅 15:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRsa2p4dPlBN414h9LwgN8Tj88EhJhNgUIW66VdMxACBRbGJuACH3UTMPMbSjR4cI-r_AYiB2WqCfDadEV-WYtOd3qjQjenIqzyglZNM-afBX0RwEE92gq4Lyuc1yciSGzNxEwx1snBRag4bLyZ6eUjIvwul_sr-o2CaALMCKgUCdVooTVmZ89nA4Pc2NTRwxOpVob34kVSxTOwhOKU5ddrX8-ySsFKbKWggZHc-0mwszkKvZPiWmJUZVYDh0XbgxG4K5vIokEj1h-P2PoygKmoKiVtcFQGQ-hSZb8FB5W_H2nG04pMMw2OCAIcT5goyRqte7gO-ZSGFYRWyDejRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده هنگام گشت‌زنی در آسمان خاورمیانه، بر فراز آب‌های خلیج فارس پرواز می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21826" target="_blank">📅 15:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ادعای تانکر ترکرز : تنها کسی که انتقال محموله‌های STS (کشتی به کشتی) را در تنگه هرمز انجام می‌دهند، خود ایرانی‌ها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21825" target="_blank">📅 13:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نرخ دلار ۲۰۹،۶۰۰ تومان(سقف تاریخی) دلار کف بازار ۲۱۲-۲۱۵ هزار تومان(سقف تاریخی) تتر ۲۰۸،۴۰۰ تومان(سقف تاریخی) بیتکوین ۷۸،۶۳۴ $ انس جهانی طلا ۴،۴۴۱ $ نفت برنت ۹۱،۰۷$ @WarRoom
🚨
🚨
🚨
🚨
🚨
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21824" target="_blank">📅 13:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eii7arjQ_AaLNUX1gR9mX7IRggKaqiVby-aJwcKUm56WZTD7wwcAreAMJr9JRlZN_rQvA46DzWsYa8hLndhf3AUnM9hP_Kag3G-IHSCZBtwx9fhVpdQROz4IfD0azn4ODRU4XCcIYwjAH4SIYqbW1ca9rGP2x3ZJYt0DTCFa4dIvUtqx4Gpai_iaHUcqN8XQfT0BCiTio2G8y-urAeTDG9NUpKkRnp3kIRuH1P-o9oHZvtRpF7UBK4ACMQfa0wHPjClLulv1KEJokOiGcH4dDVh00a22LdHaCgYGHXqMfV6goVQbtsnCFUBQUIEycNZ9ADqo5zldGjsLRAWJt17QcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار ۲۰۹،۶۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۲-۲۱۵ هزار تومان(سقف تاریخی)
تتر ۲۰۸،۴۰۰ تومان(سقف تاریخی)
بیتکوین ۷۸،۶۳۴ $
انس جهانی طلا ۴،۴۴۱ $
نفت برنت ۹۱،۰۷$
@WarRoom
🚨
🚨
🚨
🚨
🚨
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21823" target="_blank">📅 13:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره ایران: «ما کمک بسیار کمی از کشورهای دیگر دریافت می‌کنیم، در حالی که خودمان به کشورهای دیگر کمک می‌کنیم. ما
میلیاردها و میلیاردها دلار
برای کمک به ناتو و کشورهای دیگر، از جمله کره جنوبی، هزینه می‌کنیم. ما به آنها کمک می‌کنیم، اما وقتی نوبت به کمک به ما رسید، من زیاد اصرار نکردم؛ فقط پرسیدم: «آیا مایل هستید مشارکت کنید؟» و همه آنها گفتند: «نه، متشکریم.»
و من با خودم گفتم:
این موضوع را به خاطر خواهم سپرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21822" target="_blank">📅 12:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسرائیل و یونان قراردادی دفاعی به ارزش تقریبی 3 میلیارد یورو امضا کردند تا یک سیستم دفاع هوایی چند لایه برای اسرائیل در یونان ایجاد کنند. این سیستم برای مقابله با موشک‌ها، پهپادها و سایر تهدیدات هوایی احتمالی از ایران و ترکیه طراحی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21821" target="_blank">📅 12:44 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
