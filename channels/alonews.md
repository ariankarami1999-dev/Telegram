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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 991K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-138920">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdGC1d4qEd2q9UEtR_qxuoLPjGNGugEqvL8_qviU26UMyFjAp3B62Nplet9Uig7LTnkAB_g0whR7OkKlRPhLYMMuJV8rEwYYn_db1Rzr4NFxZMKgZCsAOsV4a2NXvv2rQYpqvWRoIsXH_oJWxStmCi4mURAWCQgRvgS1rx0GDUKkUHDPwX_BIvXQxPhH3epVXVOQ9iU_VfSbxVvWGFxOlyeUIGrsqYodFFpRGsRcNWYzKIjYphvUxwAP9_joajqtMkAvxdJztoYvTiZC20d4lkFwXSLRl9y4_NSds2_Ai6aZYOZqlGuvdoJzTupn0077jD6u7Hyj3yX9FwXzZDBkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنت‌کام: چتربازان ارتش ایالات متحده در حال شلیک گلوله ۱۵۵ میلی‌متری از هویتزر M777 در جریان یک رزمایش توپخانه صحرایی در خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/138920" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138919">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5dd02235.mp4?token=tPs5UPs6VmyNaUzYJJVMg89v3gQpsDJw27gWX-_sFrVv2nQjYBV_XgAPfbipt6O6kHTD8QvcpyzmPRVnXU5oz5SsR3DwFLlmGpFagVHAaJNVkaWCXmp0UjvVY2tZXR__52juufbWIC4Rp5Lap_v7MTc3QIoxlnUxdd9V90058P5vuWk8lQJY2F8kr2pcGLNvOr55d3Fi1t0yfMJLWwQPl6PEybyTUppji2SSXJgrAn16K4MVlhXPz-5Q-aMzoSzkH737JVgvOADUbOUctjz_qbbap7ffxx7jVL0iPZ4F8MsTPXrzh-DAFUQJ5-WNq74lNL8HGI9fFvEbrkTakF0iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5dd02235.mp4?token=tPs5UPs6VmyNaUzYJJVMg89v3gQpsDJw27gWX-_sFrVv2nQjYBV_XgAPfbipt6O6kHTD8QvcpyzmPRVnXU5oz5SsR3DwFLlmGpFagVHAaJNVkaWCXmp0UjvVY2tZXR__52juufbWIC4Rp5Lap_v7MTc3QIoxlnUxdd9V90058P5vuWk8lQJY2F8kr2pcGLNvOr55d3Fi1t0yfMJLWwQPl6PEybyTUppji2SSXJgrAn16K4MVlhXPz-5Q-aMzoSzkH737JVgvOADUbOUctjz_qbbap7ffxx7jVL0iPZ4F8MsTPXrzh-DAFUQJ5-WNq74lNL8HGI9fFvEbrkTakF0iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انهدام پهپاد انتحاری روسی توسط موشک پدافند اهدایی سوئد به اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138919" target="_blank">📅 18:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVtuodePqyzmPuebm4OaEy2CVTcHdM9sV-xTTSYvvp5wCJlve4WNisuAZsubsqbktOnlStvfjLA4WKCfQJ3FHThvTyettThicW3s9eT_0w_1XetWcon5RcP4ZYGMTSgRtB8YsBeEtygW9lhKJtm_qC5ASY-sAlj78crRsqlv19J-uO9bhEfxFPcHRZXN4zscHOQ-hOzRDAKBTPEr9W2jyAVEgzK0O8QI1v3Hi3-_2nWvwgXiKFrpHIWCYhknrT87IitkSZMGEym4EXoENrvxr13wn-RG0LaUAGFPYCtBsJTy3JX6uVcUzORfM0SmMtn-T2zxOWnfs_53y6uGeTo6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اقامت شبانه مردم کیف پایتخت اوکراین در ایستگاه های مترو، به دنبال حملات سنگین روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/138918" target="_blank">📅 18:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، تلاش دارد پیش از انتخابات پارلمانی اسرائیل در اکتبر، به توافق عادی‌سازی روابط با عربستان سعودی دست یابد.
🔴
روزنامه هاآرتص به نقل از منابع آگاه گزارش داد نتانیاهو به چند تن از دستیارانش گفته است که پیش از انتخابات به «یک دستاورد بزرگ دیگر» نیاز دارد و منظور او توافق با ریاض است. نتانیاهو امیدوار است موفقیت حزب لیکود در انتخابات، زمینه‌ساز ادامه نخست‌وزیری او شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/138917" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ایندیپندنت: گسترش جنگ ایران، فشار اقتصادی و سیاسی بر ترامپ را افزایش می‌دهد؛ این در حالی است ایران توان موشکی خود را حفظ کرده و انرژی جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/138916" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138915" target="_blank">📅 18:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه: واشنگتن به حماس قول داده است که نتانیاهو را ملزم به عقب‌نشینی از غزه و اجرای توافقنامه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138914" target="_blank">📅 18:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138913" target="_blank">📅 18:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ایندیپندنت: گسترش جنگ ایران، فشار اقتصادی و سیاسی بر ترامپ را افزایش می‌دهد؛ این در حالی است ایران توان موشکی خود را حفظ کرده و انرژی جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/138912" target="_blank">📅 18:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا، بسنت : ما رابطه‌ای قوی‌ای با ژاپن داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/138911" target="_blank">📅 18:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4cb2787b.mp4?token=IVkTmHuelF2E_kFPksBERDTvzI8OHJahgqaa48eBerOmrFVF6i996I90OpGO5QVXPE54MrJj_f3HrOso-Jt4ljdV5MdwfdsayTyKkIfvcrK9a9-B7S_nz_omuqFP6xrSJ34-bgj5Z8nW1nxHqnPMK56Z9iE2IUrAS8ibHeRDui_rVGtQOPguN8nqMTWDjGCmsRfHVhmNeBbqJxNreK9PnnS8WyoebWRuusBRWJNNxniecdkCDTaRBMFXP52eWeBu1YTlqibEAS7xrfbbQIzPw1K-Zfc0mzY3CxuSIoCKyKrKhlMU9oaCW02U3Qo3tbB2iRkWG-VYjbBYPpOgX0soBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4cb2787b.mp4?token=IVkTmHuelF2E_kFPksBERDTvzI8OHJahgqaa48eBerOmrFVF6i996I90OpGO5QVXPE54MrJj_f3HrOso-Jt4ljdV5MdwfdsayTyKkIfvcrK9a9-B7S_nz_omuqFP6xrSJ34-bgj5Z8nW1nxHqnPMK56Z9iE2IUrAS8ibHeRDui_rVGtQOPguN8nqMTWDjGCmsRfHVhmNeBbqJxNreK9PnnS8WyoebWRuusBRWJNNxniecdkCDTaRBMFXP52eWeBu1YTlqibEAS7xrfbbQIzPw1K-Zfc0mzY3CxuSIoCKyKrKhlMU9oaCW02U3Qo3tbB2iRkWG-VYjbBYPpOgX0soBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در راه کمپ دیوید است تا با وزرای خود در مورد ایران دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138910" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزارت دفاع روسیه امروز جمعه از تصرف دو روستای دیگر در خاک اوکراین خبر داد و اعلام کرد که نیروهای مسکو به پیشروی‌های خود در شرق و شمال شرق این کشور ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/138909" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه:
واشنگتن به حماس قول داده است که نتانیاهو را ملزم به عقب‌نشینی از غزه و اجرای توافقنامه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138908" target="_blank">📅 18:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سامانه کشتیرانی مارین ترافیک: در ۲۴ ساعت گذشته همه ۵ تردد  ثبت‌شده از تنگه هرمز از مسیر ایرانی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/138907" target="_blank">📅 18:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر خزانه آمریکا: محاصره‌ی نظامی و اقتصادی ایران متوقف نخواهد شد و ما در سراسر جهان به دنبال اموال ایران خواهیم رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138906" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یک مقام آمریکایی: ترامپ حاضر است به مذاکرات فرصتی بدهد
‏
🔴
نیویورک پست (از رسانه های حامی ترامپ) به نقل از یک مقام آمریکایی نوشت: ترامپ حاضر است به مذاکرات فرصتی بدهد اما خواستار موافقت ایران با آتش بس است.
‏
🔴
ترامپ خواهان توافق است، اما اگر حملات ایران ادامه یابد، بهایی برای پرداخت وجود خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138905" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlHY_MIqa_q4m1LvxBM84_6O4T51lvrH0T7fJalNJ7cdDi99M9RjIxWzuQoLjy3vjUHbreNaPIb6EnWQ45YceXS14VLaMkugogwEb9vpwWK41uDZr-bcvP0ktAUQrlhQ7r-AauwxP9K3CmFqMqSOQhnikR58SgvMKShVHspDWkzochYG5SRdA2e9td57tBBd9bcoG2SiJxLa7EjCEd3q6UL3pGnoUHv91K2Dr_QzVi0ywy0KVChCOkVuDzmlIcQl3ZxpPp8WIqC-erLpTdwdXIrRwL7E8RdtG5tp8hbaFF-PS4IQpQGhy7m64UVUYh58OJ1ZX4F3QKZeZy9gBq5BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کاخ سفید: جلسه امروز کابینه دولت ترامپ به صورت زنده پخش خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138904" target="_blank">📅 17:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تماس تلفنی وزرای خارجه ایران و انگلیس
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138903" target="_blank">📅 17:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgPu2Z25DsAPqWBROG-x8BxUI-Btcy-zom6GfWtXcgMb0OX0Q8RsEXq6epoXaBLoC8HlM_GwG7Z5wxJ0IxugNwTTGfSGulzQ_oG3MO0sZWtgwQuOR8LyS3gn5j3zTFn8lmIZXsZi_R5QGv6gYQJNSsAAFaiCfHoiMoV4MTVhyuBk9AiZZDyicq4TKF8w8rPHWhPwsAXwiQfG9RdsKo0FNzWy_lIW91ZfExRa3ixnr0n05Gd6lHladLa3lKD3CbkPr1RjK08N8inFqFXCoGKNLfgT4PbST4EdtK50X2m7nhAeYhrRMJE677JLmoDVS1vuDbUZd8-_GOqScDbThw6yAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر بحرین: تا قبل از ورود اسلام، ایرانی‌ها در تاریکی به سر میبردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138902" target="_blank">📅 17:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل:
پیش‌نویس توافقی که توسط شورای صلح منتشر شده، برای اسرائیل غیرقابل قبول است.
🔴
عملیات‌های ترور در غزه باید ادامه یابند، همچنین تشویق به مهاجرت ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/138901" target="_blank">📅 17:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دلیگانی، نماینده مجلس: به‌راحتی می‌توانیم شبکه برق آمریکا را از کار بیندازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138900" target="_blank">📅 17:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کانال 12 اسرائیل: تا زمانی که حماس خلع سلاح نشود، هیچگونه عقب‌ نشینی نیروهای ارتش از خط زرد انجام نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138899" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138898" target="_blank">📅 17:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: اتفاقی راجع به ایران قرار است بیوفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138897" target="_blank">📅 16:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5lHI1d4DEP0SuBDWMcHWtQ930oU67IvkoZ5nz58ukRNafsmCbyBbRMEJyM0Cm0IMAYpnr7_KYDU9E_y3WCaksEhPMPNbtXP_tw1f7PdcrJV0QpAnd8OftXEsLwtIIrQ_AExefRELItJvlj7u7T5PaorGoil1dmasYVzUshXj6bnpCnXfZlP0cVwQGS1IywlDMVeIFvBL2qlDi8Fs9BMl6Wtxg1-lMPohTrymU_F_AiI4iaQxK7F7j4rk7kdhSWPeBBFhS-wmmrRLSPh-z33EjdwoETyusB7-n8MCk4N2BP4YzYgpbQB_eb7R8orHZwjs7_64ilk31hmv1QL6aLXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8bD7v3aDIO2nLDFddYsF17niTDUDn6WCr5RYDV3ps_PFJtMhtlv-DSUJgr83M-FnX_Tddw2jRCH4YVVa_hvOzXbjS6s_Im8Fqy7SPkjuW41-dIzGeW1fhdrZDQjHyMw3KmXSGGXyiA3TQ8IolSCvQQRy1YeaH1MuX618ri1AY3XBoVGKKs0lddCij0Iy8er0CC_HuOZQoEW66g7-uRyJmVTEo36Dwb17wB6-3uNVY2cQCUF-L2-BynwZyJ8LLbE-tSk9mZNw-I2ZcQV_YyCR-zV0gllTkCGGEA8dIitO0PxR_kLubgPE7Sv9mLxgcUV8SSvyHJWE4GDDcrwjyKbBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مقایسه جیره غذایی ارتش سوریه در دوران اسد و امروز
🔴
سمت راست جیره فعلی، سمت چپ جیره قبلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138895" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138894">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: جنگ با ایران داره خوب پیش می‌ره
🔴
آمریکا داره حسابی به ایران ضربه می‌زنه و ما فقط داریم پشت سر هم پیروز می‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138894" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138893">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=Q1fz3IowPz8oft3fDVnw5SzFRBAZiy6nkv6PT1KUO1fr_j6v0tNcKEdTMOZBdRx-PF-TEk--ljjJKDNh04znqj5S2lT7KJS9QYkWQvp-xnSjvEyWYv0pzNC8G-bny3ot2telP1JwxAmByZri40RFUAPoIE7g43bsOsZACFKB-zVXEPRCoDjHgjUGa61UbLSLaPLSLgRSX0w0zLkX4gglwtmNxnTpi9hFYn-G7XiqZ6ZWv9D5d_SWLpgGAfcDIxFTucj69nhYhXZdn-79VMDt269f-fjF7G6jc9BFFm8DBwDuO7mznvgPX6hk9S1DTYPyIkHGXqQn0Sn-abBwyxS0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=Q1fz3IowPz8oft3fDVnw5SzFRBAZiy6nkv6PT1KUO1fr_j6v0tNcKEdTMOZBdRx-PF-TEk--ljjJKDNh04znqj5S2lT7KJS9QYkWQvp-xnSjvEyWYv0pzNC8G-bny3ot2telP1JwxAmByZri40RFUAPoIE7g43bsOsZACFKB-zVXEPRCoDjHgjUGa61UbLSLaPLSLgRSX0w0zLkX4gglwtmNxnTpi9hFYn-G7XiqZ6ZWv9D5d_SWLpgGAfcDIxFTucj69nhYhXZdn-79VMDt269f-fjF7G6jc9BFFm8DBwDuO7mznvgPX6hk9S1DTYPyIkHGXqQn0Sn-abBwyxS0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجران مراکشی که از طریق دریا وارد منطقه سوتای اسپانیا میشن :
🔴
یه نفر دوچرخشم آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138893" target="_blank">📅 16:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138892">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOm_rb24WpauS_QcwUxtUuXPGsMalwL2Pb_UYlVltvmiiABwvH8TyEvgeVA-hp56yYhQYY4mQzqPGoOuXWmIX99QwxjTtNqM1TzAed5VCwgtIx_cjV2ABBfZ41h6J2dB3Tkv6iJ_4WhaYUyZYehRRps34AneGJR9zfJUmts79LBBGnsivOMMFVihU89h04ZEzVhVTqp3D3wnbUJsjZCMhjauQBdW6iQ_C3P2hVygCqsuqvkEny4R1cYemFIN-XpJQds_B0_mUQQR6I76NP4Qe5dkWslFCsC3g0W70EcDckjx8WM0POplc8JwJW68HmpbwGz_OX6QbERP2qnuZ2TKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لوومر، فعال سیاسی و مشاور نزدیک جریان محافظه‌کار آمریکا
از کارخونه تولید پهپادهای
SkyFall
تو اوکراین بازدید کرد
و روی دو پهپاد رهگیر
P1-SUN
امضا زد؛ و یکی از اونا‌ها به عنوان «
تقدیم به ایران»
علامت‌گذاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138892" target="_blank">📅 16:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138891">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏
👈
ترامپ در مورد اتفاقی که در اسپانیا افتاده:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138891" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138890">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5CF8DIHUJnVU622eHRzp-ujIUtgE_LU1KQYLSmlU6BDb42b4X9WhMeAHHoL56WaWEApKPAjb0inpUEoY3Qh0VJ1xkXRK-FULYmHCxqew9NwhjOFiAQJc6WVcOrg6Qkk6FnbUYP4G-P9n91_LcsnvXyPkITSJoVdiC87yocTAGaNBZO-b7_Ob7MNV-_LMq0CfydLU0DehIaxyhbQgiIRviL0Abm0iL3uq8slegGgF1N1D_Gt35vMV0YODEoW9yGEQ1RLz1kVVJGVElJHzHzpGulUjMHSjr97wOF6e-3gwrRg5W6FwcXUumOyFfII--S7yN7lzoRg6UdCHj4hdz-FXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوال و پاسخ هوش مصنوعی
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138890" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138889">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/re6I59c_C0eBZRqAWXdyfY3NAvm_T8gLO-f8A4QT5t5ptjczvkNdJUQLWmD80cn_NAQH86zyqjjrSiQxA7Mf5bQymGvRoNo0nUK0CCePjv5kamBsCUt25N55PnBFxLBotOMhNx9ql4nWMHF6R6UHOSNXQ4r1KJAdOiUsKy5ri-I1nQYwLPAiUNHBwAdYLRfs-FsWg50KNOdq2pHQWiy5ke2V2vc8uvwRivf4t3PZKUSdcKOXwy_comizTxzYK8ml4jxvfxb8K1jkZZwvJtjyorn_FjQRry0uY7xFMuC45PyNIhomnSqO2V1hXugT8pgyXaeeuHzq3rzf0uOYK-953g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی از ترامپ خواست تا از ایلان ماسک بخواهد که اجازه دهد از سیستم استارلینک برای هدایت حملات پهپادهای اوکراینی به پایگاه‌های پرتاب موشک‌های بالیستیک در داخل روسیه استفاده شود.
🔴
ترامپ به این درخواست پاسخ قطعی نداد و سرنوشت این پیشنهاد نامشخص باقی ماند.
🔴
اوکراین استدلال می‌کند که این اقدام به جبران کمبود سیستم‌های دفاع هوایی پاتریوت کمک خواهد کرد.
🔴
در حال حاضر، شرکت SpaceX استفاده از استارلینک را در داخل روسیه محدود کرده است و فقط اجازه می‌دهد اوکراین از آن در خاک خود، از جمله مناطق اشغالی مانند کریمه، استفاده کند.
روسیه پیشتر ایلان ماسک را تهدید کرده بود اگر بیش از حد به اقدامات خصمانه خود ادامه دهد، ماهواره های شرکتش را در فضا هدف قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138889" target="_blank">📅 16:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138887">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJ5AODmCKeBb6-2EWRLMXTKVXpOyXC1Cf-yhmjXXXhUkS7V9xtWvo4OBNSVuSjp5z79KYiVPfRVyqpnCvVBsoxR7IDSe48VmJYw3tlwhAXxV1P5wglmGS-C2cgD72e1wyZl6uozkvRAyRcs25TH9IRmbMrT6l6hHCvWe1uy_MfVOki0Hk9FfmCMecvIelkvmyp6tXRgubTytPhymxmAQDQgLyFbAAH2OayGxNV_GRFMlfbMPumoyBzn5AESIOMFF4Ct_d0VFOQhbsWgKUSEwZUDsuT9X5Y7JF7OVHS5_I5Db6wDc9xFAuMMzsR46uBY2Pg-EmrjvvaU_tfQTs3kBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=Xe12nTOskuDGZfYbIBk8HAQ6s_TR_zdLvMzsOa-36qibMtkmsadum7032gb2se18cCC5cyjlxa4sEH5Vzylwv0O_PTKLNVMH6LWvE2gha6tiJ2zy_JvB0FtyzMVK3FH6PDg44jHym03iTFAIdWqQlEpsTAWsJvV-tawY_6Nrkn6azpzeuIfjWjLSwIVnKYZVCacqmdUextn6eZw1ZQ5HQ_ncz3Ub4rdHsQeBgp0vXGj_MWjfGrNBfGKs381PvDUQ3J9Rm_WrjId_-vTsT5H6iV4DNwkDOd_UaPoumZvCrFdUWqHaJamvKWoRwyDYK4dc8xwKWyGLuFm0msCy8flnCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=Xe12nTOskuDGZfYbIBk8HAQ6s_TR_zdLvMzsOa-36qibMtkmsadum7032gb2se18cCC5cyjlxa4sEH5Vzylwv0O_PTKLNVMH6LWvE2gha6tiJ2zy_JvB0FtyzMVK3FH6PDg44jHym03iTFAIdWqQlEpsTAWsJvV-tawY_6Nrkn6azpzeuIfjWjLSwIVnKYZVCacqmdUextn6eZw1ZQ5HQ_ncz3Ub4rdHsQeBgp0vXGj_MWjfGrNBfGKs381PvDUQ3J9Rm_WrjId_-vTsT5H6iV4DNwkDOd_UaPoumZvCrFdUWqHaJamvKWoRwyDYK4dc8xwKWyGLuFm0msCy8flnCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدل علی خامنه‌ای در عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138887" target="_blank">📅 16:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc2bce2332.mp4?token=RH04ukA4F9Q4AawCvtQQfFr19rAJwAjn8Bprqek-QEZBd7IFyKrDR_g-_tum4dLAYram-RN-Fk2qPZ_LMHirIPZLSxa-j3IUk1Ov7HXJLvurAIu8F03f24_xEENt_oCd80ynfgH7hwF5LFUczSfVrXYbDgWhINx93Awzk3CZbl9fF4fKgm4KowPj660zs45J4cf_L1H2rkPiNsxDaiN6cUIgyIT4rlcO77daVuakYL2umlm8HTbwwNNvS25EUTPuGrMWOWIpUkLK8uz3fRIfjC1gkH-tF3Zv1QaEutgAH45uc6LaFpOTvtCtq6KZSeuZeuXTx0xXjdYU9RKYxMKgH4oyu8TnfQPvRxZAOlAXmXEqNlFa7ydmcdWCuKj3fOgYBwUOtDKaoGaiZk27ukQKW7s10tgwOGfkxpVqGDKMTD_eqEG7cW973a69NlOtaRaRvvEc0LNvn7PrOYWoJbCGVR_enE2q1WabTwZh-wzTZw_KJGQHL0D3ehRnzWihonSrLEpfYqjFh2O1zB5OL45wjze2F1PbLvJsFuI5rhX979RKYTZewdxBB4fyNAxQb8q4Tot7iGbHBL0JmOxpVO2qmQR1DRoFLjAkFPRmyzZ5uejIltOMwvJpUUHgoS9YNkoCOwJIVdCXhzDVqgyQBU9ZI6RsaHLfeTG91qNaYpsggi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc2bce2332.mp4?token=RH04ukA4F9Q4AawCvtQQfFr19rAJwAjn8Bprqek-QEZBd7IFyKrDR_g-_tum4dLAYram-RN-Fk2qPZ_LMHirIPZLSxa-j3IUk1Ov7HXJLvurAIu8F03f24_xEENt_oCd80ynfgH7hwF5LFUczSfVrXYbDgWhINx93Awzk3CZbl9fF4fKgm4KowPj660zs45J4cf_L1H2rkPiNsxDaiN6cUIgyIT4rlcO77daVuakYL2umlm8HTbwwNNvS25EUTPuGrMWOWIpUkLK8uz3fRIfjC1gkH-tF3Zv1QaEutgAH45uc6LaFpOTvtCtq6KZSeuZeuXTx0xXjdYU9RKYxMKgH4oyu8TnfQPvRxZAOlAXmXEqNlFa7ydmcdWCuKj3fOgYBwUOtDKaoGaiZk27ukQKW7s10tgwOGfkxpVqGDKMTD_eqEG7cW973a69NlOtaRaRvvEc0LNvn7PrOYWoJbCGVR_enE2q1WabTwZh-wzTZw_KJGQHL0D3ehRnzWihonSrLEpfYqjFh2O1zB5OL45wjze2F1PbLvJsFuI5rhX979RKYTZewdxBB4fyNAxQb8q4Tot7iGbHBL0JmOxpVO2qmQR1DRoFLjAkFPRmyzZ5uejIltOMwvJpUUHgoS9YNkoCOwJIVdCXhzDVqgyQBU9ZI6RsaHLfeTG91qNaYpsggi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما نوادگان یهودیان اصیل سرزمین مقدس هستیم، و ما بخش اولی از میراث یهودیت و مسیحیت هستیم که آن را گرامی می‌داریم و که به جهان تمدنی مبتنی بر آزادی و ایمان بخشیده است.
🔴
بار دیگر، ما باید ایستاده و از آن دفاع کنیم. این میراث در معرض حملات ناشی از افزایش موج‌های یهودستیزی و مخالفت با مسیحیت انجیلی قرار دارد.
🔴
این اتفاق تصادفی نیست که این دو [یهودیت و مسیحیت] به طور همزمان مورد حمله قرار می‌گیرند، زیرا ما یکی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138886" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138885">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ba8d8342.mp4?token=OFuRN8EnUYC1jJ8e6G8OVoJREaFKVCbuQspRs-xDcFvnvSk1uK8aG2YJiG9K5GOv-av-B01TNFD_3n4WU3wVI9A_Wd2UadCpJWx30P_Hu5ExBjrrxVQKDK5DK6QIlUMWPDFHkUjvW-kzLJWCTiZYO7d4V1m6bScdUbmzp0fzlXK8_s6zt4XUXw4BECRr-EMcnK7gQCRiwNuguj2dtYGwQ6N88mi8Go2jyJy8EoD2IxM6sqvi_h4zkgQ0oKK41C9VIDXHJkAaN4P0LpVVIAY4hWVmEI5zu97LcR-kD0upqCx9r38nu7YE51s5InDNoCXFQ824SqTsP6UVzbue6ymGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ba8d8342.mp4?token=OFuRN8EnUYC1jJ8e6G8OVoJREaFKVCbuQspRs-xDcFvnvSk1uK8aG2YJiG9K5GOv-av-B01TNFD_3n4WU3wVI9A_Wd2UadCpJWx30P_Hu5ExBjrrxVQKDK5DK6QIlUMWPDFHkUjvW-kzLJWCTiZYO7d4V1m6bScdUbmzp0fzlXK8_s6zt4XUXw4BECRr-EMcnK7gQCRiwNuguj2dtYGwQ6N88mi8Go2jyJy8EoD2IxM6sqvi_h4zkgQ0oKK41C9VIDXHJkAaN4P0LpVVIAY4hWVmEI5zu97LcR-kD0upqCx9r38nu7YE51s5InDNoCXFQ824SqTsP6UVzbue6ymGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراقب باشید در این روزهای حساس گول پروژه های رژیم رو نخورید.
🔴
از سرتنگ راستی بگیر تا رپرهایی که الان شروع کردن به دعواهای مختلف و اختلاف های قومیتی.
🔴
با آنفالوکردن مهره های رژیم بزرگترین خدمت رو کردین.
#پروژه_حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138885" target="_blank">📅 16:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138884">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل:
اگر ترامپ از ما بخواهد، به حمله علیه ایران خواهیم پیوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138884" target="_blank">📅 16:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138883">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euSQ5wo6nj4hRrWH_doaY9q6AbHPdG-o8B8RmW79EWRGT5eluyQxn44NzGdpDM_go8BoBnxiAohVVwF7xZEXXGOuenv4GbAPEvm7tZPoIaTecVu5y5isCKzI8CA46osj9rNr90GQLZwrJL_UyAw4NX8ddgpZ5LjtoQNJ5tUR10wIiAPf2ZpZA7Hs88o2EOS_y4Cf0S0wnrPDim7FRYwV921SYn9CcQ696YGMHsJalxPjnIpfPezxVgm57CZmwx8PSOZjWRTLkRI-encX-TtdcIrPTizrmJRKe3L45KzO4Qpn3-mtril__FPC-8uy6QqwS-4r-TotFJbRPFAXaUxVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: عربستان قصد داره یه عملیات بزرگ دریایی یا زمینی علیه حوثی‌ها انجام بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138883" target="_blank">📅 16:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138882">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66529904ed.mp4?token=ITNX2EepU8bvY_mW46WRkKEPb2wQm70It20svjJ8AUOu3Y_sxbD_iaO_b0uXQ9skPNG7pETqxuISMcnQ2QEDsahpL5-y6t29an2nQZB-CL-Cx6A8rJROQy2Tkp6NFY-cfDwhxsoHrS8s7L_fVwOsUYKOeHBBGV8eOaOxqadLmx744DkGQtPEjto74LQ3hI3W_ajsJOSXWJxYFOKCqMyk7BYoqb14sYOHld7vWPvOeoyiqQTxWog4vxlY4UKHmwGkHkY9pmYeoyKK6O6IvVEXNrgTPz8i-wWej1Fkhr1NJDwLa2DOzwJZAxQt2BYuYwCQjy0tejMcUQRmce5ddLswcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66529904ed.mp4?token=ITNX2EepU8bvY_mW46WRkKEPb2wQm70It20svjJ8AUOu3Y_sxbD_iaO_b0uXQ9skPNG7pETqxuISMcnQ2QEDsahpL5-y6t29an2nQZB-CL-Cx6A8rJROQy2Tkp6NFY-cfDwhxsoHrS8s7L_fVwOsUYKOeHBBGV8eOaOxqadLmx744DkGQtPEjto74LQ3hI3W_ajsJOSXWJxYFOKCqMyk7BYoqb14sYOHld7vWPvOeoyiqQTxWog4vxlY4UKHmwGkHkY9pmYeoyKK6O6IvVEXNrgTPz8i-wWej1Fkhr1NJDwLa2DOzwJZAxQt2BYuYwCQjy0tejMcUQRmce5ddLswcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغی جالب در ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138882" target="_blank">📅 15:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138881">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byXuivMr0W76Fdecra-oJb_giUipgUf2wqn3BgTkGaeSSk7KFalYX54zS1Ma4o9WnbiK3d8JMr24rkRgdmXAUvt4XTpyZanLyER3RVQ9IUEOSYHT_9cnsO9H9BaQWH6K4GJ69VmXEmuq3edbnOLd-PKohE26xtX05wXeL21a5wbYfjWBbfQ1ctICR94jj9vXQhY2xZdOlnhuNrIFKvyVvC6DicdTV1UPowxiXUNszu3AKfHBPxLWp_lBsGZ8L2MVKmbZNkP3P5N9WnxdNi-M7sstadRHQ77AhNwtBx7YYHLXBzx5qXkiLR3ndGyOMOuBXT6sUOvUeYDo9W5wPq7wtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ایالات متحده، کشتی قطری را از رسیدن به پاکستان منع کرد، زیرا این کشتی به جای مسیر آمریکایی، از مسیر ایران استفاده کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138881" target="_blank">📅 15:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138880" target="_blank">📅 15:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh26dInvcZlDJQfsdwakMLNxPXRxqyp4ZpWlxvNSiiWShI6iOE7S98FfiLyvf-bQKUp79jEfRrXVmrDnRkI70JopAoR0liI6vkA9Gu6Xn3tXvXanSTunNCo20y024BXdPYxGReW-dZunppuj6MfvYUP679LHuOQoqhck0Q2K9lDl3MrAmWWcEcdyqD3WOJTVkTAx7_dGuG8zThkA9rWOsBVWauCMQGHvtduylWCPkntuTpKgrbOht5Crk8fYn-596w9YZKe1NhuppdtP6bopI0DV9HlnZQpDk_cyC5d_UKKKzJzPzhD7jY7-g0o9DYKsInPfCjZKgynOWsVpFzh8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش باراک راوید به خبر طرح آمریکا برای اعمال محاصره زمینی ایران
🔴
آیا اصلاً کسی زحمت کشید قبل از اینکه همه سایت‌های خبری اسرائیل این خبر را بزنند که اسرائیل و آمریکا "در حال بررسی" اعمال محاصره زمینی علیه ایران هستند، یک نگاهی به نقشه بیندازد یا فقط یک لحظه از مغزش استفاده کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138879" target="_blank">📅 15:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRbLCZhMmFVjFGI0-FDmag9p8KRop4yHkO_hHlZsW49vjAtfnHR6jRyPkVLdamjIpNew8srVH7_iG0cT_IBCPDYcF32zx4G3xPdyexBJYYG_AAOkzAnXOdpgDRVNhAX_K9S-ZxaIEhyqwfhktdWFJ-SHFMur8ESjWHEb8OTaua-dP5w1Wmrrf3ldTGHc5pLLeMSDFRpWM2PqxHKzhYix1g4ED6uXSKDS51acxflrZcyjijvayG3nijNNaSbfjt4oB-PU1n9VAmAWP-T9xJorAdlhEXo3fjKjYelAXb8_4sF1Cr0_6Q5b8VaY2nywARVS0L7GzLvvbDFQXEDEFmF_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با یه
مهاجم مراکشی
که اومده اسپانیا مصاحبه کردن؛ میگه تو مراکش منو اذیت میکردن فرار کردم اومدم اسپانیا
خبرنگار :
چجوری؟
مهاجم :
من تو مراکش با یه نقشه همکارم رو کشتم اما بعدش پلیس و مردم اذیتم کردن و میخواستن من رو بگیرن برای همین اومدم اسپانیا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138878" target="_blank">📅 15:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844225751b.mp4?token=Kw9qGPkla5bEJ0SHIDpqv-obNmX8_womDIM4Pr38Jz_g22RzDy1McF2AUmDYFUIx26IjQ00ziRfmmumeid8Ay53WcgcLp1Rj3wSfu-Y1r2tzq3VTr8z15kjAeufAh2NdRr3GRZzzZEA81rvLO-dhyYs8Bf2NK_Budgt4xfc7oI6JjX6x5iTKg8bQ5c6DUvb9n5KQpM4oqb_0BPvemvpJRCySQsocoiy94lywyozdZkEc71hKAstkoIOVR-S7bPx_B5_-_jKsdcW-4v7Mm-c-J6q1UstcpY0ynm-wZ80BEswTirvVbehriCWNPGTUhBw2Pigl4MnaIY0NGK5X6VIctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844225751b.mp4?token=Kw9qGPkla5bEJ0SHIDpqv-obNmX8_womDIM4Pr38Jz_g22RzDy1McF2AUmDYFUIx26IjQ00ziRfmmumeid8Ay53WcgcLp1Rj3wSfu-Y1r2tzq3VTr8z15kjAeufAh2NdRr3GRZzzZEA81rvLO-dhyYs8Bf2NK_Budgt4xfc7oI6JjX6x5iTKg8bQ5c6DUvb9n5KQpM4oqb_0BPvemvpJRCySQsocoiy94lywyozdZkEc71hKAstkoIOVR-S7bPx_B5_-_jKsdcW-4v7Mm-c-J6q1UstcpY0ynm-wZ80BEswTirvVbehriCWNPGTUhBw2Pigl4MnaIY0NGK5X6VIctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان:
نیاز داریم مدیران و مسئولان کشور را در
زیر زمین و در دل کوه
از ترور ایمن نگه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138877" target="_blank">📅 15:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138876">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/415999864d.mp4?token=tDuhXfgnm_sr_olnPjTK1j9rqqvwyA35z_lx0NkIdutF6pLC02ugpzxqWJ0ZrE-zw3rR6fwvAhqSBQobY_uxBaJ6GhNX6-hTyP-zEr0_-lKZdKTcOrC4PrBy7a591DOPfvLI3jgpRY8qxSE_tdhfkyBUyRgkTbmtlsWPeCynqGqBkyzb0k13y4D4A7o5l915szbW-4gMd-1kRx73-v_BPKWbo0m4oVozJmsfY4HAPuWxo66Ej6HtS6vb8pPw0E3NvmkmntylATM81GfVxTaw2xbaFw01ibbM_Fe0baNEU19UFwoQU0CLSHgLy92Tms1SaD0pyVkR3QckKeYB_4vApw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/415999864d.mp4?token=tDuhXfgnm_sr_olnPjTK1j9rqqvwyA35z_lx0NkIdutF6pLC02ugpzxqWJ0ZrE-zw3rR6fwvAhqSBQobY_uxBaJ6GhNX6-hTyP-zEr0_-lKZdKTcOrC4PrBy7a591DOPfvLI3jgpRY8qxSE_tdhfkyBUyRgkTbmtlsWPeCynqGqBkyzb0k13y4D4A7o5l915szbW-4gMd-1kRx73-v_BPKWbo0m4oVozJmsfY4HAPuWxo66Ej6HtS6vb8pPw0E3NvmkmntylATM81GfVxTaw2xbaFw01ibbM_Fe0baNEU19UFwoQU0CLSHgLy92Tms1SaD0pyVkR3QckKeYB_4vApw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی وایرال شده از دو پرچمی:
هشتگ نه به اعدام میزنین؟ خودتون و خاندانتون و سس خرسی رو باهم اعدام میکنیم!
هر ۴۰ هزار نفرتون فدای یه تار موی تازه عروسِ شهید علیخانی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138876" target="_blank">📅 15:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVJzQgdZjcVRghj8qMo5CNehDPwYGbTJx5LxXwgrNZDqxVI8q_jYlrrZVgry5zSjQvD5eNAQ0hB5mZJ8P7g93ebjDFK8V9ZO1pPHCfEaJh-zQ_5yqXyB2u2GCCQ6xDgI_weqLQPkC83kDjfZGoVkWLZDAb6oUmDPz5srhfGk4SYSPSBm1p3R_le7gakuY3eMMSeR9adeINfKsp10ppN62ay-QW6W7VVCSV-x2z9vg1meUv-Ge4YjgLhAbx5hxoqctTDOiTxGASH1zbKjA04rfzjIIp1TS0X7J-AYDhISXI85J-7u55OeMZU95PkyCC2vcGUC8ZdjPr-jxlJVs8wIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: اکثرا خانواده هایی که بی حجاب هستن با مشکلات اقتصادی و خانوادگی رو به رو میشن ، خانواده های مومن و با حجاب مشکلات خانوادگی ندارن و فقیر نمیشن و اکثرا ثروتمند هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138875" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uteYEN8DwCXRX5eiwviruHk5oxP-DWjVso0NoQ0GVAzckI-SjenMLBP0J7kAqwqbroqPW_cTbTGQs8NHVATUB6wqXYdt_uiFN3h3YBya_qbI4xeqhUV2F5I8PW3gMzARjdrqm_URNsbyx_AhwKRpB3kk5Oj9HrBxB_U_5zIJtIbOdFd0pAbDDBgmXpPX_BdPPwiPSaey8f-_ThRrN0FnNbsuCj_-32MmioES2tsgyNUHa5Os2w2YcU8F6SblMc0gMQz8fq9YqpZ7gO5x71eshwxhoniJYTBY79lIxq7D7OVR48Kqtq9aY-YX-Wh73UKJc-WDMsZFKpHKCXzxvOQdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوید کلهرودی، نخبه علوم سیاسی دانشگاه تهران: با جمهوری اسلامی هیچ چشم انداز مثبتی برای ایران‌ نمیبینم و این نظام روز به روز ایران رو بدبخت‌تر میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138874" target="_blank">📅 15:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
استانداری هرمزگان: دود در شرق بندرعباس ناشی از آتش‌سوزی انبار ضایعات و درختان نخل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138873" target="_blank">📅 14:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138872">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تا الان در پی هجوم مهاجمان مراکشی به اسپانیا، ۱۸ نفر از مردم این کشور کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138872" target="_blank">📅 14:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138871">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-Mez-nn3NtWZ91ZWeEjfdurV6sLvCj3IDQrMH5jKPIawaatf4sGjEaAjH7Ekp6KrioX_owLGXm9_mRNqvtPIqk-j72UR8jEhYrm4eoQw_MkHi3Fs5LFWCA6xVyBbAriaKblpUerEBDxfIkNQOtcnooy_9ErF7mZOyzvooG3goTYSImiNXJ4TU2M67wM2Au83TnhGFRXXlf9mhFvaawC-4D2cWfTD5uSPUhcYlTuqu9g5UP9f_fck0JiDSfGX5gckKXOWhnnYLOy3CBjMw9iB6UIS7e9zh0ggOio2K_uj-o0Sg67mro2NyUtRGndrx60AtowGNetoFMUSEO_ArdANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ترکیه احتمال داد کودتای صهیونی آمریکایی(اعتراض مردمی) شکل بگیره و اینترنت مردمشو قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138871" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138870">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ قرار است امروز در میان تشدید تنش‌ها، جلسه‌ای با کابینه خود در کمپ دیوید برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138870" target="_blank">📅 14:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138869">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9Mf7MB-fc6Q2TKXfusy7fsM5yR-XTE7EWs8dgEcjAXdsw8xrHRKss2uN1sQXypStU2T7T_KZ4P5Ut-txWnF-1aQnO0DfL7UnjHQMQ6wiGlV9XMDf7cbI9mpBD7DfmWlNAXSPxNF-cPh3OJrWQpMtj63okYqGDRRmhMPRkK0ejo-s3CmLQyDzeixgXcNL5YB6uqOtGX6Rgr3njiZjsGxnTp8pn9faL9ZX08zTug3LfTSi6IdQ9nLYaCqRoC92zLFJab5UuQYChZUakpXuBqNJNqVOJd4LJoG9v0Y6p4IdORV6uwKp23H_1B-UWKvTGRDUF6vlP2eVci_8fi6kercpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نیروی هوایی اسرائیل به غرب شهر غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138869" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138868">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کویت : از صبح امروز چند پهپاد
وارد حریم هوایی کویت شدن که نیروهای مسلح اون‌ها رو شناسایی و منهدم کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138868" target="_blank">📅 14:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138867">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0HU3YhjIGc1TudVbe4YJMNy71pdm0EWY170eJQTMnql-vFZxEyCQsOamWWxGk5lTEmROCV-iOmgUPBrx9beHSm6QdHo0BMKjRiEyubTe-IO32gPa8YjpcFAcAL2Idsf9fzaujB55DfhwumScf6EmJeI66-fpInHIUYmA38knPB6b68hDiQYpIqm269hdlnNhvbQdr3Idi-OdN5u1PrWPWIDxCh06s3Xze-5TIV2syPKZKq45WRLlZdCdlhhL4O_T-oL3qPbuTRZhGjmLO7jwN4i_Uj7VXmQhyako0P3azPhZeGkP5fv3CO9ebBMyQXOmbkASk9o0wrEOjVC5zRU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در یک مصاحبه، از یک مهاجم مراکشی می پرسند که در کشور شما جنگ نیست، پس چرا دارید به اسپانیا فرار می کنید؟
🔴
‏او می گوید چون در مراکش مردم مرا اذیت می کنند. من همکارمو کشتم و پلیس و مردم دنبال من هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/138867" target="_blank">📅 14:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138866">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل :  اگه ترامپ از ما بخواد، به حمله علیه ایران ملحق می‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138866" target="_blank">📅 13:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138865">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی آتش‌نشانی تهران:
دود مشاهده شده در آسمان شرق تهران، مربوط به حریق ضایعات و فضای سبز در محدوده جاجرود است.
🔴
حریق در دره است و آتش‌نشانان در حال اطفای آن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/138865" target="_blank">📅 13:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138864">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4La_MtauETFjOTDWWCg_cYyi95BqYiv7aBWR9Ingk5vXAc3GZf9JkKUX0O1ewVj9n9KvtntOoT3ik_TqK2FFSYOFYTIWXHvhmwTLlaeWTGaPuzwVfnay23U-XlRf8Br9aDaYGqsoeHpFH1HDPVe0UwApfRBLAGDvHkGGgUAbfX-k334eXQ7N-yMj8Zptdbx6-V-SA5aUsJyT4df9c3JI3wGKcEUzXutkTEoWu74iufcGJdxaUDpP3v9rEjwp_0vL5emCBOALAt0UI32As1QpCw1bQaMTWbHFxIjslmxxDkTmmZoBJ8uJBviggInEpdeI4vxuPRolr185jZVwn13IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت در ترکیه دچار اختلال شد
🔴
بزرگترین ارائه دهنده اینترنت در ترکیه در حال حاضر از ارائه خدمات باز مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/138864" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138863">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
عباسی، عضو کمیسیون آموزش مجلس:
چون کنکور یک ماه دیرتر برگزار شده است، سال تحصیلی جدید دانشگاه‌ها نیز یک ماه دیرتر و احتمالا در آبان‌ماه شروع خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138863" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPDQ9zkiMpHBqR4LlnyvO0hhLN-o-OVkOUUnvo6iGPEYjLr5b-IWheVefM97uYaycXlggP9KQuPTrk0meuq8PkEDY8hu9f9fvuu_BhjNKFIwznBikwNc7zaEQNMSRHDLLGTUZUaVLNhQTZlBj-gWDfnStE1sCjqNoI-GXw8vtkE51puu_pOtSVLFO_uzDVOLlb9gRi4683nF1hq-D-rRLIMxd9Xj1qOSlLai4KX4AoG1RyrQBqocgbLSvYoamnbxj3T8r-ukHPAWFzI3G-sYsUf-dl0AZPDPyM28PsEd2ujyceARoCjXLg6jYQuYcl_wrB1SopCTpNHuGMnuQYjX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی پیش انفجارهای در تنگه هرمز رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138862" target="_blank">📅 13:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
منابع عربی: ایالات متحده، کشتی قطری را از رسیدن به پاکستان منع کرد، زیرا این کشتی به جای مسیر مدنظر آمریکا، از مسیر ایران در تنگه هرمز استفاده کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138861" target="_blank">📅 13:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c38ab5a46.mp4?token=C0h-zFc4ewlO33tuz-bdypYmJqEuxvD6bsMMmxlFIv-TTZOjqGqvwXuLx7_qY3ARknjvNrq7GeexJcdN6ZfksV-t0zQ09Vi2x-fKH98RGKFPGTmJs7fJI4kHrPRExjAslasXNbwtnYcPTq-D9CfHLu-fhO3UCux2Z-wQ6bfLHhsch4_isQLrG05dpQzMp2uAQKuBjDhMw3S3RG58MUv5oRi_phfE17ClWPyhBgNLSDM1nFITSzBU2gc--QMndR8ck3sO6v6_CqhgVdH5n4fl8dEB6YqRC3Dw18vZwfI7eZf4Rd1wrvMHVSc_6w6KdfB99b6SwLUTfndireIvVaqqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c38ab5a46.mp4?token=C0h-zFc4ewlO33tuz-bdypYmJqEuxvD6bsMMmxlFIv-TTZOjqGqvwXuLx7_qY3ARknjvNrq7GeexJcdN6ZfksV-t0zQ09Vi2x-fKH98RGKFPGTmJs7fJI4kHrPRExjAslasXNbwtnYcPTq-D9CfHLu-fhO3UCux2Z-wQ6bfLHhsch4_isQLrG05dpQzMp2uAQKuBjDhMw3S3RG58MUv5oRi_phfE17ClWPyhBgNLSDM1nFITSzBU2gc--QMndR8ck3sO6v6_CqhgVdH5n4fl8dEB6YqRC3Dw18vZwfI7eZf4Rd1wrvMHVSc_6w6KdfB99b6SwLUTfndireIvVaqqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه در واکنش به تکذیب‌های سنتکام تصاویر انهدام یک نفتکش در تنگه هرمز رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138860" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138859">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
تلگراف : آمریکا و اسرائیل درباره احتمال تحمیل یک محاصره زمینی به ایران بحث می‌کنند.
🔴
این پیشنهاد، یکی از طرح‌هایی است که رئیس‌جمهور ترامپ و نخست‌وزیر نتانیاهو برای افزایش فشار اقتصادی بر ایران بررسی می‌کنند.
🔴
چنین اقدامی مستلزم آن است که آمریکا و اسرائیل از کشورهای همسایه ایران بخواهند مرزهای خود را با ایران محکم‌تر کنند یا ببندند و تردد کالاها به این کشور را محدود کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138859" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138858">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=H0aNX9E_I7SWQKuNXlvXb-CTIjs_C12JRt2SgRyMgy1Wi5BDkJPcyLIi288SVsASxQefD91MdiRipTjt87RFBmShAUHtHk1wd8PexFz0n0r94oNHQSEw_fDjqifx5sV18NnKwO3JVgris3ADrj64EDua2Fc7eTCtdcBLHW1HAOZgv1sKzLVkzG7wQfltw1aL5ICyt2g4EEQLxQcyZ5WOhiUVbkn8NA3zMB7DeMCFZad-Xc6-qtEU-NjrvFFIwv5oomovF8RP-AAy3bYNXLooSHwXruX567hWwfzvlf39OybOW9YH3sHwfv7edN6i1zKFJaC-pz3gZswMecT5OhtT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=H0aNX9E_I7SWQKuNXlvXb-CTIjs_C12JRt2SgRyMgy1Wi5BDkJPcyLIi288SVsASxQefD91MdiRipTjt87RFBmShAUHtHk1wd8PexFz0n0r94oNHQSEw_fDjqifx5sV18NnKwO3JVgris3ADrj64EDua2Fc7eTCtdcBLHW1HAOZgv1sKzLVkzG7wQfltw1aL5ICyt2g4EEQLxQcyZ5WOhiUVbkn8NA3zMB7DeMCFZad-Xc6-qtEU-NjrvFFIwv5oomovF8RP-AAy3bYNXLooSHwXruX567hWwfzvlf39OybOW9YH3sHwfv7edN6i1zKFJaC-pz3gZswMecT5OhtT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رائفی پور: بصورت زمینی میتونیم بریم اسرائیل رو بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138858" target="_blank">📅 13:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138857">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f540d88d.mp4?token=flMqQ6OjQdbJEqTlD74prO-bAm3FV9Zw8Hw-zD7KN6CfPZRsaGjISeuNH461ataZV93TvjdIQcBbzRoAoForvJlXi3iBoGFxNvwrvdKNuV8egQHCvYDVuHmvsF1yBq-7MbzXYdsAa_COvDkkmddZ1ZHFixXeTrZ8eAFxjfYSHlqzxHDStQNyf0cbACNphZ-IpOR91m8knGRet-ZazHGkUaXVbc1dFroopL0g5DDmIAsG94aiKwZUpF5xg_6A7PtNIPMij6MxHZMoSOpIqXMP-TSS96lOpOLXd5eM6TqVh0vOn_WYFBb14fPzuQpTghaWmRuufoKJH6QPmKy-IIxxJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f540d88d.mp4?token=flMqQ6OjQdbJEqTlD74prO-bAm3FV9Zw8Hw-zD7KN6CfPZRsaGjISeuNH461ataZV93TvjdIQcBbzRoAoForvJlXi3iBoGFxNvwrvdKNuV8egQHCvYDVuHmvsF1yBq-7MbzXYdsAa_COvDkkmddZ1ZHFixXeTrZ8eAFxjfYSHlqzxHDStQNyf0cbACNphZ-IpOR91m8knGRet-ZazHGkUaXVbc1dFroopL0g5DDmIAsG94aiKwZUpF5xg_6A7PtNIPMij6MxHZMoSOpIqXMP-TSS96lOpOLXd5eM6TqVh0vOn_WYFBb14fPzuQpTghaWmRuufoKJH6QPmKy-IIxxJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستونی از دود در میدان نفتی الاحدب در استان واسط عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138857" target="_blank">📅 13:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138856">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmMUmw3Qr8zE9_waObvwPi_MKRcx4skI3EgeYQ4I96WJ7ER4ChmXWhCdgyYdIr6yzfhdfZoJ81nxfIilt7N7GlHgE-UoFy_fhv6WBSkYVULLDtjDvTrUSdfrzjGfUEjbs2R_YBLkt3ErK4VYxoIMuwe_fR6eQ9c9o6xIXQWvyoMYbmq6IzekaLOmu5P43eOHRbhyVN43aTIHLna5_V02Rhz1O0Yx4af72eKZMFd7Ddom61A-j7IyQyruVPHONNsx_3soe1wTiPmVFeH29S6RqNMXc2QW6_RQ2SwX0ohd0QvAmHUupE-91o_nHpj5hT3WCGsswG05pcsRk73Uvef_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک سوخت‌رسان هوایی KC-135R نیروی هوایی ایالات متحده که در یک برخورد هوایی کشنده در مرز عراق در مارس ۲۰۲۶ درگیر شده بود، برای اولین بار پس از حادثه در فرودگاه بن گوریون تل‌آویو روی زمین شناسایی شده است
🔴
این هواپیما با شماره دم ۶۳-۸۰۱۷، در برخورد با یک KC-135R دیگر آسیب دید و با بخشی از دم خود که گم شده بود، فرود اضطراری انجام داد.
🔴
هواپیمای سوخت‌رسان اکنون در حال پخش کد تماس "RCH564" است که نشان می‌دهد تعمیر شده و ممکن است به زودی به ایالات متحده قاره‌ای بازگردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138856" target="_blank">📅 13:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138855">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAIJj9LS26Mtp1ekMKn0jUOPd_ucGG3RiRd1wEzsoQpQQF9h2eMzfmYtljcC-FEqR_1ZtfYvXsZ2fI8UYoA4ByIxQAmicGYl2bIOa_3WKuEcenraCBegB9nluHPHg23-jjANWY01_9XiB0vu0W3C2tJg5tpeWGIQyDcfr-kXcoSdIggkkA5RPXyAxm5GMOZlf8ujvgi8yjwV6wCE6cykJPzyoSJxuyRGondZtCjPCRWxzMh4G2vfElpwG_HlPkwU4Bw8e7A-nDouWvuGZVjw2dRyvXEIhY1ccHqgYjTGqXJeJoCDo-L1mm1-_OA3P98R7kflJeEFHJH4XtZ2Y_f74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده ولی فقیه تو‌ سپاه:
آقا مجتبی خامنه‌ای رو
خدا
انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138855" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی 4.6 ریشتر، ظهر امروز منطقه دیباج در استان سمنان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138854" target="_blank">📅 13:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روایت سی.بی.اس از رقابت نتانیاهو و بن‌سلمان برای شکل‌دهی به سیاست ترامپ در قبال ایران: سعودی نگران است نخست‌وزیر اسرائیل به دنبال تشدید بیشتر درگیری‌ها باشد
🔴
نتانیاهو سه پیشنهاد به ترامپ دادن، از جمله ادامه محاصره و اجرای حملات علیه مسیرهای زمینی انتقال تجهیزات
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138853" target="_blank">📅 13:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a7007d893.mp4?token=PaBscM-lo_S9RQlCndXAx86W28ao_H_gNXpWgVNJOM-IsRiVx_X_J1CPTT6DHMc0F-74z38MeMRM8Qck52sf4ptcl8FBi-EchmpLMRyYtY6jks_ubPi4gFM6PTfsNRZy0dMpmbfleKxL2dxF16e9YBV-AI4fPAA89dO3CA_xJrDb1s1lwXmGnwduSOc5gZpGgTXaO4xNrORKtKh27-2thQShjQIYaJE44LViGRdswso4IJMn1xw_ovuK7heAGGua8M5By7cFKjqCWEDyl3bpCLTSVgga4bVlrp1q4WcjRDh5jLbc92wElx5yik-7cLbISs43-h8-TWnJfPxgx2Xa4XwqhROvlDNzYAdoBIQFf5Zsd7k3LzSWVhWh960yM2C_TeZlBqaojB_ATjWIVGt7XyW9s843yYF9yp3l_hy-uxzolRgHaxdJilGL7tw6dGyE-hKEFfHMjPqPbB45IjWEEcS_9gv0hAvH5eehX6sj-ZLRmMO_HKlMY4egvdJsLdblqcKOSpplVRuPVTFldIrOSAWuQMw4W4aM6ggUYocP-OXMTSWSIfmN75b_-wapz848z-LF9ukYLjKZshaJs_vcITpJX60vkXBEitUAxJJ22I39CRAX9PxMB1rOf39UzenH809ufqxaQ5JTmbDdqxKiDJXmQWlFXnFtK_lUHvG2lJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a7007d893.mp4?token=PaBscM-lo_S9RQlCndXAx86W28ao_H_gNXpWgVNJOM-IsRiVx_X_J1CPTT6DHMc0F-74z38MeMRM8Qck52sf4ptcl8FBi-EchmpLMRyYtY6jks_ubPi4gFM6PTfsNRZy0dMpmbfleKxL2dxF16e9YBV-AI4fPAA89dO3CA_xJrDb1s1lwXmGnwduSOc5gZpGgTXaO4xNrORKtKh27-2thQShjQIYaJE44LViGRdswso4IJMn1xw_ovuK7heAGGua8M5By7cFKjqCWEDyl3bpCLTSVgga4bVlrp1q4WcjRDh5jLbc92wElx5yik-7cLbISs43-h8-TWnJfPxgx2Xa4XwqhROvlDNzYAdoBIQFf5Zsd7k3LzSWVhWh960yM2C_TeZlBqaojB_ATjWIVGt7XyW9s843yYF9yp3l_hy-uxzolRgHaxdJilGL7tw6dGyE-hKEFfHMjPqPbB45IjWEEcS_9gv0hAvH5eehX6sj-ZLRmMO_HKlMY4egvdJsLdblqcKOSpplVRuPVTFldIrOSAWuQMw4W4aM6ggUYocP-OXMTSWSIfmN75b_-wapz848z-LF9ukYLjKZshaJs_vcITpJX60vkXBEitUAxJJ22I39CRAX9PxMB1rOf39UzenH809ufqxaQ5JTmbDdqxKiDJXmQWlFXnFtK_lUHvG2lJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو سرباز روس هنگام حرکت؛
با (ATV) روی مین ضدتانک رفتن و انفجار رخُ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138852" target="_blank">📅 12:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138851">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02807afcad.mp4?token=kBGAAH-fDqPDHnHeC9OHdoVVTJUJLF95menqiCgf6izCSEMC3FpI2zKORnh57gDcomKjND5QQR-FnibJZrGg4IoUB50zz72uOwiKz0Orlq94AL7UzjIuR9CospjGp7tcD7YiQRPKPsNhxxrg0hrLfy5_CU4ONGDj7vZ9C60KVfO1IO8RwJXrfmwV-dyx3k4NrsHmzDs4cVGJKtGpVeuC-v4m5td4UJLGjOsrD-KsPV2yNQFXWbm1VtnScBjyIranUOzkIgrG7Smu_PYqsq-HiipZ7_X5YHxc3eXms2LnDTUzxlaeLPKrRBqkWBrzDn7H2HUPe4aEGswtpl0ygS3UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02807afcad.mp4?token=kBGAAH-fDqPDHnHeC9OHdoVVTJUJLF95menqiCgf6izCSEMC3FpI2zKORnh57gDcomKjND5QQR-FnibJZrGg4IoUB50zz72uOwiKz0Orlq94AL7UzjIuR9CospjGp7tcD7YiQRPKPsNhxxrg0hrLfy5_CU4ONGDj7vZ9C60KVfO1IO8RwJXrfmwV-dyx3k4NrsHmzDs4cVGJKtGpVeuC-v4m5td4UJLGjOsrD-KsPV2yNQFXWbm1VtnScBjyIranUOzkIgrG7Smu_PYqsq-HiipZ7_X5YHxc3eXms2LnDTUzxlaeLPKrRBqkWBrzDn7H2HUPe4aEGswtpl0ygS3UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس) مجری برنامه کودک دهه ۸۰ و ۹۰: تک تک بازداشتی‌های اعتراضات رو باید اعدام کرد و نباید به هیچکدومشون رحم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138851" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d9b65cfa.mp4?token=eQSQIXsR7A5CfeHnSkz6km0cQIabTSBUD2Lc9iu8xBKjQNkHt1RRYLpI3oo73z4p31RmviW9ibGA3nFCuvZ6NYUgqutKzKPwQv4Dp7NX1l0JyfGI8HlujSvCX5gilDm6NJHKwrnVjwkJVNBOvD55kX83MoA5_jy4l4QdyytnAw7n1xCBWyhzKgieXNYT9UQCsudqaH1FhNRb9GvpZJmhyLkgJa7Ak7M4PjIHAgSf9mK2i1o0yLwaQMFN3kWM0hEYBzdbZ4UvhD_m6XODmYKPtg_2ROOCxJfa7ZBV_a85UfYLQxtpabli-pmq8aR2J5DneA9zVRWuKml2egvBPr9AcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d9b65cfa.mp4?token=eQSQIXsR7A5CfeHnSkz6km0cQIabTSBUD2Lc9iu8xBKjQNkHt1RRYLpI3oo73z4p31RmviW9ibGA3nFCuvZ6NYUgqutKzKPwQv4Dp7NX1l0JyfGI8HlujSvCX5gilDm6NJHKwrnVjwkJVNBOvD55kX83MoA5_jy4l4QdyytnAw7n1xCBWyhzKgieXNYT9UQCsudqaH1FhNRb9GvpZJmhyLkgJa7Ak7M4PjIHAgSf9mK2i1o0yLwaQMFN3kWM0hEYBzdbZ4UvhD_m6XODmYKPtg_2ROOCxJfa7ZBV_a85UfYLQxtpabli-pmq8aR2J5DneA9zVRWuKml2egvBPr9AcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش هایی از مصاحبه محمد عرفان؛ بازپرس سابق جنایی:
ما همیشه از اعـدامی ها میپرسیم آخرین خواستتون چیه و هرچی باشه اجرا میکنیم. یکیشون گفت آخرین خواستم نیمروه. نشست ۱۵ تا تخم مرغ نیمرو خورد و بعدش اعـدامش کردیم.
یکی دیگم بود میگفت آخرین خواستم اینه که با خانوادم صحبت کنم؛ هرچی زنگ زدیم تلفنشون مشغول بود. ماهم دیگه اعـدامش کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138849" target="_blank">📅 12:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1eec1722.mp4?token=ZTTChgtycse8SpSiGpEAfx5Oce7y321ZdXalIGbZ0JVcJGsBeu0zvug9pr8aV7Kn4u1bv_rb2htzHcy9siKl7S-fyyjtB1ZPVgbLYEoEYRpARjhqDUBtzvFOg0Yv4DoSSrzUvYZids8nBbZrzT-ynHxnw8B8Bq8BpLnOn-YT6mlOXSHH-QyxDvc3ib0xA0Dip2Kedl-fFBIDLKlwv4z9YoPUhh6Vz-FivKHfB6xV0NOjZV2-AwapkSQFAYIcHIHxAkE5ck5RF0zM1_vKQ_U79BNHSq8soeTjxJ0huDWC538zdCcr5dpcZxXS3DcTCJs76-gmZuuLsY2WIGNcfk_2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1eec1722.mp4?token=ZTTChgtycse8SpSiGpEAfx5Oce7y321ZdXalIGbZ0JVcJGsBeu0zvug9pr8aV7Kn4u1bv_rb2htzHcy9siKl7S-fyyjtB1ZPVgbLYEoEYRpARjhqDUBtzvFOg0Yv4DoSSrzUvYZids8nBbZrzT-ynHxnw8B8Bq8BpLnOn-YT6mlOXSHH-QyxDvc3ib0xA0Dip2Kedl-fFBIDLKlwv4z9YoPUhh6Vz-FivKHfB6xV0NOjZV2-AwapkSQFAYIcHIHxAkE5ck5RF0zM1_vKQ_U79BNHSq8soeTjxJ0huDWC538zdCcr5dpcZxXS3DcTCJs76-gmZuuLsY2WIGNcfk_2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروندان اسپانیایی در بارسلون اسپانیا، در حال نصب سیم خاردار بر روی بالکن های خود از ترس مهاجمان مسلمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138848" target="_blank">📅 12:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سپاه : دو نفتکش متخلف تو تنگه هدف قرار گرفت و متوقف شد
🔴
۴ نفتکش دیگه هم بعد از هشدار، مسیرشون رو عوض کردن و برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138847" target="_blank">📅 12:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU-QY2X4YXtZq8oq7_5YRuUHQQ28rVXG6gjIJwoGamIpBVuW0LIsdsPv3xr_fRsisRtpjQTxtKAIp0X58xf7xvhMN9eSA8RyjhcNE3sElO4zDhXrtjbAH6o_TItYkNl3Q4VJeADtQYgBVfDUbu4t3H5MNfDj6LIUROwZ3TlhpTXAuxawD-2GeRyWjBJb6QzQo0w_cbvepKan12HfvfBgA7tQoTU1PLXTJjKPoys01x3Sjw-TWuwDxMOdVJ1CMDVpE9OrT0F7SyF4O1JHd3KMMx7ZOjzEN27zvtvWsYeoKQ3FFQ6yzUDOWjrTn0nPpWvPKq30ILJ9JMIPrEMkfAYaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مسلمانان مراکشی به منطقه‌ای خودمختار متعلق به اسپانیا در شمال مراکش حمله کرده‌اند و تقریبا این شهر یعنی سئوتا را فتح کرده‌اند
🔴
سئوتا خارج از خاک اصلی اسپانیا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138846" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDC9BI6cYFLw0KWVJqOgP0glrXYebVnylptieSjwTNSixkeXyd2H7d0Qt2xLDFgyvVPmIa_U4QikGrIp8hasCB1-PWduikeAWPl_L_z5zuT0fMztOOdlVrVP-sIbVTZZl-h3O7nqLDmJMnzkiJZzjNZVN52uAV1oyJyzMVxqJK1gncObpokb7HOge8aN-ZeWC6UTFixPPr-zdncFRTwJbtgrxoZVCZjHkGm5bT9n7MSuQn-f73IkS3SKvMUgybXJGGY1xLFDWmCtOWTLiH5SAeeo9Xr8RMZGcHW-t359m0Yhts6dMN0fnWnSEpoXsyNDt1WxTmI_Hx1EGRikDTEPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پشت صحنه «مرد سه هزار چهره» به کارگردانی مهران مدیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/138845" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1225749b49.mp4?token=D66rxxH8s5unHRB6UcUqcGxTX5GQGw6OJ7lIxaIlYw6yQ02N_s0q1eG0EKn-4etgil8upNqa2_zVKjGMKqa9BbujtpWubxG_zrfaaQSbIUssKu-RufTAeIK27vPmQ_1-8id3f4t9FBbpo9rwBCvla7vEj-XaW9nkIxHEw2a44wYNV-8i_QhG5R7s2tEWtFD4gGTwitmI965veOB71hvfx98w1OSVavjp8zqZqrGz3_wUF-uwb4VONCFLVk_txXwmOviGylCS4BLcp5dP2xz5BkOvPQRMci9Bz4LbWsOsT0arUVW0alAMRPJXD6rf7mW2JZJNUPOajcYjM1jSePR8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1225749b49.mp4?token=D66rxxH8s5unHRB6UcUqcGxTX5GQGw6OJ7lIxaIlYw6yQ02N_s0q1eG0EKn-4etgil8upNqa2_zVKjGMKqa9BbujtpWubxG_zrfaaQSbIUssKu-RufTAeIK27vPmQ_1-8id3f4t9FBbpo9rwBCvla7vEj-XaW9nkIxHEw2a44wYNV-8i_QhG5R7s2tEWtFD4gGTwitmI965veOB71hvfx98w1OSVavjp8zqZqrGz3_wUF-uwb4VONCFLVk_txXwmOviGylCS4BLcp5dP2xz5BkOvPQRMci9Bz4LbWsOsT0arUVW0alAMRPJXD6rf7mW2JZJNUPOajcYjM1jSePR8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هشتاد جلسه‌ی دادگاه برای اثبات جرم حمید نوری از جانیان شکنجه‌گر دهه ۶۰ در زندان گوهردشت در سوئد برگذار شد که این حرام زاده محکوم شناخته بشه که البته بعد از چند سال هم تاختش زدند و به رژیم جمهوری اسلامی برگشت.
🔴
برای حکم اعدامی که به محسن شکاری دادند فقط ۱۷ روز وقت گذاشتند.
🔴
حالا چطور میشه که کسانی که در دی ماه خونین بر اساس گفته های رژیم جمهوری اسلامی تعدادی از نیروهای انتظامی رو دستگیر کردند، شکنجه کردند و بعد آتش زدند ، بررسی مدارک جرم فقط در مدت ۶-۷ ماه انجام شده باشه!؟
🤔
مردم به وقتش پوست از کله این حرام زاده ها میکنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/138844" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6414829db4.mp4?token=bm_16AGLk8TWi09895ZMAZJsTA_kkemtEhSGtXES76VktjGM7SBP5kKcDsGXHAw1-FGgtBnC9n2XWTj39Gl9g-zZZniZQmSDWRmprOWCjvYbyGt70jAoeRgU0TpI80XXzkW6h8zkA6A2t6QTjtrkl3_SPuFexKfaNkKfBfXxXHe-IgKvhAtsIjdWIfAd-JS1UA_OvnY_41YsxF80dREo-yftpHh5tCJiq6zaKH8Nd2mnhqKpPqJAkHZj3xqW7Bte2jpnaEjj1EC6rnpO1yqFKJ3YyjjwojIdO9ev5boZqUKyQH4Fxa8I4cytjXycJ_fRV87-YavynWEEc8dsqBjHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6414829db4.mp4?token=bm_16AGLk8TWi09895ZMAZJsTA_kkemtEhSGtXES76VktjGM7SBP5kKcDsGXHAw1-FGgtBnC9n2XWTj39Gl9g-zZZniZQmSDWRmprOWCjvYbyGt70jAoeRgU0TpI80XXzkW6h8zkA6A2t6QTjtrkl3_SPuFexKfaNkKfBfXxXHe-IgKvhAtsIjdWIfAd-JS1UA_OvnY_41YsxF80dREo-yftpHh5tCJiq6zaKH8Nd2mnhqKpPqJAkHZj3xqW7Bte2jpnaEjj1EC6rnpO1yqFKJ3YyjjwojIdO9ev5boZqUKyQH4Fxa8I4cytjXycJ_fRV87-YavynWEEc8dsqBjHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اگر براتون سواله چرا این همه وحشت؟
🔴
چون دیشب مهاجمان مسلمان که تازه رسیده بودن به اسپانیا، ماشین های مردم را به آتش کشیدن و آهنگ های عربی را در خیابان های اسپانیا پخش کردند و به خونه مردم وارد شدند و از آنجا دزدی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138842" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=MI-dX3SpRnl287hZECMqKiO9ffTpb0GPD7wwh9CFdRdRE7OXfDv2xWniD4xeiqdv6z01mrJZdXBcGu2Gchc42d3CWWi3g02V5d1ds5d0Qrbtjg_K-GCxIfD2sSWpd_huo0veTXi2lHAJBIR7wXwwp18so9ppL4BhEmE1AMQfeYxG0iGDY3vGSarPZ9xRSFHciDidaRG1ike8durxjso2PK7gGKc-WO4BfqFxsvreVnuEIJg9GtotbYXmnV46RwfYOEEK-CVOFinCNaMW4yinMGVM8usfO_z8CRFVfy1dGFKgMgaebCKoi18rFOxc1WD5Y13xBCbR70bf49xyq-1gNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=MI-dX3SpRnl287hZECMqKiO9ffTpb0GPD7wwh9CFdRdRE7OXfDv2xWniD4xeiqdv6z01mrJZdXBcGu2Gchc42d3CWWi3g02V5d1ds5d0Qrbtjg_K-GCxIfD2sSWpd_huo0veTXi2lHAJBIR7wXwwp18so9ppL4BhEmE1AMQfeYxG0iGDY3vGSarPZ9xRSFHciDidaRG1ike8durxjso2PK7gGKc-WO4BfqFxsvreVnuEIJg9GtotbYXmnV46RwfYOEEK-CVOFinCNaMW4yinMGVM8usfO_z8CRFVfy1dGFKgMgaebCKoi18rFOxc1WD5Y13xBCbR70bf49xyq-1gNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز دوم تهاجم مسلمانان به اسپانیا آغاز شد.
🔴
خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138841" target="_blank">📅 12:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr0zqmSQMeMMgAa5cYG7YQ4WFgfHhK-kQi7uZpdMQhq9-sTLjob55ylFMFdnSvYMq1-StB6ta_ewAm_EfN8mY68fe-fGT3WqZuAy5pQEW6x3hHmrm6AGJjMWe8ySEX1_4M30V2vIspU83xaccsFc6dc0wyi3pDRaM3sXPlHdb617pJjO--sCY3_JIThBfAaw1Hb8UXSlkRLR_rNgSspp4eMIvXNgXfVFoQmgUpMNlMkEEhxxKYdiUnBPhtnXoNX2giwt4mG6BKuhPVaqe2WQ_vL6To1IfSDC-DHC0DBdKS_t0PyuFJnLGY8K0wBoPI3T5b2LfG4uNNQYomn9hnLhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بلومبرگ: جالب است که سنتکام هیچ حمله شبانه‌ای علیه ایران انجام نداد. خیلی زود است که بگوییم آیا ایالات متحده به الگوی اعمال محاصره برمی‌گردد یا خیر. و اینکه آیا این نشانه‌ای از ادامه مذاکرات دیپلماتیک است (یا خیر)
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/138840" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DITrDiAFZB0xu86-3fMQGmCKO09pt-byGvoG37rRuDcX-lyi27429ZU3UGpGcfSndkgZk6cJj6wXhQVR9rDoZxDxRN-o_odI6csbHuA6G2zXCLIVbRH76cztQbx0FLmi56vWzDSm7Ku1kz5ZalHjqbMNwg8MMZGgaDPRrYXgmoHM4Vzy-rkthHDC4mLsrBxk5fR-wpOEJlCF3g6dSMgdE6cVjkVpNM-5asCkxGVIemtb8UEQIhtsb7mBlGobpcUIFBQOhJXU3VXj-BBFSE1LkQv2lJWjj_5ij_J8b6Ec2-LUQrCY48_-XQDnMI-wgG1LZki_hmiCHVug6uwAAF4JkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138839" target="_blank">📅 12:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حادثه امنیتی در اسرائیل /منابع عربی: یک سرباز، سلاح یک نظامی را ربوده و به سمت سربازان ارتش اسرائیل شلیک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138838" target="_blank">📅 12:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بلومبرگ گزارش داده شش نفتکش سعودی پس از تهدید حوثی‌ها علیه کشتی‌های عازم بنادر دریای سرخ، مسیر خود را از تنگه باب‌المندب تغییر داده‌اند.
🔴
دو نفتکش بسیار بزرگ به‌سوی جبل‌الطارق و چهار نفتکش دیگر به‌سمت بنادر آفریقای جنوبی می‌روند؛ مسیری طولانی‌تر و پرهزینه‌تر که نشان می‌دهد ناامنی دریای سرخ حالا مستقیماً مسیر صادرات نفت عربستان را به هم زده است
🔴
یک تهدید، هزاران کیلومتر مسیر اضافه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138837" target="_blank">📅 12:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
بر اساس گزارش‌ها، نیروهای سعودی مشاهده شده‌اند که از مناطق شرقی یمن عقب‌نشینی می‌کنند، که احتمالاً در حال آماده‌سازی برای یک عملیات نظامی زمینی علیه حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138836" target="_blank">📅 12:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a16a391bce.mp4?token=Z39M8sB-YXUK3taFYV8v4VGhd9TYGGJgUIe4LXheyV_SyZn4WRQ75t1tXKzLYLEjjf1MJff5JTzCcDDnW4jLegftuYlh40Yt7OWevqV3zZbA0fzpQLv-PDqMxEisPrcrsBByBENep16rnR81RjslHvzAvjUTmcllUxh9rwhotz_azenabhW2dp4MwUUAhdJlsYYEHPRPL_pCzFf8L-u0Mjer9Y71VAc9j0S6siMOAUnvuRfJop0BbCaMPwHNLcMkWragc_D7qe7F5Q2UVOiqEBD3ypB4TiRKkA78tlw7-gWM34NgOFQH8IccYePE30UJUICMiR6GtlBmVnzWTltiHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a16a391bce.mp4?token=Z39M8sB-YXUK3taFYV8v4VGhd9TYGGJgUIe4LXheyV_SyZn4WRQ75t1tXKzLYLEjjf1MJff5JTzCcDDnW4jLegftuYlh40Yt7OWevqV3zZbA0fzpQLv-PDqMxEisPrcrsBByBENep16rnR81RjslHvzAvjUTmcllUxh9rwhotz_azenabhW2dp4MwUUAhdJlsYYEHPRPL_pCzFf8L-u0Mjer9Y71VAc9j0S6siMOAUnvuRfJop0BbCaMPwHNLcMkWragc_D7qe7F5Q2UVOiqEBD3ypB4TiRKkA78tlw7-gWM34NgOFQH8IccYePE30UJUICMiR6GtlBmVnzWTltiHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک عبور مهاجران از مرز و ورود آنها به شهر سئوتای اسپانیا را به آخرالزمان زامبی‌ها تشبیه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138835" target="_blank">📅 12:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/094c83504a.mp4?token=oFGnn4sn4odpbl1ZqheMJbzR_otHHmsuNOUqR-OMLcJEhbpbylGsmn-TLahOZyqmC8nvTcBjLYOHLhYpVwkBJ6p3HB0iDp1M72obfW1WfjTUOfadzo0wINS6CYEyZrZnj9nlCxAgp0h5Nhra0UHbnCEkHFk_M2fE4W-mCGy5tmHGKV91xSHa_HUijIbMmIfU-J9usj-jYvIkVcvluIBe5eBNPJ3y342F80s4lAO0TghiuM4V7N54ZLbpITkoarOxkv-WOGZEumH8V-jyjHq1glnXyANqzWoulz-rZ-_IIqVb-0qqgKRrtvHyI_VUAYck7W5PchacSXQc_oi4pJczeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/094c83504a.mp4?token=oFGnn4sn4odpbl1ZqheMJbzR_otHHmsuNOUqR-OMLcJEhbpbylGsmn-TLahOZyqmC8nvTcBjLYOHLhYpVwkBJ6p3HB0iDp1M72obfW1WfjTUOfadzo0wINS6CYEyZrZnj9nlCxAgp0h5Nhra0UHbnCEkHFk_M2fE4W-mCGy5tmHGKV91xSHa_HUijIbMmIfU-J9usj-jYvIkVcvluIBe5eBNPJ3y342F80s4lAO0TghiuM4V7N54ZLbpITkoarOxkv-WOGZEumH8V-jyjHq1glnXyANqzWoulz-rZ-_IIqVb-0qqgKRrtvHyI_VUAYck7W5PchacSXQc_oi4pJczeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال : می‌دونید تا الان چند نفر از روس‌ها تو این جنگ کُشته شدن؟ آماری ازش دارید؟
🔴
زلنسکی : طبق برآورد ما، مجموع تلفات نیروهای روسیه به حدود ۱ میلیون و ۶۰۰ هزار نفر رسیده
🔴
از این تعداد، حدود ۷۰۰ هزار نفر کُشته شده‌، البته این فقط یک برآورد تقریبیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138834" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت خارجه چین کشته شدن یک شهروند چینی در کویت را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138833" target="_blank">📅 12:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بی‌بی‌سی: در ۲۴ ساعت گذشته ۴۹ هزار نفر از مهاجرین مراکشی از طریق دریا وارد شهر سئوتا اسپانیا شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138832" target="_blank">📅 12:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXfsSMXXf65jNCBmmbjGVu27Z0wJ5qIajnLqEAYbv0dEKuF1WSdgHWTYnO6mnnBrHyBxLOlwxBR9P_89rIwu09nkQCdHBDGz1EFfdoOEkY08yzMKY7kr2QKKsXIo6o7mZSjtVu5OVG3Se5vDkmyDuFLt2MdOlkEFP-ZGGdnu4WZqaP2IvSE1ON_xxqdffWs2T3eTe5ohbGvzcWAZteQ0srlV_wp3NkRAd9h9E70NYC-DII14w5_5V1RSXJ8vgkd1uHiBaCGZoWPPS73YlVd1yX6SxgQtEt-sfkbguVI-dmNAFZcJLyhN6xjz5g8CMiEOg7yIRr4NmOCLVYhJv_tLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووری/زیرنویس شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/138831" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=mr4YvSiZGWsSSZATUQdxFM934U6aEdGFnu6wzmi4DxsMsZ4hPxG4BKZsxZl6x4llYempT0H9ZL_Y6R085mGkTljmJRZoff9kheKDZuVqkz2SWwTbOwqFUNzcVUYOq5pdfs53fVrWYSBGs3FnkHITlBWl7aa7A_7GUBdXSqSYjCAIAG3SmDPkMF0AfDtFHisg75L0kxL-Y942CrgQjSriXJInEl4ESXKBdM0HwDcmBX4RJjEpxuDT2xnw4OWunbcZ749amjbUSQyx3jgS7SeAphki9Cr0m8Fij5doXAvfadDzzqISWGZCQYaFFKm_nIXvpW0uKgzN9cSQ4RPIIanfNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=mr4YvSiZGWsSSZATUQdxFM934U6aEdGFnu6wzmi4DxsMsZ4hPxG4BKZsxZl6x4llYempT0H9ZL_Y6R085mGkTljmJRZoff9kheKDZuVqkz2SWwTbOwqFUNzcVUYOq5pdfs53fVrWYSBGs3FnkHITlBWl7aa7A_7GUBdXSqSYjCAIAG3SmDPkMF0AfDtFHisg75L0kxL-Y942CrgQjSriXJInEl4ESXKBdM0HwDcmBX4RJjEpxuDT2xnw4OWunbcZ749amjbUSQyx3jgS7SeAphki9Cr0m8Fij5doXAvfadDzzqISWGZCQYaFFKm_nIXvpW0uKgzN9cSQ4RPIIanfNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی هجوم مهاجران غیرقانونی که حصار مرزی را در ملیلیا  شکسته و وارد خاک اسپانیا می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138830" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138829" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا در حال بازنگری در حضور نظامی خود در کویت است
🔴
ایالات متحده در حال بازنگری در سطح حضور نظامی خود در کویت است. واشنگتن روابط مستحکمی با کویت دارد و این کشور را شریکی مهم در حفظ ثبات منطقه می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138828" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7RrR0HsE5907ijqn2PO2drNxaixV1Qj69uTKleduJT-uQbUBjVPFC6okSmnioGThPi9ddKWmStjrBYFlj6x37hoaoFg4gh8pVJ8FHS09kL1W95fnA4q1fPs5sYBeSakWK3lPVziOwUpNq286PFNOuzf_sWyT7wwJxp2PAYHOcam7wRONNjMjoifnbNTVQRw3832yk0LZkmITCIAPM-DeKY2nRHE018NFV7ZvXDBpTe0HMuZv-4wJGCSveTBG8NsShZaWx6KJz0uRvDyNOCcoid79pXdqnb9WZtkLiWP1uZj55HaEtURDmsySUV7eD-LwOuhn0rJpI00E5-2nAW8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم تشییع جنازه علی خامنه‌ای، رهبر سابق ایران، به این کشور سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکند و وقت‌کشی کند
🔴
یک مقام ارشد آمریکایی ادعا کرد که ایران سعی کرده حماس را متقاعد کند که توافق‌نامه را امضا نکند، اما این گروه ترجیح داده به حرف آنها گوش ندهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138827" target="_blank">📅 11:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یک مسئول حماس به خبرگزاری رویترز گفت: توافق غزه باید به صورت مرحله‌ای اجرا شود، اما اسرائیل باید نیروهای خود را از این منطقه خارج کند.
🔴
پس از توافق طرفین بر سر متن این توافق، اسرائیل باید اجرای مرحله اول را آغاز کند.
🔴
همچنین، گروه‌های مسلح مورد حمایت اسرائیل باید منحل شوند. اگر اسرائیل با این توافق موافقت نکند، ما آن را اجرا نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138826" target="_blank">📅 11:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=Tdw60xS6YFY9ooZxnAwo2hNJqBuRTFhCs3qpm8Bkp7lYZhPhtL8dBvHE4PdfEoB7s_JG8A2i3i4u5a1ZYlOMk63Va5jYejc12KN-0WhGXZMAQ8Acpxk_xLC8f480OmnKNZr3DqnICJWwW2ln7w2FaB5cCD8z3fA-sBOgIPaZJGAtCzakGLQCdHG-DIae12djfgHxljIMimowy7KWnzPJmw6ecu12PiSThvcHG07pzhLN8Lq7AGNaQycaTEMdvYAkptbV--dGeWTw7GHinEwffTZsXO6EG9y1GCXUIJe0l9zyrBhnES6foF-4ix-9PCcMLETcOyfzZu5n7TZ4DRN4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=Tdw60xS6YFY9ooZxnAwo2hNJqBuRTFhCs3qpm8Bkp7lYZhPhtL8dBvHE4PdfEoB7s_JG8A2i3i4u5a1ZYlOMk63Va5jYejc12KN-0WhGXZMAQ8Acpxk_xLC8f480OmnKNZr3DqnICJWwW2ln7w2FaB5cCD8z3fA-sBOgIPaZJGAtCzakGLQCdHG-DIae12djfgHxljIMimowy7KWnzPJmw6ecu12PiSThvcHG07pzhLN8Lq7AGNaQycaTEMdvYAkptbV--dGeWTw7GHinEwffTZsXO6EG9y1GCXUIJe0l9zyrBhnES6foF-4ix-9PCcMLETcOyfzZu5n7TZ4DRN4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد موگویی جای همه رو لو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138825" target="_blank">📅 11:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMds84M3u2oXmXIbMlR9AB_DWRjSH9_UoTxMwRWZU6koYyq2NLLQ3Hy6UdWOu54rhDN3VrCb-PJLdeZ5Xrq1InYhVwMmkMsbj_oSGHOKk6OWF9F57fFBIJTu6vq_ZXOnCCsJfXlQ3jKpiw0NcncX39Ta9Ht9xvP8WSy5MdmXSr5smP9HSh8HsnRbhyj4y9GJtIvyBkyZFtVPTOmqiz90xuFPMH16S2XpdVh9-yfzFNDspmjxHqZV5X0nM4Sks1HL2nfPW_n5mDiONTuNuCqAF4ucILB4dDrSFd-D0pwDpLtQMaEXpjiVJOolmJgVIbXbCUrHw19dPCIv7dYRwShWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: فک نکنم‌ جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138824" target="_blank">📅 11:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ارتش روسیه به وسیله کوادکوپترهای انتحاری، تعدادی از پمپ بنزین های اوکراین را منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138823" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLQVHpaP5Sjc1nJsi7mpqy4UHqKXmmiJUEumCQQB7nlASWeqI8RgY0tF1-WksViIfSoHzFgauFOLyLHSH--AAonsDJGsinyfCWL5FcAzdTMQNUr0Cv9bjqUQdmZ4YiwK48zqFiLtS3yHYV-671-NykD7OqnKeXAM5quKjCyMMODSTZw51koM3B73fERBOTo2aW8kNCjciQWsEKHInQvwQjjQn659yTDrMgq8jRy4gEnPR-HsaSOdNSEEdQCCmUR_aLvHB7Eb3_4mgsr67t2qkfVHC79cqLDstl9QGhtYZJTZpvi7GIWXBU44IzX5j3JG8b0Yox7cdPqqM2WcEvsUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر دهه هشتادی رئیس بانک سپه، معاون بانک دی شد
🔴
پ.ن: لابد اینم امام زمان انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138822" target="_blank">📅 11:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
روزنامه «الاخبار» نوشته اردوغان در گفتگو با عون، رئیس‌جمهور لبنان، به او توصیه کرده در توافق با اسرائیل شتاب نکند زیرا اسرائیل هدفش صلح با هیچ‌کسی نیست.
🔴
اردوغان به عون توصیه کرده که سعی کند با سفر به دمشق و دیدار با الجولانی،  روابط خود با سوریه را تقویت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138821" target="_blank">📅 11:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138820" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=Kdwt_Iwg_x44WklNMcPK6Srz9U-A3b41lhFdmyxaH2ECw23508o5OS-8vqCTUKCOi7Zk4XitD3HvHzWrlsXqrkKECyFJFh_lNnbY3AxaF-85udFbkrPAXxONfJn-kZnBXOEqy0P5XLTsDQntG-rBqtO9S65Dg72PwNbc9QE9vRnqlvCWqgk1xQSDc7Mnem7UOixEYqGvQHkRO5oGNfB4jB7ff2A0aNqJ3x4NV7MfkwGNaVMv3DCkOoGy7T2uM8P2ipmf-AWm2UW6XmWnQGpiXQtPK33ldtm4tbnn62io9e-2X4UgcoRXgv_7Spn9F_31oiJxfY_inZiA9qWoETaGaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=Kdwt_Iwg_x44WklNMcPK6Srz9U-A3b41lhFdmyxaH2ECw23508o5OS-8vqCTUKCOi7Zk4XitD3HvHzWrlsXqrkKECyFJFh_lNnbY3AxaF-85udFbkrPAXxONfJn-kZnBXOEqy0P5XLTsDQntG-rBqtO9S65Dg72PwNbc9QE9vRnqlvCWqgk1xQSDc7Mnem7UOixEYqGvQHkRO5oGNfB4jB7ff2A0aNqJ3x4NV7MfkwGNaVMv3DCkOoGy7T2uM8P2ipmf-AWm2UW6XmWnQGpiXQtPK33ldtm4tbnn62io9e-2X4UgcoRXgv_7Spn9F_31oiJxfY_inZiA9qWoETaGaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138819" target="_blank">📅 10:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الجزیره: قیمت نفت کاهش یافت، اما در مسیر ثبت رشد ماهانه ۲۰ درصدی قرار دارد
🔴
قیمت نفت روز جمعه کاهش یافت، اما همچنان در مسیر ثبت رشد ماهانه نزدیک به ۲۰ درصد قرار دارد. نفت برنت با کاهش ۱٫۰۳ دلار (۱٫۲ درصد) به ۸۸ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138817" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF0ZuIK3xu02DRmpKCd_a5nX772ZhQJCocC2nWCudDW8xjxYVLvuPF7XcnfPqYFDkF1j2AGuvYxPZ1DWIV2nY6nNiRMk7ne661ScYrO5ThaUWdp4gZiNTYVhTt00wc5CGZ1oPTKLUiFWrUt_4BJBRarP7CQywGPjLFdwmAjFGAnTxOTNShxeP_OnmOmQa2qis7kPyE-0R8WAlD3CsS2MEtofShPA5vlvfQ_06xgLPiCS6p0qOLTcl6nxxGCFmVrjpy4CFI0qYtEXwrT-aJKvaGGPvmPvk5Kqd0M7CQOIAINduxQJBDI9g49ijZubWW52annfDmjgGTiobK6qiwowEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138816" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
