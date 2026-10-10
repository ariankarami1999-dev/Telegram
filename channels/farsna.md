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
<img src="https://cdn4.telesco.pe/file/jnf4tpVuUsnUQFVu6JShczmXpIGXudOhGoAhkuqF7oTInQ43GtsEtKoKHZPZxMQiU_JYqxc4pWISiWx4s16Gy_h3RbtMz3hnXwxyj2CTu_XX7Jj8dgMmSdp46Zpl2vP1URq_lJzY4yz9LqVBKU0fuPmkQPBrltDvOY_uc1LGLzjTLrh9Xpzn_wDH9gzwjkTzMtehrY8w5sNXim2OqPuSimwjB98t6LBwOxW5vfDXP2TmryZ--4P7rgbW_wyTJxHGsGDAWjPmeZEVyaGHCmaAHkhC8HwcEc8bcVdQ3aDtJfM5adjT1wBwLgcoxJ8EMnxR2CwYRekp4mOn7eeePZ1BzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 09:36:53</div>
<hr>

<div class="tg-post" id="msg-467420">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fb2e8355.mp4?token=MkJ5mx-1TclcONrpcKT9QVRlmUcF3No3gR7Wv15KoLyNYWa9uZLhyBJgwsHdbEG-2RrnX7MLNTBkuVdoX8UNR6IQhXu2tLhpwRW8k7lyuwb9JqbG_wwe5rjexRPnXLrpaS-VD-BOH4hyKKPAXd4LrmR8C27wbFCRMQdcfhSDIYRRcto8TSZ0x6nc4gRIyozOQ6beg6yE_R7mrGwVso-zbLMxlMmIxLylGhWiJrYMQh2kI69_sT86g3J-1YJOw69AFQ9JLPUbTXFi3IimJaHnuRAmLPVLkdrS0fh3lS6tN_qPUjrJoCFDhYQV0Hq3IE8JCzfE10k9B1jZbyGAMWXjhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fb2e8355.mp4?token=MkJ5mx-1TclcONrpcKT9QVRlmUcF3No3gR7Wv15KoLyNYWa9uZLhyBJgwsHdbEG-2RrnX7MLNTBkuVdoX8UNR6IQhXu2tLhpwRW8k7lyuwb9JqbG_wwe5rjexRPnXLrpaS-VD-BOH4hyKKPAXd4LrmR8C27wbFCRMQdcfhSDIYRRcto8TSZ0x6nc4gRIyozOQ6beg6yE_R7mrGwVso-zbLMxlMmIxLylGhWiJrYMQh2kI69_sT86g3J-1YJOw69AFQ9JLPUbTXFi3IimJaHnuRAmLPVLkdrS0fh3lS6tN_qPUjrJoCFDhYQV0Hq3IE8JCzfE10k9B1jZbyGAMWXjhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز پرباران در راه ایران
🔹
سازمان جهانی هواشناسی به‌تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔹
النینو که با گرم شدن غیرعادی آب اقیانوس آرام شناخته می‌شود، معمولاً…</div>
<div class="tg-footer">👁️ 344 · <a href="https://t.me/farsna/467420" target="_blank">📅 09:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467419">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8g68APR9hcVDt8qH3P5s7XphL8bfX8Cj0Fx6wooYQFAhbm2b7Lu3VyzV9VmzKEG0Nd0cqqAjxF8frTxY0gQ9jrYNIYWcOKC20shM7TOdgYeLwlZC_HCqmHAeVwB53DLZS74IDVYgSRDpzIUr6-wwEcUt7xOL5-BONOokA5rizA23jvkD3K4PCFL2qCSzA9OBzikPHgpQcbbWnQtCyBJQIQNl36VrQMJDRnSERjjG31IT31uyMlp8-oNNBR_E9zb3Uc2nPL6XFUTq0GGDTTrJQ0qAEYpRZiAWoN38nAwE9B1O4FGPSHsZld5v8URRJyqrLgbPlAkLVwzEqaJcov-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/farsna/467419" target="_blank">📅 09:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467418">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پزشکیان برای حضور در گردهمایی آیین سال زراعی ۱۴۰۶ به کرج رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/467418" target="_blank">📅 09:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467417">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc5ec9619.mp4?token=lK7-rFFrDSaJaeqbIneV9j6TzDuLcWoQOZhZ43pG0nveZyrJ4lTptOq6jpmt7-7S0Lu9xsmx62JqRSnlWKzpXKErcz0nsrbGg4sML5CMGL5WogOdrNvqvnjgzgh05XzbQOgmEnuhAjcQGvAGhSuWXbKSq4L0B550Z_ogHsNvngmskflKCE_SRY7XCrdfA_Hm3ty8CkAXr4Rm1u-H_kEhEpXOCEJfXRHjjgxmoaM5ug4GylwA8J77VwdwBvS4zlkXgbnmagKslAKWb_bY1pY6T4pxf-Jsn9YE5UW8vYf1Fid89yAvpGCrr20AxuOozpyBANnlt9QgH3ooDkpMlIbRMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc5ec9619.mp4?token=lK7-rFFrDSaJaeqbIneV9j6TzDuLcWoQOZhZ43pG0nveZyrJ4lTptOq6jpmt7-7S0Lu9xsmx62JqRSnlWKzpXKErcz0nsrbGg4sML5CMGL5WogOdrNvqvnjgzgh05XzbQOgmEnuhAjcQGvAGhSuWXbKSq4L0B550Z_ogHsNvngmskflKCE_SRY7XCrdfA_Hm3ty8CkAXr4Rm1u-H_kEhEpXOCEJfXRHjjgxmoaM5ug4GylwA8J77VwdwBvS4zlkXgbnmagKslAKWb_bY1pY6T4pxf-Jsn9YE5UW8vYf1Fid89yAvpGCrr20AxuOozpyBANnlt9QgH3ooDkpMlIbRMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
در طرح تورم صفر، قیمت‌ها چه‌طور ثابت می‌ماند؟ پاسخ به چند سوال مهم دربارهٔ طرح تثبیت قیمت‌ها  @Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/467417" target="_blank">📅 09:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467416">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آمریکا مجوز انجام معاملات مرتبط با واردات گازوئیل از روسیه را صادر کرد
🔹
در چرخشی قابل‌توجه در سیاست تحریمی واشنگتن علیه مسکو، وزارت خزانه‌داری آمریکا مجوز انجام معاملات مرتبط با فروش، تحویل، تخلیه و واردات گازوئیل با منشأ روسیه را تا ۷ آوریل ۲۰۲۷ صادر کرد.…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/467416" target="_blank">📅 07:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467415">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMvN2Uac8AqWkugoAw09s6LVMKSCBzargA4qezMXm3eYeE3OYBv7PmZKIocRe_032V0oxNF5MmzpzvQ6RymIxIS7ZWAziuxvYQzCoastOpnk5hESeOC_KTSP57NjX_foJu_AkDROPivIsBWmFD2nyKERQUlW1EwrpVWNFOn3VCpzOONbiMrh5oGt5zg-UXi9KFRlB9WforDT7qjZJmFiBW_J4D7u1oO5FFE93zz6_RqaNy0GuoBgweEvhS-0LHneQle4V_1BYhT23Kc1NN4Lygx12CUmiMGYG_wg8Zo15z5qzzsDe0HJHO677nZCyyJS9rH9dFy-GBOu-N2PhFAWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رویترز: توافق ترامپ با روسیه تأثیر پایداری بر کاهش قیمت سوخت ندارد
🔹
تحلیل‌گران بازار انرژی می‌گویند توافق ترامپ برای عرضهٔ ۳۰۰ هزار تن گازوئیل روسیه به بازار، نمی‌تواند به کاهش پایدار قیمت سوخت منجر شود.
🔹
چراکه این کار صرفاً جریان محدودی از عرضه را به…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/467415" target="_blank">📅 07:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467414">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjPzOKiMoLaMKeesT5gXzNiT81wYGzIecA4fwUeGlBlZpid7DH82C8I5o1uOoROhnvunIqevCLs6fj_tRaEF1LPf16xfaIqQW2ViKDcKbeBVgsJbsU9REzj78vzvSTNX10n8KeVcodXmbexsdevf9_-Sr6UlKMZOFjWWys_45woQDDZPnpcTHNYCX4fW07ovhgw8LowzRUqCO127usCsNMT900IyEXOjpP7dl3-w7g54-dnRG5pAsIezKlHMRTcmAwVsNs-ODjMEw_HvvTc25FAPp4ciukkddQP9UkMrpR9N0aB-jw_VCJrh0CiqXEXVjrmxGpQHiQGL8kwZdgsqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیاران جدید نکونام، تراکتور را در سفر آسیایی همراهی نمی‌کنند
🔹
کیانوش رحمتی و ناصر فرشباف دو مربی جدیدی هستند که به کادر فنی تراکتور اضافه شده‌اند، اما به‌دلیل صادر نشدن کارت مربیگری امکان همراهی تیم در دیدار آسیایی را ندارند.
🔹
آن‌ها از هفتهٔ نخست لیگ‌برتر روی نیمکت تراکتور خواهند نشست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/467414" target="_blank">📅 07:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467413">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آغاز هفتهٔ جدید، با هوای «قابل‌قبول» تهران
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۰ و همچنان در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/467413" target="_blank">📅 06:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467412">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
مدیریت بحران مازندران: از کوهستان‌ها و مسیرهای پرخطر فاصله بگیرید
🔹
از بعدازظهر شنبه ۱۸ تا بعدازظهر یک‌شنبه ۱۹ مهرماه، در تمامی مناطق استان احتمال رگبار باران، رعدوبرق، کاهش دما و وزش باد شدید موقتی وجود دارد.
⚠️
تأکید می‌گردد شهروندان و مسافران از اتراق و توقف در حاشیه و بستر رودخانه‌ها و مسیل‌ها خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467412" target="_blank">📅 06:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467411">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3iJD7_ama-NwqJ7d7yOsoeHALmzMIekJCjNToHX7y4F20MU669gj6SZNR8_le5YRS7CQ1CvHvY_oJdx8i7riqZteIvBdNzCLH6VZle3aVxwXPSaHVmd7jEiWgDj9-yPFssnE-4-DfjEl89Lc4zM8dVScXPThibTZhAKeOlzpqXE9MyPT0akprzy4CPbqFwLzWYTBs7jU-mzWhqtdWHqKCovznvpzHq7XMneOcxsIgWrwsGZttFpUcHGw-bXnHHATH6_Hk04aEmKfWg3GmfVQY83H4VC1UZ8eVR52boK8dJTE50tsWmZyTMfmus3QpdL_0OLU-5TtNTGCydL1RaY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: دیپلماسی منطقه‌ای برای ما، صرفاً به معنای برگزاری نشست‌ها نیست؛ بلکه باید به ابزار مدیریت بحران، حفظ ارتباطات، جلوگیری از گسترش درگیری و فعال‌کردن همکاری‌های عملی تبدیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/467411" target="_blank">📅 05:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467410">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gevGMMMbq2xV8k1gVlI1Pc7ZH4adErYey4jrdut5XA_Jj-SZV5jwy6pGzlLuDrwSkDlGZtjOyvqCp3xTLfkkltwNfmE-mTR4PkrNxdbtM0ZeDr6UcEEQ_E2xBoNCcZGlw8bm1xHdcOdtvUMc2Wsktr75_blouFw8EKfXnDfFRFqoEEaBaNKXQzs8LkBkCcZOvESPLUV_0IlYpAnfSmGwbxFMG3dmMw6ia8YisRb2xUz0M7zgg0FXq1iyKlBJhEPwtagrmFaMzGaX75zJqgduuwAoM3moMQVp1zkj-GEAvMNqwz133lHFShVUp-30lD_OUtPXeA26VJUu4zpntvPfIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
در طرح تورم صفر، قیمت‌ها چه‌طور ثابت می‌ماند؟
پاسخ به چند سوال مهم دربارهٔ طرح تثبیت قیمت‌ها
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/467410" target="_blank">📅 05:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467409">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=gz3BymbB83i99l6zKbXvvS_a1MgjIizGTwevq7ZNOZPlxU_7JVT-1Sprg_rV1er94vi5neFa6OgfPs3ce8yHcd-JK-PZg7J2HC87iQ0P04kL0wqf4Vr9-wygV5A-XdbGEFDU4YiGlqmwDkK6wM7TuLfsHL94X6VT0sDDJKObxvRIhYGi0mFQXfUzpIt-58tcF3kkdjLe53EewBNL8zx48aORluQqdZkciqlfccSm-9Fd9lo3GVUYEpg07XCypyt8NwlvSNfzd-5Icvx8TJ_ZszxiB4ssXNdDvQMnfmVZmnMGESSFaZqxjhp7zrOxlJa_auKi7zUsbKYAmmt3FfOSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=gz3BymbB83i99l6zKbXvvS_a1MgjIizGTwevq7ZNOZPlxU_7JVT-1Sprg_rV1er94vi5neFa6OgfPs3ce8yHcd-JK-PZg7J2HC87iQ0P04kL0wqf4Vr9-wygV5A-XdbGEFDU4YiGlqmwDkK6wM7TuLfsHL94X6VT0sDDJKObxvRIhYGi0mFQXfUzpIt-58tcF3kkdjLe53EewBNL8zx48aORluQqdZkciqlfccSm-9Fd9lo3GVUYEpg07XCypyt8NwlvSNfzd-5Icvx8TJ_ZszxiB4ssXNdDvQMnfmVZmnMGESSFaZqxjhp7zrOxlJa_auKi7zUsbKYAmmt3FfOSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ دوباره از آرزوی خود برای دریافت جایزه صلح نوبل گفت!
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا، با انتقاد از تصمیم مربوط به جایزهٔ صلح نوبل گفت: آمریکا، با نمایندگی من به‌عنوان رئیس‌جمهور شما، باید جایزه صلح نوبل را دریافت می‌کرد؛ اما این اتفاق نیفتاد!
🔹
این تصمیم، لکه‌ای پاک‌نشدنی بر دامن کشور نروژ است؛ تصمیمی شرم‌آور و مایهٔ سرافکندگی!
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/467409" target="_blank">📅 05:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467408">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp_Wiox7jFYR0QdgeoWxU7eyxO3-SBCL2216fLTU0_-zDaYBxXVmpB9qpNZnA29xACwlqoQlOuyO15x-TH6zjWtld_pQZN6xxOEJfy0EgUBtsbpScmod2I4YIgsbZNTj8ci9ej-k96-fug9i5862LT5aiTvgGAUeM7Dlsa_Ut7BgEQ0e2WPYlwCT8y-O_Mz15GH_JxKlLpyazViMaNs2T1vM_J4zN2ayMTczwIYJ-qjFv5qUKoFzM1y7izrncqSI9rjKrl1ZQV6sGl205Mde4tRuHdTbzxeWzvm_HO7zV37wSkbS_NQv5yzYSpGt5XNlSsSMQ9CTdB40-C3QePPoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به پلیس گزارش قتل دروغ داد
🔹
مدل هوش مصنوعی آنتروپیک در جریان یک آزمایش خودکار، گزارشی جعلی دربارهٔ یک پروندهٔ قتل حل‌نشده را از طریق وب‌سایت پلیس فیلادلفیا ارسال کرد.
🔹
البته پلیس اعلام کرد سامانهٔ ضد هرزنامه این گزارش را شناسایی کرده و اجازه نداده برای بررسی در اختیار بخش‌های تحقیقاتی قرار بگیرد.
🔹
این اتفاق بار دیگر نگرانی‌ها دربارهٔ رفتارهای پیش‌بینی‌نشده عامل‌های هوش مصنوعی و ضرورت نظارت بر اقدامات خودکار آن‌ها را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/467408" target="_blank">📅 05:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467407">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYgZ5yv8rEmCI5wFUHiHyZdFiDmSarQbrpdpX9oPfINGTgeP_2EwBYJgX6ydionCZWMzExVOVbX9CzKDcv3VrvL9pZzB_sWKtVNWoPpHn6BckIeIgPTQOe3brRRld_Bs3fhWG2NUBun6feFkT3V98QPwyFk2mUVVIk46txkILNZqMahzYoiT6Is-ijPDAAH5ViLxUheo0ks8b2lth8hIZl59pw8wbN4rLE_am-OKDmzwqbRpl2Uda2h9OsP0ImJWvyXkbEE4_I7E6dNwmL5_7XzbW6WInmpEO7A0G2YfrE97HjEZtcELzVDgip9jH7Cx7bPx7FAj34D00ESj0aCtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دموکرات‌های کنگرهٔ آمریکا: بهای جنگ ترامپ با ایران را آمریکایی‌ها می‌پردازند
🔹
دموکرات‌های مجلس نمایندگان آمریکا با انتقاد از ترامپ، افزایش قیمت بنزین و گازوئیل در پی جنگ با ایران را محکوم کردند و تصمیم او برای خرید سوخت از روسیه را زیر سؤال بردند.
🔹
گرگوری میکس، عضو ارشد دموکرات کمیتهٔ امور خارجی مجلس نمایندگان آمریکا می‌گوید جنگ فاجعه‌بار ترامپ با ایران باعث افزایش شدید قیمت بنزین و گازوئیل شده و آمریکایی‌ها بهای آن را می‌پردازند.
🔹
او همچنین از تصمیم ترامپ برای خرید انرژی از روسیه انتقاد کرد و گفت این تصمیم تنها چند هفته پس از امضای قانونی رئیس‌جمهور برای اعمال تحریم علیه خریداران سوخت روسیه گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/467407" target="_blank">📅 04:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467406">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAAuZfh_jld9X1LbtGNHSAabhEXmS--XL-vSW2wkXEhyZDItbcCApR0bb0W22J83K6lP8Nkrfe9qBC51zJbddxVFjPftdXjoAcMPrKBON3cEtH2RA9Z7L2gLbwkDYkP87xhnwWYoBK1_WbTn2iATOsyH_-2s5sPlhYTNlO65sziYFSWcz3dMLMd0YA9N_NJU_Zmb_w6Y1i45V9eRaArOaD5wnkWJMHabhtBI4gHchOvNWU4Qvu-ykp43Q7VDTnd_-3v2CZ2Le52YRnVrH4pNJ95g3JX50MFuVPE2lGzWUOElSld2fQlJHi9H8MdiARj9Hy5MjiTl-K4KIKbw5etYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی کودکان حرف‌هایشان را قورت می‌دهند
🔹
بزرگ‌ترها میان کار، مسئولیت و دغدغه‌های روزمره در رفت‌وآمدند و کودکان گاهی تنها چند دقیقه توجه می‌خواهند. برای آن‌ها، شنیده شدن لزوماً به معنای حل شدن همه مشکلات‌شان نیست؛ گاهی همین که پدر یا مادر گوشی تلفن همراه را کنار بگذارد، روبه‌رویش بنشیند و اجازه دهد حرفش را تا انتها بزند، می‌تواند احساس امنیت و تعلق را در او تقویت کند.
از یک فنجان چای تا شکل‌گیری اعتمادبه‌نفس
🔹
گفت‌وگو با کودک لزوماً از پرسش‌های جدی درباره آینده، درس و موفقیت آغاز نمی‌شود. ممکن است از همان لحظه‌ای شروع شود که کودک به خانه برمی‌گردد و می‌خواهد ماجرای کوچکی را تعریف کند؛ ماجرایی که از نگاه بزرگ‌ترها چندان مهم نیست، اما برای خود او معنای ویژه‌ای دارد.
خانه کجاست؟
🔹
خانه جایی است که کودک باید بتواند سؤال کند، از نگرانی‌هایش بگوید، اشتباه کند و بی‌آنکه از تحقیر یا نادیده گرفته شدن بترسد، احساساتش را بیان کند.
🖼
چنین رابطه‌ای می‌تواند به والدین هم در امری مهم کمک کند؛ نشانه‌هایی را برای پدر و مادر روشن کند که ممکن است در شلوغی زندگی روزمره به چشم نیایند.
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/467406" target="_blank">📅 04:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467405">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg8-oebYWG0tQO4se0m0QzCRj62Yc9GqfYpAO-xfUXeWOpiF5wvWGbIj8Od8yIKzeitKIW_H2wi00HVkZUYDqBukmgo80DcEc7Nkc4D-xY3KrF1rjem2gbWThVavZ72XE8Ks0bB37YaFofyNbVrQ8706A0Wg8c9vY9bxkgjQYZu1t6hMJYSYcusPdZgJnCQF1bDe1AIS1YgXswURxqHudbE9Of4n5G4gg-jGlwON3AE6PxQnkfXVb-3gnsAZ8JgtHTGs8V3mPqZTph71FtwpbVAJot8RdWS7Yz-gJPSGN3ndBDhLtcamRYaniBiWh8ICRjEf-6pZdUXPDYbYJM_MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به مخفی‌شدنش در کامیون حمل غذا واکنش نشان داد
🔹
ترامپ دربارۀ واکنش‌های کاربران فضای مجازی به مخفی‌شدن او در کامیون حمل غذا در فرودگاه و تغییر هواپیما از ترس تهدید ایران، گفت: این موضوع مربوط به سرویس مخفی است. من فقط از دستورالعمل‌های آن‌ها پیروی می‌کنم.…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/467405" target="_blank">📅 03:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467404">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45298b396a.mp4?token=WhKbRoydpVK1YF_wDVgNRYsJ5UWbepxHbWh5JUlVzWNeYQFA05xX-tggbKIC8tt4op30-6UtrqX1DYgqzmG59mAbODotRtGj4R1PlA8pANe3FcnBNxcFyf75PCmkbCD_SDHIB2A6GKBMS45tf_5_L_KU-bdWMFTDuOKUqQrsSVWvEe8_-mR5N4PNm2HSsKLn8LmS0UMbdkDLT0gnYQeTNlnAhyzO_d4-gYOGUxTTQ7R3MF7W6JGZYw6WmLGdlMWEW7WGn8PKwJwBjpRU15grFfvnqyHiK8yt_hAaN3L8ys-Ch_a_zyRKbvHQ420fBBOC1WPOTmflgJ1AtvoHpO1NhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45298b396a.mp4?token=WhKbRoydpVK1YF_wDVgNRYsJ5UWbepxHbWh5JUlVzWNeYQFA05xX-tggbKIC8tt4op30-6UtrqX1DYgqzmG59mAbODotRtGj4R1PlA8pANe3FcnBNxcFyf75PCmkbCD_SDHIB2A6GKBMS45tf_5_L_KU-bdWMFTDuOKUqQrsSVWvEe8_-mR5N4PNm2HSsKLn8LmS0UMbdkDLT0gnYQeTNlnAhyzO_d4-gYOGUxTTQ7R3MF7W6JGZYw6WmLGdlMWEW7WGn8PKwJwBjpRU15grFfvnqyHiK8yt_hAaN3L8ys-Ch_a_zyRKbvHQ420fBBOC1WPOTmflgJ1AtvoHpO1NhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقدمهٔ
هر راحتی یک سختی است
🎙
شهید زین‌الدین
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/467404" target="_blank">📅 03:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467403">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رسانه‌های عراقی از حملهٔ تروریستی عناصر داعش به یک ایستگاه امنیتی در استان کرکوک عراق خبر می‌دهند.
🔹
گزارش این منابع از هلاکت و محاصرهٔ مهاجمین تروریست داعشی توسط نیروهای حشد شعبی و پلیس عراق حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/467403" target="_blank">📅 02:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467402">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انتقاد اوکراین از توافق ترامپ با روسیه بر سر گازوئیل
🔸
رئیس‌جمهور و وزیر خارجهٔ اوکراین از توافق ترامپ با مسکو برای عرضهٔ نفت و گازوئیل روسیه به بازارهای جهانی انرژی انتقاد کردند.
🔹
وزیر خارجه اوکراین با انتقاد از کاهش تحریم‌ها علیه روسیه گفت این اقدام نه…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467402" target="_blank">📅 02:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467401">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUnIm89IOfpzcFBUnAt358lVlj0vdAHondSyTBunFIyp12bLy1jeTqYWDrEJKQfdvk1SjdtTA-nkv7gcJTpm2qneTydsD-SCc_VMG47PywswKEUPxZYLK32nh_uvnLz3jR7UDjut7-725LJrwX46OeTlvW2fchKKJtCtR4KoeCmIJqqrVgOy22IDANr5QuXli0NOfQ_lEn9Qrh9OhPRlYL-wbTzJtpH08zCgXwBbtJCA9a4rhcuk5lwICnjQhWI4BdTVcTgcZwrN6YEpW2dg8pNgh44Xzpc6myiIch6i57u9lPk4cFYynmncCEqVmifdB0wXo7Pj0wqPPt5hNeY99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک به فضا ارزان‌تر از اجارهٔ یک نفتکش
!
🔹
اگر بخواهید یک نفتکش را برای سفر از آمریکا به چین اجاره کنید، اکنون باید بیشتر از هزینهٔ پرتاب یک موشک به فضا پول بپردازید.
🔹
گیبسون که یک شرکت کارگزاری کشتی فعال در زمینهٔ حمل‌ونقل دریایی است گفته هزینهٔ چنین سفری اکنون حدود ۸۰ میلیون دلار است، در حالی که طبق محاسبات پرتاب یک موشک فالکون ۹ شرکت اسپیس‌ایکس، در حالت معمول ۷۴ میلیون دلار هزینه دارد.
🔹
همین مبلغ در اوایل سال جاری میلادی برای خرید کامل یک نفتکش تقریباً مشابه کافی بود.
🔸
فعالان بازار نفت دراین‌باره می‌گویند تولیدکنندگان خاورمیانه ناچار شده‌اند نفت را از طریق تنگهٔ هرمز منتقل و سپس آن را به کشتی‌های دیگری انتقال دهند. این جابه‌جایی‌ها گاهی حدود یک هفته به زمان هر سفر اضافه می‌کند و بخش بزرگی از ناوگان جهانی نفتکش‌ها را برای مدت طولانی‌تری درگیر نگه می‌دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467401" target="_blank">📅 02:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467400">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">زلزلهٔ قدرتمند ۷.۷ ریشتری پاناما را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۷.۷ ریشتر روز جمعه جنوب پاناما را لرزاند و به خانه‌ها خسارت وارد کرد، برق مناطقی را قطع کرد و موجب توقف پروازها شد.
🔹
به گزارش رویترز، این زمین‌لرزه ساکنان را به خیابان‌ها کشاند و بیش از ۱۲ پس‌لرزه نیز پس از آن ثبت شد.
🔹
تاکنون، جزئیات بیشتری دربارهٔ شمار احتمالی کشته‌ها و زخمی‌ها یا میزان دقیق خسارات اعلام نشده است.
🔹
رویترز همچنین از صدور هشدار سونامی خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467400" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467399" target="_blank">📅 01:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh2-saj57bzxO4MtsZD_KfM1_TIJVzCPLpYAGRHIMrFHRSzUItP_IaSQx7I1ZfzfJAUv-XpFQ3pWvePxfQ0T8urY2DL5sM5c9OWfICHTUJRnJA5Tr6p4E9CBVOzxus0UZhDHm_wK_bjKcZCOw14f0rnjHdMk3NS0B68ZG_-HoskIboo-w_bDWdhDD1qQj1_lT4ZvKvhdakmLFTdgHWFNQbnEgKEiFxyIIurDpbUiNR6x6xrUib0icq1Q4p8ku2EdKgv3dqBL4_jXJXqQiwKl2C6b-rZNxZRLocPy_rFnyT4GpuVuTLdkreUzyhli1LZdF55SQl5zZVBp3GsUpfOC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصادف زنجیره‌ای در محور دامغان-سمنان با ۱۹ مصدوم و یک فوتی
🔹
این حادثه در فاصلهٔ ۳۰ کیلومتری سمنان رخ داد و در جریان آن، سه دستگاه خودروی سواری و ۲ دستگاه خودروی سنگین به‌صورت زنجیره‌ای با یکدیگر برخورد کردند.
🔹
طبق گزارشات اولیه، متاسفانه یک نفر در صحنهٔ تصادف جان خود را از دست داده، و ۱۹ مصدوم جهت ادامهٔ سیر درمان به بیمارستان کوثر سمنان منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/467398" target="_blank">📅 01:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOfXz2-yk633aZG0eYZ5mqy0kCkwVBgZzytP8_oe3ArOg8mjobuoc23Da2kRUlBLZ-lGr8LdCFq_KWFObCAel61NIg9GsWn_Ah0XaOruhEnbM3j5bw_KgCPPPygUkPTSYO62pEEgvWh1UY2NIzI2-t3lmEVFi7uwTKzPNlwfRd7wHm6j2De18VCyuD5A3RHqtF9_H0cr8HN1N9ox5Fw80gUbPiGIqxWblo5PuLPdgUSRBxVTDBSsU18WrTvF4QLWflSsBUmVb6aE48EDWq4ROyT-eppqOWkBv-h5QhaOv-bflKlXQXXkIDuy3cYrS-5MVNvWQNzizQYuyiLgjocdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش اپراتور فرانسوی از اختلال گستردهٔ اینترنت
🔹
در ادامهٔ اعتراضات فرانسه، گزارش تازهٔ اپراتورهای تلفن‌همراه از قطع خدمات تماس، پیامک و اینترنت همراه در تعدادی از سایت‌های مخابراتی فعال، به‌دلیل خرابی یا عملیات تعمیر و نگهداری خبر می‌دهد.
🔹
گفتنی است در روزهای گذشته، فرانسه شاهد اعتراضات گسترده‌ای بوده است که در پی آن، وضعیت امنیتی و تحولات داخلی این کشور مورد توجه قرار گرفته است.
🖼
در تصویر، سایت‌های دچار قطعی خدمات، اختلال شبکه و تعمیرات برنامه‌ریزی‌شده مشخص است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467397" target="_blank">📅 01:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E74hAaoJ4bVh_g8-b_Gl92DLzkB30NUcu-f3IctPVNHFvd90vcyavsFsHo9r4rwwziyaKx6Nq7jduLoSw1sojrq9q4jeEeNsfI22O-xQaCG_Kto9dUSOVemQb2n0IwmO13pCf2GcR7431QiNgoe4ElsW-YdMDdzhsqG0jX3rQgjt4b3rFTBBwzsxGRx1cgYNmKzCTzMsAeewtngCPivWbJAXu4iH-cb2OAHROFfWfxzVowmZ3SG3bC8NhtBpAWA-ViRMWk5RcILB2Sf8wA6a2I6Y6TXTetYtYZS23sdDrM-3GPU7-R2aFLVbLLHaea9nGWhJJH66ei5e33ZZHkBc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پوتین و ترامپ گفت‌وگو کردند
🔹
به‌دنبال انتشار اخباری دربارهٔ توافق میان مسکو و واشنگتن برای عرضهٔ گازوئیل و فرآورده‌های نفتی روسیه به بازارهای جهانی، کاخ کرملین از تماس تلفنی میان روسای جمهور این کشور و آمریکا خبر داد.
🔹
الجزیره گزارش داد، براساس بیانیهٔ…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467396" target="_blank">📅 00:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پوتین برای عرضهٔ گازوئیل به بازارهای آمریکا اعلام آمادگی کرد
🔹
رئیس‌جمهور روسیه: مسکو آمادگی خودش برای عرضه فراورده‌های نفتی به بازارهای آمریکا و کل جهان اعلام می‌دارد.
🔹
ورود نفت روسیه به بازارهای آمریکا دلالت‌های مثبتی برای اقتصاد جهان خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/467395" target="_blank">📅 00:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حضور بیرانوند در محل تمرین تراکتور پس از شب جنجالی یادگار
🔹
پس از صحبت‌های شب گذشته علیرضا بیرانوند علیه مدیریت تراکتور، این باشگاه با تصمیم جواد نکونام، دروازه‌بان خود را از تمرینات کنار گذاشته تا روز دوشنبه جلسه کمیته انضباطی بیرانوند تشکیل شود.
🔹
با این…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/467394" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5452qjJzYxcHmuawB2Mvs5jgG3peMRT7mSV0Pzjtg9_0-unA7HRzScRAJe5yCZhmkhz_EP4k33yz49gqzDcxfRS2rMvmekCV8QF5EiqQokBAPIhhatPq98v6emEz2Jb7YKomBRjEmpQuWa31HONqAKOgkaIiFESGB_cMqbt1o4T3forUivlRSJdsphLU3q-6wO23zgqs_4jslhruq6TVA40IkMkdLZzKNMJmHak8a3g0XCPfB--4XFeE4ROT7x5TE2wvoHKnQlqSDn2xDxuRWw31cMBm49yzVIF2D8TTINxJTnqjM_E28zltCXEmZLzT1s69_C0tlxItZphzUTnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند ممنوع‌الخروج شد
🔹
سازمان نظام‌وظیفه اعلام کرد تا زمان مشخص‌شدن وضعیت کمیسیون پزشکی علیرضا بیرانوند، او حق خروج از کشور را ندارد.
🔹
براین اساس، حتی اگر این دروازه‌بان با مدیران باشگاه به اختلاف نمی‌خورد، بازهم نمی‌توانست تیم را در سفر به مسقط برای بازی با الشمال همراهی کند؛ مگر آنکه مشکل خروج از کشورش را حل می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/467393" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7f_4NmoEt_mGth9ZuTspJJrWGqKTYyw6gd-KH8HSwLGsaIWT2O6un6QFsEiQauUBbPu6s4Dfeus9bRwQMS9I-j3rgVzwVkgd1IzAkhp1Czfh0D3ONVd7BtDWwXoODnUx4WIznx3Y8tmNxr7HRobB59cuEdLl9cupcOKH_NaL1wj9V-Bw9yvNlFZWXSUHtn8WfOGEk19lT5ymTD6w8Ad7XQksl6s1WKMMEAQ9D86WRJO0gplWEldMiV89dg9UfsLeCtllXJfiXA_YpK2MDgRE7tF4w19VBjbdBwNMqognOvuldw8mUCz4wgFnS_17pz2f8XBPcqHHNpFJzZ1buQJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/467392" target="_blank">📅 00:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEDrL-doas47UTxMr0Tsfs-3lV42eYrpFLIOqbw962_REpCn9eEuDJT8z_FKgmHzP0JJA8FGpiFD7H1rqJ38KEQowmRsL0ibvI0dqR-59yhyHMrrzYF2KsoY1JRoiwZaCzX2TZuFA_Mm40wGHnna1-3lPqhLoZzppsBA_yh5ZmzAa_huyNb7rAYrOQWluuF3vD8Ql8sedNmXwzE6qls2of1WLiQj4YiML2BQ7c1bIy_EC8_OF0kDbNiICFkWUITUeX2QyjVctyCI68BzlOwN3IUL640ZdEy2U6HZakKrBGCyI8HjFVaEsWdV0K7OlUtW3AvuJE17seVIyBAJQiqbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: اجازه‌دادن به روسیه برای فروش فرآورده‌های نفتی به‌منزلهٔ سرمایه‌گذاری در جنگ علیه اوکراین است.‌  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/467391" target="_blank">📅 23:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24e30c480.mp4?token=QVFW8b--22wo9emVSN4i5YHUQFd2f8dQmVpz6X3WQBAJFXOBEUU-GOVMeP2ev0GayfWPjj2Too2Q7yd3sY19jzT-oEJhx9l9L5Yn2wWee6ZaS-WW8HVXowwqgvdIgeVyie4rbFQ5M41N4pXXp0eyCEWyvM0ff3u0bBEEUU-79J1chAjbyoRULkGsD2rRxq-1HAGhJqygZONBdcg5lYWxKRnHXll-RvVfTREYaL_SmeW4bkySDc3LBYwd1zl9yhWt-PJXXL7RWKhX73-xYcoaVcnMPIMraGz1tJiHL374pHvj3ehSAKbmACPO9rthLDPQSlWCO_RuGHjg1fN7lfM5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24e30c480.mp4?token=QVFW8b--22wo9emVSN4i5YHUQFd2f8dQmVpz6X3WQBAJFXOBEUU-GOVMeP2ev0GayfWPjj2Too2Q7yd3sY19jzT-oEJhx9l9L5Yn2wWee6ZaS-WW8HVXowwqgvdIgeVyie4rbFQ5M41N4pXXp0eyCEWyvM0ff3u0bBEEUU-79J1chAjbyoRULkGsD2rRxq-1HAGhJqygZONBdcg5lYWxKRnHXll-RvVfTREYaL_SmeW4bkySDc3LBYwd1zl9yhWt-PJXXL7RWKhX73-xYcoaVcnMPIMraGz1tJiHL374pHvj3ehSAKbmACPO9rthLDPQSlWCO_RuGHjg1fN7lfM5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیانات رهبر شهید انقلاب دربارۀ نقش مردم در قدرت رزمی کشور و خطای دشمن دربارۀ قدرت نظامی ایران
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467390" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c107f3d38.mp4?token=EWRYY1EkRe32pFUKyGt3_HH_75OHOALk9q-oKQ3nMNYAO4KW3daK4AoUHD1BQLksM4tzJkvNu6zqYgMfjbIHqxLGsQj6puQ-In_KEpIlBCZMRX4-cLP5TEAffr4gYLrsz4J0HiQioStuktP5Pb7459mK4S8hQ-mf9Tj6XYBMsbQ1J0m6i0BBzbmpLMO_rhtgu1ndt1LN9f1fjK1DnkphVHrmIBW0eVjJUA61DXkWUU1JP7TOEfmo45TG2Y9m2oY2MmmGEGm9lAXNPBpfYXv6_48QL-nQ0-NWO1rDC_klyQI7JOsdaEQL8qWLcfWcnkpbOfH1cTwYyC9Jygq1f8DXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c107f3d38.mp4?token=EWRYY1EkRe32pFUKyGt3_HH_75OHOALk9q-oKQ3nMNYAO4KW3daK4AoUHD1BQLksM4tzJkvNu6zqYgMfjbIHqxLGsQj6puQ-In_KEpIlBCZMRX4-cLP5TEAffr4gYLrsz4J0HiQioStuktP5Pb7459mK4S8hQ-mf9Tj6XYBMsbQ1J0m6i0BBzbmpLMO_rhtgu1ndt1LN9f1fjK1DnkphVHrmIBW0eVjJUA61DXkWUU1JP7TOEfmo45TG2Y9m2oY2MmmGEGm9lAXNPBpfYXv6_48QL-nQ0-NWO1rDC_klyQI7JOsdaEQL8qWLcfWcnkpbOfH1cTwYyC9Jygq1f8DXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشرف اعضای تیم ملی کشتی آزاد و فرنگی به حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467389" target="_blank">📅 23:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984e3a9a47.mp4?token=vaaiBVegMEOm004hblec-4huLuts6dDyFFeMURdmxWC0VR3-jsZ1PmupmlEXPogy4g0EWP6tg_sJpzBk1rBVTcFipVua5dUWxiFWdZaGjqMgTUWQQI61tfSRAFaFYRP-ThE28bCd5gaoppAS4x6LtSPtlfOWUBTBkvYh_DKz7tC-1bO3ZO3G1nM5Si9ef1EJndOOl2pcQxtkht6pXI25oWcoCm7KO2UHMRSDnpRf3cfcC0S_8H7o80nn0G7pb4z5HMhzhpipoPwAu4ujUFMAtTiZvJpFpwsFZZpHlaoXjHf6GYXm9wSp1Wq7nZp-Ctb44Imfk5n16f76Vm3blx47GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984e3a9a47.mp4?token=vaaiBVegMEOm004hblec-4huLuts6dDyFFeMURdmxWC0VR3-jsZ1PmupmlEXPogy4g0EWP6tg_sJpzBk1rBVTcFipVua5dUWxiFWdZaGjqMgTUWQQI61tfSRAFaFYRP-ThE28bCd5gaoppAS4x6LtSPtlfOWUBTBkvYh_DKz7tC-1bO3ZO3G1nM5Si9ef1EJndOOl2pcQxtkht6pXI25oWcoCm7KO2UHMRSDnpRf3cfcC0S_8H7o80nn0G7pb4z5HMhzhpipoPwAu4ujUFMAtTiZvJpFpwsFZZpHlaoXjHf6GYXm9wSp1Wq7nZp-Ctb44Imfk5n16f76Vm3blx47GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم فاروج خراسان‌شمالی سنگر خیابان را در شب ۲۲۳ هم ترک نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/467388" target="_blank">📅 23:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAuNN9SygSVSpwRgClG3mvaDPmYiWUaMRmRCc54yBkC0WLXg3Av2KMnRVbg7xjRkvekxm7OxeEpbQ_ozhYkrREssJXzv4MDyMAcgPmD82OgUt0Z-CCfyeiafJOJPAfO37hmfCi4K8jwPKtvK9DlWCaJgLKKiiJRiuD5bWtRAZ3B5vRT_ZQELvSuMD2Q1X47Oa4SUbd4-gQiEbkrin_QdD9aJIwulV1ZMyuDY0Z2RPfwa_IoF5wCEE0gDq-rigaj3fzPkS6jpjGv4c2_Nxk9_3u1lSwKxXjwXg2Sr4hEFCeoldilsAQU4dhrkNGJSfW_7kwa2qNWWqERsMXU1COcjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-8ihuj7p1ilMKf2MPGtyv6xSoWG7E23maytvI3u2GQK7g8zozh3Sm-wWN2sroBKsXEKFrg1x7kQLKXnwEb1-ZFN8uVBSfT6Q2IJ54z2FOeqVjHfevxMzMQKydbS_pAqtOktiFmPSRUWaG2XrXOvgythGtAwFIaNjULb1YSJzmYN8Myx3ie_YHJHGFlxw_J8FItsZCuLPat6qqanslIqq_D_B-XV3j-Q2CknyTfR4Hy0NLc-uQCqvvVYu0juZyZTQvJnaNUfF0PPi4nQhUpbvEHgy6d70_qToAoRXTPN3YUH5i2Yh0H-jvMYpFsClCKTC2SkvICYxXEarqNUlq9rUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK3BR6a2roDEm8DKqClaWetuTh-IJR3ZoFvT3BlSO6qV5OFcnpyxk_2ItlOKylNsMEvEFmZO6_V74ZeiQ9B56LwIxhPi83dDWefzKepVcNZ9bibOKYlq6enaVDZpguzR3cXDLNRCyus9hH9sfbPRVfOe85Rr3fvS6adndulMqkhs-PNsPXJzZsO1pNLtioXaejZY8966tIHQVGamrNskYbmHUWARyeqHrrMBNnU-fAQHN9UPTLo4Pw591Pt2m5_n-DlyCpmPhkDzeTfaKQjhfFHSYPEfIFAHQcNC_qeaxGhm8YGMzR0VY0JGgspSdh_50GsZlMx7D5YvNIuABTyeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH4C-07mtYu8052zgZ_gnWOmb_OSMvToQlKeYLeMFNHkiff1NAHwbLkqxsKQnKTZOyIgdZ7XqhU3gcohXL_eHjKXzu08Zg3CQayd95DGxmM07P3FbHNBZGwqzQ2iGmCC_4NcsYgMpXL_2r8Xb_xMND4u3EJzsB2PnfX_wTAQL7Gk-r5Re6yLSZHn29pWdoISDowuIq-Hv5dA7iMjWtoF2AlH82e4bhAqmmCBVFXgNwzweZCRw-RYUcW252SNGZbMJulvFXGw6DJ5DDQLbBm4sa-X19ENJ_x2oYK4ESt1MwVsFBgbN23vUnMQjEpoiYe888iqn3aMT4FS-Im1KhqLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_sFsQqmKEGT8innfA2ACa4cZlxUXURj6XZuuLU-v4u6BM939dQskZFGwPavLfJ7SX4PiJ6R-1uqzQMbtUjOPFxj56gy5xi_uRA114vre86a5TWd-Ncm39fPRPgYpUEp7DLDWO6MsZCJ326XtUZGCI6SBDI2ul5Ideas92vFYg36QECLrfCRCspr3UjW2MeHORrS-fOUua3hELCcS0prDve27a91OMG0b_HfG-28otIqsZsD8PWkHv39P5WRlYKw7GOA5y9_agI4WecK5OC_5dxfNQ2pf6hW8DL96_9gsCwlb2Jt1rHmhK92q2pVwLmL0qLHUaha3QHFUnlaH0A1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dI3wSg2qCmCbyvFGazSpG4KJ-Ji41ogIdKjsP6kb7qe4hQDPlDDD9osOBC0mysmIzPTZMia8IomMFlKkd_WSsBMzDiAg0Tul1Kd6LpDnfR90f5Ab6vFn_PhUDFR-TaC-oAfuAQEh0HfgDv7SlliK3OE8XDHX0y_X_UtRVO2eEfA3-YefeJgYgGWBtsbovpWICLxjUKaXLDtg7RCSAtGuRqrogy6DVLZICMxLUAT4cWaf4N4eh7p1ULCs37TbBhFJ7-GHt8f12tkUMCNOsCyP-lMyZdxf6OrkYItOllXd5yc9Y1y8oEd2HIWMggMj5owbnQ4ylnsCNtMWWD5iMBKo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLbIUB8B4sI5f5j_8QN1gsmSfRcqQGHxJSShoDK3u4T7r-pklP5QZK-xNv_kmhoww-x7Qw93hFCp5EiG_T0sL7YSHyNmiT_YDIluAU1g1Wp00SEHoid9-RlnN_WijLXBTWPxn7uWUyE9dErYzxP9TLn037U72hSk0qRDHRU8Nkf2-EHMP4v_Wt-p84CsTrth7VviU-fEH89Vt_Rw2xUq7OmysArrtNdwum-qutROdC7farYJ2ixbgEZWwsO8WtW5rFBPbXuMFKvyoN3a_qFiWyJFJYnL2tj5HVe9pjONX9Y59sERTrcGWj-4PWrp7Ka7wznSAaO8z1J8nfjwOZbi_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل سوم برای پرسپولیس؛ اورونوف در دقیقه ۸۵ اولین گل فصلش را زد
⚽️
پرسپولیس ۳ - ۱ صنعت‌نفت @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/467381" target="_blank">📅 23:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467380">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvX8w6TkHano7gxIb8Hb9ZxJYS-eru276RSpkMXWcMyWh4UbNd9gmtBs33YL2qmf6Z2yYSLTT9qDrUJonaUd3rxwE5E_tRPI6487F4vqmq194sijE2OFnJY2RI6E9HBvBtWTs_cBeLk4csRoLoIOydlyCn4P6w9isjKSAcP9y6bQbQNnGUV57XF1JAeqkSjYnBowMeUBxCs_SGqBMc5UnNQNnzNNWiMOsSuV4BQ5BmOPmJu_G_cJj3AuUmFmWLtzBFkYLjd3jqtXmLQo-x8jRq7z_QdAnUxVn1xSgh97hx1AHNnLbPqHryw2CK9gMg45UVPR5h_Rm6-7VBGqMZlteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کابوس ترامپ به کف ۴۴ ساله رسید
🔹
ذخایر راهبردی نفت آمریکا در تازه‌ترین آمار رسمی به حدود ۲۸۳ میلیون بشکه رسیده که از پایین‌ترین مقادیر ثبت‌شده در بیش از چهار دهه اخیر به شمار می‌رود.
🔹
بر اساس داده‌های اداره اطلاعات انرژی آمریکا، ذخایر راهبردی این کشور در هفته گذشته با کاهش حدود ۷۸۴ هزار بشکه‌ای به ۲۸۲.۹۸ میلیون بشکه رسید.
🔹
این رقم در مقایسه با سطح حدود ۴۰۶ میلیون بشکه‌ای در مدت مشابه سال گذشته، افت قابل‌توجهی را نشان می‌دهد.
🔸
کاهش ذخایر در شرایطی ادامه دارد که دولت آمریکا با فشارهای ناشی از اختلال در عرضه جهانی انرژی و نوسانات قیمت نفت روبه‌رو است و ترامپ با انتخابات میان‌دوره‌ای آمریکا و نیاز به رای مواجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/467380" target="_blank">📅 23:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU1FYdDR0HnDzxspkfLeY2rYoB0meUISLf3HYZXmCx61psYsZNgXiTewu2IQXweBtVb408UHlE71BtZhnIwu5ZnUE1Mn-vWR1gfnqsm5LXBrJBH2Qg9WDBm23e4gEu-Yrl6Vw2Dfptfquo9i_hCkHVIB6HWAc4rjb1zG2wHzeGrAN_qBWDY-iQfpd88MfUE2iQzyfZbGj3SFuPR9a8eGinQpDKPSHKXAOvpAXwn9XAqa31tq_fJ9Dy1IODqGEcL6Cksbn4aKTfPwb8XQ0NpNsp9A_fTJwnF3ppFoqCiKUSlga13gSI5NKEORD4JO30GFwmWdrgwCJhjtuEFBngpcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ توافق با روسیه برای تأمین گازوئیل
🔹
رئیس‌جمهور آمریکا مدعی شد با پوتین توافق کرده تا مسکو بیش از ۳۰۰ هزار تن سوخت گازوئیل در اختیار آمریکا و بازارهای جهانی قرار دهد.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467379" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a40913d7f.mp4?token=VCApqXnDbhRlI6-9SsFinTD1KBRyOS4zqvKVnypzK3iCp3G5UMmtQoTsdbtsfKcSYIxpcA74h5sOn27tPbczRP6f1-sKPKtJIuZZ-8EpfikL7MdZQBIRRt8UFoMgW9mUOvZe8GSjgHitFCGKbyr-CjhFUH77U00iXznavud8Sm2-P0ecCtJWzr7DaRXvreobKdJ7wk2_msr_SdE_iX90OvczHWTIFb0ylvH-hkp4-tfl1YA4wY1o7SdBwdeL2SvcLQAN7He9ozzftjIllVXRkJJBc4lcBxSf81jmLLZ4wvACDGnWrdf8c9OT1GhiAO1IxnJl1Afm3p1EUs2wx-WzIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a40913d7f.mp4?token=VCApqXnDbhRlI6-9SsFinTD1KBRyOS4zqvKVnypzK3iCp3G5UMmtQoTsdbtsfKcSYIxpcA74h5sOn27tPbczRP6f1-sKPKtJIuZZ-8EpfikL7MdZQBIRRt8UFoMgW9mUOvZe8GSjgHitFCGKbyr-CjhFUH77U00iXznavud8Sm2-P0ecCtJWzr7DaRXvreobKdJ7wk2_msr_SdE_iX90OvczHWTIFb0ylvH-hkp4-tfl1YA4wY1o7SdBwdeL2SvcLQAN7He9ozzftjIllVXRkJJBc4lcBxSf81jmLLZ4wvACDGnWrdf8c9OT1GhiAO1IxnJl1Afm3p1EUs2wx-WzIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: یحیی گل‌محمدی به تیم ملی امید نزدیک است
@Sportfars</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467377" target="_blank">📅 23:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467376">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBMSHrQyfWHor9AOaNbi95GE1Ww9Ql2iiHFKa-81qYLp2YSYc3_Tg89et5Zh-b8xIh5akyWPJ1JXQU-04-YfQFObOAU7RZuCiW1Y-wKHHjN3AHwIZLRIa29Ff_VBEJGebiy56_Df8isZT53txZqYssSvYRzlUgA75phn7CKuZ4Nx0ZEKvtLCGMzyzBHdBzS_vhzqURhOsL2UROz7nLCbOoyA20vGjsQjQjCxH_wq3wOJf119Hk9xn8IRYvz9vHf1CsT2rRUYkVcpA_-ZNksQq8JXGmeTnD-xkUyn00i8G7rLM0h3DoZoGrsWxll9T8moT57qPqIhNJ9ayKDWdTz04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه نهاد آبراه خلیح فارس در مورد وجود دامنه‌های جعلی
🔹
نهاد مدیریت آبراه خلیج فارس: با توجه به برخی گزارش‌ها مبنی بر سوءاستفاده با دامنه‌های جعلی، تاکید می‌شود کلیه مکاتبات پی‌جی‌اس‌ای از طریق ایمیل و با دامنه
PGSA.ir
صورت می‌گیرد و سایر دامنه‌ها فاقد اعتبار است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467376" target="_blank">📅 23:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467375">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls4BHMF2hEnbehwuCB59M7CSjec5Z5kIzqD834pFufTqCzkFuOkdb9EinuIPIVJfeca9LlonUwenQWk-w65VQ-Kemi0CiCImIIQx79ufEkpgWZBLSPqVqZxDN08UAd-LMYJwJ8WoRndleV-eQTse9AXxu7sKv8srWOt1_t4Sp04Uy0O8naKpiJoF6QmP4kqmdklUSbx3yfA_pcHf0GgCL3aVS1yNvlY5alX2-Fp7VnLfy7XRVT1vY504u5t3XKjvutZhfr7McWDofJEVi7venfI7VkucTk1C7w8CmkpkVDBuS8_uDUnjvugCfIzhpzHwt5vGu_CZndM4JVSN4yzOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد/ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🔹
نیروی دریایی سپاه: ۲۲۰ شب حماسه حضور میلیونی و ایستادگی و پایمردی شما در دفاع از حق و عدالت دنیا را به…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467375" target="_blank">📅 23:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467374">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxHXtYNWryxVRQHvlnzfkhJp8TAYOkaIMSFgRDjyAFg8sYrA5nRiFU4_jLmiMHkq03kpQcLKZXwl1FkC8TJ5DBg7mImDmopW0QgdpY2eyH85XYQA7bVL9c3GFPuDOhronT6qowgyrIGeHJkbBNU-30t-SOH9ZHsSlMiu76dZMqmjDi9_ksW4QBw84xhWD1Ug-0UViEsTgjAyAstAVxRG-0fcIG2jslvBUVxkZrE92ZZ977M1H8ZWihRQadNTV1fAcqBMMFnYxTyPHXrUyw0RXui1K6bZZ5_hjKE1ccd5gCSW61lRIoT_OWbwvh1KEiLrZXFScJo8i1qmfh5rYbCyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مسیر فرار نفت عربستان از هرمز در آتش سوخت
🔹
تصاویر ماهواره‌ای جدید یک ایستگاه پمپاژ متعلق به خط لولهٔ راهبردی عربستان سعودی موسوم به «شرق–غرب» را نشان می‌دهد که درپی حملهٔ پنجشنبهٔ گذشتهٔ یمن، به‌شدت آسیب دیده است.
🔸
این خط لوله حدود ۱۲۰۰ کیلومتر طول دارد…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467374" target="_blank">📅 23:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467373">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2407f2c6f.mp4?token=O4FWpIhRoPOWmIDKUI1TZ572lmwrCBeQoe_w_2uKLwds-H5SV5H6ce0Lp-EjDOIiP5aVeopJ6NcuHlHdyiJhANBscpOjaJ3FF6iyPE5NEmc97n7DBb-jn5YtgboqRjDGAJYSNxYEDXiYWW6DO9xs2lx902dtfhrxQkKFizxrd3wztVm8xlOXy2GGdybUl9x5tOiXGXpJN9R6IFfvYidSKq6zqWvPVUpuTv_KtbWuMItB3RG22LYb9pPcB4Y6QWt_ACqIIIZNJ4k-ZF3SNmVYk8ap1U_MMGUafmgsznIzHako_bLTAkUIY2ey_gN1wDtd_G8zfg5khFzqjELK0nCjD7UuDfR2Ijt_vfyQr41-tB84-BZV5g-CGPlyAXhDELmQzLk4Hy9aLAuLJC5oKE0RoXaqdCYn4r2SYj37-Zp54fb64Vff-nTEPt7lJnzqH5yJXkLeknne60fB3yz0uKhu_23LFASETc7YAZVKh4ELHwpNlvt5J7CsEjIcvk68SM2e6Pa-PaY0rsLpSEXc6dakGcb9auEGZETXCoE7HUrIq2AH_YdEkpHRHob7lq5dLDWxIh-RebspejWMQyVvlgz30oFxC3QDMJKW4XbExe0zrZEk1Hn2GMuwOLB8lUT23jGyTGmjlUlVeibae7cQQWF5XCVzGj2FRhF_nkiIZfZJCT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2407f2c6f.mp4?token=O4FWpIhRoPOWmIDKUI1TZ572lmwrCBeQoe_w_2uKLwds-H5SV5H6ce0Lp-EjDOIiP5aVeopJ6NcuHlHdyiJhANBscpOjaJ3FF6iyPE5NEmc97n7DBb-jn5YtgboqRjDGAJYSNxYEDXiYWW6DO9xs2lx902dtfhrxQkKFizxrd3wztVm8xlOXy2GGdybUl9x5tOiXGXpJN9R6IFfvYidSKq6zqWvPVUpuTv_KtbWuMItB3RG22LYb9pPcB4Y6QWt_ACqIIIZNJ4k-ZF3SNmVYk8ap1U_MMGUafmgsznIzHako_bLTAkUIY2ey_gN1wDtd_G8zfg5khFzqjELK0nCjD7UuDfR2Ijt_vfyQr41-tB84-BZV5g-CGPlyAXhDELmQzLk4Hy9aLAuLJC5oKE0RoXaqdCYn4r2SYj37-Zp54fb64Vff-nTEPt7lJnzqH5yJXkLeknne60fB3yz0uKhu_23LFASETc7YAZVKh4ELHwpNlvt5J7CsEjIcvk68SM2e6Pa-PaY0rsLpSEXc6dakGcb9auEGZETXCoE7HUrIq2AH_YdEkpHRHob7lq5dLDWxIh-RebspejWMQyVvlgz30oFxC3QDMJKW4XbExe0zrZEk1Hn2GMuwOLB8lUT23jGyTGmjlUlVeibae7cQQWF5XCVzGj2FRhF_nkiIZfZJCT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خودِ مردم راوی ایستادگی و مقاومت‌شان برایِ ایران هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467373" target="_blank">📅 22:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467372">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFJpp8jB0Wx23kqP0t5_oAU7O7zVFbGbeQzBmMBuTTNNcuv336m-ezlTh3FuxCcF3Lo17j04bc9fZYlLMiRdCrp4eZgPC4x6cCcLPH1aVUfmDPOlThyEztP-yRP-_FhW8rdg-rXhijE-f5CsUz9_OEItJQM1__hwZNKZritXIXWAvZb9ZoX2lHGjfiQ7MsE3iJEnKXiAwJMUtThu4BvGxLaQ5ODggXxdlTbFx1BD9qmZqb3Ciwu5NmYwikApH-9P9fvCeWduQwLzfuyMypQumlBMlKTslBVoiD_5GZJlF10r_3jsApAttKb6Lf4oHz1FO4Q5sxzxEqSUhyCJBwHaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حالا نوبت دعوای خطیر و کریمی شد؛ جروبحث دو عضو هیئت‌رئیسهٔ فدراسیون بر سر تمدید قرارداد قلعه‌نویی  @Sportfars</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/467372" target="_blank">📅 22:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467371">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maJA_zalTWhCPp92YfY7qECzZ6LLT5jKFKvYcEPnN5cZPMawwt_PIY3969MmwmLR7Nw6lKH5DKq0I1tfpTTNbemI7oOZGbhTPCWMd9CrMs2E4KF7UPPoXIXiUEuTOZCbuXYYZja6gbi9Ua9o8riUpVeaVoRBQPNS01_q-XJxrYFy-R1gJi-DbvGOElK2dzsGKR2aM2FRZqVPqUEmv6iUMeUyZLplxthV2J9mPv_75Z79GWeCky3YquqmPL4Xxs1Ff-aUBj72jxJPpoOTlAAb6lPL7DqGgmTYNSow247r3xLbQ9Jy9ZhzlbDbjczQ69MW4tePY2oetnJQF0D-hckcKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به روبیو:به سرنوشت والرین دچار خواهيد شد و زانو خواهید زد!
🔹
رپیس مجلس در واکنش به یاوه‌گویی اخیر روبیو در مورد تمدن ایران نوشت: در طول تاریخ، ما ایرانیان با کسانی روبه‌رو شده‌ایم که خود را سروران جهان اعلام کردند و کوشیدند تمدن‌های کهن را از صفحهٔ روزگار محو کنند. آنان با آتش و شعله آمدند، اما با گرد و خاک و خواری رفتند.
🔹
کسانی که به دنبال میراث اسکندر هستند، سرنوشت والرین را خواهند داشت: زانو خواهید زد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/467371" target="_blank">📅 22:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467370">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c65ad3179.mp4?token=P_U_mz4r0bwvwrAWFkjQSvxWSuH148FgpluncsVSPjBXdR2WPz0Eu9zait6o-w4QGrVo1VZcfPX5mgdztbCKazxi4YQv0ejGEqs-kFHSMKAO-GrJjFhQbj8fqBligdZ1WBFaby0u-6wmAaqgQ6d35ku4pgId_NtstFn7dzHzmlaPQBcaihdaEKy7fUgWFXwYDgXpSZLiIyXOFTNl6hMUna1BgKt8ruo2p4ye-CsqjnexeBecjucpuhIRhU4T-kjUe2tYqBTo-g4AovCrm5wruLLGRub6JiCGl97xGqhr33-ncRauTTBxDH64Or7VGFgWIWLPupaCS5Auf2T20VDy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c65ad3179.mp4?token=P_U_mz4r0bwvwrAWFkjQSvxWSuH148FgpluncsVSPjBXdR2WPz0Eu9zait6o-w4QGrVo1VZcfPX5mgdztbCKazxi4YQv0ejGEqs-kFHSMKAO-GrJjFhQbj8fqBligdZ1WBFaby0u-6wmAaqgQ6d35ku4pgId_NtstFn7dzHzmlaPQBcaihdaEKy7fUgWFXwYDgXpSZLiIyXOFTNl6hMUna1BgKt8ruo2p4ye-CsqjnexeBecjucpuhIRhU4T-kjUe2tYqBTo-g4AovCrm5wruLLGRub6JiCGl97xGqhr33-ncRauTTBxDH64Or7VGFgWIWLPupaCS5Auf2T20VDy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم رشت مثل تمام جمعه شبهای ۷ ماه گذشته نماز استغاثه به امام زمان (عج) خواندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/467370" target="_blank">📅 22:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467369">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شهادت مامور فراجا در حملۀ تروریستی در فاریاب کرمان
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/467369" target="_blank">📅 22:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYDSYNOHGV_HNQskSvgqCkeKYuDpsOf87cxcM_4lm3FmQsQxYdF_P1Rkeu-BwBhR2ei6PB6PXVh_OSayjEPn7SidmX9C9VeRJ7PhGx7MC7DXM7KSyAnjOSZKVceiV3tCrr6vlF4tkTbR5m0CErr2hzBVKbpgznOmLsfsPKM6PRhArtR7_S726sICF6FcGqVsID6d2AUrP_tLgquo_reqyI6NVOLC4BzE8ZrTE-v65fchOs0btuQjl7RTHVD8jSNDGLajNLTShR3-F-mw1bH_XE6R2_cBQD3hTNFfTz_PI8-M41owycriZY2LmEONNl8-dmMNQaEUumoluKUMYAvkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ توافق با روسیه برای تأمین گازوئیل
🔹
رئیس‌جمهور آمریکا مدعی شد با پوتین توافق کرده تا مسکو بیش از ۳۰۰ هزار تن سوخت گازوئیل در اختیار آمریکا و بازارهای جهانی قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467368" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8698bd0285.mp4?token=Olo9_324RvL_TJ22bK4lNw7LNCrW_IAOpi1P517jjSYGCwvlNXjCOeo4zx8Bp3vBTEa1w4ut5Lk1ZjFm5gtotebeKZhBGuGbkIO6HDMFLDos9Sr3M7lDRW2heLQczCjmqJGY6vqa_HxM20z5ZJlqEEkCFCo8iwKsFio8fgyg-raM9X2_5gxWwb-nxTRz9yTNOyLUOMvRU9K3gzEcX-3RbiH2xdp0Z_BDZcrfIfCPBhtbGquSQYRc2OAn6obrzF64vVL_ZRahor4oexnYgt3ItF6-mpvg8oYoExZ5YMpZd5WkpqR2L1ZTxBHIciHK95CzaBjrLhXcqFeQbS_KQPc89w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8698bd0285.mp4?token=Olo9_324RvL_TJ22bK4lNw7LNCrW_IAOpi1P517jjSYGCwvlNXjCOeo4zx8Bp3vBTEa1w4ut5Lk1ZjFm5gtotebeKZhBGuGbkIO6HDMFLDos9Sr3M7lDRW2heLQczCjmqJGY6vqa_HxM20z5ZJlqEEkCFCo8iwKsFio8fgyg-raM9X2_5gxWwb-nxTRz9yTNOyLUOMvRU9K3gzEcX-3RbiH2xdp0Z_BDZcrfIfCPBhtbGquSQYRc2OAn6obrzF64vVL_ZRahor4oexnYgt3ItF6-mpvg8oYoExZ5YMpZd5WkpqR2L1ZTxBHIciHK95CzaBjrLhXcqFeQbS_KQPc89w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی امشب هم بر دوش مردم گرمسار  بلند است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/467367" target="_blank">📅 22:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e9475d72.mp4?token=jp1gfgUq2H0120dNBOHq0nNa3-jLbcoyfBXq0rCtkTFD677gYNFkf-FtN1yLHcnwXKY4nLfq2J4flj2pEfjdDw1v_k6grgPbP45X-Rpp0eFcU2Idof2JO44QIdqqD5VF8R9qj1dX26p5gOkVBjTe6GYlC8XHIeblkr2B4Bq42zbesb_A3_iYG2jiW0LyycgUKALXOIx6GmNPhgygo6UJaqtlnqjngi5ha7ks1b2Ks-dmNSMXboR57p2D66TYxapzhXU8h7ZkE8j5kWnVth3fl_fL_H5QS93341J8pptnLmnonfdkrcSMSws9azFo7R0Rrk23JwIM4Tx8b-Z-NhGm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e9475d72.mp4?token=jp1gfgUq2H0120dNBOHq0nNa3-jLbcoyfBXq0rCtkTFD677gYNFkf-FtN1yLHcnwXKY4nLfq2J4flj2pEfjdDw1v_k6grgPbP45X-Rpp0eFcU2Idof2JO44QIdqqD5VF8R9qj1dX26p5gOkVBjTe6GYlC8XHIeblkr2B4Bq42zbesb_A3_iYG2jiW0LyycgUKALXOIx6GmNPhgygo6UJaqtlnqjngi5ha7ks1b2Ks-dmNSMXboR57p2D66TYxapzhXU8h7ZkE8j5kWnVth3fl_fL_H5QS93341J8pptnLmnonfdkrcSMSws9azFo7R0Rrk23JwIM4Tx8b-Z-NhGm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گناباد، شبی دیگر در امتداد ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/467366" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06b82efe1.mp4?token=iN-Hw35smnr6Pvay4MkqYvZtQlKyVtob1KQf5tU0PkNXAVIaW_CcfgbIaX10NFi2x8a-Xu2IP4iC2V8LbfWtQhzFBw0phGAoDqgpwt8duJVUIU9XnKKn9wgS3GKtuX3aOHxVwkp3E7iRXpzLTKX1AzP8kCGAy68A4ediRvgAyB-oAv9V3P3AjnTEeJ-W44qvGWRM1NGIRpDT2KvnvIawRoI8IGjxKD735-E-2Kt5JM2cTilVR0_25UiSsUxH0MK8nSVJ76mjjuPd4PlE2A0ztGKwsxg2KGVCojHYd2l-rR2ORtFQzkH3e2jKh0q1_LJ5PfleblmT2U1EGEkl4NTlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06b82efe1.mp4?token=iN-Hw35smnr6Pvay4MkqYvZtQlKyVtob1KQf5tU0PkNXAVIaW_CcfgbIaX10NFi2x8a-Xu2IP4iC2V8LbfWtQhzFBw0phGAoDqgpwt8duJVUIU9XnKKn9wgS3GKtuX3aOHxVwkp3E7iRXpzLTKX1AzP8kCGAy68A4ediRvgAyB-oAv9V3P3AjnTEeJ-W44qvGWRM1NGIRpDT2KvnvIawRoI8IGjxKD735-E-2Kt5JM2cTilVR0_25UiSsUxH0MK8nSVJ76mjjuPd4PlE2A0ztGKwsxg2KGVCojHYd2l-rR2ORtFQzkH3e2jKh0q1_LJ5PfleblmT2U1EGEkl4NTlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترافیک سنگین در دو مسیر محور هراز
🔹
حرکت خودروها در مسیر هراز به کندی در حال انجام است؛ حجم ترافیک در مناطقی همانند پل لاسم، گزنک، محدوده آب اسک، بایجان، منطقه چلاو، تونل سپاسد و نارنجستان بیشتر از دیگر مناطق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/467365" target="_blank">📅 21:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d9e35815.mp4?token=L1WaEyXHxXNaadg-ZtTDcfb_e--Ycij199FuhMUKjR1kooPC_YrYst374oynhPm64xqZkJxUwRExJYB16RvAu1QnIcHjqzImykICEhpg-YE8Q_eZ2R1fuxGAv1MNQg47LtJKW8sypuJKHJqwTUAid78Twtu8018Q1LHGnXEN7iqL5-VFtgKMEoP5BQsxjhR6lkH3Q_K9AAJrXxyrQITeeXx6d-nrn2GpAaKNNIXJsNa1ZyDUWvMKYBsA6wlEwd0_P3YqPXjTx3cE4TvGyfDOzTyHfRKdy1lZtljsxNaNqUTyjBFjqEOpm3z3HFClAktxQW9Oc2xS7QiH7KdRYEdgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d9e35815.mp4?token=L1WaEyXHxXNaadg-ZtTDcfb_e--Ycij199FuhMUKjR1kooPC_YrYst374oynhPm64xqZkJxUwRExJYB16RvAu1QnIcHjqzImykICEhpg-YE8Q_eZ2R1fuxGAv1MNQg47LtJKW8sypuJKHJqwTUAid78Twtu8018Q1LHGnXEN7iqL5-VFtgKMEoP5BQsxjhR6lkH3Q_K9AAJrXxyrQITeeXx6d-nrn2GpAaKNNIXJsNa1ZyDUWvMKYBsA6wlEwd0_P3YqPXjTx3cE4TvGyfDOzTyHfRKdy1lZtljsxNaNqUTyjBFjqEOpm3z3HFClAktxQW9Oc2xS7QiH7KdRYEdgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محیط‌بان منطقۀ شکار ممنوع سوادکوه مازندران در جریان گشت‌زنی روزانه با گله گرازها روبرو شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/467364" target="_blank">📅 21:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1f2962c2.mp4?token=Xp82YwfcbrfZwUC3xcFfppUfRjosrJbcykmCy5f1xtDMP1tHzW53F3StZ3TtX_cuALdLU8E7YCeDK7P_E_3w9FG5hKV9QSdRYLKKhFAMXpQ3YkNWGGt6Di01f26SunUD1eLufC9ULzT-ei0sRGQ-XCMqMbKxB63R_ynv7IBh-OAwLGIRqNcw7YPhpqfs6ESl05owpKq0OT2iRxTUeJHx9n-K8KnEhUudOrRP5MLMt9D-0_cMQ5CsEL5pGhv6tC8Tthg-O94L1DHmmifJiXwmSJWZIjnUyJaUoBFuLEjhMn24QHfpCDz7ze-WQDTKxSKxoFzj2wkHqaVTW_UbGba9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1f2962c2.mp4?token=Xp82YwfcbrfZwUC3xcFfppUfRjosrJbcykmCy5f1xtDMP1tHzW53F3StZ3TtX_cuALdLU8E7YCeDK7P_E_3w9FG5hKV9QSdRYLKKhFAMXpQ3YkNWGGt6Di01f26SunUD1eLufC9ULzT-ei0sRGQ-XCMqMbKxB63R_ynv7IBh-OAwLGIRqNcw7YPhpqfs6ESl05owpKq0OT2iRxTUeJHx9n-K8KnEhUudOrRP5MLMt9D-0_cMQ5CsEL5pGhv6tC8Tthg-O94L1DHmmifJiXwmSJWZIjnUyJaUoBFuLEjhMn24QHfpCDz7ze-WQDTKxSKxoFzj2wkHqaVTW_UbGba9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامه نماز استغاثه به امام زمان (عج) در شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/467363" target="_blank">📅 21:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10040e9d0.mp4?token=j2Ug4WarqoKMJKHwHm5AXainfMBr0nmgh3Z1XycbA22Kn-AjTsjnjM9oPXGzj-UkE2H_73UD5aOWTx0yqbSCjjhaTQjEC34LmZ7w5E2FeRX3S1UFoarIqLy0dOwEyw6eboV6Ur-hoCOAmlP8zAThwQrkeSfMc3IV5li3F859tetegsIelRgNpl0VrdKoMb7PTDZSJpByzH9cBYim92Yy7NWPMdRZW33RP6wcApxODWIzFKz_cYwFYeb-lYSqERqjbW4gKuM45UYbBRB3Wv_QStuIXpXs77p47NlVhsZxfVtvpt0PyUWgCCSQP605rexWQX5pV29pI2Rt5W5eXpu9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10040e9d0.mp4?token=j2Ug4WarqoKMJKHwHm5AXainfMBr0nmgh3Z1XycbA22Kn-AjTsjnjM9oPXGzj-UkE2H_73UD5aOWTx0yqbSCjjhaTQjEC34LmZ7w5E2FeRX3S1UFoarIqLy0dOwEyw6eboV6Ur-hoCOAmlP8zAThwQrkeSfMc3IV5li3F859tetegsIelRgNpl0VrdKoMb7PTDZSJpByzH9cBYim92Yy7NWPMdRZW33RP6wcApxODWIzFKz_cYwFYeb-lYSqERqjbW4gKuM45UYbBRB3Wv_QStuIXpXs77p47NlVhsZxfVtvpt0PyUWgCCSQP605rexWQX5pV29pI2Rt5W5eXpu9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۲۳ شب ایستادگی در میدان ۲۲ بهمن ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/467362" target="_blank">📅 21:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7470cc38.mov?token=Mk0kp1x7KW2h527BnOtPDC27uh3HjFReH162J2Vqa0XaWFtaN05JMt4FIdvow3L_labToBLFRfvSG3PB19HWH2mlEi3T2W8wT9BXR7aiopl3MOew7eXUnT4Du7H-Z4iS6QqP4WFSb1W28HhHuEJBZW-plwmq9lYK9yRwIjKzF_A0EmTtKSBkHM_Ux4cexUCPcZBxpdadfEFho7HINErdOnyRFLQHKYLuhko3hnDoQNks6pM2RChY8KEPm01IhDKoEBxDU6l72sth9TwqBDVf67Vx3uxLs1-enDQBs9d-jsNqR8RgNr_oJj4osHg1_CYV3_OUqHSRBS3fT--Yglxd8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7470cc38.mov?token=Mk0kp1x7KW2h527BnOtPDC27uh3HjFReH162J2Vqa0XaWFtaN05JMt4FIdvow3L_labToBLFRfvSG3PB19HWH2mlEi3T2W8wT9BXR7aiopl3MOew7eXUnT4Du7H-Z4iS6QqP4WFSb1W28HhHuEJBZW-plwmq9lYK9yRwIjKzF_A0EmTtKSBkHM_Ux4cexUCPcZBxpdadfEFho7HINErdOnyRFLQHKYLuhko3hnDoQNks6pM2RChY8KEPm01IhDKoEBxDU6l72sth9TwqBDVf67Vx3uxLs1-enDQBs9d-jsNqR8RgNr_oJj4osHg1_CYV3_OUqHSRBS3fT--Yglxd8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: نشست سه جانبۀ ایران، روسیه و آذربایجان به ابتکار روسیه شکل گرفت
🔹
بعضی پروژه‌های مشترک مورد بحث و توافق قرار گرفت که همکاری اقتصادی سه کشور را دربرمی گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/467361" target="_blank">📅 21:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
بدون تعارف با روح‌الله رستمی، پرچمدار کاروان پاراآسیایی ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/467360" target="_blank">📅 21:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ae424ebf.mp4?token=Dzs0tZMc2N-23uoOLbLS6Ksd7E7hq3a18OBf2EDJDZclyOFyo8SzRQVZF14OSMexnuWb4zilox7wmvOTHrjDjbbVT0VlLJP2xS--20CQidl2mW-OJ5za4_Uk986MUtuUkBW03pMG70Zlj7lCw_o3hl5RcSQ-0L8b8o96l5-wJy8vZ_WMFdzjczHwyCf2slHo-81GM64xNQvlrrItd8s4q35CpnMfTmCBvOTAr3g3Oo4sfePdKZxgt9SsUJry-6VE90t6doZNwquHzG1L3psmZHkb8qsMUEDEV3h0lH9-znejlRlW6bw2Sk0hbpWQe0M_J0smydUkbg0tMK079cd_yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ae424ebf.mp4?token=Dzs0tZMc2N-23uoOLbLS6Ksd7E7hq3a18OBf2EDJDZclyOFyo8SzRQVZF14OSMexnuWb4zilox7wmvOTHrjDjbbVT0VlLJP2xS--20CQidl2mW-OJ5za4_Uk986MUtuUkBW03pMG70Zlj7lCw_o3hl5RcSQ-0L8b8o96l5-wJy8vZ_WMFdzjczHwyCf2slHo-81GM64xNQvlrrItd8s4q35CpnMfTmCBvOTAr3g3Oo4sfePdKZxgt9SsUJry-6VE90t6doZNwquHzG1L3psmZHkb8qsMUEDEV3h0lH9-znejlRlW6bw2Sk0hbpWQe0M_J0smydUkbg0tMK079cd_yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منشأ توفیقاتِ معنوی انسان در بیان رهبر معظم انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467359" target="_blank">📅 21:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhlUrnfCNL0oSRNYpj2wsyA0U2E_8uwh-29BrXOeKwlGMEg_m3wmM9M1LfPAqC_GHwa_AC5s9rebpmWGh3KhUVq3YcQyOHwf8s01d5BU5j0ybSambsHxVpJrg9WfFzdxyE9A6rIyL30-5quIpptiPkPe4yqUpdjKnytMrE2yBHMROsgnvTZsqSVN8JuccUy6bFT_NVl0DxdJoA9xLAYHZ-KuCCqrytNJkqEkXgzRLpDuyzqHpgFAU_Lr1OHaDt-CvPDQleT6AbkJUHRFRWAelLvdjS--TuSH3w26y2SmH4mTbfpy7cSE1DMptma8uFLKdtKu9YbVERZsvUx1MDD9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  فلای دبی پروازهای خود به ۳ شهر عربستان را لغو کرد
🔹
شرکت هواپیمایی فلای دبی امارات، پروازهای خود به ریاض و ینبع را تا ۱۰ اکتبر و پروازهای خود به ابها را تا ۱۱ اکتبر لغو کرده است. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467358" target="_blank">📅 21:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">۸ کشور تحریم‌های آمریکا علیه دیوان کیفری بین‌المللی را محکوم کردند
🔹
فرانسه، آلمان، ایتالیا، ژاپن، هلند، بریتانیا، کانادا و دانمارک در بیانیه‌ای مشترک، مخالفت خود را با تحریم‌های آمریکا علیه دیوان کیفری بین‌المللی اعلام کردند.
🔹
این کشورها هشدار دادند که تحریم‌های آمریکا تأثیر قابل‌توجهی بر فعالیت دیوان کیفری بین‌المللی خواهد گذاشت.
🔸
دولت آمریکا به ریاست دونالد ترامپ با متهم کردن دیوان کیفری بین‌المللی به هدف قرار دادن ناعادلانه شهروندان آمریکایی در پرونده‌های جنایات جنگی، اعلام کرد که آمریکا نیازی به این دادگاه ندارد.
🔸
دیوان کیفری بین‌المللی در واکنش گفت مقام‌های دولت دونالد ترامپ در حال تلاش برای «اخلال در روند اجرای عدالت» هستند و اقدام آمریکا را «حمله‌ای» به نظم حقوقی بین‌المللی دانست.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467357" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRjEfVWFlMmLNWl8S42Vsz30CJ1AkbCtKFXkhIoUu5MSqGlUqvoVslDkQItouogfq2l7ZTonIKrKqse5GcZbWMpOyD2jloA0AU_jbArkqio3TeyL5JHKXDhnTwVIAOgLbEsVnKwh5UnbGYl0kI0nSjCqA82UAVOBNA6BmT55iScTyGDgrjpmQj_jGc3N3XdlyyOoCHEG8NvLSQOjUQHQLQSLLAAtaAgXSpv46m34shytNBgJTvAkks9MMQx85pkTmQwhx7U9FpuymBPvildlD6UaYDiWqWqXJ6zlW7GIODPeig3MJtjxQdE34S09AH7kfkn9CGoehoDRfTzg25JlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو طلایی تکواندو ایران در پاریس
🔹
آرین سلیمی و ابوالفضل زندی نمایندگان تکواندو کشورمان در سومین مرحله مسابقات گرندپری تکواندو پاریس موفق به کسب مدال طلا شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467356" target="_blank">📅 21:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9NUk_aBLYbsfnckUOWkj5uVYAwCmkQd02jeoJMgQK8KIQ6Jn8dMNq5ycdzrMnbu6t58NZdzSVJAhefEM1CtrfaN5GEsLWm1sfCt5dl_zBmPZQ4t0LNrHtd1jDkc4ZqBQF4iC-54F4_o0dLdrEuX1xIefl7s3PyKWwm2GZsS2e-HFPWM5P0u7inH7UByslkDxjKSeuvlFJ0o3dMNbTtTalFH9x72crvt_YAxr_RdRnsqjXPZf0yE2ForzPFg6hHhJi4STcfPGcUdH_q2num_zW9PNehVlSCEYEczyYjJj9cVoFaRzdzG9Q6eaA2S1_Rnm0FYTmQeXBf3E_WvX9CWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت معاون اجتماعی فراجای سیستان‌وبلوچستان
🔹
یک منبع مطلع از شهادت معاون اجتماعی فراجای استان سیستان‌وبلوچستان در منطقهٔ چشمه زیارت زاهدان خبر داد.
🔹
شهیده افتخاری ساعتی پیش در جریان منفجر شدن بمب کنار جاده‌ای در مسیر حرکت خودروی پلیس در زاهدان آسمانی شد.…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467355" target="_blank">📅 21:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084aee65df.mp4?token=D8sciSmBCrtoZcyIqxlMttkp1v5JO1sO_v4E0wO7-uSCmLKKRhRO_O1umXq8fngJHBdHP8juAtn6yFUseiJmt4ScLsjxbezvEzFq5nEO7L7Ka7g2l3uvRWOjjU9pH11dpanO9Jj0exlpxZiFT--1A_7sba6mmPb95In4_HiibR6AGwLyJYMRPEEdJgFeTNHVBTpPbkQe8dmULVdY3e_1gciBs0qG94lM4546aSOezn_2OBvBWpLzlt4vKSxxncLOmgE4r6VdMKayKxHz-y9v3c3yqz-97oGk-jYNPco5HbC40qbx2LdWBimzy67mK03OVaURS-_VMDMPxlI18rUqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084aee65df.mp4?token=D8sciSmBCrtoZcyIqxlMttkp1v5JO1sO_v4E0wO7-uSCmLKKRhRO_O1umXq8fngJHBdHP8juAtn6yFUseiJmt4ScLsjxbezvEzFq5nEO7L7Ka7g2l3uvRWOjjU9pH11dpanO9Jj0exlpxZiFT--1A_7sba6mmPb95In4_HiibR6AGwLyJYMRPEEdJgFeTNHVBTpPbkQe8dmULVdY3e_1gciBs0qG94lM4546aSOezn_2OBvBWpLzlt4vKSxxncLOmgE4r6VdMKayKxHz-y9v3c3yqz-97oGk-jYNPco5HbC40qbx2LdWBimzy67mK03OVaURS-_VMDMPxlI18rUqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ؛ از «اعدام نکنید» تا دفاع از پخش مستقیم اعدام با تیرباران
🔹
رئیس‌جمهور آمریکا که سال ۱۳۹۸ در حمایت از دو سارق مسلح که اقدام به سرقت از یک زن با سلاح سرد کرده بودند پیامی با هشتگ اعدام نکنید منتشر کرده بود امروز از اعدام یک افسر سابق ارتش آمریکا با جوخه تیرباران دفاع کرد.
🔹
او گفت: «ما برای مردی که ۱۴ سرباز را کشت حکم اعدام از طریق جوخه تیرباران در نظر گرفتیم. حق او همین است.»
🔹
پیت هگزث وزیر جنگ آمریکا روز پنجشنبه گفت قصد دارد امکان تماشای عمومی اعدام افسر سابق ارتش این کشور را فراهم کند.
🔹
هگزث در گفت‌وگو با رسانه‌های آمریکا گفت: «مطمئن می‌شویم که مردم بتوانند این اعدام را تماشا کنند؛ این مجازات باید علنی باشد.»
🔹
یکی از مقام‌های وزارت دفاع آمریکا نیز اعلام کرد: «این اعدام به‌صورت زنده پخش خواهد شد و جزئیات بعداً اعلام می‌شود.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467354" target="_blank">📅 20:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZxoTBeToWY6VOjJ2Irb_Dci75CLazljvC-cTMnJDeMm3zuDP0SNsadspuPIjNIk2JCdfsCphG1g3IhIR35duIiE9AWKAHrd4gHqm3gPcWgeqiCl4bAOzodAyVzv7pn8PitLswy2dkX47sc04XGjshzRw3J9GZmn_NzaxK5h7ecXA5BFBY81MP53kpbM7lI2tBWfUHMTE-FcTsKxnIAFrn3RihSk56TsAp8KGnpJS6i-GpcJIZIvCH8e3qxTa72sQaABh6p7pCSB6GY4cSZl2syDw561WA5ctdXLQ3oZF0OR2Jeb3p8g-vnd9Hpn_n3hyjbR5xiqZo6dXN6IW0B2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التماس زلنسکی به آمریکا برای کمک در جنگ مقابل روسیه
🔹
رئیس‌جمهور اوکراین با لحنی ملتماسانه از آمریکا خواست که به کشورش در جنگ مقابل روسیه کمک کند: کمک به اوکراین برای آمریکا هیچ هزینه‌ای ندارد؛ مطلقاً هیچ هزینه‌ای. من آشکارا گفتم به ما کمک کنید از آسمانمان دفاع کنیم و بر آن مسلط شویم. آن‌وقت پوتین پشت میز مذاکره خواهد نشست.
🔹
زلنسکی سال پیش اعتراف کرده بود که جنگ با روسیه را با وعده آمریکا برای پیوستن اوکراین به ناتو آغاز کرده اما اکنون می‌بیند که واشنگتن چنین قصدی نداشته است؛ او گفته بود: آمریکا هرگز، حتی قبل از دونالد ترامپ هم ما را در ناتو نمی‌خواست و فقط در این باره حرف می‌زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/467353" target="_blank">📅 20:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b55f86f9.mp4?token=JF4XCGA_EN9TpG_sCbx4eGSTVeEcbKCwEVRvJ3SjGoAiR7QUQJb31u_P3Has3XGlsrqCdfoDPkUuiyJWTfXpYuiR87hbZtjDC84w6QSiaTbtSaRaT7XpLecRiO9NF0W7er7H-TK0LDlvVeIzt9MwADuJ-ya8oaSA23zQH72PNjlRXUeqJOERv92QKIHH0ml_WleqkZkxesc0I_2aA8IkXeKk137Jk-dYu5bJFkynEYVO7KN8RXX5D-nBvpFnWv_cdfwoZWdFGDbVj5L0c5LELDrJdvjYqFSQ38s-mxKiFjv95ZMnPwOW2vldTJy4YNapbpCjkEnpprwmn1BR4hUlnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b55f86f9.mp4?token=JF4XCGA_EN9TpG_sCbx4eGSTVeEcbKCwEVRvJ3SjGoAiR7QUQJb31u_P3Has3XGlsrqCdfoDPkUuiyJWTfXpYuiR87hbZtjDC84w6QSiaTbtSaRaT7XpLecRiO9NF0W7er7H-TK0LDlvVeIzt9MwADuJ-ya8oaSA23zQH72PNjlRXUeqJOERv92QKIHH0ml_WleqkZkxesc0I_2aA8IkXeKk137Jk-dYu5bJFkynEYVO7KN8RXX5D-nBvpFnWv_cdfwoZWdFGDbVj5L0c5LELDrJdvjYqFSQ38s-mxKiFjv95ZMnPwOW2vldTJy4YNapbpCjkEnpprwmn1BR4hUlnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدیدی از عملیات آفندی علیه مواضع ارتش تروریستی آمریکا در عملیات‌های نصر ۱ و۲ و تنبیه متجاوز
🔹
این تصاویر که برای اولین‌بار منتشر شده‌، شلیک و هدف قرارگرفتن مواضع آمریکا با پهپادهای شاهد ۱۳۶ و ۲۳۸ را نشان می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467351" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aePzfv7DcuD-e1r_K2APAOJsdXGvQB_JWBi3FBtpB24s82fpuyfjHlgHMJFHMxLiBWjIIa48w9DNDp-kCMUCXjzkhJ3ixbJq6uxp0iHsN1YpDtkkNXcYZRFFQvoVLsOwoJY_MfJDtRLtFYAUIV0dyIRUXYtaCv3gut5_0b7lmpC6DOIu5kMCGLQA-EwF33oVwCz8HtDhCvB9yqbnpK7JIBOl9Pp1QB-ce1LELoTmZOE26cjlkqsNG4HGPxRqCVBi13iEKcFfRwnBgsfZJabsONx3pE0g-1qr6EQV26GWSRWMPPmTTHDyta6GCW-UhdB-4dwJEgLjwAwKoRqs-CL-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
علیرضا دبیر و محمدرضا گلزار به تمرین امروز استقلال رفتند
🔹
تمرین امروز تیم استقلال در سالن وزنه فدراسیون کشتی برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467350" target="_blank">📅 20:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af42fe811.mp4?token=KvCf2NdHQ_4-2y81hLWBOSaMoUS5XD55Kmx74dqsY933Z_-RTjptHOD4gEyOHTOvzsNuv7JH6sXVrHSzj9OrxEz4JIceYN9dE3o-3c3JyStZ0RzBDpFvZwsguU12kpXdUx5_UWeRb99OsOC2WFDCIA4IUs22IDEwOpJY601a-ljdSd1DJ7e6iaBLzS7VXwWM2Bla-ujQAJSwWtmR1gHv1wqSmGvYm2eBu7qz13v2slndkOqPhzRIOHjpUFaT3bE-STjCva3fBL8yBM_dVhsdvwFtEw_1ol0Pq1yjsxpjYU7V-AFE26VmiM5xkN197qlRbto0plwih0G5vkmc6xvaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af42fe811.mp4?token=KvCf2NdHQ_4-2y81hLWBOSaMoUS5XD55Kmx74dqsY933Z_-RTjptHOD4gEyOHTOvzsNuv7JH6sXVrHSzj9OrxEz4JIceYN9dE3o-3c3JyStZ0RzBDpFvZwsguU12kpXdUx5_UWeRb99OsOC2WFDCIA4IUs22IDEwOpJY601a-ljdSd1DJ7e6iaBLzS7VXwWM2Bla-ujQAJSwWtmR1gHv1wqSmGvYm2eBu7qz13v2slndkOqPhzRIOHjpUFaT3bE-STjCva3fBL8yBM_dVhsdvwFtEw_1ol0Pq1yjsxpjYU7V-AFE26VmiM5xkN197qlRbto0plwih0G5vkmc6xvaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهتزاز پرچم سرخ خونخواهی در آیین جمعه نشلجی‌ها در استان اصفهان
🔹
اهالی روستای نشلج کاشان  پرچم‌های سرخ انتقام رهبر شهید انقلاب را با خود به آیین سنتی جمعه نشلجی‌ها آوردند؛ این مراسم همزمان با هفتمین روز شهادت امام‌زاده علی‌ بن ‌باقر(ع) در مشهداردهال برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467349" target="_blank">📅 20:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itu1vT5DWI6T2yCw67ZoXcCm6dl8l7gDlhq_okRSdRYeVF8PyPk23bBVd-eKZWqMN5bT3YMUqpou6Bzf57snjV4MWCGL7wng-4O2ov2Q6OEYcaWMFWyLd0a3OZfR8m2KEKWQW6kPtHLZvOsyRvH7W2t_UuGgtOuY6uIUTgmrixYXy8UEmoWro3rWZSj3Bhb-SokHLnNuj2kaN509FX6DgpfEKwx0H9K3LNgucSi0sHMTbXsnlUk0YR6t1ABufhQhrIOgcNeBogiR2vOfNazR53QorFbwEbJp6KOm8F1RrnAnWQaOoflwyNvy36T45O1FillXm2RuhB5fvy0VhyT29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی به آمریکا: برای تکرار شکست‌های تاریخی از ایران آماده باشید
🔹
سرلشکر رضایی: وقتی پس از شکست و تحقیر در برابر ایران، به آتن می‌روند تا روایتی از جنگ تمدنی را شکل دهند، بهتر است بخش مهم دیگری از تاریخ را هم بخوانند: جایی‌که امپراطور روم، در برابر شاپور اول ساسانی زانو زد.
🔹
کسی که پای تاریخ را به میان می‌کشد، باید برای تکرارش هم آماده باشد!
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467347" target="_blank">📅 20:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8f3d265c.mp4?token=kDct4VrQETe9RCOC_uyAwYcda7e7bySnie9JFLba9CdnH6PH50peXoHl3S8zpbTw1A_yHJjAWmLP8D3pjcKYW9dy7uDsxy01Hnhus3qrVjy1ii2UYMEdnUu2SyI2SzlXuHw3auAdKRJygB4WAXj7cAwBlfM4pyNMR6blMDZcHJGpyXamP8J0BvkrMu7G2_n0GUFwuqOC8c7KHBitk5I7-vxC4ESI-18fPtw7CfRdN4BRBxGthdZdt3xb43z4YXdGWzD8sA_S96SNmR0FW9QmkxAXLiS5rKskztGq7e_r-qwMW4Gc8faSE4VgTMrA34J6rQGeCN-MNeXowNSufIdrcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8f3d265c.mp4?token=kDct4VrQETe9RCOC_uyAwYcda7e7bySnie9JFLba9CdnH6PH50peXoHl3S8zpbTw1A_yHJjAWmLP8D3pjcKYW9dy7uDsxy01Hnhus3qrVjy1ii2UYMEdnUu2SyI2SzlXuHw3auAdKRJygB4WAXj7cAwBlfM4pyNMR6blMDZcHJGpyXamP8J0BvkrMu7G2_n0GUFwuqOC8c7KHBitk5I7-vxC4ESI-18fPtw7CfRdN4BRBxGthdZdt3xb43z4YXdGWzD8sA_S96SNmR0FW9QmkxAXLiS5rKskztGq7e_r-qwMW4Gc8faSE4VgTMrA34J6rQGeCN-MNeXowNSufIdrcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هاشمی، معاون وزیر ورزش: ۶ ماههٔ دوم امسال ورزشگاه آزادی به بهره‌برداری می‌رسد.
🔹
دولت ۵۰۰ میلیارد تومان دیگر برای بازسازی ورزشگاه آزادی کمک کرده است. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467346" target="_blank">📅 20:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467339">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4JESQwIg_L1c5suL_331-nzRYCvyIpgU4IcgQ5dVQJp0mvVHBt2RZQyfr9JgjKCLMHB6UaNqUf7q7whWWj488p78G0c6EMFi3ogqjBDmNkZB3hVgXVqC1BF6nm7QnrxXIIQfmtkpu-9AthhML0mGLu4RawiEW01IfUix5p35KOOEc6Izj-nlEwzt5K7iN9YHLGBL6H8D6BAGfkLHoDGmClbqUAw7Q0NpYI7A4dYfkvQCh2eooZksyj_p5Nd2Wnl7peEMJlrhWCY6DDUzd9o6DhKqXAAhObSisjfaS03sx11dAQ4CAWRzkeqwU1oUfiaPObsIqnGNUxSIYY1LyE5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvGDmAMT5Ys-nwsW6-rV2nNvh0fueZfhPrAaRP_vHZE6HYr1HZlcAGbIpUUW5m5r736A55WVKdRY7Z1VD6If2xntl8tOWFc4qEKUncwtNN4LJV2QNCLRgDWPkiZsJueI2UykbBEW58R9nTidEomdUJEywJo1_9xa89Qn869WTxLXvDVgdJZFdM0DblIQ5L4ZZNUDroJRv6PkQbE-KpZztCz0yuNcqRf7ukMUamq2woDP9qEXM7qrpw5DmGvqbnG_Gjt5LfatVg5qpmUJSvqhvzfvkf4xKfT_puonNXrIceNItVKm_pr9-BnndNTSBMJ2PHNuc4fZO6ecm65wg8gLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnPOyxn7hM4VoVOS_VlKH3gSdSLTQiYmV8NW13dzQcP4YJPC9TVpfck1lI5S0WVtSiMSXLe5G_ZVfO9YduH0Pw5xH87dmg34YEm4wCO2Q4KbTF7qXqB7EMSsoSId6G67f6I1HCumU7qxlY1bqXE1efe9hHc5R45FcgtJ7_001Kf_Da4vwedJ7XHh0VIyycZ5nbPJ_xWcgJKz1zsX9noQ6VZ72Pr7ZC2NgYMA22tXGeW9MiEKWEup6BHsEL5DFYfVvAbkWHlRxhuyXlAukYr164VvAE95VcKhI8SH0Lq4i0F0jJQr7r_h2gRuOK0yu2Bpt762_H84bplUzN6E5ksVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QX5Qamxg5DtJTKtGVfaoddSPd0RgHlEWhWJfc3WLauJCnOGUZCQh_WLXGYOLT4yM0jjT8SQcDuZezMfpkHpWedbyVjeDDI2L8tCmtjPHlTqee_DE3uQiMjY2xneJ8EMabfzZnxNvc4alL-6L1jHXXdQqIZcJoLbUNLFog2VeWCoC-tUzXbNhMgd-EMqo9QPx-LVzV458qcHdBMSsnm2tBkb56UFot__jGgQAiiD1C5lVe0RNEjIuzy5GxI2-Vc4XkSh719gsTevwgakRorVmN2ZeoQwnjMVf3WKQAcAMJyPSLBN1_ZL_e-TaSoBXkXXedBN04CnOycFCdlKxjIcClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5f9BZOZ1f2DTe69vBagzDMJfuJuZbuia2BrCWzx_aqWf7KG-XBBr8ODxiLuf22u7z3xp2njL_EpSxRsW48fcFe7ArOIAujZyi1IG7wAG5BSCNzRM2rSZqo1L_LSjWeUxn8hGKEhlDw__jpdyHigeoPuRvRaohEzMan0sFusQNSfkzdrrSeZ713bza9gDPhdg_ll1E8tkr6JZJ1sEXH9kvUFe-wwWGyR8usUJvcDy1oXuEPHqHpnagyPOssRd1bC4WVk2ZJOvPBOK-kj4I-ubQ2vGfixQCGMX0qEhmYAegKra878aJY7SV4BQIpC9ffa4ND31XefUfmVCONdaCgr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNOqVqI-X8WczRHR_wX9G-fRHMqkLYS5usjE2zzBx40U960lFLT7AWwUDAu4sNTNWQ1vT_-PAtN5iM8t5tEew1kYaHh65gweWm0cGHfruRdGPn4q32PZIvBo-_znlA6N3hKmVT1LOR3yC69ibNA2p1Gg4zY6GhloWr5oFDT442CZoph2GGl5aPiHYc1VBPCW8STnrkxKS0R66S3kxviIi2Yzrzt4zQkEViHgsy7JGEiS__eH5COgaR1b9sKCj9cPpIrkE3YF9pHm8smjYY4aRIOgYRyXVf9F1FmEJrtON6jpZKJH7s70oz6HLbeiUvWuVOXP1lJrAiADDf8ui2gEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiOupRRcl7J83bBk23hstYg-PfojkXXnHEn2kj7pt9Lwqeirq0VsEZiPZP0KxVhNCNkB40jFhwpNGvRMtlgYBx1dehpLjsYstGFqT1JgMUpUyg167U9p1Rh-cdNFcUCpEQnvFZeK8d7A9IXr8CvzS-PBwetFl_aoSEGeV0kajvk-D3-M7q54iiwhr4yUvHz8snCJv59SPZcbrlrQjswpToTIN_vTUZjeQX7LxWPguGcZcM-LdhA6fFF2MNFt0VO3HqeNRV9xX2j5992ko1njTXy_quns04h-GxdHLJTCblSmvifKbYlZLqk-wT3WX3nVP-43C0HHyiInr3Ouwgl4XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز شاد کرمانی‌ها با پیاده‌روی خانوادگی
عکس:
مهدی امین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467339" target="_blank">📅 20:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467338">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mctyu5NUAq1EZFUHasoOViqa3kglEqBVBsk0V0lC9_3_IHhperDAytDUiKzjJoOw6R8Alclfrb4IxoGhVJ4OwUf_37ACXbak7WOOjvZ4xe3zziFesphJtpBLu3ok3M2nH9r85yt6_rEQ7fsiTPonLUJtMIaQpKqPnn3IuFPduAeK9KKML8PxSCF8ldfe6R3PxALOOuABfLrpo83xguYE_FEroy9MloCfxgVbqrr9Pxi9lcGcl1SvyNVdnYXJurUxoT-5SLUI8ylFcsgATJdf2Tsi9EwOdvCT3CYGePTHs9YYYchHCvjP87U5qBmi_ULWqrc8JkuMwYy4eG6kwZiZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آغاز تحقیقات عربستان دربارۀ پرواز فلای‌دبی بدون مشارکت اسرائیل
🔹
عربستان سعودی پس از حمله هفته گذشته در کابین خلبان یک هواپیمای فلای‌دبی، تحقیقات مربوط به ایمنی هوایی را آغاز کرده است.
🔹
رژیم صهیونیستی پیشنهاد کرده است در تحقیقات ایمنی تحت رهبری عربستان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467338" target="_blank">📅 20:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467337">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPQBaf9l3tBoWPaLNAUlWLvqJKFGNRtWEkw1pMv-KN4vc72tMYe5rwN9tCw0fCtEQPNs2z4gWJbOs42hgpD8HK4qfCzjVfsTSQfbvMpDfQKsnBtPbc1RUIx-7dJETPM0UUnQ2-L3Uk1rfmCdTuskfDs_qklpEPqapbI-Ed6l5qkbMQ6oAEv6Dl3_p7yCcgZRx_IXKx3sAvUb7jMVoDRZrVT3Pir-Px-pqjdx8TxC-hYsETPaha147NwH27wjtsk4yE3XT0ezjgTyZsNba9nYTMGtgBHA9i9tut0ktvEkVyAHbrjC9YNobBhSs6f_g7zzwalRtAkN00oqX7-RWteLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه نشانه از شکست راهبرد انزوای ایران در محاسبات غرب
🔹
به باور تحلیلگران، سه انگارۀ «عبور تدریجی ایران از محاصرۀ اقتصادی، تداوم ضربات ایران به نفتکش‌ها در تنگۀ هرمز و حفظ آمادگی نظامی و امنیتی ایران برای مقابله با تهدیدات خارجی»، محاسبات آمریکا و غرب را تحت تأثیر قرار داده و فرضیۀ شکست «راهبرد انزوا و حذف ایران» را تقویت کرده است.
🔸
تحلیلگران و کارشناسان می‌گویند که بهره‌گیری، بازنمایی و تقویت انگاره‌های فوق در فضای رسانه ای روایت پیروزی ایران را تکمیل خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/467337" target="_blank">📅 19:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467336">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuGLaLNPB8FtXDGo9gxpfBQrUhqXicd3E1Lxa7vp_0UiFvXx2AWJcUP3JfWqjhx1Ns-O5LQpVY9YFpHjRusLNHw6TCwgr_9Velyvjh-5zJeyLoM31UAyUae0jiUb_sTjMJd4LHKhsBjxyvW8MN8kvVVo2bZT9W68GnkE_RVuz5SsnEuWlpcm33G6YoW6dHk63K_QuJVqeTZ8xMkv8th-AdYoX0ep2W16ZSrtcgTfyXoNFTYlbssv_vPS_-_Yx2e9FelROiOACExeGtMazlzt0lXexHF2ofVMkMsQ4Sitm4UaqfiJkX98KNDSPOJ2aRSlzh1JQ1zv2RNaNXfOr3hHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدارس هرمزگان فردا غیرحضوری است
🔹
معاون استاندار هرمزگان: فعالیت تمامی مدارس استان فردا در همۀ مقاطع تحصیلی به صورت غیرحضوری خواهد بود؛ نحوه فعالیت مدارس از روز یکشنبه مهرماه به شرح زیر است:
بندرعباس
فعالیت مدارس در تمامی مقاطع تحصیلی به صورت سه روز آموزش حضوری و دو روز آموزش غیرحضوری و مجازی در هر هفته انجام خواهد شد.
قشم، سیریک و جاسک
فعالیت مدارس در تمامی مقاطع تحصیلی به صورت ترکیبی از آموزش حضوری و غیرحضوری خواهد بود.
سایر شهرستان‌ها
فعالیت مدارس در تمامی مقاطع تحصیلی به صورت حضوری خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/467336" target="_blank">📅 19:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
شرط یمن برای پروازهای فرودگاه ریاض
🔹
یحیی سریع سخنگوی نیروهای مسلح یمن امروز گفت فقط پروازهای بشردوستانه‌ای می‌تواند به فرودگاه ریاض صورت گیرد که مجوز پرواز را از مرکز هماهنگی عملیات بشردوستانه در صنعا دریافت کرده باشند.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467335" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467334">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e625a1a11d.mp4?token=fsNe_qvJCj2sO2T5gisKe06fEZRqRT9kvd29xTdwB-GaHEaGKx-ZZSXd8IRStpmDmkDFC4tjfapoxbG2cVhfkpCntfOKP8vY_rSRiCXz3SIXPr21IstYBYzhDXqqOCYqrtdBpNvoeHly8HrkrmqjJsRJLnbE3UDpPjuSVIVzUPU-1ExG6fCbj3RTBt7cbC7n_YywcCmWW2iYLymh3_TPv3Z9xJeE7XC3b0v5xu_qdCq7BlTSLqEPv1ADNtRrKkU4ac1E0M6g8s1aedGdxvMnRJU44BslyDPat-jXRPETSLF2VZvJDVU4gqzjTJQqNJzyXBcGQJGLhHEsshFddrC7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e625a1a11d.mp4?token=fsNe_qvJCj2sO2T5gisKe06fEZRqRT9kvd29xTdwB-GaHEaGKx-ZZSXd8IRStpmDmkDFC4tjfapoxbG2cVhfkpCntfOKP8vY_rSRiCXz3SIXPr21IstYBYzhDXqqOCYqrtdBpNvoeHly8HrkrmqjJsRJLnbE3UDpPjuSVIVzUPU-1ExG6fCbj3RTBt7cbC7n_YywcCmWW2iYLymh3_TPv3Z9xJeE7XC3b0v5xu_qdCq7BlTSLqEPv1ADNtRrKkU4ac1E0M6g8s1aedGdxvMnRJU44BslyDPat-jXRPETSLF2VZvJDVU4gqzjTJQqNJzyXBcGQJGLhHEsshFddrC7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تحریم علیه ایران، اقتصاد و نظم منطقه‌ای را تهدید می‌کند  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/467334" target="_blank">📅 19:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467333">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891ab99c87.mp4?token=ukprgkVeHjrnp5lr8VLlzYO8o5cNbOx2l0oXShQ1CS-gCIyWJ2FBL62ahNbjp57odgBOXmiEkVFKlkU3PzAoF-l63-x0mYi1s8JmhE-7mi3CtTqPjZsuMCrMyM1G8K3N4p7MmhN7TSKSz2dZQuNQVyqv_3JKgwdeLNQ8BcB4kQgAB8LsGUHyQvkNWeWMmQzqajdzFvl-S6pAVaOdn-UXlfwBxwmCGVGKpz0ha0YUaRcS8VCiby2PURoxr8gruDb-WvptBCzw_jXkgyUX6s0zZ6bkzvObsdB-lGuAxu9Y4IPAtti45pLf3-44Xe_WCa9nG6PCjqJWMESjIrQwNmehqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891ab99c87.mp4?token=ukprgkVeHjrnp5lr8VLlzYO8o5cNbOx2l0oXShQ1CS-gCIyWJ2FBL62ahNbjp57odgBOXmiEkVFKlkU3PzAoF-l63-x0mYi1s8JmhE-7mi3CtTqPjZsuMCrMyM1G8K3N4p7MmhN7TSKSz2dZQuNQVyqv_3JKgwdeLNQ8BcB4kQgAB8LsGUHyQvkNWeWMmQzqajdzFvl-S6pAVaOdn-UXlfwBxwmCGVGKpz0ha0YUaRcS8VCiby2PURoxr8gruDb-WvptBCzw_jXkgyUX6s0zZ6bkzvObsdB-lGuAxu9Y4IPAtti45pLf3-44Xe_WCa9nG6PCjqJWMESjIrQwNmehqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول صنعت‌نفت توسط باصری در دقیقه ۶۶
⚽️
پرسپولیس ۲ - ۱ صنعت نفت @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/467333" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467332">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te240zFpeRzGbGUOSqGQx3gjNuymdwGTSJz2hWCDUGgRxZPZ3NjL10xbkTdkP-2oW3eUnUguE-uPuoCJA5JIfpRpdJKHWGd7cVGKNaPquKW8tS4Cayp3M9j-d6jYfwEHDuLFS1mAvxiaWJP7_JtrwlRpQC8B04TxfsobV8eDbTvnOzsyhbu1NXw40Bb1aOnoidZYjWN0d1GF3VsyRFMN4I7l91NqQ7pOOboN3wi53bEsM25uNjQNLp9w2MBSUOOOAucPsq8YzjjnpCUllOjRw90ScWnN-mPkQ8_tT6xMKmCb4Rqd-qvd3iuSNr8AZt-3QXoGhbO-J0f2qKR3QRHfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/467332" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467331">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2934295f.mp4?token=fJbGajBqbnvTf4Kn5N9PIL50HQl9fWXISjA7PkuVsaX1UmxgGn93hD5pD5klsCcoyqqIuZWK9tK7GGEVokbHIrYcoJZ2w7T8bSb-qGT2CQ94kIGzT6dw9Uk0KrAmbOZV6auCzXLWcivrsOG5HuUpZqWsvULMC3UZLvSwgI7q2aQLgz4Oi-SHL3WvK2zWtJX0KSJbTM1RakmXKB0vpydX5Fkoc9gClLmyUgTKhHWlOnBUx17uv4CN57wcdhVLvkuUzXv34pRKCkhZ_TMr8Sl9jDTUtoMBX5VKotl45pP84qlciKtREyoUrqCsOtHASo2zRVL85amM4JucsQazt0oxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2934295f.mp4?token=fJbGajBqbnvTf4Kn5N9PIL50HQl9fWXISjA7PkuVsaX1UmxgGn93hD5pD5klsCcoyqqIuZWK9tK7GGEVokbHIrYcoJZ2w7T8bSb-qGT2CQ94kIGzT6dw9Uk0KrAmbOZV6auCzXLWcivrsOG5HuUpZqWsvULMC3UZLvSwgI7q2aQLgz4Oi-SHL3WvK2zWtJX0KSJbTM1RakmXKB0vpydX5Fkoc9gClLmyUgTKhHWlOnBUx17uv4CN57wcdhVLvkuUzXv34pRKCkhZ_TMr8Sl9jDTUtoMBX5VKotl45pP84qlciKtREyoUrqCsOtHASo2zRVL85amM4JucsQazt0oxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلطان، نام پلنگ جوان شناسایی‌ شده در رودافشان دماوند
🔹
مدیرکل محیط‌زیست استان تهران: یک پلنگ نر که پیش‌تر توسط اهالی روستا مشاهده شده بود، با تلاش محیط‌بانان و نصب دوربین تله‌ای شناسایی و نام سلطان برای آن انتخاب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/467331" target="_blank">📅 18:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/577177c5a9.mp4?token=dPye-wFQIvqwguT_hijxjblkBE471MKtgyepwSU-39JK6izGB41lOT8LMiuW3DxexGYDNkI2js_NJiuMlC3YDnq0jOv9DEa1FuL71gbneWUeHdLgKZjpa7dRuP8CrYkOL2dw3w7gtzzztFqVA7v4w3s_4HeK7xAIqupsNtvT6Rm5yFEGj6-EdXvpDtpHQ9Rxy5UTeigvbwy3BR2du8y1DqrMFwYRKT19U-L7RgoPbrmRPtgt7i06uXDV-2ikOS-CTJi9kKEeoDce4iwnSgu5XZg0Fo6yxgReHXSDkrj_fXsor-j6mUReDKxBNxFM0ZfVSGCiVOetPLe-EH80RyiuLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/577177c5a9.mp4?token=dPye-wFQIvqwguT_hijxjblkBE471MKtgyepwSU-39JK6izGB41lOT8LMiuW3DxexGYDNkI2js_NJiuMlC3YDnq0jOv9DEa1FuL71gbneWUeHdLgKZjpa7dRuP8CrYkOL2dw3w7gtzzztFqVA7v4w3s_4HeK7xAIqupsNtvT6Rm5yFEGj6-EdXvpDtpHQ9Rxy5UTeigvbwy3BR2du8y1DqrMFwYRKT19U-L7RgoPbrmRPtgt7i06uXDV-2ikOS-CTJi9kKEeoDce4iwnSgu5XZg0Fo6yxgReHXSDkrj_fXsor-j6mUReDKxBNxFM0ZfVSGCiVOetPLe-EH80RyiuLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس توسط بیفوما در دقیقه ۴
⚽️
پرسپولیس ۱ - ۰ صنعت نفت @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467330" target="_blank">📅 18:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9sGTXnrCdVGp4ytbSlS5pk_G2L69P7RtEKpXGheTaE9PAR1ugcLhrvf5unNe-8R-Z8NoRrnzNxWWcQz5hpQqD0MUZ4tDW37Yjdmf3ANQ_ANFo80qVIZd0fXKNsU05gy6dRBb0sFtUJpScGsle-GYOh9EJYlUB3LGa_MzHpbizjNtW1TYmSGmuUKrfROhSQjpHe8CYMtgr37kBSYAa5eFJThwqdsa_CYqGn_KM2PxJM4SjDkYHfgcsZfzqyvZ0J6pdbi9_58pygEaEeWwfi6wMjAfvjEDIpdcjO8XSoagiRtSIm5SgSyF3juCF_YVpPjurt8oqcw7c8L3oHM2FGDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  یمن: مانع حرکت مزدوران سعودی به‌سوی باب‌المندب شدیم
🔹
سخنگوی نیروهای مسلح یمن: تحرکات مزدوران سعودی برای پیش‌روی به‌سوی باب‌المندب با مقاومت رزمندگان ناکام ماند و حملات موشکی موجب تخریب تجیهزات و کشته و زخمی شدن ده‌ها نیروی دشمن شد. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467329" target="_blank">📅 18:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3cdYsJYbS6YqSfX0NaNXqA5llkvQ1sNX_5EBHourj6tbBF42Vlf6bROGhCBOdcXod5U_-MPuJytHYKqLOL5ioiSw0el-bnrlOpnmrdkP2rfqgICiG_R2WIjgTKBS08f7mGZAUCJMOK9MLWGfHlgqw0Okj_67ntEaDBYlVXkco6sXtH3Sysf4dl-62JAoqWv5Iv2r2ZCo1PChSif_ILkq3WdlsLBR9ldoWM6OUdGb8OKFYzJP5uU0SfsrVPQ2bqqDqNTl-uXUzdbm9VgfD7WIxTOkZIwBD24CFD4NjqJzuJx6kC6pidLjUX-IzspcCxA7Fc22FbUse7P8kRQ8H7tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یکی از ستون‌های مستحکم امنیّت کشور
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467327" target="_blank">📅 18:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbad3ed44.mp4?token=AkjoVcwfxeqeocoa1d1_neAfCJPbzq_NMF-moiP3PD8hofFFtkqZdIewEUVBYugPKrkO7V8kMN9gpV8qH0u8X0yHB1477fj86DLmhwJzRHg7oZXj4VYwS4s8qADdE2k6iFD2C2QsCCr-l9eLI7F76RKATQgrsAfy8o1E3RxwSbo8McIDlClksnQVoZDGNZCabFk1KT7u2JnMRuelOqQ_sYHlckTq_usvHTo57WkwPAMrL8NsROmNjoKyGo0KKMQA9jyH0CeXRQvGYDw8jYzx3k-ZRQMdaAd62aSG3fBqYbyCtdoswpxp2nYo3f3yh00_kVJZkk7wETgdHH4Dk1DFJWvouFF7EmFEJHABJFnoEfOdF-_PI9y6HH9modsxE9J3oyAu65hbjW6JDPJ8UyQZKDpbqSr5fcL1maXuNrCNlXu7jcOvNiq7c4dLXqYYoGUs70HfQUsmeL0HSvf_AGvrMlWcWFDho9E9oaDIa6Y_rzz8DBB9b0Eg9_S_n2b3FGZCL1Lv5o1xsZDJ9XF-xwQ0NE1dgcmv2kmjl5Vg5xcHtk_AMGDjar0Z36XON8l5HWVQqbUSYSzKxGSaDPmFREaYCwQXhRuzTlqzCeDzeBS9sEerg8MW5Mj2URwF62Y1fEMOhdZrMe97tVP882EvdLI_WxPrkPjCdNw-S1TlVkwV_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbad3ed44.mp4?token=AkjoVcwfxeqeocoa1d1_neAfCJPbzq_NMF-moiP3PD8hofFFtkqZdIewEUVBYugPKrkO7V8kMN9gpV8qH0u8X0yHB1477fj86DLmhwJzRHg7oZXj4VYwS4s8qADdE2k6iFD2C2QsCCr-l9eLI7F76RKATQgrsAfy8o1E3RxwSbo8McIDlClksnQVoZDGNZCabFk1KT7u2JnMRuelOqQ_sYHlckTq_usvHTo57WkwPAMrL8NsROmNjoKyGo0KKMQA9jyH0CeXRQvGYDw8jYzx3k-ZRQMdaAd62aSG3fBqYbyCtdoswpxp2nYo3f3yh00_kVJZkk7wETgdHH4Dk1DFJWvouFF7EmFEJHABJFnoEfOdF-_PI9y6HH9modsxE9J3oyAu65hbjW6JDPJ8UyQZKDpbqSr5fcL1maXuNrCNlXu7jcOvNiq7c4dLXqYYoGUs70HfQUsmeL0HSvf_AGvrMlWcWFDho9E9oaDIa6Y_rzz8DBB9b0Eg9_S_n2b3FGZCL1Lv5o1xsZDJ9XF-xwQ0NE1dgcmv2kmjl5Vg5xcHtk_AMGDjar0Z36XON8l5HWVQqbUSYSzKxGSaDPmFREaYCwQXhRuzTlqzCeDzeBS9sEerg8MW5Mj2URwF62Y1fEMOhdZrMe97tVP882EvdLI_WxPrkPjCdNw-S1TlVkwV_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌صحنهٔ خبر بازگشت گلشیفته فراهانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467326" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
نمایش دستاورد علمی ایران در درمان فلج مغزی کودکان برای اولین بار؛ سل‌تک فارمد نور امید را روشن کرد
🔹
همزمان با روز کودک، حدود ۲۰ خانواده از کودکان فلجِ تحت درمان سلول‌درمانی، در جشن «رویش امید» گرد هم آمدند تا روایتگر تغییرات و امیدهای تازه در مسیر درمان فرزندانشان باشند.
🔹
سلول‌درمانی، فناوری نوین پزشکی در لبه دانش جهانی است؛ عرصه‌ای که ایران با تولید ۲۰ محصول از حدود ۱۵۰ محصول سلول‌درمانی جهان، سهمی قابل‌توجه در آن دارد.
🔹
سل‌تک فارمد تنها سازنده داروی فلج مغزی کودکان در ایران است و ۳ محصول دیگر در زمینه درمان‌های پوستی و مفاصل دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467325" target="_blank">📅 18:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpuzuAyofTSxBEa-wg83-2iLNMCcjmHcfF56VS6wcbmuoQmYwK8DRv8P3keJX59N5-ViuRlnyX-H72ZVK_OZdR5IQi5WCMFTMnJP2aA1pFcYIxJpyeFnwbuXPPRH5us_ZmIY1myc8tfqJsZ-tKN-ODtiALvXycP66A83qcYMXC8l5rP5V-HPhob3tTfYyVg4pLHZwRWMW_3Mji7_xTTTHrJA7QI5dd-duPChWMY5fKfy1qq9pCaKadP68tbBsqZcRBT5hzI0qlalzCXyGkp9uTGLrovpDghD3hZi2V9zeY4ObZi3Qlsjhf-t4iBui6x2MhOaSFhhYUsXbTUCqgDweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/467324" target="_blank">📅 18:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/467323" target="_blank">📅 18:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467322">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opAbzu2Dye8yTUWjNYBMbMWJ2DymGScJTkRjBgvARkyzVk2MWou4r2L0H8-q8e0EFG9T5nwI8bS1pgJsXoW8qwzb2M-drGNHhz0lAFEt_Kq5omPRfmPmlK5k11VyZ0W6PQ7y6z-3_tQNfdfh_QKDCJqkAK1Iy1gtpqMT0AFIyKqk7XCmJDzHIeXr2US_wwXCP9MUSIHdcDLjIGAlBOGiHUU3rWeMK82ehMYpdo4dHYytonDlX0TnCAo5oAUoASepfBbeUH0l6r_DYosrzEj7MWjfuVf7z1cjzmlpI-IIYWWzEcO695E5y9MBK1k3b7p5WrbKRjXQYtdadN_stnhbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار مدیریت بحران به ۶ استان کشور دربارهٔ بارش شدید باران
🔹
مرکز مدیریت بحران کشور در پی صدور هشدار نارنجی هواشناسی برای روزهای ۱۸ و ۱۹ مهر، از استان‌های گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی و سمنان خواست با تشکیل جلسات ستاد بحران، اقدامات پیشگیرانه را اجرا کنند و دستگاه‌های اجرایی و امدادی را برای مقابله با رگبار باران، رعدوبرق، وزش باد شدید و گردوخاک به آماده‌باش کامل درآورند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467322" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467321">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7qoKyfDccEwbvNtS5TqtZR_8MIAp8nOSLSrOdgOWfuezsDhITXaZZVP1cvmoJEtIbnVL1O6FAsBwjAIGlSblT00VFrpDyypN7XUtURI07j2twy_L2b8AeJOomjZ2Pr605ov0ZKb-XJuiVX8AVkN5qWvYR-mBmEX6vpiQc_7wZdXHEJShi8wJuG2qIldEZEMZulkTssIrpVIilNQlYpc6Y7NyeJoJHUQOMipYPxFsAyqe8r03eqMOE4hNdcjX-jaq_yJbFE3SXWXbsyWB3Dhq9nyWwg7ipvNB1_GI4a2cpqtKywTFAgSmy7isRX0W1cGNh5AxQiDK2OIJsjWaEYOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش سخنگوی وزارت خارجه به مواضع متناقض فرانسه دربارهٔ موضوع تسلیحات هسته‌ای
🔹
امانوئل ماکرون رئیس‌جمهور فرانسه به هنگام آزمایش یک موشک بالستیک دارای قابلیت حمل کلاهک هسته‌ای می‌گوید: «برای آزاد بودن باید ترسناک بود؛ و برای ترسناک بودن، باید قدرتمند بود.»
🔹
اما همین امانوئل ماکرون درباره ایران که از اساس دنبال سلاح هسته‌ای نبوده است، گفته: «ایران هرگز نباید صاحب سلاح هسته‌ای شود؛ نه امروز، نه پنج سال دیگر، نه ده سال دیگر؛ هرگز.»
🔹
مسئله این نیست که فرانسه چرا بازدارندگی هسته‌ای دارد؛ مسئله این است که چرا منطقی که برای فرانسه ضامن امنیت و آزادی است، درباره ایران، حتی در بحث از برنامه هسته‌ای صلح‌آمیز و تحت نظارت بین‌المللی، ناگهان به «تهدید» تبدیل می‌شود؟
🔹
واقعیت تلخ این است: آنها صلح را برای همه نمی‌خواهند؛ انحصارِ ترسناک بودن و مشروعیتِ ترساندن را می‌خواهند. خودشان باید قدرتمند و هسته‌ای و البته ترسناک بمانند و دیگران را حتی کشورهایی را که صرفا به دنبال انرژی صلح آمیز هسته‌ای هستند، با تصویر دروغین «تهدید هسته‌ای» محدود کنند.
🔹
صلحی که در آن قدرت‌های هسته‌ای، سلاح خود را ضامن آزادی و امنیت می‌دانند، اما همان منطق را برای دیگران تهدید می‌خوانند، نه صلح، که انحصار قدرت بر مبنای خودبرترپنداری است.
🔹
نظمی که برخورداری از امنیت و صلح را حق همگان نمی‌داند، بیش از آنکه حافظ صلح باشد، مشوق سیطره‌طلبی یک جمع خاص است.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/467321" target="_blank">📅 17:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3b26fd38.mp4?token=Z5356hTGDEr1o_aOsv0Yev9PFAe0GS6Zlfaf2HLgjtlxMDGQ5wJtn01nUQNVF41QuxsiZnMBcB5ZRc8GZ6t_pgoKIc5sKZTULXWfBGR8wO1WnVxODMEW5chP7bwGA_sDXD4n8cIXA2W517nxq4wtgsa3QaUPAsqOhEJvhOpj8US8D6TL4BBvu4ca0uBi_QpiePEDWKLAwl_vDDLzVR54LIciXhLOLjGinW7aInThoNxdmt_muD7wV6K8BoqAlxUhWMJLe3huuhKjCPWd6YNOKUHOwXzbNtXDeDNcSEgAIjIaRY1RdrYuIPZwhpn7X4a-nb_Xdqaq3j4_t6bGEd-mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3b26fd38.mp4?token=Z5356hTGDEr1o_aOsv0Yev9PFAe0GS6Zlfaf2HLgjtlxMDGQ5wJtn01nUQNVF41QuxsiZnMBcB5ZRc8GZ6t_pgoKIc5sKZTULXWfBGR8wO1WnVxODMEW5chP7bwGA_sDXD4n8cIXA2W517nxq4wtgsa3QaUPAsqOhEJvhOpj8US8D6TL4BBvu4ca0uBi_QpiePEDWKLAwl_vDDLzVR54LIciXhLOLjGinW7aInThoNxdmt_muD7wV6K8BoqAlxUhWMJLe3huuhKjCPWd6YNOKUHOwXzbNtXDeDNcSEgAIjIaRY1RdrYuIPZwhpn7X4a-nb_Xdqaq3j4_t6bGEd-mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان پس از شرکت و سخنرانی در ۲ اجلاس سران کشورهای مشترک المنافع و اجلاس محیط‌زیستی خزر، ترکمن باشی را به مقصد تهران ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/467320" target="_blank">📅 17:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5WWh_l5Q8GitdfzK0EslFOUxJQqZdH43vHbUH_gMm8xDBFkj5pqXPkyKaGAyoe-NYXeVYOjPj46-E0Fb93Nsr7YqxPgmzIRzw4ADtTPBA9Rk8DuFT33_QYYMggSgsQHmYfuEhdvh7MVq71a5O7EDTNtIGW20dBHprWw_SA4U36_33Xi0waxa8uSOKL1_T_r9V-fTBLSrD6G02HaayadlR2nEouyfMpUHsPw7OdshEcZAP--yW0kubI608KrjJIAVzGlB-IekFXEE2v0Xa4HDehnZ4Bjnf-AgRnw1w67gRicnXAbbHNbkVGswW4lh6brZgtUOw-7aIkqKh7ENHupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
انفجار در مسیر خودروی پلیس در زاهدان
🔹
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔹
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد.
📝
اخبار تکمیلی متعاقبا منتشر میشود. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467319" target="_blank">📅 17:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080ffd578f.mp4?token=CQOKx6FKELaCxnzM60SCg6myjZ13KqEpzKwOrP7BjeBcM6B1d7IT8BidfU2ORmKcrBHLuGnVZs3O2EWZdQLbYkgDaB47PsIKZUN-T-581xlQKNqo66oZ1IO_mtaGA2lSp6O0po7gISynKR5Tn-uU6ipi563IucR_j8gXM76hrHC2ZrZsdfFRx4ej4OdfYdmHEQRXxgp1b5gMx9uVs0Piljq3fdUIwrnk5DK4o69_-Ugsm-dVOGr6qEIN_CGkAFHIEOIqZlmFhWvnzzHcauFw5Tb7elL7F0aq9ivlM_vr-YjlU0ouKAl7oQ-Iw1GCpazEnhaMwYvmzvsNnTh4VTGtcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080ffd578f.mp4?token=CQOKx6FKELaCxnzM60SCg6myjZ13KqEpzKwOrP7BjeBcM6B1d7IT8BidfU2ORmKcrBHLuGnVZs3O2EWZdQLbYkgDaB47PsIKZUN-T-581xlQKNqo66oZ1IO_mtaGA2lSp6O0po7gISynKR5Tn-uU6ipi563IucR_j8gXM76hrHC2ZrZsdfFRx4ej4OdfYdmHEQRXxgp1b5gMx9uVs0Piljq3fdUIwrnk5DK4o69_-Ugsm-dVOGr6qEIN_CGkAFHIEOIqZlmFhWvnzzHcauFw5Tb7elL7F0aq9ivlM_vr-YjlU0ouKAl7oQ-Iw1GCpazEnhaMwYvmzvsNnTh4VTGtcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان سهمگین در راه سواحل آمریکا؛ هشدار تخلیه در سه ایالت
🔹
مرکز ملی طوفان آمریکا اعلام کرد طوفان «ایسایاس»، قرار است شامگاه جمعه به وقت محلی در نزدیکی مرز ایالت‌های فلوریدا و آلاباما به سواحل آمریکا برسد، به یک طوفان بزرگ رده ۳ تبدیل شده و سرعت بادهای پایدار آن به حدود ۱۹۳ کیلومتر بر ساعت رسیده است.
🔹
بر اساس هشدارهای هواشناسی، وقوع قطعی گسترده برق، بالا آمدن سطح آب دریا تا حدود ۲.۷ متر و بارندگی تا ۳۸ سانتی‌متر در مناطق ساحلی محتمل است. همچنین احتمال شکل‌گیری گردبادهای ناگهانی وجود دارد که می‌تواند فرصت کمی برای واکنش و پناه‌گرفتن به ساکنان مناطق آسیب‌پذیر بدهد.
🔹
در پی نزدیک‌شدن این طوفان، در بخش‌هایی از ایالت‌های آلاباما، فلوریدا و جورجیا وضعیت اضطراری اعلام شده و دستور تخلیه برخی مناطق ساحلی در آلاباما و فلوریدا صادر شده است. مقام‌های محلی از ساکنان مناطق در معرض خطر خواسته‌اند هشدارها و دستورالعمل‌های ایمنی را جدی بگیرند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/467317" target="_blank">📅 17:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUb1SpiAXAYCrZtebekwzb8Stnrz_aCcSByaEXKG_Crxuy2qU_mv9_q35QG1HiFyLlhpEy3BFN4NUzN0o1yae-ExnhUjux9tLEkMYs9-4I1Xj_GthnXrOUAi4lDuWpbfWaz_Uki3FeiEwJ6E3F7LYNjtYNcKrPGfne92IR9z9049I8Y18Eo2FZvS1CFooHJrNvhLNeP_Gf-bp5LnScS7GpajINLgCxaAgCh1NTgEmNyCTyK6Z-bCsoyBNn7uOyK7QW05WhkAvq34z7gVmY6o5MSsPjl5tzjNM37Xya9Bi2UrbotRj9SWT6s2mwdmRgpzC9SDyt1kXmIZrgXczm0WUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس آمریکا اسیر هرمز
🔹
ریزش ارزش سهام شرکت‌های آمریکایی در سایهٔ تنش با ایران ادامه دارد.
🔹
مطابق آخرین داده‌ها، حدود ۷۰ درصد شرکت‌های بزرگ آمریکایی در ماه گذشته میلادی بازدهی منفی داشته‌اند.
🔹
افزایش تورم در اثر ادامهٔ تنش‌ها در منطقه و کاهش عرضهٔ نفت، شرکت‌های آمریکایی را با بحران مواجه کرده است و پیش‌بینی می‌شود این بحران به زودی دامن‌گیر شرکت‌های پیشرو بورس نیز بشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467316" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترکمنستان چه می‌خواهد و گلستان چه دارد؟
🔹
ترکمنستان سالانه میلیاردها دلار کالا وارد می‌کند؛ و سوال اینجاست سهم گلستان به عنوان همسایه اصلی مرزی از این بازار چقدر است؟
🔹
ترکمنستان در سال ۲۰۲۵ بیش از ۵.۱ میلیارد دلار واردات داشته، در حالی که گلستان در همین سال ۴۸۱.۷ میلیون دلار کالا به ۲۸ کشور صادر کرده است. لوله و محصولات فولادی، فرآورده‌های پلیمری و محصولات غذایی، بخشی از ظرفیت صادراتی استان برای حضور در بازار همسایه شمالی است.
🔹
اما نکته اینجاست که ظرفیت به‌تنهایی کافی نیست؛ رقابت قیمتی، کیفیت، بسته‌بندی و حرکت از خام‌فروشی به سمت محصولات فرآوری‌شده، شرط ماندگاری در این بازار است. کارشناسان نیز بر ضرورت شناخت دقیق کالا، خریدار، قیمت و مسیر صادرات تأکید دارد که اینچه‌برون می‌تواند دروازه ورود کالاهای گلستان به بازار آسیای مرکزی باشد.
🔸
اکنون سفر پزشکیان به عشق‌آباد و اکسپو ۲۰۲۶ گرگان فرصتی است تا دیپلماسی اقتصادی از تفاهم‌نامه عبور کند و به قراردادهای واقعی، سرمایه‌گذاری و اشتغال برسد.
🔸
مسئله گلستان کمبود ظرفیت نیست؛ مسئله، تبدیل این ظرفیت‌ها به سهمی واقعی از بازار ترکمنستان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467315" target="_blank">📅 17:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
تداوم حملات هوایی عربستان به پایتخت یمن
🔹
شبکهٔ خبری المیادین از ۱۰ حملهٔ هوایی عربستان به جنوب صنعا پایخت یمن گزارش داد.
🔹
المیادین گفت که در این حملات، شبکهٔ مخابرات هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/467314" target="_blank">📅 17:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104e3f811.mp4?token=ti8bss-axaTxHSUhClOeQiZGzxrA_XquTBZg9euC_1XLhGJGm7t_5a8EpUCqSX_wunrpUVyAhTk6a6gzt01te2ClBtw9hXhFBCmmmnF3a5FBTwB5PVycVrvKZf-N353hPIUzFweVChefD3TodFbFsalhr7bG42KQrXQ2yO8ijPqyua2E_aj7s0xLckX7q5Zv8g2JFvEpKNCjkVr40JLVEKXe9dUj9ESQEujvWdTjW1GNuhmpU46r4guJCMfdWHWXS5kXlLbaOO02R8TPnEFE3SIkzLKUEQ37CZC0_wqwn41waHyywzyeO_NMRGWGbaZ6umvkXXZiVkENTUndwqvNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104e3f811.mp4?token=ti8bss-axaTxHSUhClOeQiZGzxrA_XquTBZg9euC_1XLhGJGm7t_5a8EpUCqSX_wunrpUVyAhTk6a6gzt01te2ClBtw9hXhFBCmmmnF3a5FBTwB5PVycVrvKZf-N353hPIUzFweVChefD3TodFbFsalhr7bG42KQrXQ2yO8ijPqyua2E_aj7s0xLckX7q5Zv8g2JFvEpKNCjkVr40JLVEKXe9dUj9ESQEujvWdTjW1GNuhmpU46r4guJCMfdWHWXS5kXlLbaOO02R8TPnEFE3SIkzLKUEQ37CZC0_wqwn41waHyywzyeO_NMRGWGbaZ6umvkXXZiVkENTUndwqvNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس توسط بیفوما در دقیقه ۴
⚽️
پرسپولیس ۱ - ۰ صنعت نفت
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/467313" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwXopFHhK0t_xhd3Pz2e9vobjU75MCvp9HBxWp_zux3M-egBvtJpDKD_sGER06Wojki9j2wDc6rGTeJmGCUKO9xfksJFLb6n669k_TE0IYhcWp_LhoT7TN0VE4DJ-xNRirOS2R6Oq-MLcgblW1jQK6r5n88FJS_NVBIRwcgEPYX7xPJa6iwJLFNVX0Ccu1KyundnAIhGKRUlIbUM1C8pVN0ED9kaeoxrSUWXCGxYFoTncmPIIDzAFDC7_hsXGI_ieyafVYk0Xz2P_ji3vmxpbgUa3nU3ESDDO2RKhOCkFuYqXvGQWhvhgo2WTDtv0nq1I5plvBohgUdg8tjEou7pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا پزشکیان در عشق‌آباد برگ برنده را رو می‌کند؟
🔹
سفر رئیس‌جمهور ایران به ترکمنستان، فراتر از دیدارهای دیپلماتیک و گفت‌وگوهای معمول، می‌تواند فرصتی برای بازتعریف روابط دو همسایه باشد؛ فرصتی که اگر با تصمیم‌های عملی همراه شود، معادلات منطقه و به ویژه شمال کشور را تحت تأثیر قرار می‌دهد. اما سؤال اصلی اینجاست: آیا این سفر می‌تواند به نقطه عطفی در همکاری‌های اقتصادی ایران و ترکمنستان تبدیل شود؟
🔹
استان گلستان به واسطه موقعیت جغرافیایی، مرز مشترک با ترکمنستان و پیوندهای تاریخی و فرهنگی و قومی ظرفیت‌هایی دارد که هنوز تمام ابعاد آن در مناسبات دوجانبه ایران و ترکمنستان به کار گرفته نشده است. در این میان، نسبت میان ظرفیت‌های موجود و آنچه تاکنون در میدان عمل محقق شده، پرسشی جدی پیش روی سیاست‌گذاران قرار می‌دهد.
🔹
تجربه همکاری‌های منطقه‌ای نشان می‌دهد که همسایگی به‌تنهایی مزیت اقتصادی نمی‌سازد؛ آنچه اهمیت دارد، تبدیل ظرفیت‌های جغرافیایی به سازوکارهای پایدار برای همکاری‌های مشترک است. از همین منظر، دیدگاه کارشناسان درباره آینده روابط دو کشور و الزامات عبور از توافق‌های روی کاغذ، اهمیت ویژه‌ای پیدا می‌کند.
🔹
ایده منطقهٔ آزاد تجاری اینچه برون _ آلتین‌عصر همان نقطهٔ عطفی است که می‌تواند پایه گذار روابط نوین این ۲ کشور همسایه و تحقق اتصال واقعی ایران به بازار ۲۲۰ میلیونی آسیای میانه باشد.
🔸
اکنون نگاه‌ها به نتایج این سفر و تصمیم‌هایی دوخته شده که می‌تواند مسیر آینده همکاری‌های تهران و عشق‌آباد را مشخص کند؛ تصمیم‌هایی که آثار آن، در صورت تحقق، محدود به روابط دیپلماتیک نخواهد ماند.
🖼
سوال اصلی همچنان این است: آیا این بار پزشکیان برگ‌برنده را رو می‌کند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467312" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c2f4c6813.mp4?token=HFVWAzVII86HxM7Uqc0Py3Suu2g-HJaPiQy7cWzxzyHutGylEV9IQjIDQM4LsZrHA99qzk-ElE_B4LkEjj9GYtyAZdwy_yZBbFy8ZRA025PVB0k6RbxxVTb-TXj-ztbjBlQdt0MV54fVqPDLM3Nv9o9xmTVjJa2YGZsQLNm-dwhYVtmfNyuG4vJbnsWVYuDAAPlDlHEYP7A4PtMiGiW07DKHujix6SYpWkeh3hcF1QAGeP1zP-OgdBmesEF8Sz7rSdT0hjwxr4dBloO2wCqJeS9NEEEJ496WRQVCoatiRwqEmGSvIaLV0AjV8HLD79Gcf7NRvFNopO_56oLMnlUZTDKvTcWcdsNHBAn6shIa74H_XtE6x46N6Vr0iSBApZgD_rQ7K5Is-tyVAyYy0wjoUx6JmyFcFTAghCzXuddIdODvNiLhe9qGc7CrFcorypNuQ5fnCgYamqaY34dNf4tzeguSNmLoi-nPcy-l7hnQ3mmXrP0hIGc3bf2LTnz9Ez5N3EEJBWs5AB0-s_zAJX3IWsLH-elrtOExEaz3hoBQx60NWYzx6YIRevi0I_ihTeHxm4rimSAnQCMqIPhzfcZ8EpCG15ULCy_9IXmhyRKJqwtEBH0kvAkqyYc3H-zcZvTgpKn6iV1NOuTQlEqhG2UjkQMtezEo8zhaRtsmuEIdL2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c2f4c6813.mp4?token=HFVWAzVII86HxM7Uqc0Py3Suu2g-HJaPiQy7cWzxzyHutGylEV9IQjIDQM4LsZrHA99qzk-ElE_B4LkEjj9GYtyAZdwy_yZBbFy8ZRA025PVB0k6RbxxVTb-TXj-ztbjBlQdt0MV54fVqPDLM3Nv9o9xmTVjJa2YGZsQLNm-dwhYVtmfNyuG4vJbnsWVYuDAAPlDlHEYP7A4PtMiGiW07DKHujix6SYpWkeh3hcF1QAGeP1zP-OgdBmesEF8Sz7rSdT0hjwxr4dBloO2wCqJeS9NEEEJ496WRQVCoatiRwqEmGSvIaLV0AjV8HLD79Gcf7NRvFNopO_56oLMnlUZTDKvTcWcdsNHBAn6shIa74H_XtE6x46N6Vr0iSBApZgD_rQ7K5Is-tyVAyYy0wjoUx6JmyFcFTAghCzXuddIdODvNiLhe9qGc7CrFcorypNuQ5fnCgYamqaY34dNf4tzeguSNmLoi-nPcy-l7hnQ3mmXrP0hIGc3bf2LTnz9Ez5N3EEJBWs5AB0-s_zAJX3IWsLH-elrtOExEaz3hoBQx60NWYzx6YIRevi0I_ihTeHxm4rimSAnQCMqIPhzfcZ8EpCG15ULCy_9IXmhyRKJqwtEBH0kvAkqyYc3H-zcZvTgpKn6iV1NOuTQlEqhG2UjkQMtezEo8zhaRtsmuEIdL2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفتگو زمانی کاربرد دارد که در سایهٔ زور نباشد  @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/467311" target="_blank">📅 16:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
تداوم حملات هوایی عربستان به پایتخت یمن
🔹
شبکهٔ خبری المیادین از ۱۰ حملهٔ هوایی عربستان به جنوب صنعا پایخت یمن گزارش داد.
🔹
المیادین گفت که در این حملات، شبکهٔ مخابرات هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/467310" target="_blank">📅 16:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
انفجار در مسیر خودروی پلیس در زاهدان
🔹
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔹
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد.
📝
اخبار تکمیلی متعاقبا منتشر میشود.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/467309" target="_blank">📅 16:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqr448du8Ll0E7aQApBo83cPlBh6bbKg9vCvTXqf7pS0swunF8LAKAt8DWQfUybREOQm5CoUwxG_qjR1PVmcdKVej-F3kitSVMSTrEYX-ECXtHTKeuoK0P22wRz68v22-zWOLp9lzJ3mwDLVmoJcoaKxchv7gtsYrJSrcwHoktkq1Km2RB56e4gztu-UMuUjjlRC842Mx5wtbMe3VahLeqHCBBcgf0UsrW361W22Fzhy2bUDumPHZdVDFmg-K52hthXD9QrD46xWILQze1GTNXdJ-dgo-ZNrtvpQ3_1IAUmmywlUUNzQPxP5GLd-O-GfP_kI1r7U09ze1J9kQ6jR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش حمله به یک کشتی در خلیج فارس
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) از وقوع یک حادثه‌ امنیتی برای یک کشتی در فاصله ۱۳ مایل دریایی غرب منطقه الجزیره امارات خبر داد.
🔹
این سازمان اعلام کرد که بر اساس گزارش‌های دریافتی از چند منبع، این شناور در حال عبور از مسیر خروجی، هدف اصابت یک پرتابه ناشناس قرار گرفته که در پی آن آتش‌سوزی رخ داده است.
🔹
به ادعای این نهاد، آتش‌سوزی مهار شده اما وضعیت خدمه، میزان خسارات وارده به شناور و پیامدهای احتمالی زیست‌محیطی این حادثه همچنان مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/467308" target="_blank">📅 16:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467301">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgXFGHW13unDH2Dds_3CCf6kpvIKbwhnL5Q4DVbSQG_X90Ul_lkk6VTGlHFc5qllab42zIufZX2u-oJ4nFssUdf12TnGRJqc-U3dXatKfktbf9znWPlLReC93tUZPmIUDD67eLqBUidCFFDFSDkVCw3TCW5OQr0wBGLGJ4PYrltqFbuudXtLPVxlKywGykaIlJtHowNWh8GGluk2uT2FRGW4mUXqSpK_OXdpDo6w0sf5UXPo_BsE2Y-hYZDudnGib3mxXgxr-4jPC3i9zVl3SN9wiQwwTqM_5FCJapKA3-bIIRs4eq8UF6GEd_fzKoWyBy_h3ixodX_YF70YlEXzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqTfc8-8w0CVynehHQzxr3yrQDEsYBXgFElD8uW9JDep2NumpQfdoUFcjO-mcrk1vyjx0UhQ22m6uqWksSF14mu4yPmOs_fS44R2cFbow-0aVD7Kzk28zBi6ZzxQ2HSBggOPGI4y7xIoWinm4LuPQg_b0wSPAx0SfSuI84N0JRVmVBTvLJZbnDaJW4ITEI4EwVXMOZMqeneLMr19NY4_ndJtYcBacdBAXoJjhlroVNSClsP9cQQ5vupB5K7jFHgpN9uTGZ1P4FBczrRIQTfpqg3q1DbxbMj9hGJFmcV_uUixgZbE8qdghzGoE8Inm4MYgXFcQaWcX859xv-yoMJo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrT4XrVecjBxbe1zu6Yu4RGh_RwpoeKpz6zUUt48ZwZTbLJP4MgzGAhHNtWrODvHPho35pDIYJQa15La1JTVpjg252aEAxfjtDbvX8IpdNgr2Z--j_WDtRnA86Y2XWQCEkfpGRkrYPMfvI9CTOrU6k18YEEOXzh_zx5FUdQyqw70xbVgIrHhgMGnTp7a6EePlZRCn-UrYYdpb92-kG1xnYMEnk5Xf0A3i3ZGzRFM1WVqaMGZjKNY6sTEw5PV5XQ7W7sclpk-hFSc2ggwfTAvOhwUJRTAlTrYgaZof8fBmic8-Gb-KIaUi8sNh0YoRjeIFLe4ZHe3e4F-CkLPEQIkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUuLR5Wdbdn4lOBAYKIRW_KYPUogB6xwHVnuQb-LakxQdN68yY2eKCkqKongiW91N6Yf8IqrN47Ywbep3ZG0KZdS96XMVyyyhiSTuHYiqLTwNxPBAw4qvm6S3yOcq2D6dwSkPLSn8-UOu5sGeDyAMKRc-FspS_Aw0zOxDADxf2JOPpj5WOGl_EalqMIC3mG6_S5f0yx1-KN4TepXfTLQQT86k0Y3IXArnZVNErHBxb2NqUlLH5vjN5Z0bO6UwpayGn0ypapDMMv8ioEnOXn-TN4AifhwzHtt63pMY14soWhQg5R7A3wM_fDx_c7houbkqADzhoj4ECEO3TX48yHqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXx-LY-tWppxxzWWCBnl-aRXoHGRl-Bvi5iG-SGLAMVPai_NRgiWbwYLiZdVvfFCvRyA7PgPktTNuJ9k1C_qWbgItxFlpfXm8uui3-GuZmU-M-waE2UtHSxjyN3tjg4vYmwp-4NODGJEOoBPiF7chyRwXavhSPVGdLrlKU3jUllcLtZKxiUQHybFrDTrriGmdSMGGBt_kw1IZ4FsYFRtWlHZyaHXwKO4V5g4wzwAww9nUKSqvgRGw1PExI-tuFztpMOrRhEYPJfTUQWGZJ-_AEgcjm7lPIv3OsHpQuPROy2Ygpa080HXXlBY7PNBOWiF6mH63kDVY-nyGxLAO3CJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUx30wr8x-UeBBS_SHWHHXIRhRucVjZsb0F7KZuAwz_fWtjKA4hNfRkdgVlvKBvU9X_riZ1nZcpOAC0-_z_3ze-8QgBz3-EcDeGQ-P5u4ACw-soFRETPxd3I8hbSrwlTc9U1vWawNsDbUFoRn898sFOD6VeD5UGgbfn2QfPaY2EmBwWjgkm7NxzFm_LbOGWj_FC2ggIbpU6cOXceoN7BvtqMYRrkSWsrWXQkQbogObStsgBRew7Dv1ZLrwmESz2NUFrjGMtUqj5qdkcdHU2FlN23fSg4GZsRygSJsP7q6RUTfWpOkVsK-HNgi2Ok4f5JHDX2TE-ORKDbmuoNFSoU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyUxNX_nodrV_jNaVWhqbQ56MVFguuJq-YnU--22Z23uU6xFjWUzpr6W9qEYkVHtWx09soNIvlLjBm-lrpWvbDZMppiyZEJhW4hE7-tAgpfVZFw9PFkX-CDVyZ2YdGeXhfk_cih32DSDkBwBVFoE-Fn8F6pQFgLWiEz6hlugcSNZcP26h9ZaoAaLv5M-GQUqLEnLYnindLPxl5r0ww-RKMAyOC5aDoX6PjJM0zRG7CiWAfoGM0N0e9bzOOokOYqGGwCrsLKiZPqagt2tOjdzhtJHcDeQdXPxYeQdBMETSTIqX7KsWH5lapJZLlDR2TW-6yZj4l6cFjVJyEzHUrlZAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ خطیب جمعهٔ تهران: تنگهٔ هرمز تا تحقق کامل شروط ایران باز نخواهد شد
🔹
حجت‌الاسلام والمسلمین حاج علی‌اکبری: ایران شروط هفت‌گانهٔ خود را اعلام کرده و پس از تحقق آن‌ها درباره اقدامات بعدی تصمیم خواهد گرفت. وی افزود تنگهٔ هرمز تا زمان تحقق شروط ایران باز نخواهد…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/467301" target="_blank">📅 16:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467300">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmJm3wc9IXVAwYKhSVpea3k_GxrAOoWCfjsxsP3dxWXtpF0V3NNPccQye2PBhAq0Gfy4WxLHOVSkGY1k35HWPXQ8XQYFXgHI21L5SYlzW9oe7mTByKv5n1oLtd37JfgQYo8_HjRJrO1vXTOiS3VilgwYQ6W49Z4Xw7vo8HaNqCcJSjs5ZCmC_yjr5AfbI1Dq8eJd7nC62-coSGjx7wHurDdVVPbb_WeDGotj8p5TBCpu02ahitU-tgNtiQC8-RQdvWq1-DSSGZ19_IOEGUbJVkoWuElWdcKr16MV4c2CGebIVdYSwPL8cSfT6fmntJp1jVwWTqZVhoY4gldRvUS4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شرط یمن برای پروازهای فرودگاه ریاض
🔹
یحیی سریع سخنگوی نیروهای مسلح یمن امروز گفت فقط پروازهای بشردوستانه‌ای می‌تواند به فرودگاه ریاض صورت گیرد که مجوز پرواز را از مرکز هماهنگی عملیات بشردوستانه در صنعا دریافت کرده باشند.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/467300" target="_blank">📅 16:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467299">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjQNRzHNRTTQZJV-yiyJx0wQfYSvuPi79Qv42bu2yPzPhPKbMggbrx8d6gNaidq8wbwl2gk7_zD4aPfIB7Sq1um0xPiKGllV-acIamKgrAqvn8-tueL6tn-wqgZJqhIBvXJvu6aEdWOzEEAV8yPUoXtpsPHbqHffAWk99fNm3UtHiKxSOgE512-3TOTmCraVvYO6PtYejOtb0kuEIv7zGNSxhYHcKzrc3sTzenneZ6bji2a2S37Kzxg2jE1MPCtwe87mQrSf1iV9IAGQ0q3ERJScO9YO7JkILaHALP8nDX0IJvSGh59QB7FaoxYGgAlYIU64BIXOD4P6X9BdHw3McQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر حکم تنفیذ دورهٔ اول ریاست‌جمهوری حضرت آیت‌الله شهید خامنه‌ای از سوی حضرت امام خمینی(ره)؛ ۱۷ مهر ۱۳۶۰
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/467299" target="_blank">📅 16:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467298">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
وقوع چند انفجار در اربیل
🔹
منابع خبری امروز از شنیده شدن صدای چندین انفجار در اربیل خبر دادند.
🔹
هنوز علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/467298" target="_blank">📅 16:20 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
