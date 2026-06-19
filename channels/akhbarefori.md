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
<img src="https://cdn4.telesco.pe/file/TsJG-tXh4zslwA5kyaFRz6zZUfRB7uw_QZrhmkocBYuy7lty-Whvl21f3Wm5nTKdK3B03bMoT-aQU5C2zZrDl0OLvOCze6zp9xWXZ2-yTyoZZPAqB8oxa5keTSnxp-cPkKdICVK4t3FDstZzRgY4v-nxLv05N5fGyjx8yjbHM2ltJenkxVQDtsjYRm86INPNv8FUDgccCJmj-UxAjifGQtYxx4s9bKQB3K6zj3empbw2KpXTyaJqfK55rcXmXaflWHMO9DIcE_1-xmjeUc8cxvbR5JonH8r7vLV2XaOgmrYLeymiN9i-niPFcu5ioDIP0Mu7hJVLm9yIBaAZgSeYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-661124">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/661124" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661123">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
خبرنگار الجزیره از حمله هوایی رژیم صهیونیستی به شهر النبطیه و حملات توپخانه‌ای به منطقه جبل الرفیع در جنوب لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/661123" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661122">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYA82aD45i-avS4k0ztqZcWQqBhqeVHJt5PO7sNw0-ITqQawwTIrmmqcRckJI9AjIumDJ41DbQTycNY5FP3i13JuapMJ0jCe5mCNXYdUbZ-cLOP1jxulWrMN-LtxlhOMnn0VXYNNSyQ5gxOh_RfnSePqv_si01bLQuk_Lv4uYW6VqBpJALmCQDferzDZ5zQINliBr9uCC5OwppXNTIW7iSHHP9i2Zmdsjv6FczGHxwMhHdtoggOjZcpaa47HNLGZxt2B8cqLuuo6jCj4aClQWeoM-WAmcyUlqRqsQZwI-qx1LLaq2RcxA6mWYWU8DnEUjHv1EFxxQQhlpZtTrVupTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت ترافیک دریایی تنگه هرمز پس از توافق تهران ـ‌ واشنگتن
روزنامه فایننشال تایمز:
🔹
پس از امضای یادداشت تفاهم تهران ـ واشنگتن کشتی‌های باری و نقتکش‌های ایران از آب‌های آسیای جنوب شرقی در حال بازگشت به خلیج فارس برای بارگیری مجدد هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/661122" target="_blank">📅 17:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661121">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بانک مرکزی: اختلال ۴ بانک ناشی از حمله سایبری است
بانک مرکزی:
🔹
اختلال در بانک‌های ملی، صادرات، تجارت و توسعه صادرات بر اثر حمله سایبری به زیرساخت ارتباطی این بانک‌ها رخ داده و خدمات پایه کارت با روش‌های جایگزین دوباره فعال شده است.
🔹
این نهاد تأکید کرد سامانه‌های شتاب و شاپرک بدون مشکل فعال‌اند، سقف برخی تراکنش‌ها افزایش یافته و شایعه ایجاد اختلال برای کنترل بازار ارز و طلا کذب است. تیم‌های فنی نیز برای رفع کامل مشکل در حال تلاش هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/661121" target="_blank">📅 17:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661120">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931579f79d.mp4?token=otsBYD3_4dnJDI4CFJsPHyxHoHtyKQm8MdGvkIinOfneBUJL7dkHTjVUzFu9eTx9k3le0Vl1yz0NttAC5XSjr4bnfnNhdrKKuS65O7qs2pC7KSVM_tl_HIUQTPfqy9Pr7Ra5FnkW6LCP0TH1eTOvPZBYq355YyWgh9-T7NIUxg0z4MV_T1t-daeyErkSxCTqJ3cJ5wSn-PdEipRVIRPDh7m_OvZaD4rm5zjoskMp4Z1VoNfLwnk4CjxxnJxa1G7vntlAWA_9xfZ-vToLWCQfY4AK5EgMKKODd-TtviJXxCp-rkfuszlJP588SUt9ukwKoaGoiUkROMqzuNSdOfoMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931579f79d.mp4?token=otsBYD3_4dnJDI4CFJsPHyxHoHtyKQm8MdGvkIinOfneBUJL7dkHTjVUzFu9eTx9k3le0Vl1yz0NttAC5XSjr4bnfnNhdrKKuS65O7qs2pC7KSVM_tl_HIUQTPfqy9Pr7Ra5FnkW6LCP0TH1eTOvPZBYq355YyWgh9-T7NIUxg0z4MV_T1t-daeyErkSxCTqJ3cJ5wSn-PdEipRVIRPDh7m_OvZaD4rm5zjoskMp4Z1VoNfLwnk4CjxxnJxa1G7vntlAWA_9xfZ-vToLWCQfY4AK5EgMKKODd-TtviJXxCp-rkfuszlJP588SUt9ukwKoaGoiUkROMqzuNSdOfoMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم صهیونیستی به نقل از یک مقام ارشد اسرائیلی: آتش‌بس به ما اجازه می‌دهد تا به تخریب زیرساخت‌ها و اقدام علیه تهدیدها ادامه دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661120" target="_blank">📅 16:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661119">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ماندگاری نظامیان اسرائیلی در جنوب لبنان با وجود ادعای برقراری آتش‌بس  شبکه ۱۳ اسرائیل به نقل از یک مقام این رژیم:
🔹
نظامیان اسرائیلی در جنوب لبنان باقی می‌مانند و همچنان آزادی عمل برای مقابله با تهدیدات را حفظ خواهند کرد.
🔹
این مقام با وجود ادامه حملات، مدعی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661119" target="_blank">📅 16:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ادعایی، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661118" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8UqEoCm9zk__zq9-rz6wJBlpv4gVfdXek_L3oeHJxTe16C06SQIWhlyEXRRFR4W9GeplK3Q045JB6tCElmk6tuv4GM62GMkzh9PSM4xbG3ObIKv8QAlX9Ywxkg58pD5IcYWEpbiFUlNix_R-uYCjwX9i67DY_sy-VjemH5uAHwhp8zA12j5EsqlhSV2rDYSLJT_RYYur4aWUZNnCzqaSV71740sRQy0-y1kSsdq2bNF_n4WIKSDLlv0f2SCaxjN1xd63nGASldivKsPQTNlzsczIWWUaS1mjMM1vHpK9a_GTH-lgCgLyQHTQFS_XgkXhb-NU7QMaZryBCkEMAT8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العرببه به نقل از یک مقام ارشد آمریکایی: توافق آتش‌بس میان اسرائیل و حزب‌الله اکنون وارد مرحلهٔ اجرا شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/661117" target="_blank">📅 16:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ارشد آمریکایی: اسرائیل و حزب‌الله بر سر آتش‌بس در ساعت ۴ بعدازظهر به وقت محلی روز جمعه توافق کرده‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661116" target="_blank">📅 16:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEIR-smtYR3Ly5IPQaYwOKoNiEuXS1pxRdxl2Bj1c6dRlNUrS3mVPrDDSm2y-cdaczy0XiiMCnmgia0XO8GAISPgpR_vjao7-g6D0pSM3UYV_Jk_DkLnNV01olKq-997-dIWkW5Tgsw_efemYfEJvfLbFrvcsVEyN3E75X3HgS1CB22M7td2ZU2AGXP4p93YWsAXSVuyMQWaTb7DTfqmjMyaF8b_XhbRU6oQIyKu1kgZAQ98mLvtDQAm4sZAZNP0PiyljAXDWgEBKdqv7JeB0r3szah1C9N4IFinpVrTR_OHJ2n2iDFHZvxwKaFXMrxs_84S0gOrimrz7qZ9clRp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFyyFcF-t_1iH-repNF5_bR6UNzN8qiZ8A23Tr_-1Ok1m7drZ4OJdEUP14ZCSoGe8v8SxrNKiwxnadkKe8FzBZMeQDiZxAy-BvcdnO-RdJIhsFQ8YZSV33wWFqGjezVZA4vunhDj58_4MJlaN9unGHJGSdf3AE0sxZwsn600EV53E0bX4e9Bp7dFhTjSjKxMa3QsXlOhJbmLbe7u0Ny8ZzB_gGyhRjClpHncbGPJtlgO_3FGtckxN1AOJo_ybzMpEBfkzw4RDHcB4pTMr4rpZixMt4mWwsA5gyabtmi7fANUUKBGIbcF7lPZ2mRW3MM_yBQDaZtyoJxOy0Kt6Jc71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tejiVkms8DN23VsrqhC-zllt2g0Nx83X8PasxyFhH7e994n9-6V1js8f44ZbpdFh3f9JTHwMFpa-8P2YAswwlXXvKgBcvSSDPf3QtZCZcSp3kgWGQGXPXyM0HWuTgHpn1yU_8oeIzM4GqpaZMTV9kMdfr1QWoLLD9Fs2-o5LXcKjwXEt9-idLfpBgSQ_jNLZ0Zw3FuMjkUdE1yLWALdWlk_PGaRXnJ84Y9azCvCVr2UDE5Yac6vYIssfrDz4rlCHgPfEOnTyOoED9SIIk4zfqxfmEjzxhcfxj8udA1miAVktk9Ayc1M7JdB5nYN9Dt4Uc7_cYXSUV4NG0BtI0TpIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0azCYDRZtc0m8gsEaH_2y9LheetxiGE56ma3K8pKT0_QaopzwkLEF8cQ--qITXLhAAza2tm5_gdXzH8aHDbmcBLLHKWuiNLbpike8vdykP-nT1CTv_cFkYZbUoREHp71luUkzfCpvo3KWcNyH8rWmXxF76JQtiqZ1bmItiIEEX5_qe7aiifJVDYFz7HqFt-qohhXO6LvVoenGJ_xzBCgVK_zg8RmsJ_8sL3J_3h3K0zV9osVx_t7kv2zpik8iFa5JAjgJywRjq03IhyzSDm8EAVJqLLoxbRl5TNAY3jdTNISZCgxN805AiWeXkt-vFvUpsuaI17UJUKA1OH67XsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVwbIrR5_BggEG3wSq7ib1L-d3xGOBbgrN2aLHq3pmKYobnUHa2w-tNQ2umw8RCW45S3kE1GIQR-nauyBm4uDIue5o3PNvrXLekAlMikVuP4DQfULLmn2yp24n1f6C-P-kduRMXTt-YfC9opdU5IYwl8YpTK4HB-fsGxHpW7of1CCtBLuJtq7r-nCywkNrrEw_k-GEqpyQqZ1St4P7mel4K8a4QnEWsGaDJ9PYYO6-WFy4bLOZTXpiQ7OXqNo4B3kNUEQy4b6gqpJPHQ0TKQfckWR6WdzLJ2xzxpVDzMktp3d3X6e2iOyjoUDDeZU_mZYJZ4hhsfm5SSb4zZrf9qNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-7clCkZ4VPTHG1W3WcQ54PdMJxDeapOAu2VYuSj-fA89eOMUShF_XYRSXAlE1UWtX_kPHfqCnoXmRYMB8EfBZ9dnjQ5V80NsgjBU_8WGrO88I6V5GOKEcWrluwCoVnHTdtPBs75VYcvCapelQNQSuqxgwqy3T8bNWE9LINLkOvyrW1ZCqCPBaaZnMltaImKLYz4hF0IZO0puiQHYp05bGvvJPl8tL5YGxU90dCNsbsY_SZCEz4PWee7LDUgUzJDaqFcTgLWzvOpPvTiWpdhnFHdDh-PRBxgv7V-Rb4AOSNBcPqJfY7W5jaurgyyFDw7TNyRjruPzNag2bOc2GeAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVlFNySnHChdL1K6JL0a_M7lspBlavHY70OktV1PdQfFP1kPczhwJzJ7aXup1cjdoDBGNALg9UBCt5z5OXrZdxivYlPadwxa91XZ0RYGOMBw7_IREcUiENvYafUULMFnuz9yJzYeZGOm5boWseFx3wUXX4R-Ds2RMUGPHH9Gwl2BwavDILdVvPyJRvWWoxxLmkUPzp562Lgb7UBTcepbCCaEbBpk6qBk6pmbrpLfZhhhKRA5eB48tXV8Vnd9XH2mHgtT__C58JNW7keRUSWZ0fz0hdZbdJ-31j-60hOO8pQ_kDUsVzVEmk5KamjNppOBCNeoBarflCzFFd3hj5qVZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم شیرخوارگان حسینی در حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/661109" target="_blank">📅 16:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ارشد آمریکایی: اسرائیل و حزب‌الله بر سر آتش‌بس در ساعت ۴ بعدازظهر به وقت محلی روز جمعه توافق کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/661108" target="_blank">📅 16:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWZLIKkNcrBig6vGstsmL1XOAOj4EW52yvBdUHzx2kSWr70_AQxsf08xsgoLC7VPVM4p4XNzIJ1cSiynLsFQlEYrzXfwnKgwePFO5QNxlosNWSKLEbB1WbB4Vgc_LU4nz0jxoqjklzyx5EWE_CpFN_pToGw8ie-zNGpphdWE1-NiEvxKxp0KXIki4DMK7cHez6L4h05N_oCyLmM6YLDy6gtc8PsbBDDArctHPVjGt4WUVlGjxIEPtCw9YSSl1BLYKJB_ifZGe_dlDEAA3y3lzz1EPrXfJmndC13_7Q0hk1aeQKApzZcou865eetT-UY8cQnA0yuz7u2U2jgmuqe1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: دولت باید از همین الان و از لبنان شروع کند، نگذاریم مردم مقاوم جنوب لبنان قتل عام شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/661107" target="_blank">📅 16:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEZoc0LzPqIGAnfVytGq97ykzyHYr-743WkKK_Bdoqm7SWLGz12M4bdjiu8uucbKg_2gJOXdf00Tzf0wzR9Gy9h0_l3KQF_h1itqxar6xuoIRLIG7Sh3CN5nd8XVccAwmxp9ZUiN3m2WHvawJC7K_-cqP461tSil_JdtemON8NYo5fuz1a7nrwYU5YtOfVJ8Mb6wF3qjVezWC4jR8e_4GQoxrQAJhaZvwEHZSGg7X0pWrKfET6tg64vKto26o9meVjwzR9yRc1UTTE5cdU0mrHrdWJid2yG3Lp0Q1NnosfOcv41dDHPLUpm2TjZRR81juxax76Y6NDRPmgxeOaxiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: جنگ ایران را تضعیف کرده است! ایران دیگر نیروی هوایی، نیروی دریایی، تجهیزات ضد هوایی، رادار یا عملاً هیچ چیز دیگری ندارد، و با این حال دموکرات‌ها می‌گویند که ایران اکنون بهتر از چهار ماه پیش است. می‌توانید تصور کنید که چنین چیزی را بگویند…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/661106" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تهدید به سبک سنتکام
ستاد فرماندهی مرکزی آمریکا:
🔹
جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/661105" target="_blank">📅 16:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1r16RB0ncPjKGfOiqK_GUi0_2LBf-mNUUcgEJLwCdJGZYb0ccrvj5xniouiY14bEsDGSBIqMgQa9IH-eqbs8BXGRsNqA_513lJhirfR-n9TJCw8i1vgc8HXzTtKkY-VBHV_TBd2ZvdWG8PvZgBWXV2Fj9xKIg3-YWClBmu-qMiAZ8iMoUhYIZVqerq9NbgW2POL51C_M4-A1NeY9qu6Rq3VYNseJHa6hPIo93Gao8cn8Nw8d-8_LMoYKgHNksjiBBnsA0SOiqQXqmil6NS3y-XAKXSVP0m3KFMDf7DG_Azqx6q_IsECAMX5Vg8ZrGAbDfEqahBl2ew-oEF1tVWQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: جنگ ایران را تضعیف کرده است! ایران دیگر نیروی هوایی، نیروی دریایی، تجهیزات ضد هوایی، رادار یا عملاً هیچ چیز دیگری ندارد، و با این حال دموکرات‌ها می‌گویند که ایران اکنون بهتر از چهار ماه پیش است. می‌توانید تصور کنید که چنین چیزی را بگویند و از آن عبور کنند؟؟؟ بعضی افراد چقدر می‌توانند احمق باشند؟؟؟./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661104" target="_blank">📅 16:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
هشدار ایران نسبت به پیامدهای جنگ‌افروزی اسرائیل در لبنان
🔹
سخنگوی وزارت خارجه ضمن محکومیت شدید حملات اسرائیل به لبنان، آمریکا را مسئول مستقیم این وضعیت دانست.
🔹
وی با استناد به توافق ۲۸ خرداد ۱۴۰۵، تأکید کرد ایران برای حفاظت از امنیت و منافع خود و متحدانش، تمامی تدابیر لازم را اتخاذ خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661103" target="_blank">📅 16:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661101">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhw_scRFb_2yiqgewTZE6XqGlzpmpW2JmOgdVlncecl7Ro42nG4xKehElMglDn7B6QiZ5BhgUNFFhopB85AVT8aH4lQIBdm_hq8bktu7tQW5OxBusCj3kf698NfmhiFtnHobGYu89IiywubqkD8jixszRD0k4KeZZI5IM4oReWYZEfnoXu7r7TaXjmFFMkYt2VdfPEkTu4uEF5ETv809NjN9gBWtnAgsbCgYZJTH-2ChOJtCm-ddfOAm1_UeiGo1NNyRnKk6Gh6wbvb-kkdRax7SvG-fvUbAcnyEkBwUrFpucdqP63a7HnWOdLSgElizhATxx5UtIcaptVYOd6cz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به رجزخوانی وزیر امنیت داخلی اسرائیل؛ فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای تمام بشریت است
🔹
این‌ها رجزخوانی یا اظهارنظر یک دیوانه و نسل‌کشِ بی نام و نشان نیست؛ بلکه گفته‌های علنی وزیر امنیت داخلی رژیم اسرائیل است.
🔹
فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای تمام بشریت است. این جریان همه انسان‌ها را تهدید می‌کند و تنها هدفی که دارد، جنگ دائمی و بی‌پایان است.
🔹
ایتامار بن گویر وزیر امنیت ملی اسراییل در پیامی که در حساب کاربری خود در شبکه ایکس منتشر کرده است با به کار بردن عبارات بسیار تند و تحریک‌آمیز  از جمله «در برابر هر قطره اشک یک مادر اسرائیلی، باید هزار مادر لبنانی عزادار و گریان شوند.» یا «تمام لبنان باید بسوزد!» از مجازات جمعی و وارد کردن رنج گسترده به غیرنظامیان لبنانی سخن می‌گوید. وی در این پیام آشکارا ضمن مردود شمردن هرگونه روند دیپلماتیک که منجر به صلح و ثبات در خاورمیانه شود، از اقدامات مبتنی بر کشتار و بی‌پایان حمایت می کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/661101" target="_blank">📅 15:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661100">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
خبرنگار الجزیره از حمله هوایی رژیم صهیونیستی به حومه شهر النبطیه در جنوب لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661100" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661090">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnSW9QylAs2stp8BRk0B4iOUEuqs8MJvwCUmOvI2m76D_wpkIrRQ15yDkB5eUpjZ_UwmFJfN1HEJU9ELRtXJBHvaH6WEk1cmYkxQbRhVUR48-YqQsnbJ8AyTKWNOX_dQ7cXcZ363IB0LUi0SSk8AmkXJU7_fVGAf55l4ODTYuAqNsK0JLczSxrrN4JfV1Ht5Wqa0Xg4u-cBqm7zCjS7LYeRI-f9ADAHPUWADZw6EGnon8YE1XJgh_PMNpDxak1dWKt2gVz3Hos3DlQ0GOo2yyewHkx0wldCdxuT-X1gXeVY2EIHorzNEN6m8be35KKdekVy38LvOMYSsUDJjGPqihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1nUkghpRsBQEzFH-UrgrtVWgYZogWapCbZvE563NJcec6SMxp9d_G5L283b6CAL3Osd7sY8H4EIjJV3aTRXTZToJec_yv_j-_Da-NOhh8Sd33NPngGtGUl-GR8g8ne8xKF7PpGc6A8jOqVIjRpgERrizrstZi1ccR0Lnfpt0RJ7IMMDHQuiWWCCu3bEOwFkLDdiEBMNlBOLD4f378VRxwNxiqlaI37QUQ0TXRWT3arc8-iZLaRIa2pOdJuy3b5DcjTANNzb5NkrKjvQrfjdRVOM1N17PbOwrwMWs3s46ts4BK8GCDyCEFqZM1sBiP0ZKTwbFz7z0qjavtyEl_dP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9GBqKsSnoH6F2YF8Wu2FtWcLyXUuWyGkDIAyYRPhUdw9yYL2LY6DhSvYC2S3zBQKFt7ar82IF6f6arg41d4JwUP01kqBzCPAMIAFn45wNHZ9igKBhLU0dTCoKjnHvHSRdoeBeP501HB4QYdlEDSxxZxa7NVnQsZu3MwnPcCq6V6Nir2vQBqvVDlbwkwxreRCRqh4x6Q5h_lT8f3rTX9Jkhk5X3hIWq-USZ0rSpy-BuP1Dpigmi9RJjl0UkZ2jQA_XJ7cT8p1KCg5dmYwVBV6H7p_sBlS61nNnkTDBD2g7s0l7N8H2Ybk0RhEdZCKmGX9VVM1IQrr70lEQBxx5g3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsz8p7JLCgQpHy2gvs5BAu_0dt02jDPWrsI9Y4jp9gJ8sVx_DrpnQ3kIJln0umXRI9lKu-2pfOQqlVtp8ynNLalKBsVAR0slRZy4p8U77VceLd2f_lxpkCF1-o0H8V5N5pruG1PhlKL2T7eDgzFwCpDiZF8AsX9veFhI9FtVNEY-YL9lGPSZvXYqNRY-tqVfS68kK-Qp9YSbY-3d1qQJoeklw3n5rWncNq1kB1RPWOmbaGsaMtGw1uR8UjmSij_jkweoCLL7irr27_7FdGkqz5XUOp5lyizB9VEMxU3l7KSmaJ2gYsKCmPJYMf3v1CCbtnMCWrCn_hY3zZcUBbqVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxOhfTPpOLKoQANeHVSCS8RontpiAy23Hf9dwk7xqded_3aBezjZSvKP8wIt411UoETxqwaeP8ccdxYmMkSNQJYuo3jS1T1l0r6rSv65YywReibkwwKOIplEIErKdljAZiUvZzQjl463_X2rjPNtdb-B12u0c0njWTF-aKfT-_woe3cupii3_UdNJPDB_qWd6Msz80tNxTOb9n1hOiSC4hrmF39fhERh4T4oubzlvLVBlVDblkt-y4t8Mj7GCGOPf6V_way45tHN6yMZJN3fwdVPYWFiSKEPSW2NGNuB1oYBVHg0mDS_lzLWYebIXsKPlTomzlWziISDjJqN6ZZL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTuPBviMiz-0nHkExoNd2dPsf5_P_tE2huZa3TB0WFdwdSbf2oKAsPneSBKJ8BmdWyG3FAxeRDF11bJMLmR3_vTDd1FFlsBeVfZN5q22bsHHV19g-w9my6vkA0IIbmewK_2qE9EdAFKinH2wgmH-JH4OoAzQnotThIx_g1sBEU0IqKSwRc2Ttp260D0j3ulzsolSN4o1Z6XP7WAcE9G9l0sK7Cm4jF1q3TYyAqlBXXrndv-4hhD-isJ2DhJCmWs8FfaYLau_csNkun-UrZaPzvRDLMfnmB4bHQk1CxQipQp4x-uRwP7vMMPrcAOWuXxY5MeHNidMxLOFiXLLQqrzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekzTl_QjFPalo9RujKb6wYjIVw1K1cXIjm5h-alcpfWXK8hQol26eNuPYbw2ZHOFJfPuCJVbAJuCT2EkY1zKCB8STy9BmVCDmOpzESLK8xz0DqVEIYpvyCErXeyg2OKCjDx2e0E-0GYaeXxH_HIrIRJU4xGlmU4ryCZYNq5F5N4Vtn4zgywTPcTomVUQO5lVQS01H_ggHEL0mqThK_39pV9UMWzCjXlhddH03tMfMxM1SNDBLmDpJGv3K5ugwnRngSyNXbWg6tmK96CvbcldZ-gY5G_1I6LDe4NGc-cbOXqdRa5dVxitAGRTiGhKRk3nxsZyoJOP8z1cLLwmPnlPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agGNIYeZqWw4VFlZEpof1eJtSAgF9Oumv0Jj5JBvgopZBLymAOrKVYitK3MJ3JNDqLeq4rHS984PWN7ufM6BL31rISqhxxfgwE5jnX_8vddasXi6q2wPM0pyBrcJFnxHTdDb4VDx8JRYxnJaw8cQYj1EDS7Bv3WPF4IlfoNalYLIp57eXvj3z_6no0WEV70EeAoKF4tb1HjsBXdYEGcOc2o1X_-lNiiZje3-HMaF8UiDE_HRxPULb7sNg4V0Kq9nC_NwgKHVW0DBMk862Y31Tz1I46bCf68zgF20nXb_mkwn3Zu16wxjrJ7VorHnUy3N_jkhvfriAnKc-HcGvjX0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhjBBbL5EFtksgRkPQsAYED9ykMLakKrzxr2lYEkXXV5aIDhiQ46rrsBGuOvJPcA3hTAAr6M2negmEzdqI6SuN2cfdyPo6evkL9Rxc9xq1edBExENMwCAkBc8Oe64YuNE6x7AU7DfrS8fjGQsAXSS0Q3FXFv1gTyZXR-4CsREg8gw-Q9R9QqPO3tpi3buEhtF1QWlJ544K6BdKdvjChkDUcJbHLCkX8vU0MwFv73OQtD9u1hk0QG8JmXNW8zA3zm1msD5GK6Uhfb6z1cUPY6qnkdIoAZTI_TxQ4MPdavRxfHxBTNkPdX7Y1MPUyQ5D3sIZyDvYCHUmJfBXatfbB-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmvZT17fIsEdolK4wXzXbuvanmhTiBsEMcFuSJD3w8D6nMZZWiA4D7YtIs1ZkGYWX6GxApFjvyLXqwmDCtvKXsfJ3nPA4oboPAfWE4f6x2Ec9xw2IODc_Xi-fAYX_rj7a5d46il8sMrVVqoWhc1AbI-eneE_rOhjUq-HTNo2dt5BJiQxCHAd-UGa-nvBdB4cyMaovLsmveh9NY1OT6usxUVRzLrNl48KhoDhxr0oez9pWxKELnEgH_NQ3eDSOwSnO3zSNyaWFBySb0MoH3mhjQANy8AyXK1PCizvxiz0TnEJhayYEaMNLS7TSlMeV3V2Gi0ry_QSxdPe6tFyVWhINg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
تصاویری زیبا از مشارکت مخاطبان عزیز خبرفوری  در پویش بزرگ شیرخوارگان حسینی.
🔸
شماهم میتوانید با ارسال عکس فرزندان دلبند خود به این پویش بپیوندید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661090" target="_blank">📅 15:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان به نقل از منابع آگاه: آمریکا به ایران اطلاع داده است که اسرائیل حملات خود را در لبنان تشدید نخواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661089" target="_blank">📅 15:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رئیس جمهور لبنان: تشدید اقدامات اسرائیل عملاً تمام تلاش‌های جاری برای تثبیت آتش‌بس و پایان جنگ را هدف قرار داده است
🔹
آنچه که اتفاق می‌افتد مانع تلاش برای دستیابی به آتش‌بس جامع در سریع‌ترین زمان ممکن نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/661088" target="_blank">📅 15:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a93vmNddBQs3OIsGhxiHO3GqQeL9yChJLs_SP-dnK3I687AXwuG1vVr2DwVwtek_gJHnAFu_Lg8bcErzFgTSdsyZPUz6cdZXV3qEQQLgXY9VaYcErkGH8UNH7QNEayU3EIMkoCDu6cS1gq-0tb2LiHKVQ3fKjY2nifVBkr8vKgEcxfFtTa-5mNLKllUNAB9tfFPVPssjud8Xr9BzF-QRKZcLAxjg3pMx62YXdr7RmTXJhILJkYbWJ5KXNzCWoaDse3UGyiOPwwsFfI9fpr5sLzKJgjOEP7TR2Bl12CWx_yhEi43RipXXVk3Td7kkNKt3Zjz64b4lT2oMJWxyKDMOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر آمریکا در اسرائیل از حملات این رژیم به لبنان حمایت کرد
🔹
در حالی که آمریکا طبق تفاهم با ایران به توقف جنگ در همه جبهه‌ها از جمله لبنان متعهد شده، سفیر آمریکا در اسرائیل مایک هاکبی از حملات اسرائیل به لبنان حمایت کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/661087" target="_blank">📅 15:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ترامپ در پاسخ به منتقدان توافق با ایران: برخی تندروها دیگر محترم نیستند
🔹
من یک آرزوی اصلی به‌عنوان رئیس‌جمهور دارم؛ هرگز نمی‌خواهم به هربرت هوورِ مرحوم و فقید تبدیل شوم
🔹
بعضی از افرادی که قبلاً به آن‌ها احترام می‌گذاشتم، دیگر برایم محترم نیستند؛ آن‌ها تندرو هستند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/661086" target="_blank">📅 15:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1391551f8.mp4?token=AzCYyXwyc3_lhNY1yJOrqCO0jxr7hbI0tferPF_GmC5FRE-17BlO7t64xk6Cd1WkSXS439Km4w2B6g6Sjr1Nla9cQeebxfdXzJVz9RiYazzALoNoFJGOL1vgaW4D4Zt0RxkZe-5PKsx7Qkngc8SKyigjuZ2dELH0lXJ2WV9OmCn8dvj5C7VlKpQUA2KQyqE31gXSn_pE3q6KljZ9XM8q1n3fsgqt5BOIkG_wdBHwL1h3mD8W9SDOGCl01PXKXN7xSEe7VkZS4UXk6SSOK5MuPv6x-N298n4r-8nV1zzjF1yrThNWkm2kNtk5zKF9zpIEKZkaMNbHVrL8Uo6jd9uJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1391551f8.mp4?token=AzCYyXwyc3_lhNY1yJOrqCO0jxr7hbI0tferPF_GmC5FRE-17BlO7t64xk6Cd1WkSXS439Km4w2B6g6Sjr1Nla9cQeebxfdXzJVz9RiYazzALoNoFJGOL1vgaW4D4Zt0RxkZe-5PKsx7Qkngc8SKyigjuZ2dELH0lXJ2WV9OmCn8dvj5C7VlKpQUA2KQyqE31gXSn_pE3q6KljZ9XM8q1n3fsgqt5BOIkG_wdBHwL1h3mD8W9SDOGCl01PXKXN7xSEe7VkZS4UXk6SSOK5MuPv6x-N298n4r-8nV1zzjF1yrThNWkm2kNtk5zKF9zpIEKZkaMNbHVrL8Uo6jd9uJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فصل جدید تاریخ: توافقی که آمریکا را در جهان کوچک کرد!
روزنامه‌نگار و نویسنده باسابقه استرالیایی:
🔹
ایالات متحده با این توافق کاملاً تحقیر شده است!
🔹
به‌نظر من، این یکی از لحظات بزرگ تاریخ جهان در قرن حاضر تا اینجاست!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/661085" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QamlW0tRtEsX7HskWFJaQfjjDb068Xhqa9J7EQmokKqFcuwLpXMoid5dbDrsxD4JktJ8RlHURJxk4hZFrlFhv4LnXX09fV05JB9HFJ6od0csrefAVOwtxl9PYBpfu8p7kUpM9nSidETnX-H6NRUIqaJErIHyNox9Wn0OiBlNcA-n43wNcU6KHpA8skcJn89mRXWuoab1XnBfeSwlF3jqmljgikX28FbuFqyp8PZdX7jWDjgoes4CUYa4nsMdJOsnQ1GJe0gt8vLcK0g45RFCWrxrS6k3x_3STeSmey7vU5nkBe-wq9fsj7DxGKZuu1Cw07y9vrvRxhUyetYOjuVMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: نگذاریم مردم مقاوم جنوب لبنان قتل عام شوند
🔹
دولت باید از همین الان و از لبنان شروع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/661084" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661079">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cA4FlR2AEsAq0-FSRda4p3TshltS2HbFnMI-Y9BESmDbPVtPlYTX9CjvKIsvU7qCyiXnA2lMdShAjHdTk3Wjbj5M1Zx6UkygWHaRpMqEam5gR0eDG5C8-bBqk-dsWMyt7gox4cZJQmbSPidpFxHOTwmNV6Wr-3lJ6LdGbpuaUfvH65C1qlqEcmpi42VYeP9KD5V1s95AOk5aEVEdu-MitS92B__FddzDzakG9TV6TvrgfkvqYTamXs1FmlWvsDRe0UgpnXdK4rjzxPztpvVklhEMMUoeOMVeaCAMknSCtq7aQtgXu2iM6FW1qHMFvDEJnQ5_-mOK2I6BGOEKvZjIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIQRlgnZS0wyO7HDF46JPtZMeNiHcCMlY0djFSVvvoFOM4EFt-wh3D3wIkDBIG3aiBBri5GL-A2QR3QbsFIpmLD4Anvu9Z4ML3FqITELU0dF4t_nuQuUw7tDAKqgkdAsIUbgANc8WWeO_z4tWY-XsqfBqlq49y7XMx7M3QP-Xo5_W77SrJHHzCEvPZlDRLONqIkjR-96vYhICaM3oTVVm6m-wK2VF2RPqGLzh78bpZzegg45XB0NymZ5PV21Tlg5_W4h23V3eUWHlY3h9aVQ97sllf07Jeo9k7R0blpCE67eD9NCNQ7BbM8XwcVVUJpkV1L8fr0YXcy9LrBVCV-CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtfVmt9siLsTr--Cw6wfRf7uXFzudqRh6r45uiQT0PdGzl1Cc66cRW17skkAywsTWSy5EQ2upb5cYA-cxcIMeneV0WnCtipCp90dujTpZW4ctXqBLaoCL1JMtmLWjivR53EzTmjwAOHAHhHHiVag1yLF-z005rTY8Mu2Tf0ZVc-gXm8tZIbZ9WgqoyOE0I4_FEg9ZYGcTZul47-xva5ir1YJ3Kws-FtwUJ--ZC-RnJzYDG4Jk8MVKZ7RACz744zfajm6A1OtedsMGGlj52vt4Z_uduLm1h1MRYWOLplK2R81QNCUZBNfXNtD4aPjxSDLzsK12NzKd9nk1vmSzXTyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/it3fWRHYefsKKB0Ls-zznqSSyeWkS0jBThS_Thn3WloDsmLCcoQN2rMAjGQBhYBTcOzKf-5LZ3rm3OJ12mQCnP0pVo1FTXVNgenzf3a4JQnupFwmaVuBmI-wC7poJoOELIsyyCElMsq9SwANQ4SLFFzYo9aZFyqMdLCY8aivjcDPK_pVkdV4dxslKytcnKI3OX6eluiHPuLaFLUvoP2lfyE9c9UolIKIVykQbMt_cE2G1dv4D2ZEhP99TkAmkCOeyFY7MdJjMQen9cHB1jYVV91RTZCQIh2AQ-b8CAyMpJcCyDcFDDL-X84941b_dZVSlqXIWOzoWK7S5m_6WDx8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fITMivOW5yWXr6AFNJs0mG7Mo6vycoLCpH5IyBxaDpvE6_tfGJo1-1yI3p7ddqAeaMxWJs-0H7k1m9MKUE9qPjdiearf2HnT04-CGbNlmlKwvpBabaOuK3S9SuhniOlpGNoOwkYaMBR31LS5eRUjUox0Ia0JqoN91T1ku8CB_FVS9TEFxDBcw1Vy4lvAXKr4rVHEvJxJS6wCDrU0FslvfptfNTVTXrS1Ls2B_1n_8QOyJPtjcTbMdFs2eFAkZREJ-5fRw44UBo2twy2vDnESWM2gfMg-Yt_9FX5rXQq58X8vg1RwyEzPFNgaOE3uzm-cObgvKJq1QtW2EUYAcCT-9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور هزاران نمازگزار در نماز جمعه امروز در مسجدالاقصی
🔹
شبکه خبری قدس اعلام کرد که نماز جمعه امروز با وجود محدودیت‌های شدید اعمال شده با حضور ۷٠ هزار نفر در مسجدالاقصی برگزار شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/661079" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661078">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای خبرنگار العربیه: مذاکرات میان آمریکا و ایران ممکن است طی چند روز آینده آغاز شود/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661078" target="_blank">📅 14:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661077">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiYiS4N_JaJmnDWWvyO6BfY9KL3hsYB_GDtyDYJ8O-GK8ct5HcNfQRMpSs6MiKYUm5QnGHZGTSx1lYe2deJxcTf7jhThVWSNE946gTI5OADz2ZKQvXJLdd_wX6cG_HQ5Q_6p1Wu41aIQEVUuHNFlq6-QL8pGqD9eLIWaeMKZeTUkyTeGZRSAEU3Zm_wAO9-IOwPzv2qzBppDZJ0G0lVGrlPNqCN5SwgtbHbEUblD9gMY79d35xFtDxPwHPGNwtQNIhXtHMfkyIVNnlwYzvoovoM6_S-jPQs-ODTWvBKYsTbeQ9WFAIlIMG9-108EaK2H5Ll6JScqqSgLQ-HYRMYXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام قاره بیشترین کشور را دارد؟
🔹
آفریقا با ۵۴ کشور مستقل، بیشترین تعداد کشورها را در میان قاره‌های جهان به خود اختصاص داده است.
🔹
آسیا با وجود آنکه پهناورترین و پرجمعیت‌ترین قاره جهان به شمار می‌رود، با ۴۹ کشور مستقل در رتبه دوم قرار دارد.
🔹
در سوی دیگر، آمریکای جنوبی و اقیانوسیه با ۱۵ و ۱۴ کشور مستقل، خلوت‌ترین قاره‌های جهان از نظر تعداد کشورها محسوب می‌شوند.
@amarfact</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/661077" target="_blank">📅 14:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661076">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24f0dfc36.mp4?token=mr1rpw4FJ2nvFUHtSmeyILL8BT1SYk4FODOUFjzI353lj46XfypLjCWxYBTQQAo1cekOOOGaOVexnsWbLC8XHpde3WTVEmsAr5QhguliDUr0v9cLA4sl7CBQDZceG4czEveAgI5WU0l1lAekQmT7qmnQtikYsUYA5JjXktTbsuFo2xnSXc9VPulGkwsQhriBWB34Eu0PgO5MyURZEqlNBaJ2iaf51zhEkxxxu3xBDWWkQRDORQ_TtleDOikOY5_fgC096J7dBoOxyNIEwG9hgq9LrdOpRQwbs9tAG5a-0cHppuHfKdIpIVXyPnIuPR-dAt7QuizStDLUhTrLVvGnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24f0dfc36.mp4?token=mr1rpw4FJ2nvFUHtSmeyILL8BT1SYk4FODOUFjzI353lj46XfypLjCWxYBTQQAo1cekOOOGaOVexnsWbLC8XHpde3WTVEmsAr5QhguliDUr0v9cLA4sl7CBQDZceG4czEveAgI5WU0l1lAekQmT7qmnQtikYsUYA5JjXktTbsuFo2xnSXc9VPulGkwsQhriBWB34Eu0PgO5MyURZEqlNBaJ2iaf51zhEkxxxu3xBDWWkQRDORQ_TtleDOikOY5_fgC096J7dBoOxyNIEwG9hgq9LrdOpRQwbs9tAG5a-0cHppuHfKdIpIVXyPnIuPR-dAt7QuizStDLUhTrLVvGnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم تجاوزات صهیونیست‌ها و حمله به شهرک الشرقیه در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661076" target="_blank">📅 14:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661075">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بیانیه حزب‌الله لبنان: آغاز رسمی عملیات عاشورایی در دفاع از لبنان را اعلام می‌کنیم
حزب‌الله لبنان:
🔹
پس از امضای تفاهم نامه ایران و آمریکا، حزب‌الله به تمامی تعهدات خود عمل کرد اما رژیم صهیونیستی به پیشروی زمینی و تجاوز هوایی ادامه داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661075" target="_blank">📅 14:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661074">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbtkMJhWEawklxI7BJWA-kpVnJQ6LIfItuZKPbSnHqi5s4SKGhwQ06N2qGEgWZowB2G9mHW0vo0GCiNVV7clpiGOsQdzsvYbqd2vBOHgPFdgf3rkMv2FPTURhxaYQ65vxhqckUNpdwXfntBcAZt4p2hKfZLewHNn5V28ldtig2PIF4E8M6Y_RKXDSmP5rJkB7X1QiVOxDShebXCLT-YZScAkG59nOL3ejL5BdgCrpwHHyZ7aBEzMpj4hPyhmCjf22BCWqBEucjss5z08FNQfU8eRZbWywCfcaehwpUitBHgZTKa8Hy0Bh3YLGM1cWsEHKwMvfiL1ciZb_QWyG9Aczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پست اینستاگرام اتحادیه جهانی کشتی از پیروزی یزدانی در رقابت های انتخابی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661074" target="_blank">📅 14:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661073">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=QXf1R_l8JjqtQ_0WP2haG8X-Cps7J889Azw0CyVp0AYocDyOtougIMxHn9qf7VlHFvMzSdSvKv2k7DMFXugxPhHFWGWV7LK3VWa2ukZarB9NlZ6HBDPfFAQg54H7UkxnIesu4Wep5jD-8BiG8MdmfdThHUf8ID-4TFh3JiCU3cUbVf4TrNjzX66CIZWOGxqnTw9zH2_uNWO3D9jZoiqoDsrTf2ExRaLj3c1C8nPtC8Wrc31vuPtpQlld-kfAGYFeFWQx3TvTCo_zVQ_Vj4bQ05w7VPQxtcfS4vvcz4GK0zfT6bTGtc3cXnifI7bPKbjcHs7iy67IJ5MWb1Cbbp6sYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=QXf1R_l8JjqtQ_0WP2haG8X-Cps7J889Azw0CyVp0AYocDyOtougIMxHn9qf7VlHFvMzSdSvKv2k7DMFXugxPhHFWGWV7LK3VWa2ukZarB9NlZ6HBDPfFAQg54H7UkxnIesu4Wep5jD-8BiG8MdmfdThHUf8ID-4TFh3JiCU3cUbVf4TrNjzX66CIZWOGxqnTw9zH2_uNWO3D9jZoiqoDsrTf2ExRaLj3c1C8nPtC8Wrc31vuPtpQlld-kfAGYFeFWQx3TvTCo_zVQ_Vj4bQ05w7VPQxtcfS4vvcz4GK0zfT6bTGtc3cXnifI7bPKbjcHs7iy67IJ5MWb1Cbbp6sYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت تنگه هرمز تحت مدیریت ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/661073" target="_blank">📅 14:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661072">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c2d34ea4f.mp4?token=pc39vxLMQAYdXBKeTu3bW42zpoV35guEoSkHv8IBlywGc72khMHqeoPFeORksspul6Q-tJwjtNz0DjU-dif3PhPdaXWd4XZdx2Hx9Z8eFPsUP_fP0BQ0QRM43o7NQRsKKGWkFZUQxMvkiDESNrbXkD4wKmMn2JKP7FqDAfiF_4xyqEOeMfs5D4bsfRSUAzbdKJ3HZA8nRTssxXByrsIq9JPiyzXJ-GX6hMYN_6-gSyQQtO0Ho73hJCruw-eB-QaVhVTm-AyhVZ59iFnQcwonx53FckmS26pJEZaOobcHipFL63cgGAW9vU7DIaQtCXWj7J-B-o5A6fzSe6_FgVjs_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c2d34ea4f.mp4?token=pc39vxLMQAYdXBKeTu3bW42zpoV35guEoSkHv8IBlywGc72khMHqeoPFeORksspul6Q-tJwjtNz0DjU-dif3PhPdaXWd4XZdx2Hx9Z8eFPsUP_fP0BQ0QRM43o7NQRsKKGWkFZUQxMvkiDESNrbXkD4wKmMn2JKP7FqDAfiF_4xyqEOeMfs5D4bsfRSUAzbdKJ3HZA8nRTssxXByrsIq9JPiyzXJ-GX6hMYN_6-gSyQQtO0Ho73hJCruw-eB-QaVhVTm-AyhVZ59iFnQcwonx53FckmS26pJEZaOobcHipFL63cgGAW9vU7DIaQtCXWj7J-B-o5A6fzSe6_FgVjs_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند جالب برای استفاده مجدد از دورریزها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/661072" target="_blank">📅 14:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661071">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
همراهی متا با رژیم صهیونیستی در جنگ علیه ایران
🔹
بنا بر اعلام این اینترسپت، اسرائیل از متا درخواست کرده پست‌های حمایت از ایران و نیز تصاویر اصابت موشک‌ها را در فیس‌بوک و اینستاگرام حذف کند.
🔹
اسناد نشان می‌دهد متا در اقدامی غیرقانونی در برخی موارد با درخواست‌های سانسور موافقت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/661071" target="_blank">📅 14:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661070">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-84qhTs2tYaA196qTUuSF04Qj6evZ_vRKx6GPL0grl5G09rfHa-28tPnW2mbtYIrckWb2vZwnEiRbteeK4lnl00dUXPe0DTIJK7p-oX4R7d0QI4fFTc1lmotZkzelOGJA-riSoiP-jNs-_gJmExLMT6f0ok7rFalk7BBh3r5HWX8jVIgJ1bVs3oVAFveqKOd8Lc07YUWymXjU5xFMNYDsuVYwGxc5Z0F2nvmD2g2UfnHPAq4K7iN9g3EsjkxJgSeGhC9cYQibFEOQpWPLDGzcaq-g6VdQIDZNiajw4v9Qc_tB-ynl0sK4N-e9jMlEG0C2Dvnc7zWlu0EuRa-mJlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/661070" target="_blank">📅 14:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661069">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTNdrGQnHnMyIS-nMmYuRGKC-QALNO2zUjYthA-hxumgXIJv-sRd_aLRiCv5yB1mGfvso14j_Fz74ZqMNbfGv1NyUDQLp-qNILD6BcsInz4Sq0ycX1krBfgnfSejnZihEcnfk7FNAMZCE6Lww8_FuU8K-TQ0KFQzUeRHsFnTC52Z1I9ZoKV7bdmmGye6RYDOLupk4IRkegArsr_249to8-q2o34EZju4zyrDSBU66At7-4yX2If9ge4KdwISuVv_Pg0z_S11vQ8BFn6ATJ8WOnoqqWhCcxaCKFmyNwf541suxfUVVm_ZVlmoHA2s1Mfq9dEnSsI30QUMBu6Fh60Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدمحمد مرندی: رژیم ترامپ به تعهداتش عمل نمی‌کند؛ ایران تحت این شرایط تفاهم‌نامه را اجرا نخواهد کرد؛ رژیم صهیونیستی به شدت مجازات خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/661069" target="_blank">📅 14:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661068">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان امروز در توضیح درباره تماس تلفنی‌اش با همتای ایرانی گفت «رئیس‌جمهور ایران دعوت من برای سفر به پاکستان را پذیرفت».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/661068" target="_blank">📅 14:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661067">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTq3u_vqIzmJ2ATkTXPgoZDfZrmPPS0-qXaGZgqi6baEQdBBCXMV-4-sjaSEJ-A-A6_34M0dcmCwGdjdXCE1q2G-Uqn4Pvl1U7LahgT6suL2U16R3E8GiFNXKSOVyDIjc37dhwawuN9t98iivy0JfpOm3bpumUT4rzl7voqhT8tVAzm1_bsMILaMhfMQv-F7PcT3AMv90ul2jNLi16wcACIHoQIfW_ksuQrF722G9O-fmWSJdJextrarlGzDNazxLrMq55McFpQhgEMBiiiHEp07PMtPJMjMT5Rwd0X_yq73qmzqK7sFhPjAlnZdBviSHSTVMDr9hRzbRMVvQmSE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه گویی نتانیاهو علیه حزب الله
🔹
نتانیاهو، نخست وزیر رژیم صهیونیستی مدعی شد حملات علیه نیروهای ما را تحمل نخواهیم کرد و حزب‌الله بهای بسیار سنگینی خواهد پرداخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/661067" target="_blank">📅 14:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661066">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ترامپ به اکسیوس: رابطه من با نتانیاهو خوب است، اما باید او را تا حدودی عاقل نگه داریم
🔹
اگر دخالت نمی‌کردم، اسرائیل نابود می‌شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/661066" target="_blank">📅 14:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661064">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL0vNtIoAaWjA04UKUwC00H8_1EiV8DXxHjBjQ99vOl4E0lSHYuOHxR8keK9YeUlRKZ6nZyxhQGOxhduCwzoayEFljah7W38z7UQGveUBvvtiz5OVRGB7arCOXNPLRXDZEAXTiaXz6-Z7VMJSfTz7x8s6oNAw9koFaoJ3y_uX2G2jlXTTU9eOUl7-B_RibR-Brv33Mg0OKGgg6OO5ORPvcaAqYEFcOaDVWoWAIGuO6KgwB5G39IudYkk_LUAARnodCaXxzBhNYKDicnvGyHGUqPN11BWpBnb8zcQZwfh65jN0dIiLLZvkE_i_JA7MdiooUl8s9x-qacvdSWj4wVH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ حادثه ترسناک که قبل از آخرالزمان رخ می دهند / اگر این نشانه را دیدید بدانید آخرالزمان نزدیک است
🔹
در احادیث آمده است که پیش از ظهور، قحطی و تنگ‌دستی آنچنان فراگیر می ‌شود که انسان‌ ها برای یک لقمه نان حاضر به انجام هر کاری می ‌شوند. امام صادق (ع) می ‌فرمایند: «به خدا سوگند، از فقر و تنگ‌دستی چنان به شما می‌ رسد که چیزی برای خوردن پیدا نمی ‌کنید.» این بحران اقتصادی و گرسنگی، وحشتی مادی و روزمره را به زندگی مردم تزریق می ‌کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223814</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/661064" target="_blank">📅 14:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fee2527.mp4?token=MO-fxX_1zc48-rqk7TKTik92BBwerXjumc0BhwGeEkqVvyQfsIXvJrrF-Y_tkBGjBy96LQ2uCDVK9UXbfVVK72tZuoGsLvhLBcXv_a0jY2N195FVn8GS-BFcFy9u6Vqt1ic6btlzicePE8PnlOACuoOW9tXkrm-48ZydcWAAO_1Rqjwx-4h6ByRMryYnqj6Ia_35q2T3ln1Jv8EZ0Z3wRMEouOKTjrSO9ihgp1J6295RoXZG0usf2dyzxsECM2I4N5B1mVfK-f4KNc8pmpc21zqS7UuPxlBMZDkaaCulS865evRY2dKqyQNoFxwiUYcnhXqVvO1lXmEoFqI5ZhRY_6aO-zLWZeg-kfZnLtFF7zePyMHyOEzFJ9LDvUHyCj-DVutbjd4geU3Nyhoahb6z3GEln3n5Y7ePBmx-HKb6WmvE7mgdbvr-C7b9e48zTf1Y6aLOKEB9K7Hjxm8soqa8tqeOSoDv7Wwbyz4ZDX0G0_1aSIBvm8j3w9mDAEcJ8waLlNCeNPb8l8ZSwr5ByJACK0UhNo7AW-Bz9xjFx1SCo0FyN5MXe3rTdIxY4aKZh8CPl16HU5QLA5GZe7TT4biOj0UDJAVvZohBHRDv_VObuwEjWw18O85C5dEMHA8Ko1XZTZiEU-7Gyd4-RND_PXGSIEkCP5sFjX4AUA3HfzG0EgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fee2527.mp4?token=MO-fxX_1zc48-rqk7TKTik92BBwerXjumc0BhwGeEkqVvyQfsIXvJrrF-Y_tkBGjBy96LQ2uCDVK9UXbfVVK72tZuoGsLvhLBcXv_a0jY2N195FVn8GS-BFcFy9u6Vqt1ic6btlzicePE8PnlOACuoOW9tXkrm-48ZydcWAAO_1Rqjwx-4h6ByRMryYnqj6Ia_35q2T3ln1Jv8EZ0Z3wRMEouOKTjrSO9ihgp1J6295RoXZG0usf2dyzxsECM2I4N5B1mVfK-f4KNc8pmpc21zqS7UuPxlBMZDkaaCulS865evRY2dKqyQNoFxwiUYcnhXqVvO1lXmEoFqI5ZhRY_6aO-zLWZeg-kfZnLtFF7zePyMHyOEzFJ9LDvUHyCj-DVutbjd4geU3Nyhoahb6z3GEln3n5Y7ePBmx-HKb6WmvE7mgdbvr-C7b9e48zTf1Y6aLOKEB9K7Hjxm8soqa8tqeOSoDv7Wwbyz4ZDX0G0_1aSIBvm8j3w9mDAEcJ8waLlNCeNPb8l8ZSwr5ByJACK0UhNo7AW-Bz9xjFx1SCo0FyN5MXe3rTdIxY4aKZh8CPl16HU5QLA5GZe7TT4biOj0UDJAVvZohBHRDv_VObuwEjWw18O85C5dEMHA8Ko1XZTZiEU-7Gyd4-RND_PXGSIEkCP5sFjX4AUA3HfzG0EgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت هجدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای شاپور سعدی‌نژاد که به دلیل ایست قلبی به بیمارستان مراجعه کرده و در ۳ مرحله روح ایشان از جسم جدا شده و تمام اتفاقات درون بیمارستان را با جزئیات مشاهده کرده و بعد از احیا شدن صحت آن مشاهدات را با پزشکان می‌سنجند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: شاپور سعدی نژاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/661063" target="_blank">📅 14:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cc005a4a3.mp4?token=AGsnyr27EufTctX_MvTf_4RUsRS3ECw_-LC22_w__k92xRvxZEsI-OM3cMLRPAQGRFFZ0A98e5MaWbJA9EgLhFo_9B9tq4TVFknnUWmSxutqdiJkc8OUIXO76zcEx-Y9ZC-fZOm67KALGKTH5R3tztYISW58RDw9Px-jE9q0wDLC5Ncx1L5Kx0_4l7taDtfvSUbgaYUoNVMZB74hedvf7Y5yU91XuHh3unNgXmSYkun4N7Msbw1WtV7MC9EgNcIc8qXHLn9ak_adM9-f0QqozfBKJk-MaNG4PfVIa28WzMu6VAnKq3sVPGeLds9GhFoemhfpbOj3EPnMehA7FYvbvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cc005a4a3.mp4?token=AGsnyr27EufTctX_MvTf_4RUsRS3ECw_-LC22_w__k92xRvxZEsI-OM3cMLRPAQGRFFZ0A98e5MaWbJA9EgLhFo_9B9tq4TVFknnUWmSxutqdiJkc8OUIXO76zcEx-Y9ZC-fZOm67KALGKTH5R3tztYISW58RDw9Px-jE9q0wDLC5Ncx1L5Kx0_4l7taDtfvSUbgaYUoNVMZB74hedvf7Y5yU91XuHh3unNgXmSYkun4N7Msbw1WtV7MC9EgNcIc8qXHLn9ak_adM9-f0QqozfBKJk-MaNG4PfVIa28WzMu6VAnKq3sVPGeLds9GhFoemhfpbOj3EPnMehA7FYvbvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران مهیب آتشفشان در فیلیپین؛ قدرت طبیعت بار دیگر به نمایش درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/661062" target="_blank">📅 14:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91afaba5ca.mp4?token=vj2VDZwa5HRq04ssufHMc8VFZqbhY1B3IBbPRuoL4Re6ZMSPa8nVGMgY_zdpEOJu3Wv6p9qM95vfIPlbdrHqFIFGcNUWlGqxwuWe5LOWUsheIcm875vlDoGBbQUklug6dZ8d9uIk17ydabCIjLGDkk1U_M4Nl0NA7OglUbN4B0tN2-VXjZh9wNFsBtrMPAMRPbttZKqVW8FutE1UOeY39vunc_aj0XA32pdwrJ3XWbOa8GnE-XrdgiUgoSvBNvxzemFiEVwhWA5sn5m02uLsGQjRhvRxYONsLKr1jSdoQaFfXb1dyJ9p9_1QmQKc--je5uX8wfILcU_LlXUv5vPzmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91afaba5ca.mp4?token=vj2VDZwa5HRq04ssufHMc8VFZqbhY1B3IBbPRuoL4Re6ZMSPa8nVGMgY_zdpEOJu3Wv6p9qM95vfIPlbdrHqFIFGcNUWlGqxwuWe5LOWUsheIcm875vlDoGBbQUklug6dZ8d9uIk17ydabCIjLGDkk1U_M4Nl0NA7OglUbN4B0tN2-VXjZh9wNFsBtrMPAMRPbttZKqVW8FutE1UOeY39vunc_aj0XA32pdwrJ3XWbOa8GnE-XrdgiUgoSvBNvxzemFiEVwhWA5sn5m02uLsGQjRhvRxYONsLKr1jSdoQaFfXb1dyJ9p9_1QmQKc--je5uX8wfILcU_LlXUv5vPzmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت باهنر از پیام معنادار رهبر انقلاب به سید محمد خاتمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/661061" target="_blank">📅 13:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ژاپن: آخرین کشتی ما با هماهنگی ایران از خلیج فارس خارج شد.
🔹
پاکستان: هیچ مانعی برای شروع مذاکرات سوئیس وجود ندارد.
🔹
تانکر ترکرز: ایران در پنج روز گذشته حدود ۱۸ میلیون بشکه نفت خام صادر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/661060" target="_blank">📅 13:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ترامپ به اکسیوس: رابطه من با نتانیاهو خوب است، اما باید او را تا حدودی عاقل نگه داریم
🔹
اگر دخالت نمی‌کردم، اسرائیل نابود می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/661059" target="_blank">📅 13:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ترکیب تیم ملی ایران برای مسابقات جهانی کشتی مشخص شد
🔹
۵۷ کیلوگرم:
میلاد والی‌زاده
🔹
۶۱ کیلوگرم:
احمد محمدنژاد‌جواد
🔹
۶۵ کیلوگرم:
رحمان عموزاد
🔹
۷۴ کیلوگرم:
امیرمحمد یزدانی
🔹
۷۹ کیلوگرم:
محمد نخودی
🔹
۸۶ کیلوگرم:
کامران قاسم‌پور
🔹
۹۲ کیلوگرم:
امیرحسین فیروزپور
🔹
۹۷ کیلوگرم:
حسن یزدانی
🔹
۱۲۵ کیلوگرم:
امیرحسین زارع
🔹
مسابقات جهانی ۲ تا ۱۰ آبان در قزاقستان برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/661058" target="_blank">📅 13:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrrZu-r3IjgAt9A_3ro1LfUPjtOfjRB3GxqxVVfQpYQ5lm2nH4N8LWiU2B5avww1LtvVcTNoKkNsf-gvhzgQCfHhakNj625Wk5IlV8dKbcBNRh3-_rHcgSgkYA3kLW2CiK4kxlTFobirv6ZMYrCelQQ43HQRUXTLlP2EV37attr9QqckkKG30Ilrn5IYQr4Syjs5Rnz16mqSskPcV0ML6GcRH1q1rFCzTFx8TjN7hK28zGN7s22HBigQcygiqhPtbqjaljFKiQFfXPToDOaBXx6NEGYPY_z_KA2FwZpEn__UDhGgyV50--xPGdhNXTXjkK5URvpjyXz38d36r00FJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هدیه تهرانی در سلامت کامل است
یک منبع نزدیک به هدیه تهرانی:
🔹
خبر منتشرشده درباره وضعیت جسمانی این بازیگر صحت ندارد
🔹
او در سلامت کامل به سر می‌برد و هیچ‌گونه مشکل جدی جسمانی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/661057" target="_blank">📅 13:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ثبت‌نام در قرعه‌کشی ایران‌خودرو بدون نیاز به واریز پول/ تکمیل‌وجه تنها در صورت برنده شدن
🔹
اگر قصد شرکت در جدیدترین دوره قرعه‌کشی محصولات ایران‌خودرو که روز یکشنبه برگزار می شود را دارید، نیازی به واریز وجه، افتتاح حساب وکالتی یا مسدود کردن موجودی در حساب بانکی نیست.
🔹
متقاضیان در این مرحله فقط درخواست خرید ثبت می‌کنند.
🔹
پس از پایان مهلت ثبت‌نام در ساعت ۱۲ روز شنبه، فرآیند قرعه‌کشی روز یکشنبه انجام خواهد شد.
🔹
فقط افرادی که در فهرست منتخبین قرار بگیرند برای واریز وجه و عقد قرارداد فراخوان می‌شوند.
🔹
در این طرح محصولات خانواده ۲۰۷، تارا، دناپلاس، راناپلاس و سورن پلاس عرضه شده‌اند.
🔹
مهلت ثبت درخواست: تا ساعت ۱۲ روز شنبه ۳۰ خردادماه
🔹
ثبت درخواست:
ikcosales.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/661056" target="_blank">📅 13:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت پیشین در برنامه «وضعیت»: بعثت مردم یعنی مشارکت مردم در رهبری. رفراندوم در قانون اساسی به رسمیت شناخته شده است. برخی می‌خواهند مردم را پایین‌تر از خود نگه دارند تا حکومت کنند؛ قرآن مردمی را که فرعون‌پروری کنند، فاسق می‌داند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/661055" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cbd488c8.mp4?token=ehjrzwRDkXBePiTWDpIooAU4Q0u-yhZVj-tmpldLRHKRrbwkMeHgoJuwbs27aos2nlOUmgpRALtS_XAdpAxyKxuW868VE61ArbR2VhBsqrpfKz-JyH8R-8yhO877dlhPxttCyJNMSia5c56Uy8EnjINpDmI5pPta_ro5kpY0B4KzvIPw4l4BcKQhe63xDIn5SsJA-ZQsG6abXXhXcbFq0JRnhtAMcrgA7Teg1jX2BqXc-ST2WcB996PaAtdo5d4pPBDV6T_i67_M6u2uqsu8GWbdP6QbTlujooXOHMLXuBrNYRCvcsaSFBGNeqzScfe8qZ4GzwmE-R6UcCMVaqD5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cbd488c8.mp4?token=ehjrzwRDkXBePiTWDpIooAU4Q0u-yhZVj-tmpldLRHKRrbwkMeHgoJuwbs27aos2nlOUmgpRALtS_XAdpAxyKxuW868VE61ArbR2VhBsqrpfKz-JyH8R-8yhO877dlhPxttCyJNMSia5c56Uy8EnjINpDmI5pPta_ro5kpY0B4KzvIPw4l4BcKQhe63xDIn5SsJA-ZQsG6abXXhXcbFq0JRnhtAMcrgA7Teg1jX2BqXc-ST2WcB996PaAtdo5d4pPBDV6T_i67_M6u2uqsu8GWbdP6QbTlujooXOHMLXuBrNYRCvcsaSFBGNeqzScfe8qZ4GzwmE-R6UcCMVaqD5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایی شگفت‌انگیزتر از اهرام ثلاثه مصر!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/661054" target="_blank">📅 13:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای ارتش رژیم صهیونیستی: بیش از ۸۰ نقطه را در لبنان هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/661053" target="_blank">📅 13:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
فارس نوشت: یک دیپلمات آگاه از روند رایزنی‌ها اعلام کرد ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/661052" target="_blank">📅 12:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نشست امنیتی صهیونیست‌ها در واکنش به ضربات کاری مقاومت لبنان
🔹
وب سایت واللا به نقل از منابعی گزارش داد که فرماندهان امنیتی و نظامی رژیم صهیونیستی جلساتی برای بحث در مورد چگونگی پاسخ به حملات (تلافی جویانه) حزب الله آغاز کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/661051" target="_blank">📅 12:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
فارس نوشت: یک دیپلمات آگاه از روند رایزنی‌ها اعلام کرد ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/661050" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJugMewMsmZRqgBabj9sweSw5oj_MapDgVybULL0rhAhI90vM4iHBfpxFqYtsaI7FBRnxG8VXC68VAFsSUDyeV8dYRJ7F6pmkrLi0D_FldP3fc8nNfUA5r3jPn5r2-5Rf6ZTAiEgS2vNtfjDdr-ZkvJNNlV1J9vbNjNvRu7pYL-ATpT3Z-e0r4-u1paVwO-K2CMIWhiNhej4hCntECxguDwf31iiJ_hnED6vUj_ZdeTrvExAmQPorQFA43qgiOiGH3z5MjmVPqW6H06piGlmbR74wRWJZnRf9jPPNKSjsGvyx-drDusFTfiN9uGYu1XJ3tSyDn2cwB61FKog_1GHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
فقط تا
شنبه ۳۰  خرداد ماه
فرصت دارید
❗️
اگه بیمه شخص ثالث خودروی شما منقضی شده، الان بهترین زمان برای تمدیده
👇
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود! فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید
✔️
تا ۲ میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
#بخشودگی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/661049" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت سیزدهم در برنامه «وضعیت»: اگر آخوندی خارج از چارچوب حکومت از نظام انتقاد کند، به‌تدریج تریبون‌هایش را از او می‌گیرند؛ ما کاری کرده‌ایم که روحانیت مجیزگوی نظام باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/661048" target="_blank">📅 12:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e99d6354.mp4?token=vMkO-NHrElic5AYtr9qLfC3a2NiQCageUFO1WkYHfDwBn1lQS5zLuA0vXMKe76qFlTP8UJOeDuRFWGJKLoePiGZnMPJK-B014JQuNwsrKHOqiMUhoiOwJSh7iPyro5_4sS-MWML45Iv_lGVmgLOKi3O27pcaQS21_BYH1H5ixKOC0Tua5jlPwG5Xqq_YvdzyuN-5MSemLxxxrJUOoO4X7FVNJ0zDRnVl-e5RArcldWFtwi4MYyUCVVpXVL9p91IfKgVca7NazYDyRF8DtXjcBJNJnBCMDaoiVhH9H3vpodsME9VrMwVCS7t5qNMCc-jhAR5nfSFbJkDfcDuXm4UfCWH40tnW64kMhdbuv_fM_IHlsjLEJqcyWFDsT292WEnXJqLDyVSFrI0yl-6yUexXnLIMIu-ATuRlkXreZaa9oBUFrp4tO3lsxBXspv9s5Vzq5SbobS7Z9uW1Ejz98OiajO72LEWmfkef0zjU7gVLCUSnIFlO-5SjvBlvqd6YAfUJLS34WbDrYzFEA7L7NNFvH4vYeNnI7gvaUIsAEIxVc1UpR_gw1lmsmXkX3Idut8k_nXk6k7GhiER7AYDrPZnGfEi48TmRXMMYzOmJhDA33mSDR3Ru6_8teeTlyPpeeSlKQ0HpjVgSqSrEVow5Y8SQDRfzQ9XINVR_Us386AFY82Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e99d6354.mp4?token=vMkO-NHrElic5AYtr9qLfC3a2NiQCageUFO1WkYHfDwBn1lQS5zLuA0vXMKe76qFlTP8UJOeDuRFWGJKLoePiGZnMPJK-B014JQuNwsrKHOqiMUhoiOwJSh7iPyro5_4sS-MWML45Iv_lGVmgLOKi3O27pcaQS21_BYH1H5ixKOC0Tua5jlPwG5Xqq_YvdzyuN-5MSemLxxxrJUOoO4X7FVNJ0zDRnVl-e5RArcldWFtwi4MYyUCVVpXVL9p91IfKgVca7NazYDyRF8DtXjcBJNJnBCMDaoiVhH9H3vpodsME9VrMwVCS7t5qNMCc-jhAR5nfSFbJkDfcDuXm4UfCWH40tnW64kMhdbuv_fM_IHlsjLEJqcyWFDsT292WEnXJqLDyVSFrI0yl-6yUexXnLIMIu-ATuRlkXreZaa9oBUFrp4tO3lsxBXspv9s5Vzq5SbobS7Z9uW1Ejz98OiajO72LEWmfkef0zjU7gVLCUSnIFlO-5SjvBlvqd6YAfUJLS34WbDrYzFEA7L7NNFvH4vYeNnI7gvaUIsAEIxVc1UpR_gw1lmsmXkX3Idut8k_nXk6k7GhiER7AYDrPZnGfEi48TmRXMMYzOmJhDA33mSDR3Ru6_8teeTlyPpeeSlKQ0HpjVgSqSrEVow5Y8SQDRfzQ9XINVR_Us386AFY82Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناخن شکسته‌ای که مادر مینابی را به فرزندش رساند
🔹
روایت مادر شهید امین احمدزاده از نحوه شناسایی پیکر کودکش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/661047" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
معاون اول قوه قضاییه: در برخورد با همکاران دشمن در ایام جنگ ۱۲ روزه و جنگ رمضان کوتاه نیامدیم و قطعاً کوتاه نخواهیم آمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/661046" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66931f0591.mp4?token=YX5-7hklF1ftyDY3rAkEbNssqJVJ8u_RPAMbJy3kgiwOVzdwQMQq-OJKgICb0lPO_T1C4X83osTxVzeD1RvvJPajljZqcXy1pi4BPJdMGCpgVTKWjFn8m2U0a7HeE1tm3fS0DMMlOUZXSYW99PqXy9B-a3IVgN4JM4F5Ss1cQPTYE1Rwy-kUNOOr1mHMnc9rXB_MfO5YX-gsKbrmj5vWHToKrrLgsEGClOcBXNnFn70bJJxyZI36vvXLc8K_bJoddAu54hwdOXu5MyIBMj6w-oGBPuEixCvysbKpVf_nNWH6b4DYeNzeAOE1vENa_aZrQiLr0_FWlP0M_EJOCMPw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66931f0591.mp4?token=YX5-7hklF1ftyDY3rAkEbNssqJVJ8u_RPAMbJy3kgiwOVzdwQMQq-OJKgICb0lPO_T1C4X83osTxVzeD1RvvJPajljZqcXy1pi4BPJdMGCpgVTKWjFn8m2U0a7HeE1tm3fS0DMMlOUZXSYW99PqXy9B-a3IVgN4JM4F5Ss1cQPTYE1Rwy-kUNOOr1mHMnc9rXB_MfO5YX-gsKbrmj5vWHToKrrLgsEGClOcBXNnFn70bJJxyZI36vvXLc8K_bJoddAu54hwdOXu5MyIBMj6w-oGBPuEixCvysbKpVf_nNWH6b4DYeNzeAOE1vENa_aZrQiLr0_FWlP0M_EJOCMPw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
هم‌اکنون بعلبک لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/661045" target="_blank">📅 12:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تبلیغ این ۱۹ کالا ممنوع‌ اعلام شد
🔹
دولت فهرست ۱۹ کالاوخدمت آسیب‌رسان به سلامت در سال ۱۴۰۵ را اعلام کرد. تبلیغ این موارد در همه رسانه‌ها ممنوع است و تولید و واردات آن‌ها مشمول عوارض تا سقف ۱۰ درصد خواهد شد.
🔹
این فهرست شامل سوسیس و کالباس، پیتزا و ساندویچ، نوشابه‌های گازدار و انرژی‌زا، برخی نوشیدنی‌ها و سس‌ها، فرآورده‌های سرخ‌شده و حجیم‌شده، سیگار و محصولات دخانی، همچنین خدمات و محصولات مرتبط با تاتو، رنگ و کراتینه مو، کاشت ناخن و برنزه‌سازی پوست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/661044" target="_blank">📅 12:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48403a0d9.mp4?token=M8mj9XHNmdTYUeGyP-XT05jAooClr57xX5Njh3CSCcMp65QrqhxJ2hBeDPTUr128Q2XagVjSVrjWntXKoL0VNdNRvz9NlvHSD4SIqmUCwGXqOXVczDQArEbBVL2hfwh-vKavzpYkf0o1NM9tDs9h0uyUzhE1ik767zdbSIR8OWuapol1muOgOOvQ3MDGTKFd7R8CsKBf2UVuu8ps-thgcJatdziOMJYmXD8iis_-SLr0HGJ6Ihj7RwjfelT7Qc5U-ydYnnAwkMXDH2NwV_dj3_X7MdVj-ldQktC89sFhwmSQS_RfIyR-DFSSdmdYlnaxpQ3tRlP1l8ml99GiTi9A8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48403a0d9.mp4?token=M8mj9XHNmdTYUeGyP-XT05jAooClr57xX5Njh3CSCcMp65QrqhxJ2hBeDPTUr128Q2XagVjSVrjWntXKoL0VNdNRvz9NlvHSD4SIqmUCwGXqOXVczDQArEbBVL2hfwh-vKavzpYkf0o1NM9tDs9h0uyUzhE1ik767zdbSIR8OWuapol1muOgOOvQ3MDGTKFd7R8CsKBf2UVuu8ps-thgcJatdziOMJYmXD8iis_-SLr0HGJ6Ihj7RwjfelT7Qc5U-ydYnnAwkMXDH2NwV_dj3_X7MdVj-ldQktC89sFhwmSQS_RfIyR-DFSSdmdYlnaxpQ3tRlP1l8ml99GiTi9A8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل کاتس، وزیر جنگ اسرائیل درباره لبنان: «ما می‌رویم داخل، تخریب می‌کنیم و بیرون نمی‌رویم. این همان کاری است که الان در لبنان انجام می‌دهیم.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/661043" target="_blank">📅 12:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to3fF8SVRLbzA2XARPxVwq88AZk3Dy1qc0aefBmoas0CqCPtn0HQQvq9eMm8mKc1AOxsK0ifHPIwfsOX111lFu2PXzABWX_Dvcn3pixsjgdt3JGHSyjhEltgT5F9uVwrDHD6Oa5Q43aHBn_tuPdr7_CLO5LPwOuR6LgducDGMELfmwjGIT4Act0p9bF0OlhzMjVho7Arp9fVU9M8hqVNqEirZUaqxts63qoFVW8UwX5Q-LOha2aJqc4gEiizhkXxtVv4SmyjANOYdlrXJGadL8-eOkEy7pYGQzdYH077IV0KkY8uXguJV3zYcQo79YRBOeLFS7EwbfOjt7JZ3a_BcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هم‌اکنون بعلبک لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/661042" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: مرکز ملی پایش مصرف انرژی تشکیل و عملکرد استان‌ها برخط رصد شود.
🔹
شهباز شریف: از طرف ملت پاکستان در مراسم تشییع آیت‌الله خامنه‌ای شرکت خواهم کرد.
🔹
۲ شهید و ۳ زخمی در حمله هوایی رژیم اسرائیل به بعلبک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/661041" target="_blank">📅 12:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت رئیسی، در «وضعیت»: فضای مجازی آمده است تا انقلاب اسلامی را نجات دهد؛ اگر سکوهای خارجی وجود نداشتند، مردم نه با رذالت پهلوی آشنا می‌شدند و نه از مظلومیت مردم غزه آگاه می‌شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/661040" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تکذیب وخامت حال میرحسین موسوی  یکی از نزدیکان خانواده میرحسین موسوی:
🔹
او به‌دلیل سرماخوردگی و با توجه به سابقه آنژیوپلاستی قلب، برای مراقبت بیشتر در بیمارستان بستری شده است.
🔹
به گفته وی، حال موسوی خوب است و خبر وخامت وضعیت او صحت ندارد./ جماران
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/661039" target="_blank">📅 11:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مکرون: درباره توافق پرسش‌های زیادی وجود دارد و معتقدم که جنگ پایان نیافته است. نتانیاهو باید در ارتباط با لبنان «مسؤولیت‌پذیری» نشان دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/661038" target="_blank">📅 11:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حکم پرونده «کنسرت کاروانسرا» صادر شد؛ شلاق، ممنوع‌الخروجی و محرومیت هنری
🔹
پرستو احمدی و هشت نفر از عوامل «کنسرت کاروانسرا» به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای خلاف اخلاق در فضای مجازی» به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال محرومیت از فعالیت هنری محکوم شدند.
🔹
ویدئوی این کنسرت آذر ۱۴۰۳ در یوتیوب منتشر شده بود./ جماران
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/661036" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661035">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_wzokcaXGyuCGpODmPrVeaDypEGdXyNOJbNF8tcOTldvIDnX3NSLUXZakxmlpaYGTMdiBjeM2Vs9cIJAxl_tdF_40GQaRGnHcozdWJKovbWO359UTxqwn4Db8cx6Nwu9_g1Klow9qf9rJ4NjuNHrzmrbakpe-t-sxowvezCiUyJ-gKdj1E4N63Xq_hiCXxtquv4vf54QezZQC6MJrUFCdxPiEg7_Q666eIS3oxU83EtW-wXkQoxAFt9dGuaQJrFbd_i0clJPJn99x9eEaMz2O1Q0vdQ0BNhBvlLUbMniAoY26q80J1fzDfSCy6fZRx48wQ9rNJD16YjFL71j09azQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس: ایرانی‌ها مثل یک کشور عادی مذاکره می‌کنند؛ تبدیل ایران به لیبی به نفع آمریکا نیست
جی‌دی ونس:
🔹
تبدیل ایران به «لیبیِ دیگر» و یک دولت فرومانده، به نفع آمریکا نیست و مشخص نیست که بنیامین نتانیاهو نیز چنین هدفی داشته باشد./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/661035" target="_blank">📅 11:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZCEkirjWNFrwJitVzEgsjaDJu4ZU-ZZHMfkQF_8jMj0kD3dGr29uEdlChaNBC7aoCQGBiim_IgavwtzPR_ips459QcEmy4sElG3aAUoMByw1DHNWE19vwW6hGEcECXepfvWvaUznGI_mE0Mhpke8y7QxXNo_uDkeS4GV7pMSGG3Y-1sfTOGxogmQe4-9I8THpsPR2BDbfIZPn-XVts5By4jiH11KsyxgPOAC_FJ6L0Bhlcvqb741o35IlkgL4_IVUEO1nKjXW3otbUCvJjIzmj7bBnK4Og9Ov_x_3gi8tEwVIbiEcEkkEJfRBhZmXzUFuVZseSFbCT_nTi6ZNZgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر لغو مذاکرات نفت رو به بالای ۸۰ دلار برگرداند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/661034" target="_blank">📅 11:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
عزت‌اللّه ضرغامی، عضو شورای عالی فضای مجازی، در «وضعیت»: بر سر اینکه معتقد بودم باید برای حمایت از پلتفرم‌های داخلی، سکوهای خارجی محدود شوند، با حسن روحانی دعوا کردیم؛ به‌طوری که جلسات شورا تا شش ماه برگزار نشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/661032" target="_blank">📅 11:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
نرخ عوارض خروج از کشور ( ۱۴۰۵)
‌
🔹
سفر اول: ۹۰۰ هزار تومان
🔹
سفر دوم: ۱ میلیون و ۵۰۰ هزار تومان
🔹
سفر سوم و بیشتر: ۲ میلیون و ۲۰۰ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/661031" target="_blank">📅 11:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f3c87e16.mp4?token=LkTBE46T0dqBBwKq96LukXaWumARKBEZAytCoXhVO0_vZBqkvk_qcBowJo8KTuAkbW0SckBPPJqIz5VpVtMVRYPt1mhfwe9GksMK6fG41lPdhV3jKWAzfMD8Uvh83scwupi-fYRCloH2KH4xXTyM5Eyxsgr3Mdf8JzWYc5n2b_FY9KjcqpM2cyRS-iGBlgKyag9gaE5fAGtjEIQCVLTV0QarkDZ2l1h6-v-OpVq1m5fJtNnVPj27qXv-FRGnOgUweUnOV1EQpOMVzbNjaqzuT470MzjGf1VspkPCixn9oind3ujIhm54J4kBUlu0Pr7Tb3W9UxlsFeNd3-_7fQ-ing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f3c87e16.mp4?token=LkTBE46T0dqBBwKq96LukXaWumARKBEZAytCoXhVO0_vZBqkvk_qcBowJo8KTuAkbW0SckBPPJqIz5VpVtMVRYPt1mhfwe9GksMK6fG41lPdhV3jKWAzfMD8Uvh83scwupi-fYRCloH2KH4xXTyM5Eyxsgr3Mdf8JzWYc5n2b_FY9KjcqpM2cyRS-iGBlgKyag9gaE5fAGtjEIQCVLTV0QarkDZ2l1h6-v-OpVq1m5fJtNnVPj27qXv-FRGnOgUweUnOV1EQpOMVzbNjaqzuT470MzjGf1VspkPCixn9oind3ujIhm54J4kBUlu0Pr7Tb3W9UxlsFeNd3-_7fQ-ing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حالا وقت VAR است!
🔹
آمریکا و اسرائیل سال‌هاست از صلح، امنیت و حقوق بشر سخن می‌گویند اما دستشان به خون هزاران کودک در ایران، غزه و لبنان آغشته است. کودکانی که هرگز فرصت زندگی، بازی و رؤیاپردازی پیدا نکردند.
🔹
حالا وقت VAR است...
🔹
صحنه‌ها را دوباره ببینیم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/661030" target="_blank">📅 11:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
دونالد ترامپ در مراسمی هنگام تلاش برای نصب مدال افتخار بر یک کهنه‌سرباز، موفق نشد و در نهایت مدال را به گردن او انداخت
/جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/661028" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5867926d65.mp4?token=dnlOjZ-YNJSZkELWp95p8mlnmJke7kvGJ49GH-O-BrgG2FN2OCXKJSt0IvyPHoUco6wKgRB8f2kEWLVT4WRGZL-txdrS78V63S0yM8fwnYEFt1YIG6orUBjCRyhTfbIWmg8xWNg4Iuk2Svm1_XG-zx9u9DyF-ShlogCX1TUU05bkWiDvXmIOa7Me_CjQEfVlw64upv49dzpYgHmzXeAx7X2mi5xkCVuf0Yr77YwDE2hTbnHxEPiOUqSzATtJSMvVvWA4LIUtvzrKHqJCYxeOQzbqgYiunt_fN9Ld-aucFcCR9PfRhdogjiP4mSTO8PEonjbVohR_BnaSAlPCvfoR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5867926d65.mp4?token=dnlOjZ-YNJSZkELWp95p8mlnmJke7kvGJ49GH-O-BrgG2FN2OCXKJSt0IvyPHoUco6wKgRB8f2kEWLVT4WRGZL-txdrS78V63S0yM8fwnYEFt1YIG6orUBjCRyhTfbIWmg8xWNg4Iuk2Svm1_XG-zx9u9DyF-ShlogCX1TUU05bkWiDvXmIOa7Me_CjQEfVlw64upv49dzpYgHmzXeAx7X2mi5xkCVuf0Yr77YwDE2hTbnHxEPiOUqSzATtJSMvVvWA4LIUtvzrKHqJCYxeOQzbqgYiunt_fN9Ld-aucFcCR9PfRhdogjiP4mSTO8PEonjbVohR_BnaSAlPCvfoR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی روسیه به تاسیسات انرژی مهم مرتبط با نیروهای مسلح اوکراین
🔹
وزارت دفاع روسیه با انتشار ویدئویی اعلام کرد که نیروهای روسی یکی از تاسیسات انرژی مهم مرتبط با نیروهای مسلح اوکراین را در منطقه خارکف با استفاده از پهپادهای "گران" هدف قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/661027" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408e952ef4.mp4?token=iFHFnUYYoYTRDHAlLmeL2yDdsMZOu40uZn1T9fPmCTcTCE13RidN3tnO4QnWeMBv9bMWyQf9aZG7PcC6_hK8py5YMQhXzrGBVNeaJTOcIcFVFfkFxdwfTv3ba7aJC-d0PfxyRNJ0-tbqmDvFuhppUcUFai9ZDmPZ5CtS9VPlnwA-i_McKU82BmRTgK2JCq91DYPd77qypdmtjjmXWWQ_jG0CQbtzMSi13erS-i--X_B0XbY4YBiclI2LeFlmW97_VpdubnYm2UD-BDpd6PEe71qoxwRiWyDiFseXMWKlUQVPjPRoBGfNAJ2_dRm2V_wCXrolzexAdT_Hw8Yu1TiVyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408e952ef4.mp4?token=iFHFnUYYoYTRDHAlLmeL2yDdsMZOu40uZn1T9fPmCTcTCE13RidN3tnO4QnWeMBv9bMWyQf9aZG7PcC6_hK8py5YMQhXzrGBVNeaJTOcIcFVFfkFxdwfTv3ba7aJC-d0PfxyRNJ0-tbqmDvFuhppUcUFai9ZDmPZ5CtS9VPlnwA-i_McKU82BmRTgK2JCq91DYPd77qypdmtjjmXWWQ_jG0CQbtzMSi13erS-i--X_B0XbY4YBiclI2LeFlmW97_VpdubnYm2UD-BDpd6PEe71qoxwRiWyDiFseXMWKlUQVPjPRoBGfNAJ2_dRm2V_wCXrolzexAdT_Hw8Yu1TiVyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جوجه‌فلامینگو‌های دریاچه مهارلو، فارس
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/661026" target="_blank">📅 10:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic57Yd50ki1J5SeUSan1HtPOlfAJ4UVJvpCMIHP3S4P6AyOd5pB-fumSa7Rfh312yRzhXLQbc8SlgBZ65K62WXjnEu-HXf93Gc8at_RtasaQTE6c6u1Irw1vLa2fQmR0HZFwdB63FC6PHJWi7-hyMBND4dvd7L-rkn-Mjd64sBt_RwhXMF5Surew0eJjb_u3sQPLqePxNML-Y-sB0UCHDARj04uvb8JWZfV0tao7JwQit46XwOLMbZ_DjF2ALS7lAa2WuT1duKXGuz8Rq_bZSJvNzRhlMfdtGpsJqgiOxJNvgUuvVf8NQN2ROs_ZrhRqzjayZy8ylGC8qIrruNNkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات دفتر رئیس‌جمهور: بدخواهان و یاوه‌گویان خارجی و بعضاً داخلی که از پیام رهبر انقلاب برداشت به اختلاف میان ارکان اصلی نظام کرده‌اند، آب در هاون می‌کوبند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/661025" target="_blank">📅 10:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDDCq-HhqfYrndlSXb-DF4HcRfOSIfd2odCVOzvAi41cw4TyP8ry5UurCsUllImwXp03ZVhkVJQ6cup0SJ91LBqfgqHjXykAx8pKB7YYzRyJfno1PQyqkIINk-FAW9JQNsx8V4Y3SpHKJz7917XeJVe3LNQXzU3QpO2kO6M68NrPGydHpm9JVpiVuDPhwJicskgFSziatHEgn_NO_pq-atFKOz_vzpdNo8ZLyd_W104vv8sNVbJX3qWP4XAcjus1LeEDQ0ySTDnlgIEEtwp2QY3XiM-XWzkQs6ISU3eHGgaScUtd5SNhaCRU41zpfXY395-QYSTbQ6dv4wbu3dzbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت جام جهانی فوتبال ۲۰۲۶
🔹
همراهان گرامی خبرفوری؛ برای حضور در این پویش کافی‌ست یک پیام صوتی ۱۵ ثانیه‌ای ارسال کرده و پیش‌بینی خود را درباره دیدار ایران و بلژیک با ما به اشتراک بگذارید.
🔸
نتیجه مسابقه چه خواهد بود؟ پیروزی، تساوی یا شکست؟
🔸
نتیجه دقیق بازی چند چند می‌شود؟
🔸
گلزنان احتمالی تیم ملی ایران را حدس بزنید.
🔸
لطفاً در ابتدای پیام صوتی، نام و شهر خود را اعلام کنید.
🔸
پیام صوتی خود را به آیدی ما ارسال کنید
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/661019" target="_blank">📅 10:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تصویری که ترامپ همزمان با لغو سفر ونس به سوئیس منتشر کرد
🔹
همزمان با اعلام لغو سفر «جی دی ونس» به سوئیس ترامپ تصویری از امضای یادداشت تفاهم با ایران را در حساب کاربری خودش در تروث‌سوشال منتشر کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/661018" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
بیانیه سپاه پاسداران اتقلاب اسلامی: ملت عزیز و رزمندگان اسلام چون کوه استوار پشتوانه دولتمردان خود هستند
🔹
اینک که دشمن متجاوز در میدان جنگ شکست خورده است و و در مقابل عظمت ملت ما زانو زده است، انتظار همه ملت و رزمندگان این است، عرصه سیاست‌ورزی نیز امتداد آن میدان شکوهمند باشد و به احقاق حقوق ملت سربلند ایران بیانجامد.
🔹
ملت عزیز و رزمندگان اسلام چون کوه استوار پشتوانه دولتمردان خود هستند و اگر دشمن عهد شکن بخواهد به زیاده‌خواهی ها و تضییع حقوق ملت ایران روی آورد، پاسداران انقلاب اسلامی آماده‌اند تا با کوچکترین اشاره آن فرمانده شجاع و حکیم شکست تاریخی بسیار بزرگتری را به آنان تحمیل کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/661017" target="_blank">📅 10:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920c65dfbb.mp4?token=UeSvGr07HBDIkDRL9-XqWlY-rqIkPt1WB4J1J4C2pcDAH-nOB7XVYfobLMtBG2PMOqfcguUuvl5HHFipNsqHX79aLDM4BnFiiV9gv7QZIjMDazqHeK3P9G4CXtlP-DGOfWaysPtgpIRXoDDXAJWuBp14I8ZEEdOsV2FyEVeaXl0k5duXFmXTUE5LWm3JgDsyKSUfG_TipBXycXZEhtjyno4SMDozBX68PNSID37QiypGW82WIc66z721bhdalxys4MlCKXjivbIef_z6bYfZ9zAt8sRY9dQdnJKeddcAKymC7n1ooXHWBWm9iABWJ7HQMMrCGo9lAoWaoxJ8FU322Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920c65dfbb.mp4?token=UeSvGr07HBDIkDRL9-XqWlY-rqIkPt1WB4J1J4C2pcDAH-nOB7XVYfobLMtBG2PMOqfcguUuvl5HHFipNsqHX79aLDM4BnFiiV9gv7QZIjMDazqHeK3P9G4CXtlP-DGOfWaysPtgpIRXoDDXAJWuBp14I8ZEEdOsV2FyEVeaXl0k5duXFmXTUE5LWm3JgDsyKSUfG_TipBXycXZEhtjyno4SMDozBX68PNSID37QiypGW82WIc66z721bhdalxys4MlCKXjivbIef_z6bYfZ9zAt8sRY9dQdnJKeddcAKymC7n1ooXHWBWm9iABWJ7HQMMrCGo9lAoWaoxJ8FU322Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی‌ها می‌پرسن چطوری کوکو سیب‌زمینی اینقدر پف می‌کنه و ترد میشه؟ رازش فقط چند تا نکته کوچیکه که خیلیا بهش دقت نمی‌کنن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/661016" target="_blank">📅 10:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
مخالفت آمریکایی‌ها با سفر ایران به آمریکا ۲ روز قبل از بازی با بلژیک
فدراسیون فوتبال ایران:
🔹
قرار بود تیم ملی برای دستیابی ملی‌پوشان به بهترین شرایط فنی و بدنی، دو روز پیش از هر مسابقه راهی شهر میزبان شود؛ اما در آستانه بازی دوم مقابل بلژیک با وجود دلایل فنی ارائه‌شده، این درخواست مورد موافقت قرار نگرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/661013" target="_blank">📅 10:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2IQg6CbUsDGDgMFz2SGHJrlMfgYTjUxgU2K2Tyuqdfmr1zJuiJFVY4WZkWmPbvpSkMt3n4mSz0s7FjXG6CCHSReO467ILzLdocT4fxNEJT9KNp2hsPNYzt2sa4YisBxkDC2dOugNWru5L8MTK-CM2i6mB_cRCgapykMOv1wLRs20l4xDt_Ic6bCmo0_OeaEwyLmJU27vXvI4f3dCfsB0rsVJn46oRUMuybbEHEKx_y0fvmdElAp-auogAZYRMOCpRSm64B61F8mrdajhzS26IdEGUqM1-nQ4kmeoziy4ItNsFRmiweQLfzrcP9ow8vDcePcrsx5_R2nAzxxX7Rycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر منتشرشده از محمد محبی فاقد اصالت و اعتبار است
فدراسیون فوتبال:
🔹
در پی انتشار تصاویری منتسب به محمد محبی در برخی شبکه‌های اجتماعی، به اطلاع می‌رساند تصاویر مذکور کاملاً جعلی بوده و با استفاده از ابزارهای هوش مصنوعی و تکنیک‌های دستکاری دیجیتال تولید شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/661012" target="_blank">📅 10:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCre3EnlszvUViFhfq3Hdz9JdWvJhlLcuu2V-kVT_w_8cWpvX21TT5wT_0LQs4YaVlfEhskITvaEXSwSqmNSXEYgdVFL1wp1B5qTVhi6P7nCDwbdggntXGns28t2KsXPb1gUHsJsdP6wjgyBX5IvY5LfFH23tNpw_CO9IP-xdVf2PePRnBZMt8VdQfoMS7fZ102CFLgpvScFJsAAYIPva4NXyujvfSH6_iKzYqn0Sb_hG2PP9nMu-A1_gd5aoI2b609GmSthcmGNbXuORyv5q6FR7Rwd8kQgiaeeR5ZY2t5q0QNja1rnbAuH8WEUhl4yOKy-t69VGr5gYgeUKGsM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن‌گویر خطاب به معاون ترامپ: هر کس به ما پشت کند زیان خواهد دید   وزیر امنیت داخلی رژیم صهیونیستی:
🔹
هر کس از ما حمایت کند، سود خواهد برد و هر کس به ما پشت کند، زیان خواهد دید؛ بنابراین ما را تهدید نکنید.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/661011" target="_blank">📅 09:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6572c6674a.mp4?token=fthA14aDBeXQig_HR6MYV1Wk0DwUx38r560vBWj64uQ6QGRBWtIdVTjsttLcti5yq70A3s9wTKl-af4ZIT7vMtn7hw9QH3Ium3y_RPzeCfKv6i6s-tzBhFLxTziYdNhptN6C4Yqc68DTf4lOr6eCWIVizpstvVAf75d8HnSQCeF9MCc97aPt8zGMc4VHSI0l2m_TNCbudiVbEzGfDCPWKE191fP580_VTFpjbeqYwyzyg43gfYoCNZUvkva3Ipx1QrLEaYjD6ObCHZ13ZPCwOfqkKLEFGJVDYUyK_oYWfFlVJlfxtvlKqrqHykrndnRQeczJOD4t3Lhh6y54LckgDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6572c6674a.mp4?token=fthA14aDBeXQig_HR6MYV1Wk0DwUx38r560vBWj64uQ6QGRBWtIdVTjsttLcti5yq70A3s9wTKl-af4ZIT7vMtn7hw9QH3Ium3y_RPzeCfKv6i6s-tzBhFLxTziYdNhptN6C4Yqc68DTf4lOr6eCWIVizpstvVAf75d8HnSQCeF9MCc97aPt8zGMc4VHSI0l2m_TNCbudiVbEzGfDCPWKE191fP580_VTFpjbeqYwyzyg43gfYoCNZUvkva3Ipx1QrLEaYjD6ObCHZ13ZPCwOfqkKLEFGJVDYUyK_oYWfFlVJlfxtvlKqrqHykrndnRQeczJOD4t3Lhh6y54LckgDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشویق وایکینگی هواداران نروژ در شبکه‌های اجتماعی بین‌الملل ترند شد #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/661010" target="_blank">📅 09:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkdPEDgzqqpZX4HeTojkDICv4nRyTQ9GdLQqjP6ZSR5WOQ9clI-IngtiEcrmUrU_Nu9yZGCf3hHs7xWyJ35GPk0_CFbZOIO8wYpx4xFSf8WMULV_7lo0Q6i1DttFiT74gsrh_AuEZ3HaDSulyHhQHXEbYnyO9LmDgSFa06iM1jwtvYvfVT48lzLkwLcQIFEdvjkIzrb_haG6_TkN8gKoFgjgB-vsfVGtJIBd-5n6bKroiXzcVfBtNi55ozdS68O445qrlQtevY53kT5PIFfM3sC-EGq4fPOgNmw5yhU_QuT7TpeuDH_4b3T9_ySY9q6p0-DDkgsqePmoBgoIye1Jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوئیس: گفت‌وگوهای میان ایالات متحده و ایران که قرار بود امروز برگزار شود، لغو شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/661009" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661007">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d057c139.mp4?token=WMAbVb4X2JQ1Unq5FHzIfnY2Sebw15Yk0PO5ZD9JxmMx7yKmAW8RN5nkXcSGg5Aj2lhTk7nSNAE_MyvVNvI3vgohhoU4C42fyaO9DkOSviGV-vz1iSFVeXHZEkO_GdfS7psjidesi7pIKIZfI9FU4T0HMkbjodX0dfIDKMmo9N2CAM0Dl9WsRhdB9MBfNQhjy1JCexYYP88Vzw8IvVeOH76dIsPS3yaxdzGgpB5CsKt5nUUs4Cl7tKIGvw6_9Sq3P5t0IdaqzYYvnF0b11fyJtvsZ2gmaanrUi9Sb0yL7V_KnUH0LB-veQQPyzBDMGBX_XxUmSm-wDTZOKbYI8An6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d057c139.mp4?token=WMAbVb4X2JQ1Unq5FHzIfnY2Sebw15Yk0PO5ZD9JxmMx7yKmAW8RN5nkXcSGg5Aj2lhTk7nSNAE_MyvVNvI3vgohhoU4C42fyaO9DkOSviGV-vz1iSFVeXHZEkO_GdfS7psjidesi7pIKIZfI9FU4T0HMkbjodX0dfIDKMmo9N2CAM0Dl9WsRhdB9MBfNQhjy1JCexYYP88Vzw8IvVeOH76dIsPS3yaxdzGgpB5CsKt5nUUs4Cl7tKIGvw6_9Sq3P5t0IdaqzYYvnF0b11fyJtvsZ2gmaanrUi9Sb0yL7V_KnUH0LB-veQQPyzBDMGBX_XxUmSm-wDTZOKbYI8An6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قابلیت جدید
اینستاگرام؛ برای هر اسلاید پست‌ها کپشن جداگانه بنویسید
!
🔹
اکنون کاربران می‌توانند با فعال‌سازی یک گزینه، برای هر عکس به‌صورت مجزا متن بنویسند. این ویژگی در‌حال عرضه است و به‌زودی برای همه فعال می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/661007" target="_blank">📅 09:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661002">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/661002" target="_blank">📅 09:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661001">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVxrRDSubXnyjvE1BoSdENJDFMDXO-W9Zd5-ki2eYPJYgxQ_c2Yvz-s4tnu7Ox9Qq3JN0dRFZlncOj5ILR27J7B5nCRDKSuZFGu4b05FsPeXsHwW8xf7pjm8QNEVrwPKhXdAx6KEUOGiD8qATMZEXTy7j4jkn7U0FGYSOI6y7HbmxFYpqr4sWJuhMhx5ThDm_KMo9Gm7Hoh6V1VAsIb0u9iJPvzJ7liUt6mMfPD9Co1I34YNq3hFW4VhoxIPLDf3qX8OY5GGMMAQyULAssbINAop3tU_enhEFB6dhkeCFeq6PaKVW5E2bdO6rPsIZ30M7ireSkLbo_bQ4Qn3hcrYLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام خصمانه ایکس علیه معاون حقوقی و بین‌الملل وزارت امور خارجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/661001" target="_blank">📅 09:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661000">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd2c324c23.mp4?token=LsxDjEN0JMWV_BFvr7BB5G2bHKKsudRiOb6LjaauJzMc_G4seMQgQDe66vwK-BYQ-on2TFDM2KEW9-_pAw5atb6eUMWb_35WX25UZOE2J6MrSNG_oLfwsCWqmSoKSnZWI3uo3nPLtkVBRXsB_8RT9fciNfLBzWB-Sg9kjmzae2neLqQ6PQ3u_P7GJyYWSPACTr3owbbyU3wHiqvtVMXtFAsq6tl4M5kIE73QejV1-UY6zWS7-lToCqRnjHgYFRO2jK9-X0N4Vi7mh0woZq1_yAoedQMSZN_N_ecXPwXq-EpvBNQ4YIfx0SO4VRJnWfPc6ppqOdNbQN3nkYKJ8sAl2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd2c324c23.mp4?token=LsxDjEN0JMWV_BFvr7BB5G2bHKKsudRiOb6LjaauJzMc_G4seMQgQDe66vwK-BYQ-on2TFDM2KEW9-_pAw5atb6eUMWb_35WX25UZOE2J6MrSNG_oLfwsCWqmSoKSnZWI3uo3nPLtkVBRXsB_8RT9fciNfLBzWB-Sg9kjmzae2neLqQ6PQ3u_P7GJyYWSPACTr3owbbyU3wHiqvtVMXtFAsq6tl4M5kIE73QejV1-UY6zWS7-lToCqRnjHgYFRO2jK9-X0N4Vi7mh0woZq1_yAoedQMSZN_N_ecXPwXq-EpvBNQ4YIfx0SO4VRJnWfPc6ppqOdNbQN3nkYKJ8sAl2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نسخه ترامپ‌تر از ترامپ پیدا شد! تقلید لوئیس مک‌لئود از ترامپ پر بازدیدترین ویدئو این روزهای فضای مجازی
شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/661000" target="_blank">📅 09:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660999">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYOIyjf2E1PlJcuRCAzCJPNGZm0dgOOL2kgHCL_BmDgrK-36ryWUXegfCfskqKjvMErgAEgnkZsFkjqUYGQj3a-CWoCCy3awdSzP1eVO1rth0RjXupzmHqQzTeMltmqb5T6Iz-OuDQcv-GnQBO0pZ9W6UhaubU0XrQ3WYh1wc45KgByGWgx79u3i97elUh81gMH3NirxDoAYAQdoiy2V1_6P5uEFzfJe7fo0r0KpkplcSISVFhSN0zTjICbBNiegsSvjTANMQ78Nw3XYcCXQqIM-oBE_Y41elSyZYbUHCYGdCFl65lDFTqhQv_IjMWRkuJgt4R9cEf22R9c8Y8YyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/660999" target="_blank">📅 09:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660997">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aexFo_sLR_IvY0CNMWO2Mhg8jYeQzHJzzRBVcDwBujOWMCdxVbq1Aan0lMy9Qf69D3lG7d_-y0MC9N_3plGM9R1yOqhB2Cd2sFyAIweAtTmllRZHT_Pm3AOJuGX3ioYLtBpt7l-gc4xcC0HdyikJa3dqQa7zmRu2K7L4FpfiSSjj_JXg0D64SfJFwyExU5LFyZjfvtc2MoA9Wl-T6rGPQs_f0_UQfBL8qecLy62DuDGcvDUjT2m8QMu8_fOillDpB844ZzDE_HyZtxlV2YLrbjEJeYph-P7vCiNo09--fxkmhDzrH7uEZp2lw3yilvt6bLlFIKEFukDE4_ZRXe6rzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عقب‌نشینی تل‌آویو در پی هشدارهای ونس
🔹
در پی هشدارهای «جی دی ونس» معاون رئیس جمهوری آمریکا به مقامات اسرائیلی درباره توافق با ایران، سفیر اسرائیل در سازمان ملل ادعا کرد که تل آویو به «دونالد ترامپ» رئیس جمهوری ایالات متحده اعتماد دارد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/660997" target="_blank">📅 08:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtD_qLhdA4nQfwjEHYQBh9_UqZSIw5dZ30loJmGZWo6LbxnO0ZEUiiVxexX3XkCXGJSfs62w7uzrmy6blIXhPM75HquM-jvJswNxDVMfzulkDI87cnahBMNyHXov2WmJBJNLTGPaI-w4Oqssmxa4PjNNBUEw8Z9Z2FFVA8yvHtWUmdYeql0c09G7H5hR0vFipPzNBWyfSqZm1N7xgeHPI7AwZ6oZFylH1EwPlLAeK2w4bNsvBTDMxSfaDZwEAvf6RlDrvYmC7h9H8Vzr6td5N-LBi2b9tlRHV69qR47yNQ1mhrOlAarQxgx1Ale01bDMrN3zdSL9fREHQ2O9kGT9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار عجیب جام جهانی/ مالکیت توپ بیشتر نتیجه بدتر!
🔹
پنج تیمی که بیشترین مالکیت توپ را در هفته نخست جام جهانی ۲۰۲۶ داشتند، پرتغال، اسپانیا ، ترکیه، سوئیس و اروگوئه، هیچ‌کدام نتوانستند بازی افتتاحیه خود را ببرند.
🔹
این پنج تیم در مجموع ۱۱۷ شوت زدند، اما تنها ۳ گل به ثمر رساندند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/660995" target="_blank">📅 08:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660991">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krLa8tRTiCCCHsM-A3EOZ6pA3xCCEhM4XEIBueNUehZ38piY_iP4D7s9fUEJCdDV0LSydp88Y0LZklc12E1lS405AewsAaNy4I5lEaxVE4x6My87C3q463UEnAkew0i2Ht3scKuVAqCcF2gYa54BRwsMZomymrca4UQVRmZNzfK-T7SnBzQ_Ab7kAbOn9S0hd-tCVavq2jZYD3zo9z8K0QG-UNwVGwORQ-ph6rQgTh0bIrA5riif_ogtVgB9mJdOTIfJGvImL2U4TGExa9wJf_blfvLTybSN5soO6Z8AZ-YuWGf32dHl6GzjlzBPy7C_qf4PbJ1j8O3R5Dj06mjsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/660991" target="_blank">📅 08:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660989">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
کانال‌های تلگرامی صهیونیستی: «برای نجات جان سربازان اسرائیل در جنوب لبنان دعا کنید»
🔹
رسانه‌های عبری از وقوع تلفات گسترده برای نظامیان اشغالگر در حملات حزب‌الله خبر می‌دهند. آمار تلفات همچنان تحت سانسور ارتش صهیوینستی قرار دارد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/660989" target="_blank">📅 08:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660988">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سوئیس: گفت‌وگوهای میان ایالات متحده و ایران که قرار بود امروز برگزار شود، لغو شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/660988" target="_blank">📅 08:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660987">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGeCShDkYfSPL_swNg0vEAOIfBF7BejKJrKR3SehSHRRu8NJvezekQskUbMJWUuqpxHL_BGeKXdD6YR117RnF92OJyFpbMtM0Sr2hLYJY9-wAgdx7nOkQHkTkyIkaa0dO8WLSSt-Vu1sypmOksSfuSWsijVioNQNle0Q5OpH1H5AOhXb4CIhZDNgTdsOas0cdY2tflBtpYeSNHaws9K8SAZqQL6xWVMpl1zu_2qbacUGUhO0TSu3Hj71LpJcxX5d8oF24mbDQfRH_WddVlQjG-6EKtkRaZDdhoy5yH82fgwJLDRM5Psuwomr_nj6q2FDZ_LV4QDNNBJ8phlreQrpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال‌های تلگرامی صهیونیستی: «برای نجات جان سربازان اسرائیل در جنوب لبنان دعا کنید
»
🔹
رسانه‌های عبری از وقوع تلفات گسترده برای نظامیان اشغالگر در حملات حزب‌الله خبر می‌دهند. آمار تلفات همچنان تحت سانسور ارتش صهیوینستی قرار دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/660987" target="_blank">📅 08:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660984">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7Fj7ropIX3eZkVcBRtT8-cp6EI0F5Ur7N1LGBd-t3FvzOLLfZ1e64kKGQ7YmPDFAKRc3ttYWqYQl_fYlDEfP0WSF28tU-xLrkVEg60O5zcx5xZcW4nyK14TGbpHdOWWYnR-yjyWACVn59LesRQ_XR6vTnAyCgVnDncsLf5Ns5kXSCPvcc85geDQyH7c2VQPa_Oy7x28qF7RciJuJB6S7KPXgZP5Mw47fDEEljtarhuwbVleMw2tKLXK_eWAbwOCjNe0w7lPppjBxa2JLMWJ_NahqWnViPRvVcFRXUfzvDND4QbdlSyyo2pSl0ZotChKYGMLolCrbSkUSuzn13I0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh_mpzYbXfDk-9h1W_XOE1uFZ-ZySpQFB-L10mmPuSig4Ea7zLLPkqaKTxjalkE4l_BtfqVSmn-o4MRN_DecUc5bOWMrwfEgE9Blg_vg1mt830GgPLUXEKGEv7j-0K_q_JNC59LcmZv4QWIIi-ODbGqKQ1psSZC8z-sK4qJPWTh-fhMNXGq6P2Ai9YlpuTryn2ag43DpVr-jQuRlz8S3x_mhfOXUaX76iY-dlqvTdyQrSFMu8VzoY1iWnrPFT7GFD08KKoUlLKxxLegavmfeZHMJdwTMvsnqaOOD9t0jUQV_0GnnkaZXCoGVGMhBuoLgk9_42kLS7mOX073YmsDN7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/923742a447.mp4?token=P9WbcBJbHTXQptaG4RUH8HhX60tZS3qHIZDYK1eTqj1rI5JFtS5bQa17XJbbRdjhV3Aj-DLO865PJ2wEoabadv3ZTFvzgLh6eRp5UUIVGsKpv7l6JJPBLs4GzRc9h8iNbTLob2SU6mYxTlvlpvtVsIA0aZ1az8U8myut4Sgd1cWkLJugvJl7RKJ3xCo7cDK0AYOKK9u55bbLAla9u5jhmUCkWGpe6CmF_6m9puz-X6ErumUSrZQs5bOByJ8TFx8nBxIS0k5oLwXvUsUTV0wPafPUe3MkaPOxPscul1dpkSoP_b9YBJWQOOB1nuByCNCvyr9EscmXPd1U6c_yrQfUdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/923742a447.mp4?token=P9WbcBJbHTXQptaG4RUH8HhX60tZS3qHIZDYK1eTqj1rI5JFtS5bQa17XJbbRdjhV3Aj-DLO865PJ2wEoabadv3ZTFvzgLh6eRp5UUIVGsKpv7l6JJPBLs4GzRc9h8iNbTLob2SU6mYxTlvlpvtVsIA0aZ1az8U8myut4Sgd1cWkLJugvJl7RKJ3xCo7cDK0AYOKK9u55bbLAla9u5jhmUCkWGpe6CmF_6m9puz-X6ErumUSrZQs5bOByJ8TFx8nBxIS0k5oLwXvUsUTV0wPafPUe3MkaPOxPscul1dpkSoP_b9YBJWQOOB1nuByCNCvyr9EscmXPd1U6c_yrQfUdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه حملات شدید هوایی و توپخانه‌ای اسرائیل به جنوب لبنان
🔹
همزمان با پاتک شدید رزمندگان حزب الله به نظامیان اشغالگر، جنگنده‌های اسرائیلی مناطقی در جنوب لبنان از جمله استان النبطیه را هدف حملات هوایی قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/660984" target="_blank">📅 08:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660983">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO7gxytpxjWlEX65xE-n3Ez0P0YmwFuEpHZDdbiAT8zJwLOuZoTXTOVkik6HOe3o2EMPmWDjnWlWv6RfygIuTYU2KNYtC8jau5a9HwJ-egXA56ALU4G4kUgk7CzYip3zJHjyFHnu-Mg2qTW6busGBnLGzTL9ZMC4UCHc_2fRxw4Tt6J3w3SmYKZap-xiyXg3TPTS3RJGfZaNx3z1072fJvqmftrKwm6zm9pcQHGih0t_54w-7wyOoM-VKM1SQ329ptbNwmVY1Fx1d_gfsH36JrxSWOhWScJ7RE8nRGq1M9f6MYkP4-VfrRoPdQ_A9nhQ0yRSFFCstYwNp8Q1VInBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در واکنش به پیام مقام معظم رهبری: گوش به فرمانیم/ اگر بخواهند دوباره همان مسیر را بروند سیلی محکم‌تری خواهند خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/660983" target="_blank">📅 08:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660982">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
عقب‌نشینی انگلیس از مداخله در تنگه هرمز/ کوپر: مین‌روبی برعهده ایران است
🔹
وزیر امور خارجه انگلیس در اظهاراتی که از عقب‌نشینی لندن از مداخله مستقیم در تنگه هرمز حکایت دارد، مسئولیت مین‌روبی این آبراه را برعهده ایران دانست و نقش نیروهای انگلیسی را به ارائه حمایت احتمالی محدود کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/660982" target="_blank">📅 07:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660981">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ترامپ: از اسرائیل در صورت حمله به ایران دفاع می‌کنیم
ترامپ، در مصاحبه با کانال ۱۴ تلویزیون رژیم صهیونیستی:
🔹
چنانچه اسرائیل تصمیم بگیرد به صورت مستقل به ایران حمله کند ایالات متحده «قطعاً» از آن حمایت خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/660981" target="_blank">📅 07:36 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
