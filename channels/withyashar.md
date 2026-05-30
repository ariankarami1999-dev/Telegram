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
<img src="https://cdn4.telesco.pe/file/AXI3kVeVnvMhtoMqjE7KhrY1VfRvc_B-jncJDO3BhaymhX0Z1iF39Fdvs9Wg6-o2Qbmv16JDdxN-rRTlJ1nv_ZKxqjobYXkE0kpRctwnP-Boo4DqAxKkmXYjVyZsvd8tMwZKrN8rog1KmaKAw9QROFEvJ7fEiELL2xFfJttfHs6mix7rI5NkpB10aEv86ERY409KVTOBE3IWRJOSVRClThbsGFaSkxUawmtPvQBc06ZH44U7libCZWmCK8ri-STBG6bJQgwiwbG7ZgNpyB0s6fY_A45qPDqXyTQ1d62QgOPkCIX15XQotBmH5_hRsKtKgZ0AoqMxzh8Cq8FivZN50Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 281K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 19:29:26</div>
<hr>

<div class="tg-post" id="msg-12943">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی فدراسیون فوتبال:
روزبه چشمی به‌دلیل مصدومیت جام جهانی را از دست داد
@withyashar</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/withyashar/12943" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12942">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تلگراف: دو ژنرال قدرتمند، احمد وحیدی و محمد جعفری، با هم متحد شدن تا قالیباف رو از قدرت برکنار کنن.
@withyashar</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/withyashar/12942" target="_blank">📅 19:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12941">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، گفت مردم ایران برای ساختن آینده کشور خود آماده‌اند و از جهان نمی‌خواهند آینده ایران را برای آنان رقم بزند، بلکه خواستار آن هستند که جامعه جهانی در کنار ملت ایران بایستد.
او در بخش دیگری از سخنانش، با اشاره به خروج اجباری خود از ایران در ۱۰ سالگی، گفت که با وجود گذشت ۴۷ سال، هرگز امید خود را به آزادی ایران از دست نداده و همواره صدای مردمی بوده است که امکان بیان خواسته‌هایشان را نداشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/withyashar/12941" target="_blank">📅 19:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=i4thrGNSVcexxVe6A15H9mAcloK3ztnDqthKlRyE9w7OhcrQnk6uveqv_lv-vnhkCBmvWROzgPouRJcSn58AgEj_hX_Zwm_WNeCDptzTQs45kuUMW53dDfSaMzoq-t-17dwoQt6JBpNAKEXY25nKPxsOHdtn_HrnZ26uSZ-VoXtneX9PzDOt0j6uuIFDlhZcIntG1CqgtCNh62L5gSfGCPl3DVcrDdFhHSbt95_IRbhcdRW1P50HkBimnO2YeEoSf3RLDyfpmgYnCzCmAZLBFOFVofgJ8fQGOTEidW8qkLEVDBNUZWkdB8OX6gcRo7eNDNFjaKZJTmitBt6UwoeO7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=i4thrGNSVcexxVe6A15H9mAcloK3ztnDqthKlRyE9w7OhcrQnk6uveqv_lv-vnhkCBmvWROzgPouRJcSn58AgEj_hX_Zwm_WNeCDptzTQs45kuUMW53dDfSaMzoq-t-17dwoQt6JBpNAKEXY25nKPxsOHdtn_HrnZ26uSZ-VoXtneX9PzDOt0j6uuIFDlhZcIntG1CqgtCNh62L5gSfGCPl3DVcrDdFhHSbt95_IRbhcdRW1P50HkBimnO2YeEoSf3RLDyfpmgYnCzCmAZLBFOFVofgJ8fQGOTEidW8qkLEVDBNUZWkdB8OX6gcRo7eNDNFjaKZJTmitBt6UwoeO7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مک‌اننی از فاکس:
بلومبرگ گزارش داده است که حملات موشکی ایرانی چند آمریکایی را در یک پایگاه هوایی کویتی زخمی کرده‌اند. فکر می‌کنید اوضاع در چه وضعیتی است؟
مایک جانسون، سخنگو:
دیشب با رئیس‌جمهور ترامپ صحبت کردم. او کاملاً در جریان است. فکر می‌کنم رهبری جدید ایرانی‌ها می‌خواهد این درگیری را به پایان برساند.
@withyashar</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/12940" target="_blank">📅 18:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHgSr3rTf2e2IMHQoc2QEMVjAwMXLBZhNORqIlnx86q8f-wjRaFzodeqOvWQLOKRVtj3-DLNzQxH5iffbthpcJoveSmP3zQr7psspRchmD6NNebPus6waxJfI4vMCBclcgl0PAwNNj67FQf9MFldFTmlwwonSMIKFPUPC-gK2aqiuvB8iziH_O8w0t2Vph360gZayVO6wLeECxwH_2C28f_p_y8Z9Y_26PI3y5h0IMfxWTeGjxt3qrc6gMvy_Y87tgvT-neEt9Ii1NrZ-zJWaNBqTxTsEcAAX21d9YxeLfd87Ksk25sDHoZvjm7fI-alhtwpz-sDTz4gcUnyqCpEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می‌رسد که ناو آبی/خاکی یو‌اس‌اس باکسر (lhd-4) قرار نیست در حوزه مسئولیت سنت‌کام  مستقر شود. ناو آبی‌خاکی کلاس واسپ نیز امروز از بندر سِمبانوان در سنگاپور حرکت کرد؛ اگرچه اکنون به سمت شرق در حرکت است.
@withyashar</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/12939" target="_blank">📅 17:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا در جنوب اوکراین، گفت که دنیای آزاد هنوز متوجه ماهیت جمهوری اسلامی نشده است.
شاهزاده رضا پهلوی درباره تلاش برای توافق با جمهوری اسلامی با امید به ایجاد ثبات، گفت که یک سگ وحشی در نهایت دست شما را گاز می‌گیرد.
او افزود: «پهپادهایی که اوکراین را هدف قرار می‌دهد از سوی جمهوری اسلامی تهیه شده و با همان پهپادها مردم معترض خود را در خیابان تعقیب می‌کند تا تک‌تیراندازها آن‌ها را هدف قرار دهند.»
شاهزاده رضا پهلوی گفت که تهران و مسکو معماران مشترک هرج‌ومرج در جهان هستند.
@withyashar</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/12938" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عمان: در آب‌های سرزمینی خود جسمی شناور را مشاهده کردیم که مظنون به مین دریایی است‌
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/12937" target="_blank">📅 17:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea39bc17f.mp4?token=SoNTyWOGdihNEDMvuhSxdenNp8xhOaT9AyeVxgBynUdHf8aA2xneIfIZmdxv2eaqIeU9FCeMi581R4lS_2MS4g4tzvydXXoaiAGvp_n2vxh0SPh4VaJ7klyMK5LpS_kQebNEkw1h3SN8wFt4H1YwbwcTUqKd6auqm5r1jTytRqivu8l-WBLquPxj1n5IGxQ62gtTJr-rgT3snu26KculW4eozU9KKmg8ZANg9ahB64v0xUJA78xz9I3RK3qrf3siudz9BlSWoRm64AnMrvAN2zpSUDbV26QiPhz9Z_Am9Bai10rtHj0QzMQiKc9Qsi39IqIesSPAjc4smNozgH1Wtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea39bc17f.mp4?token=SoNTyWOGdihNEDMvuhSxdenNp8xhOaT9AyeVxgBynUdHf8aA2xneIfIZmdxv2eaqIeU9FCeMi581R4lS_2MS4g4tzvydXXoaiAGvp_n2vxh0SPh4VaJ7klyMK5LpS_kQebNEkw1h3SN8wFt4H1YwbwcTUqKd6auqm5r1jTytRqivu8l-WBLquPxj1n5IGxQ62gtTJr-rgT3snu26KculW4eozU9KKmg8ZANg9ahB64v0xUJA78xz9I3RK3qrf3siudz9BlSWoRm64AnMrvAN2zpSUDbV26QiPhz9Z_Am9Bai10rtHj0QzMQiKc9Qsi39IqIesSPAjc4smNozgH1Wtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست درباره ایران: ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم.
و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/12936" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزیر جنگ آمریکا: به محاصره دریایی ادامه میدهیم.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12935" target="_blank">📅 15:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/12934" target="_blank">📅 13:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">#shahzade من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/12933" target="_blank">📅 13:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓡𝓪𝓼𝓪</strong></div>
<div class="tg-text">#shahzade
من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/12932" target="_blank">📅 13:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#shahzade</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/12931" target="_blank">📅 13:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سفر قاهره با یاشار غمی ندارد فقط لذت ببریم از وقایع
👑</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/12930" target="_blank">📅 13:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صداوسیما : طبق نظرسنجی که از مردم انجام دادیم، اکثریت مردم از وصل شدن اینترنت ناراضی و ناراحتن. باید فورا مجددا قطع بشه
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/12929" target="_blank">📅 12:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تسنیم : با وجود اینکه ترامپ در شبکه Truth Social اعلام کرد که محاصره دریایی ایران «اکنون برداشته خواهد شد»، ملوانان ایرانی گزارش می‌دهند که این محاصره همچنان به طور کامل برقرار است.
کشتی‌هایی که پس از اعلام ترامپ تلاش کردند از خط محاصره عبور کنند، توسط ناوهای نیروی دریایی آمریکا هشدار داده شدند که فوراً بازگردند وگرنه با آتش مواجه خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/12928" target="_blank">📅 12:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!  @withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/12927" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/12926" target="_blank">📅 11:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتانیاهو خطاب به لبنان : درخواست اتش بس دولت شمارو رد میکنیم
باید بگم که اسرائیل تا نابودی کامل حزب الله ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12925" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاخ سفید به الجزیره گفت:
ترامپ تا زمانی که خواسته‌های آمریکا برآورده نشود، توافقی نخواهد کرد و ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/12924" target="_blank">📅 10:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNxlVL8dD6QbN7Dwssek1cnOBrUQUTCRvhwaA87xblT3IobCuOy7edLQKf5ds1FlAq5u-DfiQbV1Iz4HRjcQQ04LMM2Lx32JS7R1DjXpKbNBI0-Q3F9YDcmf6JyosZrSLqU--PbVKOYG3pycMCUzZUknM8I2yZ1IK4-C_j9-THfWx6z_uwZbaiIim7Kji812TGSbNbj4Ct37rcCh2CgroVHQq__IHpKEhWOPVV8MtotztaBKeQSbQXu7YHJcM3L24tC_KolbnOYegz8VEx436Uj5BkgI1AW2ItyPBtw1Xl8FugtijPUCWPHO0zM6HE56oTbWO3wJO0bqJpukvRABPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشک ترامپ: «دست دادن مکرر»، علت کبودی دست‌های رئیس‌جمهور آمریکا است
این یک اثر شایع و خوش‌خیم است
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/12923" target="_blank">📅 10:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سنتکام:  هر شناوری که در حال انجام یا حمایت از فعالیت‌ های مین‌گذاری در تنگهٔ هرمز دیده بشه، توسط ما هدف قرار خواهد گرفت!
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/12922" target="_blank">📅 03:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=B12E47vmYka50uXW17DSM5H0jqKG6ZnMJ_lPDqXSimw7drRHXvKVeH980Yf-s_vK2w97PxUSwMvz2_5wTJodDxZ9kfnsqDtbjUQprBZC4Kk8o_7RAPzhYaGOSU9sNQU-hy0GR0Z2lpcx6BSd8NuHcCBNkwTg3dYGmg37iCclBOtlI2FunprSRoyCbuifkF13vCRPKuWVFo7evpOJGk2-rbbJbS2QAaKGxohe6rptfNVKNhDKWp8E3Pa9xv6YnCHRnaEtOIF43nh4vsuiJFjvlV5oG1IX3jEc_hTkozRWPW09nWh022XNCMvD2MAb5Fp1coNxECpWZ-O3ecg4v8EQyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=B12E47vmYka50uXW17DSM5H0jqKG6ZnMJ_lPDqXSimw7drRHXvKVeH980Yf-s_vK2w97PxUSwMvz2_5wTJodDxZ9kfnsqDtbjUQprBZC4Kk8o_7RAPzhYaGOSU9sNQU-hy0GR0Z2lpcx6BSd8NuHcCBNkwTg3dYGmg37iCclBOtlI2FunprSRoyCbuifkF13vCRPKuWVFo7evpOJGk2-rbbJbS2QAaKGxohe6rptfNVKNhDKWp8E3Pa9xv6YnCHRnaEtOIF43nh4vsuiJFjvlV5oG1IX3jEc_hTkozRWPW09nWh022XNCMvD2MAb5Fp1coNxECpWZ-O3ecg4v8EQyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلزار: نماز میخونم و شبا هم هر موقع بیدار شم شروع میکنم به دعا کردن
@withyashar
❄️
👃</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12921" target="_blank">📅 02:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک مقام کاخ سفید در گفت‌و‌گو با خبرنگار شبکۀ الجزیره مدعی شد: دونالد ترامپ هیچ توافقی را امضا نخواهد کرد مگر آنکه این توافق مطالبات آمریکا را تأمین کرده و با خطوط قرمز تعیین‌شده از سوی او همخوانی داشته باشد.
«واشنگتن هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست پیدا کند».
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12920" target="_blank">📅 02:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12918">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">@withyashar
وضعیت</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12918" target="_blank">📅 01:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12916">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اسرائیل هیوم: مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12916" target="_blank">📅 01:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12915">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">https://t.me/boost/withyashar
بچه‌ها عالی بود
👏
👏
، بوست ۳۴۸ تا دیگه لازم داره. لطفاً این پیام رو برای تمام دوستانتون که تلگرام پرمیوم(تیک) دارن بفرستین و ازشون خواهش کنین که چنل رو بوست کنن
❤️‍🩹
چیزی‌ تا ایموجی نمونده
🤰
🫃🏻</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12915" target="_blank">📅 01:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12914">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شکست مذاکرات پنتاگون
؛
اصرار تل‌آویو بر تداوم جنگ در لبنان
منبع رسمی لبنانی: طرف اسرائیلی با درخواست هیئت لبنانی برای آتش بس مخالفت کرد
یک منبع رسمی لبنانی در گفت‌وگو با المیادین اعلام کرد:  هیئت نظامی مذاکره‌کننده در پنتاگون، به درخواست خود برای برقراری آتش‌بس واقعی دست نیافت. این هیئت بر مطالبه آتش‌بس پافشاری کرد، اما با مخالفت مکرر اسرائیل مواجه شد.
به گفته این منبع، هیئت اسرائیلی از عقب‌نشینی از اراضی اشغالی لبنان خودداری کرده و بر «نابودی (توانمندی‌های نظامی) حزب الله» اصرار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/12914" target="_blank">📅 01:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12913">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgR4KqqdzcSXcdPa6nCq_L2N4OhopP4IxIEk763RbnOCaNGtt1PAEkCaJZ7WBdYYltXNIPrlOp9I0LXP4pVaoMGfn-KIkHcIzeQhK0CvK-pha5B0yZIWpuwWjPpzlBVEFtcm0p-jhpgemJyJ_lEY1T0Js81v6a6nPT9-f2ubo2fnGX7NVWv4KlOo5gIh78Xdh-gNE-kvDvyX9WLCqC21QeD48A2tFvsvOzzyVbk1VNxSy-5ulXSZTcBq_q7vVKp90qXXyXxNN-dFMVRgNbwkrtTMkzPoZ6e7z_nxdhxpDuAHYODbEVm7nn2MNKDVofG4AkekjVPGahVd7JctdoOwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
@withyashar
زبانم قاسمه کتلته…
🥴</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/12913" target="_blank">📅 00:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12912">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">صداوسیما: منابع محلی از فعال شدن سامانه پدافندی در جزیره قشم حوالی ساعت ۲۱:۲۵ خبر دادند.
بررسی‌های اولیه حاکی است این اقدام به احتمال زیاد در مقابله با ریزپرنده‌ها انجام شده و با موفقیت همراه بوده است.
سامانه‌های پدافندی آرش‌ کمان‌گیر در روزهای اخیر عملکرد موفقی در مقابله با پهپادهای دشمن داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/12912" target="_blank">📅 00:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12911">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حسین علایی:
سه روز قبل از ۹ اسفند به شمخانی گفتم امریکا جنگ رو با تـرور رهبر شروع میکنه؛ گفت نمیتونن اینکارو کنن. چون نمیتونن پیداش کنن.
سه روز بعد هم خودشو زدن هم رهبر رو. اونا اطلاعاتشون خیلی قویه.
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/12911" target="_blank">📅 00:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12910">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWB40nCXEeA_6NmO8CJD9LDZ60qRQNtX_LNr-thmQyyx9RbRyRa5WIfGCl4qE-Lxw8IzgExCBR53azkQq-F8-93oxTdRKzqSfKxN8AfkeoqoUV15dIaqmvsafny1m-kpy4UCMI_Qw1Je-Xz25hSkhsEcNIVZ4lnkTX0vRdBywq0rWdSNIJA7vmed96NStsdb5_IQDRPWTA66AV8oPYG2cPR0B4Bu_HzLF3heQ7vt6rj5-LgM37W7E5XozAtiNazkJ6LTRyfcUR3rqsSuDlR5W1jOMLbZNDcnXOvotTfNQ3xk5xEKkQacLr_Yro_l6upfWON5gd0tSj3BsV2nwpGEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالک شبکه ایران اینترنشنال به ادعای فاینانشال تایمز
گزارش Financial Times درباره ایران اینترنشنال می‌گوید این شبکه به‌صورت رسمی توسط شرکت بریتانیایی
Volant Media UK
اداره می‌شود، اما ساختار مالکیت آن پیچیده و چندلایه است و از طریق شرکت‌هایی در بریتانیا و جزایر کیمن انجام می‌شود. طبق این گزارش، این شرکت در سال‌های اخیر با زیان‌های سنگین و بدهی‌های بزرگ (بیش از ۴۰۰ میلیون پوند) روبه‌رو بوده و اخیراً بخشی از بدهی‌ها از طریق تبدیل بدهی به سهام بازسازی شده است. در جریان این تغییرات، سهام قابل توجهی به یک شرکت ثبت‌شده در جزایر کیمن به نام
Info-Cast Cayman Limited
منتقل شده که مدیر آن فردی به نام
صالح حسین الدویس
معرفی شده است؛ او در گزارش FT به‌عنوان مدیری مرتبط با گروه رسانه‌ای سعودی
SRMG
شناخته می‌شود. این گزارش تأکید می‌کند که مالکیت شبکه شفاف و مستقیم نیست و در قالب ساختارهای مالی پیچیده و آفشور انجام شده است
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/12910" target="_blank">📅 00:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12909">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شاهزاده رضا پهلوی :اگر اروپا می‌تواند اتحادیه خودش را داشته باشد، چرا ما نتوانیم در خاورمیانه اتحادیه‌ای داشته باشیم؟
چرا نتوانیم در پروژه‌های مشترک مربوط به امنیت ملی، اطلاعات و حتی همکاری‌های نظامی همکاری کنیم؟
چرا باید بخش زیادی از بودجه‌مان را صرف تسلیحات و مسابقه تسلیحاتی کنیم، به جای اینکه این منابع را صرف رفاه، صندوق‌های بازنشستگی، بهداشت و آموزش کنیم؟
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/12909" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12908">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیویورک پست: وجوه مسدود شده مستقیما به ایران ارسال نخواهد شد، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده خواهد شد و پرداخت آنها منوط به تعهد تهران به باز کردن تنگه هرمز و پاکسازی مین‌ها خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12908" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12907">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شاهزاده رضا پهلوی:تصور کنید که فردا مدل سیلیکون ولی در سیستان و بلوچستان اجرا شود. چرا که نه؟
هر چیزی که کشور نیاز داشته باشد از هوش مصنوعی گرفته تا فناوری و نوآوری می‌تواند در آنجا توسعه یابد.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/12907" target="_blank">📅 23:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12906">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام دولتی:
نشست ترامپ در اتاق عملیات به پایان رسید وحدود دو ساعت به طول انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/12906" target="_blank">📅 23:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12905">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیویورک پست:
زمان نهایی شدن تفاهم‌نامه بین آمریکا و ایران مشخص نیست
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/12905" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12904">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=ciyizOj8UegN5nLl57vLezTtzBzuP2M3bKa2NcxFnllUfVdgkkiN9r2_5rPZfJ9Lu4B1MCCQtEHI3H1oZidQZngHcbc68ysZHBkIN_KF0gi26kAwPz-bTn_Ht_4zc1SCX06zv6XEcZn-cXbbNF86UYWdxC_sWGiNWh3NIdI9Fs6eKxAztdi7UTcKew9ZOIo1_Ukm_BQoD_oAYOlczQZu59w_DfRTISntk6kgZ3cgZfilWmMMaJunlrDlJFCGDMesqSVFCijlVdQAUnsSa_r7cpy3_kzLpl6_j0xquXxdYWgvpgh52iLrQFDfsMA-5D4XwLQL9Pz2ErRlZFUVw_MTKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=ciyizOj8UegN5nLl57vLezTtzBzuP2M3bKa2NcxFnllUfVdgkkiN9r2_5rPZfJ9Lu4B1MCCQtEHI3H1oZidQZngHcbc68ysZHBkIN_KF0gi26kAwPz-bTn_Ht_4zc1SCX06zv6XEcZn-cXbbNF86UYWdxC_sWGiNWh3NIdI9Fs6eKxAztdi7UTcKew9ZOIo1_Ukm_BQoD_oAYOlczQZu59w_DfRTISntk6kgZ3cgZfilWmMMaJunlrDlJFCGDMesqSVFCijlVdQAUnsSa_r7cpy3_kzLpl6_j0xquXxdYWgvpgh52iLrQFDfsMA-5D4XwLQL9Pz2ErRlZFUVw_MTKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت:
ما حدود ۱ میلیارد دلار از رمزارزهای ایران را توقیف کرده‌ایم فقط مستقیم کیف‌پول‌ها را گرفته‌ایم.
برخی از آن‌ها شاید همین الان در حال تایپ کردن باشند و هنوز متوجه نشده‌اند که کیف‌پولشان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/12904" target="_blank">📅 23:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12903">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شبکه کان اسرائیل :
نتانیاهو خواستار از سرگیری حملات به ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12903" target="_blank">📅 23:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12902">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پست جدیددد اتاق جنگ داغ داغ کلیک کنید و کارای اداریش رو انجام بدید
💥
https://www.instagram.com/reel/DY7xeuCRP_4/?igsh=aW9oOXNnbno1NDJ6</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/12902" target="_blank">📅 22:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12901">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNW2y9F6aqjs1B6Qjx12shcj617DkjhDuRQL4wFNo4pHiLUC16l00RrOlCT0rumeQSgpr-ADzi0NAcxxjVTJcA_5p74TVf52CT9kZpe-p0oQ-Ql9EZOvN_7PWWy7UkTFbkkRN4ps2KEHEOQtKerEuos76RZmoLMhvGDbVw_as5tDWXiCK4gY3-qRYk-zck01vafNgL0WIti7bGDGPvE9i75wsMJ5Zwd9Nz9X7K9cTwU1KrkFhYEFakyLN_B6MFtWZ-G2XxZxMHr3KtT804zBaHX14VnLidmM2pFfVZPtXb6EIhJzdFeLOU2uWiKLUvUn2-jB1U91bpA1HK6yxVofkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/12901" target="_blank">📅 22:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12900">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">المانیتور: تیم ترامپ، در اقدامی قابل توجه، ایده ایجاد یک صندوق ۳۰۰ میلیارد دلاری را برای ایران مطرح کرده است.
این پیشنهاد در شرایطی مطرح می‌شود که پیش از این، تهران یک پیشنهاد تجاری مشابه را رد کرده بود.
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/12900" target="_blank">📅 22:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12899">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش انفجار دارم از‌ بندر</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/12899" target="_blank">📅 22:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12898">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/12898" target="_blank">📅 22:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12897">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدای نوتیفیکیشن پولای بلوکه شدست دارن واریز میکنن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/12897" target="_blank">📅 22:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12896">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تسنیم: ریز پرنده دشمن رو تو قشم زدیم
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/12896" target="_blank">📅 22:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12895">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/12895" target="_blank">📅 22:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12894">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">منابع محلی ۲ انفجار در قشم همزمان با فعالیت پدافند هوایی گزارش دادند.
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/12894" target="_blank">📅 21:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12893">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cf89fccf.mp4?token=iGNKf3wsFQlGvv3tRCUrCPMJRO1SgZo5d_SUMo2ijSvuL9SQw3xhHSrn6fIvLrcXbcIS07OtlT19XVIJwNuQlJWqFU_uqzCDzbb9jMqfxKr1W5tO8qYzXDZ8Lrr2pQHzpbv6uAc5Y7PhLtD_wgpJr-xiG9cT9Qb8_Mwj533vq-pq_hpjFf89JMNqNDfWXYymzDXcccUFAEGqy8ZNyVUmIYGSFk7gNdkHtHaHu-0LZTPCRgTM6SYE8cTKY9w7H5nRv0TWJyIxsJaSfR_xviOHsO2cuRvqMMCMhx2opxKjj1yOpYl6xkDNkynck8rbZYluhhFckugnSc8jVHAGkS6jmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cf89fccf.mp4?token=iGNKf3wsFQlGvv3tRCUrCPMJRO1SgZo5d_SUMo2ijSvuL9SQw3xhHSrn6fIvLrcXbcIS07OtlT19XVIJwNuQlJWqFU_uqzCDzbb9jMqfxKr1W5tO8qYzXDZ8Lrr2pQHzpbv6uAc5Y7PhLtD_wgpJr-xiG9cT9Qb8_Mwj533vq-pq_hpjFf89JMNqNDfWXYymzDXcccUFAEGqy8ZNyVUmIYGSFk7gNdkHtHaHu-0LZTPCRgTM6SYE8cTKY9w7H5nRv0TWJyIxsJaSfR_xviOHsO2cuRvqMMCMhx2opxKjj1yOpYl6xkDNkynck8rbZYluhhFckugnSc8jVHAGkS6jmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدافند قشم همچنان فعاله
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12893" target="_blank">📅 21:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12892">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امشب از ته وجودتون خالصانه از خدا بخواهید امیدوارم که ندای ما را بشنود و بهترینها برایمان اتفاق بیفته
🍀</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12892" target="_blank">📅 21:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12891">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">سلام اين  مسير دقيقا مسير قاهره هست  . درست داره ميره ولى ما چون مسير قاهره رو بلد نيستم فكر ميكنيم داريم اشتباه ميريم</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/12891" target="_blank">📅 21:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12890">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a2a5d870.mp4?token=b1SGuR5CFqWq-g0pes1f51xsiyuAJBynZpMZDJ8usdDKMfRItQheqvteNVebyukTK3S6vJNndSJa6VRUDMvCOAI84TZrgZy9r0FDCGTevjuao6087a4mcn4Jh6tBTeeYC6A8pIfQDYj_2FF-5vb3AjAAbj4iCFC4mMvEUWgBVqj_gWOml7M9w-gMkFvXdMVm4wvRv8YO2YWzmYdOiK7sLLl0z_oJajwb0z7OTcBzvXt5Qix4F71kpRtgL3FhhHM4qOVAXK1aq3KhAXz4kZ3JO45-q9kpbHQQ0XFEijPRvQ8sk1Dlv1uJ6l7WJvLXiJumVCDJK5E6O7UcCMpup_s-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a2a5d870.mp4?token=b1SGuR5CFqWq-g0pes1f51xsiyuAJBynZpMZDJ8usdDKMfRItQheqvteNVebyukTK3S6vJNndSJa6VRUDMvCOAI84TZrgZy9r0FDCGTevjuao6087a4mcn4Jh6tBTeeYC6A8pIfQDYj_2FF-5vb3AjAAbj4iCFC4mMvEUWgBVqj_gWOml7M9w-gMkFvXdMVm4wvRv8YO2YWzmYdOiK7sLLl0z_oJajwb0z7OTcBzvXt5Qix4F71kpRtgL3FhhHM4qOVAXK1aq3KhAXz4kZ3JO45-q9kpbHQQ0XFEijPRvQ8sk1Dlv1uJ6l7WJvLXiJumVCDJK5E6O7UcCMpup_s-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ :  الان پدافند قشم
💥
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/12890" target="_blank">📅 21:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12889">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
پدافند قشم فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/12889" target="_blank">📅 21:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12888">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرگزاری فرانسوی: جارد کوشنر مانع امضای تفاهم‌نامه بین آمریکا و ایران شد
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/12888" target="_blank">📅 20:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12887">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🤣
😃</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12887" target="_blank">📅 20:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12886">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/12886" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مدیرکل آژانس بین‌المللی انرژی اتمی پیشنهاد داد که قزاقستان اورانیوم غنی‌شده ایران را نگه‌داری کند
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/12885" target="_blank">📅 20:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لارنس نورمن، خبرنگار وال استریت ژورنال:
این توافقی که ازش صحبت می‌شه فعلاً یه توافق کامل نیست که تمامی مسائل از جمله هسته‌ای رو در بر بگیره
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/12884" target="_blank">📅 20:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12882">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/12882" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12881">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza Rohani</strong></div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/12881" target="_blank">📅 20:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12880">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/12880" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12879">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsa</strong></div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12879" target="_blank">📅 19:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12878">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/12878" target="_blank">📅 19:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12877">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پرزیدنت ترامپ در اتاق وضعیت کاخ سفید مستقر شد.
تصمیم‌گیری نهایی درباره مذاکرات با رژیم ایران در دستور کار است.
نیویورک پست: واشینگتن برای گام‌های بعدی آماده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/12877" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12876">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/12876" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12875">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAm.ir_reza</strong></div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/12875" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12874">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jangal bedoneh risheh (iG @yashar)</div>
  <div class="tg-doc-extra">siavash ghomeishi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/12874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/12874" target="_blank">📅 19:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12873">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فارس: متن توافق که تحت قالب «تعهد در برابر تعهد» تدوین شده، در مراحل نهایی تصویب در ایران قرار دارد و هنوز تصمیم قطعی اتخاذ نشده است.
@withyashar
کلان رژیم جمهوری اسهالی‌تو کاره فیفتی فیفتیه
🥴
🤣</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/12873" target="_blank">📅 19:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12872">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فارس : ترامپ تا نیمی از پول رو نداده همه چیز باد هوا است
@withyashar
🤣</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/12872" target="_blank">📅 19:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12871">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری فارس: ادعاهای ترامپ دروغه و فعلاً خبری از توافق نیست.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/12871" target="_blank">📅 19:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12870">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmR5vIk3V6v45GzLqgwz-CURXHtfM6tRgPtloL99Utn3Gl1p06bPFUpYzlZJwk0rT_d0WJM9jsXtcqMCUuL60i50atrPK2LK00kB4zhidrvaymloqKJJKglfIiLSLARPCb1EaR50HbwLZZToGCc-eu1iITBHhrQMK7Q6YtbGbwN_EoEucQUtAWzRCObffmMdHHTAeSZjlGD6KzLsbagr57VBfNrgeDpRn1zuU5UlkHj_OhZPJD6vZqMkL_emRZaP261mUbD9SZL_FZ6fEML3laa6YcpQowUfWH2rTn_0_wz5vdkws1WdgVGTZN6LZRDRpotTYfJzTFU1BdwG2eKjtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از پست ترامپ در تروث سوشال، قیمت نفت برنت برای اولین بار پس از 50 روز به زیر 90 دلار در هر بشکه رسید.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/12870" target="_blank">📅 19:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12869">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/12869" target="_blank">📅 19:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12868">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرنگارهای نزدیک به کاخ سفید می‌گویند: ترامپ منظورش را در پستش اشتباه بیان کرده بود؛ او در واقع پایان محاصره دریایی علیه ایران را اعلام نکرده.
بلکه منظورش این بوده که اگر ایران با این شروط موافقت کند، آن محاصره لغو خواهد شد.
@withyashar
🥴</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/12868" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12867">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار : یا موسئ ادرکنی
@withyashar
معنی ادرکنی : مرا دریاب و به فریادم برس</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/12867" target="_blank">📅 18:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12866">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12866" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12865">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال ۱۵ عبری: به نظر میرسد ترامپ با یادداشت تفاهم با ایران موافقت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/12865" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12864">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الجزیره: ناوگان سوخت رسان های آمریکا در فرودگاه بن‌گوریون تا ۷۲ ساعت دیگر به پایگاه های اصلی خود در اروپا برمیگردند
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12864" target="_blank">📅 18:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12863">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12863" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12862">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.  تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما…</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12862" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12861">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ytts1fIKleL8bLL-eAP21cWNsDAoYJCMyhh5ZWkN-iA2bH_o4vQl1TeEqQIaW4E73c9kZWw3NocqZkzaaOet7sEOUIVOJ-RZqmV6U94Ms3oB4azEQgO5utRmzEhu9LXuHvubqzsmmLBWOWg72GyNRz3aM7GJW4ZEMEz1kS2hWBnZUpTWBDOqAD65-AONpjzh85Vq7ngo_J_paOR6HYfTQlOBJvyarcVG6H5DP7CalHxiJ8PGT4zb1QW1zBvKfn2jFGuOYvUxjDBX33QLYZEwBoDXAqljccFwe4TgQUnfbhfY3qPfYtB6xnwahYesnJvG5cd9Hu7msNWkiIyja0cHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
@withyashar
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
@withyashar
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/12861" target="_blank">📅 18:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12860">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02caddcc.mp4?token=ODwDPdTYPXJ45arzmmTghebUfBQkT3gI2eo0UudV1Ilxp6eChWebOlIQVTKFA9mdA4XsyeQknnudH4fNBbGNbRSzfllQa_ZWoeFO-bQROEuCSOtHgqMHQn3UMPD3bmHv6MSQBTZApFl7VlzzIYL7BwTp16fOhCt7mSLCbexPEtS2TZxb_7aqevGD8nFG0LqnIedqyFf3kmiyiF9EHXGJ7aW1Y491QojmTLYegusRGon6YcTZrr4yhywcfDBuBClsqcVse9bZfGB7R5tFBgedWcbuELmwvpz9oEj3_GQNhwqLCCphpPwHhEixMTe5FHRo4i1Hu1V0xFcRGnlKgkeneg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02caddcc.mp4?token=ODwDPdTYPXJ45arzmmTghebUfBQkT3gI2eo0UudV1Ilxp6eChWebOlIQVTKFA9mdA4XsyeQknnudH4fNBbGNbRSzfllQa_ZWoeFO-bQROEuCSOtHgqMHQn3UMPD3bmHv6MSQBTZApFl7VlzzIYL7BwTp16fOhCt7mSLCbexPEtS2TZxb_7aqevGD8nFG0LqnIedqyFf3kmiyiF9EHXGJ7aW1Y491QojmTLYegusRGon6YcTZrr4yhywcfDBuBClsqcVse9bZfGB7R5tFBgedWcbuELmwvpz9oEj3_GQNhwqLCCphpPwHhEixMTe5FHRo4i1Hu1V0xFcRGnlKgkeneg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم تحلیلگر ارشد صدا و سیما:   دوران بمب اتم دیگه گذشته الان با عملیات میکروبی و بیولوژیک میشه حمله کنیم و بعدش نگیم که ما بودیم
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12860" target="_blank">📅 18:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12859">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">️فاکس نیوز به نقل از وزیر جنگ آمریکا: ایران دو گزینه دارد: یا از طریق مذاکره برنامه هسته ای خود را کنار بگذارد یا از طریق نیروهای ما
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/12859" target="_blank">📅 17:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12858">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تسنیم : مذاکرات در جریان است و متن توافق تغییر هایی داشته است
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/12858" target="_blank">📅 17:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12857">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEic6OzAAUuNp3A7B6GmCagn9yr3rt5VZkY2XHTU7QqUn1bgVKcFuVh7Vxj_c3wkezeB0VXOKTP19dqVooAWGVOZnqnbBzrZvC0drQ5fbSKm-1NHP_i2zCYCbp03YNYWyISmtaUbqKUA-E3VuAv0GK0s2M4XZ0aA1TZw9UcgpaADaA4ZmSSe-vqNv_uBxuCCMquDZWi_mMJQCAwU37u-tV6qTqapnoOCXh9MaTaCLIqb2-kl5_7m7TdCdzzWbjV0f_mZb56cJIL8KWOUcpqYS38dBUT2oBC30MFv13cuEuT5rOM91HbJ5fGuBOIOrWhy-dRyFvNHVKN4uw-GVZgQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مم با قر خالیباف‌ در اکس :
۱- ما امتیازات را نه با گفتگو، بلکه با موشک‌ها می‌گیریم، در مذاکره فقط آن‌ها را تثبیت می‌کنیم.
۲- هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳- پیروز هر توافق، کسی است که از فردای آن بهتر برای جنگ آماده شود.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/12857" target="_blank">📅 16:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12856">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">️سی‌ان‌ان: ترامپ به مشاورانش گفته  که برای تصمیم‌گیری در مورد امضای توافق احتمالی با تهران به چند روز زمان نیاز داره
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/12856" target="_blank">📅 15:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12855">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9HaUrQq17gWoX_NFlwe1d9sSWTF4rHni1QOEG0MtOg5cUJWDx1SC4fF7gUEa42vC0AbDXSuvxZyJCCUe9tRFR59m6uXWscyY-1pgeZPZ-zSIyrfj8zeljjPTBES_1h0-SZrJ7FRRPvWi99QvC8gw1K8Pu2v398FvV2NVQYoaUSnwuvn9Gnpu5Kwni389M9lCROyEsHR6ufLowHLza2Lu9_H5gfrfUxSWtFd3Q9qZ6ZYWi23qU6qSqKXmJQzuSl9uSAJVCGAyol65mFXORx7Yn6rl7reJ40aQ_Fs-yInE394M6jTvnYUKyBr3eo1z0C_wsa6AtXfmRwoYuJSRUI2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سری سوالات بی جواب تجمعات شبانه
😃
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/12855" target="_blank">📅 14:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12854">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froms@ti🍁🍂️</strong></div>
<div class="tg-text">سلام یاشار جان
من نامزدمو یه هفته پیش از دست دادم سرطان داشت
😔
تا لحظه ی اخر میگفت ناامید نباش یاشار گفته میزنه،تو دی ماه هم واقعا به سختی نجات پیدا  کردیم از تو خیابون .واقعا اگه ما پیروز نشیم من حس میکنم خون این همه ادم پایمال میشه،ما فقط به امید شما داریم زندگی میکنیم.هیچ وقت اخرین حرفشو تو ملاقات اخر یادم نمیره.فقط پیام دادم بگم  حتی امید اون ادمی که روی تخت بیمارستان هم نفس های اخرشو میکشه هم  هستی
🥺
خدا حفظت کنه واسه ما
🙏
❤️
🌺</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/12854" target="_blank">📅 14:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12853">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=PXUNVFZeCrZ5yW1uQYDWw45qcrOhmkyAVjqxMfnCA4xjjaVhMeLQsg593gGK-JzABpc4ucEm1o9HlerhfOvCFB3nQqA5XdYuBiBAevtsfq5U92HN0q7oO8GGeQuyU-BESuzR3ZM9Wj3X7WtGnY9t-PFyqxX07RKSfiSj16I80oVaizCnUaiY-ZkDBN5hLOgkSuj-OSxiE01gIopb0GWTMufdQAu14Pd5b-GLjA5q5V6yUAaCsZyuw1VsvpL2XhxtGFsaGzFGL2dsMEqBHoAMIhtea0G0bcSkkKvh3wFdS39qSPvUDSZuYNdYha_a8pOHjaAD7WycS8QtN-l5TavdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=PXUNVFZeCrZ5yW1uQYDWw45qcrOhmkyAVjqxMfnCA4xjjaVhMeLQsg593gGK-JzABpc4ucEm1o9HlerhfOvCFB3nQqA5XdYuBiBAevtsfq5U92HN0q7oO8GGeQuyU-BESuzR3ZM9Wj3X7WtGnY9t-PFyqxX07RKSfiSj16I80oVaizCnUaiY-ZkDBN5hLOgkSuj-OSxiE01gIopb0GWTMufdQAu14Pd5b-GLjA5q5V6yUAaCsZyuw1VsvpL2XhxtGFsaGzFGL2dsMEqBHoAMIhtea0G0bcSkkKvh3wFdS39qSPvUDSZuYNdYha_a8pOHjaAD7WycS8QtN-l5TavdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست ، وزیر دفاع آمریکا با لاتی‌ پر مانند مربیی که تیمش را به زمین میفرستد،  خطاب به نیروهای آمریکا روی ناو USS Boxer گفت:
«رئیس‌جمهور گفت: ایران یا می‌تواند راه درست را انتخاب کند یعنی پای میز مذاکره توافق کند یا با مردِ سمت چپ من طرف شود.»
«آن مردِ سمت چپ، اتفاقاً من بودم.»
«اما در واقع من نیستم…»
«شمایید.»
یعنی شما نیروهای نظامی آمریکا هستید.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/12853" target="_blank">📅 14:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12852">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromomid.behroozi</strong></div>
<div class="tg-text">سلام یاشار عزیز من امشب عروسیمه امشب میزنه آماده باشم تو باغ مهمونا رو از قبل آماده کنم میزنه ؟؟
😂
😂</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12852" target="_blank">📅 14:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12851">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بر اساس تحلیل نشریه اکونومیست، طرفین درگیر ممکن است بیش از هر زمان دیگری به یک توافق نزدیک شده باشند.
با این حال، این توافق جامع نخواهد بود و جنگ را برای همیشه پایان نخواهد داد.
این نشریه در ادامه توضیح می‌دهد که چگونه ملاحظات و بازی‌های سیاسی، عامل اصلی ارسال این پیام‌های ضدونقیض از سوی طرفین است
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/12851" target="_blank">📅 13:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12850">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیویورک تایمز: یکی از جدیدترین و شگفت‌انگیزترین عناصر پیش‌نویس توافق صلح ایران، یک صندوق سرمایه‌گذاری پیشنهادی برای ایران به مبلغ ۳۰۰ میلیارد دلار است.
ایران در ابتدا این موضوع را به عنوان غرامت برای خسارات جنگ (که آن را بین ۳۰۰ میلیارد تا ۱ تریلیون دلار تخمین می‌زند) مطرح کرد. طرف آمریکایی آن را به عنوان یک «صندوق سرمایه‌گذاری بین‌المللی» که به تسهیل آن کمک می‌کند، بازتعریف کرده است
یک چارچوب نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از استیو ویتکوف و جرد کوشنر نشأت گرفته است که پروژه‌های املاک و مستغلات تهران و یک ابزار سرمایه‌گذاری گسترده‌تر را به عنوان شیرین‌کننده‌های معامله مطرح کردند
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/12850" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان من گفتم فردا میگم کجا متن ها رو بفرستید دوبار هم در متن تاکیید کردم! پیغام هایی که الان دایرکت دادید بین پیغام های‌دیگه میره و از دست میره حتی نیمتونم بخونم
😟
چرا درک نمیکنید خیلی واضح گفتم</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/12849" target="_blank">📅 13:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12848">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی…</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/12848" target="_blank">📅 13:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12847">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=A-mzgRaw7gjCW4Xzzt4jPi3JEjjWsgt-8Ejg4bUJu9H3m4wTYGdzICQSJrogLZ47Uqc_p7PHaWLwEyiq1Fw8FLJvakMF95mCby9TOeQyDbbTjaNXW-mqoNdFpEoWlr5g6I8GLHwrYv3y6KwbvUwaMFT1GvQ_5p6Q4E-CYRIbfHCgkObJwgJkph26ciie8VXYbQDwoV-SAiUmdJVBtGfM-VSjw6P4tmbazWSSmagswUrSSxM57jvU9ym9RmB64UZZaoZTZUT9r8fR_s7OCaco3X3SH2obmEFrZDZDuBOqZBonEYo917ra-NPG8NAsTKLQDtRDTpY_EnAQiRDtcz5JEjPoDeNGmww1tZ4GLIZB2LVSjuHu8bDwihbIcBYOSnzLkhxUMmrRTDx9QMGOJmH93im3ptRHtrYjNs7w8GEFQhx0Xsq2rQ2Qt8WR2ueDaD33o3OUZsUl5a4GLGeKa0f9a3Nafv2LsGOeOhgW29lM-1YpQgUeH0CjOYHPF7_-3DPuQNRLzlQcXmm9aYIvdGZnWGp_EZzT_ChTBrGI408yJHOX0fllzzyKBud-7wAr9uw_4gU6xfppV9B3DMa9RLvwq85FoKx3CDbkP8tGtQhijZTSzQv6RTJO6abXiVxbnytvMPAEFU0Nb-ZMPC7VMxc9klJUB5QhE2jbAkLQz_Zxwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=A-mzgRaw7gjCW4Xzzt4jPi3JEjjWsgt-8Ejg4bUJu9H3m4wTYGdzICQSJrogLZ47Uqc_p7PHaWLwEyiq1Fw8FLJvakMF95mCby9TOeQyDbbTjaNXW-mqoNdFpEoWlr5g6I8GLHwrYv3y6KwbvUwaMFT1GvQ_5p6Q4E-CYRIbfHCgkObJwgJkph26ciie8VXYbQDwoV-SAiUmdJVBtGfM-VSjw6P4tmbazWSSmagswUrSSxM57jvU9ym9RmB64UZZaoZTZUT9r8fR_s7OCaco3X3SH2obmEFrZDZDuBOqZBonEYo917ra-NPG8NAsTKLQDtRDTpY_EnAQiRDtcz5JEjPoDeNGmww1tZ4GLIZB2LVSjuHu8bDwihbIcBYOSnzLkhxUMmrRTDx9QMGOJmH93im3ptRHtrYjNs7w8GEFQhx0Xsq2rQ2Qt8WR2ueDaD33o3OUZsUl5a4GLGeKa0f9a3Nafv2LsGOeOhgW29lM-1YpQgUeH0CjOYHPF7_-3DPuQNRLzlQcXmm9aYIvdGZnWGp_EZzT_ChTBrGI408yJHOX0fllzzyKBud-7wAr9uw_4gU6xfppV9B3DMa9RLvwq85FoKx3CDbkP8tGtQhijZTSzQv6RTJO6abXiVxbnytvMPAEFU0Nb-ZMPC7VMxc9klJUB5QhE2jbAkLQz_Zxwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر:
ایران امتیاز های خیلی قابل توجه، مادی  به ایالات متحده داده که قبلا میگفت غیر ممکنه
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/12847" target="_blank">📅 13:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فارس نیوز ، خطیب نماز جمعهٔ تهران: دشمن متوقف نیست، ما باید در مرز دانش و فناوری حرکت کنیم
حجت‌الاسلام ابوترابی: تعرض آمریکا در سحرگاه دیروز به نقطه‌ای در حاشیه فرودگاه بندرعباس که نه خسارت جانی داشت و نه خسارت مالی، اما تعرض به آسمان و زمین ایران بود. این تعرض از پایگاه هوایی آمریکا در منطقه انجام شد
@withyashar
🥴</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12846" target="_blank">📅 13:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی رسمی و محترمانه صحبتهای خود را بنویسید  و امروز بر روی متن تمرکز کنید و فردا از ساعت ۱۰ صبح تا ۱۰ شب برای من ارسال کنید تا چکیده ای از تمام آنها را ارسال کنم و فقط کلام من نباشد. حتی شده یک کلمه از پیام هر شخص را برمیداریم و متنی باهم میسازیم که در خور باشد. پس از شما دعوت میکنم به این کمپین بپیوندید ،لطفا امروز و فردا از فرستادن دایرکتهای غیرمعمول بپرهیزید سوال بیشتری را نمیتوانم پاسخ بدهم متن کامل است هر صحبتی که دارید  در  همان متن بنویسید تا همه با هم متن پایانی را استوری،  کامنت ، دایرکت و ایمیل کنیم
🙌🏾
. شروع ارسال فردا ۱۰ صبح و آخرین مهلت ارسال برای من  فردا ۱۰ شب است.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/12845" target="_blank">📅 11:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تحلیل عوستاد رائفی پور :
آمریکایی‌ها نیروهای بیگانه فضایی هم کمک گرفتن
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/12844" target="_blank">📅 11:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12843">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/12843" target="_blank">📅 11:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسرائیل هیوم در گزارشی نوشت موساد در سال‌های اخیر شاخه‌ای محرمانه برای نزدیک‌تر کردن سقوط جمهوری اسلامی ایجاد کرده است. به گفته منابع آگاه، رییس موساد متقاعد شده است که اگر ترامپ با تهران توافق نکند و محاصره دریایی را ادامه دهد، جمهوری اسلامی تا پایان سال ۲۰۲۶ سقوط می‌کند.
ماموریت ابتدایی این شاخه که در سال ۲۰۲۱ و پس از آغاز ریاست داوید بارنیا بر موساد ایجاد شد، عملیات‌ هدفمند برای کنار زدن مقام‌های ارشد جمهوری اسلامی بود، اما به‌تدریج به بخشی از راهبرد گسترده‌تر موساد برای «تغییر رژیم» تبدیل شد.
رییس پیشین این شاخه به اسرائیل هیوم گفت موساد در گذشته بیشتر از طریق ترور افراد را حذف می‌کرد، اما اکنون افشای اطلاعات شرم‌آور یا آسیب‌زننده درباره مقام‌ها می‌تواند آن‌ها را از حلقه قدرت خارج کند؛ روشی که به گفته او «ارزان‌تر و ساده‌تر از عملیات ترور» است.، مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/12842" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12841">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنتکام : ادعا: تلویزیون دولتی ایران ادعا کرد که نیروهای ایرانی یک هواپیمای آمریکایی را در نزدیکی بوشهر سرنگون کرده‌اند. نادرست.
حقیقت: هیچ هواپیمای آمریکایی سرنگون نشده است. تمام دارایی‌های هوایی ایالات متحده در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/12841" target="_blank">📅 10:09 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
