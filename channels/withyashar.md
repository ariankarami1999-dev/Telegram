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
<img src="https://cdn4.telesco.pe/file/oFbKfpJzv9R_RpzK4JO9jX3GNDQfkETohQT1PzyIQfFHmv6AlXiEp7FumRHgsXhqSjppnExbRvSixqFCcpQ7D6saQWho39I9_BMLgtLFr6LRdgIl4ZxU4JWiXywyXGvbMknEjJNkvICBSOVxosInDYWS7EbgKRljVh7oVN-plvch-AZq8Bt_kYALpzuoDsJxRN6Cg8Gsx3ZEudfrB620nX8taiNUzdMbvod3I1b8jlZdfIx8jXCEoUGTZRLOyqpNw2guPBp4zc1yp8ZT3fj1ULJJEQFag-K77qHYa2-F8caIl3DriwMuTSD-EpQDF6sHqi7i_s6KHxpBFp2GnVBX3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 448K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 00:05:49</div>
<hr>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس اداره اخبار مجلس:
۵۰ روز است که یه بشکه نفت هم نفروختیم.
هیچ کالایی هم از جنوب وارد کشور نشده‌. محاصره اقتصادی بدجور دستمونو بسته.
@WarRoom</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/22398" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">زاکانی: وصیت نامه آقا با خودش تو بمبارون از بین رفته
@WarRoom
😁</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/22397" target="_blank">📅 23:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتانیاهو: «اگر ما علیه ایران اقدام نمی‌کردیم، ایران امروز بمب‌های اتمی داشت که قصد نابودی ما را داشتند.
حالا آنها دوباره تلاش خواهند کرد. آنها دوباره تلاش می‌کنند و دوباره تلاش خواهند کرد تا محوری را که ما شکستیم، بازسازی کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/22396" target="_blank">📅 23:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قالیباف : بستن تنگه هرمز به ضرر ایران شد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/22395" target="_blank">📅 23:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پرتاب۳ موشک از سیریک سمت تنگه ( رادار ندارن موش کور شدن ول میدن )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/22394" target="_blank">📅 22:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدای انفجار از تنگه ، امشب تنگه گیسو گیس کشیه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/22393" target="_blank">📅 22:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22392">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : آنچه سنتکام امروز ، تأیید کرده این است که سپاه پاسداران به سمت
دو ناو آمریکایی
موشک بالستیک شلیک کرده و سنتکام هم می‌گوید
ناو هواپیمابر و یک ناوشکن
موشک‌ها را جاخالی داده‌اند و هیچ نیروی آمریکایی آسیب ندیده است. در واکنش، آمریکا به سه نفتکش ایرانی حمله کرده است. بنابراین رسانه های زرد که به دروغ نوشته‌اند
«جورج واشنگتن به‌دلیل موشک‌های ایرانی عقب‌نشینی کرد»
، اصلا در خبر رسمی
نیامده
کدام ناو بوش یا واشنگتن
وبعد هم اگر
تغییر موقعیت عملیاتی یا دور شدن تاکتیکی ناو از محدوده خطر
انجام شود هم نرمال است ولی سنتکام چیزی‌نگفته است که ناو منطقه را ترک کرده یا به‌دلیل اصابت/ترس از موشک‌ها عقب‌نشینی کرده باشد !!!
@WarRoom</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/22392" target="_blank">📅 22:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عضو هیئت‌رئیسه مجلس : هم اکنون احتمال حمله به اسرائیل هم وجود دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/22391" target="_blank">📅 22:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22390" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اتاق جنگ با یاشار با افتخار عرزشی سوز ترین چنل تلگرام
🙌🏾
😁
💥
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22389" target="_blank">📅 21:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromUTA</strong></div>
<div class="tg-text">یاشار  ناموسا سگ میرینه بهت؟</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22388" target="_blank">📅 21:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=jLL_5lvIugp-A-DVdXsMNXL3NOLQrpje5vqg5QKf1hyq1hQoVRd2NniNwV_nBvMKfcnOkNg_SX4ggooIGNuDkSvlB4tayadk6rXyY-lDbEILNwbmcY98lZX7IK84S15FmOCNBpzTyMh_Z23att75yZdUUTwX_5bZxvXza5azeP8o8RX6drNz4_nO6zSPaBhQJYxg_P3yKOyvPjuern-NPEoZrmM74ZwWHKTBfhG9gnsR7hh1z7mj-bDxVMv1Ct0I-NACuYloSdWdsd6wkg2V_41vTi1WkYPhtWeynsdgI-FdACxccM8Y4QQMiP_RkmL548R4Bk94220iset7ZFsq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=jLL_5lvIugp-A-DVdXsMNXL3NOLQrpje5vqg5QKf1hyq1hQoVRd2NniNwV_nBvMKfcnOkNg_SX4ggooIGNuDkSvlB4tayadk6rXyY-lDbEILNwbmcY98lZX7IK84S15FmOCNBpzTyMh_Z23att75yZdUUTwX_5bZxvXza5azeP8o8RX6drNz4_nO6zSPaBhQJYxg_P3yKOyvPjuern-NPEoZrmM74ZwWHKTBfhG9gnsR7hh1z7mj-bDxVMv1Ct0I-NACuYloSdWdsd6wkg2V_41vTi1WkYPhtWeynsdgI-FdACxccM8Y4QQMiP_RkmL548R4Bk94220iset7ZFsq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
تنبیه</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22387" target="_blank">📅 21:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش ۲ انفجار جدید جاسک رأس ساعت ۸ @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22386" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قرارگاه خاتم‌ :جون مادرتون نزنین
قرارگاه مرکزی خاتم‌الانبیا: به ارتش آمریکا هشدار داده می‌شود که در صورت ادامه اقدامات خصمانه، ایجاد ناامنی، مزاحمت برای کشتی‌های ایرانی و محاصره دریایی ایران، ضربات نیروهای مسلح جمهوری اسلامی علیه شناورهای نظامی آمریکا در منطقه شدیدتر از گذشته خواهد بود و امکان گسترش دامنه آن نیز وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22385" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d6f60dbf.mp4?token=oEBsibjpivk-6BoGT0J0EWzeGtVPwJiia1dMCGM1DYQpeCr5cJ9f7FwqNIPnoPk23VNGUcKo5Vi9Ij1uJdA8o_o31OJp442OCKTVkVb7Ktyi90zZSH840_qFWpkU7oOtaa-JERZYoJsWir8v29Z7QYPZ3FF6fDOr1D1-JNryRXLUK9_fUxGxfpIrI_-g6iVpB9UXuquOH1nNVPsO2McqzoSBlp73bpQZ3bffVduyGh8N-VtHph3o7ZXMl-i1942784l2DHGvveP-tzWKN8cCeuExmaw1kIDhUSDcfjAYw2GoE3tvaFe6VNcLOsmjBdqlGsp8x83zUBOxq9Ew9eisFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d6f60dbf.mp4?token=oEBsibjpivk-6BoGT0J0EWzeGtVPwJiia1dMCGM1DYQpeCr5cJ9f7FwqNIPnoPk23VNGUcKo5Vi9Ij1uJdA8o_o31OJp442OCKTVkVb7Ktyi90zZSH840_qFWpkU7oOtaa-JERZYoJsWir8v29Z7QYPZ3FF6fDOr1D1-JNryRXLUK9_fUxGxfpIrI_-g6iVpB9UXuquOH1nNVPsO2McqzoSBlp73bpQZ3bffVduyGh8N-VtHph3o7ZXMl-i1942784l2DHGvveP-tzWKN8cCeuExmaw1kIDhUSDcfjAYw2GoE3tvaFe6VNcLOsmjBdqlGsp8x83zUBOxq9Ew9eisFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین، نشست خود را با ویتکوف و کوشنر، نماینده ویژه ایالات متحده، آغاز کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22384" target="_blank">📅 20:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q20vxzodiO27jBFdRbTxv7AUG-aa1yaxWgPoDB4HGKdrpKEBKKiDWRIxbhJyLHwB1-o-E9uFwfbxRLmkcHh3cR8jWg31ykqBh93-dBqO-_928bDKGd92kEO24t5aLnzknwtRWAgiq8YktlCOFDtDr5hJ0rFPPo3yxd4qzOPDVOE5XCcky_K-SjIsTixg8BSOoDqTV5gRYJ9Q2noj5m_q-uYkPR0s8AKczgGVg4hecmRnVLAIkdh4D9PLgAmxsR8Ftf4BfkoXf-fQJwtXBpzl4gZKccs7czhcMpRY9fIFzLl0_GrzaBfH79YU9swJArjZd3Za6mfyLmLJDfXZlAkx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78ca28583e.mp4?token=nY7EBd0_wRUpTFDiB8a2LHNCbt7xo_r3caF8lwYkfAUC2lxBwFgxZ5vwYPPeZa1y8m3evSr_-h0HKPwStT66nx9htDDCFj9bLuifNGOA_GcgbfyvzvAtGsYlnMJYuRVsRePNbvtEkxAPoiuU8C0DXouGjGHvvyXxdVvvjFxNJWWsbOd6PNSD3TyxXTGtlaBEuBmdkkK55AK2QC9S7nRjQDw_QPXrUcjttbRjQmd8-yStGKNntg5rQ-D9JsoVp5Jj1q9WlX3Ao3jb0uCdilJJrNUEGVffLURqUq--T7aAGBVMswFNiwyoY2b2Ybi9Az0VkDnQj0ujS4U_9DcQBLf39w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78ca28583e.mp4?token=nY7EBd0_wRUpTFDiB8a2LHNCbt7xo_r3caF8lwYkfAUC2lxBwFgxZ5vwYPPeZa1y8m3evSr_-h0HKPwStT66nx9htDDCFj9bLuifNGOA_GcgbfyvzvAtGsYlnMJYuRVsRePNbvtEkxAPoiuU8C0DXouGjGHvvyXxdVvvjFxNJWWsbOd6PNSD3TyxXTGtlaBEuBmdkkK55AK2QC9S7nRjQDw_QPXrUcjttbRjQmd8-yStGKNntg5rQ-D9JsoVp5Jj1q9WlX3Ao3jb0uCdilJJrNUEGVffLURqUq--T7aAGBVMswFNiwyoY2b2Ybi9Az0VkDnQj0ujS4U_9DcQBLf39w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7 نفر زنده زنده سوختن و جونشون رو از دست دادن...
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22382" target="_blank">📅 20:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش صدای دو انفجار قشم از سمت تنگه ، ۲۰:۰۷ دقیقه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/22381" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اتاق جنگ با یاشار : با وجود ادامه درگیری ایران و آمریکا ولی هم‌زمانی با
مذاکرات صلح روسیه و اوکراین و آتش‌بس سه‌روزه میان دو طرف، بیت‌کوین هم‌اکنون از ۸۰ هزار دلار عبور کرده است.
در صورت موفقیت مذاکرات و اعلام پایان جنگ روسیه و اوکراین، کاهش ریسک‌های ژئوپلیتیکی و افزایش اشتهای سرمایه‌گذاران برای دارایی‌های پرریسک می‌تواند موج تازه‌ای در بازار ایجاد کند؛ به‌گونه‌ای که
عبور بیت‌کوین از ۱۰۰ هزار دلار نیز می‌تواند به یکی از سناریوهای جدی بازار تبدیل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/22380" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83eb31b467.mp4?token=huP5Nek7rdAnw1t0hQAI0WNxqmXga5YCNLD1oPcMMFmYMwnWEV9yNEBKDUSEAMJ1vCj3j6-aOsT41OX4YPDDoJfdE4XgLeJZZci9QhOmZlq9ZN0SPA2hWehP3lF8s2kG08tx5xIQM1lG8nFtw9au1nW_NplWlgKPr5YbwjD4Em59ny4TCrmO7-SmFRdDwuc0N1G5XkKGRKd7BW9P2SaMwkYk6UIp7Qb02Xf8O4a9L1prmfj7xZ-4HnsoIc1C4MEIf5qeNofe-tjGM7ZH949fmsCcN9teuloSFQD5CW7sD4fRET_irC3HzPEgPRzq6dpB9Z_MCQ24heRYLLJUz2zVFzAyEJl22kxCA4fe79LkDIHwvwdJC8gJ0sqaEkjOrnTHI72-Bm8c2oIVncSE6MRZYrDO3MipHgzourgNIQRTnjE4vcl563wmlg4c4rglpCjH6T12Lw37TbafkRjpKg8AjmLlwqskIzGbsmK1RD34DX5-mvR6iXSSG7GrOoO49yMJT2pklvMhSeIt5Q2TL4rkw_zhW3okDuy402ul7YLLlrP2U70ZfOeP3OPFlfvVJQB9NwmGx6xErPGL2B4Cab4mn4DGsAk10LxNX9alDvrL3j-Ucp3zfhv4BHx3Hl7GNJD-eMuoST5gsHXXzme_L0m9M49e4NXjedgTPoOhhSQEXE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83eb31b467.mp4?token=huP5Nek7rdAnw1t0hQAI0WNxqmXga5YCNLD1oPcMMFmYMwnWEV9yNEBKDUSEAMJ1vCj3j6-aOsT41OX4YPDDoJfdE4XgLeJZZci9QhOmZlq9ZN0SPA2hWehP3lF8s2kG08tx5xIQM1lG8nFtw9au1nW_NplWlgKPr5YbwjD4Em59ny4TCrmO7-SmFRdDwuc0N1G5XkKGRKd7BW9P2SaMwkYk6UIp7Qb02Xf8O4a9L1prmfj7xZ-4HnsoIc1C4MEIf5qeNofe-tjGM7ZH949fmsCcN9teuloSFQD5CW7sD4fRET_irC3HzPEgPRzq6dpB9Z_MCQ24heRYLLJUz2zVFzAyEJl22kxCA4fe79LkDIHwvwdJC8gJ0sqaEkjOrnTHI72-Bm8c2oIVncSE6MRZYrDO3MipHgzourgNIQRTnjE4vcl563wmlg4c4rglpCjH6T12Lw37TbafkRjpKg8AjmLlwqskIzGbsmK1RD34DX5-mvR6iXSSG7GrOoO49yMJT2pklvMhSeIt5Q2TL4rkw_zhW3okDuy402ul7YLLlrP2U70ZfOeP3OPFlfvVJQB9NwmGx6xErPGL2B4Cab4mn4DGsAk10LxNX9alDvrL3j-Ucp3zfhv4BHx3Hl7GNJD-eMuoST5gsHXXzme_L0m9M49e4NXjedgTPoOhhSQEXE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ویدیویی که امروز از بنیامین نتانیاهو در شبکه‌های اجتماعی منتشر شده، در واقع مربوط به
سال ۲۰۲۰ و دوران کرونا
است. نتانیاهو در این موزیک‌ویدیو در کنار
عدن بن زِکِن (Eden Ben Zaken)
، خواننده مشهور اسرائیلی، آهنگ
«یش بی آهاوا» (Yesh Bi Ahava)
را اجرا می‌کند. این ویدیو با هدف
جمع‌آوری کمک برای سالمندان نیازمند و مقابله با تنهایی آنها در دوران قرنطینه کرونا
منتشر شده بود.
@WarRoom
😁
یاشار : باید یه فیت باهاش بدم بعد از جنگ</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22379" target="_blank">📅 20:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22378">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش ۲ انفجار جدید جاسک رأس ساعت ۸
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/22378" target="_blank">📅 20:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/22377" target="_blank">📅 20:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنگوی سابق مجلس: پیش نویس قطعنامه جدید آژانس، کد رمز برای حمله مجدد به مراکز هسته ای ایران است. ترامپ اعلام کرد ممکن است خیلی زود به کوه کلنگ حمله کنیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22376" target="_blank">📅 19:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر جنگ آمریکا: اگر ایران به کشتی‌های آمریکایی شلیک کند، ما ناوگان حامل نفت ایران را که فاقد تجهیزات دفاعی است، نابود خواهیم کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22375" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph-Zj6Ju-GslI6ixnrcblYm19RAHQc_Etu3qNfI1G0tOirOYEFygBNtI9cLp76zGQ5ZFjGzSPJlCzAk7W6siAqY3eqBMebtEYPzjXfaRV_xJ9G7fzAeAyCM9phEoD3M9ebxVqExp7NKysO16Q1pE5gQVbe6baXamoUmXfbYFk_aDGyUw7N58bbrmDKsmB7LG8Z49Z_mJRk_t7W_vaj1j4R4qIWixraXhzr1gv4qp4r-3Qf9VXaKDA8erfWEfupDG8kNxosKz30gmNAcTeAbhFE_4JpYykySyNOMErCDHb4zMSi8NyuTdVA5ObLU6u5fstCoAw6lyQCJHa5n9w8AEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای سنتکام نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند. همچنین نیروهای آمریکایی نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند؛ این نفتکش پس از آن هدف قرار گرفت…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22374" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با یاشار : در عملیات‌های طولانی بر فراز خلیج فارس، به‌ویژه در مأموریت‌های مرتبط با ایران، استفاده از هواپیماهای سوخت‌رسان اهمیت زیادی دارد؛ زیرا جنگنده‌ها می‌توانند بدون بازگشت به پایگاه، با
سوخت‌گیری هوایی ساعت‌ها در منطقه عملیاتی باقی بمانند
. این روش علاوه بر افزایش زمان ماندگاری در آسمان، نیاز به فرود و برخاست مجدد را کاهش می‌دهد؛ چرخه‌هایی که فشار قابل‌توجهی بر سازه و ارابه فرود هواپیما وارد می‌کنند. همچنین بازگشت مکرر به پایگاه‌های منطقه‌ای می‌تواند زمان‌بر و پرریسک باشد؛ به‌ویژه در شرایطی که
موقعیت پایگاه‌های مورد استفاده افشا شود و این پایگاه‌ها در معرض حملات موشکی و پهپادی قرار بگیرند
. از طرفی، جنگنده با سوخت‌گیری هوایی وابستگی کمتری به یک پایگاه مشخص دارد و می‌تواند
مسیر و مدت مأموریت خود را با توجه به شرایط لحظه‌ای تغییر دهد
. به همین دلیل، تانکرهای سوخت‌رسان نقش مهمی در حفظ
حضور مستمر، انعطاف‌پذیر و ایمن‌تر جنگنده‌ها در منطقه
دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22373" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیروهای سنتکام نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند. همچنین نیروهای آمریکایی نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند؛ این نفتکش پس از آن هدف قرار گرفت…</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22372" target="_blank">📅 18:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22371">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql79ia_QSa7McTr0WtpY3pGyOgX0dGZI5n8CKdIzaHv2iHzpkjlQ7rwC5DPtlMWLH4XRtHrnj_XstMFoRgl27vt1eg1Q1ufYA0zRjO7NT8a6-fnsRmxhEOscIw5202BxgDfCS8MVOsN8SuwixKNSxosRrBYz2_9cv-s_cWh54rNB4l7h6UyY_49BR0tQnU3JSiZ3iYqNBgHjQUlGpHEfU86_iJ_0j7liOns_SecxkMj-FiD89iWzUOKeKRVbNPuPpYDkMKE1A14j7ZR7nnIrAjkpr79daxoZiHdyvo8-YGWgumN_Av9AfHjNGh7T401S9IY4IP6uO3ZfZhnnbrmrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/22371" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ززززدن گزارش های زیاد از صدای انفجار جدید از خارگ و جاسک
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/22370" target="_blank">📅 18:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم !
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/22369" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیروی هوایی آمریکا به خدمه کشتی ایرانی ۳ دقیقه وقت خروج داد
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/22368" target="_blank">📅 18:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c9c110ff.mp4?token=Esxf7pyTqLkMJP2Vq5syg5NFZ0yT0Tv-aTJines_ZG3b6VCzEqOZm7xcKqmEXTx_RbxnJv_804hkVPkIHNpyg5KwHOJEoTzIv8Qi1TGmYjCzcspeQ5ShKBlYbBHf7LlWjgXEqbyhBSsUa8d7RA_lHnYeOdmbNvACrwTbC8bkHAPm3A3ElPC92yMK7RQxGyzYxvTEJPON13n1lc3dD5duUkSvZPLghoCxJJ8Z3ZqVeJXYAywl5iMHBEYhqroonVRulqHC2C7zGp4c8-G5o4SIVgsBI-v7AtyGp61m2pWPrK0SU27AtKa38KSOBXWX7TuX5s30oTgTcJoyC_uZbQgroRdSzlEQdN1xx6ws4SlktiQ61AKoW7Ib6hZxevB9svbZ35FGqsMAD2q3T4FUzXn2v3fmxxL4XEyjV1zA9ZsFfywnEGAy-iRx9xbT5ZXtC4SqsJtMNkz7aNyHaUODmw150smcRXs24VpcuYieFAb_mgCa4vuGnol1Kg1B9oEr7gPsNFRC-ouiNcGht40Zf9oSvAY0vfPgf1pYPdzDO4PylMUI_PTkqmGB8JafhcXhzrhCl9HcvGq_DxKBS9ibm0QNpGdseWYtFE4aGN_mnXDZ_pYCrLcZ3Io0TQxaMJGqU7bOsxZEERuE2gF84kfIeOBN5wQITkHGp40VkDrefLNAS8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c9c110ff.mp4?token=Esxf7pyTqLkMJP2Vq5syg5NFZ0yT0Tv-aTJines_ZG3b6VCzEqOZm7xcKqmEXTx_RbxnJv_804hkVPkIHNpyg5KwHOJEoTzIv8Qi1TGmYjCzcspeQ5ShKBlYbBHf7LlWjgXEqbyhBSsUa8d7RA_lHnYeOdmbNvACrwTbC8bkHAPm3A3ElPC92yMK7RQxGyzYxvTEJPON13n1lc3dD5duUkSvZPLghoCxJJ8Z3ZqVeJXYAywl5iMHBEYhqroonVRulqHC2C7zGp4c8-G5o4SIVgsBI-v7AtyGp61m2pWPrK0SU27AtKa38KSOBXWX7TuX5s30oTgTcJoyC_uZbQgroRdSzlEQdN1xx6ws4SlktiQ61AKoW7Ib6hZxevB9svbZ35FGqsMAD2q3T4FUzXn2v3fmxxL4XEyjV1zA9ZsFfywnEGAy-iRx9xbT5ZXtC4SqsJtMNkz7aNyHaUODmw150smcRXs24VpcuYieFAb_mgCa4vuGnol1Kg1B9oEr7gPsNFRC-ouiNcGht40Zf9oSvAY0vfPgf1pYPdzDO4PylMUI_PTkqmGB8JafhcXhzrhCl9HcvGq_DxKBS9ibm0QNpGdseWYtFE4aGN_mnXDZ_pYCrLcZ3Io0TQxaMJGqU7bOsxZEERuE2gF84kfIeOBN5wQITkHGp40VkDrefLNAS8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود اتوبان آزادگان
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/22367" target="_blank">📅 18:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM-aawi2xQL1VLqc3N6K3mTCW0Xu9M5WCSxgdlv54BQioC-xrF0f6beEH_WdYAGYt9gQd4SrqqqzJBYNzYOuVwYOKcVgJt5kWOtJrs6eRhfVYjRvtQvesCcWrF1Ujleb5jf7qq5eG5CbHHDliH7-1nqHh4R9NZU6yg3EpvLjSyNze0iJ2uYwazIol3jo56Bj0lNnjOn2FsgHDvButuKvuuqk5Tvw5PCKgLmCP9TGOZllDaNb71B_lPBRfjNz6MOkTW0RuZVh5H4x404z3e3Z9YE0S_ejujH1Kfxs-kxzMfv7PDoQqCJCoeOf3n1TzSLEVh5k8KVT909e0UNucqeuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز:
روسیه از سال ۲۰۲۳ در قالب برنامه محرمانه
C430L
به ایران برای توسعه موشک‌های کروز مافوق صوت کمک کرده است؛ تحقیقات این روزنامه بر پایه مکاتبات افشاشده روسیه، سوابق سفر متخصصان و اسناد ثبت اختراع نظامی نشان می‌دهد کارشناسان موشکی روسیه در توسعه
پیشران رم‌جت
به ایران کمک کرده‌اند؛ فناوری‌ای که می‌تواند موشک را با سرعت چند برابر صوت به پرواز درآورد و برای موشک‌های ضدکشتی و حمله به اهداف زمینی به کار رود. این همکاری حتی در جریان جنگ آمریکا و اسرائیل با ایران در سال ۲۰۲۶ نیز ادامه داشته و در صورت تکمیل، می‌تواند توان ایران برای تهدید ناوهای هواپیمابر و دیگر شناورهای جنگی آمریکا در منطقه را افزایش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/22366" target="_blank">📅 18:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22365">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش صدای انفجار جدید جاسک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/22365" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سفارت آمریکا در بحرین: آمریکایی‌هایی که در حال حاضر در خاورمیانه هستند باید نهایت احتیاط را رعایت کنند و از احتمال لغو پروازها، بسته شدن حریم هوایی و اختلالات سفر آگاه باشند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22364" target="_blank">📅 17:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دریاسالار
برد کوپر، فرمانده سنتکام
، گفت: پیام ما به سپاه پاسداران باید روشن باشد:
اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی بسیار سنگین‌تری به شما تحمیل خواهیم کرد؛ با از کار انداختن سه کشتی شما.
ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم،
ناوگان محدود و آسیب‌پذیر نفتکش‌های ایران را منهدم خواهیم کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22363" target="_blank">📅 17:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967738cda4.mp4?token=reocLdGFVJ2jBhB_cm1gUS25rBKGAEu6EMdJuB9uyexVZ1bZ1i49DWiTSQlUW9SpDpq_Gturk6Fl0deIztMpCtjhKcUX4GN5-AdosahphQeDiUhDBu9uSqXPGvcN7eE6zii_sPL9tGjC8Dxy5Ji54YecFTdPfzNeY15fenUEjXBQUDNXnkvVBju0j4IydwhCtv8OOrDAvW4W1WY7Dx3rKtpWF0lh81NaF-xZTBgVOs2u8iCx5rrN-i5WcR1kTlFWFHm35ekoRcDTbv8YzWOMWAS6Srpo84BOT0D1Muhau8xUS9rnrp884QbBxBOCaziWxIl7rfGiicC8Lvj_7PotQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967738cda4.mp4?token=reocLdGFVJ2jBhB_cm1gUS25rBKGAEu6EMdJuB9uyexVZ1bZ1i49DWiTSQlUW9SpDpq_Gturk6Fl0deIztMpCtjhKcUX4GN5-AdosahphQeDiUhDBu9uSqXPGvcN7eE6zii_sPL9tGjC8Dxy5Ji54YecFTdPfzNeY15fenUEjXBQUDNXnkvVBju0j4IydwhCtv8OOrDAvW4W1WY7Dx3rKtpWF0lh81NaF-xZTBgVOs2u8iCx5rrN-i5WcR1kTlFWFHm35ekoRcDTbv8YzWOMWAS6Srpo84BOT0D1Muhau8xUS9rnrp884QbBxBOCaziWxIl7rfGiicC8Lvj_7PotQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای سنتکام
نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند
. همچنین نیروهای آمریکایی
نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند
؛ این نفتکش پس از آن هدف قرار گرفت که به خدمه آن دستور داده شد کشتی را ترک کنند و نیروهای آمریکایی با اصابت به
چندین نقطه حیاتی کشتی، آن را غیرقابل استفاده کردند
. سنتکام اعلام کرد این
سه نفتکش ایرانی بخشی از یک شبکه چندمیلیارد دلاری انتقال پنهانی نفت
هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی آن در منطقه را تأمین می‌کند و مدعی شد
ایران توانایی دفاع از این نفتکش‌ها را ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22362" target="_blank">📅 17:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد که پس از شلیک موشک‌های بالستیک سپاه پاسداران به سمت 2 ناو جنگی نیروی دریایی آمریکا که در آب‌های منطقه در حال گشت‌زنی بودند، نیروهای آمریکایی
3 نفتکش ایرانی را هدف قرار دادند
یک ناو هواپیمابر و یک ناوشکن موشکی آمریکایی با موفقیت از چندین حمله ایران عبور کردند و
هیچ نیروی آمریکایی آسیب ندید
.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22361" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وال‌‌استریت ژورنال
:
ایده
«تغییر رژیم» در ایران بار دیگر در واشنگتن جدی شده
است. این نشریه می‌نویسد در داخل دولت ترامپ، این دیدگاه که جمهوری اسلامی یک واقعیت دائمی در منطقه است، دوباره در حال کمرنگ شدن است و برخی مقام‌ها به امکان تغییر بنیادین وضعیت سیاسی ایران توجه بیشتری نشان می‌دهند.بر اساس گزارش‌های وال‌استریت ژورنال، دولت آمریکا هم‌زمان روی
فشار اقتصادی، تحریم‌ها و محاصره دریایی
به‌عنوان ابزارهایی برای تشدید فشار بر تهران حساب باز کرده است؛ هدف این است که فشار اقتصادی به اندازه‌ای افزایش یابد که جمهوری اسلامی به تغییر رفتار یا پذیرش خواسته‌های آمریکا وادار شود
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22360" target="_blank">📅 17:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26928dc53.mp4?token=c6idbEsOwORNvAzGUuoN6OCF5JNPK1EHsSo8GEEBF0YiRazUI5LuoHwAjCaWCkivTIO_hLBLEmxNkBLdih7unKowFrcNTUs5vuLsHlTGNF5ZaYe58xYUoRnFM0aM_bZ4XZ6xvB17dLCGGzyR52Lv7r0oWq2nuHJucXKxT2WE1pziQc_V2e0xWI0JoMMAoOstLhFjvJeNt3kgyzrRmgs3wInSHMvOKeBMVjGDcDuMPgQRY3g31_pyeK4MSaUdZzdFfi1LenPYnFsb0oxQdb9emBA89RSmO64mPm2qvq-cskG3pk07S1sKEgXR94kyhD61PwXUYZHzasIVNwFHNut7QyPmmCWC9SBzwMnEaLL3Myd_EZP-AdXCbW9e2QzRr0HIOpDYzECUB0xGTOmT_fq6xfgc1HTIQXYtNdtLcAS7DUMYnrXdluezmf9uxKK5EvotlVYkNyGLrghzJNhs1xeqPIzMTch8i3Db_jyi6xvI9al4YU6INyPHNNw2wwR1BmjTBw6QpH7z7eux_IfTlbuZ9F6oFJ_e7XS8ltxz38_PG-Ay-wBxzjsmW7WBR0i-feYQip5LVDLgHPjfNHg-_X0nvEFVjdvKh9cs3P_63U4WGnUgLVqNs5orELsI0vUHxo1lYlRTDfpK4C3F4dXLH5ahntT2ZpfJe-L1uYSF0BFm_j4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26928dc53.mp4?token=c6idbEsOwORNvAzGUuoN6OCF5JNPK1EHsSo8GEEBF0YiRazUI5LuoHwAjCaWCkivTIO_hLBLEmxNkBLdih7unKowFrcNTUs5vuLsHlTGNF5ZaYe58xYUoRnFM0aM_bZ4XZ6xvB17dLCGGzyR52Lv7r0oWq2nuHJucXKxT2WE1pziQc_V2e0xWI0JoMMAoOstLhFjvJeNt3kgyzrRmgs3wInSHMvOKeBMVjGDcDuMPgQRY3g31_pyeK4MSaUdZzdFfi1LenPYnFsb0oxQdb9emBA89RSmO64mPm2qvq-cskG3pk07S1sKEgXR94kyhD61PwXUYZHzasIVNwFHNut7QyPmmCWC9SBzwMnEaLL3Myd_EZP-AdXCbW9e2QzRr0HIOpDYzECUB0xGTOmT_fq6xfgc1HTIQXYtNdtLcAS7DUMYnrXdluezmf9uxKK5EvotlVYkNyGLrghzJNhs1xeqPIzMTch8i3Db_jyi6xvI9al4YU6INyPHNNw2wwR1BmjTBw6QpH7z7eux_IfTlbuZ9F6oFJ_e7XS8ltxz38_PG-Ay-wBxzjsmW7WBR0i-feYQip5LVDLgHPjfNHg-_X0nvEFVjdvKh9cs3P_63U4WGnUgLVqNs5orELsI0vUHxo1lYlRTDfpK4C3F4dXLH5ahntT2ZpfJe-L1uYSF0BFm_j4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من به قطر حمله کردم
من آن را بمباران کردم و هم در طول جنگ به آنها حمله کردم، و آنها به من حمله کردند.
کل این ماجرای قطر یک بلوف بزرگ است. قطر یک کشور متخاصم است، اما قطر کشوری نیست که چیزی را به ما دیکته کند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22359" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی) دلار کف بازار :حدود ۲۳۰ هزار تومان! تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی) بیتکوین ۷۹،۶۴۶ $ انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت) نفت برنت  ۹۶،۲۸$(آخرین قیمت) @WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22358" target="_blank">📅 15:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرگزاری تاس:
ویتکاف و کوشنر، فرستادگان ترامپ، با پوتین گفت‌وگو کردند.
پوتین دستور توقف حملات به اوکراین را صادر کرد
به‌مدت سه روز هیچ حمله‌ای به کی‌یف انجام نشود؛ این تصمیم در چارچوب مقدمات سفر هیئت آمریکایی اتخاذ شده است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22357" target="_blank">📅 15:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی) دلار کف بازار :حدود ۲۳۰ هزار تومان! تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی) بیتکوین ۷۹،۶۴۶ $ انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت) نفت برنت  ۹۶،۲۸$(آخرین قیمت) @WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22355" target="_blank">📅 15:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f970801a4.mp4?token=MIERummDZmD32_rKujRlzerWu4wigQ-xUQc6jefp9vQOwPCd-McLRjkySumM0Ew8jyUgq5xh9a3zauyiH89n9XeSIMSpOZ3Q1I8p8xt39oWR_snn-_sOv0omB0RCFc97wohIba_CjJ7lQIt0Gwsxea7uOCslZA4H4FsJslhlCxnOXtKQOPrzxwAX4v6r5J42qlh0DNeAzH1TDK2FeQTMEXUID5pvN2EfyQrJ4724htRr1o8gWO5ronuaLDjRDi1m09pANsUwMumQOU-sKhJNv2IzhrMPQ7N4aLdb_EroDlltDtFRRJpZBrLqE8eGZdc-Hw6QkwVuyk2_BRflhHghcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f970801a4.mp4?token=MIERummDZmD32_rKujRlzerWu4wigQ-xUQc6jefp9vQOwPCd-McLRjkySumM0Ew8jyUgq5xh9a3zauyiH89n9XeSIMSpOZ3Q1I8p8xt39oWR_snn-_sOv0omB0RCFc97wohIba_CjJ7lQIt0Gwsxea7uOCslZA4H4FsJslhlCxnOXtKQOPrzxwAX4v6r5J42qlh0DNeAzH1TDK2FeQTMEXUID5pvN2EfyQrJ4724htRr1o8gWO5ronuaLDjRDi1m09pANsUwMumQOU-sKhJNv2IzhrMPQ7N4aLdb_EroDlltDtFRRJpZBrLqE8eGZdc-Hw6QkwVuyk2_BRflhHghcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : درصورت پیروزی در انتخابات رژیم ایران را عوض میکنم
نتانیاهو: سوال اصلی در این انتخابات این است: چه کسی کارهایی را که باید انجام شوند، به پایان خواهد رساند؟ چه کسی بالاخره این رژیم را در ایران نابود خواهد کرد؟ چه کسی بالاخره حزب‌الله را نابود خواهد کرد؟ چه کسی بالاخره حماس را نابود خواهد کرد؟
مخالفان سیاسی من در برابر هر فشاری تسلیم می‌شوند. آمریکا به آنها می‌گوید "نه"، و آنها بلافاصله می‌لرزند.
آیا آنها این کار را انجام خواهند داد؟ نه. آنها این کار را انجام نخواهند داد. ما این کار را انجام می‌دهیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22354" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5ab34899.mp4?token=g0NEEMb7PoehQ45RdWZhFxNVmXeIdqM5yELqu23CjY4-18QBvXVh7ZWeGJYsl11UZeBh4zfg0bkqWGeghSKrGFzl2sykLNOT3l1KfobzNUOhI-CQnI74a3S2VBz0lHGzHYiq9Vp13Q1xRxRRmi6NLvXH9eKDtiWv1KF22ViZL63YqI4ZLb5kzMHEaIDQkFeJ12m4dDt6ndd8bgIfV65xc-P0vSa1IRbsZiBV4_fB8OPJC4Qa1FBbN7V9Y-P20rs3jjrDW5RJGmYdKnaAGObFS5ptLws2L4u71Gkw3JA8l4l-iaiC6pEtwAjUCO4dC_9q1VcIYbs1prsZfgIe-YrgRKQ6XDBIQguteOH8jdFosiQxk_37V9Nl51Y_MFkcvVJwx-WECNiikB4ScZznc8CDDv6yKXt6990gKRNiaCVgr3zre3zoq4dKRYZbhlPhiFLuQIQUsrhjunLtNs-fNHNlAHQNQ8NkB65KXGx4crTv1z6DrNM98Cs8ZcFclqo0w31GiCiolIkh8r4lVoDgd_rfEfNW4t9Qj6xBb2R349BBvXjyjPUo89o7pDPrcb_BgBfFcIYc7sVWdWe58pWzx_XjuUaOxzejnkDRn9ONy0Q7I5o4dIG23xEhMRLp6QV8J8f4CeQtOT5DUtIPBCuXQMB7fJJqcQhf2SDUc2d5S_0jdp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5ab34899.mp4?token=g0NEEMb7PoehQ45RdWZhFxNVmXeIdqM5yELqu23CjY4-18QBvXVh7ZWeGJYsl11UZeBh4zfg0bkqWGeghSKrGFzl2sykLNOT3l1KfobzNUOhI-CQnI74a3S2VBz0lHGzHYiq9Vp13Q1xRxRRmi6NLvXH9eKDtiWv1KF22ViZL63YqI4ZLb5kzMHEaIDQkFeJ12m4dDt6ndd8bgIfV65xc-P0vSa1IRbsZiBV4_fB8OPJC4Qa1FBbN7V9Y-P20rs3jjrDW5RJGmYdKnaAGObFS5ptLws2L4u71Gkw3JA8l4l-iaiC6pEtwAjUCO4dC_9q1VcIYbs1prsZfgIe-YrgRKQ6XDBIQguteOH8jdFosiQxk_37V9Nl51Y_MFkcvVJwx-WECNiikB4ScZznc8CDDv6yKXt6990gKRNiaCVgr3zre3zoq4dKRYZbhlPhiFLuQIQUsrhjunLtNs-fNHNlAHQNQ8NkB65KXGx4crTv1z6DrNM98Cs8ZcFclqo0w31GiCiolIkh8r4lVoDgd_rfEfNW4t9Qj6xBb2R349BBvXjyjPUo89o7pDPrcb_BgBfFcIYc7sVWdWe58pWzx_XjuUaOxzejnkDRn9ONy0Q7I5o4dIG23xEhMRLp6QV8J8f4CeQtOT5DUtIPBCuXQMB7fJJqcQhf2SDUc2d5S_0jdp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در مورد سوء قصد علیه پسرش یائیر:
فقط می‌توانم بگویم که چنین سوء قصدی وجود داشته است. این یک اقدام قابل توجه بود. سرویس‌های امنیتی به سرعت اقدام کردند.
آنها حتی نیروهای کمکی از نیروهایی که در ایالات متحده داشتیم آوردند تا او را به سرعت از ایالات متحده خارج کنند. این کاملاً واقعی است.
و این اتفاق در نتیجه رفتار غیرمسئولانه - واقعاً بی‌ملاحظه - چندین روزنامه‌نگار و افراد دیگر رخ داد که مکان یائیر را به صورت زنده افشا کردند: آدرس دقیق محل اقامت او، عکسی از آپارتمان، شماره طبقه، شماره آپارتمان.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22353" target="_blank">📅 14:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/175ac48990.mp4?token=H1DB7I4V7EOwqdSL0dodGsG2_aWlKMMBM16S1DLd2wbifllnHkLHkTgg-kepL83_6tqip6uvgYjU8S95BWjRzP6DKRpUueLvJ9GX4ZnSR893p6TDpE7i0Ji5CGGTebET1PNoAJ85MAY18OwL_FuDdLzG7DsC_N-aMu_nJUR9uYGnpRIPzD49tI_u2pPf0rh4-hlhc1ujNbI4sjRyhRMr8p8saNhMdYSTy69PqXfzrtD7Zx-1OCDdwicRAWkkQ7rn__y0kSgUtJ9zsZRFQZqupRroJkrP4ix6VWvLGbmu6irvbWcErvwdXXveaU6uCmKAiz18kEvPcsdo_fpT4TWhuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/175ac48990.mp4?token=H1DB7I4V7EOwqdSL0dodGsG2_aWlKMMBM16S1DLd2wbifllnHkLHkTgg-kepL83_6tqip6uvgYjU8S95BWjRzP6DKRpUueLvJ9GX4ZnSR893p6TDpE7i0Ji5CGGTebET1PNoAJ85MAY18OwL_FuDdLzG7DsC_N-aMu_nJUR9uYGnpRIPzD49tI_u2pPf0rh4-hlhc1ujNbI4sjRyhRMr8p8saNhMdYSTy69PqXfzrtD7Zx-1OCDdwicRAWkkQ7rn__y0kSgUtJ9zsZRFQZqupRroJkrP4ix6VWvLGbmu6irvbWcErvwdXXveaU6uCmKAiz18kEvPcsdo_fpT4TWhuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نِتانیاهو درباره ایران: چه کسی در تاریخ ۷ اکتبر فکر می‌کرد که ما چهره‌ی خاورمیانه را تغییر خواهیم داد؟ من فکر می‌کردم.
نیت من این بود که در نهایت با ایران درگیر شویم
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22352" target="_blank">📅 14:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMett</strong></div>
<div class="tg-text">سلام یاشار
روزت بخیر
این صحبت درست نیست
خودروهای لوکس از منابع ارزی فردی که در حجم بالا ذخیره داره خارج میشه و معادل همون مقدار بابت ترخیص پرداخت میشه و از این طریق به جیب دولت کمک میکنه
اون دارایی اگر بابت پورشه ۹۱۱ نره قفل توی کشو هستش
واقع بینانه باید پذیرفت ج.ا. در راهبردهای نظامی و اقتصادی در شرایط فشار حداکثری موفق بوده و در مورد اجازه واردات خودرو لوکس هم تصمیم درستی گرفته</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22351" target="_blank">📅 14:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو درباره غزه: بازسازی غزه فقط در صورتی امکان‌پذیره که ابتدا خلع سلاح انجام بشه. هنوز نمی‌تونم بگم چه نوع بازسازی‌ای انجام خواهد شد، چون در حال گفت‌وگو با دوستان آمریکایی‌مون درباره این موضوع هستیم. گاهی اوقات دیدگاه ما با آمریکا یکیه، اما گاهی هم اختلاف نظر داریم. وقتی اختلافی وجود داشته باشه، آمریکا منافع خودش رو مطرح می‌کنه و من هم از منافع اسرائیل دفاع می‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22350" target="_blank">📅 14:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d1a681e.mp4?token=uUPbXA9w3q2kCNHo4MwYz9C1xd3xFY_UGr1em1M7uQVAOSOl4WfRhKq_5cRwmpMufJJPkbtQP0nvoniQZLHd9LeP29OKO6FzQ8L_dfgCiHirHAJaBLOSGRC9BkzARJegTIYWwP_JlB-vq_W4-ZA83DOOrbaIkBjL8gYNCc-mIgXyR4ZMg8wiPpzbi14hvqWJPYSRPp7RZRrdD95qO9eNnKrJoepgKmLqaj7EuYHb22WuxYj3aeaVbviwjQxSyo3lor5ztAV9Uci2LOUYy7vb9eTX3Pyc--GpQoc7JajdIMr0EQSBUu6KGTpTBkFIu5ILEMBxjPifbN4RB53N5j-8qDEMUONYT-_yNlu_u4E8mP81J0tGO_iUw_6wvBrRQ_wkN-KqusohAJjJtPMYjDT19NACBo6QGu9OxaAHTk9vzFFI6IrzvcAHDCKs2UgwuVqCXqoHn1wcLuLes6XkQcxljYISfatasq3BScHLhbcSTrGo1XKk0BSXH1KBzLOzUpb2R7Aa_k_oCyZ4Muzk3e8-pwUirDsPEJPIqtkKyZpMyzQCchHsI1nSCHbIyoXfTANphSSBWnzmh4ToaVYZqdmtz30h3gT8D2x7JHBmcbo20e80ya_beY7SSKmQTuU2YVKk5PfkBey_G022RvH7GSrCkouKpaX0LKynu6fRFKiCUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d1a681e.mp4?token=uUPbXA9w3q2kCNHo4MwYz9C1xd3xFY_UGr1em1M7uQVAOSOl4WfRhKq_5cRwmpMufJJPkbtQP0nvoniQZLHd9LeP29OKO6FzQ8L_dfgCiHirHAJaBLOSGRC9BkzARJegTIYWwP_JlB-vq_W4-ZA83DOOrbaIkBjL8gYNCc-mIgXyR4ZMg8wiPpzbi14hvqWJPYSRPp7RZRrdD95qO9eNnKrJoepgKmLqaj7EuYHb22WuxYj3aeaVbviwjQxSyo3lor5ztAV9Uci2LOUYy7vb9eTX3Pyc--GpQoc7JajdIMr0EQSBUu6KGTpTBkFIu5ILEMBxjPifbN4RB53N5j-8qDEMUONYT-_yNlu_u4E8mP81J0tGO_iUw_6wvBrRQ_wkN-KqusohAJjJtPMYjDT19NACBo6QGu9OxaAHTk9vzFFI6IrzvcAHDCKs2UgwuVqCXqoHn1wcLuLes6XkQcxljYISfatasq3BScHLhbcSTrGo1XKk0BSXH1KBzLOzUpb2R7Aa_k_oCyZ4Muzk3e8-pwUirDsPEJPIqtkKyZpMyzQCchHsI1nSCHbIyoXfTANphSSBWnzmh4ToaVYZqdmtz30h3gT8D2x7JHBmcbo20e80ya_beY7SSKmQTuU2YVKk5PfkBey_G022RvH7GSrCkouKpaX0LKynu6fRFKiCUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هواپیمای نظامی آمریکایی در فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق فرود آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22349" target="_blank">📅 14:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9102f4bd1c.mp4?token=viuB2qyM_9ZUE4BpiyI3XP9I-XZH8evKUEISDZ1WqgnwMPcIQPpH2aRzzwk28UzLWAl63XB9cz4sO77NsNpD-qL92Psa7UVd90KpnOANOC40rSEAIwaqzKZ5MThxlVOOWCnL5HGW4p_UyAdjV1Is9l9kYpW2-8o-cmk5wzNKIXB2WS4PSoIpm-6aWL2XHOTGR_fcMDyioj27Oxa8f3sBtd8SMU2lv0O24zlkcS_wQE-uytPpgnqw-J9NBMJ9ZRm7qXgEbYEfHLUKMPGKZ4bU9SSaZJI8RysFjG4lxWZKZszU0YOhi_bLYtzi9Jia_bR-2EQB2jikes6oPe_6HfsqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9102f4bd1c.mp4?token=viuB2qyM_9ZUE4BpiyI3XP9I-XZH8evKUEISDZ1WqgnwMPcIQPpH2aRzzwk28UzLWAl63XB9cz4sO77NsNpD-qL92Psa7UVd90KpnOANOC40rSEAIwaqzKZ5MThxlVOOWCnL5HGW4p_UyAdjV1Is9l9kYpW2-8o-cmk5wzNKIXB2WS4PSoIpm-6aWL2XHOTGR_fcMDyioj27Oxa8f3sBtd8SMU2lv0O24zlkcS_wQE-uytPpgnqw-J9NBMJ9ZRm7qXgEbYEfHLUKMPGKZ4bU9SSaZJI8RysFjG4lxWZKZszU0YOhi_bLYtzi9Jia_bR-2EQB2jikes6oPe_6HfsqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
: اونا می‌تونن به ما حمله کنن و ما هم پاسخ می‌دیم.
متوجه شدید ایران داره به همه شلیک می‌کنه؟ به کی شلیک نمی‌کنه؟ فقط اسرائیل.
چرا؟ چون دقیقاً متوجه حرف من هستن؛ تا وقتی من نخست‌وزیرم، چنان ضربه‌ای بهشون وارد می‌شه که حتی نمی‌خوام جزئیاتش رو بگم. این ضربه از قبل آماده شده.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22348" target="_blank">📅 14:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی) دلار کف بازار :حدود ۲۳۰ هزار تومان! تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی) بیتکوین ۷۹،۶۴۶ $ انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت) نفت برنت  ۹۶،۲۸$(آخرین قیمت) @WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22347" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405d38bbbf.mp4?token=e2U--iDM69Bi-mpIxpGs1utd2VAZZoNaUBoq2ucH2fzVM3cmQm297I6TllA4x61XlC_2JPzJpwF-WdDMCBcZj9ZB_SQpshyZJSYHh72Ebrhn5KmJsMkgFfbkbYsQPejoOTov3F0kensDgsNronwSf2ZNQYTHWazpL4nojw4EM2e5hfUJ6VfOp1hDqXUE2BbMUKojRm05IuLyY6xf8Udhq98ueFeoF-V_QmYn50K_973Eivh8oDY8tAsBZ-88E2z0rG6o-tR2p788cuZnYjlDqZZy7t_NwpwXpub0wDytJtRzGg0jeAppUgAFaen11Jh91UWmz8N_bPfGKUK-6huudg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405d38bbbf.mp4?token=e2U--iDM69Bi-mpIxpGs1utd2VAZZoNaUBoq2ucH2fzVM3cmQm297I6TllA4x61XlC_2JPzJpwF-WdDMCBcZj9ZB_SQpshyZJSYHh72Ebrhn5KmJsMkgFfbkbYsQPejoOTov3F0kensDgsNronwSf2ZNQYTHWazpL4nojw4EM2e5hfUJ6VfOp1hDqXUE2BbMUKojRm05IuLyY6xf8Udhq98ueFeoF-V_QmYn50K_973Eivh8oDY8tAsBZ-88E2z0rG6o-tR2p788cuZnYjlDqZZy7t_NwpwXpub0wDytJtRzGg0jeAppUgAFaen11Jh91UWmz8N_bPfGKUK-6huudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکسیوس گزارش داده است که استیو ویتکوف و جرد کوشنر، فرستادگان دونالد ترامپ، این آخر هفته به مسکو و کی‌یف سفر می‌کنند تا تلاش‌های دیپلماتیک آمریکا برای پایان دادن به جنگ روسیه و اوکراین را از سر بگیرند. طبق گزارش آکسیوس، قرار است ویتکوف و کوشنر شنبه با ولادیمیر…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22346" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وال‌‌استریت ژورنال:
محاصره دریایی آمریکا از تیرماه صادرات نفت ایران را تقریباً متوقف کرده و بستن تنگه هرمز از سوی ایران نیز ترامپ را به پذیرش شروط تهران وادار نکرده است. طبق این گزارش، رهبران ایران انتظار دارند وضعیت کنونی و فشارهای اقتصادی ناشی از آن حدود
پنج ماه دیگر
ادامه پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22345" target="_blank">📅 13:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پارلمان پاکستان برای نخستین بار به عاصم منیر اختیار قانونی فرماندهی هر سه نیروی ارتش، نیروی دریایی و نیروی هوایی را اعطا کرد
دوره فرماندهی او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت
وی در مقام «فیلد مارشال»، مصونیت قانونی خود را تا پایان عمر حفظ می‌کند و برکناری او تنها با رأی دو سوم پارلمان امکان‌پذیر است
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22344" target="_blank">📅 13:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی)
دلار کف بازار :حدود ۲۳۰ هزار تومان!
تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی)
بیتکوین ۷۹،۶۴۶ $
انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت)
نفت برنت  ۹۶،۲۸$(آخرین قیمت)
@WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22343" target="_blank">📅 13:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر جنگ اسرائیل :
منتظریم ایران به تصرف تپه "علی الطاهر" واکنش نشون بده و حرکتی بزنه تا از غل و زنجیر و محدودیت‌های ایجاد شده توسط ترامپ آزاد بشیم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22342" target="_blank">📅 13:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صحبت های زیبای یک کاربر درباره پست قبلی
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22341" target="_blank">📅 13:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : سوی دیگر فشار اقتصادی ، نمایشگاه های کشور های خلیج فارس با کمبود خودرو هایی مواجع شدند که در لیست واردات ایران قرار‌ دارند و تا مواردی برای لکسوس ال اکس ۶۰۰ تا ۲۰،۰۰۰$ قیمت این خودرو در بازار افزایش یافته ، بعد از صحبتم با یک نمایشگاه دار قدیمی ، وی گفت جنگ فشار بالای به ما وارد کرد ولی در ۳۰ روز گذشته ۲۰۰ خودرو فروخته ام و در تعجبم از این بازار تمام خودرو هایم که به ایران میرفت فروخته شده ، چند روز پیش خودرو جی۶۳ و پورشه ۹۱۱ هم به لیست واردات اضافه شدند ! پیغام واتس اپش را که نشان داد شخصی در حال مذاکره برای خودرو جی کلاس ۶ چرخ (6x6) بسیار لیمتد بود از وی ! و پرسید چطور پس میگویند کسی پول ندارد ؟! دلار در این لحظه ۲۲۵،۰۰۰ تومان است !
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22340" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81fbb27ca2.mp4?token=UX5-c4ZHQHVv_WobHvnZCRoz1KyAXefD8n6ay82GTI_WwfeORIzxnklLdmJSx1VkDHXqLorx3Ap59DH9NmLif9MIH729AcaBAcR8eYFff_SvYaAu7d8tDlr2eKw2SnYGa_knPe21UXuLWJCBOo6fqpIswgJ763PGYvk7SrK5XNdA5zCD3Ptr8FdQc6Om7o19YrYLWQlg2H1IyV0FrH8EvXk77Si1xaT_fe7o_H9IuqpJloylMoeRvbAyZMImDj1K5NVGAHapTKTTTDns7faDsl0KKDgRcaCu1F_oS8KExwAEcD3e4ziYKpHpmyTd3eK8gRsMM-LHamZ_qxpEc6Whug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81fbb27ca2.mp4?token=UX5-c4ZHQHVv_WobHvnZCRoz1KyAXefD8n6ay82GTI_WwfeORIzxnklLdmJSx1VkDHXqLorx3Ap59DH9NmLif9MIH729AcaBAcR8eYFff_SvYaAu7d8tDlr2eKw2SnYGa_knPe21UXuLWJCBOo6fqpIswgJ763PGYvk7SrK5XNdA5zCD3Ptr8FdQc6Om7o19YrYLWQlg2H1IyV0FrH8EvXk77Si1xaT_fe7o_H9IuqpJloylMoeRvbAyZMImDj1K5NVGAHapTKTTTDns7faDsl0KKDgRcaCu1F_oS8KExwAEcD3e4ziYKpHpmyTd3eK8gRsMM-LHamZ_qxpEc6Whug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از نفتکش هدف قرارگرفته توسط آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22339" target="_blank">📅 12:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت بنابر گزارش منابع محلی به خبرگزاری دانشجو، یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22338" target="_blank">📅 10:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22337">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1lIUWnF2AaxCsTg5c7vCqxKBiqbTwlUt3jpvdSwjC9hlwGVv-wIFcLYPbyInIJ2Px5Q2zafgIzI0YyGwsaZYvdRwAmPI8om0xBIEBFesLW5bCJRmUtnnGaYCx_Cs86qpm-8oYXqfwhITk2IcbTn7K1ifU81o6E0_pn1QLDjjNcpf9mCYaGcQp_z6PutTRKRlI3wDwFv5U5WwWI66UMO5d2pcHO0fSM9meWqNIRaZ3y3JO8YuM-zgJOAdFogZAchGzk0_mpKD5DkIQE56Ef4xI7660CW3jwJ5noSlU8M_8rZ67eAAVJ8YB_g_yxq4iPJrF2nYzv3igdm3csFxTR5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای روسیه احتمالا دارد نیرو های روس را از عسلویه بوشهر خارج میکند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22337" target="_blank">📅 10:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsaTUNZ🛸</strong></div>
<div class="tg-text">یاشار ی انفجار جدید شنیده شد
🚨
(جزیره خارک)</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22336" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22335">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAb Mh</strong></div>
<div class="tg-text">یاشار دوباره هم صدای انفجار اومد ۲ تا بود ایندفعه صداش خیلی شدید تر بود</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22335" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhcP32ZpKT4wMScrD9EPlACz3BW_MveI_ucazIOUskOwrsGaeHyQpq7bFwx_xjqDATIVzW2FC_Gz2V1Q7xVw9wu0mexfcE5RqFaoqQlTxzJs1cYX_D1oVE3ngvqwf4OwcXneKekDEXdZssV63oNk_PIK1tR5O0YNtveqDiIXZQAgx1Rbm7vryr1IqJBXPrBL-jEdIWf-zehQ-MlAC8y-zcr_HVNh9nc1L2nfdFUNxjDZvoj5Z9llwcdwfzr4-gJiQgOCjUb0VIu03UmrpGmgLUJUVK30PF4jUhHwLQSv46aEjf-ibIXly52SUCnwECNBGIFo25w4qpD8rdGnv0KXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش انفجار ،  پایگاه نظامی حیدر کرار در محدوده شهرستان دماوند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22334" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">یاشار سلام داشتم می‌رفتم دلی جان یه دفعه پشتم ترکید فکر کردم لاستیکمه پشتمو نگاه کردم دیدم دود بلند شده از لای کوه می‌دونم چی اونجا بود زدنش</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22333" target="_blank">📅 10:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c67d702f0.mp4?token=eD3unJv2EwR-YoiRWMWBFbyfSdx3-_6HVQHDssSBuXcgbJzYBBJbCDbL-v9hUg5ERC3KgfTRzFpeWx8BSPsJBZK2UsisBQvbFWjFrOJ22OORSMF99REsw5RDF-e5No9Rc6d2MWVfKLoO2Mh3w0hkjMN9ZYu4TOXkWlemuoV9dCApZw8ExwNjOwS4ecmK-VjtFNsxbbawP-Y0ltxlCgq6nbmpM1Tj0C-o93xBaClUBu7rm1Py9vt4HD2P9uXvTqcLSNj2_rQnlpy7LeFR0MNlnPwqzh5RqTP-aVlmvQT4RU6vHGvvPMaGX0FwcyGqvjteIekfusJDbBButjzLQP0Y2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c67d702f0.mp4?token=eD3unJv2EwR-YoiRWMWBFbyfSdx3-_6HVQHDssSBuXcgbJzYBBJbCDbL-v9hUg5ERC3KgfTRzFpeWx8BSPsJBZK2UsisBQvbFWjFrOJ22OORSMF99REsw5RDF-e5No9Rc6d2MWVfKLoO2Mh3w0hkjMN9ZYu4TOXkWlemuoV9dCApZw8ExwNjOwS4ecmK-VjtFNsxbbawP-Y0ltxlCgq6nbmpM1Tj0C-o93xBaClUBu7rm1Py9vt4HD2P9uXvTqcLSNj2_rQnlpy7LeFR0MNlnPwqzh5RqTP-aVlmvQT4RU6vHGvvPMaGX0FwcyGqvjteIekfusJDbBButjzLQP0Y2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : خوب مشخص نیست دوره ولی شناورا دارن آب میریزن روش
صدای ۳ انفجار جدید
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22332" target="_blank">📅 10:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش صدای انفجار جدید جزیره خارگ
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22331" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">طبق گزارش منابع محلی به صدا و سیما رژیم:
نفتکش هدف قرار گرفته‌شده در جزیره خارک، یک نفتکش کوچک بوده است.
بر اساس این گزارش، این حادثه تلفات جانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22330" target="_blank">📅 10:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌋</strong></div>
<div class="tg-text">نیم ساعت پیش فکر کردیم بوشهرو زدن خارگ ۴۵ کیلومتر فاصله داره صدای سه انفجارش تا اینجا رسید</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22329" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfIGzHJ5q9XMrGHeHeZEiN7nn8WXuL7z0Ymov7i_HsSfDU79jk5Ta5wnhZ_T4VSh8D3uxdwR7zN40-w8MJkO8BjVNUnPXfBjQ4kIjn53ouNcQd6dOBMH6H3adurrbto81G1BkDu846suspR0rVvkl7taOihBcmovsb7o7Es81Kbdm71TJP7kyr5NFuKzElR9h8g5pX4CmhnBORdk4FjliA-A0NqfTY8eXab1dt14U4Wb5hhwffwkMLuph21nMaYDZVHc3o_kp2uq0CGJp2MUQsziacnhso9HPreOlWAheG9co9OiUvKTR7eW9FouA3_3S4DElPtcm_PQbTCoiAoVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه صفه اصفهان
💨
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22328" target="_blank">📅 10:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۵ صدای انفجار جزیره خارگ
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22327" target="_blank">📅 10:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSXs0dR1Z-y52zfTr9Wg401eW747x9krWfReD2oK5LIR3RoOwSHTGqdJwLSMJMOkbJh6dO2ozSGak0TnG7CqmQcjSkKh4mE-jokIZfGlPOsZpCVvclv0v0qeXt3ivCoNgQ9A7QiiElZWhHPZX7OGbIJ0LHQ5_wFdedNLKPd8wuu4_aIcqAaX1wjO4BF5x9SWBVnH7b3Ka9wtzdjJdKjUO8WIsznNq3t6JqqLooFBfqYOtiJ-InxCblzMEfrAwjn-Jn9ZPG20aatRohXigJEijfAy1l8ZF_NxcFsJFXN3Um6swoMCoKjH9xwmrAtfpzcgOKBkIzJM3RTOqjd4mFLOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار کوه صفه ، اصفهان
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22326" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22325" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت
بنابر گزارش منابع محلی به خبرگزاری دانشجو، یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22324" target="_blank">📅 10:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe9vqCx5kEv4gTHz_aaE8Bwp9Rm430wsr-l75lcZXpyuVXSw3t-PDZXWoRn4ZXVXy6YKwWSGhHc_i-8lWiNg4R0MKsqX68UNy_RBFF67VGhy2kcACDGOwDrK02t69O8947L7p0SB19ToX8FO7aDIv0cenYxa2dtHnNosFh4zP0cRuXDp9fSRjgFOt2NU_gnjSHpotsEImxpSdAN7XfWPUCbe7uT_zD5k-M-LXiANOn8SbNCpIcA3ofYWFTyWT5aqrPZDRJ734dimQ37U3Bo2IMdnmGO2ICDO_XQzZz_ca-NBU7gj-Oxl7KLoBO2WWWfzQMbN5w-Md9Xvabfoe3KlCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اسباب بازیهای بجا مانده از کودکان بیگناه علی الطاهر!
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22323" target="_blank">📅 09:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیویورک‌تایمز: ایران فعلاً حاضر به پذیرش شروط آمریکا نیست
طبق یک ارزیابی جدید اطلاعاتی آمریکا، ایران بعد از ماه‌ها درگیری نسبت به توانایی خودش برای حمله به پایگاه‌های آمریکا در منطقه اعتماد بیشتری پیدا کرده و فعلاً فشار واشنگتن رو برای توافق کافی نمی‌بینه.
برآورد آمریکا اینه که ایران احتمالاً تا انتخابات میان‌دوره‌ای نوامبر حاضر به پذیرش شروط واشنگتن نمیشه و ممکنه درگیری رو چند ماه دیگه هم ادامه بده.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22322" target="_blank">📅 09:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش های  زیاد : جنگنده ها از مهر اباد بلند شدن
سلام صبح بخیر الان جنگده از بالاسرمون رد شد تو جاده آزادگان فتح هستم تهران
سلام داداش
همین الان شهریار جنگنده از بالاسرمون رد شد
هنوزم صداش هست تو آسمون
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22321" target="_blank">📅 09:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیویورک‌پست
:
ذخایر سوخت ایران، تحت تأثیر تحریم‌های شدید و محاصره اقتصادی آمریکا، ممکن است تنها برای حدود
دو ماه دیگر
پاسخگوی نیاز داخلی کشور باشد. بر اساس این گزارش، کاهش شدید واردات و دشوار شدن تأمین سوخت از خارج، ایران را با سه گزینه روبه‌رو می‌کند:
۱.سهمیه‌بندی شدید بنزین، ۲.افزایش قیمت بنزین یا ۳.ایجاد بازار چندنرخی سوخت
.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22320" target="_blank">📅 09:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">در ارزان‌ترین حالت محاسبه لیست ساده ترین لوازم‌التحریر «کلاس اول» نشان می‌دهد امسال یک خانواده ایرانی برای تهیه حداقل وسایل موردنیاز دانش‌آموز خود باید دست‌کم ۱.۴ میلیون تومان هزینه کند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22319" target="_blank">📅 08:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏خبرگزاری سعودی الحدث : نیروی دریایی یمن دو قایق حوثی‌ها را که قصد داشتند الفجره و بندر المخا را هدف قرار دهند، منهدم کردند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22318" target="_blank">📅 08:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏علی مجتبی روزبهانی، سفیر جمهوری اسلامی در ترکمنستان: تهران و عشق‌آباد درباره چارچوب حقوقی دریای خزر در حال رایزنی هستند و مشورت‌های دوجانبه مسئولان و نهادهای دولتی مرتبط ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22317" target="_blank">📅 08:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیویورک‌تایمز:
مقام‌های آمریکایی می‌گویند حدود
۵۰ نفر از اعضای ستاد مشترک ارتش آمریکا
در چارچوب تحقیقات درباره افشای اطلاعات محرمانه مربوط به جنگ ایران، تحت آزمایش دروغ‌سنج قرار گرفته‌اند. محور تحقیقات، شناسایی عاملان افشای اطلاعات درباره
کاهش ذخایر مهمات حیاتی آمریکا، از جمله موشک‌های دوربرد و موشک‌های رهگیر پاتریوت
است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22316" target="_blank">📅 08:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی ضعیف‌تر از همیشه است و سقوط آن در دسترس قرار دارد؛ این حکومت برای بقای خود می‌جنگد
@WaRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22315" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUislCaJqHsW2ALgzPU2X3X8VcUk-lKqfy2YRLaUPzSROWinXFfJ-1aRMETLRcSFDKP5H3cMbQXgy2yyDntTshu16C8NbzC6kRogxT7FCNt0-e4Q6n-X4Ea8oL_tf00oRqDJB8JecEY3mmzIxZJOWGEJlinLMFxlQb6NDvCaEGt-BQiHZ6CbG2pk4aZd-ySlS_H_Dx9n-FmMd0x7ry5_9un1Y_VFyMy-xCh5uFN1wwdRSFAy9dgdUp6OeUyNSfUYoFx0ZMy3Pig1lAsCA3Ogn9tAUBc4YwnoKfdH7XPmBfyzBk8jhG8faDuoZRkuhwG83vltpThYwukhgo9rfvhjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی حامل گاز مایع "ال غشامیه" متعلق به قطر، مسیر خود را از "راس لفان" در قطر به "الفجیره" در امارات متحده عربی تغییر داد، پس از آنکه این کشتی یک مانور چرخش ناگهانی و غیرقابل توضیحی را در مسیر جنوبی انجام داد، مسیری که توسط ایالات متحده پشتیبانی می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22314" target="_blank">📅 23:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هم اکنون ۵ پرتاب از سیریک
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22313" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22312" target="_blank">📅 23:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c89a571e.mp4?token=TcHw5apeClH2c6zSaPEfUXtZmx2zK7eS11KTCR2j9yjDct9YKqdgOvt3lvkWrSS_YMSQMrzQe_J0PBeb_EX-A7pLrw7bBZ5dHjATVzqhR7_djypxfEiML7_3Jnx_rsQdcXzeAkDFXEQyvgI-cnnqiMl-Q4yIH6-F1T1wGfgXKzECxS7w53ntboSsQkaAS5BgiACLVpj2wiVnGG-3_Zkatr-Ey-1KuSJi-PTMn424o4yEzBzU7L0iDY3ysVVXYvcOrAt175ZXHCNeRGX1z1oVH_rNPFFD-xSNfW8zmfRn5MEE65r-xeHrBTPxLEJOpqxRCO-DNrrOyNhNUE5QrOqTuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c89a571e.mp4?token=TcHw5apeClH2c6zSaPEfUXtZmx2zK7eS11KTCR2j9yjDct9YKqdgOvt3lvkWrSS_YMSQMrzQe_J0PBeb_EX-A7pLrw7bBZ5dHjATVzqhR7_djypxfEiML7_3Jnx_rsQdcXzeAkDFXEQyvgI-cnnqiMl-Q4yIH6-F1T1wGfgXKzECxS7w53ntboSsQkaAS5BgiACLVpj2wiVnGG-3_Zkatr-Ey-1KuSJi-PTMn424o4yEzBzU7L0iDY3ysVVXYvcOrAt175ZXHCNeRGX1z1oVH_rNPFFD-xSNfW8zmfRn5MEE65r-xeHrBTPxLEJOpqxRCO-DNrrOyNhNUE5QrOqTuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: مردم آمریکا چه زمانی باید منتظر یک راه‌حل درباره ایران باشند؟
ترامپ: انقلاب؟
خبرنگار: راه‌حل.
ترامپ: تفاوت بزرگی است. فکر کردم «انقلاب» جالب‌تر بود.
نکته: در انگلیسی، واژه‌های
Revolution
به معنی «انقلاب» و
Resolution
به معنی «راه‌حل» یا «حل‌وفصل» از نظر تلفظ و شکل نوشتاری بسیار شبیه هستند و ترامپ با همین شباهت، به عمد سیگنالی گفت انقلاب.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22311" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دونالد ترامپ درباره ایران : به شی جین‌پینگ گفتم لطفاً در موضوع ایران دخالت نکنید. چین واقعاً درگیر این موضوع نیست و دخالت بسیار کمی دارد؛ در حالی که می‌توانست نقش و دخالت بسیار بیشتری داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22310" target="_blank">📅 22:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درباره تنگه هرمز: همین حالا خطوط لوله در حال ساخت هستند. مسیر زمینی از طریق سوریه هم در حال ساخت است؛ در واقع، این مسیر باز است. مردم با کامیون‌های بزرگ، کامیون‌های عظیم حامل نفت، از طریق سوریه عبور می‌کنند. مسیرهای جایگزین زیادی برای تنگه هرمز در حال ایجاد است. تنگه هرمز دیگر مانند گذشته نیست
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22309" target="_blank">📅 22:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ درباره ایران: آنها رادار نصب کردند، زیرا ما قبلاً آن را از کار انداخته بودیم. حالا ما آن را برای بار دوم از کار انداخته‌ایم. اکنون ما هیچ فعالیتی را مشاهده نمی‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22308" target="_blank">📅 22:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795f134b33.mp4?token=WTndVguvMrOUxZaO2i7JrbZTnoCGmogYdyVofnPkagSLZLUe0V1vqxBnjqxtDTkPkkyC7CKuehwU0PlxFCvtCXUlMuklV75-jBe25di43tiMELAhbh9Yq9pta9HDrD09mhFzgGGo22p_7rvNkdRKSGbkA5YxiKEyOgPgmIFRDrTVoMBMG305r6Sm5SZATtNM-MuhmVK6jLHd8KSwR2dEEqTBiOE_YGcDylMuJ38lT-BoM3EUP6BHIK2WDShjGbYmF94vmC3Zv2J8MLfCFpfAhIHcITP3xcc2ADGOVHRlY5jWZUBsG2GETmbFnmfOdVblaViTWE6XvgdjfRxGnyxFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795f134b33.mp4?token=WTndVguvMrOUxZaO2i7JrbZTnoCGmogYdyVofnPkagSLZLUe0V1vqxBnjqxtDTkPkkyC7CKuehwU0PlxFCvtCXUlMuklV75-jBe25di43tiMELAhbh9Yq9pta9HDrD09mhFzgGGo22p_7rvNkdRKSGbkA5YxiKEyOgPgmIFRDrTVoMBMG305r6Sm5SZATtNM-MuhmVK6jLHd8KSwR2dEEqTBiOE_YGcDylMuJ38lT-BoM3EUP6BHIK2WDShjGbYmF94vmC3Zv2J8MLfCFpfAhIHcITP3xcc2ADGOVHRlY5jWZUBsG2GETmbFnmfOdVblaViTWE6XvgdjfRxGnyxFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: ۱۸ نفر در جنگ با ایران جان خود را از دست داده‌اند. ما شاهد حضور نیروهای نظامی برای مدت زمان بی‌سابقه‌ای بوده‌ایم.
ترامپ: بی سابقه؟ مگه نمیدونی ما چه مدت در ویتنام حضور داشتیم؟
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22307" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a52585ca0.mp4?token=bSB1Bqf4eGfcZn9sXZ2FlOn5rNcdvIv3JCYpta4YcyUwu-eqX5qbHcqYUwFX5aKLUgHQBTA36k2SQgeEs73j2-1K6P_GPssUeQ4slSyPxWx63izORgXY1i9JlOWrNuYW4BTw0Y-1JGt2P2Y2vP_oS6NBLeQUJVAPV7QYvbfbE_ohF8mxZS-poB4DzHWGazXhGQQGJmyRHKwvadm2dSaa97qdvSBrVFfv3a48FY-qZbQBnP0H025RFszHmPy6GH67GsP72NW1CO4BI33NUBQwC7ciV6sE6sJfh9rIK90htpcEBuHBhBbXWGcu70toZNazjuba_tPeIVVSDotY5VmL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a52585ca0.mp4?token=bSB1Bqf4eGfcZn9sXZ2FlOn5rNcdvIv3JCYpta4YcyUwu-eqX5qbHcqYUwFX5aKLUgHQBTA36k2SQgeEs73j2-1K6P_GPssUeQ4slSyPxWx63izORgXY1i9JlOWrNuYW4BTw0Y-1JGt2P2Y2vP_oS6NBLeQUJVAPV7QYvbfbE_ohF8mxZS-poB4DzHWGazXhGQQGJmyRHKwvadm2dSaa97qdvSBrVFfv3a48FY-qZbQBnP0H025RFszHmPy6GH67GsP72NW1CO4BI33NUBQwC7ciV6sE6sJfh9rIK90htpcEBuHBhBbXWGcu70toZNazjuba_tPeIVVSDotY5VmL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ممکن است خیلی زود به کوه کلنگ ضربه بزنیم اگر
اتفاقی در حال رخ دادن باشد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22306" target="_blank">📅 22:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233e0dbdb1.mp4?token=YDJCf25sV7yhQMkiUiEvJw1rcutsMTAncYnzL7IlYUpETTljB0jXasux8yqGoKwtn7KHfISjhQNiMH2Phap-uJP8AaxMArA25dLPuvU8r7nu6Kpe_GrxBJkRCXGD-7y96CYAyQ88UWWsjGPwLacziXCPNMkf0Ff2tLL9FBXhNexIdepwlZ_Kx4xj9H7l97J8T94zkgu7ciIY3679dDkYl00mT--KPR-Th0IpLFRVcWXvokc9OkSH_xW5-htr79OmnT0uD_N1FPwsD0wO2S7V1l5uGYph7JT-m8jomeYlPbGEdaKhPNscxUEmpr-pYHOFcvM2VnGNseX5nNNj3oTveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233e0dbdb1.mp4?token=YDJCf25sV7yhQMkiUiEvJw1rcutsMTAncYnzL7IlYUpETTljB0jXasux8yqGoKwtn7KHfISjhQNiMH2Phap-uJP8AaxMArA25dLPuvU8r7nu6Kpe_GrxBJkRCXGD-7y96CYAyQ88UWWsjGPwLacziXCPNMkf0Ff2tLL9FBXhNexIdepwlZ_Kx4xj9H7l97J8T94zkgu7ciIY3679dDkYl00mT--KPR-Th0IpLFRVcWXvokc9OkSH_xW5-htr79OmnT0uD_N1FPwsD0wO2S7V1l5uGYph7JT-m8jomeYlPbGEdaKhPNscxUEmpr-pYHOFcvM2VnGNseX5nNNj3oTveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22305" target="_blank">📅 22:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آکسیوس:
دولت ترامپ در حال تدوین یک راهبرد پساجنگ برای خاورمیانه است که هدف آن
مهار ایران، ایجاد ثبات در منطقه و گسترش روابط میان اسرائیل و کشورهای عربی
است. بر اساس این طرح که هنوز در مراحل اولیه قرار دارد، ایجاد یک
ائتلاف منطقه‌ای با حمایت آمریکا
، توافق‌هایی درباره
غزه و روابط اسرائیل با سوریه و لبنان
و همچنین
عادی‌سازی روابط عربستان و اسرائیل
می‌تواند در دستور کار قرار گیرد. آکسیوس می‌گوید تدوین این راهبرد احتمالاً
چند هفته دیگر
زمان می‌برد و هنوز جزئیات آن نهایی نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22304" target="_blank">📅 21:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شبکه NBC:سربازان آمریکایی پس از درگیری با ایران، دوره استراحت خود را در یک تفرجگاه گردشگری در تایلند سپری می‌کنند؛ در حالی که فضای متشنج ناشی از جنگ با ایران همچنان حاکم است. این صحنه، تضاد میان فضای تفریحی تفرجگاه‌ها و وضعیت آماده‌باشی را که ارتش آمریکا به دلیل جنگ در آن قرار دارد، به تصویر می‌کشد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22303" target="_blank">📅 21:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قرارگاه خاتم الانبیا : حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22302" target="_blank">📅 21:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقام امریکایی به نیویورک‌تایمز: ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد ایران ممکن است به‌جای مذاکره به دنبال طولانی‌کردن جنگ تا انتخابات میان‌دوره‌ای آمریکا باشد
تهران درک روشن‌تری از توانمندی‌های نظامی خود پیدا کرده و ممکن است در حال بررسی یک تشدید قابل‌توجه تنش باشد ، ممکن است بار دیگر به سطح تنش‌ها در ماه ژوئیه بازگردیم
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22301" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۲ اسراییل : امشب جمهوری اسلامی شروع کننده جنگ بود و به پایگاه امریکا در اردن موشک شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22300" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۲ اسرائیل و باراک راوید : مقام آمریکایی می‌گوید:
«تا این لحظه، ما از هیچ حمله‌ای به پایگاه‌های آمریکا در اردن اطلاع نداریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22299" target="_blank">📅 20:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش‌ شنیده شدن صدای‌ انفجار در اردن
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22298" target="_blank">📅 20:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHdjoFYRAP4zJua4P9eJRrmTqjSuqKtp4tUxtJYDi4XYaCZG7d8NiE-_viGuiRjnuNtRi5pl8uoim0evzkEtL2Nw1csQt1kollb4Y-mSP98CiSPSDa5IkybhXdGrvkqB2-iPmp7x7Eibuze2N-R7que3QKQPTWKtaZ3ZBLQRZWaISAYhqGzdRjmD9_CZj9gOVtZG2qFNeJVI4QauyKPGHmdYN7WHafMSX0qLT4d6Z9bhQl6IoObjsdNGRSf1TJELWsqsOW9Icndlm9hpRoMiuikehdGYP1oVgwu13HOP5iSlGHz_7S5g7Jbr6iBamNpc7-hNsPbAMP6OJBfEZHG-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: دیوانگان چپ افراطی، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ این جنگ را برای آمریکا پیروز شود. به عبارت دیگر، آنها ترجیح می‌دهند ما ببازیم تا اینکه پیروز شویم! این افراد بسیار بیمارند و از نوعی اختلال شدید به نام «سندروم جنون ترامپ» یا TDS رنج می‌برند؛ اصطلاحی که گاهی برای «سندروم جنون ترامپ» به کار می‌رود
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22297" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
