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
<img src="https://cdn1.telesco.pe/file/aTs6AYiHKzg1q6H9cfSyC60rOeMAYMfoy7ejOjMGGgrx6-5HmBMZhqt0E3aeL5cIUO4as1PyyriU4n5PG19TwXSdRNDi9fSjloqlEJxns5Bj3e9b5g_dRfcCEGROHS84M3_x9gBroTDSOQuDgBgiN72PpzsC_icvVIUnoNH-x1wTUL9GuYAqbx81DmDRu4_DuU-pFe6S3XwOwROgaWRwR6R5ERCeclnC2mWd37ZBpBOCOmIc5pGZS_g7Gz-XYXgF6kBgdTOZdB0EIbHt1tE5JkFQ8IqHYhX6qNLWilMQfO56Nc9RYfRTk66QMp1zLtzm24y6R5weSGr1YKemXwERNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.4K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bLS7JHQPsRP2lzGlg0m73VT6iXUXC07qXTIaxfk14823V6My6ocJCprJhg4oxjdpH8EnIrCWsaVCSYTA1m3Q1jeUdWI_O5RYFlZjlmWgOYYxueA0cIfsRv4LRRG367xQctnAd95D76yzpGHFpUlf-DwN8al1DNloisocf9HcUepByeJn3Vg8mmNy228lQvw8iDvILnlrn2x-Ra_S8QKJGX4Zi7XqIT5Pe9oDtxJpPKJ6PuYNrznmWPdZWdHZkwVL7mcR6AuahEj_XIdwrHrKOV0hCoMgnW7fTdjPdSl1QE0x3GVO8eKj83mkHTZoB2_5OQ5odQnF98gqsGPtGsF_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UYWq80mIP56OM8A3qCz4fNvbM-VI26ier4GjhkEnnc3e-waUuwbnkYH-CCH6rbUg3HjWYaD-lEzbQAsXGPAT7bOqU4n2bF0XWjApuIC3HKzPtarSGuR0IQKnSjjF5obVBE28Tz7mSi6QySYHv5iD68VyREohHW2ce1s2lsokwg_kLTmBVMqI_JflJLLa9SEhh7LsBwr-7FE-9NQj06SGz3ulEraS_NvzpkVWvuKAOuUgdiqSEl6VF-IlDoZ8nEtQ9gTkStmo4EU_q-BqA-vpwxp0IXTo10dnVnmIrFaisgZtyjSRYt_M6J6UhzHDpgZ8qDY8I53OsnvMEFnvdHYrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mssPgqddEiO8nclrBfkpyjWXKtoxCvQBMeSSb2kD479ryINm5I-w-fQBerkOuRov8wWZfo4q0tHEdPblaAPNFIR-vYULrRtg1g0lYwJqc2A1hhBP-HFneM4HV9cK69aB6IxPC_oUcqEbbLh37EJ-Yphy34fvtKjg_q3UTrPcHkWcFAUdbTsY913zHsrgwVzcqiI-cdHAZLJHjGNgD5dstzPX5Llnu9J_WPa_CYwTn7X0ovQtW0VkaIdWBsAk8H9uqsXD8fiTJsI2cLxw3ql9E6UsmSpEneEeNxmlJGZWcNUAb0IR_cKnG7PAWvjTaqXykqPr-Yzy3NQE-6uBvX88kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JnK0iDHBV5_j8dxUdu-cIlRuybsL0xoUP_VstHq1Bvjugqc4VfojCwKDl-WkbruYtGNj472lQRGTHOHXcwzKXsU5EnOL6tcyd32Esv7yh-L4p3Fy4HuLTTKmy0nvnYveb4LOvOt-iJ3jBc4x6BsBeBmHc137J7h2UIdjKK_gbVLt-NOAJqXGlkbnyekVQ4jdLaHQ7OxeqIZCRI2nuxYPWriOm9hh7LjX4KGMzKNUCS-i8qJmUgf1h8YVDXwwGnVYBJOGMRsD2_N8HT-FqW0-zjHmgBbtSvDp92cmBp3qbc5PgjNWSDtJ5w2NPUWa5VNtkE_X7svD_I9EIMyDTQUz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PzKuePB7F31YqeH4K5J3595QeHLsdoPtV7vgVusWajLIeGuRl0BKTwpMLoyA3MiuPAzynI3GOwKgvTBywqrk9X_8MeIALYlZwfayq_A7oHQX-PJvYmY8SwSXCnyX0sbXxGCGZiVU4mnr5Lhlz7dsLrhmN5iXmerzOUtz7V3epaKU0qx5Rrdqvcx-m4K4JO7JOUOzWAZYjA1bL-8Tl7VF1a1UxxeoDLIGTe68ae3n25uJODbN8EgjrBs78SueQHPXbA8i_tUcKoUeE4Icb6msoAaedgLMZk4lFCb4Lxc0ml6q2lmaSOzpz0Xcwmojk-H5SDDYjElJ53GEc5WCJCHNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nr8MdNoL9p1x0-mX8EhOPMR8DpulxwX_tAsq2p0XnACNkLLwzmtWxvRvxXEqq9sMdWJ6dg5OjrPNVvXcY-G0Ikrr5ojCnScFGuI0rtGTQzBtN4zgahV1zJksX3X9Ca3XAl7zHrjyLhAT-I0wUhw4ibxx6V5uguy1uw6Pfk8c4YVnt2vlT4Hpvm-wXSLQtxClurMnL1LJ-FmlFYePccllBDpFdCmmvU_eGg7pHARA1z0ML0zjBMNOBZyIvndAMaUptQzBzqmjlHRwpF12YLzELeOCNBa1ElA7-Lx0TJmMoh7MdoLV6ZCgY7eQ1Kmy73F5c3o3ncQcT5gmCoylTkbs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvzEQXUibxr2LlPFRM01QUlfqKylHmljZyDXxoZYptR22w6_VpYOkZL2GsRPFcWojIe_TeqqYKLjimcwKNhmuve2IZo1GhbUosgLgdc4rO4KNAD7v06hDeKeuCSAcBIAmeNbDNfprzwOvCRO-7Ot7MFdR1ppNMAfvkz78UjfNTM4sQ_cIaH9XnQsJiiEu5s6UH_NZ94VHO_fjcnPa7yubqC7L2pDPa-FFRqliRYDlTGYS_P6atPnJpp4d5tHPceoeaTKqf_9SHhrZZXMREk_GnhdZHEac7ScRN3tjy5alfUm2B_77psimmTibwlSS8mJ5q-qgYbpVrcC18-FCeNWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVPzilIbGfJ95mSPSihKvK29BkO0ABkpi5qwsF4FEAy0N7LmHyeYchifR_SztBbQHlEmsMTxkeGYdXFWhoMwae5F6NKCnnF7Tnrzwz8WQJNo8rhRwG7dLtnHHiCLAYeKYl47oExg4SELbOQm_Q7QOsct__2ArMg1dFwE_fYLWky7_f7szbMje4llvDP07rMLoQM7oaUa6i86d1SgeToSWoUi_d5c2Ncvr-uDxcLTO2frVORxWl7jVPIuVfuvXIhNzxqG51rijDtZIJ6YLzfLsl3nmBOCO5X1aRQKj1fiCtsVaLwtVflWIDCkiUz14GaoNLLe_7k4712TUIvpgggmVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BIeQ3-y_hwkhHJ1xMZs03kiTGZ5XxOGrE_vMgGgFjFVY4N3RaA_6dw3zMIgFaekJVZh2c1Ei8QRTx9i7U16OZHk-ay7s9uGftsdBcO4hycKMJJl2indwOTcUI0NmpnjJ3p_HVxfrkOrvh09cFUKGFC2daw52DD5UUgAv7h9VNxweOBgLe-XqsfTMb_yLlBnYCaN9ZTICygYBm8BVL9_knBx_Uz_jziMJeq6OMspoqSwXDOIUrgKbGtezEnHBGfNm8IevikwE_U8RvVuvjK45hC884N6Fded2-AX6F7vGVN-qwigAmyCGpMcqdxWqudwTm52YMfaj6-0ORLZyd-TjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/snE85oaRbmXCr2J4dx_ZBwFGO-TLLWc1ea9BPqSCa9-C93-yrrGO1URMZDZ3LfBzcp55uO6wEQ56o5M3rFUj3s2G6PCsN0vzCYaAvh51xjC3MD8EnpO6qkrqUFo1MYVFTD8cO44iFnTz6jrU3yY8GA0mpP7bv644iPBP7JJhLkfhW0uusAOfgvoL5Gz8AFmoHudY2C7m6jlMwwnZBBHAkML-WbzUKu53TTA3W2XL-y7qLrT4bUQ4DDbmk6drAAj-pE0shZV3n9VDzh1Ed3NtkiDvTaC3pJL9QgORxmyRlemDh3h3pitnmRSn6wFhXgyGd4uNMVnnUCCroWT0p9VnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eq2m56LRZEL-Rtb7YHMMN5h2ZmuzR-hYbcu4bDFcqasAEr5arA4GQkotspP9Qqq_7zn1oCQwO9eNgGEEhELZJbvClSGBwhwhJvOkUmSTuYYpLr7GPK2fFS4utiTaAHiAttbeKHGAnuLcJQgFgPLik4LQANOpBUtbs9cB885D4p2-PTqDKx1E4jQXVsONZWk0rlerMOqMZhPuK6mJdiGc0DQMJMUb4RxhV24dKtwJc7qqU6pp41Je9qaqMwscVcCDOkDyOmJUb2wuWtTmrrUn-x0PVJE5HU2k-3PtNAN7ruuW8fmA3nJADgQEz1jDRFo0AeAKnhLzcUHjtYA-U0kCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Be2WvZW-zCYrzVxqA0kJ0kTdz6CCKxEhHlRfwDC7xZ7H0SgwmIYPBGzmybhr5rsXaDsgXayF_xnIOPVif8o_LbJkMhJpdcHNbVbYrvY8XAlbUleeeYWvlNAE0jqb9TEH5FWNjKOPeVWfOihe7BPx2VfR1enM3ZELtev6jrFhG8glagUB0nyNS8j001BGP9HuKjBh8qnQOLZ1-N1QXlVmeVYV7arkADU8Rcg0W3g_0ktcGjYo64yW58h7q43otZFbNq5yfmn2g_VKH56JHPS7ux11o44G1Hgk24hMtvGiFAQSoBdI60krbD-Zh9PVxNQIP0QyhzJzo1yvt4YCmS0p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4rt8iz0IpfmDjp8Bgq4ue0GNO_dreotjl1Y-AGYBw93DvwkuNGHtVWBc3K0HsjfBpYgqHv3uW3biGnQAaPE36N2e1ujtJaUFxU5hjAkIIQjeyBEXUeH1OiCkq63IFOQrcl86jmNGU4DOC8JWToBLkT_3EQntYRLeuaHVnc30xnwp3A9EB6AlKDc7tWhOdRJqmHwwW_yp0Rs2aVwxB4wp5CXAZXvuJRJhntR_4eI9etR5DEoPXsWbrLaHLDV9RULyDr9tOBs5zHmCqgy8U-BHOWM-JReO4Fbb9W-DzICBew3p6zWo3w0iz9YXsM2XDhOdQuFZ3k1irkgXoqYHW7xVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MuU6JIuwxGFIX8ASVwcOPhUaEGfyvu8vvGtLQwL-JqF7nS8iXDYopD7ff0wRZk6bWx-6T5ZGhtgdFyxIBDvRyCYYDs4GgG9ateJ9__EnW2PQwCkE0SPftk2jqeIIaQq_jxInM3B2Z7IaF1R5Wh6Pel0cnK4lDs3hjHKr106N0NpCU1THIapEwyv7aq6prXizWpB4rUMT7tn6Gq2QCrP5mjoXWtmUPTBQ14Vc8AlE1-BDtQt1zYr8rs2rJIAb-7fIBdRjGhsK45Y2W5VPFPDG7VWg3G3Y1YBRhMrJ-ioMqcPCCmXAeVkw39CQNNhjzcQ18-FgWY7HpGFWDdfo_l-6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RDw-KDWQ4KZPiC0zMVhH0FamlQKDy5-zcVTXVwZDzisWBDD0epnY6eB1Dy3OV4aRXJ9nEFas_i0zvriPK9L6LDo4dFOHhVsxj4DoxSH4xHWoFW5OHfNGGKRzKGN5u3Ta91_TWFzaEMJU909UaO3NhO34dm-VEtBHFi4ILbgaiiyJJHGTl3vfoL6hNCvuYZxo9m8ORrX-veHGPjUarP0cO5trFZkO6KrTnkbC1y1JCGCbJX4C5OkkeJ0LDR6xVtLg_dFh08PKEKGfJNOVP9CUvDGhI37QhHAYlV3qGLMtxjQhnJ8DTRxrXnySqGhgSN6Bq5jJ5vvgqOMKJ2NSQ-muUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kf05zI-zWAXbbAVrafwW6ZfVoxXRYmLzDILiJ_zxyDAG7XJxTJCvZ8cK_bxR2NsShbwGv6HwIsiuwIYRCWd_V1Av-QWnWBK9ESkzMWRyB8GwzrLJcGRplB-u6lshR5Ik0x2JXLzuzRnOoyMHlYBkeFQ-zaiBstg9mPFeeNkVVHtnhWyAUEjjvHGEYAEhgZwT4p3ozp75BwqoWe4hFILFDBhmalci1JdPVheYUNmo6O2UJTGfGqWKdaQVLkLDKXmLV13ZnQeAkxFeQCr884jy88PKTHmuArmXVuGRwfX1C6-CpOxIywMPZUxEx2H6ivPSeffIHOJNynDVaC6JI2DOEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Hlv5HtCJeuOaRNzco4N3ZhySh3RfPGfoXEMPidPTUfXF8SYYJ0JAAGLZfdp87KvwBbtB4fOScwms_C6bFxr4PQ7tutGo7hNpcifGeoy0Oz1jRuw1SBfbvLR7yWN5jl-NWwWpakHm0eo4SfH6EI-rwFeNGWgENRygXWFMLzforHxVELP4w700_2WMkbXstU6SYzrRtT38F0gOtP3GuE0E8yIu4KkSLsMWlZw7tTNNA7VWL4SgQ_udT1yCAsGi70EM7Jqk8jt2htiO5ekVmbCGzosxmAPdZLkOb0BB2SxNY9vKNEvXrp7_P__cmhWlq1ooGI-wqxxZi-j_sNfAEc-mGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Hlv5HtCJeuOaRNzco4N3ZhySh3RfPGfoXEMPidPTUfXF8SYYJ0JAAGLZfdp87KvwBbtB4fOScwms_C6bFxr4PQ7tutGo7hNpcifGeoy0Oz1jRuw1SBfbvLR7yWN5jl-NWwWpakHm0eo4SfH6EI-rwFeNGWgENRygXWFMLzforHxVELP4w700_2WMkbXstU6SYzrRtT38F0gOtP3GuE0E8yIu4KkSLsMWlZw7tTNNA7VWL4SgQ_udT1yCAsGi70EM7Jqk8jt2htiO5ekVmbCGzosxmAPdZLkOb0BB2SxNY9vKNEvXrp7_P__cmhWlq1ooGI-wqxxZi-j_sNfAEc-mGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHxg5LNArtA09_fWadAqPf_P-LO4UCrp26m6jzASvO-ZHYoLAUnt_wWIAn22pf0zNfvJZquyuWhNz69ufa72ZbvCom1s3dMcsYQQ28-kB8pH2IDXRLAI9ySqiqrSRbrD7ndkh1OLngYBjjGUqsWnFxw5Fc_Uk-fqZ1vbx_8uLbsDl5l3S7ZGf0sOhMsvPLKZk4YcX3gQoo4F9WU3KUy6GRZIixL22LBSG6HMgavOgN3afOkh9l_3CuNrBucI21vTxg_vsYgAZaq2jr-aj0v3ueDhgC6iP5aw9Bvy-zbLow1Tn94ajaGvEpYHu4gBQa3BvZ05F1M78lLS-ypLSVufdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9xzEk44P5I5TW37CrnQ7TVxDSoH_irmtUjNPsyBP_f1SArR6-0RdhqkxNKz0ECBEUGJgfRNGo1-8yat7V-2M-QLxws2zgrbxbKedsNBzTlawR2q16NfqEocpFsiLqvlW31hpDIZSFqxPoAeJxxL4P_Oe3xhNA8wjLhp2Gc8513KQBm4KOfzH_lHiQcXcmiT9JFrIPMMdZYbKwD8ZC7eCuPp-7I_L8oik75rIEH_qm9oeLp6Se38BavmF9oR6ITODYcgZ7aJocCYRgDGvMsoQXTsOwj8AOKutB_ejLiETuFHFuWWt6TKnSwGjyfsCI1Qk2l_qu56Qfkb_pcGtQwRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QqPUx10X3xTiyOlr_Y2B1Fi9ZLP3f1YdLLL1rj2JUQ4dzRs1G-hRR8BWoHcYujtsVI4GQcmcgAW84bf6TRypqKAceDUnmtDtnXRjAeSr6I4Oo53_6UQ6EV5Agjhn8DipjDaxWoBEi-nOZdGQWzhgXJx0HnURwrs_HTpUO2F61JDYL5Udd4YGJ6Zj_m-hGmCW9wz3uLNtprTXNcqQcCaE3EQcl5lPbDPSyJzaBzrifDDBHSa8j7vP7Nw-h3rMiBZ9W1-a_smPz2VKOOtLxd1h1XojlSkea6fXEUHT4EYXsqW3RkPBS5R5l4rvqo95t8hhzj9MEp-FJmdBBpAwYMKtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QnN1iHOcnKw1cvQvZWvfiE4ph3ivWvXwqDz1ujyuYS9tHoe0AOGi_RMYj3dUEezMENGxuQiAoa7XqX_5MW_8mBCx9wBE6CrV4z81JAa13RGw8QNBvD9TuEuH1eLqQxilW5v0HPJrUDRA7YGhHvTwEsDrvpPvBp5saJS5ooB-xmnPSMIR7D4btDLhI904bZuasfRKO-u6NTFYaJTsIlaJuXZ0kErKGSscMkFSaEEYyMKwtK14NBkbJbv_VCpNIzMtsavskbvj9QvmJAl7tHeucbHEk5a7vUVyks7UwZnwHNVB-msxR53Uo7hhoZIJiGDmLKvKIslOKydFmNvbmpKTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/heDKpe1Dub814HQEUCPJnftK2IRvTHMDJKvHte9NY3WIU-QA2-7YJ5qm2xEsFQtSPnUVW2wVNaj-S22Wj_7rdQ7x5xmPrkAmAFpfzp8deMncZYG0rnFStvV8mYfABnbmDCX88o5YCSn7YouWXzH9H0pk0-9NIY5ZIL8o_gjdmbIoTX3UKxlryAIe4dXwV354f81jhXhm62RVnaqO0lyxn5PaGi5gnDKnJVWuSvqI0JzmpZTC-gQMcesfDQMfysYmDbRlRcHyIsqsAV0cBVrytpyYgO_JiBtPVMiRDvwNOp9fulF5KOv9hl50G8SAgDRARC8_shFog436kAElCazg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNke6sqTTe9V-TrEWeLR2MCA31oapNRXXov3tGai_NxHk_2r08fibNFSJvDpJHpcJkvHAePM-YhIgV5x6qonL8wgHoHZUtxLRQJ7BsobQFknj8IudvKqp24bv8hHDpSLVHeDgm3W7O3a5C2ULHFxcr2mRiOaYptYyvTG9sDtjCmn-ES3EzpBrCLZo-l7C_LxBsGG9L5v_QZphWXDXwYfS-GGjO-d8kQXZmodjAk4gi4VWdrs8-O-qtu4CcrQXQJrpy39wfAaQDmAMIA8KQ3C90EIN002Qt65rVn4asRXjfdMfkm5h4R7xboC99Rrxz6VNvK8HshOYLY45lNKcJGdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kSdaFbwgeYaC2_U3aCjIbijX2El6nkmF3DUfOJ87nsDCxpOErEECjaNUVDfrHpNNvNJqyUiNrF1hL1eO_APuff0yAUKTfRd9rotmmkzPGGfREDIzkYu2Gq9MRUAVQF4oM2qyfF9DuGK9-6oDhw1N_KmllI70g0dGPynVaQjAKEhLFwJg6YQOXYPNse2x8-JB0DXC1n79jsbTRcPHyqzbG_HKJf_BacFAjm0n2F-AJa8aG5NyL1uhr3KC3Zg0Tlk7ov_N9f4rTT_1t34VwkX61_3Nqj-31SHBWk66aY3e7YcTrC_d2hpiBI3rSfYifPXrj7sEZNZlhz_ekTVQz4s3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgYjWyL4R9LVdladb7ZpKb4MBN-GXQ_3uvDaXmlaUy3mOPRtM7K3nzXDVYhftSbtn95IFB6pkDdEksxVCCKDhpp6RmDEwh4d7Efu_ho8D0F_pGfFdrEQABepkIqjfX0OmqzxzVs5nBwEeYlvitzNVSTK5v9csuossr8U0qLlEwFbv_D4DzYQJrNBpniFwhDi3Gi6DEiOgAl5z8pogFvnllinlB-b8vskKJjW0d0i-lf4h-kVgGuX8HcqpDQbX6evdE0btFrkQms5txZbzeJZV92lXdl6WBtE8016bjNwQqfYH6Av21_1LIe4-eHoEFejRL2cGelphS2NlPs1PL9E0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFy251ivyNFQ1nYBcizlUveklPH0UEdaefPv2bzN0WB-WZ2hOEpFxo6dmky_Re1wR2tjJF0hLK7fc_USORO1QJbqNSUsaVJggRmAnMpV10JG4jK9Vbc9DsQCcgmXSOUARjKK9-8xItFDJJapbLsK3HaW9L3gq5CmBivW-1t76hrmd499z63m8O9T08UVev2BF1lHgY-dPRfRFGY_u4SbAemNROTrduUzXG-ruedbzJe78E2OPbmHFCmfUOUTWtXs4WO4SJq-YHzy1vg8IBRV9TJwX6SabEQ8joRSd-_ZemH45zFPGcK2fF5Stpp0lejdBmHF3IEyeJtwDtFqPNH9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GpVOGGTb68nPIx6HVhKfDkRl1cUcYvWWpVxkQxSldjjO66dQeZNeMhcXx8C3t7s-yrEL4O2ePN39Q2syfA5UvROiIhyZmQ2zNnmSW_fYlKmJEVxqj65OnEcFLM_05ErXFwHn6s4z_mSwuMdWG12PU8dIUh38n-R3mQoPUjuAPZQDXhRVKH2Ol-7hy449u0HkmPLVoOF-_9NFhSRiuK3NNvDDQ-j7p10l0D0n6KZdx3HsRaE7K0xEP2IxKwI6lS9b2w5eYAsmea2v3VGsB0z5ajT4kXKDFDDo7iQuec8GIZ8IXMJiElzYNpmQ6pxdudyRqCRRMHpKwZuMVYcmLMqCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zu-vZcNLWZgm1-UBtpq6qehTkezfGW29JxZgJeAVjAfLhTGYMwkfZ06o3zd84qmsmKkNX0XQsFdMEP0L_s1DcILZS-VS0chgXR0sqw_RdLiDE3rqReR9c9CAf0Wa2oyfAwQr6-qEnuqtsJy8uT6GKzWB0RuHzEICld1xkbxsrgr6KMolV9w2lL5yyOWJJdKSm1gEgCotttnaI0ktEYzCo9tANk25c7LxJgeUytkQIj8f0Yn4jtWhpDuujIbLSOZQ7sUaMecEJ0BnEAgX3tF-hVZu2uu35TaWMBADZREyczvKeew-MCy6ikT-yxeneOT6CipRx2YtvtOfqJLjUbpUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFXGFu5R-ae2X436e3utoWtxW29vFUYiOtXETcKD_ungKd23GdVBN2a6Pnl8Gws7PpPfazZLMA0ew0CKQe8o11--i9AVCZdeCfaRYgT8C84Vkp9tcRjTDPi18dCMYvX6nh8M3ZLAzRCUvzTo-LXb-GEUWfkgpCkDooyox5yDsHpzmsB1Iu8E-Tipl_2n1tVqLW6buI34h5Xc1lW09I_HKPlfDetmYl7tAI4mkcfvDsP9vOnZBTfi6QMTtBycxnGTgM7ndT_AKLCXk-6AKVwWZHH4Oll3PJP30qEPL53gK7tmi0-Jkmdkc8TI1XfCV5-a3GNrXFZCaQgCEofQ5LYIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BFoQbsZCUBZ_JVAamViJCyzqys_AzQTZBy7NtkJTlFbFsprNl_OfN80OKUQdLWms-2r4ZytZyLvKSv6dN6WHEtZDUQnBZbi7nkuC9E60XZg387U7kj_4TXdC5hjRQuE5EihybabWWwjZvAOC4icmESb8xHXqN1ZvaUmOnC6u229MfxIYSFbxU8Or_mEamcGp4vDJT3PPq4zQRERMPdqfyPKs8eUA5j6j18de-MnWDWnROS5MJsQgwC9akfqvQJWccIT3bBQjC4StryYgBEmhTTdPGYs82dYN1kEtLY69Jw2C6ZHW1Vfwi1P3ySNTnTluFaFV3VnidC2tjkbisjYAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hIedb901VCk__UfNpEqkJZuPzAi7GFztcQ30_7MWW6VbUoQaCMbeRyBIs0wL0lGa4vr9IWWjDBsUbDA2Vu0auaB0Jpx399vptUrX_iyxfl7MaJSNtPe7eT-2CFxe3nMxLC2onczGNt68iK5OybwJf_MSwcSq39OgoZJQpa2MI0IddAZOuPrYMLbItdP2Z5mNHYhZb_AogzfFpkzhJKv5SfnskbfD88eRVyADBiZB8DzmjUZ7WEd738X8tpI8rSAdCye2-nJwfxDnEdWVBABlCnxBQE5O0NJ5NLndJSCv-Z1qurNGltv8_yAwo3SdEcodWl3GGHdUPhsFyEgd_ZlU4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5bbcdIZu10ldyo-SeRLYampXUBGYXku2Lf9WpxbtZtfrts0CptvDG_F79qdHKKMO6plq-qYU1-hQ1jKQWQAY5ckOnNm0rlbpSgiFpYUwoa3EpwNqMtfA6QK2gWqf368sAzhJjPzlBpqy09iH-kDIqXh6FhN-s0RqsxRGBq73nbo5Yl4yc2xOWhDbD73MI9km9TKvpuVOtbrJ9kGXhLJ8i3QMmUHv1pYAX3s_3OmyxAC0mCkUP97tF6rZuNaoEGNc7STNmNnYl0p7BxDtnLcBhn5LvOBaOtBviClpWJrzg2TfiweoQ7pjJXZSl7wnmmBrVSblKmSVOBk40OPBoMlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXXV1VXtk9fJ5qsq6cutTYK8YIXBHFwNKXXDT_kcycBHzNiQ366DZp5hG7IGg1qg-cq4Ri5l6zlQ2nyNDuK633MSj2_w39k007thicfQqMjqMMNojyVhPvaTblFP5LvVIxaoMHbO9QF-PKzEVQ-vt0jom42B313BrxiO6Kc0msBkOzdKLKcNjJ9fFZSyIrj07xsrGsRiqtj7mWnIdijBoNhJsn-v4FCNkV57quNUUiqXdt0jpnW079cjuSk_sLAwvqEmWg5PvMJLPMvlCCOE2sy7x4SmKkrxw34CIEEVVYL_-m9HwM6MVv_xJqGso8j8f1s3ni5AjdvRjmBIwTk8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKfQ_jl5K7jtl-e-GfRTVgFmKJtqAArl01A7u-KUKGf2MOxNywat5BkLVvhkGzReMNxpcxdpQ0_1upPs29NDv-aHnWlO2d4N3sbVmmd_Khuv8FDVN5Gwn_lBY27xuVoF6ubKO8nO5d0PWE2Yg9LfAZUHEMj2ollzOXvNE0H5tWu0-xFva3-7MPufxWeorA-YTbbFGighZ1qfqiKw3E7MdpFTcJvXwnt_OxbpMhGyRvp-RLTxtlAcWnJOwNDz3r1vznfZoZmM6-Y-gNPPIvvfZWEvb-qvJZwkLz12LpnvI3T3t6RoHeWnCkxebjEVeibRsm114D73QqDqUw6eypz-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhwHYcQks0ga0VCIQkjE8u7-JAo7-pkft8jBPeVoxRSEoNSlk0yRFGPjoJERD08DEiY856Qhd6z5K7L7yB-FUvFMnQFEgGqXQy6ElViU6RoFdzOPj6iFBSRkKwuk4-Jd25X4sD00_Wx6JLHnYAWipIrpL8LIXXw2PqCjgAbXOJURNb34J2Cf269NWTHuHgXXQPctFSntYv60hSvxn_jEXQ9w4KNJdorl9HAAz-pm6YpPCoDMpXLk9yohD6bsE2ybs5xaTDueFB1oDpvlcbko0ypIpY_Pvy2vbx-Xcy9dXdpwYf0T_XtRtqTTN8PvtHXKMYjt7C10VDaZuvEqrxXGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQf7DXtjgr2kvcTWdoxhfiQxc3gEEOOryVpxUAMpKhpuPeHjgcKhGcyDPIvEajB8ezhxK_se4cfKacIYWdnnaa4WEjMwpr-_4gxKHP7TEMTpOMg9qWOtGYz2i2Johc6g-cLLFXV_2l38Cyg876uEdXwGNfCoDfkgauImXS-3S7Hsq2D0BF8LrPNj-xm_WzNVN5ojuB_gMYaLf2m0HKRpv_S5s3gukpur-MlPCdmcNp1ENNVv9Vr9gZqchCxBOKEoaQh8LCc0orpw2KL6g0Njgrg5f8Y0mKPQnVFuJrf7wkJcikXTkTWS055infFMQeG973JlTxB8ef10M6si7pdczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E5Aa8Nl9GJGEcA8ckog9luOSIw7g8NZ4yVCb5PtoDzlkhLxwzJjO-vC1uE6Kd8od7IUylNs5g3eyNNFTUyIJWVLC9ySs2OC3cAP8O3b-V1OOiGPPCL3LbeaMI-7_duTpSEB3gEd8f1wviEkFqUzr3ArHVL3_WypvA5_wtjiEyuhAw5YrecN91mES_QaYeUuI4Z5Ee--cu9oqlbQlhTdghsKS17tmW97X5RDb-wAvR0WB6FZ7Tq2WT2ZDjsHSDJlEt2eXqzXfW2Lnov_jQN_CKUNDjJSB3Ds1tXU5Lq4TwYP13kgUZIHGguzaEfAb73-fBncL9FM7QZl2tPiaxDO5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/trT3REDU1PCvNbR4zedVijRfA9YvtG-nF8THlNvpirM4xrWj2cJ-Ul_THKSfSt6kEnddwRhrur5VtHF0ZmYXuY0BVccebjFFbfoKrFbS7BFEqfYKu8lZkm2MmRDQ7yDGM6xy0aHKL0eqUK2xe1kbkHHKvW0hpONruGVkjivnrkk2tvCl9zw703CdinC86HtwuyAK8MZJmJfZW3d5iD13oQnXz_rBeXwzyRYKthRGBkO7OnMBlPBzRxbQwPXg_R7fBDjbKrZ2moa_5uSk29QMV1tE4xa_4dATk9L9XQdk7DVcJjLw09-hsERTWroGBXuihU_dc17NtL33ajHSjyAgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uqDsOj31sx0pnfWvCiCNFtiIfKU8mEraIZ0pg9opPkLWZHPMACC--zY5HPO-uAVg0njjzzm3L9Tj9vf2ZeAFGls7zXC6DljNHc8yGuaJt4jx24DbDnF3jgXbklbfvUMYxlqN5IPfhMEoRYKjZh4ZG1dlIlpQ5wEYzCVxCPpnoRJQFGc53niVEsxTOu7B-RQw1dluT-ehjWziDvZnhgV4cDliUBVcWHQXB35ognbmxlTwaVbFnzdXJvWqoa6dU2utsDSDCX9W9UymteXvRDOJzC2uzZ1uTOTrhE3imevApbO3BOOTFpvM3SXUs7dLTxdAzr987jxy6aoadtOLKKiwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pfCru-NQcIH_xMwJS7YA_9L0NY2Ey_FEVKCrijwhvicFyNrPuoUizcruc3ziqydRpPowwPrES3HLOdJ974B12EimxtH3HFzK0ZIX6WyUOxWmM-ncvDntGtsY1MB3nYD7ViwL0U3L6EGalO7bbOzj8vcBjKoDzd6I7JOADhcWPMWq7zvkfEoxZsqZliFYbK6OMCKcwMXUuSElF9BVOkm9hj4PjDCqENs-lhM-9yWiWGKLhJbrrqh8co-w4j7l4yIRJ76agD0B_yNzttUm7f4Zc_X0unGoJsp2vStMU5jVHwdAQNsowq3rOCb9PlL_YY9hueDhGLrHtYNWBhA9pM2g9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K4-NQsj3DZNS9Y0bMP-Y2ipILZ9ihekqiBh422S1PLahlB4lnJG132Z4Fytlf2MeGOeSr1xe5_-xq9z1TMjXWoPZbh7qVHXuZj4Cm5NryBkAcBGbzQ2uB-YvMQKyd-rn3r5F16IaWz1R8OBAZsV2qVc9_fNnyDCnpRH0hF0hCdY99MhGGVSkLEuHhqSnwWnvwbyHPauPQp1XDT_u7Zb3fU7-95MN0qVj_TVLhDhS9otNEOG6AcniQDi0UW44_Q2Q39wwdElv1UhpCdQYSKTY-lHE5m7I8XaqVJ2fI0VYsB3qf7JyEQbL1AgdZ0gi3MgDsPqhi_eMb0jkDQoBJ2L8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQnYoOZY4ckg7bqCaP5R8FK3nJkSx9TI12bzfO0Bgc_9BDzfIOdYM4YZs1aOGzh8ANTggPiH_FmTbNBUpYJYkW58qrSrrMARMjjjGEIy6G7CWCWsf4avVQDBGJe86FGiUPUR957P1DsdVu24IosAkumbePD3EUy1EUhpz8vkofEQIwfhPgXu7aCjL5ZSRqdw_L7vc0gjQvRwQAJc0aVNbS83huUCT-4RTu5uzZ2iUC5p_QnPsuf-oDEGJ8fZIk7Gw-c2aR7wb8BThiPT_JO-F87nxpbZ5qeuH11S9k8QBVgA7fX3kkhMY7jbaGJi0oD8lz13OD-1ZEgLkOpMPjASbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cJNxYqVA9O4wANYq27M2OiWqcIY53XVh9dF8BDege4RsMltzXZtgPTE8xg3LfyapfR1Isy9g24bBfuG8WimfBgmxB2OBpeIsLfYTFT874YbDoz0XjWuVsJpCb8WU9m2aUgj5Ya8B923ZQqNZ_hJvoZIF1czS1hzdAumvnzYhESF8VCr5CY2Fx-BUztR-YZ-E5ws6ZOR472WzEfEDw2e1abudjhEnbk9_L6Tiqr6KwG0dYbiFzIf7xmTLLUxseiGTmQYPs70Mx5bRFdLue_xfl3zb8JWpMeh17ibjZ4J0xTfrVgl3VjEgpgtA9VPHpJQfbUCj9UbraioPHaVshqWPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dsG-cgZ7R4zghYpOarzgrTcEtKdu7r-OQHNoORi49TZHL6MO7Kj5AF0ZAgPeKgbWI2t5QMg5D4v2GvsyQeAGCXLegud0MdOrLM-tv-KbPgfKenk4BKlkwP5KPhZ087ROP460jsF2NSPzxIiEyXs1lYIpls2Q1YhvLc8qYWhJyXFrHFUtVg6OGuhjk8H6hyLBFV4qNJerep3Yy-Y3O-WkL3bwaE6_RpZQTd0ShZyflkn5tzIPZmEsNbQBo8ybL1EuVFh4cXWhN2yOq5OnjXIYpaO3PerQ0l5846iIdBh4iBYII60Cfaca8CHhS4zT4GK4ceUaG94EomC_rkxBmPrTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kk388L0gfDcn8CiRxiSIvbHs42A_3coBCriAiRnjLu3guV6TMn2XBGA7Cf8I1dtWfjwBsLKOEtMYbb6HJrQ6Rcdq4w7-9qp7uQnAH_rlW4J3eHQlE5u1uQN68mxPFK9zTbo1FaqnFGHQogZSWogOiUmaVwFiQgWA0Is98NKcRItDXhTuEUE8UoHIrqDuOYwG0jXv9uiz1wLshr1pFMLg2mg9JCraHAJRZOF7Ur2iGDeinS69uEh40JnAg2OCUVvHZpCc3SAJ-QzFzXSbyg7kvXy87I1nMI3sE8cbTuAZRZuM9FYrUuTL1ZPS8JqkCOyQxP5qaoiTLLBkBwRD4FXbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSjQVi9CJ_uw3TZFFBxm5HN8T93n0Td2LK-FeOMbXL8dvBm9PY4chXw761WzAjx4nWFvTn1Alkp4xnHEMw5z2-LmeFv7uAxUvuo-j_R_0nj7XHfQTB7CaSP4psEutT3-wZu8KrzD0-XjUxOxXILIIh3wZOjiAFIMla8dal054KcT9Ca9dPVOl5FrjDLFHi5NNTg6L4lbiF8ykrnnqCp5rtkXkna52wYfdK2xUo5TnBEGA0Gyxs3leD76p8voYnMeHUFpilq9PiiWUV2cXSfAiWeSnQRuwNgr0G0IaxgRV6bq072vUZ4oC2Unw6eaN4WZBDVYUCGGvHgs01BHcHKT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OoCH48GSO8a22y9yx8ehQBsP8_u7wqYIii6o4H8zC3IFrY-J18RiLePVm559JDF7Yi3XKf9lya1Qq3uDvfBirNlJP3BrsCLeDmb9XtM8449Fc8lX2UBE5_xdDqMzHh7xkqL6JRiU3P4S1ZYJnAZXa2USLAGaAn34gtydSzHokhCkKwcF9Zpez0DfIjhK2Ai-m_q_4182bsK9DPptbbo953lu2rFcNwLvnmV61AsVtuc22FmRv9BvZVEfr0N_28g5qZxYm_52_Cx7S3varZB-96UiLRZ4T5CWuoF9W6iLIxVQuW574Fq1QveVheLmtwfeeVwT6iFUAYOtac7LKFd5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WzOazlu1HGkSbfEEjxdefpRj8-n95PZFtZLdyIxEBst124HgBdrMU98mFiHC5op-pIlRypFEJwTYwlzONLk9RYmTUTWf2QRvsQMaxdrOmljxchpC-IEIDCneEW5hTyclv7oneBjgccHPZK_1rZcFm5ilqeGdyeeFcQYeNxaPetNUZoDlsOccAsqgc5Zc_HxZJUFplV5xK-hlQsH3QhUz8jVdPZm88N5d7oEU12v5PyGIl3E3et9ZEZ-Vf1u-pvVaDNrgtOXjRHcIdqoQKiovyCAYsO2EXwhBozspjai16fheKT5cJTo988i6kd23qdsbGlSdPSdO7gT5hSMyUujzMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QlWx7RWZ0P0XkDnALP0_RFA7EMBiuQc9xnydSn1XwqlGFunvg5DbJF8948BKF_Lkc_0KHPkdv0ZjERw7hUJpz-XuWaUGdRWbo_ybulmDQZOEcN82DlVsKsITGuT1rEeD8h50XhA1b9915tSOrRTKeYuU6OfiPRJl8ahcS9KBiA44MYxiKpSNWysfWw9WulrrzctU8G9wFFFwclUgc5y0EYL4DYIdv7s3Aw5MPf9bXrWge5VYyZhyP7bZ6ircTo5ZBbGN_9GqjbFuPchU5DBD56uAmmKNheAzwMhoNhftzC7KTaEOG2amsmbi69R9aIR04gFoiVdyoohioEXzT_lYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aPe7HsFrwnb9fGG_rK9AOlsZQ6IsLsxPvHfSzFpCjA0_JDVJ-yXvJv_hrvxVCVJ3K8UqkrAuBoDgoEJwZCTU1GVEppuVLeBvC5QL14e4r9An7nBv4YOA3ztLOAgwzOTO_RKxWx6kSw9zpGtrCGObBMxOMekF2WVBzESbRew2StWf-gtcLtkE1Z6dgqh39RgQiWUYoh8V4sIR07dae0PFSjUy7WlYtiHw9VcQ7Vbwbs_aIWpBMAtAtGYNgkwSkZgIoTkPe5IGswokIK4l9KwYWfx-OpMpPF2lMQ2OwT9MQNVhOoqZD06fu_FzpB9Id2aD2Ou3M-ScE1u5vRsVXPUUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/miirgkma1PZTTWxuTeAKQ_3sHRpAFRYdf5zu23_cr19t2p1_FpTetceXWATGnLmxH5lj7bdeAkJ4tqfjro22_HVZkTsEnJ8wcAXFZ2hdV5CNEfKi2ohjlw_vcOMr-XGb_p1vi2iFeBlW3t35uYZpRm_9QbpuASLexD5jStohiVmf2SU-bKGsiJMnb_1iGoI0xG3ZbE25a2rPAdy2P1EiSj7VVadoRaGikT6tOIOxZhDxIb1V1bPjyFo-5lfjQ1qA2Khag91HRz_r_PBVMXcdRhJ6rCWGR1tRONEWUmL1xY5aVV8V_HfUWxHdxeOGRf-eSF-7NOYXAOCwcSZJ-0GzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIJYBlKFUv045XHCaTRCf3ABPrf1sh6-xqqlpxRX2ha9c6nArlQ40GaT_4YN0U_GfWSIbQCSdnf1Wa9LyCtccpgzpd_oMY0yucOeCD3BQ_-3ubZv_Wo1R9M--UDCSSJFZp0gfIFQGs_9daBMb4_h7XLw-2iGkx6-GEcTtPvspIWuB5BfdVCJ-DI1X_S0dfGYENgPYONi2JB6OfSocjUa20dN2P-Xd-p2lFN_tTQyQrHTFEAKomWigjpnB5pBlOAnJMMqrVDWn1pUo0vUymK-iNkoHZH1oWY1pTXnemwtlXm8Qr8GS-UmsmzpZAEAAq_qkFv2EWUSiKCOdOO89bCf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tt-vAnG-uJR4rT5P5sxf3mBBC74UOnYRRTsAFuCZ77h2qo65Ty4LzgcA7LtyxFJb3ewWhNf6KlHHDKPkknQ-EwnGv_DZbIeJaUhpKn7iz1vROCKK68wcrZ-IwMtPXwcldAFSI4AQ_UqakkkzP_3Lfj67pxi837-HBPs2wRQxevsPDLvL5xPXbO5x-M9AFlduKStYrRnDJZfRJWHlDtHmUj3lYY-0ef9L4O7YznNzHX2F2pcIREWDQcf6Ejh2ujyLrBLchqj5ztxhZ1ckL1WnsRCScBTLwsp0j9XniRTIeM3Hlp798smnhPPAQkyeXHcz7nR72FNU1iwRnkqZ-6Z2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbyHt8bzCF0xGlfCBFMMV_IaSzc4dxxCIBsQBP1D9YV604h-RXlJCbbDqHV_3S9Ves4WsJmuJugPjOMbZVmtJSNEtW-1cDEpUYIHvIiUYSFia_6czx4Ua620qDjLGf5tdLbDOLGVJ2GlvjsicuOZS4sbsyoXYpzw85zNwMVpn4ie30tRGp20FQJx0nOzuE79sY6JrxZtIGIA_uZtSVRzWKEzw0zKUYARTG8naz2npzTsZf0ww5uCJMBjQaRtLuMwl3k8AWdzOh83zeLjhXZV1QfuwiR54kQ5tcHj6LHP0q4-UdEsP_EA_drRtLSsAjI883c5bADD4JBC8luypOK-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m6AVGNMY8TDRbbwjUdRwNX4wAfln6cqtk0BOtAM2xYrhIYgxOrD2YMHjvlIc0QCyAjaDIM9Q85fs7V5nayaqU-thzxj9E3RNtZRjakEUqz2eLcZ7R702H0XB0VD2AdLUWki7_6pjCmhJ848RdOW1b7g0hJGpghjXcIE2oSiUmLm7lJ6fxTDzvZHe5fCycyzfZis_91r02NMqM7dexQYiI9C3yyvT4tf-6M-j0gKefu5CL3l7o9nPAtZuVJkNS4pTN7X7MIB8itTdMom7y7B-jAztOzG1ISavrkvpyymWQuGwIFa09GOAhdiqFlhJuH5-d8I_ttrTi0yOsU4pf_tgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BL_9-PnejPm7EupAb0Z0mzqdE_cGpe94xj5huvJPgt6fMRPds5fdGRQkUSSt88pX0xkpDYX8Ux_3x_uQwVflB58b8x1GNl48N1ze0ZpxQok4m3YwwaJrRlUeyj7NGLFPiSC71dxx9jUdaoPV1l0T10RHVP_Rtpudnm1rlptBRFwNDyoE6pT31zukDk0yzhuS76quBbKQUvRZD6-JyZvxyr2gUMFvpE552ofCxPCC22z3AG8OGT2XWQWQHhmmrs10wxV02lHOUYXEUmmQTnpiulcECswTDDdt1Ig2myZFiL94EoHhcQL27ZILIbNBNcUkoPDgbn2DIx1KLEMG1wg2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e4Cf2CzIZK0Owg_6Fl97xpW7PsS-alf5KZrx-3S4yoK9Xh6lgI2sazCZKCdGfQX1sF4FxQ_2o78MGLvw7odJqhbrCkKYtLMXT4s_SzbGavNDoRT0u8UQ5EYAjQHyH5qCUNAXsUmisnXCyneYdQwA8MexydLktQ-oT4CCz5TTmzcyS7SzRB8o4Cp0n5RuIS6gDv5PZHPWAXPc8M-tNW8fmFk1E7DozsqGqUI5i3JJk_PcnonoGiHrVS841PEn8zdso6oKLtGdEuSsx6dB-2uSK6RWK1KBKHcKVrWtkaI1kzqH8tHqg7Mp2me4F7j1bkWnlKcYrG3s-cKEdea2sjqJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfTySO9lhP0aP_P4WuChTZ3MbROK9bmtI1kXmNm0ogrvyvPnJv6bLCWrYbCXTaSGdx6BJOupx9EfQQ-TGdDGLODEB-EweXmChRL7JjKluXA4RcTwZ4hYI6KOWlYtZhXrmD2RH6adPwOOEQ7eHhOH4ezcpaiRlUhRm3W2ooId-l-_nbMv5_a230kvfL68-6J-tus1EnUc3psOCI_cdilVZPuODzbkersEMXqHCBUIlZhvvQ83W5lHUujl-7fIaSA_6c5K-XzATrrQls3G-aJ7rf5xoJWtwN2EOTn9IWfzlbSKo9WMXtUP9Qb4ewtanE5hGLXosbPOzk2ieRPR9Jb_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gyumdgjyYAIr5gtlUV9OEFovx4016Qz-m44-QUV1YrKf9eAmufr1i5-J6H7wcodx_qpmE-9yLwJeqlAy9nPL4YUEvJGr3JKpZRpemzz_4KjtCLmnkUVlOwnk59yPAAMMB-hyjf0aUaYKxB9NbOfk2L0AkAg1exUCWTxVKVgeCbAFi1TBzswcGDW_8eeTXhXKlt6My02cACQPoFHaJAE7SGTkUkimOppgiKfdaymElGlCzdP-ovczNnWJF9wxRQYGqsJu0pwQC5FPQgzlWs6lx-dQ6Cw_Iu3PXC0A4iBmETPJ6xx5iBoDDwb2yBwX6IwWeD2BzM6Pz5nRG84JljAVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKbg0QXUMYrJg9VcHGDDijlZanZN51CBPe82SnFcsQyV9MwASgni9Rp18x4njsP-EnltQCUQYwA08Unb729aWz4BE1NjRtVUi9NUCPNxlVGVqkisI0F8zu9C3jLZDv_vDYhfd7L98jw0otZOePWPNYQ0Q2mMkalEjvMdLTjxOd-rOf0Iu-baaWA4rfHyFIpiINAghaFKsHQqkVnPW7UD-snQj7DQ5HAwP4xOmKp87XbVmxtidyZHxkH5dCOEJacYO23_Qi-BjJu0vmH_N1oRQs-A7lIwq9KYX6LdLDMggcYQsprUOgoBSbJ5dXsvUzlkFzxoXeEVTR1KJZe8TdWwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKMDSGgTi6DKmyjIf641UqJcqJcDR7ny7UTvpMp4_PErH9EyqGjC9yVAyGA5bXGE9bJckolW3EJpcxCK12T317V5ux826jXDGShMfbY2fBh-bwleN2Xa8AlaI4Q3UThsJUnNgQMPeSQjNvIV_9CvKECi5nuz8q-5klHRNLTVjUonrKwUcBncLUBTho6xiUv466nBGe1fxZW4oJHTb2RWZr8L3LI121vsbYquxbTt2n_8FGgpYOcf_qaFKJzq-kMWhupX77r9aHX1jYM9I4w3WNR4t5tSuyR_71SgFfKnKZ_pXSvH0aPa4EEs2ED8PD_cdeQduu6-7yGNuhzF0cnIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gYCtqWmgGpifAjHF91Fncm7Lcf31D2aLo7nLp5Uftx8ShV1goPXKIjR3R-GunLAJ_2S4pWB044XWFkcGJ-L2-VSPn7jd8K4OwAEZrkM5LkOMdLm4b0YTlxaAvZ2lR0Bf0G2vMkpHqJ7_nx0u6h3EkUO8R_ee8tYB1aTSYOraf4sm36ygaqWqkQ5e6Ij5aIBgF39q0EgPUSTxbbq0pt8DoLHwtJqVn9hBWoB2vOrPgkFiC9Obuy90LzVDGTO5Il3AOUNRG1FvAQpL055_Bd2lH0nIDVy2byy79wj6binfNNp7sziZDydJO6jOXlcuRcn6dlywBcvaPgOpIdxfprN6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iUSzQ_MhNJp7l3aEHk7y6XIPoS-K2juYtBAG-b_SbI7PZB35WHXDRw1b4UD_G0mSti2aecA9kHupumdBJCj8r7SmE-gBDwlk5Gfx85HdyD-xXDimeRaELlvISpDQrmTju-rf2kF6PM8LLBg9YN6dIJXGpNAJWfxD3cGIll33Ngp-UY3D4WSqLsDyY-PTMfj8Ter_f9oisZ6XIs7raBry41w9eIwwWSpuk7IJrttMGJccySB8UYGUf0ctpygcvwzf_wS2B0GntksKCM8JWZbFA8mBU3RYT0Vj8YKYEZ4TSAmcaWjF5W1GvOY-NXQj5CyIqzSVnE3J8swQrI-QestWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L5JZgIzziRLmQKrWtD61G9a6E3jNaKJjwSyOroaV48s67B7SU6iqU_X0tDoTz8QqTrDnXlPrYirw1Gr6UDesvVSVDy863FrT4DB0oMBkDcJ4Zi-TftuAKNAEmgso_eiVh5o8llbrrRJFYF7HOKaUmtZ1FzUaUPViqCHAiyeVF8NISTVGHESniy44dWKT15yZUPDmnpI7EbtWYhYMmzb35hnOi65KjI5AH80sMKRlUQegVE0H7s6BGMPVwYjUolG-PmWd5s_yVPBi3eyItY0iDC69bMajpK63tswtwVKtuFTIGzv3AdpNAYurXoZGqETz_1LBsfPoujdPw7dyF40ovg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mv3-o_iGsAHFVAKhITKYMF6wmDOc8H1M4HJUoSxFCRVeeVd424ybRYagNJ6k_gc2Gke-vyPqm3IsHw5vfugHD7hnGs-JBCeZAuvD1l8dhTetHupg8RXxnkTW-_vyAzlfsmbPQ43PIjYENnES5iwM3drfl2D9v8lDCjBVB7FclNtu7_f3U2oh6oIGzY3hruf5maZM8d2Ecx_8HCE0GhBc6fk9ul9jfU50HyT6e3FY4oJT-jpR77Q5_5jKeDBw21jwUDMuEtd4FegM63G_LUZMq2yaY5XwgAPsImcCbwo9__Uw157FFo4o88Cuju2UUk0jkhy8GJElSwp_00s8jueT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gGnEhqOrRTP0gmOiyI93gKezTjQNGGrNt-SaDf6OZpmbwWo6vHqvbSjHAhvdngcxnGfU7EgTH5U_Pfb1iWNE4VMkt4kVuxPeBoJ2rOAzy9ffkxCBLTDC2kCwFzb2xGa3EvJ4hXjsmuaTVBUIx5g8isRsJr9Eaud2mfIUVwEY7wALUbzL5XSgiUg5l7XLXUNQIta-jTqX2NRDPuFWNP35iKrZA2bCDa5h9VPlASbeJHDrynk1_BpQgwoxNFgLj14HHvglvERlp5m2LJPauKBVOUpYXo_4cOsTt3UJUV8qHv_R3aTNc3yOP80hGEqgCTH7IUG5tT531bg946l9GfLxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5Z1ceSYPVf_Ywj8RNU9fWRtZyxdBzPs55yzweHkV5qWIWdwPSFQkZeejMVyC1gppKN8IbJrLzujnTWF4Tl1RolHz0nU56znE6zEbCv7c3N9_7YU0AV-e9XGmybYkbtFdnj75NuHT-M0iMHCqlChW26zon6mivOIADCQNhPBlYFwRVTzxOWPzc1_xjeFPPSmfHL-7_O9E1QVpmYOWu_oFYfpAmB2_kgwMcTo2sxpI2ZtDN4xu0SXaniDfiiX4_xkc2a5MdTP3YVqtNpOJcO-Ux9YVoT697VrCz-4Y5L-bKXrV9CZsuYXIbDM2_ivwDqTeUBWJ-dlBvzT5Oc-6N8jCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3T7wEDV3qFazJDP1KMs3oQU3Am6-Q9WjOu7pjnvFV3s8uGSSvHQ5aZpxkG5FDX4jHz__wWqmZokl5kDxqCXznYHLHKgbAV1DFTtbxOB22eHRnLmz-WDwOBMa7cPPxePiZ9NzXvCYRREfQikbY4xWKEWdDwZcdBg-ffhWvAW6B2yUvi-nmDf9ArmNrbg2oK_3sAA8qZ7j37FHaBuZHN8kCxo7aTVYkDmjh12xt7fEFUNDadAbafyJ1Kt5znNCyn8nGvfvnJyef-LzaDvuPszlnY7aiozRA7YV3Yu1vicSWf4nyLIf7XZ2RfikaPeYnJkWDRtfldoj0bxL3jTtCVtxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXpJrxX3NdLHzUWGrv-piDrtpp81taUFIQSOrb2yXxpg1NhNlHU7IlLj3gEhRvzo2-AodYBXZZ7ggJHH4Q0oFBeOqC0sKC64BD_kPI15V8PjvArOT1m9GlI_PS65LNiDjN_Xr9YRYc5MZxbiTIVzk54bZWOuTP0LpvbH4HG-XxMOri2F-Dbv453kojTMobdlNI5_t-vVZ5HdrW-zmDpqTMBKrtkp21ChtRZHGo4fOjx8bbbWq0Q8edUioGCx1-aGX-Lwvgb5NDDJnDnicNtQWCbd8TEUEhsKcbiq8yOzD3IxQQAWYvk8WvfR09RkgFWTHLS-jcAH-0WqCq4-dZXj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RKt0B0Y_1Dipl_vsbfm2sgl4cKhsgSyYbCY-kvYPIzP-VP9szzcH8Iq2hnj34PRnAMKtPrjTsJeMlFjmEk0IMCGKpijsKPFfaux4ywKxgWmsZbgfxwB7-yPYpUUpokZgNDFxB_R8B1PGolYrTxNIhEu5WOwYuTcg3cw9rs0SB-rnl6j6obWsw55VX9I1VpuGOHY1YIksbNso0_dM1Hu_zPV6HFCc6R60geaP9quhqnGXdZ98Goyfyx0Hc1pzo2PTB-xn-JHXnScG-qhbIUE-AeV-xw6W2cUALrnDH821gu9ngrTnSwxv2ZJdFsmpP-XkVr9f_xicJsJ-o4Tca4OQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QccQ627oNem8vtbYA03s1QOxeWyhnNepDla1qHY_g9R84JkOtJH94t_7eZL9VJIVBlM3ST2owAyRy-mOJxM1ZWJF3N0co9aFnZpocYhjqU5Uv37IU0HmW6lbeHCKCZRV80cL4YUOs7_x8JZLbfgZ2sPRqZA-oCxj41pv2n4_jTKrZivU4ssOMl4kj8r-LisCYef9P9M1IkO4mjdEVvgI1MCAcvlFFBKqTPkmRVrnIcWdmMMKg1SPvV3ByAMRwAdaLPMOggNlaR-CmdGRlJbm-J0TEhoo8zEoHPkNVDZJucVl-BHrny1Ja1ydDJ39UOkHBXauXASPZ_QJSzFqWFvpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u52gDjE7YtSxfDiHZwc7m9iKGJ2S1pVTG701Yg8On4ZSfHEKs0StWppVPxq7LBU6rkYByBKJTnRJraLn0MFwmpJePFNmC_kljjSJwHRbGzoEqqgrA89yQCALuLC33YYIh1eNOxfd0owVGWXsjGgTZs0jXSE2NGqWmu0tbTAZuy03S4yCmH1_8wJzNaSzaDLjHAr--7_8GH_duFs8orM_jfAaaxQUaJvGkD47hk7JwwNSehaxNXkDg65Bpk_3bYUrCVJtTW3zLGsbkvDbG4XDjvoi1cTc0WGi1zVWkoSqQGD-zD95zpVkjerMt9Jg2SZ2bqNxuCVrWBWc_nvfQDwoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tYypbAov_V08-btEHTAEJW2rY0LcPBt-4Sq8uvgaoTZQveKwnOg7bv1t1cBNIsZuQFykoWPe6JKzy62tz4rIjTk-jMMMazrvHdmCMzLfieGksSgqt8Z3XY3D116zX4mQHgx-Hp4tQG4SgfRT5YuqVs81f1qBoJASWzDv9saENeYxxLHd88ADivCSvEfkhwJQAsAwCH-qdkD3pvpQNJJpDOTps2jKwKDb_xzbo2aCeUYQ3Ew3ehzoHffkAZuw5v62E6PBagM4KBZIy3tZLqIquWmWrBBTxhKS9OxoOoZx6lZa2WGKHmDua08NNRMtY-Uprko5kWrT_Whuw_zeLNzavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
