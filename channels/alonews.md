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
<img src="https://cdn4.telesco.pe/file/AaR_R3pyhxNfD3ghknxpT2U8LFFWby_SQ1f2GX3_xxWjldS57E8pUpaGSzg8aGnihA1B1PWm890nvrThqB2ZFZnCpib3KJuqRuYqWsiFU4D-fCCl2qUdp2f-dEBMBUBsaoCWxoEP_R38Cq6YI4rN-ewFx0g01ShEgOCMSiZ2x8PG8EUIhngLt0bsyugPkaSJx6LtYEE-RdPtowJDKZrdWsbf_JeGsdzGbBEUQB2_2QuMCiY4Xc4duyQgbRZfBqvlj3HtUA1wAJKpPZD9cfhBIbUY3Gh8HxfAn_P-VmyIPHjZ5fp-H4wId6AFlydG_yfwmxJnJLbdza2m971LSESZCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 921K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 21:27:45</div>
<hr>

<div class="tg-post" id="msg-123350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شبکه ان‌بی‌سی ادعا کرد: مذاکره‌کنندگان آمریکایی و ایرانی سه روز پیش در دوحه بر سر شرایط توافق آتش‌بس به توافق رسیدند، اما هر دو طرف در اعلام نهایی آن تأخیر می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/alonews/123350" target="_blank">📅 21:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8l2KI_Grdolb0xPw9faBohPIUjLcTEyTn9PZqtCP687AE9r0FlcgZg0f_cS8Wh9TrcaH5wMbmFXuGTwemhK2hoDS9KPYOZ7a5D3QXudWrFlRFWhI3vxJziXiShaPtftbNKGEAWa-PBkVYdrJgpFd5CzV39lmK6YKugjiZmj7qUe-jshkYIMi5293M2w0zRAhXO9ReXcAMnTV7oGco8qyNvQFoQsc7lEi5korGkwi1u5sUUGD7VOfXzqY7bGyCHgTL1baswljJTGAqOWC3OqjnXc0SlxHKYBoYmNLVVZKYWlsnl79tsF8pZC-WGbZC-_RS0Xc18Zh06nLw_DqX6EOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه CNN به نقل از تصاویر ماهواره‌ای: ایران با استفاده از بلدوزر و کامیون، در حال بازگشایی تأسیسات زیرزمینی موشکی و بیرون کشیدن زرادخانه عظیم خود است که ادعاهای ترامپ مبنی بر نابودی آن را زیر سؤال می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/123349" target="_blank">📅 21:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/سی‌ان‌ان: منابع آمریکایی هشدار می‌دهند که هرگونه پیشرفت در مذاکرات با ایران می‌تواند به سرعت لغو شود اگر ترامپ تصمیم بگیرد تأیید خود را بر یادداشت تفاهم پیشنهادی صادر نکند.
🔴
ترامپ به دنبال تضمین‌هایی است که هر توافقی قوی‌تر از توافق هسته‌ای دوران اوباما در سال ۲۰۱۵ که او از آن خارج شد به نظر برسد، در حالی که همچنین تحت فشار متحدان جمهوری‌خواه و نتانیاهو، برای عدم کاهش فشار بر ایران قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/123348" target="_blank">📅 21:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سی‌ان‌ان : ترامپ تو تلاشه قبل از تایید توافق با ایران، مشورت بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123347" target="_blank">📅 21:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123346">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نخبگان عمانی در واکنش به تهدید ترامپ: عمان باج نخواهد داد، این تهدیدات نشانه قلدرمآبی و شکست ترامپ در منطقه است و ما در موضع ثابت خود در قبال جنگ علیه ایران باقی می‌مانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123346" target="_blank">📅 20:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
مدیرعامل شرکت ارتباطات زیرساخت:
بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها، چند روزی زمان می‌برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/123345" target="_blank">📅 20:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123344">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پزشکیان، رئیس‌جمهور: به دنبال سلاح هسته‌ای نیستیم و با ذلت دیپلماسی نمی‌کنیم؛ ناآرامی منطقه به خاطر اسرائیل است و حضور ۸۰ روزه مردم در صحنه، دنیا را متعجب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123344" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fMeB1eX1lx4grzaIglNUzPvkruCVRq4kok-tgpFr3NSAhBAtUynDpoYOyipUp-PrNWVgE-GkSTJq4GTjafrNliwze-cmjljKJ7f_yFzXfIg8BNKMNRF7mVUaciHhIo-LtdoRJTIhPJ6BEFRNbvV1rh5RrzZMvWt_NIFR-izTF0yQdntbKs5QQJMEX0u1hcSXPKwuihyJaYIHq_jVekA853LYTfG3TjBv2iC8fiWcXkDeTMggu3hHIHRemPqiBO8djaJMH9n6vpnXnaYQrfwmSrwNwRqOweOsIwg3t_QRCg_UZkgSe8N9-5M39K0jwOc3-jXNCBr4GdjiamXV1PoAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشور های دارای سریع ترین اینترنت موبایل در جهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123343" target="_blank">📅 20:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123342">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
معاون وزیر خارجه: به هرگونه نقض آتش‌بس، پاسخ قاطعانه می‌دهیم، تا زمانی که تفاهمی در راستای منافع ملی نباشد، ایران آن را امضا نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123342" target="_blank">📅 20:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123341">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmwi2AFAJhfEkQkhgplwrr0DgdAAWt6ezQNCfEvuLs7o4v-8FiYQAxORH9Lv3lxDi6nlGxDPl9uNrl225Xxmns2rKtk65v5TtlpOtApXGjSfdHHu3YVnTPYBVnQd8uqvfXtLUwaQgOoiRJMWe3LrJ_urmDhq2hEC1dhMYcNwxU008GllCCG6UiTof8EWNGOISDLqfnKJO-bf3Mp1hGl4DXNKZGO9YWHSGPw2XLXCNh7w0r4ryM6kLjGIlfdguCuZeMC9biVumV74q7nuJgsAcxpW44xY3BXc24hoB6GJLwjSMCTGc88D9JjscUO-yIzVuXzU8BHfuECFcJzeJy1nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای العربیه به نقل از یک منبع دیپلماتیک : توافق بین واشنگتن و تهران در دو مرحله خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123341" target="_blank">📅 20:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123340">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کاخ سفید اعلام کرد تفاهم‌نامه‌ای وجود دارد که ترامپ هنوز آن را امضا نکرده است.
🔴
به نقل از الجزیره، ادعا شده این یک آتش‌بس ۶۰ روزه است، تنگه هرمز بازگشایی خواهد شد، ایران قول می‌دهد ظرف ۳۰ روز تمام مین‌ها را پاکسازی کند و متعهد می‌شود که سلاح هسته‌ای نسازد.
🔴
ایالات متحده در مورد کاهش تحریم‌ها و آزاد شدن دارایی‌های ایران بحث خواهد کرد.
🔴
به طور موازی، محاصره دریایی ایالات متحده لغو خواهد شد و سپس آنها در مورد اورانیوم غنی‌شده مذاکره خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123340" target="_blank">📅 20:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123339">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : آمریکا از اسرائیل خواسته درباره هر نوع عملیات ترور در لبنان، از جمله جنوب لبنان، مرتب گزارش و به‌روزرسانی بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/123339" target="_blank">📅 20:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123338">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVdxxt4Mgm4xuS_Lr32Lr82lmdBPiGz86We-V-mNV6Xb8a4U1LA6lXmWuIaQSx-X_6pQr8dkAJt0_0hMpgmB78tgC4MUREzkfVREjpvXAfxFho2OswuRdYBxMdKdyTVtZaCWBiyP_fPry7h1Vrjhz7S5QsW9stwg0llsyy2Z7Y0q8ZeymrXNFC4CrOwc6H3bswL2ZprFQpa15kvf-z1X9SAhKXZtgGNL3sbzRDxPqPoyOSUiz2WdMnpx5TqjRbZmwSaMzItiZ4ZR_uchflilswxj8EwfFFd13ycs-gGK9OHmVCaXp_IE_fivQopMt0I8KgwozGe1e-IooXiv8O_4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه‌بندی تیم‌های جام‌جهانی در رنکینگ فیفا
@AloSport</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/123338" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123337">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/123337" target="_blank">📅 20:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123336">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/123336" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123335">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDebvyT-Gw6NEhxN4vF9AQ3J_os69P21cG2FxHwWtZu3JpUMHHeLtmBScPwVjou6G-FMu7o-31KDrkUKhPKKaecNZuTrpAqfHlHAyDVkzygTp0mHCvs-sasW-3UyMBZSfR1037Ha3CTaOmLGfHbB3qiy0wmWkZ9rBr04XLV2DZI_P5VjgMt9TAyNLIQ8F23QNHjLTre6a8FMofrWUbQ7VI37tAjkclblnuzj5ThOGvrdtJDZGOKuKL9u8e7aRo9yw_Q9BjHQZITZg-y5zvi4q1DWLwtFvWaILJ-myjPr7-W4KAXMgihU88qSzNHo2p_ImFkgwKUtzCosFSXIPVgwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/123335" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123334">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه:
هیچ چیز حملاتی را که امروز در جنوب لبنان انجام می‌شود توجیه نمی‌کند.
🔴
ما بار دیگر خواستار پایان این حملات، بازگشت به صلح و گفتگو، و ایجاد یک راه حل پایدار هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/123334" target="_blank">📅 20:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbe8jVzgt-NiekUpItVCCuY16d5IvKhQEjUBDeu2BP4KsSDatNvfJw1CV03kgfCdHY-Ckq71QiQg5I7HGY-dp77WtOlsly2LEVframltidSkXdYthQEvE0ABAtut0zgGfzWwAOW1vTbJvfDi0SM5Zx8YVdlnfFpZLqw8d42xahjTwHQXZSvtV8nTILozyxRQyhxFsftdrmzBbiBhkDcK7tZgE4IHRbk1PQNpA0uw7-7-0OwwyiRaUOPpgZUJzU3VtoZmahcZv0yhorCTXFtWXQmS6UUMpmZ3tEMNVFhbCrTNvXOqqdCU1z5mcS9OY7G-qhzz6_BHSnkWp8UfEcp7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتحادیه اروپا: اگر اوضاع تنگه هرمز بهبود نیابد، بازار سوخت جت با مشکل مواجه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123333" target="_blank">📅 20:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxhZzuyhv15qhK8-zIYd_Cw9BlAzAx_n49O7qx0OGKu3QR4Dh03soYKmRaVICK6ZEV6kYsajQ5OqIXIsY9_joevOWwTkRJ8owbTcjoIxOD9ayYt3Rx26s7q5ZWGr1I_piXitfNABNV11S5s7GZv7eL2dKTDd9_fjoDjnktCwhQUyqkg8o_HDCIE-FFGpT3hSTXcl4DpedMpeUop3smN96GfE4NGURzZ6Lbq5wa4zdNmwWRAoFvQWQmrEtp0xWu7q0VUsdqlvWt4Dg8NwKSSOv9cD0T8f0dB6-IarqlZ7Oyy-O7Ci97wbx1evj78sKMimUMmsLaBZrJ-XfmykZzD81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکبری، معاون وزیر ارتباطات: بهبود کیفیت اینترنت چند روزی زمان میبره پس صبور باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123332" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/su85yh-pjDSbZ8ZPxTdms0SrWLbpp7Que_Rl-g1YgLqXwMDp08Bu5AJyTSzA-RhDAvEXR68UeA94QRnqXcuu6_hECnoBbuZLPQys7alQHvn2L13BvdB9tNcKvbwcFDsf1s0eBPhM8bek_YA41tT_TDHIuS5omrBlpU3QQE802jFtOwSJUNpP2JZtG9-eehIQGPvobYEPzAhPRuT_RKarRpc-CGfUD9SlF196-WdDAJ_e12urTlbNewxyZUP7HfDLDcdR0O_TfOHZa6SN17ZzJk4EdQEjjmTW39bhPJMfrhvcoU8LB_cyq0V1eMzytUzpCmifvgxb-JAa5VBT6CJgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا خطاب به عمان: می‌دانیم با ایران دارید چیکار می‌کنید، مجازات خواهید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123331" target="_blank">📅 19:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123330">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل به نقل از یک منبع نظامی عالی رتبه: بعید نمی‌دانیم که لبنان بخشی از توافق آینده آمریکا با ایران باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123330" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123329">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ادعای یک منبع دیپلماتیک به «الحدث»:
پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123329" target="_blank">📅 19:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123328">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس: مذاکرات با پیشرفت قابل‌توجهی همراه بوده، بخش عمده پیشنهادات ایران پذیرفته شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123328" target="_blank">📅 19:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123327">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
عزیزی، رئیس کمیسیون امنیت ملی مجلس: ایران پیشنهاد‌های خودش را در قالب متن ۱۴ بندی ارسال کرده
🔴
تنها مشکل سردرگمی آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123327" target="_blank">📅 19:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123326">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
دن کین، رئیس ستاد مشترک آمرکا وارد کاخ سفید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123326" target="_blank">📅 19:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123325">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd4b148b0.mp4?token=TNlBLvZglFnrUuc4CEDvWk5Qzx1a2tpd5InZX3b67WUH4R1z2eLi2Ralv8LP3AOwLd6hwpGHGumHXjpoZ0jjcoCmRxU2QQJF6CrnxyppU3FVpP0eQQ-FHxqjL0pyoK4KtuWbY9kYeuiP8PtZA6miN19v7N72RMffklGTxKZYcaCoT6kOXxnaw6RA2LhYtfgpV3DqS5__aYvotSpQjpyjY4zhZODXu4kHbvIimOFXI-4Ubc3PWTrP76vzC4iWhFPMafrDNIEj-Ia0TqRjFdFPFH2ohGkfeA8XuvOnbiKX6uyMPOxG_P3JSX2SFH0z3K_t42dbx5g8cFc2-uq9ePpJxU2TIl78hHmZGRrS1E-5nVXUtVNKtBV3OLXtozYrYxf-WhD2M16SjvEwhPSuBZPrmZt89xRcTNsJ4ZrLfZLo2jAXT0km1zZSuNmQ0Oa-oDEfmw7tZTbKtNYzN42Jp53M-HdS1OATSvehwrXEVgicOW77kJpjmSMfihu9jsMVlIUHYBf4d49IENaUTnZPoJdtpz9tCtNHBKOznbvevzMmZlN6QaZuUiCtWEnXGDL4343e_izPEUgqjxLzt9EeI4FxJOYOobZoY5ClngDvHHPlpo_V6DvfBO1ZOepmX6S3ykayYKm9q8Ms_rZ3LS-0EOEiXvr6B5ErSlMCZB6DKYVpdrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd4b148b0.mp4?token=TNlBLvZglFnrUuc4CEDvWk5Qzx1a2tpd5InZX3b67WUH4R1z2eLi2Ralv8LP3AOwLd6hwpGHGumHXjpoZ0jjcoCmRxU2QQJF6CrnxyppU3FVpP0eQQ-FHxqjL0pyoK4KtuWbY9kYeuiP8PtZA6miN19v7N72RMffklGTxKZYcaCoT6kOXxnaw6RA2LhYtfgpV3DqS5__aYvotSpQjpyjY4zhZODXu4kHbvIimOFXI-4Ubc3PWTrP76vzC4iWhFPMafrDNIEj-Ia0TqRjFdFPFH2ohGkfeA8XuvOnbiKX6uyMPOxG_P3JSX2SFH0z3K_t42dbx5g8cFc2-uq9ePpJxU2TIl78hHmZGRrS1E-5nVXUtVNKtBV3OLXtozYrYxf-WhD2M16SjvEwhPSuBZPrmZt89xRcTNsJ4ZrLfZLo2jAXT0km1zZSuNmQ0Oa-oDEfmw7tZTbKtNYzN42Jp53M-HdS1OATSvehwrXEVgicOW77kJpjmSMfihu9jsMVlIUHYBf4d49IENaUTnZPoJdtpz9tCtNHBKOznbvevzMmZlN6QaZuUiCtWEnXGDL4343e_izPEUgqjxLzt9EeI4FxJOYOobZoY5ClngDvHHPlpo_V6DvfBO1ZOepmX6S3ykayYKm9q8Ms_rZ3LS-0EOEiXvr6B5ErSlMCZB6DKYVpdrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: اسرائیل دیگر صرفاً یک قدرت منطقه‌ای نیست — بلکه اکنون یک قدرت جهانی است.
🔴
و چرا یک قدرت جهانی؟ چون ما فناوری‌های سطح جهانی داریم.
🔴
امروز، آنها این را می‌بینند — در خلیج فارس و جاهای دیگر.
🔴
ما اکنون در موقعیتی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123325" target="_blank">📅 19:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123324">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1ee2f450.mp4?token=SjKc9gHUmPLEVvZjgsTvbr5UBxX58Qg4qLfmJE-BxWi6PitZWeGe5By5sTBRgbCq7YDlPxBMsKhqxElfz7TF033JddXw65d39NBRsMQ0DVFT7p7BtLdNsgFnrMXFbKCWzhktMlY5LXYW3Wkl-Vn6Ku9mY8DscS4Xmd8Of6_X8hxp0SAdZXWOx8bDPi7zVnr7smkiT58XdFuXjcXWYmgv6jnev-tLU1tShs5VdW-phrbfyLjiGsCoO_Wc_irDrt21lJpIjb69tdG9Bc9GNREy_RxBtaZvZ2hY7WgbQJB1I7dcXeZ_o1q4H_G_CZPy7iZ4K2gFMblcSGQpLqyHsCM1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1ee2f450.mp4?token=SjKc9gHUmPLEVvZjgsTvbr5UBxX58Qg4qLfmJE-BxWi6PitZWeGe5By5sTBRgbCq7YDlPxBMsKhqxElfz7TF033JddXw65d39NBRsMQ0DVFT7p7BtLdNsgFnrMXFbKCWzhktMlY5LXYW3Wkl-Vn6Ku9mY8DscS4Xmd8Of6_X8hxp0SAdZXWOx8bDPi7zVnr7smkiT58XdFuXjcXWYmgv6jnev-tLU1tShs5VdW-phrbfyLjiGsCoO_Wc_irDrt21lJpIjb69tdG9Bc9GNREy_RxBtaZvZ2hY7WgbQJB1I7dcXeZ_o1q4H_G_CZPy7iZ4K2gFMblcSGQpLqyHsCM1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
در نتیجه بحران نفت، جهان منابع انرژی خود را متنوع کرد. آنها نفت را در مکان‌های جدید پیدا کردند و مسیرهای تأمین جدیدی ایجاد کردند.
همین اتفاق اینجا هم خواهد افتاد. من همین حالا به شما می‌گویم: آنها شروع به جستجوی خطوط لوله انرژی خواهند کرد که به جای عبور از خلیج، به سمت غرب حرکت می‌کنند.
و ما فرصتی داریم که در آن مسیر به سمت مدیترانه باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123324" target="_blank">📅 19:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123323">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c381825c.mp4?token=URsGtHvbQBN4IZRBa4Aq9HMwWpEXvbAx-eZb0kXtpReLy2zf6A9D8BVIWG1KG3i54gcOdt_83SbhyUScAVZUPgnnijB8StsBqNiFVjppY5YbffWxkicuI8j5q9l1FTI06YKgaUbNzEomU8eF_ZifTu4rqBMEwbKZ9yWNI6xUH_FJABUtjjiDjJbhuTQByYsvutkT1ho1oQxR9FKJ6wYEYB40TFz_v-Hojl_zB2LljinKhZeRi7rI82LeGOCIH1CyHKMzYMFbO3mwVYH6mIgOAsrFO0lM9cIns8S_QwxGcqYdeF5FqTob6C3qlIzVpAdK3b3Begj5BnIJe6BRGmI3JYrYBpOOaGXibHzsGADD2_chg9adxfckqeQCCgtvSbY7mUtVZwUhAFYoOUftLG7HUSDBOtTwDbhB2-sgmZQ2sA4yw5pKu5ftUXXUPaEQ0nn69ZXSAfe6bamRWLoC83N1A5DlMz5i2m2RWjXDFSx0sgSespPIVcJx-KqSuGWV1ao598NMbT-xPBQbipsYmbKvKYaKz3ew7fHccxvcY38stGwZlrZ0Q0-qBOhcnB5sM_2bFcYhS6OrF5tJlpYgKOliYrpbuiyLh642dncfq6TmKKC0gGikNwRz_G3Ewb1MaHht4fHyfXk-9hs34QLlCWE-fKBSXtZq3bbUa2IHYocYclM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c381825c.mp4?token=URsGtHvbQBN4IZRBa4Aq9HMwWpEXvbAx-eZb0kXtpReLy2zf6A9D8BVIWG1KG3i54gcOdt_83SbhyUScAVZUPgnnijB8StsBqNiFVjppY5YbffWxkicuI8j5q9l1FTI06YKgaUbNzEomU8eF_ZifTu4rqBMEwbKZ9yWNI6xUH_FJABUtjjiDjJbhuTQByYsvutkT1ho1oQxR9FKJ6wYEYB40TFz_v-Hojl_zB2LljinKhZeRi7rI82LeGOCIH1CyHKMzYMFbO3mwVYH6mIgOAsrFO0lM9cIns8S_QwxGcqYdeF5FqTob6C3qlIzVpAdK3b3Begj5BnIJe6BRGmI3JYrYBpOOaGXibHzsGADD2_chg9adxfckqeQCCgtvSbY7mUtVZwUhAFYoOUftLG7HUSDBOtTwDbhB2-sgmZQ2sA4yw5pKu5ftUXXUPaEQ0nn69ZXSAfe6bamRWLoC83N1A5DlMz5i2m2RWjXDFSx0sgSespPIVcJx-KqSuGWV1ao598NMbT-xPBQbipsYmbKvKYaKz3ew7fHccxvcY38stGwZlrZ0Q0-qBOhcnB5sM_2bFcYhS6OrF5tJlpYgKOliYrpbuiyLh642dncfq6TmKKC0gGikNwRz_G3Ewb1MaHht4fHyfXk-9hs34QLlCWE-fKBSXtZq3bbUa2IHYocYclM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو پهپادهای FPV فیبر نوری را «طاعون جهانی» و «تهدید استراتژیک» خواند و گفت اسرائیل اولین کشوری در جهان خواهد بود که راه‌حلی برای آن‌ها توسعه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123323" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123322">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: در هیچ جبهه‌ای عقب‌نشینی نخواهیم کرد و در صورت لزوم آماده‌ایم برای جنگ با ایران بازگردیم
🔴
تصمیم گرفته‌ایم روابط خود را با دفتر دبیرکل سازمان ملل متحد قطع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123322" target="_blank">📅 19:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123321">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: «شاید نوعی توافق بین عراقچی، ویتکوف، قالیباف، کوشنر و دیگران وجود داشته باشد — اما رهبر ایران و رئیس جمهور آمریکا هیچ تأییدی نداده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123321" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123320">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
آمریکا ۲ شرکت هواپیمایی ایران را تحریم کرد
🔴
وزیر خزانه‌داری آمریکا نوشت: دسترسی ۲ شرکت هواپیمایی ایران به نقاط فرود، سوخت‌گیری و فروش بلیت مسدود خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123320" target="_blank">📅 18:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123319">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ادعای شبکه ۱۲ اسرائیل : رهبر ایران با توافق موافقت نکرده، و این یکی از دلایلی هست که باعث شد ترامپ به نفاهم‌نامه «بله» نگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123319" target="_blank">📅 18:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123318">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کالاس ،مسئول سیاست خارجی اتحادیه اروپا: ایران و ایالات متحده در حال حاضر در مرحله‌ای بسیار خطرناک میان جنگ و صلح قرار دارند.
🔴
ادامه این جنگ به نفع هیچ‌کس نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123318" target="_blank">📅 18:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123317">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا: هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نمی‌کنیم و هر بازیگری که مستقیم یا غیرمستقیم در تسهیل آن نقش داشته باشد، هدف قرار خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123317" target="_blank">📅 18:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123316">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الجزیره به نقل ازیک مقام آمریکایی : حوادث اخیر هرمز تهدیدی برای مذاکرات نیست
🔴
حوادث اخیر در تنگه هرمز، مذاکرات با ایران را تهدید نمی‌کند و این گفتگوها با هدف دستیابی به توافق، همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123316" target="_blank">📅 18:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123315">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: محدودیت‌های شدیدی علیه خطوط هوایی ایران از جمله محرومیت از حق نشست و برخاست، خدمات سوخت‌رسانی و سیستم‌های فروش بلیت وضع می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123315" target="_blank">📅 18:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123314">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXZNFJMlSN2dd9BFHMcNkJe_HeBQvxX8RucI9DtteoxMgmONGQuOfeHy8nSz8x0EDpfeWhJE-UjZVLL4J4zMjzP11JdWYRQM0GbI0kDho4r9pAW62SYCSOVno3MwSnCB5OAMMOj9GXtXVmibpLt1zwN12Pca5k4SJJzhwpR4lTh9cUU_NVDJ63e7xbfR2OoZ0GOD1zuwm6iynKZA9SSI2o4PMqmENI31iD7wJZCblHGVPfpQU9e9hPl4VA_U2gNe0NXl5is-UsI0C-b17hMF04Ex7WQ3hhrK9kRe-0rln5Op36xcyJJcEK1seWG4AtZfQh0cmQ5PlVGLXIdpz0BgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس:
اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123314" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123313">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
🔴
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند
🔴
مذاکره‌کنندگان…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123313" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123312">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
🔴
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند
🔴
مذاکره‌کنندگان آمریکایی جزییات توافق نهایی را به ترامپ گزارش دادند، اما او فوراً آن را تأیید نکرد.
🔴
«رئیس‌جمهور به میانجی‌گران اعلام کرد که چند روز برای فکر کردن در این مورد فرصت می‌خواهد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123312" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123311">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10b0b9d0c8.mp4?token=Kdd63oqkz4cS08LppE_g0d6D_ma57eMm6re_AoofqWgCrDldLlErxFuIVYLbyX7Y563clvjNO4TQSXTo04tLk5FxKPeaq5BHgcgqAgNu8LdWicg5hXRUiEkw9oHoUoaK0MjXqABBUzEw2jnFU_U1wUSROaj6wsvPHiDTjqTdq9ig-_1DGQrSU5DStKmyEijZsMPVLu0TciJf7Iv_iuVIFAz97OsiEXlg2R4pUqw3mGOLMitghtDme4dqm8G8oQVhMVdce_Y9n5bKEifro79B8p9sfmiaCUZVOMaasj8inCf-hf2XGpHJxaFaVa7Ns2SravwzBX1O83vDP6fL_b0fEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10b0b9d0c8.mp4?token=Kdd63oqkz4cS08LppE_g0d6D_ma57eMm6re_AoofqWgCrDldLlErxFuIVYLbyX7Y563clvjNO4TQSXTo04tLk5FxKPeaq5BHgcgqAgNu8LdWicg5hXRUiEkw9oHoUoaK0MjXqABBUzEw2jnFU_U1wUSROaj6wsvPHiDTjqTdq9ig-_1DGQrSU5DStKmyEijZsMPVLu0TciJf7Iv_iuVIFAz97OsiEXlg2R4pUqw3mGOLMitghtDme4dqm8G8oQVhMVdce_Y9n5bKEifro79B8p9sfmiaCUZVOMaasj8inCf-hf2XGpHJxaFaVa7Ns2SravwzBX1O83vDP6fL_b0fEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد.
ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در حال حاضر با حماس درگیر هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123311" target="_blank">📅 17:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123310">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgiDqfdNRJduZota8llWLig0v-OmZfHM1ZaBzdPpEm4IJI5RJYkTDHnc7uDEEtvhMZcJsBR5uTkHfWg03h-C7plNdcd0Zh_ZmambP8dqpljbVn9AHWhtEiiBYn8R9rLyJJtxJdCd1isLUGYUGoZbUT6DCdmHy3a720yTaKIzA7OJojG19zC8COEnTw-sMqy2ymUVMmmTQtr_1oOU6AFTDovOr1Y7hES8yn21zqOlHqlLs2nzavEJly23mTBrARMtALZ6h5fPZonU_AP_pf3u9EIst1SEZB5MPrZWyTS0c8_WMI_lvWL0GnDlw7swPigFlXlHGMyLMk8jD5YWpbaBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ماجرای نماز خواندن کریستیانو رونالدو
سعد السبیعی، مدیر پیشین اداره حقوقی باشگاه النصر:
🔴
پیش از آخرین بازی مقابل ضمک، دون (رونالدو) با بازیکنان نماز خواند و سعی کرد در رکوع و سجود از آن‌ها تقلید کند.
@AloSport</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123310" target="_blank">📅 17:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123309">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
روسیه:
ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123309" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac373359e1.mp4?token=ax2kKjLBG8JMFfPdf90jzXUXqLW2yHRciO1uIt8QAoqeMFFt5fgh9ZR-d527RPYTxxAdmorfk8m2eTfqlVL_y40Xly-ef8ZIE7oLRk0jVBFj7VryMbjaXxnyyJwirOaeT8U6dUtpLJ9cYSmsPc18eVB2u6M1FKZWQyLZKYV9amwjxfNWqWJzYQxZNPHRUQ9RgYuoet3zADicOLwR6nUA7-vzE_0DMdL9s9ztQ4P3PKAoLY6UbFTRYUe0rv-lSVmGQtgTDhSJE1ZkFbtP6A17oV1z1om0K4xYS9xVVU-J11sN3RZeYVxC17zVqV8enrX-z_29suXBFI9XUjhEz7KoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac373359e1.mp4?token=ax2kKjLBG8JMFfPdf90jzXUXqLW2yHRciO1uIt8QAoqeMFFt5fgh9ZR-d527RPYTxxAdmorfk8m2eTfqlVL_y40Xly-ef8ZIE7oLRk0jVBFj7VryMbjaXxnyyJwirOaeT8U6dUtpLJ9cYSmsPc18eVB2u6M1FKZWQyLZKYV9amwjxfNWqWJzYQxZNPHRUQ9RgYuoet3zADicOLwR6nUA7-vzE_0DMdL9s9ztQ4P3PKAoLY6UbFTRYUe0rv-lSVmGQtgTDhSJE1ZkFbtP6A17oV1z1om0K4xYS9xVVU-J11sN3RZeYVxC17zVqV8enrX-z_29suXBFI9XUjhEz7KoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت وخیم لبنان بعد بمباران امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123305" target="_blank">📅 17:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123304">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده درباره محاصره:
نیروهای آمریکایی اکنون ۱۱۱ کشتی تجاری را برای اطمینان از رعایت قوانین هدایت کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123304" target="_blank">📅 17:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123303">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fef6c239.mp4?token=l4f8v_UAAV_8ST1jyXwHUjdfNQyeg9qmc6fBcN8VaVixwrK3FLGqp0BthY2oL4KfqtCXehN2y8J8UG0r50CIZ4s0rQqgglsxuP5h4WViLrEusX-rNTybqqrpBat5pfOcAkSY1grXkfKcgsMsKLU4ngjnwwt6969XHM4CQiwS4wHfLYZOl7azNkIH2LPCvL9LqsTw8mfI_KVj06dMfdSpYGQppCj-IfxMu1v239dzGCjbLTnpOnbzqEc1ky9zKrjcTTE3xUoNkw9sdzX0WjMiDFbI40FH2hAIV2MF2PXDTjnGFHFQa8Hs50oqH3ogY3aSYkypWNbBT2i9GYETmJtg5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fef6c239.mp4?token=l4f8v_UAAV_8ST1jyXwHUjdfNQyeg9qmc6fBcN8VaVixwrK3FLGqp0BthY2oL4KfqtCXehN2y8J8UG0r50CIZ4s0rQqgglsxuP5h4WViLrEusX-rNTybqqrpBat5pfOcAkSY1grXkfKcgsMsKLU4ngjnwwt6969XHM4CQiwS4wHfLYZOl7azNkIH2LPCvL9LqsTw8mfI_KVj06dMfdSpYGQppCj-IfxMu1v239dzGCjbLTnpOnbzqEc1ky9zKrjcTTE3xUoNkw9sdzX0WjMiDFbI40FH2hAIV2MF2PXDTjnGFHFQa8Hs50oqH3ogY3aSYkypWNbBT2i9GYETmJtg5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: الان ما تو بیروت حمله کردیم، دیروز در صور هم حمله کردیم
- نیروهای ما از رود لیتانی عبور کردن،ما اونا رو می‌زنیم و خیلی شدیدتر هم خواهیم زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123303" target="_blank">📅 16:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCbHOppYD_sCg2-5ZU9zWzpXjoSREezHaj_T4wsLtOi4SP3tdrXXxHkn2BRNwiWnHSdx28s5AycpkUb1hVfrSIcOrnpgWfv9TYX9BXe8klVXbOHBkFIpe9LOHv5txqSdJi-YACZF9_m9uA-gssbVYFxLFsWmh_DK5fP9HIbHnnWH0ndt38rMdizSWK1fcplKSnysrpzuvnspU7jGoNPLthTW2PN1nyKO7n9H8E-EkNgTAlQl3GGe5tcyVBtP2C-Gya8XT8sTTdTQU7TvvpeqJgD0GXcukzd1HlzLBnTT81T5dwt0LF5gygsM73TZ_6JmRU3UkWAqxoV4SJmvg_wl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ترامپ و وزارت خزانه‌داری ایالات متحده در حال طراحی اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور ترامپ هستند
🔴
اگر این اسکناس منتشر شود، رئیس‌جمهور ترامپ اولین فرد زنده‌ای خواهد بود که از سال ۱۸۶۶ روی پول ایالات متحده ظاهر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123301" target="_blank">📅 16:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دولت عراق حملات ایران به کویت را بی‌شرمانه خواند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123300" target="_blank">📅 16:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123299">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVCrsn_5ziYDwKYGqyZqjD3nIQe0UAcQOZqfZ_gbtQuPPlxbPCGCD4yTsHxiy6DqYKtFpBXV3oWqIWCDE-_Jgreho-V7BHIF9q-2XV8kYuamvXp0EP_9KIwByVyT5OBMOrOdRBTOrleHtyQtqr-6QiggW3Xnvr2THW8yUua_62JNWQfGMEyhx57HpmCtHoxY8_mZ1zkABi36dWeydPY8WZyByAveFT8ESISxE_2dzKL2cX7MXHksJAZjQpolUfiQ7m9y1opNDvf1qHarWX-WoXR7qfubCZaiy58WCC3oaPzfa8wCQH1AzEs-vqFDC82CfuYzXIvVdlGHhiXnhxpUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم، کارشناس ارشد صدا و سیما: ایندفعه دیگه جنگی نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123299" target="_blank">📅 16:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
هواشناسی: تا چند روز آینده خیلی گرم میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123298" target="_blank">📅 16:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY7u-6QngzIiXAGK_1ynGEfINa1Wem_vQ2TT74-gdbmz8FeElK8BwsQvoxGmVMks5aZ9ZiM0AGFtjxK3skGSQ4I5Qa-qHmXkB4UC3aed9z1R2WUhLg9SSarSXI46LCgsgIolnbRjhIL1y9MqFhdSI9yxMohpk8TjHc2PzSMcF158czTU9ROGoUoNTGFvZyOMFVCUCpnAhkXiKHo93WFPJdwKsJXgf-6jweLmYHgTLf0tbf4u72nVdZFFSEuaDG09I63v8oFCuWtk-GW0oadIK-K9kW15QWj0DUXoL8e3cSmUT1OuDW_4q3-veFFxt1da14UQ11pJiuthrWayWwqF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوالفضل ابوترابی، نماینده مجلس: آمریکا بعد از جام جهانی و انتخابات کنگره دوباره حمله می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123297" target="_blank">📅 16:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123296">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFIyavwqNFTh4OGbInC_ULPPdLLY89RbbR5VTgr9fmmPDuBu4yHPSbDh1kZkzjGN06ZvCFfbZEk_orVXV77sIJOBep-RF1emwtq0w1ibuiHwTXNGWvuC0201S7IFM5ogL1G7kEOKUvaG2xXnsp2S0doMNFzmlLiEDX5sFlAYGa7vcy1VD1bv0Qja2SiZJPpLgLXkgtArBclUqgHLlb_f4koeC7g5Ua3cvOL8Dbj2c5SvkVO4QcQ-jzPd5293x2hOdAmSykg_te0Iva7LgkHmPpYULDWt2BjhXxTDL-_avtVGm-FiWLd7P8I0H5p-d_mZZWVxOi7erKcHYq_6THfObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه سنتکام درباره اتفاقات دیشب :
🔴
دیشب ایران یه موشک بالستیک به سمت کویت شلیک کرد که توسط پدافند کویت رهگیری و منهدم شد.
این اقدام، نقض جدی آتش‌بس بود؛ اونم فقط چند ساعت بعد از اینکه نیروهای ایرانی 5 پهپاد انتحاری رو اطراف تنگه هرمز به پرواز درآوردن که تهدید محسوب میشدن.
البته که همه این پهپادا توسط نیروهای آمریکایی ساقط شدن و حتی جلوی پرتاب ششمین پهپاد هم از یه سایت کنترل زمینی تو بندرعباس گرفته شد.
🔴
نیروهای آمریکا و متحداش تو منطقه همچنان آماده‌باش هستن و واسه دفاع از نیروها و منافعشون مقابل «اقدامات تهاجمی و غیرموجه ایران» هوشیار باقی میمونن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123296" target="_blank">📅 15:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123295">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سه نفتکش با پرچم‌های پالائو و سیرالئون در دریای سیاه هدف حمله پهپادی قرار گرفتند، اما این حادثه تلفات جانی یا آسیب به خدمه در پی نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123295" target="_blank">📅 15:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123294">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیرخارجه پاکستان جمعه ۸ خرداد به واشنگتن خواهد رفت تا با مارکو روبیو دیدار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123294" target="_blank">📅 15:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123293">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgENMPzABHkf79AVALnUst9upWaJjr1hHY1M4m6r5aM9-UhUecqVXdNdZ8kp5V5bTzZ3qr2uPz0mIGwaU50ZQjFD3zLQV6HEaJiWkDsOS0D32ABkTowmVH3jbOEMSCBr2NiLU_2WJZMsOZv5-QOrpuS5OjCJ_FkhwDksDQD4JvykFJwE4hF06HhXo1Zr-_40zcV0gCINd5YB6cl-mX5lIz_Of3-M60cKmymPjYBJOJIZqLVWsUXrgg7RukEoAihCdBHwHZ4J1SEf0kbuYQHG08pHQMl3-cAaH8RoGI-BOxDZoZZCgxRbIF2AvkeKwwGVWEQGuE7dMZG6q5BPrgRJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیتنا، پایگاه اختصاصی اخبار اینترنت:   تمرکز ۹۱ درصدی ترافیک اینترنت در تهران است و بازگشت توزیع عادی پهنای باند زمان‌بر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123293" target="_blank">📅 15:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123292">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJps_Gv7b8BBJwlfPQd8K78qFHJLP08JkQlvU4h3a2PZSiKDRUgnNniD0zIpVIZ5EbbI1ZiRjJPdqtd4LXOSrbUkwYswQ35H5Cs3rG4JYHXRdgWUeK7mFsE9EXatKY0V24WF4UMfrridGvHjfVrbi8GkIDaYBCUxrupqd8-JvUxdyUqUm0W7PphJ0zMUoJugl2sPdkADroQA0_m_GA-nFnpr-7PXPVOSPxqyfOnxl9x3jol7qKDQtJPN6LYDLDHgMUoalH4sEXQrO2CwmTudxkFnHM_nlxsz65Z_ALWyLT0BY7USo7r3f-R71cf-W8WtxSl8O9jqMwVvbMyIIIZziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست
:
مقامات دولت ترامپ، اداره حکاکی و چاپ را تحت فشار قرار داده‌اند تا یک اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور طراحی کند، که این اولین بار در بیش از ۱۵۰ سال گذشته است که تصویر یک فرد زنده روی پول رایج آمریکا چاپ می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123292" target="_blank">📅 15:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123291">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/123291" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123290">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3UrtH5XWzZgU2bz3pkt2aTUlLOofxP-cYKqFs93CSqpOCGeG5RoMwsTTU0wCOal8cl2Gz96qkXa0ABRE6QINI2yKcag2lOaidaVipEmVK0oep7hnRae3xN3EefOGDdHShuCwHiQGWBK-4uaNWKReocRkIuKFenoC_ii2q8s5zHBxeOHsIofM09w6EWto3c_UB_2JgKuhFrHBkAc8jFu1CN-_B7EdpUI0e3KmVYN_B-4EkNiFY84q_2luVXm-IGQg8F7HK8nyl8q75D3uzACx0xHnCtY9xQgvkY28F9ui7UVmhTqRWSHoPiSC-duiCoongpF-tc0iMWQJZ6Fc1bjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123290" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123289">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5ec1c3aa88.mp4?token=dWMDk6y5xG_oUUkPVZWrwxyNTrrFTkiuDgNPZspuNQEB7W8oEoSNX5R3Y5gyHUB5loPiqjuGoKz9K-oFWoCG6dSTH490xdxwexnLCdFqhbDVZsg6w7OBVC_r0ptzOe3l7S8xJz3-mNf5xPQEfnavKLtDLKm4NEpp32CvgbcNZ7jSveucGoNZCcTcTf6F1d-v5Zb64vjrPmvjap2avBO6kqzUWJnI0EiaR05wfhos4hY29npvRN7XKUaf2ep2YUmShU4stofGTjVPBf0-31B9CPeBD0Fe2Q7q_-rVbatFDf1Fbewgtl9FPvrTooA0Eeg-cUKMc3nEagkMKYFdlISG_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5ec1c3aa88.mp4?token=dWMDk6y5xG_oUUkPVZWrwxyNTrrFTkiuDgNPZspuNQEB7W8oEoSNX5R3Y5gyHUB5loPiqjuGoKz9K-oFWoCG6dSTH490xdxwexnLCdFqhbDVZsg6w7OBVC_r0ptzOe3l7S8xJz3-mNf5xPQEfnavKLtDLKm4NEpp32CvgbcNZ7jSveucGoNZCcTcTf6F1d-v5Zb64vjrPmvjap2avBO6kqzUWJnI0EiaR05wfhos4hY29npvRN7XKUaf2ep2YUmShU4stofGTjVPBf0-31B9CPeBD0Fe2Q7q_-rVbatFDf1Fbewgtl9FPvrTooA0Eeg-cUKMc3nEagkMKYFdlISG_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف تازه اینترنت پرو خریده، بعد پسرش بهش خبر میده اینترنتا وصل شده.
واکنش باباهه خداست
😂
😂
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123289" target="_blank">📅 15:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123288">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
سه ماهه حامیان جمهوری اسلامی با خیال راحت توی خیابون جمع می‌شن؛ نه خبری از حمله‌ست، نه «ناامنی»، نه تروریستی که پیداش بشه.
🔴
اما همین که مردم معترض می‌آن توی خیابون، لباس‌شخصی، چماق‌دار، موتور‌سوار و تروریست ها با هم فعال می‌شن!
🔴
چرا؟ چون این تروریست‌ها از بیرون نیومدن؛ همون بازوی خیابونی رژیم هستن. همون‌هایی که وقتی نوبت مردم می‌رسه، مأموریت‌شون می‌شه ترس، سرکوب و خون‌ریزی و کشتار مردم بیگناه.
🤔
تروریست حکومتیه که برای حفظ خودش، خیابون رو به میدان وحشت تبدیل می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123288" target="_blank">📅 15:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
تصویری از محل حمله ترور هدفمند
🔴
هدف ترور به نقل از منابع اسرائیلی: علی حصنی،فرمانده یگان موشکی لشکر امام حسین
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123287" target="_blank">📅 15:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
تسنیم نوشت: برخی مدارس با لغو امتحانات مجازی، نمرات دانش‌آموزان را بر اساس ارزشیابی کیفی ثبت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123286" target="_blank">📅 15:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اکسیوس: در حالی که دولت آمریکا فشار اقتصادی بر کوبا را افزایش می‌دهد، احتمال روبه‌رو شدن با بی‌ثباتی بزرگ در این کشور وجود دارد
🔴
این رویکرد شتاب‌گرایی تدریجی است؛ یعنی فشار افزایش می‌یابد، اما از مداخله مستقیم خودداری می‌شود
🔴
دولت ترامپ معتقد است که بدتر شدن کمبود مواد غذایی، برق و سوخت می‌تواند تظاهرات ضد دولتی در هاوانا را برانگیزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123285" target="_blank">📅 15:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پروازهای رامسر به مشهد و اصفهان پس از ماه ها وقفه برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123283" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت خارجه قطر: نخست‌وزیر قطر در تماس با وزیر خارجه ژاپن تأکید کرد که همۀ طرف‌ها باید به میانجی‌گری برای حل بحران [آمریکا و ایران] پاسخ مثبت دهند.
🔴
نخست‌وزیر قطر بر ضرورت حل مسالمت‌آمیز ریشه‌های بحران برای دستیابی به توافقی پایدار تأکید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123282" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123281">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
تصویری از محل حمله ترور هدفمند
🔴
هدف ترور به نقل از منابع اسرائیلی: علی حصنی،فرمانده یگان موشکی لشکر امام حسین
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123281" target="_blank">📅 15:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84bd29044.mp4?token=vTK_AdAcAjRq1yXmtlnynVHUC8M-b3dyyo9UEHfTAJZd5sq6VLrv014R0doS-iWahc3Bxk7STRwxcXb0eQG0NwZvtHrt2ZXYLC1-tdnS1Y6aVPMc9T2brVJZspPUeEBoXDuuXNO_wBvAHjqNJaFiYR2FuxRkbaR2dyy5m2kQHeUxn8j6Shv0PoWGK7kVGpxMCECTe3sjnLQ7ws_RylWqlHvDyI-d4k2Ml161_GAo1bAK4qYC08iAc7ICMkBt2I9u8ToVmLnW5UK1L2d_vCEeC0Iy0EcOpDzKIf5kiz8gjhJ04r12TuKnqij5KFvy0SC-uzH9rvp42hhj-6enza2DEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84bd29044.mp4?token=vTK_AdAcAjRq1yXmtlnynVHUC8M-b3dyyo9UEHfTAJZd5sq6VLrv014R0doS-iWahc3Bxk7STRwxcXb0eQG0NwZvtHrt2ZXYLC1-tdnS1Y6aVPMc9T2brVJZspPUeEBoXDuuXNO_wBvAHjqNJaFiYR2FuxRkbaR2dyy5m2kQHeUxn8j6Shv0PoWGK7kVGpxMCECTe3sjnLQ7ws_RylWqlHvDyI-d4k2Ml161_GAo1bAK4qYC08iAc7ICMkBt2I9u8ToVmLnW5UK1L2d_vCEeC0Iy0EcOpDzKIf5kiz8gjhJ04r12TuKnqij5KFvy0SC-uzH9rvp42hhj-6enza2DEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نیروهای تروریستی که ایران رو اشغال کردن در 18 و 19 دی در حال شلیک مستقیم به مردم معترض بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123280" target="_blank">📅 15:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mQZ48e-FAlhQ5E7ecn5wo2yS3oWiU1f5uKwBqlYIxavbnwN0PmUGbGUJfmmoMPEF6hTTMqlhYVrjvRnWxzCnN370v8AWRGzIgXNV_LMkbxRMYc4r8Cpf7cf8YwfvdZ6zVtGm_uciRp4rmM4Mcq4CP3S_VpcVfKbV5Xbw71_F1Skkp01t6W2-S8eNvGNKAPwy1Td0O5la5-HpjLU-QUCrHmpzQ_RSJCYcnhe1ikmy-FqSVEMNmfNJCkpWDG_vvwqFn2DksjCzyENVR2IMC4lZFPs_9N47oAOolTTkVLl5mslei_wp9-Ei8czDE-xNdYT2HDYvngux88lQzWNEyen4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از محل حمله ترور هدفمند
🔴
هدف ترور به نقل از منابع اسرائیلی:
علی حصنی،فرمانده یگان موشکی لشکر امام حسین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123279" target="_blank">📅 15:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656bb517c.mp4?token=KTMlKfXuhURJY9eoaCdr4xmPUdOG60OWf3nhnNUXJWP_wOAAWcLKtnnx87d6DmbQ_OZe7LpFw03PYxiQuARDZn_t7RL7MNgXNZhBCw97h8i1KqpsW4ROS6b8v1f1FZewvR7M7-M8wHin9moJj_e0Eo81bxnlcgKHWagLaNOTPopHe9IIEup7R5n7ko-6QCV-6qguncvhGVdy9evHeDz4jqc8HepJRn0CSlskUxclpA8Upo0gljzD7qrywFCN_Bew6ws8xZIg4wYbpiuSPELIqo1MElhrXkxc-RuD8Dt0Zp2kotyuCe1rJChe3ixMcxCeS7arZqyCCai8yZQLkZL5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656bb517c.mp4?token=KTMlKfXuhURJY9eoaCdr4xmPUdOG60OWf3nhnNUXJWP_wOAAWcLKtnnx87d6DmbQ_OZe7LpFw03PYxiQuARDZn_t7RL7MNgXNZhBCw97h8i1KqpsW4ROS6b8v1f1FZewvR7M7-M8wHin9moJj_e0Eo81bxnlcgKHWagLaNOTPopHe9IIEup7R5n7ko-6QCV-6qguncvhGVdy9evHeDz4jqc8HepJRn0CSlskUxclpA8Upo0gljzD7qrywFCN_Bew6ws8xZIg4wYbpiuSPELIqo1MElhrXkxc-RuD8Dt0Zp2kotyuCe1rJChe3ixMcxCeS7arZqyCCai8yZQLkZL5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: اروپا ابزارهای خاص خود را برای دفاع در برابر موشک‌های کروز دارد، اما وقتی صحبت از تهدیدات بالستیک می‌شود، وضعیت بسیار دشوارتر است.
🔴
ما مجبوریم عمدتاً به ایالات متحده تکیه کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123278" target="_blank">📅 15:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سپاه: شب گذشته چندین کشتی با دستکاری و خاموش کردن سیستم‌های ناوبری، قصد ورود به خلیج فارس را داشتند که نیروی دریایی سپاه دو فروند از آن‌ها را متوقف کرد؛ مابقی نیز مجبور به بازگشت شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123277" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKcOqaD3Rnkpj3LNx7WH2Ncnf0GGGhz70TeGu4pFy3xfV30qqGyrQTUE_dNX1ZjYkTE33ZT_dOL_bk7BX6aZzx3xMEvN9uwXVpQyCOxFd2N-ISRBLYHNIdEhj1-j5GnKUbO6RAJm_DwkrIeHETobkaF-tlExrBXW4-ihDg0U5lz3tgGDmkYuk-oUiWaGsv5IwtgPUmFpZYPbCgqFE3Qp9yXKis26VCEVfyfl3CAOgdnXSi0D2q56M_PkVDbtzMo-msTJm0i5_6ULpLCKOnvAuqfVxWuytZuHLf_o-2tQYUu2lHfCG9axat4J7fHJJ3Ur1t8EhxN7cjY7O83o8v1-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXO8bylDPOZeHmPrvoKKuhUOUD8GqNG7CmhWmHIFmD4eb5Fb9mghtF-fvmeWVb5k27MY8rxaZAX2I6RcfcmADkXv-JpkRNB5qf-hMq04-Lt0aPFCB7FqUR-6uovOjze4_z16xdJBWcn1XsgF3Zox4PNfxYhb3Ns_EqGrT3TR09lpZn0tDOtBKGPUpH2DuymXL-SqnWjyqJ0pr0UCdYwfps5E-vuNUF117QyV9Lhg0rgyqcH43_saVK1tqfPHa6VompQLz4-hO2rclSz8BYXYOQ3-0dMOh1-_7HmUbJGkrx5iOT5fnkNcvRl-Mwa5QxCut9pjAIMBSptXKBXB_D2OnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی به شهر النبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123275" target="_blank">📅 15:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
آکسیوس: افزایش فشار واشنگتن بر کوبا؛ برنامه‌ریزی واشنگتن برای بحران احتمالی در تابستان
🔴
طبق گزارش آکسیوس، دولت ترامپ در بحبوحه نگرانی‌ها از بی‌ثباتی بزرگ در کوبا طی تابستان امسال، فشارها بر این کشور را از طریق تحریم‌های شدیدتر افزایش داده است.
🔴
مقامات آمریکایی اعلام کرده‌اند که در صورت تشدید ناآرامی‌ها، گزینه‌های نظامی احتمالی را بررسی کرده‌اند، هرچند تهاجم مستقیمی برنامه‌ریزی نشده است.
🔴
این استراتژی بر فلج کردن اقتصادی کوبا از طریق هدف قرار دادن منابع اصلی درآمد و شرکت‌های وابسته به ارتش این کشور تمرکز دارد.
🔴
مقامات این رویکرد را یک «شتاب‌گرایی تدریجی» توصیف می‌کنند؛ یعنی افزایش حداکثری فشارها در عین اجتناب از مداخله مستقیم در شرایط فعلی.
🔴
واشنگتن بر این باور است که تشدید کمبود مواد غذایی، برق و سوخت در کوبا می‌تواند جرقه اعتراضاتی مشابه تظاهرات ضد دولتی گذشته را بزند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123274" target="_blank">📅 15:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: «علی الحسینی»، مسئول موشکی حزب‌الله در یگان امام حسین ترور شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123273" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQh9i9Zkr65cOZrMy6M4Vo6A2TD11vpEwmYotl6lQ57ttB-JtCybPYRSTt-B9iA0h8h5AqHeqEakW0i2wuzVYHs_bmTrSCAIkqu6hxD953vmto14KKIPG1Imdq0Se3cs4QjYQLz5i3PbQGPpkCDqgImg2schFugwFdYV_lPD_52S6CUtyKIXcOy2NIDdj0y-1sQTuOW8RJDzPJGDcr0gNqDL2ncef5BytVagXwGaDFSrQWMpXhT99laqj3KAbj2zsgV5v3tzSupAHe1eckYDFZnY4ATOoACSuOhy1zmmsUiUR-b2--UU7UG4UgSdpi_RblESFXKnSjhcX5TGMO8C6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOQxSFU_zK96gUSD_DH8_umBiePLwN2Am0QGoY3RoogJGPto5HudqqH_0t1DeOuqjhmJlSBKz9YaSMZc6fzd1oViYFaKhe6IWgpV3iNDszRIxezn_GWB2tZ7HmdZ4b6tbJAexqE-gtIpWDhwmumcyuvhufd4IAYKmd9biua4QRGjSaiFEbzFERr_Dk82B2VmY6nL_5jfYtuGMB2QB9kua2UGB6banzW-C5vOafn2836HiHMqpkMtzlRuFSDn4MJU5aXgS1LVuSr5I5Ha18ngn4sTzMMS2xhS3tYqhcbKb7m39Q2W9cDH4RZxTcLQTnG3s_f4Z96tednAw_LvH5IMng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60d30259c.mp4?token=LesVCvoOaPo5leY9hQE1Cq-0_1aVUbWZBaqbFv39E82XmWkVdq0e8hkw2LMvP_CzP6pZMEZtfu_VJLgxewv2dAryOsqvWF57mdi_ZHDV3hyzo9arNkZnPGO2k3h6iiiWydw8-PofxGUtpg56vrT9mvVwIB1BwX1r0WT8wYUy8RpyUqYBSqMHA1w9pSi6QTmx731Gc91GfR6mqPXicQh75uCJzcEDJSsZfm-Cv5pzV2XCmX30pf_II9iPvFkE3yrfiE1MdpD4zgYvE992IjD7nq-8I17DpIte4x6vu0NRBIGhF8-8EhjQAmelUu-SluXuEw-RGpCJR4ONLqTh0evkaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60d30259c.mp4?token=LesVCvoOaPo5leY9hQE1Cq-0_1aVUbWZBaqbFv39E82XmWkVdq0e8hkw2LMvP_CzP6pZMEZtfu_VJLgxewv2dAryOsqvWF57mdi_ZHDV3hyzo9arNkZnPGO2k3h6iiiWydw8-PofxGUtpg56vrT9mvVwIB1BwX1r0WT8wYUy8RpyUqYBSqMHA1w9pSi6QTmx731Gc91GfR6mqPXicQh75uCJzcEDJSsZfm-Cv5pzV2XCmX30pf_II9iPvFkE3yrfiE1MdpD4zgYvE992IjD7nq-8I17DpIte4x6vu0NRBIGhF8-8EhjQAmelUu-SluXuEw-RGpCJR4ONLqTh0evkaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / کانال دوازده اسرائیل: پس از هفته ها ارتش به طور مستقیم به بیروت حمله کرد
🔴
برآورد می‌شود این حمله برای ترور یک مقام ارشد حزب‌الله باشد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123270" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123269">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
قطر و امارات، حمله ایران به پایگاه آمریکایی در خاک کویت را محکوم کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123269" target="_blank">📅 14:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123268">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MP6VZNCr6LpABxGvWbg2vDOHVoDrGXIunIlpn-lyGQHpmXqtrH0o4z5bIbSRfCFzPhBkv0fWptIYrPVQySrjDSgVQD65ZPrd6EGfHi2DsvMGQ2jE4A59FXHuPmWJOEkdbCHPJzL37kdXO6MEa2KoDSrlSk_cztqQKLjcoFyKniNlOPw6y0NIceuw0Zs9Ag_nK8pR19nEfTPaGY9J_rOguF0QQU_GqfBrYbDAjujsyqqeq512swQrFThbcOBxiQrDEtdptO7bD1eBWIWzx6AwlMM9CScv8aTjJxVpxNnTygnujF63xvI2Ky0DE4URctCi2ODrh2w7wv4CqVs4TJpe0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منصور هادی رئیس‌جمهور فراری یمن، در ریاض درگذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123268" target="_blank">📅 14:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123267">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری/سنتکام حمله ایران با یک عدد موشک بالستیک به کویت را نقض فاحش آتش‌بس خواند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123267" target="_blank">📅 14:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123266">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBEsql1Ko_jUIft97Rtxh0dsPfvazDUkJfWkclYiqkpg4L4Cx7V51x5EIRA6tJ3Mfr0JUGLqRoWx_J3PhrxZCw-SXRGs6npt3V7xjQ_578hjttlaEuXywxALp55ZujFz9lgAKp_tQl6nYVEc1W0XIOE6DoNshAuZsBpvQ75VVN9itrxH9jrSuAoQGKYOKB2bUuiyy8UD12i6-J9bdqucznYEVXkQd0NHGimnlLFdS74BYU6wzclVlMEZzcHIwfoCvPyAFNjRUmSSnC0L-ktljJ46Km-el23mJcLvWNNTQbmHpUgUXx1PXuqfzu-vExmD7lvTd6Stk_D7hnlc0nSKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: کشورهای حوزه خلیج فارس احتمالاً درخواست ترامپ برای پیوستن به توافق‌نامه ابراهیم را جدی نمی‌گیرند و آن را «زودهنگام» می‌دانند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123266" target="_blank">📅 14:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuQRNrzU3kY5fGtdn8228-BmtoCD4T2EpIy648E9IPos45NZMoJ8jA-8LAj-iRGqevLLPmeYxGUrOUZsShgJvPXcTPTS8s22kNZkKcY_idl2YppPZp5RgbCKrQ4HW1LP-MuwWHBDh48D-hsp8rNjdBRLYOAQDDAvyAl427zHgC0qFOVjr0qQP23TUZOEDaTmxeMtclBoJGkZawtyQjfthI3bfJblWmSUnLtyIIfj9q77YJ7UHQhZcrjcdh-a0sVU5gSK6J5TaEWo2HdE0uI0eU0bfGBaSnwvY-dRMPbYAfcq1bFjx6JLIAMvuepDICZXgOhQk0skL5z4XQPYOJVqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddpzrwDgPcVVG0i6chlhmxGaTmcWvSDYKWvWf_Uax9RS1SBBZEgH3wGVyNvvX1Kh8h-DUlw0ENew7iGOJM9G7O62ADno-R8Y2RP-aZFfNAFNj2BAg4fu01rnRpNhpAdtWtjsdfiVb_Pb16wHTk1tZ5wsNbb49CUfNHxDINO1Qah3kXUUQaxrmEvr_Ht6uOlbccqJD_8XI1-tIpBTOKJ4K9Mgyrxq_el8FY5ZBqpU4XN_Fvp3Nk1iTOlmWAJd8NVhg37WeYB5XNtuHRWI0zlgLdQNKSyMXCSYhHXLMYzwtUEme3-LqfOZVx_JKcpOnwFLSMuW7X0G4WFi9R2lBbq2Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0GFtGInmboginVqFb2dkfYH0OZsWUZcSC9XZih2SoZcztlle7qtibHZS5p9lhAzG5AOcvZWDlGjo10Q-uS70OBSszcThGkgapRnaS9n6bY96pF4hcbh__PDTHi1h-dU_FJwEeW9hQj9Y9iwV_CKAFjNiGlUlzK62o43A1BnUW5lFjLSxgqj_OvxFDCBfXtJwEAykl7f381egqJi_2k_RVxsqsgGMkObr4uleRfy8YpHxAyi_hV5hvCw_l-PoT8Zcuyfc75o_TMiOWwV2jaDur-KIX0rUG3QPPpuwauTzftLcA9jj_dADXVqIUS0_0EhuiJV_nXNuktK7otw5Pf39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4Kwj-eQuxSfaMBKafUtilPQjPxpRkp5_D2s8zlhtzKWxF0OKFSisIdKbF8MOMo9fuJSpaz4Lyo-qYZaJUQ13jFK6d3t2ekn0DP79aXzeLHh5cKPPGEN-cLQDr5QgzdUd-CMJop9LJMv_tn-AdlXqD5P7Wa_t0qJfeT3alC_ENrjUhQ5a8MxJgp2oOyNp6FR8EgPJ8pp82y3d1sBVrWtcU-tK-LXvWrGvWJbEAokCZpdiw8jkUYOP_kOj87RdF6114fKv290x6mTO35Q-pzwQ1JG-2eA3Kgmnx3jvzJgo79Z1w7-ucfH1RrYh_-t3AJcz9Ve2nYoHWsy8F0Auzr5DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که سی‌ان‌ان منتشر کرده نشون میده که تا حالا حداقل ۵۰ تا از نقاط دسترسی به ۱۸ سایت موشکی پاکسازی شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123262" target="_blank">📅 14:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123261">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da27079b92.mp4?token=Xs5cuYW5_Ows55-kMuQOlJTutiwgwLtxnnxtjCyR2sU_q1grzwCW68yX2TRc_7E8BdE0OJUNsVYXYZQb2I8G6IDj59F7KmvsvNJ52lcPZNzQD6QMuk3A0xOEHJoNgli9dhJb3NY6iJJixt-8KE-hEF_SQrSkJ8IPmN_JDJjmIrkTHaVzJXXxvIpgR63rdjL-_1u7Udd5ojkoK8K7M3CPjqgsWLa3D9d68-g5MMYKC89b6wtfoLvo6duBvepeV4k5EocURF8kMcRLn_0lMTC88NjqA8vOg2rTci687TIMGkqpp6t341G06EKPMybIl6WHOLvFz1nSDll1QvqReNyXrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da27079b92.mp4?token=Xs5cuYW5_Ows55-kMuQOlJTutiwgwLtxnnxtjCyR2sU_q1grzwCW68yX2TRc_7E8BdE0OJUNsVYXYZQb2I8G6IDj59F7KmvsvNJ52lcPZNzQD6QMuk3A0xOEHJoNgli9dhJb3NY6iJJixt-8KE-hEF_SQrSkJ8IPmN_JDJjmIrkTHaVzJXXxvIpgR63rdjL-_1u7Udd5ojkoK8K7M3CPjqgsWLa3D9d68-g5MMYKC89b6wtfoLvo6duBvepeV4k5EocURF8kMcRLn_0lMTC88NjqA8vOg2rTci687TIMGkqpp6t341G06EKPMybIl6WHOLvFz1nSDll1QvqReNyXrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل : تو ۲۴ ساعت گذشته بیشتر از
۱۳۵
هدف حزب‌الله رو تو صور، بقاع و جنوب لبنان، زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123261" target="_blank">📅 14:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52efb03882.mp4?token=peT2o5B_TlOnUkvV-V8E-CphOhiqkMA3LpuLK26KeDWrqPFQ-5U82W6dE7tk3UIcCQCpLjTvr7Ro9g1T95qyPXOamV3YMVdrvQrRK_pvyEwbyEYt-KNcwhJuQRUU1oXBv1MbbhYEVTxZqydKweHCOkSTwYQ3NzRQTTUmhLOIOYpTKJCBQG5zHj_eKoRmrSQTFMPs5pxzlllMAm8Y9xy07TedAiHu_VwpV-vopdSzkNXeeK67vfmBkXuiTNl81PJ146FpTG2d1nhzIKWNoGaXV-umMBpYpYrBh9IvhryhmSx2VxOabUSz3Fr-061T6F_tlpBRwO35L6e8EfzCnzIDYlBA0KxAmNpbdSH0vDH57D4K69DHaMZTlkVFHw1psIWtFYrqyBWYU7nGYbWPfnTMafVR2PpXf9cxnHUZQd3gId-Wv2zV_cOE7srdiQXo-WC3ke-QeMaMP465ghD0FvlE-f2SZgdnN0YfFsIXgh2wwTLi0s4wQNtimy60_hLFGmZjA2D_RSeE-8d5jLe0yse9IKqMQ9kPqEuvQpx3ZSE9lBvh1uGRuL24apGKzJa1PUF9y1cGAIPMXHbhu_lbVQ0Cyfm9l2z-gQ5e6wwXxxstUNZCXbZ6hcxyxy6uYZw3kENKVF33C_0fAGeZUin2xX9M3q6o8vNUBm9lShUhx1jqTjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52efb03882.mp4?token=peT2o5B_TlOnUkvV-V8E-CphOhiqkMA3LpuLK26KeDWrqPFQ-5U82W6dE7tk3UIcCQCpLjTvr7Ro9g1T95qyPXOamV3YMVdrvQrRK_pvyEwbyEYt-KNcwhJuQRUU1oXBv1MbbhYEVTxZqydKweHCOkSTwYQ3NzRQTTUmhLOIOYpTKJCBQG5zHj_eKoRmrSQTFMPs5pxzlllMAm8Y9xy07TedAiHu_VwpV-vopdSzkNXeeK67vfmBkXuiTNl81PJ146FpTG2d1nhzIKWNoGaXV-umMBpYpYrBh9IvhryhmSx2VxOabUSz3Fr-061T6F_tlpBRwO35L6e8EfzCnzIDYlBA0KxAmNpbdSH0vDH57D4K69DHaMZTlkVFHw1psIWtFYrqyBWYU7nGYbWPfnTMafVR2PpXf9cxnHUZQd3gId-Wv2zV_cOE7srdiQXo-WC3ke-QeMaMP465ghD0FvlE-f2SZgdnN0YfFsIXgh2wwTLi0s4wQNtimy60_hLFGmZjA2D_RSeE-8d5jLe0yse9IKqMQ9kPqEuvQpx3ZSE9lBvh1uGRuL24apGKzJa1PUF9y1cGAIPMXHbhu_lbVQ0Cyfm9l2z-gQ5e6wwXxxstUNZCXbZ6hcxyxy6uYZw3kENKVF33C_0fAGeZUin2xX9M3q6o8vNUBm9lShUhx1jqTjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: امروز در سوئد به‌صورت کاری حضور دارم.
🔴
ما در حال آماده‌سازی یک بسته دفاعی بزرگ برای اوکراین و یک گام قوی در خصوص جنگنده‌های گریفن هستیم که قطعاً نیروی هوایی رزمی ما را مؤثرتر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123260" target="_blank">📅 14:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b5ff794a.mp4?token=sHguo7khiXA8CJwmc4qvjOBgRMljWBX1VDloAhkNWjk0qOqv8-VStyTi2CiXKk75D_KDm9klJ5ox_RuLnMC9ifueGkYS60s3ggFUZOh-K8fBtPvmYhcQrPB6I3zp6iN1bBf_QRMX1ULVHsurGKujdzkzqHNi3M04DOp710KuL1DceBQN34ca4NSQWdLrMESAsO5N-rxvR5OFq2whRbyJq8PnMYMc9foMsXNSUIP7z6rV15NiXM5_k6pNpZqw9tlww8MfsRc6rSJMn_r6YolC5IE9tLo9RhaQH5wrrA88p1SNK3Wv5DAYyG-PZcy2L5L7AsfOEcBVicBl7dzGlONErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b5ff794a.mp4?token=sHguo7khiXA8CJwmc4qvjOBgRMljWBX1VDloAhkNWjk0qOqv8-VStyTi2CiXKk75D_KDm9klJ5ox_RuLnMC9ifueGkYS60s3ggFUZOh-K8fBtPvmYhcQrPB6I3zp6iN1bBf_QRMX1ULVHsurGKujdzkzqHNi3M04DOp710KuL1DceBQN34ca4NSQWdLrMESAsO5N-rxvR5OFq2whRbyJq8PnMYMc9foMsXNSUIP7z6rV15NiXM5_k6pNpZqw9tlww8MfsRc6rSJMn_r6YolC5IE9tLo9RhaQH5wrrA88p1SNK3Wv5DAYyG-PZcy2L5L7AsfOEcBVicBl7dzGlONErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین از ساخت نیروگاه هسته‌ای در قزاقستان خبر داد
🔴
در جریان سفر رئیس‌جمهور روسیه به قزاقستان، توافقنامه ساخت نیروگاه هسته‌ای توسط شرکت روس‌اتم روسیه در قزاقستان، به امضای طرفین رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123259" target="_blank">📅 14:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaff230743.mp4?token=qMycbzjR_msASkj8rEhXoEm2TPlGO4CukNmpF7mpJCVHtMTDBSkJMO2KjMf6PcFYb76s8IJD5773oS0xy9LViZUOSzwlvFMW_a9Q0GTg4a4IRRLa9aUPeRe6HFj8E2ubV3mjPgQBoIPtO90hOqi33t8BOr4rISDymtCjmD0B_RCMGdXcHB_j-aDEPysgOcdKL-tRoTEnpn97wbzclEizVNfoTZ0qtW3mh2NcQgG47QynebXMsLCdqX0jewELPEOLiwN1XxyDo1x4MjouIb-QJepr_zTaF_1jhof6YzvTBeaDnq3I6g2d0te5pDx0VMHJb-1LwA2L862Kmu1dHSV9KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaff230743.mp4?token=qMycbzjR_msASkj8rEhXoEm2TPlGO4CukNmpF7mpJCVHtMTDBSkJMO2KjMf6PcFYb76s8IJD5773oS0xy9LViZUOSzwlvFMW_a9Q0GTg4a4IRRLa9aUPeRe6HFj8E2ubV3mjPgQBoIPtO90hOqi33t8BOr4rISDymtCjmD0B_RCMGdXcHB_j-aDEPysgOcdKL-tRoTEnpn97wbzclEizVNfoTZ0qtW3mh2NcQgG47QynebXMsLCdqX0jewELPEOLiwN1XxyDo1x4MjouIb-QJepr_zTaF_1jhof6YzvTBeaDnq3I6g2d0te5pDx0VMHJb-1LwA2L862Kmu1dHSV9KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی عجیبی که توسط کاخ سفید به جهت ۶.۷ میلیونی شدن فالوورهای اکانت کاخ سفید در تیک‌تاک منتشر شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123258" target="_blank">📅 14:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کویت : ما حمله‌ی دیشبِ سپاه رو محکوم میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123257" target="_blank">📅 14:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: منابع دخیل در میانجیگری آمریکا و ایران می‌گویند در ساعات اخیر پیشرفت قابل توجهی حاصل شده است و شکاف‌ها بین طرفین در حال کاهش است، اگرچه چندین اختلاف هنوز باقی مانده است
🔴
یکی از مسائل اصلی حل نشده، درخواست ایران برای تعهد واضحی است که امضای توافق به معنای پایان دائمی جنگ باشد، از جمله درگیری‌های مربوط به اسرائیل، ایران و لبنان، و اینکه پس از امضای توافق امکان بازگشت به جنگ وجود نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123256" target="_blank">📅 14:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
الجزیره: سقوط سهام آسیا از بالاترین حد تاریخی خود پس از حملات آمریکا به ایران
🔴
ارزهای آسیایی با فشار مواجه شدند، زیرا شاخص دلار با کاهش امیدها برای حل سریع جنگ، به بالاترین حد یک‌ هفته‌ای خود رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123255" target="_blank">📅 14:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123254">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sVivQ-QEYLn_qaWTQw4jJoIiDrS_7QcREa5r8PeSXh_4n-T9STY75wrKj_Wsv1OeccDXgLSYU_fSfyf8R1J5mo2G13T5vXmsAuIadg_Q2UgSMnbLhaFucC8OCg5bdr8MUdy6KHFXDD9XOfbmUZkyPkXY1Q5itM5tk0oFJq167dEVX9uFblJh5j-V62d2XQsO4wBMl4SNKSsOLgVHn07DQG2dq4pzXpxSC-Lj2SS1MlKRcEHkEEhRXi8w7WRIBhf9SDrA6e9VueOvL0wX9TWwj2KTiVRtj-Y5l8OE0a6UNrzMyeuPe4B5UJ8xbgaXRzJYIWBIQXyuP-XYgVUJickA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123254" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123253">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
آمریکایی‌ها هر روز ما را تهدید و مقام‌های رسمی ما را تحقیر می‌کنند، نباید با چنین دولتی مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123253" target="_blank">📅 13:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b3059c39.mp4?token=HNbwIEXk6rM9r-WAHKyQrbVETu7uT0uzD6BUhEGfVHZXkizWRatw9xetQw0fQmz8A_kAoGwBPatzz4GUx7d4j3DHDvB5Kpi1bkvS_sFlI8XidXRfWhsZzyEnNM0_Pe_I8VC3qyDYnUqUCwZhTRufnDKh29evR57xbrgoztBvLfie0LGXGVyEfJ3uGjw60XBC2RzceMBOBdbaHUNw80_PuJMBAZe2yNsGGlEr6UU2ZEEQN8R7PCEZSKyCaQRC0WW3gRp8GsWwDIxs5FwJXD7vZjMfpQPeqGXlWVBTqXPip5fRKuZnPO4iryumTyrP74FaPvt81xzTWhaiSdzSvzCnVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b3059c39.mp4?token=HNbwIEXk6rM9r-WAHKyQrbVETu7uT0uzD6BUhEGfVHZXkizWRatw9xetQw0fQmz8A_kAoGwBPatzz4GUx7d4j3DHDvB5Kpi1bkvS_sFlI8XidXRfWhsZzyEnNM0_Pe_I8VC3qyDYnUqUCwZhTRufnDKh29evR57xbrgoztBvLfie0LGXGVyEfJ3uGjw60XBC2RzceMBOBdbaHUNw80_PuJMBAZe2yNsGGlEr6UU2ZEEQN8R7PCEZSKyCaQRC0WW3gRp8GsWwDIxs5FwJXD7vZjMfpQPeqGXlWVBTqXPip5fRKuZnPO4iryumTyrP74FaPvt81xzTWhaiSdzSvzCnVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین : حجم تجارت بین روسیه و قزاقستان به‌زودی از ۳۰ میلیارد دلار عبور می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123252" target="_blank">📅 13:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123251">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
امواج مدیا: قطع روابط سومالی و امارات؛ افشای شکاف استراتژیک عمیق میان ابوظبی و ریاض
🔴
قطع روابط دیپلماتیک میان سومالی و امارات متحده عربی، نشان‌دهنده یک شکاف استراتژیک و گسترده‌تر میان ابوظبی و ریاض است.
🔴
عامل اصلی شکل‌گیری این بحران، سوءظن شدید موگادیشو به دولت امارات است؛ چرا که سومالی معتقد است ابوظبی توافق به رسمیت شناختن متقابل میان اسرائیل و سومالی‌لند را تسهیل و هدایت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123251" target="_blank">📅 13:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYJOAwYr3BI-iQgkO-t-Sxk6SAwekSoE9BmaUrmG5OyCd3Nth1LtQxmVSfOnmE63tkl_pxlfGTsunXT1SFYt9RkXAitGcy5Ag6DhYNF44y5zrd3_-iJN7WJf9sqIESF4Epu_muTa6PjmP1dmdjvghu-XvhlA10JVUA9HrtDCW55LY9qelIjUx8B4pJwvMpCMT5oJq6M3XynZf_MajUcoF0CA0CGxVKq59hoAQdVvXe3IRGCMkoe0PX5S0bMvgQDasEEoupqXu7grccgBzxFlNlDUW06jphBV4Zw4Brm5QDJ1AIm1nCjDWniu12BwY-0w0UH7LoVRVGRL0yxxfG1Lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۶.۰۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123250" target="_blank">📅 13:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOR_s6k1pokX-vVCHxN41d4pittavsBtfwImiReWrtV5QLTYC6ZYTNMaRnEyCd8l749Pz-zNlV3BlupR3cVpBAuT3cFOgvsx2DPcHDfmAyCiAri0p6aJq1v14-CW00tEeLR9d5bGTa91XOvmwPKQUYLKmu7N6J5Q67jdkN1lBqbd65KXJWhwChI-sQTv7jNKHgmRtVrVDNABCi6ND_843HXEiLy5fDkbIcnwDbLdRC6OyEpCBQ11vV8XQtYsnj_7p9SuiF3PqYN8kKatAuAUtfxCfO7qg5k3K97XH2EwZ4IyDxWbYOAgl7gK1CoVjb0CV6ePSdwAAYQEoEg-yJ58ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمودار جدید نت بلاکس نشان می دهد همچنان بخشی از محدودیت های اینترنت باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123249" target="_blank">📅 13:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر علوم، تحقیقات و فناوری درباره زمان برگزاری کنکور سراسری ۱۴۰۵، اعلام کرد که پیش‌بینی ما این است که کنکور در دهه سوم مرداد برگزار شود و رئیس سازمان سنجش به‌زودی جزئیات آن را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123248" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzcvxootPQbFQAOKE7FsgB7-xwx9_CM_kj9eRpHV7pQ72LPhtywHz1rDS4xQ4JYmNkzXX3O_lv-h8sJfPaBJATwPgZ6LWTvEWQuEl_VDC2svp3vLm7uTpZSzEcXu25KstrMXqeB7YAbCj2Wjmy6Y3OFhX6HrBHEUPBJ6BMWSdzZYjj3MH7_4XB6vfVNbxP-tclQr8pvyXLT0nM-Cc4oX-eaaOL1zi-RKZUbFKkmT2-8dkEeFN9pYziIyPW00zyWFyJFGXgSxJeVARDITVPQh_x3czZWTPzylhUIwUYxN9nl_z6mgnFWNl25_oLAeXIcZmgUNZUQsnsmuFyroBIXIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوارنگاره جدید میدان فلسطین تهران: اسرائیل ۱۵ سال آینده را نخواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/123247" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClcE_yuJR7xl4ogGSjPIr9SDAjBpSisP2SMgm8jmUJl7wPHaOAFLjEzydN0EUzUVXfmvlREzg8yorC2_VUrIA8yHk0wWxVb5MQqzaR9Y1GRjN__c98_pHsWm7LNXCWyJLPKTaCbzZIGzygYLew-RNpdR8-eRFd_RLbV1PX8pdC1CALhfWxzET52GhdSPM7z4qVwevuW7mmYW-LC862BsXW2cnbxatNx6aIA7gTIlNvSl1kZtd9zGSqhuWrrZVuDLLOjdtdNH7XSP3ycYy19v4Ead0DmjB0tzYMYwHoVqhkvCUZyk4tMOnbdgWWmhIVmuOhlF5yUITm5XjSsYjcAKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
«روزنامه وال‌استریت ژورنال دیروز گزارش داد که ایران برای دور زدن تحریم‌ها و محاصره آمریکا، از سازوکاری موسوم به انتقال کشتی‌به‌کشتی استفاده می‌کند؛ به این صورت که کشتی‌های تحریم‌شده حامل نفت ایران، پیش از ارسال محموله به چین، بار خود را در دریا به کشتی دیگری منتقل می‌کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123246" target="_blank">📅 12:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f949a64946.mp4?token=YmvxWjwPjLJJ-4_uL-rB_qUSJD1qrIH5CChQusGwSKMpXCn1iCXGpMNZwNpdQUyJIAf6JPJ_rPRVmgCEt1mlY7P-7vNBPhtMaa-vLO-Uk3ZcKx8JcQCUi0rD0Tm3P7_zBajU8tjAkDKl5yHr-bbwgj9U6g7GIugX2Zj7OBWORtYRL69WB7k2N6xFeY9BCJy8dxxdK_tKULJmo2ppTP8Z1u6BI4RJ2Rp5Xa9gjaP2wp40JmaqkBGC06LVlcG2q1rSNy4GtvJhTP8tECc86DZzoKBJNR4x5Kb4AyV_m6lxBQ1Src3dSRpGg1yYFaPJW-7mjmBLuOJP3Cp8Odq193yAcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f949a64946.mp4?token=YmvxWjwPjLJJ-4_uL-rB_qUSJD1qrIH5CChQusGwSKMpXCn1iCXGpMNZwNpdQUyJIAf6JPJ_rPRVmgCEt1mlY7P-7vNBPhtMaa-vLO-Uk3ZcKx8JcQCUi0rD0Tm3P7_zBajU8tjAkDKl5yHr-bbwgj9U6g7GIugX2Zj7OBWORtYRL69WB7k2N6xFeY9BCJy8dxxdK_tKULJmo2ppTP8Z1u6BI4RJ2Rp5Xa9gjaP2wp40JmaqkBGC06LVlcG2q1rSNy4GtvJhTP8tECc86DZzoKBJNR4x5Kb4AyV_m6lxBQ1Src3dSRpGg1yYFaPJW-7mjmBLuOJP3Cp8Odq193yAcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه ویدیو حمله دیشب رو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123245" target="_blank">📅 12:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تعداد مبتلایان به هانتاویروس مرتبط با یک کشتی کروز به ۱۳ نفر افزایش یافت که از این میان سه نفر جان باخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123244" target="_blank">📅 12:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مراد ویسی: یا توافق میشه یا جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123243" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کرملین: روسیه به کارکنان سفارت‌‌خانه‌ها هشدار داده است که باید کی‌یف را ترک کنند و پس از آن، هر کس تصمیم خود را خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123242" target="_blank">📅 12:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2g87L1Ri6qPjiqWEDW4wIXdmIq4BbWUx_R6vCgAcsAlnNbc8YjkhnUj6-rJSqhmxxHTNPgPQX8RZSyTlz1o8yNLm_fIeqft08ns7nKiMKMeXnvEa_TNj63O_Dwt3665nRR6CGtps19kCH-4fgMYa32QuPa3wydS0jBHirl-O7BH_ZVO7JaiUM8PmcN9bx1PnnwUvUn0QXJhC99yyufUaPNiebkaGXKZD7EU7V6wfljfJ4BALTJ1JeIG2_lHPDpY1po3hlUBhEZGbieF-691g2osJZKtjI14DV8Qy0FYBc2jC7nzUjB-avSlCyfeDwF0JmsG6-wIIjT5e-z-5xsVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در یک پست در Truth Social از نخست‌وزیر ارمنستان، پاشینیان، برای انتخاب مجدد حمایت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123241" target="_blank">📅 12:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ایر ایندیا، پروازها به اسرائیل رو تا ۳۱ ژوئیه لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123240" target="_blank">📅 12:25 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
