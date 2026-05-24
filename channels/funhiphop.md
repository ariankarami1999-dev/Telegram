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
<img src="https://cdn4.telesco.pe/file/V1vEagIvlliBZ8AqabnI9k1mZUCiSQojMQhovJoH61r9NwcVSWRLQ6BRlp1hlzEB3iba_mSE8577es9496VtLQQuTAMSKN6cKkajkzUsOLzYHVXVu1ppZK3U_ELhfenVm042rL6u81GsUmRsllk8wjzfFz12_pLPJWjyUmaXdu16i9eghci4cFt-qsDwugN7FxVMn_ze8ZqAn55Yy-Y5RV9iyPuN_R-5S7y2KfkzyzudY5xpWFkIfFHHFwzDavvsYD3k6sEZKuNbCRwi9K-Y1D5u0x37yx8oJ16A8_6C8xqUxfnnSsgyUd0qfpiiNKqCbuRXbjYMMLfvTz69Sb_ADQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 09:05:40</div>
<hr>

<div class="tg-post" id="msg-75730">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ان وای پی: نصیره بست ۲۱ ساله، مهاجم تیراندازی نزدیک کاخ سفید، طبق گزارش‌ها خود را «عیسی مسیح» معرفی می‌کرد.
او پس از شلیک ده‌ها گلوله توسط نیروهای فدرال هدف قرار گرفت و کشته شد. گفته می‌شود وی سابقه مشکلات روانی و نقض محدودیت نزدیک شدن به کاخ سفید را داشته است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/funhiphop/75730" target="_blank">📅 08:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک‌تایمز: مقام‌های آمریکایی مدعی شدند ایران در توافق پیشنهادی ترامپ با کنار گذاشتن ذخایر اورانیوم غنی‌شده موافقت کرده است. جزئیات این موضوع در مذاکرات آینده بررسی خواهد شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/funhiphop/75729" target="_blank">📅 07:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8mCZP6gCXC8FL_WnFTBMz3_eOJCicj5cWtUgXc47CtDH70u12I6LzOvbZjCamfbKI_bZzfURmCAaSmJgUHU3A5mE_52jBWr177r0HzthLyXX0AN8-QHATvNMXoiAOJNQhq6ODgM1OzKcDqIfD7DRNZeG-G5Or2RpndNlNgc-X9_bqAbuoHHgS7pUQuxDI3hBKxEC4xaBgief8stD3CpyJcho7uOyvro6p6aRsamOHfMk_K59tpbRYmVrIy_tEgAcDVNEmuBDlTnvBu-x9-V5G5smzY9et9EARBloa7vRHeCyWiq3wmB0gBOZb7cB2HHcgIgzkPkptNUGh98nLdUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا قحطی بود برا اون عکس پسر؟
باید سعی کنی تا انتهای مسیر نیش ترمز نزنی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/funhiphop/75728" target="_blank">📅 05:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikURi3GNgThs-8qiDbtLFh_p8daSmgOi2_hRD3_R8T9lNvkUyDQeGuak8qY1vXsMhBpKhbFyv9xAAy1A42B-R1pm8UajAoIPU6ot9353sBQoXYsp8Lvq39gQvBWFpq8IbGq5vWxwqN0Vbku5XCUFr73naL4nzez3BPhW3stKUZA25_oelb6pfV4DbnW-Vm9XDs1TzHCNASeNcsQt-WRrhLUXwe41-CQGpnL5B4nhbFuPn55PA8DLE8verZ8CCpw0iZ11I74baS10I9xWK31qamvu-mQwDZj4uWgpbyjHbqi7xp476M7gvVehKVo8YW30DaiuBw9QrFUYZGpsnVb-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه یه سری حرومزاده برای چس تومن پول، اقدام به تبلیغ بدافزار در قالب vpn کردن. روش کار به این صورته که با عنوان “نسخه فلان مود شده / رایگان” یا “قیمت vpn خیلی خیلی ارزون” شما رو توی تله میندازن و میگن برای اجرا باید فلان فایل رو نصب کنید.
از نصب هرگونه فایل تحت عنوان vpn از منابع مشکوک در تلگرام، جدا پرهیز کنید.
گوشیتون کاملا بگا میره و میشه منبع تبلیغات برای قشر حرومزاده دزد.
الان همه وی پی ان پولیا با همون نرم افزارهای عادی v2ray کار‌ میکنه و نیازی به نصب چیز جدیدی نیست.
@Funhiphop
| Comentive</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/75724" target="_blank">📅 01:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
نیلی افشار بلاگر اینستا رو یادتونه که بعد قطعی اینترنت بی پولی بهش فشار آورد و اومد سمت Only fans ؟!
👀
برای ورود به چنلش صد دلار هزینه کردیم تا عکس و فیلمای جدیدشو برای شما بزاریم توی رباتمون
💵
‌‌ مشاهده عکس و فیلمای نیلی  ارزش دانلود 85 از 100
🍒</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/funhiphop/75723" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcKqjzQh3SsbFrefLtCliu1BcaFSgNmCCTUqj48VyivXSLsPn8MBQlAw_vqgIES18Ew3MnDqP0YELuUlpNxyukiLk1bFpq0Gx9i4CByKojocnaZnvxWhUse6Uueglr-SnFR1pRVev5bncFyk_xdEyqb6Pf36OhfSDGfgKWxwbzeiUy8iZ7PZAK7etLMom-Jrgd_3DoRZbVvAwwLmWwDrPGF3-iq6Sx4IHM-TZk_xo7hhCsUbPuAWYLCMScYsKehK3r6V9t6ItwG0ntQPZFAcf5qhEnBEJU5Fhgh_2QvARNvuIBQn47rO_bdS3d2CAEaKaBPyJyFIqOwrsDGIfk64Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیلی افشار
بلاگر اینستا رو یادتونه که بعد قطعی اینترنت بی پولی بهش فشار آورد و اومد سمت
Only fans
؟!
👀
برای ورود به چنلش
صد دلار
هزینه کردیم تا عکس و فیلمای جدیدشو برای شما بزاریم توی
رباتمون
💵
‌‌
مشاهده عکس و فیلمای نیلی
ارزش دانلود 85 از 100
🍒</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/funhiphop/75722" target="_blank">📅 01:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الجزیره: توافق موقت بین ایران و آمریکا به مراحل نهایی نزدیک شده و احتمال کاهش تنش و باز شدن نسبی تنگه هرمز وجود داره.
فارس: برخلاف ادعای ترامپ، تنگه هرمز کاملاً به شرایط قبل برنمی‌گرده و کنترلش همچنان در اختیار ایران باقی می‌مونه.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/75721" target="_blank">📅 00:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjcFobkTaTJLrL-fjNiPJcikiAj_03W-tDXPYaTGC8BSLrjtYSPJZDAdEGzvbySiC3hBhseqNK4Wb84UuURQDRwEzhK6SnRyi9W3bZp80W-oSvaYEgOHEKOAUWH_9J5OsGSixucpX81qHl8gpyUkdc6vpBu6Eccg6Tqn73eEo5QYKFckQ3xBIsuTDn2eIl5PsAKsYUQfea421CzPVMTiD6A_Jg207wKief-3HK4y3dU7lEnkoaZ91smuDbFLxzVXzx-Ww3kLnR9hzl4dSnYqvunfBr6S_CcTgzgv6mOSc4BNPLbGp2wAUY9T6UoULC-Sj4kx-Joz45ZtOw-1ceN0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/75720" target="_blank">📅 00:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ کصکش من که میدونم داری دروغ میگی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/75719" target="_blank">📅 00:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه:
«در نگاه رومیان، روم بی‌همتا و مرکز بلامنازع جهان بود. اما ایرانیان این تصور را در هم شکستند؛ زمانی که مارکوس یولیوس فیلیپوس (فیلیپ عرب) برای جنگ با ایران به شرق لشکر کشید، نبرد نه با پیروزی روم، بلکه با صلحی بر اساس شروط ساسانیان پایان یافت؛ تا جایی که امپراتور روم ناچار شد شرایط صلح با ایران را بپذیرد و در برابر آن تسلیم شود.»
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75718" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVtpdDxlCQpWweaOeVc7OAaUKaULAKWoijAvkmdDyDhGTbML7_u1Qe4ivYsJ6oZkAkFacxNxRKbOSkk2Dejg4SYtjEpJdvz56O171zVQq1BA2DaMcIpUSHya-4rC5FcBqWjAU--1j-8eP5EWnzkchBsd7y0TtovXvP9yLM7XLfpx7-uLOWas0EyCz5r6VihVpykKbFpd2Dkited3H5YKcOL-nLLnjBXE0Q9Ei8jHSmXWZTnnKZmDjoPGivbuVeyy5ai8VQ98Fvvid3OcNFe5n4oCgFqch2FCXhZ8iRtT4qpcTQ2ThyTC9fnhK0q01pERmlKeJRXQ6yEyWunWG3z-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش اتریوم به خبر های مثبت مذاکرات
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/75714" target="_blank">📅 00:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قبل جنگ دوازده روزه قیمت تتر ریخت و بعدش زدن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/75713" target="_blank">📅 00:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از من به شما یادگاری، هروقت دیدین یه جمهوری خواه آمریکایی داره از صلح و مذاکره صحبت میکنه، دقیقا همونجاست که مطمئن باشید قراره دیر یا زود عملیات نظامی رخ بده، و البته این عملیاتم فقط در راستای منافع خودشون و منافع آمریکا انجام میدن، نه کمک به کسی.  @FunHipHop…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75711" target="_blank">📅 00:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](ChamanDarKhak)</strong></div>
<div class="tg-text">از من به شما یادگاری، هروقت دیدین یه جمهوری خواه آمریکایی داره از صلح و مذاکره صحبت میکنه، دقیقا همونجاست که مطمئن باشید قراره دیر یا زود عملیات نظامی رخ بده، و البته این عملیاتم فقط در راستای منافع خودشون و منافع آمریکا انجام میدن، نه کمک به کسی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/75710" target="_blank">📅 00:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دفعه اول جمعه زدن دفعه دوم شنبه زدن  قطعا دفعه سوم یکشنبه(فردا) میزنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75709" target="_blank">📅 00:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
ترامپ:  من در دفتر بیضی شکل کاخ سفید هستم، جایی که همین الان تماس تلفنی بسیار خوبی با محمد بن سلمان آل سعود، رئیس جمهور عربستان سعودی، محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست وزیر محمد بن عبدالرحمن بن جاسم…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/75708" target="_blank">📅 00:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
ترامپ:
من در دفتر بیضی شکل کاخ سفید هستم، جایی که همین الان تماس تلفنی بسیار خوبی با محمد بن سلمان آل سعود، رئیس جمهور عربستان سعودی، محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الذوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رجب طیب اردوغان، رئیس جمهور ترکیه، عبدالفتاح السیسی، رئیس جمهور مصر، ملک عبدالله دوم، پادشاه اردن و ملک حمد بن عیسی آل خلیفه، پادشاه بحرین، در مورد جمهوری اسلامی ایران و همه موارد مربوط به یادداشت تفاهم مربوط به صلح داشتیم. توافقی تا حد زیادی مورد مذاکره قرار گرفته است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همانطور که ذکر شد، می‌باشد. جداگانه، من با بی‌بی نتانیاهو، نخست‌وزیر اسرائیل، تماس تلفنی داشتم که آن هم خیلی خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به زودی اعلام خواهد شد. علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/funhiphop/75707" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75706">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سلام وحید
‏تعداد زیادی جت جنگنده با سرعت بالا از اسراییل بر خواستند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/75706" target="_blank">📅 23:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75704">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دفعه اول جمعه زدن دفعه دوم شنبه زدن  قطعا دفعه سوم یکشنبه(فردا) میزنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/funhiphop/75704" target="_blank">📅 23:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دفعه اول جمعه زدن
دفعه دوم شنبه زدن
قطعا دفعه سوم یکشنبه(فردا) میزنن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/funhiphop/75703" target="_blank">📅 23:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdHr5OxQ5Jd0w-otx4_WpU-GSJ5YMWCWs98gy462Ir2QANs9EudV8YXX09BN91tKOTb_Tnagez-vo7G1TuW_hhHr5QoUOwAseXGijgRdeJMNMFKkLfhV7sWuaLm5xIVfUNXutXfZNF1xKIIW5j2kUL5PKx9xQr2F2LrlPjItIbTeRhF2S1JCzlM6NOePYCdQHn3nW1IWtgrtI_hJVfWq1jRC-YvIE5AwBaSq1lzJ5Rw4dWXRoMm6kPapbHSYzQP2EneM8W4VwKovsSH9XjPxy91n22dBoQRx9FBT_l1Re0ts6gTzt1rbmbB2F-ABLP7jqmivP0toaOsoQlGeFpkUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه: تنها چندساعت تا نهایی شدن توافق میان ایران و آمریکا فاصله داریم.</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/75702" target="_blank">📅 22:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فاکس نیوز: هیچ توافق بین ایران و آمریکا صورت نگرفته است.
یک دیپلمات منطقه ای گفت تماس دونالد ترامپ با رهبران منطقه ای بسیار مثبت بوده است و رهبران منطقه ای از شتاب جدید گفت و گو ها استقبال کردند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/funhiphop/75701" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چه توافق بشه چه توافق نشه چه جنگ بشه چه جنگ نشه
ایرانی ساده فرقی به حال تو نمیکنه چون تو جفت حالتش برای اینکه نشون بدی زرنگی پامیشی میری باک 30 لیتریت رو پر میکنی برمیگردی خونه
دلار و تورم پایین نمیاد که هیچ چندبرابر هم میشه صدات رو هم نمیتونی در بیاری
جلوچشمات رانت خوری میکنن بازم کاری از دستت برنمیاد
پس توی هیچکدوم از این حالت ها اوضاع و احوال ایرانی تغییری نمیکنه
اینه سیاست آخوند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/75700" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نیوزسیتی پرو: جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/75699" target="_blank">📅 22:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">48 ساله توافق نشده نکنه انتظار دارید توافق شه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/75698" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الحدث به نقل از منبع عالی‌رتبه: ظرف چندساعت آینده توافق میان ایران و آمریکا اعلام می‌شه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75693" target="_blank">📅 21:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0l8iIQZ41Me8TBDXB4F6DsPIu3ZbqJJGLX7AVilQMjtuwcJLQbOuvBcI2QhikVxNYINwA9EreiYE3UlXzhiejgjd2zt89sbh_C2FHb3WDNcCu3Ir9nYa7mjUTh9YrSl66onHCmnn9d-1KK4zOoKE6mIp9hXvnOlYlc9FKWAJCdi4HFW136eht5DQEq8Z6EFa0aVGWRvKSjhbvXPl4sRwWwgcn7a7-oorl3MS1fYjPxGSbtZPbAO23vOleiiaNtErl_LZxIrNlstSfi4r4hPTW2jnqOgvSV2WGZjX_Fmcjytjilw6EypwTcia4I5FW_gwn9ytsHgRXUPOI2sDbw2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا: آمریکای خاورمیانه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75692" target="_blank">📅 21:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نمودار محبوبیت ترامپ بشدت کاهشی گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/75691" target="_blank">📅 21:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مقام آمریکایی به آکسیوس:
توافق میان ایران و آمریکا برای پایان جنگ، نزدیک و در آستانهٔ نهایی شدنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/75690" target="_blank">📅 21:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الحدث به نقل از منبع عالی‌رتبه: ظرف چندساعت آینده توافق میان ایران و آمریکا اعلام می‌شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/75689" target="_blank">📅 21:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/75687" target="_blank">📅 21:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuBc9r4PXXOMk26N_B7JOfHxMv3DgagLwmCnUI9XEdonktXlch8ZbOfAJ7UIMH_I2LaOEGkSZuQxpMZJ5MlwQyFBFy7iMdTrJ1mXE4Z1A7eUd0urUO_dt75mhXAljWXAF5H5_Jx1f7jfOm927bZDzaPQiahLwNWQxxK6ZzCNdLm7w7kHG5ldheGnkwyHkhqsUcKYvTxzIiTYjsKaP5RMec2GGLtMB-_blZUKDv-d3kfZ_KF8jGFceHKlI_Y0B6bireJgBDVrzlR-ZJ3KufoUDpN-nDwN3iQYqmTyoah6FMGphTAF6OOCiWm_ClKhHiNXKLEJ08kxM_CnPlsZQyjdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/funhiphop/75686" target="_blank">📅 21:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حمله کنسله   منابع آگاه می‌گویند به ایران ۲۴ ساعت فرصت داده شده تا چارچوب توافق را برای ۳۰ روز مذاکرات بیشتر بپذیرد، در غیر این صورت حملات از سر گرفته خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/75684" target="_blank">📅 21:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حمله کنسله
منابع آگاه می‌گویند به ایران ۲۴ ساعت فرصت داده شده تا چارچوب توافق را برای ۳۰ روز مذاکرات بیشتر بپذیرد، در غیر این صورت حملات از سر گرفته خواهد شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/75683" target="_blank">📅 21:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">لیندسی گراهام: تو منطقه بعضی از قدرت‌ها ترامپ رو تحت فشار میذارن که جنگ با ایران رو از سر بگیره (امارات و کویت و بحرین و عربستان احتمالا) و بعضیا اون رو تحت فشار گذاشتن تا توافق صلح فعلی رو قبول کنه (قطر و عمان و پاکستان).
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75682" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نهادهای حکومتی در تهران در حال تخلیه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/75681" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: اگر برای اسرائیل خوب نبود، معامله‌ای انجام نمی‌دادم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75680" target="_blank">📅 20:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75678">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آکسیوس: نتانیاهو از ترامپ خواسته دور جدیدی از حملات رو آغاز کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/75678" target="_blank">📅 20:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75677">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپو پوشش نمیدم من، خستم کرد</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/75677" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=Iep3NPpv39l0_Ms2dGaen1dHiHnKLVKVczhKFJs4M14ShU_qoCtqqc5zs3t3FTQl8fsxqnHPERwFGWRC3HpIcCOQ1S31WPa6sf-bBNsWEz3S8ZItEul_pq2oka2yhCnbne5_27Tu_lQCjpFlwZBO15WWBem4uoOBi9_jL22EL__Lok8mqaBQWOqV38O8eo-vbvJt_b4jk_yTMtuCB61kYBrsBtWNK_EdEjRGs2VprlglnRmYnNWoNQ8h6j5bzdV_FzpQL-AI31fjq_F9b29pRaaLcDIE_C31WUsHh1rBggGKw_wDpiuiFJyq6fvvk0xZun3jHzehRB2Z3gySclH0kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=Iep3NPpv39l0_Ms2dGaen1dHiHnKLVKVczhKFJs4M14ShU_qoCtqqc5zs3t3FTQl8fsxqnHPERwFGWRC3HpIcCOQ1S31WPa6sf-bBNsWEz3S8ZItEul_pq2oka2yhCnbne5_27Tu_lQCjpFlwZBO15WWBem4uoOBi9_jL22EL__Lok8mqaBQWOqV38O8eo-vbvJt_b4jk_yTMtuCB61kYBrsBtWNK_EdEjRGs2VprlglnRmYnNWoNQ8h6j5bzdV_FzpQL-AI31fjq_F9b29pRaaLcDIE_C31WUsHh1rBggGKw_wDpiuiFJyq6fvvk0xZun3jHzehRB2Z3gySclH0kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا من هزینه نمیکنم برم اینستا اینارو ببینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75676" target="_blank">📅 19:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/75675" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j41sglQtxJrbai-wJaeD31ppSySzWwtIDOkPXZpcy81KOn_1qVBsVluq5ZsJ_ZJRkOOkmnUYeH3KF64y9GlaUqFOB5nf9s46mEzp5Ls18AtIhYWkI3P3VaOCxsYoaIMB68gb3ufVijSJJs9S4jMZs_NrUDzPbGoNIsAfKA-xvsgmGPnBrc__NV6Gp_kD_uVgM1oqm6N48INLOOdF2ugLKUa4gcjVNGF98Lqw-N5c8r-jYL6_-kyB3b6tjq0N2a-CBUj66jMcIzrK2fo4r436uP1pHokPR8JI3NF95aYhvtIR3KP_Xbx3TfzVGTgCVGifSQbN8EmG__94skI1ZF8ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/75674" target="_blank">📅 19:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار اکسیوس در توییتر: ترامپ میگوید پیش نویس جدید توافق با ایران را با مشاورانش بررسی میکند و احتمالا تصمیم نهایی را روز یکشنبه میگیرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/75673" target="_blank">📅 19:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک تایمز: فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند. این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/75672" target="_blank">📅 19:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75671">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فایننشال تایمز:
میانجی‌ها معتقدند که آمریکا و ایران به تمدید آتش‌بس به مدت ۶۰ روز و فراهم کردن زمینه برای مذاکرات هسته‌ای نزدیک شده‌اند.
توافق پیشنهادی شامل بازگشایی تدریجی تنگه هرمز، بحث درباره رقیق‌سازی یا تحویل ذخیره اورانیوم غنی‌شده بسیار ایران، و تسهیل محاصره آمریکا بر بنادر ایران، همراه با رفع تحریم‌ها و آزادسازی مرحله‌ای دارایی‌های خارجی تهران است.
یک مانع بزرگ همچنان درخواست رئیس‌جمهور ترامپ است که ایران ذخیره ۴۴۰ کیلوگرمی اورانیوم نزدیک به درجه تسلیحاتی خود را تحویل دهد و سه سایت اصلی هسته‌ای خود – نطنز، فردو و اصفهان – را از کار بیندازد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/75671" target="_blank">📅 18:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">من خودم بتمنم ولی الان بحث، بحث وطنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/75670" target="_blank">📅 17:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLRaAG1uBSO8I_B4Fd_ZOzMTwl5OKyE-LRssUqAE8i5NI4gVA5NaIXMMFh8PSL6fM6DYc09Ifu8DmXbSMX4Ak8e2nBgN_ZLifnOtleustI8S6IeYjDQTBkGIP7nalw975tO-l5MZB1SNzTvYRnRBp_K1ijJ_ma1-9LfA3loOnlQIZpUYgWvO_L4AKTbrDRJd0r13x-id8XJZdekpCJIfUJHio0lNU14oEDavAl1Nn5WPHJ4FOPRdqrfg4RPUhOJShRBqUvG48q54jotHyziedQIdpCBxNzjcYMnK9XuIe6I-cIPDRLCnAcEROgowwoEXlFsuQVqlSZdN8JJEEwmVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور پررنگ بتمن در تجمع اعتراضی دانش‌ آموزان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75669" target="_blank">📅 17:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آخرین باری که اتابکی گفت میزنن ۸ روز بعدش زدن امیدوار شو ایرانی   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/75668" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75667" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک مقام ایرانی به الجزیره:
ما به یک تفاهم‌نامه با میانجی پاکستانی دست یافته‌ایم و در انتظار پاسخ آمریکایی‌ها هستیم.
تفاهم‌نامه شامل پایان جنگ، رفع محاصره، باز کردن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود زیرا این مسائل پیچیده‌اند و نیاز به زمان کافی برای مذاکره دارند.
پس از ۳۰ روز از امضای تفاهم‌نامه، ممکن است درِ مذاکرات هسته‌ای باز شود.
قرار بود رئیس ارتش پاکستان [عاصم منیر] تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی به واشنگتن رفت.
برای ایران امکان دادن امتیازات بیشتر از آنچه در تفاهم‌نامه آمده، وجود ندارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/75666" target="_blank">📅 17:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا: آمریکای خاورمیانه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/75665" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUIIsVN5Qemijzoj7T8Ynm84x0W4dLalBALcTezTMHCGxT5SaNgpnahJXlfJusoRqy9tI9uGlQ5F0r31mKVNpJjnD4DjWePWRbGxjaZWCxY8w1NU_J-zBGskMyrRIHzOi4pbiYEUxXqtrenJiApQdBotDYEJu7C4FxBfOjJ_DgfYgluY9-sf6QZ9Xoac1QzFU6vbHoxv43IE6o9aLBx43rSE8YLeJFl0xBxBH3VlyjvrQT4iX_E4GrSO589wFjqVl9ha3Ov71gSQAeVmqpZhRNG1EUlmDs4U8MaAA26YqhgarHJd20DuTAbaLkMX5U8XC433OCDQZbVFbGA1F3ixvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا:
آمریکای خاورمیانه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75664" target="_blank">📅 16:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b026396695.mp4?token=OuhzMt3aR1MOMEK7B-FzkkN0mcouy52N0leXu9V_cIBvriG5_6WSeWzp_nH4d5tiZBpDqN20B3JRyEpqybVfyLJpOQ3p56G6kmB2Ru-LJAvt71BO_eg5O6SQIEsDHhZxKXE24UZDqalz5XH54kk_EPH-sbm65i1WrbWxGVzhyyX4JuCBJ2eLZy_K5R398kiuPNG9n3-7cA79wNaIKQq-RSayM5PPBlgbQqH4_0eOrskRtxDBF6VNmPpH4exRRP0m4cG2lZcljPTVbXXXurePWuLlVKJ3HHQWurxy_0IY72aT7XRSCYS9a8lMxdxtcRWKulAbLnO5gpAo5uX6Gggxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b026396695.mp4?token=OuhzMt3aR1MOMEK7B-FzkkN0mcouy52N0leXu9V_cIBvriG5_6WSeWzp_nH4d5tiZBpDqN20B3JRyEpqybVfyLJpOQ3p56G6kmB2Ru-LJAvt71BO_eg5O6SQIEsDHhZxKXE24UZDqalz5XH54kk_EPH-sbm65i1WrbWxGVzhyyX4JuCBJ2eLZy_K5R398kiuPNG9n3-7cA79wNaIKQq-RSayM5PPBlgbQqH4_0eOrskRtxDBF6VNmPpH4exRRP0m4cG2lZcljPTVbXXXurePWuLlVKJ3HHQWurxy_0IY72aT7XRSCYS9a8lMxdxtcRWKulAbLnO5gpAo5uX6Gggxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/75663" target="_blank">📅 16:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/75662" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیدار عاصم منیر با پزشکیبان و قالیباف در تهران   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/75661" target="_blank">📅 16:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiAOA_Ejwfk0NCsIjKgpzRbFcgr_gDE1-ju8Sgdyx07XHQ1ViZNl9rZk6g3RYxnFWW96Jw2g54XPkThJ2MJZaqt7_FUHePoCDEPj8bFSC-i3opwvfiKT06OEAOvfZHNldzpbEFsC9NvRYpKn7kxAZBtYaf9okobDJzeHMdeYaIpoqhCvRlmWvKRdEAZp1UmZTkkVfympzlZKvsa94wG2oPIGMhQ0B32gqryko56wUCazYVNdvU7ioYHuBKnkJ8VimVJqMqzbLel0cmvYIIUddJGfYYSZrAdFTRDmeDe7kwBu8UQg1pmEgf-wCJ2XUexw1rhru7J65y2nN9qY6EdIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا واقعا</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/75660" target="_blank">📅 15:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=SGzdqc7_O1wlo3qQR3c4gR8mEfBzQHuu5bJYEC2GQaACjpuByxPhQI1cceOmLebxl_e8PwuOKr2hkL-zPFts4wX6-ZR-cluu-uFxa1GqvbkQasaLeEmNeX9ks9_3mbDBDieP8BcDbBmts_9Of1g1UhIxqKzTYAHk7H3e-nB0hSk2A_XEV804aEFoYvUtAHg5U-P_B8kHR8WESbsoXiqyvz5wZSLGVgvFfqlzvnt08S3uFPggilu33B-IeAm-kNbKULnRLLEF_ggO0w4tF3WAFc0OOXkbDG-a3xzP_pIOFwDCxSNvPXlbX2IXcX9kT1or3pCiA-c7_syP7rq_q53tDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=SGzdqc7_O1wlo3qQR3c4gR8mEfBzQHuu5bJYEC2GQaACjpuByxPhQI1cceOmLebxl_e8PwuOKr2hkL-zPFts4wX6-ZR-cluu-uFxa1GqvbkQasaLeEmNeX9ks9_3mbDBDieP8BcDbBmts_9Of1g1UhIxqKzTYAHk7H3e-nB0hSk2A_XEV804aEFoYvUtAHg5U-P_B8kHR8WESbsoXiqyvz5wZSLGVgvFfqlzvnt08S3uFPggilu33B-IeAm-kNbKULnRLLEF_ggO0w4tF3WAFc0OOXkbDG-a3xzP_pIOFwDCxSNvPXlbX2IXcX9kT1or3pCiA-c7_syP7rq_q53tDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ توی توییتر که با هوش مصنوعی یه مجری که مخالفش هستو میندازه توی سطل آشغال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75659" target="_blank">📅 14:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تنها کلاینتی که تیم فان هیپ هاپ با بیش از ۷ سال فعالیت از لحاظ امنیت تأیید می‌کنه، کلاینت فاطمیون هست. به صورت رسمی از گارد جاویدان  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75657" target="_blank">📅 14:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این همه پست زدم شرایط رو محیا کردم برا تبلیغ کانفیگ
ولی مهدی تبلیغی نزد
رسانه ی مردمی رو بشناسید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75656" target="_blank">📅 14:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etM6_8Ud1woBhEUH33gZeQBy5rl9WsDVgUvIG-Yoc5UP5bIjRNk-9EFj_ryzKnYRiujAgPuRZHtCAv-8SS23UcF7P-OVgL76L09gohcE0HYfy90h-e8-0aWkrHTtMfJKPwtFSjxPbm1ZnHh2WQw05FGAf-VAlQYGZvLK25465UN92bnVh2RG8Yqz-LfwY6lmHG5RyU9mpjwU4tzv6EG8hZBFtGDwzMDXXUk_dG7Z6ab8m2xp-JdbBnDNCKeA293MFWsC-oCqZ2l4t9xsdt3p1jcesxwudQwklui32XGESe5KPCqmN-2LdttkryLqMIP5BRkBnKLnvHIosGaACmGg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کلاینتی که تیم فان هیپ هاپ با بیش از ۷ سال فعالیت از لحاظ امنیت تأیید می‌کنه، کلاینت فاطمیون هست.
به صورت رسمی از گارد جاویدان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75655" target="_blank">📅 14:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوستان این بحثا برا کساییه که اطلاعات مهمی رو گوشیشون هست و آدم مهمین، شما به کیر هیچکس نیستید به راحتی میتونید از شیر و خورشید استفاده کنید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/75653" target="_blank">📅 14:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این اکانت داشت تبلیغ کلاینت شیر و خورشید رو میکرد  صرف نظر از حرفایی که قبلاً از شیر و خورشید زدیم، خواستم در جریان بزارمتون.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/75651" target="_blank">📅 14:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui7PqB2ALqg-26SqCI08yp-ZW8hN69O4Zpy97WH_GCiBvdw5dCyWM-oJhGz4LkFcwDg_sbpWdBhvrTKShKtkaf6_B8j08XUIOI0dHu1s7bjzAAvK08nTwlR-mAKFG7yqS-5pzaof0l9uCB5mPZoJWrVXtUOLIn7BX5l5AwRupRUTIOYTrPoUQjNJ6LupW3JF-yXoIxvTpmJ2-CO2TfaM0wOQQtmVDa1vHCTioix1PkALVg1GhYLrm__QJ1SELlEjfpuRXrtLiO7VwUz4kkyfTBfOjbN0JWy8NjRqKT0omwbZ_5A3winuwleNrmtsoSFW45sapufqoqJ5Ba64QBvFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اکانت داشت تبلیغ کلاینت شیر و خورشید رو میکرد
صرف نظر از حرفایی که قبلاً از شیر و خورشید زدیم، خواستم در جریان بزارمتون.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75650" target="_blank">📅 14:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دیدار عاصم منیر با پزشکیبان و قالیباف در تهران   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/75648" target="_blank">📅 14:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75644">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7fzHfLFrF5QpN2mBLgJ1S3k9pAXnEE1xGz4s9sYtWsDjfYsfgm5aFrX55R8EEKbRBJy0gdLMzbGIhiL8-zht8Ka16YiaZ6soikxSO-YAYqHOGXX5H6Sgi7a2untiUM8hD2ZuZCEguznLZpkz9Zyavu5l-KJe955l4SesbNirKFNCpMATsg6Tv5zgwS18YAuEM1XU7YcHLpuF9LsRW5M_r3g1I-w1IrELquksh6rt_FtfHriJaC70UVVQp3RKZy0_MidOLPRsYGgWhyYqI6LZtjrY3RPVSgVJ2uIl5VbzfouWe98P_csJI6C2apGUwj44eLIkjbGgo-L6qB6AXVD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krIyaHp_ZX_3ZsnOlU8MUGzRl8OBhP2oT9kvx3d2jpdnFwqH4Nvffie7h_-mN0-MgRNMTZvYez-ZwINlyGXkIVZ4xNbUjK4Iuzy6LRzQbre-E4aOeAlheHOT0mnJf9ljujOpomTMFmVmZxg1H0RhRxp5w-0QkhQrozUWczQ8UEmlJDkAMDCjvkYCFpGS79cYDF2FJzz0aim2hC95Vfji3kAWPRzIBPeUMkwsnCX4yEGWl9dX3mLfxN6zlFhT2yIGlBp7i4HQS_dSX-JU47iYdZQsEopTqWT9lRpUzry2653fahtwDwqibzl-G_BlOaf5HPxitGpjZcFRpaJxG1rhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUmfYEZHSuD4IrGC3zvFkTap9yxlUUpYJ2Egy6zL1mDgku5Bv8Oq_QbCaWpymOUc054pUU3IMbh1ph00PYJwAl0iKH5eb7J2tq6d4ZmizIT2m-O9ezQkx0l0ykcW7UXM2pDygULreV48WdZpsTekIgcpHtuqsTgWBS6AOi3j1SEwAEQ6yAeWQAJq6KBQaUgLCDrFdIUhuDntzCS1bvFBweeFR2a1NyR3QExexaYMn-TzoxVCWYDzn7VzXXnIUe7z4MAiuOr_4YS9q6CtaTSn3sx91zUr7JVbY4r4SVOkUSOoAxoGKai9gKj3OqbfOEq6OQ79BhPJWvIcwnNmpu8ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsjwgcDB7twa19NkpeV0gVKRR3vrDAhOeMS54uIdIZyoQWdzudgDjq6XIb3U_gIGkNdVShgbd4rBylHphqzNk7wqW-xfjDd7SPXJQxZsFzrU3TEQPCLWpCPm9uJicrDIdQR7jAgkzan7q--XX9xNn1I1qGRqjcM5FK54C4LH47u2zhJIfg-WGHxNsaD0_oeDWHw8oZxl5JBQOOYPN2MRNeL6xczJo7X71-BOrbvK8CV8JQG_aWI9CZW9XNVV4SDTE5Cy-hGfooX-h-7LbZHwsMlOtP30QlNYFOMCs-TfLYcBnVqtv2RAGRi5FlISnvzBfqZ_vG-ReneXt_ZsblTmDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبر سفر عاصم منیر به ایران تکذیب شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75644" target="_blank">📅 14:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75643">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">العربیه بمب دراپ کرد:  کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند. ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/75643" target="_blank">📅 13:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75642">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6s-xr70H2NywA-1b4xhx4q_EU7c3sygzBz6-yYzlae5fzNnSc0ZlxnpniZDy2qmFTBXDSyQdfXbKETakOZJmWtTjNymK0JgAqDwMxw0mHd0g-g14O-OuTLm-S_9IoyYXRmS7wD1LfNsGcyNFYwAK0FyoC-93WooznHuMuKfpPVxF40Vyyzw8eZfcMBIXJN0P9iY2EGr-i93nsT5F1ba-bXnX5YrkvPofUw-tNw2wk20C6ArsV7QBHiwlu2eColC41FypDehsP4G991Dz8QX81ucTQayFHW8eP6FtsZ-XkkeMGXV4nKtpqz0nNXzv0o5MsdaqHPoYTjeAzeu9e6yKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف از خود نباشه ولی من تو چنین اقلیمی هنوز خودکشی نکردم. 4  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/75642" target="_blank">📅 13:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_lJsCOHiwfAbQKc07A0S9Y3PDAaV3KMQSBOVlkZQg61z5HVPSBWB8ginoxvB2NJHnK6rseMdGFLDEa5vGv-2GYfzT6BslnYCyzcLC8pCtyY9eZsklLpM7FcqvBE5qd7j0eRKsX7QI8cevKuJmWXlmvkZNqqSWee1neFX8hEnMgGBif05kxu5c9Hi6VMZ2SVUliV_cBzYrd2-VI5CRdi2T2uF-8cmpEgIIvNu6mtPfFsSeZmJPVvv3mQ5vDsDPtR16Vpewvm3VDfYJr9IhtE3SPUGHoypH7gmfF6Ynk1pJXgU_y47b6aDK_d9iSJ0KHPisBW0IsveqjvgwwV4xnffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد بی ادبید
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75640" target="_blank">📅 12:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/75639" target="_blank">📅 12:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9YIv7tyqPkeHioGT4bmXglaepyLuu8NOJOX6_FWReo-RdKU4bYLjLGCPc5lts6UEJDP1mTQHNhEMbsvZ5PeiWc1arAmU0H8FGj_tNWG1leLKAHwNI7p-NZ8S7gykMrHF-Swn6ta8fmZtby7ry99zGn6wV5qtl2jvjfgTFAkFsTSUGf42pr4w-M1_tH3kFmDuip0wXcfTj2H6NRavOLjPm7iF190xYp1v4SiaOBFMuP8s1LxMzmHijUWU4uUz32oGjWowgLLXSAWoq4WcLibKQwnzQVemUiR0gwDmdvehCLNrKkvnjtt_gRoFuxdaox48jTvzR47-70GbAUA_pwe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت
گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی: 5GB | 950T
10GB | 1800T
20GB | 3500T
50GB | 7500T
100GB | 13,000T
📩
خرید و پشتیبانی:
@VeloraSupports</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/75638" target="_blank">📅 12:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thV3jmHZruesh2hHAmxNY-xVUIMwl1ayjYwfYrc9baba8UAaai9w1S-RHQlVqmoy0L-nIvoOCc0tkkWwRzld-ZJs710U7Y4MKOsEJyGnODCPbmcildKNm1ElFAK09_yrjGqzsZS37XMJZctdi0pGcOTK072_9IkzgI6bmxwQ8TJ931loJtIEg_b1dS_O6DoUZvvijQGzOzWq9m_5CVkotoskPtPvhXdd4Fu6f1vSU5b371T93qGxzvUuM9wEVSQdq0TSfRQSBC7Kx56lk3scK1xOa1kpjbzKmRFcQ60j3O9EOfZVHyIdSFbZrek1jYYOyxMK2Ah9D4HL83oERRTpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز اکانت اتاق جنگ اسرائیل دلقک بازیش گل کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/75636" target="_blank">📅 12:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش رویترز از شکست استراتژیک ترامپ:
سه ماه پس از جنگی که قرار بود در شش هفته با پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر کرده است و قادر به یافتن راه خروجی حفظ آبرو یا گسترش حملات نیست.
با وجود حملات نظامی آمریکا، ایران فرو نپاشیده است؛ کنترل مداوم آن بر تنگه هرمز — که یک پنجم نفت جهان از آن عبور می‌کند — همچنان اهرم اصلی آن است.
تحلیلگران می‌گویند رئیس‌جمهوری که به پیروزی‌های خود می‌بالد اکنون با چالشی روبرو است که می‌تواند جایگاه جهانی آمریکا را بیشتر از هر درگیری در دهه‌های اخیر تضعیف کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/75635" target="_blank">📅 12:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سازمان هواپیمایی کشوری با صدور نوتام جدید، محدودیت پروازها و فعالیت فرودگاه‌های غرب کشور را تا صبح دوشنبه اعلام کرد.  @Funhiphop | ALI</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/75633" target="_blank">📅 12:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALKZN3g1fUNRgDHIqOYCV047uW_YZGE_4s86wqE_tYb0Hk-ViCkhzzijLlA0TKEtm81y1Qll4JkMc43E5ngU7_mVNNW0hWcr3PuXS3SuKyEKJ-WRMzYZaELCwN6tjU75iZyd7rDKRbinHt4fLkeMvuOxRaTVOJ5z4qeYSmAmT5Od7VN3FWgYbbJjnOwqJ1F4S9OtGLsPBKGXF85vV6Cpa5bVrkzfBDx3zCu8_KP8lpyn6dO-mRXWbytIGbHaTxzXijPhp9KE01CDBJYKm7LGaf_mNukg8dgryk9iXMLJi3u6-OfY3tX9DUaisscz19nJEjFdKZdWK9dqhbAAEt9W8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو سیناب ازت میخواد که همین الان سهم ناهارتو بهش ببخشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/75632" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asSmDEJQUc4QPft1fOpvDJ2pUAW5_S19yQML6KK3LgD9i46mg0jjHdRp8QaUp0k7gL-Bd0lGQm0ro8hi5xsZqH5hM6xlfhFyfGBbu8a7Q-13XZIDA7_A9uNr3ZUsb52JaEMzRhptuBESZ9MaJDukAtX7dwhGWsHWcei047LoDUCSx4vMhl7L3agyfQgL3wj0K5gv1TK-mkXM4vebdfuswupkv25NzTwrLfKmgvxcy5O3VS1WrFoSpuW9wiFOmGlfHHPgpsFaswpJAS5oklH4AMqYzw5ofqk6XCvkhvS-xAJ6mJGRzXGGM-MUixhtz0GkJ0990pSL16cN_rer2XzwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه در جهان یکیست</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/75627" target="_blank">📅 11:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بخت و اقبالتو گاییدم پسر  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/75626" target="_blank">📅 11:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2XG5FyZyT-wBbpXa2mZ-3kHFb-VPIybUT4-nRlpRp8OGGbIQTtRJDRhzF0emMoBOqPEUuHSg6Px3ltJrHwvEucwjIu_iZOlvacoXgB1T_OVWyfkx_OtW5OAHURM2EAaTll7zxiCl2yWBmobyButUPtGP8_LnhXwETdh_0Tbcn7dgjjXA-f09CWarKRJKDqSmEekGtwAZ-TKCLF1bM36EFfNZRCM47bfh0GX8wOiloeF9Z_KVo0xgvq6q3UODEBXloaNTXvC3iOygWXABrcPEfEs4zZ5lMcFAd4r4CbNT4ZTbbGu27og3SLsHzesnrdYEi9KW-SfeemhcVFVV_ssNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخت و اقبالتو گاییدم پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/funhiphop/75625" target="_blank">📅 11:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">غیررسمی: آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی رو رد کرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75624" target="_blank">📅 10:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">غیررسمی: آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی رو رد کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/75623" target="_blank">📅 10:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سازمان هواپیمایی کشوری با صدور نوتام جدید، محدودیت پروازها و فعالیت فرودگاه‌های غرب کشور را تا صبح دوشنبه اعلام کرد.
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/75622" target="_blank">📅 10:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الان رئیس صدا سیما داره فک میکنه چطوری جنگنده وارد استودیو بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/funhiphop/75621" target="_blank">📅 10:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoEa09Kdmma6aKfGfgzAinfWKiPl5i0VW9P0kljitvRuwZ7zG5pakHanTGlwPhJG-5zfl9CVVagyr72XguQ_Xwp2SL6WlX04EzidrkBg2GmS_0auWq9Zvx6dPd3D_KTD5gWUpudCZDEHfE-CC7sn7-TTTXKFaqawtEMg4i5gv9tlBRjLDRGZsaYGUgQ51zugdiaUw_60UGWFA35VVvoLykf6TnugRi1cgHpsCpT72NGfm0k4jsZvA2tIOn-Ba3KYm6hxkRIYuqQEHrMxyxGwky5NwOiy5aVDhF832AILnPl4qbtdSmi84DlFG6yVesNBnAw8BMdaqPQveyGVix6_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف از خود نباشه تو چنین کشوری هنوز روانی نشدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/funhiphop/75620" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBcSXNHx9Lwn59PINTtT1Drtb42Ex8julhnYXUEYv2XGk_AD0RLPW8bnFL3QSQkNAxZ342qzFyF7LCmgcaC4F2yLx9BPWCt55vmEPL-UUDrTyGFIUtBIumfVRm803XAKhANlb9229aIStWEcoOsI7u8--RjZMkA7tUCBP7UcQr2l-pfxI90rU6FHjqu3Fi_ZTdglG9k2lDD_Zc0kZLejT0caJ4S7N-mPbZWYwNZgcOh6NTDt2CMXD79M081pnN0jvHvzz-upp0-g1sAtwpf6Z_UN6aRupz-M_cAWbhz3Z_yAeLj9qx93ZuLgmo3t2PvMqxg_5EONGbxIGONE2RIX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه مادری از این دراز بد قواره‌ گاییده شد</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/funhiphop/75619" target="_blank">📅 10:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTuCauov5RP-sk33I21Fz8AYqrCiG2aQTxI8_xE2UU_qwo4CxYvOyMa94l1wp2eOk6ZRVGAmYGDj-iidujBTqzioHTpM__qyy7LWnRmc1r97tVnHgrnMp2IMpv2lV8fO1-F0GJwmHtmMNo8Ko6j3Np61uAidJgoEf9t0Pc5iCdz-fe9KfGJMPER48zBZQeyJdoZBmMsD56SYCqWwQ6V7bETsVoqHuTf6CHuOez6m2jbtKwaT1P5qRdSgaqqjTkKbjlC_WpE8bsJAUwEKJfbWvT0aSr2by_o6NzVz6ePB2LtxserNrP0OePUAmR4s-Y47_7hFgeiUGI1mxoGvd2wcHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/75618" target="_blank">📅 10:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی وزارت دفاع و پشتیبانی نیروهای مسلح، سردار طلایی‌نیک:
ترامپ چاره‌ای جز پذیرش خواسته‌های مردم ایران و احترام به حقوق کشور ما ندارد.
عدم احترام حقوق ایران منجر به شکست‌های بیشتر برای ترامپ خواهد شد.
در میدان نبرد و دیپلماسی به یک اندازه، برآورده کردن خواسته‌های مردم ایران تنها راه خروج از جنگ سوم تحمیلی بر دشمن آمریکایی صهیونیستی است.
همچنین ترامپ باید با پذیرش پیشنهاد ایرانی، مراقب جلوگیری از خسارات و هزینه‌های بیشتر ناشی از ادامه جنگ باشد، چه برای مردم آمریکا و چه برای جامعه بین‌المللی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75615" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75612">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb842b6ea.mp4?token=i9cFuAtWsDFNnc0-aEE2aIyJ1joIJVCKl0MCWAwonSxwpDJ08CxqybIUNuZLay1_DVBZ31MR2psyXqWNU6GKYSqFxBeXbU0fpRqwxwrt5K8ecPMvY7RRkRHS9CcMeGxVxy9viyCnKtbJmTCKdPLxfuLzpSpDjJo6BuIUcjFT1ybxbH3uW2ehnVO398rtpYHrA7Z2Abud6r6xMcW6YnjCkMHNv959rFCeMMj2xfS32acpX-UcJdCsGnsf8XC8niFJicJT3CoiB-HlulRD5kSjrXZAcXHu69nPhCLBgvmQTO9ft4qNDNJ5qDoJELS19yS2nyLNTOvkfojgK2gSmrSpCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb842b6ea.mp4?token=i9cFuAtWsDFNnc0-aEE2aIyJ1joIJVCKl0MCWAwonSxwpDJ08CxqybIUNuZLay1_DVBZ31MR2psyXqWNU6GKYSqFxBeXbU0fpRqwxwrt5K8ecPMvY7RRkRHS9CcMeGxVxy9viyCnKtbJmTCKdPLxfuLzpSpDjJo6BuIUcjFT1ybxbH3uW2ehnVO398rtpYHrA7Z2Abud6r6xMcW6YnjCkMHNv959rFCeMMj2xfS32acpX-UcJdCsGnsf8XC8niFJicJT3CoiB-HlulRD5kSjrXZAcXHu69nPhCLBgvmQTO9ft4qNDNJ5qDoJELS19yS2nyLNTOvkfojgK2gSmrSpCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دن اسکاوینو، رئیس دفتر کاخ سفید و مشاور قدیمی ترامپ، یه ویدیو از B-2 منتشر کرده.
آخرین باری که اینکار رو کرده بود (ویدیوی دومی) یک روز قبل از حمله‌ی ۹ اسفند بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/75612" target="_blank">📅 05:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75611">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کسکشا نکنه زمینی میخوان حمله بکنن
تا این لحظه، هیچ جنگنده اسرائیلی امشب بر فراز سوریه یا عراق پرواز نکرده است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/75611" target="_blank">📅 05:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75610">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=BobXJx2phy9fZOcvXN8A-241Qfj4XkksG9Ftam4ISyYGaxjESuThZ6phQ9xF4uKKU6B-BAzbjIeNfQ2Jb5NI2_DiUZnbiysreUsTDDQzfUpTl7s-x6FgdmYqOy_PSPRKK8dre8FSZrnf0I1lLNLvJoUNVaf2hlThFan6AzdFbuxf_8mOGp-nyKB7ZLQwsX9_EWf_nEl0j82EFwZIWz5L1XR7-NDs_fyz1H5yq_C17gyStixdLePRK8H5vhFNThiCRyyp4hBUFM_JPwW0GiCq9VWmr5MSacDoPoRNRL4IVAqEa09WCIVQ8bhOG2iSdDcH4hZlQav3yOcMk65JdtGp1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=BobXJx2phy9fZOcvXN8A-241Qfj4XkksG9Ftam4ISyYGaxjESuThZ6phQ9xF4uKKU6B-BAzbjIeNfQ2Jb5NI2_DiUZnbiysreUsTDDQzfUpTl7s-x6FgdmYqOy_PSPRKK8dre8FSZrnf0I1lLNLvJoUNVaf2hlThFan6AzdFbuxf_8mOGp-nyKB7ZLQwsX9_EWf_nEl0j82EFwZIWz5L1XR7-NDs_fyz1H5yq_C17gyStixdLePRK8H5vhFNThiCRyyp4hBUFM_JPwW0GiCq9VWmr5MSacDoPoRNRL4IVAqEa09WCIVQ8bhOG2iSdDcH4hZlQav3yOcMk65JdtGp1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت قطری ایرانو ترک کرده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75610" target="_blank">📅 05:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75609">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هیئت قطری ایرانو ترک کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75609" target="_blank">📅 05:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bd9ce2b9.mp4?token=rz_WNRy1rdFDOwYbvhZcjPFmDSZOqmtGe49uBfjJV_xw80fnTGE-aJtfHj7lmpAmL9Ut7sEvKGFv2Y7jm4Uo1-PbA1Z1SOLLHIpYgopoNyE3JBVPaJrWHiDvZ8VkAj2t4Kkm5idTrwCtLTmY_W9oDlZcsRmGvpZD_pEw7KJYH06lu-74j99ln2mDqEe_ezEYs6xIBr05ExijoBHNveTFQtqxg2lHFpRsHDqFmkjbQgxlEIaLHfwp0oLbYEOlxN22kPy4O_rWf4VNE0Yd7UIw9wRLebOH5CPdiyQeTDsx8T2ZO0cBBSFSHqcfPoWIqWw3VqvFCVf5PfhPXn0D7M7SMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bd9ce2b9.mp4?token=rz_WNRy1rdFDOwYbvhZcjPFmDSZOqmtGe49uBfjJV_xw80fnTGE-aJtfHj7lmpAmL9Ut7sEvKGFv2Y7jm4Uo1-PbA1Z1SOLLHIpYgopoNyE3JBVPaJrWHiDvZ8VkAj2t4Kkm5idTrwCtLTmY_W9oDlZcsRmGvpZD_pEw7KJYH06lu-74j99ln2mDqEe_ezEYs6xIBr05ExijoBHNveTFQtqxg2lHFpRsHDqFmkjbQgxlEIaLHfwp0oLbYEOlxN22kPy4O_rWf4VNE0Yd7UIw9wRLebOH5CPdiyQeTDsx8T2ZO0cBBSFSHqcfPoWIqWw3VqvFCVf5PfhPXn0D7M7SMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/75606" target="_blank">📅 04:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W92D_V8GMCXI5ltPMjlC8zsLk6WuGprk5wTbu_d0QVSOCsX9-FY7elZ49EZv1FWXOFYMgW1hqWKx5VMn6d9UKx6Hwzb2jLhIJnp7yPxXQKABX3iWSVKc2DZptRT6G6dSxT40dC0Kwe-wRUPm64r-R0XvoRXxG6TQYNAltuyYGvqiKr8NjCEO_wKyxVLEFNXd1NzKh4X9X2CMD2M4Z3CS4NqMtllQ30vyVjUe-0yJQ16a635ESuwXLtR8DkY9pLTcl0exeAsYjAn2nD-jjiazqCZ_XbYWtKQRyrBH3PLBc7WAjzp2HrGALZjgvcucw9pkIMyNoVuz5k3rPyA5VYcvKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست:
ایوانکا ترامپ، دختر ترامپ هدف ترور توسط یک تروریست آموزش‌دیده در سپاه پاسداران انقلاب اسلامی قرار گرفته است، در یک نقشه پیچیده برای انتقام‌گیری از ترامپ به خاطر حذف قاسم سلیمانی.
محمد باقر سعد داوود السعدی، که یک هفته پیش دستگیر شده، قسم خورده بود که ایوانکا را بکشد و حتی نقشه خانه‌اش در فلوریدا را به همراه داشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/funhiphop/75605" target="_blank">📅 04:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سی‌بی‌اس: دولت ترامپ برای دور جدیدی از  حملات علیه ایران اماده شده
چندین عضو ارتش و جامعه اطلاعاتی ایالات متحده برنامه های روز یادبود خود را به دلیل حملات احتمالی لغو کرده اند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/75604" target="_blank">📅 02:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسپویل:
این هفته هم نمیزنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/funhiphop/75603" target="_blank">📅 01:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیوزسیتی پرو:
حریم هوایی بخشی از غرب کشور تا روز دوشنبه بسته شد.
نوتامی که صادر شده یک استثنا داره که اون هم پرواز هواپیماهای روزانه تو روز هست. شب و ممنوع اعلام کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/funhiphop/75602" target="_blank">📅 01:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آخرشم نفهمیدیم لین کُس چجور سیستم عاملیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/75600" target="_blank">📅 01:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اکسیوس یه سر خط خبری دادی، یه جاش گفت مذاکره در حال پیشرفته یجاش گفت قراره جنگ بشه یجاش گفت نشانه هایی برای از سر گرفته شدن جنگ وجود نداره، به راستی که منطقیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/75599" target="_blank">📅 01:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خداوکیلی مهدکودک سر خیابون ما وضعیتش از اپوزوسیونای ایرانی بهتره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/75598" target="_blank">📅 01:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERmDm_ZoZnZZYDWfO2nEPiF0D98OhaeDKotD2COWeNlI8OWK8UTCkgIK9uQN09Yv8PnwxbqD4ObT2eAsEPf8iznlRc-ou-QJklhwiRBUkjfH55R6dd-ju-OIFjB-d7DIHhqE7fAveuD8sAKE5FjbQWp9UPYC0as5yDeV6C3HipT60DzXPxTixTs94YVcJRggqWkAfW5eEE7YPITp5Ai85qAqeTXAnJJvsRzFT0T7bJjM_k6xnpOyy2u6GV9xZ33K0NccPTNhv0MYSt732sb4h-cdjRC8aIPv4B3X-AZ-oSYL5ZDJdGGT92p6OxiLFqZ9ouJQmWbe27IlRjYnQKPKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/75596" target="_blank">📅 23:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDwEufjPWn8pFR8icIYRd1_HcAvcRy2VFGRSaOmEzMuHrogL-NMXFy69U4KZZxL6EhF6jv0hRjrex8tH8l7uh8IOUNiG0HDRbTLvN0ViYG3KCNrE7Dz-qA4Q0wzPuRwOgdKNmIn7189jC4n2V4SjPmXtYPJ9qNbZ_s6zMIRdmugTe98YG-eiikH6b7-STIIh3vsSLxGoIiCfCtGCABkh5182XI8hV7JmmJPy-93UHGgmIqYJyTM9uoVhd-dR8z-MQGaZ7du5Hm7dNdsCvhJ81r1BqRGXaFMRE_wNKuTBix0Mu2QSzx5sbQiZUtSaHhG8cn9cglmvzaun1UQ1pysB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط به بنده خدا رضا پهلوی چیکار داشت این
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/75593" target="_blank">📅 23:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یادمه پیشرو پست زده بود تو چنلش:
این آخرین نبرده بعد بقیشو خالی گذاشته بود
بعد دید فدایی از شیر و خورشید و پهلوی حمایت کرد
ادیتش زد نوشت پهلوی بر میگرده
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/funhiphop/75592" target="_blank">📅 23:36 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
