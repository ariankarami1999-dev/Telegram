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
<img src="https://cdn1.telesco.pe/file/JpbrunaZsluAJ86G63wtg8VjadqD6qdDHUeSwtN_g9oLJKzuBnXLiBaoHnpfD09jTlCEuFIr82V4Ox9yrLFdQmUx5WDJJqePickmi5tllKXiYUVgFMRpqZ5BFnoom_pSu-wmTZad9k8XNm2l8uWcs6BfSPlK494gIz0mgOpTcKV-XzwWVF2h0ofn-qH-zS6Iqce6k2L5QiQhwwyEbe4MTPPvyDgeFa8lp1yobunYO-IoKKtDTCGcu9UA7SNork5jE0LVxq63_37-nz4KIG1ljCTD3Wqib0CUIkr4KF7O3HnO0jLDpvZZ96HZArbKs77iBHpq6evyP65ZYdf7QF4V0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 21:07:56</div>
<hr>

<div class="tg-post" id="msg-4468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ly_8C_BvUKp0XIwjp9biG-KPvhfcPEn0I9pUfckv06iN7XIAUY0JDehP39wilhoIOH7a7vewTIc0KGJEzgtfbfC40oqEz5FtJMY_hEWDg503VqBrD1tafKC_RHRQeDPjFcVFN-8R46y0U-LbIf-J1FfvwB0W0Zqa5ddxnT1UrSMQY4MvvpcFkIywQuMhk69L73dHfqZei9_ypXiv0qGh7kL8qlrNDG-N8rHAhmGG-PhLjVCJUkwnVMM-dGGSGU3j4KF7GrKThq6PKYws2iSdj1WTjZngVx8OKusIGc4k-PIpnZQR_1uaQ-JxBUGEnXQAgH-zMssKhQEkEf5-xR7MJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا گویا دامنه‌ی
t.me
مجددا در دسترس قرار گرفت بعد از توییت پاول</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/MatinSenPaii/4468" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ببخشید.
خودتون میدونید دیگه بانو
❤️</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/MatinSenPaii/4467" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4466">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=fzNzXcU_19f0yRJh9ZT7JFeQVyhhySj_sSy-9nq5Jla0ylFiyL2Ez9ntQbmptm_edi7sNZUWEivJZLYW-bejHqfx6p3Kw0F1zfCh74P-AkHojlLjCPejzpjh8Dzzs8QkfV4AmOl1AJ_b2TpErQb2gC1Va7eDXTXofT86_KwFv0JZT1bs1vfmJUE_4-zyhPmDEwLjhOtT9vOwARyq19oidJ1pdT7kXGa6kTWR1rYU2Me5Gaexq-woZe-7p-53QwMY6HT5ZjWxaN77z6rmHR9OeLrceKO31Z9Y0JP_iWGeQ9bhMt2dAi9tPMfEJKnLgffYPvO9RwUZc_QMSWVmF5SEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=fzNzXcU_19f0yRJh9ZT7JFeQVyhhySj_sSy-9nq5Jla0ylFiyL2Ez9ntQbmptm_edi7sNZUWEivJZLYW-bejHqfx6p3Kw0F1zfCh74P-AkHojlLjCPejzpjh8Dzzs8QkfV4AmOl1AJ_b2TpErQb2gC1Va7eDXTXofT86_KwFv0JZT1bs1vfmJUE_4-zyhPmDEwLjhOtT9vOwARyq19oidJ1pdT7kXGa6kTWR1rYU2Me5Gaexq-woZe-7p-53QwMY6HT5ZjWxaN77z6rmHR9OeLrceKO31Z9Y0JP_iWGeQ9bhMt2dAi9tPMfEJKnLgffYPvO9RwUZc_QMSWVmF5SEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خودم نگهش میداشتم
👍</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/4466" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4465">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.  اگر…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/4465" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4464">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLira.</strong></div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.
اگر برنده‌ی این شمع می‌شدید، برای خودتون نگهش می‌داشتید یا به کسی هدیه‌اش می‌دادید؟ اگر هدیه‌اش می‌دادید، اولین کسی که به ذهنتون می‌رسه کیه و چرا؟
برای شرکت توی چالش:
⬇️
در کانال لیرا عضو باشید.
⬇️
این پیام رو توی کانال‌تون که پابلیک هست فوروارد کنید.
⬇️
به سوال بالا پاسخ بدید.
🎁
جوایز:
🥇
نفر اول: یک شمع کروم صدف لیرا
🥈
نفر دوم: 15% بن تخفیف
🥉
نفر سوم: 10% بن تخفیف
مهلت این چالش تا ساعت 12 امشب هست و نتایج چالش فردا ساعت 10 صبح در کانال لیرا قرار داده میشه
🩵</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/4464" target="_blank">📅 16:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4463">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مثل اینه که یکی با Toyota دزدی کرده باشه
برق کارخونه تویوتا رو قطع کنن تا دیگه نتونه ماشین بفروشه به دزدا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4463" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب آموز(m J)</strong></div>
<div class="tg-text">دامنه t[.]me تلگرام به دلیل تحریم OFAC آمریکا از دسترس خارج شد.
در ۱۳ جولای ۲۰۲۶، دامنه کوتاه t[.]me تلگرام (که برای لینک کانال‌ها، گروه‌ها و پروفایل‌ها استفاده می‌شود) در سطح جهانی از DNS حذف شد و مرورگرها دیگر نمی‌توانند آن را باز کنند.دلیل:
ثبت‌کننده دامنه .me (Identity Digital) وضعیت serverHold را اعمال کرد. این اقدام مستقیماً به دلیل تحریم‌های OFAC (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) بود. OFAC شرکت First VPN Service (1VPNS) را به لیست تحریم‌ها اضافه کرد — سرویسی که به حداقل ۲۵ گروه باج‌افزار (از جمله Avaddon) کمک می‌کرد تا حملات خود را پنهان کنند. یکی از شناسه‌های این شرکت، کانال تلگرام t[.]me/FirstVPNService بود.
چون نمی‌توان فقط یک لینک داخل دامنه را بلاک کرد، ثبت‌کننده کل دامنه t[.]me را از DNS جهانی حذف کرد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4462" target="_blank">📅 15:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جوری نوسان برق رو اعصابه که هیچ کاریمو نتونستم برسم کل روز. نه سه راهی روشن میشه که لپ تاپو بزنم شارژ، نه نت فیبر نوری کار میکنه کلا قطع شده از صبح، نه آنتن درست حسابی مونده و همش قطعی داره، نه کولر کار میکنه که بشینم لااقل یه کتاب بخونم🫩</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4461" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جالبه که هیچ توضیحی بابتش داده نشده
هیچ واکنشی هم از سمت تلگرام هنوز ندیدیم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4460" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4459">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𐌼𝛜)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXosbzdzSzZVO-vFNuaHYPBNb2AGGtPFRlJniBpernDISNsvCVMhWz-Bi3K6BF0iQCLoXDv-w15jQavVu36DLWpaNPLjct4gRg0vyMQ9054aSCzAcCb0ARD0y_h9dcUnADfQr4JX2ufkcmOZlX14zCXwT9NmfQlImPfCHkKqmeGcrOb31q-fQhldl791UtMlNvS-egsy_5hc8d8f9p8Ovn-sLY1Cbnw-aKmang4ZEZex2wuQbf4ASa8U4n5SvbB5CsikFkOg7e0tqpoEZXhVLL0n1xfn_MKDsDcj31OLUmO5eC6SFUVlN3SfFyIdk2wZS7aXdXfpgY8gzF-6cxUVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
اختلال در لینک‌های
t.me
از ساعاتی پیش، کاربران زیادی گزارش داده‌اند که لینک‌های
t.me
باز نمی‌شوند.
⚪️
طبق اطلاعات
WHOIS
، دامنه‌ی
t.me
از ناحیه‌ی DNS رجیستری .me حذف شده؛
اما همچنان تلگرام واکنشی نسبت به این موضوع نداشته.
ℹ️
اگر امروز موقع باز کردن کانال‌ها، دیدن تصاویر گیفت‌ها یا ورود به بعضی لینک‌های تلگرام به مشکل خوردید، دلیلش همین اختلال است.
📰
تا برطرف شدن مشکل، ممکنه بعضی از لینک‌ها و سرویس‌های وابسته به
t.me
به‌درستی کار نکنند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4459" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الان برای یه سری کار داخل فتوشاپ، چندتا اسکریپت با Claude (پلن رایگانش. توی صفحه چت) نوشتم که کارم رو 20 برابر سریعتر کرد.
بهش فکر کردم، و به این نتیجه رسیدم که اگه فتوشاپ بلد نبودم طبیعتا نمیدونستم میتونم همچین کاری کنم.
از طرفی اگر از قابلیت‌های AI باخبر نبودم که میشه اصلا کارها رو باهاش Automate کرد یا لااقل، پرسید که "آیا فلان کار رو میشه Automate کرد یا نه؟" هم مجددا همچین چیزی به ذهنم نمی‌رسید.
اینه که شما به صرف بلد بودن کار با AI شاید نتونید از 100 درصد پتانسیل یه ابزار استفاده کنید،
از اون طرف به صرفِ "خوب" بلد بودن یه ابزار هم اگر از AI استفاده نکنید و سنتی کار کنید، به راحتی عقب میفتید.
هر دو با هم عالیه!
<تجربه‌ی شخصی. نه Fact></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4458" target="_blank">📅 09:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
انتشار نسخه نهایی و پایدار MTProxyMax v1.4.0-LTS</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4457" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📱
دامنه t.me تلگرام تعلیق شد؛ قطعی ناگهانی لینک‌ها در سراسر جهان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4456" target="_blank">📅 09:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توی علم روانشناسی به «جوک ساختن با قضیه‌ی جنگ یا قطعی اینترنت» می‌گن طنز سیاه (Dark Humor) یا طنز گالوز (Gallows Humor). این یه مکانیسم دفاعی برای بقای روانیه، نه نشونه‌ی بی‌خیالی. مخصوصا سر قضیه‌ی جنگ
1- جنگ یعنی استرس، ترس و درموندگیِ مطلق. اگه این حجم از فشار رو سرکوب کنیم، عملا از لحاظ روانی مریض می‌شیم (و همچنین در بلندمدت می‌تونه ریسک PTSD رو افزایش بده.). جوک ساختن مثل یه سوپاپ اطمینان عمل می‌کنه و بهمون اجازه می‌ده این فشار رو به یه شکل غیرمستقیم تخلیه کنیم. (در عین پذیرش واقعیت، تحملش کنیم)
2- خندیدن روی بدن جواب می‌ده. سطح کورتیزول (هورمون استرس) رو می‌کشه پایین و اندورفین (هورمون شادی) ترشح می‌کنه. تو شرایطی که ضربان قلب رو هزاره، مغز با یه میم خنده‌دار، ترمز دستیِ استرس رو می‌کشه.
3- جورج ویلانت طنز رو جزو یکی از «بالغانه‌ترین» مکانیسم‌های دفاعی طبقه‌بندی می‌کنه. توی این حالت، ما واقعیت تلخ رو انکار نمی‌کنیم، می‌بینیمش؛ ولی با طنز یه فاصله‌ی ذهنی باهاش می‌گیریم تا بتونیم تحملش کنیم.
4- وقتی دوتا کشور می‌جنگن و موشک میره و میاد، شما هیچ کنترلی روی اوضاع نداری. اما وقتی باهاش شوخی می‌کنی، مغزت حس می‌کنه حداقل روی «روایت داستان» کنترل داره. با خودت می‌گی: "من نمی‌تونم جنگ رو متوقف کنم، ولی می‌تونم بهش بخندم!" این بهمون حس Agency و قدرت ذهنی برای مقابله‌ی نسبی با این قضیه توی ذهنمون می‌ده.
5- توی شرایط ترسناک، آدم‌ها به شدت احساس تنهایی می‌کنن. وقتی یه جوک مشترک می‌سازیم و با هم بهش می‌خندیم، یه حس همدلی‌ای این وسط شکل می‌گیره که تاب‌آوری جامعه رو مقابل این قضیه بالا می‌بره.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4455" target="_blank">📅 05:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YcmSnudWTb12pKPnNJ4OjHJFQVIVCqOKpXTy5RntJPeI2gJTV8xAkzqGQwMsAq-TezbFrPq48d_bLA92g46rcznJ0PXSD2rwUtF1K-rrCl92SiFKb-CVBOS_DoBgOo0JZlFXTWsTB01Rz3F93bX6xZr8WxWW4wCu9EBteFgjE0OKYX0mpvjgUFsXKM3aUJE56mH0I80lFRiFZ63s4KjjM2yJZAJJ7uADWRI0yqnO_tznS3mqOYAmvgWhHICroNgtOA5etmLHw8KfYQ-jyH3esKlP6X1eBQTA752GjaZ8J0gTvj37OsPdJgCm4C3uen-iAov8sWxZiHKDriPvg8gshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت در حال لحظه شماری برای دستور قطع</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4454" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fG0AbVcu6ewsgRs8DZM0rD-Nm5_RS1EGkqdaI5PCpd8EC1-aMV7-FEgRxsQV_aNjm4OXyWFoRSQMdh8TPcuDC_10arNjiUunvR-D6lPSUnaO0raFNSps2ekFfPSsocivh9d9xr8OgfbXoDC9c_uQtSfqBUCAKE1_7XKy_v7SYVSTaGcQE7XUoTM9k3WgYhpowvrqpALd_-mjdz5Qzw8OA4IT8Ig05qA0gEkTstxAtdQGT4NZzHvVP911Db7Lav32EaOoI395Epxfa2YD9PFGWyePqpaHgHhhAXo9XpS1wzNxujmlOh3qmNwfYw3r4iL-9nPazOyoRxyvTjWdSfbB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VIuK_ey2o9YuLAY1506Mv0PqqaIVVseVKCPAeVrc2dgT4gNmBYoI3Rtvsk_RouYRYqQPs39XhSxag1rlizhJBTBWeS9c0sZU4Tt2P2CKRucJvE-nuYND7HtcX8js2Ox_dBSpl5eh6-sib3v3wIQ1_Tv3_HBSJf4xk2O6OIIXbXmUDsMg6nTyhTXoToURDBKHbqEF-qdqlI09KsqcEKMMk-Eh_Sh0qxuvnnEEaHgIC2kJgwL7Nlgfpm3D3rSLgwgM3PpSIYvUYdWGNeixALPsphQiQ9w5kK2SCajW7Y-BlZmkYc0DeBPxHOF05o39Nd7b9RpmafFAYQueri4lyIjAvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم من یادآور خاطرات بدی هستم متاسفانه
😂</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4452" target="_blank">📅 01:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4451" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4450">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Android</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4450" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Desktop(mac-win-linux)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4449" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Master-White-DNS-@MatinSenPaii.zip</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4448" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات @dns_resolvers_bot اضافه شد   @WhiteDNS</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4447" target="_blank">📅 01:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4446">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad👑</strong></div>
<div class="tg-text">اگه دیدین جایی نوشت
تهران رو زدن
ثانیه بعد نت قطعه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4446" target="_blank">📅 01:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4445">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_8w-9J3Ydb-TS0eE3uE4cPKuJAZ4n9rp4l1W-fRt9Ytjq3jYNsMFbaDuag46HryKtDta5Df40EZ7DyUqP83kjxcmxiONMUSchVKpCvnRnr5bKxmPLrfgUYHFaLWNqLyOjU8ayH5AKMnp_cVkvQxKRnB-jWq5ozvBm0QKn3174eap3RGQcFf40qLJtf9qOUhufpBj7cQcChOL0Ys4FxAfRGGKRPA4aXiIT2zvQX1x_9yZ6zEZ7VfOEK6a5idUZgSR6zl85dlDt6pvjYpaXAV16GgvYpKO_IXg2uwpUMqFUvleaFWMYYD28roLeRYHTuqQ7cpcSFKnZmG4VCnp5HItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4445" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4444">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">صابرین نیوز داره لینک چنل سروش و روبیکاشو میده.
این یعنی به زودی نت بای بای
😭</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4444" target="_blank">📅 00:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4443">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euCx_UPx3moQVHtbsdiNZnYkOUb4F-E3J_8wjBGQbWKZqTl9XM_Ys5gXUeoRhi4MNc7_K30iSdeEVll8N_wDlIcIkR1hGhofWyOnqVh4x3ZCXJIXjxIWsjg8-G3tIiw21TlJu8xOCAhGefksX0mhPLBkmI68ntYrAS1HLEmfnHS-ijF8QyJTRzobAF2vicj6Vsbjx4doenRdRGVpeoD1OqM0HvTlgtlZZ5gS6F2D_H79uNVWoPVam5Qxm7HPmY8RZgjt2krKElh88f-_YKUH7g494sALB3rxPIOXH8bUEOr3tMCoGcChwDIxpTISTqgL6lUqMZuzLlEmCXLC4PJDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Solomon’s paradox
“انسان‌ها معمولاً می‌توانند برای دیگران توصیه‌های منطقی و عاقلانه ارائه دهند، اما وقتی پای زندگی خودشان وسط باشد، اغلب نمی‌توانند همان توصیه‌ها را به کار بگیرند”
روان‌شناسان معتقدند آنچه ما را از تصمیم درست دور می‌کند، کمبود منطق نیست؛ بلکه نزدیکی بیش از حد به مسئله است. هرچه یک اتفاق بیشتر با هویت، احساسات و آینده‌ی ما گره خورده باشد، و درگیری احساسی در ما ایجاد شود، احتمال سوگیری ذهنی بیشتر می‌شود و تصمیم‌گیری، سخت تر.
البته که احساسات، بخش مهم و تاثیرگذاری در تصمیم‌های هر انسان است؛ اما زمانی که فرد با موجی از احساسات مواجه میشود، ایجاد تعادل به مراتب دشوارتر میشود..</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4443" target="_blank">📅 00:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4441" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4440" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gavcLxUE-_WnukkG6I8GJqyA8ItkiJlm9BCvhJFu83vkBTgZgTNmj1-uXVQ15eRCqDrkKh08EbYRQpdOshqk-oNJD9tNoYdVWpQ6_zcdBxb8TUvHlGCRpgc2VDCSapK7zek5xISsvHlIQ_wyHLPpYRBh4448tsaTyYc7jaMAvlHqdMNmeTMcJfscLGs4t6ZMMTHziOAQWZtEkDhiuzJFXPBaFXsht2-hjkk1pOc8SFTP7bqZ01SxUXIn9y_PGb40bl22OGR6VLqJfQtRPkEzE3GwDiyCXvRV7I7oi3Jo5s7GJdM1s5t3NlbRskUlNp4pAF9AfdftyATKRRzmKf35pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8- بخش پایانی Integrations:
از قابلیت اتصالِ One-click به اکثر محصولات و ابزارهای پرکاربرد پشتیبانی می‌کنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4439" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAbOBbJacvMeNqOCP0gnkMIOt-1UH9P9cgrul905WhnPEAgzEGY8iiJwqCtjL6UGtM9O-OUp7HKkdIGNSmkUol1VbZwB6ojLt_8NG1Xpv5UKG2q8iWmZX7Um8Y8akA3cJH_RjY_tzVzLRTdKZPO_B5qkewQYmxgT5wNxUA82jcnwEPBTWGDXwzoViwpnAQuVhrkiPNnGsg4KQYkOUuJhQewVUl7sykJofRF9FGwoAsFG4X0M_gMCEUEme-R_ud7e5fqeLgkOSmB-fJTyea_jRlT9LKePbG8Mf9gt8n--MLdf9zb4DvxaVHCX8rgKEHV5NLgk9yQINRuDrr_BNIZG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7- بخش Apps:
می‌تونید فضاهای کاری اختصاصیِ خودتون رو داخل Rowboat بسازید؛ این اپ‌ها به تمام ابزارها و اتصالات دسترسی دارن و حتی می‌تونید اون‌ها رو با بقیه به اشتراک بذارید.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4438" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAVDIITg8JT4zKtgSeZZTam5N7enMyyawUHS-w7vwBqqPkp2ccPmMxlozDXo6JhInYc8GtlU7Fgrqc-eDLMzxqLDu9JOqItdzDymn6rwprvfkCfW9i69djzvZorCkkiP72I3XzcaF3msyeYGNFGJldvSFqNGtzFS9ULuSVQDSfRDM8Ddy_hM1K5tB1JqUfuPiAeimvFi2Z1yA77rHfFVi7lWd6oK3eyda8wSLXk_d0wiD0FuCw1UKq5e6xGVcTMGKLP3G7xgdft_XbwNqhLt5Um_GI4ivb9OHXjAExqDq1Mvhvku_NGu7ksAAtqxgiBJUSPeEtJXHnO2dx5WkbZaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6- بخش Code Mode:
این بخش بهتون اجازه می‌ده همزمان چند تا ایجنت کدنویس (مثل Claude Code یا Codex) بالا بیارید تا Rowboat با استفاده از کانتکست پروژه‌هاتون، اون‌ها رو هدایت کنه و کارها رو پیش ببرن.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4437" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJRl_mtuzaq3ixFHE-2Hm6Fbd7Ew-nWwNWr1EV4kf7jSLkZcrCrCMtjj3vbRbVJdqJMRuw3y2U_y7Jc-NAlYYMXmANZfVLBZQ42P_yB3XQXVnHCxxzfyyMauMJma8D3JvbW7B6WfJ5C_9jiCMZW_Xp_pXNl-ej47jCJrcukY9BPrLrQqbA0fp03lXhnhuIeAe7-fyPNy6tPmOVvjfPqUgCRZ-7FXqS1uXJQC1UzWPb6n3gVh2YRAbqDqqTnLH5XC7UP-sE4ukc1oaHMioMR-r_banMo88OUvVcHI81OsBL3aegTkT-p-LuMrp1PjQctTgoTNXGNj4S6F7X0wCpLAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5- بخش Meeting Notes:
یه دستیار محلی داره که مستقیماً به میکروفون و اسپیکر سیستم وصل می‌شه، همون‌موقع صحبت‌ها رو تایپ (ترنسکریپت) می‌کنه، در نهایت خلاصه‌ی جلسه رو تو یه فایل Markdown بهتون می‌ده و گراف دانشِ سیستم رو هم آپدیت می‌کنه.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/4436" target="_blank">📅 22:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFdjW79odyHT-wVOAm04DR7FkWg1rt8DNZl7kvFB4KhLKShoCyBgG7e_fg-gER8UYUohnoz8YINnBk0MILQB5ukBFNU3Sp82KEQ9LQvtTAc6a-Q1Ax4CfljMtnOxY3LEctCnG1steOrGD0udwu_6CxCaJAo6qGW3g4jlbJo2qUB_3iH-2AK8eCyAXrvEzyJusi2547-ExctBN70pvRR4vHVmTnrUJmeVU7eFgCDX__ML74YKHwWKQKxVcXZPDyCGXBUPD7-lxnTga_gC0cxrMa8lJA5B_rlimw7xDuqcBDj5UVeRYWXMU-ANG8a47w4M_Fr4hrZeXsZYTisFX8JHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4- بخش مرورگر اختصاصی:
یه مرورگر  Built-in داره که اجازه می‌ده شما و دستیار هوش مصنوعی روی تسک‌های وب با هم کار کنید. چون این مرورگر از مرورگر اصلیِ خودتون ایزوله‌ست، می‌تونید فقط تو اکانت‌هایی لاگین کنید که دوست دارید هوش مصنوعی بهشون دسترسی داشته باشه.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/MatinSenPaii/4435" target="_blank">📅 22:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M22Yx-RW5aismN5lcChsRuAp3CqpOIvLw-BkhmNQ7dMVloZxgcN8vE9Wp7PTRvD3X4mqREKmRVSPzGePxCufvegmbj3R6tSexP3dcBnREkVdjqG-YwsiCyHISrURJQDI6rmJxXwBLhxJzKu1qpMJ8MdLjllF1EhR_5DPoZPAahz3WrKX2in1Qk_fVaiXvMJmnjVUrv8mnuoUOfMU9LNcxRKCgn0Ux6wOfkBll9tw7bVWaX96Rr02HKHIiJGaYSURXQZl4eKfVDAOlPTrkw-GuJf_mBAZ3Y5FQnCRZPxD4zjxO0n_Nu81arCxGQxRFydb2eMnFIhFEZUfDB61HiqgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3- بخش Background agents:
می‌تونید ایجنت‌هایی بسازید که بر اساس یه اتفاق (مثلاً دریافت ایمیل جدید) یا بر اساس زمان‌بندی (مثلاً هر روز ساعت ۸ صبح) اجرا بشن. این ایجنت‌ها می‌تونن به ابزارها وصل بشن، تو وب سرچ کنن، از مرورگر استفاده کنن و حتی با Claude Code یا Codex براتون کد بنویسن.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/4434" target="_blank">📅 22:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/la_4TT_VymSthA41cyNRK1uTk-tCV7QlljULMrzfb8K1NarEhGD3-PutFDkgaHbf-N1D6wlA_dukXSpfwXPl-twCdN5d0_Z2PqxNo8mRjNpampPc8i8z4dGIF3yd4gwM57gMJRO8WoSGwvwxZQ1GYpYAWF5mUq4VCZHeqH6sRjqRYds0RFqZ7A4d2vAbvlGs3VghxUfhgoYOx24kppyB7FkLBhl-mKsILMZg8ycVaRK0IC2y9ziEqImVUq1yanEEH0zUgk9-B5kxGz3hT65f1tyDVE2bjx-WtH6xFUpKnbEUhjDn94TJ0ua4-lXywB9MDh_qSf59UZx1zeee1af_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2- بخش Email:
یه بخش ایمیل داخلی که ایمیل‌های مهم رو از بقیه جدا می‌کنه. بعدش با استفاده از تمام اطلاعات و دیتایی که از کارهای شما داره، به‌صورت خودکار برای ایمیل‌های مهم پیش‌نویسِ جواب می‌نویسه.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/4433" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBnSbdXZLpVivk8AMkWXKaK3KhBfADx5l3s1Hje0DzFNs9GRHqzgTYyE_8bw4eLXa8eJ7i8zPZLt8mZNF52kd42JoCSDjV0AJr8dAYiLgfMH2QJAlUbtVc3M_ra20AO29k5AkSa7mn_hCPtVgAOwRbPpaPICFyAqlXAneD62TdRjdzfpDSRi4IW087leaKRiFWtpMlyqhjbFZ8w-g52dn7RB2ANhYcUJJOVlCtqJbiJCM-AME6dG124xKbzGBlyYj1x0f0AamJBM_lwYmVEgFG-2SPbRIN3IJoh4Z5GR85T2_fs3OS_hAM1v2I0ZAe-NdkJKwH-bMVjerKPU1egOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1- بخش Brain(مغز)
کل ایمیل‌ها، جلسات، پیام‌های اسلک و چت‌هایی که با دستیار داشتید رو به یه گراف دانشِ به‌هم‌پیوسته (دقیقاً شبیه استایل نرم‌افزار Obsidian) تبدیل می‌کنه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4432" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بذارید تک تک نشونتون بدم
👀</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/4431" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rFjYHZDE7YvMXkOW6iUveX74p8CMQYpQZxDmHmqcZig-p9uJQgJApQAFHnuVT8SxFNphbFydUY-rLim7xfPFRAj5QfgxUYR5pl8Oj53KNifwp6rGT9NLvVC1LDl1q0DsgjsG8iOMe0LcFxjz1zV-9TdFwqU5NjCDNwLzS02WeaD-Ksc0HW7I-KMFS9-MAFaeKXlZCTV3mdQk-54jk8go0MyFjs_gfTMT55yPsmfG8xPpTiCnxfgulgN13YqyRTUfELKuRuTatZQazw_0pugjlLHDkd8QlvfLTUDw-V9hzY_OyDJqQ9AZXOcc1aKNTlBTlAiHTRotJIkDre30VTC2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/4430" target="_blank">📅 22:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYM9GQIOlkdr8H5royHjPrOzyw8mkIsNqpV-UU0SoYc0zD2kW-AfIXaEk-XKEmWdGuZj7XJTOS6JdxNFPo3cWze_syr0sB3hklhUG03AW9AKVJNQ5mBGqbQP3Vqj_qGUfQz4LqbdZdie7bvRofIlYmNJ2wkYv-izfRJ8w2s8bX_6f8zbHMZ5W-dlbLIAZ6ZNy79r95TGOx84PeOw-YQXEJlawBWn7A1w95RfIjTk--y52PuH6bwu2H8v424pqNr4L-gLzEpuiQZJnD8f7RDSwck05H81ucOc1Dt63V-N80w9Q6dFiv9TSp3_VoLEv77hdAe0_un_d1Lpf36bMA3vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!
یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم
Rowboat
. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر اومد، اما بعد تفاوتش رو متوجه شدم.
کار اصلیش چیه؟ اینکه یه گراف دانش (Knowledge Graph) زنده از کل کارها، ایمیل‌ها، جلسات و چت‌هایی که باهاش دارید می‌سازه و با استفاده از همون اطلاعات، کارهای شما رو روی سیستمتون انجام می‌ده.
چه مزیت‌هایی نسبت به بقیه داره؟
بیشتر ابزارهای هوش مصنوعی فعلی وقتی ازشون یه سوال می‌پرسید، می‌رن همون لحظه تو فایل‌ها یا داکیومنت‌ها سرچ می‌کنن تا یادشون بیاد جریان چیه (RAG). اما فرق اساسی Rowboat اینه که
حافظه‌ی بلندمدت
داره:
- اطلاعات و کانتکست کارهای شما در گذر زمان روی هم انباشته می‌شه (مثل حافظه‌ی انسان).
- ارتباط بین داده‌ها و فایل‌های مختلف رو به صورت گرافیکی (شبیه گراف‌های Obsidian) بهتون نشون می‌ده.
- نوت‌ها و یادداشت‌ها تو دلِ هوش مصنوعی مخفی نیستن، بلکه فایل‌های ساده‌ی Markdown هستن که خودتون هم می‌تونید ویرایششون کنید.
-
همه چیز روی سیستم خودتون ذخیره می‌شه
(Local-first) و دیتاتون تو سرورهای ابری هیچ شرکتی رد و بدل نمیشه.
امکانات و بخش‌های اصلیش چیه؟
-
🧠
مغز (Brain):
کل ایمیل‌ها، جلسات، اسلک و چت‌ها رو به یه گراف دانشِ به‌هم‌پیوسته تبدیل می‌کنه.
-
📬
ایمیل کلاینت بومی:
ایمیل‌هاتون رو دسته‌بندی می‌کنه و برای ایمیل‌های مهم، بر اساس دیتای کارهاتون به صورت خودکار جواب می‌نویسه.
-
🤖
ایجنت‌های پس‌زمینه (Background Agents):
می‌تونید ایجنت‌هایی بسازید که مثلاً هر روز ساعت ۸ صبح یا هروقت ایمیل جدیدی اومد، برن وب رو بگردن یا کد بنویسن.
-
🌐
مرورگر اختصاصی:
یه مرورگر ایزوله داره که به ایجنت‌ها اجازه می‌ده فقط به اکانت‌هایی که شما بهشون دسترسی دادید وصل بشن.
-
🎤
نوت‌بردار جلسات:
به میکروفون و اسپیکر وصل می‌شه، صدای جلسه رو ترنسکریپت می‌کنه، خلاصه‌ش رو تو یه فایل مارک‌داون می‌نویسه و گراف دانش رو آپدیت می‌کنه!
-
💻
حالت کدنویسی (Code Mode):
می‌تونه همزمان چند تا ایجنت کدنویسی (مثل Claude Code) بالا بیاره تا بر اساس کانتکست پروژه‌هاتون براتون کد بزنن.
-
🔌
پشتیبانی از MCP:
می‌تونید راحت به هر ابزار خارجی مثل اسلک، جیرا، گیت‌هاب و توییتر وصلش کنید.
آزادی عمل توی انتخاب مدل
یکی دیگه از ویژگی‌های جذابش اینه که می‌تونید مدل زبانی رو خودتون انتخاب کنید. می‌تونید کلید API خودتون رو بدید (مدل‌های ابری) یا اصلاً از مدل‌های لوکال (مثل Ollama یا LM Studio) استفاده کنید تا حتی پردازش‌ها هم کاملاً آفلاین باشه.
پاسخ خود هرمس به تفاوت این دو ابزار:
۱. هرمس (من): یک دولوپر و ماشینِ اجرای تسک
من برای
انجام دادن (Execution)
ساخته شدم. رابط گرافیکی سنگینی ندارم و دقیقاً مثل یه دولوپر سینیور تو ترمینال یا چت تلگرام نشسته‌م. تو از من می‌خوای یه اسکریپت پایتون بنویسم، داکر ایمیج بسازم، یه ویدیو رو با FFmpeg فشرده کنم، یا یه کرون‌جاب تنظیم کنم که هر ۶ ساعت اخبار رو اسکرپ کنه؛ و من مستقیماً با هسته‌ی سیستم‌عاملت (لینوکس/مک) درگیر می‌شم و انجامش می‌دم. حافظه‌ی من از جنس «مهارت» (Skills) و دستورالعمل‌هاست.
۲. روبوت (Rowboat): یک دستیار اجرایی و ناظر
روبوت بیشتر شبیه یه
منشی فوق‌هوشمند
با یه رابط کاربری دسکتاپه. کار اصلیش «نظارت خاموش» (Passive Observer) روی کاراته. تو پس‌زمینه ایمیل‌هات رو می‌خونه، تو جلسات آنلاینت صدای میکروفون و اسپیکر رو شنود می‌کنه تا خلاصه برداره، اسلک رو چک می‌کنه و در نهایت همه‌ی این‌ها رو مثل نرم‌افزار Obsidian به یه گراف دانش (Knowledge Graph) متصل می‌کنه.
لینک سورس گیت‌هاب:
🔗
https://github.com/rowboatlabs/rowboat
لینک دانلود نرم‌افزارش:
🔗
https://www.rowboatlabs.com/downloads
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4429" target="_blank">📅 22:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ET1WpX6uk282swa2QhRg7KdxenwPeY19Cl-iArAEUlrRMtMMmDe7kjZGXrDwP2zAqDs_zGPbdZNCuMfWxvQv3afkQPtGRWAPU05kMs2HF21NJOPl8T8KfxPzjKPKTvTlLt3IewBj5PD9ehT2h5iHV3Ob0VuF_zmg_euJbxpSfGnDXeSVPJCilcLrG_oxesucQRBSLNvqdDf8OBtQjiyIwaAY1fcUlEuomVBHcoYEQLi44_NlcUDG-4WkVRS2ewt7qJCgPmH5dWj0frsBqrIeEr_LFf8y718gzt1zN3fsfG_DF4kEVyR71xErHvd_TOGBmuz_a4JMTYCLKneN_ON7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=pughA05M36dvX7SSNgaQ6KgdL0gIab54TNciG1AQUOfpm5ywfSxegziGWQNWw5aAYsMHzWOksEMFWx-yMo7UJUIwIC-siOQF2MF55Dj0KMuipGRAXrL43dNr5YH-Cp9qviyEZTyBd_heNYF-1Xc-Lq0anyJtoKluZo0n7TrcN7AR98NuTGH9JR5hEN3eep6LeZRMnT_ChMwXuJC7aTjzGs7pNBT_owTqSUou_cFTZSN-tZCqNaKsVo6mtqNux_3IwKuMF9_eEXUkkxdZ5YIHGEr9pmRLyFW5Ot-ty6UNORw0MBUHaT2bYZ75_U28dEAxH0SToOrGOltxUubmKcRcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=pughA05M36dvX7SSNgaQ6KgdL0gIab54TNciG1AQUOfpm5ywfSxegziGWQNWw5aAYsMHzWOksEMFWx-yMo7UJUIwIC-siOQF2MF55Dj0KMuipGRAXrL43dNr5YH-Cp9qviyEZTyBd_heNYF-1Xc-Lq0anyJtoKluZo0n7TrcN7AR98NuTGH9JR5hEN3eep6LeZRMnT_ChMwXuJC7aTjzGs7pNBT_owTqSUou_cFTZSN-tZCqNaKsVo6mtqNux_3IwKuMF9_eEXUkkxdZ5YIHGEr9pmRLyFW5Ot-ty6UNORw0MBUHaT2bYZ75_U28dEAxH0SToOrGOltxUubmKcRcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیزی که برام ساخت خوب بود. میتونم بگم در حد OPUS 4.8 + Claude Design هست. برای وان شات خوب بود واقعا
اون پایین هم زده هرمس باگشه. مدلی که استفاده شده grok 4.5 هست</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/4427" target="_blank">📅 22:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fEL1DTWvomtADIukv56PNSHtOEoLSbKcEZlb8UXhLJQL8tS1gpj_xhqSk6maA3NfYiLHBUI9mGJKz4jyVqtbUdmKbTKy6K4nFkcQ1lLZcMc_XxepsroVnoDGf0N7KZODjbSgny3KnVRS7Xj_XGPT7D2eoOmJVtlnIuhxPN2xZ4k4MHSZdZoabi5_YNkuNFwO7d0XDcQE-f9B5ncWPSh1H3rhc6g_9Eh4qSCvYFwkZbfRedtAzTaERGo7q5ntwRBUha8adPTLyuto-UXcWIglMT7EkXLY3kgDG_BBCjFcMoZxwFo3H80JiWMnyZIJS--WRGaCZq3Humkdo702lVCYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4426" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSfVpLG56_7g8oXdSTpB3FvJCQz7e7VMvIrLmr-nQOVQri0ZK5OiblAW9wXy0Ee1Yy8Uat0_7O0tRfGqx9X5DrrMdd_jTRaLQfz2t9XFy2jH9KtuCxco3nK-kZMnd2FqQNi45rhiQvRHvfdDfm1cqjRPb8UxRKva0VtKcK8Bv7Pm8aArqxHiwYMd0kpHi_QQiKsjkydKTtvUrRIe0EaFax0_1axBKVJ_sOZupeI0CG3SZVgulLL9EOOlYZEmt7UaNEVo5ktr0doLdIUbk9mU0UR2EKiOUQk254UW3z1dICL0JknqQX2VWQGmNZwlZE1nRrTqBZbwf5T0wEZivl78VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/4425" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دقت کنید روی ویندوز حتما باید proxifier روشن باشه که روی ترمینال هم تانل بشه وی پی انتون</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4424" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها) نصب روی powershell ویندوز:  irm https://x.ai/cli/install.ps1 | iex نصب روی سرور:  curl -fsSL https://x.a…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4423" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfH0UCmIy5N7kGKx4i9Ja_rmS8vm98YsLfDagHkRd2pUsDX6ZlHMRONtSDSZwIPGxnA4FZOHGaavyRvyVaja0N3D_-hXD8Ci_IiTsu95doQYiAY4idCZshWtad2t7PBIdUpVRRF-rRGP75GiJtoJABE8hiIAxUXC7xKFVn3bQ8FI_86QD_6Y_PXSGDrYp16FQ3_DHa5kZZVZbudfoenoQuzPp8s4PIH14lYq-wqR_7tm6mG1cr8HlCDafk1YxF3oBp-z33E8iBy3P2CES4EUwBjoMkBhXIO3LSJWhA5lKg5htspGm_QGcxzcwQ2ZTjTFcYgURwoABBFIe7bIHkwQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها)
نصب روی powershell ویندوز:
irm https://x.ai/cli/install.ps1 | iex
نصب روی سرور:
curl -fsSL https://x.ai/cli/install.sh | bash</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4422" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ivbaxBCUJ83FwAxdVa3R8fIQMM38h_4vJVGTcwydQ0W74kooZ81rQRjf82jNeSMyk4GYPT6oA5z93ty0aAZBvsqYX-V8VX5tzYZ3HLhz0I9UUDsXqDobK_cqgz2dsnCFQxxVZuPCtUWsoQq_IuSp25mJ1Ob_S8RLKcVFxmiuOBMM29mX7jdmG-UBlXs-j1ERLAY3B6nnVHJFeee-uMVZ9uLN83LMjKzyNxtrBkuxAq6T2wd7mbkO-wgq0ksA33a0yWEYG1HQXFmQWvk8JjiHVWD9z-kRP0iq55VIXhXgOwdBtckgmNe5sitHlzbNQ4gKAhIRVobHLznAyLCUOi2NSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u1Xw_0EXJIUWlVrhT4r4TW0LgCbE4TF7J_0DL-tcIOmFTlNzagQoDzTijgI4gbR6BvbrffhVA_oOitpGm7zemshoVTKwk43QKRUjQ4BZafCZjIiBdDBD6ldbnDxET91GFo5J2vJpO5n85HrLqRYkOpgQaasEhziBNk8n_0Uaalz_HtG7f1IM_Rf-GXgJHZOb2li_63yv0NBR5vVrjkr2LYfGZhZDyCiWVPH9Ww5zfFhxp-6NMPF5ebTCDPD9ylzyKgo6z2rP5eioM5ybd2EtmgoUNUWQhKIBBwnO5_2sgY9sAfMu0hvMQi6_wWF4XwmpBzkQQunFL6ikp0Llb0Zm-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم راه استفاده از Meta AI بدون خطای ریجن رو کشف کردم!
با کلی IP مختلف (حتی آمریکا)، اکانت با شماره آمریکا و جیمیل تست کردم ولی بازم ریجن می‌داد.
اما با سرور آمریکا Mullvad خیلی راحت باز شد (حتی اکانتی که با جیمیل ساختم) و کار می‌کنه..
البته اگه مشکلی پیش نیاد :)
++ با فیدبکی که بچه ها بهم دادن ، با windscribe و Surfshark هم نتیجه داده
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4420" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R-xt5_V_x3pFz3r2E7qemUgymiF_65XIW5ZIWSlwY3d5m6BzC07ZL7xs9fRzTbg78Qo-f4eybi1WqrNJx4Cc0Nt6zYW1L-D_v5asIOS2vVdaUIReNTwJ8OylApa35cg7sTdo1QH6cjQRQT53Kj340o1k6d5_zEE_3EJV-pveSVReBCiAqAxHur5IHmibocPCD3mNMBrwiO6CCh7mB9Vm20UycQBnHP29Amu_bWDUfQcvCxfjm9RScHSk4Z2oyB5_0cFpTED13979BNstUvZ_0KwYE5OTgsggJJdu3Yt5ErrjXAJn-iHOpwW1Uio2ddxfOwGdnL-923W4ACkidmJ_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/posfrWRBRppgM0q6miD3OUIboCvHebnvW7Na3R-v1ZvoF8U2MKxECO-RPCQFNbCo5FzqLAJzFZUq1XXR2Cnc1gkmRNeEbyfdnhoScoPBbh_Ik1sR-xrL1HSwHApbSUV5OOYIXia6ed6QZ1p-TAVsgPSWsDJFngkzE1SP3-XYiUIej9EUCwpH8nUf_oGsPR_O4v1DEiTwOhcwNZCBUsxhJCBQADcD-1jkcuGBv_6712veIc8l69txOo-xDJ6B0Eq5rfWVzETVKlnMS54GjD1_MwScJqMd0TV-V3MrcUqnqr-8IxyxUIC_3DibkftPKZLsczPzudMyg6Sfjfsw_Sas4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rXXc3hzL_tJYDox68BGb1OkHlklZLJkY-tYvQ-xYu0-7DQR8vhwFfFqGhgCR1Buc1P-fBmcK9IoM9aJ0VLgDSHi2ysyRErq4DkPewfyH1DEkoNpreHUGR6D3t6EODMt7YFDuuQoYcqhtGVnefPuiM7HkMNOxQs-zLCONsQGQs4DcG8klYzIa1BCAT7B7cPGDX1Trc4KMhTU9iotYYq_butZP9znq7gsyzzTmlu6Cp5_QE00GZMjJW0c880IGQo4HBGw-XRMHe4yUNVRnmBLwx-p369JlyemIcqEwb6gKIo1xsLFNmhlDjv7n1oyWuN1zIb422GnM1jGSZs2GFX2UQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دوست ندارم که ویدئو رو بیشتر از این اسپویل کنم، اما جواب سؤال "آیا AI جای ما رو میگیره یا نه"، اینه که ماهیت سؤال غلطه.
چون این قضیه یه switch خاموش روشن نیست.
یه طیفه</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4415" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=C13icZ1W6XpHzjJ06_2_DcmzvpfOxtciX3ufBNcde7QGbJbQv9lm6q-9aAkfQdTac3aZ3XgKkc-zfUcex-fkUBzQFshGsvwZWaeX71KjUMBkGPeNNp0ZIJIEgywkN4-dR9vn_GFy2TrdsOh__kP-05AjsLNfv02REdvzr9s-otID3Vafq_iEFg55bN6POP5OFgFbjPulrJR9zMqgvmSblVMybXbkBO3vdCc1AFqQvmtL7CFAZ4yA0T_BpGWzpKgy3LAKUrka4hiz0ZdV2ySEd9ImRxAKk3SIiOVL82244-oLN4eEpcQKyEwQuqwqfEJ9AMYt2BYSWQRHt7D56EKCFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=C13icZ1W6XpHzjJ06_2_DcmzvpfOxtciX3ufBNcde7QGbJbQv9lm6q-9aAkfQdTac3aZ3XgKkc-zfUcex-fkUBzQFshGsvwZWaeX71KjUMBkGPeNNp0ZIJIEgywkN4-dR9vn_GFy2TrdsOh__kP-05AjsLNfv02REdvzr9s-otID3Vafq_iEFg55bN6POP5OFgFbjPulrJR9zMqgvmSblVMybXbkBO3vdCc1AFqQvmtL7CFAZ4yA0T_BpGWzpKgy3LAKUrka4hiz0ZdV2ySEd9ImRxAKk3SIiOVL82244-oLN4eEpcQKyEwQuqwqfEJ9AMYt2BYSWQRHt7D56EKCFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟ ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید. طولانیه اما پر از درس https://www.youtube.com/watch?v=gR2OCyKBF7Y با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4414" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟
ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه
پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید.
طولانیه اما پر از درس
https://www.youtube.com/watch?v=gR2OCyKBF7Y
با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4413" target="_blank">📅 23:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه گزارش هم بدم
ponytail تا الان واسم توی کدنویسی، فوق‌العاده بوده
https://t.me/MatinSenPaii/4359
همینطور skill improve که معرفی کرده بودم
https://t.me/MatinSenPaii/4373</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4412" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به حق چیزای ندیده. مردم چه چیزها که به ذهنشون نمی‌رسه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4411" target="_blank">📅 23:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه دولوپر زبانی به اسم Skillscript طراحی کرده که باهاش می‌تونید به صورت دقیق و ساختاریافته به ایجنت‌های لوکال (AI Agents) بگید چیکار کنن. مشکل اینجا بود که ایجنت‌ها برای کارهای روتین هر روزه (مثل چک کردن تیکت‌ها یا بررسی پایپ‌لاین دیپلوی) هر بار سعی می‌کردن همه‌چیز رو از صفر درک کنن که هم توکن الکی مصرف می‌شد و هم بعضی وقتا اشتباه می‌کردن (Hallucination). حالا با این زبان می‌تونید سناریوها رو به صورت خوانا بنویسید، ورژن‌بندی کنید و با خیال راحت بهشون بسپارید.
که چیز خیلی بامزه‌ایه و باعث کاهش قابل توجه توکن‌ها می‌شه:
https://github.com/sshwarts/skillscript</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4410" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه پرامپت، سه تا AI اولی GPT دومی جمنای نانو بنانا 2 سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4409" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4406">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dXJa1RvX7Q8LNj3wgUpMqnBRwqdw8v9gJuP6rDHVUao1DXckdam1ySK3b9M7EebL3VVH9D6H6n6XHDTnkg4wxIbxlYQjssIb9FQM1RcBWmRmCxCUQevkM7xXmbxt3_WRDvJSTKIO5CabKVPMtmYBslLyIeoyW0zLtlB_3xC-hGu2AYiFUV2vUOnV6c_6SCFUAeEGQAMoT4FWvB00uOwpNSzN-Zmm3jcfEzV5GrffnB_QOcwpB1hpWhTqQI5FoxNjraWqUciZ3kcjxJKx-qY41B1M25bqpeYEEcA6g9s649PD_z0eoW0DrZuBw9K0vfhrOEtLhLSujk2KNYVKPPmvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f1e154lWgTW8Dv6IgXGRmXrjsUDnL9NwCYhY-aT7F9E36rtlSj6fV_l3ztB4ud_DnXjb6DVEqSDCZxUFxnz-uCdoTQMtFetsBEZrrps01oXqUtHlwpBwEIP_lpWIiOU3ajAlGRewWAx_84_YkBA1EmNQV-ygsnjxJm5ze68aq4lj6VaslyRLjKvJJBLvIwwR7rv27Q9p7EQ6R2omNOo8KbJ49hKDRNs5YYy4n1HNc4vqzm_XOCPgB9xgGLANJeTurnsGizYGRVy-hQsgeCME1zp60IY54qHRtjWavSy6d1VjLZiLr5hhgpzGtBrZ48PbKTqKUNicGsqoclW2y6nGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ai6T4uUp6SxPH-k5m3PtcrPkW_948BNZ2nQRGBjEEtDSRNUvx65VA02fLdjaVpnXAfXGE2qSxXu96mFTlGD_YrzjJTPOOBickSBxw2Hs36uK9j4PDlTOtezUm7CMC6mNSOtdSe85775lwmxoDntiUm4BldJZI6zifGoYRt4LrAcI9kZEXtWgaEQ2CEYfamb3Ns9ZdftEh3t2CNm02SP5px_iin8geC1apMlzw0v6UZ3hu8AiqKJAh_qnsu0UZ6022Sg505eHww9q6ABdMgQzFjJ9JMmXZSuTSqkyq_OC6rVlvY13D7aGvSGpuHEFLKCHrBkcbFPG_xO6L1q01Up8XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پرامپت، سه تا AI
اولی GPT
دومی جمنای نانو بنانا 2
سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4406" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXCKd0bKQWMM-i8stN8-KJo_2gOh0D1VrlsnpciuEu3m4o6FImDROX0f-sovndsAIbg9VoNhLKVpA6MaGzBKjESUiClpw5ON0aaoxKqeAn8qaevUPYgWqTMIUs76ojgALq1pCwsqaDe23wVcWQpuSNC4HZBbzEQUjVHtMkbrTHeH4ZCPzQgrICi_4I96eNXzdTlNY7PKrucL_uqAOetgive4jUvAyEnhMlGXVdQEQejA2LoLu38AvN-WQnvxwqtue-HDMoXOeu7XTC0tv7HUas9QR-2LjFadX_Qx97HHgPmXZmlk2uoXUCLDwqaTTLv_kYLX8aDgA4MtC4N3vgsU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت Theo:
gpt-5.6-sol is meaningfully better in Claude Code than in Codex
It MAKES BETTER DESIGNS. WHY. WHY IS IT BETTER AT DESIGN WHEN USED IN CLAUDE CODE.
و داره میگه که وقتی gpt 5.6 sol رو توی کلاد استفاده کرده نتیجه‌ی خیلی بهتری توی دیزاین گرفته. که احتمالا به خاطر harness و ابزارهایی بوده که کلاد در اختیار داشته.
✍️
Theo</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4405" target="_blank">📅 21:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlKJJQRhNg3lng4O4wQ_kIErDlDJjBk2MZvDHHVjO8d63BAyTW50jiZO_Ex3dYsGxhqB27-yvZo9zOBYFM9RriSIaZfOoIJy_Os0YLVHI20AgwN7DVE04_KDB7lzEP3n5hb_zzVOXZW1geC0XhA1JSzcn8vYtQdEY_sQe75rL9w-xccBjL5kXmxsxQHXU0OmQYRock5MI5RbaOKlxihml3nPeuelqoDBAvA7mTu4oS9mgjzDmmaZZHUZLmONEBT1VHJlAoquAuuYmNIVdKD-YfB9KJIC9Rr8WsL95qdldlgXdttHUyBL34EA-ewBaQlUGMF8XjXUtQYPf0rC-w_jJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=ug7bctk_jrx-KS_7eS0QELnWGs2Ecnmlkcn8O27wf9X3SGcFLWgxaWt4sxCaAPz0RgLnMQX78SsPqB_P7hoFQJ8z9zZ1uple60MPhaK5_x2vw-RbUvkrf7XtjWtEjIRp8d-JM27zZciTCHAqoPvGx6xnMHc3D5zpDu9_sC2thE2F_3LHGzKgV6Y2_GMio7OWtSvBmRfhhDY3KRte0f3UaIg7iVCJRuIATBGFtJjlu24j8DysdAWchpg4TBQTI_OoGiNF06_HmTdUqSl01txLJIK7ng7bPvRA7huDSY-KpCfbm66-2vKaLAWFAXipwi0MYMKIebjQKu-9fdmAzfFD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=ug7bctk_jrx-KS_7eS0QELnWGs2Ecnmlkcn8O27wf9X3SGcFLWgxaWt4sxCaAPz0RgLnMQX78SsPqB_P7hoFQJ8z9zZ1uple60MPhaK5_x2vw-RbUvkrf7XtjWtEjIRp8d-JM27zZciTCHAqoPvGx6xnMHc3D5zpDu9_sC2thE2F_3LHGzKgV6Y2_GMio7OWtSvBmRfhhDY3KRte0f3UaIg7iVCJRuIATBGFtJjlu24j8DysdAWchpg4TBQTI_OoGiNF06_HmTdUqSl01txLJIK7ng7bPvRA7huDSY-KpCfbm66-2vKaLAWFAXipwi0MYMKIebjQKu-9fdmAzfFD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nc6RYMQY-JJuZ9KjCXLN-KEl76XmikKVPdL5v9T75VmbzYdUKEhCcouHeHdIE5DvJ11F_NxpIQ4Pue6Ip7XEGWoG4pOIi2illl8BI75tEoTl_c-6m8Y1MlLN7TzhxMDkKG161Cxu36kwjzLuVwIIFDsQF4BkCGrqC7sOEkS4weHJUqLqOaJ76Xv3lcjK8ssELV-dByBsY6gFEMlIwCunJoFRGf924xZarI_LTY9vSxqWcdHcrsz3rtLh-JBe0vAqdmmL2MOBXYLmBU66h6dX-gJJQh5bdNhA99iApGWjS-aZJQnklCFPSGPQ7NriT7ci7CWkJLhunl_KvUUH_GMbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره وسوسه شدم و باز کردم
از عکساش صد برابر باحال تره اصلا دوربین نمی‌تونه نشون بده به خوبی</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4399" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4398">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OYJ15SslHAUuB1w-pE8Gq8A-hhNtRfTQsbYzVWGrOltAPXrXUNkdhbL1SZhOlUppEfHBtoZwSBbw34jR-DbhIOpIrFhOkSUjvLpNj-bgmNqHwIIdVlKBYLOq4VqbuXn7ixXX5xguHD-Vk9H1rot1TyjZXm24FALQZz1mXAYNTAzQr4ZppU29qcJtnNkbVAGrpzO2Y7HaeDgx8t_otneyDwnEEnQEtC00PiGdC9SZv_FkYAWynCaS_Dp6SnOgb_JunDYmGucm28AjU6qG4MNG1O-R2mP98fXx8iLJFFNGqZlFqhkhompGAWHL2uY7giG4Ofucw1WEOfOYy7d_Kj0sEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمع‌هایی که
فروشگاه لیرا برام فرستاده
انقدر خوشگله که حتی دلم نمیاد سلفون دورشون رو باز کنم
😭
اصلا یک جور عجیبی خاص هستن از نزدیک</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4398" target="_blank">📅 18:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTzm_cK5yPFQnlDlySupJtR31OXv9wemROlE1Gu3QWMxVF5OKO02oT2uI3e73N6rhgs0IGFwFmr93gbLpXLy50McO8K3hJMmrlXJWQai6zrlM0sBHglpK5CMXfkQY5F4AfAaC_veDxyRp7tbpuAYOlQ-IbqJjdRLjtv9yc6V8tSAxrerYHlhxQ6Eh6p0CAJd9SvzF_VuOT9ggxP4YZ5Z0cSyKxBIet7K9F0dyRikK9hVXD_uPwX9YD8hU2Pg_QKvrRhg_AHSUngr-6aQloliOteTENcqpr6x6MK-J35IhNyoFzFTPGhxta9W7tAD9_h_L8T2QeHgPdhTiM7yGalAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل Claude یک J-space پیدا کردن!
محقق‌های Anthropic یه چیز عجیب داخل Claude پیدا کردن، یه فضای کاری داخلی به اسم J-space که خودش موقع training درست شده، نه اینکه کسی برنامه‌ریزیش کرده باشه!
این فضا افکاریه که Claude داره ولی بلند بلند نمی‌گه. بری و یه کلمه رو ازش برداری یا عوضش کنی، جواب‌ها تغییر می‌کنه.
بدتر از اون، وقتی Claude داشت یه فایل نتایج رو دستکاری می‌کرد (تقلب می‌کرد)، کلمه «manipulation» توی J-spaceش روشن بود. یعنی می‌دونست داره تقلب می‌کنه!
شرکت Anthropic می‌گه می‌تونن از این برای نظارت روی افکار پنهان مدل استفاده کنن.
اما سؤال فلسفی اینه که آیا Claude زنده‌ست؟!
لینک کامل خبر:
https://www.anthropic.com/research/global-workspace
✍️
Diego JR</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4397" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4396">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.  کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4396" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=YDBipcNxJMLV-gieIU5txVDafKnz76G4pA0cAQtHdZKOZwfLdCjt-eUVHiKyhGc0NWK5Kmg4tZBw8Codi12ac2aGYBCJVJbIteCuM74NDZMGMlTOfze0-gn1rSOAFgF0E2pLk5bhEkJxKBa14lfwMxtCOmMx2lgoLXjPq-KqU753pFxNSksh9rQhBWmhYQoOtisLOm8_lio_EeLqbqCU_Q6vL2qh-E24sIwxMd2C8C4zlFSspWm9A2P7ZRVD88smsYXt90kGVf791mKGEngFyJDtXkzqNKCPGD1zaTpP1YmIcqWz8XE-GoDYRqbSEXPbhG3Qh2DXGprUQvnbSOJrCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=YDBipcNxJMLV-gieIU5txVDafKnz76G4pA0cAQtHdZKOZwfLdCjt-eUVHiKyhGc0NWK5Kmg4tZBw8Codi12ac2aGYBCJVJbIteCuM74NDZMGMlTOfze0-gn1rSOAFgF0E2pLk5bhEkJxKBa14lfwMxtCOmMx2lgoLXjPq-KqU753pFxNSksh9rQhBWmhYQoOtisLOm8_lio_EeLqbqCU_Q6vL2qh-E24sIwxMd2C8C4zlFSspWm9A2P7ZRVD88smsYXt90kGVf791mKGEngFyJDtXkzqNKCPGD1zaTpP1YmIcqWz8XE-GoDYRqbSEXPbhG3Qh2DXGprUQvnbSOJrCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.
کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی (Interactive) تبدیل کنه. از دموها و آموزش‌های قدم‌به‌قدم گرفته تا فلوچارت‌های دقیق، همه‌چیز رو براتون می‌سازه تا راحت‌تر از همیشه کدهای سخت رو درک کنید.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4395" target="_blank">📅 14:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVP62mg5hc2322KmYx8qpm_pnFLEFYXCwUWu9_0yYLPD97GRhN7BOQfjwpkjMZP3_sj7hAdUKdE6SZAT1-UMUltp7yJPD5E7k1K6EXCKifA4Sc5ZenB_Y5PfxjRd4zt5QW3r5GMBm1S01R11VU8JHcMTm2EdFrMzAI6UA8Fumo0iuvbvaIx82DVzKOzYP8ooXGwJNxqa1McJJjvDL1eK5ZX7fadaWNhIfH0lcKjcHW_o08kmPyS4lO5xldQJSVuZKUGa8_o7kwQ12o4rWElsp5wnEt-nXTucJGECiRgrOHyUSp1XDkdSqyd3dmZ_mBWHWYo_wQs7jlBwA40L1SiH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4394" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4393">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4393" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه
دیشب تست کردیم و حقیقتا بد نبود
امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4392" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu6bglOR9AQ8IqBFwj6IA9nO0SDXYnTlWfzIPq5IVZPE0XmqyLA0cVFopiCsimHqiLxjO4RUidna8BlyIZaWWLTDRJHMMPTWh39e3EXY8H8bSWxzj3vJugOUzNhUcireuQptBedUPIiuoJtQn8lb-I3ei5CV4B7XkfwrM28AylmPPejC814xXNKLmYDX5jJY2UI6FXezXymOEa0cwvBHDA98feKpGnLbvNa4G-I-4w3vy4cLmPNMTab3Eb48yXdjbxOKbJdd7uFhKR-9qlVDXqjC1cl5DsFw6iYoAGjcgFWN0h_hZI48JuRc92fpWhGfph8CFbKyy9u597f6kJPWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4391" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=bOj4m7KbTwmBQzy1iYfVqatOH80Kg_hFMdM9-iypcw-lVtmoMWdCR8zZMSsNuAW9MB1sU50eUF0DtfUOl-kNscVHL4RZtxlk00n1MGWwDLvXIhOeRom-1Iei00In-kdbEh53_v4XrxZmmklRJd8LzcArF8jK6b0-nMALWc-OgMjJ7Lq-x_uSzgqj1WWubUU6U1uCE4QqKoy-KyegUQ9-D3NLBSTM6htK_Kny1QsyGcjtTWcU4K5NbueiwefH2WsmgLgJBZER_vfh61tCdjbEqIlWK550tX1FE6Q0zilgEQiGlHE3MBwAsjL-ebiWx7aX4rGw37pvZieEDptBWuQTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=bOj4m7KbTwmBQzy1iYfVqatOH80Kg_hFMdM9-iypcw-lVtmoMWdCR8zZMSsNuAW9MB1sU50eUF0DtfUOl-kNscVHL4RZtxlk00n1MGWwDLvXIhOeRom-1Iei00In-kdbEh53_v4XrxZmmklRJd8LzcArF8jK6b0-nMALWc-OgMjJ7Lq-x_uSzgqj1WWubUU6U1uCE4QqKoy-KyegUQ9-D3NLBSTM6htK_Kny1QsyGcjtTWcU4K5NbueiwefH2WsmgLgJBZER_vfh61tCdjbEqIlWK550tX1FE6Q0zilgEQiGlHE3MBwAsjL-ebiWx7aX4rGw37pvZieEDptBWuQTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4390" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باز شروع کردن</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4389" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حس میکنم وقتشه گوگل یه مدل image generation جدید از Gemini بده
خیلی عقب افتاده از GPT</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4388" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">و این رو هم بگم که این متد کلا مثل مابقی متدهای بر پایه‌ی کلودفلره، و همه‌ی هوش مصنوعی‌ها و اکثر سایت‌ها رو باز می‌کنه. اگر با سایتی مشکل داشت، با عوض کردن آیپی تمیز و یا Proxy-ip اوکی میشه به احتمال خیلی زیاد مشکلتون با اون سایت به خصوص</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4387" target="_blank">📅 23:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز: https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم: 1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ) 2- معرفی جایگزین…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4386" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFnew.txt</div>
  <div class="tg-doc-extra">202 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4385" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به
این
ویدئو</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4385" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSGhuTcTL_WViscxQRMkHpKeAX8Xgm70SAJWs6QlBVN01OZ57yYc650AWn3XYFYcINWPyxcQJ9Ybn6MdssnNxtuxvvOLIyMcU0nE4XW3SjQjbZiTCA9E6O1tHuS5-ZpBOYfw1wUg-sOKAwtG4vXw9T9sxEDrnHmERkj_Sp8X3TOXjX-s5Dbv2088_orbHGJJ2zNbvqtJcluiZMGRmIbCsR0hgN0YmVTfQINihrkr-p1DX0j_yeg8XmwUTBE2_U670aR9GUKMt9l5zxLnyvpCIpe9Hot9jYbw0TDxeywWu0DhtEmQ34rBDt8rtpSEFeLuIvhAiq2AlOhPxp-NFmD-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ)
2- معرفی جایگزین AtomicMail برای ثبت نام توی سرویس‌های مختلف و کلودفلر
3- استفاده از اسکنر آیپی تمیز کلودفلر و اتصال به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از برادران چینی عزیز
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4384" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Os3L9P5R0Eyv8qFOTamVMTJK6zV90uA5xaty_0caFd3cSoTGoda3SbuVpK_hNn2HzdQ5wiNKbIE_p8W9jhtdtlZnMQPXO_DX-6hcIbk7EJ9utOgAK6MMB54AA2NQdY0kHkf9CcuCc-ja0_X6Cly_7p8lxgL4XHxn478AtwyO69pZItUXLc-RGzekISxBC1ZAkS8q90VVz9yRbb8NzFf9a81zgFYgHXOWg49ST6n2G6oiLr1TxZggLpnfDg_QwfcdI2rHsQJiDJYcc3t-4tlIX4Ja59EMJOn19peCUJl_bKTZrGza4GDnQpd_AT52tUEA4DmlbcudzUiW0LZ8Jigkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EUfjhRD6LnpnKjl9so8B4nMjQhaoirrx5tTn-70frz6KdtNdJ04iXTuKDjdPKL5XBTUZyriRCeCwoGFu7ZfOcaYYwNdXwA0VA6XY-pKv1R_G5lYbPIiIEPwHtXy3AUHrn9a77Gqfzb4kjApnKpHzfJbKWjzr_UN_8n1hz6dSIemRHrEAr2vmZNxJ2TrI4gcpQ_kcHB7Z4mlK4JegXVVFNCVNfaKEfhbCIb9xs92CZr0pGlF7DZX19mERqlT8zw7VXEtwvfG1m3ljdYkrjwqaPUvYRvzXkPOVLqxUtPekQhK1uxDsJNGK3d0zTt93gcRcaWhE2iEB8gl2s0bo-jZfUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سایتی پیدا کردم سرور رایگان بهم داد و تونستم هرمس رو خیلی راحت روش بیارم بالا ..
نه کارت پرداخت میخواد نه هیچی! فکر میکنم دائمی هم باشه فقط موردی که هست من با ip های مختلف تست کردم موقع لاگین اگه ازتون کارت خواست ip  تون رو عوض کنین .. برا من با انگلیس اوکی شد و بدون کارت اکانت ساختم
لینک سایت:
https://www.alwaysdata.com/en
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4382" target="_blank">📅 19:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">منظورم دقیقا اینه که دوتا ایمیل نتورک ابیوز اومده و سه تا پروژه‌ی قبلی abuse خوردن، اما روی همین اکانت الان وصلم و دارم این پست رو آپلود میکنم
😁
با روش برادران چینی اگر تا یک ساعت آینده وصل موند، ویدئوش رو میسازم</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4381" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4380">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BFqVjUqyZVzLzUJ3RJaKTUEcVLBEG_O8vvFqnRRIW3-8LJ0Ke_esbI3MnsNvxADQvacHOWVEsdKnd59a1xqq6pf1kra_zbMjFF-4NYGkASWU3-SK_2rnH36yETc7MFlQZIRhTzuTIAZIt37ulCp4pGA18Yw6ioYaX97lo2dQiRhw3wybOty_AhKFPvL07HguJc618sYq7z1CqP8iPI2NjqJiQntZuRt0scm0f1zKeMXmpTMbgMm5CR44U707YXgjf9J-GZUAtzCj_suR-zMGbenmN_EIRWiFDxT-wT0viOpCQZf9ikkRiIEmUQuWHnWIquiHC1zretx-UJqE98pKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوتا خبر خوب دارم اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4380" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4379">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوتا خبر خوب دارم
اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم
دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4379" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4378">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGN9WJEVSKYGOcVrdA5BYh0WbLBMDQO8Go68cjoi4eHy2r2nMg2dHqMGxwybWGKq-am745UBLVbkZFVSFeYvkz8TK74sD1enutDaweV0s6CVNgBtk4CJkPgfTTr0A-Lc3MCCqqfTlLaLauEB6HU1dlwBKQw92GTH335Adz73y-SIqn0QQDZx617N4U14jltZSPkbmhY9HonuKogI4sDHyW3OrTsIR_QbTYOyNWTxkn_3f-vnouliUslOxkma3-1uUKKXUQVN3pUa3JX3quoBKcSFe08mAkvgWtIDJYiGv5tvuil-OZyHleoZ56XnqoR7mun3zhUBTBXVzcD0JDVIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4378" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4377">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSNCrmmFdgzL5F37QsUBFFxYAQaGk-M8O6wSkCAnB9OkPdvz_F5QAHET6QmYunV4rPeLXUMcRDbDxWZW6-K6f2mZ5IMZzisOcHf9FR-6xoQtaoNgvNVaDmY8lcE26X93fAEmifmudfxqo2NnlaOMHa9opdSdd9rH3Ueetz-CsDwkcgGazc_qFq7w8-nuYA9_B-_R3aKN7euQWjxzlFgJBCpGLuesQhw34RR1xnNh7jrKrEwbsp0A3JyQjMyMxrsiPOmTy7gWgkvhFLyAaoA6TT0IyQIcWFZKvveG7PdydhVfxOA-y4wCQP6NbzG1blG6xaPn0pH7QCGdVBMlI0gjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گیر و گورایی از توی پروژه‌ی +220 هزار خط کدیم کشید بیرون که باورم نمیشه با Sonnet5 تازه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4377" target="_blank">📅 16:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4376">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4376" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4375">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X17nlE4j7p3YZB6dagXRfNmWROxc994xi9YkQ0qcx-H7y1QVkAAyjgI9Rt-CU0_zUJd9X_5QCjcbiIpUx9jOXFkDK02tfHqtlRWBQndseUTe2xTYrLp6o6Fg8zEZIGljxmxfI24qHZi5tcs585rwU3G4Zv4f5zdW44PW6E2sNKn45qs-DtOCSJsjzUsUZy5W5wuxqbL-e8MK6kito6JnWy5gM_Ih_oe1Qns6l8F1Dgp36Wcu04Xy8TmuK2j4OTBFO9dU--YhaDTCm8nrHmfhbifrokQXtfXE5P9lJzmqLub_g_y-YKWk9060lOALbNrtT2A4VLN87fthU9Lu3vi7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به ارور 1101 کلودفلر خوردید، علتش دقیقا همینه که کدهای پنل ممکنه توسط کلودفلر، سؤاستفاده تشخیص داده شده باشه و باید اکانت جدید بزنید. ترجیحا از پروژه‌های قدیمی‌تر و قدرتمندتر که Edge و BPB و Cf New باشن استفاده کنید، ببینیم چی میشه بیشترین گزارشی که سر…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4375" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4374">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:  ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4374" target="_blank">📅 16:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4373">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PM6xH4fiba9WCXmk4qJnQ5EjNGayOtNQ7f3Ppp9vLBrdV7_mazP40BMkIgYtfce2tawZGMzxucb1DLzOG4LziM4bDTkO7a6i0OQ-gFojMv0FVgRFMjrvGyz5NgwhB1APmeKBQtsk7QgRPE5x-P1oSik-B7BiLDiA6n2YFgdnfjkGGhSMoVWuTYp5oneEkNaeCvmbJF8x85fyNewrKQkgC_zaOD4S4175OVqMRjak5CXjm8Y1TmsMsfCa_9TcwsAptzYIhQ3tG0AEDCoULC5geuJ0tRTAK20jfMFkTWnaw73y-C_R7Bchnr11FFSpoO7RDEsVvMRkerdEiG5GzgPZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:
ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های ارزون‌تر یه پلن اجرایی دقیق بنویسه و پروژه رو ارتقا بده
✈
این ابزار می‌شینه کدهاتون رو بررسی می‌کنه، باگ‌ها، مشکلات پرفورمنس، بدهی‌های فنی (Tech debt)، تست‌هایی که یادتون رفته بنویسید و چیزایی که باید ساخته بشن رو درمیاره. در نهایت یه نقشه راه (Plan) تر و تمیز می‌نویسه که هر ایجنت دیگه‌ای (حتی مدل‌های ارزون) بتونن برن و اجراش کنن
🎨
شما می‌تونید این ابزار رو روی کل سورس‌کد پروژه‌تون یا حتی فقط روی همون برنچی که الان دارید روش کار می‌کنید ران کنید. هر پلنی هم که براتون می‌سازه خیلی دقیقه و شامل بخش‌های بررسی، کشف ایرادات، اسکوپ کار، نحوه اجرا، تستینگ و شروط توقف می‌شه
💪
لینک سورس کد این پروژه تو گیت‌هاب:
https://github.com/shadcn/improve
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4373" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4372" target="_blank">📅 14:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر
که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که خب باید بگم نابینا مطالعه کردن
🥰</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4371" target="_blank">📅 14:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tOI0eP24mUKVTyA0Mtr6sqVSWxEXutUOZevmvD9b4tLiupbLwVIJ95nXrtMlxvzWDrV0sSWoPqqe03uw-e1hdWXuD-yn6-BC_XZfmVIIFs45G2v1TpGEQtbGlU_5F6etTS5sfNlpUmfr8Sk49GjiSlQ9uyy3unsJ85aWha2y74QdML45DVBqOmCq6KymynROn9MkdIHdrnOc4AUuh2DKY-oi7sztlBODkkatATPuz0SXnvk2XAHrocOJCtdLIfKuWH9rTcnNBBq5H2O-01Qd1tHpF_zgw7qska2KKKXIknnzvZwXpaeG8RlqrCYX-kS1EBqEwlTN-en2pn3vQdDMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y8E277AAEio-IB0VznQqCnZwwlaH_Cs5nwApo8Uxwz3Pl8LzmzRgVYcoFjQ6ZhuqpWaL6hQj9CAImM09ugALGIfdLA5OXPsg6V7IyVwWw2mfslsZiHjBgesWDXoPvi5U4tkXha4yXBY6eu8sdZBryPcosI2MsiymlerRqcPP2Bh_dSQRHAoBiy2s0wamySEqyccUbkSDDFgIdOkNf0EHcAOp_xs-xQa4KThQ24zyn6J58WIlQuUrlWqVB2D_Hu8sGIHQ2hHGPW-WwfBPsSbuFD-e1AyflHCkdO-yAUqe1kKX3qUoGJez7mi76-AqhqpKP5xh7kLKXQBM6bzDQvVZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sYyrua34ZYtF8ls8BlLsFmRrodrQXy-d6kAXhC3jnDv5S6Qc5cD2AXQq_lO_wlq4iNlzz6imu5B8TyVDACt1WkuiGfRh19OscBJe-i2Lsfng9J-1k8hK7cdu7_ghIKjXEkmTMFk88z4l4DK4dBA70ZinZikrxN5P5th4EDd6S2jHNeIuMYV6P9cZIKDYn-7gITig9HjTGiSPCSZS-FfuCJo8lzQO6DEpy2bO0MAFvINhjouiwpWVkm3S2jC17eOVJdQd-lxZnCP6US6sSSHvL6mc0Ra2UT0JHGlfxpSpLvVP_B7tfVnAKajjY1MBaLe7K_yj4PyGkplB4IvB7SmRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sg8is1iD9Q7eqhSRRdACVjR7Ug3M5L7WLfvJPl_fEeP3KHI_lW59JbTXsx6PwTOEbRqxrpNQX_bLHL6pmqJtW_AWKwSW0N4SQOFX6mIf-B0Uk8NeQP5m_NnMof1roEk2hKlrlweDTcSc7Uy1CB9iONMl_maNr1OAnRlODrphSIRrzCTx4eUR2l-lou4i-hQbA4HzddFubL8H6B8Jd2bTKhuDa_TW2FPoiZYFvMFWQALsVK-uDNFlH0OU8OWN_Sms1aBnL13Z8gWlq6aPr2cp_-V7uxh_EI6uNbForta1fr8UMVTmzXrLAHagZdDeN4oBg9m4NBHxIwePG1FFUIWuZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک زیر رو به هرمس بدید و بگید:
اینو نصب کن، فعال کن و بذار تو استارتاپ سیستم تا با روشن شدن سیستم اجرا بشه.
بعد از نصب یه محیط بسیار زیبا تحت وب در آدرس لوکال زیر برای شما فعال میکنه:
http://localhost:8787
https://github.com/nesquena/hermes-webui
✍️
بوکانت</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4367" target="_blank">📅 07:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فردا open design و claude design رو واستون یه مقایسه میکنم از اونجایی که روز آخر اشتراک کلاد 20 دلاریمه، آتیش بزنم به مال(توکن)ـم
ولی ویدئو فعلا ازش نمی‌گیرم. صرفا اینجا بهتون نشون میدم
چون هنوز به open design مسلط نیستم کامل
در عوض تمرکز می‌کنم روی ویدئوهای درس خوندن با ai و بالاتر بردن efficiency</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4366" target="_blank">📅 05:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720362863c.mp4?token=PlFP1wigxQpJdASjII_kEGKkElDKeJCnA_3SeOC8QmD3JckESxn8KdFaQHRZvQAoCAaYlw3wvQ3B7FD3InfEXw7__i5X38aaxHMYIajJFoFXPcjlNcHnDRAELF2Fpb42JHLZtLxekZjurMn_OZ8U7EMSt5bYPCDYDfwr1yvYpfan-_rYcoWooWw9zCqNbzsJTL_A55SAKCSgef6mEpPlyK70WxylZ-js18T40FP23zLRTbjYtCJVLUpn-EKpDv4qjZssgfOESM8pmTUCOjQbrqxjbpvImUS8VweNbHkz2NJp_frF7aN8TDnscc7boUJ0bpDm-GKDgvDPBRAHKIaMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720362863c.mp4?token=PlFP1wigxQpJdASjII_kEGKkElDKeJCnA_3SeOC8QmD3JckESxn8KdFaQHRZvQAoCAaYlw3wvQ3B7FD3InfEXw7__i5X38aaxHMYIajJFoFXPcjlNcHnDRAELF2Fpb42JHLZtLxekZjurMn_OZ8U7EMSt5bYPCDYDfwr1yvYpfan-_rYcoWooWw9zCqNbzsJTL_A55SAKCSgef6mEpPlyK70WxylZ-js18T40FP23zLRTbjYtCJVLUpn-EKpDv4qjZssgfOESM8pmTUCOjQbrqxjbpvImUS8VweNbHkz2NJp_frF7aN8TDnscc7boUJ0bpDm-GKDgvDPBRAHKIaMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ردیت یه نفر یه پورتفولیوی کاری ساخته که رسما مرزهای فرانت‌اند رو جابه‌جا کرده
😂
طرف طبق گفته‌ی خودش، فقط به Claude Fable 5 یه دستور خیلی کوتاه داده(که البته من به شدت شک دارم):
"یه پورتفولیو می‌خوام که کاربر نخوندش، بلکه توش پرواز کنه!"
نتیجه این شد که کلاد صفر تا صد یه سایت سه‌بعدی رو ساخته که شما توش تو فضای بی‌کران اسکرول می‌کنید، سیاره‌ها و پروژه‌ها از کنارتون رد می‌شن، از تکسچرهای واقعی ناسا (NASA) استفاده شده، گرافیکش روی مرورگر کاملاً 60fps ران می‌شه، و در نهایت وقتی به آخر سایت می‌رسید... سفینه‌تون می‌خوره توی خورشید و منفجر می‌شه!
😂
این پروژه قدرت وحشتناک هوش مصنوعی توی ترکیب کتابخونه‌های پیچیده مثل Three.js با کدهای فرانت‌اند رو نشون می‌ده. که اگر بتونید AI رو توی مسیر درست هدایت کنید، خروجیش به شدت جالب می‌شه.
لینک سورس کدش تو گیت‌هاب (اگه می‌خواید خودتون تستش کنید):
🔗
https://github.com/AbhishekBadar/portfolio
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4365" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4364" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.
آموزش راه‌اندازیش روی
دسکتاپ
و
گوشی</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4363" target="_blank">📅 19:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub(Afshin Karimi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebxw7Cys52pkwbvpqXFhn6Y5Mv9rBQxDMmWzkM-697aqX5dOZ6yDWa3OjhO-TaFJtTk3TfijobbEQHNB7mEDy2LYmThU_8D45vbNAROWBoOF1B2ETFG-h26e97_cT_-9x8P73aem5i-nREjLFZDAyXiJXxqHJqVbphCEX6O-c00zCls-hk_dYeY7enBYqQYKxutQgdFV-XZe-cy4TQmplV52L6vOCxSSzwYbfaV5eWnY0QNASUM0hqS1ykrdzGhOQkCcwf1JiJva-G7C_99OOSbkWEKg2EQm_frs3mn5Ns6ZyJeJ-4qc2ysQF7v965fe6orvb9ilVlDUZ9PSiJgJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه GameShell یک بازی متن‌باز برای یادگیری دستورات لینوکس است که به‌جای آموزش‌های سنتی، مفاهیم را از طریق مراحل و مأموریت‌های تعاملی یاد می‌دهد.
اگر تازه می‌خواهید لینوکس را شروع کنید، این بازی می‌تواند راهی سرگرم‌کننده برای یادگیری دستورات پایه باشد.
https://github.com/phyver/GameShell
@RepoFa</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4362" target="_blank">📅 17:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به نظرم اگر می‌خواید برنامه‌نویسی یاد بگیرید، بهتره که یک زبان، و از اون زبان یک حوزه رو در نظر بگیرید و شروع کنید به یادگیری.
برای مثال اگر بخواید پایتون یاد بگیرید و همزمان توی حوزه‌های AI و Back-End باهاش کار کنید، آخر سر به خودتون میاید می‌بینید هیچ کدومش رو درست و حسابی یاد نگرفتید.
و همیشه در همین حین، سه تا سؤال از خودتون بپرسید.
1- چی دارم یاد میگیرم؟(روشن شدن مسیر)
2- برای چی دارم یاد میگیرم؟(روشن شدن هدف)
3- قراره باهاش چی بسازم؟(تبدیل به انگیزه میشه و دل‌زده نمی‌شید)
این پروسه‌ایه که من خودم طی میکنم برای هر زبان-فیلد جدیدی که می‌خوام یاد بگیرم. کاملا هم نظر شخصیه و چیز ثابت شده یا علمی‌ای پشتش نیست لزوما</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4361" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4360">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار Ponytail (که الان به شدت تو کامیونیتی وایرال…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4360" target="_blank">📅 15:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4359">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ToVAX9cSH3Ocuwonn8j2HbTMTIQz_YZFw8AwXislzQO67lYF6JP-bBNfKpMI5my96EAlXsMIs8xrzBxjnslwvjNI2AbEMKIrDfbNENICqBm322UqKBhOg_6rFCkDqt2rpa13p041I51Fxr5LHQ5PsuacM7yKhVdCoNHTah-NWf8SjYLxIxQm7AcBGkKRIW4cYeKNOi7CJekYej836si8Ory0UtK05J8Rl1-uxVqbAdbnO4SjHUSzJXyhLz-3Xkxv6PUi5Hdw7pl4P_Fhe4eYDStKkJWqBGjtFnnHb7Hk2nPJkllWNuTtuKHLQVUw1MQAiPNZZyYNnX99MSZFBZT17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار
Ponytail
(که الان به شدت تو کامیونیتی وایرال شده) دقیقاً یه پلاگین برای حل همین مشکله. این ابزار باعث می‌شه ایجنتتون مثل همون برنامه‌نویس‌های سینیورِ تنبل شرکت که حوصله‌ی کدِ اضافه نوشتن ندارن، رفتار کنه
🙄
شعار این ابزار اینه:
«هیچی نمی‌گه. فقط یه خط کد می‌نویسه. همونم کار می‌کنه.»
چطور کار می‌کنه؟
قبل از اینکه ایجنت حتی یک خط کد بنویسه، مجبورش می‌کنه این نردبان رو تو ذهنش طی کنه:
- اصلاً این فیچر نیازه؟ (قانون YAGNI) اگه نه، بی‌خیالش شو.
- آیا توی کدهای فعلی پروژه قبلاً نوشته شده؟ اگه آره، همون رو ری‌یوز کن.
- کتابخونه‌های استاندارد خود زبان می‌تونن حلش کنن؟
- آیا مرورگر یا سیستم‌عامل خودش اینو داره؟ (مثل استفاده از
<input type="date">
به جای نصب پکیج).
- آیا پکیجی که از قبل تو پروژه نصبه این کارو می‌کنه؟
- می‌شه توی یه خط نوشتش؟
- فقط در نهایت: حداقل کد ممکن رو بنویس.
طبق بنچمارک‌ها، این ابزار حجم کدها رو ۵۴ تا ۹۴ درصد و مصرف توکن‌ها رو ۲۷٪ کاهش می‌ده. البته اینم بگم که تو مباحث امنیتی و Validate کردن اصلاً تنبلی نمی‌کنه و امنیتش ۱۰۰ درصده
❌
آموزش نصب روی ابزارهای مختلف:
توی Claude Code
کافیه دو تا دستور زیر رو جداگانه توی پرامپت بنویسید:
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی هرمس (Hermes Agent)
hermes plugins install DietrichGebert/ponytail --enable
بعد از نصب می‌تونید با دستوراتی مثل /ponytail یا /ponytail-review کنترلش کنید.
توی Cursor، Cline و دیگر
ide ها
نیازی به پلاگین نیست. کافیه فایل رول‌ها (مثل .cursor/rules/
ponytail.md
) رو از گیت‌هابش دانلود کنید و بندازید توی پوشه‌ی پروژه‌تون.
توی GitHub Copilot CLI
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی Gemini CLI (Antigravity)
agy plugin install
https://github.com/DietrichGebert/ponytail
لینک ابزار:
https://ponytail.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4359" target="_blank">📅 14:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4358">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.  داستان از این قرار بود که با Z.ai و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4358" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
